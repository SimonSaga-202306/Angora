local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.poe", package.seeall)

function index()
    entry({ "api", "poe" }, alias("api", "poe", "info"), nil).hidden = true
    entry({ "api", "poe", "info" }, call("handle_info"), nil).leaf = true
    entry({ "api", "poe", "conf" }, call("handle_config"), nil).leaf = true
    entry({ "api", "poe", "portinfo" }, call("handle_portinfo"), nil).leaf = true
    entry({ "api", "poe", "portconf" }, call("handle_portconf"), nil).leaf = true
end

function handle_info()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        return luci.http.write_json({ hdr = { code = 100, message = "Oper unsupported!", type = "fail" } })
    end

    local poeinfo = mydb.getpoeinfo()
    local data = tools.array_check(poeinfo)
    return luci.http.write_json({ hdr = { code = 0, message = "ok", type = "success" }, result = data })
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")

        local poeinfo = mydb.getpoeconf()
        params['power_supply'] = tools.valfilter(params['power_supply'], poeinfo['power_supply_def'])
        if params["alarm_percent"] == luci.json.null then params["alarm_percent"] = 0 end
        if not mydb.setpoeconf(params) then
            return luci.http.write_json({ hdr = { code = 100, message = "Given parameters are invalid!", type = "fail" } })
        end
        return luci.http.write_json({ hdr = { code = 0, message = "ok", type = "success" } })
    end

    local destbl = {}
    local poeinfo = mydb.getpoeconf()
    destbl['power_supply'] = tonumber(poeinfo['power_supply'])
    destbl['res_percent'] = tonumber(poeinfo['res_percent'])
    destbl['alarm_percent'] = tonumber(poeinfo['alarm_percent'])
    destbl['disc_mode'] = 'DC'
    destbl['alg'] = 'energy-saving'

    local data = tools.array_check(destbl)
    return luci.http.write_json({ hdr = { code = 0, message = "ok", type = "success" }, result = data })
end

function handle_portinfo()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        return luci.http.write_json({ hdr = { code = 100, message = "Oper unsupported!", type = "fail" } })
    end

    local poeiftbl = mydb.getpoeifinfotbl()
    local data = { data = tools.array_check(poeiftbl) }
    return luci.http.write_json({ hdr = { code = 0, message = 'ok', type = 'success' }, result = data })
end

function handle_portconf()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['admin_state']) == "boolean" or type(params['admin_state']) == "nil", "admin_state is error")

        local info = params['info']
        if info["max_power"] == luci.json.null then info["max_power"] = 0 end
        local portsgrp = params['ports'] or {}
        local poeiftbl = mydb.getpoeifconftbl()
        for _, ifx in ipairs(portsgrp) do
            for _, poeif in ipairs(poeiftbl) do
                if ifx == tonumber(poeif['id']) then
                    ack = mydb.setpoeifconf(tools.tMerge(poeif, info))
                    if ack == false then return luci.http.write_json({ hdr = { code = 100,
                        message = "Given parameters are invalid!", type = "fail" } }) end
                end
            end
        end

        return luci.http.write_json({ hdr = { code = 0, message = "ok", type = "success" } })
    end

    local poeiftbl = mydb.getpoeifconftbl()
    local data = { data = tools.array_check(poeiftbl) }
    return luci.http.write_json({ hdr = { code = 0, message = 'ok', type = 'success' }, result = data })
end
