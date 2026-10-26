#! /bin/sh

maxsize=$((1024 * 1024 * 10)) # 10M
get_filesize() {
    echo "$(stat -c "%s" $1)"
}

filesize=$(get_filesize "/var/log/all")
if [ $filesize -gt $maxsize ]; then
    # echo "$filesize > $maxsize"
    /usr/sbin/logrotate -f /etc/logrotate.d/rsyslog
fi
