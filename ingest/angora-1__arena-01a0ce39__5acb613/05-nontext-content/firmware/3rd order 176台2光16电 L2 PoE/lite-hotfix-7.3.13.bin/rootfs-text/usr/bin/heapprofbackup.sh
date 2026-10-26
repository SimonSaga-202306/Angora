#!/bin/bash

mkdir -p /var/heap/backup/
inotifywait -m --format '%w %f' -e close_write /var/heap | while read dir file
do
    FILECHANGE=${dir}${file}
    echo "backup file $FILECHANGE"
    gzip -c $FILECHANGE > /var/heap/backup/${file}.gz
    rm $FILECHANGE
done

