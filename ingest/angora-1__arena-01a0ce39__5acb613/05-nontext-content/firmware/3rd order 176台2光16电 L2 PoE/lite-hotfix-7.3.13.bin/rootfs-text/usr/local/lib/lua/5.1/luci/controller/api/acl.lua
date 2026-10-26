local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.acl", package.seeall)

function index()
    entry({"api", "acl"}, alias("api", "acl", "conf"), nil).hidden = true
    entry({"api", "acl", "conf"}, call("handle_config"), nil).leaf = true
    entry({"api", "acl", "rules"}, call("handle_rules"), nil).leaf = true
    entry({"api", "acl", "port"}, call("handle_port"), nil).leaf = true
end

function acl_gettypeopts()
    return { "IP", "IP-Extend", "MAC", "IPV6"}
end

function acl_typetrans(acltype, extflag)
    local trans = {}
    -- trans["10"] = "MAC"
    -- trans["20"] = "IP"
    -- trans["30"] = "IPV6"
    -- trans["11"] = "MAC-Extend"
    -- trans["21"] = "IP-Extend"
    -- trans["31"] = "IPV6-Extend"
    -- trans["MAC"] = { 1, 0 }
    -- trans["IP"] = { 2, 0 }
    -- trans["IPV6"] = { 3, 0 }
    -- trans["MAC-Extend"] = { 1, 1 }
    -- trans["IP-Extend"] = { 2, 1 }
    -- trans["IPV6-Extend"] = { 3, 1 }
    trans["11"] = "MAC"
    trans["20"] = "IP"
    trans["21"] = "IP-Extend"
    trans["31"] = "IPV6"
    trans["MAC"] = { 1, 1 }
    trans["IP"] = { 2, 0 }
    trans["IP-Extend"] = { 2, 1 }
    trans["IPV6"] = { 3, 1 }
    return trans[acltype .. (extflag or "")]
end

function acl_getfilteropts()
    return { "Permit", "Deny" }--, "Mirror"}
end

function acl_filtertypetrans(filtertype)
    local trans = {}
    trans["0"] = "deny"
    trans["1"] = "permit"
    trans["2"] = "mirror"
    trans["deny"] = "0"
    trans["permit"] = "1"
    trans["mirror"] = "2"
    return trans[tostring(filtertype)] or ""
end

function acl_getprotoopts()
    return { "any", "gre", "icmp", "igmp", "ip", "ipcomp", "ospf", "pim", "rsvp", "tcp", "udp", "vrrp" }
end

