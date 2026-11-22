from common import *
from itertools import product

# ---------- Toán ----------
A12 = list(range(12))
R3 = {(a, b) for a in A12 for b in A12 if (a - b) % 3 == 0}
assert all((a, a) in R3 for a in A12)
assert all((b, a) in R3 for a, b in R3)
assert all((a, d) in R3 for a, b in R3 for c, d in R3 if b == c)
CLS = {r: [a for a in A12 if a % 3 == r] for r in range(3)}
assert CLS == {0: [0, 3, 6, 9], 1: [1, 4, 7, 10], 2: [2, 5, 8, 11]}
assert sorted(sum(CLS.values(), [])) == A12   # phân hoạch: rời nhau, phủ hết

D12 = [1, 2, 3, 4, 6, 12]
REL = [(a, b) for a in D12 for b in D12 if b % a == 0]
LOOPS = [(a, b) for a, b in REL if a == b]
NONLOOP = [(a, b) for a, b in REL if a != b]
COVER = [(a, b) for a, b in NONLOOP if not any(c not in (a, b) and c % a == 0 and b % c == 0 for c in D12)]
TRANS = [p for p in NONLOOP if p not in COVER]
assert len(REL) == 18 and len(LOOPS) == 6 and len(NONLOOP) == 12
assert sorted(COVER) == [(1, 2), (1, 3), (2, 4), (2, 6), (3, 6), (4, 12), (6, 12)] and len(TRANS) == 5
# phản đối xứng, bắc cầu
assert all(not ((b, a) in REL) for a, b in NONLOOP)
assert all((a, d) in REL for a, b in REL for c, d in REL if b == c)
assert 6 % 4 and 4 % 6                       # 4, 6 không so sánh được
SUB = [2, 3, 4, 6]
MINL = [x for x in SUB if not any(y != x and x % y == 0 for y in SUB)]
MAXL = [x for x in SUB if not any(y != x and y % x == 0 for y in SUB)]
assert MINL == [2, 3] and MAXL == [4, 6]
assert not any(all(y % x == 0 for y in SUB) for x in SUB) and not any(all(x % y == 0 for y in SUB) for x in SUB)

D30 = [1, 2, 3, 5, 6, 10, 15, 30]
SET = {1: "∅", 2: "{a}", 3: "{b}", 5: "{c}", 6: "{a,b}", 10: "{a,c}", 15: "{b,c}", 30: "{a,b,c}"}
PR = {"a": 2, "b": 3, "c": 5}


def as_set(n):
    return {k for k, p in PR.items() if n % p == 0}


for x in D30:
    assert SET[x] == ("∅" if x == 1 else "{" + ",".join(sorted(as_set(x))) + "}")
    for y in D30:
        assert (y % x == 0) == (as_set(x) <= as_set(y))
C30 = [(a, b) for a in D30 for b in D30 if a != b and b % a == 0 and not any(c not in (a, b) and c % a == 0 and b % c == 0 for c in D30)]
assert len(C30) == 12

R = 0.42
P12 = {1: (0, -0.2), 2: (-1.4, 1.3), 3: (1.4, 1.3), 4: (-2.8, 2.8), 6: (0, 2.8), 12: (-1.4, 4.3)}
P30 = {1: (0, -0.4), 2: (-2.3, 1.1), 3: (0, 1.1), 5: (2.3, 1.1), 6: (-2.3, 2.6), 10: (0, 2.6), 15: (2.3, 2.6), 30: (0, 4.1)}


def v3(p):
    return np.array([p[0], p[1], 0])


def node(lbl, p, col=BLUE, size=30):
    c = Circle(R, color=col, stroke_width=4, fill_color=CELL, fill_opacity=1).move_to(v3(p))
    return VGroup(c, Text(str(lbl), font=FONT, font_size=size).move_to(c))


