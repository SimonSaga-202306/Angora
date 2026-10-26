local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.erps", package.seeall)

function index()
    entry({"api", "erps"}, alias("api", "erps", "info"), nil).hidden = true
    entry({"api", "erps", "info"}, call("handle_info"), nil).leaf = true
    entry({"api", "erps", "inst"}, call("handle_instance"), nil).leaf = true
    entry({"api", "erps", "ring"}, call("handle_ring"), nil).leaf = true
end

--['cmd'] is a magic number
function handle_info()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['name']) == "string", "name is error")
        assert(type(params['oper']) == "string", "oper is error")

        local inst = mydb.geterpsinst(params['name'])
        if inst and inst['OwnerInterface'] and inst['OwnerInterface'] == "None" then
            return luci.http.write_json({hdr = {code = 100, message = "Cannot revert on non-owner node", type = "fail"}})
        end

        local ntbl = {}
        ntbl['name'] = params['name']
        ntbl['cmd'] = '3'
        ntbl['is_east'] = ''
        mydb.seterpsstate(ntbl)
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local erpsstatetbl = mydb.geterpsstatetable()
    for _, v in ipairs(erpsstatetbl) do
        local mtbl = {}
        mtbl['name'] = v['name']
        mtbl['ringid'] = tonumber(v['ringid'])
        mtbl['state'] = v['state']
        mtbl['lastevt'] = v['lastpriority']
        mtbl['east'] = v['east']
        mtbl['west'] = v['west']
        table.insert(destbl, mtbl)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_instance()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['name']) == "string", "name is error")

        local erpsinsttbl = mydb.geterpsinsttable()
        if params['oper'] == "del" then
            for _, v in ipairs(erpsinsttbl) do
                if v['Name'] == params['name'] then
                    mydb.delerpsinst(params['name'])
                end
            end
            return luci.http.write_json({hdr = {code = 0, message = "complete deletion", type = "success"}})
        else
            assert(type(params['rapsvlan']) == "number", "rapsvlan is error")
            assert(type(params['ringid']) == "number" and (params['ringid'] > 0 and params['ringid'] <= 255), "ringid is error")
            assert(type(params['id']) == "nil" or (type(params['id']) == "number" and params['id'] >= 0 and params['id'] <= 255), "id is error")
            assert(type(params['level']) == "nil" or (type(params["level"]) == "number" and params['level'] >= 0 and params['level'] <= 7), "level is error")

            for _, v in ipairs(erpsinsttbl) do
                if params['name'] == v['Name'] then
                    mydb.delerpsinst(tostring(params['name']))
                end
            end

            local ntbl = {}
            ntbl['RAPSvlan'] = params['rapsvlan']
            ntbl['Name'] = params['name']
            ntbl['Ring'] = tostring(params['ringid'])
            ntbl['ID'] = tostring(params['id'] or 0)
            ntbl['Level'] = tostring(params['level'] or 0)
            ntbl['OwnerInterface'] = params['ownerif'] or 'None'
            ntbl['Subringif'] = params['subringif'] or 'None'
            ntbl['Attachedinst'] = params['attachinst'] or ''
            if not mydb.seterpsinst(ntbl) then
                return luci.http.write_json({hdr = {code = 100, message = "edit instance is error", type = "fail"}})
            end

            return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
        end
    end

    local destbl = {}
    local erpsinsttbl = mydb.geterpsinsttable()
    for _, v in ipairs(erpsinsttbl) do
        local mtbl = {}
        mtbl['name'] = v['Name']
        mtbl['id'] = tonumber(v['ID'])
        mtbl['ringid'] = tonumber(v['Ring'])
        mtbl['level'] = tonumber(v['Level'])
        mtbl['rapsvlan'] = tonumber(v['RAPSvlan'])
        mtbl['ownerif'] = v['OwnerInterface']
        mtbl['subringif'] = v['Subringif']
        mtbl['attachinst'] = v['Attachedinst']
        table.insert(destbl, mtbl)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end

function handle_ring()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params['id']) == "number", "id is error")

        local ringid = tostring(params['id'])
        local erpsringtbl = mydb.geterpsringtable()
        if params['delete'] == true then
            for _, v in ipairs(erpsringtbl) do
                if v['Index'] == ringid then
                    mydb.delerpsring(ringid)
                end
            end
            return luci.http.write_json({hdr = {code = 0, message = "complete deletion", type = "success"}})
        else
            assert(type(params['east']) == 'string', "east-interface is error")
            assert(type(params['west']) == 'string', "west-interface is error")

            local porttbl = mydb.getporttable(27)
            local eastport = mydb.getportintbl_by_name(porttbl, params['east'])
            local westport = mydb.getportintbl_by_name(porttbl, params['west'])
            if (eastport and eastport['mytype'] == 0x10 ) or (westport and westport['mytype'] == 0x10) then
                return luci.http.write_json({hdr = {code = 100, message = "Cannot configure member interface of port-channel!", type = "fail"}})
            end

            for _, v in ipairs(erpsringtbl) do
                if v['Index'] == ringid then
                    mydb.delerpsring(ringid)
                end
            end

            local ntbl = {}
            ntbl['Index'] = ringid
            ntbl['EASTInterface'] = params['east']
            ntbl['WESTInterface'] = params['west']
            if not mydb.seterpsring(ntbl) then
                return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
            end
        end
        return luci.http.write_json({hdr = {code = 0, message = "Create ring successfully", type = "success"}})
    end

    local destbl = {}
    local erpsringtbl = mydb.geterpsringtable()
    for _, v in ipairs(erpsringtbl) do
        local mtbl = {}
        mtbl['id'] = tonumber(v['Index'])
        mtbl['east'] = v['EASTInterface']
        mtbl['west'] = v['WESTInterface']
        table.insert(destbl, mtbl)
    end

    local data = {data = tools.array_check(destbl)}
    luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
