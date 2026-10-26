local json = require "luci.json"
local mydb = require "luci.mydb"
local srvdb = require "luci.controller.lib.srvdb"
local tools = require "luci.controller.lib.tools"
local nixio = require "nixio"
local fs = require "nixio.fs"

module("luci.controller.api.diag", package.seeall)

function index()
    entry({"api", "diag"}, alias("api", "diag", "info"), nil).hidden = true
    entry({"api", "diag", "info"}, call("handle_info"), nil).leaf = true
    entry({"api", "diag", "action"}, call("handle_action"), nil).leaf = true
    entry({"api", "diag", "transceivers"}, call("handle_transceivers"), nil).leaf = true
    entry({"api", "diag", "transceiver"}, call("handle_transceiver"), nil).leaf = true
    entry({"api", "diag", "cabledetect"}, call("handle_cabledetect"), nil).leaf = true
end

function diag_cmd(cmd, addr)
    if addr and addr:match("^[%w%-%.:_]+$") then

        local result = ''
		local util = io.popen(cmd % addr)
		if util then
			while true do
				local ln = util:read("*l")
				if not ln then break end
                result = result .. ln .. "\n"
			end

			util:close()
		end

		return result
	end

    return "addr unreachable"
end

function handle_info()
    local pkgname = "diag.tar"
    local pkgpath = "/var/"
    local logfile = "log/"
    local diagfile = "diag/"

    os.execute("mkdir -p " .. pkgpath .. diagfile)
    os.execute("/usr/bin/diag.sh " .. pkgpath .. diagfile)
    local backup_cmd = "cd " .. pkgpath .." && tar -cf - " .. logfile .. " " .. diagfile
    local reader = srvdb.ltn12_popen(backup_cmd)

    local sys_info = srvdb.getsysinfo()
    local host = luci.http.getenv('HTTP_HOST') or "NULL"
    luci.http.header('Content-Disposition', 'attachment; filename="backup-%s-%s-%s"' % {sys_info["hostname"] or luci.sys.hostname(), host, pkgname})
    luci.http.prepare_content("application/x-targz")
    luci.ltn12.pump.all(reader, luci.http.write)
    os.execute("rm -rf " ..  pkgpath .. diagfile)
end

function handle_action()
    if luci.http.getenv('REQUEST_METHOD') == 'POST' then
        local params = json.decode(luci.http.content())
        local args = params['args']
        local addr = args['ipv4'] or args['ipv6']

        local ack = ''
        local has_ping6 = fs.access("/bin/ping6") or fs.access("/usr/bin/ping6")
        local has_traceroute6 = fs.access("/usr/bin/traceroute6")
        if params['cmd'] == 'ping' then
            ack = diag_cmd("ping -c 5 -W 5 %q 2>&1", addr)
        elseif params['cmd'] == 'ping6' then
            if has_ping6 then
                ack = diag_cmd("ping6 -c 5 -W 5 %q 2>&1", addr)
            else
                ack = "Install iputils-ping6 for IPv6 ping"
            end
        elseif  params['cmd'] == 'traceroute' then
            ack = diag_cmd("traceroute -q 1 -m 20 -w 1 -n %q 2>&1", addr)
        elseif params['cmd'] == 'traceroute6' then
            if has_traceroute6 then
                ack = diag_cmd("traceroute6 -q 1 -m 20 -w 1 -n %q 2>&1", addr)
            else
                ack = "Install iputils-traceroute6 for IPv6 traceroute"
            end
        else
            return luci.http.write_json({hdr = {code = 100, message = "cmd is error", type = "fail"}})
        end

        local data = {output = ack}
        luci.http.prepare_content("application/json")
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
    end
end

function handle_transceivers()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "GET" then
        local destbl = {}
        local opticalinfotbl = mydb.getopticalinfotbl()
        for _, optical in ipairs(opticalinfotbl) do
            local row = {}
            row['id'] = tonumber(optical['ifx'])
            row['name'] = optical['ifname']
            row['state'] = optical['state']
            row['status'] = optical['ts_state']
            if optical['ts_state'] == "OK" then
                row['temperature'] = tonumber(optical['temp'])
                row['temperature_st'] = optical['temp_state']
                row['voltage'] = tonumber(optical['volt']) / 10000
                row['voltage_st'] = optical['volt_state']
                row['current'] = tonumber(optical['bias']) / 500
                row['current_st'] = optical['bias_state']
                row['rx_power'] = tonumber(optical['rx_power']) / 100
                row['rx_power_st'] = optical['rxp_state']
                row['tx_power'] = tonumber(optical['tx_power']) / 100
                row['tx_power_st'] = optical['txp_state']
            else
                row['temperature_st'] = "NA"
                row['voltage_st'] = "NA"
                row['current_st'] = "NA"
                row['rx_power_st'] = "NA"
                row['tx_power_st'] = "NA"
            end
            table.insert(destbl, row)
        end

        local data = { data = tools.array_check(destbl) }
        luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
    end
