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

module("luci.controller.lib.tools", package.seeall)

function index()
end

function bool_trans(val)
    local trans = {}
    trans["0"] = false
    trans["1"] = true
    trans["false"] = "0"
    trans["true"] = "1"
    return trans[tostring(val)]
end

function array_check(v)
    if type(v) == "table" then
        if not next(v) then
            v[2] = 'nil'
        end
    end
    return v
end

--- Make sure the `val` is in the range `low` and `high`
---@param val any
---@param low number
---@param high number
function range_hit(val, low, high)
    assert(low <= high, "Range boundary value exception")
    if type(val) == "number" and val >= low and val <= high then
        return true
    end

    return false
end

function non_empty(val)
    if tostring(val) ~= "nil" then
        return true
    end
    return false
end

function non_null(val)
    if val and val == luci.json.null then
        return true
    end
    return false
end

--- func desc : val is null return def
---@param val any
---@param def any
function valfilter(val, def)
    local default = def or 0
    if non_null(val) then
        return default
    end
    return val
end

function tMerge(t1, t2)
    for k, v in pairs(t2) do if (v ~= nil and v ~= luci.json.null) then t1[k] = v end end
    return t1
end

function datalst_trans(val)-- replace ' ' by ','  delete extra ','
    local s = val
    s = string.gsub(s, " ", ",")
    s = string.gsub(s, "^,+", "")
    s = string.gsub(s, ",+$", "")
    s = string.gsub(s, ",,+", ",")
    return s
end


--- string trans to table.
--- strings cannot contain negative numbers.
function str2array(str)
    local list = {}
    local list1 = string.split(datalst_trans(str), ',')
    for _, s in ipairs(list1) do
        local list2 = string.split(s, '-')
        local range = {}
        range[1] = tonumber(list2[1])
        range[2] = tonumber(list2[#list2])
        if next(range) then
            for idx = range[1], range[2], 1 do
                list[idx] = true
            end
        end
    end

    local tbl = {}
    for k, v in pairs(list) do
        table.insert(tbl, k)
    end

    table.sort(tbl)
    return tbl
end

--- array trans to string.
--- The values of the array must be arranged from small to large, and cannot contain negative numbers.
function array2str(array)
    local str = ''
    local start, over = array[#array], array[#array]
    for k, v in ipairs(array) do
        if over + 1 ~= v then
            str = str .. (start == over and start or (start .. '-' .. over)) .. ','
            start = v
        end
        over = v

        if k == #array then
            str = str .. (start == over and start or (start .. '-' .. over))
        end
    end

    str = string.gsub(str, '^%d+,', '')
    return str
end

--- The values in the array1/array2 must be non-negative number.
--- Returns a deduplicated array.
function array_and(array1, array2)
    assert(type(array1) == "table", "array1 is not a table")
    assert(type(array2) == "table", "array2 is not a table")
    table.sort(array1)
    table.sort(array2)
    local array1maxval = next(array1) and array1[#array1] or 0
    local array2maxval = next(array2) and array2[#array2] or 0
    local cycle = (array1maxval > array2maxval) and array1maxval or array2maxval
    local array, tbl, tmp1, tmp2 = {}, {}, {}, {}

    for i = 1, #array1, 1 do
        tmp1[array1[i]] = true
    end

    for i = 1, #array2, 1 do
        tmp2[array2[i]] = true
    end

    for i = 1, cycle, 1 do
        if tmp1[i] and tmp2[i] then
            tbl[i] = true
        end
    end

    for i = 1, cycle, 1 do
        if tbl[i] then
            table.insert(array, i)
        end
    end

    return array
end

--- add array2 to array1
--- The values in the array1/array2 must be non-negative number.
--- Returns a deduplicated array.
function array_add(array1, array2)
    assert(type(array1) == "table", "array1 is not a table")
    assert(type(array2) == "table", "array2 is not a table")
    table.sort(array1)
    table.sort(array2)
    local array1maxval = next(array1) and array1[#array1] or 0
    local array2maxval = next(array2) and array2[#array2] or 0
    local cycle = (array1maxval > array2maxval) and array1maxval or array2maxval
    local array, tbl = {}, {}
    for i = 1, #array1, 1 do
        tbl[array1[i]] = true
    end

    for i = 1, #array2, 1 do
        tbl[array2[i]] = true
    end

    for i = 1, cycle, 1 do
        if tbl[i] then
            table.insert(array, i)
        end
    end

    return array
end

--- delete array2 from array1
--- The values in the array1/array2 must be non-negative number.
--- Returns a deduplicated array.
function array_del(array1, array2)
    assert(type(array1) == "table", "array1 is not a table")
    assert(type(array2) == "table", "array2 is not a table")
    table.sort(array1)
    table.sort(array2)
    local array1maxval = next(array1) and array1[#array1] or 0
    local array2maxval = next(array2) and array2[#array2] or 0
    local cycle = (array1maxval > array2maxval) and array1maxval or array2maxval
    local array, tbl = {}, {}
    for i = 1, #array1, 1 do
        tbl[array1[i]] = true
    end

    for i = 1, #array2, 1 do
        tbl[array2[i]] = false
    end

    for i = 1, cycle, 1 do
        if tbl[i] then
            table.insert(array, i)
        end
    end

    return array
end
