local librpc = require "librpc"
local table = require "table"
local string = require "string"
local os = require "os"
local util = require "luci.util"
local json = require "luci.json"
local tostring = tostring
local tonumber = tonumber
local pairs = pairs
local ipairs = ipairs
local next = next
local bit = bit
local math = math
local type = type
local translate = luci.i18n.translate
local exec = luci.sys.exec
local io = io
local setmetatable = setmetatable
local getmetatable = getmetatable
local assert = assert
local tools = require "luci.controller.lib.tools"

module "luci.mydb"

local vlanfmt = "Index Name State tagmbr untagmbr"
local portfmt = "Name Mode NativeVLAN AllowVLAN Speed Adminshut State"
local erpsinstfmt = "Name ID Ring Level RAPSvlan OwnerInterface"
local erpsringfmt = "Index EASTInterface WESTInterface"
local aclfmt = "name acltype extflag rules"
local ipchangefile = "/tmp/.ipchanged"

function dbgprint(str, more)
    local truncate = (more or 1) == 0
    local fd = io.open("/luci/tmp", "a+")
    if fd ~= nil then
        local s = tostring(str)
        if truncate and #s > 80 then
            s = string.sub(s, 1, 80) .. " ...(more)"
        end
        fd:write(s .. "\n")
        fd:close()
    end
end

function dbgtprint(t, loop, offset, more)
    local recursive = loop or 1
    local indent = offset or 0
    local space = string.rep(" ", indent)
    local detail = more or 0
    for i, v in pairs(t) do
        if type(v) == "table" then
            dbgprint(space .. "[" .. i .. "]: table - recursive " .. recursive)
            if recursive == 1 then
                dbgtprint(v, 1, indent + 4, detail)-- always recursive
            end
        else if type(v) == "boolean" or type(v) == "number" or type(v) == "string" then
                dbgprint(space .. "[" .. i .. "]: " .. type(v) .. " - " .. tostring(v), detail)
            end
        end
    end
end

function trim(str)
    return (string.gsub(str, "^%s*(.-)%s*$", "%1"))
end

function copy3(obj, seen)
    -- Handle non-tables and previously-seen tables.
    if type(obj) ~= 'table' then return obj end
    if seen and seen[obj] then return seen[obj] end

    -- New table; mark it as seen an copy recursively.
    local s = seen or {}
    local res = setmetatable({}, getmetatable(obj))
    s[obj] = res
    for k, v in pairs(obj) do res[copy3(k, s)] = copy3(v, s) end
    return res
end

function hex2bin(str)
    return (str:gsub('..', function(cc) return string.char(tonumber(cc, 16)) end))
end

function bin2hex(str)
    return (str:gsub('.', function(c) return string.format('%02X', string.byte(c)) end))
end

--[[
    function ipchangefileexist()
        local f = io.open(ipchangefile, "r")
        if f then f:close() end
        return f ~= nil
    end

    function clearipchangefile()
        os.execute("rm -f " .. ipchangefile)
    end
]]--


--[[
function writecfg()
    str = "&&&&&&1"
    result = librpc.callapi("oltmib_devinfo_set_1", str)
    clearipchangefile()
end
]]--

function genemptydata(rownum, fmt)
    local data = {}
    for i = 1, rownum do
        local row = {}
        for col in fmt:gmatch("[^%s]+") do
            row[col] = ""
        end
        table.insert(data, row)
    end

    return data
end

function millifmt(v)
    v = tonumber(v)
    local v_i = math.floor(v)
    local v_d = v - v_i
    local s = string.format("%d", v_i)
    local pos = string.len(s) % 3
    if pos == 0 then
        pos = 3
    end
    if v_d ~= 0 then -- decimal
        return string.sub(s, 1, pos)
        .. string.gsub(string.sub(s, pos + 1), "(...)", ",%1")
        .. string.sub(string.format("%.2f", v_d), 2)
    else -- integer
        return string.sub(s, 1, pos)
        .. string.gsub(string.sub(s, pos + 1), "(...)", ",%1")
    end
end

function hexstrreverse(str)
    local num = #str / 2
    local revstr = ""
    for i = 1, num do
        revstr = string.sub(str, 2 * i - 1, 2 * i) .. revstr
    end
    return revstr
end

function datalst_trans(val)-- replace ' ' by ','  delete extra ','
    local s = val
    s = string.gsub(s, " ", ",")
    s = string.gsub(s, "^,+", "")
    s = string.gsub(s, ",+$", "")
    s = string.gsub(s, ",,+", ",")
    return s
end

function mac_trans(val)-- replace ' ' by ','  delete extra ','
    local s = val
    s = string.gsub(s, "%.", "")
    s = string.gsub(s, "-", "")
    s = string.gsub(s, ":", "")
    return string.lower(s)
end

function ip2str(val)
    val = tonumber(val)
    return bit.band(bit.rshift(val, 24), 255) .. "." .. bit.band(bit.rshift(val, 16), 255) .. "." .. bit.band(bit.rshift(val, 8), 255) .. "." .. bit.band(bit.rshift(val, 0), 255)
end

function str2ip(val)
    local num = string.split(val, ".")
    if #num == 4 then
        return bit.lshift(tonumber(num[1]), 24) + bit.lshift(tonumber(num[2]), 16) + bit.lshift(tonumber(num[3]), 8) + tonumber(num[4])
    end
    return -1
end

function bool_str()
    return { "False", "True" }
end
function bool_trans(val)
    local trans = {}
    trans["0"] = "False"
    trans["1"] = "True"
    trans["False"] = "0"
    trans["True"] = "1"
    return trans[val] or "-"
end
function bool2int(val)
    return val and 1 or 0
end

function ablity_str()
    return { "Disabled", "Enabled" }
end
function ablity_trans(val)
    local trans = {}
    trans["0"] = "Disabled"
    trans["1"] = "Enabled"
    trans["Disabled"] = "0"
    trans["Enabled"] = "1"
    return trans[val] or "-"
end

function linkstate_trans(val)
    local trans = {}
    trans["0"] = "Down"
    trans["1"] = "Up"
    trans["Down"] = "0"
    trans["Up"] = "1"
    return trans[val] or "-"
end

function port_modetrans(val)
    local data = {}
    data["Invalid"] = "0"
    data["Access"] = "1"
    data["Hybrid"] = "2"
    data["Trunk"] = "3"
    data["0"] = "Invalid"
    data["1"] = "Access"
    data["2"] = "Hybrid"
    data["3"] = "Trunk"
    return data[val] or ""
end

function port_intfmodetrans(val)
    local data = {}
    --data["QSGMII"] = "0"
    data["1000BASE-X"] = "1"
    data["CASCADE"] = "2"
    data["SGMII"] = "3"
    data["XGMII"] = "4"
    data["2500BASE-X"] = "5"
    data["10GBASE-X"] = "6"
    data["100BASE-FX"] = "7"
    data["10G-KR"] = "8"
    --data["0"] = "QSGMII"
    data["1"] = "1000BASE-X"
    data["2"] = "CASCADE"
    data["3"] = "SGMII"
    data["4"] = "XGMII"
    data["5"] = "2500BASE-X"
    data["6"] = "10GBASE-X"
    data["7"] = "100BASE-FX"
    data["8"] = "10G-KR"
    return data[val] or ""
end

function port_inbandantrans(val)
    local data = {}
    -- data["OFF"] = "-1"
    data["OFF"] = "0"
    data["ON"] = "1"
    data["-1"] = "OFF"
    data["0"] = "OFF"
    data["1"] = "ON"
    return data[val] or ""
end

function port_adminshuttrans(val)
    local data = {}
    data["No shutdown"] = "0"
    data["Shutdown"] = "1"
    data["0"] = "No shutdown"
    data["1"] = "Shutdown"
    data[""] = ""
    return data[val] or ""
end

function port_statetrans(val)
    local data = {}
    data["Down"] = "0"
    data["Up"] = "1"
    data["0"] = "Down"
    data["1"] = "Up"
    data[""] = ""
    return data[val] or ""
end

function getpmode()
    return { "Trunk", "Access", "Hybrid" }
end

function getportmode(data)
    local tbl = {}
    -- if bit.band(data["mode_ability"], 0x1) == 0x1 then table.insert(tbl, "QSGMII") end
    if bit.band(data["mode_ability"], 2) == 2 then table.insert(tbl, "1000BASE-X") end
    -- if bit.band(data["mode_ability"], 0x4) == 0x4 then table.insert(tbl, "CASCADE") end
    if bit.band(data["mode_ability"], 8) == 8 then table.insert(tbl, "SGMII") end
    -- if bit.band(data["mode_ability"], 0x10) == 0x10 then table.insert(tbl, "XGMII") end
    if bit.band(data["mode_ability"], 32) == 32 then table.insert(tbl, "2500BASE-X") end
    if bit.band(data["mode_ability"], 64) == 64 then table.insert(tbl, "10GBASE-X") end
    if bit.band(data["mode_ability"], 128) == 128 then table.insert(tbl, "100BASE-FX") end
    -- if bit.band(data["mode_ability"], 0x100) == 0x100 then table.insert(tbl, "10G-KR") end
    return tbl
end

function mediumtrans(val)
    local data = {}
    data["INVALID"] = "-1"
    data["RJ45"] = "0"
    data["SFP"] = "1"
    data["AUTO_PREFER_RJ45"] = "2"
    data["AUTO_PREFER_SFP"] = "3"
    data["-1"] = "INVALID"
    data["0"] = "RJ45"
    data["1"] = "SFP"
    data['2'] = "AUTO_PREFER_RJ45"
    data["3"] = "AUTO_PREFER_SFP"
    return data[val] or ""
end
function getmediumopts(data)
    local tbl = {}
    if bit.band(data["if_attr_flags"], 256) == 256 then table.insert(tbl, "RJ45") end
    if bit.band(data["if_attr_flags"], 512) == 512 then table.insert(tbl, "SFP") end
    if bit.band(data["if_attr_flags"], 256) == 256 and bit.band(data["if_attr_flags"], 512) == 512 then
        table.insert(tbl, "AUTO_PREFER_RJ45")
        table.insert(tbl, "AUTO_PREFER_SFP")
    end
    return tbl
end

function duplextrans(val)
    local data = {}
    data["AUTO"] = "0"
    data["FULL"] = "1"
    data["HALF"] = "2"
    data["0"] = "AUTO"
    data["1"] = "FULL"
    data["2"] = "HALF"
    return data[val] or ""
end
function getduplexopts(data)
    local tbl = {}
    if bit.band(data["if_attr_flags"], 65536) == 65536 then table.insert(tbl, "AUTO") end
    if bit.band(data["if_attr_flags"], 131072) == 131072 then table.insert(tbl, "FULL") end
    if bit.band(data["if_attr_flags"], 262144) == 262144 then table.insert(tbl, "HALF") end
    return tbl
end

function bwtrans(val)
    local data = {}
    data["AUTO"] = "0"
    data["10M"] = "1"
    data["100M"] = "2"
    data["1000M"] = "3"
    --data["2500M"] = "4"
    data["10000M"] = "5"
    data["0"] = "AUTO"
    data["1"] = "10M"
    data["2"] = "100M"
    data["3"] = "1000M"
    --data["4"] = "2500M"
    data["5"] = "10000M"
    return data[val] or ""
end

function getbwopts(data)
    local tbl = {}
    if bit.band(data["if_attr_flags"], 1) == 1 then table.insert(tbl, "AUTO") end
    if bit.band(data["if_attr_flags"], 2) == 2 then table.insert(tbl, "10M") end
    if bit.band(data["if_attr_flags"], 4) == 4 then table.insert(tbl, "100M") end
    if bit.band(data["if_attr_flags"], 8) == 8 then table.insert(tbl, "1000M") end
    return tbl
end

function fctrans(val)
    local data = {}
    data["AUTO"] = "0"
    data["ON"] = "1"
    data["OFF"] = "2"
    data["0"] = "AUTO"
    data["1"] = "ON"
    data["2"] = "OFF"
    return data[val] or ""
end
function getfcopts(data)
    local tbl = {}
    if bit.band(data["if_attr_flags"], 16777216) == 16777216 then table.insert(tbl, "AUTO") end
    if bit.band(data["if_attr_flags"], 33554432) == 33554432 then table.insert(tbl, "ON") end
    if bit.band(data["if_attr_flags"], 67108864) == 67108864 then table.insert(tbl, "OFF") end
    return tbl
end

porttable = {}
function getporttable(filtertype)
    porttable = {}
    -- traverse port
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_portinfo_getn_1", str)
        _, _, ifx, name, desc, mytype, if_attr_flags, mode, nativevlan, tagvlan, untagvlan, mtype, mstate, conf_dp, duplex, conf_bw, speed, conf_fc, fc, admin_shutdown, state, mtu, isolate, msg, oper, result = string.find(str, string.rep("(.-)&", 23) .. "(.*)")
        if (result == "0" and (filtertype == nil or bit.band(tonumber(mytype), tonumber(filtertype)) ~= 0)) then
            local row = {}
            str2 = librpc.callapi("oltmib_portintfmode_get_1", ifx .. "&")
            _, _, _, _, intfmode, ability, autoneg_ability, _, _, _ = string.find(str2, string.rep("(.-)&", 7) .. "(.*)")
            str3 = librpc.callapi("oltmib_portinbandan_get_1", ifx .. "&")
            _, _, _, inbandan, _, _, _ = string.find(str3, string.rep("(.-)&", 4) .. "(.*)")
            row["Index"] = ifx
            row["Name"] = name
            row["Desc"] = desc
            row["mytype"] = tonumber(mytype)
            row["if_attr_flags"] = tonumber(if_attr_flags)
            row["mode_ability"] = tonumber(ability)
            row["autoneg_ability"] = tonumber(autoneg_ability)
            -- row["Medium"] = mediumtrans(medium)
            row["mtype"] = mediumtrans(mtype)
            row["mstate"] = mediumtrans(mstate)
            if row["mtype"] == "SFP" then
                row["Portmode"] = port_intfmodetrans(intfmode)
                row["Inband"] = port_inbandantrans(inbandan)
            else
                row["Portmode"] = ""
                row["Inband"] = ""
            end
            if mytype == "2" then
                row["Portmode"] = ""
                row["Medium"] = ""
                row["Inband"] = ""
            end
            row["Mode"] = port_modetrans(tostring(mode))
            row["NativeVLAN"] = tostring(nativevlan)
            row["Tagvlan"] = tostring(tagvlan)
            row["Untagvlan"] = tostring(untagvlan)
            row["Conf_dp"] = duplextrans(conf_dp)
            row["Conf_bw"] = bwtrans(conf_bw)
            row["Conf_fc"] = fctrans(conf_fc)
            row["Flowcontrol"] = fctrans(fc)
            row["MTU"] = mtu
            row["Isolate"] = isolate
            if admin_shutdown == "1" or state == "0" then
                row["Speed"] = "-"
                row["Duplex"] = "-"
            else
                row["Speed"] = tostring(tonumber(speed) * 8)
                row["Duplex"] = duplextrans(duplex)
            end
            if (admin_shutdown == "1") then
                row["State"] = "Down"
                row["Adminshut"] = "Shutdown"
            else
                row["State"] = port_statetrans(state)
                row["Adminshut"] = "No shutdown"
            end
            table.insert(porttable, row)-- add it in order for ipairs
        end
    end
    return porttable
end

function getportintbl(porttbl, ifx)
    for _, v in pairs(porttbl) do
        if v["Index"] == ifx then
            return v
        end
    end
    return nil
end

function getportintbl_by_name(porttbl, name)
    for _, v in pairs(porttbl) do
        if v["Name"] == name then
            return v
        end
    end
    return nil
end

function getportid(ifname)
    str = librpc.callapi("oltmib_portinfo_get_1", "&" .. ifname)
    _, _, ifx, name, desc, mytype, if_attr_flags, mode, nativevlan, tagvlan, untagvlan, mtype, mstate, conf_dp, duplex, conf_bw, speed, conf_fc, fc, admin_shutdown, state, mtu, isolate, msg, oper, result = string.find(str, string.rep("(.-)&", 23) .. "(.*)")
    if (result == "0") then
        return tostring(ifx)
    end

    return nil
end

function getport(index)
    index = datalst_trans(index)
    --dbgprint("getport index "..index.." number "..tonumber(index))
    if tonumber(index) == nil then
        return genemptydata(1, portfmt)[1]
    end
    local row = {}
    str = librpc.callapi("oltmib_portinfo_get_1", index .. "&")
    _, _, ifx, name, desc, mytype, if_attr_flags, mode, nativevlan, tagvlan, untagvlan, mtype, mstate, conf_dp, duplex, conf_bw, speed, conf_fc, fc, admin_shutdown, state, mtu, isolate, msg, oper, result = string.find(str, string.rep("(.-)&", 23) .. "(.*)")
    if (result == "0") then
        str2 = librpc.callapi("oltmib_portintfmode_get_1", index .. "&")
        _, _, _, _, intfmode, ability, autoneg_ability, _, _, _ = string.find(str2, string.rep("(.-)&", 7) .. "(.*)")
        str3 = librpc.callapi("oltmib_portinbandan_get_1", ifx .. "&")
        _, _, _, inbandan, _, _, _ = string.find(str3, string.rep("(.-)&", 4) .. "(.*)")
        row["Index"] = ifx
        row["Name"] = name
        row["Desc"] = desc
        row['mytype'] = tonumber(mytype)
        row["if_attr_flags"] = tonumber(if_attr_flags)
        row["mode_ability"] = tonumber(ability)
        row["autoneg_ability"] = tonumber(autoneg_ability)
        row["Portmode"] = port_intfmodetrans(intfmode)
        row["Inband"] = port_inbandantrans(inbandan)
        -- row["Medium"] = mediumtrans(medium)
        row["mtype"] = mediumtrans(mtype)
        row["mstate"] = mediumtrans(mstate)
        if row["mtype"] == "SFP" then
            row["Portmode"] = port_intfmodetrans(intfmode)
            row["Inband"] = port_inbandantrans(inbandan)
        else
            row["Portmode"] = ""
            row["Inband"] = ""
        end
        if mytype == "2" then
            row["Portmode"] = ""
            row["Medium"] = ""
            row["Inband"] = ""
        end
        row["Mode"] = port_modetrans(mode)
        row["NativeVLAN"] = nativevlan
        row["Tagvlan"] = tostring(tagvlan)
        row["Untagvlan"] = tostring(untagvlan)
        row["Conf_dp"] = duplextrans(conf_dp)
        row["Duplex"] = duplextrans(duplex)
        row["Conf_bw"] = bwtrans(conf_bw)
        row["Conf_fc"] = fctrans(conf_fc)
        row["Flowcontrol"] = fctrans(fc)
        row["MTU"] = mtu
        row["Isolate"] = isolate
        row["Speed"] = tostring(tonumber(speed) * 8 / 1000000) .. "Mbps"
        row["Adminshut"] = port_adminshuttrans(tostring(admin_shutdown))
        row["State"] = port_statetrans(tostring(state))
    end
    return row
end

