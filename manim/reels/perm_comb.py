from common import *
from itertools import permutations, combinations, product, combinations_with_replacement
from math import factorial, comb, perm

# ---------- Toán ----------
P3 = ["".join(p) for p in permutations("ABC")]
assert P3 == ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"] and factorial(3) == 6
assert factorial(5) == 120 and factorial(10) == 3628800 and factorial(20) == 2432902008176640000
assert perm(8, 3) == 8 * 7 * 6 == 336 == factorial(8) // factorial(5)
T4 = ["".join(p) for p in permutations("ABCD", 3)]
assert len(T4) == 24 == perm(4, 3)
GROUPS = {}
for t in T4:
    GROUPS.setdefault("".join(sorted(t)), []).append(t)
assert sorted(GROUPS) == ["ABC", "ABD", "ACD", "BCD"] and all(len(v) == 6 for v in GROUPS.values())
assert comb(4, 3) == 4 == 24 // 6
assert comb(10, 3) == 120 and perm(10, 3) == 720 and 720 // 6 == 120 and comb(10, 7) == 120
L = "ABC"
OR = ["".join(p) for p in permutations(L, 2)]
ORR = ["".join(p) for p in product(L, repeat=2)]
UN = ["".join(p) for p in combinations(L, 2)]
UNR = ["".join(p) for p in combinations_with_replacement(L, 2)]
assert (len(OR), len(ORR), len(UN), len(UNR)) == (6, 9, 3, 6)
assert len(OR) == perm(3, 2) and len(ORR) == 3 ** 2 and len(UN) == comb(3, 2) and len(UNR) == comb(3 + 2 - 1, 2)
assert 10 ** 4 == 10000 and comb(5, 2) == 10 and perm(5, 3) == 60 and comb(4 + 3 - 1, 3) == 20

# bàn tròn 5 người: quy về dạng bắt đầu bằng A
CIRC = {min("".join(p[i:] + p[:i]) for i in range(5)) for p in permutations("ABCDE")}
assert len(CIRC) == 24 == factorial(5) // 5 == factorial(4)
# ủy ban 2 nữ (trong 8) + 3 nam (trong 10)
assert comb(8, 2) == 28 and comb(10, 3) == 120 and 28 * 120 == 3360
assert comb(18, 5) == 8568


def chunk(lst, k):
    return "\n".join("  ".join(lst[i:i + k]) for i in range(0, len(lst), k))


