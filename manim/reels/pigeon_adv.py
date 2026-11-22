from common import *
from math import ceil, sqrt, dist
from itertools import combinations

# ---------- Toán ----------
assert ceil(4001 / 1000) == 5 and ceil(4000 / 1000) == 4
assert ceil(97 / 10) == 10 and 97 // 10 == 9
PTS = [(0.15, 0.2), (0.7, 0.15), (0.35, 0.75), (0.8, 0.85), (0.6, 0.4)]
quad = lambda p: (int(p[0] >= 0.5), int(p[1] >= 0.5))
SAME = [(i, j) for i, j in combinations(range(5), 2) if quad(PTS[i]) == quad(PTS[j])]
assert SAME == [(1, 4)]
D14 = dist(PTS[1], PTS[4])
assert "%.2f" % D14 == "0.27" and D14 <= sqrt(2) / 2 and "%.3f" % (sqrt(2) / 2) == "0.707"
TIGHT = [(0, 0), (1, 0), (0, 1), (1, 1), (0.5, 0.5)]
assert abs(min(dist(a, b) for a, b in combinations(TIGHT, 2)) - sqrt(2) / 2) < 1e-12
PAIRS = [(1, 10), (2, 9), (3, 8), (4, 7), (5, 6)]
CHOSEN = [2, 3, 5, 7, 8, 10]
hit = [p for p in PAIRS if p[0] in CHOSEN and p[1] in CHOSEN]
assert hit == [(3, 8)]
assert all(any(a in s and b in s for a, b in PAIRS) for s in combinations(range(1, 11), 6))
assert not all(any(a in s and b in s for a, b in PAIRS) for s in combinations(range(1, 11), 5))
SEQ7 = [3, 5, 2, 6, 4, 1, 5]
PS = [sum(SEQ7[:k + 1]) for k in range(7)]
PM = [x % 7 for x in PS]
assert PS == [3, 8, 10, 16, 20, 21, 26] and PM == [3, 1, 3, 2, 6, 0, 5]
assert SEQ7[1] + SEQ7[2] == 7 and sum(SEQ7[:6]) == 21
REP = [int("1" * k) % 6 for k in range(1, 5)]
assert REP == [1, 5, 3, 1] and 1111 - 1 == 1110 == 6 * 185
SEQ = [3, 8, 2, 9, 5, 1, 7, 4, 10, 6]


def labels(a):
    inc, dec = [], []
    for k in range(len(a)):
        inc.append(1 + max([inc[j] for j in range(k) if a[j] < a[k]], default=0))
        dec.append(1 + max([dec[j] for j in range(k) if a[j] > a[k]], default=0))
    return inc, dec


INC, DEC = labels(SEQ)
assert INC == [1, 2, 1, 3, 2, 1, 3, 2, 4, 3] and DEC == [1, 1, 2, 1, 2, 3, 2, 3, 1, 3]
assert len(set(zip(INC, DEC))) == 10 and max(INC) == 4
I4 = [0, 1, 3, 8]
assert [SEQ[i] for i in I4] == [3, 8, 9, 10]
TI, TD = labels([3, 2, 1, 6, 5, 4, 9, 8, 7])
assert max(TI) == 3 and max(TD) == 3


