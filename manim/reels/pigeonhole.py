from common import *
import random
from math import sqrt

SIDE = 2.0
SQ2 = sqrt(2)


def cell_of(p):
    return (int(p[0] >= 1), int(p[1] >= 1))


def trial(seed):
    rnd = random.Random(seed)
    pts = [(rnd.uniform(0.02, 1.98), rnd.uniform(0.02, 1.98)) for _ in range(5)]
    cells = {}
    for p in pts:
        cells.setdefault(cell_of(p), []).append(p)
    crowded = [v for v in cells.values() if len(v) >= 2]
    assert crowded                                    # nguyên lý Dirichlet: 5 > 4
    pair = None
    for v in crowded:
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                d = sqrt((v[i][0] - v[j][0]) ** 2 + (v[i][1] - v[j][1]) ** 2)
                assert d <= SQ2 + 1e-12
                if pair is None or d < pair[0]:
                    pair = (d, v[i], v[j])
    # khoảng cách nhỏ nhất của cả 5 điểm cũng ≤ √2
    allmin = min(sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2) for i, a in enumerate(pts) for b in pts[i+1:])
    assert allmin <= SQ2
    return pts, pair


for s in range(2000):
    trial(s)


class Pigeonhole(Scene):
    def construct(self):
        c = cap("Nguyên lý chuồng chim", 44)
        self.add(c)
        U = 2.1                      # 1 đơn vị toán = 1.8 đơn vị màn hình
        O = np.array([-U, 0.3, 0])   # góc dưới-trái hình vuông 2x2
        P = lambda p: O + np.array([p[0] * U, p[1] * U, 0])
        sq = Square(2 * U, color=WHITE, stroke_width=4).move_to(O + np.array([U, U, 0]))
        self.play(Create(sq), run_time=0.8)
        c = swap_cap(self, c, cap("Hình vuông 2 × 2 chia thành 4 ô", 34))
        v = Line(P((1, 0)), P((1, 2)), color=GOLD, stroke_width=3)
        h = Line(P((0, 1)), P((2, 1)), color=GOLD, stroke_width=3)
        self.play(Create(v), Create(h), run_time=0.9)
        cellrect = {}
        for cx in (0, 1):
            for cy in (0, 1):
                cellrect[(cx, cy)] = Square(U, stroke_width=0, fill_color=GOLD, fill_opacity=0).move_to(P((cx + 0.5, cy + 0.5)))
                self.add(cellrect[(cx, cy)])
        diag = DashedLine(P((0, 0)), P((1, 1)), color=DIM, stroke_width=3)
        dl = MathTex(r"\sqrt2", font_size=34, color=DIM).move_to(P((0.62, 0.34)) + np.array([0.0, 0.0, 0]))
        self.play(Create(diag), FadeIn(dl), run_time=0.8)
        info = Text("Trong một ô, hai điểm cách nhau ≤ √2", font=FONT, font_size=28, color=DIM).move_to([0, -0.5, 0])
        self.play(FadeIn(info), run_time=0.6)
        self.wait(0.5)
        self.play(FadeOut(diag), FadeOut(dl), run_time=0.3)

        c = swap_cap(self, c, cap("Đặt 5 điểm bất kỳ", 38, GOLD))
        cnt_txt = Text("5 điểm > 4 ô", font=FONT, font_size=36, color=GOLD).move_to([0, -1.7, 0])
        result_txt = None
        for t, seed in enumerate([7, 21, 33]):
            pts, (d, p1, p2) = trial(seed)
            dots = [Dot(P(p), radius=0.1, color=BLUE) for p in pts]
            rt = [0.75, 0.4, 0.3][t]
            for dot in dots:
                self.play(FadeIn(dot, shift=DOWN * 0.5), run_time=rt)
            if t == 0:
                self.play(FadeIn(cnt_txt), run_time=0.5)
            cr = cellrect[cell_of(p1)]
            ln = Line(P(p1), P(p2), color=GOLD, stroke_width=6)
            self.play(cr.animate.set_fill(GOLD, 0.3), Create(ln), *[Indicate(dots[i], color=GOLD) for i, p in enumerate(pts) if p in (p1, p2)], run_time=0.9)
            dtxt = MathTex(r"d=%.2f\le\sqrt2" % d, font_size=44, color=GOLD).move_to([0, -3.0, 0])
            if result_txt:
                self.play(Transform(result_txt, dtxt), run_time=0.3)
            else:
                result_txt = dtxt
                self.play(Write(dtxt), run_time=0.6)
            self.wait(1.0 if t == 0 else 0.6)
            self.play(FadeOut(VGroup(*dots)), FadeOut(ln), cr.animate.set_fill(GOLD, 0), run_time=0.4)
            if t == 0:
                c = swap_cap(self, c, cap("Thử cách đặt khác…", 36))
        c = swap_cap(self, c, cap("Luôn có 2 điểm cùng một ô!", 36, GOLD))
        concl = Text("5 điểm, 4 ô ⇒ có ô chứa ≥ 2 điểm\n⇒ có 2 điểm cách nhau ≤ √2", font=FONT, font_size=30, line_spacing=0.9).move_to([0, -4.7, 0])
        self.play(FadeIn(concl), run_time=0.8)
        self.wait(3.0)
