#!/bin/bash
# usage: show.sh <video-stem> <file.py> : in mốc phụ đề và chữ hiển thị chính
cd "$(dirname "$0")/.."
python3 - "$1" <<'PY'
import json,sys
d=json.load(open(f'media/vo_cache/probes/{sys.argv[1]}.json')); print(d['duration'])
cs=d['captions']
for i,(t,c) in enumerate(cs):
    end=cs[i+1][0] if i+1<len(cs) else d['duration']
    print(f'{t:7.2f}-{end:7.2f} ({end-t:5.1f}s) {c}')
PY
grep -nE 'para\(|Text\(' "$2" | grep -vE 'font_size=(1[0-9]|2[0-6])\b' | sed -E 's/font=FONT, //; s/^([0-9]+): +/\1 /' | cut -c1-150
