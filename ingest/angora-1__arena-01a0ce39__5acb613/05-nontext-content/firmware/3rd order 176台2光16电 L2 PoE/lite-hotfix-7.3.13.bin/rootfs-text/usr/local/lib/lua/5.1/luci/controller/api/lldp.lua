local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.lldp", package.seeall)

function index()
    entry({"api", "lldp"}, alias("api", "lldp", "conf"), nil).hidden = true
    entry({"api", "lldp", "conf"}, call("handle_config"), nil).leaf = true
    entry({"api", "lldp", "port"}, call("handle_port"), nil).leaf = true
    entry({"api", "lldp", "neighbor"}, call("handle_neighbor"), nil).leaf = true
    entry({"api", "lldp", "stat"}, call("handle_statistics"), nil).leaf = true
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['status']) == "boolean", "status is error")

        local lldpcfg = mydb.getlldpcfg()
        local lldpcfgdata = {}
        lldpcfgdata['status'] = params['status'] and 'Enabled' or 'Disabled'
        lldpcfgdata['sysname'] = params['name'] or lldpcfg['sysname'] or ''
        lldpcfgdata['sysdesc'] = params['desc'] or lldpcfg['sysdesc'] or ''
        mydb.setlldpcfg(lldpcfgdata)
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local lldpcfg = mydb.getlldpcfg()
    local lldpcfgdata = {}
    lldpcfgdata['status'] = lldpcfg['status'] == 'Enabled'
    lldpcfgdata['name'] = lldpcfg['sysname']
    lldpcfgdata['desc'] = lldpcfg['sysdesc']
    local data = lldpcfgdata
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_port()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['info']['tx_hold']) == "nil" or (type(params['info']['tx_hold']) == "number" and params['info']['tx_hold'] > 0 and params['info']['tx_hold'] <= 100), "tx_hold is error")
        assert(type(params['info']['tx_interval']) == "nil" or (type(params['info']['tx_interval']) == "number" and params['info']['tx_interval'] > 4 and params['info']['tx_interval'] <= 3600), "tx_interval is error")
        assert(type(params['info']['reinit_delay']) == "nil" or (type(params['info']['reinit_delay']) == "number" and params['info']['reinit_delay'] > 0 and params['info']['reinit_delay'] <= 10), "reinit_delay is error")
        assert(type(params['info']['fast_tx']) == "nil" or (type(params['info']['fast_tx']) == "number" and params['info']['fast_tx'] > 0 and params['info']['fast_tx'] <= 3600), "fast_tx is error")
        assert(type(params['info']['tx_fast_init']) == "nil" or (type(params['info']['tx_fast_init']) == "number" and params['info']['tx_fast_init'] > 0 and params['info']['tx_fast_init'] <= 8), "tx_fast_init is error")
        assert(type(params['info']['tx_credit_max']) == "nil" or (type(params['info']['tx_credit_max']) == "number" and params['info']['tx_credit_max'] > 0 and params['info']['tx_credit_max'] <= 10), "tx_credit_max is error")

        local info = params['info']
        local oper = params['oper'] or ''
        local portsgrp = params['ports'] or {}
        for _, ifx in ipairs(portsgrp) do
            local lldpifcfgdata = mydb.getlldpifcfg({ifx = tostring(ifx)})
            lldpifcfgdata['desc'] = info['desc'] or lldpifcfgdata['desc']
            lldpifcfgdata['agid'] = info['agent_circuit_id'] or lldpifcfgdata['agid']
            lldpifcfgdata['assigned'] = info['locally_assigned'] or lldpifcfgdata['assigned']
            lldpifcfgdata['admin_status'] = info['state'] or lldpifcfgdata['admin_status']
            lldpifcfgdata['chassis_subtype'] = info['chassis_subtype'] or lldpifcfgdata['chassis_subtype']
            lldpifcfgdata['portid_subtype'] = info['port_id_subtype'] or lldpifcfgdata['portid_subtype']
            lldpifcfgdata['mgmtaddr_subtype'] = info['mgmt_addr_subtype'] or lldpifcfgdata['mgmtaddr_subtype']
            lldpifcfgdata['basic_tlvs'] = info['basic_tlvs'] or lldpifcfgdata['basic_tlvs']
            lldpifcfgdata['dot1_tlvs'] = info['dot1_tlvs'] or lldpifcfgdata['dot1_tlvs']
            lldpifcfgdata['dot3_tlvs'] = info['dot3_tlvs'] or lldpifcfgdata['dot3_tlvs']
            lldpifcfgdata['msg_tx_hold'] = info['tx_hold'] or lldpifcfgdata['msg_tx_hold']
            lldpifcfgdata['msg_tx_interval'] = info['tx_interval'] or lldpifcfgdata['msg_tx_interval']
            lldpifcfgdata['reinit_delay'] = info['reinit_delay'] or lldpifcfgdata['reinit_delay']
            lldpifcfgdata['msg_fast_tx'] = info['fast_tx'] or lldpifcfgdata['msg_fast_tx']
            lldpifcfgdata['tx_fast_init'] = info['tx_fast_init'] or lldpifcfgdata['tx_fast_init']
            lldpifcfgdata['tx_credit_max'] = info['tx_credit_max'] or lldpifcfgdata['tx_fast_init']
            if not mydb.setlldpifcfg(lldpifcfgdata) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local lldpifcfgtbl = mydb.getlldpifcfgtbl()
    for _, lldpifcfg in ipairs(lldpifcfgtbl) do
        local lldpifcfgdata = {}
        lldpifcfgdata['id'] = tonumber(lldpifcfg['ifx'])
        lldpifcfgdata['name'] = lldpifcfg['ifname']
        lldpifcfgdata['desc'] = lldpifcfg['desc']
        lldpifcfgdata['agent_circuit_id'] = lldpifcfg['agid']
        lldpifcfgdata['locally_assigned'] = lldpifcfg['assigned']
        lldpifcfgdata['state'] = lldpifcfg['admin_status']
        lldpifcfgdata['chassis_subtype'] = lldpifcfg['chassis_subtype']
        lldpifcfgdata['port_id_subtype'] = lldpifcfg['portid_subtype']
        lldpifcfgdata['mgmt_addr_subtype'] = lldpifcfg['mgmtaddr_subtype']
        lldpifcfgdata['basic_tlvs'] = lldpifcfg['basic_tlvs']
        lldpifcfgdata['basic_tlvs'] = tools.array_check(lldpifcfgdata['basic_tlvs'])
        lldpifcfgdata['dot1_tlvs'] = lldpifcfg['dot1_tlvs']
        lldpifcfgdata['dot1_tlvs'] = tools.array_check(lldpifcfgdata['dot1_tlvs'])
        lldpifcfgdata['dot3_tlvs'] = lldpifcfg['dot3_tlvs']
        lldpifcfgdata['dot3_tlvs'] = tools.array_check(lldpifcfgdata['dot3_tlvs'])
        lldpifcfgdata['tx_hold'] = tonumber(lldpifcfg['msg_tx_hold'])
        lldpifcfgdata['tx_interval'] = tonumber(lldpifcfg['msg_tx_interval'])
        lldpifcfgdata['reinit_delay'] = tonumber(lldpifcfg['reinit_delay'])
        lldpifcfgdata['fast_tx'] = tonumber(lldpifcfg['msg_fast_tx'])
        lldpifcfgdata['tx_fast_init'] = tonumber(lldpifcfg['tx_fast_init'])
        lldpifcfgdata['tx_credit_max'] = tonumber(lldpifcfg['tx_credit_max'])
        table.insert(destbl, lldpifcfgdata)
    end

    local data = {data = tools.array_check(destbl)}
    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_neighbor()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "GET" then
        local neitbl = mydb.getlldpneitbl()
        local iftbl = {}
        for _, v in pairs(neitbl) do 
            local id = tonumber(v['id'])
            if iftbl[id] == nil then
                iftbl[id] = {id=id, name=v['name'], info={v['info']}}
            else
                table.insert(iftbl[id]['info'], v['info'])
            end
        end
        local tbl = {}
        for _, v in pairs(iftbl) do    -- fix write_json return empty array issue
            table.insert(tbl, v)
        end
        local function comp(a, b)
            return a['id'] < b['id']
        end
        table.sort(tbl, comp)
        local data = {data = tools.array_check(tbl)}
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
    end
