from common import *
from itertools import combinations, product

# ---------- Quine–McCluskey cho F(a,b,c,d) = Σm(0,2,3,5,7,8,10,11,13,15) (ví dụ bốn biến trong bài 13-05) ----------
MINT = [0, 2, 3, 5, 7, 8, 10, 11, 13, 15]
NV = 4
VARS = "abcd"


def bits(m):
    return format(m, "04b")


def combine(x, y):
    diff = [i for i in range(NV) if x[i] != y[i]]
    if len(diff) == 1 and all((x[i] == "-") == (y[i] == "-") for i in range(NV)):
        i = diff[0]
        if "-" in (x[i], y[i]):
            return None
        return x[:i] + "-" + x[i + 1:]
    return None


def covers(code, m):
    b = bits(m)
    return all(c == "-" or c == bb for c, bb in zip(code, b))


GROUPS = {}
for m in MINT:
    GROUPS.setdefault(bits(m).count("1"), []).append(m)
assert GROUPS == {0: [0], 1: [2, 8], 2: [3, 5, 10], 3: [7, 11, 13], 4: [15]}

# Vòng 1: các cặp giữa nhóm k và k+1
COL1 = [(m,) for k in sorted(GROUPS) for m in GROUPS[k]]
PAIRS = []
for k in sorted(GROUPS):
    for a in GROUPS.get(k, []):
        for b in GROUPS.get(k + 1, []):
            r = combine(bits(a), bits(b))
            if r:
                PAIRS.append(((a, b), r))
assert len(PAIRS) == 13
assert [p[1] for p in PAIRS] == ["00-0", "-000", "001-", "-010", "10-0", "0-11", "-011", "01-1", "-101", "101-", "-111", "1-11", "11-1"]
used1 = {m for (a, b), _ in PAIRS for m in (a, b)}
assert used1 == set(MINT)          # mọi minterm đều được đánh dấu

# Vòng 2
QUADS = {}
used2 = set()
for (p1, c1), (p2, c2) in combinations(PAIRS, 2):
    r = combine(c1, c2)
    if r:
        used2 |= {c1, c2}
        QUADS.setdefault(r, []).append((p1, p2))
assert set(QUADS) == {"-0-0", "-01-", "--11", "-1-1"}
assert used2 == {c for _, c in PAIRS}   # mọi cặp đều dán tiếp được
# vòng 3: không dán được nữa
assert not any(combine(x, y) for x, y in combinations(QUADS, 2))
PI = ["-0-0", "-01-", "--11", "-1-1"]
PI_M = {c: [m for m in MINT if covers(c, m)] for c in PI}
assert PI_M == {"-0-0": [0, 2, 8, 10], "-01-": [2, 3, 10, 11], "--11": [3, 7, 11, 15], "-1-1": [5, 7, 13, 15]}
# nguyên tố cốt yếu
ESS = {}
for m in MINT:
    who = [c for c in PI if covers(c, m)]
    if len(who) == 1:
        ESS.setdefault(who[0], []).append(m)
assert ESS == {"-0-0": [0, 8], "-1-1": [5, 13]}
REST = [m for m in MINT if not any(covers(c, m) for c in ESS)]
assert REST == [3, 11]
assert [c for c in PI if all(covers(c, m) for m in REST) and c not in ESS] == ["-01-", "--11"]


def term_lits(code):
    return [(VARS[i], ch == "0") for i, ch in enumerate(code) if ch != "-"]


def F(a, b, c, d):
    return (8 * a + 4 * b + 2 * c + d) in MINT


for a, b, c, d in product([0, 1], repeat=4):
    res = ((not b) and (not d)) or (b and d) or (c and d)
    res2 = ((not b) and (not d)) or (b and d) or ((not b) and c)
    assert bool(res) == F(a, b, c, d) == bool(res2)
# không có phủ 2 hạng
assert not any(all(any(covers(x, m) for x in pair) for m in MINT) for pair in combinations(PI, 2))