class PermComb(Scene):
    def wait(self, duration=1.0, **kw):
        super().wait(duration * 1.7, **kw)

    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Đếm cách chọn và sắp xếp", 40)
        t1 = Text("Hoán vị\n& Tổ hợp", font=FONT, font_size=84, color=GOLD, line_spacing=1.0).move_to([0, 1.5, 0])
        t2 = para("Hai câu hỏi quyết định mọi thứ:\nthứ tự có quan trọng không?  có được lặp lại không?", 28, y=-1.3)
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. Cây hoán vị ABC =====
        c = swap_cap(self, c, cap("Có bao nhiêu cách xếp A, B, C?", 40, GOLD))
        root = Dot([0, 5.2, 0], color=DIM, radius=0.08)
        self.play(FadeIn(root), run_time=0.3)
        lv1, lv2, lv3, edges = [], [], [], []
        for i, a in enumerate("ABC"):
            x1 = -3.0 + 3.0 * i
            n1 = Text(a, font=FONT, font_size=34, color=BLUE).move_to([x1, 3.8, 0])
            lv1.append(n1)
            edges.append(Line(root.get_center(), n1.get_top() + UP * 0.05, color=DIM, stroke_width=2))
            rest = [b for b in "ABC" if b != a]
            for j, b in enumerate(rest):
                x2 = x1 - 0.75 + 1.5 * j
                n2 = Text(b, font=FONT, font_size=34, color=GREEN).move_to([x2, 2.4, 0])
                lv2.append(n2)
                edges.append(Line(n1.get_bottom() + DOWN * 0.05, n2.get_top() + UP * 0.05, color=DIM, stroke_width=2))
                last = [x for x in rest if x != b][0]
                n3 = Text(last, font=FONT, font_size=34, color=GOLD).move_to([x2, 1.0, 0])
                lv3.append((n3, a + b + last))
                edges.append(Line(n2.get_bottom() + DOWN * 0.05, n3.get_top() + UP * 0.05, color=DIM, stroke_width=2))
        e1 = [e for e in edges[:]]
        k1 = para("3 lựa chọn cho vị trí 1", 24, BLUE, y=-0.3)
        self.play(*[Create(edges[i * 5]) for i in range(3)], *[FadeIn(n) for n in lv1], FadeIn(k1), run_time=0.9)
        self.wait(1.2)
        k2 = para("còn 2 cho vị trí 2", 24, GREEN, y=-0.9)
        self.play(*[Create(edges[i * 5 + 1 + 2 * j]) for i in range(3) for j in range(2)], *[FadeIn(n) for n in lv2], FadeIn(k2), run_time=0.9)
        self.wait(1.2)
        k3 = para("còn 1 cho vị trí 3", 24, GOLD, y=-1.5)
        self.play(*[Create(edges[i * 5 + 2 + 2 * j]) for i in range(3) for j in range(2)], *[FadeIn(n) for n, _ in lv3], FadeIn(k3), run_time=0.9)
        words = VGroup(*[Text(w, font=FONT, font_size=24, color=WHITE).move_to([n.get_x(), 0.35, 0]) for n, w in lv3])
        assert [w for _, w in lv3] == P3
        self.play(FadeIn(words), run_time=0.6)
        self.wait(1.0)
        r = para("3 × 2 × 1 = 3! = 6 hoán vị", 40, GOLD, y=-2.7)
        self.play(Write(r), run_time=0.8)
        self.wait(2.0)
        gr = VGroup(*[Text(s, font=FONT, font_size=28, color=col) for s, col in [
            ("5! = 120", WHITE), ("10! = 3 628 800", WHITE), ("20! ≈ 2,4 × 10¹⁸", RED)]]).arrange(DOWN, buff=0.3).move_to([0, -4.6, 0])
        self.play(LaggedStart(*[FadeIn(m) for m in gr], lag_ratio=0.5), run_time=1.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 3. Chỉnh hợp P(8,3) =====
        c = swap_cap(self, c, cap("Chọn 3 trong 8, có thứ tự", 40, GOLD))
        q = para("8 vận động viên chạy chung kết.\nCó bao nhiêu cách trao Vàng, Bạc, Đồng?", 30, WHITE, y=5.0)
        self.play(FadeIn(q), run_time=0.6)
        runners = VGroup(*[VGroup(Circle(0.32, color=BLUE, fill_opacity=0.25, stroke_width=3),
                                  Text(str(i + 1), font=FONT, font_size=24)).move_to([-3.5 + i * 1.0, 3.3, 0]) for i in range(8)])
        self.play(LaggedStart(*[FadeIn(m) for m in runners], lag_ratio=0.08), run_time=1.0)
        hs = [1.6, 2.2, 1.2]
        xs = [-2.2, 0, 2.2]
        names = ["Bạc", "Vàng", "Đồng"]
        cols = ["#c0c0c0", GOLD, "#cd7f32"]
        cnt = ["7", "8", "6"]
        pods = VGroup()
        for x, h, nm, col, k in zip(xs, hs, names, cols, cnt):
            b = Rectangle(width=2.0, height=h, color=col, fill_color=col, fill_opacity=0.25, stroke_width=3)
            b.move_to([x, -0.5 + h / 2, 0])
            t = Text(nm, font=FONT, font_size=26, color=col).move_to(b.get_center() + DOWN * (h / 2 - 0.3))
            pods.add(VGroup(b, t))
        self.play(FadeIn(pods), run_time=0.8)
        order = [1, 0, 2]
        nums = [None] * 3
        for idx in order:
            x, h, k, col = xs[idx], hs[idx], cnt[idx], cols[idx]
            n = Text(k + " cách", font=FONT, font_size=30, color=col).move_to([x, -0.5 + h + 0.4, 0])
            nums[idx] = n
            self.play(FadeIn(n, shift=DOWN * 0.2), run_time=0.6)
            self.wait(1.2)
        r = para("8 × 7 × 6 = 336", 44, GOLD, y=-1.6)
        self.play(Write(r), run_time=0.8)
        self.wait(1.5)
        f = para("P(n, k) = n × (n−1) × … × (n−k+1) = n! / (n−k)!", 26, WHITE, y=-2.8)
        f2 = para("P(8, 3) = 8! / 5! = 40320 / 120 = 336", 26, DIM, y=-3.5)
        assert factorial(8) == 40320
        self.play(FadeIn(f), run_time=0.6)
        self.wait(1.5)
        self.play(FadeIn(f2), run_time=0.6)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 4. Từ chỉnh hợp sang tổ hợp =====
        c = swap_cap(self, c, cap("Bỏ thứ tự: chia cho k!", 42, GOLD))
        q = para("Từ A, B, C, D lấy 3 chữ cái có thứ tự: P(4,3) = 24 bộ", 28, WHITE, y=5.3)
        self.play(FadeIn(q), run_time=0.6)
        grid = VGroup()
        pal = [BLUE, GREEN, GOLD, RED]
        for i, (key, items) in enumerate(sorted(GROUPS.items())):
            row = VGroup(*[Text(t, font=FONT, font_size=28, color=WHITE).move_to([-3.75 + j * 1.1, 4.1 - i * 0.8, 0]) for j, t in enumerate(items)])
            grid.add(row)
        flat = [m for row in grid for m in row]
        import random
        rnd = random.Random(3)
        sh = flat[:]
        rnd.shuffle(sh)
        self.play(LaggedStart(*[FadeIn(m) for m in sh], lag_ratio=0.04), run_time=1.6)
        self.wait(1.0)
        n1 = para("Gom các bộ có cùng tập chữ cái thành một hàng:", 24, DIM, y=0.6)
        self.play(FadeIn(n1), run_time=0.5)
        boxes = VGroup()
        for i, row in enumerate(grid):
            self.play(row.animate.set_color(pal[i]), run_time=0.4)
            box = SurroundingRectangle(row, color=pal[i], buff=0.1, corner_radius=0.12)
            key = sorted(GROUPS)[i]
            lab = Text("{" + ",".join(key) + "}", font=FONT, font_size=20, color=pal[i]).next_to(box, RIGHT, buff=0.12)
            boxes.add(VGroup(box, lab))
            self.play(Create(box), FadeIn(lab), run_time=0.4)
        self.wait(1.0)
        e = para("Mỗi tập 3 chữ cái xuất hiện 3! = 6 lần", 28, WHITE, y=-0.2)
        self.play(FadeIn(e), run_time=0.5)
        self.wait(1.5)
        r = para("C(4, 3) = 24 / 6 = 4", 42, GOLD, y=-1.4)
        self.play(Write(r), run_time=0.8)
        self.wait(1.2)
        f = para("C(n, k) = P(n, k) / k! = n! / (k! (n−k)!)", 30, WHITE, y=-2.6)
        box = SurroundingRectangle(f, color=GOLD, buff=0.2, corner_radius=0.12)
        self.play(FadeIn(f), Create(box), run_time=0.7)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 5. Ban cán sự vs đội 3 người =====
        c = swap_cap(self, c, cap("Cùng 10 người, hai câu hỏi", 40, GOLD))
        l1 = para("Bầu lớp trưởng, lớp phó, thủ quỹ\n(vai trò khác nhau: có thứ tự)", 28, BLUE, y=4.6)
        r1 = para("P(10, 3) = 10 × 9 × 8 = 720", 36, BLUE, y=3.3)
        l2 = para("Chọn 3 người đi thi\n(cả đội như nhau: không thứ tự)", 28, GREEN, y=1.8)
        r2 = para("C(10, 3) = 720 / 3! = 120", 36, GREEN, y=0.5)
        for m in (l1, r1, l2, r2):
            self.play(FadeIn(m), run_time=0.6)
            self.wait(1.5)
        sym = para("Chọn 3 người đi = chọn 7 người ở lại:\nC(10, 3) = C(10, 7) = 120", 28, GOLD, y=-1.3)
        self.play(FadeIn(sym), run_time=0.6)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 5b. Bàn tròn =====
        c = swap_cap(self, c, cap("Xếp 5 người quanh bàn tròn", 40, GOLD))
        q = para("Chỉ quan tâm ai ngồi cạnh ai (xoay bàn không đổi)", 26, WHITE, y=5.2)
        self.play(FadeIn(q), run_time=0.5)
        ctr = np.array([0, 2.4, 0])
        table = Circle(radius=1.3, color=DIM, stroke_width=3).move_to(ctr)
        seats = VGroup()
        for i, ch in enumerate("ABCDE"):
            ang = PI / 2 - i * 2 * PI / 5
            p_ = ctr + 2.0 * np.array([np.cos(ang), np.sin(ang), 0])
            cc = Circle(radius=0.42, color=BLUE, stroke_width=3, fill_color=CELL, fill_opacity=1).move_to(p_)
            seats.add(VGroup(cc, Text(ch, font=FONT, font_size=30).move_to(cc)))
        self.play(Create(table), FadeIn(seats), run_time=0.8)
        self.wait(1.0)
        e1 = para("Xoay cả bàn: A B C D E, B C D E A, C D E A B, …\nđều là MỘT cách ngồi", 24, WHITE, y=-0.3)
        self.play(FadeIn(e1), run_time=0.5)
        spos = [s_.get_center().copy() for s_ in seats]
        for step in range(1, 6):
            self.play(*[seats[i].animate(path_arc=-2 * PI / 5).move_to(spos[(i + step) % 5]) for i in range(5)], run_time=0.7)
            self.wait(0.3)
        e2 = para("5! = 120 cách xếp hàng, mỗi cách ngồi bị đếm 5 lần", 24, WHITE, y=-1.6)
        self.play(FadeIn(e2), run_time=0.5)
        self.wait(1.5)
        e3 = para("120 / 5 = (5 − 1)! = 24 cách", 36, GOLD, y=-2.7)
        self.play(FadeIn(e3, scale=1.2), run_time=0.6)
        self.wait(1.5)
        e4 = para("Cách nghĩ khác: cố định A, xếp 4 người còn lại: 4! = 24", 22, DIM, y=-3.8)
        self.play(FadeIn(e4), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 5c. Ủy ban =====
        c = swap_cap(self, c, cap("Ghép hai lần chọn", 42, GOLD))
        q = para("Lớp có 8 nữ, 10 nam. Chọn ban 5 người\ngồm đúng 2 nữ và 3 nam?", 28, WHITE, y=5.0)
        self.play(FadeIn(q), run_time=0.6)
        self.wait(1.5)
        a1 = para("Chọn 2 nữ: C(8, 2) = 28", 30, RED, y=3.4)
        a2 = para("Chọn 3 nam: C(10, 3) = 120", 30, BLUE, y=2.4)
        a3 = para("Quy tắc nhân: 28 × 120 = 3360", 34, GOLD, y=1.2)
        for m in (a1, a2, a3):
            self.play(FadeIn(m), run_time=0.5)
            self.wait(1.5)
        w = para("Sai lầm hay gặp: C(18, 5) = 8568 là chọn 5 người bất kỳ,\nkhông bảo đảm đúng 2 nữ", 22, DIM, y=-0.3)
        self.play(FadeIn(w), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 6. Bảng 4 trường hợp =====
        c = swap_cap(self, c, cap("Lấy 2 từ {A, B, C}: bốn kiểu đếm", 38, GOLD))
        cells = [
            ("Có thứ tự, không lặp", OR, 3, "P(3,2) = 6", BLUE, (-2.05, 3.2)),
            ("Có thứ tự, có lặp", ORR, 3, "3² = 9", GOLD, (2.05, 3.2)),
            ("Không thứ tự, không lặp", UN, 3, "C(3,2) = 3", GREEN, (-2.05, -0.6)),
            ("Không thứ tự, có lặp", UNR, 3, "C(3+2−1, 2) = 6", RED, (2.05, -0.6)),
        ]
        for title, items, k, frm, col, (x, y) in cells:
            rect = RoundedRectangle(width=3.95, height=3.6, corner_radius=0.2, color=col, stroke_width=3).move_to([x, y, 0])
            tt = Text(title, font=FONT, font_size=22, color=col).move_to([x, y + 1.45, 0])
            fitw(tt, 3.7)
            it = Text(chunk(items, k), font=FONT, font_size=28, line_spacing=0.9).move_to([x, y + 0.35, 0])
            ff = Text(frm, font=FONT, font_size=26, color=col).move_to([x, y - 1.35, 0])
            fitw(ff, 3.7)
            self.play(Create(rect), FadeIn(tt), run_time=0.5)
            self.play(FadeIn(it), run_time=0.6)
            self.play(FadeIn(ff), run_time=0.5)
            self.wait(1.6)
        g = VGroup(*[Text(s, font=FONT, font_size=21, color=col) for s, col in [
            ("tổng quát: n!/(n−k)!", BLUE), ("tổng quát: nᵏ", GOLD), ("tổng quát: C(n,k)", GREEN), ("tổng quát: C(n+k−1, k)", RED)]])
        for m, (_, _, _, _, _, (x, y)) in zip(g, cells):
            m.move_to([x, y - 0.9, 0])
        self.play(FadeIn(g), run_time=0.6)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 7. Đố nhanh =====
        c = swap_cap(self, c, cap("Đố nhanh: dùng công thức nào?", 40, GOLD))
        qs = [
            ("Mã PIN 4 chữ số", "có thứ tự, có lặp:  10⁴ = 10 000", GOLD),
            ("Chọn 2 món từ thực đơn 5 món", "không thứ tự, không lặp:  C(5,2) = 10", GREEN),
            ("Xếp 3 trong 5 bạn vào 3 ghế khác nhau", "có thứ tự, không lặp:  P(5,3) = 60", BLUE),
            ("Mua 3 ly trà sữa từ 4 vị (được trùng vị)", "không thứ tự, có lặp:  C(6,3) = 20", RED),
        ]
        y = 4.8
        for qq, aa, col in qs:
            m = para(qq, 28, WHITE, y=y)
            self.play(FadeIn(m), run_time=0.5)
            self.wait(1.8)
            a = para(aa, 26, col, y=y - 0.65)
            self.play(FadeIn(a, shift=UP * 0.1), run_time=0.5)
            self.wait(1.5)
            y -= 1.9
        self.wait(1.0)
        last = para("Ly trà sữa là bài toán chia kẹo (stars and bars)\nở bài 7.5", 24, DIM, y=-3.4)
        self.play(FadeIn(last), run_time=0.5)
        self.wait(4.0)
