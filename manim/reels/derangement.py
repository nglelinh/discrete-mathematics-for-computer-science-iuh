from common import *
from itertools import permutations
from math import factorial, e

def D(n):
    return sum((-1) ** k * factorial(n) // factorial(k) for k in range(n + 1))
for n in range(1, 9):
    brute = sum(1 for p in permutations(range(n)) if all(p[i] != i for i in range(n)))
    assert brute == D(n), n
assert [D(n) for n in range(1, 8)] == [0, 1, 2, 9, 44, 265, 1854]
INV_E = "%.10f" % (1 / e)
assert INV_E == "0.3678794412"
assert abs(D(15) / factorial(15) - 1 / e) < 1e-12


class Derangement(Scene):
    def construct(self):
        c = cap("Hoán vị không điểm cố định", 36)
        self.add(c)
        perms = list(permutations(range(1, 5)))
        assert len(perms) == 24
        cw, ch = 1.3, 1.05
        cells, derg = [], []
        grid = VGroup()
        for idx, p in enumerate(perms):
            r, col = divmod(idx, 6)
            box = RoundedRectangle(corner_radius=0.12, width=cw - 0.12, height=ch - 0.12, color=DIM,
                                   stroke_width=2, fill_color=CELL, fill_opacity=1)
            txt = VGroup(*[MathTex(str(v), font_size=34, color=(RED if v == i + 1 else WHITE))
                           for i, v in enumerate(p)]).arrange(RIGHT, buff=0.08)
            g = VGroup(box, txt)
            g.move_to([(col - 2.5) * cw, 4.2 - r * ch, 0])
            txt.move_to(box)
            grid.add(g)
            cells.append(g)
            derg.append(all(v != i + 1 for i, v in enumerate(p)))
        assert sum(derg) == 9
        sub = Text("24 hoán vị của 1 2 3 4", font=FONT, font_size=28, color=DIM).move_to([0, 5.5, 0])
        # chữ số đỏ = điểm cố định: ẩn trước, chỉ hiện ở bước 2
        for g, p in zip(cells, perms):
            for i, ch_ in enumerate(g[1]):
                ch_.set_color(WHITE)
        self.play(LaggedStart(*[FadeIn(g, scale=0.7) for g in cells], lag_ratio=0.04), FadeIn(sub), run_time=2.2)
        c = swap_cap(self, c, cap("Đỏ = phần tử đứng đúng chỗ", 34, RED))
        anims = []
        for g, p in zip(cells, perms):
            for i, v in enumerate(p):
                if v == i + 1:
                    anims.append(g[1][i].animate.set_color(RED))
        self.play(*anims, run_time=1.2)
        self.wait(0.5)
        c = swap_cap(self, c, cap("Không có số đỏ nào?", 36, GOLD))
        keep = [g for g, d in zip(cells, derg) if d]
        drop = [g for g, d in zip(cells, derg) if not d]
        self.play(*[g.animate.set_opacity(0.15) for g in drop],
                  *[g[0].animate.set_fill(GOLD, 0.35).set_stroke(GOLD, 3) for g in keep], run_time=1.2)
        res = MathTex(r"D_4=9\ \text{trong}\ 24", font_size=54, color=GOLD).move_to([0, -0.5, 0])
        self.play(Write(res), run_time=0.8)
        self.wait(0.8)

        # --- phần hội tụ ---
        self.play(FadeOut(grid), FadeOut(sub), FadeOut(res), run_time=0.5)
        c = swap_cap(self, c, cap("Tỉ lệ Dₙ / n! khi n lớn", 36))
        tn = ValueTracker(1)
        nl = MathTex(r"n=", font_size=48)
        nn = Integer(1, font_size=48)
        dl = MathTex(r"D_n=", font_size=48)
        dn = Integer(0, font_size=48, color=GOLD)
        rl = MathTex(r"\frac{D_n}{n!}=", font_size=56)
        rn = DecimalNumber(0.0, num_decimal_places=10, font_size=56)
        ref = MathTex(r"\frac1e=0.3678794412\ldots", font_size=44, color=DIM)
        nl.move_to([-1.2, 3.8, 0]); dl.move_to([-1.8, 2.5, 0]); rl.move_to([-2.6, 1.0, 0]); ref.move_to([0, -0.6, 0])

        def N_():
            return int(round(tn.get_value()))
        nn.add_updater(lambda m: (m.set_value(N_()), m.next_to(nl, RIGHT, buff=0.15)))
        dn.add_updater(lambda m: (m.set_value(D(N_())), m.next_to(dl, RIGHT, buff=0.15)))
        def upd(m):
            n = N_()
            v = D(n) / factorial(n)
            m.set_value(v)
            gold_digits(m, "%.10f" % v, INV_E)
            m.next_to(rl, RIGHT, buff=0.2)
        rn.add_updater(upd)
        bar_bg = Line([-3.5, -2.1, 0], [3.5, -2.1, 0], color=DIM, stroke_width=3)
        marker_e = Line([-3.5 + 7 * (1 / e), -1.9, 0], [-3.5 + 7 * (1 / e), -2.3, 0], color=GOLD, stroke_width=4)
        dot = Dot(radius=0.12, color=GOLD)
        dot.add_updater(lambda m: m.move_to([-3.5 + 7 * (D(N_()) / factorial(N_())), -2.1, 0]))
        self.play(*[FadeIn(m) for m in (nl, nn, dl, dn, rl, rn, ref, bar_bg, marker_e, dot)], run_time=0.8)
        self.play(tn.animate.set_value(6), run_time=4.0, rate_func=smooth)
        self.play(tn.animate.set_value(15), run_time=4.5, rate_func=rush_into)
        formula = MathTex(r"D_n=n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}\ \to\ \frac{n!}{e}",
                          font_size=44, color=GOLD).move_to([0, -3.9, 0])
        c = swap_cap(self, c, cap("Gần 36,8% hoán vị là derangement", 32, GOLD))
        self.play(Write(formula), run_time=1.2)
        note = Text("Bao–loại trừ: 1 − 1 + 1/2! − 1/3! + …", font=FONT, font_size=28, color=DIM).move_to([0, -5.3, 0])
        self.play(FadeIn(note), run_time=0.5)
        self.wait(3.0)
