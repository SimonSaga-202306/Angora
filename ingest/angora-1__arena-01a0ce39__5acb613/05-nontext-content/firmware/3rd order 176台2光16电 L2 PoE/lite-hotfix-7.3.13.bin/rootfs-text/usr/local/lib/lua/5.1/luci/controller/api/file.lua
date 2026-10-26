local nixio = require "nixio"
local fs = require "nixio.fs"
local json = require "luci.json"
local mydb = require "luci.mydb"
local srvdb = require "luci.controller.lib.srvdb"
local tools = require "luci.controller.lib.tools"

module("luci.controller.api.file", package.seeall)

function index()
    entry({"api", "file"}, alias("api", "file", "pkg")).hidden = true
    entry({"api", "file", "image"}, call("handle_image")).leaf = true
    entry({"api", "file", "pkg"}, call("handle_package")).leaf = true
    entry({"api", "file", "progress"}, call("handle_progress")).leaf = true
    entry({"api", "file", "config"}, call("handle_config")).leaf = true
    entry({"api", "file", "cert"}, call("handle_cert")).leaf = true
    entry({"api", "file", "key"}, call("handle_key")).leaf = true
    entry({"api", "file", "info"}, call("handle_info")).leaf = true
    entry({"api", "file", "hashmap"}, call("handle_hashmap")).leaf = true
end

function handle_config()
    local cfgfile = "startup.conf"
    local cfgfiletmp = "startup.conf.web"
    local cfgpath = "/data/"
    local restore_cmd = "cat > " .. cfgpath .. cfgfiletmp
    local backup_cmd = "cat " .. cfgpath .. cfgfile .. " 2>>/dev/null"

    if luci.http.getenv('REQUEST_METHOD') == 'POST' then
        local fp
        luci.http.setfilehandler(function(meta, chunk, eof)
            if not fp then fp = io.popen(restore_cmd, "w") end
            if chunk then fp:write(chunk) end
            if eof then
                fp:close()
                luci.sys.exec("cd " .. cfgpath .. " && dos2unix " .. cfgfiletmp .. " && mac2unix " .. cfgfiletmp)
                luci.sys.exec("cd " .. cfgpath .. " && mv " .. cfgfiletmp .. " " .. cfgfile)
            end
        end)
        luci.http.formvalue() -- setfilehandler take effect after formvalue
        luci.http.prepare_content("application/json")
        luci.http.write_json({hdr = {code = 0, message = 'ok', type = 'success'}})

    end
    if luci.http.getenv('REQUEST_METHOD') == 'GET' then
        local reader = srvdb.ltn12_popen(backup_cmd)
        local sys_info = srvdb.getsysinfo()
        local host = luci.http.getenv('HTTP_HOST') or "NULL"
        luci.http.header('Content-Disposition', 'attachment; filename="backup-%s-%s-%s"' % {sys_info["hostname"] or luci.sys.hostname(), host, cfgfile})
        luci.http.prepare_content("application/x-targz")
        luci.ltn12.pump.all(reader, luci.http.write)
    end
end

local image_tmp = "/swupgrade/bin/firmware.img"
function handle_image()
    if luci.http.getenv('REQUEST_METHOD') ~= 'POST' then return end
    luci.sys.exec("mkdir -p /swupgrade/bin/")
    local fp
    luci.http.setfilehandler(function(meta, chunk, eof)
        if not fp then fp = io.open(image_tmp, "w") end
        if chunk then fp:write(chunk) end
        if eof then fp:close() end
    end)
    luci.http.formvalue() -- setfilehandler take effect after formvalue
    luci.http.prepare_content("application/json")
    luci.http.write_json({hdr = {code = 0, message = 'ok', type = 'success'}})
end

local scriptfile = '/usr/bin/webupgrade.sh'
local progressfile = '/tmp/luci.upgrade.process'
function writeProgress(progress, total) luci.sys.exec("echo " .. progress .. " " .. total .. " > " .. progressfile) end

