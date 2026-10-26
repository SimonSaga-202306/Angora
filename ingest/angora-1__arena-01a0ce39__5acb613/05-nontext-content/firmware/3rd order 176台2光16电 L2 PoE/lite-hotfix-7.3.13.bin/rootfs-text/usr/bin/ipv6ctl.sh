#!/bin/bash
debugfile= #/tmp/ipv6ctl.txt

if [ -n "$debugfile" ]; then
    echo "=====================================================================================" >>$debugfile
    echo "INTERFACE=$INTERFACE, MODE=$MODE, ACCEPT_ROUTER=$ACCEPT_ROUTER, ENABLE_RA=$ENABLE_RA" >>$debugfile
fi
if [[ -z "$INTERFACE" || -z "$MODE" ]]; then
    if [ -n "$debugfile" ]; then echo "environment variables missing" >>$debugfile; fi
    exit 1
fi

set_default() {
    sysctl net.ipv6.conf.$INTERFACE.disable_ipv6=1
    sysctl net.ipv6.conf.$INTERFACE.autoconf=0
    sysctl net.ipv6.conf.$INTERFACE.forwarding=0
    sysctl net.ipv6.conf.$INTERFACE.accept_ra=0
    sysctl net.ipv6.conf.$INTERFACE.accept_ra_defrtr=0
}
set_static() {
    if [ -n "$ENABLE_RA" ]; then sysctl sysctl net.ipv6.conf.$INTERFACE.forwarding=1; fi
    sysctl net.ipv6.conf.$INTERFACE.disable_ipv6=0
}
set_slaac() {
    if [ -n "$ACCEPT_ROUTER" ]; then sysctl net.ipv6.conf.$INTERFACE.accept_ra_defrtr=1; fi
    sysctl net.ipv6.conf.$INTERFACE.accept_ra=1
    sysctl net.ipv6.conf.$INTERFACE.autoconf=1
    sysctl net.ipv6.conf.$INTERFACE.disable_ipv6=0
}
set_dhcpv6() {
    if [ -n "$ACCEPT_ROUTER" ]; then sysctl net.ipv6.conf.$INTERFACE.accept_ra_defrtr=1; fi
    sysctl net.ipv6.conf.$INTERFACE.accept_ra=1
    sysctl net.ipv6.conf.$INTERFACE.disable_ipv6=0
}

case $MODE in
default)
    set_default
    ;;
static)
    set_default
    set_static
    ;;
enable_ra)
    set_ra 1
    ;;
disable_ra)
    set_ra 0
    ;;
slaac)
    set_default
    msg=$(set_slaac 2>&1)
    if [ -n "$debugfile" ]; then echo "$msg" >>$debugfile; fi
    ;;
dhcpv6)
    set_default
    msg=$(set_dhcpv6 2>&1)
    if [ -n "$debugfile" ]; then echo "$msg" >>$debugfile; fi
    ;;
*) #echo "Please make sure the option is start/stop."
    if [ -n "$debugfile" ]; then echo "invalid mode" >>$debugfile; fi
    exit 1
    ;;
esac
