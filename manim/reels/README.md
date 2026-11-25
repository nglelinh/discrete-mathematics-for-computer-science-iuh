# Reel Manim (video dọc 9:16)

Các video dọc từ 20 giây đến khoảng 4 phút rưỡi (1080×1920, không nhạc) minh hoạ bài học bằng [Manim Community](https://www.manim.community/).
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
Các reel `graycode`, `fibonacci`, `incl_excl`, `perm_comb`, `stars_bars`, `tree_traversal`, `huffman`, `relations` chỉ dùng `Text` (Unicode), không cần LaTeX.
File nén đặt vào `public/videos/reels/` và nhúng vào bài bằng thẻ `<video>` (xem bài 07-04).

## Thêm nhạc (tuỳ chọn)
```bash
ffmpeg -i out.mp4 -i music.mp3 -map 0:v -map 1:a -c:v copy -c:a aac -shortest out_music.mp4
```

## Danh sách
| File | Scene | Video | Bài |
|---|---|---|---|
| `pascal_pi.py` | `PascalPi` | `pascal-to-pi.mp4` (tiếng Việt, 4 phút 18 giây, có lời dẫn ElevenLabs) và `pascal-to-pi_en.mp4` (tiếng Anh) | 07-04 |
| `handshake.py` | `Handshake` | `handshake-lemma.mp4` | 12-01 |
| `konigsberg.py` | `Konigsberg` | `konigsberg-bridges.mp4` | 12-04 |
| `fibonacci.py` | `Fibonacci` | `fibonacci-binet.mp4` | 10-02 |
| `euclid.py` | `Euclid` | `euclid-gcd-tiling.mp4` | 15-01 |
| `cardioid.py` | `Cardioid` | `modular-times-table.mp4` | 15-02 |
| `derangement.py` | `Derangement` | `derangement-one-over-e.mp4` | 11-04 |
| `graycode.py` | `GrayCode` | `karnaugh-maps-gray-code.mp4` | 13-04 |
| `pigeonhole.py` | `Pigeonhole` | `pigeonhole-square.mp4` | 08-01 |
| `dnf_cnf.py` | `DnfCnf` | `dnf-cnf-normal-forms.mp4` | 01-04 |
| `induction.py` | `Induction` | `induction-dominoes.mp4` | 03-03 |
| `qm.py` | `Qm` | `quine-mccluskey.mp4` | 13-05 |
| `mst.py` | `Mst` | `mst-kruskal-prim.mp4` | 16-03 |
| `dijkstra.py` | `Dijkstra` | `dijkstra-shortest-path.mp4` | 17-01 |
| `nfa_dfa.py` | `NfaDfa` | `nfa-to-dfa-subset-construction.mp4` | 18-05 |
| `incl_excl.py` | `InclExcl` | `inclusion-exclusion.mp4` | 07-03, 11-03 |
| `perm_comb.py` | `PermComb` | `permutations-combinations.mp4` | 07-02 |
| `stars_bars.py` | `StarsBars` | `stars-and-bars.mp4` | 07-05 |
| `tree_traversal.py` | `TreeTraversal` | `tree-traversal.mp4` | 16-02 |
| `huffman.py` | `Huffman` | `huffman-coding.mp4` | 16-04 |
| `relations.py` | `Relations` | `equivalence-partial-order.mp4` | 05-03 |
| `cantor.py` | `Cantor` | `cantor-diagonal.mp4` | 04-03 |
| `pigeon_adv.py` | `PigeonAdv` | `pigeonhole-advanced.mp4` | 08-02 |
| `nonhom.py` | `NonHom` | `nonhomogeneous-recurrence.mp4` | 10-03 |
| `divide_conquer.py` | `DivideConquer` | `divide-and-conquer-master.mp4` | 10-04 |
| `bfs_dfs.py` | `BfsDfs` | `bfs-vs-dfs.mp4` | 12-04 |
| `big_o.py` | `BigO` | `big-o-growth.mp4` | 14-02 |
| `rsa_dh.py` | `Rsa` | `rsa-diffie-hellman.mp4` | 15-03 |

### Ghi chú về `pascal_pi.py`
- Chọn ngôn ngữ bằng biến môi trường: `REEL_LANG=vi manim -qh --disable_caching -o pascal_pi_vi pascal_pi.py PascalPi` (hoặc `REEL_LANG=en`). Cảnh chỉ dùng `Text` Unicode, không cần LaTeX.
- Nội dung: dựng tam giác Pascal, các đường chéo, lấy cách một số trên đường chéo thứ ba, chuỗi Nilakantha, chứng minh bằng tách phân thức và chuỗi Leibniz, tốc độ hội tụ. Đầu file có các `assert` kiểm tra mọi con số bằng numpy và mpmath.
- `vo_scripts_pascal_pi.py` chứa lời dẫn tiếng Việt theo từng mục và mốc thời gian để thu âm và ghép tiếng. Bản tiếng Việt đã có lời dẫn (ElevenLabs, giọng Trường, eleven_v3); `vo/pascal_pi_pads.json` thêm khoảng dừng cuối mục 3 và 5 để lời dẫn không tràn. Bản tiếng Anh vẫn không tiếng.
