local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"
local comdb = require "luci.controller.lib.comdb"
local vlandb = require "luci.controller.lib.vlandb"

module("luci.controller.api.vlan", package.seeall)

function index()
    entry({"api", "vlan"}, alias("api", "vlan", "conf"), nil).hidden = true
    entry({"api", "vlan", "conf"}, call("handle_config"), nil).leaf = true
    entry({"api", "vlan", "trunk"}, call("handle_trunk"), nil).leaf = true
    entry({"api", "vlan", "info"}, call("handle_info"), nil).leaf = true
end

function modetrans(val)
    local data = {}
    data["Access"] = "1"
    data["Hybrid"] = "2"
    data["Trunk"] = "3"
    data["1"] = "Access"
    data["2"] = "Hybrid"
    data["3"] = "Trunk"
    return data[tostring(val)]
end

function portMap(filtertype)
    local portmap = {}
    local porttbl = mydb.getporttable(filtertype)
    for _,v in ipairs(porttbl) do
        portmap[v['Index']] = v['Name']
        portmap[v['Name']] = v['Index']
    end
    return portmap
end

function vlan_statetrans(val)
    local data = {}
    data["Invalid"] = "0"
    data["Disabled"] = "1"
    data["Active"] = "2"
    data["0"] = "Invalid"
    data["1"] = "Disabled"
    data["2"] = "Active"
    data[""] = ""
    return data[val]
end

function getvlantable(id, step)
    local step = tonumber(step) or 20
    vlantable = {}
    result = "0"
    str = "&" .. (id or "")
    while (result == "0" and step > 0) do
        str = librpc.callapi("oltmib_vlaninfo_getn_1", str)
        _, _, mytype, vid, name, state, tagmbr, untagmbr, msg, oper, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["Index"] = vid
            row["Name"] = name
            row["type"] = tonumber(mytype)
            row["tagmbr"] = tagmbr
            row["untagmbr"] = untagmbr
            row["State"] = vlan_statetrans(state)
            table.insert(vlantable, row)-- add it in order for ipairs
            step = step - 1;
        end
    end
    return vlantable
end

