local sauth = require "luci.sauth"
local authapi = require "luci.authapi"
local json = require "luci.json"
local mydb = require "luci.mydb"
local srvdb = require "luci.controller.lib.srvdb"
local tools = require "luci.controller.lib.tools"
local nixio = require "nixio"
local fs = require "nixio.fs"

module("luci.controller.api.sys", package.seeall)

function index()
    entry({"api", "sys"}, alias("api", "sys", "action"), nil).hidden = true
    entry({"api", "sys", "action"}, call("handle_action"), nil).leaf = true
    entry({"api", "sys", "info"}, call("handle_info"), nil).leaf = true
    entry({"api", "sys", "flash"}, call("handle_flash"), nil).leaf = true
    entry({"api", "sys", "perf"}, call("handle_perf"), nil).leaf = true
    entry({"api", "sys", "conf"}, call("handle_config"), nil).leaf = true
    entry({"api", "sys", "cap"}, call("handle_capability"), nil).leaf = true
    entry({"api", "sys", "customize_v5_x"}, call("handle_customize_v5_x"), nil).leaf = true
    entry({"api", "sys", "alert"}, call("handle_alert"), nil).leaf = true
end

function handle_action()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['oper']) == "string", "oper is error")

        if params['oper'] == 'reboot' then 
            luci.http.write_json({hdr = {code = 0, message = "reboot", type = "success"}})
            os.execute('touch /var/log/warmstart')
            luci.sys.reboot()
        elseif params['oper'] == 'save' then
            srvdb.writecfg()
            luci.http.write_json({hdr = {code = 0, message = "save", type = "success"}})
        elseif params['oper'] == 'reset' then
            luci.sys.exec("cd /data && cp -a startup.def startup.conf ")
            luci.http.write_json({hdr = {code = 0, message = "reset", type = "success"}})
        else
            luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
        end
    end
end

function handle_info()
    luci.http.prepare_content("application/json")
    local info = srvdb.getsysinfo()
    local cmdline = luci.sys.exec("cat /proc/cmdline 2>>/dev/null")
    local data = {}
    data['rid'] = string.match(cmdline, "ID=([%w_%-]+)")
    data['id'] = info['pid']
    data['sn'] = info['psn']
    data['mac'] = info['mac']
    data['hwver'] = info['hwver']
    data['swver'] = info['swver']
    data['releasedate'] = info['swdate']
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_flash()
    luci.http.prepare_content("application/json")
    local linestr = luci.sys.exec("df -h | grep '/$' | head -1")
    local args = {}
    for v in string.gmatch(linestr, "[%S]+") do table.insert(args, v) end
    local data = {name = args[1], unit = {string.match(args[2], "[a-zA-Z]+")}, data = {{name = 'Avail', value = tonumber(string.match(args[4], "%d+"))}, {name = 'Used', value = tonumber(string.match(args[3], "%d+"))}}};
    luci.http.write_json({hdr = {code = 0, message = 'ok', type = 'success'}, result = data})
end

function mem_unittrans(unit)
    local row = {}
    row["B"] = "Byte"
    row["K"] = "KiB"
    row["M"] = "MiB"
    return unit and row[unit] or "B"
end

function mem_unit2num(unit)
    local row = {}
    row["B"] = 1
    row["K"] = 1024
    row["M"] = 1024 * 1024
    return unit and row[unit] or 1
end

