local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"
local comdb = require "luci.controller.lib.comdb"
local vlandb = require "luci.controller.lib.vlandb"
module("luci.controller.api.port", package.seeall)

function index()
    entry({"api", "port"}, alias("api", "port", "info"), nil).hidden = true
    entry({"api", "port", "info"}, call("handle_info"), nil).leaf = true
    entry({"api", "port", "stat"}, call("handle_statistics"), nil).leaf = true
    entry({"api", "port", "conf"}, call("handle_config"), nil).leaf = true
    entry({"api", "port", "ratelimit"}, call("handle_ratelimit"), nil).leaf = true
    entry({"api", "port", "storm"}, call("handle_storm"), nil).leaf = true
    entry({"api", "port", "mirror"}, call("handle_mirror"), nil).leaf = true
    entry({"api", "port", "isolate"}, call("handle_isolate"), nil).leaf = true
    entry({"api", "port", "aggconf"}, call("handle_aggconf"), nil).leaf = true
    entry({"api", "port", "aggport"}, call("handle_aggport"), nil).leaf = true
end

function adminshuttrans(val)
    local data = {}
    data["No shutdown"] = "1"
    data["Shutdown"] = "2"
    data["1"] = "No shutdown"
    data["2"] = "Shutdown"
    return data[val]
end

function modetrans(pmode, type)
    local data1 = {}
    -- data1["SVI"] = "0"
    data1["Access"] = "1"
    data1["Hybrid"] = "2"
    data1["Trunk"] = "3"
    data1["L3"] = "100"
    data1["SVI"] = ""
    data1["1"] = "Access"
    data1["2"] = "Hybrid"
    data1["3"] = "Trunk"
    data1["100"] = "L3"
    local data2 = {}
    data2['1'] = "L3"
    data2['4'] = "SVI"
    return data1[tostring(pmode)] or data2[tostring(type)]
end

function getportmodetbl(data)
    local tbl = {}
    -- if bit.band(data["mode_ability"], 0x1) == 0x1 then table.insert(tbl, {name = "QSGMII", autoneg = bit.band(data["autoneg_ability"], 0x1) == 0x1}) end
    if bit.band(data["mode_ability"], 0x2) == 0x2 then table.insert(tbl, {name = "1000BASE-X", autoneg = bit.band(data["autoneg_ability"], 0x2) == 0x2}) end
    -- if bit.band(data["mode_ability"], 0x4) == 0x4 then table.insert(tbl, {name = "CASCADE", autoneg = bit.band(data["autoneg_ability"], 0x4) == 0x4}) end
    if bit.band(data["mode_ability"], 0x8) == 0x8 then table.insert(tbl, {name = "SGMII", autoneg = bit.band(data["autoneg_ability"], 0x8) == 0x8}) end
    -- if bit.band(data["mode_ability"], 0x10) == 0x10 then table.insert(tbl, {name = "XGMII", autoneg = bit.band(data["autoneg_ability"], 0x10) == 0x10}) end
    if bit.band(data["mode_ability"], 0x20) == 0x20 then table.insert(tbl, {name = "2500BASE-X", autoneg = bit.band(data["autoneg_ability"], 0x20) == 0x20}) end
    if bit.band(data["mode_ability"], 0x40) == 0x40 then table.insert(tbl, {name = "10GBASE-X", autoneg = bit.band(data["autoneg_ability"], 0x40) == 0x40}) end
    if bit.band(data["mode_ability"], 0x80) == 0x80 then table.insert(tbl, {name = "100BASE-FX", autoneg = bit.band(data["autoneg_ability"], 0x80) == 0x80}) end
    -- if bit.band(data["mode_ability"], 0x100) == 0x100 then table.insert(tbl, {name = "10G-KR", autoneg = bit.band(data["autoneg_ability"], 0x100) == 0x100}) end

    return tbl
end

function dhcptrans(data)
    local tbl = {}
    tbl["1"] = false
    tbl["2"] = true
    tbl["false"] = "1"
    tbl["true"] = "2"
    return tbl[tostring(data)]
end

