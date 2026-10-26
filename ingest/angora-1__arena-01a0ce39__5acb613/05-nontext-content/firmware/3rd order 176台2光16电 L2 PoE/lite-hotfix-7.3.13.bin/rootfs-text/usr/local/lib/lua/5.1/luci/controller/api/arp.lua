local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.arp", package.seeall)

function index()
    entry({"api", "arp"}, alias("api", "arp", "conf"), nil).hidden = true
    entry({"api", "arp", "conf"}, call("handle_config"), nil).leaf = true
    entry({"api", "arp", "info"}, call("handle_info"), nil).leaf = true
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['info']['ip']) == "string", "ip is error")
        assert(type(params['info']['mac']) == "string", "mac is error")

        local info = params['info']
        local oper = params['oper'] or ''
        local mac = mydb.mac_trans(info['mac'])
        local sarpdata = {}
        sarpdata['ip'] = info['ip']
        sarpdata['ifname'] = info['name']
        sarpdata['mac'] = info['mac']
        sarpdata['mac'] = string.sub(mac, 1, 4) .. '.' .. string.sub(mac, 5, 8) .. '.' .. string.sub(mac, 9, 12)
        if oper == "del" then sarpdata['oper'] = "2" end
        if not mydb.setsarp(sarpdata) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local sarptbl = mydb.getsarptbl()
    for _, sarp in ipairs(sarptbl) do
        local sarpdata = {}
        sarpdata['ip'] = sarp['ip']
        sarpdata['mac'] = sarp['mac']
        sarpdata['name'] = sarp['ifname']
        table.insert(destbl, sarpdata)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_info()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")

        local oper = params['oper'] or ''
        -- local info = params['info']
        -- local type = info['type']
        -- local args = info['args']
        if oper == "clear" then
            if not mydb.setarp( { oper = "2" } ) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local arptbl = mydb.getarptbl()
    for _, arp in ipairs(arptbl) do
        local arpdata = {}
        arpdata['id'] = 0   -- magic number
        arpdata['name'] = arp['ifname']
        arpdata['mac'] = arp['mac']
        arpdata['ip'] = arp['ip']
        arpdata['type'] = arp['type']
        table.insert(destbl, arpdata)
    end

    local data = {data = tools.array_check(destbl)}
    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
