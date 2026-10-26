#!/bin/sh

do_analyse() {
	logname=/var/log/crash.log
	cd /var/core/
	filelist=`ls | grep core-`
	for corename in $filelist
	do
		procname=${corename#*-}
		procname=${procname%%-*}
		echo "===============$corename($procname)===============" >> $logname
		gdb -q $procname $corename -ex "info f" -ex "info locals" -ex "thread apply all bt full 15" -ex "quit"  >> $logname 2>/dev/null
		echo "=====================================================\n"  >> $logname
		rm -f $corename
	done
}

do_analyse
while true #run indefinitely
do 
	inotifywait -e create /var/core
	do_analyse
done	

