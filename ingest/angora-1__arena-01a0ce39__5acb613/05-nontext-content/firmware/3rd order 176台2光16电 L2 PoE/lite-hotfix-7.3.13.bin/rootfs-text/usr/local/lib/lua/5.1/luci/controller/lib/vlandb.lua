local librpc = require "librpc"
local table = require "table"
local string = require "string"
local os = require "os"
local util = require "luci.util"
local json = require "luci.json"
local nixio = require "nixio"
local fs = require "nixio.fs"
local tostring = tostring
local tonumber = tonumber
local pairs = pairs
local ipairs = ipairs
local next = next
local bit = bit
local math = math
local type = type
local translate = luci.i18n.translate
local io = io
local setmetatable = setmetatable
local getmetatable = getmetatable
local tools = require "luci.controller.lib.tools"
local bit = bit

module("luci.controller.lib.vlandb", package.seeall)

function index()
end

function typeint2str(data)
    data = tonumber(data) or 0
    local type = "Invalid"
    if (bit.band(data, 1) ~= 0) then type = "Static" end
    if (bit.band(data, 2) ~= 0) then type = "Dynamic" end
    return type
end

function typestr2int(data)
    local tbl = {}
    tbl["Static"] = bit.lshift(1, 0) + bit.lshift(1, 2)
    tbl["Dynamic"] = bit.lshift(1, 1) + bit.lshift(1, 2)
    return tbl[tostring(data)] or ""
end

--- Vlanlist string trans to table.
---@param vlanstr string
---@return table vlantbl
function vlanstr2tbl(vlanstr)
    local array = tools.str2array(vlanstr)
    assert(not next(array) or tools.range_hit(array[1], 1, 4094), "illegal vlanstr")
    assert(not next(array) or tools.range_hit(array[#array], 1, 4094), "illegal vlanstr")
    return array
end

--- Vlanlist array trans to string.
---@param vlanarray table
---@return string vlanlist
function vlanarray2str(vlanarray)
    table.sort(vlanarray)
    assert(not next(vlanarray) or tools.range_hit(vlanarray[1], 1, 4094), "illegal vlanlist")
    assert(not next(vlanarray) or tools.range_hit(vlanarray[#vlanarray], 1, 4094), "illegal vlanlist")
    return tools.array2str(vlanarray)
end

--- Untagvlan and tagvlan merged into allowvlan.
---@param untagmbr string
---@param tagmbr string
---@return string allowvlan
function allowvlan_pack(untagmbr, tagmbr)
    local vlanlist = {}
    local taglist1 = string.split(tools.datalst_trans(tagmbr), ',')
    for _, s in ipairs(taglist1) do
        local taglist2 = string.split(s, '-')
        local range = {}
        range[1] = tonumber(taglist2[1])
        range[2] = tonumber(taglist2[#taglist2])
        if next(range) then
            for vid = range[1], range[2], 1 do
                vlanlist[vid] = true 
            end
        end
    end

    local untaglist1 = string.split(tools.datalst_trans(untagmbr), ',')
    for _, s in ipairs(untaglist1) do
        local untaglist2 = string.split(s, '-')
        local range = {}
        range[1] = tonumber(untaglist2[1])
        range[2] = tonumber(untaglist2[#untaglist2])
        if next(range) then
            for vid = range[1], range[2], 1 do
                vlanlist[vid] = true 
            end
        end
    end

    local vlanarray = {}
    for k, v in pairs(vlanlist) do
        table.insert(vlanarray, k)
    end

    table.sort(vlanarray)
    local allowvlan = vlanarray2str(vlanarray)
    return allowvlan
end

--- Decompose allowvlan into untagvlan and tagvlan.
---@param pvid number
---@param vmode string
---@param allowvlan string ：allowvlan supports standard multi-vlan representation methods ("-" and "," and combinations of both);
---@return string untagvlan 
---@return string tagvlan
function allowvlan_parse(pvid, vmode, allowvlan, untaggedvlan)
    local untagvlan = ''
    local tagvlan = ''
    if vmode == 'Trunk' then
        local vlanlist = vlanstr2tbl(allowvlan)

        local mark = false
        for k, vid in ipairs(vlanlist) do
            if pvid == vid then
                untagvlan = tostring(pvid)
                mark = k
            end
        end

        if mark then table.remove(vlanlist, mark) end
        tagvlan = vlanarray2str(vlanlist)
    elseif vmode == 'Hybrid' then
        tagvlan = tools.array_del(vlanstr2tbl(allowvlan), vlanstr2tbl(untaggedvlan or ""))
        tagvlan = tools.array_del(tagvlan, vlanstr2tbl(pvid or ""))
        tagvlan = tools.array2str(tagvlan)
        untagvlan = untaggedvlan or ""
    end

    return untagvlan, tagvlan
end

--[[
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
]]--
