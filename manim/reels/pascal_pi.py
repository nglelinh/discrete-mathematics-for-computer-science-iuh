from manim import *
from math import comb, pi as PI, floor, log10, sqrt
import numpy as np

# 9:16 vertical, 1080x1920  (1 unit = 120 px)
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = "#0e0e10"

GOLD = "#f5c542"
DIM = "#8a8d93"
FONT = "DejaVu Sans"
PI_STR = "3.1415926536"

# ---- math, verified at import time ----
DENOMS = [comb(2 * k + 2, 3) for k in range(1, 6)]
assert DENOMS == [4, 20, 56, 120, 220]
for _k in range(1, 200):
    assert abs(4 / ((2*_k)*(2*_k+1)*(2*_k+2)) - (2/3)/comb(2*_k+2, 3)) < 1e-15

def S(k):
    s = 3.0
    for j in range(1, k + 1):
        s += (-1) ** (j + 1) * (2 / 3) / comb(2 * j + 2, 3)
    return s

KMAX = 2000
PART = [S(k) for k in range(KMAX + 1)]
ERR = [abs(p - PI) for p in PART]


def cap(text, size=34, color=WHITE):
    return Text(text, font=FONT, font_size=size, color=color)


class PascalPi(Scene):
    def construct(self):
        R = 0.32
        DX = sqrt(3) * R * 1.05
        DY = 0.5
        TOP = 0.95
        N = 12

        # ---------- Pascal's triangle ----------
        cells = {}
        rows = []
        for n in range(N + 1):
            row = VGroup()
            for k in range(n + 1):
                hexa = RegularPolygon(6, start_angle=PI / 2 if False else np.pi / 2,
                                      radius=R, color=DIM, stroke_width=1.6,
                                      fill_color="#1a1b20", fill_opacity=1)
                num = MathTex(str(comb(n, k)), font_size=26)
                if num.width > 0.5:
                    num.scale_to_fit_width(0.5)
                g = VGroup(hexa, num)
                g.move_to([(k - n / 2) * DX, TOP - n * DY, 0])
                cells[(n, k)] = g
                row.add(g)
            rows.append(row)

        title = cap("Tam giác Pascal", 44).move_to([0, 6.3, 0])
        self.add(title)
        self.play(LaggedStart(*[FadeIn(r, shift=DOWN * 0.15) for r in rows],
                              lag_ratio=0.22), run_time=3.0)
        ident = MathTex(r"\binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k}",
                        font_size=34).move_to([0, -6.2, 0])
        self.play(FadeIn(ident), run_time=0.5)

        # ---------- third diagonal ----------
        c2 = cap("Đường chéo thứ ba: C(n, 3)", 34).move_to([0, 6.3, 0])
        self.play(ReplacementTransform(title, c2), run_time=0.5)
        diag = [(n, 3) for n in range(3, N + 1)]
        self.play(*[cells[p][0].animate.set_fill(GOLD, 0.25).set_stroke(GOLD, 2.5)
                    for p in diag], run_time=1.0)
        evens = [(n, 3) for n in (4, 6, 8, 10, 12)]
        self.play(*[cells[p][0].animate.set_fill(GOLD, 0.9) for p in evens],
                  *[cells[p][1].animate.set_color(BLACK) for p in evens],
                  run_time=0.8)
        self.play(*[Indicate(cells[p], color=GOLD, scale_factor=1.25) for p in evens],
                  run_time=0.8)

        c3 = cap("Cách một số: C(2k + 2, 3)", 34, GOLD).move_to([0, 6.3, 0])
        self.play(ReplacementTransform(c2, c3), run_time=0.5)

        # ---------- series layout ----------
        head = MathTex(r"\pi=3+\tfrac{2}{3}\Big(")
        signs = ["", "-", "+", "-", "+"]
        terms = VGroup(*[
            MathTex((s if s else "") + r"\tfrac{1}{" + str(d) + "}")
            for s, d in zip(signs, DENOMS)])
        dots = MathTex(r"-\cdots")
        tail = MathTex(r"\Big)")
        series = VGroup(head, *terms, dots, tail).arrange(RIGHT, buff=0.18)
        series.scale_to_fit_width(7.9)
        series.move_to([0, 5.0, 0])
        self.play(FadeIn(head), FadeIn(tail), FadeIn(dots), run_time=0.6)

        # ---------- running sum + plot ----------
        L = ValueTracker(-1)  # log10 k ; < 0 means k = 0

        def kk():
            v = L.get_value()
            return 0 if v < 0 else min(KMAX, int(floor(10 ** v + 1e-6)))

        s_lab = MathTex(r"S_k=", font_size=40).move_to([-3.2, 3.35, 0])
        s_num = DecimalNumber(3.0, num_decimal_places=10, font_size=50)
        pi_ref = MathTex(r"\pi=3.14159\,26535\,89793\ldots", font_size=28, color=DIM)
        k_lab = MathTex(r"k=", font_size=34)
        k_num = Integer(0, font_size=34)

        def place_s():
            s_num.next_to(s_lab, DOWN, buff=0.15, aligned_edge=LEFT)
            pi_ref.next_to(s_num, DOWN, buff=0.2, aligned_edge=LEFT)
            k_lab.next_to(pi_ref, DOWN, buff=0.2, aligned_edge=LEFT)
            k_num.next_to(k_lab, RIGHT, buff=0.1)
        place_s()

        def s_upd(m):
            m.set_value(PART[kk()])
            txt = "%.10f" % PART[kk()]
            match = 0
            for a, b in zip(txt, PI_STR):
                if a == b:
                    match += 1
                else:
                    break
            for i, ch in enumerate(m.submobjects):
                ch.set_color(GOLD if i < match else WHITE)
            m.next_to(s_lab, DOWN, buff=0.15, aligned_edge=LEFT)
        s_num.add_updater(s_upd)
        k_num.add_updater(lambda m: (m.set_value(kk()), m.next_to(k_lab, RIGHT, buff=0.1)))

        axes = Axes(x_range=[0, 3.4, 1], y_range=[0, 10, 2],
                    x_length=3.5, y_length=1.9,
                    axis_config={"color": DIM, "stroke_width": 2, "include_ticks": True,
                                 "include_tip": False}).move_to([2.3, 2.75, 0])
        ax_t = MathTex(r"\log|S_k-\pi|", font_size=24, color=DIM).next_to(axes, UP, buff=0.08)
        ax_x = MathTex(r"\log k", font_size=24, color=DIM).next_to(axes, DOWN, buff=0.05).align_to(axes, RIGHT)

        def curve():
            n = kk()
            pts = [axes.c2p(log10(j), log10(ERR[j]) + 11) for j in range(1, n + 1)
                   if ERR[j] > 0]
            g = VGroup()
            if len(pts) >= 2:
                ln = VMobject(color=GOLD, stroke_width=3).set_points_as_corners(pts)
                g.add(ln)
            if pts:
                g.add(Dot(pts[-1], radius=0.07, color=GOLD))
            return g
        curve_m = always_redraw(curve)

        self.play(FadeIn(s_lab), FadeIn(s_num), FadeIn(pi_ref), FadeIn(k_lab),
                  FadeIn(k_num), FadeIn(axes), FadeIn(ax_t), FadeIn(ax_x), run_time=0.8)
        self.add(curve_m)

        # ---------- numbers fly into the series ----------
        c4 = cap("Chuỗi Nilakantha", 38, GOLD).move_to([0, 6.3, 0])
        self.play(ReplacementTransform(c3, c4), run_time=0.4)
        durs = [1.5, 1.1, 0.85, 0.65, 0.5]
        for i, (n, d) in enumerate(zip((4, 6, 8, 10, 12), DENOMS)):
            src = cells[(n, 3)][1]
            self.play(
                TransformFromCopy(src, terms[i]),
                Flash(cells[(n, 3)], color=GOLD, flash_radius=0.5, line_length=0.12),
                run_time=durs[i])
            self.play(L.animate.set_value(log10(i + 1)), run_time=durs[i] * 0.5,
                      rate_func=smooth)
        self.wait(0.3)

        # ---------- sprint to k = 2000 ----------
        c5 = cap("Hội tụ rất nhanh!", 38).move_to([0, 6.3, 0])
        self.play(ReplacementTransform(c4, c5), run_time=0.4)
        self.play(L.animate.set_value(log10(KMAX)), run_time=5.0,
                  rate_func=lambda t: t ** 1.6)
        self.wait(0.3)
        c6 = cap("Chữ số vàng: đã cố định", 34, GOLD).move_to([0, 6.3, 0])
        self.play(ReplacementTransform(c5, c6), run_time=0.4)
        self.play(Indicate(s_num, color=GOLD, scale_factor=1.08), run_time=1.0)
        c7 = cap("Từ tam giác Pascal ra π!", 38).move_to([0, 6.3, 0])
        self.play(ReplacementTransform(c6, c7), run_time=0.4)
        self.wait(1.5)
