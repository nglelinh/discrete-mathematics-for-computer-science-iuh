# Reel Manim (video dọc 9:16)

Các video ngắn 20–30 giây (1080×1920, không nhạc) minh hoạ bài học bằng [Manim Community](https://www.manim.community/).
Phong cách chung: nền tối, phụ đề tiếng Việt, vùng an toàn |x| ≤ 4, |y| ≤ 6,5 (khung 9×16 đơn vị). Cấu hình và hàm dùng chung nằm trong `common.py`.

## Cài đặt
```bash
python3 -m venv venv && . venv/bin/activate
pip install manim          # cần LaTeX (texlive-latex-extra, texlive-science, dvisvgm), ffmpeg và font DejaVu Sans
```

## Render
```bash
cd manim/reels
manim -qh handshake.py Handshake    # -> media/videos/handshake/1920p60/Handshake.mp4
ffmpeg -i media/videos/handshake/1920p60/Handshake.mp4 -c:v libx264 -crf 26 -preset slow \
  -pix_fmt yuv420p -movflags +faststart -an handshake-lemma.mp4
```
File nén đặt vào `public/videos/reels/` và nhúng vào bài bằng thẻ `<video>` (xem bài 07-04).

## Thêm nhạc (tuỳ chọn)
```bash
ffmpeg -i out.mp4 -i music.mp3 -map 0:v -map 1:a -c:v copy -c:a aac -shortest out_music.mp4
```

## Danh sách
| File | Scene | Video | Bài |
|---|---|---|---|
| `pascal_pi.py` | `PascalPi` | `pascal-to-pi.mp4` | 07-04 |
| `handshake.py` | `Handshake` | `handshake-lemma.mp4` | 12-01 |
| `konigsberg.py` | `Konigsberg` | `konigsberg-bridges.mp4` | 12-04 |
| `fibonacci.py` | `Fibonacci` | `fibonacci-golden-ratio.mp4` | 10-02 |
| `euclid.py` | `Euclid` | `euclid-gcd-tiling.mp4` | 15-01 |
| `cardioid.py` | `Cardioid` | `modular-times-table.mp4` | 15-02 |
| `derangement.py` | `Derangement` | `derangement-one-over-e.mp4` | 11-04 |
| `graycode.py` | `GrayCode` | `gray-code-cube.mp4` | 13-04 |
| `pigeonhole.py` | `Pigeonhole` | `pigeonhole-square.mp4` | 08-01 |
| `dnf_cnf.py` | `DnfCnf` | `dnf-cnf-normal-forms.mp4` | 01-04 |
