require "bit"
require "luci.sys"
require "luci.tools.webadmin"
require "nixio.fs"
local json = require "luci.json"
local comdb = require "luci.controller.lib.comdb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.modbus", package.seeall)

function index()
    entry({"api", "modbus"}, alias("api", "modbus", "conf"), nil).hidden = true
    entry({"api", "modbus", "conf"}, call("handle_config"), nil).leaf = true
    entry({"api", "modbus", "state"}, call("handle_state"), nil).leaf = true
    entry({"api", "modbus", "stat"}, call("handle_statistics"), nil).leaf = true
end

function serial_mode(val)
    local mode = {}
    mode['none'] = 0
    mode['tcp-client'] = 1
    mode['tcp-server'] = 2
    return mode[tostring(val)]
end

function baud_rate(val)
    local baudrate = {}
    baudrate['300'] = 300
    baudrate['1200'] = 1200
    baudrate['9600'] = 9600
    baudrate['19200'] = 19200
    baudrate['38400'] = 38400
    baudrate['57600'] = 57600
    baudrate['115200'] = 115200
    return baudrate[tostring(val)]
end

function data_bits(val)
    local bits = {}
    bits['7'] = 7
    bits['8'] = 8
    return bits[tostring(val)]
end

function stop_bits(val)
    local bits = {}
    bits['1'] = 1
    bits['2'] = 2
    return bits[tostring(val)]
end

