require "bit"
require "luci.sys"
require "luci.tools.webadmin"
require "nixio.fs"
local json = require "luci.json"
local comdb = require "luci.controller.lib.comdb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.dhcpsrv", package.seeall)

function index()
    entry({"api", "dhcpsrv"}, alias("api", "dhcpsrv", "conf"), nil).hidden = true
    entry({"api", "dhcpsrv", "conf"}, call("handle_config"), nil).leaf = true
    entry({"api", "dhcpsrv", "info"}, call("handle_info"), nil).leaf = true
    entry({"api", "dhcpsrv", "lease"}, call("handle_lease"), nil).leaf = true
    entry({"api", "dhcpsrv", "subnet"}, call("handle_subnet"), nil).leaf = true
    entry({"api", "dhcpsrv", "host"}, call("handle_host"), nil).leaf = true
end

function dhcpauthor_trans(val)
    if not val then return "" end
    local trans = {}
    trans[""] = "none"
    trans["none"] = ""
    return trans[val] or val
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['admin_state']) == "boolean", "admin_state is error")
        assert(type(params['authoritative']) == "string", "authoritative is error")
        if params['srv_name'] and tools.range_hit(params['srv_name'], 0, 79) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end

        local conf = {}
        conf["status"] = tools.bool_trans(params['admin_state'])
	    conf["author"] = params['authoritative']
	    conf["defleasetm"] = tools.valfilter(params['lease_def'])
	    conf["servername"] = params['srv_name']
	    conf["dns"] = params['dns']

        local data = {}
        table.insert(data, "type=param;name=authoritative;")
        table.insert(data, "type=param;name=default-lease-time;")
        table.insert(data, "type=param;name=server-name;")
        table.insert(data, "type=opt;name=domain-name-servers;")
        if not comdb.dhcpd_delall("/dhcpd/global", data, 4) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        data = {}
        table.insert(data, "type=status;status=" .. conf["status"] .. ";")
        if conf["author"] ~= "none" then
            table.insert(data, "type=param;name=authoritative;val=" .. conf["author"] .. ";")
        end
        if conf['servername'] then table.insert(data, "type=param;name=server-name;val=" .. conf["servername"] .. ";") end
        if conf['dns'] then table.insert(data, "type=opt;name=domain-name-servers;val=" .. conf["dns"]..";") end
        if conf['defleasetm'] then table.insert(data, "type=param;name=default-lease-time;val=" .. conf["defleasetm"] .. ";") end
        if not comdb.dhcpd_setall("/dhcpd/global", data, 2) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local global = comdb.dhcpd_getall("/dhcpd/global", 2)[1]
    destbl['admin_state'] = tools.bool_trans(global['status'])
    destbl['authoritative'] = dhcpauthor_trans(global['authoritative'])
    destbl['lease_def'] = tonumber(global['default-lease-time'])
    destbl['srv_name'] = global['server-name']
    destbl['dns'] = global['domain-name-servers']

    local data = tools.array_check(destbl)
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_info()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "GET" then
        local destbl = {}
        local global = comdb.dhcpd_getall("/dhcpd/global", 2)[1]
        destbl['admin_state'] = tools.bool_trans(global['status'])
        destbl['state'] = false
        destbl['errmsg'] = luci.sys.exec("cat /tmp/dhcpd.test 2>>/dev/null")
        local status = luci.sys.exec("pidof dhcpd")
        if #status > 0 then
            destbl['state'] = true
        end

        local data = destbl
        luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
    end
end

