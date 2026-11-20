from common import *
from math import gcd

A, B = 252, 105
STEPS = []
a, b = A, B
while b:
    STEPS.append((a, b, a // b, a % b))
    a, b = b, a % b
G = a
assert G == gcd(A, B) == 21 and STEPS == [(252, 105, 2, 42), (105, 42, 2, 21), (42, 21, 2, 0)]


class Euclid(Scene):
    def construct(self):
        c = cap("Thuật toán Euclid", 44)
        self.add(c)
        SC = 6.9 / A
        cx, cy = 0.0, 3.2          # tâm hình chữ nhật
        x0, y0 = cx - A * SC / 2, cy - B * SC / 2   # góc dưới-trái

        def rect(x, y, w, h, color, fill=0.0, sw=3):
            r = Rectangle(width=w * SC, height=h * SC, color=color, stroke_width=sw,
                          fill_color=color, fill_opacity=fill)
            r.move_to([x0 + (x + w / 2) * SC, y0 + (y + h / 2) * SC, 0])
            return r
        big = rect(0, 0, A, B, WHITE, 0, 4)
        wl = MathTex(str(A), font_size=36).next_to(big, UP, buff=0.12)
        hl = MathTex(str(B), font_size=36).next_to(big, LEFT, buff=0.12)
        self.play(Create(big), FadeIn(wl), FadeIn(hl), run_time=1.0)
        q = Text("Lát bằng hình vuông lớn nhất có thể", font=FONT, font_size=28, color=DIM).move_to([0, 0.9, 0])
        self.play(FadeIn(q), run_time=0.5)

        cols = [BLUE, "#8fd694", "#ff9f6b"]
        eqs = [
            r"252=2\cdot105+42",
            r"105=2\cdot42+21",
            r"42=2\cdot21+0",
        ]
        eq_m = []
        # vùng còn lại (x, y, w, h)
        x, y, w, h = 0, 0, A, B
        for i, (a, b, qt, r) in enumerate(STEPS):
            s = b                     # cạnh hình vuông
            squares = []
            for j in range(qt):
                if w >= h:            # xếp theo chiều ngang
                    squares.append(rect(x + j * s, y, s, s, cols[i], 0.35))
                else:                 # xếp theo chiều dọc
                    squares.append(rect(x, y + j * s, s, s, cols[i], 0.35))
            lab = [MathTex(r"%d\times%d" % (s, s), font_size=max(18, 30 - 5 * i)).move_to(sq) for sq in squares] if s * SC > 0.7 else []
            e = MathTex(eqs[i], font_size=44).move_to([0, -0.4 - 1.25 * i, 0])
            eq_m.append(e)
            self.play(LaggedStart(*[FadeIn(sq, scale=0.8) for sq in squares], lag_ratio=0.4),
                      *[FadeIn(l) for l in lab], Write(e), run_time=[3.0, 2.6, 2.2][i])
            if w >= h:
                x, w = x + qt * s, w - qt * s
            else:
                y, h = y + qt * s, h - qt * s
            if r:
                rem = rect(x, y, w, h, GOLD, 0.0, 5)
                self.play(Create(rem), run_time=0.9)
                self.wait(0.8)
                self.play(FadeOut(rem), run_time=0.3)
            else:
                self.wait(0.3)
        assert w * h == 0 or r == 0
        c = swap_cap(self, c, cap("Cạnh nhỏ nhất = ước chung lớn nhất", 32, GOLD))
        # lưới 21x21 phủ toàn bộ
        lines = VGroup()
        for k in range(1, A // G):
            lines.add(Line([x0 + k * G * SC, y0, 0], [x0 + k * G * SC, y0 + B * SC, 0], stroke_width=1.5, color=GOLD))
        for k in range(1, B // G):
            lines.add(Line([x0, y0 + k * G * SC, 0], [x0 + A * SC, y0 + k * G * SC, 0], stroke_width=1.5, color=GOLD))
        self.play(Create(lines), run_time=2.0)
        res = MathTex(r"\gcd(252,105)=21", font_size=62, color=GOLD).move_to([0, -5.3, 0])
        cnt = MathTex(r"252=12\cdot21,\quad 105=5\cdot21", font_size=36, color=DIM).move_to([0, -4.2, 0])
        self.play(Write(res), FadeIn(cnt), run_time=1.2)
        self.wait(4.0)
