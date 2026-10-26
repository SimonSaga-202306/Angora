local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.mac", package.seeall)

function index()
    entry({"api", "mac"}, alias("api", "mac", "conf"), nil).hidden = true
    entry({"api", "mac", "conf"}, call("handle_config"), nil).leaf = true
    entry({"api", "mac", "entry"}, call("handle_entry"), nil).leaf = true
    entry({"api", "mac", "info"}, call("handle_info"), nil).leaf = true
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['aging']) == "number" and params['aging'] >= 0 and params['aging'] <= 600, "aging is error")

        local macparam = {}
        macparam['value'] = tostring(params['aging'])
        mydb.setmacparam(macparam)
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local macparam = mydb.getmacparam()
    local aging = tonumber(macparam['value'])
    local data = {aging = aging}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_entry()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['info']['mac']) == "string", "mac is error")
        assert(type(params['info']['type']) == "string", "type is error")

        local ack = true
        local info = params['info']
        local oper = params['oper'] or ""
        local macdata = {}
        macdata['mac'] = info['mac']
        macdata['vid'] = mydb.filter_vlan(tostring(info['vid'] or ''))
        macdata['vid'] = tostring(info['vid'])
        if oper ~= "del" and info['type'] == 'filter' then
            ack = mydb.setfiltermac(macdata)
        elseif oper ~= "del" and info['type'] == 'static' then
            local port = mydb.getport(info['id'])
            if port and port['mytype'] == 0x10 then
                return luci.http.write_json({hdr = {code = 100, message = "Cannot configure member interface of port-channel!", type = "fail"}})
            end
            macdata['ifname'] = port['Name']
            ack = mydb.setstaticmac(macdata)
        elseif info['type'] == 'filter' then
            macdata['oper'] = '2'
            ack = mydb.setfiltermac(macdata)
        else
            local port = mydb.getport(info['id'])
            if port and port['mytype'] == 0x10 then
                return luci.http.write_json({hdr = {code = 100, message = "Cannot configure member interface of port-channel!", type = "fail"}})
            end
            macdata['ifname'] = port['Name']
            macdata['oper'] = '2'
            ack = mydb.setstaticmac(macdata)
        end

        if not ack then return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}}) end
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local porttbl = mydb.getporttable(11)
    local staticmactbl = mydb.getstaticmactbl()
    local filtermactbl = mydb.getfiltermactbl()
    for _, staticmac in ipairs(staticmactbl) do
        local staticmacdata = {}
        local portinfo = mydb.getportintbl_by_name(porttbl, staticmac['ifname'])
        if portinfo then
            staticmacdata['id'] = tonumber(portinfo['Index'])
            staticmacdata['name'] = staticmac['ifname']
            staticmacdata['vid'] = tonumber(staticmac['vid'])
            staticmacdata['mac'] = staticmac['mac']
            staticmacdata['type'] = 'static'
            table.insert(destbl, staticmacdata)
        end
    end

    for _, filtermac in ipairs(filtermactbl) do
        local filtermacdata = {}
        filtermacdata['vid'] = tonumber(filtermac['vid'])
        filtermacdata['mac'] = filtermac['mac']
        filtermacdata['type'] = 'filter'
        table.insert(destbl, filtermacdata)
    end

    local data = {data = tools.array_check(destbl)}
    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function getmactbl(data)
    tbl = {}
    init_cnt = tonumber(data['step']) or 1024
    cnt = init_cnt
    result = "0"
    if not (data["type"] and data["type"] == "dynamic") then
        str = (data["mac"] or "") .. "&" .. (data['vid'] or "")
        while (result == "0" and cnt > 0 ) do
            str = librpc.callapi("oltmib_fdb_getn_1", str)
            _, _, mac, vid, ifname, is_forward, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
            if (result == "0") then
                local row = {}
                row["mac"] = mac
                row["vid"] = vid
                row["ifname"] = ifname
                row['type'] = is_forward == "1" and "static" or "filter"
                table.insert(tbl, row)
                cnt = cnt - 1
            end
        end
    end

    result = "0"
    str = ""
    if (cnt == init_cnt and data["type"] and data["type"] == "dynamic") then str = (data["mac"] or "") .. "&" .. (data['vid'] or "") end
    while (result == "0" and cnt > 0) do
        str = librpc.callapi("oltmib_fdb_dynamic_getn_1", str)
        _, _, mac, vid, ifname, is_forward, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["mac"] = mac
            row["vid"] = vid
            row["ifname"] = ifname
            row['type'] = "dynamic"
            table.insert(tbl, row)
            cnt = cnt - 1
        end
    end

    return tbl
end

function handle_info()
    luci.http.prepare_content("application/json")
    local type = luci.http.formvalue("type") or ""
    local mac = luci.http.formvalue("mac") or ""
    local vid = luci.http.formvalue("vid") or 0
    local step = luci.http.formvalue("step") or 1024

    local destbl = {}
    local porttbl = mydb.getporttable(11)
    local mactbl = getmactbl({mac = mac, vid = vid, step = step, type = type})

    for k, v in ipairs(mactbl) do
        local mac = {}
        local portinfo = mydb.getportintbl_by_name(porttbl, v['ifname'])
        mac['id'] = portinfo and tonumber(portinfo['Index'])
        mac['name'] = v['ifname']
        mac['vid'] = tonumber(v['vid'])
        mac['mac'] = v['mac']
        mac['type'] = v['type']
        table.insert(destbl, mac)
    end

    local data = {data = tools.array_check(destbl)}
    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
