#!/bin/sh

watch_start() {
	ps -e|grep coreanalyser |grep -v grep
	if [ $? -ne 0 ]
	then
		echo "start core analyser..."
		coreanalyser.sh &
	else
		echo "core analyser is already runing....."
	fi
}

watch_stop() {
	echo "stop core analyser..."
	pkill coreanalyser.sh
	pkill inotifywait
}

watch_restart() {
	watch_stop
	watch_start
}

if [ "$1" = "start" ]; then
	watch_start
elif [ "$1" = "stop" ]; then
	watch_stop
elif [ "$1" = "restart" ]; then
	watch_restart
else
	watch_start
	#echo "Please make sure the option is start/stop/restart."
fi

