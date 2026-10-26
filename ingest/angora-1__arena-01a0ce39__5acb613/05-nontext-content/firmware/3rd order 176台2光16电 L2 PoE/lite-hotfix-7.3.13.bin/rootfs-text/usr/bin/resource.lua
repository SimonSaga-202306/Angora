
local file_cpuinfo  = "/proc/cpuinfo";
local file_stat     = "/proc/stat";
local file_loadavg  = "/proc/loadavg";
local file_meminfo  = "/proc/meminfo";
local file_uptime  = "/proc/uptime";
local file_resource = "/tmp/resource.txt";

function get_cpu_num()
    local num = 0
    local fd = io.open(file_cpuinfo, "r")
    if fd then
        while true do
            local linestr = fd:read()
            if not linestr then
                break
            else
                num = linestr:match("processor") and (num + 1) or num
            end
        end

        fd:close()
    end

    return num
end

function get_cpu_usage(interval)
    local cpu_total1 , cpu_total2 = 0, 0
    local cpu1, cpu2 = {}, {}
    local fd = io.open(file_stat, "r")
    if fd then
        local linestr = fd:read() or ""
        for v in string.gmatch(linestr, "[^%s]+") do
            table.insert(cpu1, v)
        end

        for k = 2, #cpu1 do
            cpu_total1 = cpu_total1 + cpu1[k]
        end

        fd:close()
    end

    os.execute("sleep " .. interval)

    fd = io.open(file_stat, "r")
    if fd then
        local linestr = fd:read() or ""
        for v in string.gmatch(linestr, "[^%s]+") do
            table.insert(cpu2, v)
        end

        for k = 2, #cpu2 do
            cpu_total2 = cpu_total2 + cpu2[k]
        end

        fd:close()
    end

    local total = cpu_total2 - cpu_total1 + 1;                       -- +1 to fix divide 0 issue
    local idle = cpu2[5] - cpu1[5];
    local difference = math.floor( ( 100 - idle * 100 / total ) * 100 )  / 100;

    local fd = io.open(file_loadavg, "r")
    local loadavg
    if fd then
        local linestr = fd:read()
        loadavg = linestr or ""

        fd:close()
    end

    return {difference, loadavg}
end

function get_mem_usage()
    local fd = io.open(file_meminfo, "r")
    local mem = {}
    if fd then
        for i = 1, 2 do
            local linestr = fd:read() or ""
            mem[i] = string.match(linestr, "[%d]+") or "0"
        end

        fd:close()
    end

    return mem
end

function get_dev_uptime()
    local fd = io.open(file_uptime, "r")
    local uptime = 0
    if fd then
        local linestr = fd:read() or ""
        uptime = string.match(linestr, "[%d%.]+ [%d%.]+") or ""

        fd:close()
    end

    return uptime
end

function write_resource(data)
    local fd = io.open(file_resource, "w")
    if fd then
        local linestr = fd:write(data .. "\n")

        fd:close()
    end
end

local cpu_num = get_cpu_num()
while true do
    local data = cpu_num
    local uptime = ""
    for _, v in pairs(get_cpu_usage(5)) do
        data = data .. " " .. v
    end

    for k, v in pairs(get_mem_usage()) do
        data = ((k == 1) and (data .. "\n") or (data .. " ")) .. v
    end

    uptime = get_dev_uptime()
    data = data .. "\n" .. uptime

    write_resource(data)
end
