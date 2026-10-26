local json = require "luci.json"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.dns", package.seeall)

function index()
    entry({"api", "dns"}, alias("api", "dns", "server"), nil).hidden = true
    entry({"api", "dns", "server"}, call("handle_server"), nil).leaf = true
    entry({"api", "dns", "domain"}, call("handle_domain"), nil).leaf = true
    entry({"api", "dns", "host"}, call("handle_host"), nil).leaf = true
end

function dnstype_trans(data)
    local tbl = {}
    tbl["0"] = "static"
    tbl["1"] = "dynamic"
    tbl["static"] = "0"
    tbl["dynamic"] = "1"

    return tbl[tostring(data)] or ""
end

function getdnservertbl()
    local tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_dnserver_getn_1", str)
        _, _, _, ip, ipv6, mtype, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
        if (result == "0") then
            local row = {}
            row['type'] = dnstype_trans(mtype)
            row['ip'] = ip
            row['ipv6'] = ipv6
            table.insert(tbl, row)
        end
    end

    return tbl
end

function setdnserver(data, oper)
    str = "&" .. (data['ip'] or "") .. "&" .. (data['ipv6'] or "") .. "&" .. dnstype_trans(data['type']) .. "&&"  .. (oper or "")
    result = librpc.callapi("oltmib_dnserver_set_1", str)
    return result == "0"
end

function getdnsdomaintbl()
    local tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_dnsdomain_getn_1", str)
        _, _, name, ip, ipv6, mtype, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
        if (result == "0") then
            local row = {}
            row['name'] = name
            row['type'] = dnstype_trans(mtype)
            table.insert(tbl, row)
        end
    end

    return tbl
end

function setdnsdomain(data, oper)
    str = (data['name'] or "") .. "&&&" .. dnstype_trans(data['type']) .. "&&"  .. (oper or "")
    result = librpc.callapi("oltmib_dnsdomain_set_1", str)
    return result == "0"
end

function getdnshosttbl()
    local tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_dnshost_getn_1", str)
        _, _, name, ip, ipv6, mtype, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
        if (result == "0") then
            local row = {}
            row['name'] = name
            row['ip'] = ip
            row['ipv6'] = ipv6
            table.insert(tbl, row)
        end
    end

    return tbl
end

function getdnshost(data)
    local tbl = {}
    result = "0"
    str = (data["name"] or "") .. "&&&&&&"
    str = librpc.callapi("oltmib_dnshost_get_1", str)
    _, _, name, ip, ipv6, mtype, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
    if (result == "0") then
        tbl['name'] = name
        tbl['ip'] = ip
        tbl['ipv6'] = ipv6
    end

    return tbl
end

function setdnshost(data, oper)
    str = (data['name'] or "") .. "&" .. (data['ip'] or '') .. "&" .. (data['ipv6'] or '') .. "&&&"  .. (oper or "")
    result = librpc.callapi("oltmib_dnshost_set_1", str)
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

        if oper == "del" then
            oper = 2
        end

        for _, server in ipairs(info) do
            local dnsdata = {}
            dnsdata['type'] = server['type']
            if (server['ip'] and string.match(server['ip'], ":")) then
                dnsdata['ipv6'] = server['ip']
            else
                dnsdata['ip'] = server['ip']
            end

            if not setdnserver(dnsdata, oper) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local dnservertbl = getdnservertbl()
    for _, server in ipairs(dnservertbl) do
        local row = {}
        row['type'] = server['type']
        if (server['ipv6'] and server['ipv6'] ~= "") then
            row['ip'] = server['ipv6']
        elseif (server['ip'] and server['ip'] ~= "") then
            row['ip'] = server['ip']
        else
            row['ip'] = ""
        end

        table.insert(destbl, row)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_domain()
    luci.http.prepare_content("application/json")

    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")

        local info = params['info']
        local oper = params['oper'] or ''

        if (oper == "del") then
            oper = 2
        end

        for _, domain in ipairs(info) do
            local dnsdata = {}
            dnsdata['name'] = domain['name']
            dnsdata['type'] = domain['type']

            if not setdnsdomain(dnsdata, oper) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local domaintbl = getdnsdomaintbl()
    for _, domain in ipairs(domaintbl) do
        local row = {}
        row['name'] = domain['name']
        row['type'] = domain['type']
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

        local info = params['info']
        local oper = params['oper'] or ''

        if (oper == "del") then
            oper = 2
        end

        for _, host in ipairs(info) do
            local dnsdata = {}
            dnsdata['name'] = host['name']
            dnsdata['ip'] = host['ip']
            dnsdata['ipv6'] = host['ipv6']

            if not setdnshost(dnsdata, oper) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end

            if oper ~= 2 then
                local dnshost = getdnshost(dnsdata)
                if next(dnshost) then
                    dnsdata['ip'] = (dnshost['ip'] ~= "" and host['ip'] == "") and dnshost['ip'] or ""
                    dnsdata['ipv6'] = (dnshost['ipv6'] ~= "" and host['ipv6'] == "") and dnshost['ipv6'] or ""

                    if dnsdata['ip'] ~= "" or dnsdata['ipv6'] ~= "" then
                        if not setdnshost(dnsdata, 2) then
                            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                        end
                    end
                end
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local hosttbl = getdnshosttbl()
    for _, host in ipairs(hosttbl) do
        local row = {}
        row['name'] = host['name']
        row['ip'] = host['ip']
        row['ipv6'] = host['ipv6']
        table.insert(destbl, row)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
