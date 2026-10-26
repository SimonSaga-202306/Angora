local sauth = require "luci.sauth"
local srvdb = require "luci.controller.lib.srvdb"
local mydb = require "luci.mydb"

module("luci.authapi", package.seeall)

function get_sess()
    local sid = luci.http.getcookie("sysauth") or ''
    local sess = sauth.read(sid)
    --local token = luci.sys.uniqueid(16)
    --local sess = {user = "test", realuser = "test", token = token}
    return sess
end

function check_auth()
    local uri = luci.http.getenv('REQUEST_URI')
    local method = luci.http.getenv("REQUEST_METHOD")
    if uri == '/cgi-bin/luci/api/user/login' then return true end
    if string.match(uri, '/cgi%-bin/luci/api/sys/info') and method == "GET" then return true end
    if string.match(uri, '/cgi%-bin/luci/api/sys/customize_v5_x') and method == "GET" then return true end
    local sess = get_sess()
    if not sess then luci.http.status(401, "Unauthorized") end
    return sess
end

function do_auth(data)
    if not data['username'] then return nil end
    local account
    local privilege = 15
    local fs = require "nixio.fs"
    if fs.stat('/etc/pam.d/web') then
        os.execute("[ -e /tmp/pamhelper.txt ] && rm /tmp/pamhelper.txt")
        if os.execute('pamhelper -n web -u ' .. data['username'] .. ' -p ' .. data['password'] .. " 2>&1 > /dev/null") ~= 0 then return nil end

        local do_author = false
        if fs.stat('/tmp/aaa/authorization/web') then       -- web authorization enabled
            local author_form, level
            if fs.stat('/tmp/pamhelper.txt') then
                local env = io.popen("cat /tmp/pamhelper.txt")
                if env then
                    local l
                    while true do
                        l = env:read("*l")
                        if not l then break end
                        if string.match(l, "PRIV_LVL=") then level = tonumber(string.match(l, "=([^%s]+)")) end
                        if string.match(l, "AUTHOR_FORM=") then author_form = string.match(l, "=([^%s]+)") end
                    end
                    env:close()
                end
            end

            if author_form then
                privilege = level or 0
                do_author = true
            end
        end

        if not do_author then
            account = srvdb.getaccount({name=data['username']})
            privilege = account["privilege"] or privilege
        end
    else
        if not luci.sys.user.checkpasswd(data['username'], data['password']) then return nil end
        account = srvdb.getaccount({name=data['username']})
        privilege = account["privilege"] or privilege
    end

    local sid = luci.sys.uniqueid(16)
    local token = luci.sys.uniqueid(16)
    local sess = { user = data['username'], realuser = data['username'], token = token, privilege = privilege }
    sauth.reap()
    sauth.write(sid, sess)
    luci.http.header("Set-Cookie", "sysauth=" .. sid .. "; path=/cgi-bin/luci/")
    return sess
end

function kill_auth(sid)
    local stat, code, msg
    if sid then stat, code, msg = sauth.kill(sid) end
    luci.http.header("Set-Cookie", "sysauth=; path=/cgi-bin/luci/")
    return stat, code, msg
end