function handle_lease()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "GET" then
        luci.sys.exec("perl /usr/bin/dhcp-lease-list.pl --parsable --lease /var/lib/dhcp/dhclient.leases > /tmp/dhcpd.webleases")
        local destbl = {}
        for line in io.lines("/tmp/dhcpd.webleases") do --MAC 00:0e:c6:c1:38:4a IP 2.2.2.100 HOSTNAME liulang-deb BEGIN 1970-01-01 03:15:40 END 1970-01-01 03:25:40 MANUFACTURER ASIX ELECTRONICS CORP.
            line = string.gsub(line, "[\r\n]+", "")
            local row = {}
            _, _, row["mac"], row["ip"], row["name"], row["start_tm"], row["end_tm"], row["manufacturer"] = string.find(line, "MAC (%S+) IP (%S+) HOSTNAME (%S+) BEGIN (.+) END (.+) MANUFACTURER (.+)")
            table.insert(destbl, row)
        end

        local data = {data = tools.array_check(destbl)}
        luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
    end
end

function handle_subnet()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")

        local info = params['info']
        local oper = params['oper'] or ""
        local conf = {}
        conf["prefix"] = info['prefix']
	    conf["startip"] = info['start_ip']
	    conf["endip"] = info['end_ip']
	    conf["gateway"] = info['gateway']
	    conf["dns"] = info['dns']

        local data = {}
        table.insert(data, "type=subnet;prefix=" .. conf["prefix"] .. ";")
        if not comdb.dhcpd_delall("/dhcpd/subnet", data, 2) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        if oper ~= "del" then
            if not conf["prefix"] or conf["prefix"] == "" then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end

            data = {}
            table.insert(data, "type=subnet;prefix=".. conf["prefix"]..";")
            if conf["startip"] and conf["startip"] ~= "" and conf["endip"] and conf["endip"] ~= "" then
                table.insert(data, "type=range;subnet=" .. conf["prefix"] .. ";startip="..conf["startip"] .. ";endip=" .. conf["endip"] .. ";")
            end
            if conf["gateway"] and conf["gateway"] ~= "" then
                table.insert(data, "type=opt;subnet=" .. conf["prefix"] .. ";name=routers;val=" .. conf["gateway"] .. ";")
            end
            if conf['dns'] and conf["dns"] ~= "" then
                table.insert(data, "type=opt;subnet=".. conf["prefix"] .. ";name=domain-name-servers;val=" .. conf["dns"] .. ";")
            end
            if not comdb.dhcpd_setall("/dhcpd/subnet", data, 4) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local subnettbl = comdb.dhcpd_getall("/dhcpd/subnet", 4)
    for _, subnet in ipairs(subnettbl) do
        local row = {}
        row['prefix'] = subnet['prefix']
        row['start_ip'] = subnet['startip']
        row['end_ip'] = subnet['endip']
        row['gateway'] = subnet['routers']
        row['dns'] = subnet['domain-name-servers']
        table.insert(destbl, row)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_host()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['info']['name']) == "string", "name is error")

        local info = params['info']
        local oper = params['oper'] or ""
        local conf = {}
        conf["name"] = info['name']
	    conf["type"] = info['type']
	    conf["mac"] = info['mac']
	    conf["ip"] = info['ip']

        local data = {}
        table.insert(data, "type=host;name=" .. conf["name"] .. ";")
        if not comdb.dhcpd_delall("/dhcpd/host", data, 2) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        if oper ~= "del" then
            assert(type(info['mac']) == "string", "mac is error")
            assert(type(info['ip']) == "string", "ip is error")
            assert(type(info['type']) == "string", "type is error")
            if conf["name"] == "" or conf["mac"] == "" then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
            if conf["type"] == "static" and conf["ip"] == "" then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end

            data = {}
            table.insert(data, "type=host;name=" .. conf["name"] .. ";subtype=" .. conf["type"]..";mac=" .. conf["mac"] .. ";ip=" .. conf["ip"] .. ";")
            if not comdb.dhcpd_addall("/dhcpd/host", data, 4) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local hosttbl = comdb.dhcpd_getall("/dhcpd/host", 4)
    for _, host in ipairs(hosttbl) do
        local row = {}
        row['name'] = host['name']
        row['type'] = host['type']
        row['mac'] = host['mac']
        row['ip'] = host['ip']
        table.insert(destbl, row)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