local file_resource = '/tmp/resource.txt'
function handle_perf()
    luci.http.prepare_content("application/json")
    local data = {cpu = {}, memory = {}}
    local lines = {}
    local fd = io.open(file_resource, "r")
    if fd then
        while true do
            local linestr = fd:read()
            if not linestr then
                break
            else
                table.insert(lines, linestr)
            end
        end

        fd:close()
    end

    local cpu_idle = 0
    local cpu_num = 1
    local mem_free = 0
    local uptime, updays, uphours, upmins
    _, _, cpu_num, cpu_idle, data["cpu"]["1min"], data["cpu"]["5min"], data["cpu"]["15min"] = string.find(lines[1] or "", string.rep("([%d%.]+) ", 5))
    _, _, data["memory"]["total"], mem_free = string.find(lines[2] or "", "([%d%.]+) ([%d%.]+)")
    _, _, uptime = string.find(lines[3] or "", "([%d%.]+)")
    cpu_num = tonumber(cpu_num) or 1
    cpu_num = (cpu_num == 0) and 1 or cpu_num
    data["cpu"]["0"] = tonumber(cpu_idle)
    data["cpu"]["1min"] = (tonumber(data["cpu"]["1min"]) or 0) * 100 / cpu_num
    data["cpu"]["5min"] = (tonumber(data["cpu"]["5min"]) or 0) * 100 / cpu_num
    data["cpu"]["15min"] = (tonumber(data["cpu"]["15min"]) or 0) * 100 / cpu_num
    data["memory"]["total"] = tonumber(data["memory"]["total"]) or 0
    data["memory"]["used"] = data["memory"]["total"] - (tonumber(mem_free) or 0)
    data["memory"]["unit"] = "KiB"

    if data["cpu"]["1min"] > 100 then data["cpu"]["1min"] = 100 end
    if data["cpu"]["5min"] > 100 then data["cpu"]["5min"] = 100 end
    if data["cpu"]["15min"] > 100 then data["cpu"]["15min"] = 100 end

    uptime = math.floor(tonumber(uptime) or 0)
    updays = math.floor(uptime / (60 * 60 * 24))
    uphours = math.floor(uptime / (60 * 60)) % 24
    upmins = math.floor(uptime / 60) % 60
    data["uptime"] = ((updays == 0) and "" or (updays .. "d ")) .. string.format("%02d:%02d", uphours, upmins)
    data["time"] = os.date("%H:%M:%S", os.time())

    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function getloginfo()
    local tbl = {}
    str = librpc.callapi("oltmib_sysloginfo_get_1", "")
    _, _, console_ability, console, monitor_ability, monitor, terminal_monitor, trap_ability, trap, interval, burst, buffer, web_buffer, msg, oper, result = string.find(str, string.rep("(.-)&", 13) .. "(.*)")
    if (result == "0") then
        tbl['web_buffer'] = web_buffer
    end

    return tbl
end