function serial_parity(val)
    local parity = {}
    parity['none'] = 1
    parity['odd'] = 2
    parity['even'] = 3
    parity['mark'] = 4
    parity['space'] = 5
    return parity[tostring(val)]
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info'] == "table", "info is error"))
        assert(type(params['info']['id'] == "number", "id is error"))
        assert(type(params['info']['mode'] == "string", "mode is error"))
        assert(type(params['info']['serial'] == "table", "serial is error"))
        assert(type(params['info']['com'] == "table", "com is error"))

        local check = true
        if not serial_mode(params['info']['mode']) then check = false end
        if not baud_rate(params['info']['serial']['baudrate']) then check = false end
        if not data_bits(params['info']['serial']['databits']) then check = false end
        if not stop_bits(params['info']['serial']['stopbits']) then check = false end
        if not serial_parity(params['info']['serial']['parity']) then check = false end
        if not tools.range_hit(params['info']['com']['bufsz'], 0, 128) then check = false end
        if not tools.range_hit(params['info']['com']['interval'], 1, 1000) then check = false end
        if not tools.range_hit(params['info']['com']['max_pktlen'], 0, 1460) then check = false end
        if not tools.range_hit(params['info']['com']['alive_interval'], 10, 300) then check = false end

        if params['info']['mode'] == "tcp-server" and params['info']['server'] then
            if params['info']['server']['port'] and not tools.range_hit(params['info']['server']['port'], 1, 65535) then check = false end
        end

        if not check then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end

        local oper = params['oper'] or ''
        local info = params['info']
        local ids = params['ids'] or {}
        for _, id in ipairs(ids) do
            local data = {}
            local global = {}
            global['id'] = id
            table.insert(data, "type=mode;id=" .. id)
            if not comdb.sdsm_delall("/sdsm/conf", data, 2) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end

            if oper ~= "reset" then
                global['mode'] = info['mode']
                global['serial'] = {}
                global['serial']['baud'] = info['serial']['baudrate']
                global['serial']['databits'] = info['serial']['databits']
                global['serial']['parity'] = info['serial']['parity']
                global['serial']['stopbits'] = info['serial']['stopbits']
                global['pack'] = {}
                global['pack']['buffer'] = info['com']['bufsz']
                global['pack']['interval'] = info['com']['interval']
                global['pack']['length'] = info['com']['max_pktlen']
                global['pack']['alive'] = info['com']['alive_interval']
                global['server'] = {}
                global['server']['port'] = ''
                global['server']['connection'] = ''
                if info['server'] then
                    global['server']['port'] = info['server']['port'] or ''
                    global['server']['connection'] = info['server']['max_connection'] or ''
                end
                global['client'] = { {id = 1}, {id = 2}, {id = 3}, {id = 4} }
                if info['client'] and info['client'][1] and info['client'][2] and info['client'][3] and info['client'][4] then
                    for i = 1, 4 do
                        if type(info['client'][i]['rport']) == "number" and not tools.range_hit(info['client'][i]['rport'], 1, 65535) then
                            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
                        end
                        if type(info['client'][i]['lport']) == "number" and not tools.range_hit(info['client'][i]['lport'], 1, 65535) then
                            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
                        end
                        global['client'][i]['ip'] = info['client'][i]['rip'] or ''
                        global['client'][i]['rport'] = tools.valfilter(info['client'][i]['rport'], "") or ""
                        global['client'][i]['lport'] = tools.valfilter(info['client'][i]['lport'], "") or ""
                    end
                else
                    for i = 1, 4 do
                        global['client'][i]['ip'] = ''
                        global['client'][i]['rport'] = ''
                        global['client'][i]['lport'] = ''
                    end
                end

                data = {}
                table.insert(data, "type=mode;id=" .. global['id'] .. ";" .. "mode=" .. global['mode'] .. ";")
                table.insert(data, "type=serial;id=" .. global['id'] .. ";baud=" .. global['serial']['baud'] .. ";databits=" ..
                                    global['serial']['databits'] .. ";parity=" .. global['serial']['parity'] .. ";stopbits=" ..
                                    global['serial']['stopbits'] .. ";")
                table.insert(data, "type=pack;id=" .. global['id'] .. ";buffer=" .. global['pack']['buffer'] .. ";interval=" ..
                                    global['pack']['interval'] .. ";length=" .. global['pack']['length'] .. ";alive=" ..
                                    global['pack']['alive'] .. ";")

                if global['mode'] == "tcp-client" then
                    for i = 1, 4 do
                        table.insert(data, "type=client;id=" .. global['id'] .. ";clientid=" .. i .. ";ip=" ..
                                            global['client'][i]['ip'] .. ";rport=" .. global['client'][i]['rport'] ..
                                            ";lport=" .. global['client'][i]['lport'] .. ";")
                    end
                end

                if global['mode'] == "tcp-server" then
                    table.insert(data, "type=server;id=" .. global['id'] .. ";port=" .. global['server']['port'] ..
                                        ";connection=" .. global['server']['connection'] .. ";")
                end

                if not comdb.sdsm_setall("/sdsm/conf", data, 1) then
                    return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                end
            end
        end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local conftbl = comdb.sdsm_getall("/sdsm/conf", 1)
    for _, conf in ipairs(conftbl) do
        local row = {}
        row['id'] = tonumber(conf['id'])
        row['mode'] = conf['mode']
        row['serial'] = {}
        row['serial']['baudrate'] = tonumber(conf['serial']['baud'])
        row['serial']['databits'] = tonumber(conf['serial']['databits'])
        row['serial']['parity'] = conf['serial']['parity']
        row['serial']['stopbits'] = tonumber(conf['serial']['stopbits'])
        row['com'] = {}
        row['com']['bufsz'] = tonumber(conf['pack']['buffer'])
        row['com']['interval'] = tonumber(conf['pack']['interval'])
        row['com']['max_pktlen'] = tonumber(conf['pack']['length'])
        row['com']['alive_interval'] = tonumber(conf['pack']['alive'])
        if type(conf['server']) == "table" then
            row['server'] = {}
            row['server']['port'] = tonumber(conf['server']['port'])
            row['server']['max_connection'] = tonumber(conf['server']['connection'])
        end

        row['client'] = { {id = 1}, {id = 2}, {id = 3}, {id = 4} }
        if type(conf['client']) == "table" then
            for k, v in ipairs(conf['client']) do
                row['client'][k]['id'] = tonumber(v['id'])
                row['client'][k]['rip'] = v['ip'] ~= "0.0.0.0" and v['ip'] or nil 
                row['client'][k]['rport'] = v['rport'] ~= "0" and tonumber(v['rport']) or nil
                row['client'][k]['lport'] = v['lport'] ~= "0" and tonumber(v['lport']) or nil
                if v['valid'] == "0" then
                    row['client'][k]['rip'] = nil
                    row['client'][k]['rport'] = nil
                    row['client'][k]['lport'] = nil
                end
            end
            row['client'] = tools.array_check(row['client'])
        end

        table.insert(destbl, row)
    end

    local data = { data = tools.array_check(destbl) }
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_state()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "GET" then
        local destbl = {}
        local statustbl = comdb.sdsm_getall("/sdsm/status", 2)
        for _, status in ipairs(statustbl) do
            local row = {}
            row['id'] = status['id']
            row['mode'] = status['mode']
            row['state'] = status['Status']
            row['peer_ip'] = status['Remote-IP']
            row['peer_port'] = tonumber(status['Remote-Port'])
            row['local_ip'] = status['Local-IP']
            row['local_port'] = tonumber(status['Local-Port'])
            table.insert(destbl, row)
        end

        local data = { data = tools.array_check(destbl) }
        luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
    end
end

function handle_statistics()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "GET" then
        local destbl = {}
        local stattbl = comdb.sdsm_getall("/sdsm/statistics", 1)
        for _, stat in ipairs(stattbl) do
            local row = {}
            row['id'] = tonumber(stat['id'])
            row['net_rx_octets'] = tonumber(stat['Net Octets Rx'])
            row['net_rx_pkts'] = tonumber(stat['Net Packets Rx'])
            row['net_tx_octets'] = tonumber(stat['Net Octets Tx'])
            row['net_tx_pkts'] = tonumber(stat['Net Packets Tx'])
            row['serial_rx_octets'] = tonumber(stat['Serial Octets Rx'])
            row['serial_rx_pkts'] = tonumber(stat['Serial Packets Rx'])
            row['serial_tx_octets'] = tonumber(stat['Serial Octets Tx'])
            row['serial_tx_pkts'] = tonumber(stat['Serial Packets Tx'])
            row['net_chg_cnt'] = tonumber(stat['Net Connect Up/Down times'])
            row['serial_drop_cnt'] = tonumber(stat['Serial Overload Drop Packets'])
            table.insert(destbl, row)
        end

        local data = { data = tools.array_check(destbl) }
        luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
    end
end
