local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.stp", package.seeall)

function index()
    entry({"api", "stp"}, alias("api", "stp", "info"), nil).hidden = true
    entry({"api", "stp", "info"}, call("handle_info"), nil).leaf = true
    entry({"api", "stp", "conf"}, call("handle_config"), nil).leaf = true
    entry({"api", "stp", "port"}, call("handle_port"), nil).leaf = true
    entry({"api", "stp", "inst"}, call("handle_instance"), nil).leaf = true
end

function handle_info()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")

        local pname = params['name']
        local oper = params['oper']
        if params['oper'] == "clear" then
            local stpifstatedata = {}
            stpifstatedata['ifname'] = pname
            mydb.setstpifstate(stpifstatedata)
        end
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local stpifstatetbl = mydb.getstpifstatetbl()
    for _, v in ipairs(stpifstatetbl) do
        local mtbl = {}
        mtbl['id'] = tonumber(v['ifx'])
        mtbl['name'] = v['ifname']
        mtbl['instance'] = tonumber(v['instance'])
        mtbl['version'] = v['version']
        mtbl['role'] = v['role']
        mtbl['state'] = v['state']
        mtbl['rootbid'] = v['rootbid']
        mtbl['regrootbid'] = v['regrootbid']
        mtbl['desbid'] = v['desbid']
        table.insert(destbl, mtbl)
    end
    
    local data = {data = tools.array_check(destbl)}
    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params['mode']) == "string", "mode is error")
        assert(type(params['state']) == "boolean", "state is error")
        assert(type(params['bpdu_guard']) == "boolean", "bpduguard is error")
        assert(type(params['bpdu_filter']) == "boolean", "bpdufilter is error")
        assert(type(params['errdis_tout_st']) == "boolean", "errdis is error")
        assert(type(params['mst_reg']) == "string", "region is error")
        assert(type(params['max_hops']) == "number" and params['max_hops'] > 0 and params['max_hops'] <= 40, "maxhops is error")
        assert(type(params['forward_delay']) == "number" and params['forward_delay'] > 3 and params['forward_delay'] <= 30, "forwardtime is error")
        assert(type(params['hello_time']) == "number" and params['hello_time'] > 0 and params['hello_time'] <= 10, "hellotime is error")
        assert(type(params['max_age']) == "number" and params['max_age'] > 5 and params['max_age'] <= 40, "maxage is error")
        assert(type(params['priority']) == "number" and params['priority'] >= 0 and params['priority'] <= 61440, "priority is error")
        assert(type(params['tx_hold_cnt']) == "number" and params['tx_hold_cnt'] > 0 and params['tx_hold_cnt'] <= 10, "txcount is error")
        assert(type(params['errdis_tout']) == "number" and params['errdis_tout'] > 9 and params['errdis_tout'] <= 1000000, "errdistm is error")
        assert(type(params['mst_rev']) == "number" and params['mst_rev'] >= 0 and params['mst_rev'] <= 65535, "revision is error")

        local stpglobal, stpmst = {}, {}
        stpglobal['mode'] = params['mode']
        stpglobal['status'] = params['state'] and 'Enable' or 'Disable'
        stpglobal['bpduguard'] = params['bpdu_guard'] and'Enable' or 'Disable'
        stpglobal['bpdufilter'] = params['bpdu_filter'] and 'Enable' or 'Disable'
        stpglobal['maxhops'] = params['max_hops'] 
        stpglobal['forwardtime'] = params['forward_delay']
        stpglobal['hellotime'] = params['hello_time']
        stpglobal['maxage'] = params['max_age']
        stpglobal['priority'] = params['priority']
        stpglobal['txcount'] = params['tx_hold_cnt']
        stpglobal['errdis'] = params['errdis_tout_st'] and 'Enable' or 'Disable'
        stpglobal['errdistm'] = params['errdis_tout']
        stpmst['region'] = params['mst_reg']
        stpmst['revision'] = params['mst_rev']
        mydb.setstpglobal(stpglobal)
        mydb.setstpmst(stpmst)
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local stpglobal = mydb.getstpglobal()
    local stpmst = mydb.getstpmst()
    destbl['mode'] = stpglobal['mode']
    destbl['state'] = stpglobal['status'] == 'Enable'
    destbl['bpdu_guard'] = stpglobal['bpduguard'] == 'Enable'
    destbl['bpdu_filter'] = stpglobal['bpdufilter'] == 'Enable'
    destbl['max_hops'] = tonumber(stpglobal['maxhops'])
    destbl['forward_delay'] = tonumber(stpglobal['forwardtime'])
    destbl['hello_time'] = tonumber(stpglobal['hellotime'])
    destbl['max_age'] = tonumber(stpglobal['maxage'])
    destbl['priority'] = tonumber(stpglobal['priority'])
    destbl['tx_hold_cnt'] = tonumber(stpglobal['txcount'])
    destbl['errdis_tout_st'] = stpglobal['errdis'] == 'Enable'
    destbl['errdis_tout'] = tonumber(stpglobal['errdistm'])
    destbl['mst_reg'] = stpmst['region']
    destbl['mst_rev'] = tonumber(stpmst['revision'])
    local data = destbl
    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_port()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        local info = params['info']
        local insttbl = info['instance'] or {}
        local portsgrp = params['ports'] or {}

        local stpiftbl = mydb.getstpiftbl()
        for _, portidx in ipairs(portsgrp) do
            local pid = tostring(portidx)
            local port = mydb.getport(pid)
            if port and port['mytype'] == 0x10 then
                return luci.http.write_json({hdr = {code = 100, message = "Cannot configure member interface of port-channel! ", type = "fail"}})
            end

            local stpifdata1 = mydb.getstpif(port['Name'], "")
            stpifdata1['status'] = type(info['state']) == "boolean" and (info['state'] and 'Enable' or 'Disable') or stpifdata1['status']
            stpifdata1['pathcost'] = info['pathcost'] and tostring(info['pathcost']) or stpifdata1['pathcost']
            stpifdata1['linktype'] = info['link_type'] or stpifdata1['linktype']
            stpifdata1['rootguard'] = type(info['root_guard']) == "boolean" and (info['root_guard'] and 'Enable' or 'Disable') or stpifdata1['rootguard']
            stpifdata1['autoedge'] = type(info['auto_edge']) == "boolean" and (info['auto_edge'] and 'Enable' or 'Disable') or stpifdata1['autoedge']
            stpifdata1['edgeport'] = type(info['edge_port']) == "boolean" and (info['edge_port'] and 'Enable' or 'Disable') or stpifdata1['edgeport']
            stpifdata1['portfast'] = type(info['port_fast']) == "boolean" and (info['port_fast'] and 'Enable' or 'Disable') or stpifdata1['portfast']
            stpifdata1['bpduguard'] = info['bpdu_guard'] or stpifdata1['bpduguard']
            stpifdata1['bpdufilter'] = info['bpdu_filter'] or stpifdata1['bpdufilter']
            mydb.setstpif(stpifdata1)

            -- delete the original instance
            for _, stpif in ipairs(stpiftbl) do
                if stpif['ifx'] == pid then
                    local stpifdata2 = mydb.getstpif(port['Name'], stpif['instance'])
                    stpifdata2['oper'] = '2'
                    mydb.setstpif(stpifdata2)
                end
            end

            -- Restore default instance configuration
            local stpifdef = mydb.stpifdefault()
            stpifdata1['instance'] = stpifdef['instance']
            stpifdata1['priority'] = stpifdef['priority']
            stpifdata1['tcn'] = stpifdef['tcn']
            mydb.setstpif(stpifdata1)

            -- add instance
            for _, inst in ipairs(insttbl) do
                stpifdata1['instance'] = tostring(inst['id'])
                stpifdata1['priority'] = inst['priority'] or stpifdata1['priority']
                stpifdata1['tcn'] = type(inst['tcn_restrict']) == "boolean" and (inst['tcn_restrict'] and 'Enable' or 'Disable') or stpifdata1['tcn']
                mydb.setstpif(stpifdata1)
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local portlist = {}
    local stpiftbl = mydb.getstpiftbl()
    for _, stpif in ipairs(stpiftbl) do
        if not portlist[stpif['ifx']] then
            local stpifdata = {}
            portlist[stpif['ifx']] = true
            stpifdata['id'] = tonumber(stpif['ifx'])
            stpifdata['name'] = stpif['ifname']
            stpifdata['state'] = stpif['status'] ~= 'Disable'
            stpifdata['pathcost'] = tonumber(stpif['pathcost'])
            stpifdata['link_type'] = stpif['linktype']
            stpifdata['root_guard'] = stpif['rootguard'] == 'Enable'
            stpifdata['auto_edge'] = stpif['autoedge'] == 'Enable'
            stpifdata['edge_port'] = stpif['edgeport'] == 'Enable'
            stpifdata['port_fast'] = stpif['portfast'] == 'Enable'
            stpifdata['bpdu_guard'] = stpif['bpduguard']
            stpifdata['bpdu_filter'] = stpif['bpdufilter']
            stpifdata['instance'] = {}
            table.insert(stpifdata['instance'], {id = tonumber(stpif['instance']), priority = tonumber(stpif['priority']), tcn_restrict = stpif['tcn'] == 'Enable'})
            table.insert(destbl, stpifdata)
        else
            local inst = {id = tonumber(stpif['instance']), priority = tonumber(stpif['priority']), tcn_restrict = stpif['tcn'] == 'Enable'}
            for idx, stpifdata in ipairs(destbl) do
                if stpifdata['id'] == tonumber(stpif['ifx']) then
                    table.insert(destbl[idx]['instance'], inst)
                    break
                end
            end
        end
    end

    local data = {data = tools.array_check(destbl)}
    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_instance()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params['id']) == "number" and params['id'] > 0 and params['id'] <= 63 , "id is error")
 
        local id = tostring(params['id'])
        local stpinst = mydb.getstpinst(id)
        if next(stpinst) then
            stpinst['oper'] = '2'
            mydb.setstpinst(stpinst)
        end

        if params['oper'] ~= 'del' then
            assert(type(params['vlanlist']) == "string", "vlanlist is error")
            assert(type(params['priority']) == "number" and params['priority'] >= 0 and params['priority'] <= 61440, "priority is error")

            stpinst['oper'] = '0'
            stpinst['id'] = id
            stpinst['priority'] = tostring(params['priority'])
            stpinst['vlanlst'] = mydb.filter_vlan(params['vlanlist'])
            if not mydb.setstpinst(stpinst) then
                return luci.http.write_json({hdr = {code = 100, message = "Failed to modify instance", type = "fail"}})
            end
        end
        
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local stpinsttbl = mydb.getstpinsttbl()
    for _, stpinst in ipairs(stpinsttbl) do
        local stpinstdata = {}
        stpinstdata['id'] = tonumber(stpinst['id'])
        stpinstdata['vlanlist'] = stpinst['vlanlst']
        stpinstdata['priority'] = tonumber(stpinst['priority'])
        table.insert(destbl, stpinstdata)
    end

    local data = {data = tools.array_check(destbl)}
    return luci.http.write_json({hdr = {code = 0, message = 'ok', type = 'success'}, result = data})
end
