from common import *
from itertools import product

GREEN = "#6bd68a"
VARS = "pqr"


# ---------- Toán: kiểm tra mọi công thức trong reel bằng bảng chân trị ----------
def imp(a, b):
    return (not a) or b


def f_ex(p, q, r):          # f = (p → q) ∧ (q → r)
    return imp(p, q) and imp(q, r)


def g_ex(p, q, r):          # g = (p ↔ q) → r
    return imp(p == q, r)


ROWS = list(product([True, False], repeat=3))          # TTT, TTF, ..., FFF
F_VAL = [f_ex(*r) for r in ROWS]
assert F_VAL == [True, False, False, False, True, False, True, True]
T_ROWS = [r for r in ROWS if f_ex(*r)]
F_ROWS = [r for r in ROWS if not f_ex(*r)]
assert len(T_ROWS) == 4 and len(F_ROWS) == 4


def lit(v, neg):
    return ("¬" if neg else "") + v


def dnf_term(row):          # biến T giữ nguyên, biến F thêm ¬
    return "(" + " ∧ ".join(lit(v, not b) for v, b in zip(VARS, row)) + ")"


def cnf_clause(row):        # biến T thêm ¬, biến F giữ nguyên
    return "(" + " ∨ ".join(lit(v, b) for v, b in zip(VARS, row)) + ")"


def ev_dnf(rows, p, q, r):
    return any(all(x == b for x, b in zip((p, q, r), row)) for row in rows)


def ev_cnf(rows, p, q, r):
    return all(any(x != b for x, b in zip((p, q, r), row)) for row in rows)


for row in ROWS:
    assert ev_dnf(T_ROWS, *row) == f_ex(*row)
    assert ev_cnf(F_ROWS, *row) == f_ex(*row)
# rút gọn nêu trong reel: f ≡ (¬p ∨ q) ∧ (¬q ∨ r)
for row in ROWS:
    p, q, r = row
    assert f_ex(*row) == ((not p or q) and (not q or r))
# g: các bước biến đổi
for p, q, r in ROWS:
    g = g_ex(p, q, r)
    s2 = (not ((not p or q) and (not q or p))) or r
    s3 = ((not (not p or q)) or (not (not q or p))) or r
    s4 = (p and not q) or (q and not p) or r
    s5 = (((p or not p) and (p or q) and (not p or not q) and (not q or q))) or r
    s6 = ((p or q) and (not p or not q)) or r
    s7 = (p or q or r) and (not p or not q or r)
    assert g == s2 == s3 == s4 == s5 == s6 == s7
G_ROWS_F = [r for r in ROWS if not g_ex(*r)]
assert G_ROWS_F == [(True, True, False), (False, False, False)]
G_DNF = lambda p, q, r: (p and not q) or (q and not p) or r
G_CNF = lambda p, q, r: (p or q or r) and (not p or not q or r)


# ---------- Hàm dựng hình ----------
SYM = {"∧": BLUE, "∨": GOLD, "¬": RED}


def T(s, size=32, color=WHITE, hl=None, sym=True, font=FONT):
    t2c = {}
    if sym:
        t2c.update(SYM)
    if hl:
        for h in ([hl] if isinstance(hl, str) else hl):
            t2c[h] = GREEN
    return Text(s, font=font, font_size=size, color=color, t2c=t2c)


def fit(m, w=8.0):
    if m.width > w:
        m.scale_to_fit_width(w)
    return m


def tbl_cell(x, y, s, color=WHITE, size=34):
    return Text(s, font=FONT, font_size=size, color=color).move_to([x, y, 0])


def tf(b):
    return "T" if b else "F"


