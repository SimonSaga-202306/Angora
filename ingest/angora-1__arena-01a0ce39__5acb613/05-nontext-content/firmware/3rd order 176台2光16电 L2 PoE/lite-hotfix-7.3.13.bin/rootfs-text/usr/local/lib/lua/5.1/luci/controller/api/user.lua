local json = require "luci.json"
local srvdb = require "luci.controller.lib.srvdb"
local authapi = require "luci.authapi"
local sauth = require "luci.sauth"
local librpc = require "librpc"

module("luci.controller.api.user", package.seeall)

function index()
    entry({"api", "user"}, alias("api", "user", "login"), nil).hidden = true
    entry({"api", "user", "login"}, call("action_login"), nil).hidden = true
    entry({"api", "user", "logout"}, call("action_logout"), nil).leaf = true
    entry({"api", "user", "info"}, call("handle_info"), nil).leaf = true
    entry({"api", "user", "conf"}, call("handle_config"), nil).leaf = true
end

function action_access(data)
    local fromtype = data["fromtype"] or ""
    if fromtype ~= "web" then
        return true
    end

    str = (data["name"] or "Unknown") .. "&" .. (data["from"] or "Unknown") .. "&" .. (data["privilege"] or "") .. "&" .. data["dir"] .. "&" .. data["state"]
    result = librpc.callapi("oltmib_accesslog_set_1", str)
    return result == "0"
end

function action_login()
    local from = luci.http.getenv("REMOTE_ADDR")
    local params = json.decode(luci.http.content()) or {}
    local sess = authapi.get_sess()
    if not sess then sess = authapi.do_auth(params) end
    if not sess then
        action_access({ name = params['username'], from=from, dir="1", state="0", fromtype = params['fromtype'] })
        luci.http.status(403, "Forbidden")
        return
    end
    if (sess['privilege'] and sess['privilege'] < 15) then
        action_access({ name = sess['user'], from = from, privilege = sess['privilege'], dir = "1", state= "0", fromtype = params['fromtype'] })
    else
        action_access({ name = sess['user'], from = from, privilege = sess['privilege'], dir = "1", state= "1", fromtype = params['fromtype'] })
    end

    local result = {roles = {{roleName = "Super Admin", value = "super"}}, username = sess['user'], token = sess['token'], realName = sess['realuser'] or sess['user'], privilege = sess['privilege'], desc = 'manager'}
    luci.http.prepare_content("application/json")
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = result})
end

function action_logout()
    local params = json.decode(luci.http.content()) or {}
    local privilege = params['privilege'] or 0
    local from = luci.http.getenv("REMOTE_ADDR")
    local stat = authapi.kill_auth(luci.http.getcookie("sysauth"))
    if stat and privilege >= 15 then action_access({ name = params['username'], from=from, dir="0", state="1", fromtype = params['fromtype'] }) end

    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
end

function handle_info()
    local sess = authapi.get_sess()
    if not sess then
        luci.http.status(404, "Not Found")
        return
    end
    luci.http.prepare_content("application/json")
    local sid = luci.sys.uniqueid(16)
    local result = {roles = {{roleName = "Super Admin", value = "super"}}, userId = sid, username = sess['user'], token = sess['token'], realName = sess['realuser'] or sess['user'], desc = 'manager', homePath = '', password = 'test', avatar = ''}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = result})
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "table is error")
        assert(type(params['name']) == "string" and string.len(params['name']) < 33, "name is a string / can't more than 32 bytes")

        local mtbl = {}
        mtbl['name'] = params['name']
        if params['oper'] ~= 'del' then
            if not (type(params['pwd']) == "string" and string.len(params['pwd']) < 33) then
                return luci.http.write_json({hdr = {code = 1000, message = "Password is a string / can't more than 32 bytes", type = "fail"}})
            else
                local account = {}
                if not params['privilege'] then account = srvdb.getaccount({name=params['name']}) end
                mtbl['privilege'] = params['privilege'] or account['privilege'] or 15
                mtbl['pwd'] = params['pwd']
                mtbl['oper'] = '1'
            end
        else
            mtbl['pwd'] = ''
            mtbl['oper'] = '2'
        end

        if not srvdb.setaccount(mtbl) then
            return luci.http.write_json({hdr = {code = 100, message = "Account edit error", type = "fail"}})
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local account = srvdb.getaccounttbl()
    local data = {data = account}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