function getacltbl()
    acltable = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_acl_getn_1", str)
        _, _, name, acltype, extflag, cntflag, reseq_start, reseq_step, desc, sn, filtertype, proto, src, srcmsk, sport, dst, dstmsk, dport, ethertype, cos, cnt, msg, oper, result = string.find(str, string.rep("(.-)&", 21) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["name"] = name
            row["acltype"] = acl_typetrans(acltype, extflag)
            row["desc"] = desc
            row["cntflag"] = cntflag
            row["reseq_start"] = reseq_start
            row["reseq_step"] = reseq_step
            table.insert(acltable, row)
        end
    end
    return acltable
end

function getacl(arg_name)
    if arg_name == "new" then
        return genemptydata(1, aclfmt)
    end
    local acl = { rules = {} }
    result = "0"
    name = arg_name
    str = arg_name .. "&&&&&&&&&&&&&&&&&&&&" .. 5
    while (name == arg_name and result == "0") do
        str = librpc.callapi("oltmib_acl_getn_1", str)
        _, _, name, acltype, extflag, cntflag, reseq_start, reseq_step, desc, sn, filtertype, proto, src, srcmsk, sport, dst, dstmsk, dport, ethertype, cos, cnt, msg, oper, result = string.find(str, string.rep("(.-)&", 21) .. "(.*)")
        if (name == arg_name and result == "0") then
            acl["name"] = name
            acl["acltype"] = acl_typetrans(acltype, extflag)
            acl["desc"] = desc
            acl["cntflag"] = cntflag
            acl["reseq_start"] = reseq_start
            acl["reseq_step"] = reseq_step
            table.insert(acl["rules"], { sn = sn, control = acl_filtertypetrans(filtertype), proto = proto, src = src, srcmsk = srcmsk, sport = sport, dst = dst, dstmsk = dstmsk, dport = dport, ethertype = ethertype, cos = cos, cnt = cnt })
        end
    end
    return acl
end

function setacl(data, oper)
    local tmp = acl_typetrans(data["acltype"])
    acltype, extflag = tmp[1], tmp[2]
    str = data["name"] .. "&" .. acltype .. "&" .. extflag .. "&" .. (data["cntflag"] or "") .. "&" .. (data["reseq_start"] or "") .. "&" .. (data["reseq_step"] or "") .. "&" .. (data["desc"] or "") .. "&"
        .. (data["sn"] or "") .. "&" .. (acl_filtertypetrans(data["control"]) or "") .. "&" .. (data["proto"] or "").. "&" .. (data["src"] or "") .. "&" .. (data["srcmsk"] or "") .. "&" .. (data["sport"] or "") .. "&"
        .. (data["dst"] or "") .. "&" .. (data["dstmsk"] or "") .. "&" .. (data["dport"] or "") .. "&" .. (data["ethertype"] or "") .. "&" .. (data["cos"] or "") ..  "&&&" .. oper
    result = librpc.callapi("oltmib_acl_set_1", str)
    return result == "0"
end

function getacliftbl()
    acliftable = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_aclif_getn_1", str)
        _, _, ifx, name, ifin, ifout, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["ifx"] = ifx
            row["name"] = name
            row["in"] = ifin
            row["out"] = ifout
            table.insert(acliftable, row)
        end
    end
    return acliftable
end

function setaclif(data)
    str = data["ifx"] .. "&" .. (data["name"] or "") .. "&" .. data["in"] .. "&" .. data["out"]
    return librpc.callapi("oltmib_aclif_set_1", str) == "0"
end

function handle_port()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")

        local info = params['info']
        local oper = params['oper'] or ''
        local portsgrp = params['ports'] or {}
        if oper ~= "del" then
            local aclifdata = {}
            aclifdata['in'] = tools.valfilter(info['in'], '') or ''
            aclifdata['out'] = tools.valfilter(info['out'], '') or ''
            for _, ifx in pairs(portsgrp) do
                local portinfo = mydb.getport(ifx)
                if portinfo['mytype'] == 0x10 then
                    return luci.http.write_json({hdr = {code = 100, message = "Cannot configure member interface of port-channel!", type = "fail"}})
                end

                aclifdata['ifx'] = ifx
                if not setaclif(aclifdata) then
                    return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                end
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local acliftbl = getacliftbl()
    for ifx, aclif in ipairs(acliftbl) do
        local aclifdata = {}
        aclifdata['id'] = tonumber(aclif['ifx'])
        aclifdata['name'] = aclif['name']
        aclifdata['in'] = aclif['in']
        aclifdata['out'] = aclif['out']
        table.insert(destbl, aclifdata)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv('REQUEST_METHOD') == 'POST' then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['info']['type']) == "string", "type is error")
        assert(type(params['info']['name']) == "string", "name is error")

        local info = params['info']
        local oper = params['oper'] or ''

        if not tools.range_hit(string.len(info['name']), 1, 64) or (string.match(info['name'], "^%d") and not tonumber(info['name'])) then
            return luci.http.write_json({hdr = {code = 100, message = "Parameter name is invalid.", type = "fail"}})
        end

        local acldata = {}
        acldata['name'] = info['name']
        acldata['acltype'] = info['type']
        acldata['sn'] = 0
        if oper == "del" then
            -- del ACL, SN must be 0
            oper = 2
        elseif oper == "clear" then
            -- reset ACL counters
            oper = 4
        else
            -- add/update ACL
            acldata['desc'] = tools.valfilter(info['desc'], '') or ''
            acldata['cntflag'] = tools.bool_trans(info['cnt_enable'])
            acldata['reseq_start'] = tools.valfilter(info['reseq_start'], 10) or 10
            acldata['reseq_step'] = tools.valfilter(info['reseq_step'], 10) or 10
        end

        if not setacl(acldata, oper) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})    
    end

    local destbl = {}
    local acltbl = getacltbl()
    for _, acl in ipairs(acltbl) do
        local acldata = {}
        acldata['name'] = acl['name']
        acldata['type'] = acl["acltype"]
        acldata['desc'] = acl["desc"]
        acldata['cnt_enable'] = tools.bool_trans(acl["cntflag"])
        acldata['reseq_start'] = tonumber(acl["reseq_start"])
        acldata['reseq_step'] = tonumber(acl["reseq_step"])
        table.insert(destbl, acldata)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_rules()
    luci.http.prepare_content("application/json")
    if luci.http.getenv('REQUEST_METHOD') == 'POST' then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['info']['type']) == "string", "type is error")
        assert(type(params['info']['name']) == "string", "name is error")

        local info = params['info']
        local rules = info['rules'] or {}
        local oper = params['oper'] or ''

        if not tools.range_hit(string.len(info['name']), 1, 64) or (string.match(info['name'], "^%d") and not tonumber(info['name'])) then
            return luci.http.write_json({hdr = {code = 100, message = "Parameter name is invalid.", type = "fail"}})
        end

        if #rules > 128 then
            return luci.http.write_json({hdr = {code = 100, message = "A maximum of 128 rules can be configured under a single ACL-ID!", type = "fail"}})
        end

        if oper == "del" then oper = 2 end
        local acldata = {}
        local acltbl = getacltbl()
        for _, v in ipairs(acltbl) do
            if v['name'] and v['name'] == info['name'] and v['acltype'] == info['type'] then
                acldata['name'] = v['name']
                acldata['acltype'] = v['acltype']
                acldata["desc"] = v["desc"]
                acldata["cntflag"] = v["cntflag"]
                acldata["reseq_start"] = v["reseq_start"]
                acldata["reseq_step"] = v["reseq_step"]
            end
        end

        if not acldata['name'] then return luci.http.write_json({hdr = {code = 100, message = "Parameter name is invalid.", type = "fail"}}) end

        local acl = getacl(info['name'])
        for _, rule in ipairs(rules) do
            acldata['sn'] = tools.valfilter(rule['sn'], '') or ''
            acldata['control'] = tools.valfilter(rule['control'], '') or ''
            acldata['proto'] = tools.valfilter(rule['proto'], 'any') or 'any'
            acldata['src'] = tools.valfilter(rule['src'], '') or ''
            acldata['srcmsk'] = tools.valfilter(rule['src_mask'], '') or ''
            acldata['sport'] = tools.valfilter(rule['sport'], '') or ''
            acldata['dst'] = tools.valfilter(rule['dst'], '') or ''
            acldata['dstmsk'] = tools.valfilter(rule['dst_mask'], '') or ''
            acldata['dport'] = tools.valfilter(rule['dport'], '') or ''
            acldata["ethertype"] = tonumber(tools.valfilter(rule['ethertype'], '')) or 65536
            acldata["cos"] = tonumber(tools.valfilter(rule['cos'], '')) or -1
            if not setacl(acldata, oper) then
                return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local acldata = {}
    local name = luci.http.formvalue('name') or ""
    local type = luci.http.formvalue('type') or ""
    local acl = getacl(name)
    acldata['name'] = name
    acldata['type'] = type
    acldata['rules'] = {}
    if type == acl['acltype'] then 
        for k, v in ipairs(acl["rules"]) do
            acldata['rules'][k] = { sn = tonumber(v['sn']), control = v['control'], proto = v['proto'], src = v['src'], src_mask = v['srcmsk'], sport = v['sport'], dst = v['dst'], 
                                    dst_mask = v['dstmsk'], dport = v['dport'], ethertype = (tonumber(v['ethertype']) == 65536 and "" or string.format("0x%04x", v['ethertype'])), 
                                    cos = (tonumber(v['cos']) == -1 and "" or tonumber(v['cos'])), counters = v['cnt'] }
        end
    end

    acldata['rules'] = tools.array_check(acldata['rules'])

    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = acldata})
end
