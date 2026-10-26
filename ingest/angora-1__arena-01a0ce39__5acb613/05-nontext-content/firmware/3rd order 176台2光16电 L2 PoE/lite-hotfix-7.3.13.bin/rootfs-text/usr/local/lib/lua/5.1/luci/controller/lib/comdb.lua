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

module ("luci.controller.lib.comdb", package.seeall)

function index()
end

function dbgprint(str)
    local fd = io.open("/luci/tmp", "a+")
    if fd ~= nil then
        fd:write(tostring(str) .. "\n")
        fd:close()
    end
end

function setopt(val)
    local tbl = {}
    tbl['1'] = "1"  -- add
    tbl['2'] = "2"  -- del
    tbl['6'] = "6"  -- update
    return tbl[tostring(val)] or "6"
end

function com_getall(apiname, uri, step, opt)
    local step = step or 4
    local range_start = 0
    local global = {}
    while true do
        local row = {}
        local data = "range_start="..range_start..";range_count="..step..";" .. (opt or "")
        local str = librpc.callapi(apiname, uri.."&"..data.."&5")
        _, _, row["uri"], row["data"], oper, result = string.find(str, string.rep("(.-)&", 3) .. "(.*)")
        if (result ~= "0") then
            return {}
        end
        local tbl = json.decode(row["data"]) or {}
        for _, v in ipairs(tbl) do
            table.insert(global, v)
        end
        if #tbl < step then
            break
        end
        range_start = range_start + step
    end
    return global
end

--- func desc
---@param apiname string
---@param uri string
---@param cmdlst table
---@param step number
---@param oper number
function com_setall(apiname, uri, cmdlst, step, oper)
    local oper = setopt(oper)
    local step = step or 4
    local data = ""
    for i = 1, #cmdlst, step do
        data = cmdlst[i]
        for j = 1, step - 1 do
            data = data .. (cmdlst[i + j] and ("|" .. cmdlst[i + j]) or "")     -- There can be no spaces before and after "|"
        end
        --dbgprint("line: " .. data)
        if librpc.callapi(apiname, uri .. "&" .. data .. "&" .. oper) ~= "0" then
            return false
        end
    end

    return true
end

function dhcpd_getall(uri, step)
    return com_getall("oltmib_dhcpdinfo_get_1", uri, step)
end

function dhcpd_setall(uri, cmdlst, step)
    return com_setall("oltmib_dhcpdinfo_set_1", uri, cmdlst, step, 6)
end

function dhcpd_addall(uri, cmdlst, step)
    return com_setall("oltmib_dhcpdinfo_set_1", uri, cmdlst, step, 1)
end

function dhcpd_delall(uri, cmdlst, step)
    return com_setall("oltmib_dhcpdinfo_set_1", uri, cmdlst, step, 2)
end

function dhcpsnp_getall(uri, step)
    return com_getall("oltmib_dhcpsnp_get_1", uri, step)
end

function dhcpsnp_setall(uri, cmdlst, step)
    return com_setall("oltmib_dhcpsnp_set_1", uri, cmdlst, step, 6)
end

function sdsm_getall(uri, step)
    return com_getall("oltmib_sdsminfo_get_1", uri, step)
end

function sdsm_setall(uri, cmdlst, step)
    return com_setall("oltmib_sdsminfo_set_1", uri, cmdlst, step, 6)
end

function sdsm_delall(uri, cmdlst, step)
    return com_setall("oltmib_sdsminfo_set_1", uri, cmdlst, step, 2)
end
