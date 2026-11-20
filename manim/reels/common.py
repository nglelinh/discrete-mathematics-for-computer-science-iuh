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
    return Text(text, font=FONT, font_size=size, color=color).move_to([0, CAP_Y, 0])


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
