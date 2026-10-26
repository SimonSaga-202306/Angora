local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.psec", package.seeall)

function index()
    entry({"api", "psec"}, alias("api", "psec", "port"), nil).hidden = true
    entry({"api", "psec", "port"}, call("handle_port"), nil).leaf = true
    entry({"api", "psec", "mac"}, call("handle_mac"), nil).leaf = true
    entry({"api", "psec", "portinfo"}, call("handle_portinfo"), nil).leaf = true
    entry({"api", "psec", "macinfo"}, call("handle_macinfo"), nil).leaf = true
end

function handle_port()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['info']['state']) == "boolean", "state is error")
        assert(type(params['info']['max_mac_num']) == "number" and params['info']['max_mac_num'] > 0 and params['info']['max_mac_num'] <= 1024, "max_mac_num is error")
        assert(type(params['info']['sticky']) == "boolean", "sticky is error")
        assert(type(params['info']['aging_time']) == "number" and params['info']['aging_time'] >= 0 and params['info']['aging_time'] <= 1440, "aging_time is error")
        assert(type(params['info']['aging_static']) == "boolean", "aging_static is error")
        assert(type(params['info']['violation_mode']) == "string", "violation_mode is error")

        local info = params['info']
        local portsgrp = params['ports'] or {}
        for _, pid in ipairs(portsgrp) do
            local nsmpsdata = mydb.getnsmps({ifx = tostring(pid)})
            nsmpsdata['enable'] = info['state'] and 'Enabled' or 'Disabled'
            nsmpsdata['max'] = info['max_mac_num']
            nsmpsdata['sticky'] = info['sticky'] and 'Enabled' or 'Disabled'
            nsmpsdata['aging_time'] = tostring(info['aging_time'])
            nsmpsdata['aging_static'] = info['aging_static'] and 'Enabled' or 'Disabled'
            nsmpsdata['violation_mode'] = info['violation_mode']
            if not mydb.setnsmps(nsmpsdata) then
                return luci.http.write_json({hdr = {code = 100, message = "Failed to modify port", type = "fail"}})
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local nsmpsstatetbl = mydb.getnsmpsstatetbl()
    for _, nsmpsstate in ipairs(nsmpsstatetbl) do
        local nsmpsdata = {}
        nsmpsdata['id'] = tonumber(nsmpsstate['ifx'])
        nsmpsdata['name'] = nsmpsstate['name']
        nsmpsdata['state'] = nsmpsstate['enable'] == 'Enabled'
        nsmpsdata['max_mac_num'] = tonumber(nsmpsstate['max'])
        nsmpsdata['sticky'] = nsmpsstate['sticky'] == 'Enabled'
        nsmpsdata['aging_time'] = tonumber(nsmpsstate['aging_time'])
        nsmpsdata['aging_static'] = nsmpsstate['aging_static'] == 'Enabled'
        nsmpsdata['violation_mode'] = nsmpsstate['violation_mode']
        table.insert(destbl, nsmpsdata)
    end

    local data = {data = tools.array_check(destbl)}
    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_mac()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        local info = params['info']
        local oper = params['oper'] or ''

        if oper ~= "del" then
            local nsmpsmacdata = {}
            nsmpsmacdata['ifx'] = tostring(info['id'])
            nsmpsmacdata['name'] = ''
            nsmpsmacdata['vid'] = '0'
            nsmpsmacdata['mac'] = info['mac']
            nsmpsmacdata['type'] = info['type']
            if not mydb.setnsmpsmac(nsmpsmacdata) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        else
            local nsmpsmacstatetbl = mydb.getnsmpsmacstatetbl()
            for _, nsmpsmacstate in ipairs(nsmpsmacstatetbl) do
                if info['id'] == tonumber(nsmpsmacstate['ifx']) and info['mac'] == nsmpsmacstate['mac'] then
                    nsmpsmacstate['oper'] = '2'
                    if not mydb.setnsmpsmac(nsmpsmacstate) then
                        return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                    end
                end
            end
        end

        
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local nsmpsmacstatetbl = mydb.getnsmpsmacstatetbl()
    for _, nsmpsmacstate in ipairs(nsmpsmacstatetbl) do
        local mtbl = {}
        mtbl['id'] = tonumber(nsmpsmacstate['ifx'])
        mtbl['name'] = nsmpsmacstate['name']
        mtbl['mac'] = nsmpsmacstate['mac']
        mtbl['type'] = nsmpsmacstate['type']
        table.insert(destbl, mtbl)
    end

    local data = {data = tools.array_check(destbl)}
    return luci.http.write_json({hdr = {code = 0, message = 'ok', type = 'success'}, result = data})
end

function handle_portinfo()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "GET" then
        local destbl = {}
        local nsmpsstatetbl = mydb.getnsmpsstatetbl()
        for _, nsmpsstate in ipairs(nsmpsstatetbl) do
            local nsmpsdata = {}
            nsmpsdata['id'] = tonumber(nsmpsstate['ifx'])
            nsmpsdata['name'] = nsmpsstate['name']
            nsmpsdata['state'] = nsmpsstate['enable'] == 'Enabled'
            nsmpsdata['total_mac_num'] = tonumber(nsmpsstate['total_mac_num'])
            nsmpsdata['conf_mac_num'] = tonumber(nsmpsstate['config_mac_num'])
            nsmpsdata['violation_count'] = tonumber(nsmpsstate['violation_count'])
            nsmpsdata['last_violation_mac'] = nsmpsstate['last_violate_mac']
            nsmpsdata['last_violation_stamp'] = nsmpsstate['last_violate_stamp']
            table.insert(destbl, nsmpsdata)
        end

        local data = {data = tools.array_check(destbl)}
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
    end
end

function handle_macinfo()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "GET" then
        local destbl = {}
        local nsmpsmacstatetbl = mydb.getnsmpsmacstatetbl()
        for _, nsmpsmacstate in ipairs(nsmpsmacstatetbl) do
            local mtbl = {}
            mtbl['id'] = tonumber(nsmpsmacstate['ifx'])
            mtbl['name'] = nsmpsmacstate['name']
            mtbl['vid'] = tonumber(nsmpsmacstate['vid'])
            mtbl['mac'] = nsmpsmacstate['mac']
            mtbl['type'] = nsmpsmacstate['type']
            mtbl['aging'] = tonumber(nsmpsmacstate['age_time_left'])
            table.insert(destbl, mtbl)
        end

        local data = {data = tools.array_check(destbl)}
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
    end
end