end

function handle_statistics()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")

        local oper = params['oper'] or ''
        local portsgrp = params['ports'] or {}
        if oper == 'clear' then
            local lldpifstat = {}
            if not next(portsgrp) then
                local porttable = mydb.getporttable(19)
                for _, port in ipairs(porttable) do
                    lldpifstat['ifx'] = port['Index']
                    if not mydb.setlldpifstat(lldpifstat) then return
                        luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                    end
                end
            else
                for _, ifx in ipairs(portsgrp) do
                    lldpifstat['ifx'] = tostring(ifx)
                    if not mydb.setlldpifstat(lldpifstat) then return
                        luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                    end
                end
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local lldpifstattbl = mydb.getlldpifstattbl()
    for _, lldpifstat in ipairs(lldpifstattbl) do
        local lldpifstatdata = {}
        lldpifstatdata['id'] = tonumber(lldpifstat['ifx'])
        lldpifstatdata['name'] = lldpifstat['ifname']
        lldpifstatdata['tx'] = tonumber(lldpifstat['tx'])
        lldpifstatdata['aged'] = tonumber(lldpifstat['aged'])
        lldpifstatdata['rx'] = tonumber(lldpifstat['rx'])
        lldpifstatdata['rx_err'] = tonumber(lldpifstat['rx_err'])
        lldpifstatdata['discard'] = tonumber(lldpifstat['discards'])
        lldpifstatdata['discard_tlv'] = tonumber(lldpifstat['discard_tlvs'])
        lldpifstatdata['unknown_tlv'] = tonumber(lldpifstat['unknown_tlvs'])
        table.insert(destbl, lldpifstatdata)
    end

    local data = {data = tools.array_check(destbl)}
    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})    
end
