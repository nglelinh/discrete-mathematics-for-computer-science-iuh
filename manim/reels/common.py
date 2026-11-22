"""Cấu hình và hàm dùng chung cho các reel Manim 9:16 (1080x1920, không nhạc)."""
from manim import *
import numpy as np

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9      # 1 đơn vị = 120 px
config.frame_height = 16
config.background_color = "#0e0e10"

GOLD = "#f5c542"
DIM = "#8a8d93"
RED = "#ff6b6b"
BLUE = "#6cb6ff"
CELL = "#1a1b20"
FONT = "DejaVu Sans"
CAP_Y = 6.3      # vị trí phụ đề (vùng an toàn: |x| <= 4, -6.5 <= y <= 6.8)


def cap(text, size=36, color=WHITE):
    t = Text(text, font=FONT, font_size=size, color=color)
    if t.width > 8.0:
        t.scale_to_fit_width(8.0)
    return t.move_to([0, CAP_Y, 0])


def swap_cap(scene, old, new, rt=0.45):
    scene.play(ReplacementTransform(old, new), run_time=rt)
    return new


def gold_digits(num_mobj, text, ref):
    """Tô vàng các ký tự đầu của `text` trùng với `ref`."""
    match = 0
    for a, b in zip(text, ref):
        if a != b:
            break
        match += 1
    for i, ch in enumerate(num_mobj.submobjects):
        ch.set_color(GOLD if i < match else WHITE)


# ---------- Hàm dùng thêm cho các reel dài (2026-11) ----------
GREEN = "#6bd68a"


def para(text, size=30, color=WHITE, y=0.0, x=0.0, w=7.8, **kw):
    """Đoạn chữ (có thể nhiều dòng), tự thu nhỏ nếu rộng quá w."""
    m = Text(text, font=FONT, font_size=size, color=color, line_spacing=1.1, **kw)
    if m.width > w:
        m.scale_to_fit_width(w)
    return m.move_to([x, y, 0])


def wipe(scene, keep=(), rt=0.5):
    """Xoá mọi thứ trên màn hình trừ các đối tượng trong keep."""
    mobs = [m for m in scene.mobjects if m not in keep]
    if mobs:
        scene.play(*[FadeOut(m) for m in mobs], run_time=rt)


def bexpr(s, size=32, color=WHITE):
    """Biểu thức Boole: '~' đứng trước một chữ = phủ định, vẽ gạch ngang riêng trên chữ đó."""
    plain, neg_idx, gi, i = "", [], 0, 0
    while i < len(s):
        ch = s[i]
        if ch == "~":
            neg_idx.append(gi)
            i += 1
            continue
        plain += ch
        if not ch.isspace():
            gi += 1
        i += 1
    t = Text(plain, font=FONT, font_size=size, color=color)
    g = VGroup(t)
    if neg_idx:
        top = max(t[j].get_top()[1] for j in neg_idx) + 0.05 * size / 32
        for j in neg_idx:
            ch = t[j]
            inset = 0.14 * ch.width + 0.02 * size / 32
            g.add(Line([ch.get_left()[0] + inset, top, 0], [ch.get_right()[0] - inset, top, 0],
                       color=color, stroke_width=2.6 * size / 32))
    return g


def fitw(m, w=7.8):
    if m.width > w:
        m.scale_to_fit_width(w)
    return m
