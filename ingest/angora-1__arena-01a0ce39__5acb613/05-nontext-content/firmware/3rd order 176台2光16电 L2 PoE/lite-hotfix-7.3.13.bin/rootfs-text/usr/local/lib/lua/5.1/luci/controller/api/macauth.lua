local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.macauth", package.seeall)

function index()
    entry({"api", "macauth"}, alias("api", "macauth", "port"), nil).hidden = true
    entry({"api", "macauth", "port"}, call("handle_port"), nil).leaf = true
    entry({"api", "macauth", "conf"}, call("handle_config"), nil).leaf = true
    entry({"api", "macauth", "info"}, call("handle_info"), nil).leaf = true
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['state']) == "boolean", "state is error")

        local authglobaldata = {}
        authglobaldata['config'] = '2'
        authglobaldata['oper'] = params['state'] and '0' or '2'
        if not mydb.setauthglobal(authglobaldata) then
            return luci.http.write_json({hdr = {code = 100, message = "Port authentication is configured", type = "fail"}})
        end
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local authglobal = mydb.getauthglobal()
    local state = authglobal['config'] == 2
    local data = {state = state}
    return luci.http.write_json({hdr = {code = 0, message = 'ok', type = 'success'}, result = data})
end

function handle_port()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        local info = params['info']

        local portsgrp = params['ports'] or {}
        for _, pid in ipairs(portsgrp) do
            local macauthportdata = {}
            macauthportdata['ifx'] = tostring(pid)
            local macauthport = mydb.getmacauthport(macauthportdata)
            macauthport['authmacPortControl'] = type(info['state']) == "boolean" and (info['state'] and 'Enable' or 'Disable') or macauthport['authmacPortControl']
            macauthport['mac_address_aging'] = type(info['aging']) == "boolean" and (info['aging'] and 'Enabled' or 'Disabled') or macauthport['mac_address_aging']
            if not mydb.setmacauthport(macauthport) then
                return luci.http.write_json({hdr = {code = 100, message = "Failed to modify port", type = "fail"}})
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local macauthporttbl = mydb.getmacauthporttbl()
    for _, macauthport in ipairs(macauthporttbl) do
        local macauthportdata = {}
        macauthportdata['id'] = tonumber(macauthport['ifx'])
        macauthportdata['name'] = macauthport['name']
        macauthportdata['state'] = macauthport['authmacPortControl'] == 'Enable'
        macauthportdata['aging'] = macauthport['mac_address_aging'] == 'Enabled'
        table.insert(destbl, macauthportdata)
    end

    local data = {data = tools.array_check(destbl)}
    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_info()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['info']['id']) == "number", "info is error")
        assert(type(params['info']['vid']) == "number", "info is error")
        assert(type(params['info']['mac']) == "string", "mac is error")

        local info = params['info']
        local oper = params['oper'] or ""
        local staticmacdata = {}
        staticmacdata['ifx'] = tostring(info['id'])
        staticmacdata['ifname'] = info['name']
        staticmacdata['vid'] = tostring(info['vid'])
        staticmacdata['mac'] = info['mac']
        staticmacdata['is_dynamic'] = info['aging'] and 'Enabled' or 'Disabled'
        staticmacdata['fwd'] = info['state'] and 'True' or 'False'
        if oper ~= "delete" then
            if not mydb.setstaticmac(staticmacdata) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        else
            local macauthusertbl = mydb.getmacauthusertbl()
            for _, macauthuser in ipairs(macauthusertbl) do
                if info['id'] == tonumber(macauthuser['ifx']) and info['vid'] == tonumber(macauthuser['vid']) and info['mac'] == macauthuser['mac'] then
                    macauthuser['oper'] = '2'
                    if not mydb.setmacauthuser(macauthuser) then
                        return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                    end
                end
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local macauthusertbl = mydb.getmacauthusertbl()
    for _, macauthuser in ipairs(macauthusertbl) do
        local macauthuserdata = {}
        macauthuserdata['id'] = tonumber(macauthuser['ifx'])
        macauthuserdata['name'] = macauthuser['ifname']
        macauthuserdata['vid'] = tonumber(macauthuser['vid'])
        macauthuserdata['mac'] = macauthuser['mac']
        macauthuserdata['aging'] = macauthuser['is_dynamic'] == 'Enabled'
        macauthuserdata['state'] = macauthuser['fwd'] == 'True'
        macauthuserdata['timestamp'] = macauthuser['timestamp']
        table.insert(destbl, macauthuserdata)
    end

    local data = {data = tools.array_check(destbl)}
    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
