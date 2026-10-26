local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.qos", package.seeall)

function index()
    entry({"api", "qos"}, alias("api", "qos", "conf"), nil).hidden = true
    entry({"api", "qos", "conf"}, call("handle_config"), nil).leaf = true
    entry({"api", "qos", "queue"}, call("handle_queue"), nil).leaf = true
    entry({"api", "qos", "cos"}, call("handle_cos"), nil).leaf = true
    entry({"api", "qos", "dscp"}, call("handle_dscp"), nil).leaf = true
    entry({"api", "qos", "class"}, call("handle_class"), nil).leaf = true
    entry({"api", "qos", "policy"}, call("handle_policy"), nil).leaf = true
    entry({"api", "qos", "port"}, call("handle_port"), nil).leaf = true
    entry({"api", "qos", "portconf"}, call("handle_portconf"), nil).leaf = true
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['state']) == "boolean", "state is error")
        assert(type(params['alg']) == "string", "alg is error")

        if not mydb.setqoscfg( { status = tools.bool_trans(params['state']), alg = params['alg'] } ) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local conf = mydb.getqoscfg()
    destbl['state'] = tools.bool_trans(conf['status'])
    destbl['alg'] = conf['alg']

    local data = destbl
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_queue()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['data']) == "table", "ports is error")

        local queueweight = {}
        local data = params['data']
        for _, row in ipairs(data) do
            if not tools.range_hit(row['queue'], 0, 7) or not tools.range_hit(row['weight'], 0, 32) then
                return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
            end
            table.insert(queueweight, { weight = row['weight'] } )
        end

        if not mydb.setqueueweight(queueweight) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local queueweighttbl = mydb.getqueueweighttbl()
    for _, queueweight in pairs(queueweighttbl) do
        local row = {}
        row['queue'] = tonumber(queueweight['queue'])
        row['weight'] = tonumber(queueweight['weight'])
        table.insert(destbl, row)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_cos()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['data']) == "table", "ports is error")

        local cos2dscp = {}
        local cos2queue = {}
        local data = params['data']
        for _, row in ipairs(data) do
            if not tools.range_hit(row['cos'], 0, 7) or not tools.range_hit(row['queue'], 0, 7) or not tools.range_hit(row['dscp'], 0, 63) then
                return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
            end
            table.insert(cos2dscp, { dscp = row['dscp'] } )
            table.insert(cos2queue, { queue = row['queue'] })
        end

        if not mydb.setcos2dscp(cos2dscp) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        if not mydb.setcos2queue(cos2queue) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local cos2dscptbl = mydb.getcos2dscptbl()
    local cos2queuetbl = mydb.getcos2queuetbl()
    for i, cos2dscp in pairs(cos2dscptbl) do
        local row = {}
        row['cos'] = tonumber(cos2dscp['cos'])
        row['dscp'] = tonumber(cos2dscp['dscp'])
        row['queue'] = tonumber(cos2queuetbl[i]['queue'])
        table.insert(destbl, row)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_dscp()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['data']) == "table", "ports is error")

        local data = params['data']
        local dscptbl = params['dscp'] or {}
        local oper = params['oper'] or ''
        local dscp2cos = mydb.getdscp2costbl()
        local dscp2queue = mydb.getdscp2queuetbl()
        local dscp2dscp = mydb.getdscp2dscptbl()
        if oper == "del" then
            for _, dscp in ipairs(dscptbl) do
                dscp2cos[dscp + 1]['cos'] = ""
                dscp2queue[dscp + 1]['queue'] = ""
                dscp2dscp[dscp + 1]['dscp2'] = ""
            end
        else
            for _, dscp in ipairs(dscptbl) do
                dscp2cos[dscp + 1]['cos'] = tools.range_hit(data['cos'], 0, 7) and data['cos'] or dscp2cos[dscp + 1]
                dscp2queue[dscp + 1]['queue'] = tools.range_hit(data['queue'], 0, 7) and data['queue'] or dscp2queue[dscp + 1]
                dscp2dscp[dscp + 1]['dscp2'] = tools.range_hit(data['new_dscp'], 0, 63) and data['new_dscp'] or dscp2dscp[dscp + 1]
            end
        end

        if not mydb.setdscp2cos(dscp2cos) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        if not mydb.setdscp2queue(dscp2queue) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        if not mydb.setdscp2dscp(dscp2dscp) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local dscp2costbl = mydb.getdscp2costbl()
    local dscp2queuetbl = mydb.getdscp2queuetbl()
    local dscp2dscptbl = mydb.getdscp2dscptbl()
    for i, dscp2cos in pairs(dscp2costbl) do
        local row = {}
        row['dscp'] = tonumber(dscp2cos["dscp"])
        row['cos'] = tonumber(dscp2cos["cos"])
        row['queue'] = tonumber(dscp2queuetbl[i]["queue"])
        row['new_dscp'] = tonumber(dscp2dscptbl[i]["dscp2"])
        table.insert(destbl, row)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_class()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['info']['name']) == "string", "name is error")

        if not params['info']['value'] then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end
        if type(params['info']['value']) == "table" then
            local invalid_conf = true
            for _, v in pairs(params['info']['value']) do
                if v ~= "" then
                    invalid_conf = false
                end
            end
            if invalid_conf then
                return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
            end
        end

        local ack = true
        local info = params['info']
        local oper = params['oper'] or ""
        local classtbl = mydb.getclasstbl()
        for _, class in ipairs(classtbl) do
            if class['name'] == info['name'] then
                class['matchtype'] = ''
                if not mydb.setclass(class, 2) then
                    return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
                end
            end
        end

        -- local class = mydb.getclass(info['name'])
        -- if next(class) then
        --     if not mydb.setclass(class, 2) then
        --         return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        --     end
        -- end

        local class = {}
        if oper ~= "del" then
            class['name'] = info['name']
            class['matchtype'] = info['match']
            class['value'] = ""
            if info['match'] and type(info['value']) == "table" then
                if info['match'] == "none" then
                    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
                elseif info['match'] == "l4" then
                    local l4port = ""
                    local map = {
                        { type = info['value']["tcp_src_port"], prefix = "1 1 " },
                        { type = info['value']["tcp_dst_port"], prefix = "1 2 " },
                        { type = info['value']["udp_src_port"], prefix = "2 1 " },
                        { type = info['value']["udp_dst_port"], prefix = "2 2 " }
                    }
                    for i = 1, 4 do
                        if map[i]["type"] then
                            l4port = mydb.vlanstr2tbl(map[i]["type"])   -- string trans to table
                            for _, v in ipairs(l4port) do
                                if not tools.range_hit(v, 0, 65535) then
                                    return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
                                end
                                class['value'] = map[i]["prefix"] .. v
                                ack = mydb.setclass(class, 1) and ack
                            end
                        end
                    end
                elseif info['match'] == "dhcp" or info['match'] == "cos" then
                    local map = {
                        { match = "dhcp", low = 0, high = 63 },
                        { match = "cos", low = 0, high = 7 }
                    }
                    local idlst = mydb.vlanstr2tbl(info['value']['value'])
                    if #idlst > 8 then
                        return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
                    end

                    local i = 1;
                    if info['match'] == "cos" then i = 2 end
                    for _, v in ipairs(idlst) do
                        if not tools.range_hit(v, map[i]["low"], map[i]["high"]) then
                            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
                        end
                        class['value'] = v
                        ack = mydb.setclass(class, 1) and ack
                    end
                elseif info['match'] == "etype" then
                    if tonumber(info['value']['value']) > 0xffff then
                        return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
                    end
                    class['value'] = string.format("%x", info['value']['value'])
                    ack = mydb.setclass(class, 1) and ack
                elseif info['match'] == "acl" then
                    class['value'] = info['value']['name']
                    ack = mydb.setclass(class, 1) and ack
                else
                    if info['match'] == "vlan-range" then
                        if not tools.range_hit(info['value']['start'], 1, 4094) or not tools.range_hit(info['value']['end'], 1, 4094) or info['value']['start'] >= info['value']['end'] then
                            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
                        end
                        class['value'] = info['value']['start'] .. "-" .. info['value']['end']
                    else
                        if info['match'] == "vlan" and not tools.range_hit(tonumber(info['value']['value']), 1, 4094) then
                            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
                        end

                        class['value'] = info['value']['value']
                    end
                    ack = mydb.setclass(class, 1) and ack
                end
            end
        end

        if not ack then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local classtbl = mydb.getclasstbl()
    for _, class in ipairs(classtbl) do
        local row = {}
        row['name'] = class['name']
        row['match'] = class['matchtype']
        row['value'] = {}
        if class['matchtype'] == "acl" then
            row['value']['name'] = class["value"]
        elseif class['matchtype'] == "etype" or class['matchtype'] == "dscp" or class['matchtype'] == "v6dscp" or class['matchtype'] == "cos" then
            row['value']['value'] = class['value']
        elseif  class['matchtype'] == "l4" then
            row['value']['tcp_src_port'] = string.match(class['value'], "tcp source%-port ([%d%,%-]+)")
            row['value']['tcp_dst_port'] = string.match(class['value'], "tcp destination%-port ([%d%,%-]+)")
            row['value']['udp_src_port'] = string.match(class['value'], "udp source%-port ([%d%,%-]+)")
            row['value']['udp_dst_port'] = string.match(class['value'], "udp destination%-port ([%d%,%-]+)")
        elseif class['matchtype'] == "vlan" then
            row['value']['value'] = tonumber(class['value'])
        elseif class['matchtype'] == "vlan-range" then
            local vrstart, vrend = string.match(class['value'], "(%d+)-(%d+)")
            row['value']['start'] = tonumber(vrstart)
            row['value']['end'] = tonumber(vrend)
        else    -- class['matchtype'] == "none"
            -- void
        end
        table.insert(destbl, row)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_policy()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "table is error")
        if type(params['info']['rules']) == "table" and #params['info']['rules'] > 8 then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end

        local info = params['info']
        local rules = info['rules'] or {}
        local oper = params['oper'] or ''
        local policytbl = mydb.getpolicytbl()
        local policy = {name = info['name'], police = 'none'}
        for _, row in ipairs(policytbl) do
            if policy['name'] == row['name'] then
                row['cname'] = ""
                if not mydb.setpolicy(row, 2) then
                    return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                end
            end
        end

        if oper ~= "del" then
            if next(rules) then
                for _, v in ipairs(rules) do
                    if v['cir'] and not tools.range_hit(v['cir'], 32, 1000000) then return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}}) end
                    if v['cbs'] and not tools.range_hit(v['cbs'], 4, 31250) then return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}}) end
                    if v['mod_val'] then
                        if v['mod'] == "cos" and not tools.range_hit(v['mod_val'], 0, 7) then 
                            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
                        end
                        if v['mod'] == "dscp" and not tools.range_hit(v['mod_val'], 0, 63) then 
                            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
                        end
                        if v['mod'] == "vlan" and not tools.range_hit(v['mod_val'], 1, 4094) then 
                            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
                        end
                    end

                    if v['cir'] and v['cbs'] then
                        policy['police'] = "ratelimit"
                        policy["cir"] = v['cir']
                        policy["cbs"] = v['cbs']
                    end
                    policy['cname'] = v['class'] or ""
                    policy['settype'] = v['mod'] or "none"
                    policy["setval"] = v['mod_val']
                    if not mydb.setpolicy(policy, 1) then
                        return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                    end
                end
            else
                policy['cname'] = ""
                policy['settype'] = "none"
                if not mydb.setpolicy(policy, 1) then
                    return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                end
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local policyname = {}
    local policytbl = mydb.getpolicytbl()
    for _, policy in ipairs(policytbl) do
        local row = {}
        if policyname[policy['name']] then
            row['class'] = policy["cname"]
            row['mod'] = policy["settype"]
            row['cir'] = tonumber(policy['cir'] ~= "0" and policy['cir'] or nil)
            row['cbs'] = tonumber(policy['cbs'] ~= "0" and policy['cbs'] or nil)
            row['mod_val'] = tonumber(policy['setval'])
            for i, v in ipairs(destbl) do
                if v['name'] == policy['name'] then
                    table.insert(destbl[i]['rules'], row)
                end
            end
        else
            policyname[policy['name']] = true
            row['name'] = policy['name']
            row['rules'] = {}
            if policy["cname"] and policy["cname"] ~= "" then
                row['rules'][1] = { class = policy["cname"], mod = policy["settype"], cir = tonumber(policy['cir'] ~= "0" and policy['cir'] or nil), cbs = tonumber(policy['cbs'] ~= "0" and policy['cbs'] or nil), mod_val = tonumber(policy['setval']) }
            end
            row['rules'] = tools.array_check(row['rules'])
            table.insert(destbl, row)
        end
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_port()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        if params["info"]['defcos'] and not tools.range_hit(params["info"]['defcos'], 0 , 7) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end

        local info = params['info'] or {}
        local portsgrp = params['ports'] or {}
        local oper = params['oper'] or ""
        local platform = mydb.getdevplatform()
        local qosiftbl = {}
        if platform == "AC5" or platform == "LITE" then
            qosiftbl = mydb.getqospolicyiftbl()
        else
            qosiftbl = mydb.getqosiftbl()
        end
        for _, ifx in ipairs(portsgrp) do
            for _, qosif in pairs(qosiftbl) do
                if ifx == tonumber(qosif['ifx']) then
                    local portinfo = mydb.getport(ifx)
                    if portinfo and portinfo['mytype'] == 0x10 then
                        return luci.http.write_json({hdr = {code = 100, message = "Cannot configure member interface of port-channel!", type = "fail"}})
                    end
                    qosif['cos'] = info['defcos'] or ''
                    qosif['trustmode'] = info['trust'] or qosif['trustmode']
                    qosif['in'] = info['in'] or qosif['in']
                    if platform == "AC5" or platform == "LITE" then
                        if not mydb.setqospolicyif(qosif, 1) then
                            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                        end
                    else
                        if not mydb.setqosif(qosif, 1) then
                            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                        end
                    end
                end
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local platform = mydb.getdevplatform()
    local qosiftbl = {}
    if platform == "AC5" or platform == "LITE" then
        qosiftbl = mydb.getqospolicyiftbl()
    else    -- platform == "X1021"
        qosiftbl = mydb.getqosiftbl()
    end
    for _, qosif in pairs(qosiftbl) do
        local row = {}
        row['id'] = tonumber(qosif['ifx'])
        row['name'] = qosif['name']
        row['defcos'] = tonumber(qosif['cos'])
        row['trust'] = qosif['trustmode']
        row['in'] = qosif['in']
        table.insert(destbl, row)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function getqosifcfg(index)
    local tbl = {}
    str = librpc.callapi("oltmib_qosifcfg_get_1", index .. "&")
    _, _, ifx, ifname, queue_cir, queue_cbs, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
    if (result == "0") then
        tbl["ifx"] = ifx
        tbl["name"] = ifname
        tbl["queue"] = {}
        for i, v in ipairs(string.split(queue_cir, ',')) do
            if (not tbl["queue"][i]) then tbl["queue"][i] = {} end
            tbl["queue"][i]["idx"] = i - 1
            tbl["queue"][i]["cir"] = tonumber(v)
        end

        for i, v in ipairs(string.split(queue_cbs, ',')) do
            if (not tbl["queue"][i]) then tbl["queue"][i] = {} end
            tbl["queue"][i]["idx"] = i - 1
            tbl["queue"][i]["cbs"] = tonumber(v)
        end
    end

    return tbl
