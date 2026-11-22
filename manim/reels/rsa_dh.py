from common import *
from math import gcd

# ---------- Toán ----------
P_, G_, A_, B_ = 23, 5, 6, 15
PA, PB = pow(G_, A_, P_), pow(G_, B_, P_)
assert (PA, PB) == (8, 19)
assert pow(PB, A_, P_) == pow(PA, B_, P_) == 2
assert pow(5, 2, 23) == 2 and pow(5, 4, 23) == 4 and (4 * 2) % 23 == 8
DLOG = [pow(5, k, 23) for k in range(1, 12)]
assert DLOG == [5, 2, 10, 4, 20, 8, 17, 16, 11, 9, 22]
p, q = 61, 53
n, phi, e = p * q, (p - 1) * (q - 1), 17
assert (n, phi) == (3233, 3120) and gcd(e, phi) == 1
assert 3120 == 17 * 183 + 9 and 17 == 1 * 9 + 8 and 9 == 1 * 8 + 1
assert 1 == 2 * 3120 - 367 * 17
d = -367 % phi
assert d == 2753 == pow(e, -1, phi) and e * d == 46801 == 1 + 15 * phi
M = 123
assert gcd(M, n) == 1
SQ = [M]
for _ in range(4):
    SQ.append(SQ[-1] ** 2 % n)
assert bin(17) == "0b10001"
C = SQ[4] * SQ[0] % n
assert SQ == [123, 2197, 3173, 367, 2136] and C == 855 == pow(M, e, n)
assert pow(C, d, n) == M
assert bin(d) == "0b101011000001" and bin(d).count("1") == 5 and len(bin(d)) - 3 == 11

YEL, ORG, GRN, BRN = "#F4D03F", "#E67E22", "#27AE60", "#8E5B3A"
PRED, PBLU = "#E74C3C", "#3498DB"


