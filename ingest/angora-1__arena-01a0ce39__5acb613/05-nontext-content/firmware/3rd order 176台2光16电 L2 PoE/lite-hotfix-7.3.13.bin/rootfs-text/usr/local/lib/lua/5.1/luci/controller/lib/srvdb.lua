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
local getdevplatform = luci.mydb.getdevplatform
local setmetatable = setmetatable
local getmetatable = getmetatable

module ("luci.controller.lib.srvdb", package.seeall)
local ipchangefile = "/tmp/.ipchanged"

function index()
end

function ltn12_popen(command)
    local fdi, fdo = nixio.pipe()
    local pid = nixio.fork()
    if pid > 0 then
        fdo:close()
        local close
        return function()
            local buffer = fdi:read(2048)
            local wpid, stat = nixio.waitpid(pid, "nohang")
            if not close and wpid and stat == "exited" then close = true end

            if buffer and #buffer > 0 then
                return buffer
            elseif close then
                fdi:close()
                return nil
            end
        end
    elseif pid == 0 then
        nixio.dup(fdo, nixio.stdout)
        fdi:close()
        fdo:close()
        nixio.exec("/bin/sh", "-c", command)
    end
end

function timetrans(sec)
    local longSec = tonumber(sec)
    s = longSec % 60;
    m = (longSec - s) / 60 % 60;
    h = ((longSec - s) / 60 - m) / 60 % 24;
    d = (((longSec - s) / 60 - m) / 60 - h) / 24;
    return d .. "d " .. h .. "h " .. m .. "m " .. s .. "s "
end

function ipchangefileexist()
    local f = io.open(ipchangefile, "r")
    if f then f:close() end
    return f ~= nil
end

function clearipchangefile()
    os.execute("rm -f " .. ipchangefile)
end

function writecfg()
    str = "&&&&&&1"
    result = librpc.callapi("oltmib_devinfo_set_1", str)
    clearipchangefile()
end

function getsysinfo()
    str = ""
    str = librpc.callapi("oltmib_devinfo_get_1", str)
    _, _, devsn, prdid, mac, swver, swdate, hwver, _, uptime, hostname, result = string.find(str, string.rep("(.-)&", 9) .. "(.*)")
    return { hostname = hostname, mac = mac, hwver = hwver, swver = swver, swdate = swdate, psn = devsn, pid = prdid, uptime = timetrans(uptime) }
end

function setsysinfo(data)
    str = "&&&&&&&&" .. data["hostname"]
    if (data["hostname"] == "") then
        str = "&&&&&&&&&2" -- reset hostname
    end
    result = librpc.callapi("oltmib_devinfo_set_1", str)
end

function getaccount(data)
    account = {}
    str = librpc.callapi("oltmib_account_get_1", "&&&&" .. (data["name"] or ""))
    _, _, status, key, keytype, ip, name, pwd, privilege, msg, oper, result = string.find(str, string.rep("(.-)&", 9) .. "(.*)")
    if (result == "0") then
        account["name"] = name
        account["privilege"] = tonumber(privilege)
    end

    return account
end

function getaccounttbl()
    accounttbl = {}
    -- traverse erpsring
    result = "0"
    str = ""
    while (result == "0") do
        str = librpc.callapi("oltmib_account_getn_1", str)
        _, _, status, key, keytype, ip, name, pwd, privilege, msg, oper, result = string.find(str, string.rep("(.-)&", 9) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["name"] = name
            row["privilege"] = tonumber(privilege)
            table.insert(accounttbl, row)-- add it in order for ipairs
        end
    end
    return accounttbl
end

function setaccount(data)
    str = "&&&&" .. data["name"] .. "&" .. (data["pwd"] or "") .. "&" .. (data["privilege"] or "") .. "&&" .. (data["oper"] or "")
    result = librpc.callapi("oltmib_account_set_1", str)
    return result == "0"
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
end

function ntpsync_trans(val)
    local tbl = {}
    tbl["0"] = "unsynchronized"
    tbl["1"] = "synchronized"
    tbl["unsynchronized"] = "0"
    tbl["synchronized"] = "1"

    return tbl[tostring(val)] or ""
end

function getntp()
    local row = {}
    str = librpc.callapi("oltmib_ntp_get_1", "")
    _, _, zone, ip, ipv6, host, state, sync, stratum, referid, refertm, log2_precision, root_delay, root_dispersion, msg, oper, result = string.find(str, string.rep("(.-)&", 14) .. "(.*)")
    if (result == "0") then
        row["time"] = string.gsub(luci.sys.exec("date \"+%H:%M:%S\""), "\n", "")
        row["date"] = string.gsub(luci.sys.exec("date \"+%Y/%m/%d\""), "\n", "")
        row["zone"] = zone
        row["ip"] = ip
        row["ipv6"] = ipv6
        row["host"] = host
        row["state"] = state
        row["sync"] = ntpsync_trans(sync)
        row["stratum"] = stratum
        row["referid"] = referid
        row["refertm"] = refertm
        row["log2_precision"] = log2_precision
        row["root_delay"] = root_delay
        row["root_dispersion"] = root_dispersion
    end
    return row
end

function setntp(data)
    str = (data["zone"] or "") .. "&" .. (data["ip"] or "") .. "&" .. (data["ipv6"] or "") .. "&" .. (data["host"] or "")
    result = librpc.callapi("oltmib_ntp_set_1", str)
    if data["date"] and data["time"] then
        os.execute("date -s \"" .. data["date"] .. " " .. data["time"] .. "\"")
        os.execute("hwclock -w")
    end

    return result == "0"
end

function getzonetbl()
    local zonelist = '/var/log/zonlist'
    local file, err = io.open(zonelist, "rb")
    local platform = getdevplatform()
    if file == nil then
        if platform == "AC5" then
            os.execute("find /usr/share/zoneinfo/posix/ -type f -printf '%f\n' | sort | uniq > " .. zonelist)
        elseif platform == "LITE" then
            os.execute("find /usr/share/zoneinfo/ -type l -printf '%f\n' | sort | uniq > " .. zonelist)
        else
            os.execute("find /usr/share/zoneinfo/posix/ -type f -print | sed 's#.*/##' | sort | uniq > " .. zonelist)
        end
        file, err = io.open(zonelist, "rb")
        if file == nil then
            return {}
        end
    end
    local data = file:read("*a")
    file:close()
    data = string.gsub(data, "\r", "")
    local tbl = string.split(data, "\n")
    table.insert(tbl, 1, "UTC")
    table.remove(tbl, #tbl)
    return tbl
end
