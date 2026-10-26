require "bit"
require "luci.sys"
require "luci.tools.webadmin"
require "nixio.fs"
local json = require "luci.json"
local comdb = require "luci.controller.lib.comdb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.dhcpsnp", package.seeall)

function index()
    entry({"api", "dhcpsnp"}, alias("api", "dhcpsnp", "conf"), nil).hidden = true
    entry({"api", "dhcpsnp", "conf"}, call("handle_config"), nil).leaf = true
    entry({"api", "dhcpsnp", "port"}, call("handle_port"), nil).leaf = true
    entry({"api", "dhcpsnp", "db"}, call("handle_db"), nil).leaf = true
end

function option82_int2bool(state)
    local opt82, opt82_extend_fmt = false, false
    if (tonumber(state) > 0) then opt82 = true end
    if (tonumber(state) > 1) then opt82_extend_fmt = true end
    return opt82, opt82_extend_fmt
end

function option82_bool2int(opt82, opt82_extend_fmt)
    local state
    if (not opt82) then
        state = 0
    elseif (not opt82_extend_fmt) then
        state = 1
    else
        state = 2
    end

    return state
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")

        local conf = {}
        conf['enable'] = tools.bool_trans(params['state'])
        conf["vlanlist"] = params['vlanlst']
        conf["mac_verify"] = tools.bool_trans(params['verify_mac'])
        conf["option82"] = option82_bool2int(params['support_opt82'], params['opt82_extend_fmt'])
        conf["write_delay"] = tools.valfilter(params['db_delay'])

        local data = {}
        table.insert(data, "type=enable;enable=" .. conf["enable"] .. ";")
        table.insert(data, "type=vlanlist;vlanlist=" .. conf["vlanlist"] .. ";")
        table.insert(data, "type=mac_verify;mac_verify=" .. conf["mac_verify"] .. ";")
        table.insert(data, "type=option82;option82=" .. conf["option82"] .. ";")
        if conf["write_delay"] then table.insert(data, "type=write_delay;write_delay=" .. conf["write_delay"] .. ";") end
        if not comdb.dhcpsnp_setall("/dhcpsnp/conf", data, 2) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local config = comdb.dhcpsnp_getall("/dhcpsnp/conf", 2)[1]
    destbl['state'] = tools.bool_trans(config['enable'])
    destbl['vlanlst'] = config['vlanlist']
    destbl['verify_mac'] = tools.bool_trans(config['mac_verify'])
    destbl['support_opt82'], destbl['opt82_extend_fmt'] = option82_int2bool(config['option82'])
    destbl['db_delay'] = tonumber(config['write_delay']) ~= 0 and tonumber(config['write_delay']) or nil

    local data = tools.array_check(destbl)
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_port()
   luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")

        if type(params['info']['circuitid']) == "string" and not tools.range_hit(#params['info']['circuitid'], 3, 63) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end

        if type(params['info']['remoteid']) == "string" and not tools.range_hit(#params['info']['remoteid'], 0, 63) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end

        local oper = params or ''
        local info = params['info']
        local portsgrp = params['ports'] or {}
        local conf = {}
        conf["trust"] = tools.bool_trans(info['trust'])
        conf["rate"] = tools.valfilter(info['ratelimit'], -1)
        conf["circuitid"] = tools.valfilter(info['circuitid'], "")
        conf["remoteid"] = tools.valfilter(info['remoteid'], "")
        for i = 1, #portsgrp do
            local data = {}
            table.insert(data, "type=if_trust;trust=" .. conf["trust"] .. ";" .. "ifindex=" .. portsgrp[i] .. ";")
            if conf["rate"] then table.insert(data,"type=if_rate;rate=" .. conf["rate"] .. ";" .. "ifindex=" .. portsgrp[i] .. ";") end
            if conf["circuitid"] then table.insert(data,"type=if_circuitid;circuitid=" .. conf["circuitid"] .. ";" .. "ifindex=" .. portsgrp[i] .. ";") end
            if conf["remoteid"] then table.insert(data,"type=if_remoteid;remoteid=" .. conf["remoteid"] .. ";" .. "ifindex=" .. portsgrp[i] .. ";") end
            if not comdb.dhcpsnp_setall("/dhcpsnp/port", data, 2) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local porttbl = comdb.dhcpsnp_getall("/dhcpsnp/port", 2)
    for _, port in ipairs(porttbl) do
        local row = {}
        row['id'] = tonumber(port['id'])
        row['name'] = port['name']
        row['trust'] = tools.bool_trans(port['trust'])
        row['ratelimit'] = port['rate'] ~= "-1" and tonumber(port['rate']) or nil
        row['circuitid'] = port['circuitid'] or ""
        row['remoteid'] = port['remoteid'] or ""
        table.insert(destbl, row)
    end

    local data = { data = tools.array_check(destbl) }
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_db()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")

        local oper = params['oper'] or ''
        local info = params['info'] or {}
        local args = info['args'] or {}
        local type = info['type'] or ""
        local data = {}
        if oper == "clear" then
            if type == "all" then
                table.insert(data, "type=clear;memory=1")
            else
                for _, v in ipairs(args) do
                    if type ~= "" and v ~= "" then
                        table.insert(data, "type=clear;" .. type .."=" .. v)
                    end
                end
            end
        elseif oper == "write" then
            table.insert(data, "type=write_flash;write_flash=1;")
        elseif oper == "clearFlash" then
            table.insert(data, "type=clear;flash=1")
        else
            -- oper == "read"
            table.insert(data, "type=renew;renew=1;")
        end
        if not comdb.dhcpsnp_setall("/dhcpsnp/db", data, 2) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local dbtbl = comdb.dhcpsnp_getall("/dhcpsnp/db", 2)
    for _, db in ipairs(dbtbl) do
        local row = {}
        row['id'] = tonumber(db['ifindex'])
        row['name'] = db['ifname']
        row['vid'] = tonumber(db['vid'])
        row['mac'] = db['mac']
        row['ip'] = db['ip']
        row['lease'] = tonumber(db['lease'])
        row['type'] = "dynamic"
        table.insert(destbl, row)
    end

    local data = { data = tools.array_check(destbl) }
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
