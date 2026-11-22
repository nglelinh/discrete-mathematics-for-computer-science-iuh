from common import *
from math import comb
from itertools import product


def sols(n, r, lo=None, hi=None):
    lo = lo or [0] * n
    hi = hi or [r] * n
    return [t for t in product(*[range(lo[i], hi[i] + 1) for i in range(n)]) if sum(t) == r]


def word(t):
    return "|".join("*" * x for x in t)


# ---------- Toán ----------
S5 = sols(3, 5)
assert len(S5) == 21 == comb(7, 2)
W5 = [word(t) for t in S5]
assert len(set(W5)) == 21 and all(w.count("*") == 5 and w.count("|") == 2 and len(w) == 7 for w in W5)
assert word((2, 3, 0)) == "**|***|" and word((0, 0, 5)) == "||*****" and word((1, 2, 2)) == "*|**|**"
assert len(sols(4, 10)) == comb(13, 3) == 286
assert len(sols(3, 5, lo=[1, 1, 1])) == comb(4, 2) == 6
assert len(sols(3, 12, lo=[2, 1, 4])) == comb(7, 2) == 21 and 12 - 2 - 1 - 4 == 5
UP4 = sols(3, 10, hi=[4, 4, 4])
assert len(UP4) == 6 == comb(12, 2) - 3 * comb(7, 2) + 3 * 1 and comb(12, 2) == 66
assert sorted(UP4) == [(2, 4, 4), (3, 3, 4), (3, 4, 3), (4, 2, 4), (4, 3, 3), (4, 4, 2)]
assert len(sols(3, 10, lo=[5, 0, 0])) == 21 and len(sols(3, 10, lo=[5, 5, 0])) == 1 and len(sols(3, 10, lo=[5, 5, 5])) == 0
assert comb(4 + 6 - 1, 6) == 84 and comb(3, 5) == 0
KCOL = [RED, "#f2a0c0", BLUE]     # sô-cô-la, dâu, việt quất


def star(r=0.16, col=GOLD):
    return Star(n=5, outer_radius=r, inner_radius=r * 0.45, color=col, fill_color=col, fill_opacity=1, stroke_width=1)


def bar(h=0.5, col=WHITE):
    return Line(UP * h / 2, DOWN * h / 2, color=col, stroke_width=6)


def sb(t, unit=0.42, r=0.16, h=0.5, colored=False):
    g = VGroup()
    k = 0
    for i, x in enumerate(t):
        for _ in range(x):
            g.add(star(r, KCOL[i] if colored else GOLD).move_to([k * unit, 0, 0]))
            k += 1
        if i < len(t) - 1:
            g.add(bar(h).move_to([k * unit, 0, 0]))
            k += 1
    return g


