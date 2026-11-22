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


# ---------- Phần mở rộng: phương trình đặc trưng, Binet, nghiệm kép ----------
PSI = (1 - sqrt(5)) / 2
assert abs(PHI * PHI - (PHI + 1)) < 1e-12 and abs(PSI * PSI - (PSI + 1)) < 1e-12
assert abs(PHI - PSI - sqrt(5)) < 1e-12 and abs(PHI + PSI - 1) < 1e-12 and abs(PHI * PSI + 1) < 1e-12
F0 = [0, 1]
while len(F0) < 41:
    F0.append(F0[-1] + F0[-2])
A_, B_ = 1 / sqrt(5), -1 / sqrt(5)
assert abs(A_ + B_) < 1e-12 and abs(A_ * PHI + B_ * PSI - 1) < 1e-12
for n in range(0, 41):
    assert round(A_ * PHI ** n + B_ * PSI ** n) == F0[n]
    assert round(PHI ** n / sqrt(5)) == F0[n] or n == 0
assert F0[10] == 55 and F0[20] == 6765
assert "%.2f" % (PHI ** 10) == "122.99" and "%.4f" % (PSI ** 10) == "0.0081"
assert "%.3f" % (PHI ** 10 / sqrt(5)) == "55.004" and "%.2f" % (PHI ** 5 / sqrt(5)) == "4.96"
# nghiệm kép: a_n = 4a_{n-1} - 4a_{n-2}, a0 = 1, a1 = 6  ->  a_n = (1 + 2n) 2^n
AK = [1, 6]
while len(AK) < 10:
    AK.append(4 * AK[-1] - 4 * AK[-2])
assert AK[:5] == [1, 6, 20, 56, 144]
assert all(AK[n] == (1 + 2 * n) * 2 ** n for n in range(10))
assert 1 * 2 ** 1 != 6          # dạng C·2^n với C = a0 = 1 cho a1 = 2 ≠ 6


def ratio_str(n):
    return "%.10f" % (FIB[n] / FIB[n - 1])


def ratio_text(n, y):
    s = ratio_str(n).replace(".", ",")
    t = Text(s, font=FONT, font_size=50).move_to([0.9, y, 0])
    m = 0
    for a, b in zip(s, PHI_STR.replace(".", ",")):
        if a != b:
            break
        m += 1
    for i in range(len(t)):
        t[i].set_color(GOLD if i < m else WHITE)
    return t


