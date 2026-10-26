#!/bin/sh

image_tmp="/swupgrade/bin/firmware.img"
upgradestatefile='/tmp/luci.upgrade.state'
start() {
    echo 'running' >$upgradestatefile
    sync
    /usr/bin/swupgrade main $image_tmp >/dev/null
    if [ $? -ne 0 ]; then
        echo 'ko' >$upgradestatefile
    else
        echo 'ok' >$upgradestatefile
    fi
}

running() {
    pidof swupgrade
}

result() {
    cat $upgradestatefile
}

if [ "$1" = "start" ]; then
    start &
elif [ "$1" = "running" ]; then
    running
elif [ "$1" = "result" ]; then
    result
else
    echo "Please make sure the option is start/running/result."
fi
