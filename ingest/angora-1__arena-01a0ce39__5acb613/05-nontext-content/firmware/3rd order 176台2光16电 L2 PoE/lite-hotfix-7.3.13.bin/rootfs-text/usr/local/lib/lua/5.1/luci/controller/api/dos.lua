local json = require "luci.json"
local srvdb = require "luci.controller.lib.srvdb"
local tools = require "luci.controller.lib.tools"
local nixio = require "nixio"
local fs = require "nixio.fs"

module("luci.controller.api.dos", package.seeall)

function index()
    entry({"api", "dos"}, alias("api", "dos", "config"), nil).hidden = true
    entry({"api", "dos", "config"}, call("handle_config"), nil).leaf = true
    entry({"api", "dos", "port"}, call("handle_port"), nil).leaf = true
end

function dostype_trans(data)
    local tbl = {}
    tbl["0"] = "syn-flood"
    tbl["1"] = "icmp-flood"
    tbl["2"] = "arp-flood"
    tbl["3"] = "null-scan"
    tbl["4"] = "syn-fin"
    tbl["5"] = "syn-sportl1024"
    tbl["6"] = "fin-noack"
    tbl["syn-flood"] = "0"
    tbl["icmp-flood"] = "1"
    tbl["arp-flood"] = "2"
    tbl["null-scan"] = "3"
    tbl["syn-fin"] = "4"
    tbl["syn-sportl1024"] = "5"
    tbl["fin-noack"] = "6"

    return tbl[tostring(data)] or ""
end

function getdosglobaltbl()
    local tbl = {}
    result = "0"
    dostype = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_dosglobal_get_1", "&&" .. dostype)
        _, _, _, _, dostype, limit_enable, limit, cnt_enable, drops_cnt, permit_cnt, msg, oper, result = string.find(str, string.rep("(.-)&", 10) .. "(.*)")
        if (result == "0") then
            local row = {}
            row['type'] = dostype_trans(dostype)
            row['state_enable'] = limit_enable
            row['limit'] = limit
            row['cnt_enable'] = cnt_enable
            row['drops_cnt'] = drops_cnt
            row['permit_cnt'] = permit_cnt
            table.insert(tbl, row)
            dostype = dostype + 1
        end
    end

    return tbl
end

function setdosglobal(data, oper)
    str = "&&" .. dostype_trans(data['type']) .. "&" .. (data['state_enable'] or "") .. "&" .. (data['limit'] or "") .. "&" .. (data['cnt_enable'] or "") .. "&&&&"  .. (oper or "")
    result = librpc.callapi("oltmib_dosglobal_set_1", str)
    return result == "0"
end

function getdosiftbl()
    local tbl = {}
    local idx = 0
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_dosif_getn_1", str)
        _, _, ifx, name, dostype, limit_enable, limit, cnt_enable, drops_cnt, permit_cnt, msg, oper, result = string.find(str, string.rep("(.-)&", 10) .. "(.*)")
        if (result == "0") then
            local row = {}
            if (not next(tbl) or tbl[idx]["ifx"] ~= ifx) then
                idx = idx + 1
                tbl[idx] = {}
                tbl[idx]['ifx'] = ifx
                tbl[idx]['name'] = name
                tbl[idx]['type'] = {}
                row['name'] = dostype_trans(dostype)
                row['state_enable'] = limit_enable
                row['limit'] = limit
                row['cnt_enable'] = cnt_enable
                row['drops_cnt'] = drops_cnt
                row['permit_cnt'] = permit_cnt
                table.insert(tbl[idx]['type'], row)
            else
                row['name'] = dostype_trans(dostype)
                row['state_enable'] = limit_enable
                row['limit'] = limit
                row['cnt_enable'] = cnt_enable
                row['drops_cnt'] = drops_cnt
                row['permit_cnt'] = permit_cnt
                table.insert(tbl[idx]['type'], row)
            end
        end
    end

    return tbl
end

function setdosif(data, oper)
    str =  data['ifx'] .. "&&" .. dostype_trans(data['type']) .. "&" .. (data['state_enable'] or "") .. "&" .. (data['limit'] or "")
    result = librpc.callapi("oltmib_dosif_set_1", str)
    return result == "0"
end

function handle_config()
    luci.http.prepare_content("application/json")

    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")

        local info = params['info']
        local oper = params['oper'] or ''

        if (info['limit'] and not tools.range_hit(tonumber(info['limit']), 0, 10000)) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end

        if oper == "clear" then
            -- reset counters
            oper = 4
        end

        for _, v in ipairs(info) do
            local dosdata = {}
            dosdata['type'] = v['type']
            dosdata['limit'] = v['limit'] or ''
            dosdata['cnt_enable'] = tools.bool_trans(v['cnt_enable'])
            if (type(v['state_enable']) == "boolean") then
                dosdata['state_enable'] = tools.bool_trans(v['state_enable'])
            else
                dosdata['state_enable'] = v['limit'] and 1 or 0
            end
            if not setdosglobal(dosdata, oper) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local dosglobaltbl = getdosglobaltbl()
    for _, dosglobal in ipairs(dosglobaltbl) do
        local row = {}
        row['type'] = dosglobal['type']
        row['state_enable'] = tools.bool_trans(dosglobal['state_enable'])
        row['limit'] = tonumber(dosglobal['limit'])
        row['cnt_enable'] = tools.bool_trans(dosglobal['cnt_enable'])
        row['drops_cnt'] = dosglobal['drops_cnt']
        row['permit_cnt'] = dosglobal['permit_cnt']
        table.insert(destbl, row)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_port()
    luci.http.prepare_content("application/json")

    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")

        local info = params['info']
        local portsgrp = params['ports'] or {}
        local oper = params['oper'] or ''

        if (info['limit'] and not tools.range_hit(tonumber(info['limit']), 0, 10000)) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end

        for _, ifx in ipairs(portsgrp) do
            local dosdata = {}
            dosdata['ifx'] = ifx
            dosdata['type'] = info['type']
            dosdata['limit'] = info['limit'] or ''
            if (type(info['state_enable']) == "boolean") then
                dosdata['state_enable'] = tools.bool_trans(info['state_enable'])
            else
                dosdata['state_enable'] = info['limit'] and 1 or 0
            end

            if not setdosif(dosdata) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local dosiftbl = getdosiftbl()
    for _, dosif in ipairs(dosiftbl) do
        local row = {}
        row['id'] = tonumber(dosif['ifx'])
        row['name'] = dosif['name']
        row['type'] = {}
        for k, v in ipairs(dosif['type']) do
            row['type'][k] = {}
            row['type'][k]['name'] = v['name']
            row['type'][k]['state_enable'] = tools.bool_trans(v['state_enable'])
            row['type'][k]['limit'] = tonumber(v['limit'])
            row['type'][k]['cnt_enable'] = tools.bool_trans(v['cnt_enable'])
            row['type'][k]['drops_cnt'] = v['drops_cnt']
            row['type'][k]['permit_cnt'] = v['permit_cnt']
        end
        table.insert(destbl, row)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
