#!/usr/bin/env bash
# make_sheet.sh STILLS_DIR OUT.png [COLS] — contact sheet via ffmpeg tile
set -euo pipefail
d="$1"; out="$2"; cols="${3:-5}"
n=$(ls "$d"/*.png | wc -l | tr -d ' ')
rows=$(( (n + cols - 1) / cols ))
ffmpeg -y -v error -pattern_type glob -i "$d/*.png" \
  -vf "scale=384:-1,tile=${cols}x${rows}:margin=4:padding=4" "$out"
echo "$out: $n stills, ${cols}x${rows}"