class Fibonacci(Scene):
    def wait(self, duration=1.0, **kw):
        super().wait(duration * 1.5, **kw)

    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Truy hồi tuyến tính", 44)
        t1 = Text("Fibonacci", font=FONT, font_size=90, color=GOLD).move_to([0, 1.5, 0])
        t2 = para("Từ hình xoắn ốc, tỉ lệ vàng\nđến công thức Binet", 34, y=-0.6)
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. Hình vuông và xoắn ốc (giữ từ bản cũ) =====
        c = swap_cap(self, c, cap("Ghép hình vuông cạnh F(n)", 40, GOLD))
        sq, (rx0, ry0, rx1, ry1) = build_squares()
        cx, cy = (rx0 + rx1) / 2, (ry0 + ry1) / 2
        ORG = np.array([0, 1.3, 0])

        def P(x, y):
            return ORG + np.array([(x - cx) * SC, (y - cy) * SC, 0])
        pal = ["#6cb6ff", "#8fd694", "#f5c542", "#ff9f6b", "#c792ea", "#6cb6ff", "#8fd694", "#f5c542", "#ff9f6b"]
        sqs, labs = [], []
        for i, (x, y, s) in enumerate(sq):
            m = Square(s * SC, color=pal[i], stroke_width=3, fill_color=pal[i], fill_opacity=0.18).move_to(P(x + s / 2, y + s / 2))
            sqs.append(m)
            labs.append(Text(str(FIB[i]), font=FONT, font_size=int(min(44, 14 + 26 * s * SC / 2))).move_to(m) if s * SC > 0.45 else None)
        seq = para("1, 1, 2, 3, 5, 8, 13, 21, 34, 55, …", 36, WHITE, y=5.3)
        rule = para("F(n) = F(n−1) + F(n−2)", 34, GOLD, y=4.6)
        self.play(Write(seq), run_time=1.0)
        self.play(FadeIn(rule), run_time=0.6)
        arcs = []
        for ctr, r, st, en in spiral(sq):
            a0 = np.arctan2((st - ctr)[1], (st - ctr)[0])
            a1 = np.arctan2((en - ctr)[1], (en - ctr)[0])
            da = (a1 - a0 + np.pi) % (2 * np.pi) - np.pi
            arcs.append(Arc(radius=r * SC, start_angle=a0, angle=da, arc_center=P(*ctr), color=WHITE, stroke_width=5))
        for i in range(NSQ):
            an = [FadeIn(sqs[i], scale=0.6), Create(arcs[i])]
            if labs[i] is not None:
                an.append(FadeIn(labs[i]))
            self.play(*an, run_time=max(0.4, 1.0 - 0.08 * i))
        n1 = para("Mỗi hình vuông mới có cạnh bằng tổng hai cạnh trước", 26, DIM, y=-3.4)
        self.play(FadeIn(n1), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 3. Tỉ số =====
        c = swap_cap(self, c, cap("Tỉ số hai số liên tiếp", 40, GOLD))
        lab = para("F(n+1) / F(n) =", 40, WHITE, y=3.0)
        nl = para("n = 1", 32, DIM, y=1.9)
        rt = ratio_text(1, 0.8)
        self.play(FadeIn(lab), FadeIn(nl), FadeIn(rt), run_time=0.6)
        steps = [2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 20, 25, 30, 39]
        for n in steps:
            self.play(Transform(rt, ratio_text(n, 0.8)), Transform(nl, para(f"n = {n}", 32, DIM, y=1.9)), run_time=0.45 if n < 9 else 0.35)
            self.wait(0.35 if n < 9 else 0.2)
        ph = para("φ = (1 + √5)/2 = 1,6180339887…", 34, GOLD, y=-0.8)
        self.play(FadeIn(ph), run_time=0.6)
        q = para("Vì sao lại ra đúng số này?\nCâu trả lời nằm ở phương trình đặc trưng.", 30, WHITE, y=-2.6)
        self.play(FadeIn(q), run_time=0.6)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 4. Phương trình đặc trưng =====
        c = swap_cap(self, c, cap("Phương trình đặc trưng", 42, GOLD))
        lines = [
            ("Thử nghiệm dạng F(n) = rⁿ  (r ≠ 0):", DIM),
            ("rⁿ = rⁿ⁻¹ + rⁿ⁻²", WHITE),
            ("Chia hai vế cho rⁿ⁻²:", DIM),
            ("r² = r + 1", GOLD),
        ]
        ys = [5.0, 4.2, 3.3, 2.5]
        objs = []
        for (s, col), y in zip(lines, ys):
            m = para(s, 40 if col is not DIM else 28, col, y=y)
            self.play(FadeIn(m), run_time=0.6)
            objs.append(m)
            self.wait(1.6)
        ax = Axes(x_range=[-1.5, 2.5, 1], y_range=[-1.5, 3, 1], x_length=6.4, y_length=3.6,
                  axis_config={"color": DIM, "stroke_width": 2, "include_tip": False}).move_to([0, -0.9, 0])
        curve = ax.plot(lambda x: x * x - x - 1, x_range=[-1.4, 2.4], color=BLUE, stroke_width=5)
        cl = para("y = r² − r − 1", 26, BLUE, y=1.0)
        self.play(Create(ax), run_time=0.6)
        self.play(Create(curve), FadeIn(cl), run_time=1.0)
        d1 = Dot(ax.c2p(PHI, 0), color=GOLD, radius=0.11)
        d2 = Dot(ax.c2p(PSI, 0), color=GREEN, radius=0.11)
        l1 = Text("φ ≈ 1,618", font=FONT, font_size=26, color=GOLD).next_to(d1, DOWN, buff=0.25)
        l2 = Text("ψ ≈ −0,618", font=FONT, font_size=26, color=GREEN).next_to(d2, DOWN, buff=0.25)
        self.play(GrowFromCenter(d1), GrowFromCenter(d2), FadeIn(l1), FadeIn(l2), run_time=0.8)
        roots = para("Hai nghiệm:  φ = (1 + √5)/2,   ψ = (1 − √5)/2", 28, WHITE, y=-3.6)
        self.play(FadeIn(roots), run_time=0.6)
        self.wait(2.0)
        lin = para("Truy hồi tuyến tính nên mọi tổ hợp\nF(n) = A·φⁿ + B·ψⁿ  đều thỏa F(n) = F(n−1) + F(n−2)", 28, GOLD, y=-5.0)
        self.play(FadeIn(lin), run_time=0.7)
        self.wait(4.0)
        wipe(self, keep=[c])

        # ===== 5. Tìm hằng số -> Binet =====
        c = swap_cap(self, c, cap("Tìm A, B từ điều kiện đầu", 40, GOLD))
        g = VGroup(*[Text(s, font=FONT, font_size=32, color=col) for s, col in [
            ("F₀ = 0:   A + B = 0", WHITE),
            ("F₁ = 1:   A·φ + B·ψ = 1", WHITE),
            ("Thay B = −A:   A(φ − ψ) = 1", DIM),
            ("φ − ψ = √5   ⇒   A = 1/√5,   B = −1/√5", WHITE),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        fitw(g).move_to([0, 3.6, 0])
        for m in g:
            self.play(FadeIn(m, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(1.8)
        bn = para("F(n) = (φⁿ − ψⁿ) / √5", 52, GOLD, y=0.6)
        bl = para("Công thức Binet", 28, DIM, y=-0.65)
        box = SurroundingRectangle(bn, color=GOLD, buff=0.25, corner_radius=0.15)
        self.play(Write(bn), run_time=1.0)
        self.play(Create(box), FadeIn(bl), run_time=0.6)
        self.wait(2.0)
        ck = para("Thử n = 10:  (122,99 − 0,0081) / 2,2361 = 55,000  ✓", 28, WHITE, y=-1.6)
        self.play(FadeIn(ck), run_time=0.6)
        self.wait(2.5)
        why = para("Số vô tỉ cộng trừ với nhau mà ra đúng số nguyên!", 26, DIM, y=-2.5)
        self.play(FadeIn(why), run_time=0.5)
        self.wait(2.5)
        wipe(self, keep=[c])

        # ===== 6. Vì sao tỉ số -> phi =====
        c = swap_cap(self, c, cap("Vì sao F(n+1)/F(n) → φ?", 42, GOLD))
        a1 = para("|ψ| ≈ 0,618 < 1  nên  ψⁿ → 0", 34, GREEN, y=4.6)
        a2 = para("F(n) ≈ φⁿ / √5   (làm tròn là ra đúng F(n))", 32, WHITE, y=3.6)
        self.play(FadeIn(a1), run_time=0.6)
        self.wait(1.8)
        self.play(FadeIn(a2), run_time=0.6)
        self.wait(1.8)
        rows = [("n", "φⁿ/√5", "F(n)"), ("5", "4,96", "5"), ("10", "55,004", "55"), ("20", "6765,00003", "6765")]
        tb = VGroup()
        for i, r in enumerate(rows):
            for j, s in enumerate(r):
                tb.add(Text(s, font=FONT, font_size=30, color=BLUE if i == 0 else (GOLD if j == 2 else WHITE)).move_to([-2.6 + j * 2.5, 2.2 - i * 0.65, 0]))
        assert "%.5f" % (PHI ** 20 / sqrt(5)) == "6765.00003"
        self.play(LaggedStart(*[FadeIn(m) for m in tb], lag_ratio=0.05), run_time=1.4)
        self.wait(2.5)
        a3 = para("F(n+1) / F(n) ≈ φⁿ⁺¹ / φⁿ = φ", 40, GOLD, y=-1.2)
        self.play(FadeIn(a3), run_time=0.7)
        self.wait(2.0)
        a4 = para("Đó là lý do các chữ số vàng ở phần trước ổn định dần.", 26, DIM, y=-2.3)
        self.play(FadeIn(a4), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 7. Nghiệm kép =====
        c = swap_cap(self, c, cap("Khi phương trình có nghiệm kép", 38, GOLD))
        e = para("a(n) = 4a(n−1) − 4a(n−2),   a₀ = 1,   a₁ = 6", 32, WHITE, y=5.0)
        self.play(FadeIn(e), run_time=0.6)
        self.wait(1.5)
        ce = para("r² − 4r + 4 = (r − 2)² = 0   →   r = 2 (kép)", 30, GOLD, y=4.1)
        self.play(FadeIn(ce), run_time=0.6)
        self.wait(2.0)
        w1 = para("Thử a(n) = A·2ⁿ + B·2ⁿ = (A + B)·2ⁿ: chỉ còn một hằng số", 26, RED, y=3.0)
        w2 = para("a₀ = 1 ⇒ A + B = 1, nhưng khi đó a₁ = 2 ≠ 6  ✗", 26, RED, y=2.3)
        self.play(FadeIn(w1), run_time=0.6)
        self.wait(2.0)
        self.play(FadeIn(w2), run_time=0.6)
        self.wait(2.5)
        ok = para("Dạng đúng:  a(n) = (A + B·n)·2ⁿ", 34, GREEN, y=1.1)
        self.play(FadeIn(ok), run_time=0.6)
        self.wait(1.5)
        s1 = VGroup(*[Text(s, font=FONT, font_size=30) for s in [
            "a₀ = 1:   A = 1",
            "a₁ = 6:   (1 + B)·2 = 6   ⇒   B = 2",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to([0, -0.4, 0])
        for m in s1:
            self.play(FadeIn(m), run_time=0.6)
            self.wait(1.6)
        res = para("a(n) = (1 + 2n)·2ⁿ", 46, GOLD, y=-2.0)
        self.play(Write(res), run_time=0.9)
        chk = para("Kiểm tra: 1, 6, 20, 56, 144 …  và 4·20 − 4·6 = 56  ✓", 26, DIM, y=-3.1)
        self.play(FadeIn(chk), run_time=0.6)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 8. Tóm tắt =====
        c = swap_cap(self, c, cap("Ba bước giải truy hồi bậc hai", 38, GOLD))
        sm = VGroup(*[Text(s, font=FONT, font_size=30, color=col) for s, col in [
            ("1. Viết phương trình đặc trưng r² = c₁r + c₂", WHITE),
            ("2. Hai nghiệm r₁ ≠ r₂:  a(n) = A·r₁ⁿ + B·r₂ⁿ", BLUE),
            ("    Nghiệm kép r:  a(n) = (A + B·n)·rⁿ", GREEN),
            ("3. Dùng a₀, a₁ để tìm A, B", WHITE),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        sm[2].shift(RIGHT * 0.5)
        fitw(sm, 7.6).move_to([0, 2.6, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.2) for m in sm], lag_ratio=0.45), run_time=2.6)
        self.wait(2.5)
        e2 = para("Fibonacci là trường hợp r² = r + 1:\nhai nghiệm φ, ψ cho ra công thức Binet.", 28, GOLD, y=-1.4)
        self.play(FadeIn(e2), run_time=0.6)
        self.wait(5.0)