function setloginfo(data)
    result = librpc.callapi("oltmib_sysloginfo_set_1", "&&&&&&&&&&" .. data['web_buffer'])
    return result == "0"
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        -- ['timeout']
        if params['hostname'] and type(params['hostname']) == "string" and #params['hostname'] < 64 then
            local sysdata = {}
            sysdata['hostname'] = params['hostname']
            srvdb.setsysinfo(sysdata)
        end

        if params['telnet'] ~= nil then
            local telnet = {}
            telnet['name'] = 'Telnet Server'
            telnet['enabled'] = params['telnet'] and 1 or 0
            srvdb.setsvc(telnet)
        end

        if params['ssh'] ~= nil then
            local ssh = {} 
            ssh['name'] = 'SSH Server'
            ssh['enabled'] = params['ssh'] and 1 or 0
            srvdb.setsvc(ssh)
        end

        if params['http'] ~= nil or params['https'] ~= nil then
            local web = {}
            local http, https = 0, 0
            local svctbl = srvdb.getsvctbl()
            for _, srv in ipairs(svctbl) do
                if srv['name'] == 'HTTP Server' then
                    http = srv['enabled']
                end
                if srv['name'] == "HTTPS Server" then
                    https = srv['enabled']
                end
            end

            if params['http'] ~= nil then
                http = params['http'] and 1 or 0
            end
            if params['https'] ~= nil then
                https = params['https'] and 1 or 0
            end
            web['name'] = 'Web Server'
            web['status'] = srvdb.webstatus_pack(http, https)
            srvdb.setsvc(web)
        end

        if params['dyinggasp'] ~= nil then
            local dyinggaspcap = mydb.getdyinggaspcap()
            if dyinggaspcap ~= 0 then
                local dyinggasp = mydb.getdyinggasp()
                dyinggasp['status'] = params['dyinggasp'] and '1' or '0'
                mydb.setdyinggasp(dyinggasp)
            end
        end

        if params['log_cap'] ~= nil then
            if not tools.range_hit(params['log_cap'], 20, 200) then
                luci.http.write_json({hdr = {code = 100, message = "log_cap is error!", type = "fail"}})
            end
            setloginfo( {web_buffer=params['log_cap']} )
        end

        local mgmtinfo = params['mgmtinfo'] or {}
        if mgmtinfo['vid'] ~= nil then
            local mgmtdata = {}
            mgmtdata['VID'] = tostring(mgmtinfo['vid'])
            mgmtdata['ipv4type'] = mgmtinfo['ipv4type']
            mgmtdata['IP'] = mgmtinfo['ipv4addr'] or ''
            mgmtdata['Mask'] = mgmtinfo['ipv4mask'] or ''
            mgmtdata['Gateway'] = mgmtinfo['ipv4gw'] or ''
            mgmtdata['ipv6type'] = mgmtinfo['ipv6type']
            mgmtdata['IPv6'] = mgmtinfo['ipv6addr'] or ''
            mgmtdata['Prefix6'] = mgmtinfo['ipv6prefixlen'] or ''
            mgmtdata['Gateway6'] = mgmtinfo['ipv6gw'] or ''
            mydb.setmgmtip(mgmtdata, "")
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local sysinfo = srvdb.getsysinfo()
    destbl['hostname'] = sysinfo['hostname']
    destbl['timeout'] = 600                    -- magic number 

    local dyinggaspcap = mydb.getdyinggaspcap()
    local dyinggasp = mydb.getdyinggasp()
    if dyinggaspcap ~= 0 and tonumber(dyinggasp['status']) ~= 0 then
        destbl['dyinggasp'] = true
    else
        destbl['dyinggasp'] = false
    end

    local svctbl = srvdb.getsvctbl()
    for _, v in ipairs(svctbl) do
        if v['name'] == "Telnet Server" then
            destbl['telnet'] = v['enabled'] ~= 0
        elseif v['name'] == "SSH Server" then
            destbl['ssh'] = v['enabled'] ~= 0
        elseif v['name'] == "HTTP Server" then
            destbl['http'] = v['enabled'] ~= 0
        else 
            destbl['https'] = v['enabled'] ~= 0
        end
    end

    local loginfo = getloginfo()
    destbl['log_cap'] = tonumber(loginfo['web_buffer'])

    local mgmtlist = mydb.getmgmtip()
    local mgmtinfo = {}
    destbl['mgmtip'] = false
    if mgmtlist['VID'] ~= '' and mgmtlist['VID'] ~= '0' then
        destbl['mgmtip'] = true
        mgmtinfo['vid'] = tonumber(mgmtlist['VID'])
        mgmtinfo['ipv4type'] = mgmtlist['ipv4type']
        mgmtinfo['ipv4addr'] = mgmtlist['IP']
        mgmtinfo['ipv4mask'] = mgmtlist['Mask']
        mgmtinfo['ipv4gw'] = mgmtlist['Gateway']
        mgmtinfo['ipv6type'] = mgmtlist['ipv6type']
        mgmtinfo['ipv6addr'] = mgmtlist['IPv6']
        mgmtinfo['ipv6prefixlen'] = mgmtlist['Prefix6'] ~= '' and tonumber(mgmtlist['Prefix6']) or 0
        mgmtinfo['ipv6gw'] = mgmtlist['Gateway6']
        destbl['mgmtinfo'] = mgmtinfo
    end
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = destbl})
end

