from common import *


# ---------- Toán: kiểm tra mọi khẳng định trong reel ----------
for n in range(1, 300):
    assert sum(range(1, n + 1)) == n * (n + 1) // 2
for k in range(1, 300):
    assert k * (k + 1) // 2 + (k + 1) == (k + 1) * (k + 2) // 2
    # n^2 + n: bước "lẻ -> lẻ" đúng về mặt đại số, nhưng n^2 + n luôn chẵn
    assert ((k + 1) ** 2 + (k + 1)) - (k * k + k) == 2 * (k + 1)
    assert (k * k + k) % 2 == 0


def is_prime(m):
    if m < 2:
        return False
    i = 2
    while i * i <= m:
        if m % i == 0:
            return False
        i += 1
    return True


EULER = [n * n + n + 41 for n in range(41)]
assert all(is_prime(v) for v in EULER[:40])
assert EULER[40] == 1681 == 41 * 41
assert EULER[:5] == [41, 43, 47, 53, 61] and EULER[39] == 1601
assert 60 == 6 * 10 == (2 * 3) * (2 * 5)


# ---------- Hình ----------
def domino_row(idx, x0=-3.75, s=0.74, y0=-1.0, h=1.35, w=0.22, color=WHITE):
    """Domino tại các vị trí idx (0-based). Trả về list (i, rect)."""
    out = []
    for i in idx:
        r = Rectangle(width=w, height=h, stroke_width=0, fill_color=color, fill_opacity=1)
        r.move_to([x0 + i * s + w / 2, y0 + h / 2, 0])
        out.append((i, r))
    return out


def fall_anims(rects, flat_last=True, flat=()):
    an = []
    for j, r in enumerate(rects):
        last = (j == len(rects) - 1 and flat_last) or j in flat
        ang = -PI / 2 if last else -68 * DEGREES
        an.append(Rotate(r, angle=ang, about_point=r.get_corner(DR)))
    return an


def tri_dots(n, x0, y0, d=0.5, color=GOLD, r=0.13):
    """Tam giác chấm: hàng i (từ trên, i = 1..n) có i chấm."""
    g = VGroup()
    for i in range(1, n + 1):
        for j in range(i):
            g.add(Dot([x0 + j * d, y0 - (i - 1) * d, 0], radius=r, color=color))
    return g


def comp_dots(n, x0, y0, d=0.5, color=BLUE, r=0.13):
    """Phần bù trong hình chữ nhật n x (n+1): hàng i có n+1-i chấm ở cột i..n."""
    g = VGroup()
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            g.add(Dot([x0 + j * d, y0 - (i - 1) * d, 0], radius=r, color=color))
    return g


def L(lines, size=30, color=WHITE, buff=0.3):
    g = VGroup(*[Text(s, font=FONT, font_size=size, color=c) for s, c in
                 [(x if isinstance(x, tuple) else (x, color)) for x in lines]])
    g.arrange(DOWN, aligned_edge=LEFT, buff=buff)
    if g.width > 7.8:
        g.scale_to_fit_width(7.8)
    return g


