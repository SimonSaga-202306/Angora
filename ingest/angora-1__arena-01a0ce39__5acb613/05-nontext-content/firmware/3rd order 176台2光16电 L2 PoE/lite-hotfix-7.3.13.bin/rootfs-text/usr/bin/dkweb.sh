#!/bin/sh

work_dir=/www
ignore_paths="cgi-bin luci-static . /"
pkg_path=${1:-"/tmp/pkg/dkweb.tar"}
abs_pkgpath="$(cd -P $(dirname $pkg_path) && pwd)/$(basename $pkg_path)" # use the physical directory structure without following symbolic links

get_filesize() {
    echo "$(stat -c "%s" $1)"
}
check() {
    maxsize=$((1024 * 1024 * 50)) # 50M, avoid an image uploaded
    filesize=$(get_filesize "$pkg_path")
    if [ $filesize -gt $maxsize ]; then
        echo "[dkweb] invalid pkg size $filesize" >&2 && exit 1
    fi
}

clear() {
    cd $work_dir || exit 1
    for f in $(ls); do
        $(echo "$ignore_paths" | grep -wq "$f")
        if [ $? -ne 0 ]; then
            rm -rf $f
        fi
    done
}
deploy() { cd $work_dir && tar -xf $abs_pkgpath; }

check && clear && deploy