class DnfCnf(Scene):
    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Dạng chuẩn tắc", 44)
        t1 = Text("DNF và CNF", font=FONT, font_size=84, color=GOLD).move_to([0, 1.2, 0])
        t2 = Text("Hai cách viết chuẩn\ncho mọi công thức logic", font=FONT, font_size=38, line_spacing=1.1).move_to([0, -0.7, 0])
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(1.8)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. Literal =====
        c = swap_cap(self, c, cap("Literal là gì?", 44, GOLD))
        d = Text("Literal: một biến, hoặc phủ định của một biến", font=FONT, font_size=30).move_to([0, 4.4, 0])
        d.scale_to_fit_width(7.8)
        self.play(FadeIn(d), run_time=0.7)
        good = [T(s, 54) for s in ("p", "¬q", "r", "¬r")]
        VGroup(*good).arrange(RIGHT, buff=0.9).move_to([0, 2.4, 0])
        ok = Text("Đều là literal", font=FONT, font_size=30, color=GREEN).move_to([0, 1.1, 0])
        self.play(LaggedStart(*[FadeIn(g, shift=UP * 0.2) for g in good], lag_ratio=0.3), run_time=1.6)
        self.play(FadeIn(ok), run_time=0.5)
        self.wait(1.5)
        bad = [T(s, 46) for s in ("p ∧ q", "¬(p ∨ q)", "p → q")]
        VGroup(*bad).arrange(DOWN, buff=0.55).move_to([-1.8, -2.0, 0])
        crosses = []
        for b in bad:
            crosses.append(Text("✗", font=FONT, font_size=44, color=RED).next_to(b, RIGHT, buff=0.6))
        why = Text("Không phải literal:\nđây là công thức ghép,\ncòn phủ định thì chỉ\nđứng ngay trước một biến", font=FONT, font_size=28, color=DIM, line_spacing=1.1).move_to([2.0, -2.0, 0])
        self.play(LaggedStart(*[FadeIn(b) for b in bad], lag_ratio=0.3), run_time=1.2)
        self.play(*[FadeIn(x) for x in crosses], FadeIn(why), run_time=0.8)
        self.wait(3.0)
        self.play(*[FadeOut(m) for m in good + bad + crosses + [d, ok, why]], run_time=0.5)

        # ===== 3. Hình dạng DNF / CNF =====
        c = swap_cap(self, c, cap("Hai dạng chuẩn", 44, GOLD))
        h1 = Text("DNF: tuyển của các hội", font=FONT, font_size=36, color=BLUE).move_to([0, 4.8, 0])
        self.play(FadeIn(h1), run_time=0.6)
        terms = ["p ∧ ¬q", "¬p ∧ r", "q"]
        tm = []
        for s in terms:
            tx = T(s, 38)
            bx = SurroundingRectangle(tx, color=BLUE, buff=0.22, corner_radius=0.15, stroke_width=4)
            tm.append(VGroup(bx, tx))
        ors = [Text("∨", font=FONT, font_size=44, color=GOLD) for _ in range(2)]
        row = VGroup(tm[0], ors[0], tm[1], ors[1], tm[2]).arrange(RIGHT, buff=0.3).move_to([0, 3.3, 0])
        fit(row, 8.2)
        self.play(LaggedStart(*[FadeIn(m) for m in row], lag_ratio=0.25), run_time=1.6)
        n1 = Text("Mỗi khung là một hội (AND) của các literal.\nCác khung nối với nhau bằng OR.", font=FONT, font_size=30, color=DIM, line_spacing=1.1).move_to([0, 1.6, 0])
        n1.scale_to_fit_width(min(n1.width, 7.8))
        self.play(FadeIn(n1), run_time=0.6)
        self.wait(3.0)

        h2 = Text("CNF: hội của các tuyển", font=FONT, font_size=36, color=GOLD).move_to([0, 0.0, 0])
        self.play(FadeIn(h2), run_time=0.6)
        cl = []
        for s in ["p ∨ ¬q", "¬p ∨ r", "q"]:
            tx = T(s, 38)
            bx = SurroundingRectangle(tx, color=GOLD, buff=0.22, corner_radius=0.15, stroke_width=4)
            cl.append(VGroup(bx, tx))
        ands = [Text("∧", font=FONT, font_size=44, color=BLUE) for _ in range(2)]
        row2 = VGroup(cl[0], ands[0], cl[1], ands[1], cl[2]).arrange(RIGHT, buff=0.3).move_to([0, -1.5, 0])
        fit(row2, 8.2)
        self.play(LaggedStart(*[FadeIn(m) for m in row2], lag_ratio=0.25), run_time=1.6)
        n2 = Text("Mỗi khung là một mệnh đề con (clause),\ntức là OR của các literal.\nCác khung nối với nhau bằng AND.", font=FONT, font_size=30, color=DIM, line_spacing=1.1).move_to([0, -3.5, 0])
        n2.scale_to_fit_width(min(n2.width, 7.8))
        self.play(FadeIn(n2), run_time=0.6)
        self.wait(3.5)
        k = Text("Hai dạng này đổi vai ∧ và ∨ cho nhau", font=FONT, font_size=32, color=WHITE).move_to([0, -5.6, 0])
        self.play(FadeIn(k), run_time=0.6)
        self.wait(2.5)
        self.play(*[FadeOut(m) for m in [h1, row, n1, h2, row2, n2, k]], run_time=0.6)

        # ===== 4. Bảng chân trị =====
        c = swap_cap(self, c, cap("Từ bảng chân trị ra DNF", 40, GOLD))
        fx = T("f = (p → q) ∧ (q → r)", 36, sym=False).move_to([0, 5.4, 0])
        self.play(FadeIn(fx), run_time=0.7)
        xs = [-1.9, -0.8, 0.3, 1.9]
        y0, dy = 4.5, 0.55
        heads = [tbl_cell(x, y0, s, GOLD) for x, s in zip(xs, ["p", "q", "r", "f"])]
        line = Line([-2.6, y0 - 0.3, 0], [2.6, y0 - 0.3, 0], color=DIM, stroke_width=2)
        cells = []
        for i, (row_, fv) in enumerate(zip(ROWS, F_VAL)):
            ys = y0 - (i + 1) * dy - 0.05
            cs = [tbl_cell(x, ys, tf(b)) for x, b in zip(xs[:3], row_)]
            cs.append(tbl_cell(xs[3], ys, tf(fv), GREEN if fv else RED))
            cells.append(cs)
        self.play(*[FadeIn(h) for h in heads], Create(line), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(m) for cs in cells for m in cs], lag_ratio=0.02), run_time=1.6)
        self.wait(1.0)
        rule = Text("Chỉ xét hàng có f = T. Mỗi hàng cho một hội:\nbiến T giữ nguyên, biến F thêm ¬", font=FONT, font_size=30, color=GOLD, line_spacing=1.1).move_to([0, -0.9, 0])
        rule.scale_to_fit_width(min(rule.width, 7.8))
        self.play(FadeIn(rule), run_time=0.6)
        self.wait(2.0)
        for i, cs in enumerate(cells):
            if not F_VAL[i]:
                self.play(*[m.animate.set_opacity(0.3) for m in cs], run_time=0.3)
        self.wait(0.5)
        pre_x, tx_x = -2.7, -2.0
        lines_made = []
        for j, row_ in enumerate(T_ROWS):
            i = ROWS.index(row_)
            box = SurroundingRectangle(VGroup(*cells[i]), color=GOLD, buff=0.06, stroke_width=3)
            ty = -2.3 - j * 0.9
            term = T(dnf_term(row_), 40).move_to([tx_x, ty, 0], aligned_edge=LEFT)
            term.align_to([tx_x, 0, 0], LEFT).set_y(ty)
            grp = [term]
            if j > 0:
                pre = Text("∨", font=FONT, font_size=40, color=GOLD).move_to([pre_x, ty, 0])
                grp.append(pre)
            self.play(Create(box), run_time=0.4)
            self.play(*[TransformFromCopy(VGroup(*cells[i][:3]), g) if g is term else FadeIn(g) for g in grp], run_time=0.9)
            self.wait(1.0)
            self.play(FadeOut(box), run_time=0.2)
            lines_made.append(grp)
        fin = Text("DNF đầy đủ của f", font=FONT, font_size=32, color=GREEN).move_to([0, -6.1, 0])
        self.play(FadeIn(fin), run_time=0.6)
        self.wait(3.0)
        self.play(FadeOut(fin), FadeOut(rule), *[FadeOut(m) for g in lines_made for m in g], run_time=0.6)

        # ===== 5. CNF từ hàng F =====
        c = swap_cap(self, c, cap("Từ bảng chân trị ra CNF", 40, GOLD))
        self.play(*[cs[m_].animate.set_opacity(1) for cs in cells for m_ in range(4)], run_time=0.4)
        for i, cs in enumerate(cells):
            if F_VAL[i]:
                self.play(*[m.animate.set_opacity(0.3) for m in cs], run_time=0.25)
        rule = Text("Chỉ xét hàng có f = F. Mỗi hàng cho một mệnh đề con:\nbiến T thêm ¬, biến F giữ nguyên", font=FONT, font_size=30, color=GOLD, line_spacing=1.1).move_to([0, -0.9, 0])
        rule.scale_to_fit_width(min(rule.width, 7.8))
        self.play(FadeIn(rule), run_time=0.6)
        self.wait(2.5)
        why = Text("Mệnh đề con này chỉ sai đúng ở hàng đó,\nnên hội của chúng loại hết các hàng F", font=FONT, font_size=26, color=DIM, line_spacing=1.1).move_to([0, -6.3, 0])
        why.scale_to_fit_width(min(why.width, 7.8))
        lines_made = []
        for j, row_ in enumerate(F_ROWS):
            i = ROWS.index(row_)
            box = SurroundingRectangle(VGroup(*cells[i]), color=RED, buff=0.06, stroke_width=3)
            ty = -2.3 - j * 0.9
            cl_ = T(cnf_clause(row_), 40).move_to([tx_x, ty, 0])
            cl_.align_to([tx_x, 0, 0], LEFT).set_y(ty)
            grp = [cl_]
            if j > 0:
                pre = Text("∧", font=FONT, font_size=40, color=BLUE).move_to([pre_x, ty, 0])
                grp.append(pre)
            self.play(Create(box), run_time=0.4)
            self.play(*[TransformFromCopy(VGroup(*cells[i][:3]), g) if g is cl_ else FadeIn(g) for g in grp], run_time=0.9)
            self.wait(1.0)
            self.play(FadeOut(box), run_time=0.2)
            lines_made.append(grp)
        self.play(FadeIn(why), run_time=0.6)
        self.wait(3.5)
        fin = Text("CNF đầy đủ của f", font=FONT, font_size=32, color=GREEN).move_to([0, -6.1, 0])
        self.play(FadeOut(why), FadeIn(fin), run_time=0.6)
        self.wait(2.0)
        # rút gọn
        sm = T("Rút gọn được: f ≡ (¬p ∨ q) ∧ (¬q ∨ r)", 30, sym=True)
        fit(sm, 7.8)
        sm.move_to([0, -6.1, 0])
        self.play(FadeOut(fin), FadeIn(sm), run_time=0.7)
        self.wait(3.0)
        self.play(*[FadeOut(m) for g in lines_made for m in g], FadeOut(sm), FadeOut(rule),
                  *[FadeOut(m) for cs in cells for m in cs], *[FadeOut(h) for h in heads], FadeOut(line), FadeOut(fx), run_time=0.7)

        # ===== 6. Biến đổi bằng luật =====
        c = swap_cap(self, c, cap("Đưa công thức về DNF, CNF", 40, GOLD))
        gx = T("g = (p ↔ q) → r", 44, sym=False).move_to([0, 5.2, 0])
        self.play(FadeIn(gx), run_time=0.7)
        plan = Text("3 việc: bỏ → và ↔, đẩy ¬ vào trong, rồi phân phối", font=FONT, font_size=28, color=DIM).move_to([0, 4.3, 0])
        plan.scale_to_fit_width(7.6)
        self.play(FadeIn(plan), run_time=0.6)
        self.wait(2.0)

        def run_steps(steps, y_start, dy=1.35, size=34):
            """steps: (công thức, phần tô sáng, tên luật). Trả về danh sách mobject."""
            made = []
            y = y_start
            for formula, hl, law in steps:
                m = T(formula, size, hl=hl, sym=False)
                fit(m, 7.8)
                m.move_to([0, y, 0])
                lw = Text(law, font=FONT, font_size=26, color=GOLD)
                lw.scale_to_fit_width(min(lw.width, 7.8))
                lw.next_to(m, DOWN, buff=0.2)
                self.play(FadeIn(m, shift=DOWN * 0.15), FadeIn(lw), run_time=0.8)
                self.wait(2.4)
                made += [m, lw]
                y -= dy
            return made, y

        stage1 = [
            ("(p ↔ q) → r", None, "Bước 0: công thức ban đầu"),
            ("¬(p ↔ q) ∨ r", "¬(p ↔ q) ∨ r", "Bỏ →:  A → B ≡ ¬A ∨ B"),
            ("¬((p → q) ∧ (q → p)) ∨ r", "(p → q) ∧ (q → p)", "Bỏ ↔:  A ↔ B ≡ (A → B) ∧ (B → A)"),
            ("¬((¬p ∨ q) ∧ (¬q ∨ p)) ∨ r", ["(¬p ∨ q)", "(¬q ∨ p)"], "Bỏ → lần nữa"),
            ("(¬(¬p ∨ q) ∨ ¬(¬q ∨ p)) ∨ r", ["¬(¬p ∨ q)", "¬(¬q ∨ p)"], "De Morgan:  ¬(A ∧ B) ≡ ¬A ∨ ¬B"),
            ("(p ∧ ¬q) ∨ (¬p ∧ q) ∨ r", ["(p ∧ ¬q)", "(¬p ∧ q)"], "De Morgan và phủ định kép"),
        ]
        made1, ylast = run_steps(stage1, 3.3)
        ylast = ylast - 0.5
        box = SurroundingRectangle(made1[-2], color=GREEN, buff=0.1, stroke_width=4)
        res = Text("Đã là DNF", font=FONT, font_size=34, color=GREEN).move_to([0, ylast, 0])
        self.play(Create(box), FadeIn(res), run_time=0.8)
        self.wait(3.0)
        # sang CNF
        keep = made1[-2].copy()
        self.play(*[FadeOut(m) for m in made1], FadeOut(box), FadeOut(res), FadeOut(plan), run_time=0.6)
        c = swap_cap(self, c, cap("Tiếp: từ DNF sang CNF", 40, GOLD))
        keep.move_to([0, 4.0, 0])
        self.add(keep)
        lw0 = Text("Muốn CNF thì phân phối ∨ qua ∧", font=FONT, font_size=28, color=GOLD).next_to(keep, DOWN, buff=0.2)
        self.play(FadeIn(lw0), run_time=0.6)
        self.wait(1.5)
        stage2 = [
            ("((p ∨ ¬p) ∧ (p ∨ q) ∧\n(¬q ∨ ¬p) ∧ (¬q ∨ q)) ∨ r",
             ["(p ∨ ¬p)", "(p ∨ q)", "(¬q ∨ ¬p)", "(¬q ∨ q)"], "Phân phối:  A ∨ (B ∧ C) ≡ (A ∨ B) ∧ (A ∨ C)"),
            ("((p ∨ q) ∧ (¬p ∨ ¬q)) ∨ r", ["(p ∨ q)", "(¬p ∨ ¬q)"], "p ∨ ¬p ≡ T,  q ∨ ¬q ≡ T,  A ∧ T ≡ A"),
            ("(p ∨ q ∨ r) ∧ (¬p ∨ ¬q ∨ r)", ["(p ∨ q ∨ r)", "(¬p ∨ ¬q ∨ r)"], "Phân phối ∨ r vào từng mệnh đề"),
        ]
        made2, ylast = run_steps(stage2, 2.0, dy=2.0, size=32)
        ylast = ylast - 0.3
        box = SurroundingRectangle(made2[-2], color=GREEN, buff=0.1, stroke_width=4)
        res = Text("Đã là CNF", font=FONT, font_size=34, color=GREEN).move_to([0, ylast, 0])
        self.play(Create(box), FadeIn(res), run_time=0.8)
        self.wait(3.5)
        self.play(*[FadeOut(m) for m in made2 + [box, res, keep, lw0, gx]], run_time=0.6)

        # ===== 7. Kiểm tra bảng chân trị =====
        c = swap_cap(self, c, cap("Kiểm tra: cùng bảng chân trị", 38, GOLD))
        gx = T("g = (p ↔ q) → r", 38, sym=False).move_to([0, 5.3, 0])
        self.play(FadeIn(gx), run_time=0.5)
        xs2 = [-3.0, -2.1, -1.2, 0.2, 1.7, 3.1]
        hs = ["p", "q", "r", "g", "DNF", "CNF"]
        y0 = 4.2
        hd = [tbl_cell(x, y0, s, GOLD, 30) for x, s in zip(xs2, hs)]
        ln = Line([-3.5, y0 - 0.3, 0], [3.7, y0 - 0.3, 0], color=DIM, stroke_width=2)
        self.play(*[FadeIn(h) for h in hd], Create(ln), run_time=0.6)
        allc = []
        for i, row_ in enumerate(ROWS):
            ys = y0 - (i + 1) * 0.7 - 0.05
            vals = [*row_, g_ex(*row_), bool(G_DNF(*row_)), bool(G_CNF(*row_))]
            cs = []
            for k_, (x, v) in enumerate(zip(xs2, vals)):
                col = WHITE if k_ < 3 else (GREEN if v else RED)
                cs.append(tbl_cell(x, ys, tf(v), col, 32))
            allc.append(cs)
        self.play(LaggedStart(*[FadeIn(m) for cs in allc for m in cs], lag_ratio=0.02), run_time=1.6)
        self.wait(1.5)
        ok_boxes = []
        for i, cs in enumerate(allc):
            b = SurroundingRectangle(VGroup(*cs[3:]), color=GREEN, buff=0.11, stroke_width=2.5)
            ok_boxes.append(b)
        self.play(LaggedStart(*[Create(b) for b in ok_boxes], lag_ratio=0.12), run_time=1.8)
        ck = Text("3 cột giống nhau ở cả 8 hàng", font=FONT, font_size=34, color=GREEN).move_to([0, -2.2, 0])
        self.play(FadeIn(ck), run_time=0.6)
        self.wait(1.5)
        ck2 = Text("Biến đổi đúng luật thì bảng chân trị không đổi.\nTa nên thử lại như vậy sau khi biến đổi dài.", font=FONT, font_size=30, color=DIM, line_spacing=1.1).move_to([0, -3.9, 0])
        ck2.scale_to_fit_width(min(ck2.width, 7.8))
        self.play(FadeIn(ck2), run_time=0.6)
        self.wait(3.5)
        self.play(*[FadeOut(m) for m in [gx, ln, ck, ck2] + hd + ok_boxes + [m for cs in allc for m in cs]], run_time=0.6)

        # ===== 8. Vì sao quan trọng =====
        c = swap_cap(self, c, cap("Vì sao cần CNF?", 44, GOLD))
        a1 = Text("Mọi công thức đều có cả DNF lẫn CNF", font=FONT, font_size=32, color=WHITE).move_to([0, 4.4, 0])
        a1.scale_to_fit_width(7.8)
        a1b = Text("(đọc thẳng từ bảng chân trị, như ở trên)", font=FONT, font_size=28, color=DIM).move_to([0, 3.7, 0])
        self.play(FadeIn(a1), FadeIn(a1b), run_time=0.8)
        self.wait(2.5)
        sat = Text("SAT solver nhận đầu vào là CNF", font=FONT, font_size=34, color=GOLD).move_to([0, 2.2, 0])
        sat.scale_to_fit_width(7.8)
        self.play(FadeIn(sat), run_time=0.7)
        cnfx = T("(x ∨ ¬y) ∧ (¬x ∨ z) ∧ (y ∨ z)", 40).move_to([0, 0.8, 0])
        fit(cnfx, 8.0)
        self.play(FadeIn(cnfx), run_time=0.8)
        ex = Text("Mỗi mệnh đề con là một ràng buộc.\nSolver tìm cách gán x, y, z\nđể mọi ràng buộc cùng đúng.", font=FONT, font_size=32, line_spacing=1.15).move_to([0, -1.3, 0])
        self.play(FadeIn(ex), run_time=0.8)
        self.wait(4.0)
        warn = Text("Lưu ý: phân phối ∨ qua ∧ có thể làm công thức\nphình to rất nhanh khi có nhiều biến,\nnên người ta còn dùng cách mã hoá khác\nđể giữ CNF ngắn.", font=FONT, font_size=28, color=DIM, line_spacing=1.15).move_to([0, -4.2, 0])
        warn.scale_to_fit_width(min(warn.width, 7.8))
        self.play(FadeIn(warn), run_time=0.7)
        self.wait(5.0)
        self.play(*[FadeOut(m) for m in [a1, a1b, sat, cnfx, ex, warn]], run_time=0.6)

        # ===== 9. Tóm tắt =====
        c = swap_cap(self, c, cap("Tóm tắt", 44, GOLD))
        def col(title, color, l1, l2, l3, sample, x):
            ttl = Text(title, font=FONT, font_size=48, color=color)
            body = Text(f"{l1}\n{l2}\n{l3}", font=FONT, font_size=32, line_spacing=1.2)
            smp = T(sample, 32)
            g = VGroup(ttl, body, smp).arrange(DOWN, buff=0.4)
            return g
        dn = col("DNF", BLUE, "Tuyển của các hội", "Lấy các hàng T", "Mỗi hàng một hội", "(p ∧ q ∧ r) ∨ …", 0)
        cn = col("CNF", GOLD, "Hội của các tuyển", "Lấy các hàng F", "Mỗi hàng một mệnh đề con", "(¬p ∨ ¬q ∨ r) ∧ …", 0)
        dn.move_to([0, 3.3, 0])
        cn.move_to([0, -1.2, 0])
        self.play(FadeIn(dn), run_time=0.8)
        self.wait(2.0)
        self.play(FadeIn(cn), run_time=0.8)
        self.wait(2.5)
        end = Text("Biến đổi bằng luật:\nbỏ →, ↔ · đẩy ¬ vào trong · phân phối", font=FONT, font_size=30, color=GREEN, line_spacing=1.2).move_to([0, -4.7, 0])
        end.scale_to_fit_width(min(end.width, 7.8))
        self.play(FadeIn(end), run_time=0.7)
        self.wait(4.5)
