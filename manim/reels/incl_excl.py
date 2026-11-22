from common import *
from itertools import combinations

# ---------- Toán ----------
N = 100
A = {k for k in range(1, N + 1) if k % 2 == 0}
B = {k for k in range(1, N + 1) if k % 3 == 0}
C = {k for k in range(1, N + 1) if k % 5 == 0}
assert (len(A), len(B), len(C)) == (50, 33, 20)
assert (len(A & B), len(A & C), len(B & C), len(A & B & C)) == (16, 10, 6, 3)
U = A | B | C
assert len(U) == 50 + 33 + 20 - 16 - 10 - 6 + 3 == 74 and N - len(U) == 26
REG = {"A": len(A - B - C), "B": len(B - A - C), "C": len(C - A - B), "AB": len((A & B) - C),
       "AC": len((A & C) - B), "BC": len((B & C) - A), "ABC": len(A & B & C)}
assert REG == {"A": 27, "B": 14, "C": 7, "AB": 13, "AC": 7, "BC": 3, "ABC": 3}
assert sum(REG.values()) == 74
# 2 tập: 50 sv, 30 Anh, 20 Pháp, 10 cả hai
assert 30 + 20 - 10 == 40 and 50 - 40 == 10
# số lần đếm mỗi vùng qua từng bước
STEP1 = {"A": 1, "B": 1, "C": 1, "AB": 2, "AC": 2, "BC": 2, "ABC": 3}
STEP2 = {r: STEP1[r] - sum(1 for p in ("AB", "AC", "BC") if set(p) <= set(r)) for r in STEP1}
STEP3 = {r: STEP2[r] + (1 if r == "ABC" else 0) for r in STEP1}
assert STEP2 == {"A": 1, "B": 1, "C": 1, "AB": 1, "AC": 1, "BC": 1, "ABC": 0}
assert all(v == 1 for v in STEP3.values())
# chu kỳ 30: trong 1..30 có 8 số không chia hết cho 2, 3, 5
assert sum(1 for k in range(1, 31) if k % 2 and k % 3 and k % 5) == 8
# tổng quát: một phần tử thuộc đúng m tập được đếm sum_{j>=1} (-1)^{j+1} C(m,j) = 1 lần
from math import comb
for m in range(1, 10):
    assert sum((-1) ** (j + 1) * comb(m, j) for j in range(1, m + 1)) == 1
assert 2 ** 4 - 1 == 15
from itertools import permutations
DER = ["".join(p) for p in permutations("ABC") if all(p[i] != "ABC"[i] for i in range(3))]
assert DER == ["BCA", "CAB"] and 6 - 3 * 2 + 3 * 1 - 1 == 2
DER4 = sum(1 for p in permutations(range(4)) if all(p[i] != i for i in range(4)))
assert DER4 == 24 - 4 * 6 + 6 * 2 - 4 * 1 + 1 == 9