class Induction(Scene):
    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Chứng minh cho mọi n", 44)
        t1 = Text("Quy nạp\ntoán học", font=FONT, font_size=84, color=GOLD, line_spacing=1.0).move_to([0, 1.4, 0])
        t2 = para("Hai bước để chứng minh\nvô hạn mệnh đề P(1), P(2), P(3), …", 36, y=-1.4)
        self.play(FadeIn(c), Write(t1), run_time=1.3)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. Câu hỏi =====
        c = swap_cap(self, c, cap("Một công thức quen thuộc", 42, GOLD))
        f = para("1 + 2 + … + n = n(n+1)/2", 46, GOLD, y=4.6)
        self.play(Write(f), run_time=1.2)
        rows = []
        for n in range(1, 6):
            lhs = " + ".join(str(i) for i in range(1, n + 1))
            s = f"n = {n}:   {lhs} = {n*(n+1)//2}   ✓"
            rows.append((s, WHITE))
        chk = L(rows, 32, buff=0.35).move_to([0, 1.4, 0])
        for m in chk:
            m[-1].set_color(GREEN)
            self.play(FadeIn(m, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(1.0)
        q = para("Thử đến n = 5, n = 1000 vẫn đúng.\nNhưng n thì có vô hạn giá trị.", 32, DIM, y=-2.4)
        self.play(FadeIn(q), run_time=0.7)
        self.wait(2.5)
        q2 = para("Cần một lập luận đúng cho mọi n cùng lúc", 34, WHITE, y=-4.4)
        self.play(FadeIn(q2), run_time=0.7)
        self.wait(2.5)
        wipe(self, keep=[c])

        # ===== 3. Domino =====
        c = swap_cap(self, c, cap("Hình ảnh domino", 44, GOLD))
        floor = Line([-4.2, -1.0, 0], [4.2, -1.0, 0], color=DIM, stroke_width=3)
        dm = domino_row(range(11))
        rects = [r for _, r in dm]
        nums = VGroup(*[Text(str(i + 1), font=FONT, font_size=22, color=DIM).next_to(r, DOWN, buff=0.25) for i, r in dm])
        self.play(Create(floor), LaggedStart(*[FadeIn(r, shift=UP * 0.3) for r in rects], lag_ratio=0.08), run_time=1.4)
        self.play(FadeIn(nums), run_time=0.5)
        m1 = para("Viên thứ n đổ  =  P(n) đúng", 36, WHITE, y=3.6)
        self.play(FadeIn(m1), run_time=0.7)
        self.wait(2.0)
        r1 = para("① Viên số 1 đổ", 34, GREEN, y=-3.0)
        r1b = para("Bước cơ sở: P(1) đúng", 28, GREEN, y=-3.6)
        r2 = para("② Viên k đổ thì kéo viên k+1 đổ", 34, BLUE, y=-4.6)
        r2b = para("Bước quy nạp: P(k) ⇒ P(k+1), với mọi k", 28, BLUE, y=-5.2)
        self.play(FadeIn(r1), FadeIn(r1b), run_time=0.7)
        self.wait(1.8)
        self.play(FadeIn(r2), FadeIn(r2b), run_time=0.7)
        self.wait(2.5)
        push = Arrow([-4.4, 0.2, 0], [-3.8, 0.2, 0], color=GREEN, buff=0, stroke_width=6, max_tip_length_to_length_ratio=0.4)
        self.play(GrowArrow(push), run_time=0.5)
        self.play(LaggedStart(*fall_anims(rects), lag_ratio=0.35), run_time=4.0)
        m2 = para("Có đủ ① và ②  ⇒  mọi viên đều đổ", 34, GOLD, y=2.4)
        self.play(FadeIn(m2), run_time=0.7)
        self.wait(3.0)
        self.play(FadeOut(VGroup(*rects)), FadeOut(push), FadeOut(m2), FadeOut(nums), run_time=0.5)

        # Thiếu ①
        m3 = para("Thiếu ①: không ai đẩy viên đầu", 34, RED, y=2.4)
        dm = domino_row(range(11))
        rects = [r for _, r in dm]
        self.play(FadeIn(VGroup(*rects)), FadeIn(m3), r1.animate.set_opacity(0.25), r1b.animate.set_opacity(0.25), run_time=0.7)
        nofall = para("Không viên nào đổ, dù ② vẫn đúng", 28, DIM, y=1.6)
        self.play(FadeIn(nofall), run_time=0.6)
        self.wait(3.0)
        self.play(FadeOut(VGroup(*rects)), FadeOut(m3), FadeOut(nofall), r1.animate.set_opacity(1), r1b.animate.set_opacity(1), run_time=0.5)

        # Thiếu ② ở một chỗ
        m4 = para("Thiếu ② ở một chỗ: chuỗi bị đứt", 34, RED, y=2.4)
        idx = [i for i in range(11) if i not in (6, 7)]
        dm = domino_row(idx)
        rects = [r for _, r in dm]
        self.play(FadeIn(VGroup(*rects)), FadeIn(m4), r2.animate.set_opacity(0.25), r2b.animate.set_opacity(0.25), run_time=0.7)
        push = Arrow([-4.4, 0.2, 0], [-3.8, 0.2, 0], color=GREEN, buff=0, stroke_width=6, max_tip_length_to_length_ratio=0.4)
        self.play(GrowArrow(push), run_time=0.4)
        self.play(LaggedStart(*fall_anims(rects[:6]), lag_ratio=0.35), run_time=2.6)
        stop = para("Viên 9, 10, 11 vẫn đứng", 28, DIM, y=1.6)
        self.play(FadeIn(stop), run_time=0.6)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 4. Nguyên lý =====
        c = swap_cap(self, c, cap("Nguyên lý quy nạp", 44, GOLD))
        g = L([("Nếu", WHITE),
               ("  • P(n₀) đúng", GREEN),
               ("  • với mọi k ≥ n₀:  P(k) đúng ⇒ P(k+1) đúng", BLUE),
               ("thì P(n) đúng với mọi n ≥ n₀.", GOLD)], 32, buff=0.45).move_to([0, 3.0, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.2) for m in g], lag_ratio=0.5), run_time=2.6)
        self.wait(3.0)
        n1 = para("P(k) gọi là giả thiết quy nạp.", 30, WHITE, y=-0.6)
        n2 = para("k là một số bất kỳ ≥ n₀, không phải số cụ thể.\nTa không chứng minh P(k), ta chỉ giả sử nó\nđể suy ra P(k+1).", 28, DIM, y=-2.4)
        self.play(FadeIn(n1), run_time=0.6)
        self.wait(1.5)
        self.play(FadeIn(n2), run_time=0.7)
        self.wait(4.5)
        wipe(self, keep=[c])

        # ===== 5. Trực giác hình học =====
        c = swap_cap(self, c, cap("Vì sao lại là n(n+1)/2?", 42, GOLD))
        n = 4
        d = 0.62
        x0, y0 = -1.55, 4.3
        gold = tri_dots(n, x0, y0, d)
        lab = para("1 + 2 + 3 + 4", 32, GOLD, y=1.3)
        self.play(LaggedStart(*[GrowFromCenter(p) for p in gold], lag_ratio=0.08), run_time=1.4)
        self.play(FadeIn(lab), run_time=0.5)
        self.wait(1.2)
        blue = comp_dots(n, x0, y0, d)
        self.play(TransformFromCopy(gold, blue, path_arc=PI), run_time=1.8)
        box = SurroundingRectangle(VGroup(gold, blue), color=DIM, buff=0.2, stroke_width=2)
        w_l = Text("5 cột", font=FONT, font_size=26, color=DIM).next_to(box, UP, buff=0.15)
        h_l = Text("4 hàng", font=FONT, font_size=26, color=DIM).next_to(box, LEFT, buff=0.15)
        self.play(Create(box), FadeIn(w_l), FadeIn(h_l), run_time=0.8)
        e1 = para("2 · (1 + 2 + 3 + 4) = 4 · 5 = 20", 34, WHITE, y=0.3)
        self.play(FadeOut(lab), FadeIn(e1), run_time=0.7)
        self.wait(2.0)
        e2 = para("Tổng quát: 2 · (1 + … + n) = n(n+1)", 32, WHITE, y=-1.0)
        self.play(FadeIn(e2), run_time=0.7)
        self.wait(2.0)
        e3 = para("Hình vẽ cho ta đoán công thức.\nGiờ chứng minh chặt bằng quy nạp.", 30, DIM, y=-3.0)
        self.play(FadeIn(e3), run_time=0.7)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 6. Chứng minh =====
        c = swap_cap(self, c, cap("Chứng minh bằng quy nạp", 42, GOLD))
        pn = para("P(n):  1 + 2 + … + n = n(n+1)/2", 34, WHITE, y=5.2)
        self.play(FadeIn(pn), run_time=0.6)
        b_h = para("Bước cơ sở (n = 1)", 34, GREEN, y=4.1)
        b_1 = para("Vế trái = 1,   vế phải = 1·2/2 = 1   ✓", 30, WHITE, y=3.4)
        self.play(FadeIn(b_h), run_time=0.5)
        self.play(FadeIn(b_1), run_time=0.7)
        self.wait(2.2)
        s_h = para("Bước quy nạp", 34, BLUE, y=2.2)
        s_1 = para("Giả sử P(k) đúng:  1 + … + k = k(k+1)/2", 30, WHITE, y=1.5)
        s_2 = para("Cần chứng minh P(k+1):", 30, DIM, y=0.7)
        s_3 = para("1 + … + k + (k+1) = (k+1)(k+2)/2", 32, GOLD, y=0.05)
        self.play(FadeIn(s_h), run_time=0.5)
        self.play(FadeIn(s_1), run_time=0.7)
        self.wait(2.0)
        self.play(FadeIn(s_2), FadeIn(s_3), run_time=0.8)
        self.wait(2.5)
        ch = VGroup(
            Text("1 + … + k + (k+1)", font=FONT, font_size=32),
            Text("= k(k+1)/2 + (k+1)", font=FONT, font_size=32),
            Text("= (k+1)(k/2 + 1)", font=FONT, font_size=32),
            Text("= (k+1)(k+2)/2   ✓", font=FONT, font_size=32, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.32).move_to([-1.2, -2.3, 0])
        notes = [None,
                 Text("giả thiết quy nạp", font=FONT, font_size=24, color=GOLD),
                 Text("đặt k+1 ra ngoài", font=FONT, font_size=24, color=DIM),
                 None]
        self.play(FadeIn(ch[0]), run_time=0.6)
        for i in range(1, 4):
            an = [FadeIn(ch[i], shift=DOWN * 0.15)]
            if notes[i] is not None:
                notes[i].next_to(ch[i], RIGHT, buff=0.35)
                if notes[i].get_right()[0] > 4.0:
                    notes[i].shift(LEFT * (notes[i].get_right()[0] - 4.0))
                an.append(FadeIn(notes[i]))
            self.play(*an, run_time=0.8)
            self.wait(2.0 if i < 3 else 1.5)
        self.wait(1.0)
        # hình: thêm một hàng k+1 chấm
        k = 4
        tri = tri_dots(k, -1.5, -4.6, 0.36, GOLD, 0.09).scale(1.0)
        row = VGroup(*[Dot([-1.5 + j * 0.36, -4.6 - k * 0.36, 0], radius=0.09, color=GREEN) for j in range(k + 1)])
        tri.move_to([-2.0, -5.3, 0]); row.next_to(tri, DOWN, buff=0.27, aligned_edge=LEFT)
        grp = VGroup(tri, row).move_to([-2.4, -5.6, 0])
        t_l = Text("tổng cũ", font=FONT, font_size=24, color=GOLD).next_to(tri, RIGHT, buff=0.5)
        r_l = Text("+ hàng mới k+1", font=FONT, font_size=24, color=GREEN).next_to(row, RIGHT, buff=0.4)
        self.play(FadeIn(tri), FadeIn(t_l), run_time=0.6)
        self.play(LaggedStart(*[GrowFromCenter(p) for p in row], lag_ratio=0.1), FadeIn(r_l), run_time=1.0)
        self.wait(3.0)
        self.play(*[FadeOut(m) for m in [b_h, b_1, s_h, s_1, s_2, s_3, ch, notes[1], notes[2], tri, row, t_l, r_l]], run_time=0.6)
        conc = para("Cơ sở đúng, bước quy nạp đúng.\nTheo nguyên lý quy nạp:\nP(n) đúng với mọi n ≥ 1.", 36, GOLD, y=1.5)
        self.play(FadeIn(conc), run_time=0.8)
        self.wait(4.0)
        wipe(self, keep=[c])

        # ===== 7. Thử nhiều giá trị chưa đủ =====
        c = swap_cap(self, c, cap("Thử nhiều giá trị chưa phải chứng minh", 34, GOLD))
        fe = para("n² + n + 41 có luôn là số nguyên tố?", 34, WHITE, y=5.0)
        self.play(FadeIn(fe), run_time=0.7)
        lines = []
        for n in [0, 1, 2, 3, 4]:
            lines.append(f"n = {n}:   {EULER[n]}")
        lines += ["…", "n = 39:   1601"]
        g = VGroup(*[Text(s, font=FONT, font_size=30) for s in lines]).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to([-1.2, 1.5, 0])
        oks = VGroup(*[Text("nguyên tố", font=FONT, font_size=26, color=GREEN).next_to(m, RIGHT, buff=0.6) for m in g if m.text != "…"])
        self.play(LaggedStart(*[FadeIn(m) for m in g], lag_ratio=0.25), run_time=2.2)
        self.play(FadeIn(oks), run_time=0.6)
        a40 = para("40 lần liên tiếp đều đúng…", 30, DIM, y=-1.6)
        self.play(FadeIn(a40), run_time=0.6)
        self.wait(2.0)
        bad = para("n = 40:   1681 = 41 · 41", 38, RED, y=-2.9)
        self.play(FadeIn(bad, scale=1.2), run_time=0.8)
        self.wait(2.0)
        moral = para("Kiểm tra từng trường hợp không thay được\nbước quy nạp cho k bất kỳ.", 30, WHITE, y=-4.8)
        self.play(FadeIn(moral), run_time=0.7)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 8. Chứng minh sai 1: quên bước cơ sở =====
        c = swap_cap(self, c, cap("Chứng minh sai 1: quên bước cơ sở", 36, RED))
        cl = para("“Mệnh đề”: n² + n là số lẻ với mọi n ≥ 1", 32, WHITE, y=5.1)
        self.play(FadeIn(cl), run_time=0.7)
        st = VGroup(
            Text("Giả sử k² + k lẻ. Khi đó", font=FONT, font_size=30, color=BLUE),
            Text("(k+1)² + (k+1) = (k² + k) + 2(k+1)", font=FONT, font_size=30),
            Text("= số lẻ + số chẵn = số lẻ", font=FONT, font_size=30),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.32).move_to([0, 3.0, 0])
        for m in st:
            self.play(FadeIn(m), run_time=0.7)
            self.wait(1.4)
        okk = para("Bước quy nạp hoàn toàn đúng!", 32, GREEN, y=1.1)
        self.play(FadeIn(okk), run_time=0.6)
        self.wait(2.0)
        base = para("Nhưng n = 1:  1 + 1 = 2  là số chẵn  ✗", 32, RED, y=-0.2)
        self.play(FadeIn(base), run_time=0.7)
        self.wait(2.0)
        tr = para("Thật ra n² + n = n(n+1) là tích hai số liên tiếp,\nnên luôn chẵn. Mệnh đề sai với mọi n.", 28, DIM, y=-1.7)
        self.play(FadeIn(tr), run_time=0.7)
        self.wait(3.0)
        floor = Line([-4.2, -5.0, 0], [4.2, -5.0, 0], color=DIM, stroke_width=3)
        dm = domino_row(range(11), y0=-5.0, h=1.1)
        self.play(FadeIn(floor), FadeIn(VGroup(*[r for _, r in dm])), run_time=0.6)
        nd = para("Bước ② đúng mà không có viên đầu tiên đổ", 28, WHITE, y=-5.8)
        self.play(FadeIn(nd), run_time=0.6)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 9. Chứng minh sai 2: ngựa cùng màu =====
        c = swap_cap(self, c, cap("Chứng minh sai 2: mọi con ngựa cùng màu", 32, RED))
        cl = para("“Mệnh đề”: trong mọi đàn n con ngựa,\ncác con đều cùng màu", 32, WHITE, y=5.0)
        self.play(FadeIn(cl), run_time=0.7)
        bs = para("Cơ sở n = 1: một con thì cùng màu  ✓", 30, GREEN, y=3.6)
        self.play(FadeIn(bs), run_time=0.6)
        self.wait(1.5)
        sh = para("Bước quy nạp: xét đàn k+1 con", 30, BLUE, y=2.6)
        self.play(FadeIn(sh), run_time=0.6)
        K1 = 6
        xs = [-3.0 + i * 1.2 for i in range(K1)]
        horses = VGroup(*[VGroup(Circle(radius=0.42, color=GOLD, fill_color=GOLD, fill_opacity=0.35, stroke_width=4),
                                 Text(str(i + 1) if i < K1 - 1 else "k+1", font=FONT, font_size=24 if i < K1 - 1 else 20)).move_to([x, 0.6, 0])
                          for i, x in enumerate(xs)])
        horses[K1 - 2][1].become(Text("k", font=FONT, font_size=24).move_to(horses[K1 - 2][0]))
        horses[K1 - 3][1].become(Text("…", font=FONT, font_size=24).move_to(horses[K1 - 3][0]))
        self.play(LaggedStart(*[FadeIn(h) for h in horses], lag_ratio=0.1), run_time=1.0)
        top = Brace(VGroup(*horses[:K1 - 1]), UP, color=BLUE, buff=0.15)
        topl = Text("bỏ con cuối: k con, cùng màu", font=FONT, font_size=24, color=BLUE).next_to(top, UP, buff=0.1)
        bot = Brace(VGroup(*horses[1:]), DOWN, color=GREEN, buff=0.15)
        botl = Text("bỏ con đầu: k con, cùng màu", font=FONT, font_size=24, color=GREEN).next_to(bot, DOWN, buff=0.1)
        self.play(GrowFromCenter(top), FadeIn(topl), run_time=0.8)
        self.wait(1.5)
        self.play(GrowFromCenter(bot), FadeIn(botl), run_time=0.8)
        self.wait(1.5)
        mid = para("Phần chung nối hai nhóm ⇒ cả đàn cùng màu?", 30, WHITE, y=-1.6)
        self.play(FadeIn(mid), run_time=0.6)
        self.wait(3.0)
        self.play(*[FadeOut(m) for m in [horses, top, topl, bot, botl, mid]], run_time=0.5)
        wh = para("Thử bước từ k = 1 sang k + 1 = 2", 30, GOLD, y=1.7)
        h1 = VGroup(Circle(radius=0.5, color=GOLD, fill_color=GOLD, fill_opacity=0.5, stroke_width=4), Text("1", font=FONT, font_size=28)).move_to([-1.0, 0.0, 0])
        h2 = VGroup(Circle(radius=0.5, color=BLUE, fill_color=BLUE, fill_opacity=0.5, stroke_width=4), Text("2", font=FONT, font_size=28)).move_to([1.0, 0.0, 0])
        self.play(FadeIn(wh), FadeIn(h1), FadeIn(h2), run_time=0.7)
        b1 = SurroundingRectangle(h1, color=BLUE, buff=0.15)
        b2 = SurroundingRectangle(h2, color=GREEN, buff=0.15)
        l1 = Text("bỏ con cuối", font=FONT, font_size=22, color=BLUE).next_to(b1, DOWN, buff=0.15)
        l2 = Text("bỏ con đầu", font=FONT, font_size=22, color=GREEN).next_to(b2, DOWN, buff=0.15)
        self.play(Create(b1), Create(b2), FadeIn(l1), FadeIn(l2), run_time=0.8)
        emp = para("Hai nhóm không có con chung!", 34, RED, y=-2.0)
        self.play(FadeIn(emp), run_time=0.6)
        self.wait(2.0)
        ex = para("Nên P(1) ⇒ P(2) sai. Bước quy nạp phải đúng\nvới MỌI k, kể cả k nhỏ nhất.\nỞ đây chuỗi domino gãy ngay viên thứ hai.", 28, DIM, y=-4.0)
        self.play(FadeIn(ex), run_time=0.7)
        self.wait(5.0)
        wipe(self, keep=[c])

        # ===== 10. Quy nạp mạnh =====
        c = swap_cap(self, c, cap("Quy nạp mạnh", 44, GOLD))
        d1 = L([("Giả thiết: P(n₀), P(n₀+1), …, P(k) đều đúng", BLUE),
                ("Cần chứng minh: P(k+1)", GOLD)], 30, buff=0.35).move_to([0, 4.7, 0])
        self.play(FadeIn(d1), run_time=0.8)
        self.wait(2.5)
        ex = para("Ví dụ: mọi n ≥ 2 là tích các số nguyên tố", 32, WHITE, y=3.0)
        self.play(FadeIn(ex), run_time=0.7)
        cases = L([("• k+1 nguyên tố: xong.", WHITE),
                   ("• k+1 là hợp số: k+1 = a · b, với 2 ≤ a, b ≤ k", WHITE),
                   ("  P(a) và P(b) đúng ⇒ ghép lại được k+1", GREEN)], 28, buff=0.35).move_to([0, 1.3, 0])
        for m in cases:
            self.play(FadeIn(m), run_time=0.7)
            self.wait(1.6)
        # cây phân tích 60
        def node(s, p, col=WHITE):
            return Text(s, font=FONT, font_size=34, color=col).move_to(p)
        n60 = node("60", [0, -1.0, 0], GOLD)
        n6 = node("6", [-1.6, -2.4, 0]); n10 = node("10", [1.6, -2.4, 0])
        leaves = [node("2", [-2.4, -3.8, 0], GREEN), node("3", [-0.8, -3.8, 0], GREEN),
                  node("2", [0.8, -3.8, 0], GREEN), node("5", [2.4, -3.8, 0], GREEN)]
        edges = VGroup(*[Line(a.get_center(), b.get_center(), color=DIM, stroke_width=2, buff=0.3) for a, b in
                         [(n60, n6), (n60, n10), (n6, leaves[0]), (n6, leaves[1]), (n10, leaves[2]), (n10, leaves[3])]])
        self.play(FadeIn(n60), run_time=0.4)
        self.play(Create(edges[0]), Create(edges[1]), FadeIn(n6), FadeIn(n10), run_time=0.8)
        self.play(*[Create(e) for e in edges[2:]], *[FadeIn(x) for x in leaves], run_time=0.8)
        res = para("60 = 6 · 10 = (2 · 3) · (2 · 5)", 32, WHITE, y=-4.9)
        self.play(FadeIn(res), run_time=0.6)
        why = para("6 và 10 nhỏ hơn 60 nhưng không phải 59:\ncần giả thiết cho mọi số nhỏ hơn, không chỉ P(k).", 26, DIM, y=-6.0)
        self.play(FadeIn(why), run_time=0.6)
        self.wait(5.0)
        wipe(self, keep=[c])

        # ===== 11. Tổng kết =====
        c = swap_cap(self, c, cap("Khuôn trình bày một chứng minh", 38, GOLD))
        steps = L([("1. Phát biểu P(n) và miền của n", WHITE),
                   ("2. Bước cơ sở: kiểm tra P(n₀)", GREEN),
                   ("3. Giả sử P(k) đúng, với k ≥ n₀ bất kỳ", BLUE),
                   ("4. Suy ra P(k+1), có dùng P(k)", BLUE),
                   ("5. Kết luận theo nguyên lý quy nạp", GOLD)], 32, buff=0.5).move_to([0, 2.2, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.2) for m in steps], lag_ratio=0.5), run_time=3.0)
        self.wait(2.0)
        end = para("Thiếu bước 2 hoặc bước 4 sai ở một k nào đó,\ncả chứng minh sụp đổ.", 30, DIM, y=-2.4)
        self.play(FadeIn(end), run_time=0.7)
        self.wait(5.0)