function handle_info()
    luci.http.prepare_content("application/json")
    local destbl = {}
    local portinfotbl = comdb.com_getall("oltmib_nsm_get_1", "/nsm/portinfo", 4)
    for _, portinfo in pairs(portinfotbl) do
        local row = {}
        row['id'] = tonumber(portinfo['id'])
        row['name'] = portinfo['name']
        row['mtype'] = mydb.mediumtrans(portinfo['mtype'])
        row['mstate'] = mydb.mediumtrans(portinfo['mstate'])
        row['state'] = mydb.port_statetrans(portinfo['state'])
        row['adminstate'] = adminshuttrans(portinfo['adminstate'])
        row['aggid'] = tonumber(portinfo['aggid'])
        row['pmode'] = modetrans(portinfo['pmode'], portinfo['ptype'])
        row['ingress'] = (tonumber(portinfo['ingress']) or 0) * 8
        row['egress'] = (tonumber(portinfo['egress']) or 0) * 8
        if row['pmode'] ~= "SVI" then table.insert(destbl, row) end
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        if params['info']['desc'] and not tools.range_hit(#params['info']['desc'], 0, 80) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end

        local portsgrp = params['ports'] or {}
        local info = params['info'] or {}
        local oper = params['oper'] or ""
        local conftbl = {}
        conftbl['desc'] = tools.valfilter(info['desc'], "")
        conftbl['pmode'] = tools.valfilter(info['pmode'], "Access")
        conftbl['pmode'] = modetrans(conftbl['pmode'])
        conftbl['pvid'] = tools.valfilter(info['pvid'], "1")
        conftbl['allowvlan'] = tools.valfilter(info['allowvlan'], '')
        conftbl['ip4_dhcp'] = dhcptrans(info['ip4_dhcp'])
        conftbl['ip4'] = tools.valfilter(info['ip4'], '')
        conftbl['prefix4'] = tools.valfilter(info['prefix4'], '')
        conftbl['ip6_dhcp'] = dhcptrans(info['ip6_dhcp'])
        conftbl['ip6'] = tools.valfilter(info['ip6'], '')
        conftbl['prefix6'] = tools.valfilter(info['prefix6'], '')
        conftbl['mtype'] = info['mtype'] and mydb.mediumtrans(info['mtype'])
        conftbl['speed'] =  info['speed'] and mydb.bwtrans(info['speed'])
        conftbl['duplex'] = info['duplex'] and mydb.duplextrans(info['duplex'])
        conftbl['fc'] = info['fc'] and mydb.fctrans(info['fc'])
        conftbl['mtu'] = tools.valfilter(info['mtu'], "1500")
        conftbl['adminstate'] = tools.valfilter(info['adminstate'], "No shutdown")
        conftbl['adminstate'] = adminshuttrans(info['adminstate'])
        conftbl['untagvlan'] = tools.valfilter(info['untaggedvlan'], '')

        local data = {}
        if info['pmode'] and info['pmode'] == "SVI" then    -- pmode = SVI
            assert(conftbl['pvid'], "invalid pvid")

            local str = "type=port;pvid=" .. conftbl['pvid'] .. ";ptype=4"
            if oper ~= "del" then    -- update
                if conftbl['ip4_dhcp'] then str = str .. ";ip4_dhcp=" .. conftbl['ip4_dhcp'] end
                if conftbl['ip4'] and conftbl['prefix4'] then str = str .. ";ip4=" .. conftbl['ip4'] .. ";prefix4=" .. conftbl['prefix4'] end
                if conftbl['ip6_dhcp'] then str = str .. ";ip6_dhcp=" .. conftbl['ip6_dhcp'] end
                if conftbl['ip6'] and conftbl['prefix6'] then str = str .. ";ip6=" .. conftbl['ip6'] .. ";prefix6=" .. conftbl['prefix6'] end
            else
                oper = "2"
            end
            table.insert(data, str)
        else                                                -- pmode = phy || ap || apmen
            for _, ifx in ipairs(portsgrp) do
                local str = "type=port;id=".. ifx
                if oper == "del" then
                    if  conftbl['pmode'] then str = str .. ";pmode=" .. conftbl['pmode'] end
                    if  conftbl['pvid'] then str = str .. ";pvid=" .. conftbl['pvid'] end
                else
                    if conftbl['desc'] then str = str .. ";desc=" .. conftbl['desc'] end
                    if conftbl['adminstate'] then str = str .. ";adminstate=" .. conftbl['adminstate'] end
                    if conftbl['mtype'] then str = str .. ";mtype=" .. conftbl['mtype'] end
                    if conftbl['speed'] then str = str .. ";speed=" .. conftbl['speed'] end
                    if conftbl['duplex'] then str = str .. ";duplex=" .. conftbl['duplex'] end
                    if conftbl['fc'] then str = str .. ";fc=" .. conftbl['fc'] end
                    if conftbl['mtu'] then str = str .. ";mtu=" .. conftbl['mtu'] end
                    if conftbl['pmode'] then str = str ..";pmode=" .. conftbl['pmode'] end
                    if conftbl['ip4_dhcp'] then str = str .. ";ip4_dhcp=" ..  conftbl['ip4_dhcp'] end
                    if conftbl['ip6_dhcp'] then str = str .. ";ip6_dhcp=" ..  conftbl['ip6_dhcp'] end
                    if conftbl['ip4'] and conftbl['prefix4'] then str = str .. ";ip4=" .. conftbl['ip4'] .. ";prefix4=" .. conftbl['prefix4'] end
                    if conftbl['ip6'] and conftbl['prefix6'] then str = str .. ";ip6=" .. conftbl['ip6'] .. ";prefix6=" .. conftbl['prefix6'] end
                    if conftbl['pvid'] then str = str .. ";pvid=" .. conftbl['pvid'] end
                    if conftbl['allowvlan'] and (conftbl['pmode'] == "2" or conftbl['pmode'] == "3") then
                        str = str .. ";allowvlan=" .. conftbl['allowvlan']
                    end
                    if conftbl['untagvlan'] and conftbl['pmode'] == "2" then
                        str = str .. ";untagvlan=" .. conftbl['untagvlan']
                    end
                    table.insert(data, str)

                    local portinfo = mydb.getport(tostring(ifx))
                    if info['fspeed'] or info['autoneg'] then
                        portinfo['Portmode'] = info['fspeed'] or portinfo['Portmode']
                        portinfo['Inband'] = info['autoneg'] or portinfo['Inband']
                        if info['fspeed'] then portinfo['mode_flag'] = 1 end
                        if not mydb.setintfmode(portinfo) then
                            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                        end
                    end
                end
            end
        end

        if not comdb.com_setall("oltmib_nsm_set_1", "/nsm/portconf", data, 3, oper) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local porttbl = mydb.getporttable(27)
    local portconftbl = comdb.com_getall("oltmib_nsm_get_1", "/nsm/portconf", 2)
    for _, v in ipairs(portconftbl) do
        local row = {}
        row['id'] = tonumber(v['id'])
        row['name'] = v['name']
        row['desc'] = v['desc']
        row['pmode'] = modetrans(v['pmode'], v['ptype'])
        row['pvid'] = tonumber(v['pvid'])
        if row['pmode'] == "SVI" then
            row['pvid'] = tonumber(string.match(row['name'], "%d+"))
        end
        row['allowvlan'] = v['allowvlan']
        row['untaggedvlan'] = v['untagvlan']
        row['ip4_dhcp'] = dhcptrans(v['ip4_dhcp'])
        row['ip4'] = v['ip4']
        row['prefix4'] = tonumber(v['prefix4'])
        row['ip6_dhcp'] = dhcptrans(v['ip6_dhcp'])
        row['ip6'] = v['ip6']
        row['prefix6'] = tonumber(v['prefix6'])
        row['mtype'] = mydb.mediumtrans(v['mtype'])
        row['mstate'] = mydb.mediumtrans(v['mstate'])
        row['speed'] = mydb.bwtrans(v['speed'])
        row['duplex'] = mydb.duplextrans(v['duplex'])
        row['ability'] = mydb.getmediumopts({if_attr_flags = v['ability']})
        for _, opt in ipairs( mydb.getbwopts({if_attr_flags = v['ability']}) ) do
            table.insert(row['ability'], opt)
        end
        for _, opt in ipairs( mydb.getduplexopts({if_attr_flags = v['ability']}) ) do
            table.insert(row['ability'], opt)
        end
        for _, opt in ipairs( mydb.getfcopts({if_attr_flags = v['ability']}) ) do
            table.insert(row['ability'], opt)
        end
        row['ability'] = tools.array_check(row['ability'])

        row['mode_ability'] = {}
        for _, info in ipairs(porttbl) do
            if v['id'] == info['Index'] then
                row['fspeed'] = info['Portmode']
                row['autoneg'] = info['Inband']
                for _, opt in ipairs( getportmodetbl({mode_ability = info['mode_ability'], autoneg_ability = info['autoneg_ability']}) ) do
                    table.insert(row['mode_ability'], opt)
                end
            end
        end
        row['mode_ability'] = tools.array_check(row['mode_ability'])

        row['fc'] = mydb.fctrans(v['fc'])
        row['mtu'] = tonumber(v["mtu"])
        row['adminstate'] = adminshuttrans(v['adminstate'])
        table.insert(destbl, row)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_statistics()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['ports']) == "table", "ports is error")

        local portsgrp = params['ports']
        local oper = params['oper']
        if oper == 'clear' then
            if next(portsgrp) then
                for _, v in ipairs(portsgrp) do
                    local portstat = mydb.getport(v)
                    mydb.setportstat(portstat)
                end
            else
                -- delete all port
                local porttbl = mydb.getporttable(27)
                for _, v in ipairs(porttbl) do
                    local portstat = mydb.getport(v['Index'])
                    mydb.setportstat(portstat)
                end
            end

            return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
        end
    end

    local destbl = {}
    local porttbl = mydb.getporttable(27)
    local portstattbl = mydb.getportstattbl(27)
    for _, v in pairs(portstattbl) do
        local mtbl = {}
        mtbl['id'] = tonumber(v['Index'])
        mtbl['name'] = v['Name']
        mtbl['undersize'] = v['Undersize']
        mtbl['oversize'] = v['Oversize']
        mtbl['crc'] = v['Crc']
        mtbl['collision'] = v['Collision']
        mtbl['rxload'] = 0
        mtbl['txload'] = 0
        mtbl['speed'] = ''
        mtbl['state'] = 'Down'
        for _, p in pairs(porttbl) do
            if v['Index'] == p['Index'] then
                local speed = tonumber(string.match(p['Speed'], "%d+") or '0')
                mtbl['state'] = p['State']
                mtbl['duplex'] = p['Duplex']
                if speed > 1000000000 then
                    mtbl['speed'] = tostring(speed / 1000000000) .. 'G'
                else
                    mtbl['speed'] = tostring(speed / 1000000) .. 'M'
                end

                if speed ~= 0 then
                    mtbl['rxload'] = (tonumber(v['Rxbps']) + tonumber(v['Rxpps']) * 20 * 8) * 100 / speed
                    mtbl['rxload'] = tonumber(string.format("%.2f", mtbl['rxload']))
                    mtbl['rxload'] = (mtbl['rxload'] > 100) and 100 or mtbl['rxload']
                    mtbl['txload'] = (tonumber(v['Txbps']) + tonumber(v['Txpps']) * 20 * 8) * 100 / speed
                    mtbl['txload'] = tonumber(string.format("%.2f", mtbl['txload']))
                    mtbl['txload'] = (mtbl['txload'] > 100) and 100 or mtbl['txload']
                end
            end
        end

        table.insert(destbl, mtbl)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_ratelimit()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['ports']) == "table", "ports is error")
        assert(type(params['info']['incir']) == "number" and (params['info']['incir'] > 63 and params['info']['incir'] <= 1000000 or params['info']['incir'] == 0), "incir is error")
        assert(type(params['info']['incbs']) == "number" and (params['info']['incbs'] > 31 and params['info']['incbs'] <= 16384 or params['info']['incbs'] == 0), "incbs is error")
        assert(type(params['info']['outcir']) == "number" and (params['info']['outcir'] > 63 and params['info']['outcir'] <= 1000000 or params['info']['outcir'] == 0), "outcir is error")
        assert(type(params['info']['outcbs']) == "number" and (params['info']['outcbs'] > 31 and params['info']['outcbs'] <= 16384 or params['info']['outcbs'] == 0), "outcbs is error")

        local info = params['info']
        local portsgrp = params['ports']
        local info_incir, info_incbs = tostring(info['incir']), tostring(info['incbs'])
        local info_outcir, info_outcbs =  tostring(info['outcir']), tostring(info['outcbs'])
        local ratelimittbl = mydb.getratelimittbl()
        for _, v in ipairs(portsgrp) do
            local ntbl = {}
            ntbl['ifx'] = tostring(v)
            ntbl['in_cir'] = info_incir
            ntbl['in_cbs'] = info_incbs
            ntbl['out_cir'] = info_outcir
            ntbl['out_cbs'] = info_outcbs
            ntbl['name'] = ''
            for _, p in pairs(ratelimittbl) do
                if ntbl['ifx'] == p['ifx'] then
                    ntbl['name'] = p['name']
                end
            end
            mydb.setratelimit(ntbl)
        end
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local porttbl = mydb.getporttable(27)
    local ratelimittbl = mydb.getratelimittbl()
    for _, v in pairs(ratelimittbl) do
        local mtbl = {}
        mtbl['id'] = tonumber(v['ifx'])
        mtbl['incir'] = tonumber(v['in_cir'])
        mtbl['incbs'] = tonumber(v['in_cbs'])
        mtbl['outcir'] = tonumber(v['out_cir'])
        mtbl['outcbs'] = tonumber(v['out_cbs'])
        mtbl['name'] = v['name']
        mtbl['state'] = 'down'
        for _, p in pairs(porttbl) do
            if p['Index'] == v['ifx'] then
                mtbl['state'] = p['State']
            end
        end

        table.insert(destbl, mtbl)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_storm()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['ports']) == "table", "ports is error")
        assert(type(params['info']['type']) == "string", "type is error")
        assert(type(params['info']['percent']) == "nil" or (type(params['info']['percent']) == "number" and (params['info']['percent'] >= 0 and params['info']['percent'] <= 100)), "percent is error")

        local info = params['info']
        local portsgrp = params['ports']
        local percent = tostring(info['percent'] or 0)
        local stormctrltbl = mydb.getstormcontroltbl()
        for _, v in ipairs(portsgrp) do
            local ntbl = {}
            ntbl['ifx'] = tostring(v)
            for _, p in pairs(stormctrltbl) do
                if ntbl['ifx'] == p['ifx'] then
                    ntbl['name'] = p['name']
                    ntbl['type'] = info['type']
                    ntbl['value'] = percent
                end
            end
            mydb.setstormcontrol(ntbl)
        end
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local stormctrltbl = mydb.getstormcontroltbl()
    for _, v in pairs(stormctrltbl) do
        local mtbl = {}
        mtbl['id'] = tonumber(v['ifx'])
        mtbl['name'] = v['name']
        mtbl['type'] = v['type']
        mtbl['percent'] = v['value']
        table.insert(destbl, mtbl)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_mirror()
    local mirrorcap = mydb.getdevcapint("PROD_UD_CLASS", "mirror_cap") or 7
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['id']) == "number" and (params['id'] >= 1 and params['id'] <= mirrorcap), "id is error")

        local mirror = {}
        mirror['sid'] = tostring(params['id'])
        mirror['mode'] = params['mode']
        mirror['desc'] = params['desc']
        mirror['to'] = params['dst']
        mirror['to_switch'] = tools.bool_trans(params['switch'])
        mirror['rspan_vlan'] = params['remote_vlan']
        mirror['src_rx'] = table.concat(params['src_rx'] or {}, ',')
        mirror['src_tx'] = table.concat(params['src_tx'] or {}, ',')
        mirror['src_vlan'] = tools.str2array(params['src_vlan'] or "")
        if (#mirror['src_vlan'] > 8) then return luci.http.write_json({hdr = {code = 1000, message = "The number of VLANs cannot exceed 8.", type = "fail"}}) end
        mirror['src_vlan'] = tools.array2str(mirror['src_vlan'])
        if params['oper'] == 'del' then
            mirror['oper'] = '2'
        end

        if not mydb.setmirror(mirror) then return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}}) end
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local mirrortbl = mydb.getmirrortbl()
    for k = 1, mirrorcap, 1 do
        local row = {}
        row['id'] = k
        row['dst'] = ''
        row['src_rx'] = {}
        row['src_tx'] = {}
        for _, mirror in pairs(mirrortbl) do
            if row['id'] == tonumber(mirror['sid']) then
                row['mode'] = mirror['mode']
                row['desc'] = mirror['desc']
                row['dst'] = mirror['to']
                row['switch'] = tools.bool_trans(mirror['to_switch'])
                row['remote_vlan'] = tonumber(mirror['rspan_vlan']) ~= 0 and tonumber(mirror['rspan_vlan']) or nil
                row['src_rx'] = mirror['src_rx'] == "" and row['src_rx'] or string.split(mirror['src_rx'], ",")
                row['src_tx'] = mirror['src_tx'] == "" and row['src_tx'] or string.split(mirror['src_tx'], ",")
                row['src_vlan'] = tools.array2str(tools.str2array(mirror['src_vlan'] or ""))
            end
        end

        row['src_rx'] = tools.array_check(row['src_rx'])
        row['src_tx'] = tools.array_check(row['src_tx'])
        table.insert(destbl, row)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_isolate()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['ports']) == "table", "ports is error")
        assert(type(params['info']['enable']) == "boolean", "enable is error")

        local message = ""
        local info = params['info']
        local portsgrp = params['ports']
        local isolate_en = info['enable'] and '1' or '0'
        for _, v in ipairs(portsgrp) do
            local ntbl = mydb.getport(v)
            if ntbl['mytype'] == 0x10 then
                return luci.http.write_json({hdr = {code = 100, message = "Cannot configure member interface of port-channel! ( " .. ntbl['Name'] .. " )", type = "fail"}})
            end
            ntbl['Isolate'] = isolate_en
            ntbl['Tagvlan'] = ""
            ntbl['Untagvlan'] = ""
            mydb.setport(ntbl)
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local porttbl = mydb.getporttable(11)
    for _, v in pairs(porttbl) do
        local mtbl = {}
        mtbl['id'] = tonumber(v['Index'])
        mtbl['name'] = v['Name']
        mtbl['enable'] = v['Isolate'] ~= '0'
        table.insert(destbl, mtbl)
    end

    local data = {data = destbl}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