function setport(data)
    -- add vlan 1 forcely
    local portlst1 = string.split(datalst_trans(data["Index"]), ',')
    for _, s in pairs(portlst1) do
        local portlst2 = string.split(s, '-')
        local start = tonumber(portlst2[1])
        local over = tonumber(portlst2[#portlst2])
        for i = start, over, 1 do
            str = i .. "&" .. data["Name"] .. "&" .. data["Desc"] .. "&&&" .. port_modetrans(data["Mode"]) .. "&" .. data["NativeVLAN"] .. "&"
            .. data["Tagvlan"] .. "&" .. data["Untagvlan"] .. "&" .. mediumtrans(data["mtype"]) .. "&&" .. duplextrans(data["Conf_dp"]) .. "&&"
            .. bwtrans(data["Conf_bw"]) .. "&&" .. fctrans(data["Conf_fc"]) .. "&&" .. port_adminshuttrans(data["Adminshut"]) .. "&&"
            .. data["MTU"] .. "&" .. data["Isolate"]
            result = librpc.callapi("oltmib_portinfo_set_1", str)
            if tonumber(result) ~= 0 then return false end
            if data["mtype"] ~= "RJ45" then
                str2 = i .."&" .. (data["mode_flag"] or "") .. "&" .. port_intfmodetrans(data["Portmode"])
                result2 = librpc.callapi("oltmib_portintfmode_set_1", str2)
                if tonumber(result2) ~= 0 then return false end
                if data["Portmode"] ~= "10GBASE-X" then
                    str2 = i .. "&" .. port_inbandantrans(data["Inband"])
                    result2 = librpc.callapi("oltmib_portinbandan_set_1", str2)
                    if tonumber(result2) ~= 0 then return false end
                end
            end
            --dbgprint("setport ifx "..i.." portmode "..data["Portmode"])
        end
    end
    return true
end

function setintfmode(data)
    -- add vlan 1 forcely
    local portlst1 = string.split(datalst_trans(data["Index"]), ',')
    for _, s in pairs(portlst1) do
        local portlst2 = string.split(s, '-')
        local start = tonumber(portlst2[1])
        local over = tonumber(portlst2[#portlst2])
        for i = start, over, 1 do
            if data["mtype"] ~= "RJ45" then
                str = i .."&" .. (data["mode_flag"] or "") .. "&" .. port_intfmodetrans(data["Portmode"])
                result = librpc.callapi("oltmib_portintfmode_set_1", str)
                if tonumber(result) ~= 0 then return false end
                if data["Portmode"] ~= "10GBASE-X" then
                    str = i .. "&" .. port_inbandantrans(data["Inband"])
                    result = librpc.callapi("oltmib_portinbandan_set_1", str)
                    if tonumber(result) ~= 0 then return false end
                end
            end
        end
    end
    return true
end

function vlan_statetrans(val)
    local data = {}
    data["Invalid"] = "0"
    data["Disabled"] = "1"
    data["Active"] = "2"
    data["0"] = "Invalid"
    data["1"] = "Disabled"
    data["2"] = "Active"
    data[""] = ""
    return data[val]
end

function getcombinevlan(vlantable)
    local vlantable2 = {}
    local startidx, endidx, tmpidx, starti
    for i, e in ipairs(vlantable) do
        tmpidx = tonumber(e["Index"])
        --dbgprint("getcombinevlan0 "..tmpidx.." record: "..(startidx or "nil").." "..(endidx or "nil"))
        if endidx == nil then
            startidx = tmpidx
            endidx = tmpidx
            starti = i
        else if tmpidx == endidx + 1 then
                endidx = tmpidx
            else
                if startidx == endidx then
                    table.insert(vlantable2, vlantable[starti])
                else
                    table.insert(vlantable2, { Index = startidx .. "-" .. endidx, State = "Active" })
                end
                startidx = tmpidx
                endidx = tmpidx
                starti = i
            end
        end
    end
    if endidx ~= nil then
        if startidx == endidx then
            table.insert(vlantable2, vlantable[starti])
        else
            table.insert(vlantable2, { Index = startidx .. "-" .. endidx, State = "Active" })
        end
    end
    return vlantable2
end

function portmbr_idx2name(idlst, porttbl)
    local ifarr = string.split(idlst, ",")
    local namelst = ""
    for _, ifx in ipairs(ifarr) do
        p = getportintbl(porttbl, ifx)
        namelst = namelst .. (p and p["Name"] or "") .. (p and "," or "")
    end
    namelst = string.gsub(namelst, ",+$", "")
    return namelst
end
function portmbr_name2idx(namelst, porttbl)
    local namearr = string.split(namelst, ",")
    local idlst = ""
    for _, name in ipairs(namearr) do
        p = getportintbl_by_name(porttbl, name)
        idlst = idlst .. (p and p["Index"] or "") .. (p and "," or "")
    end
    idlst = string.gsub(idlst, ",+$", "")
    return idlst
end

function getvlantable(combine)
    vlantable = {}
    -- porttbl = getporttable(11)
    -- traverse vlan
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_vlaninfo_getn_1", str)
        _, _, mytype, vid, name, state, tagmbr, untagmbr, msg, oper, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["Index"] = vid
            row["Name"] = name
            row["type"] = tonumber(mytype)
            -- row["tagmbr"] = string.gsub(portmbr_idx2name(tagmbr, porttbl), ",", ", ")
            -- row["untagmbr"] = string.gsub(portmbr_idx2name(untagmbr, porttbl), ",", ", ")
            row["tagmbr"] = tagmbr
            row["untagmbr"] = untagmbr
            row["State"] = vlan_statetrans(state)
            table.insert(vlantable, row)-- add it in order for ipairs
        end
    end
    if false and #vlantable > 20 and combine then -- never combine in new mode
        return getcombinevlan(vlantable)
    end
    return vlantable
end

-- Only supports looking up static vlan
function getvlan(index)
    if index == "new" then
        return genemptydata(1, vlanfmt)[1]
    end
    porttbl = getporttable(11)
    local row = {}
    str = librpc.callapi("oltmib_vlaninfo_get_1", "5&" .. index)
    _, _, mytype, vid, name, state, tagmbr, untagmbr, msg, oper, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
    if (result == "0") then
        row["Index"] = vid
        row["Name"] = name
        row["type"] = tonumber(mytype)
        row["State"] = vlan_statetrans(tostring(state))
        -- row["tagmbr"] = portmbr_idx2name(tagmbr, porttbl)
        -- row["untagmbr"] = portmbr_idx2name(untagmbr, porttbl)
        row["tagmbr"] = tagmbr
        row["untagmbr"] = untagmbr
    end
    return row
end

-- Only supports deleting static vlan
function delvlan(index)
    if index then
        local vlanlst1 = string.split(datalst_trans(index), ',')
        for _, s in pairs(vlanlst1) do
            local vlanlst2 = string.split(s, '-')
            local start = tonumber(vlanlst2[1])
            local over = tonumber(vlanlst2[#vlanlst2])
            for i = start, over, 1 do
                if i ~= 1 then -- vlan 1 cannot be deleted
                    str = "5&" .. i .. string.rep("&", 6) .. "2"
                    result = librpc.callapi("oltmib_vlaninfo_set_1", str)
                end
            end
        end
    end
end

-- Only supports the creation of static VLANs and the update of member ports
function setvlan(data)
    local vlanlst1 = string.split(datalst_trans(data["Index"]), ',')
    result = true
    for _, s in pairs(vlanlst1) do
        local vlanlst2 = string.split(s, '-')
        local start = tonumber(vlanlst2[1]) or 0
        local over = tonumber(vlanlst2[#vlanlst2]) or 0
        for i = start, over, 1 do
            -- parse vlan change first
            local oldtagmbrlst = {}
            local olduntagmbrlst = {}
            local olddata = getvlan(i)
            if olddata["Index"] then
                oldtagmbrlst = tools.str2array(olddata['tagmbr'] or "")
                olduntagmbrlst = tools.str2array(olddata['untagmbr'] or "")
                local deltagmbr = tools.array_del(oldtagmbrlst, data['tagmbr'])
                local deluntagmbr = tools.array_del(olduntagmbrlst, data['untagmbr'])
                if next(deltagmbr) or next(deluntagmbr) then
                    str = "5&" .. i .. "&" .. (data['name'] or "") .. "&&" .. table.concat(deltagmbr, ",") .. "&" .. table.concat(deluntagmbr, ",") .. "&&" .. "2"
                    result = (librpc.callapi("oltmib_vlaninfo_set_1", str) == "0") and result
                end
            end
            local addtagmbr = tools.array_del(data['tagmbr'], oldtagmbrlst)
            local adduntagmbr = tools.array_del(data['untagmbr'], olduntagmbrlst)
            str = "5&" .. i .. "&" .. (data['name'] or "") .. "&&" ..table.concat(addtagmbr, ",") .. "&" .. table.concat(adduntagmbr, ",") .. "&&" .. "1"
            result = (librpc.callapi("oltmib_vlaninfo_set_1", str) == "0") and result
        end
    end
    return result
end

function erpsstatetrans(val)
    local data = {}
    data["Invalid"] = "0"
    data["Init"] = "1"
    data["Pending"] = "2"
    data["Idle"] = "3"
    data["FS"] = "4"
    data["Protection"] = "5"
    data["MS"] = "6"
    data["0"] = "Invalid"
    data["1"] = "Init"
    data["2"] = "Pending"
    data["3"] = "Idle"
    data["4"] = "FS"
    data["5"] = "Protection"
    data["6"] = "MS"
    return data[val] or ""
end
function erpslinkstatetrans(val)
    local data = {}
    data["Invalid"] = "0"
    data["Unblocked"] = "1"
    data["Blocked"] = "2"
    data["0"] = "Invalid"
    data["1"] = "Unblocked"
    data["2"] = "Blocked"
    return data[val] or ""
end

function erpslinkstatustrans(val)
    local data = {}
    data["Up"] = "1"
    data["Down"] = "2"
    data["1"] = "Up"
    data["2"] = "Down"
    return data[val] or ""
end

function erpspriotrans(val)
    local data = {}
    data["0"] = "NO-REQ"
    data["1"] = "RAPS-NR"
    data["2"] = "RAPS-NR-RB"
    data["3"] = "WTB-RUN"
    data["4"] = "WTB-EXP"
    data["5"] = "WTR-RUN"
    data["6"] = "WTR-EXP"
    data["7"] = "ADMIN-MS"
    data["8"] = "RAPS-MS"
    data["9"] = "RAPS-SF"
    data["10"] = "LOCAL-CLEAR-SF"
    data["11"] = "LOCAL-SF"
    data["12"] = "RAPS-FS"
    data["13"] = "ADMIN-FS"
    data["14"] = "ADMIN-CLEAR"
    data["15"] = "INITIALIZE"
    return data[val] or ""
end

function geterpsstatetable()
    erpsstatetable = {}
    -- traverse erpsinst
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_erpsstate_getn_1", str)
        _, _, name, ringid, state, lastpriority, eaststatus, eaststate, east_nodeid, east_bpr, weststatus, weststate, west_nodeid, west_bpr, cmd, is_east, msg, oper, result = string.find(str, string.rep("(.-)&", 16) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["name"] = name
            row["ringid"] = ringid
            row["state"] = erpsstatetrans(state)
            row["lastpriority"] = erpspriotrans(lastpriority)
            row["east"] = erpslinkstatetrans(eaststate) .. "(" .. erpslinkstatustrans(eaststatus) .. ")" .. "(" .. east_nodeid .. ", " .. east_bpr .. ")"
            row["west"] = erpslinkstatetrans(weststate) .. "(" .. erpslinkstatustrans(weststatus) .. ")" .. "(" .. west_nodeid .. ", " .. west_bpr .. ")"
            -- row["eaststatus"] = erpslinkstatustrans(eaststatus)
            -- row["eaststate"] = erpslinkstatetrans(eaststate)
            -- row["east_nodeid"] = east_nodeid
            -- row["east_bpr"] = east_bpr
            -- row["weststatus"] = erpslinkstatustrans(weststatus)
            -- row["weststate"] = erpslinkstatetrans(weststate)
            -- row["west_nodeid"] = west_nodeid
            -- row["west_bpr"] = west_bpr
            table.insert(erpsstatetable, row)-- add it in order for ipairs
        end
    end
    return erpsstatetable
end

function seterpsstate(data)
    str = data["name"] .. string.rep("&", 12) .. data["cmd"] .. "&" .. (data["is_east"] or "")
    result = librpc.callapi("oltmib_erpsstate_set_1", str)
end

function geterpsowner()
    return { "None", "East", "West" }
end

function geterpsinsttable()
    erpsinsttable = {}
    -- traverse erpsinst
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_erpsinst_getn_1", str)
        _, _, name, id, profname, ringid, level, rapsvlan, ownerpname, subringif, attachedinst, msg, oper, result = string.find(str, string.rep("(.-)&", 11) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["Name"] = name
            row["ID"] = id
            row["Ring"] = ringid
            row["Level"] = level
            row["RAPSvlan"] = rapsvlan
            row["OwnerInterface"] = ownerpname
            row["Subringif"] = subringif
            row["Attachedinst"] = attachedinst
            table.insert(erpsinsttable, row)-- add it in order for ipairs
        end
    end
    return erpsinsttable
end

function geterpsinst(index)
    if index == "new" then
        return genemptydata(1, erpsinstfmt)[1]
    end
    local row = {}
    str = librpc.callapi("oltmib_erpsinst_get_1", index .. "&")
    _, _, name, id, profname, ringid, level, rapsvlan, ownerpname, subringif, attachedinst, msg, oper, result = string.find(str, string.rep("(.-)&", 11) .. "(.*)")
    if (result == "0") then
        row["Name"] = name
        row["ID"] = id
        row["Ring"] = ringid
        row["Level"] = level
        row["RAPSvlan"] = rapsvlan
        row["OwnerInterface"] = ownerpname
        row["Subringif"] = subringif
        row["Attachedinst"] = attachedinst
    end
    return row
end

function delerpsinst(index)
    str = index .. string.rep("&", 10) .. "2"
    result = librpc.callapi("oltmib_erpsinst_set_1", str)
end

function seterpsinst(data)
    str = data["Name"] .. "&" .. data["ID"] .. "&&" .. data["Ring"] .. "&" .. data["Level"] .. "&" .. data["RAPSvlan"] .. "&" .. data["OwnerInterface"]
    .. "&" .. data["Subringif"] .. "&" .. data["Attachedinst"]
    result = librpc.callapi("oltmib_erpsinst_set_1", str)
    return result == '0'
end

function geterpsringtable()
    erpsringtable = {}
    -- traverse erpsring
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_erpsring_getn_1", str)
        _, _, index, eastpname, westpname, msg, oper, result = string.find(str, string.rep("(.-)&", 5) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["Index"] = tostring(index)
            row["EASTInterface"] = tostring(eastpname)
            row["WESTInterface"] = tostring(westpname)
            table.insert(erpsringtable, row)-- add it in order for ipairs
        end
    end
    return erpsringtable
end

function geterpsring(index)
    if index == "new" then
        return genemptydata(1, erpsringfmt)[1]
    end
    local row = {}
    str = librpc.callapi("oltmib_erpsring_get_1", index .. "&")
    _, _, index, eastpname, westpname, msg, oper, result = string.find(str, string.rep("(.-)&", 5) .. "(.*)")
    if (result == "0") then
        row["Index"] = tostring(index)
        row["EASTInterface"] = tostring(eastpname)
        row["WESTInterface"] = tostring(westpname)
    end
    return row
end

function delerpsring(index)
    str = index .. string.rep("&", 4) .. "2"
    result = librpc.callapi("oltmib_erpsring_set_1", str)
end

function seterpsring(data)
    str = data["Index"] .. "&" .. data["EASTInterface"] .. "&" .. data["WESTInterface"]
    --dbgprint("set erpsring index "..data["Index"].." east "..data["EASTInterface"].." west "..data["WESTInterface"])
    result = librpc.callapi("oltmib_erpsring_set_1", str)
    return result == '0'
end

function prefix2mask(prefix)
    prefix = tonumber(prefix) or 0
    intnum = 4294967295 - bit.lshift(1, 32 - prefix) + 1
    mask = bit.band(bit.rshift(intnum, 24), 255) .. "." .. bit.band(bit.rshift(intnum, 16), 255) .. "."
    .. bit.band(bit.rshift(intnum, 8), 255) .. "." .. bit.band(bit.rshift(intnum, 0), 255)
    return mask
end

function mask2prefix(mask)
    _, _, value1, value2, value3, value4 = string.find(mask, string.rep("(.-)%.", 3) .. "(.*)")
    intnum = bit.lshift(tonumber(value1) or 0, 24) + bit.lshift(tonumber(value2) or 0, 16)
    + bit.lshift(tonumber(value3) or 0, 8) + bit.lshift(tonumber(value4) or 0, 0)
    prefix = 32
    while (bit.band(intnum, 1) == 0 and prefix > 0) do
        intnum = bit.rshift(intnum, 1)
        prefix = prefix - 1
    end
    --dbgprint("mask "..mask.." value "..value1..value2..value3..value4.." int "..intnum.." prefix "..prefix)
    return prefix
end

function iptypetrans(val)
    local data = {}
    data["0"] = "None"
    data["1"] = "Static"
    data["2"] = "DHCP"
    data["None"] = "0"
    data["Static"] = "1"
    data["DHCP"] = "2"
    return data[val] or ""
end

function getmgmtip()
    local row = {}
    str = librpc.callapi("oltmib_mgmtvlan_get_1", "")
    _, _, row["VID"], row["ipv4type"], ipprefix, row["Gateway"], row["ipv6type"], prefix6, row["Gateway6"], msg, oper, result = string.find(str, string.rep("(.-)&", 9) .. "(.*)")
    if (result == "0") then
        _, _, ip, prefix = string.find(ipprefix, string.rep("(.-)/", 1) .. "(.*)")
        row["IP"] = ip or ""
        row["Mask"] = prefix ~= "" and prefix2mask(prefix) or ""
        _, _, ipv6, prefix6 = string.find(prefix6, string.rep("(.-)/", 1) .. "(.*)")
        row["IPv6"] = ipv6 or ""
        row["Prefix6"] = prefix6 or ""
        row["ipv4type"] = iptypetrans(row["ipv4type"])
        row["ipv6type"] = iptypetrans(row["ipv6type"])
    end
    return row
end

function setmgmtip(data, ifname)
    ip = data["IP"] .. "/" .. mask2prefix(data["Mask"])
    ipv6 = data["IPv6"] .. "/" .. data["Prefix6"]
    str = data["VID"] .. "&" .. iptypetrans(data["ipv4type"]) .. "&" .. ip .. "&" .. data["Gateway"] .. "&" .. iptypetrans(data["ipv6type"]) .. "&" .. ipv6 .. "&" .. data["Gateway6"]
    result = librpc.callapi("oltmib_mgmtvlan_set_1", str)
    os.execute("touch " .. ipchangefile)
    if (ifname ~= "") then
        setport({ Index = "", Name = ifname, Desc = "", Mode = "Access", NativeVLAN = data["VID"], AllowVLAN = data["VID"], Speed = "", Adminshut = "No shutdown" })
    end
end

--[[
function getaccounttbl()
    accounttbl = {}
    -- traverse erpsring
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_account_getn_1", str)
        _, _, status, key, keytype, ip, name, pwd, msg, oper, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["name"] = name
            table.insert(accounttbl, row)-- add it in order for ipairs
        end
    end
    return accounttbl
end
function setaccount(data)
    str = "&&&&" .. data["name"] .. "&" .. (data["pwd"] or "") .. "&&" .. (data["oper"] or "")
    result = librpc.callapi("oltmib_account_set_1", str)
end

function setsysinfo(data)
    str = "&&&&&&&&" .. data["hostname"]
    if (data["hostname"] == "") then
        str = "&&&&&&&&&2" -- reset hostname
    end
    result = librpc.callapi("oltmib_devinfo_set_1", str)
    --dbgprint("setsysinfo "..data["hostname"].." str "..str.." result "..result)
end

function timetrans(sec)
    local longSec = tonumber(sec)
    s = longSec % 60;
    m = (longSec - s) / 60 % 60;
    h = ((longSec - s) / 60 - m) / 60 % 24;
    d = (((longSec - s) / 60 - m) / 60 - h) / 24;
    return d .. "d " .. h .. "h " .. m .. "m " .. s .. "s "
end

function getsysinfo()
    str = ""
    str = librpc.callapi("oltmib_devinfo_get_1", str)
    _, _, devsn, prdid, mac, swver, swdate, hwver, _, uptime, hostname, result = string.find(str, string.rep("(.-)&", 9) .. "(.*)")
    return { hostname = hostname, mac = mac, hwver = hwver, swver = swver, swdate = swdate, psn = devsn, pid = prdid, uptime = timetrans(uptime) }
end

function webstatus_parse(st)
    local http_status, https_status
    webstatus = tonumber(st)
    if webstatus == 2 or webstatus == 4 then
        http_status = 1
    else
        http_status = 0
    end
    if webstatus == 3 or webstatus == 4 then
        https_status = 1
    else
        https_status = 0
    end
    return http_status, https_status
end
function webstatus_pack(http_status, https_status)
    if http_status == 0 and https_status == 0 then
        return 1
    end
    if http_status == 1 and https_status == 0 then
        return 2
    end
    if http_status == 0 and https_status == 1 then
        return 3
    end
    if http_status == 1 and https_status == 1 then
        return 4
    end
    return 1
end

function getsvctbl()
    str = librpc.callapi("oltmib_telnet_get_1", "")
    _, _, telstatus, _ = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
    str = librpc.callapi("oltmib_ssh_get_1", "")
    _, _, sshstatus, _ = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
    str = librpc.callapi("oltmib_web_get_1", "")
    _, _, webstatus, _ = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
    http_status, https_status = webstatus_parse(webstatus)
    local tbl = {}
    table.insert(tbl, { name = "Telnet Server", enabled = tonumber(telstatus) })
    table.insert(tbl, { name = "SSH Server", enabled = tonumber(sshstatus) })
    table.insert(tbl, { name = "HTTP Server", enabled = tonumber(http_status) })
    table.insert(tbl, { name = "HTTPS Server", enabled = tonumber(https_status) })
    return tbl
end

function setsvc(data)
    str = ""
    if (data["enabled"] == 0) then
        str = "&&&&&&&2"
    end
    if (data["name"] == "Telnet Server") then
        result = librpc.callapi("oltmib_telnet_set_1", str)
    end
    if (data["name"] == "SSH Server") then
        result = librpc.callapi("oltmib_ssh_set_1", str)
    end
    if (data["name"] == "Web Server") then
        result = librpc.callapi("oltmib_web_set_1", data["status"])
    end
    --dbgprint("setsvc "..data["name"].." state "..data["enabled"].." result "..result)
end
]]--

function communitytypetrans(val)
    local data = {}
    data["Read-write"] = "0"
    data["Read-only"] = "1"
    data["0"] = "Read-write"
    data["1"] = "Read-only"
    return data[val] or ""
end

function getsnmpcommunitytable()
    snmpcommunitytable = {}
    -- traverse snmpcommunity
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_snmp_community_getn_1", str)
        _, _, _, key, keytype, _, _, _, _, _, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["name"] = tostring(key)
            row["type"] = communitytypetrans(tostring(keytype))
            snmpcommunitytable[key] = row
        end
    end
    return snmpcommunitytable
end

function state2oper(state)
    oper = 2 -- oltmib_oper_del
    if (state == 1 or state == "1") then
        oper = 1
    end
    return oper
end

function getcommunitytype()
    return { "Read-write", "Read-only" }
end

function setsnmpcommunity(data, state)
    str = "&" .. data["name"] .. "&" .. communitytypetrans(data["type"]) .. "&&&&&" .. state2oper(state)
    result = librpc.callapi("oltmib_snmp_community_set_1", str)
    return result == "0"
    --dbgprint("setsnmpcommunity "..data["name"].." mytype "..data["type"].." result "..result)
end

function getsnmpsrvtable()
    snmpsrvtable = {}
    -- traverse snmpsrv
    result = "0"
    str = "&&&0.0.0.0"
    while (result == "0") do
        str = librpc.callapi("oltmib_snmp_srv_getn_1", str)
        _, _, _, key, _, ip, _, _, _, _, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["ip"] = tostring(ip)
            row["community"] = tostring(key)
            table.insert(snmpsrvtable, row)
        end
        --dbgprint("getsnmpsrvtable "..ip.." community "..key.." result "..result)
    end
    return snmpsrvtable
end

function setsnmpsrv(data, state)
    str = "&" .. data["community"] .. "&&" .. data["ip"] .. "&&&&" .. state2oper(state)
    return (librpc.callapi("oltmib_snmp_srv_set_1", str) == "0")
end

function getsnmpviewtable()
    local snmpviewtable = {}
    -- traverse snmpview
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_snmp_view_getn_1", str)
        _, _, row["name"], row["oidlst"], _, _, result = string.find(str, string.rep("(.-)&", 4) .. "(.*)")
        if (result == "0") then
            table.insert(snmpviewtable, row)
        end
        --dbgprint("getsnmpviewtable "..ip.." community "..key.." result "..result)
    end
    return snmpviewtable
end

function getsnmpview(name)
    local row = {}
    str = librpc.callapi("oltmib_snmp_view_get_1", name)
    _, _, row["name"], row["oidlst"], _, _, result = string.find(str, string.rep("(.-)&", 4) .. "(.*)")
    if (result == "0") then
        return row
    end
    return {}
end

function setsnmpview(data, state)
    str = data["name"] .. "&" .. data["oidlst"] .. "&&" .. state2oper(state)
    result = librpc.callapi("oltmib_snmp_view_set_1", str)
    --dbgprint("setsnmpview "..data["ip"].." community "..data["community"].." result "..result)
end

function snmp_secmodeltrans(val)
    local data = {}
    data["noAuthNoPriv"] = "1"
    data["authNoPriv"] = "2"
    data["authPriv"] = "3"
    data["1"] = "noAuthNoPriv"
    data["2"] = "authNoPriv"
    data["3"] = "authPriv"
    return data[val] or ""
end
function snmp_vertrans(val)
    local data = {}
    data["v1"] = "1"
    data["v2c"] = "2"
    data["v3"] = "3"
    data["1"] = "v1"
    data["2"] = "v2c"
    data["3"] = "v3"
    return data[val] or ""
end
function snmp_authtypetrans(val)
    local data = {}
    data["MD5"] = "1"
    data["SHA"] = "2"
    data["1"] = "MD5"
    data["2"] = "SHA"
    return data[val] or ""
end
function snmp_enctypetrans(val)
    local data = {}
    data["AES"] = "1"
    data["DES"] = "2"
    data["1"] = "AES"
    data["2"] = "DES"
    return data[val] or ""
end
function snmp_sendinformtrans(val)
    local data = {}
    data["Traps"] = "0"
    data["Informs"] = "1"
    data["0"] = "Traps"
    data["1"] = "Informs"
    return data[val] or ""
end
function ip_familytrans(val)
    local data = {}
    data["IPv4"] = "2"
    data["IPv6"] = "10"
    data["2"] = "IPv4"
    data["10"] = "IPv6"
    return data[val] or ""
end
function getsnmpgrouptable()
    local snmpgrouptable = {}
    -- traverse snmpgroup
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_snmp_group_getn_1", str)
        _, _, row["name"], row["ver"], row["sec_model"], row["rview"], row["wview"], row["nview"], _, _, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            row["ver"] = snmp_vertrans(row["ver"])
            row["sec_model"] = snmp_secmodeltrans(row["sec_model"])
            table.insert(snmpgrouptable, row)
        end
        --dbgprint("getsnmpgrouptable "..ip.." community "..key.." result "..result)
    end
    return snmpgrouptable
end

function setsnmpgroup(data, state)
    str = data["name"] .. "&" .. snmp_vertrans(data["ver"]) .. "&" .. snmp_secmodeltrans(data["sec_model"]) .. "&" .. data["rview"] .. "&" .. data["wview"] .. "&&&" .. state2oper(state)
    result = librpc.callapi("oltmib_snmp_group_set_1", str)
    return result == "0"
    --dbgprint("setsnmpgroup "..data["ip"].." community "..data["community"].." result "..result)
end

function getsnmpusertable()
    local snmpusertable = {}
    -- traverse snmpuser
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_snmp_user_getn_1", str)
        _, _, row["name"], row["group"], row["authtype"], row["authpass"], row["enctype"], row["encpass"], _, _, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            row["authtype"] = snmp_authtypetrans(row["authtype"])
            row["enctype"] = snmp_enctypetrans(row["enctype"])
            table.insert(snmpusertable, row)
        end
        --dbgprint("getsnmpusertable "..ip.." community "..key.." result "..result)
    end
    return snmpusertable
end

function setsnmpuser(data, state)
    str = data["name"] .. "&" .. data["group"] .. "&" .. snmp_authtypetrans(data["authtype"]) .. "&" .. data["authpass"] .. "&" .. snmp_enctypetrans(data["enctype"]) .. "&" .. data["encpass"] .. "&&" .. state2oper(state)
    result = librpc.callapi("oltmib_snmp_user_set_1", str)
    return result == "0"
    --dbgprint("setsnmpuser "..data["ip"].." community "..data["community"].." result "..result)
end

function getsnmphosttable()
    local snmphosttable = {}
    -- traverse snmphost
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_snmp_host_getn_1", str)
        _, _, row["family"], row["ipstr"], row["ver"], row["user"], row["send_inform"], row["sec_model"], _, _, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            row["family"] = ip_familytrans(row["family"])
            row["ver"] = snmp_vertrans(row["ver"])
            row["send_inform"] = snmp_sendinformtrans(row["send_inform"])
            row["sec_model"] = snmp_secmodeltrans(row["sec_model"])
            table.insert(snmphosttable, row)
        end
        --dbgprint("getsnmphosttable "..ip.." community "..key.." result "..result)
    end
    return snmphosttable
end

function setsnmphost(data, state)
    str = ip_familytrans(data["family"]) .. "&" .. data["ipstr"] .. "&" .. snmp_vertrans(data["ver"]) .. "&" .. data["user"] .. "&" .. snmp_sendinformtrans(data["send_inform"]) .. "&" .. snmp_secmodeltrans(data["sec_model"]) .. "&&" .. state2oper(state)
    result = librpc.callapi("oltmib_snmp_host_set_1", str)
    return result == "0"
    --dbgprint("setsnmphost "..data["ip"].." community "..data["community"].." result "..result)
end

function getigmpsnptbl()
    str = librpc.callapi("oltmib_igmpsnp_get_1", "")
    _, _, igmpsnpstatus, unknown_mcast_discard, tcn_suppression, msg, oper, result = string.find(str, string.rep("(.-)&", 5) .. "(.*)")
    return { { name = translate("IGMP Snooping"), enabled = tonumber(igmpsnpstatus) },
    { name = translate("Discard Unknown Multicast"), enabled = tonumber(unknown_mcast_discard) },
    { name = translate("TC Suppression"), enabled = tonumber(tcn_suppression) } }
end

function setigmpsnptbl(data)
    str = data[1]["enabled"] .. "&" .. data[2]["enabled"] .. "&" .. data[3]["enabled"]
    result = librpc.callapi("oltmib_igmpsnp_set_1", str)
end

function getmroutertbl()
    mroutertable = {}
    -- traverse mrouter
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_igmpsnp_mrouter_getn_1", str)
        _, _, vid, ifname, msg, oper, result = string.find(str, string.rep("(.-)&", 4) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["vid"] = tostring(vid)
            row["ifname"] = tostring(ifname)
            table.insert(mroutertable, row)
        end
        --dbgprint("getmroutertable "..vid.." ifname "..ifname.." result "..result)
    end
    return mroutertable
end

function setmrouter(data, state)
    str = data["vid"] .. "&" .. data["ifname"] .. "&&" .. state2oper(state)
    result = librpc.callapi("oltmib_igmpsnp_mrouter_set_1", str)
    --dbgprint("setmrouter "..vid.." ifname "..ifname.." result "..result)
    return result == "0"
end

function getstaticgrptbl()
    staticgrptable = {}
    -- traverse staticgrp
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_igmpsnp_static_grp_getn_1", str)
        _, _, vid, ifname, grpip, srcip, mytype, msg, oper, result = string.find(str, string.rep("(.-)&", 7) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["vid"] = (vid)
            row["ifname"] = (ifname)
            row["grpip"] = (grpip)
            row["srcip"] = (srcip)
            row["type"] = (mytype)
            table.insert(staticgrptable, row)
        end
        --dbgprint("getstaticgrptable "..vid.." ifname "..ifname.." grpip "..grpip.." srcip "..srcip.." result "..result)
    end
    return staticgrptable
end

function setstaticgrp(data, state)
    str = data["vid"] .. "&" .. data["ifname"] .. "&" .. data["grpip"] .. "&" .. data["srcip"] .. "&&&" .. state2oper(state)
    result = librpc.callapi("oltmib_igmpsnp_static_grp_set_1", str)
    --dbgprint("setstaticgrp "..vid.." ifname "..ifname.." grpip "..grpip.." srcip "..srcip.." result "..result)
    return result == "0"
end

function getigspgrptbl()
    igspgrptable = {}
    -- traverse staticgrp
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_igmpsnp_grp_getn_1", str)
        _, _, vid, ifname, grpip, srcip, mytype, msg, oper, result = string.find(str, string.rep("(.-)&", 7) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["vid"] = (vid)
            row["ifname"] = (ifname)
            row["grpip"] = (grpip)
            row["srcip"] = (srcip)
            if mytype == "1" then
                row["type"] = "mrouter"
            else
                row["type"] = "report"
            end
            table.insert(igspgrptable, row)
        end
        --dbgprint("getstaticgrptable "..vid.." ifname "..ifname.." grpip "..grpip.." srcip "..srcip.." result "..result)
    end
    return igspgrptable
end

function getstpmode()
    return { "MSTP", "RSTP", "STP" }
end

function getstpstatus()
    return { "Enable", "Disable" }
end

function stpmodetrans(mode)
    local data = {}
    data["2"] = "STP"
    data["4"] = "RSTP"
    data["5"] = "MSTP"
    data["STP"] = "2"
    data["RSTP"] = "4"
    data["MSTP"] = "5"
    return data[mode] or ""
end
function stpstatustrans(mode)
    local data = {}
    data["0"] = "Disable"
    data["1"] = "Enable"
    data["Disable"] = "0"
    data["Enable"] = "1"
    return data[mode] or ""
end

function getstpglobal()
    local data = {}
    str = librpc.callapi("oltmib_mstp_global_get_1", "")
    _, _, mstpstatus, bpduguard, bpdufilter, maxhops, hellotime, forwardtime, maxage, priority, txcount, errdis, errdistm, msg, oper, result
    = string.find(str, string.rep("(.-)&", 13) .. "(.*)")
    str2 = librpc.callapi("oltmib_sptmode_get_1", "")
    _, _, stpmode, edge, msg2, oper2, result2 = string.find(str2, string.rep("(.-)&", 4) .. "(.*)")
    if result == "0" and result2 == "0" then
        data["status"] = stpstatustrans(mstpstatus)
        data["bpduguard"] = stpstatustrans(bpduguard)
        data["bpdufilter"] = stpstatustrans(bpdufilter)
        data["maxhops"] = maxhops
        data["hellotime"] = hellotime
        data["forwardtime"] = forwardtime
        data["maxage"] = maxage
        data["priority"] = priority
        data["txcount"] = txcount
        data["errdis"] = stpstatustrans(errdis)
        data["errdistm"] = errdistm
        data["mode"] = stpmodetrans(stpmode)
    end
    return data
end

function setstpglobal(data)
    str = stpstatustrans(data["status"]) .. "&" .. stpstatustrans(data["bpduguard"]) .. "&" .. stpstatustrans(data["bpdufilter"]) .. "&" .. data["maxhops"] .. "&"
    .. data["hellotime"] .. "&" .. data["forwardtime"] .. "&" .. data["maxage"] .. "&" .. data["priority"] .. "&" .. data["txcount"] .. "&"
    .. stpstatustrans(data["errdis"]) .. "&" .. data["errdistm"]
    str2 = stpmodetrans(data["mode"])
    librpc.callapi("oltmib_sptmode_set_1", str2)
    result = librpc.callapi("oltmib_mstp_global_set_1", str)
    if result == "4" then -- try again if bridge removed temporally
        os.execute("sleep " .. "0.5s")
        result = librpc.callapi("oltmib_mstp_global_set_1", str)
    end
    --dbgprint("setstpstatus "..data.." result "..result)
end

function getstpmst()
    local data = {}
    str = librpc.callapi("oltmib_mstp_mst_get_1", "")
    _, _, region, revision, msg, oper, result = string.find(str, string.rep("(.-)&", 4) .. "(.*)")
    if result == "0" then
        data["region"] = region
        data["revision"] = revision
    end
    return data
end

function setstpmst(data)
    str = data["region"] .. "&" .. data["revision"]
    result = librpc.callapi("oltmib_mstp_mst_set_1", str)
    --dbgprint("setstpstatus "..data.." result "..result)
end

function getstpinsttbl()
    stpinsttbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_mstp_inst_getn_1", str)
        _, _, instid, vlanlst, priority, msg, oper, result = string.find(str, string.rep("(.-)&", 5) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["id"] = instid
            row["vlanlst"] = vlanlst
            row["priority"] = priority
            table.insert(stpinsttbl, row)
        end
    end
    return stpinsttbl
end

function getstpinst(id)
    local row = {}
    if id == "new" or id == "" then
        return row
    end
    str = librpc.callapi("oltmib_mstp_inst_get_1", id)
    _, _, instid, vlanlst, priority, msg, oper, result = string.find(str, string.rep("(.-)&", 5) .. "(.*)")
    if (result == "0") then
        row["id"] = instid
        row["vlanlst"] = vlanlst
        row["priority"] = priority
    end
    return row
end

function setstpinst(data)
    str = data["id"] .. "&" .. datalst_trans(data["vlanlst"]) .. "&" .. data["priority"] .. "&&" .. (data["oper"] or "")
    result = librpc.callapi("oltmib_mstp_inst_set_1", str)
    return result == '0'
end

function getstplinktype()
    return { "P2P", "Share", "Auto" }
end

function stplinktypetrans(mode)
    local data = {}
    data["0"] = "Share"
    data["1"] = "P2P"
    data["2"] = "Auto"
    data["Share"] = "0"
    data["P2P"] = "1"
    data["Auto"] = "2"
    return data[mode] or ""
end

function getbpduopts()
    return { "Default", "Enable", "Disable" }
end

function stpbpdutrans(mode)
    local data = {}
    data["0"] = "Enable"
    data["1"] = "Disable"
    data["2"] = "Default"
    data["Enable"] = "0"
    data["Disable"] = "1"
    data["Default"] = "2"
    return data[mode] or ""
end

function stpifdefault()
    local tbl = {}
    --tbl["ifx"] = ifx
    tbl["instance"] = '0'
    --tbl["ifname"] = ifname
    --tbl["status"] = "Enable"
    tbl["tcn"] = "Disable"
    tbl["priority"] = "128"
    --tbl["pathcost"] = "20000000"
    --tbl["linktype"] = "P2P"
    --tbl["rootguard"] = "Disable"
    --tbl["autoedge"] = "Disable"
    --tbl["edgeport"] = "Disable"
    --tbl["portfast"] = "Disable"
    --tbl["bpdufilter"] = "Default"
    --tbl["bpduguard"] = "Default"
    return tbl
end

function getstpiftbl()
    stpiftbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_mstp_if_getn_1", str)
        _, _, ifx, instance, ifname, status, tcn, priority, pathcost, linktype, rootguard, autoedge, edgeport, portfast, bpdufilter, bpduguard, msg, oper, result = string.find(str, string.rep("(.-)&", 16) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["ifx"] = ifx
            row["instance"] = instance
            row["ifname"] = ifname
            str2 = librpc.callapi("oltmib_stpifstatus_get_1", ifx)
            _, _, ifx, ifname, status, msg, oper, result = string.find(str2, string.rep("(.-)&", 5) .. "(.*)")
            row["status"] = stpstatustrans(status)
            row["tcn"] = stpstatustrans(tcn)
            row["priority"] = priority
            row["pathcost"] = pathcost
            row["linktype"] = stplinktypetrans(linktype)
            row["rootguard"] = stpstatustrans(rootguard)
            row["autoedge"] = stpstatustrans(autoedge)
            row["edgeport"] = stpstatustrans(edgeport)
            row["portfast"] = stpstatustrans(portfast)
            row["bpdufilter"] = stpbpdutrans(bpdufilter)
            row["bpduguard"] = stpbpdutrans(bpduguard)
            table.insert(stpiftbl, row)
        end
    end
    return stpiftbl
end

function getstpif(name, instance)
    local row = {}
    if name == "new" or name == "" then
        return row
    end
    str = librpc.callapi("oltmib_mstp_if_get_1", "&" .. instance .. "&" .. name)
    _, _, ifx, instance, ifname, status, tcn, priority, pathcost, linktype, rootguard, autoedge, edgeport, portfast, bpdufilter, bpduguard, msg, oper, result = string.find(str, string.rep("(.-)&", 16) .. "(.*)")
    if (result == "0") then
        row["ifx"] = ifx
        row["instance"] = instance
        row["ifname"] = ifname
        str2 = librpc.callapi("oltmib_stpifstatus_get_1", ifx)
        _, _, ifx, ifname, status, msg, oper, result = string.find(str2, string.rep("(.-)&", 5) .. "(.*)")
        row["status"] = stpstatustrans(status)
        row["tcn"] = stpstatustrans(tcn)
        row["priority"] = priority
        row["pathcost"] = pathcost
        row["linktype"] = stplinktypetrans(linktype)
        row["rootguard"] = stpstatustrans(rootguard)
        row["autoedge"] = stpstatustrans(autoedge)
        row["edgeport"] = stpstatustrans(edgeport)
        row["portfast"] = stpstatustrans(portfast)
        row["bpdufilter"] = stpbpdutrans(bpdufilter)
        row["bpduguard"] = stpbpdutrans(bpduguard)
    end
    return row
end

function setstpif(data)
    str = (data["ifx"] or "") .. "&" .. data["instance"] .. "&" .. data["ifname"] .. "&" .. stpstatustrans(data["status"]) .. "&" .. stpstatustrans(data["tcn"])
    .. "&" .. data["priority"] .. "&" .. data["pathcost"] .. "&" .. stplinktypetrans(data["linktype"])
    .. "&" .. stpstatustrans(data["rootguard"]) .. "&" .. stpstatustrans(data["autoedge"]) .. "&" .. stpstatustrans(data["edgeport"])
    .. "&" .. stpstatustrans(data["portfast"]) .. "&" .. stpbpdutrans(data["bpdufilter"]) .. "&" .. stpbpdutrans(data["bpduguard"])
    .. "&&" .. (data["oper"] or "")
    result = librpc.callapi("oltmib_mstp_if_set_1", str)
    if data["oper"] ~= "2" and result == "0" then -- add & success
        str2 = (data["ifx"] or "") .. "&" .. data["ifname"] .. "&" .. stpstatustrans(data["status"])
        result2 = librpc.callapi("oltmib_stpifstatus_set_1", str2)
    end
end

function stpvertrans(mode)
    local data = {}
    data["1"] = "STP"
    data["2"] = "RSTP"
    data["4"] = "MSTP"
    return data[mode] or ""
end

function stproletrans(mode)
    local data = {}
    data["0"] = "Master"
    data["1"] = "Alternate"
    data["2"] = "Root"
    data["3"] = "Designated"
    data["4"] = "Disabled"
    data["5"] = "Backup"
    return data[mode] or ""
end

function stpstatetrans(mode)
    local data = {}
    data["0"] = "Blocked"
    data["1"] = "Listening"
    data["2"] = "Learning"
    data["3"] = "Forwarding"
    data["4"] = "Blocked"
    data["5"] = "Discard"
    return data[mode] or ""
end

function getstpifstatetbl()
    stpiftbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_mstp_ifstate_getn_1", str)
        _, _, ifx, instance, ifname, version, role, state, rootbid, regrootbid, desbid, msg, oper, result = string.find(str, string.rep("(.-)&", 11) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["ifx"] = ifx
            row["instance"] = instance
            row["ifname"] = ifname
            -- str2 = librpc.callapi("oltmib_stpifstatus_get_1", ifx)
            -- _, _, ifx, ifname, status, msg, oper, result = string.find(str2, string.rep("(.-)&", 5) .. "(.*)")
            row["version"] = stpvertrans(version)
            row["role"] = stproletrans(role)
            row["state"] = stpstatetrans(state)
            row["rootbid"] = rootbid
            row["regrootbid"] = regrootbid
            row["desbid"] = desbid
            if row["role"] ~= "Disabled" then
                table.insert(stpiftbl, row)
            end
        end
    end
    return stpiftbl
end

function setstpifstate(data)
    str = "&&" .. (data["ifname"] or "")
    result = librpc.callapi("oltmib_mstp_reset_if_detect_1", str)
    return result == "0"
end

function getportstattbl(filtertype)
    portstattable = {}
    -- traverse portstat
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_portstat_getn_1", str)
        _, _, ifx, mytype, name, rxpkts, rxbytes, rxmcpkts, txpkts, txbytes, txmcpkts, undersize, oversize, crc, collision, msg, oper, result = string.find(str, string.rep("(.-)&", 15) .. "(.*)")
        if (result == "0" and (filtertype == nil or bit.band(tonumber(mytype), tonumber(filtertype)) ~= 0)) then
            local row = {}
            str = librpc.callapi("oltmib_portrate_get_1", ifx .. "")
            _, _, ifx, mytype, name, rxBps, rxpps, rxmcpps, txBps, txpps, txmcpps, msg, oper, result = string.find(str, string.rep("(.-)&", 11) .. "(.*)")
            row["Index"] = tostring(ifx)
            row["Name"] = tostring(name)
            row["RxPkts"] = rxpkts
            row["RxBytes"] = rxbytes
            row["TxPkts"] = txpkts
            row["TxBytes"] = txbytes
            row["Rxbps"] = tostring(tonumber(rxBps) * 8)
            row["Rxpps"] = rxpps
            row["Txbps"] = tostring(tonumber(txBps) * 8)
            row["Txpps"] = txpps
            row['Undersize'] = undersize
            row['Oversize'] = oversize
            row['Crc'] = crc
            row['Collision'] = collision
            table.insert(portstattable, row)
        end
    end
    return portstattable
end

function setportstat(data)
    result = librpc.callapi("oltmib_portstat_set_1", data["Index"] .. "&&&&&&&&&&&&&&2")
end

function mirror_dirtrans(dir)
    local trans = {}
    trans["0"] = "disable"
    trans["1"] = "rx"
    trans["2"] = "tx"
    trans["3"] = "both"
    trans["disable"] = "0"
    trans["rx"] = "1"
    trans["tx"] = "2"
    trans["both"] = "3"
    return trans[tostring(dir)] or ""
end

function mirror_statetrans(state)
    local trans = {}
    trans["0"] = "shutdown"
    trans["1"] = "no destination"
    trans["2"] = "no source"
    trans["3"] = "no operation"
    trans["4"] = "active"
    trans["shutdown"] = "0"
    trans["no destination"] = "1"
    trans["no source"] = "2"
    trans["no operation"] = "3"
    trans["active"] = "4"
    return trans[tostring((state))] or ""
end

function mirror_modetrans(mode)
    local trans = {}
    trans["0"] = "span"
    trans["1"] = "remote-source"
    trans["2"] = "remote-destination"
    trans["span"] = "0"
    trans["remote-source"] = "1"
    trans["remote-destination"] = "2"
    return trans[tostring((mode))] or ""
end

function getmirrortbl()
    mirrortable = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_pminfo_getn_1", str)
        _, _, sid, mode, desc, to, to_switch, rspan_vlan, src, src_vlan, dir, state, msg, oper, result = string.find(str, string.rep("(.-)&", 12) .. "(.*)")
        if (result == "0") then
            if mirrortable[tonumber(sid)] then
                if (bit.band(tonumber(dir), 1) == 1) then
                    mirrortable[tonumber(sid)]["src_rx"] = mirrortable[tonumber(sid)]["src_rx"] == "" and src or (mirrortable[tonumber(sid)]["src_rx"] .. "," .. src)
                end
                if (bit.band(tonumber(dir), 2) == 2) then
                    mirrortable[tonumber(sid)]["src_tx"] = mirrortable[tonumber(sid)]["src_tx"] == "" and src or (mirrortable[tonumber(sid)]["src_tx"] .. "," .. src)
                end
            else
                local row = {}
                row["sid"] = sid
                row["mode"] = mirror_modetrans(mode)
                row["desc"] = desc
                row["to"] = to
                row["to_switch"] = to_switch
                row["rspan_vlan"] = rspan_vlan
                row["src_rx"] = ""
                row["src_tx"] = ""
                if (bit.band(tonumber(dir), 1) == 1) then
                    row["src_rx"] = src
                end
                if (bit.band(tonumber(dir), 2) == 2) then
                    row["src_tx"] = src
                end
                row["src_vlan"] = src_vlan
                row["state"] = mirror_statetrans(state)
                mirrortable[tonumber(sid)] = row
            end
        end
    end
    return mirrortable
end

function getmirror(session)
    mirror = { src_rx = "", src_tx = ""}
    if session == "new" then
        return mirror
    end
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_pminfo_getn_1", str)
        _, _, sid, mode, desc, to, to_switch, rspan_vlan, src, src_vlan, dir, state, msg, oper, result = string.find(str, string.rep("(.-)&", 12) .. "(.*)")
        if (result == "0" and sid == session) then
            mirror["sid"] = sid
            mirror["mode"] = mirror_modetrans(mode)
            mirror["desc"] = desc
            mirror["to"] = to
            mirror["to_switch"] = to_switch
            mirror["rspan_vlan"] = rspan_vlan
            if (bit.band(tonumber(dir), 1) == 1) then
                mirror["src_rx"] = mirror["src_rx"] == "" and src or (mirror["src_rx"] .. "," .. src)
            end
            if (bit.band(tonumber(dir), 2) == 2) then
                mirror["src_tx"] = mirror["src_tx"] == "" and src or (mirror["src_tx"] .. "," .. src)
            end
            mirror["src_vlan"] = src_vlan
            mirror["state"] = mirror_statetrans(state)
        end
    end
    return mirror
end

function setmirror(data)
    if data["oper"] == "2" then -- del session
        librpc.callapi("oltmib_pminfo_set_1", data["sid"] .. "&&&&&&&&&&&2")
    else
        data["src_rx"] = data["src_rx"] or ""
        data["src_tx"] = data["src_tx"] or ""
        data["src_vlan"] = datalst_trans(data["src_vlan"] or "")
        data["to"] = data["to"] or ""
        data["to_switch"] = (mirror_modetrans(data["mode"]) == "2") and "1" or data["to_switch"] or ""
        data["rspan_vlan"] = data["rspan_vlan"] or ""
        librpc.callapi("oltmib_pminfo_set_1", data["sid"] .. "&&&&&&&&&&&2") -- del first
        if data["src_vlan"] == "" and data["src_rx"] == "" and data ["src_tx"] == "" then
            result = librpc.callapi("oltmib_pminfo_set_1", data["sid"] .. "&" .. mirror_modetrans(data["mode"]) .. "&" .. (data["desc"] or "") .. "&"  .. data["to"].. "&" .. data["to_switch"] .. "&" .. data["rspan_vlan"] .. "&&&"
                    .. mirror_dirtrans("disable") .. "&" .. mirror_statetrans(data["state"]) .. "&&" .. (data["oper"] or ""))
            if result ~= "0" then -- one fail all fail
                librpc.callapi("oltmib_pminfo_set_1", data["sid"] .. "&&&&&&&&&&&2") -- del first
                return false
            end
        end

        if (data["src_vlan"] ~= "") then
            result = librpc.callapi("oltmib_pminfo_set_1", data["sid"] .. "&" .. mirror_modetrans(data["mode"]) .. "&" .. (data["desc"] or "") .. "&" .. data["to"].. "&" .. data["to_switch"] .. "&" .. data["rspan_vlan"] .. "&&" .. data["src_vlan"] .. "&"
                    .. mirror_dirtrans("rx") .. "&" .. mirror_statetrans(data["state"]) .. "&&" .. (data["oper"] or ""))
            if result ~= "0" then -- one fail all fail
                librpc.callapi("oltmib_pminfo_set_1", data["sid"] .. "&&&&&&&&&&&2") -- del first
                return false
            end
        end

        local srclst1 = string.split(datalst_trans(data["src_rx"]), ',')
        for _, src in pairs(srclst1) do
            result = librpc.callapi("oltmib_pminfo_set_1", data["sid"] .. "&" .. mirror_modetrans(data["mode"]) .. "&" .. (data["desc"] or "") .. "&" .. data["to"].. "&" .. data["to_switch"] .. "&" .. data["rspan_vlan"] .. "&" .. src .. "&&"
                    .. mirror_dirtrans("rx") .. "&" .. mirror_statetrans(data["state"]) .. "&&" .. (data["oper"] or ""))
            if result ~= "0" then -- one fail all fail
                librpc.callapi("oltmib_pminfo_set_1", data["sid"] .. "&&&&&&&&&&&2") -- del first
                return false
            end
        end

        local srclst2 = string.split(datalst_trans(data["src_tx"]), ',')
        for _, src in pairs(srclst2) do
            result = librpc.callapi("oltmib_pminfo_set_1", data["sid"] .. "&" .. mirror_modetrans(data["mode"]) .. "&" .. (data["desc"] or "") .. "&" .. data["to"].. "&" .. data["to_switch"] .. "&" .. data["rspan_vlan"] .. "&" .. src .. "&&"
                    .. mirror_dirtrans("tx") .. "&" .. mirror_statetrans(data["state"]) .. "&&" .. (data["oper"] or ""))
            if result ~= "0" then -- one fail all fail
                librpc.callapi("oltmib_pminfo_set_1", data["sid"] .. "&&&&&&&&&&&2") -- del first
                return false
            end
        end
    end
    return true
end

function getratelimittbl()
    ratelimittable = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_ratelimitinfo_getn_1", str)
        _, _, ifx, name, in_cir, in_cbs, out_cir, out_cbs, msg, oper, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["ifx"] = tostring(ifx)
            row["name"] = tostring(name)
            row["in_cir"] = tostring(in_cir)
            row["in_cbs"] = tostring(in_cbs)
            row["out_cir"] = tostring(out_cir)
            row["out_cbs"] = tostring(out_cbs)
            table.insert(ratelimittable, row)
        end
    end
    return ratelimittable
end

function setratelimit(data)
    result = librpc.callapi("oltmib_ratelimitinfo_set_1", data["ifx"] .. "&" .. (data["name"] or "") .. "&" .. data["in_cir"] .. "&" .. data["in_cbs"] .. "&" .. data["out_cir"] .. "&" .. data["out_cbs"])
    return result == "0"
end

function storm_typetrans(mytype)
    local trans = {}
    trans["0"] = "disabled"
    trans["1"] = "broadcast"
    trans["2"] = "multicast"
    trans["3"] = "unicast"
    trans["4"] = "multicast_broadcast"
    trans["5"] = "unicast_broadcast"
    trans["6"] = "all"
    trans["disabled"] = "0"
    trans["broadcast"] = "1"
    trans["multicast"] = "2"
    trans["unicast"] = "3"
    trans["multicast_broadcast"] = "4"
    trans["unicast_broadcast"] = "5"
    trans["all"] = "6"
    return trans[tostring(mytype)] or ""
end

function getstormcontrolopts()
    return { "disabled", "broadcast", "multicast", "unicast", "multicast_broadcast", "unicast_broadcast", "all" }
end

function getstormcontroltbl()
    stormcontroltable = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_stormcontrolinfo_getn_1", str)
        _, _, ifx, name, mytype, level, fraction, msg, oper, result = string.find(str, string.rep("(.-)&", 7) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["ifx"] = ifx
            row["name"] = name
            row["type"] = storm_typetrans(mytype)
            row["level"] = level
            row["fraction"] = fraction
            if row["type"] == "disabled" then
                row["value"] = 0
            else
                row["value"] = tonumber(level) + tonumber(fraction) / 100
            end

            table.insert(stormcontroltable, row)
        end
    end
    return stormcontroltable
end

function setstormcontrol(data)
    val = tonumber(data["value"])
    data["level"] = math.floor(val)
    data["fraction"] = math.floor(val * 100 % 100)
    --dbgprint("set storm ifx "..data["ifx"].." name "..data["name"].." type "..data["type"].." value "..data["value"].." level "..data["level"].." fraction "..data["fraction"])
    result = librpc.callapi("oltmib_stormcontrolinfo_set_1", data["ifx"] .. "&" .. data["name"] .. "&" .. storm_typetrans(data["type"]) .. "&" .. data["level"] .. "&" .. data["fraction"])
end

--[[
function dhcpsnpstatus_trans(status)
    local trans = {}
    trans["0"] = "disabled"
    trans["1"] = "enabled"
    trans["disabled"] = "0"
    trans["enabled"] = "1"
    return trans[tostring(status)] or ""
end

function getdhcpsnpopts()
    return { "disabled", "enabled" }
end

function getdhcpsnpstatus()
    result = "0"
    str = ""
    str = librpc.callapi("oltmib_dhcpsnp_status_get_1", str)
    _, _, status, msg, oper, result = string.find(str, string.rep("(.-)&", 3) .. "(.*)")
    return status or ""
end

function setdhcpsnpstatus(data)
    result = librpc.callapi("oltmib_dhcpsnp_status_set_1", data["status"])
end

function getdhcpsnptrusttbl()
    dhcpsnptrusttable = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_dhcpsnp_trustinfo_getn_1", str)
        _, _, ifx, name, trust, msg, oper, result = string.find(str, string.rep("(.-)&", 5) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["ifx"] = tostring(ifx)
            row["name"] = tostring(name)
            row["trust"] = dhcpsnpstatus_trans(trust)
            dhcpsnptrusttable[tonumber(ifx)] = row
        end
    end
    return dhcpsnptrusttable
end

function setdhcpsnptrust(data)
    --dbgprint("set dhcpsnp trust ifx "..data["ifx"].." name "..data["name"].." trust "..data["trust"])
    result = librpc.callapi("oltmib_dhcpsnp_trustinfo_set_1", data["ifx"] .. "&" .. data["name"] .. "&" .. dhcpsnpstatus_trans(data["trust"]))
end
]]--

function qosalg_trans(alg)
    local trans = {}
    trans["0"] = "sp"
    trans["1"] = "wrr"
    trans["sp"] = "0"
    trans["wrr"] = "1"
    return trans[tostring(alg)] or ""
end

function getqoscfg()
    str = librpc.callapi("oltmib_qoscfg_get_1", "")
    _, _, status, alg, msg, oper, result = string.find(str, string.rep("(.-)&", 4) .. "(.*)")
    if (result == "0") then
        return { status = status, alg = qosalg_trans(alg) }
    end
    return {}
end

function setqoscfg(data)
    --dbgprint("set qos status " .. data["status"] .. " alg " .. data["alg"])
    str = data["status"] .. "&" .. qosalg_trans(data["alg"])
    return librpc.callapi("oltmib_qoscfg_set_1", str) == "0"
end

function getqueueweighttbl()
    local tbl = {}
    str = librpc.callapi("oltmib_queueweight_get_1", "")
    _, _, lst, msg, oper, result = string.find(str, string.rep("(.-)&", 3) .. "(.*)")
    if (result == "0") then
        for i, v in ipairs(string.split(lst, ',')) do
            tbl[i] = { queue = tostring(i - 1), weight = v }
        end
    end
    return tbl
end

function setqueueweight(data)
    local lst = ""
    for i, v in ipairs(data) do
        lst = lst .. v["weight"] .. ","
    end
    --dbgprint("set queueweight queue " .. lst)
    return librpc.callapi("oltmib_queueweight_set_1", lst) == "0"
end

function getcos2dscptbl()
    local tbl = {}
    str = librpc.callapi("oltmib_cos2dscp_get_1", "")
    _, _, lst, msg, oper, result = string.find(str, string.rep("(.-)&", 3) .. "(.*)")
    if (result == "0") then
        for i, v in ipairs(string.split(lst, ',')) do
            tbl[i] = { cos = tostring(i - 1), dscp = v }
        end
    end
    return tbl
end

function setcos2dscp(data)
    --dbgprint("set cos2dscp cos " .. data["cos"] .. " dscp " .. data["dscp"])
    local lst = ""
    for i, v in ipairs(data) do
        lst = lst .. v["dscp"] .. ","
    end
    return librpc.callapi("oltmib_cos2dscp_set_1", lst) == "0"
end

function getcos2queuetbl()
    local tbl = {}
    str = librpc.callapi("oltmib_cos2queue_get_1", "")
    _, _, lst, msg, oper, result = string.find(str, string.rep("(.-)&", 3) .. "(.*)")
    if (result == "0") then
        for i, v in ipairs(string.split(lst, ',')) do
            tbl[i] = { cos = tostring(i - 1), queue = v }
        end
    end
    return tbl
end

function setcos2queue(data)
    --dbgprint("set cos2queue cos " .. data["cos"] .. " queue " .. data["queue"])
    local lst = ""
    for i, v in ipairs(data) do
        lst = lst .. v["queue"] .. ","
    end
    return librpc.callapi("oltmib_cos2queue_set_1", lst) == "0"
end

function getdscp2costbl()
    local tbl = {}
    str = librpc.callapi("oltmib_dscp2cos_get_1", "")
    _, _, lst, msg, oper, result = string.find(str, string.rep("(.-)&", 3) .. "(.*)")
    if (result == "0") then
        --dbgprint("get dscp2cos " .. lst)
        for i, v in ipairs(string.split(lst, ',')) do
            tbl[i] = { dscp = tostring(i - 1), cos = v }
        end
    else -- always show
        for i, v in ipairs(string.split(lst, ',')) do
            tbl[i] = { dscp = tostring(i - 1), cos = "-" }
        end
    end
    return tbl
end

function setdscp2cos(data)
    local lst = ""
    local oper = 2
    for i, v in ipairs(data) do
        if v["cos"] ~= "-" then
            oper = 1
        end
        lst = lst .. (tonumber(v["cos"]) or math.floor((i - 1) / 8)) .. ","
    end
    --dbgprint("set dscp2cos " .. lst)
    return librpc.callapi("oltmib_dscp2cos_set_1", lst .. "&&" .. oper) == "0"
end

function getdscp2dscptbl()
    local tbl = {}
    str = librpc.callapi("oltmib_dscp2dscp_get_1", "")
    _, _, lst, msg, oper, result = string.find(str, string.rep("(.-)&", 3) .. "(.*)")
    if (result == "0") then
        for i, v in ipairs(string.split(lst, ',')) do
            tbl[i] = { dscp1 = tostring(i - 1), dscp2 = v }
        end
    else -- always show
        for i, v in ipairs(string.split(lst, ',')) do
            tbl[i] = { dscp1 = tostring(i - 1), dscp2 = "-" }
        end
    end
    return tbl
end

function setdscp2dscp(data)
    local lst = ""
    local oper = 2
    for i, v in ipairs(data) do
        if v["dscp2"] ~= "-" then
            oper = 1
        end
        lst = lst .. (tonumber(v["dscp2"]) or (i - 1)) .. ","
    end
    --dbgprint("set dscp2dscp dscp " .. lst)
    return librpc.callapi("oltmib_dscp2dscp_set_1", lst .. "&&" .. oper) == "0"
end

function getdscp2queuetbl()
    local tbl = {}
    str = librpc.callapi("oltmib_dscp2queue_get_1", "")
    _, _, lst, msg, oper, result = string.find(str, string.rep("(.-)&", 3) .. "(.*)")
    if (result == "0") then
        --dbgprint("get dscp2queue " .. lst)
        for i, v in ipairs(string.split(lst, ',')) do
            tbl[i] = { dscp = tostring(i - 1), queue = v }
        end
    end
    return tbl
end

function setdscp2queue(data)
    local lst = ""
    for i, v in ipairs(data) do
        lst = lst .. (tonumber(v["queue"]) or math.floor((i - 1) / 8)) .. ","
    end
    --dbgprint("set dscp2queue " .. lst)
    return librpc.callapi("oltmib_dscp2queue_set_1", lst) == "0"
end

function qos_trustmodeopts()
    return { "none", "cos", "dscp" }
end

function qos_trustmodetrans(mode)
    local trans = {}
    trans["0"] = "none"
    trans["1"] = "cos"
    trans["2"] = "dscp"
    trans["none"] = "0"
    trans["cos"] = "1"
    trans["dscp"] = "2"
    return trans[tostring(mode)] or ""
end

-- function getqostrustiftbl()
--     tbl = {}
--     result = "0"
--     str = ""
--     while (result == "0") do
--         str = librpc.callapi("oltmib_qostrustif_getn_1", str)
--         _, _, ifx, name, trustmode, cos, qosin, qosout, msg, oper, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
--         if (result == "0") then
--             local row = {}
--             row["ifx"] = ifx
--             row["name"] = name
--             row["trustmode"] = qos_trustmodetrans(trustmode)
--             row["cos"] = cos
--             row["in"] = qosin
--             row["out"] = qosout
--             tbl[tonumber(ifx)] = row
--         end
--     end
--     return tbl
-- end

-- function setqostrustif(data, oper)
--     --dbgprint("set qostrustif name " .. data["name"])
--     librpc.callapi("oltmib_qostrustif_set_1", data["ifx"] .. "&" .. data["name"] .. "&" .. qos_trustmodetrans(data["trustmode"]) .. "&" .. data["cos"] .. "&" .. data["in"] .. "&" .. data["out"] .. "&&" .. oper)
-- end

function getqosiftbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_qosif_getn_1", str)
        _, _, ifx, name, trustmode, cos, qosin, qosout, msg, oper, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["ifx"] = ifx
            row["name"] = name
            row["trustmode"] = qos_trustmodetrans(trustmode)
            row["cos"] = cos
            row["in"] = qosin
            row["out"] = qosout
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setqosif(data, oper)
    --dbgprint("set qosif name " .. data["name"])
    return librpc.callapi("oltmib_qosif_set_1", data["ifx"] .. "&" .. data["name"] .. "&" .. qos_trustmodetrans(data["trustmode"]) .. "&" .. data["cos"] .. "&" .. data["in"] .. "&" .. data["out"] .. "&&" .. oper) == "0"
end

function getqospolicyiftbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_qospolicyif_getn_1", str)
        _, _, ifx, name, trustmode, cos, qosin, qosout, msg, oper, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["ifx"] = ifx
            row["name"] = name
            row["trustmode"] = qos_trustmodetrans(trustmode)
            row["cos"] = cos
            row["in"] = qosin
            row["out"] = qosout
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setqospolicyif(data, oper)
    --dbgprint("set qospolicyif name " .. data["name"])
    result = librpc.callapi("oltmib_qospolicyif_set_1", data["ifx"] .. "&" .. data["name"] .. "&" .. qos_trustmodetrans(data["trustmode"]) .. "&" .. data["cos"] .. "&" .. data["in"] .. "&" .. data["out"] .. "&&" .. oper)
    return result == "0"
end

function class_matchtypeopts()
    return { "none", "acl", "etype", "dscp", "cos", "l4", "vlan-range", "vlan" }
end

function class_matchtypetrans(type)
    local trans = {}
    trans["0"] = "none"
    trans["1"] = "acl"
    trans["2"] = "etype"
    trans["3"] = "dscp"
    trans["4"] = "v6dscp"
    trans["5"] = "cos"
    trans["6"] = "l4"
    trans["7"] = "vlan-range"
    trans["8"] = "vlan"
    trans["none"] = "0"
    trans["acl"] = "1"
    trans["etype"] = "2"
    trans["dscp"] = "3"
    trans["v6dscp"] = "4"
    trans["cos"] = "5"
    trans["l4"] = "6"
    trans["vlan-range"] = "7"
    trans["vlan"] = "8"
    return trans[tostring(type)] or ""
end

function getclasstbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_class_getn_1", str)
        _, _, name, matchtype, value, msg, oper, result = string.find(str, string.rep("(.-)&", 5) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["name"] = name
            row["matchtype"] = class_matchtypetrans(matchtype)
            row["value"] = value
            table.insert(tbl, row)
        end
    end
    return tbl
end

function getclass(data)
    str = librpc.callapi("oltmib_class_get_1", data["name"])
    _, _, name, matchtype, value, msg, oper, result = string.find(str, string.rep("(.-)&", 5) .. "(.*)")
    if (result == "0") then
        local row = {}
        row["name"] = name
        row["matchtype"] = class_matchtypetrans(matchtype)
        row["value"] = value
        return row
    end
    return {}
end

function setclass(data, oper)
    --dbgprint("set class name " .. data["name"])
    str = data["name"] .. "&" .. class_matchtypetrans(data["matchtype"]) .. "&" .. data["value"] .. "&&" .. oper
    return librpc.callapi("oltmib_class_set_1", str) == "0"
end

function policy_settypeopts()
    return { "none", "cos", "dscp", "vlan" }
end

function policy_settypetrans(type)
    local trans = {}
    trans["0"] = "none"
    trans["1"] = "cos"
    trans["2"] = "dscp"
    trans["10"] = "vlan"
    trans["none"] = "0"
    trans["cos"] = "1"
    trans["dscp"] = "2"
    trans["vlan"] = "10"
    return trans[tostring(type)] or ""
end

function policy_policeopts()
    return { "none", "ratelimit" }-- "srtcm", "trtcm"}
end

function policy_policetrans(type)
    local trans = {}
    trans["0"] = "none"
    trans["1"] = "none"
    --trans["2"] = "srtcm"
    trans["2"] = "ratelimit"
    trans["3"] = "trtcm"
    trans["none"] = "1"
    --trans["srtcm"] = "2"
    trans["ratelimit"] = "2"
    trans["trtcm"] = "3"
    return trans[tostring(type)] or ""
end

function getpolicytbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_policy_getn_1", str)
        _, _, name, cname, settype, setval, police, cir, cbs, pir, action, msg, oper, result = string.find(str, string.rep("(.-)&", 11) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["name"] = name
            row["cname"] = cname
            row["settype"] = policy_settypetrans(settype)
            row["setval"] = setval
            row["police"] = policy_policetrans(police)
            row["cir"] = cir
            row["cbs"] = cbs
            row["pir"] = pir
            row["action"] = action
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setpolicy(data, oper)
    --dbgprint("set policy name " .. data["name"] .. " oper " .. oper)
    str = data["name"] .. "&" .. data["cname"] .. "&" .. policy_settypetrans(data["settype"]) .. "&" ..
    (data["setval"] or "") .. "&" .. policy_policetrans(data["police"]) .. "&" .. (data["cir"] or "") ..
    "&" .. (data["cbs"] or "") .. "&" .. (data["pir"] or "") .. "&" .. (data["action"] or "") .. "&&" .. oper
    return librpc.callapi("oltmib_policy_set_1", str) == '0'
end

function getmacparam()
    str = librpc.callapi("oltmib_fdbparam_get_1", "")
    _, _, agetime, msg, oper, result = string.find(str, string.rep("(.-)&", 3) .. "(.*)")
    return { name = translate("Aging Time(s)"), value = agetime }
end

function setmacparam(data)
    librpc.callapi("oltmib_fdbparam_set_1", data["value"])
end

function getstaticmactbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_fdb_getn_1", str)
        _, _, mac, vid, ifname, is_forward, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
        if (result == "0" and is_forward == "1") then
            local row = {}
            row["mac"] = mac
            row["vid"] = vid
            row["ifname"] = ifname
            table.insert(tbl, row)
        end
    end
    return tbl
end

function getstaticmac()
    return { mac = "", vid = "", ifname = "" }
end

function setstaticmac(data)
    return librpc.callapi("oltmib_fdb_set_1", mac_trans(data["mac"]) .. "&" .. data["vid"] .. "&" .. data["ifname"] .. "&" .. "1" .. "&&" .. (data["oper"] or "")) == "0"
end

function getfiltermactbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_fdb_getn_1", str)
        _, _, mac, vid, ifname, is_forward, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
        if (result == "0" and is_forward == "0") then
            local row = {}
            row["mac"] = mac
            row["vid"] = vid
            row["ifname"] = ifname
            table.insert(tbl, row)
        end
    end
    return tbl
end

function getfiltermac()
    return { mac = "", vid = "" }
end

function setfiltermac(data)
    return librpc.callapi("oltmib_fdb_set_1", mac_trans(data["mac"]) .. "&" .. data["vid"] .. "&&" .. "0" .. "&&" .. (data["oper"] or "")) == "0"
end

function poelegacy_trans(val)
    local trans = {}
    trans["0"] = "OFF"
    trans["1"] = "ON"
    trans["OFF"] = "0"
    trans["ON"] = "1"
    return trans[val] or ""
end
function getpoeinfo()
    local row = {}
    str = librpc.callapi("oltmib_poeinfo_get_1", "")
    _, _, power_consume, powered_ports, msg, oper, result = string.find(str, string.rep("(.-)&", 4) .. "(.*)") -- str maybe nil
    if (result == "0") then
        row["power_consume"] = tonumber(power_consume) / 10
        row["powered_ports"] = powered_ports
    end
    return row
end
function setpoeinfo(data)
    return librpc.callapi("oltmib_poeinfo_set_1", "&" .. tonumber(data["power_consume"]) * 10 .. "&" .. data["powered_ports"]) == "0"
end

function getpoeconf()
    local row = {}
    str = librpc.callapi("oltmib_poeconf_get_1", "")
    _, _, power_supply, power_supply_def, res_percent, alarm_percent, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)") -- str maybe nil
    if (result == "0") then
        row["power_supply"] = tonumber(power_supply) / 10
        row["power_supply_def"] = tonumber(power_supply_def) / 10
        row["res_percent"] = tonumber(res_percent)
        row["alarm_percent"] = tonumber(alarm_percent)
    end
    return row
end
function setpoeconf(data)
    return librpc.callapi("oltmib_poeconf_set_1", tonumber(data["power_supply"]) * 10 .. "&&" .. data["res_percent"] .. "&" .. data["alarm_percent"]) == "0"
end

function poereason_trans(val)
    local trans = {}
    trans["2"] = "Unknown"
    trans["5"] = "Short"
    trans["6"] = "Overflow"
    trans["7"] = "Overload"
    trans["8"] = "Management"
    return trans[val] or "--"
end

function poeclass_trans(val)
    local num = tonumber(val)
    if num > 0 and num < 10 then
        return tostring(num - 1)
    else
        return "-"
    end
end

function poeiftype_trans(val)
    local num = tonumber(val)
    if num > 0 then
        return "BT"
    else
        return "AT"
    end
end

function getpoeifinfotbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_poeifinfo_getn_1", str)
        _, _, ifx, name, poe_enable, force_on, desc, status, power_consume, icut, pd_class, errdis_state, mpsabsent_counter, 
            invalid_signature_counter, power_denied_counter, overload_counter, short_counter, mtype, msg, oper, result = string.find(str or "", string.rep("(.-)&", 18) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["id"] = tonumber(ifx)
            row["name"] = name
            row["admin_state"] = (poe_enable == "1")
            row["force_on"] = (force_on == "1")
            row["desc"] = desc
            row["status"] = (status == "1")
            row["reason"] = poereason_trans(status)
            row["power"] = tonumber(power_consume) / 10
            row["icut"] = tonumber(icut) / 10
            row["class"] = poeclass_trans(pd_class)
            row["errdis_state"] = (errdis_state == "1")
            row["mpsabsent_counter"] = tonumber(mpsabsent_counter)
            row["invalid_signature_counter"] = tonumber(invalid_signature_counter)
            row["power_denied_counter"] = tonumber(power_denied_counter)
            row["overload_counter"] = tonumber(overload_counter)
            row["short_counter"] = tonumber(short_counter)
            row["type"] = poeiftype_trans(mtype)
            table.insert(tbl, row)
        end
    end
    return tbl
end
function setpoeifinfo(data)
    str = data["id"] .. "&" .. (data["name"] or "") .. "&" .. bool2int(data["admin_state"]) .. "&" .. bool2int(data["force_on"])
    result = librpc.callapi("oltmib_poeifinfo_set_1", str)
    return result == "0"
end

function poepriority_trans(val)
    local trans = {}
    trans["1"] = "Low"
    trans["2"] = "Medium"
    trans["3"] = "High"
    trans["Low"] = "1"
    trans["Medium"] = "2"
    trans["High"] = "3"
    return trans[val] or ""
end
function poepddetmode_trans(val)
    local trans = {}
    trans["0"] = "None"
    trans["1"] = "Flow"
    trans["2"] = "Ping"
    trans["None"] = "0"
    trans["Flow"] = "1"
    trans["Ping"] = "2"
    return trans[val] or ""
end
function getpoeifconftbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_poeifconf_getn_1", str)
        _, _, ifx, name, poe_enable, desc, max_power, max_power_max, priority, pddet_mode, pddet_ipstr, pddet_interval, pddet_times, force_on, legacy, msg, oper, result = string.find(str or "", string.rep("(.-)&", 15) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["id"] = tonumber(ifx)
            row["name"] = name
            row["admin_state"] = (poe_enable == "1")
            row["desc"] = desc
            row["max_power"] = tonumber(max_power)
            row["max_power_max"] = tonumber(max_power_max)
            row["priority"] = poepriority_trans(priority)
            row["pddet_mode"] = poepddetmode_trans(pddet_mode)
            row["pddet_ipstr"] = pddet_ipstr
            row["pddet_interval"] = tonumber(pddet_interval)
            row["pddet_times"] = tonumber(pddet_times)
            row["force_on"] = (force_on == "1")
            row["legacy"] = (legacy == "1")
            table.insert(tbl, row)
        end
    end
    return tbl
end
function setpoeifconf(data)
    str = data["id"] .. "&" .. (data["name"] or "") .. "&" .. bool2int(data["admin_state"]) .. "&" .. data["desc"] .. "&" .. data["max_power"]
        .. "&&" .. poepriority_trans(data["priority"]) .. "&" .. poepddetmode_trans(data["pddet_mode"]) .. "&" .. data["pddet_ipstr"] .. "&" .. data["pddet_interval"]
        .. "&" .. data["pddet_times"] .. "&" .. bool2int(data["force_on"]) .. "&" .. bool2int(data["legacy"])
    result = librpc.callapi("oltmib_poeifconf_set_1", str)
    return result == "0"
end

function getagalg()
    return { "dst-mac", "src-mac", "src-dst-mac", "dst-ip", "src-ip", "src-dst-ip", "dst-port", "src-port", "src-dst-port" }
end

function agalg_trans(val)
    local trans = {}
    trans["1"] = "dst_mac"
    trans["2"] = "src_mac"
    trans["3"] = "src_dst_mac"
    trans["4"] = "src_ip"
    trans["5"] = "dst_ip"
    trans["6"] = "src_dst_ip"
    trans["7"] = "src_port"
    trans["8"] = "dst_port"
    trans["9"] = "src_dst_port"
    trans["dst_mac"] = "1"
    trans["src_mac"] = "2"
    trans["src_dst_mac"] = "3"
    trans["src_ip"] = "4"
    trans["dst_ip"] = "5"
    trans["src_dst_ip"] = "6"
    trans["src_port"] = "7"
    trans["dst_port"] = "8"
    trans["src_dst_port"] = "9"
    return trans[val] or "-"
end

function getagsys()
    str = librpc.callapi("oltmib_agsys_get_1", "")
    _, _, alg, msg, oper, result = string.find(str, string.rep("(.-)&", 3) .. "(.*)")
    return { { name = translate("Load balancing method"), value = agalg_trans(alg) } }
end

function setagsys(data)
    return librpc.callapi("oltmib_agsys_set_1", agalg_trans(data["value"] or "")) == "0"
end

function getagmode()
    return { "Manual", "Active", "Passive" }
end
function agmode_trans(val)
    local trans = {}
    trans["1"] = "Manual"
    trans["2"] = "Active"
    trans["3"] = "Passive"
    trans["-"] = "0"
    trans["Manual"] = "1"
    trans["Active"] = "2"
    trans["Passive"] = "3"
    return trans[val] or "-"
end

function getagtbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_ag_getn_1", str)
        _, _, ifx, name, key, mode, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["ifx"] = ifx
            row["name"] = name
            if key == "0" then
                row["key"] = "-"
            else
                row["key"] = key
            end
            row["mode"] = agmode_trans(mode)
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setag(data)
    result = librpc.callapi("oltmib_ag_set_1", data["ifx"] .. "&&" .. data["key"] .. "&" .. agmode_trans(data["mode"]) .. "&&" .. (data["oper"] or ""))
    return result == "0"
end

function getauthglobal()
    local row = {}
    str = librpc.callapi("oltmib_auth_global_get_1", "")
    _, _, config, msg, oper, result = string.find(str, string.rep("(.-)&", 3) .. "(.*)")
    if (result == "0") then
        row["config"] = tonumber(config)
    end
    return row
end

function setauthglobal(data)
    str = data["config"] .. "&&" .. (data["oper"] or "")
    result = librpc.callapi("oltmib_auth_global_set_1", str)
    return result == "0"
end

function d1x_portctrl_str()
    return { "Disabled", "Auto" } --"Force Unauthorized", "Force Authorized", 
end
function d1x_portctrl_trans(val)
    local trans = {}
    trans["0"] = "Disable"
    trans["1"] = "Force Unauthorized"
    trans["2"] = "Force Authorized"
    trans["3"] = "Auto"
    trans["Disable"] = "0"
    trans["Force Unauthorized"] = "1"
    trans["Force Authorized"] = "2"
    trans["Auto"] = "3"
    return trans[val] or "Disabled"
end
function d1x_ctrldir_str()
    return { "Both", "In" }
end
function d1x_ctrldir_trans(val)
    local trans = {}
    trans["0"] = "Both"
    trans["1"] = "In"
    trans["Both"] = "0"
    trans["In"] = "1"
    return trans[val] or "-"
end

function getd1xport(data)
    str = data["ifx"]
    local row = {}
    str = librpc.callapi("oltmib_d1x_pcfg_get_1", str)
    _, _, row["ifx"], row["name"], row["portControl"], row["adminControlledDirections"], row["keyTxEnabled"], row["protocol_version"], row["quietPeriod"],
    row["txPeriod"], row["reAuthEnabled"], row["reAuthPeriod"], row["suppTimeout"], row["serverTimeout"], msg, oper, result = string.find(str, string.rep("(.-)&", 14) .. "(.*)")
    if (result == "0") then
        row["portControl"] = d1x_portctrl_trans(row["portControl"])
        row["adminControlledDirections"] = d1x_ctrldir_trans(row["adminControlledDirections"])
        row["keyTxEnabled"] = ablity_trans(row["keyTxEnabled"])
        row["reAuthEnabled"] = ablity_trans(row["reAuthEnabled"])
    end
    return row
end

function getd1xporttbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_d1x_pcfg_getn_1", str)
        _, _, row["ifx"], row["name"], row["portControl"], row["adminControlledDirections"], row["keyTxEnabled"], row["protocol_version"], row["quietPeriod"],
        row["txPeriod"], row["reAuthEnabled"], row["reAuthPeriod"], row["suppTimeout"], row["serverTimeout"], msg, oper, result = string.find(str, string.rep("(.-)&", 14) .. "(.*)")
        if (result == "0") then
            row["portControl"] = d1x_portctrl_trans(row["portControl"])
            row["adminControlledDirections"] = d1x_ctrldir_trans(row["adminControlledDirections"])
            row["keyTxEnabled"] = ablity_trans(row["keyTxEnabled"])
            row["reAuthEnabled"] = ablity_trans(row["reAuthEnabled"])
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setd1xport(row)
    str = row["ifx"] .. "&&" .. d1x_portctrl_trans(row["portControl"]) .. "&" .. d1x_ctrldir_trans(row["adminControlledDirections"]) .. "&" .. ablity_trans(row["keyTxEnabled"])
    .. "&" .. row["protocol_version"] .. "&" .. row["quietPeriod"] .. "&" .. row["txPeriod"] .. "&" .. ablity_trans(row["reAuthEnabled"]) .. "&" .. row["reAuthPeriod"]
    .. "&" .. row["suppTimeout"] .. "&" .. row["serverTimeout"]
    result = librpc.callapi("oltmib_d1x_pcfg_set_1", str)
    return result == "0"
end

function d1x_portstatus_trans(val)
    local trans = {}
    trans["0"] = "-"
    trans["1"] = "Authorized"
    trans["2"] = "Unauthorized"
    trans["-"] = "0"
    trans["Authorized"] = "1"
    trans["Unauthorized"] = "2"
    return trans[val] or "-"
end
function d1x_paestate_trans(val)
    local trans = {}
    trans["0"] = "Down"
    trans["1"] = "Init"
    trans["2"] = "Disconnected"
    trans["3"] = "Connecting"
    trans["4"] = "Authenticating"
    trans["5"] = "Authenticated"
    trans["6"] = "Aborting"
    trans["7"] = "Held"
    trans["8"] = "Force Auth"
    trans["9"] = "Force Unauth"
    trans["10"] = "Restart"
    return trans[val] or "-"
end

function getd1xportsttbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_d1x_pst_getn_1", str)
        _, _, row["ifx"], row["name"], row["portEnabled"], row["portControl"], row["portStatus"], row["pae_state"], msg, oper, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            row["portEnabled"] = ablity_trans(row["portEnabled"])
            row["portControl"] = d1x_portctrl_trans(row["portControl"])
            row["portStatus"] = d1x_portstatus_trans(row["portStatus"])
            row["pae_state"] = d1x_paestate_trans(row["pae_state"])
            table.insert(tbl, row)
        end
    end
    return tbl
end

function ma_portctrl_str()
    return { "Disable", "Enable" }
end
function ma_portctrl_trans(val)
    local trans = {}
    trans["0"] = "-"
    trans["1"] = "Enable"
    trans["2"] = "Disable"
    trans["-"] = "0"
    trans["Enable"] = "1"
    trans["Disable"] = "2"
    return trans[val] or "-"
end
function ma_portmode_str()
    return { "-", "Shutdown", "Filter" }
end
function ma_portmode_trans(val)
    local trans = {}
    trans["0"] = "-"
    trans["1"] = "Shutdown"
    trans["2"] = "Filter"
    trans["-"] = "0"
    trans["Shutdown"] = "1"
    trans["Filter"] = "2"
    return trans[val] or "-"
end
function ma_failaction_str()
    return { "Drop traffic", "Restrict VLAN" }
end
function ma_failaction_trans(val)
    local trans = {}
    trans["0"] = "Restrict VLAN"
    trans["1"] = "Drop traffic"
    trans["Restrict VLAN"] = "0"
    trans["Drop traffic"] = "1"
    return trans[val] or "-"
end

function getmacauthport(data)
    str = data["ifx"]
    local row = {}
    str = librpc.callapi("oltmib_macauth_pcfg_get_1", str)
    _, _, row["ifx"], row["name"], row["authmacPortControl"], row["authmacPortMode"], row["dynamic_vlan_creation"], row["mac_address_aging"], row["auth_fail_action"],
    row["restrict_vid"], msg, oper, result = string.find(str, string.rep("(.-)&", 10) .. "(.*)")
    if (result == "0") then
        row["authmacPortControl"] = ma_portctrl_trans(row["authmacPortControl"])
        row["authmacPortMode"] = ma_portmode_trans(row["authmacPortMode"])
        row["dynamic_vlan_creation"] = ablity_trans(row["dynamic_vlan_creation"])
        row["mac_address_aging"] = ablity_trans(row["mac_address_aging"])
        row["auth_fail_action"] = ma_failaction_trans(row["auth_fail_action"])
    end
    return row
end

function getmacauthporttbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_macauth_pcfg_getn_1", str)
        _, _, row["ifx"], row["name"], row["authmacPortControl"], row["authmacPortMode"], row["dynamic_vlan_creation"], row["mac_address_aging"], row["auth_fail_action"],
        row["restrict_vid"], msg, oper, result = string.find(str, string.rep("(.-)&", 10) .. "(.*)")
        if (result == "0") then
            row["authmacPortControl"] = ma_portctrl_trans(row["authmacPortControl"])
            row["authmacPortMode"] = ma_portmode_trans(row["authmacPortMode"])
            row["dynamic_vlan_creation"] = ablity_trans(row["dynamic_vlan_creation"])
            row["mac_address_aging"] = ablity_trans(row["mac_address_aging"])
            row["auth_fail_action"] = ma_failaction_trans(row["auth_fail_action"])
            if row["auth_fail_action"] ~= "Restrict VLAN" then
                row["restrict_vid"] = ""
            end
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setmacauthport(row)
    str = row["ifx"] .. "&&" .. ma_portctrl_trans(row["authmacPortControl"]) .. "&" .. ma_portmode_trans(row["authmacPortMode"]) .. "&" .. ablity_trans(row["dynamic_vlan_creation"])
    .. "&" .. ablity_trans(row["mac_address_aging"]) .. "&" .. ma_failaction_trans(row["auth_fail_action"]) .. "&" .. row["restrict_vid"]
    result = librpc.callapi("oltmib_macauth_pcfg_set_1", str)
    return result == "0" 
end

function getmacauthusertbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_nsmauthmac_getn_1", str)
        _, _, row["vid"], row["mac"], row["is_dynamic"], row["fwd"], row["timestamp"], row["ifx"], row["ifname"], msg, oper, result = string.find(str, string.rep("(.-)&", 9) .. "(.*)")
        if (result == "0") then
            row["is_dynamic"] = ablity_trans(row["is_dynamic"])
            row["fwd"] = bool_trans(row["fwd"])
            row["timestamp"] = os.date("%Y-%m-%d %X", tonumber(row["timestamp"]))
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setmacauthuser(row)
    str = row["vid"] .. "&" .. row["mac"] .. "&" .. ablity_trans(row["is_dynamic"]) .. "&" .. bool_trans(row["fwd"]) .. "&&" .. row["ifx"] .. "&" .. row["ifname"] .. "&&" .. (row["oper"] or "")
    result = librpc.callapi("oltmib_nsmauthmac_set_1", str)
    return result == "0"
end

function getradglobal()
    local row = {}
    str = librpc.callapi("oltmib_radglobal_get_1", "")
    _, _, row["shared_secret"], row["key"], row["timeout"], row["max_retry"], row["deadtime"], row["srcif"], row["srcport"], msg, oper, result = string.find(str, string.rep("(.-)&", 9) .. "(.*)")
    if (result == "0") then
        return row
    end
    return {}
end

function setradglobal(row)
    str = row["shared_secret"] .. "&" .. row["key"] .. "&" .. row["timeout"] .. "&" .. row["max_retry"] .. "&" .. row["deadtime"] .. "&" .. row["srcif"] .. "&" .. row["srcport"] .. "&&" .. (row["oper"] or "")
    result = librpc.callapi("oltmib_radglobal_set_1", str)
    return result == "0"
end

function getradsrvtbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_radsrv_getn_1", str)
        _, _, row["ip"], row["auth_port"], row["acct_port"], row["shared_secret"], row["key"], row["timeout"], row["max_retry"],
        msg, oper, result = string.find(str, string.rep("(.-)&", 9) .. "(.*)")
        if (result == "0") then
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setradsrv(row)
    str = row["ip"] .. "&" .. row["auth_port"] .. "&" .. row["acct_port"] .. "&" .. row["shared_secret"] .. "&" .. row["key"] .. "&" .. row["timeout"] .. "&" .. row["max_retry"] .. "&&" .. (row["oper"] or "")
    result = librpc.callapi("oltmib_radsrv_set_1", str)
    return result == "0"
end

function vlanvpn_class_trans(val)
    local trans = {}
    trans["0"] = "Stacking"
    trans["1"] = "Mapping"
    trans["Stacking"] = "0"
    trans["Mapping"] = "1"
    return trans[val] or "-"
end

function getvlanvpn(data)
    local row = {}
    str = librpc.callapi("oltmib_vlanvpn_get_1", data["name"])
    _, _, row["name"], row["class"], row["rule"], row["apply"], msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
    porttbl = getporttable(11)
    row["apply"] = string.gsub(portmbr_idx2name(row["apply"], porttbl), ",", ", ")
    return row
end

function getvlanvpntbl()
    porttbl = getporttable(11)
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_vlanvpn_getn_1", str)
        _, _, row["name"], row["class"], row["rule"], row["apply"], msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
        if (result == "0") then
            row["class"] = vlanvpn_class_trans(row["class"])
            local rulelst = string.split(row["rule"], ";")
            row["rule"] = ""
            for i = 1, #rulelst do
                local vlanlst = string.split(rulelst[i], ":")
                if #vlanlst < 2 then
                    break
                end
                row["rule"] = row["rule"] .. "cvlan " .. vlanlst[2] .. " svlan " .. vlanlst[1] .. "\n"
            end
            row["apply"] = string.gsub(portmbr_idx2name(row["apply"], porttbl), ",", ", ")
            row["apply"] = datalst_trans(row["apply"])
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setvlanvpn(row)
    str = row["name"] .. "&&" .. row["rule"] .. "&&&" .. (row["oper"] or "")
    result = librpc.callapi("oltmib_vlanvpn_set_1", str)
    return result == "0"
end

function getvlanvpniftbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_vlanvpnif_getn_1", str)
        _, _, row["ifx"], row["name"], row["type"], row["enable_basic"], row["stack"], row["map"], msg, oper, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            row["type"] = tonumber(row["type"])
            row["enable_basic"] = ablity_trans(row["enable_basic"])
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setvlanvpnif(row)
    str = row["ifx"] .. "&&&" .. ablity_trans(row["enable_basic"]) .. "&" .. row["stack"] .. "&" .. row["map"]
    result = librpc.callapi("oltmib_vlanvpnif_set_1", str)
    return result == "0"
end

function onu_status_trans(val)
    local trans = {}
    trans["0"] = "Online"
    trans["1"] = "Ready"
    trans["2"] = "Offline"
    trans["Online"] = "0"
    trans["Ready"] = "1"
    trans["Offline"] = "2"
    return trans[val] or "-"
end
function onu_svc_trans(val)
    local ret = ""
    val = tonumber(val)
    if bit.band(val, 1) ~= 0 then
        ret = ret .. "GE "
    end
    if bit.band(val, 2) ~= 0 then
        ret = ret .. "FE "
    end
    if bit.band(val, 4) ~= 0 then
        ret = ret .. "VoIP "
    end
    if bit.band(val, 8) ~= 0 then
        ret = ret .. "TDM "
    end
    return ret
end
function onu_type_trans(val)
    local trans = {}
    trans["0"] = "SFU"
    trans["1"] = "HGU"
    trans["2"] = "SBU"
    trans["3"] = "BOX MDU of Ethernet interfaces"
    trans["4"] = "Small-sized Chassis MDU of Ethernet interfaces"
    trans["5"] = "Small-sized Chassis MDU of DSL interfaces"
    trans["6"] = "Medium-sized Chassis MDU of DSL interfaces"
    trans["7"] = "Chassis MDU of DSL interfaces and Ethernet interfaces"
    trans["8"] = "MTU"
    return trans[val] or "-"
end
function onu_ptype_trans(val)
    local trans = {}
    trans["0"] = "Not Support"
    trans["1"] = "Type C"
    trans["2"] = "Type D"
    return trans[val] or "-"
end
function getonu(row)
    str = librpc.callapi("oltmib_onuinfo_get_1", row["ifx"] .. "&" .. row["llid"])
    _, _, row["ifx"], row["llid"], row["mac"], row["ifname"], row["desc"], row["status"], row["timestamp"], row["distance"], row["oamver"], row["valid"], row["vendor"]
    , row["model"], row["onuid"], row["hwver"], row["swver"], row["frmverstr"], row["chip_vendorid"], row["chip_model"], row["chip_revision"],
    row["chip_date"], row["service"], row["num_ge"], row["bmp_gestr"], row["num_fe"], row["bmp_festr"], row["num_us_queue"],
    row["max_queue_usport"], row["num_ds_queue"], row["max_queue_dsport"], row["battery_backup"], row["cap2_valid"], row["onu_type"],
    row["multillid"], row["protetion_type"], row["num_pon"], row["num_slot"], row["num_if_type"], row["intfstr"], row["cap2_battery_backup"],
    msg, oper, result
    = string.find(str, string.rep("(.-)&", 41) .. "(.*)")
    if (result == "0") then
        row["name"] = row["ifname"] .. ":" .. row["llid"]
        row["status"] = onu_status_trans(row["status"])
        row["oamver"] = "0x" .. string.format("%X", tonumber(row["oamver"]))
        row["timestamp"] = os.date("%Y-%m-%d %X", tonumber(row["timestamp"]))
        row["frmverstr"] = "0x" .. row["frmverstr"]
        row["chip_vendorid"] = "0x" .. row["chip_vendorid"]
        row["chip_model"] = "0x" .. row["chip_model"]
        row["chip_revision"] = "0x" .. string.format("%X", tonumber(row["chip_revision"]))
        row["chip_date"] = "0x" .. row["chip_date"]
        row["service"] = onu_svc_trans(row["service"])
        row["battery_backup"] = bool_trans(row["battery_backup"])
        row["onu_type"] = onu_type_trans(row["onu_type"])
        row["protetion_type"] = onu_ptype_trans(row["protetion_type"])
        row["cap2_battery_backup"] = bool_trans(row["cap2_battery_backup"])
        row["bmp_gestr"] = hexstrreverse(row["bmp_gestr"])
        row["bmp_festr"] = hexstrreverse(row["bmp_festr"])
        local intf = {}
        string.gsub(row["intfstr"], '(........)', function(w) table.insert(intf, hexstrreverse(w)) end)
        row["intf"] = {}
        for i = 1, #intf / 2 do
            local iftype = tonumber(intf[2 * i - 1], 16)
            local ifnum = tonumber(intf[2 * i], 16)
            if ifnum > 0 then
                row["intf"][iftype] = ifnum
            end
        end
    end
    return row
end
function getonutbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_onuinfo_getn_1", str)
        _, _, row["ifx"], row["llid"], row["mac"], row["ifname"], row["desc"], row["status"], row["timestamp"], row["distance"], row["oamver"], row["valid"], row["vendor"]
        , row["model"], row["onuid"], row["hwver"], row["swver"], row["frmverstr"], row["chip_vendorid"], row["chip_model"], row["chip_revision"],
        row["chip_date"], row["service"], row["num_ge"], row["bmp_gestr"], row["num_fe"], row["bmp_festr"], row["num_us_queue"],
        row["max_queue_usport"], row["num_ds_queue"], row["max_queue_dsport"], row["battery_backup"], row["cap2_valid"], row["onu_type"],
        row["multillid"], row["protetion_type"], row["num_pon"], row["num_slot"], row["num_if_type"], row["intfstr"], row["cap2_battery_backup"],
        msg, oper, result
        = string.find(str, string.rep("(.-)&", 41) .. "(.*)")
        if (result == "0") then
            row["status"] = onu_status_trans(row["status"])
            row["name"] = row["ifname"] .. ":" .. row["llid"]
            if row["status"] ~= "Ready" and row["oamver"] == "0" then
                row["oamver"] = ""
            else
                row["oamver"] = "0x" .. string.format("%X", tonumber(row["oamver"]))
            end
            if row["status"] ~= "Ready" and row["distance"] == "0" then
                row["distance"] = ""
            end
            if row["status"] ~= "Ready" and row["timestamp"] == "0" then
                row["timestamp"] = ""
            else
                row["timestamp"] = os.date("%Y-%m-%d %X", tonumber(row["timestamp"]))
            end
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setonu(row)
    str = row["ifx"] .. "&" .. row["llid"] .. "&" .. row["mac"] .. "&" .. string.rep("&", 37) .. (row["oper"] or "")
    result = librpc.callapi("oltmib_onuinfo_set_1", str)
end

function deregonu(row)
    str = row["ifx"] .. "&" .. row["llid"] .. "&" .. row["mac"] .. "&" .. string.rep("&", 37) .. (row["oper"] or "")
    result = librpc.callapi("oltmib_onu_dereg_1", str)
end

function getonutpl(row)
    str = librpc.callapi("oltmib_onutpl2_get_1", row["name"])
    _, _, row["name"], row["config"], msg, oper, result = string.find(str, string.rep("(.-)&", 4) .. "(.*)")
    if (result == "0") then
    end
    return row
end
function getonutpltbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_onutpl2_getn_1", str)
        _, _, row["name"], row["config"], msg, oper, result = string.find(str, string.rep("(.-)&", 4) .. "(.*)")
        if (result == "0") then
            row["config"] = string.gsub(row["config"], ";", "\n")
            row["config"] = string.gsub(row["config"], "|", " ")
            row["config"] = string.gsub(row["config"], ">", "->")
            row["config"] = string.gsub(row["config"], "dba:(%d+) (%d+) (%d+)", "dba pir %1 cir %2 fir %3")
            row["config"] = string.gsub(row["config"], "sla:(%d+)", "sla downstream pir %1")
            row["config"] = string.gsub(row["config"], "port:(%d+) tag (%d+)", "port %1 vlan mode tag %2")
            row["config"] = string.gsub(row["config"], "port:(%d+) pool (%d+) (%d+) (%w+)", "port %1 vlan mode tag base %2 step %3 description %4")
            row["config"] = string.gsub(row["config"], "port:(%d+) pool (%d+) (%d+)", "port %1 vlan mode tag base %2 step %3")
            row["config"] = string.gsub(row["config"], "port:(%d+) trunk (%d+) ([%d%-, ]+)", "port %1 vlan mode trunk allowed %3 default %2")
            row["config"] = string.gsub(row["config"], "port:(%d+) trans (%d+) ([%d%-, ]+)", "port %1 vlan mode translation default %2 entry %3")
            row["config"] = string.gsub(row["config"], "port:(%d+) agg (%d+) ([%d%-, ]+)", "port %1 vlan mode aggregation default %2 entry %3")
            row["config"] = string.gsub(row["config"], "bu(%s)", "broadband-universal-service location enable%1")
            row["config"] = string.gsub(row["config"], "(%l+)%-(%l+):([%d%-]+) ([%d%-]+)", "alarm %1-%2 threshold %3 %4")
            row["config"] = string.gsub(row["config"], "loopback%-detection:(%d+)", "alarm loopback-detection port %1")
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setonutpl(row)
    str = row["name"] .. "&" .. row["config"] .. "&&" .. (row["oper"] or "")
    result = librpc.callapi("oltmib_onutpl2_set_1", str)
end

function getonutplapply(row)
    str = librpc.callapi("oltmib_onutpl2apply_get_1", row["ifx"])
    _, _, row["ifx"], row["ifname"], row["config"], msg, oper, result = string.find(str, string.rep("(.-)&", 5) .. "(.*)")
    if (result == "0") then
    end
    return row
end
function getonutplapplytbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_onutpl2apply_getn_1", str)
        _, _, row["ifx"], row["ifname"], row["config"], msg, oper, result = string.find(str, string.rep("(.-)&", 5) .. "(.*)")
        if (result == "0") then
            row["config"] = string.gsub(row["config"], ";", "\n")
            row["config"] = string.gsub(row["config"], "|", " ")
            row["config"] = string.gsub(row["config"], "llid:(%w+) ([^%s]+)", "onu-template %1 apply-llid %2")
            row["config"] = string.gsub(row["config"], "model:(%w+) (%w+) (%w+)", "onu-template %1 apply-model vendor-id %2 model-id %3")
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setonutplapply(row)
    str = row["ifx"] .. "&" .. (row["ifname"] or "") .. "&" .. row["config"] .. "&&" .. (row["oper"] or "")
    result = librpc.callapi("oltmib_onutpl2apply_set_1", str)
end

function getonuopticalinfo(row)
    str = librpc.callapi("oltmib_onuopticalinfo_get_1", row["ifx"] .. "&" .. row["llid"])
    _, _, row["ifx"], row["llid"], row["temp"], row["volt"], row["tx_bias"], row["tx_power"], row["rx_power"], result
    = string.find(str, string.rep("(.-)&", 7) .. "(.*)")
    if (result == "0") then
        row["temp"] = tostring(tonumber(row["temp"]) / 1000)
        row["volt"] = tostring(tonumber(row["volt"]) / 1000)
        row["tx_bias"] = tostring(tonumber(row["tx_bias"]) / 1000)
        row["tx_power"] = tostring(tonumber(row["tx_power"]) / 1000)
        row["rx_power"] = tostring(tonumber(row["rx_power"]) / 1000)
    end
    return row
end

function getonucfg(row)
    str = librpc.callapi("oltmib_onucfg2_get_1", row["ifx"] .. "&" .. row["llid"])
    _, _, row["ifx"], row["llid"], row["ifname"], row["mac"], row["status"], row["config"], msg, oper, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
    if (result == "0") then
        row["name"] = row["ifname"] .. ":" .. row["llid"]
        row["status"] = onu_status_trans(row["status"])
    end
    return row
end
function getonucfgtbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_onucfg2_getn_1", str)
        _, _, row["ifx"], row["llid"], row["ifname"], row["mac"], row["status"], row["config"], msg, oper, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            row["name"] = row["ifname"] .. ":" .. row["llid"]
            row["status"] = onu_status_trans(row["status"])
            row["config"] = string.gsub(row["config"], ";", "\n")
            row["config"] = string.gsub(row["config"], "|", " ")
            row["config"] = string.gsub(row["config"], ">", "->")
            row["config"] = string.gsub(row["config"], "desc:(%w+)", "description %1")
            row["config"] = string.gsub(row["config"], "dba:(%d+) (%d+) (%d+)", "dba pir %1 cir %2 fir %3")
            row["config"] = string.gsub(row["config"], "sla:(%d+)", "sla downstream pir %1")
            row["config"] = string.gsub(row["config"], "cos:(%d+)", "mls qos cos %1")
            row["config"] = string.gsub(row["config"], "port:(%d+) tag (%d+)", "port %1 vlan mode tag %2")
            row["config"] = string.gsub(row["config"], "port:(%d+) pool (%d+) (%d+) (%w+)", "port %1 vlan mode tag base %2 step %3 description %4")
            row["config"] = string.gsub(row["config"], "port:(%d+) pool (%d+) (%d+)", "port %1 vlan mode tag base %2 step %3")
            row["config"] = string.gsub(row["config"], "port:(%d+) trunk (%d+) ([%d%-, ]+)", "port %1 vlan mode trunk allowed %3 default %2")
            row["config"] = string.gsub(row["config"], "port:(%d+) trans (%d+) ([%d%-, ]+)", "port %1 vlan mode translation default %2 entry %3")
            row["config"] = string.gsub(row["config"], "port:(%d+) agg (%d+) ([%d%-, ]+)", "port %1 vlan mode aggregation default %2 entry %3")
            row["config"] = string.gsub(row["config"], "bu(%s)", "broadband-universal-service location enable%1")
            row["config"] = string.gsub(row["config"], "(%l+)%-(%l+):([%d%-]+) ([%d%-]+)", "alarm %1-%2 threshold %3 %4")
            row["config"] = string.gsub(row["config"], "loopback%-detection:(%d+)", "alarm loopback-detection port %1")
            row["config"] = string.gsub(row["config"], "port:(%d+) loop", "port %1 loopback-detection")
            row["config"] = string.gsub(row["config"], "port:(%d+) shut", "port %1 shutdown")
            row["config"] = string.gsub(row["config"], "port:(%d+) fc", "port %1 flowcontrol")
            row["config"] = string.gsub(row["config"], "port:(%d+) us_rate (%d+) (%d+) (%d+)", "port %1 rate-limit upstream cir %2 cbs %3 ebs %4")
            row["config"] = string.gsub(row["config"], "port:(%d+) ds_rate (%d+) (%d+)", "port %1 rate-limit downstream pir %2 cir %3")
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setonucfg(row)
    str = row["ifx"] .. "&" .. row["llid"] .. "&" .. (row["ifname"] or "") .. "&" .. mac_trans(row["mac"] or "") .. "&" .. (row["status"] or "") .. "&" .. row["config"] .. "&&" .. (row["oper"] or "")
    result = librpc.callapi("oltmib_onucfg2_set_1", str)
end

function onu_upgstatus_trans(val)
    local trans = {}
    trans["0"] = "Prepare"
    trans["1"] = "Downloading"
    trans["2"] = "Checking"
    trans["3"] = "Activating"
    trans["4"] = "Wait-for-restarting"
    trans["5"] = "Wait-for-committing"
    trans["6"] = "Commiting"
    trans["7"] = "Complete"
    trans["8"] = "Prepare-timeout"
    trans["9"] = "Download-timeout"
    trans["10"] = "Check-timeout"
    trans["11"] = "Activate-timeout"
    trans["12"] = "Commit-timeout"
    trans["13"] = "Prepare-error"
    trans["14"] = "Download-error"
    trans["15"] = "Check-error"
    trans["16"] = "Activate-error"
    trans["17"] = "Commit-error"
    trans["18"] = "Unknown-error"
    return trans[val] or "-"
end
function getonuupgtbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_onuupg2_getn_1", str)
        _, _, row["ifx"], row["llid"], row["ifname"], row["mac"], row["vendor"], row["model"], row["hwver"], row["swver"],
        row["frmverstr"], row["chip_vendoridstr"], row["chip_modelstr"], row["chip_revision"], row["chip_datestr"],
        row["status"], row["upg_status"], row["snmp_status"], row["img"], msg, oper, result = string.find(str, string.rep("(.-)&", 19) .. "(.*)")
        if (result == "0") then
            row["name"] = row["ifname"] .. ":" .. row["llid"]
            row["frmverstr"] = "0x" .. row["frmverstr"]
            row["chip_vendoridstr"] = "0x" .. row["chip_vendoridstr"]
            row["chip_modelstr"] = "0x" .. row["chip_modelstr"]
            row["chip_revision"] = "0x" .. string.format("%X", tonumber(row["chip_revision"]))
            row["chip_datestr"] = "0x" .. row["chip_datestr"]
            row["status"] = onu_status_trans(row["status"])
            row["upg_status"] = onu_upgstatus_trans(row["upg_status"])
            if row["status"] == "Ready" then
                table.insert(tbl, row)
            end
        end
    end
    return tbl
end

function setonuupg(row)
    str = row["ifx"] .. "&" .. row["llid"] .. string.rep("&", 17) .. (row["oper"] or "")
    result = librpc.callapi("oltmib_onuupg2_set_1", str)
end

function getonuupgstatustbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_onuupg2status_getn_1", str)
        _, _, row["ifx"], row["llid"], row["ifname"], row["mac"], row["vendor"], row["model"], row["hwver"], row["swver"],
        row["frmverstr"], row["chip_vendoridstr"], row["chip_modelstr"], row["chip_revision"], row["chip_datestr"],
        row["status"], row["upg_status"], row["snmp_status"], row["img"], msg, oper, result = string.find(str, string.rep("(.-)&", 19) .. "(.*)")
        if (result == "0") then
            row["name"] = row["ifname"] .. ":" .. row["llid"]
            row["frmverstr"] = "0x" .. row["frmverstr"]
            row["chip_vendoridstr"] = "0x" .. row["chip_vendoridstr"]
            row["chip_modelstr"] = "0x" .. row["chip_modelstr"]
            row["chip_revision"] = "0x" .. string.format("%X", tonumber(row["chip_revision"]))
            row["chip_datestr"] = "0x" .. row["chip_datestr"]
            row["status"] = onu_status_trans(row["status"])
            row["upg_status"] = onu_upgstatus_trans(row["upg_status"])
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setonuupgstatus(row)
    str = row["ifx"] .. "&" .. row["llid"] .. string.rep("&", 17) .. (row["oper"] or "")
    result = librpc.callapi("oltmib_onuupg2status_set_1", str)
end

function getonublktbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_onublktbl_getn_1", str)
        _, _, row["ifx"], row["mac"], row["ifname"], msg, oper, result = string.find(str, string.rep("(.-)&", 5) .. "(.*)")
        if (result == "0") then
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setonublk(row)
    str = row["ifx"] .. "&" .. mac_trans(row["mac"]) .. string.rep("&", 3) .. (row["oper"] or "")
    result = librpc.callapi("oltmib_onublktbl_set_1", str)
end

function getponopticalinfotbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_ponoptical_getn_1", str)
        _, _, row["ifx"], row["ifname"], row["state"], row["config"], msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
        if (result == "0") then
            row["state"] = linkstate_trans(row["state"])
            string.gsub(row["config"], "temp:([%d%.%-]+);", function(s) row["temp"] = s end)
            string.gsub(row["config"], "vol:([%d%.%-]+);", function(s) row["vol"] = s end)
            string.gsub(row["config"], "tx_bias:([%d%.%-]+);", function(s) row["tx_bias"] = s end)
            string.gsub(row["config"], "tx_pwr:([%d%.%-]+);", function(s) row["tx_pwr"] = s end)
            table.insert(tbl, row)
        end
    end
    return tbl
end

function getponopticalinfo_onu(row)
    str = librpc.callapi("oltmib_pononuoptical_get_1", row["ifx"])
    _, _, row["ifx"], row["ifname"], row["state"], row["config"], msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
    row["onu"] = {}
    if (result == "0") then
        string.gsub(row["config"], "rx_pwr:(%d+)%|([%d%.%-]+);", function(s1, s2) table.insert(row["onu"], { llid = s1, rx_pwr = s2 }) end)
    end
    if result == "5" then
        table.insert(row["onu"], { msg = "gathering information, please wait..." })
    end
    return row
end

function getuniportstate(row)
    str = librpc.callapi("oltmib_onuportstate_get_1", row["ifx"] .. "&" .. row["llid"] .. "&" .. row["uni"])
    _, _, row["ifx"], row["llid"], row["uni"], row["linkup"], result = string.find(str, string.rep("(.-)&", 4) .. "(.*)")
    if (result == "0") then
        row["linkup"] = linkstate_trans(row["linkup"])
    end
    return row
end


function getdevcapbool(feature, name)
    str = librpc.callapi("oltmib_devcapbool_get_1", feature .. "&" .. name)
    _, _, feature, name, val, valstr, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
    return tonumber(val)
end
function getdevcapint(feature, name)
    str = librpc.callapi("oltmib_devcapint_get_1", feature .. "&" .. name)
    _, _, feature, name, val, valstr, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
    return tonumber(val)
end
function getdevcapstr(feature, name)
    str = librpc.callapi("oltmib_devcapstr_get_1", feature .. "&" .. name)
    _, _, feature, name, val, valstr, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
    return valstr
end

function getdevplatform()
    local platform = getdevcapstr("PROD_ARCH_TYPE", "")
    if platform == "mac5" then
        return "AC5"
    elseif platform == "mpc3" or platform == "mac3-lite" then
        return "LITE"
    elseif platform == "mips_seal" then
        return "X1021"
    else
        return "LITE"
    end
end

function getlibconfbool(file, entry, defval)
    str = librpc.callapi("oltmib_libconfbool_get_1", file .. "&" .. entry)
    _, _, file, entry, val, valstr, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
    return result == "0" and tonumber(val) or defval
end
function getlibconfint(file, entry, defval)
    str = librpc.callapi("oltmib_libconfint_get_1", file .. "&" .. entry)
    _, _, file, entry, val, valstr, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
    return result == "0" and tonumber(val) or defval
end
function getlibconfstr(file, entry, defval)
    str = librpc.callapi("oltmib_libconfstr_get_1", file .. "&" .. entry)
    _, _, file, entry, val, valstr, msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
    return result == "0" and valstr or defval
end

function getonumgmt(row)
    str = librpc.callapi("oltmib_onumgmt_get_1", row["ifx"] .. "&" .. row["llid"])
    _, _, row["ifx"], row["llid"], row["ifname"], row["ip"], row["mask"], row["gateway"], row["cvid"], row["svid"], row["priority"], msg, oper, result
    = string.find(str, string.rep("(.-)&", 11) .. "(.*)")
    if result == "0" then
        row["ip"] = ip2str(row["ip"])
        row["mask"] = ip2str(row["mask"])
        row["gateway"] = ip2str(row["gateway"])
    end
    return row
end

function getsvitbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_svi_getn_1", str)
        _, _, row["vid"], row["name"], row["prefix"], msg, oper, result = string.find(str, string.rep("(.-)&", 5) .. "(.*)")
        if (result == "0") then
            local s = string.split(row["prefix"], "/")
            if #s == 2 then
                row["ip"] = s[1]
                row["mask"] = s[2]
            else
                row["ip"] = ""
                row["mask"] = ""
            end
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setsvi(row)
    str = row["vid"] .. "&" .. row["name"] .. "&" .. row["prefix"] .. string.rep("&", 2) .. (row["oper"] or "")
    result = librpc.callapi("oltmib_svi_set_1", str)
end

function arp_type_trans(val)
    local trans = {}
    trans["1"] = "Dynamic"
    trans["2"] = "Static"
    return trans[val] or val
end
function getarptbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_arp_getn_1", str)
        _, _, row["ip"], row["mac"], row["ifname"], row["type"], msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
        if (result == "0") then
            row["type"] = arp_type_trans(row["type"])
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setarp(row)
    str = string.rep("&", 5) .. (row["oper"] or "")
    result = librpc.callapi("oltmib_arp_set_1", str)
    return result == "0"
end

function getsarptbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_sarp_getn_1", str)
        _, _, row["ip"], row["mac"], row["ifname"], row["type"], msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
        if (result == "0") then
            row["type"] = arp_type_trans(row["type"])
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setsarp(row)
    str = row["ip"] .. "&" .. row["mac"] .. "&" .. (row["ifname"] or "") .. string.rep("&", 3) .. (row["oper"] or "")
    result = librpc.callapi("oltmib_sarp_set_1", str)
    return result == "0"
end

function getroutetbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_route_getn_1", str)
        _, _, row["prefix"], row["nextip"], row["nextif"], row["distance"], row["tag"], row["desc"], msg, oper, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setroute(row)
    str = row["prefix"] .. "&" .. row["nextip"] .. "&" .. (row["nextif"] or "") .. "&" .. (row["distance"] or "1") .. "&" .. (row["tag"] or "") .. "&" .. (row["desc"] or "") .. "&&" .. (row["oper"] or "")
    result = librpc.callapi("oltmib_route_set_1", str)
    return result == "0"
end

function getdyinggaspcap()
    str = librpc.callapi("oltmib_dyinggasp_support_1", "")
    _, _, _, status, msg, oper, result = string.find(str, string.rep("(.-)&", 4) .. "(.*)")
    return result == "0" and tonumber(status) or 0
end
function getdyinggasp()
    local row = {}
    str = librpc.callapi("oltmib_dyinggasp_get_1", "")
    _, _, row["type"], row["status"], msg, oper, result = string.find(str, string.rep("(.-)&", 4) .. "(.*)")
    if (result == "0") then
        return row
    end
    return {}
end
function setdyinggasp(row)
    str = row["type"] .. "&" .. row["status"] .. "&&" .. (row["oper"] or "")
    result = librpc.callapi("oltmib_dyinggasp_set_1", str)
end

function optical_statetrans(val)
    local trans = {}
    trans["0"] = "(OK)"
    trans["1"] = "(WARN)"
    trans["2"] = "(ALARM)"
    trans["3"] = "(ALARM)"
    return trans[val] or "(" .. val .. ")"
end
function optical_tsstatetrans(val)
    local trans = {}
    trans["0"] = "OK"
    trans["1"] = "Open channel fail"
    trans["2"] = "Read eeprom fail"
    trans["3"] = "Transceiver type error"
    trans["4"] = "Transceiver absent"
    trans["5"] = "Transceiver unsupport"
    trans["6"] = "Transceiver timeout"
    return trans[val] or val
end
function getopticalinfotbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        retrycnt = 100
        local row = {}
        str = librpc.callapi("oltmib_optical_getn_1", str)
        _, _, row["ifx"], row["ifname"], row["state"], row["ts_state"], row["temp"], row["temp_state"], row["volt"], row["volt_state"], row["bias"], row["bias_state"],
        row["rx_power"], row["rxp_state"], row["tx_power"], row["txp_state"], msg, oper, result = string.find(str, string.rep("(.-)&", 16) .. "(.*)")
        while (result == "5" and retrycnt > 0) do -- not ready
            os.execute("sleep 0.01")
            retrycnt = retrycnt - 1
            str = librpc.callapi("oltmib_optical_get_1", str)
            _, _, row["ifx"], row["ifname"], row["state"], row["ts_state"], row["temp"], row["temp_state"], row["volt"], row["volt_state"], row["bias"], row["bias_state"],
            row["rx_power"], row["rxp_state"], row["tx_power"], row["txp_state"], msg, oper, result = string.find(str, string.rep("(.-)&", 16) .. "(.*)")
        end
        if (result == "0" and row["ts_state"] ~= "5") then
            row["state"] = port_statetrans(row["state"])
            row["ts_state"] = optical_tsstatetrans(row["ts_state"])
            row["temp_state"] = optical_statetrans(row["temp_state"])
            row["volt_state"] = optical_statetrans(row["volt_state"])
            row["bias_state"] = optical_statetrans(row["bias_state"])
            row["rxp_state"] = optical_statetrans(row["rxp_state"])
            row["txp_state"] = optical_statetrans(row["txp_state"])
            table.insert(tbl, row)
        end
    end
    return tbl
end

function getopticalinfo_port(data)
    retrycnt = 50
    local row = {}
    str = librpc.callapi("oltmib_opticaldetail_get_1", data["ifx"])
    _, _, row["ifx"], row["ifname"], row["state"], row["sfp_base_type"], row["trans_type"], row["connect_type"], row["wavelength"], row["len_smf"], row["len_smf_100m"],
    row["len_50_125_om3"], row["len_50_125_om2"], row["len_625_125_om1"], row["len_copper"], row["ddm_support"], row["vendor_sn"], row["id_no_exist"], row["alarmstr"],
    row["vendor_name"], row["vendor_oui"], row["vendor_pn"], row["vendor_rev"], row["manufact_date"], row["encoding"], msg, oper, result = string.find(str, string.rep("(.-)&", 25) .. "(.*)")
    while (result == "5" and retrycnt > 0) do -- not ready
        os.execute("sleep 0.1")
        retrycnt = retrycnt - 1
        str = librpc.callapi("oltmib_opticaldetail_get_1", str)
        _, _, row["ifx"], row["ifname"], row["state"], row["sfp_base_type"], row["trans_type"], row["connect_type"], row["wavelength"], row["len_smf"], row["len_smf_100m"],
        row["len_50_125_om3"], row["len_50_125_om2"], row["len_625_125_om1"], row["len_copper"], row["ddm_support"], row["vendor_sn"], row["id_no_exist"], row["alarmstr"],
        row["vendor_name"], row["vendor_oui"], row["vendor_pn"], row["vendor_rev"], row["manufact_date"], row["encoding"], msg, oper, result = string.find(str, string.rep("(.-)&", 25) .. "(.*)")
    end
    if (result == "0") then
        row["state"] = port_statetrans(row["state"])
        return row
    end
    return {}
end

function vrrp_ssenablestr(val)
    return { "Disable", "Enable" }
end
function vrrp_ssenabletrans(val)
    local trans = {}
    trans["0"] = "Disable"
    trans["1"] = "Enable"
    trans["Disable"] = "0"
    trans["Enable"] = "1"
    return trans[val] or val
end
function vrrp_ssownerstr(val)
    return { "Backup", "Master" }
end
function vrrp_ssownertrans(val)
    local trans = {}
    trans["0"] = "Backup"
    trans["1"] = "Master"
    trans["Backup"] = "0"
    trans["Master"] = "1"
    return trans[val] or val
end
function getvrrpssconftbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_vrrp_ssconf_getn_1", str)
        _, _, row["vrid"], row["ifname"], row["ip"], row["owner"], row["conf_prio"], row["adv_int"], row["preempt"], row["monitor_if"], row["delta_prio"], row["enable"], msg, oper, result = string.find(str, string.rep("(.-)&", 12) .. "(.*)")
        if (result == "0") then
            row["owner"] = vrrp_ssownertrans(row["owner"])
            if row["conf_prio"] == "-1" then
                row["conf_prio"] = ""
            end
            row["preempt"] = bool_trans(row["preempt"])
            if row["monitor_if"] == "" then
                row["delta_prio"] = ""
            end
            row["enable"] = vrrp_ssenabletrans(row["enable"])
            table.insert(tbl, row)
        end
    end
    return tbl
end

function getvrrpssconf(data)
    local row = {}
    str = librpc.callapi("oltmib_vrrp_ssconf_get_1", data["vrid"])
    _, _, row["vrid"], row["ifname"], row["ip"], row["owner"], row["conf_prio"], row["adv_int"], row["preempt"], row["monitor_if"], row["delta_prio"], row["enable"], msg, oper, result = string.find(str, string.rep("(.-)&", 12) .. "(.*)")
    row["owner"] = vrrp_ssownertrans(row["owner"])
    if row["conf_prio"] == "-1" then
        row["conf_prio"] = ""
    end
    row["preempt"] = bool_trans(row["preempt"])
    if row["monitor_if"] == "" then
        row["delta_prio"] = ""
    end
    row["enable"] = vrrp_ssenabletrans(row["enable"])
    return row
end

function setvrrpssconf(row)
    row["owner"] = vrrp_ssownertrans(row["owner"])
    if row["conf_prio"] == "" then
        row["conf_prio"] = "-1"
    end
    row["preempt"] = bool_trans(row["preempt"])
    str = row["vrid"] .. "&" .. row["ifname"] .. "&" .. row["ip"] .. "&" .. row["owner"] .. "&" .. row["conf_prio"] .. "&" .. row["adv_int"] .. "&" .. row["preempt"]
    .. "&" .. (row["monitor_if"] or "") .. "&" .. (row["delta_prio"] or "") .. "&" .. row["enable"] .. "&&" .. (row["oper"] or "")
    result = librpc.callapi("oltmib_vrrp_ssconf_set_1", str)
end

function vrrp_ssstatustrans(val)
    local trans = {}
    trans["-1"] = "-"
    trans["0"] = "Down"
    trans["1"] = "Up"
    return trans[val] or val
end
function vrrp_ssroletrans(val)
    local trans = {}
    trans["1"] = "Initialize"
    trans["2"] = "Backup"
    trans["3"] = "Master"
    return trans[val] or val
end
function getvrrpssstatetbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_vrrp_ssstate_getn_1", str)
        _, _, row["vrid"], row["admin_state"], row["shutdown_flag"], row["role"], row["monitor_status"], row["prio"], msg, oper, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            row["admin_state"] = vrrp_ssenabletrans(row["admin_state"])
            row["shutdown_flag"] = bool_trans(row["shutdown_flag"])
            row["role"] = vrrp_ssroletrans(row["role"])
            row["monitor_status"] = vrrp_ssstatustrans(row["monitor_status"])
            table.insert(tbl, row)
        end
    end
    return tbl
end

function getlldpcfg()
    local data = {}
    str = librpc.callapi("oltmib_lldpcfg_get_1", "")
    _, _, data["status"], data["sysname"], data["sysdesc"], data["chassis"], msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
    if (result == "0") then
        data["status"] = ablity_trans(data["status"])
        return data
    end
    return {}
end

function setlldpcfg(data)
    result = librpc.callapi("oltmib_lldpcfg_set_1", ablity_trans(data["status"]) .. "&" .. data["sysname"] .. "&" .. data["sysdesc"] .. "&" .. ((data["chassis"]) or ""))
    return result == "0"
end

function lldp_statusstr()
    return { "Disable", "RxOnly", "TxOnly", "TxRx" }
end

function lldp_statustrans(data)
    local trans = {}
    trans["0"] = "Disable"
    trans["1"] = "Disable"
    trans["2"] = "RxOnly"
    trans["4"] = "TxOnly"
    trans["8"] = "TxRx"
    trans["Disable"] = "1"
    trans["RxOnly"] = "2"
    trans["TxOnly"] = "4"
    trans["TxRx"] = "8"
    return trans[data] or data
end

function lldp_chassisstr()
    return { "mac-address", "if-alias", "if-name", "ip-address", "locally-assigned" }
end

function lldp_chassistrans(data)
    local trans = {}
    trans["1"] = "default"
    trans["2"] = "if-alias"
    trans["4"] = "mac-address" -- default
    trans["6"] = "if-name"
    trans["5"] = "ip-address"
    trans["7"] = "locally-assigned"
    trans["default"] = "1"
    trans["if-alias"] = "2"
    trans["mac-address"] = "4"
    trans["if-name"] = "6"
    trans["ip-address"] = "5"
    trans["locally-assigned"] = "7"
    return trans[data] or data
end

function lldp_portidstr()
    return { "mac-address", "if-alias", "ip-address", "if-name", "agt-circuit-id", "locally-assigned" }
end

function lldp_portidtrans(data)
    local trans = {}
    trans["0"] = "default"
    trans["1"] = "if-alias"
    trans["3"] = "mac-address" -- default
    trans["4"] = "ip-address"
    trans["5"] = "if-name"
    trans["6"] = "agt-circuit-id"
    trans["7"] = "locally-assigned"
    trans["default"] = "0"
    trans["if-alias"] = "1"
    trans["mac-address"] = "3"
    trans["ip-address"] = "4"
    trans["if-name"] = "5"
    trans["agt-circuit-id"] = "6"
    trans["locally-assigned"] = "7"
    return trans[data] or data
end

function lldp_mgmtaddrstr()
    return { "mac-address", "ip-address" }
end

function lldp_mgmtaddrtrans(data)
    local trans = {}
    trans["6"] = "mac-address"
    trans["1"] = "ip-address"
    trans["mac-address"] = "6"
    trans["ip-address"] = "1"
    return trans[data] or data
end

function lldp_basictlvarr()
    local arr = {}
    arr["1"] = "port-description"
    arr["2"] = "system-name"
    arr["4"] = "system-capabilities"
    arr["8"] = "system-description"
    arr["16"] = "management-address"
    return arr
end
function lldp_8021tlvarr()
    local arr = {}
    arr["1"] = "port-vlanid"
    arr["2"] = "vlan-name"
    arr["4"] = "port-ptcl-vlanid"
    arr["8"] = "ptcl-identity"
    arr["16"] = "vid-digest"
    arr["32"] = "mgmt-vid"
    arr["64"] = "link-agg"
    -- arr["2048"] = "data-center-bridging"
    return arr
end
function lldp_8023tlvarr()
    local arr = {}
    arr["128"] = "mac-phy"
    -- arr["256"] = "power-via-mdi"
    arr["1024"] = "max-mtu-size"
    return arr
end

--[[
function lldp_tlvstr2int(data, arr)
    local num = 0;
    local tlvs = string.split(data, ",")
    for i = 1, #tlvs do
        for k, v in pairs(arr) do
            if (tlvs[i] == v) then
                num = bit.bor(num, tonumber(k))
            end
        end
    end
    return num
end
function lldp_tlvint2str(data, arr)
    local str = ""
    local num = tonumber(data)
    for k, v in pairs(arr) do
        if bit.band(num, tonumber(k)) ~= 0 then
            str = str .. v .. ","
        end
    end
    return str
end
]]--
function lldp_tlvarray2int(data, arr)
    local num = 0;
    local tlvs = data or {}
    for _, v in ipairs(tlvs) do
        for k, opt in pairs(arr) do
            if v == opt then
                num = bit.bor(num, tonumber(k))
            end
        end
    end
    return num
end
function lldp_tlvint2array(data, arr)
    local tbl = {}
    local num = tonumber(data)
    for k, v in pairs(arr) do
        if bit.band(num, tonumber(k)) ~= 0 then
            table.insert(tbl, v)
        end
    end
    return tbl
end

function getlldpifcfgtbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_lldpifcfg_getn_1", str)
        _, _, row["ifx"], row["ifname"], row["desc"], row["agid"], row["assigned"], row["admin_status"],
        row["chassis_subtype"], row["portid_subtype"], row["mgmtaddr_subtype"], row["basic_tlvs"], row["optional_tlvs"], row["msg_tx_hold"], row["msg_tx_interval"],
        row["reinit_delay"], row["msg_fast_tx"], row["tx_fast_init"], row["tx_credit_max"], msg, oper, result = string.find(str, string.rep("(.-)&", 19) .. "(.*)")
        if (result == "0") then
            row["admin_status"] = lldp_statustrans(row["admin_status"])
            -- row["chassis_subtype"] = lldp_chassistrans(row["chassis_subtype"])
            -- row["portid_subtype"] = lldp_portidtrans(row["portid_subtype"])
            -- row["mgmtaddr_subtype"] = lldp_mgmtaddrtrans(row["mgmtaddr_subtype"])
            --row["basic_tlvs"] = lldp_tlvint2str(row["basic_tlvs"], lldp_basictlvarr())
            -- row["basic_tlvs"] = string.gsub(row["basic_tlvs"], ",$", "")
            -- local str_8021 = lldp_tlvint2str(row["optional_tlvs"], lldp_8021tlvarr())
            -- row["optional_tlvs"] = str_8021 .. lldp_tlvint2str(row["optional_tlvs"], lldp_8023tlvarr())
            -- row["optional_tlvs"] = string.gsub(row["optional_tlvs"], ",$", "")

            row["chassis_subtype"] = lldp_chassistrans(row["chassis_subtype"])
            row["portid_subtype"] = lldp_portidtrans(row["portid_subtype"])
            row["mgmtaddr_subtype"] = lldp_mgmtaddrtrans(row["mgmtaddr_subtype"])
            row["basic_tlvs"] = lldp_tlvint2array(row["basic_tlvs"], lldp_basictlvarr())
            row["dot1_tlvs"] = lldp_tlvint2array(row["optional_tlvs"], lldp_8021tlvarr())
            row["dot3_tlvs"] = lldp_tlvint2array(row["optional_tlvs"], lldp_8023tlvarr())
            table.insert(tbl, row)
        end
    end
    return tbl
end

function getlldpifcfg(row)
    str = librpc.callapi("oltmib_lldpifcfg_get_1", row["ifx"])
    _, _, row["ifx"], row["ifname"], row["desc"], row["agid"], row["assigned"], row["admin_status"],
    row["chassis_subtype"], row["portid_subtype"], row["mgmtaddr_subtype"], row["basic_tlvs"], row["optional_tlvs"], row["msg_tx_hold"], row["msg_tx_interval"],
    row["reinit_delay"], row["msg_fast_tx"], row["tx_fast_init"], row["tx_credit_max"], msg, oper, result = string.find(str, string.rep("(.-)&", 19) .. "(.*)")
    if result == "0" then
        row["admin_status"] = lldp_statustrans(row["admin_status"])
        row["chassis_subtype"] = lldp_chassistrans(row["chassis_subtype"])
        row["portid_subtype"] = lldp_portidtrans(row["portid_subtype"])
        row["mgmtaddr_subtype"] = lldp_mgmtaddrtrans(row["mgmtaddr_subtype"])
        --row["basic_tlvs"] = lldp_tlvint2str(row["basic_tlvs"], lldp_basictlvarr())
        --row["basic_tlvs"] = string.gsub(row["basic_tlvs"], ",$", "")
        --local str_8021 = lldp_tlvint2str(row["optional_tlvs"], lldp_8021tlvarr())
        --row["optional_tlvs"] = str_8021 .. lldp_tlvint2str(row["optional_tlvs"], lldp_8023tlvarr())
        --row["optional_tlvs"] = string.gsub(row["optional_tlvs"], ",$", "")
        row["basic_tlvs"] = lldp_tlvint2array(row["basic_tlvs"], lldp_basictlvarr())
        row["dot1_tlvs"] = lldp_tlvint2array(row["optional_tlvs"], lldp_8021tlvarr())
        row["dot3_tlvs"] = lldp_tlvint2array(row["optional_tlvs"], lldp_8023tlvarr())
        return row
    end
    return {}
end

function setlldpifcfg(data)
    data["admin_status"] = lldp_statustrans(data["admin_status"])
    data["chassis_subtype"] = lldp_chassistrans(data["chassis_subtype"])
    data["portid_subtype"] = lldp_portidtrans(data["portid_subtype"])
    data["mgmtaddr_subtype"] = lldp_mgmtaddrtrans(data["mgmtaddr_subtype"])
    --data["basic_tlvs"] = lldp_tlvstr2int(data["basic_tlvs"], lldp_basictlvarr())
    --local int_8021 = lldp_tlvstr2int(data["optional_tlvs"], lldp_8021tlvarr())
    --local int_8023 = lldp_tlvstr2int(data["optional_tlvs"], lldp_8023tlvarr())
    data["basic_tlvs"] = lldp_tlvarray2int(data["basic_tlvs"], lldp_basictlvarr())
    local int_8021 = lldp_tlvarray2int(data["dot1_tlvs"], lldp_8021tlvarr())
    local int_8023 = lldp_tlvarray2int(data["dot3_tlvs"], lldp_8023tlvarr())
    if data["basic_tlvs"] ~= 0 then
        data["basic_tlvs"] = bit.bor(data["basic_tlvs"], 128)
    end
    if int_8021 ~= 0 then
        data["basic_tlvs"] = bit.bor(data["basic_tlvs"], 32)
    end
    if int_8023 ~= 0 then
        data["basic_tlvs"] = bit.bor(data["basic_tlvs"], 64)
    end
    data["optional_tlvs"] = bit.bor(int_8021, int_8023)
    result = librpc.callapi("oltmib_lldpifcfg_set_1", data["ifx"] .. "&" .. (data["ifname"] or "") .. "&" .. data["desc"] .. "&" .. data["agid"] .. "&" .. data["assigned"] .. "&" .. data["admin_status"] .. "&" ..
    data["chassis_subtype"] .. "&" .. data["portid_subtype"] .. "&" .. data["mgmtaddr_subtype"] .. "&" .. data["basic_tlvs"] .. "&" .. data["optional_tlvs"] .. "&" .. data["msg_tx_hold"] .. "&" .. data["msg_tx_interval"] .. "&" ..
    data["reinit_delay"] .. "&" .. data["msg_fast_tx"] .. "&" .. data["tx_fast_init"] .. "&" .. data["tx_credit_max"])
    return result == '0'
end

function getlldpneitbl()
    local tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_lldpifnei_getn_1", str)
        _, _, row["id"], row["rmac"], row["name"], row["info"], msg, oper, result = string.find(str, string.rep("(.-)&$", 6) .. "(.*)")
        if (result == "0") then
            table.insert(tbl, row)
        end
    end
    return tbl
end

function getlldpifstattbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_lldpifstat_getn_1", str)
        _, _, row["ifx"], row["ifname"], row["tx"], row["aged"], row["rx"], row["rx_err"], row["discards"], row["discard_tlvs"], row["unknown_tlvs"], msg, oper, result = string.find(str, string.rep("(.-)&", 11) .. "(.*)")
        if (result == "0") then
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setlldpifstat(data)
    result = librpc.callapi("oltmib_lldpifstat_set_1", data["ifx"])
    return result == '0'
end

function ps_viomode_str()
    return { "Restrict", "Shutdown" }
end
function ps_viomode_trans(val)
    local data = {}
    data["0"] = "Restrict"
    data["1"] = "Shutdown"
    data["Restrict"] = "0"
    data["Shutdown"] = "1"
    return data[val] or "-"
end

function getnsmpsstatetbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_nsmpsstate_getn_1", str)
        _, _, row["ifx"], row["name"], row["enable"], row["max"], row["total_mac_num"], row["config_mac_num"], row["sticky"], row["aging_time"], row["aging_static"],
        row["violation_mode"], row["violation_count"], row["last_violate_mac"], row["last_violate_stamp"], msg, oper, result = string.find(str, string.rep("(.-)&", 15) .. "(.*)")
        if (result == "0") then
            if row["last_violate_mac"] == "00-00-00-00-00-00" then
                row["last_violate_mac"] = ""
            end
            row["last_violate_stamp"] = trim(row["last_violate_stamp"])
            if row["last_violate_stamp"] == "Thu Jan  1 00:00:00 1970" then
                row["last_violate_stamp"] = ""
            end
            row["enable"] = ablity_trans(row["enable"])
            row["sticky"] = ablity_trans(row["sticky"])
            row["aging_static"] = ablity_trans(row["aging_static"])
            row["violation_mode"] = ps_viomode_trans(row["violation_mode"])
            table.insert(tbl, row)
        end
    end
    return tbl
end

function getnsmps(data)
    local row = {}
    str = librpc.callapi("oltmib_nsmps_get_1", data["ifx"])
    _, _, row["ifx"], row["name"], row["enable"], row["max"], row["sticky"], row["aging_time"], row["aging_static"], row["violation_mode"], msg, oper, result = string.find(str, string.rep("(.-)&", 10) .. "(.*)")
    row["enable"] = ablity_trans(row["enable"])
    row["sticky"] = ablity_trans(row["sticky"])
    row["aging_static"] = ablity_trans(row["aging_static"])
    row["violation_mode"] = ps_viomode_trans(row["violation_mode"])
    return row
end

function setnsmps(data)
    result = librpc.callapi("oltmib_nsmps_set_1", data["ifx"] .. "&" .. data["name"] .. "&" .. ablity_trans(data["enable"]) .. "&" .. data["max"]
    .. "&" .. ablity_trans(data["sticky"]) .. "&" .. data["aging_time"] .. "&" .. ablity_trans(data["aging_static"]) .. "&" .. ps_viomode_trans(data["violation_mode"]) .. "&&" .. (data["oper"] or ""))
    return result == "0"
end

function ps_mactype_str()
    return { "Static", "Sticky" }
end
function ps_mactype_trans(val)
    local data = {}
    data["0"] = "Static"
    data["1"] = "Dynamic"
    data["2"] = "Sticky"
    data["Static"] = "0"
    data["Dynamic"] = "1"
    data["Sticky"] = "2"
    return data[val] or "-"
end

function getnsmpsmacstatetbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_nsmpsmacstate_getn_1", str)
        _, _, row["ifx"], row["name"], row["vid"], row["mac"], row["type"], row["age_time_left"], msg, oper, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            row["type"] = ps_mactype_trans(row["type"])
            --if row["age_time_left"] == "0" then
                --row["age_time_left"] = "-"
            --end
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setnsmpsmac(data)
    result = librpc.callapi("oltmib_nsmpsmac_set_1", data["ifx"] .. "&" .. data["name"] .. "&" .. data["vid"] .. "&" .. data["mac"] .. "&" .. ps_mactype_trans(data["type"]) .. "&&" .. (data["oper"] or ""))
    return result == "0"
end

function ipsg_typetrans(data)
    local tbl = {}
    tbl['1'] = "Static"
    tbl['2'] = "Snooping"
    tbl["Static"] = "1"
    tbl["Snooping"] = "2"
    return tbl[tostring(data)] or ""
end

function getnsmipsgiftbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_nsmipsgif_getn_1", str)
        _, _, row["ifx"], row["name"], row["verify_source_enable"], row["arp_check_enable"], row["static_user_num"], row["total_user_num"], msg, oper, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            row["verify_source_enable"] = ablity_trans(row["verify_source_enable"])
            row["arp_check_enable"] = ablity_trans(row["arp_check_enable"])
            table.insert(tbl, row)
        end
    end
    return tbl
end

function getnsmipsgif(data)
    local row = {}
    str = librpc.callapi("oltmib_nsmipsgif_get_1", data["ifx"])
    _, _, row["ifx"], row["name"], row["verify_source_enable"], row["arp_check_enable"], row["static_user_num"], row["total_user_num"], msg, oper, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
    row["verify_source_enable"] = ablity_trans(row["verify_source_enable"])
    row["arp_check_enable"] = ablity_trans(row["arp_check_enable"])
    return row
end

function setnsmipsgif(data)
    result = librpc.callapi("oltmib_nsmipsgif_set_1", data["ifx"] .. "&" .. data["name"] .. "&" .. ablity_trans(data["verify_source_enable"]) .. "&" .. ablity_trans(data["arp_check_enable"]) .. "&&&&" .. (data["oper"] or ""))
    return result == "0"
end

function getnsmipsgusertbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_nsmipsguser_getn_1", str)
        _, _, row["ifx"], row["name"], row["vid"], row["mac"], row["ipstr"], row["type"], msg, oper, result = string.find(str, string.rep("(.-)&", 8) .. "(.*)")
        if (result == "0") then
            row["lease"] = "Infinite"
            row["type"] = ipsg_typetrans(row["type"])
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setnsmipsguser(data)
    result = librpc.callapi("oltmib_nsmipsguser_set_1", data["ifx"] .. "&" .. data["name"] .. "&" .. data["vid"] .. "&" .. data["mac"] .. "&" .. data["ipstr"] .. "&" .. ipsg_typetrans(data["type"] or "Static") .. "&&" .. (data["oper"] or ""))
    return result == "0"
end

function getmbaserialtbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_mbaserial_getn_1", str)
        _, _, row["id"], row["brate"], row["databits"], row["parity"], row["stopbits"], msg, oper, result = string.find(str, string.rep("(.-)&", 7) .. "(.*)")
        if (result == "0") then
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setmbaserial(data)
    result = librpc.callapi("oltmib_mbaserial_set_1", data["id"] .. "&" .. data["brate"] .. "&" .. data["databits"] .. "&" .. data["parity"] .. "&" .. data["stopbits"] .. "&&" .. (data["oper"] or ""))
    return result == "0"
end

function mba_instmode_str()
    return { "TCP Client", "TCP Server" }
end
function mba_instmode_trans(val)
    local data = {}
    data["1"] = "TCP Client"
    data["2"] = "TCP Server"
    data["TCP Client"] = "1"
    data["TCP Server"] = "2"
    return data[val] or "-"
end

function getmbainsttbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_mbainst_getn_1", str)
        _, _, row["name"], row["mode"], row["sip"], row["sport"], row["dip"], row["dport"], row["keyword"], row["interval"], msg, oper, result = string.find(str, string.rep("(.-)&", 10) .. "(.*)")
        if (result == "0") then
            row["mode"] = mba_instmode_trans(row["mode"])
            if row["sport"] == "0" then
                row["sport"] = ""
            end
            if row["dport"] == "0" then
                row["dport"] = ""
            end
                table.insert(tbl, row)
        end
    end
    return tbl
end

function getmbainst(name)
    if (name == "new") then
        return {name="Default"}
    end
    local row = {}
    str = librpc.callapi("oltmib_mbainst_get_1", name)
    _, _, row["name"], row["mode"], row["sip"], row["sport"], row["dip"], row["dport"], row["keyword"], row["interval"], msg, oper, result = string.find(str, string.rep("(.-)&", 10) .. "(.*)")
    if (result == "0") then
        row["mode"] = mba_instmode_trans(row["mode"])
        if row["sport"] == "0" then
            row["sport"] = ""
        end
        if row["dport"] == "0" then
            row["dport"] = ""
        end
        return row
    end
    return {name="Default"}
end

function setmbainst(data)
    result = librpc.callapi("oltmib_mbainst_set_1", data["name"] .. "&" .. mba_instmode_trans(data["mode"]) .. "&" .. data["sip"] .. "&" .. data["sport"] .. "&" .. data["dip"] .. "&" 
        .. data["dport"] .. "&" .. data["keyword"] .. "&" .. data["interval"] .. "&&" .. (data["oper"] or ""))
    return result == "0"
end

function mba_inststatus_trans(val)
    local data = {}
    data["1"] = "Connected"
    data["2"] = "Disconnected"
    return data[val] or "-"
end
function getmbainststatetbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_mbainststate_getn_1", str)
        _, _, row["name"], row["mode"], row["status"], row["sip"], row["sport"], row["dip"], row["dport"], row["keepalive_cnt"], msg, oper, result = string.find(str, string.rep("(.-)&", 10) .. "(.*)")
        if (result == "0") then
            row["mode"] = mba_instmode_trans(row["mode"])
            row["status"] = mba_inststatus_trans(row["status"])
            if row["sip"] == "0.0.0.0" then
                row["sip"] = ""
            end
            if row["sport"] == "0" then
                row["sport"] = ""
            end
            if row["dip"] == "0.0.0.0" then
                row["dip"] = ""
            end
            if row["dport"] == "0" then
                row["dport"] = ""
            end
            table.insert(tbl, row)
        end
    end
    return tbl
end
function getmbaserialstatistbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_mbaserialstatis_getn_1", str)
        _, _, row["id"], row["err"], row["last_errpkt"], row["last_errcode"], msg, oper, result = string.find(str, string.rep("(.-)&", 6) .. "(.*)")
        if (result == "0") then
            table.insert(tbl, row)
        end
    end
    return tbl
end
function getmbainststatistbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_mbainststatis_getn_1", str)
        _, _, row["name"], row["rx_bytes"], row["rx_pkts"], row["rx_err"], row["rx_last_errpkt"], row["rx_last_errcode"], row["tx_err"], row["tx_drop"], row["connect_cnt"], msg, oper, result = string.find(str, string.rep("(.-)&", 11) .. "(.*)")
        if (result == "0") then
            table.insert(tbl, row)
        end
    end
    return tbl
end

function ioctl_dir_trans(val)
    local data = {}
    data["1"] = "in"
    data["2"] = "out"
    data["input"] = "1"
    data["output"] = "2"
    return data[val] or tostring(val)
end
function ioctl_dir_str(val)
    return {"in", "out"}
end
function ioctl_level_trans(val)
    local data = {}
    data["1"] = "high"
    data["2"] = "low"
    data["high"] = "1"
    data["low"] = "2"
    return data[val] or "-" -- tostring(val)
end
function ioctl_level_str(val)
    return {"high", "low"}
end
function getioctlinfotbl()
    tbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_ioctlinfo_getn_1", str)
        _, _, row["id"], row["dir"], row["level"], row["level_def"], row["desc"], msg, oper, result = string.find(str, string.rep("(.-)&", 7) .. "(.*)")
        if (result == "0") then
            row["dir"] = ioctl_dir_trans(row["dir"])
            row["level"] = ioctl_level_trans(row["level"])
            row["level_def"] = ioctl_level_trans(row["level_def"])
            table.insert(tbl, row)
        end
    end
    return tbl
end

function setioctlinfo(data)
    result = librpc.callapi("oltmib_ioctlinfo_set_1", data["id"] .. "&" .. ioctl_dir_trans(data["dir"]) .. "&" .. ioctl_level_trans(data["level"]) .. "&&" .. data["desc"] .. "&&" .. (data["oper"] or ""))
    return result == "0"
end

--- Vlanlist string trans to table.
---@param vlanstr string
---@return table vlantbl
function vlanstr2tbl(vlanstr)
    local vlanlist = {}
    local vlanlist1 = string.split(datalst_trans(vlanstr), ',')
    for _, s in ipairs(vlanlist1) do
        local vlanlist2 = string.split(s, '-')
        local range = {}
        range[1] = tonumber(vlanlist2[1])
        range[2] = tonumber(vlanlist2[#vlanlist2])
        if next(range) then
            for vid = range[1], range[2], 1 do
                vlanlist[vid] = true 
            end
        end
    end

    local vlantbl = {}
    for k, v in pairs(vlanlist) do
        table.insert(vlantbl, k)
    end

    table.sort(vlantbl)
    return vlantbl
end

--- Vlanlist array trans to string.
---@param vlanarray table
---@return string vlanlist
function vlanarray2str(vlanarray)
    local vlanlist = ''
    local start, over = 4096, 4096
    for k, vid in ipairs(vlanarray) do
        if over + 1 ~= vid then
            vlanlist = vlanlist .. (start == over and start or (start .. '-' .. over)) .. ','
            start = vid
        end
        over = vid

        if k == #vlanarray then
            vlanlist = vlanlist .. (start == over and start or (start .. '-' .. over))
        end
    end

    vlanlist = string.gsub(vlanlist, '^%d+,', '')
    return vlanlist
end

--- Filter uncreated vlans in vlanlist.
---@param vlanlist string
---@return string vlanstr
function filter_vlan(vlanlist)
    local vlanmbr = {}
    local vlanarray = vlanstr2tbl(vlanlist)
    local vlantbl = getvlantable()
    for _, vlan in ipairs(vlantbl) do
        local vlanidx = tonumber(vlan['Index'])
        for _, vid in ipairs(vlanarray) do
            if vlanidx == vid then
                table.insert(vlanmbr, vid)
            end
        end
    end

    local vlanstr = vlanarray2str(vlanmbr)
    return vlanstr
end