end

function handle_transceiver()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "GET" then
        local alarm_array = {
            -- "Temperature high", -- start from index 1
            "Temperature low", "Voltage high", "Voltage low", -- /* 偏置电流 */
            "TX Channel bias high", "TX Channel bias low", "TX Channel2 bias high",
            "TX Channel2 bias low", "TX Channel3 bias high", "TX Channel3 bias low",
            "TX Channel4 bias high", "TX Channel4 bias low", " ", " ", " ", " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ", " ", " ", -- /* 接受光功率 */
            "RX Channel power high", "RX Channel power low", "RX Channel2 power high",
            "RX Channel2 power low", "RX Channel3 power high", "RX Channel3 power low",
            "RX Channel4 power high", "RX Channel4 power low", " ", " ", " ", " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ", " ", " ", -- /* 发送光功率 */
            "TX Channel power high", "TX Channel power low", "TX Channel2 power high",
            "TX Channel2 power low", "TX Channel3 power high", "TX Channel3 power low",
            "TX Channel4 power high", "TX Channel4 power low", " ", " ", " ", " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
            " ", " ", " ", " ", -- /* 通道无接收光故障 */
            "RX Channel loss of signal", "RX Channel2 loss of signal",
            "RX Channel3 loss of signal", "RX Channel4 loss of signal", " ", " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ", " ",
            -- /* 通道无发送光故障 */
            "TX Channel loss of signal", "TX Channel2 loss of signal",
            "TX Channel3 loss of signal", "TX Channel4 loss of signal", " ", " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ", " ", -- /* 通道发送故障 */
            "TX Channel fault", "TX Channel2 fault", "TX Channel3 fault",
            "TX Channel4 fault", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
            " ",
            -- /* 其它模块特有的以及公用的如校检,模块未就绪等 */
            "Transceiver info checksum error!", "Module not ready", "RX not ready",
            "TX CDR loss of lock", "RX CDR loss of lock",
            "Transceiver type and port configuration mismatch",
            "Transceiver type not supported by port hardware"
        }
        alarm_array[0] = "Temperature high"

        local destbl = {}
        local port = mydb.getport(luci.http.formvalue("id") or "")
        if port and port["if_attr_flags"] and bit.band(port["if_attr_flags"], 512) == 512 then
            mydb.getopticalinfo_port( { ifx = port['Index'] } )
            os.execute("sleep 0.2")     -- Adding some delay between the two read operations can achieve real-time effect.
            local opticalinfo = mydb.getopticalinfo_port( { ifx = port['Index'] } )
            destbl['id'] = tonumber(opticalinfo['ifx'])
            destbl['name'] = opticalinfo['ifname']
            destbl['state'] = opticalinfo['state']
            destbl['sfp_base_type'] = opticalinfo['sfp_base_type']
            destbl['trans_type'] = opticalinfo['trans_type']
            destbl['connect_type'] = opticalinfo['connect_type']
            destbl['wavelength'] = tonumber(opticalinfo['wavelength'])
            destbl['len_smf'] = tonumber(opticalinfo['len_smf'])
            destbl['len_smf_100m'] = tonumber(opticalinfo['len_smf_100m'])
            destbl['len_50_125_om3'] = tonumber(opticalinfo['len_50_125_om3'])
            destbl['len_50_125_om2'] = tonumber(opticalinfo['len_50_125_om2'])
            destbl['len_625_125_om1'] = tonumber(opticalinfo['len_625_125_om1'])
            destbl['len_copper'] = tonumber(opticalinfo['len_copper'])
            destbl['ddm_support'] = opticalinfo['ddm_support'] ~= "0"
            destbl['vendor_sn'] = opticalinfo['vendor_sn']
            destbl['vendor_name'] = opticalinfo['vendor_name']
            destbl['vendor_oui'] = opticalinfo['vendor_oui']
            destbl['vendor_pn'] = opticalinfo['vendor_pn']
            destbl['vendor_rev'] = opticalinfo['vendor_rev']
            destbl['manufact_date'] = opticalinfo['manufact_date']
            destbl['encoding'] = opticalinfo['encoding']
            destbl['alarm'] = {}
            local alarmstr = mydb.hex2bin(string.upper(opticalinfo["alarmstr"] or ""))
            for i = 0, string.len(alarmstr) * 8 - 1 do
                local a_i = math.floor(i / 8) + 1
                local b_i = i % 8
                local b = string.byte(alarmstr, a_i)
                if b ~= nil and bit.band(bit.rshift(b, b_i), 1) == 1 then
                    table.insert(destbl['alarm'], alarm_array[i] or "nil")
                end
            end
            destbl['alarm'] = tools.array_check(destbl['alarm'])
        end

        local data = tools.array_check(destbl)
        luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
    end
