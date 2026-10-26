#! /bin/sh

if getent group root; then
    echo ""
else
    cp /etc/group- /etc/group
    cp /etc/passwd- /etc/passwd
    cp /etc/shadow- /etc/shadow
    echo "System restart for root user is missing." 
    sync
    sleep 1 
    reboot &
    sleep 30 
fi

if grep root /etc/passwd; then
    echo ""
else
    cp /etc/group- /etc/group
    cp /etc/passwd- /etc/passwd
    cp /etc/shadow- /etc/shadow
    echo "System restart for root user is missing."
    sync
    sleep 1
    reboot &
    sleep 30 
fi
