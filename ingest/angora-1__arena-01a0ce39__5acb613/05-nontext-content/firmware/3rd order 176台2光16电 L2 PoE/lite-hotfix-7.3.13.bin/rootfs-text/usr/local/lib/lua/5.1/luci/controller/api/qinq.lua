local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.qinq", package.seeall)

function index()
    entry({"api", "qinq"}, alias("api", "qinq", "conf"), nil).hidden = true
    entry({"api", "qinq", "conf"}, call("handle_config"), nil).leaf = true
    entry({"api", "qinq", "port"}, call("handle_port"), nil).leaf = true
    entry({"api", "qinq", "info"}, call("handle_info"), nil).leaf = true
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv('REQUEST_METHOD') == 'POST' then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['info']['name']) == "string" and #params['info']['name'] <= 32, "name is error")

        if params['info']['name'] == "" then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        local info = params['info']
        local rules = info['rules'] or {}
        local oper = params['oper'] or ''
        local vlanvpn = {}
        vlanvpn['name'] = info['name']
        vlanvpn['rule'] = ''
        vlanvpn['oper'] = '2'
        mydb.setvlanvpn(vlanvpn)

        if oper ~= "del" then
            vlanvpn['oper'] = '1'
            for _, rule in ipairs(rules) do
                if rule['cvlanlist'] and rule['cvlanlist'] ~= '' and rule['svlan'] and rule['svlan'] ~= '' then
                    vlanvpn['rule'] = vlanvpn['rule']  .. rule['svlan'] .. ":" .. rule['cvlanlist'] .. ";"
                end
            end

            if not mydb.setvlanvpn(vlanvpn) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})    
    end

    local destbl = {}
    local vlanvpntbl = mydb.getvlanvpntbl()
    for _, vpn in ipairs(vlanvpntbl) do
        local row = {}
        row["name"] = vpn['name']
        row['rules'] = {}
        for cvlan, svlan in string.gmatch(vpn['rule'], "cvlan (%S+) svlan (%d+)\n") do
            table.insert(row['rules'], { cvlanlist = cvlan, svlan = tonumber(svlan)})
        end
        row['rules'] = tools.array_check(row['rules'])
        table.insert(destbl, row)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_port()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")

        local info = params['info']
        local portsgrp = params['ports'] or {}
        local vlanvpnifdata = {}
        for _, ifx in ipairs(portsgrp) do
            local portinfo = mydb.getport(ifx)
            if portinfo and portinfo['mytype'] == 0x10 then
                return luci.http.write_json({hdr = {code = 100, message = "Cannot configure member interface of port-channel!", type = "fail"}})
            end

            -- del 
            vlanvpnifdata['ifx'] = ifx
            vlanvpnifdata['enable_basic'] = "Disabled"
            vlanvpnifdata['stack'] = ''
            vlanvpnifdata['map'] = ''
            mydb.setvlanvpnif(vlanvpnifdata)

            -- add
            vlanvpnifdata['enable_basic'] = info['basic'] and "Enabled" or "Disabled"
            vlanvpnifdata['stack'] = info['stacking'] or ''
            vlanvpnifdata['map'] = info['mapping'] or ''
            if not mydb.setvlanvpnif(vlanvpnifdata) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        end
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local vlanvpniftbl = mydb.getvlanvpniftbl()
    for _, vlanvpnif in ipairs(vlanvpniftbl) do
        local row = {}
        row['id'] = tonumber(vlanvpnif['ifx'])
        row['name'] = vlanvpnif['name']
        row['basic'] = vlanvpnif['enable_basic'] == "Enabled"
        row['stacking'] = vlanvpnif['stack'] == "(null)" and "" or vlanvpnif['stack']
        row['mapping'] = vlanvpnif['map'] == "(null)" and "" or vlanvpnif['map']
        table.insert(destbl, row)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})    
end

function handle_info()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "GET" then
        local destbl = {}
        local vlanvpntbl = mydb.getvlanvpntbl()
        for _, vpn in ipairs(vlanvpntbl) do
            local row = {}
            row["name"] = vpn['name']
            row['class'] = vpn['class']
            row['apply'] = string.split(vpn['apply'], ",")
            row['apply'] = tools.array_check(row['apply'])
            row['rules'] = {}
            for cvlan, svlan in string.gmatch(vpn['rule'], "cvlan (%S+) svlan (%d+)\n") do 
                table.insert(row['rules'], { cvlanlist = cvlan, svlan = tonumber(svlan)})
            end
            row['rules'] = tools.array_check(row['rules'])
            table.insert(destbl, row)
        end

        local data = {data = tools.array_check(destbl)}
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
    end
end
