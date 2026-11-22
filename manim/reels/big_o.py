from common import *
from math import log2, sqrt

# ---------- Toán ----------
TAB = [(n, round(n * log2(n)), n * n, 2 ** n) for n in (10, 20, 40, 60)]
assert [r[1] for r in TAB] == [33, 86, 213, 354]
assert TAB[1][3] == 1048576
assert round(2 ** 40 / 1e9 / 60) == 18
assert round(2 ** 60 / 1e9 / 3600 / 24 / 365.25) == 37 and int(2 ** 60 / 1e9 / 3600 / 24 / 365.25) == 36
f = lambda n: 3 * n * n + 5 * n + 2
assert f(5) == 102 > 4 * 25 and all(f(n) <= 4 * n * n for n in range(6, 2000))
X0 = (5 + sqrt(33)) / 2
assert 5.3 < X0 < 5.4
assert all(f(n) <= 10 * n * n for n in range(1, 2000)) and all(f(n) >= 3 * n * n for n in range(1, 2000))
assert sum(1 for i in range(10) for j in range(i + 1, 10)) == 45 == 10 * 9 // 2
i, k = 1000, 0
while i > 1:
    i //= 2
    k += 1
assert k == 9 == int(log2(1000))
assert all(100 * n > n * n for n in range(1, 100)) and 100 * 100 == 100 ** 2 and all(100 * n < n * n for n in range(101, 500))


