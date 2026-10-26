local sys = require "luci.sys"
local fs = require "nixio.fs"
local json = require "luci.json"
local srvdb = require "luci.controller.lib.srvdb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.time", package.seeall)

function index()
    entry({"api", "time"}, alias("api", "stp", "zoneinfo"), nil).hidden = true
    entry({"api", "time", "zoneinfo"}, call("handle_zoneinfo"), nil).leaf = true
    entry({"api", "time", "conf"}, call("handle_config"), nil).leaf = true
    entry({"api", "time", "info"}, call("handle_info"), nil).leaf = true
end

function handle_zoneinfo()
    luci.http.prepare_content("application/json")
    local mtbl = srvdb.getzonetbl()
    local data = {data = mtbl}
    return luci.http.write_json({hdr = {code = 0, message = 'ok', type = 'success'}, result = data})
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == 'table', "params is error")

        if params['zone'] ~= nil or params['date'] ~= nil or params['time'] ~= nil or params['ntp_srv'] ~= nil or params['ntp_ipv6srv'] ~= nil or params['ntp_hostsrv'] ~= nil then
            local ntbl = {}
            local ntp = srvdb.getntp()
            ntbl['date'] = params['date']
            ntbl['time'] = params['time']
            ntbl['zone'] = params['zone'] or ntp['zone']
            ntbl['ip'] = params['ntp_srv'] or ntp['ip']
            ntbl['ipv6'] = params['ntp_ipv6srv'] or ntp['ipv6']
            ntbl['host'] = params['ntp_hostsrv'] or ntp['host']
            srvdb.setntp({zone = "UTC", ip = ntp['ip'], ipv6 = ntp['ipv6'], host = ntp['host']})
            if not srvdb.setntp(ntbl) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        end
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local ntp = srvdb.getntp()
    local mtbl = {}
    mtbl['zone'] = ntp['zone']
    mtbl['date'] = ntp['date']
    mtbl['time'] = ntp['time']
    mtbl['ntp_srv'] = ntp['ip']
    mtbl['ntp_ipv6srv'] = ntp['ipv6']
    mtbl['ntp_hostsrv'] = ntp['host']
    if (ntp['state'] ~= "0") then
        mtbl['sysinfo'] = {}
        mtbl['sysinfo']['sync'] = ntp['sync']
        mtbl['sysinfo']['stratum'] = tonumber(ntp['stratum'])
        mtbl['sysinfo']['referid'] = ntp['referid']
        mtbl['sysinfo']['refertm'] = ntp['refertm']
        mtbl['sysinfo']['log2_precision'] = tonumber(ntp['log2_precision'])
        mtbl['sysinfo']['root_delay'] = tonumber(ntp['root_delay'])
        mtbl['sysinfo']['root_dispersion'] = tonumber(ntp['root_dispersion'])
    end

    local data = mtbl
    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_info()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "GET" then
        local mtbl = {}
        local ntp = srvdb.getntp()
        if (ntp['ip'] ~= "" or ntp['ipv6'] ~= "" or ntp['host'] ~= "") then
            local log = io.popen("ntpq -pn | awk 'NR > 2'")
            if log then
                while true do
                    local tbl = {}
                    local l = log:read("*l")
                    if not l then break end
                    -- Example: *192.168.1.100 ( .LOCL.           1 u   63   64    3    0.928   -5.625   2.841
                    -- Delete the " ( " in remote
                    table.insert(tbl, string.match(l, "%S+") or "")
                    l = string.sub(l, 17)
                    for s in string.gmatch(l, "%S+") do table.insert(tbl, s) end

                    if #tbl == 10 then
                        table.insert(mtbl, { srv = tbl[1], referid = tbl[2], stratum = tbl[3], type = tbl[4], when = tbl[5],
                                poll = tbl[6], reach = tbl[7], delay = tbl[8], offset = tbl[9], jitter = tbl[10] })
                    end
                end
                log:close()
            end
        end

        local data = tools.array_check(mtbl)
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = {data = data}})
    end
end
