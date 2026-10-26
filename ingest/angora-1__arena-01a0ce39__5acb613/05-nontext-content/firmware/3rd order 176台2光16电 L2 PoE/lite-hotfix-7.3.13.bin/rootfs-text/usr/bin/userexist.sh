#! /bin/bash

die() { echo "$*" 1>&2 ; exit 1; }

if [ $# -ne 2 ]; then
    die "invalid arguments! usage $0 {username} {enc_pass|plain_pass}"
fi
name=$1
pass=$2
# echo "checking user $name pass $pass"
if [ "${pass:0:1}" == "$" ]; then
    cat /etc/shadow | grep "$name:$pass:" >/dev/null && echo "true" || die "false"
else
    spass=$(cat /etc/shadow | grep "$name:") # abc:$1$nVoAA4a0$G/iaScm9mZ.urRHbDawgb/::0:99999:7:::
    if [ -z "$spass" ]; then
        die "false"
    fi
    spass=${spass#*$name:} # $1$nVoAA4a0$G/iaScm9mZ.urRHbDawgb/::0:99999:7:::
    spass=${spass%%:*} # $1$nVoAA4a0$G/iaScm9mZ.urRHbDawgb/
    salt=${spass%\$*} # $1$nVoAA4a0
    newpass=$(perl -e "print crypt('$pass','$salt')")
    # echo "spass=$spass" && echo "npass=$newpass"
    [ "$spass" == "$newpass" ] && echo "true" || die "false"
fi