class BigO(Scene):
    def wait(self, duration=1.0, **kw):
        super().wait(duration * 1.85, **kw)

    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Tốc độ tăng của hàm", 42)
        t1 = Text("Big-O", font=FONT, font_size=110, color=GOLD).move_to([0, 2.0, 0])
        t2 = para("Khi n lớn dần, thuật toán nào\nchậm đi nhanh hơn?", 32, y=-0.6)
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. Bảng giá trị =====
        c = swap_cap(self, c, cap("Số phép tính theo n", 44, GOLD))
        hdr = ["n", "n log₂n", "n²", "2ⁿ"]
        cols = [BLUE, GREEN, GOLD, RED]
        xs = [-3.2, -1.4, 0.6, 2.8]
        rows = [hdr] + [[str(n), str(a), str(b), v] for (n, a, b, _), v in zip(TAB, ["1 024", "1 048 576", "≈ 1,1 · 10¹²", "≈ 1,2 · 10¹⁸"])]
        tb = VGroup()
        for i, r in enumerate(rows):
            y = 4.6 - i * 0.9
            g = VGroup(*[Text(s, font=FONT, font_size=26 if i else 28, color=cols[j] if i == 0 else WHITE).move_to([xs[j], y, 0]) for j, s in enumerate(r)])
            fitw(g)
            tb.add(g)
            self.play(FadeIn(g), run_time=0.5)
            self.wait(0.5)
        line = Line([-3.9, 4.15, 0], [3.9, 4.15, 0], color=DIM, stroke_width=1.5)
        self.play(Create(line), run_time=0.3)
        self.wait(1.0)
        e1 = para("Máy chạy 10⁹ phép tính mỗi giây:", 26, WHITE, y=-0.3)
        e2 = para("2⁴⁰ phép ≈ 18 phút", 30, GOLD, y=-1.3)
        e3 = para("2⁶⁰ phép ≈ 36 năm!", 34, RED, y=-2.3)
        e4 = para("còn 60² = 3600 phép: chưa tới 1 phần triệu giây", 24, GREEN, y=-3.3)
        for e in (e1, e2, e3, e4):
            self.play(FadeIn(e), run_time=0.5)
            self.wait(1.2)
        self.wait(2.0)
        wipe(self, keep=[c])

        # ===== 3. Đồ thị tăng trưởng =====
        c = swap_cap(self, c, cap("Các đường tăng trưởng", 42, GOLD))
        ax = Axes(x_range=[0, 10, 1], y_range=[0, 100, 10], x_length=7.2, y_length=7.0, tips=False,
                  axis_config={"color": DIM, "stroke_width": 2}).move_to([0, 1.3, 0])
        xl = Text("n", font=FONT, font_size=24, color=DIM).next_to(ax.x_axis.get_end(), DOWN, buff=0.15)
        self.play(Create(ax), FadeIn(xl), run_time=0.8)
        curves = [
            (lambda x: x, [0, 10], BLUE, "n"),
            (lambda x: x * log2(x) if x > 0 else 0, [0.01, 10], GREEN, "n log n"),
            (lambda x: x * x, [0, 10], GOLD, "n²"),
            (lambda x: 2 ** x, [0, log2(100)], RED, "2ⁿ"),
        ]
        labs = VGroup()
        for fn, xr, col, nm in curves:
            g = ax.plot(fn, x_range=xr + [0.02], color=col, stroke_width=4)
            end = g.get_end()
            lab = Text(nm, font=FONT, font_size=24, color=col).next_to(end, UP if nm in ("n²", "2ⁿ") else RIGHT, buff=0.1)
            if nm in ("n", "n log n"):
                lab.next_to(end, LEFT + UP * 0.6, buff=0.05)
            labs.add(lab)
            self.play(Create(g), FadeIn(lab), run_time=1.0)
            self.wait(0.6)
        e = para("2ⁿ vượt khỏi khung từ n ≈ 7;\nn² chậm hơn nhưng vẫn bỏ xa n log n", 24, WHITE, y=-3.3)
        self.play(FadeIn(e), run_time=0.5)
        self.wait(2.0)
        e2 = para("Big-O chỉ quan tâm hình dạng đường cong khi n lớn,\nkhông quan tâm vài giá trị đầu", 24, GOLD, y=-4.8)
        self.play(FadeIn(e2), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 4. Định nghĩa với c và n₀ =====
        c = swap_cap(self, c, cap("Định nghĩa O lớn", 44, GOLD))
        d = para("f(n) = O(g(n)) nếu có hằng số c > 0 và n₀\nsao cho f(n) ≤ c · g(n) với mọi n ≥ n₀", 26, WHITE, y=5.0)
        self.play(FadeIn(d), run_time=0.6)
        self.wait(2.0)
        ax = Axes(x_range=[0, 10, 1], y_range=[0, 420, 50], x_length=7.2, y_length=5.6, tips=False,
                  axis_config={"color": DIM, "stroke_width": 2}).move_to([0, 0.6, 0])
        self.play(Create(ax), run_time=0.6)
        gf = ax.plot(lambda x: 3 * x * x + 5 * x + 2, x_range=[0, 10.6 - 0.62, 0.02], color=WHITE, stroke_width=4)
        gc = ax.plot(lambda x: 4 * x * x, x_range=[0, sqrt(420 / 4), 0.02], color=GOLD, stroke_width=4)
        lf = Text("f(n) = 3n² + 5n + 2", font=FONT, font_size=22, color=WHITE).move_to(ax.c2p(3.2, 330))
        lc = Text("4n²  (c = 4)", font=FONT, font_size=22, color=GOLD).move_to(ax.c2p(7.9, 400))
        self.play(Create(gf), FadeIn(lf), run_time=1.0)
        self.play(Create(gc), FadeIn(lc), run_time=1.0)
        self.wait(1.0)
        vl = DashedLine(ax.c2p(X0, 0), ax.c2p(X0, 4 * X0 * X0), color=RED, stroke_width=3)
        nl = Text("≈ 5,37", font=FONT, font_size=20, color=RED).next_to(ax.c2p(X0, 0), DOWN, buff=0.15)
        self.play(Create(vl), FadeIn(nl), run_time=0.6)
        zone = Rectangle(width=ax.c2p(10, 0)[0] - ax.c2p(X0, 0)[0], height=ax.c2p(0, 420)[1] - ax.c2p(0, 0)[1],
                         stroke_width=0, fill_color=GREEN, fill_opacity=0.12).move_to(ax.c2p(X0, 0), aligned_edge=DL)
        self.play(FadeIn(zone), run_time=0.5)
        s1 = para("4n² ≥ f(n) ⇔ n² − 5n − 2 ≥ 0 ⇔ n ≥ 5,37…", 24, WHITE, y=-2.7)
        self.play(FadeIn(s1), run_time=0.5)
        self.wait(1.5)
        s2 = para("n = 5: f = 102 > 100 = 4·5²\ntừ n₀ = 6 trở đi luôn đúng", 24, GREEN, y=-3.7)
        self.play(FadeIn(s2), run_time=0.5)
        self.wait(1.5)
        s3 = para("⇒ f(n) = O(n²). Bài học chọn c = 10, n₀ = 1 cũng được:\nc và n₀ không duy nhất, chỉ cần tồn tại", 24, GOLD, y=-5.2)
        self.play(FadeIn(s3), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 5. Ω và Θ =====
        c = swap_cap(self, c, cap("Ω (chặn dưới) và Θ (chặt)", 40, GOLD))
        d = para("f = Ω(g): f(n) ≥ c · g(n) khi n đủ lớn\nf = Θ(g): vừa O(g) vừa Ω(g)", 26, WHITE, y=5.0)
        self.play(FadeIn(d), run_time=0.6)
        self.wait(1.5)
        ax = Axes(x_range=[0, 10, 1], y_range=[0, 420, 50], x_length=7.2, y_length=5.6, tips=False,
                  axis_config={"color": DIM, "stroke_width": 2}).move_to([0, 0.6, 0])
        g4 = ax.plot(lambda x: 4 * x * x, x_range=[0, sqrt(105), 0.02], color=GOLD, stroke_width=4)
        g3 = ax.plot(lambda x: 3 * x * x, x_range=[0, 10, 0.02], color=BLUE, stroke_width=4)
        gf = ax.plot(lambda x: 3 * x * x + 5 * x + 2, x_range=[0, 10.6 - 0.62, 0.02], color=WHITE, stroke_width=4)
        band = ax.get_area(g4, x_range=[X0, sqrt(105)], bounded_graph=g3, color=GREEN, opacity=0.2)
        self.play(Create(ax), Create(g3), Create(g4), run_time=1.0)
        self.play(Create(gf), FadeIn(band), run_time=1.0)
        l4 = Text("4n²", font=FONT, font_size=22, color=GOLD).move_to(ax.c2p(9.0, 400))
        l3 = Text("3n²", font=FONT, font_size=22, color=BLUE).move_to(ax.c2p(9.6, 230))
        lf = Text("f(n)", font=FONT, font_size=22, color=WHITE).move_to(ax.c2p(7.4, 300))
        self.play(FadeIn(l4), FadeIn(l3), FadeIn(lf), run_time=0.5)
        s1 = para("3n² ≤ f(n) ≤ 4n² khi n ≥ 6:\nf bị kẹp giữa hai bội của n²", 26, WHITE, y=-2.8)
        self.play(FadeIn(s1), run_time=0.5)
        self.wait(2.0)
        s2 = para("⇒ f(n) = Θ(n²)", 36, GREEN, y=-4.0)
        self.play(FadeIn(s2, scale=1.2), run_time=0.5)
        self.wait(1.5)
        s3 = para("Θ là câu trả lời \"đúng cỡ\";\nO chỉ nói \"không lớn hơn\"", 26, GOLD, y=-5.2)
        self.play(FadeIn(s3), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 6. Quy tắc =====
        c = swap_cap(self, c, cap("Quy tắc rút gọn", 44, GOLD))
        rs = VGroup(*[Text(s, font=FONT, font_size=26, color=col, line_spacing=1.1) for s, col in [
            ("Bỏ hằng số nhân: 5n² = O(n²)", WHITE),
            ("Giữ số hạng lớn nhất:\nn + n log n + 100 = Θ(n log n)", WHITE),
            ("Cơ số log không quan trọng:\nlog₂n và log₁₀n chỉ khác một hằng số", WHITE),
            ("Vòng lặp nối tiếp: cộng;  lồng nhau: nhân", WHITE),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        fitw(rs).move_to([0, 3.0, 0])
        for r in rs:
            self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(1.3)
        ch = para("1 < log n < n < n log n < n² < n³ < 2ⁿ < n!", 30, GOLD, y=-1.2)
        self.play(FadeIn(ch), run_time=0.6)
        self.wait(1.0)
        ar = Arrow([-3.6, -2.0, 0], [3.6, -2.0, 0], color=RED, buff=0, stroke_width=4)
        al = Text("tăng càng lúc càng nhanh", font=FONT, font_size=22, color=RED).next_to(ar, DOWN, buff=0.15)
        self.play(GrowArrow(ar), FadeIn(al), run_time=0.6)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 7. Đếm vòng lặp =====
        c = swap_cap(self, c, cap("Đếm bước trong code", 44, GOLD))
        code1 = Text("for i in range(n):\n    for j in range(i + 1, n):\n        so_sanh(i, j)", font="Menlo", font_size=24, color=WHITE, line_spacing=1.1)
        code1.move_to([-3.8, 4.4, 0], aligned_edge=LEFT)
        box1 = SurroundingRectangle(code1, color=BLUE, buff=0.2, corner_radius=0.1)
        self.play(FadeIn(code1), Create(box1), run_time=0.7)
        s1 = para("(n−1) + (n−2) + … + 1 + 0 = n(n−1)/2 lần\nn = 10: 45 lần  ⇒ Θ(n²)", 26, BLUE, y=2.4)
        self.play(FadeIn(s1), run_time=0.5)
        self.wait(2.5)
        code2 = Text("i = n\nwhile i > 1:\n    i = i // 2", font="Menlo", font_size=24, color=WHITE, line_spacing=1.1)
        code2.move_to([-3.8, 0.4, 0], aligned_edge=LEFT)
        box2 = SurroundingRectangle(code2, color=GREEN, buff=0.2, corner_radius=0.1)
        self.play(FadeIn(code2), Create(box2), run_time=0.7)
        s2 = para("Mỗi vòng chia đôi: n = 1000 → 500 → 250 → … → 1\nchỉ 9 vòng ≈ log₂1000  ⇒ Θ(log n)", 24, GREEN, y=-1.6)
        self.play(FadeIn(s2), run_time=0.5)
        self.wait(2.5)
        s3 = para("Lồng vòng chia đôi trong vòng n ⇒ Θ(n log n)", 26, GOLD, y=-3.0)
        self.play(FadeIn(s3), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 8. Bẫy thường gặp =====
        c = swap_cap(self, c, cap("Những bẫy thường gặp", 42, RED))
        ps = [
            ("O chỉ là chặn trên: n = O(n²) vẫn ĐÚNG,\nnhưng nói Θ(n) mới chính xác", WHITE),
            ("Hằng số vẫn quan trọng khi n nhỏ:\n100n > n² với mọi n < 100", WHITE),
            ("2ⁿ⁺¹ = 2 · 2ⁿ = O(2ⁿ), nhưng\n2²ⁿ = 4ⁿ không là O(2ⁿ):\ntỉ số 4ⁿ / 2ⁿ = 2ⁿ không bị chặn", WHITE),
            ("n² không là O(n): cần n² ≤ c·n, tức n ≤ c\ncho mọi n lớn — không thể", WHITE),
            ("O(n²) không có nghĩa là \"chạy n² giây\":\nchỉ là cách tăng khi n lớn", WHITE),
        ]
        y = 4.9
        for i, (s, col) in enumerate(ps):
            t = Text(f"{i + 1}. " + s, font=FONT, font_size=24, color=col, line_spacing=1.1)
            fitw(t).move_to([-3.9, y, 0], aligned_edge=UL)
            y -= t.height + 0.55
            self.play(FadeIn(t, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(2.0)
        self.wait(2.0)
        wipe(self, keep=[c])

        # ===== 9. Tóm tắt =====
        c = swap_cap(self, c, cap("Tóm tắt", 44, GOLD))
        sm = VGroup(*[Text(s, font=FONT, font_size=30, color=col, line_spacing=1.1) for s, col in [
            ("O: chặn trên,  Ω: chặn dưới,\nΘ: đúng cỡ", GOLD),
            ("Chứng minh = tìm c và n₀", WHITE),
            ("Bỏ hằng số, giữ số hạng trội", BLUE),
            ("Đếm vòng lặp: cộng nối tiếp,\nnhân lồng nhau", GREEN),
            ("2ⁿ bùng nổ: tránh thuật toán mũ\nkhi n lớn", RED),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        fitw(sm, 7.8).move_to([0, 1.8, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.2) for m in sm], lag_ratio=0.5), run_time=3.0)
        self.wait(6.0)
