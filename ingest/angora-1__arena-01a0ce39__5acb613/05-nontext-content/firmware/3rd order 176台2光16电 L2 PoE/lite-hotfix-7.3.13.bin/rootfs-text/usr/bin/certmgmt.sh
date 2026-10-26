#!/bin/sh

opt=${2:-"all"}

cust_dir="/data/customize/http/"
cert_dir="/etc/http/"
cert_file="cert.pem"
key_file="key.pem"
tmp_file="file"

back_dir="/data/backcert/"
back_certdef_file="certdef.pem"
back_keydef_file="keydef.pem"
back_certupgrade_file="certupgrade.pem"
back_keyupgrade_file="keyupgrade.pem"

download_path=${cert_dir}${tmp_file}
running_cert_path=${cert_dir}${cert_file}
running_key_path=${cert_dir}${key_file}
back_certdef_path=${back_dir}${back_certdef_file}
back_keydef_path=${back_dir}${back_keydef_file}
back_certupgrade_path=${back_dir}${back_certupgrade_file}
back_keyupgrade_path=${back_dir}${back_keyupgrade_file}

install() {
    # update back_certdef_path
    if [ -e ${cust_dir}${cert_file} ] && [ -e $back_certdef_path ]; then
        rm $back_certdef_path >/dev/null
        cp ${cust_dir}${cert_file} $back_certdef_path
    fi

    # update back_keydef_path
    if [ -e ${cust_dir}${key_file} ] && [ -e $back_keydef_path ]; then
        rm $back_keydef_path >/dev/null
        cp ${cust_dir}${key_file} $back_keydef_path
    fi

    # update running_cert_path
    if [ -e $back_certupgrade_path ]; then
        cp $back_certupgrade_path $running_cert_path >/dev/null
    elif [ -e ${cust_dir}${cert_file} ]; then
        cp ${cust_dir}${cert_file} $running_cert_path >/dev/null
    fi

    # update running_key_path
    if [ -e $back_keyupgrade_path ]; then
        cp $back_keyupgrade_path $running_key_path >/dev/null
    elif [ -e ${cust_dir}${key_file} ]; then
        cp ${cust_dir}${key_file} $running_key_path >/dev/null
    fi
}

upgrade() {
    if [ ! -d $back_dir ]; then
        mkdir $back_dir || exit 1
    fi

    if [ ! -e $download_path ]; then
        echo "The upgrade file is missing."
        exit 1
    fi

    #backup file
    if [ ! "$opt" = "cert" ] && [ ! "$opt" = "key" ]; then
        echo "Please make sure the option is cert/key."
        exit 1
    fi

    echo "Upgarde ${opt} file."

    if [ ! -e $back_certdef_path ] || [ ! -e $back_keydef_path ]; then
        [ -e $back_certdef_path ] && rm $back_certdef_path >/dev/null
        [ -e $back_keydef_path ] && rm $back_keydef_path >/dev/null

        cp $running_cert_path $back_certdef_path #Backup def file only once before revert
        cp $running_key_path $back_keydef_path #Backup def file only once before revert
    fi

    if [ "$opt" = "cert" ]; then
        mv $download_path $back_certupgrade_path #backup upgrade file
    else
        mv $download_path $back_keyupgrade_path #backup upgrade file
    fi    

    install
}

revert() {
    [ -e $back_certupgrade_path ] && rm $back_certupgrade_path >/dev/null
    if [ -e $back_certdef_path ]; then
        [ -e $running_cert_path ] && rm $running_cert_path >/dev/null
        mv $back_certdef_path $running_cert_path
    fi

    [ -e $back_keyupgrade_path ] && rm $back_keyupgrade_path >/dev/null
    if [ -e $back_keydef_path ]; then
        [ -e $running_key_path ] && rm $running_key_path >/dev/null
        mv $back_keydef_path $running_key_path
    fi

    install
}

read() {
    if [ -e $back_certdef_path ] || [ -e $back_keydef_path ]; then
        exit 0
    fi

    exit 1
}

if [ "$1" = "install" ]; then
    install
elif [ "$1" = "upgrade" ]; then
    upgrade
elif [ "$1" = "revert" ]; then
    revert
elif [ "$1" = "read" ]; then
    read
else
    echo "Please make sure the option is install/upgrade/revert/read."
fi
