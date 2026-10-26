local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.dot1x", package.seeall)

function index()
    entry({"api", "dot1x"}, alias("api", "dot1x", "conf"), nil).hidden = true
    entry({"api", "dot1x", "conf"}, call("handle_config"), nil).leaf = true
    entry({"api", "dot1x", "port"}, call("handle_port"), nil).leaf = true
    entry({"api", "dot1x", "info"}, call("handle_info"), nil).leaf = true
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['state']) == "boolean", "state is error")

        local authglobaldata = {}
        authglobaldata['config'] = '1'
        authglobaldata['oper'] = params['state'] and '0' or '2'
        if not mydb.setauthglobal(authglobaldata) then 
            return luci.http.write_json({hdr = {code = 100, message = "MAC-based authentication is configured", type = "fail"}})
        end
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local authglobal = mydb.getauthglobal()
    local state = authglobal['config'] == 1
    local data = {state = state}
    return luci.http.write_json({hdr = {code = 0, message = 'ok', type = 'success'}, result = data})
end

function handle_port()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")

        if params['info']['protocol_version'] and not tools.range_hit(tonumber(params['info']['protocol_version']), 1, 2) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end
        if params['info']['quietPeriod'] and not tools.range_hit(tonumber(params['info']['quietPeriod']), 1, 65535) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end
        if params['info']['txPeriod'] and not tools.range_hit(tonumber(params['info']['txPeriod']), 1, 65535) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end
        if params['info']['reAuthPeriod'] and not tools.range_hit(tonumber(params['info']['reAuthPeriod']), 1, 4294967295) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end
        if params['info']['suppTimeout'] and not not tools.range_hit(tonumber(params['info']['reAuthPeriod']), 1, 65535) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end
        if params['info']['serverTimeout'] and not not tools.range_hit(tonumber(params['info']['reAuthPeriod']), 1, 65535) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}}) 
        end

        local info = params['info']
        local portsgrp = params['ports'] or {}
        for _, pid in ipairs(portsgrp) do
            local d1xportdata = {}
            d1xportdata['ifx'] = tostring(pid)
            local d1xport = mydb.getd1xport(d1xportdata)
            d1xport['portControl'] = tools.valfilter(info['control'], "Disable") or d1xport['portControl']
            d1xport['protocol_version'] = tools.valfilter(info['version'], 2) or d1xport['protocol_version']
            d1xport['quietPeriod'] = tools.valfilter(info['quiet_period'], 60) or d1xport['quietPeriod']
            d1xport['txPeriod'] = tools.valfilter(info['tx_period'], 30) or d1xport['txPeriod']
            d1xport['reAuthEnabled'] = type(info['reauth_enable']) == 'boolean' and (info['reauth_enable'] and "Enabled" or "Disabled") or d1xport['reAuthEnabled']
            d1xport['reAuthPeriod'] = tools.valfilter(info['reauth_period'], 3600) or d1xport['reAuthPeriod']
            d1xport['suppTimeout'] = tools.valfilter(info['supp_tout'], 30) or d1xport['suppTimeout']
            d1xport['serverTimeout'] = tools.valfilter(info['srv_tout'], 30) or d1xport['serverTimeout']
            if not mydb.setd1xport(d1xport) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local d1xporttbl = mydb.getd1xporttbl()
    for _, d1xport in ipairs(d1xporttbl) do
        local d1xportdata = {}
        d1xportdata['id'] = tonumber(d1xport['ifx'])
        d1xportdata['name'] = d1xport['name']
        d1xportdata['control'] = d1xport['portControl']
        d1xportdata['version'] = tonumber(d1xport['protocol_version'])
        d1xportdata['quiet_period'] = tonumber(d1xport['quietPeriod'])
        d1xportdata['tx_period'] = tonumber(d1xport['txPeriod'])
        d1xportdata['reauth_enable'] = d1xport['reAuthEnabled'] == 'Enabled'
        d1xportdata['reauth_period'] =  tonumber(d1xport['reAuthPeriod'])
        d1xportdata['supp_tout'] = tonumber(d1xport['suppTimeout'])
        d1xportdata['srv_tout'] = tonumber(d1xport['serverTimeout'])
        table.insert(destbl, d1xportdata)
    end

    local data = {data = tools.array_check(destbl)}
    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_info()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "GET" then
        local destbl = {}
        local d1xportsttbl = mydb.getd1xportsttbl()
        for _, d1xportst in ipairs(d1xportsttbl) do
            local d1xportstdata = {}
            d1xportstdata['id'] = tonumber(d1xportst['ifx'])
            d1xportstdata['name'] = d1xportst['name']
            d1xportstdata['enable'] = d1xportst['portEnabled'] == 'Enabled'
            d1xportstdata['control'] = d1xportst['portControl']
            d1xportstdata['state'] = d1xportst['portStatus']
            d1xportstdata['pae_state'] = d1xportst['pae_state']
            table.insert(destbl, d1xportstdata)
        end

        local data = {data = tools.array_check(destbl)}
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
    end
end
