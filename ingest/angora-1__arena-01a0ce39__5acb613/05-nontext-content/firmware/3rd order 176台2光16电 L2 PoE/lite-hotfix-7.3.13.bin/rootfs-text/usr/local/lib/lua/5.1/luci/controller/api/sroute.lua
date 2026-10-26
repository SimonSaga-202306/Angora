local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.sroute", package.seeall)

function index()
    entry({"api", "sroute"}, alias("api", "sroute", "conf"), nil).hidden = true
    entry({"api", "sroute", "conf"}, call("handle_config"), nil).leaf = true
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['info']['prefix']) == "string", "prefix is error")
        assert(type(params['info']['nexthop']) == "string", "nexthop is error")

        if params['info']['desc'] and #params['info']['desc'] > 31 then
            return luci.http.write_json({hdr = {code = 100, message = "'desc' cannot be longer than 31 characters", type = "fail"}})
        end

        local info = params['info']
        local oper = params['oper'] or ''
        local routedata = {}
        routedata['prefix'] = info['prefix']
        routedata['nextip'] = info['nexthop']
        routedata['desc'] = info['desc']
        if oper == "del" then routedata['oper'] = "2" end
        if not mydb.setroute(routedata) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local routetbl = mydb.getroutetbl()
    for _, route in ipairs(routetbl) do
        local routedata = {}
        routedata['prefix'] = route['prefix']
        routedata['nexthop'] = route['nextip']
        routedata['desc'] = route['desc']
        table.insert(destbl, routedata)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
