--[[
LuCI - Lua Configuration Interface

Copyright 2008 Steven Barth <steven@midlink.org>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

$Id$
]] --
local sauth = require "luci.sauth"
local json = require "luci.json"
local mydb = require "luci.mydb"
local authapi = require "luci.authapi"

module("luci.controller.api.index", package.seeall)

function index()
    local root = node()
    if not root.target then
        root.target = alias("api")
        root.index = true
    end

    local page = node("api")
    page.target = firstchild()
    page.title = _("Administration")
    page.order = 10
    -- page.sysauth = "admin"
    -- page.sysauth_authenticator = "htmlauth"
    page.ucidata = true
    page.index = true

    -- Empty services menu to be populated by addons
    entry({"api", "services"}, firstchild(), _("Services"), 10).index = true
end
