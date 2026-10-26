local json = require "luci.json"
local srvdb = require "luci.controller.lib.srvdb"
local tools = require "luci.controller.lib.tools"
local nixio = require "nixio"
local fs = require "nixio.fs"

module("luci.controller.api.log", package.seeall)

function index()
    entry({"api", "log"}, alias("api", "log", "info"), nil).hidden = true
    entry({"api", "log", "info"}, call("handle_loginfo"), nil).leaf = true
end

function handle_loginfo()
    luci.http.prepare_content("application/json")

    if luci.http.getenv("REQUEST_METHOD") == "GET" then
        local lasttime = luci.http.formvalue("lasttime") or ''
        local cnt = luci.http.formvalue("max_len") or 20
        local month, day, clock = string.match(lasttime, "(%a+)%s%s(%d+)%s(%d+:%d+:%d+)")
        local timestamp = (month or '') .. '  ' .. (day or '') .. ' ' .. (clock or '')
        local logsstr = luci.sys.exec("tail -n " .. cnt .. " /var/log/syslog 2>/dev/null")
        local loglist = {}

        local logarr = string.split(logsstr, "\n")
        if logarr[#logarr] == "" then logarr[#logarr] = nil end
        if string.gsub(timestamp, " ", "") ~= "" then
            local idx = 0
            for i = 0, #logarr - 1 do
                local data = string.match(logarr[#logarr - i], "^<%d+>(.*)")
                if data then logarr[#logarr - i] = data end
                local date = string.match(logarr[#logarr - i], "(%a+%s%s%d+%s%d+:%d+:%d+)")
                if date == timestamp then
                    idx = #logarr - i
                end
                if idx ~= 0 and date ~= timestamp then
                    break
                end
            end

            for i = (idx ~= 0) and idx or 1, #logarr do
                table.insert(loglist, logarr[i])
            end
        else
            for k, v in ipairs(logarr) do
                local data = string.match(v, "^<%d+>(.*)")
                if not data then data = v end
                table.insert(loglist, data)
            end
        end

        luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = tools.array_check(loglist)})
    end
end
