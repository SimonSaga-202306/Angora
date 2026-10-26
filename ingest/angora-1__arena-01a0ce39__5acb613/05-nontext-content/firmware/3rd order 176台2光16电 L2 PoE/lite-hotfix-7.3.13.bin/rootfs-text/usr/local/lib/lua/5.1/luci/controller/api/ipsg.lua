local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.ipsg", package.seeall)

function index()
    entry({"api", "ipsg"}, alias("api", "ipsg", "port"), nil).hidden = true
    entry({"api", "ipsg", "port"}, call("handle_port"), nil).leaf = true
    entry({"api", "ipsg", "user"}, call("handle_user"), nil).leaf = true
    entry({"api", "ipsg", "info"}, call("handle_info"), nil).leaf = true
end

function handle_port()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['info']['verify_src']) == "boolean", "verify_source_enable is error")
        assert(type(params['info']['arp_check']) == "boolean", "arp_check_enable is error")

        local info = params['info']
        local portsgrp = params['ports']
        for _, pid in ipairs(portsgrp) do
            local nsmipsgifdata = mydb.getnsmipsgif( { ifx = tostring(pid) } )
            nsmipsgifdata['verify_source_enable'] = info['verify_src'] and "Enabled" or "Disabled"
            nsmipsgifdata['arp_check_enable'] = info['arp_check'] and "Enabled" or "Disabled"
            if not mydb.setnsmipsgif(nsmipsgifdata) then
                return luci.http.write_json({hdr = {code = 100, message = "Failed to modify port", type = "fail"}})
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local nsmipsgiftbl = mydb.getnsmipsgiftbl()
    for _, nsmipsgif in ipairs(nsmipsgiftbl) do
        local nsmipsgdata = {}
        nsmipsgdata['id'] = tonumber(nsmipsgif['ifx'])
        nsmipsgdata['name'] = nsmipsgif['name']
        nsmipsgdata['verify_src'] = nsmipsgif['verify_source_enable'] == 'Enabled'
        nsmipsgdata['arp_check'] = nsmipsgif['arp_check_enable'] == 'Enabled'
        table.insert(destbl, nsmipsgdata)
    end

    local data = {data = tools.array_check(destbl)}
    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_user()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['info']['id']) == "number", "id is error")
        assert(type(params['info']['vid']) == "number" and params['info']['vid'] > 0 and params['info']['vid'] <= 4094, "vid is error")

        local info = params['info']
        local oper = params['oper'] or ''
        if oper ~= "del" then
            local nsmipsguserdata = {}
            nsmipsguserdata['ifx'] = tostring(info['id'])
            nsmipsguserdata['name'] = ''
            nsmipsguserdata['vid'] = mydb.filter_vlan(tostring(info['vid']))
            nsmipsguserdata['ipstr'] = info['ip']
            nsmipsguserdata['mac'] = info['mac']
            nsmipsguserdata['type'] = info['type']
            if not mydb.setnsmipsguser(nsmipsguserdata) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        else
            local nsmipsgusertbl = mydb.getnsmipsgusertbl()
            for _, nsmipsguser in ipairs(nsmipsgusertbl) do
                if info['ip'] == nsmipsguser['ipstr'] and info['mac'] == nsmipsguser['mac'] then
                    nsmipsguser['oper'] = '2'
                    nsmipsguser['type'] = info['type']
                    if not mydb.setnsmipsguser(nsmipsguser) then
                        return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                    end
                end
            end
        end

       
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local nsmipsgusertbl = mydb.getnsmipsgusertbl()
    for _, nsmipsguser in ipairs(nsmipsgusertbl) do
        local nsmipsguserdata = {}
        nsmipsguserdata['id'] = tonumber(nsmipsguser['ifx'])
        nsmipsguserdata['name'] = nsmipsguser['name']
        nsmipsguserdata['vid'] = tonumber(nsmipsguser['vid'])
        nsmipsguserdata['ip'] = nsmipsguser['ipstr']
        nsmipsguserdata['mac'] = nsmipsguser['mac']
        nsmipsguserdata['lease'] = nsmipsguser['lease']
        nsmipsguserdata['type'] = nsmipsguser['type']
        table.insert(destbl, nsmipsguserdata)
    end

    local data = {data = tools.array_check(destbl)}
    return luci.http.write_json({hdr = {code = 0, message = 'ok', type = 'success'}, result = data})
end

function handle_info()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "GET" then
        local destbl = {}
        local id, name, type
        local nsmipsgiftbl = mydb.getnsmipsgiftbl()
        local nsmipsgusertbl = mydb.getnsmipsgusertbl()
        for _, nsmipsgif in ipairs(nsmipsgiftbl) do
            if nsmipsgif['verify_source_enable'] == 'Enabled' or nsmipsgif['arp_check_enable'] == 'Enabled' then
                id = tonumber(nsmipsgif['ifx'])
                name = nsmipsgif['name']
                if nsmipsgif['verify_source_enable'] == 'Enabled' and nsmipsgif['arp_check_enable'] == 'Enabled' then
                    type = 'IP/ARP'
                elseif nsmipsgif['verify_source_enable'] == 'Enabled' then
                    type = 'IP'
                else
                    type = 'ARP'
                end

                for _, nsmipsguser in ipairs(nsmipsgusertbl) do
                    if nsmipsgif['ifx'] == nsmipsguser['ifx'] then
                        local nsmipsgdata = {}
                        nsmipsgdata['id'] = id
                        nsmipsgdata['name'] = name
                        nsmipsgdata['type'] = type
                        nsmipsgdata['filter'] = 'Permit'
                        nsmipsgdata['ip'] = nsmipsguser['ipstr']
                        nsmipsgdata['mac'] = nsmipsguser['mac']
                        nsmipsgdata['vid'] = nsmipsguser['vid']
                        nsmipsgdata['origin'] = nsmipsguser['type']
                        table.insert(destbl, nsmipsgdata)
                    end
                end
                table.insert(destbl, {id = id, name = name, type = type, filter = 'Deny', ip = 'All', mac = 'All', vid = 'All'})
            end
        end

        local data = {data = tools.array_check(destbl)}
        return luci.http.write_json({hdr = {code = 0, message = 'ok', type = 'success'}, result = data})
    end
end