function getProgressTotal()
    local platform = mydb.getdevplatform()
     if platform == "AC5" then
        return 4
    elseif platform == "LITE" then
        return 18
    else
        return 12
    end
end

function readProgress()
    local s = luci.sys.exec('cat ' .. progressfile)
    local val = string.split(s, ' ')
    local progress = val[1]
    local total = val[2]
    progress = progress and tonumber(progress) or 0
    total = total and tonumber(total) or getProgressTotal()
    return progress, total
end

function handle_progress()
    local type = luci.http.formvalue('type')
    if type == 'start' then
        luci.sys.exec(scriptfile .. " start >/dev/null")
        local progress, total = readProgress()
        progress = 0
        writeProgress(progress, total)
        return luci.http.write_json({hdr = {code = 0, message = 'ok', type = 'success'}, result = {progress = progress, total = total}})
    end

    local state = luci.sys.exec(scriptfile .. " running")
    local progress, total = readProgress()
    progress = progress + 1
    if state == '' then
        total = progress
    else
        if total <= progress then total = progress + 1 end
    end
    writeProgress(progress, total)

    if progress == total then
        local state = luci.sys.exec(scriptfile .. " result")
        if string.match(state, 'ko') then
            luci.http.write_json({hdr = {code = 1000, message = 'System upgrade failed', type = 'error'}, result = {progress = progress, total = total}})
            return
        end
    end

    luci.http.prepare_content("application/json")
    luci.http.write_json({hdr = {code = 0, message = 'ok', type = 'success'}, result = {progress = progress, total = total}})
end

function handle_package()
    if luci.http.getenv('REQUEST_METHOD') ~= 'POST' then return end
    local pkgdir = '/tmp/pkg/'
    local datadir = '/data/'
    luci.sys.exec("mkdir -p " .. pkgdir)
    local pkgtmppath = pkgdir .. 'pkgtmp'
    local fp
    luci.http.setfilehandler(function(meta, chunk, eof)
        if not fp then fp = io.open(pkgtmppath, "w") end
        if chunk then fp:write(chunk) end
        if eof then fp:close() end
    end)
    local params = luci.http.formvalue() -- setfilehandler take effect after formvalue
    local pkgpath = ""
    if params['name'] and params['name'] == 'dkweb' then
        pkgpath = pkgdir .. params['name'] .. ".tar"
        luci.sys.exec("mv  " .. pkgtmppath .. " " .. pkgpath)
        luci.sys.exec("/usr/bin/dkweb.sh " .. pkgpath)
    elseif params['name'] and params['name'] == 'data' then
        pkgpath = pkgdir .. params['name'] .. ".zip"
        luci.sys.exec("mv  " .. pkgtmppath .. " " .. pkgpath)
        luci.sys.exec("swupgrade data " .. pkgpath)
    else
        luci.http.prepare_content("application/json")
        luci.http.write_json({hdr = {code = 1000, message = 'Invalid file', type = 'fail'}})
    end

    luci.http.prepare_content("application/json")
    luci.http.write_json({hdr = {code = 0, message = 'ok', type = 'success'}})
end

function handle_cert()
    local certfile = "cert.pem"

    local fp
    luci.http.setfilehandler(function(meta, chunk, eof)
        if not meta then return end
        if not fp then fp = io.popen("cat >> /etc/http/" .. meta.name, "w") end
        if chunk then fp:write(chunk) end
        if eof then fp:close() end
    end)

    local upload = luci.http.formvalue("file")
    if upload and #upload > 0 then luci.sys.exec("/usr/bin/certmgmt.sh upgrade cert") end
end

function handle_key()
    local keyfile = "key.pem"

    local fp
    luci.http.setfilehandler(function(meta, chunk, eof)
        if not meta then return end
        if not fp then fp = io.popen("cat >> /etc/http/" .. meta.name, "w") end
        if chunk then fp:write(chunk) end
        if eof then fp:close() end
    end)

    local upload = luci.http.formvalue("file")
    if upload and #upload > 0 then luci.sys.exec("/usr/bin/certmgmt.sh upgrade key") end
