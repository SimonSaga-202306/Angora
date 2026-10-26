#!/bin/sh

tgtdir=${1:-"."}
[ ! -d $tgtdir ] && echo "dir $tgtdir not found" >&2 && exit 0

#diag
export TERM=vt100

cp "/data/startup.conf" $tgtdir/ 2>>/dev/null
df >$tgtdir/flash.txt
free -m >$tgtdir/cache.txt
top -bn2 -d1 >$tgtdir/cpu.txt
echo | imish -e 'show version' >$tgtdir/version.txt
echo | imish -e 'show running-config' >$tgtdir/running.conf
echo | imish -e 'show interface brief' >$tgtdir/ifstatus.txt
echo | imish -e 'show counters interface' >$tgtdir/counters.txt
