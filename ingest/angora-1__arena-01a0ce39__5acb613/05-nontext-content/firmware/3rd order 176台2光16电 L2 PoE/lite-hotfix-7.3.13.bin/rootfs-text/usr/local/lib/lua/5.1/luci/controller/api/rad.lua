local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.rad", package.seeall)

function index()
    entry({"api", "rad"}, alias("api", "rad", "conf"), nil).hidden = true
    entry({"api", "rad", "conf"}, call("handle_config"), nil).leaf = true
    entry({"api", "rad", "srv"}, call("handle_server"), nil).leaf = true
end

function handle_config()
    local default_key = "******"
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['tout']) == 'number' and tools.range_hit(params['tout'], 1, 60), "timeout is error")
        assert(type(params['retry']) == 'number' and tools.range_hit(params['retry'], 1, 100), "retry is error")
        assert(type(params['deadtime']) == 'number' and tools.range_hit(params['deadtime'], 0, 1440), "deadtime is error")

        if params['key'] and params['key'] ~= "" and not tools.range_hit(#params['key'], 1, 63) then
            return luci.http.write_json({hdr = {code = 1000, message = "The key length cannot be more than 63", type = "fail"}})
        end

        local radglobal = mydb.getradglobal()
        radglobal["shared_secret"] = 7
        radglobal['key'] = params['key'] or ""
        if radglobal['key'] ~= default_key then
            radglobal["shared_secret"] = 0
        end
        radglobal['timeout'] = tostring(params['tout'])
        radglobal['max_retry'] = tostring(params['retry'])
        radglobal['deadtime'] = tostring(params['deadtime'])
        if not mydb.setradglobal(radglobal) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local radglobal = mydb.getradglobal()
    destbl['key'] = default_key
    destbl['tout'] = tonumber(radglobal['timeout'])
    destbl['retry'] = tonumber(radglobal['max_retry'])
    destbl['deadtime'] = tonumber(radglobal['deadtime'])

    local data = destbl
    return luci.http.write_json({hdr = {code = 0, message = 'ok', type = 'success'}, result = destbl})
end

function handle_server()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['info']['ip']) == "string", "ip is error")

        if params['info']['ip'] == "" then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end

        if params['info']['auth_port'] and not tools.range_hit(params['info']['auth_port'], 1, 65535) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end
        if params['info']['tout'] and not tools.range_hit(params['info']['tout'], 1, 60) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end
        if params['info']['retry'] and not tools.range_hit(params['info']['retry'], 1, 100) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end
        if params['info']['key'] and params['info']['key'] ~= "" and not tools.range_hit(#params['info']['key'], 1, 63) then
            return luci.http.write_json({hdr = {code = 1000, message = "The key length cannot be more than 63", type = "fail"}})
        end

        local info = params['info']
        local oper = params['oper'] or ""
        if oper ~= "del" then
            local radsrvdata = {ip = "", auth_port = "1812", acct_port = "1813", shared_secret = "", key= "", timeout= "5", max_retry = "3"}
            radsrvdata['ip'] = info['ip']
            radsrvdata['auth_port'] = tostring(info['auth_port'])
            radsrvdata['key'] = info['key'] or radsrvdata['key']
            radsrvdata['timeout'] = tostring(info['tout'])
            radsrvdata['max_retry'] = tostring(info['retry'])
            if not mydb.setradsrv(radsrvdata) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        else
            local radsrvtbl = mydb.getradsrvtbl()
            for _, radsrv in ipairs(radsrvtbl) do
                if info['ip'] == radsrv['ip'] and info['auth_port'] == tonumber(radsrv['auth_port']) then
                    radsrv['oper'] = "2"
                    if not mydb.setradsrv(radsrv) then
                        return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                    end
                end
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local radsrvtbl = mydb.getradsrvtbl()
    for _, radsrv in ipairs(radsrvtbl) do
        local radsrvdata = {}
        radsrvdata['ip'] = radsrv['ip']
        radsrvdata['auth_port'] = tonumber(radsrv['auth_port'])
        radsrvdata['tout'] = tonumber(radsrv['timeout'])
        radsrvdata['retry'] = tonumber(radsrv['max_retry'])
        table.insert(destbl, radsrvdata)
    end

    local data = {data = tools.array_check(destbl)}
    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