end

function check_disk(name, path)
    local validDisk = {["/"] = "Rootfs", ["/var"] = "Log", ["/data"] = "Config"}
    if path == '/' and name ~= 'rootfs' then return nil end
    return validDisk[path]
end

function handle_info()
    luci.http.prepare_content("application/json")
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")

        local oper = params['oper'] or ""
        if oper == 'clean' then luci.sys.exec("cd /var/log/ && rm -f syslog.* all.* && echo > syslog && echo > all") end

        if oper == 'swap' then luci.sys.exec("swupgrade swap-images") end

        if oper == 'revert' then luci.sys.exec("/usr/bin/certmgmt.sh revert") end

        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    -- fs
    local args = {}
    local fsarray = {}
    local linestr = luci.sys.exec("df | grep -E -v '^File'")
    for v in string.gmatch(linestr, "[%S]+") do table.insert(args, v) end
    for i = 1, #args, 6 do
        if check_disk(args[i], args[i + 5]) then
            table.insert(fsarray, {name = check_disk(args[i], args[i + 5]), used = tonumber(string.match(args[i + 2], "%d+")), avail = tonumber(string.match(args[i + 3], "%d+"))})
        end
    end

    if (#args) % 6 ~= 0 then fsarray = {} end

    -- cleanopts
    local cleanopts = {}

    -- images
    local images = {}
    images[1] = {name = "active", state = "active"}
    images[2] = {name = "standby", state = "standby"}
    luci.sys.exec("swupgrade show-images /tmp/active.txt /tmp/standby.txt")
    local swap = luci.sys.exec("cat /tmp/active.txt /tmp/standby.txt 2>>/dev/null")
    swap = string.split(swap, '\n')
    images[1]['swver'], images[1]['releasedate'], images[2]['swver'], images[2]['releasedate'] = swap[1], swap[2], swap[3], swap[4]

    -- cert
    local cert = luci.sys.exec("/usr/bin/certmgmt.sh read && echo -n 1 || echo -n 0")

    local data = {fs = tools.array_check(fsarray), cleanopts = tools.array_check(cleanopts), images = tools.array_check(images), cert=tools.bool_trans(cert)}
    luci.http.write_json({hdr = {code = 0, message = 'ok', type = 'success'}, result = data})
end

function readFile(path)
    local fp = io.open(path, "r")
    if fp == nil then return nil end
    local content = fp:read("*a")
    fp:close()
    return content
end

function writeFile(path, content)
    local fp = io.open(path, "w")
    if fp == nil then return false end
    fp:write(content)
    fp:close()
    return true
end

function handle_hashmap()
    luci.http.prepare_content("application/json")
    local dir = "/data/dkweb/"
    luci.sys.exec("mkdir -p " .. dir)
    if luci.http.getenv("REQUEST_METHOD") == "POST" then
        local params = json.decode(luci.http.content())
        assert(type(params) == "table", "params is error")
        assert(type(params["file"]) == "string" and (string.find(params["file"], "/") == nil), "params is error")
        local path = dir .. params["file"]
        local content = readFile(path) or "[]"
        local map = json.decode(content) or {}
        if params['oper'] == 'del' then
            map[params["key"]] = nil
        else
            map[params["key"]] = params["info"]
        end
        writeFile(path, json.encode(map))
        return luci.http.write_json({hdr = {code = 0, message = "ok", type = "success"}})
    end

    local params = luci.http.formvalue() -- setfilehandler take effect after formvalue
    assert(type(params) == "table" and params['file'], "params is error")
    local path = dir .. params["file"]
    local content = readFile(path) or "[]"
    local map = json.decode(content) or {}
    local data
    if params["key"] and #params["key"] > 0 then
        data = map[params["key"]] or {}
    else
        data = map
    end
    luci.http.write_json({hdr = {code = 0, message = 'ok', type = 'success'}, result = data})
end