# bài tập: 1..1000 không chia hết cho 3, 5, 7
T357 = [1000 // d for d in (3, 5, 7, 15, 21, 35, 105)]
assert T357 == [333, 200, 142, 66, 47, 28, 9]
assert 333 + 200 + 142 - 66 - 47 - 28 + 9 == 543
assert sum(1 for k in range(1, 1001) if k % 3 and k % 5 and k % 7) == 457 == 1000 - 543

CA, CB, CC = BLUE, GOLD, GREEN
R = 1.85
CEN = {"A": np.array([-1.05, 3.1, 0]), "B": np.array([1.05, 3.1, 0]), "C": np.array([0, 1.25, 0])}
LPOS = {"A": [-1.85, 3.55, 0], "B": [1.85, 3.55, 0], "C": [0, 0.45, 0], "AB": [0, 3.85, 0],
        "AC": [-1.2, 1.85, 0], "BC": [1.2, 1.85, 0], "ABC": [0, 2.5, 0]}


def circ(name, col, center):
    return Circle(radius=R, color=col, stroke_width=5, fill_color=col, fill_opacity=0.12).move_to(center)


def region_labels(vals, color=WHITE, size=34):
    return {r: Text(str(v), font=FONT, font_size=size, color=color).move_to(LPOS[r]) for r, v in vals.items()}


class InclExcl(Scene):
    def wait(self, duration=1.0, **kw):
        super().wait(duration * 1.7, **kw)

    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Đếm không trùng", 44)
        t1 = Text("Nguyên lý\nbù trừ", font=FONT, font_size=84, color=GOLD, line_spacing=1.0).move_to([0, 1.5, 0])
        t2 = para("Cộng các tập, trừ phần đếm trùng,\ncộng lại phần bị trừ quá tay", 32, y=-1.3)
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. Hai tập =====
        c = swap_cap(self, c, cap("Hai tập hợp", 44, GOLD))
        q = para("Lớp 50 sinh viên: 30 học tiếng Anh, 20 học tiếng Pháp,\n10 học cả hai. Bao nhiêu bạn học ít nhất một môn?", 26, WHITE, y=5.2)
        self.play(FadeIn(q), run_time=0.7)
        ca = circ("A", CA, [-1.0, 2.2, 0])
        cb = circ("B", CB, [1.0, 2.2, 0])
        la = Text("Anh", font=FONT, font_size=30, color=CA).move_to([-2.6, 4.3, 0])
        lb = Text("Pháp", font=FONT, font_size=30, color=CB).move_to([2.6, 4.3, 0])
        self.play(Create(ca), Create(cb), FadeIn(la), FadeIn(lb), run_time=1.0)
        n_a = Text("20", font=FONT, font_size=40).move_to([-1.9, 2.2, 0])
        n_ab = Text("10", font=FONT, font_size=40, color=RED).move_to([0, 2.2, 0])
        n_b = Text("10", font=FONT, font_size=40).move_to([1.9, 2.2, 0])
        self.play(FadeIn(n_a), FadeIn(n_ab), FadeIn(n_b), run_time=0.6)
        s1 = para("30 + 20 = 50?", 36, WHITE, y=-0.4)
        self.play(FadeIn(s1), run_time=0.5)
        self.wait(1.2)
        lens = Intersection(ca, cb, color=RED, fill_color=RED, fill_opacity=0.45, stroke_width=0)
        s2 = para("Sai: 10 bạn ở phần giao bị đếm hai lần,\nmột lần trong 30, một lần trong 20", 28, RED, y=-1.6)
        self.play(FadeIn(lens), FadeIn(s2), run_time=0.7)
        self.wait(3.0)
        s3 = para("|A ∪ B| = |A| + |B| − |A ∩ B| = 30 + 20 − 10 = 40", 28, GOLD, y=-3.0)
        self.play(FadeIn(s3), FadeOut(lens), run_time=0.7)
        self.wait(2.5)
        s4 = para("Còn 50 − 40 = 10 bạn không học môn nào", 26, DIM, y=-4.0)
        self.play(FadeIn(s4), run_time=0.5)
        self.wait(2.5)
        wipe(self, keep=[c])

        # ===== 3. Ba tập: mỗi vùng được đếm bao nhiêu lần =====
        c = swap_cap(self, c, cap("Ba tập: mỗi vùng bị đếm mấy lần?", 38, GOLD))
        cs = {k: circ(k, col, CEN[k]) for k, col in zip("ABC", (CA, CB, CC))}
        nm = {"A": Text("A", font=FONT, font_size=34, color=CA).move_to(CEN["A"] + np.array([-1.7, 1.4, 0])),
              "B": Text("B", font=FONT, font_size=34, color=CB).move_to(CEN["B"] + np.array([1.7, 1.4, 0])),
              "C": Text("C", font=FONT, font_size=34, color=CC).move_to(CEN["C"] + np.array([1.9, -1.1, 0]))}
        self.play(*[Create(x) for x in cs.values()], *[FadeIn(x) for x in nm.values()], run_time=1.0)
        f1 = para("Bước 1:  |A| + |B| + |C|", 30, WHITE, y=-1.4)
        lab = region_labels(STEP1)
        self.play(FadeIn(f1), *[FadeIn(l) for l in lab.values()], run_time=0.8)
        for r in ("AB", "AC", "BC"):
            lab[r].set_color(RED)
        lab["ABC"].set_color(RED)
        e1 = para("Phần giao đôi bị đếm 2 lần, phần giữa 3 lần", 26, RED, y=-2.1)
        self.play(FadeIn(e1), run_time=0.5)
        self.wait(3.0)
        f2 = para("Bước 2:  − |A∩B| − |A∩C| − |B∩C|", 30, WHITE, y=-3.0)
        lab2 = region_labels(STEP2)
        lab2["ABC"].set_color(RED)
        self.play(FadeIn(f2), *[Transform(lab[r], lab2[r]) for r in lab], run_time=0.9)
        e2 = para("Phần giữa bị trừ 3 lần: giờ thành 0", 26, RED, y=-3.7)
        self.play(FadeIn(e2), run_time=0.5)
        self.wait(3.0)
        f3 = para("Bước 3:  + |A∩B∩C|", 30, WHITE, y=-4.6)
        lab3 = region_labels(STEP3, GREEN)
        self.play(FadeIn(f3), *[Transform(lab[r], lab3[r]) for r in lab], run_time=0.9)
        e3 = para("Mọi vùng đều được đếm đúng 1 lần ✓", 28, GREEN, y=-5.3)
        self.play(FadeIn(e3), run_time=0.5)
        self.wait(3.5)
        self.play(*[FadeOut(m) for m in [f1, f2, f3, e1, e2, e3]], *[FadeOut(l) for l in lab.values()], run_time=0.5)
        frm = VGroup(Text("|A ∪ B ∪ C| = |A| + |B| + |C|", font=FONT, font_size=30),
                     Text("− |A∩B| − |A∩C| − |B∩C|", font=FONT, font_size=30, color=RED),
                     Text("+ |A∩B∩C|", font=FONT, font_size=30, color=GREEN)).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([0, -2.4, 0])
        self.play(FadeIn(frm), run_time=0.8)
        self.wait(4.0)
        wipe(self, keep=[c])

        # ===== 4. Ví dụ chia hết =====
        c = swap_cap(self, c, cap("Từ 1 đến 100: chia hết cho 2, 3 hoặc 5?", 34, GOLD))
        cs = {k: circ(k, col, CEN[k]) for k, col in zip("ABC", (CA, CB, CC))}
        nm = {"A": Text("chia hết 2", font=FONT, font_size=24, color=CA).move_to(CEN["A"] + np.array([-1.6, 2.05, 0])),
              "B": Text("chia hết 3", font=FONT, font_size=24, color=CB).move_to(CEN["B"] + np.array([1.6, 2.05, 0])),
              "C": Text("chia hết 5", font=FONT, font_size=24, color=CC).move_to(CEN["C"] + np.array([2.6, -1.3, 0]))}
        self.play(*[Create(x) for x in cs.values()], *[FadeIn(x) for x in nm.values()], run_time=1.0)
        rows = [("|A| = ⌊100/2⌋ = 50", "|A∩B| = ⌊100/6⌋ = 16"),
                ("|B| = ⌊100/3⌋ = 33", "|A∩C| = ⌊100/10⌋ = 10"),
                ("|C| = ⌊100/5⌋ = 20", "|B∩C| = ⌊100/15⌋ = 6")]
        tb = VGroup()
        for i, (l, r) in enumerate(rows):
            tb.add(Text(l, font=FONT, font_size=26).move_to([-2.0, -1.3 - i * 0.55, 0]))
            tb.add(Text(r, font=FONT, font_size=26, color=RED).move_to([2.0, -1.3 - i * 0.55, 0]))
        fitw(tb)
        for i in range(3):
            self.play(FadeIn(tb[2 * i]), run_time=0.5)
            self.wait(0.6)
        n1 = para("Chia hết cho cả 2 và 3 ⇔ chia hết cho 6 (vì 2, 3 nguyên tố cùng nhau)", 22, DIM, y=-3.0)
        self.play(FadeIn(n1), run_time=0.5)
        for i in range(3):
            self.play(FadeIn(tb[2 * i + 1]), run_time=0.5)
            self.wait(0.6)
        t3 = para("|A∩B∩C| = ⌊100/30⌋ = 3", 26, GREEN, y=-3.7)
        self.play(FadeIn(t3), run_time=0.5)
        self.wait(1.5)
        tot = para("50 + 33 + 20 − 16 − 10 − 6 + 3 = 74", 36, GOLD, y=-4.8)
        self.play(FadeIn(tot), run_time=0.7)
        self.wait(2.0)
        lab = region_labels(REG, WHITE, 32)
        rn = para("Số phần tử từng vùng (cộng lại vẫn là 74)", 24, DIM, y=-5.6)
        self.play(*[FadeIn(l) for l in lab.values()], FadeIn(rn), run_time=0.8)
        self.wait(4.0)
        wipe(self, keep=[c])

        # ===== 5. Lưới 1..100 =====
        c = swap_cap(self, c, cap("Kiểm tra trên lưới 1…100", 40, GOLD))
        g = VGroup()
        for k in range(1, 101):
            r, cc = divmod(k - 1, 10)
            sq = Square(0.7, stroke_width=1.5, color=DIM).move_to([-3.15 + cc * 0.7, 5.0 - r * 0.7, 0])
            t = Text(str(k), font=FONT, font_size=18, color=WHITE).move_to(sq)
            g.add(VGroup(sq, t))
        self.play(FadeIn(g, lag_ratio=0.005), run_time=1.2)
        anims = []
        for k in range(1, 101):
            if k in U:
                col = CA if k in A else (CB if k in B else CC)
                anims.append(g[k - 1][0].animate.set_fill(col, 0.45))
        self.play(LaggedStart(*anims, lag_ratio=0.01), run_time=2.5)
        cnt = para("74 ô được tô, 26 ô còn trống", 32, GOLD, y=-2.6)
        self.play(FadeIn(cnt), run_time=0.6)
        self.wait(2.0)
        cp = para("Dạng bù: 100 − 74 = 26 số không chia hết\ncho số nào trong 2, 3, 5", 26, WHITE, y=-3.9)
        self.play(FadeIn(cp), run_time=0.6)
        self.wait(2.0)
        p = para("Mỗi 30 số liên tiếp có đúng 8 số như vậy:\n1, 7, 11, 13, 17, 19, 23, 29", 26, DIM, y=-5.3)
        assert [k for k in range(1, 31) if k % 2 and k % 3 and k % 5] == [1, 7, 11, 13, 17, 19, 23, 29]
        self.play(FadeIn(p), run_time=0.6)
        self.wait(4.0)
        wipe(self, keep=[c])

        # ===== 5b. Bài tập 1..1000 =====
        c = swap_cap(self, c, cap("Bài tập: từ 1 đến 1000", 42, GOLD))
        q = para("Có bao nhiêu số từ 1 đến 1000\nkhông chia hết cho 3, 5 và 7?", 30, WHITE, y=5.0)
        self.play(FadeIn(q), run_time=0.6)
        self.wait(2.0)
        h = para("Đếm phần bù: số chia hết cho ÍT NHẤT một trong ba số.\nSố bội của d trong 1..1000 là ⌊1000/d⌋", 24, DIM, y=3.6)
        self.play(FadeIn(h), run_time=0.5)
        self.wait(2.0)
        terms = [("+ ⌊1000/3⌋ + ⌊1000/5⌋ + ⌊1000/7⌋", "= 333 + 200 + 142 = 675", WHITE),
                 ("− ⌊1000/15⌋ − ⌊1000/21⌋ − ⌊1000/35⌋", "= 66 + 47 + 28 = 141", RED),
                 ("+ ⌊1000/105⌋", "= 9", GREEN)]
        y = 2.2
        for a_, b_, col in terms:
            ta = Text(a_, font=FONT, font_size=26, color=col)
            tb = Text(b_, font=FONT, font_size=26, color=col)
            g = VGroup(ta, tb).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
            fitw(g).move_to([-3.7, y, 0], aligned_edge=UL)
            self.play(FadeIn(g, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(1.6)
            y -= g.height + 0.35
        u = para("Chia hết cho ít nhất một số: 675 − 141 + 9 = 543", 26, GOLD, y=-1.6)
        self.play(FadeIn(u), run_time=0.5)
        self.wait(1.5)
        r = para("Không chia hết: 1000 − 543 = 457", 36, GOLD, y=-2.8)
        self.play(FadeIn(r, scale=1.2), run_time=0.6)
        self.wait(1.5)
        n = para("Lưu ý: 15, 21, 35, 105 là bội chung nhỏ nhất,\nđúng vì 3, 5, 7 đôi một nguyên tố cùng nhau", 22, DIM, y=-4.2)
        self.play(FadeIn(n), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 6. Tổng quát =====
        c = swap_cap(self, c, cap("Với n tập hợp", 44, GOLD))
        gl = VGroup(*[Text(s, font=FONT, font_size=30, color=col) for s, col in [
            ("+ tổng các tập đơn", WHITE),
            ("− tổng các giao đôi", RED),
            ("+ tổng các giao ba", GREEN),
            ("− tổng các giao bốn", RED),
            ("…  dấu đổi luân phiên", DIM),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.38).move_to([0, 3.6, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.2) for m in gl], lag_ratio=0.4), run_time=2.4)
        self.wait(2.0)
        w = para("Phần tử thuộc đúng m tập được đếm\nC(m,1) − C(m,2) + C(m,3) − … = 1 lần", 28, WHITE, y=0.2)
        self.play(FadeIn(w), run_time=0.6)
        self.wait(3.0)
        nt = para("n tập cho 2ⁿ − 1 số hạng: 4 tập đã là 15 số hạng", 26, DIM, y=-1.6)
        self.play(FadeIn(nt), run_time=0.5)
        self.wait(2.5)
        self.wait(1.0)
        wipe(self, keep=[c])

        # ===== 7. Ứng dụng: không ai nhận đúng thư =====
        c = swap_cap(self, c, cap("Ứng dụng: không lá thư nào đúng chỗ", 36, GOLD))
        q = para("3 lá thư A, B, C bỏ ngẫu nhiên vào 3 phong bì A, B, C.\nCó bao nhiêu cách để không lá nào vào đúng phong bì?", 26, WHITE, y=5.2)
        self.play(FadeIn(q), run_time=0.7)
        self.wait(1.5)
        d1 = para("Xét các cách có thư i nằm đúng phong bì i", 26, DIM, y=4.1)
        self.play(FadeIn(d1), run_time=0.5)
        self.wait(1.5)
        lines = VGroup(*[Text(s, font=FONT, font_size=28, color=col) for s, col in [
            ("Tất cả:  3! = 6", WHITE),
            ("− một thư đúng chỗ:  C(3,1)·2! = 6", RED),
            ("+ hai thư đúng chỗ:  C(3,2)·1! = 3", GREEN),
            ("− cả ba đúng chỗ:  C(3,3)·0! = 1", RED),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to([0, 2.0, 0])
        for m in lines:
            self.play(FadeIn(m, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(1.2)
        r = para("6 − 6 + 3 − 1 = 2", 40, GOLD, y=-0.1)
        self.play(FadeIn(r), run_time=0.6)
        self.wait(1.0)
        boxes = VGroup()
        for k, w in enumerate(DER):
            row = VGroup()
            for i, ch in enumerate(w):
                env = Rectangle(width=1.0, height=0.7, color=DIM, stroke_width=2).move_to([-3.0 + k * 3.6 + i * 1.1, -1.6, 0])
                el = Text("ABC"[i], font=FONT, font_size=18, color=DIM).next_to(env, DOWN, buff=0.1)
                lt = Text(ch, font=FONT, font_size=30, color=GOLD).move_to(env)
                row.add(VGroup(env, el, lt))
            boxes.add(row)
        boxes.move_to([0, -1.75, 0])
        self.play(LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.4), run_time=1.2)
        lst = para("Chỉ có BCA và CAB  ✓   (với 4 lá thư: 9 cách)", 26, WHITE, y=-2.9)
        self.play(FadeIn(lst), run_time=0.5)
        self.wait(2.5)
        ap = para("Bù trừ còn dùng để đếm số không chia hết, mật khẩu\nthiếu loại ký tự, số toàn ánh giữa hai tập…", 24, DIM, y=-4.4)
        self.play(FadeIn(ap), run_time=0.6)
        self.wait(4.0)