function setvlanbitmap(data)
    assert(type(data) == "table" and type(data["vlans"]) == "table", "vlan is error")

    local tagmbr = table.concat(data["tagmbr"] or {}, ",")
    local untagmbr = table.concat(data["untagmbr"] or {}, ",")
    local step = 256
    local cir = (#data["vlans"] % step == 0) and (#data["vlans"] / step) or ((#data["vlans"] - #data["vlans"] % step) / step + 1)

    local loop, vid, vlanbitmap
    for i = 1, cir, 1 do
        local vlantbl = {}
        loop = ((i == cir) and (#data["vlans"] % step ~= 0)) and (#data["vlans"] % step) or step
        for j = 1, loop, 1 do
            vid = data["vlans"][(i - 1) * step + j]
            vlantbl[(vid - vid % 6) / 6 + 1] = (vlantbl[(vid - vid % 6) / 6 + 1] or 0x40) + bit.lshift(1, vid % 6)
        end

        vlanbitmap = ""
        for i = 1, 683, 1 do
            vlanbitmap = vlanbitmap .. string.char(vlantbl[i] or 0x40)
        end

        str = "5&" .. vlanbitmap .. "&" .. tagmbr .. "&" .. untagmbr .. "&&" .. (data["oper"] or "")
        if librpc.callapi("oltmib_vlanbitmapinfo_set_1", str) ~= "0" then
            return false
        end
    end

    return true
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv('REQUEST_METHOD') == 'POST' then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")

        local data = {}
        if params['delete'] == true then
            assert(type(params['vlans']) == "table", "vlans is error")
            data["oper"] = 2
            data["vlans"] = params['vlans']
            if not setvlanbitmap(data) then
                return luci.http.write_json({hdr = {code = 100, message = "Failed to delete VLANs", type = "fail"}})
            end
            for _, vid in ipairs(params['vlans']) do
                if vid == 1 then
                    return luci.http.write_json({hdr = {code = 100, message = "Default VLAN cannot be deleted", type = "fail"}})
                end
            end
            return luci.http.write_json({hdr = {code = 0, message = "delete complete", type = "success"}})
        else
            local portsgrp = params['ports']
            local info = params['info']
            local tagmbr = params['taggedMember'] or {}
            local untagmbr = params['untaggedMember'] or {}
            local vlantbl = vlandb.vlanstr2tbl(info['id'])

            if #vlantbl > 1 then
                data["vlans"] = vlantbl
                data["tagmbr"] = tagmbr
                data["untagmbr"] = untagmbr
                if not setvlanbitmap(data) then
                    return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                end
            else
                if info['name'] and string.match(info['name'], " ") then
                    return luci.http.write_json({hdr = {code = 1000, message = "VLAN names do not support spaces!", type = "fail"}})
                end

                data['Index'] = vlandb.vlanarray2str(vlantbl)
                data['tagmbr'] = tagmbr
                data['untagmbr'] = untagmbr
                data['name'] = info['name']
                if not mydb.setvlan(data) then
                    return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                end
            end

            return luci.http.write_json({hdr = {code = 0, message = "edit complete", type = "success"}})
        end
    end

    local id = luci.http.formvalue("id")
    local step = luci.http.formvalue("step")
    local portmap = portMap(11)
    local vlantbl = getvlantable(id, step)
    local destbl = {}
    for _, v in pairs(vlantbl) do
        local mtbl = {}
        mtbl['id'] = tonumber(v['Index'])
        mtbl['name'] = v['Name']
        mtbl['type'] = vlandb.typeint2str(v['type'])

        mtbl['untaggedMember'] = ""
        mtbl['taggedMember'] = ""
        for _, v in ipairs(tools.str2array(v['untagmbr'])) do
            mtbl['untaggedMember'] = mtbl['untaggedMember'] .. portmap[tostring(v)] .. ", "
        end
        for _, v in ipairs(tools.str2array(v['tagmbr'])) do
            mtbl['taggedMember'] = mtbl['taggedMember'] .. portmap[tostring(v)] .. ", "
        end
        mtbl['untaggedMember'] = string.gsub(mtbl['untaggedMember'], ", $", "")
        mtbl['taggedMember'] = string.gsub(mtbl['taggedMember'], ", $", "")
        table.insert(destbl, mtbl)
    end

    local data = {data = tools.array_check(destbl)}

    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function setport(index, pvid, pmode, allowvlan, untagvlan)
    assert(index, "index is error")

    local data = {}
    local str = "type=port;id=".. index
    if modetrans(pmode) then
        str = str .. ";pmode=" .. modetrans(pmode)
    end

    if tonumber(pvid) and tools.range_hit(tonumber(pvid), 1, 4094) then
        str = str .. ";pvid=" .. pvid
    end

    if modetrans(pmode) == "3" or modetrans(pmode) == "2" and allowvlan then
        str = str .. ";allowvlan=" .. allowvlan
    end

    if modetrans(pmode) == "2" and untagvlan then
        str = str .. ";untagvlan=" .. untagvlan
    end

    table.insert(data, str)

    return comdb.com_setall("oltmib_nsm_set_1", "/nsm/portconf", data, 3, 6)
end

function handle_trunk()
    luci.http.prepare_content("application/json")
    if luci.http.getenv('REQUEST_METHOD') == 'POST' then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['ports']) == "table", "ports is error")
        assert(type(params['info']['pmode']) == "string", "pmode is error")
        assert(tonumber(params['info']['pvid']) and tools.range_hit(tonumber(params['info']['pvid']), 1, 4094), "pvid is error")

        local portsgrp = params['ports']
        local info = params['info']
        local pmode = info['pmode']
        local pvid = info['pvid']
        local allowvlan = info['allowvlans']
        local untagvlan = info['untaggedvlans']
        for _, v in ipairs(portsgrp) do
            local row = mydb.getport(v)
            if row['mytype'] == 0x10 then
                return luci.http.write_json({hdr = {code = 100, message = "Cannot configure member interface of port-channel!", type = "fail"}})
            end

            if not setport(v, pvid, pmode, allowvlan, untagvlan) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local porttbl = mydb.getporttable(11)
    local portconftbl = comdb.com_getall("oltmib_nsm_get_1", "/nsm/portconf", 2, "type=11")
    for _, v in ipairs(portconftbl) do
        local row = {}
        row['id'] = tonumber(v['id'])
        row['name'] = v['name']
        row['pmode'] = modetrans(v['pmode'])
        row['pvid'] = tonumber(v['pvid'])
        row['allowvlans'] = v['allowvlan']
        row['untaggedvlans'] = v['untagvlan']
        table.insert(destbl, row)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_info()
    luci.http.prepare_content("application/json")

    local destbl = {}
    local vlantbl= {}
    str = librpc.callapi("oltmib_cvlan_table_get_1", "")
    _, _, vlans, msg, oper, result = string.find(str, string.rep("(.-)&", 3) .. "(.*)")
    if result == "0" then
        local byte, vid
        for i = 1, 683, 1 do
            byte = string.byte(vlans, i, i)
            for j = 0, 5, 1 do
                if bit.band(byte, bit.lshift(1, j)) ~= 0 then
                    vid = (i - 1) * 6 + j
                    table.insert(destbl, vid)
                end
            end
        end
    end

    local data = {vlan = tools.array_check(destbl)}

    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
