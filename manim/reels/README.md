# Reel Manim (video dọc 9:16)

Các video ngắn 20–30 giây (1080×1920, không nhạc) minh hoạ bài học bằng [Manim Community](https://www.manim.community/).

## Cài đặt
```bash
python3 -m venv venv && . venv/bin/activate
pip install manim          # cần LaTeX (texlive) và ffmpeg
```

## Render
```bash
manim -qh pascal_pi.py PascalPi          # -> media/videos/pascal_pi/1920p60/PascalPi.mp4
ffmpeg -i PascalPi.mp4 -c:v libx264 -crf 26 -preset slow -pix_fmt yuv420p -movflags +faststart -an out.mp4
```
File nén đặt vào `public/videos/reels/` và nhúng vào bài bằng thẻ `<video>` (xem bài 07-04).

## Thêm nhạc (tuỳ chọn)
```bash
ffmpeg -i out.mp4 -i music.mp3 -map 0:v -map 1:a -c:v copy -c:a aac -shortest out_music.mp4
```

## Danh sách
| File | Scene | Bài |
|---|---|---|
| `pascal_pi.py` | `PascalPi` | 07-04 |
