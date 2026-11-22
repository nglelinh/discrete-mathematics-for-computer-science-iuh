from common import *
from math import log2
from functools import lru_cache


def T(a, f):
    @lru_cache(None)
    def t(n):
        return 1 if n == 1 else a * t(n // 2) + f(n)
    return t


# ---------- Toán ----------
ms = T(2, lambda n: n)
assert ms(16) == 80 == 16 * 4 + 16
LV_MS = [2 ** i * (16 // 2 ** i) for i in range(4)] + [16]
assert LV_MS == [16] * 5 and sum(LV_MS) == 80
bs = T(1, lambda n: 1)
assert bs(16) == 5 == log2(16) + 1
q4 = T(4, lambda n: n)
LV_4 = [4 ** i * (16 // 2 ** i) for i in range(4)] + [4 ** 4]
assert LV_4 == [16, 32, 64, 128, 256] and sum(LV_4) == q4(16) == 496 == 2 * 16 ** 2 - 16
sq = T(2, lambda n: n * n)
LV_SQ = [2 ** i * (16 // 2 ** i) ** 2 for i in range(4)] + [16]
assert LV_SQ == [256, 128, 64, 32, 16] and sum(LV_SQ) == sq(16) == 496
assert "%.3f" % log2(3) == "1.585" and "%.2f" % log2(7) == "2.81"
# 2T(n/2) + n log n: tầng i đóng góp n·(log n − i) ⇒ tổng ≈ n log²n / 2
nl = T(2, lambda n: n * int(log2(n)))
assert nl(16) == 16 * (4 + 3 + 2 + 1) + 16


class DivideConquer(Scene):
    def wait(self, duration=1.0, **kw):
        super().wait(duration * 1.9, **kw)

    def tree(self, a, levels, y0=4.0, dy=1.25, labels=None, x0=-0.6, width=6.4, col=BLUE):
        """Vẽ cây đệ quy với a con mỗi nút; trả về list các tầng (VGroup)."""
        lv = []
        prev = None
        for i in range(levels):
            k = a ** i
            y = y0 - i * dy
            xs = [x0 - width / 2 + width * (j + 0.5) / k for j in range(k)]
            g = VGroup()
            size = 26 if k <= 4 else (20 if k <= 8 else 14)
            for j, x in enumerate(xs):
                lab = labels[i] if labels else ""
                if k <= 16:
                    t = Text(lab, font=FONT, font_size=size, color=col).move_to([x, y, 0])
                else:
                    t = Dot([x, y, 0], radius=0.03, color=col)
                g.add(t)
            edges = VGroup()
            if prev is not None:
                for j in range(k):
                    p = prev[j // a]
                    edges.add(Line(p.get_center() + DOWN * 0.22, g[j].get_center() + UP * 0.2, color=DIM, stroke_width=1.5))
            self.play(Create(edges), FadeIn(g), run_time=0.6)
            lv.append(VGroup(edges, g))
            prev = g
        return lv

    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Hệ thức truy hồi chia để trị", 38)
        t1 = Text("Chia\nđể trị", font=FONT, font_size=90, color=GOLD, line_spacing=1.0).move_to([0, 2.0, 0])
        t2 = para("T(n) = a · T(n/b) + f(n)\na bài toán con, mỗi bài cỡ n/b,\nf(n) là công chia + gộp", 30, y=-1.0)
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(3.0)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. Cây đệ quy merge sort =====
        c = swap_cap(self, c, cap("Cây đệ quy: T(n) = 2T(n/2) + n", 36, GOLD))
        e = para("Merge sort với n = 16, T(1) = 1. Mỗi nút ghi chi phí gộp", 24, WHITE, y=5.3)
        self.play(FadeIn(e), run_time=0.5)
        lv = self.tree(2, 5, labels=["16", "8", "4", "2", "1"])
        sums = VGroup()
        for i in range(5):
            s = Text(f"= {LV_MS[i]}", font=FONT, font_size=26, color=GOLD).move_to([3.4, 4.0 - i * 1.25, 0])
            sums.add(s)
            self.play(Indicate(lv[i][1], color=GOLD), FadeIn(s), run_time=0.6)
        self.wait(1.2)
        n1 = para("Mỗi tầng tốn đúng n = 16: 2^i nút × n/2^i", 26, WHITE, y=-2.6)
        self.play(FadeIn(n1), run_time=0.5)
        self.wait(1.5)
        n2 = para("Có log₂16 = 4 tầng chia + 1 tầng lá", 26, WHITE, y=-3.5)
        self.play(FadeIn(n2), run_time=0.5)
        self.wait(1.2)
        n3 = para("T(16) = 16 × 4 + 16 = 80 = n log₂n + n", 30, GOLD, y=-4.5)
        self.play(FadeIn(n3), run_time=0.6)
        self.wait(1.2)
        n4 = para("⇒ T(n) = Θ(n log n)", 36, GREEN, y=-5.6)
        self.play(FadeIn(n4, scale=1.2), run_time=0.6)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 2b. Thế ngược =====
        c = swap_cap(self, c, cap("Cách khác: thế ngược", 44, GOLD))
        e = para("Thay T(n/2) = 2T(n/4) + n/2 vào, rồi lặp lại:", 26, WHITE, y=5.1)
        self.play(FadeIn(e), run_time=0.5)
        lines = ["T(n) = 2T(n/2) + n", "     = 4T(n/4) + n + n = 4T(n/4) + 2n", "     = 8T(n/8) + 3n",
                 "     = …", "     = 2^j · T(n/2^j) + j · n"]
        ul = VGroup()
        for i, l in enumerate(lines):
            t = Text(l, font=FONT, font_size=28, color=WHITE if i < 4 else GOLD).move_to([-3.7, 3.8 - i * 0.9, 0], aligned_edge=LEFT)
            fitw(t, 7.6)
            ul.add(t)
            self.play(FadeIn(t, shift=DOWN * 0.15), run_time=0.6)
            self.wait(1.0)
        e2 = para("Dừng khi n/2^j = 1, tức j = log₂n:", 26, WHITE, y=-0.9)
        self.play(FadeIn(e2), run_time=0.5)
        self.wait(1.0)
        e3 = para("T(n) = n · T(1) + n log₂n = n log₂n + n", 30, GOLD, y=-2.0)
        self.play(FadeIn(e3), run_time=0.6)
        self.wait(1.5)
        e4 = para("Cùng kết quả với cây đệ quy: với n = 16\nta được 16 · 4 + 16 = 80 ✓", 26, GREEN, y=-3.4)
        self.play(FadeIn(e4), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 3. Tìm kiếm nhị phân =====
        c = swap_cap(self, c, cap("T(n) = T(n/2) + 1", 44, GOLD))
        e = para("Tìm kiếm nhị phân: mỗi bước bỏ một nửa, tốn 1 phép so sánh", 24, WHITE, y=5.3)
        self.play(FadeIn(e), run_time=0.5)
        chain = VGroup()
        for i, n in enumerate([16, 8, 4, 2, 1]):
            b = RoundedRectangle(width=2.6 - 0.4 * i, height=0.7, corner_radius=0.12, color=BLUE).move_to([-1.0, 4.0 - i * 1.2, 0])
            t = Text(f"n = {n}", font=FONT, font_size=24, color=BLUE).move_to(b)
            s = Text("1", font=FONT, font_size=26, color=GOLD).move_to([2.6, 4.0 - i * 1.2, 0])
            chain.add(VGroup(b, t, s))
            self.play(FadeIn(chain[-1]), run_time=0.4)
        self.wait(1.0)
        n1 = para("Mỗi tầng 1 nút, chi phí 1: T(16) = 5 = log₂16 + 1", 26, WHITE, y=-2.3)
        n2 = para("⇒ T(n) = Θ(log n)", 36, GREEN, y=-3.5)
        self.play(FadeIn(n1), run_time=0.5)
        self.wait(1.5)
        self.play(FadeIn(n2, scale=1.2), run_time=0.5)
        self.wait(1.5)
        n3 = para("n = 1 tỉ phần tử: chỉ khoảng 30 phép so sánh", 26, DIM, y=-4.6)
        self.play(FadeIn(n3), run_time=0.5)
        self.wait(2.5)
        wipe(self, keep=[c])

        # ===== 4. 4T(n/2) + n: lá thắng =====
        c = swap_cap(self, c, cap("T(n) = 4T(n/2) + n", 44, GOLD))
        e = para("4 bài toán con: số nút tăng nhanh hơn chi phí giảm", 24, WHITE, y=5.3)
        self.play(FadeIn(e), run_time=0.5)
        lv = self.tree(4, 3, y0=4.2, dy=1.3, labels=["16", "8", "4"], width=6.4)
        dots = Text("⋮", font=FONT, font_size=30, color=DIM).move_to([-0.6, 0.6, 0])
        self.play(FadeIn(dots), run_time=0.3)
        bars = VGroup()
        for i, v in enumerate(LV_4):
            y = -0.4 - i * 0.75
            lab = Text(["tầng 0", "tầng 1", "tầng 2", "tầng 3", "lá"][i], font=FONT, font_size=22, color=DIM).move_to([-3.3, y, 0])
            r = Rectangle(width=v / 256 * 5.6, height=0.5, color=RED, fill_color=RED, fill_opacity=0.6, stroke_width=0).move_to([-2.6, y, 0], aligned_edge=LEFT)
            t = Text(str(v), font=FONT, font_size=22, color=WHITE).next_to(r, RIGHT, buff=0.12)
            bars.add(VGroup(lab, r, t))
            self.play(FadeIn(lab), GrowFromEdge(r, LEFT), FadeIn(t), run_time=0.45)
        self.wait(1.0)
        n1 = para("Chi phí mỗi tầng nhân đôi: 16, 32, 64, 128, 256\nTổng 496 = 2n² − n: tầng lá chiếm phần lớn", 24, WHITE, y=-4.4)
        n2 = para("⇒ T(n) = Θ(n²)", 36, GREEN, y=-5.7)
        self.play(FadeIn(n1), run_time=0.5)
        self.wait(2.0)
        self.play(FadeIn(n2, scale=1.2), run_time=0.5)
        self.wait(2.5)
        wipe(self, keep=[c])

        # ===== 5. 2T(n/2) + n²: gốc thắng =====
        c = swap_cap(self, c, cap("T(n) = 2T(n/2) + n²", 44, GOLD))
        e = para("Chi phí gộp lớn: tầng trên cùng nặng nhất", 26, WHITE, y=5.2)
        self.play(FadeIn(e), run_time=0.5)
        bars = VGroup()
        for i, v in enumerate(LV_SQ):
            y = 3.8 - i * 0.85
            lab = Text(["tầng 0", "tầng 1", "tầng 2", "tầng 3", "lá"][i], font=FONT, font_size=22, color=DIM).move_to([-3.3, y, 0])
            r = Rectangle(width=v / 256 * 5.6, height=0.55, color=BLUE, fill_color=BLUE, fill_opacity=0.6, stroke_width=0).move_to([-2.6, y, 0], aligned_edge=LEFT)
            t = Text(str(v), font=FONT, font_size=22, color=WHITE).next_to(r, RIGHT, buff=0.12)
            bars.add(VGroup(lab, r, t))
            self.play(FadeIn(lab), GrowFromEdge(r, LEFT), FadeIn(t), run_time=0.45)
        self.wait(1.0)
        n1 = para("Tầng i: 2^i nút × (n/2^i)² = n²/2^i — giảm một nửa mỗi tầng\nTổng < 2n²: gốc quyết định", 24, WHITE, y=-0.8)
        self.play(FadeIn(n1), run_time=0.5)
        self.wait(2.0)
        n2 = para("⇒ T(n) = Θ(n²)", 36, GREEN, y=-2.1)
        self.play(FadeIn(n2, scale=1.2), run_time=0.5)
        self.wait(1.2)
        n3 = para("Thú vị: T(16) = 496, đúng bằng ví dụ trước!\nCùng Θ(n²) nhưng vì lý do ngược nhau:\nở trên lá thắng, ở đây gốc thắng", 24, GOLD, y=-3.8)
        self.play(FadeIn(n3), run_time=0.6)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 6. Định lý thợ =====
        c = swap_cap(self, c, cap("Định lý thợ (Master Theorem)", 40, GOLD))
        e = para("T(n) = aT(n/b) + f(n).  Đặt k = log(a) / log(b):\nsố lá là n^k", 26, WHITE, y=5.0)
        self.play(FadeIn(e), run_time=0.6)
        self.wait(1.5)
        cases = [
            ("① f(n) nhỏ hơn n^k (cỡ đa thức)", "lá thắng ⇒ T(n) = Θ(n^k)", RED),
            ("② f(n) = Θ(n^k)", "các tầng ngang nhau ⇒ Θ(n^k · log n)", GOLD),
            ("③ f(n) lớn hơn n^k (cỡ đa thức)\n    và a·f(n/b) ≤ c·f(n) với c < 1", "gốc thắng ⇒ T(n) = Θ(f(n))", BLUE),
        ]
        y = 3.3
        for a_, b_, col in cases:
            t1 = Text(a_, font=FONT, font_size=26, color=col, line_spacing=1.1)
            t2 = Text(b_, font=FONT, font_size=26, color=WHITE)
            grp = VGroup(t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            fitw(grp).move_to([-3.8, y, 0], aligned_edge=LEFT)
            y -= grp.height + 0.6
            self.play(FadeIn(grp, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(2.0)
        n = para("Đúng như ba bức tranh vừa rồi:\nlá thắng, các tầng bằng nhau, gốc thắng", 24, DIM, y=-3.6)
        self.play(FadeIn(n), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 7. Bảng ví dụ =====
        c = swap_cap(self, c, cap("Áp dụng định lý thợ", 44, GOLD))
        rows = [("hệ thức", "k", "TH", "kết quả", DIM),
                ("2T(n/2) + n  (merge sort)", "1", "②", "n log n", WHITE),
                ("T(n/2) + 1  (nhị phân)", "0", "②", "log n", WHITE),
                ("4T(n/2) + n", "2", "①", "n²", WHITE),
                ("2T(n/2) + n²", "1", "③", "n²", WHITE),
                ("3T(n/2) + n  (Karatsuba)", "1,585", "①", "n^1,585", WHITE),
                ("7T(n/2) + n²  (Strassen)", "2,81", "①", "n^2,81", WHITE)]
        tbl = VGroup()
        for i, (a_, k_, th, r_, col) in enumerate(rows):
            y = 4.6 - i * 0.9
            tbl.add(VGroup(Text(a_, font=FONT, font_size=22, color=col).move_to([-3.95, y, 0], aligned_edge=LEFT),
                           Text(k_, font=FONT, font_size=22, color=col).move_to([1.0, y, 0]),
                           Text(th, font=FONT, font_size=24, color=col if i == 0 else GOLD).move_to([2.0, y, 0]),
                           Text(r_, font=FONT, font_size=22, color=col if i == 0 else GREEN).move_to([3.3, y, 0])))
        for r in tbl:
            self.play(FadeIn(r), run_time=0.45)
            self.wait(0.6)
        self.wait(1.0)
        w = para("Không áp dụng được: T(n) = 2T(n/2) + n log n\nf lớn hơn n nhưng không \"cỡ đa thức\".\nCây đệ quy: tầng i tốn n(log n − i) ⇒ Θ(n log²n)", 24, RED, y=-2.4)
        self.play(FadeIn(w), run_time=0.6)
        self.wait(4.0)
        wipe(self, keep=[c])

        # ===== 8. Tóm tắt =====
        c = swap_cap(self, c, cap("Tóm tắt", 44, GOLD))
        sm = VGroup(*[Text(s, font=FONT, font_size=30, color=col, line_spacing=1.1) for s, col in [
            ("Vẽ cây đệ quy, cộng chi phí\ntheo từng tầng", WHITE),
            ("Tầng bằng nhau ⇒ thêm thừa số log n", GOLD),
            ("Tầng tăng dần ⇒ lá thắng: Θ(n^k)", RED),
            ("Tầng giảm dần ⇒ gốc thắng: Θ(f(n))", BLUE),
            ("Định lý thợ = ba trường hợp đó", GREEN),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        fitw(sm, 7.8).move_to([0, 1.8, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.2) for m in sm], lag_ratio=0.5), run_time=3.0)
        self.wait(6.0)
