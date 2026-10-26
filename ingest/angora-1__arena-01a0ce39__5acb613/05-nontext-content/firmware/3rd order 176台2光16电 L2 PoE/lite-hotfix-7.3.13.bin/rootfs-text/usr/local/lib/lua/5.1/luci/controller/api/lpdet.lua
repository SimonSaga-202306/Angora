local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"
local librpc = require "librpc"

module("luci.controller.api.lpdet", package.seeall)

function index()
    entry({"api", "lpdet"}, alias("api", "lpdet", "conf"), nil).hidden = true
    entry({"api", "lpdet", "conf"}, call("handle_conf"), nil).leaf = true
    entry({"api", "lpdet", "portconf"}, call("handle_portconf"), nil).leaf = true
end

function handle_conf()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")

        local oper = ""
        state = tools.bool_trans(params["admin_state"])
        interval = params["interval"]
        trap_state = tools.bool_trans(params["trap"])

        ret = librpc.callapi("oltmib_lpdet_global_set_1", state .. "&" .. interval .. "&" .. trap_state .. "&&" .. oper .. "&" ) == "0"
        if not ret then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    str = librpc.callapi("oltmib_lpdet_global_get_1", "")
    _, _, state, interval, trap_state, msg, oper, result = string.find(str, string.rep("(.-)&", 5) .. "(.*)")
    destbl["admin_state"] = tools.bool_trans(state)
    destbl["interval"] = tonumber(interval)
    destbl["trap"] = tools.bool_trans(trap_state)

    local data = tools.array_check(destbl)
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_portconf()
    luci.http.prepare_content("application/json")
    if luci.http.getenv('REQUEST_METHOD') == 'POST' then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params["ports"]) == "table", "ports is error")
        assert(type(params["info"]) == "table", "info is error")
        assert(type(params["info"]["status"]) == "boolean", "status is error")

        local porttbl = params["ports"] or {}
        local info = params["info"]
        local oper = params["oper"] or ''
        for _, id in pairs(porttbl) do
            local vlantbl = {}
            local vlanstr = ""
            local portinfo = mydb.getport(id)
            if portinfo and portinfo["mytype"] == 0x10 then
                return luci.http.write_json({hdr = {code = 100, message = "Cannot configure the member interface of port-channel!", type = "fail"}})
            end

            str = librpc.callapi("oltmib_lpdet_portinfo_get_1", id .. "&&&&&&&&&&")
            _, _, ifx, name, state, vlan_list, action_type, action_status, timestamp, count, msg, oper, result = string.find(str, string.rep("(.-)&", 10) .. "(.*)")
            if result ~= "0" then
                return luci.http.write_json({hdr = {code = 100, message = "May be trying to configure the member interface of port-channel!", type = "fail"}})
            end

            vlanstr = tools.valfilter(info["vlans"], "none") or ""
            if vlanstr ~= "" and vlanstr ~= "none" then
                vlantbl = mydb.vlanstr2tbl(vlanstr)
                if #vlantbl > 8 then
                    return luci.http.write_json({hdr = {code = 1000, message = "Configure the maximum number of vlans to 8!", type = "fail"}})
                end
                vlanstr = mydb.vlanarray2str(vlantbl)
            end

            ret = librpc.callapi("oltmib_lpdet_portinfo_set_1", ifx .. "&&" .. tools.bool_trans(info["status"]) .. "&" .. (vlanstr or "") .. "&" .. (info["action"] or action_type) .. "&&&&&6&") == "0"
            if not ret then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    result = "0"
    str = ""
    while (result == "0") do
        local row = {}
        str = librpc.callapi("oltmib_lpdet_portinfo_getn_1", str)
        _, _, ifx, name, state, vlan_list, action_type, action_status, timestamp, count, msg, oper, result = string.find(str, string.rep("(.-)&", 10) .. "(.*)")
        if (result == "0") then
            row["id"] = tonumber(ifx)
            row["name"] = name
            row["status"] = tools.bool_trans(state)
            row["action"] = action_type
            row["actionlast"] = action_status
            row["lasttime"] = timestamp
            row["count"] = tonumber(count)
            row["vlans"] = vlan_list
            table.insert(destbl, row)
        end
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
