local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.igsp", package.seeall)

function index()
    entry({"api", "igsp"}, alias("api", "igsp", "conf"), nil).hidden = true
    entry({"api", "igsp", "conf"}, call("handle_config"), nil).leaf = true
    entry({"api", "igsp", "info"}, call("handle_info"), nil).leaf = true
    entry({"api", "igsp", "mrouter"}, call("handle_mrouter"), nil).leaf = true
    entry({"api", "igsp", "group"}, call("handle_group"), nil).leaf = true
end

function handle_info()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "GET" then

        local destbl = {}
        local porttbl = mydb.getporttable(11)
        local igspgrptbl = mydb.getigspgrptbl()
        for _, igspgrp in ipairs(igspgrptbl) do
            local portinfo = mydb.getportintbl_by_name(porttbl, igspgrp['ifname'])
            local igsp = {}
            igsp['id'] = tonumber(portinfo['Index'])
            igsp['name'] = igspgrp['ifname']
            igsp['vid'] = tonumber(igspgrp['vid'])
            igsp['grp_addr'] = igspgrp['grpip']
            igsp['src_addr'] = igspgrp['srcip']
            igsp['type'] = igspgrp['type']
            table.insert(destbl, igsp)
        end

        local data = {data = tools.array_check(destbl)}
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
    end
end

function handle_mrouter()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['info']['id']) == "number", "id is error")
        assert(type(params['info']['vid']) == "number" and params['info']['vid'] > 0 and params['info']['vid'] <= 4094, "vid is error")

        local info = params['info']
        local oper = params['oper'] or ''
        local portinfo = mydb.getport(info['id'])
        if portinfo and portinfo['mytype'] == 0x10 then
            return luci.http.write_json({hdr = {code = 100, message = "Cannot configure member interface of port-channel!", type = "fail"}})
        end

        local mrouterdata = {}
        mrouterdata['ifname'] = portinfo['Name']
        mrouterdata['vid'] = info['vid']
        if oper == 'del' then
            oper = "2"
        else
            oper = "1"
        end

        if not mydb.setmrouter(mrouterdata, oper) then
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local porttbl = mydb.getporttable(11)
    local mroutertbl = mydb.getmroutertbl()
    for _, mrouter in ipairs(mroutertbl) do
        local portinfo = mydb.getportintbl_by_name(porttbl, mrouter['ifname'])
        local mrouterdata = {}
        mrouterdata['id'] = tonumber(portinfo['Index'])
        mrouterdata['name'] = mrouter['ifname']
        mrouterdata['vid'] = tonumber(mrouter['vid'])
        table.insert(destbl, mrouterdata)
    end

    local data = {data = tools.array_check(destbl)}
    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_group()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['info']) == "table", "info is error")
        assert(type(params['info']['id']) == "number", "id is error")
        assert(type(params['info']['vid']) == "number" and params['info']['vid'] > 0 and params['info']['vid'] <= 4094, "vid is error")
        assert(type(params['info']['grp_addr']) == "string", "grp_addr is error")

        local info = params['info']
        local oper = params['oper'] or ''
        local portinfo = mydb.getport(info['id'])
        if portinfo and portinfo['mytype'] == 0x10 then
            return luci.http.write_json({hdr = {code = 100, message = "Cannot configure member interface of port-channel!", type = "fail"}})
        end

        local staticgrpdata = {}
        staticgrpdata['ifname'] = portinfo['Name']
        staticgrpdata['vid'] = info['vid']
        staticgrpdata['grpip'] = info['grp_addr']
        staticgrpdata['srcip'] = info['src_addr'] or ''

        if oper == 'del' then
            oper = "2"
        else
            oper = "1"
        end

        if not mydb.setstaticgrp(staticgrpdata, oper) then 
            return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
        end
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local porttbl = mydb.getporttable(11)
    local staticgrptbl = mydb.getstaticgrptbl()
    for _, staticgrp in ipairs(staticgrptbl) do
        local portinfo = mydb.getportintbl_by_name(porttbl, staticgrp['ifname'])
        local staticgrpdata = {}
        staticgrpdata['id'] = tonumber(portinfo['Index'])
        staticgrpdata['name'] = staticgrp['ifname']
        staticgrpdata['vid'] = tonumber(staticgrp['vid'])
        staticgrpdata['grp_addr'] = staticgrp['grpip']
        staticgrpdata['src_addr'] = staticgrp['srcip']
        table.insert(destbl, staticgrpdata)
    end

    local data = {data = tools.array_check(destbl)}
    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})    
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['state']) == "boolean", "state is error")
        assert(type(params['drop_unknown']) == "boolean", "drop_unknown is error")
        assert(type(params['suppress_tc']) == "boolean", "suppress_tc is error")

        local igmpsnptbl = {}
        igmpsnptbl[1] = { enabled = params['state'] and "1" or "0" }
        igmpsnptbl[2] = { enabled = params['drop_unknown'] and "1" or "0" }
        igmpsnptbl[3] = { enabled = params['suppress_tc'] and "1" or "0" }
        mydb.setigmpsnptbl(igmpsnptbl)
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local igmpsnptbl = mydb.getigmpsnptbl()
    local igmpsnpdata = {}
    igmpsnpdata['state'] = igmpsnptbl[1]['enabled'] ~= 0
    igmpsnpdata['drop_unknown'] = igmpsnptbl[2]['enabled'] ~= 0
    igmpsnpdata['suppress_tc'] = igmpsnptbl[3]['enabled'] ~= 0
    local data = igmpsnpdata
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