class StarsBars(Scene):
    def wait(self, duration=1.0, **kw):
        super().wait(duration * 1.6, **kw)

    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Tổ hợp có lặp", 44)
        t1 = Text("Sao và vạch", font=FONT, font_size=84, color=GOLD).move_to([0, 2.0, 0])
        t2 = para("Stars and bars: đếm cách chọn khi\nđược lấy trùng và không xét thứ tự", 30, y=0.2)
        demo = sb((2, 3, 0), unit=0.6, r=0.24, h=0.8).move_to([0, -1.6, 0])
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), LaggedStart(*[FadeIn(m) for m in demo], lag_ratio=0.1), run_time=1.2)
        self.wait(2.5)
        self.play(FadeOut(t1), FadeOut(t2), FadeOut(demo), run_time=0.5)

        # ===== 2. Bài toán bánh =====
        c = swap_cap(self, c, cap("Chọn 5 chiếc bánh từ 3 loại", 40, GOLD))
        q = para("Ba loại: sô-cô-la, dâu, việt quất. Mỗi loại còn rất nhiều.\nCó bao nhiêu cách chọn 5 chiếc (chỉ quan tâm số lượng mỗi loại)?", 24, WHITE, y=5.3)
        self.play(FadeIn(q), run_time=0.7)
        names = ["sô-cô-la", "dâu", "việt quất"]
        boxes = VGroup()
        for i in range(3):
            b = RoundedRectangle(width=2.3, height=1.5, corner_radius=0.15, color=KCOL[i], stroke_width=3).move_to([-2.6 + 2.6 * i, 3.0, 0])
            l = Text(names[i], font=FONT, font_size=24, color=KCOL[i]).next_to(b, DOWN, buff=0.15)
            boxes.add(VGroup(b, l))
        self.play(FadeIn(boxes), run_time=0.6)
        examples = [((2, 3, 0), "2 sô-cô-la, 3 dâu, 0 việt quất"), ((0, 0, 5), "cả 5 chiếc đều việt quất"), ((1, 2, 2), "1, 2, 2")]
        y = 0.6
        for t, desc in examples:
            inbox = VGroup()
            for i, x in enumerate(t):
                for j in range(x):
                    inbox.add(star(0.2, KCOL[i]).move_to(boxes[i][0].get_center() + np.array([-0.75 + (j % 4) * 0.5, 0.25 - (j // 4) * 0.5, 0])))
            self.play(LaggedStart(*[FadeIn(s, scale=1.5) for s in inbox], lag_ratio=0.1), run_time=0.8)
            d = Text(f"({t[0]}, {t[1]}, {t[2]})   {desc}", font=FONT, font_size=24).move_to([0, y + 0.55, 0])
            fitw(d, 7.8)
            self.play(FadeIn(d), run_time=0.4)
            line = sb(t, colored=True).move_to([0, y, 0])
            self.play(TransformFromCopy(inbox, VGroup(*[m for m in line if isinstance(m, Star)])),
                      *[FadeIn(m) for m in line if not isinstance(m, Star)], run_time=1.0)
            self.wait(1.4)
            self.play(FadeOut(inbox), run_time=0.3)
            y -= 1.6
        k = para("Bỏ hộp đi: mỗi cách chọn = một dãy 5 sao và 2 vạch.\nVạch là vách ngăn giữa các loại.", 26, GOLD, y=-4.6)
        self.play(FadeIn(k), run_time=0.6)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 3. Đếm: chọn vị trí cho 2 vạch =====
        c = swap_cap(self, c, cap("7 ô, chọn 2 ô làm vạch", 42, GOLD))
        slots = VGroup(*[Square(0.85, color=DIM, stroke_width=2).move_to([-3.0 + i * 1.0, 3.6, 0]) for i in range(7)])
        nums = VGroup(*[Text(str(i + 1), font=FONT, font_size=20, color=DIM).next_to(slots[i], DOWN, buff=0.1) for i in range(7)])
        self.play(FadeIn(slots), FadeIn(nums), run_time=0.6)
        content = VGroup()
        demo_pairs = [(2, 6), (0, 1), (1, 4), (4, 5)]
        for (a, b) in demo_pairs:
            new = VGroup(*[(bar(0.6) if i in (a, b) else star(0.2)).move_to(slots[i]) for i in range(7)])
            tup = []
            run = 0
            for i in range(7):
                if i in (a, b):
                    tup.append(run)
                    run = 0
                else:
                    run += 1
            tup.append(run)
            assert sum(tup) == 5 and len(tup) == 3
            lab = Text(f"vạch ở ô {a + 1}, {b + 1}   →   ({tup[0]}, {tup[1]}, {tup[2]})", font=FONT, font_size=28).move_to([0, 2.2, 0])
            if len(content):
                self.play(Transform(content, VGroup(new, lab)), run_time=0.6)
            else:
                content = VGroup(new, lab)
                self.play(FadeIn(content), run_time=0.6)
            self.wait(1.2)
        r = para("Số cách = C(7, 2) = 21", 44, GOLD, y=0.9)
        self.play(Write(r), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(content), run_time=0.4)
        # liệt kê 21
        grid = VGroup()
        for idx, t in enumerate(S5):
            col_, row_ = divmod(idx, 7)
            g = sb(t, unit=0.27, r=0.1, h=0.32)
            lbl = Text(f"({t[0]},{t[1]},{t[2]})", font=FONT, font_size=18, color=DIM)
            item = VGroup(g, lbl).arrange(RIGHT, buff=0.15)
            item.move_to([-2.85 + col_ * 2.85, -0.1 - row_ * 0.62, 0])
            grid.add(item)
        self.play(LaggedStart(*[FadeIn(m) for m in grid], lag_ratio=0.06), run_time=3.0)
        n1 = para("Đủ cả 21 dãy, không thiếu, không trùng (song ánh)", 24, WHITE, y=-4.6)
        self.play(FadeIn(n1), run_time=0.5)
        self.wait(4.0)
        wipe(self, keep=[c])

        # ===== 4. Tổng quát =====
        c = swap_cap(self, c, cap("Công thức tổng quát", 44, GOLD))
        g = VGroup(*[Text(s, font=FONT, font_size=30, color=col) for s, col in [
            ("Chọn r đồ vật từ n loại (được lặp)", WHITE),
            ("= số nghiệm nguyên ≥ 0 của x₁ + x₂ + … = r (n biến)", WHITE),
            ("r sao + (n − 1) vạch, chọn chỗ cho vạch:", DIM),
        ]]).arrange(DOWN, buff=0.35)
        fitw(g, 7.8).move_to([0, 4.4, 0])
        for m in g:
            self.play(FadeIn(m), run_time=0.6)
            self.wait(1.2)
        f = para("C(r + n − 1, n − 1) = C(r + n − 1, r)", 36, GOLD, y=2.3)
        box = SurroundingRectangle(f, color=GOLD, buff=0.2, corner_radius=0.12)
        self.play(Write(f), Create(box), run_time=1.0)
        self.wait(2.0)
        e1 = para("x₁ + x₂ + x₃ + x₄ = 10:   C(13, 3) = 286 nghiệm", 30, WHITE, y=0.8)
        self.play(FadeIn(e1), run_time=0.6)
        self.wait(2.0)
        e2 = para("Chọn 6 viên kẹo từ 4 loại:   C(9, 6) = 84", 30, WHITE, y=-0.1)
        self.play(FadeIn(e2), run_time=0.6)
        self.wait(2.0)
        w = para("Không nhầm với C(n, r): chọn 5 từ 3 loại thì C(3, 5) = 0,\nnhưng có lặp vẫn có 21 cách.", 24, RED, y=-1.5)
        self.play(FadeIn(w), run_time=0.6)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 5. Ràng buộc dưới =====
        c = swap_cap(self, c, cap("Ràng buộc dưới: phát trước", 40, GOLD))
        q = para("x₁ + x₂ + x₃ = 12  với  x₁ ≥ 2, x₂ ≥ 1, x₃ ≥ 4", 30, WHITE, y=5.2)
        self.play(FadeIn(q), run_time=0.6)
        self.wait(1.2)
        pre = sb((2, 1, 4), unit=0.5, r=0.19, h=0.6, colored=True).move_to([0, 3.9, 0])
        pl = para("Đặt sẵn 2 + 1 + 4 = 7 sao vào đúng nhóm", 24, DIM, y=3.2)
        self.play(FadeIn(pre), FadeIn(pl), run_time=0.8)
        self.wait(1.5)
        y1 = para("Còn 5 sao chia tự do:  y₁ + y₂ + y₃ = 5", 30, WHITE, y=2.2)
        self.play(FadeIn(y1), run_time=0.6)
        self.wait(1.5)
        r = para("C(7, 2) = 21 nghiệm", 40, GOLD, y=1.1)
        self.play(Write(r), run_time=0.7)
        self.wait(2.0)
        e = para("Mỗi bạn ít nhất 1 chiếc (5 bánh, 3 bạn):\nphát trước mỗi bạn 1, còn 2 → C(4, 2) = 6", 26, BLUE, y=-0.6)
        self.play(FadeIn(e), run_time=0.6)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 6. Ràng buộc trên =====
        c = swap_cap(self, c, cap("Ràng buộc trên: cần bù trừ", 40, GOLD))
        q = para("x₁ + x₂ + x₃ = 10, mỗi biến không quá 4", 32, WHITE, y=5.2)
        self.play(FadeIn(q), run_time=0.6)
        lines = VGroup(*[Text(s, font=FONT, font_size=28, color=col) for s, col in [
            ("Không ràng buộc:  C(12, 2) = 66", WHITE),
            ("Một biến ≥ 5 (bớt 5):  3 × C(7, 2) = 63", RED),
            ("Hai biến ≥ 5 (tổng còn 0):  3 × 1 = 3", GREEN),
            ("Ba biến ≥ 5: không thể", DIM),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        fitw(lines, 7.8).move_to([0, 3.0, 0])
        for m in lines:
            self.play(FadeIn(m, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(1.4)
        r = para("66 − 63 + 3 = 6", 44, GOLD, y=0.6)
        self.play(Write(r), run_time=0.7)
        self.wait(1.2)
        sl = VGroup()
        for i, t in enumerate(sorted(UP4)):
            g = sb(t, unit=0.3, r=0.11, h=0.36)
            lbl = Text(f"({t[0]},{t[1]},{t[2]})", font=FONT, font_size=22, color=DIM)
            item = VGroup(g, lbl).arrange(RIGHT, buff=0.3)
            item.move_to([0, -0.4 - i * 0.62, 0])
            sl.add(item)
        self.play(LaggedStart(*[FadeIn(m) for m in sl], lag_ratio=0.2), run_time=1.6)
        n2 = para("Đúng 6 nghiệm: các hoán vị của (4,4,2) và (4,3,3)", 24, WHITE, y=-4.4)
        self.play(FadeIn(n2), run_time=0.5)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 7. Tóm tắt =====
        c = swap_cap(self, c, cap("Tóm tắt", 44, GOLD))
        sm = VGroup(*[Text(s, font=FONT, font_size=28, color=col) for s, col in [
            ("r đồ vật, n loại, được lặp, không thứ tự", WHITE),
            ("→ r sao, n − 1 vạch → C(r + n − 1, n − 1)", GOLD),
            ("Ràng buộc dưới: phát trước rồi chia phần còn lại", BLUE),
            ("Ràng buộc trên: trừ các nghiệm vượt (bù trừ)", GREEN),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        fitw(sm, 7.8).move_to([0, 3.0, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.2) for m in sm], lag_ratio=0.5), run_time=2.6)
        demo = sb((2, 3, 0), unit=0.6, r=0.24, h=0.8, colored=True).move_to([0, -0.4, 0])
        self.play(FadeIn(demo), run_time=0.6)
        self.wait(5.0)
