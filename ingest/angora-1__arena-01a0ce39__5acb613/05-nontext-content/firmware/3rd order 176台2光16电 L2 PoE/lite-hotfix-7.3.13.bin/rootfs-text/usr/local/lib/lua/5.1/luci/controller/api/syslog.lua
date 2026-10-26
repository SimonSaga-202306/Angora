local json = require "luci.json"
local srvdb = require "luci.controller.lib.srvdb"
local tools = require "luci.controller.lib.tools"
local nixio = require "nixio"
local fs = require "nixio.fs"

module("luci.controller.api.syslog", package.seeall)

function index()
    entry({"api", "syslog"}, alias("api", "syslog", "server"), nil).hidden = true
    entry({"api", "syslog", "server"}, call("handle_server"), nil).leaf = true
end

function getsyslogservertbl()
    local tbl = {}
    result = "0"
    id = 0
    while (result == "0") do
        str = librpc.callapi("oltmib_syslogremote_get_1", id .. "&&&&&")
        _, _, server, ip, port, mdg, oper, result = string.find(str, string.rep("(.-)&", 5) .. "(.*)")
        if (result == "0") then
            local row = {}
            id = id + 1
            row['id'] = server
            row['ip'] = ip
            row['udp_port'] = port
            table.insert(tbl, row)
        end
    end

    return tbl
end

function setsyslogserver(data)
    str = data['id'] .. "&" .. (data['ip'] or "") .. "&" .. (data['udp_port'] or "")
    result = librpc.callapi("oltmib_syslogremote_set_1", str)
    return result == "0"
end

function handle_server()
    luci.http.prepare_content("application/json")

    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")

        local info = params['info']
        local oper = params['oper'] or ''

        if (not tools.range_hit(tonumber(info['id']), 0, 2)) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end

        if (tonumber(info['udp_port']) and not tools.range_hit(tonumber(info['udp_port']), 1, 65535)) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end

        local serverdata = {}
        serverdata['id'] = info['id']
        serverdata['ip'] = info['ip']
        serverdata['udp_port'] = info['udp_port']
        if not setsyslogserver(serverdata) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local syslogservertbl = getsyslogservertbl()
    for _, v in ipairs(syslogservertbl) do
        local row = {}
        row['id'] = tonumber(v['id'])
        row['ip'] = v['ip']
        row['udp_port'] = tonumber(v['udp_port'])
        table.insert(destbl, row)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