# ---------- Hình ----------
def bexpr(s, size=32, color=WHITE):
    """'~' đứng trước một chữ = phủ định, vẽ gạch ngang trên chữ đó."""
    plain, neg_idx, gi = "", [], 0
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == "~":
            neg_idx.append(gi)
            i += 1
            continue
        plain += ch
        if not ch.isspace():
            gi += 1
        i += 1
    t = Text(plain, font=FONT, font_size=size, color=color)
    g = VGroup(t)
    if neg_idx:
        top = max(t[j].get_top()[1] for j in neg_idx) + 0.05 * size / 32
        for j in neg_idx:
            ch = t[j]
            inset = 0.14 * ch.width + 0.02 * size / 32
            g.add(Line([ch.get_left()[0] + inset, top, 0], [ch.get_right()[0] - inset, top, 0], color=color, stroke_width=2.6 * size / 32))
    return g


def code_term(code):
    return "".join(("~" if neg else "") + v for v, neg in term_lits(code))


def code_text(code, size=30, color=WHITE, hl=None):
    t = Text(code, font=FONT, font_size=size, color=color)
    if hl is not None:
        t[hl].set_color(RED)
    return t


class Qm(Scene):
    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Rút gọn hàm Boole", 44)
        t1 = Text("Quine–McCluskey", font=FONT, font_size=70, color=GOLD).move_to([0, 1.4, 0])
        t2 = para("Phương pháp bảng: làm được với nhiều biến,\nkhông cần vẽ bản đồ Karnaugh", 32, y=-0.6)
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. Đề bài và ý tưởng =====
        c = swap_cap(self, c, cap("Đề bài", 44, GOLD))
        f = para("F(a, b, c, d) = Σm(0, 2, 3, 5, 7, 8, 10, 11, 13, 15)", 30, WHITE, y=4.6)
        self.play(FadeIn(f), run_time=0.7)
        f2 = para("10 minterm, mỗi minterm là một tích 4 literal", 28, DIM, y=3.8)
        self.play(FadeIn(f2), run_time=0.6)
        self.wait(2.5)
        k = para("Một phép biến đổi duy nhất:", 30, GOLD, y=2.4)
        law = bexpr("xy + x~y = x", 44, WHITE).move_to([0, 1.4, 0])
        self.play(FadeIn(k), FadeIn(law), run_time=0.7)
        self.wait(2.0)
        e1 = bexpr("~a~b~c~d + ~a~bc~d = ~a~b~d", 38).move_to([0, -0.1, 0])
        e2 = Text("0000  +  0010  →  00-0", font=FONT, font_size=38).move_to([0, -1.2, 0])
        e2[6].set_color(RED); e2[11].set_color(RED); e2[-2].set_color(RED)
        self.play(FadeIn(e1), run_time=0.7)
        self.wait(1.5)
        self.play(FadeIn(e2), run_time=0.7)
        self.wait(1.5)
        e3 = para("Hai mã khác đúng một bit thì dán được,\nbit khác nhau thay bằng dấu “-” (biến bị bỏ)", 28, WHITE, y=-2.8)
        self.play(FadeIn(e3), run_time=0.6)
        self.wait(4.0)
        self.play(*[FadeOut(m) for m in [f2, k, law, e1, e2, e3]], f.animate.move_to([0, 5.2, 0]).scale(0.9), run_time=0.6)

        # ===== 3. Bước 1: nhóm theo số bit 1 =====
        c = swap_cap(self, c, cap("Bước 1: nhóm theo số bit 1", 40, GOLD))
        x1 = -2.2
        rows1 = {}
        col1 = VGroup()
        y = 4.2
        seps = VGroup()
        glab = VGroup()
        for k_ in sorted(GROUPS):
            if k_ > 0:
                seps.add(Line([x1 - 1.6, y + 0.24, 0], [x1 + 1.6, y + 0.24, 0], color=DIM, stroke_width=1.5))
            gl = Text(f"{k_}", font=FONT, font_size=24, color=BLUE).move_to([x1 - 1.85, y - 0.24 * (len(GROUPS[k_]) - 1), 0])
            glab.add(gl)
            for m in GROUPS[k_]:
                r = VGroup(Text(f"{m}", font=FONT, font_size=30, color=DIM).move_to([x1 - 0.9, y, 0]),
                           Text(bits(m), font=FONT, font_size=30).move_to([x1 + 0.5, y, 0]))
                rows1[m] = r
                col1.add(r)
                y -= 0.48
            y -= 0.12
        h1 = Text("số 1   m    mã abcd", font=FONT, font_size=22, color=BLUE).move_to([x1 - 0.6, 4.75, 0])
        self.play(FadeIn(h1), run_time=0.4)
        for k_ in sorted(GROUPS):
            items = [rows1[m] for m in GROUPS[k_]]
            self.play(*[FadeIn(r, shift=RIGHT * 0.2) for r in items], FadeIn(glab[k_]), run_time=0.6)
            self.wait(0.6)
        self.play(Create(seps), run_time=0.5)
        n1 = para("Chỉ hai nhóm kề nhau mới có thể\ncó mã khác đúng một bit", 28, WHITE, y=-1.5)
        self.play(FadeIn(n1), run_time=0.6)
        self.wait(3.5)
        self.play(FadeOut(n1), run_time=0.4)

        # ===== 4. Bước 2: dán lần 1 =====
        c = swap_cap(self, c, cap("Bước 2: dán các cặp", 42, GOLD))
        x2 = 1.9
        h2 = Text("cặp        mã", font=FONT, font_size=22, color=BLUE).move_to([x2, 4.75, 0])
        self.play(FadeIn(h2), run_time=0.4)
        rows2 = []
        checks1 = {}
        y = 4.2
        prev_g = None
        for idx, ((a, b), code) in enumerate(PAIRS):
            ga = bits(a).count("1")
            if prev_g is not None and ga != prev_g:
                y -= 0.12
            prev_g = ga
            diff = [i for i in range(NV) if bits(a)[i] != bits(b)[i]][0]
            r = VGroup(Text(f"{a},{b}", font=FONT, font_size=26, color=DIM).move_to([x2 - 0.75, y, 0]),
                       code_text(code, 28, WHITE, hl=diff).move_to([x2 + 0.85, y, 0]))
            rows2.append(r)
            y -= 0.42
            slow = idx < 3
            ba = SurroundingRectangle(rows1[a], color=GOLD, buff=0.05, stroke_width=3)
            bb = SurroundingRectangle(rows1[b], color=GOLD, buff=0.05, stroke_width=3)
            hl = [rows1[a][1][diff].animate.set_color(RED), rows1[b][1][diff].animate.set_color(RED)]
            self.play(Create(ba), Create(bb), *hl, run_time=0.5 if slow else 0.3)
            if slow:
                expl = para(f"{bits(a)} và {bits(b)} khác đúng một bit → {code}", 28, WHITE, y=-2.6)
                self.play(FadeIn(expl), run_time=0.4)
            self.play(TransformFromCopy(VGroup(rows1[a], rows1[b]), r), run_time=0.7 if slow else 0.45)
            new_checks = []
            for m in (a, b):
                if m not in checks1:
                    ck = Text("✓", font=FONT, font_size=26, color=GREEN).next_to(rows1[m], RIGHT, buff=0.2)
                    checks1[m] = ck
                    new_checks.append(FadeIn(ck))
            self.play(*new_checks, rows1[a][1][diff].animate.set_color(WHITE), rows1[b][1][diff].animate.set_color(WHITE),
                      FadeOut(ba), FadeOut(bb), run_time=0.35)
            if not slow:
                self.wait(0.4)
            if slow:
                self.wait(1.5)
                self.play(FadeOut(expl), run_time=0.3)
            if idx == 2:
                note = para("Mã nào đã tham gia dán thì đánh dấu ✓", 28, GREEN, y=-2.6)
                self.play(FadeIn(note), run_time=0.5)
                self.wait(2.0)
                self.play(FadeOut(note), run_time=0.3)
        allm = para("13 cặp. Cả 10 minterm đều có ✓:\nkhông minterm nào đứng riêng một mình", 28, WHITE, y=-2.8)
        self.play(FadeIn(allm), run_time=0.6)
        self.wait(3.5)
        no = para("Ví dụ 2 = 0010 và 5 = 0101 khác ba bit: không dán", 26, DIM, y=-4.3)
        self.play(FadeIn(no), run_time=0.5)
        self.wait(3.0)
        self.play(FadeOut(allm), FadeOut(no), run_time=0.4)

        # ===== 5. Bước 3: dán lần 2 =====
        c = swap_cap(self, c, cap("Bước 3: dán tiếp", 42, GOLD))
        g1 = VGroup(col1, seps, glab, h1, *checks1.values())
        g2 = VGroup(*rows2, h2)
        self.play(FadeOut(g1), g2.animate.shift(LEFT * 4.1), run_time=0.8)
        rule = para("Dán tiếp khi dấu “-” cùng vị trí\nvà phần còn lại khác đúng một bit", 28, WHITE, y=-2.6)
        self.play(FadeIn(rule), run_time=0.6)
        self.wait(2.5)
        x3 = 2.0
        h3 = Text("nhóm 4 ô       mã", font=FONT, font_size=22, color=BLUE).move_to([x3, 4.75, 0])
        self.play(FadeIn(h3), run_time=0.4)
        code_row = {code: rows2[i] for i, (_, code) in enumerate(PAIRS)}
        checks2 = {}
        rows3 = {}
        y = 4.2
        for qi, code in enumerate(PI):
            p1, p2 = QUADS[code][0]
            c1 = dict(PAIRS)[p1]
            c2 = dict(PAIRS)[p2]
            ms = PI_M[code]
            r = VGroup(Text(",".join(map(str, ms)), font=FONT, font_size=26, color=DIM).move_to([x3 - 0.8, y, 0]),
                       Text(code, font=FONT, font_size=28).move_to([x3 + 1.15, y, 0]))
            rows3[code] = r
            y -= 0.62
            others = [dict(PAIRS)[q1] for q1, q2 in QUADS[code][1:]] + [dict(PAIRS)[q2] for q1, q2 in QUADS[code][1:]]
            ba = SurroundingRectangle(code_row[c1], color=GOLD, buff=0.05, stroke_width=3)
            bb = SurroundingRectangle(code_row[c2], color=GOLD, buff=0.05, stroke_width=3)
            self.play(Create(ba), Create(bb), run_time=0.4)
            if qi == 0:
                expl = para(f"{c1} và {c2}  →  {code}", 30, GOLD, y=-4.2)
                self.play(FadeIn(expl), run_time=0.4)
            self.play(TransformFromCopy(VGroup(code_row[c1], code_row[c2]), r), run_time=0.6)
            anims = []
            for cc in [c1, c2] + others:
                if cc not in checks2:
                    ck = Text("✓", font=FONT, font_size=24, color=GREEN).next_to(code_row[cc], RIGHT, buff=0.15)
                    checks2[cc] = ck
                    anims.append(FadeIn(ck))
            self.play(*anims, FadeOut(ba), FadeOut(bb), run_time=0.4)
            if qi == 0:
                self.wait(1.2)
                dup = para("(0,8) với (2,10) cũng ra -0-0: chỉ ghi một lần", 26, DIM, y=-4.2)
                self.play(ReplacementTransform(expl, dup), run_time=0.5)
                self.wait(2.5)
                self.play(FadeOut(dup), run_time=0.3)
            else:
                self.wait(1.0)
        bad = para("00-0 và 001-: dấu “-” lệch vị trí → không dán", 26, DIM, y=-4.2)
        self.play(FadeIn(bad), run_time=0.5)
        self.wait(2.5)
        stop = para("Bốn mã 4 ô không dán thêm được nữa: dừng", 28, WHITE, y=-4.2)
        self.play(ReplacementTransform(bad, stop), run_time=0.5)
        self.wait(2.5)
        self.play(FadeOut(stop), FadeOut(rule), run_time=0.4)

        # ===== 6. Nguyên nhân nguyên tố =====
        c = swap_cap(self, c, cap("Nguyên nhân nguyên tố", 42, GOLD))
        self.play(FadeOut(VGroup(*rows2, h2, *checks2.values())), FadeOut(h3), VGroup(*rows3.values()).animate.move_to([-1.2, 3.4, 0]), run_time=0.7)
        e = para("Các mã không có ✓ là nguyên nhân nguyên tố.\nĐọc mã: 1 → biến, 0 → biến có gạch, - → bỏ", 26, WHITE, y=0.4)
        self.play(FadeIn(e), run_time=0.6)
        self.wait(2.0)
        names = {}
        for i, code in enumerate(PI):
            r = rows3[code]
            nm = bexpr(f"N{i+1} = " + code_term(code), 32, GOLD).next_to(r, RIGHT, buff=0.6)
            names[code] = nm
            self.play(FadeIn(nm, shift=LEFT * 0.2), run_time=0.5)
            self.wait(1.0)
        ex = bexpr("-0-0:  a bỏ, b = 0, c bỏ, d = 0  →  ~b~d", 28, DIM).move_to([0, -1.2, 0])
        self.play(FadeIn(ex), run_time=0.6)
        self.wait(3.0)
        self.play(FadeOut(e), FadeOut(ex), run_time=0.4)
        q = para("Có cần dùng cả 4 không?", 32, WHITE, y=0.0)
        self.play(FadeIn(q), run_time=0.5)
        self.wait(2.0)
        self.play(FadeOut(q), FadeOut(f), *[FadeOut(r) for r in rows3.values()], *[FadeOut(n) for n in names.values()], run_time=0.5)

        # ===== 7. Bảng phủ =====
        c = swap_cap(self, c, cap("Bảng phủ", 44, GOLD))
        lx = -3.25
        xs = [-2.15 + j * 0.68 for j in range(len(MINT))]
        y0 = 4.4
        dy = 0.75
        head = [Text(str(m), font=FONT, font_size=26, color=BLUE).move_to([x, y0, 0]) for x, m in zip(xs, MINT)]
        rlab = [bexpr(code_term(code), 30, GOLD).move_to([lx, y0 - (i + 1) * dy, 0]) for i, code in enumerate(PI)]
        grid = VGroup(Line([lx - 0.6, y0 - 0.38, 0], [xs[-1] + 0.4, y0 - 0.38, 0], color=DIM, stroke_width=2),
                      Line([lx + 0.65, y0 + 0.35, 0], [lx + 0.65, y0 - 4.5 * dy, 0], color=DIM, stroke_width=2))
        self.play(*[FadeIn(h) for h in head], *[FadeIn(r) for r in rlab], Create(grid), run_time=0.8)
        marks = {}
        for i, code in enumerate(PI):
            ms = []
            for j, m in enumerate(MINT):
                if covers(code, m):
                    t = Text("×", font=FONT, font_size=34, color=WHITE).move_to([xs[j], y0 - (i + 1) * dy, 0])
                    marks[(code, m)] = t
                    ms.append(t)
            self.play(LaggedStart(*[FadeIn(t, scale=1.4) for t in ms], lag_ratio=0.15), run_time=0.7)
        ex = para("Hàng: nguyên nhân nguyên tố.  Cột: minterm phải phủ.\n× : hàng đó phủ cột đó", 26, WHITE, y=0.3)
        self.play(FadeIn(ex), run_time=0.6)
        self.wait(3.0)
        self.play(FadeOut(ex), run_time=0.3)

        # ===== 8. Nguyên tố cốt yếu =====
        c = swap_cap(self, c, cap("Nguyên tố cốt yếu", 44, GOLD))
        s1 = para("Tìm cột chỉ có đúng một dấu ×", 30, WHITE, y=0.3)
        self.play(FadeIn(s1), run_time=0.5)
        self.wait(1.0)
        col_boxes = []
        for code, ms in ESS.items():
            for m in ms:
                j = MINT.index(m)
                bx = Rectangle(width=0.6, height=4 * dy + 0.7, color=RED, stroke_width=3).move_to([xs[j], y0 - 2.1 * dy, 0])
                col_boxes.append(bx)
                self.play(Create(bx), marks[(code, m)].animate.set_color(RED), run_time=0.5)
                self.wait(0.6)
        s2 = bexpr("Cột 0, 8 chỉ có ~b~d.  Cột 5, 13 chỉ có bd.", 28, WHITE).move_to([0, -0.5, 0])
        self.play(FadeIn(s2), run_time=0.6)
        self.wait(2.0)
        s3 = para("Bắt buộc phải chọn hai hạng này", 30, GREEN, y=-1.4)
        hl_rows = []
        for code in ESS:
            i = PI.index(code)
            hl_rows.append(SurroundingRectangle(VGroup(rlab[i], *[marks[(code, m)] for m in PI_M[code]]), color=GREEN, buff=0.12, stroke_width=4))
        self.play(FadeIn(s3), *[Create(h) for h in hl_rows], run_time=0.7)
        self.wait(2.5)
        covered = sorted({m for code in ESS for m in PI_M[code]})
        s4 = para("Hai hạng này đã phủ 0, 2, 5, 7, 8, 10, 13, 15", 28, WHITE, y=-2.4)
        dim_cols = []
        for m in covered:
            j = MINT.index(m)
            dim_cols.append(head[j].animate.set_opacity(0.25))
            for code in PI:
                if (code, m) in marks:
                    dim_cols.append(marks[(code, m)].animate.set_opacity(0.25))
        self.play(FadeIn(s4), *dim_cols, *[FadeOut(b) for b in col_boxes], run_time=0.8)
        self.wait(2.0)
        s5 = para("Còn lại cột 3 và 11", 30, GOLD, y=-3.3)
        self.play(FadeIn(s5), *[Indicate(head[MINT.index(m)], color=GOLD) for m in REST], run_time=0.9)
        self.wait(2.0)
        s6 = VGroup(bexpr("~bc", 28, WHITE), Text(" và cd đều phủ cả 3 lẫn 11, cùng 2 literal", font=FONT, font_size=28)).arrange(RIGHT, buff=0.1)
        if s6.width > 7.8:
            s6.scale_to_fit_width(7.8)
        s6.move_to([0, -4.3, 0])
        self.play(FadeIn(s6), run_time=0.6)
        self.wait(3.0)
        i3 = PI.index("--11")
        pick = SurroundingRectangle(VGroup(rlab[i3], *[marks[("--11", m)] for m in PI_M["--11"]]), color=BLUE, buff=0.12, stroke_width=4)
        s7 = VGroup(Text("Chọn cd (chọn", font=FONT, font_size=26, color=BLUE), bexpr("~bc", 26, BLUE),
                    Text("cũng được, cùng chi phí)", font=FONT, font_size=26, color=BLUE)).arrange(RIGHT, buff=0.12).move_to([0, -5.2, 0])
        self.play(Create(pick), FadeIn(s7), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 9. Kết quả =====
        c = swap_cap(self, c, cap("Kết quả", 44, GOLD))
        before = para("10 minterm, mỗi cái 4 literal", 28, DIM, y=4.3)
        res = bexpr("F = ~b~d + bd + cd", 56, GREEN).move_to([0, 2.8, 0])
        self.play(FadeIn(before), run_time=0.5)
        self.play(Write(res), run_time=1.2)
        self.wait(1.5)
        alt = bexpr("hoặc  F = ~b~d + bd + ~bc", 32, WHITE).move_to([0, 1.5, 0])
        self.play(FadeIn(alt), run_time=0.6)
        self.wait(2.0)
        cnt = para("3 hạng, 6 literal. Không thể chỉ dùng 2 hạng:\nhai hạng cốt yếu chưa phủ 3 và 11.", 28, WHITE, y=-0.2)
        self.play(FadeIn(cnt), run_time=0.6)
        self.wait(3.0)
        chk = para("Kiểm tra lại trên đủ 16 hàng của bảng chân trị: khớp", 26, GREEN, y=-1.7)
        self.play(FadeIn(chk), run_time=0.6)
        self.wait(2.5)
        km = VGroup(bexpr("Trên K-map: ~b~d là 4 góc, bd là khối 2×2 ở giữa,", 26, DIM),
                    Text("cd là cột cd = 11. Cùng kết quả, cách tìm khác.", font=FONT, font_size=26, color=DIM)).arrange(DOWN, buff=0.2)
        if km.width > 7.8:
            km.scale_to_fit_width(7.8)
        km.move_to([0, -3.3, 0])
        self.play(FadeIn(km), run_time=0.6)
        self.wait(4.0)
        wipe(self, keep=[c])

        # ===== 9b. Don't-care =====
        c = swap_cap(self, c, cap("Nếu có don't-care?", 42, GOLD))
        d1 = para("Don't-care: tổ hợp đầu vào không bao giờ xảy ra,\nđầu ra là gì cũng được (ký hiệu d hoặc X)", 28, WHITE, y=4.0)
        d2 = para("Phần 1: coi như minterm, đưa vào để dán", 28, BLUE, y=2.2)
        d3 = para("→ có thể ra nguyên nhân nguyên tố rộng hơn", 26, DIM, y=1.5)
        d4 = para("Phần 2: KHÔNG mở cột cho don't-care", 28, GREEN, y=0.2)
        d5 = para("→ không bắt buộc phải phủ chúng", 26, DIM, y=-0.5)
        for m in [d1, d2, d3, d4, d5]:
            self.play(FadeIn(m), run_time=0.6)
            self.wait(1.8)
        self.wait(2.5)
        wipe(self, keep=[c])

        # ===== 10. Tổng kết =====
        c = swap_cap(self, c, cap("Quine–McCluskey gồm hai phần", 38, GOLD))
        sm = VGroup(*[Text(s, font=FONT, font_size=30, color=col) for s, col in [
            ("Phần 1: tìm mọi nguyên nhân nguyên tố", BLUE),
            ("1. Viết mã nhị phân, nhóm theo số bit 1", WHITE),
            ("2. Dán hai nhóm kề, đánh dấu ✓", WHITE),
            ("3. Lặp đến khi không dán được; mã không ✓ là kết quả", WHITE),
            ("Phần 2: chọn phủ ít hạng nhất", GREEN),
            ("4. Lập bảng phủ, lấy nguyên tố cốt yếu", WHITE),
            ("5. Phủ nốt các cột còn lại", WHITE),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        sm[4].shift(DOWN * 0.25)
        for m in sm[5:]:
            m.shift(DOWN * 0.25)
        if sm.width > 7.6:
            sm.scale_to_fit_width(7.6)
        sm.move_to([0, 2.4, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.2) for m in sm], lag_ratio=0.4), run_time=3.5)
        self.wait(3.5)
        end = para("Máy tính làm được với nhiều biến. Khi bảng phủ lớn,\nbước 5 là bài toán phủ tập (NP-khó), công cụ thực tế\ndùng heuristic như Espresso.", 26, DIM, y=-2.6)
        self.play(FadeIn(end), run_time=0.7)
        self.wait(5.0)
