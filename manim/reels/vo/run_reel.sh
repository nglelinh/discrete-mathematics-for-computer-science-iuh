#!/bin/bash
# usage: run_reel.sh <reel> <video.mp4> "<tên hiển thị>"   (mux + kiểm tra + commit + push)
cd "$(dirname "$0")/.."
python3 vo/dm_vo.py mux "$1" | tail -2 || exit 1
ffprobe -v error -show_entries stream=codec_type,duration -of csv=p=0 "../../public/videos/reels/$2" | tr '\n' ' '; echo
vo/commit_reel.sh "$2" "Reel $3: thêm lời dẫn tiếng Việt" manim/reels/vo/narration_dm.py manim/reels/vo/fetch_el.py manim/reels/vo/run_reel.sh manim/reels/vo/probe.py manim/reels/vo/dm_vo.py | tail -1
