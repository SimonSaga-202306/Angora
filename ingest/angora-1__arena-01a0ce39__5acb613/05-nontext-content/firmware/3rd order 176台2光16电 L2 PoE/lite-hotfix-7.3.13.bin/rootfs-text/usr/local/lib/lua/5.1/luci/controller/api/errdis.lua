local json = require "luci.json"
local tools = require "luci.controller.lib.tools"
local librpc = require "librpc"
local bit = bit

module("luci.controller.api.errdis", package.seeall)

function index()
    entry({ "api", "errdis" }, alias("api", "errdis", "conf"), nil).hidden = true
    entry({ "api", "errdis", "conf" }, call("handle_config"), nil).leaf = true
    entry({ "api", "errdis", "portconf" }, call("handle_portconfig"), nil).leaf = true
end

local reasonMap = {
    -- { name = "LAG Mismatch", flag = bit.lshift(1, 0) },
    { name = "BPDU Guard", flag = bit.lshift(1, 1) },
    { name = "Port Up/Down", flag = bit.lshift(1, 2) },
    { name = "Port Security", flag = bit.lshift(1, 3) },
    -- { name = "MAC Flapping", flag = bit.lshift(1, 4) },
    -- { name = "PoE Exception", flag = bit.lshift(1, 5) }，
    { name = "Loop Detect", flag = bit.lshift(1, 6) }
}
function reason2modes(reason)
    local tbl = {}
    for _, v in pairs(reasonMap) do
        table.insert(tbl, { name = v["name"], state = (bit.band(reason, v["flag"]) ~= 0) })
    end
    return tbl
end

function modes2reason(tbl)
    local reason = 0
    for _, v in pairs(tbl) do
        if v["state"] then
            for _, m in pairs(reasonMap) do
                if v["name"] == m["name"] then
                    reason = bit.bor(reason, m["flag"])
                end
            end
        end
    end
    return reason
end

function print_reason(reason)
    local modes = reason2modes(reason)
    for _, v in pairs(modes) do
        if v["state"] then
            return v["name"]
        end
    end

    return ""
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")

        reason = modes2reason(params["mode"])
        timeout = tools.valfilter(params["timeout"], 0) ~= 0
        interval = timeout and params["timeout"] or 0
        ret = librpc.callapi("oltmib_errdisable_set_1", reason .. "&" .. tools.bool_trans(timeout) .. "&" .. interval) == "0"
        if not ret then
            return luci.http.write_json({ hdr = { code = 100, message = "Given parameters are invalid!", type = "fail" } })
        end
        return luci.http.write_json({ hdr = { code = 0, message = "ok", type = "success" } })
    end

    str = librpc.callapi("oltmib_errdisable_get_1", "")
    _, _, reason, timeout, interval, msg, oper, result = string.find(str, string.rep("(.-)&", 5) .. "(.*)")
    local destbl = { mode = reason2modes(tonumber(reason)), timeout = timeout ~= "0" and tonumber(interval) or 0 }

    local data = tools.array_check(destbl)
    return luci.http.write_json({ hdr = { code = 0, message = "ok", type = "success" }, result = data })
end

function handle_portconfig()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params["ports"]) == "table", "params is error")

        local porttbl = params["ports"]
        for _, id in ipairs(porttbl) do
            ret = librpc.callapi("oltmib_errdisportinfo_set_1", id .. "&&&&") == "0"
            if not ret then
                return luci.http.write_json({ hdr = { code = 100, message = "Given parameters are invalid!", type = "fail" } })
            end
        end

        return luci.http.write_json({ hdr = { code = 0, message = "ok", type = "success" } })
    end

    local destbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_errdisportinfo_getn_1", str)
        _, _, ifx, name, reason, msg, oper, result = string.find(str, string.rep("(.-)&", 5) .. "(.*)")
        if (result == "0") then
            row["id"] = tonumber(ifx)
            row["name"] = name
            row["reason"] = print_reason(reason)
            table.insert(destbl, row)
        end
    end

    local data = tools.array_check(destbl)
    return luci.http.write_json({ hdr = { code = 0, message = "ok", type = "success" }, result = data })
end