class PigeonAdv(Scene):
    def wait(self, duration=1.0, **kw):
        super().wait(duration * 1.8, **kw)

    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Nguyên lý Dirichlet nâng cao", 40)
        t1 = Text("Chuồng và\nbồ câu", font=FONT, font_size=84, color=GOLD, line_spacing=1.0).move_to([0, 1.8, 0])
        t2 = para("Phần khó nhất luôn là: chọn \"chuồng\" thế nào?", 30, y=-0.6)
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. Dạng tổng quát =====
        c = swap_cap(self, c, cap("Dạng tổng quát", 44, GOLD))
        f = para("N con bồ câu vào n chuồng ⇒ có chuồng\nchứa ít nhất ⌈N/n⌉ con", 30, GOLD, y=5.0)
        self.play(FadeIn(f), run_time=0.6)
        boxes = VGroup(*[Rectangle(width=1.4, height=1.6, color=BLUE, stroke_width=3).move_to([-2.4 + i * 1.6, 2.6, 0]) for i in range(4)])
        self.play(Create(boxes), run_time=0.6)
        dots = VGroup()
        for k in range(9):
            b = boxes[k % 4]
            dd = Dot(b.get_center() + np.array([-0.35 + (k // 4) * 0.35, 0.4 - (k // 4) * 0.4, 0]), radius=0.13, color=GOLD)
            dots.add(dd)
            self.play(FadeIn(dd, shift=DOWN * 0.3), run_time=0.2)
        e = para("9 con, 4 chuồng: chia đều nhất\nvẫn có chuồng 3 con = ⌈9/4⌉", 26, WHITE, y=1.0)
        self.play(FadeIn(e), run_time=0.5)
        self.wait(2.0)
        x1 = para("Hash table 1000 bucket: cần 4001 khóa để chắc chắn\ncó bucket chứa ít nhất 5 khóa (4000 khóa thì chưa chắc)", 24, WHITE, y=-0.9)
        x2 = para("97 tác vụ cho 10 server: có server nhận ≥ ⌈9,7⌉ = 10;\nchia đều nhất thì mỗi server nhận 9 hoặc 10", 24, WHITE, y=-2.7)
        self.play(FadeIn(x1), run_time=0.6)
        self.wait(2.5)
        self.play(FadeIn(x2), run_time=0.6)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 3. 5 điểm trong hình vuông =====
        c = swap_cap(self, c, cap("5 điểm trong hình vuông cạnh 1", 38, GOLD))
        q = para("Chứng minh: có hai điểm cách nhau\nkhông quá √2/2 ≈ 0,707", 28, WHITE, y=5.2)
        self.play(FadeIn(q), run_time=0.6)
        S = 4.6
        O = np.array([-2.3, -0.4, 0])

        def m(p):
            return O + np.array([p[0] * S, p[1] * S, 0])
        sq = Square(S, color=WHITE, stroke_width=3).move_to(m((0.5, 0.5)))
        self.play(Create(sq), run_time=0.5)
        pts = VGroup(*[Dot(m(p), radius=0.12, color=GOLD) for p in PTS])
        self.play(LaggedStart(*[GrowFromCenter(d_) for d_ in pts], lag_ratio=0.2), run_time=1.0)
        self.wait(1.0)
        h = para("Chia thành 4 ô vuông cạnh 1/2 (4 chuồng)", 24, BLUE, y=-0.9)
        cross = VGroup(Line(m((0.5, 0)), m((0.5, 1)), color=BLUE, stroke_width=3), Line(m((0, 0.5)), m((1, 0.5)), color=BLUE, stroke_width=3))
        self.play(Create(cross), FadeIn(h), run_time=0.8)
        self.wait(1.5)
        h2 = para("5 điểm, 4 ô ⇒ có ô chứa ít nhất 2 điểm", 26, WHITE, y=-1.7)
        hl = Square(S / 2, color=RED, fill_color=RED, fill_opacity=0.15, stroke_width=0).move_to(m((0.75, 0.25)))
        self.play(FadeIn(h2), FadeIn(hl), pts[1].animate.set_color(RED), pts[4].animate.set_color(RED), run_time=0.7)
        self.wait(1.5)
        diag = DashedLine(m((0.5, 0)), m((1, 0.5)), color=GREEN, stroke_width=3)
        h3 = para("Hai điểm trong cùng một ô cách nhau không quá\nđường chéo ô: √(1/4 + 1/4) = √2/2", 24, GREEN, y=-2.8)
        self.play(Create(diag), FadeIn(h3), run_time=0.8)
        self.wait(2.0)
        seg = Line(m(PTS[1]), m(PTS[4]), color=RED, stroke_width=4)
        h4 = para("Ở đây: khoảng cách ≈ 0,27", 24, RED, y=-3.8)
        self.play(Create(seg), FadeIn(h4), run_time=0.6)
        self.wait(2.0)
        self.play(FadeOut(pts), FadeOut(seg), FadeOut(hl), FadeOut(diag), FadeOut(h4), run_time=0.5)
        tp = VGroup(*[Dot(m(p), radius=0.12, color=GOLD) for p in TIGHT])
        h5 = para("Không thể tốt hơn: 4 góc + tâm\ncó mọi khoảng cách ≥ √2/2", 26, GOLD, y=-4.9)
        self.play(FadeIn(tp), FadeIn(h5), run_time=0.7)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 3b. 9 điểm, tam giác diện tích nhỏ =====
        c = swap_cap(self, c, cap("9 điểm và tam giác nhỏ", 42, GOLD))
        q = para("9 điểm trong hình vuông cạnh 1, không có\n3 điểm thẳng hàng. Chứng minh: có tam giác\nvới 3 đỉnh là các điểm đó, diện tích ≤ 1/8", 26, WHITE, y=5.0)
        self.play(FadeIn(q), run_time=0.6)
        O = np.array([-2.3, -1.0, 0])
        sq = Square(S, color=WHITE, stroke_width=3).move_to(m((0.5, 0.5)))
        cross = VGroup(Line(m((0.5, 0)), m((0.5, 1)), color=BLUE, stroke_width=3), Line(m((0, 0.5)), m((1, 0.5)), color=BLUE, stroke_width=3))
        P9 = [(0.1, 0.15), (0.35, 0.3), (0.8, 0.2), (0.62, 0.38), (0.2, 0.7), (0.58, 0.62), (0.7, 0.9), (0.9, 0.7), (0.4, 0.85)]
        self.play(Create(sq), Create(cross), run_time=0.7)
        d9 = VGroup(*[Dot(m(p), radius=0.11, color=GOLD) for p in P9])
        self.play(LaggedStart(*[GrowFromCenter(x) for x in d9], lag_ratio=0.1), run_time=0.9)
        h = para("9 điểm, 4 ô ⇒ có ô chứa ít nhất ⌈9/4⌉ = 3 điểm", 26, WHITE, y=-1.9)
        self.play(FadeIn(h), run_time=0.5)
        self.wait(1.5)
        tri3 = Polygon(m(P9[5]), m(P9[6]), m(P9[7]), color=RED, fill_color=RED, fill_opacity=0.35, stroke_width=3)
        self.play(FadeIn(tri3), *[d9[i].animate.set_color(RED) for i in (5, 6, 7)], run_time=0.6)
        h2 = para("Tam giác nằm trong ô vuông cạnh 1/2\nnên diện tích ≤ ½ · (1/2)² = 1/8", 26, RED, y=-3.3)
        self.play(FadeIn(h2), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 4. Tổng bằng 11 =====
        c = swap_cap(self, c, cap("Chọn 6 số từ 1 đến 10", 42, GOLD))
        q = para("Chứng minh: luôn có hai số có tổng bằng 11", 28, WHITE, y=5.2)
        self.play(FadeIn(q), run_time=0.5)
        self.wait(1.0)
        pb = VGroup()
        pos = {}
        for i, (a, b) in enumerate(PAIRS):
            r = RoundedRectangle(width=1.4, height=2.0, corner_radius=0.15, color=BLUE, stroke_width=3).move_to([-3.0 + i * 1.5, 2.6, 0])
            ta = Text(str(a), font=FONT, font_size=34).move_to(r.get_center() + UP * 0.45)
            tb = Text(str(b), font=FONT, font_size=34).move_to(r.get_center() + DOWN * 0.45)
            pos[a], pos[b] = ta, tb
            pb.add(VGroup(r, ta, tb))
        e = para("5 chuồng: các cặp có tổng 11", 24, BLUE, y=1.1)
        self.play(FadeIn(pb), FadeIn(e), run_time=0.8)
        self.wait(1.5)
        e2 = para("Chọn 6 số, chẳng hạn 2, 3, 5, 7, 8, 10:", 28, WHITE, y=0.3)
        self.play(FadeIn(e2), run_time=0.5)
        for x in CHOSEN:
            self.play(pos[x].animate.set_color(GOLD), Flash(pos[x], color=GOLD, flash_radius=0.4), run_time=0.35)
        self.play(pb[2][0].animate.set_fill(RED, 0.3).set_color(RED), run_time=0.5)
        e3 = para("6 số, 5 chuồng ⇒ có chuồng chứa\ncả hai số: 3 + 8 = 11", 28, RED, y=-1.0)
        self.play(FadeIn(e3), run_time=0.5)
        self.wait(2.0)
        e4 = para("Với 5 số thì chưa chắc:\n1, 2, 3, 4, 5 không có cặp nào", 26, DIM, y=-2.6)
        self.play(FadeIn(e4), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 5. Số dư của tổng tiền tố =====
        c = swap_cap(self, c, cap("Đoạn liên tiếp có tổng chia hết cho 7", 36, GOLD))
        q = para("Với 7 số nguyên bất kỳ, luôn có một đoạn\nliên tiếp có tổng chia hết cho 7.\nVí dụ: 3, 5, 2, 6, 4, 1, 5", 28, WHITE, y=5.0)
        self.play(FadeIn(q), run_time=0.6)
        self.wait(1.5)
        hdr = VGroup(*[Text(s, font=FONT, font_size=24, color=DIM).move_to([-3.2, y, 0]) for s, y in (("số", 3.6), ("tổng S", 2.9), ("dư mod 7", 2.2))])
        self.play(FadeIn(hdr), run_time=0.4)
        cols = []
        for k in range(7):
            x = -1.8 + k * 0.85
            a = Text(str(SEQ7[k]), font=FONT, font_size=28).move_to([x, 3.6, 0])
            s_ = Text(str(PS[k]), font=FONT, font_size=26, color=WHITE).move_to([x, 2.9, 0])
            r = Text(str(PM[k]), font=FONT, font_size=30, color=GOLD).move_to([x, 2.2, 0])
            cols.append((a, s_, r))
            self.play(FadeIn(a), FadeIn(s_), FadeIn(r), run_time=0.35)
        self.wait(1.0)
        e = para("S₁ = 3, S₂ = 3 + 5, …: 7 tổng đầu,\nmỗi tổng có số dư thuộc {0, 1, …, 6}", 26, WHITE, y=1.1)
        self.play(FadeIn(e), run_time=0.5)
        self.wait(1.2)
        e2 = para("Nếu có tổng dư 0: xong. Nếu không,\n7 tổng chỉ có 6 số dư khác 0 (6 chuồng)\n⇒ có hai tổng cùng số dư", 26, WHITE, y=-0.6)
        self.play(FadeIn(e2), run_time=0.5)
        self.wait(2.5)
        self.play(cols[0][2].animate.set_color(RED), cols[2][2].animate.set_color(RED), run_time=0.5)
        e3 = para("S₁ ≡ S₃ ≡ 3 ⇒ S₃ − S₁ = 5 + 2 = 7", 28, RED, y=-2.2)
        self.play(FadeIn(e3), run_time=0.5)
        self.wait(2.0)
        self.play(cols[5][2].animate.set_color(GREEN), run_time=0.4)
        e4 = para("Ở đây cũng có S₆ = 21 ≡ 0:\nsáu số đầu có tổng 21", 26, GREEN, y=-3.2)
        self.play(FadeIn(e4), run_time=0.5)
        self.wait(2.0)
        e5 = para("Cùng ý: có bội của 6 chỉ gồm chữ số 0, 1.\n1, 11, 111, 1111 chia 6 dư 1, 5, 3, 1\n⇒ 1111 − 1 = 1110 = 6 × 185", 26, GOLD, y=-4.9)
        self.play(FadeIn(e5), run_time=0.6)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 6. Erdős–Szekeres =====
        c = swap_cap(self, c, cap("Định lý Erdős–Szekeres", 42, GOLD))
        q = para("Mọi dãy n² + 1 số khác nhau đều có\ndãy con tăng hoặc giảm dài n + 1.\nVới n = 3: 10 số → có dãy con dài 4", 26, WHITE, y=5.0)
        self.play(FadeIn(q), run_time=0.6)
        self.wait(2.0)
        xs = [-3.6 + k * 0.8 for k in range(10)]
        hd = VGroup(*[Text(s, font=FONT, font_size=22, color=col).move_to([-3.9, y, 0]) for s, col, y in (("a", WHITE, 3.3), ("t", GREEN, 2.6), ("g", RED, 1.9))])
        hd.shift(RIGHT * 0.0)
        av = [Text(str(v), font=FONT, font_size=30).move_to([xs[k] + 0.3, 3.3, 0]) for k, v in enumerate(SEQ)]
        self.play(FadeIn(hd), LaggedStart(*[FadeIn(a) for a in av], lag_ratio=0.08), run_time=1.0)
        e = para("Nhãn (t, g) của mỗi số: độ dài dãy con\ntăng (t) và giảm (g) dài nhất kết thúc tại đó", 24, DIM, y=0.9)
        self.play(FadeIn(e), run_time=0.6)
        self.wait(2.0)
        tv, gv = [], []
        for k in range(10):
            t_ = Text(str(INC[k]), font=FONT, font_size=26, color=GREEN).move_to([xs[k] + 0.3, 2.6, 0])
            g_ = Text(str(DEC[k]), font=FONT, font_size=26, color=RED).move_to([xs[k] + 0.3, 1.9, 0])
            tv.append(t_)
            gv.append(g_)
            self.play(FadeIn(t_), FadeIn(g_), av[k].animate.set_color(GOLD), run_time=0.35)
            self.play(av[k].animate.set_color(WHITE), run_time=0.1)
        self.wait(1.0)
        p1 = para("Số trước nhỏ hơn ⇒ t của số sau lớn hơn;\nsố trước lớn hơn ⇒ g của số sau lớn hơn\n⇒ 10 nhãn đôi một khác nhau", 24, WHITE, y=-0.6)
        self.play(FadeIn(p1), run_time=0.6)
        self.wait(2.5)
        p2 = para("Nếu mọi t, g ≤ 3 thì chỉ có 3 × 3 = 9 nhãn\n(9 chuồng) cho 10 số: vô lý!", 26, GOLD, y=-2.2)
        self.play(FadeIn(p2), run_time=0.6)
        self.wait(2.5)
        self.play(tv[8].animate.set_color(GOLD).scale(1.3), *[av[i].animate.set_color(GREEN) for i in I4], run_time=0.6)
        p3 = para("t = 4 tại số 10: dãy con tăng 3, 8, 9, 10", 28, GREEN, y=-3.3)
        self.play(FadeIn(p3), run_time=0.5)
        self.wait(2.0)
        p4 = para("Không thể giảm xuống 9 số: dãy\n3 2 1 6 5 4 9 8 7 không có dãy con\ntăng hay giảm nào dài 4", 26, DIM, y=-4.8)
        self.play(FadeIn(p4), run_time=0.5)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 7. Tóm tắt =====
        c = swap_cap(self, c, cap("Mẹo chọn chuồng", 44, GOLD))
        sm = VGroup(*[Text(s, font=FONT, font_size=30, color=col, line_spacing=1.1) for s, col in [
            ("Hình học: chia hình thành các ô nhỏ", BLUE),
            ("Số học: dùng số dư (mod n)", GOLD),
            ("Cặp số: gom các phần tử \"bù nhau\"\nvào cùng một chuồng", GREEN),
            ("Dãy số: gắn nhãn cho từng phần tử,\nrồi đếm số nhãn có thể có", RED),
            ("Tin học: hash, cân bằng tải —\nva chạm là không tránh được", WHITE),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        fitw(sm, 7.8).move_to([0, 1.8, 0])
        self.play(LaggedStart(*[FadeIn(m_, shift=RIGHT * 0.2) for m_ in sm], lag_ratio=0.5), run_time=3.0)
        e = para("Bồ câu nhiều hơn chuồng\n⇒ va chạm chắc chắn xảy ra", 30, GOLD, y=-3.6)
        self.play(FadeIn(e), run_time=0.6)
        self.wait(6.0)
