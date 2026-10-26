local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.snmp", package.seeall)

function index()
    entry({"api", "snmp"}, alias("api", "snmp", "conf"), nil).hidden = true
    entry({"api", "snmp", "conf"}, call("handle_config"), nil).leaf = true
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv('REQUEST_METHOD') == 'POST' then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['version']) == "number", "version is error")

        if params['community'] and not tools.range_hit(#params['community'], 1, 31) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end

        if params['encrypt_pwd'] and not tools.range_hit(#params['encrypt_pwd'], 8, 31) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end

        if params['auth_pwd'] and not tools.range_hit(#params['auth_pwd'], 8, 31) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end

        if params['hosts'] and type(params['hosts']) ~= "table" then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end

        local communitytbl = mydb.getsnmpcommunitytable()
        for _, community in pairs(communitytbl) do
            mydb.setsnmpcommunity(community, 2)
        end

        local grouptable = mydb.getsnmpgrouptable()
        for _, group in ipairs(grouptable) do
            mydb.setsnmpgroup(group, 2)
        end

        if params['community'] then     -- snmp version equal to 2 or 3
            if params['version'] == 3 then
                local authpwd = params['auth_pwd'] or ''
                local privpwd = params['encrypt_pwd'] or ''
                local sec_model = "authPriv"
                if authpwd ~= '' and privpwd ~= '' then
                    sec_model = "authPriv"
                elseif authpwd ~= '' then
                    sec_model = "authNoPriv"
                else
                    sec_model = "noAuthNoPriv"
                end

                -- add group
                local group = {name = params['community'], ver = "v3", sec_model = sec_model, rview = "all", wview = "all"}
                if not mydb.setsnmpgroup(group, 1) then
                    return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                end

                if sec_model == "authPriv" then
                    -- add user
                    local user = {name = params['community'], group = group['name'], authtype = "MD5", authpass = authpwd, enctype = "DES", encpass = privpwd}
                    if not mydb.setsnmpuser(user, 1) then
                        return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                    end

                    -- add ip
                    local host = {ver = "v3", user = user['name'], send_inform = "Traps", sec_model = sec_model}
                    for _, ipstr in ipairs(params['hosts'] or {}) do
                        if ipstr ~= "" then
                            host['family'] = string.match(ipstr, ":") and "IPv6" or "IPv4"
                            host['ipstr'] = ipstr
                            if not mydb.setsnmphost(host, 1) then
                                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                            end
                        end
                    end
                end
            else
                local community = {name = params['community'], type = "Read-write"}
                if not mydb.setsnmpcommunity(community, 1) then
                    return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                end
                local host = {ver = "v2c", user = community['name'], send_inform = "Traps", sec_model = "noAuthNoPriv"}
                for _, ipstr in ipairs(params['hosts'] or {}) do
                    if ipstr ~= "" then
                        host['family'] = string.match(ipstr, ":") and "IPv6" or "IPv4"
                        host['ipstr'] = ipstr
                        if not mydb.setsnmphost(host, 1) then
                            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                        end
                    end
                end
            end
        end
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})    
    end

    local destbl = {}
    destbl['location'] = ""
    destbl['hosts'] = {}
    local grouptbl = mydb.getsnmpgrouptable()
    if next(grouptbl) then
        destbl['version'] = grouptbl[1]['ver']
        destbl['community'] = grouptbl[1]['name'] or ''
        if destbl['version'] == "v3" then
            destbl['trap_community'] = destbl['community']
            local usertbl = mydb.getsnmpusertable()
            for _, user in ipairs(usertbl) do
                if user['name'] == destbl['trap_community'] then
                    destbl['auth_pwd'] = user['authpass']
                    destbl['encrypt_pwd'] = user['encpass']
                    break
                end
            end
        end
    end

    local hosttbl = mydb.getsnmphosttable()
    for _, host in ipairs(hosttbl) do
        if host['user'] ~= '' and host['user'] == destbl['community'] and host['ipstr'] ~= '' and host['send_inform'] == "Traps" and host['ver'] == destbl['version'] then
            table.insert(destbl['hosts'], host['ipstr'])
        end
    end

    destbl['version'] = tonumber(string.match(destbl['version'] or '0', "%d"))
    destbl['hosts'] = tools.array_check(destbl['hosts'])

    local data = tools.array_check(destbl)
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