end

function getqosifcfgtbl(data)
    local tbl = {}
    str = ""
    result = "0"
    while (result == "0") do
        str = librpc.callapi("oltmib_qosifcfg_getn_1", str)
        _, _, ifx, ifname, queue_cir, queue_cbs, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["ifx"] = ifx
            row["name"] = ifname
            row["queue"] = {}
            for i, v in ipairs(string.split(queue_cir, ',')) do
                if (not row["queue"][i]) then row["queue"][i] = {} end
                row["queue"][i]["idx"] = i - 1
                row["queue"][i]["cir"] = tonumber(v)
            end

            for i, v in ipairs(string.split(queue_cbs, ',')) do
                if (not row["queue"][i]) then row["queue"][i] = {} end
                row["queue"][i]["idx"] = i - 1
                row["queue"][i]["cbs"] = tonumber(v)
            end
            table.insert(tbl, row)
        end
    end

    return tbl
end

function setqosifcfg(data)
    local cir = ""
    local cbs = ""
    for i, v in ipairs(data["queue"]) do
        cir = cir .. v["cir"] .. ","
        cbs = cbs .. v["cbs"] .. ","
    end

    return librpc.callapi("oltmib_qosifcfg_set_1", data["ifx"] .. "&&" .. cir .. "&" .. cbs .. "&&&") == "0"
end

function handle_portconf()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")

        local info = params['info'] or {}
        local portsgrp = params['ports'] or {}
        local oper = params['oper'] or ""

        for _, ifx in ipairs(portsgrp) do
            local portinfo = mydb.getport(ifx)
            if portinfo and bit.band(portinfo['mytype'], 0x8) == 0x8 then
                return luci.http.write_json({hdr = {code = 100, message = "Cannot configure port-channel interface!", type = "fail"}})
            end

            local qosif = getqosifcfg(ifx) or {}
            local idx
            if next(qosif) then
                for _, v in ipairs(info["queue"] or {}) do
                    if (not next(qosif["queue"])) then qosif["queue"] = {} end
                    idx = tonumber(v["idx"]) + 1
                    qosif["queue"][idx] = {cir = v["cir"], cbs = v["cbs"]}
                end

                if not setqosifcfg(qosif) then
                    return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                end
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local qosifcfgtbl = getqosifcfgtbl()
    for _, qosif in ipairs(qosifcfgtbl) do
        local row = {}
        row['id'] = tonumber(qosif['ifx'])
        row['name'] = qosif['name']
        row['queue'] = qosif['queue']

        table.insert(destbl, row)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