class Rsa(Scene):
    def wait(self, duration=1.0, **kw):
        super().wait(duration * 1.7, **kw)

    def pot(self, col, x, y, r=0.45, label=None, lc=WHITE):
        c_ = Circle(radius=r, color=WHITE, stroke_width=2, fill_color=col, fill_opacity=1).move_to([x, y, 0])
        g = VGroup(c_)
        if label:
            g.add(Text(label, font=FONT, font_size=20, color=lc).next_to(c_, DOWN, buff=0.12))
        return g

    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Mật mã khóa công khai", 42)
        t1 = Text("RSA &\nDiffie–Hellman", font=FONT, font_size=72, color=GOLD, line_spacing=1.0).move_to([0, 2.0, 0])
        t2 = para("Hai người chưa từng gặp nhau, nói chuyện\nqua kênh ai cũng nghe được.\nLàm sao giữ bí mật?", 28, y=-1.0)
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(3.0)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. Trộn sơn =====
        c = swap_cap(self, c, cap("Diffie–Hellman: trộn sơn", 40, GOLD))
        al = Text("Alice", font=FONT, font_size=30, color=PRED).move_to([-2.8, 5.0, 0])
        bo = Text("Bob", font=FONT, font_size=30, color=PBLU).move_to([2.8, 5.0, 0])
        mid = DashedLine([0, 5.4, 0], [0, -3.4, 0], color=DIM)
        ev = Text("kênh công khai\n(Eve nghe được)", font=FONT, font_size=18, color=DIM, line_spacing=1.0).move_to([0, -3.9, 0])
        self.play(FadeIn(al), FadeIn(bo), Create(mid), FadeIn(ev), run_time=0.8)
        y0 = self.pot(YEL, 0, 3.8, label="màu chung", lc=YEL)
        self.play(FadeIn(y0), run_time=0.5)
        s0 = para("① Thống nhất công khai một màu vàng", 22, WHITE, y=2.6)
        self.play(FadeIn(s0), run_time=0.4)
        self.wait(1.2)
        ar = self.pot(PRED, -2.8, 3.8, label="bí mật của Alice", lc=PRED)
        br = self.pot(PBLU, 2.8, 3.8, label="bí mật của Bob", lc=PBLU)
        self.play(FadeIn(ar), FadeIn(br), run_time=0.6)
        self.wait(1.0)
        ao = self.pot(ORG, -2.8, 1.4, label="vàng + đỏ")
        bg = self.pot(GRN, 2.8, 1.4, label="vàng + xanh")
        s1 = para("② Mỗi người trộn màu chung với màu bí mật", 22, WHITE, y=0.2)
        self.play(FadeOut(s0), FadeIn(s1), TransformFromCopy(VGroup(y0[0], ar[0]), ao[0]), TransformFromCopy(VGroup(y0[0], br[0]), bg[0]), run_time=1.0)
        self.play(FadeIn(ao[1]), FadeIn(bg[1]), run_time=0.4)
        self.wait(1.2)
        s2 = para("③ Gửi hỗn hợp cho nhau qua kênh công khai", 22, WHITE, y=0.2)
        ao2, bg2 = ao[0].copy(), bg[0].copy()
        self.play(FadeOut(s1), FadeIn(s2), ao2.animate.move_to([2.8, -0.9, 0]), bg2.animate.move_to([-2.8, -0.9, 0]), run_time=1.2)
        self.wait(1.0)
        s3 = para("④ Trộn thêm màu bí mật của mình vào", 22, WHITE, y=0.2)
        ka = self.pot(BRN, -2.8, -2.4, label="màu chung bí mật", lc=GOLD)
        kb = self.pot(BRN, 2.8, -2.4, label="màu chung bí mật", lc=GOLD)
        self.play(FadeOut(s2), FadeIn(s3), TransformFromCopy(VGroup(bg2, ar[0]), ka[0]), TransformFromCopy(VGroup(ao2, br[0]), kb[0]), run_time=1.0)
        self.play(FadeIn(ka[1]), FadeIn(kb[1]), run_time=0.4)
        self.wait(1.5)
        s4 = para("Cả hai đều có vàng + đỏ + xanh. Eve chỉ thấy vàng, cam,\nxanh lá — và \"tách màu\" khỏi hỗn hợp là rất khó", 22, GOLD, y=-5.2)
        self.play(FadeIn(s4), run_time=0.6)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 3. DH với số =====
        c = swap_cap(self, c, cap("Diffie–Hellman với số", 42, GOLD))
        s0 = para("Công khai: số nguyên tố p = 23, cơ số g = 5", 28, YEL, y=5.0)
        self.play(FadeIn(s0), run_time=0.5)
        rows = [
            ("Alice chọn bí mật a = 6", "Bob chọn bí mật b = 15", WHITE),
            ("A = 5⁶ mod 23 = 8", "B = 5¹⁵ mod 23 = 19", WHITE),
            ("gửi 8 →", "← gửi 19", DIM),
            ("K = 19⁶ mod 23 = 2", "K = 8¹⁵ mod 23 = 2", GOLD),
        ]
        y = 3.8
        for a_, b_, col in rows:
            ta = Text(a_, font=FONT, font_size=24, color=PRED if col is WHITE else col).move_to([-2.1, y, 0])
            tb = Text(b_, font=FONT, font_size=24, color=PBLU if col is WHITE else col).move_to([2.1, y, 0])
            fitw(ta, 3.9), fitw(tb, 3.9)
            self.play(FadeIn(ta), FadeIn(tb), run_time=0.5)
            self.wait(1.3)
            y -= 0.9
        s1 = para("Cùng khóa K = 2 vì (5⁶)¹⁵ = (5¹⁵)⁶ = 5⁹⁰", 26, GOLD, y=0.0)
        self.play(FadeIn(s1), run_time=0.5)
        self.wait(2.0)
        s2 = para("Tính lũy thừa nhanh bằng bình phương liên tiếp:\n5² = 25 ≡ 2,  5⁴ ≡ 2² = 4,  5⁶ = 5⁴ · 5² ≡ 4 · 2 = 8", 24, WHITE, y=-1.5)
        self.play(FadeIn(s2), run_time=0.5)
        self.wait(2.5)
        s3 = para("Eve biết 23, 5, 8, 19. Muốn tìm a phải giải\n5 mũ a ≡ 8 (mod 23): bài toán logarit rời rạc", 24, RED, y=-3.2)
        self.play(FadeIn(s3), run_time=0.5)
        self.wait(2.0)
        tl = VGroup()
        for k, v in enumerate(DLOG[:8]):
            t = Text(f"5{'¹²³⁴⁵⁶⁷⁸'[k]}≡{v}", font=FONT, font_size=22, color=GOLD if v == 8 else DIM).move_to([-3.4 + k * 0.97, -4.6, 0])
            tl.add(t)
        self.play(LaggedStart(*[FadeIn(t) for t in tl], lag_ratio=0.15), run_time=1.5)
        s4 = para("Chỉ còn cách thử lần lượt. Với p cỡ 600 chữ số: bất khả thi", 22, WHITE, y=-5.5)
        self.play(FadeIn(s4), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 4. RSA: tạo khóa =====
        c = swap_cap(self, c, cap("RSA: tạo khóa", 44, GOLD))
        steps = [
            ("① Chọn hai số nguyên tố p = 61, q = 53", WHITE),
            ("② n = p · q = 3233   (công khai)", BLUE),
            ("③ φ(n) = (p − 1)(q − 1) = 60 · 52 = 3120   (bí mật)", RED),
            ("④ Chọn e = 17 với gcd(17, 3120) = 1   (công khai)", BLUE),
            ("⑤ Tìm d với e · d ≡ 1 (mod 3120)   (bí mật)", RED),
        ]
        y = 4.9
        for s_, col in steps:
            t = para(s_, 26, col, y=y)
            self.play(FadeIn(t, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(1.4)
            y -= 0.95
        k1 = para("Khóa công khai: (n, e) = (3233, 17)\nKhóa bí mật: d", 30, GOLD, y=-0.6)
        self.play(FadeIn(k1), run_time=0.6)
        self.wait(2.0)
        k2 = para("Biết p, q thì tính φ(n) dễ; chỉ biết n = 3233\nthì phải phân tích n ra thừa số", 24, DIM, y=-2.4)
        self.play(FadeIn(k2), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 5. Euclid mở rộng =====
        c = swap_cap(self, c, cap("Tìm d: Euclid mở rộng", 42, GOLD))
        lines1 = ["3120 = 17 · 183 + 9", "17 = 1 · 9 + 8", "9 = 1 · 8 + 1"]
        g1 = VGroup()
        for i, l in enumerate(lines1):
            t = Text(l, font=FONT, font_size=30, color=WHITE).move_to([0, 4.8 - i * 0.85, 0])
            g1.add(t)
            self.play(FadeIn(t), run_time=0.5)
            self.wait(0.8)
        s0 = para("Số dư 1 ⇒ gcd = 1. Thế ngược từ dưới lên:", 24, DIM, y=2.2)
        self.play(FadeIn(s0), run_time=0.5)
        lines2 = ["1 = 9 − 8", "  = 9 − (17 − 9) = 2 · 9 − 17", "  = 2 · (3120 − 183 · 17) − 17", "  = 2 · 3120 − 367 · 17"]
        g2 = VGroup()
        for i, l in enumerate(lines2):
            t = Text(l, font=FONT, font_size=26, color=WHITE if i < 3 else GOLD).move_to([-3.2, 1.3 - i * 0.8, 0], aligned_edge=LEFT)
            g2.add(t)
            self.play(FadeIn(t), run_time=0.5)
            self.wait(1.0)
        s1 = para("⇒ −367 · 17 ≡ 1 (mod 3120)", 28, WHITE, y=-2.3)
        s2 = para("d = −367 + 3120 = 2753", 36, GOLD, y=-3.3)
        s3 = para("Kiểm tra: 17 · 2753 = 46801 = 15 · 3120 + 1 ✓", 24, GREEN, y=-4.4)
        for s_ in (s1, s2, s3):
            self.play(FadeIn(s_), run_time=0.5)
            self.wait(1.5)
        self.wait(1.5)
        wipe(self, keep=[c])

        # ===== 6. Mã hóa =====
        c = swap_cap(self, c, cap("Mã hóa: C = M¹⁷ mod 3233", 40, GOLD))
        s0 = para("Thông điệp M = 123. 17 = 10001 (nhị phân) = 16 + 1", 26, WHITE, y=5.0)
        self.play(FadeIn(s0), run_time=0.5)
        self.wait(1.2)
        sq = [("123¹ ", "123"), ("123² ", "2197"), ("123⁴ ", "2197² ≡ 3173"), ("123⁸ ", "3173² ≡ 367"), ("123¹⁶", "367² ≡ 2136")]
        g = VGroup()
        for i, (a_, b_) in enumerate(sq):
            t = Text(f"{a_} ≡ {b_}", font=FONT, font_size=28, color=GOLD if i in (0, 4) else WHITE).move_to([-3.0, 3.8 - i * 0.8, 0], aligned_edge=LEFT)
            g.add(t)
            self.play(FadeIn(t), run_time=0.45)
            self.wait(0.6)
        s1 = para("Mỗi bước: bình phương rồi lấy dư cho 3233", 24, DIM, y=-0.3)
        self.play(FadeIn(s1), run_time=0.5)
        self.wait(1.0)
        s2 = para("123¹⁷ = 123¹⁶ · 123 ≡ 2136 · 123 ≡ 855", 30, GOLD, y=-1.4)
        self.play(FadeIn(s2), run_time=0.6)
        self.wait(1.5)
        s3 = para("C = 855: ai cũng mã hóa được vì (n, e) công khai", 26, BLUE, y=-2.6)
        self.play(FadeIn(s3), run_time=0.5)
        self.wait(1.5)
        s4 = para("Chỉ 4 lần bình phương + 1 lần nhân thay vì 16 lần nhân", 22, DIM, y=-3.6)
        self.play(FadeIn(s4), run_time=0.5)
        self.wait(2.5)
        wipe(self, keep=[c])

        # ===== 7. Giải mã + vì sao đúng =====
        c = swap_cap(self, c, cap("Giải mã: M = C²⁷⁵³ mod 3233", 38, GOLD))
        s0 = para("2753 = 101011000001 (nhị phân): 11 lần bình phương\n+ 4 lần nhân, thay vì 2752 lần nhân", 24, WHITE, y=4.9)
        self.play(FadeIn(s0), run_time=0.5)
        self.wait(2.0)
        s1 = para("855²⁷⁵³ mod 3233 = 123 ✓", 36, GREEN, y=3.4)
        self.play(FadeIn(s1, scale=1.2), run_time=0.6)
        self.wait(1.5)
        s2 = para("Vì sao lấy lại đúng M?", 30, GOLD, y=2.1)
        self.play(FadeIn(s2), run_time=0.5)
        why = [
            ("e · d = 46801 = 1 + 15 · φ(n)", WHITE),
            ("C^d = M^(e·d) = M · (M^φ(n))¹⁵", WHITE),
            ("Định lý Euler: M^φ(n) ≡ 1 (mod n) khi gcd(M, n) = 1", BLUE),
            ("⇒ C^d ≡ M · 1¹⁵ = M (mod n)", GOLD),
        ]
        y = 1.0
        for s_, col in why:
            t = para(s_, 26, col, y=y)
            self.play(FadeIn(t), run_time=0.5)
            self.wait(1.6)
            y -= 0.95
        s3 = para("(Thực ra công thức vẫn đúng cả khi gcd(M, n) ≠ 1,\nnhờ định lý số dư Trung Hoa)", 22, DIM, y=-3.4)
        self.play(FadeIn(s3), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 8. An toàn =====
        c = swap_cap(self, c, cap("RSA an toàn đến đâu?", 42, GOLD))
        s0 = para("Kẻ tấn công biết n = 3233 và e = 17.\nNếu phân tích được n = 61 · 53\nthì tính ngay được φ(n) và d", 26, WHITE, y=4.9)
        self.play(FadeIn(s0), run_time=0.5)
        self.wait(2.0)
        s1 = para("3233 nhỏ, phân tích trong tích tắc.\nThực tế n dài 2048 bit (khoảng 617 chữ số):\nchưa ai biết cách phân tích nhanh", 24, RED, y=2.7)
        self.play(FadeIn(s1), run_time=0.5)
        self.wait(2.5)
        rows = [("", "Diffie–Hellman", "RSA"), ("mục đích", "thỏa thuận khóa", "mã hóa, chữ ký"),
                ("bài toán khó", "logarit rời rạc", "phân tích thừa số"), ("công cụ", "lũy thừa mod p", "Euclid, Euler")]
        tb = VGroup()
        for i, (a_, b_, d_) in enumerate(rows):
            yy = 0.8 - i * 0.85
            tb.add(VGroup(Text(a_, font=FONT, font_size=22, color=DIM).move_to([-3.0, yy, 0]),
                          Text(b_, font=FONT, font_size=22, color=GOLD if i == 0 else WHITE).move_to([-0.2, yy, 0]),
                          Text(d_, font=FONT, font_size=22, color=GOLD if i == 0 else WHITE).move_to([2.7, yy, 0])))
        for r in tb:
            self.play(FadeIn(r), run_time=0.4)
            self.wait(0.8)
        s2 = para("HTTPS dùng cả hai: thỏa thuận khóa phiên rồi\nmã hóa đối xứng (AES) cho nhanh", 22, BLUE, y=-3.2)
        self.play(FadeIn(s2), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 9. Tóm tắt =====
        c = swap_cap(self, c, cap("Tóm tắt", 44, GOLD))
        sm = VGroup(*[Text(s, font=FONT, font_size=30, color=col, line_spacing=1.1) for s, col in [
            ("DH: cả hai cùng tính g mũ ab (mod p)\nmà không gửi khóa", GOLD),
            ("RSA: n = pq, ed ≡ 1 (mod φ(n))", BLUE),
            ("Mã hóa M^e, giải mã C^d (mod n)", WHITE),
            ("Lũy thừa nhanh: bình phương liên tiếp", GREEN),
            ("Euler bảo đảm giải mã đúng", RED),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        fitw(sm, 7.8).move_to([0, 1.8, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.2) for m in sm], lag_ratio=0.5), run_time=3.0)
        self.wait(6.0)