function handle_capability()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "GET" then
        local data = {}
        data['l3'] = mydb.getdevcapbool("PROD_UD_CLASS", "l3_support") ~= 0
        data['poe'] = mydb.getdevcapbool("PROD_UD_CLASS", "poe") ~= 0
        data['ioctl'] = mydb.getdevcapbool("PROD_UD_CLASS", "io_support") ~= 0
        data['sdsm'] = mydb.getdevcapbool("PROD_UD_CLASS", "sds_support") ~= 0
        data['dhcpd'] = mydb.getdevcapbool("PROD_UD_CLASS", "dhcp_server") ~= 0
        data['dyinggasp'] = mydb.getdyinggaspcap() ~= 0
        data['transceiver'] = mydb.getdevcapbool("PROD_UD_CLASS", "optic_support") ~= 0
        data['dot1x'] = mydb.getdevcapbool("PROD_UD_CLASS", "dot1x") ~= 0
        data['erps'] = mydb.getdevcapbool("PROD_UD_CLASS", "erps") ~= 0
        data['pon'] = mydb.getdevcapbool("PROD_UD_CLASS", "pon") ~= 0
        data['acl'] = mydb.getdevcapbool("PROD_UD_CLASS", "acl_support") ~= 0
        data['dhcpsnp'] = mydb.getdevcapbool("PROD_UD_CLASS", "dhcpsnooping_support") ~= 0
        data['ipsg'] = mydb.getdevcapbool("PROD_UD_CLASS", "ipsourceguard_support") ~= 0
        data['mstp'] = mydb.getdevcapbool("PROD_UD_CLASS", "mstp_support") ~= 0
        data['psec'] = mydb.getdevcapbool("PROD_UD_CLASS", "portsecurity_support") ~= 0
        data['qinq'] = mydb.getdevcapbool("PROD_UD_CLASS", "qinq_support") ~= 0
        data['qos'] = {}
        data['qos']['policy'] = mydb.getdevcapbool("PROD_UD_CLASS", "qos.policy_support") ~= 0
        data['qos']['max_queue'] = mydb.getdevcapint("PROD_UD_CLASS", "qos.max_queue") or 7
        data['qos']['min_queue'] = mydb.getdevcapint("PROD_UD_CLASS", "qos.min_queue") or 0
        data['qos']['wrr_max_weight'] = mydb.getdevcapint("PROD_UD_CLASS", "qos.wrr_max_weight") or 32
        data['qos']['wrr_min_weight'] = mydb.getdevcapint("PROD_UD_CLASS", "qos.wrr_min_weight") or 0
        data['lpdet'] = mydb.getdevcapbool("PROD_UD_CLASS", "loopdetect") ~= 0
        data['cabledet'] = mydb.getdevcapbool("PROD_UD_CLASS", "cabledetect") ~= 0
        data['https'] = mydb.getdevcapbool("PROD_UD_CLASS", "https_support") ~= 0

        data['platform'] = mydb.getdevplatform()
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
    end
end

function handle_customize_v5_x()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "GET" then
        local destbl = {}
        destbl['version'] = mydb.getlibconfstr("/data/customize/config", "version", nil)
        destbl['support_web_zh'] = mydb.getlibconfbool("/data/customize/config", "support_web_zh", nil)
        if (type(destbl['support_web_zh']) == "number") then destbl['support_web_zh'] = tools.bool_trans(destbl['support_web_zh']) end
        destbl['lang_label_def'] = mydb.getlibconfstr("/data/customize/config", "lang_label_def", nil)
        destbl['lang_label_cust'] = mydb.getlibconfstr("/data/customize/config", "lang_label_cust", nil)
        destbl['contact'] = mydb.getlibconfstr("/data/customize/config", "contact", nil)
        destbl['location'] = mydb.getlibconfstr("/data/customize/config", "location", nil)
        destbl['vendor_oid'] = mydb.getlibconfint("/data/customize/config", "vendor_oid", nil)
        destbl['product_name'] = mydb.getlibconfstr("/data/customize/config", "product_name", nil)
        destbl['web_title'] = mydb.getlibconfstr("/data/customize/config", "web_title", nil)
        destbl['authhtm'] = mydb.getlibconfstr("/data/customize/config", "authhtm", "sysauth")
        destbl['logo_pos'] = mydb.getlibconfstr("/data/customize/config", "logo_pos", nil)
        destbl['sys_desc'] = mydb.getlibconfstr("/data/customize/config", "sys_desc", nil)

        local data = tools.array_check(destbl)
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
    end
end

function getalert()
    local row = {}
    str = librpc.callapi("oltmib_alert_get_1", "")
    _, _, passwd_det_enable, passwd_det_state, ip_det_enable, ip_det_state, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
    if result == "0" then
        row['passwd_det_enable'] = passwd_det_enable
        row['passwd_det_state'] = passwd_det_state
        row['ip_det_enable'] = ip_det_enable
        row['ip_det_state'] = ip_det_state
    end
    return row
end

function handle_alert()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "GET" then
        local destbl = {}
        local alert = getalert()
        destbl['passwd_det_enable'] = tools.bool_trans(alert['passwd_det_enable'])
        destbl['passwd_det_state'] = tools.bool_trans(alert['passwd_det_state'])
        destbl['ip_det_enable'] = tools.bool_trans(alert['ip_det_enable'])
        destbl['ip_det_state'] = tools.bool_trans(alert['ip_det_state'])

        local data = tools.array_check(destbl)
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
    end
end
