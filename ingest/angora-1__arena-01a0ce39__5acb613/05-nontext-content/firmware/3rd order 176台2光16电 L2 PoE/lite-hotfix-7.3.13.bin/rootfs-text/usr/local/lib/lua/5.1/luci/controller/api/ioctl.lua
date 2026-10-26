local json = require "luci.json"
local mydb = require "luci.mydb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.ioctl", package.seeall)

function index()
    entry({"api", "ioctl"}, alias("api", "ioctl", "conf"), nil).hidden = true
    entry({"api", "ioctl", "conf"}, call("handle_config"), nil).leaf = true
end

function handle_config()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        if type(params['info']) == "table" and params['info']['desc'] and not tools.range_hit(#params['info']['desc'], 0, 64) then
            return luci.http.write_json({hdr = {code = 1000, message = "Given parameters are invalid!", type = "fail"}})
        end

        local ids = params['ids']
        local info = params['info'] or {}
        local oper = params['oper'] or ""
        local ioctlinfotbl = mydb.getioctlinfotbl()
        for _, id in ipairs(ids) do
            for _, ioctlinfo in ipairs(ioctlinfotbl) do
                if id == tonumber(ioctlinfo['id']) then
                    ioctlinfo['desc'] = info['desc'] or ioctlinfo['desc']
                    if ioctlinfo['dir'] == "out" then
                        ioctlinfo['level'] = info['level'] or ioctlinfo['level']
                    else
                        ioctlinfo['level'] = 0
                    end

                    if not mydb.setioctlinfo(ioctlinfo) then
                        return luci.http.write_json({hdr = {code = 100, message = "Given parameters are invalid!", type = "fail"}})
                    end
                end
            end
        end
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local destbl = {}
    local ioctlinfotbl = mydb.getioctlinfotbl()
    for _, ioctlinfo in ipairs(ioctlinfotbl) do
        local row = {}
        row['id'] = tonumber(ioctlinfo['id'])
        row['desc'] = ioctlinfo['desc']
        row['dir'] = ioctlinfo['dir']
        row['level'] = ioctlinfo['level']
        row['level_def'] = ioctlinfo['level_def']
        table.insert(destbl, row)
    end

    local data = { data = tools.array_check(destbl) }
    return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}, result = data})
end