-- ['nameprefix'] , ['maxid'] are magic numbers
function handle_aggconf()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['alg']) == "string", "alg is error")

        local ntbl = {}
        ntbl['value'] = params['alg']
        if not mydb.setagsys(ntbl) then
            return luci.http.write_json({hdr = {code = 100, message = "Set port-channel load-balance " .. params['alg'] .." fail", type = "fail"}})
        end
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local agsys = mydb.getagsys()
    for _, v in pairs(agsys) do
        destbl['alg'] = v['value']
        destbl['nameprefix'] = 'po'
        destbl['maxid'] = mydb.getdevcapint("PROD_UD_SPEC", "ap.ap_cap") or 12
    end

    local data = destbl
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_aggport()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")

        local info = params['info']
        local aggs = params['aggs'] or {}
        local agtbl = mydb.getagtbl()
        if info['delete'] == true then
            for _, v in ipairs(aggs) do
                local ntbl = {}
                ntbl['oper'] = '2'
                ntbl['key'] = tostring(v)
                for _, p in pairs(agtbl) do
                    if ntbl['key'] == p['key'] then
                        ntbl['ifx'] = p['ifx']
                        mydb.setag(ntbl)
                    end
                end
            end
            return luci.http.write_json({hdr = {code = 0, message = "Given parameters are invalid!", type = "success"}})
        else
            assert(type(params['ports']) == "table" or type(params['ports']) == "nil", "ports is error")
            assert(type(info['id']) == "number", "id is error")
            assert(type(info['mode']) == "string", "mode is error")

            local ack = true
            local portsgrp = params['ports'] or {}
            local ntbl = {}
            ntbl['oper'] = '2'
            ntbl['key'] = tostring(info['id'])
            for _, v in pairs(agtbl) do
                if ntbl['key'] == v['key'] then
                    ntbl['ifx'] = v['ifx']
                    ntbl['mode'] = v['mode']
                    mydb.setag(ntbl)
                end
            end

            ntbl['oper'] = '1'
            ntbl['mode'] = info['mode']
            for _, v in ipairs(portsgrp) do
                ntbl['ifx'] = tostring(v)
                ack = mydb.setag(ntbl) and ack
            end

            if not ack then return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}}) end
            return luci.http.write_json({hdr = {code = 0, message = "edit complete", type = "success"}})
        end
    end

    local destbl = {}
    local agtbl = mydb.getagtbl()
    for _, v in pairs(agtbl) do
        local mtbl = {}
        mtbl['id'] = tonumber(v['ifx'])
        mtbl['name'] = v['name']
        mtbl['aggid'] = v['key'] ~= '-' and tonumber(v['key']) or 0
        mtbl['aggmode'] = v['mode']
        table.insert(destbl, mtbl)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
