#!/usr/bin/env bash
# render.sh N -> scan2v/djvuN.jpg at native resolution (Vol II 1912, Commons)
set -u
W=${PM_WORK:-work}; o="$W/scan2v/djvu$1.jpg"; [[ -s $o ]] && exit 0
t=$(mktemp --suffix=.pnm); ddjvu -format=pnm -page="$1" "${DJVU:-$W/djvu/vol2.djvu}" "$t" && python3 -c "from PIL import Image;import sys;Image.open(sys.argv[1]).convert('RGB').save(sys.argv[2],quality=90)" "$t" "$o.part.jpg" && mv "$o.part.jpg" "$o"; rm -f "$t"
