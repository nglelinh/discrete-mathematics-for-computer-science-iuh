from common import *
from math import sqrt

PHI = (1 + sqrt(5)) / 2
PHI_STR = "1.6180339887"
FIB = [1, 1]
while len(FIB) < 40:
    FIB.append(FIB[-1] + FIB[-2])
RATIO = [FIB[i + 1] / FIB[i] for i in range(39)]          # RATIO[n-1] = F_{n+1}/F_n
assert abs(RATIO[-1] - PHI) < 1e-12
assert all(abs(round((PHI ** n - (-1 / PHI) ** n) / sqrt(5)) - FIB[n - 1]) == 0 for n in range(1, 35))  # Binet
NSQ = 9
SC = 7.4 / 55
assert FIB[NSQ] == 55


def build_squares():
    """Các hình vuông Fibonacci (đơn vị gốc) theo vòng: phải, trên, trái, dưới."""
    sq = [(0, 0, 1)]
    x0, y0, x1, y1 = 0, 0, 1, 1
    for i in range(1, NSQ):
        s = FIB[i]
        d = i % 4
        if d == 0:   # phải
            sq.append((x1, y0, s)); x1 += s
        elif d == 1: # trên
            sq.append((x0, y1, s)); y1 += s
        elif d == 2: # trái
            sq.append((x0 - s, y0, s)); x0 -= s
        else:        # dưới
            sq.append((x0, y0 - s, s)); y0 -= s
    return sq, (x0, y0, x1, y1)


def spiral(sq):
    """Danh sách (tâm, bán kính, điểm đầu, điểm cuối) của các cung 1/4, liên tục tiếp tuyến."""
    def run(start, tan):
        cur, tn, res = np.array(start, float), np.array(tan, float), []
        for (x, y, s) in sq:
            corners = [np.array(p, float) for p in [(x, y), (x + s, y), (x + s, y + s), (x, y + s)]]
            found = None
            for ctr in corners:
                rad = cur - ctr
                if abs(np.linalg.norm(rad) - s) > 1e-9:
                    continue
                for sg in (1, -1):
                    t = sg * np.array([-rad[1], rad[0]]) / s
                    if np.dot(t, tn) > 0.999:
                        found = (ctr, sg, t)
            if not found:
                return None
            ctr, sg, t = found
            end = ctr + t * s
            res.append((ctr, s, cur.copy(), end.copy()))
            re_ = end - ctr
            tn = sg * np.array([-re_[1], re_[0]]) / s
            cur = end
        return res
    x, y, s = sq[0]
    for st in [(0, 0), (1, 0), (1, 1), (0, 1)]:
        for tn in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            r = run(st, tn)
            if r:
                return r
    raise RuntimeError("no spiral")


class Fibonacci(Scene):
    def construct(self):
        c = cap("Dãy Fibonacci", 44)
        self.add(c)
        sq, (rx0, ry0, rx1, ry1) = build_squares()
        cx, cy = (rx0 + rx1) / 2, (ry0 + ry1) / 2
        ORG = np.array([0, 1.9, 0])

        def P(x, y):
            return ORG + np.array([(x - cx) * SC, (y - cy) * SC, 0])

        pal = ["#6cb6ff", "#8fd694", "#f5c542", "#ff9f6b", "#c792ea", "#6cb6ff", "#8fd694", "#f5c542", "#ff9f6b"]
        sqs, labs = [], []
        for i, (x, y, s) in enumerate(sq):
            m = Square(s * SC, color=pal[i], stroke_width=3, fill_color=pal[i], fill_opacity=0.18)
            m.move_to(P(x + s / 2, y + s / 2))
            sqs.append(m)
            if s * SC > 0.45:
                labs.append(Integer(FIB[i], font_size=min(44, 14 + 26 * s * SC / 2)).move_to(m))
            else:
                labs.append(None)

        # dãy số ở trên
        seq = MathTex(r"1,\,1,\,2,\,3,\,5,\,8,\,13,\,21,\,34,\,55,\ldots", font_size=40).move_to([0, 5.4, 0])
        self.play(Write(seq), run_time=1.0)

        arc_list = []
        for ctr, r, st, en in spiral(sq):
            a0 = np.arctan2((st - ctr)[1], (st - ctr)[0])
            a1 = np.arctan2((en - ctr)[1], (en - ctr)[0])
            da = (a1 - a0 + np.pi) % (2 * np.pi) - np.pi
            arc_list.append(Arc(radius=r * SC, start_angle=a0, angle=da, arc_center=P(*ctr),
                                color=WHITE, stroke_width=5))

        c = swap_cap(self, c, cap("Ghép hình vuông cạnh F\u2099", 36, GOLD))
        for i in range(NSQ):
            anims = [FadeIn(sqs[i], scale=0.6), Create(arc_list[i])]
            if labs[i] is not None:
                anims.append(FadeIn(labs[i]))
            self.play(*anims, run_time=max(0.35, 0.95 - 0.1 * i))
        self.wait(0.8)

        c = swap_cap(self, c, cap("Tỉ số hai số liên tiếp", 38))
        n_tr = ValueTracker(1)
        lab = MathTex(r"\frac{F_{n+1}}{F_n}=", font_size=52).move_to([-2.3, -2.6, 0])
        num = DecimalNumber(1.0, num_decimal_places=10, font_size=56)
        nlab = MathTex(r"n=", font_size=40)
        nnum = Integer(1, font_size=40)
        phi_ref = MathTex(r"\varphi=\frac{1+\sqrt5}{2}=1.6180339887\ldots", font_size=36, color=DIM)

        def lay():
            num.next_to(lab, RIGHT, buff=0.25)

        def upd(m):
            n = int(min(39, max(1, round(n_tr.get_value()))))
            m.set_value(RATIO[n - 1])
            gold_digits(m, "%.10f" % RATIO[n - 1], PHI_STR)
            lay()
        num.add_updater(upd)
        nlab.move_to([-1.0, -3.9, 0])
        nnum.add_updater(lambda m: (m.set_value(int(round(n_tr.get_value()))), m.next_to(nlab, RIGHT, buff=0.12)))
        phi_ref.move_to([0, -5.0, 0])
        lay()
        self.play(FadeIn(lab), FadeIn(num), FadeIn(nlab), FadeIn(nnum), FadeIn(phi_ref), run_time=0.7)
        self.play(n_tr.animate.set_value(7), run_time=3.5, rate_func=smooth)
        self.play(n_tr.animate.set_value(39), run_time=4.5, rate_func=rush_into)
        self.wait(0.3)
        c = swap_cap(self, c, cap("Tỉ lệ vàng φ ≈ 1,618", 38, GOLD))
        self.play(Indicate(num, color=GOLD, scale_factor=1.06), run_time=1.0)
        binet = MathTex(r"F_n=\frac{\varphi^{n}-\psi^{n}}{\sqrt5},\ \psi=\frac{1-\sqrt5}{2}", font_size=40, color=GOLD).move_to([0, -6.0, 0])
        self.play(FadeIn(binet), run_time=0.8)
        self.wait(3.5)