end

function handle_cabledetect()
    luci.http.prepare_content("application/json")
    if luci.http.getenv('REQUEST_METHOD') == 'POST' then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['ports']) == "table", "ports is error")

        local porttbl = params['ports']
        -- Empty array means all ports, otherwise means the specified port
        if next(porttbl) then
            for _, ifx in pairs(porttbl) do
                local port = mydb.getport(ifx)
                if port and port["if_attr_flags"] and bit.band(port["if_attr_flags"], 256) == 256 then
                    ret = librpc.callapi("oltmib_cabledetect_set_1", port["Index"] .. "&&&&&&&&&&&&") == "0"
                    if not ret then
                        return luci.http.write_json({hdr = {code = 100, message = "Interface do not support cable detect!", type = "fail"}})
                    end
                end
            end
        else
            local porttbl = mydb.getporttable(27)
            for _, port in pairs(porttbl) do
                if port["if_attr_flags"] and bit.band(port["if_attr_flags"], 256) == 256 then
                    ret = librpc.callapi("oltmib_cabledetect_set_1", port["Index"] .. "&&&&&&&&&&&&") == "0"
                    if not ret then
                        return luci.http.write_json({hdr = {code = 100, message = "Interface do not support cable detect!", type = "fail"}})
                    end
                end
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local id = luci.http.formvalue("id")
    if id and id == "all" then
        result = "0"
        str = ""
        while (result == "0") do
            local row = {}
            str = librpc.callapi("oltmib_cabledetect_getn_1", str)
            _, _, ifx, name, PA_len, PB_len, PC_len, PD_len, PA_state, PB_state, PC_state, PD_state, msg, oper, result = string.find(str, string.rep("(.-)&", 12) .. "(.*)")
            if (result == "0") then
                local row = {}
                row["id"] = tonumber(ifx)
                row["name"] = name
                row["PA_length"] = tonumber(PA_len)
                row["PB_length"] = tonumber(PB_len)
                row["PC_length"] = tonumber(PC_len)
                row["PD_length"] = tonumber(PD_len)
                row["PA_state"] = PA_state
                row["PB_state"] = PB_state
                row["PC_state"] = PC_state
                row["PD_state"] = PD_state
                table.insert(destbl, row)
            end
        end

        local data = {data = tools.array_check(destbl)}
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
    end

    local port = mydb.getport(id or "")
    if port and port["if_attr_flags"] and bit.band(port["if_attr_flags"], 256) == 256 then
        str = librpc.callapi("oltmib_cabledetect_get_1", port["Index"] .. "&&&&&&&&&&")
        _, _, ifx, name, PA_len, PB_len, PC_len, PD_len, PA_state, PB_state, PC_state, PD_state, msg, oper, result = string.find(str, string.rep("(.-)&", 12) .. "(.*)")
        if (result == "0") then
            local row = {}
            row["id"] = tonumber(ifx)
            row["name"] = name
            row["PA_length"] = tonumber(PA_len)
            row["PB_length"] = tonumber(PB_len)
            row["PC_length"] = tonumber(PC_len)
            row["PD_length"] = tonumber(PD_len)
            row["PA_state"] = PA_state
            row["PB_state"] = PB_state
            row["PC_state"] = PC_state
            row["PD_state"] = PD_state
            table.insert(destbl, row)
        end
    else
        return luci.http.write_json({hdr = {code = 1000, message = "Interface do not support cable detect!", type = "fail"}})
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