def arrow(p, q, angle=0.0, col=DIM, tip=True):
    a, b = v3(p), v3(q)
    d = (b - a) / np.linalg.norm(b - a)
    s, e = a + d * (R + 0.05), b - d * (R + 0.05)
    if angle == 0:
        return Arrow(s, e, buff=0, color=col, stroke_width=3, max_tip_length_to_length_ratio=0.12) if tip else Line(s, e, color=col, stroke_width=3)
    return CurvedArrow(s, e, angle=angle, color=col, stroke_width=3, tip_length=0.2)


def loop(p, col=DIM):
    return Circle(0.2, color=col, stroke_width=3).move_to(v3(p) + np.array([R + 0.08, R + 0.08, 0]))


class Relations(Scene):
    def wait(self, duration=1.0, **kw):
        super().wait(duration * 1.5, **kw)

    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Quan hệ trên một tập hợp", 40)
        t1 = Text("Tương đương\n& Thứ tự", font=FONT, font_size=80, color=GOLD, line_spacing=1.0).move_to([0, 1.6, 0])
        t2 = para("Một bên gom nhóm (phân hoạch),\nmột bên sắp xếp (sơ đồ Hasse)", 30, y=-1.0)
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. Ba tính chất =====
        c = swap_cap(self, c, cap("Quan hệ tương đương: 3 tính chất", 38, GOLD))
        items = [
            ("Phản xạ", "a ~ a với mọi a", BLUE),
            ("Đối xứng", "a ~ b  ⇒  b ~ a", GREEN),
            ("Bắc cầu", "a ~ b, b ~ c  ⇒  a ~ c", GOLD),
        ]
        y = 4.6
        for k, (nm, rule, col) in enumerate(items):
            t = Text(nm, font=FONT, font_size=32, color=col).move_to([-2.4, y, 0])
            r = Text(rule, font=FONT, font_size=26).move_to([1.4, y, 0])
            if k == 0:
                pic = VGroup(node("a", (-2.4, y - 1.0), col, 26))
                pic.add(loop((-2.4, y - 1.0), col))
            elif k == 1:
                pic = VGroup(node("a", (-3.2, y - 1.0), col, 26), node("b", (-1.6, y - 1.0), col, 26),
                             CurvedArrow(v3((-2.75, y - 0.9)), v3((-2.05, y - 0.9)), angle=-0.8, color=col, tip_length=0.15),
                             CurvedArrow(v3((-2.05, y - 1.1)), v3((-2.75, y - 1.1)), angle=-0.8, color=col, tip_length=0.15))
            else:
                pa, pb, pc = (-3.4, y - 1.55), (-1.2, y - 0.75), (1.0, y - 1.55)
                pic = VGroup(node("a", pa, col, 26), node("b", pb, col, 26), node("c", pc, col, 26),
                             arrow(pa, pb, col=col), arrow(pb, pc, col=col), arrow(pa, pc, col=RED))
            self.play(FadeIn(t), FadeIn(r), FadeIn(pic), run_time=0.7)
            self.wait(1.6)
            y -= 2.2
        ex = para("Ví dụ: a ~ b khi a − b chia hết cho 3 (đồng dư mod 3)", 26, WHITE, y=-2.4)
        self.play(FadeIn(ex), run_time=0.6)
        self.wait(2.5)
        wipe(self, keep=[c])

        # ===== 3. Mod 3 -> lớp tương đương =====
        c = swap_cap(self, c, cap("Đồng dư mod 3 trên {0, 1, …, 11}", 38, GOLD))
        nums = {}
        for i, a in enumerate(A12):
            ang = PI / 2 - i * TAU / 12
            nums[a] = node(a, (2.4 * np.cos(ang), 2.6 + 2.4 * np.sin(ang)), DIM, 28)
        self.play(LaggedStart(*[GrowFromCenter(m) for m in nums.values()], lag_ratio=0.05), run_time=1.2)
        self.wait(0.8)
        cols = [BLUE, GREEN, GOLD]
        links = VGroup()
        for r in range(3):
            cl = CLS[r]
            for x, y_ in zip(cl, cl[1:] + cl[:1]):
                links.add(Line(nums[x].get_center(), nums[y_].get_center(), color=cols[r], stroke_width=2, stroke_opacity=0.6))
        links.set_z_index(-1)
        n1 = para("Nối các số có cùng số dư khi chia cho 3", 24, DIM, y=-0.6)
        self.play(Create(links), FadeIn(n1), *[nums[a][0].animate.set_color(cols[a % 3]) for a in A12], run_time=1.5)
        self.wait(2.0)
        boxes = VGroup()
        targets = []
        for r in range(3):
            bx = RoundedRectangle(width=2.5, height=3.2, corner_radius=0.2, color=cols[r], stroke_width=3).move_to([-2.75 + 2.75 * r, 2.6, 0])
            boxes.add(bx)
            for j, a in enumerate(CLS[r]):
                targets.append(nums[a].animate.move_to(bx.get_center() + np.array([-0.5 + (j % 2) * 1.0, 0.65 - (j // 2) * 1.2, 0])))
        self.play(FadeOut(links), FadeOut(n1), run_time=0.4)
        self.play(*targets, Create(boxes), run_time=1.6)
        labs = VGroup(*[Text(f"[{r}]", font=FONT, font_size=30, color=cols[r]).next_to(boxes[r], DOWN, buff=0.2) for r in range(3)])
        self.play(FadeIn(labs), run_time=0.5)
        self.wait(1.5)
        p1 = para("3 lớp tương đương: rời nhau, hợp lại đúng bằng cả tập", 26, WHITE, y=-0.6)
        p2 = para("→ một phân hoạch. Tập thương A/~ = {[0], [1], [2]}", 26, GOLD, y=-1.4)
        self.play(FadeIn(p1), run_time=0.6)
        self.wait(1.5)
        self.play(FadeIn(p2), run_time=0.6)
        self.wait(2.0)
        th = para("Định lý: quan hệ tương đương ⇔ phân hoạch", 30, GOLD, y=-2.7)
        box = SurroundingRectangle(th, color=GOLD, buff=0.2, corner_radius=0.12)
        self.play(FadeIn(th), Create(box), run_time=0.7)
        self.wait(1.5)
        ap = para("Trong CNTT: bucket của hash table, Union-Find,\nthành phần liên thông của đồ thị", 24, DIM, y=-4.0)
        self.play(FadeIn(ap), run_time=0.6)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 4. Thứ tự bộ phận =====
        c = swap_cap(self, c, cap("Thứ tự bộ phận: đổi một tính chất", 38, GOLD))
        lines = VGroup(*[Text(s, font=FONT, font_size=30, color=col) for s, col in [
            ("Phản xạ:  a ≼ a", BLUE),
            ("Phản đối xứng:  a ≼ b và b ≼ a  ⇒  a = b", RED),
            ("Bắc cầu:  a ≼ b, b ≼ c  ⇒  a ≼ c", GOLD),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        fitw(lines, 7.8).move_to([0, 4.2, 0])
        for m in lines:
            self.play(FadeIn(m, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(1.4)
        e = para("Đối xứng thay bằng phản đối xứng:\nhai phần tử khác nhau không thể \"đi vòng\" về nhau", 26, WHITE, y=1.7)
        self.play(FadeIn(e), run_time=0.6)
        self.wait(2.5)
        ex = VGroup(*[Text(s, font=FONT, font_size=26, color=DIM) for s in [
            "≤ trên số thực (toàn phần: mọi cặp so sánh được)",
            "⊆ trên các tập con",
            "a | b (a chia hết b) trên số nguyên dương",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        fitw(ex, 7.8).move_to([0, -0.4, 0])
        self.play(LaggedStart(*[FadeIn(m) for m in ex], lag_ratio=0.4), run_time=1.6)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 5. Từ quan hệ chia hết đến sơ đồ Hasse =====
        c = swap_cap(self, c, cap("Ước của 12 với quan hệ chia hết", 38, GOLD))
        nodes = {d: node(d, P12[d]) for d in D12}
        self.play(*[GrowFromCenter(m) for m in nodes.values()], run_time=0.8)
        loops = VGroup(*[loop(P12[a]) for a, _ in LOOPS])
        cov = {p: arrow(P12[p[0]], P12[p[1]]) for p in COVER}
        tr = {p: arrow(P12[p[0]], P12[p[1]], angle=-0.55 if P12[p[1]][0] <= P12[p[0]][0] else 0.55, col=RED) for p in TRANS}
        for m in tr.values():
            m.set_color(DIM)
        allg = VGroup(loops, *cov.values(), *tr.values())
        self.play(Create(allg), run_time=1.8)
        s1 = para("Đủ 18 cặp (a, b) với a | b: mũi tên từ a đến b", 26, WHITE, y=-1.4)
        self.play(FadeIn(s1), run_time=0.5)
        self.wait(2.5)
        s2 = para("Bước 1: bỏ 6 vòng (phản xạ, luôn có)", 26, BLUE, y=-2.2)
        self.play(FadeIn(s2), loops.animate.set_color(BLUE), run_time=0.5)
        self.wait(1.0)
        self.play(FadeOut(loops), run_time=0.6)
        self.wait(1.0)
        s3 = para("Bước 2: bỏ 5 cạnh suy ra được nhờ bắc cầu\n(ví dụ 1 → 4 vì đã có 1 → 2 → 4)", 26, RED, y=-3.3)
        self.play(FadeIn(s3), *[m.animate.set_color(RED) for m in tr.values()], run_time=0.6)
        self.wait(2.0)
        self.play(*[FadeOut(m) for m in tr.values()], run_time=0.7)
        self.wait(1.0)
        s4 = para("Bước 3: vẽ phần tử lớn hơn ở trên, bỏ đầu mũi tên", 26, GOLD, y=-4.5)
        lines = {p: arrow(P12[p[0]], P12[p[1]], tip=False, col=WHITE) for p in COVER}
        self.play(FadeIn(s4), *[ReplacementTransform(cov[p], lines[p]) for p in COVER], run_time=0.9)
        self.wait(1.5)
        s5 = para("Sơ đồ Hasse: chỉ còn 7 cạnh phủ", 30, GOLD, y=-5.5)
        self.play(FadeIn(s5), run_time=0.5)
        self.wait(3.0)
        self.play(*[FadeOut(m) for m in (s1, s2, s3, s4, s5)], run_time=0.5)

        # ===== 6. Đọc sơ đồ Hasse =====
        c = swap_cap(self, c, cap("Đọc sơ đồ Hasse", 42, GOLD))
        r1 = para("a | b  ⇔  đi được từ a lên b theo các cạnh", 26, WHITE, y=-1.4)
        self.play(FadeIn(r1), run_time=0.5)
        self.wait(1.5)
        self.play(nodes[4][0].animate.set_fill(RED, 0.5), nodes[6][0].animate.set_fill(RED, 0.5), run_time=0.5)
        r2 = para("4 và 6: không ai chia hết ai, không so sánh được\n→ thứ tự bộ phận, không phải toàn phần", 26, RED, y=-2.5)
        self.play(FadeIn(r2), run_time=0.6)
        self.wait(2.5)
        self.play(nodes[4][0].animate.set_fill(CELL, 1), nodes[6][0].animate.set_fill(CELL, 1),
                  nodes[1][0].animate.set_fill(GREEN, 0.5), nodes[12][0].animate.set_fill(GOLD, 0.5), run_time=0.5)
        r3 = para("1 là phần tử nhỏ nhất, 12 là lớn nhất", 26, WHITE, y=-3.7)
        self.play(FadeIn(r3), run_time=0.5)
        self.wait(2.0)
        self.play(nodes[1].animate.set_opacity(0.15), nodes[12].animate.set_opacity(0.15),
                  *[lines[p].animate.set_opacity(0.15) for p in COVER if 1 in p or 12 in p], run_time=0.6)
        for d in (2, 3):
            nodes[d][0].set_fill(GREEN, 0.5)
        for d in (4, 6):
            nodes[d][0].set_fill(GOLD, 0.5)
        r4 = para("Chỉ xét {2, 3, 4, 6}: tối tiểu 2, 3 và tối đại 4, 6,\nnhưng không có nhỏ nhất hay lớn nhất", 24, GOLD, y=-4.9)
        self.play(FadeIn(r4), run_time=0.6)
        self.wait(4.0)
        wipe(self, keep=[c])

        # ===== 7. Ước của 30 = khối lập phương = P({a,b,c}) =====
        c = swap_cap(self, c, cap("Ước của 30: một khối lập phương", 38, GOLD))
        n30 = {d: node(d, P30[d], BLUE, 28) for d in D30}
        e30 = VGroup(*[arrow(P30[a], P30[b], tip=False, col=WHITE) for a, b in C30])
        self.play(Create(e30), *[GrowFromCenter(m) for m in n30.values()], run_time=1.4)
        f = para("30 = 2 · 3 · 5: mỗi ước chọn có hoặc không từng thừa số", 24, WHITE, y=-1.4)
        self.play(FadeIn(f), run_time=0.5)
        self.wait(2.0)
        m = para("Đổi 2 → a, 3 → b, 5 → c:", 26, DIM, y=-2.2)
        self.play(FadeIn(m), run_time=0.4)
        new = {}
        for d in D30:
            t = Text(SET[d], font=FONT, font_size=20 if len(SET[d]) > 3 else 24, color=GOLD).move_to(n30[d][1])
            new[d] = t
        self.play(*[Transform(n30[d][1], new[d]) for d in D30], run_time=1.2)
        self.wait(1.5)
        r = para("(ước của 30, |)  có cùng sơ đồ Hasse với  (P({a,b,c}), ⊆)", 24, GOLD, y=-3.2)
        self.play(FadeIn(r), run_time=0.6)
        self.wait(1.5)
        r2 = para("Hai poset đẳng cấu: chia hết ↔ bao hàm", 28, WHITE, y=-4.1)
        self.play(FadeIn(r2), run_time=0.5)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 8. Tóm tắt =====
        c = swap_cap(self, c, cap("So sánh", 44, GOLD))
        hdr = VGroup(Text("Tương đương", font=FONT, font_size=30, color=BLUE).move_to([-2.2, 4.6, 0]),
                     Text("Thứ tự bộ phận", font=FONT, font_size=30, color=GOLD).move_to([2.2, 4.6, 0]))
        rows = [("phản xạ", "phản xạ"), ("đối xứng", "phản đối xứng"), ("bắc cầu", "bắc cầu"),
                ("→ các lớp, phân hoạch", "→ sơ đồ Hasse"), ("ví dụ: mod n", "ví dụ: |, ⊆, ≤")]
        tb = VGroup()
        for i, (a, b) in enumerate(rows):
            col_a = RED if i == 1 else WHITE
            tb.add(Text(a, font=FONT, font_size=24, color=col_a).move_to([-2.2, 3.7 - i * 0.75, 0]))
            tb.add(Text(b, font=FONT, font_size=24, color=col_a).move_to([2.2, 3.7 - i * 0.75, 0]))
        div = Line([0, 5.0, 0], [0, 0.0, 0], color=DIM, stroke_width=2)
        self.play(FadeIn(hdr), Create(div), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(m) for m in tb], lag_ratio=0.1), run_time=2.0)
        self.wait(2.5)
        e = para("Chỉ khác nhau ở một tính chất,\nnhưng một bên gom nhóm, một bên xếp thứ bậc.", 26, GOLD, y=-1.2)
        self.play(FadeIn(e), run_time=0.6)
        self.wait(5.0)
