#!/usr/bin/env bash
# fetch_vol1_pages.sh FIRST LAST -> $PM_WORK/scan/djvuN.jpg: Commons' own 1920 px renders of the 1910 Vol I scan
# (djvu page = printed page + 22). These are the images the Vol I readers and judges saw; Commons caps its
# thumbnails at 1920 px. The crop check renders the DjVu at native resolution instead (bs_check.py).
set -u
W=${PM_WORK:-work}; mkdir -p "$W/scan"
F='Russell%2C_Whitehead_-_Principia_Mathematica%2C_vol._I%2C_1910.djvu'
for ((n=$1; n<=$2; n++)); do
  [[ -s $W/scan/djvu$n.jpg ]] && continue
  curl -sS -A 'pm-text-audit/0.1 (research)' -o "$W/scan/djvu$n.jpg" -w "$n %{http_code} %{size_download}\n" \
    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/$F/page$n-1920px-$F.jpg"
  sleep 1
done
