from common import *
from fractions import Fraction as F


def run(rec, init, N):
    a = list(init)
    while len(a) < N:
        a.append(rec(len(a), a))
    return a


# ---------- Toán ----------
C1 = run(lambda n, a: 2 * a[n - 1] + 3, [1], 5)
assert C1 == [1, 5, 13, 29, 61] == [4 * 2 ** n - 3 for n in range(5)]
H = run(lambda n, a: 2 * a[n - 1] + 1, [0], 6)
assert H == [2 ** n - 1 for n in range(6)]
P1 = run(lambda n, a: 2 * a[n - 1] + n, [0], 5)
assert P1 == [0, 1, 4, 11, 26] == [2 ** (n + 1) - n - 2 for n in range(5)]
# p(n) = -n - 2 là nghiệm riêng
assert all((-n - 2) == 2 * (-(n - 1) - 2) + n for n in range(1, 20))
E1 = run(lambda n, a: 3 * a[n - 1] + 2 ** n, [1], 5)
assert E1 == [1, 5, 19, 65, 211] == [3 ** (n + 1) - 2 ** (n + 1) for n in range(5)]
assert all(-2 * 2 ** n == 3 * (-2 * 2 ** (n - 1)) + 2 ** n for n in range(1, 20))
R1 = run(lambda n, a: 2 * a[n - 1] + 2 ** n, [1], 5)
assert R1 == [1, 4, 12, 32, 80] == [(n + 1) * 2 ** n for n in range(5)]
assert all(n * 2 ** n == 2 * (n - 1) * 2 ** (n - 1) + 2 ** n for n in range(1, 20))
G = run(lambda n, a: a[n - 1] + n, [0], 6)
assert G == [n * (n + 1) // 2 for n in range(6)]
X = run(lambda n, a: 2 * a[n - 1] - a[n - 2] + 3 ** n, [1, 3], 5)
assert X[:4] == [1, 3, 14, 52]
D = F(9, 4)
assert 9 * D == 6 * D - D + 9
A, B = F(-5, 4), F(-5, 2)
assert all(A + B * n + D * 3 ** n == X[n] for n in range(5))


class NonHom(Scene):
    def wait(self, duration=1.0, **kw):
        super().wait(duration * 1.85, **kw)

    def check(self, vals, y, label="kiểm tra"):
        """Hàng giá trị kiểm tra a(0..4)."""
        hdr = Text(label, font=FONT, font_size=22, color=DIM).move_to([-3.3, y, 0])
        cells = VGroup()
        for k, v in enumerate(vals):
            r = Rectangle(width=1.0, height=0.62, color=GREEN, stroke_width=2).move_to([-1.9 + k * 1.15, y, 0])
            t = Text(str(v), font=FONT, font_size=26, color=GREEN).move_to(r)
            n = Text(f"n={k}", font=FONT, font_size=18, color=DIM).next_to(r, UP, buff=0.08)
            cells.add(VGroup(r, t, n))
        self.play(FadeIn(hdr), LaggedStart(*[FadeIn(c_) for c_ in cells], lag_ratio=0.15), run_time=1.0)
        return VGroup(hdr, cells)

    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Hệ thức truy hồi không thuần nhất", 36)
        t1 = Text("Thuần nhất\n+ riêng", font=FONT, font_size=80, color=GOLD, line_spacing=1.0).move_to([0, 2.0, 0])
        t2 = para("a(n) = c · a(n−1) + f(n)\nphần f(n) \"thêm vào\" làm bài toán khó hơn", 30, y=-0.8)
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. Chồng chất =====
        c = swap_cap(self, c, cap("Nguyên lý chồng chất", 44, GOLD))
        b1 = para("Nghiệm tổng quát = h(n) + p(n)", 36, GOLD, y=4.8)
        self.play(FadeIn(b1), run_time=0.6)
        b2 = para("h(n): nghiệm tổng quát của phần thuần nhất\na(n) = c · a(n−1)  (bỏ f(n) đi)", 26, BLUE, y=3.3)
        b3 = para("p(n): MỘT nghiệm riêng bất kỳ\ncủa hệ thức đầy đủ (có f(n))", 26, RED, y=1.6)
        self.play(FadeIn(b2), run_time=0.6)
        self.wait(1.5)
        self.play(FadeIn(b3), run_time=0.6)
        self.wait(1.5)
        b4 = para("Vì sao? Nếu a(n) và p(n) cùng thỏa hệ thức đầy đủ\nthì hiệu a(n) − p(n) thỏa phần thuần nhất:\nf(n) bị triệt tiêu khi trừ", 24, WHITE, y=-0.4)
        self.play(FadeIn(b4), run_time=0.6)
        self.wait(2.5)
        b5 = para("Quy trình: tìm h(n) → đoán p(n) → cộng lại\n→ dùng điều kiện đầu để tìm hằng số", 26, GOLD, y=-2.6)
        self.play(FadeIn(b5), run_time=0.6)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 3. f(n) là hằng số =====
        c = swap_cap(self, c, cap("f(n) là hằng số", 44, GOLD))
        e0 = para("a(n) = 2a(n−1) + 3,   a(0) = 1", 32, WHITE, y=5.0)
        self.play(FadeIn(e0), run_time=0.6)
        s1 = para("① Thuần nhất: a(n) = 2a(n−1) ⇒ h(n) = A · 2ⁿ", 26, BLUE, y=3.8)
        self.play(FadeIn(s1), run_time=0.6)
        self.wait(1.5)
        s2 = para("② Đoán p(n) = C (hằng số):\nC = 2C + 3 ⇒ C = −3", 26, RED, y=2.5)
        self.play(FadeIn(s2), run_time=0.6)
        self.wait(1.8)
        s3 = para("③ a(n) = A · 2ⁿ − 3;  a(0) = 1 ⇒ A − 3 = 1 ⇒ A = 4", 26, WHITE, y=1.2)
        self.play(FadeIn(s3), run_time=0.6)
        self.wait(1.5)
        s4 = para("a(n) = 4 · 2ⁿ − 3", 40, GOLD, y=0.1)
        self.play(FadeIn(s4, scale=1.2), run_time=0.6)
        self.wait(1.0)
        ck = self.check(C1, -1.4)
        s5 = para("Truy hồi: 1, 2·1+3 = 5, 2·5+3 = 13, …\nkhớp công thức ✓", 24, GREEN, y=-2.6)
        self.play(FadeIn(s5), run_time=0.5)
        self.wait(2.0)
        s6 = para("Tháp Hà Nội: H(n) = 2H(n−1) + 1, H(0) = 0\nđoán p = C ⇒ C = −1 ⇒ H(n) = 2ⁿ − 1", 26, BLUE, y=-4.3)
        self.play(FadeIn(s6), run_time=0.6)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 4. f(n) là đa thức =====
        c = swap_cap(self, c, cap("f(n) là đa thức", 44, GOLD))
        e0 = para("a(n) = 2a(n−1) + n,   a(0) = 0", 32, WHITE, y=5.0)
        self.play(FadeIn(e0), run_time=0.6)
        s1 = para("① h(n) = A · 2ⁿ", 26, BLUE, y=3.9)
        self.play(FadeIn(s1), run_time=0.5)
        s2 = para("② f(n) = n bậc 1 ⇒ đoán p(n) = Bn + C", 26, RED, y=2.9)
        self.play(FadeIn(s2), run_time=0.6)
        self.wait(1.5)
        s3 = para("Bn + C = 2(B(n−1) + C) + n = (2B + 1)n + (2C − 2B)", 24, WHITE, y=1.9)
        self.play(FadeIn(s3), run_time=0.6)
        self.wait(2.0)
        s4 = para("So hệ số của n:  B = 2B + 1 ⇒ B = −1\nSo hệ số tự do:  C = 2C − 2B ⇒ C = −2", 26, WHITE, y=0.6)
        self.play(FadeIn(s4), run_time=0.6)
        self.wait(2.0)
        s5 = para("p(n) = −n − 2;  a(0) = A − 2 = 0 ⇒ A = 2", 26, RED, y=-0.6)
        self.play(FadeIn(s5), run_time=0.6)
        self.wait(1.2)
        s6 = para("a(n) = 2ⁿ⁺¹ − n − 2", 40, GOLD, y=-1.6)
        self.play(FadeIn(s6, scale=1.2), run_time=0.6)
        ck = self.check(P1, -3.0)
        s7 = para("Truy hồi: 0 → 2·0+1 = 1 → 2·1+2 = 4\n→ 2·4+3 = 11 ✓", 24, GREEN, y=-4.3)
        self.play(FadeIn(s7), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 5. f(n) là hàm mũ =====
        c = swap_cap(self, c, cap("f(n) là hàm mũ", 44, GOLD))
        e0 = para("a(n) = 3a(n−1) + 2ⁿ,   a(0) = 1", 32, WHITE, y=5.0)
        self.play(FadeIn(e0), run_time=0.6)
        s1 = para("① h(n) = A · 3ⁿ", 26, BLUE, y=3.9)
        s2 = para("② Đoán p(n) = D · 2ⁿ (cùng cơ số với f)", 26, RED, y=2.9)
        self.play(FadeIn(s1), run_time=0.5)
        self.play(FadeIn(s2), run_time=0.6)
        self.wait(1.5)
        s3 = para("D · 2ⁿ = 3D · 2ⁿ⁻¹ + 2ⁿ\nchia cho 2ⁿ⁻¹:  2D = 3D + 2 ⇒ D = −2", 26, WHITE, y=1.6)
        self.play(FadeIn(s3), run_time=0.6)
        self.wait(2.0)
        s4 = para("a(n) = A · 3ⁿ − 2ⁿ⁺¹;  a(0) = A − 2 = 1 ⇒ A = 3", 26, WHITE, y=0.2)
        self.play(FadeIn(s4), run_time=0.6)
        self.wait(1.2)
        s5 = para("a(n) = 3ⁿ⁺¹ − 2ⁿ⁺¹", 40, GOLD, y=-0.9)
        self.play(FadeIn(s5, scale=1.2), run_time=0.6)
        ck = self.check(E1, -2.4)
        s6 = para("Truy hồi: 3·1+2 = 5, 3·5+4 = 19,\n3·19+8 = 65 ✓", 24, GREEN, y=-3.7)
        self.play(FadeIn(s6), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 6. Cộng hưởng =====
        c = swap_cap(self, c, cap("Trường hợp cộng hưởng", 44, RED))
        e0 = para("a(n) = 2a(n−1) + 2ⁿ,   a(0) = 1", 32, WHITE, y=5.0)
        self.play(FadeIn(e0), run_time=0.6)
        s1 = para("h(n) = A · 2ⁿ — cùng cơ số 2 với f(n)!", 26, BLUE, y=3.9)
        self.play(FadeIn(s1), run_time=0.6)
        self.wait(1.2)
        s2 = para("Thử p(n) = D · 2ⁿ:  D · 2ⁿ = D · 2ⁿ + 2ⁿ ⇒ 0 = 2ⁿ ✗", 26, RED, y=2.8)
        self.play(FadeIn(s2), run_time=0.6)
        self.wait(1.5)
        s3 = para("D · 2ⁿ đã là nghiệm thuần nhất, nên vế trái\nkhông bao giờ \"tạo ra\" được phần 2ⁿ thêm vào", 24, DIM, y=1.7)
        self.play(FadeIn(s3), run_time=0.6)
        self.wait(2.0)
        s4 = para("Sửa: nhân thêm n ⇒ p(n) = D · n · 2ⁿ", 28, GOLD, y=0.5)
        self.play(FadeIn(s4), run_time=0.6)
        self.wait(1.2)
        s5 = para("Dn2ⁿ = 2D(n−1)2ⁿ⁻¹ + 2ⁿ = D(n−1)2ⁿ + 2ⁿ\n⇒ Dn = Dn − D + 1 ⇒ D = 1", 24, WHITE, y=-0.7)
        self.play(FadeIn(s5), run_time=0.6)
        self.wait(2.0)
        s6 = para("a(n) = A2ⁿ + n2ⁿ, a(0) = 1 ⇒ A = 1 ⇒ a(n) = (n + 1) · 2ⁿ", 26, GOLD, y=-1.9)
        self.play(FadeIn(s6), run_time=0.6)
        ck = self.check(R1, -3.3)
        s7 = para("Tương tự a(n) = a(n−1) + n, a(0) = 0:\nh là hằng số (r = 1), f là đa thức ⇒ nhân n:\np(n) = n(Bn + C) ⇒ a(n) = n(n + 1)/2", 24, BLUE, y=-5.0)
        self.play(FadeIn(s7), run_time=0.6)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 7. Bậc hai =====
        c = swap_cap(self, c, cap("Hệ thức bậc hai", 44, GOLD))
        e0 = para("X(n) = 2X(n−1) − X(n−2) + 3ⁿ\nX(0) = 1, X(1) = 3", 30, WHITE, y=4.9)
        self.play(FadeIn(e0), run_time=0.6)
        s1 = para("① r² − 2r + 1 = 0: nghiệm kép r = 1 ⇒ h(n) = A + Bn", 24, BLUE, y=3.5)
        self.play(FadeIn(s1), run_time=0.6)
        self.wait(1.5)
        s2 = para("② 3 không phải nghiệm đặc trưng ⇒ p(n) = D · 3ⁿ\nchia cho 3ⁿ⁻²:  9D = 6D − D + 9 ⇒ D = 9/4", 24, RED, y=2.2)
        self.play(FadeIn(s2), run_time=0.6)
        self.wait(2.0)
        s3 = para("③ X(0): A + 9/4 = 1 ⇒ A = −5/4\n    X(1): A + B + 27/4 = 3 ⇒ B = −5/2", 24, WHITE, y=0.7)
        self.play(FadeIn(s3), run_time=0.6)
        self.wait(2.0)
        s4 = para("X(n) = −5/4 − 5n/2 + (9/4) · 3ⁿ", 34, GOLD, y=-0.5)
        self.play(FadeIn(s4, scale=1.2), run_time=0.6)
        self.wait(1.0)
        s5 = para("Truy hồi: X(2) = 2·3 − 1 + 9 = 14\n               X(3) = 2·14 − 3 + 27 = 52\nCông thức: −5/4 − 5 + 81/4 = 14 ✓\n                 −5/4 − 15/2 + 243/4 = 52 ✓", 24, GREEN, y=-2.4)
        self.play(FadeIn(s5), run_time=0.6)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 8. Bảng đoán nghiệm =====
        c = swap_cap(self, c, cap("Đoán p(n) theo f(n)", 44, GOLD))
        rows = [("f(n)", "đoán p(n)", DIM), ("hằng số k", "C", WHITE), ("đa thức bậc d", "đa thức bậc d", WHITE),
                ("k · sⁿ", "D · sⁿ", WHITE), ("(đa thức) · sⁿ", "(đa thức cùng bậc) · sⁿ", WHITE)]
        tbl = VGroup()
        for i, (a, b, col) in enumerate(rows):
            y = 4.2 - i * 0.95
            tbl.add(Text(a, font=FONT, font_size=26, color=col).move_to([-2.0, y, 0]),
                    Text(b, font=FONT, font_size=26, color=GOLD if i else col).move_to([1.8, y, 0]))
            if i < len(rows) - 1:
                tbl.add(Line([-3.9, y - 0.47, 0], [3.9, y - 0.47, 0], color=DIM, stroke_width=1.5))
        self.play(LaggedStart(*[FadeIn(x) for x in tbl], lag_ratio=0.1), run_time=2.0)
        self.wait(2.0)
        w = para("Nếu dạng đoán trùng với nghiệm thuần nhất\n(s là nghiệm đặc trưng; với đa thức là s = 1)\nthì nhân thêm n, hoặc n² nếu nghiệm kép", 26, RED, y=-0.8)
        self.play(FadeIn(w), run_time=0.7)
        self.wait(4.0)
        wipe(self, keep=[c])

        # ===== 9. Tóm tắt =====
        c = swap_cap(self, c, cap("Bốn bước", 44, GOLD))
        sm = VGroup(*[Text(s, font=FONT, font_size=30, color=col, line_spacing=1.1) for s, col in [
            ("1. Giải phần thuần nhất → h(n)", BLUE),
            ("2. Đoán p(n) cùng dạng với f(n),\n    nhân thêm n nếu cộng hưởng", RED),
            ("3. Cộng lại, dùng điều kiện đầu\n    để tìm hằng số", WHITE),
            ("4. Kiểm tra vài số hạng đầu", GREEN),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        fitw(sm, 7.8).move_to([0, 2.0, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.2) for m in sm], lag_ratio=0.5), run_time=3.0)
        self.wait(6.0)
