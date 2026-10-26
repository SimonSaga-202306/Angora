#!/bin/sh
# attention for permissions

cust_dir=/data/customize/
www_dir=/www
cert_dir=/etc/http

[ -e /usr/bin/resource.lua ] && lua /usr/bin/resource.lua &
[ -e /usr/bin/certmgmt.sh ] && /usr/bin/certmgmt.sh install

cd $cust_dir 2>/dev/null || exit 1
[ -e logo.png ] && cp -a logo.png $www_dir/logo_light.png && cp -a logo.png $www_dir/logo_dark.png && chmod 666 $www_dir/logo_*.png # compatible for old luci web's logo customization
[ -e dkweb.tar ] && /usr/bin/dkweb.sh $cust_dir/dkweb.tar && rm -f dkweb.tar
[ -e www/zh_CN.json ] && rm -f www/zh_CN.json
[ -e www/en_US.json ] && rm -f www/en_US.json
[ -d www ] && cp -a www/* $www_dir/
