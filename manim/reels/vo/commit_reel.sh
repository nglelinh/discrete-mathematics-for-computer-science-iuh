#!/bin/bash
# usage: commit_reel.sh <video.mp4> "<message>" [extra files...]   (chạy ở gốc repo)
set -e
cd "$(dirname "$0")/../../.."
v="public/videos/reels/$1"; msg="$2"; shift 2
ffprobe -v error -show_entries stream=codec_type -of csv=p=0 "$v" | grep -q audio || { echo "NO AUDIO in $v"; exit 2; }
git add "$v" "$@"
hits=$(git diff --cached | grep -acE 'AIz[a]|GEMINI_API_KEY[=]|xi-api-ke[y]|sk_[A-Za-z0-9]{8}' || true)
[ "$hits" = "0" ] || { echo "SECRET PATTERN HITS: $hits"; git reset -q; exit 3; }
git diff --cached --stat
git commit -q -m "$msg"
git pull --rebase --autostash -q origin main
git push -q origin HEAD:main
git log --oneline -1
