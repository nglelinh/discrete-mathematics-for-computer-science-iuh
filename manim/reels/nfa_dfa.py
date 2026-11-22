from common import *
import re
from itertools import product

# ---------- NFA và xây dựng tập con (kiểm tra bằng code) ----------
# L = các chuỗi bắt đầu bằng 1 và kết thúc bằng 01
NQ = ["q0", "q1", "q2", "q3"]
DELTA = {("q0", "1"): {"q1"}, ("q1", "0"): {"q1", "q2"}, ("q1", "1"): {"q1"}, ("q2", "1"): {"q3"}}
START, FINAL = "q0", {"q3"}
SIGMA = "01"


def step(S, a):
    out = set()
    for q in S:
        out |= DELTA.get((q, a), set())
    return frozenset(out)


def subset():
    start = frozenset({START})
    order, trans, todo = [start], {}, [start]
    while todo:
        S = todo.pop(0)
        for a in SIGMA:
            T = step(S, a)
            trans[(S, a)] = T
            if T not in order:
                order.append(T)
                todo.append(T)
    return order, trans


ORDER, TRANS = subset()
F = lambda *xs: frozenset(xs)
assert ORDER == [F("q0"), F(), F("q1"), F("q1", "q2"), F("q1", "q3")]
NAME = {F("q0"): "A", F(): "∅", F("q1"): "B", F("q1", "q2"): "C", F("q1", "q3"): "D"}
ACC = [S for S in ORDER if S & FINAL]
assert ACC == [F("q1", "q3")]


def nfa_accepts(w):
    S = F(START)
    for ch in w:
        S = step(S, ch)
    return bool(S & FINAL)


def dfa_accepts(w):
    S = F(START)
    for ch in w:
        S = TRANS[(S, ch)]
    return S in ACC


for n in range(0, 11):
    for t in product(SIGMA, repeat=n):
        w = "".join(t)
        exp = re.fullmatch(r"1[01]*01", w) is not None
        assert nfa_accepts(w) == dfa_accepts(w) == exp


def trace(w):
    S, out = F(START), [F(START)]
    for ch in w:
        S = step(S, ch)
        out.append(S)
    return out


assert trace("1001") == [F("q0"), F("q1"), F("q1", "q2"), F("q1", "q2"), F("q1", "q3")]
assert trace("0101")[1] == F()
assert 2 ** 4 == 16


def sname(S):
    return "{" + ", ".join(sorted(S)) + "}" if S else "∅"


EDGE_C = "#8a8d93"


def state(name, p, r=0.42, final=False, size=28):
    c = Circle(radius=r, color=WHITE, fill_color=CELL, fill_opacity=1, stroke_width=3).move_to(p)
    g = VGroup(c)
    if final:
        g.add(Circle(radius=r - 0.08, color=WHITE, stroke_width=3).move_to(p))
    g.add(Text(name, font=FONT, font_size=size).move_to(p))
    return g


def loop(st, label, r=0.42, up=True):
    c = st.get_center()
    sgn = 1 if up else -1
    a = CurvedArrow(c + np.array([-0.26, sgn * (r - 0.05), 0]), c + np.array([0.26, sgn * (r - 0.05), 0]),
                    angle=-sgn * 1.45 * PI, color=EDGE_C, stroke_width=4, tip_length=0.2)
    t = Text(label, font=FONT, font_size=26, color=WHITE).move_to(c + np.array([0, sgn * (r + 1.08), 0]))
    return VGroup(a, t)


def arrow(s1, s2, label, angle=0, r=0.42, lab_off=None):
    p1, p2 = s1.get_center(), s2.get_center()
    if angle == 0:
        a = Arrow(p1, p2, buff=r, color=EDGE_C, stroke_width=4, tip_length=0.22, max_tip_length_to_length_ratio=0.3)
        mid = a.get_center()
        n = np.array([-(p2 - p1)[1], (p2 - p1)[0], 0])
        n = n / np.linalg.norm(n)
        lp = mid + n * 0.28
    else:
        d = (p2 - p1) / np.linalg.norm(p2 - p1)
        rot = lambda v, t: np.array([v[0] * np.cos(t) - v[1] * np.sin(t), v[0] * np.sin(t) + v[1] * np.cos(t), 0])
        q1 = p1 + rot(d, angle / 2) * r
        q2 = p2 - rot(d, -angle / 2) * r
        a = CurvedArrow(q1, q2, angle=angle, color=EDGE_C, stroke_width=4, tip_length=0.22)
        mid = a.point_from_proportion(0.5)
        lp = mid + (mid - (p1 + p2) / 2) / max(np.linalg.norm(mid - (p1 + p2) / 2), 1e-6) * 0.25
    if lab_off is not None:
        lp = a.point_from_proportion(0.5) + lab_off
    t = Text(label, font=FONT, font_size=26, color=WHITE).move_to(lp)
    return VGroup(a, t)


def start_arrow(st, r=0.42):
    c = st.get_center()
    return Arrow(c + LEFT * (r + 0.75), c + LEFT * r, buff=0, color=WHITE, stroke_width=4, tip_length=0.2, max_tip_length_to_length_ratio=0.4)


def build_nfa(y=4.3):
    xs = [-3.0, -1.0, 1.1, 3.2]
    st = {q: state(q, [x, y, 0], final=(q in FINAL)) for q, x in zip(NQ, xs)}
    ed = [arrow(st["q0"], st["q1"], "1"), loop(st["q1"], "0, 1"), arrow(st["q1"], st["q2"], "0"), arrow(st["q2"], st["q3"], "1")]
    sa = start_arrow(st["q0"])
    return st, ed, sa


def tape(w, y, x0=None, size=40):
    cells = VGroup()
    for i, ch in enumerate(w):
        sq = Square(0.7, color=DIM, stroke_width=3)
        t = Text(ch, font=FONT, font_size=size)
        cells.add(VGroup(sq, t))
    cells.arrange(RIGHT, buff=0.06).move_to([0, y, 0])
    return cells


class NfaDfa(Scene):
    def set_active(self, st, S, color=GOLD):
        return [st[q][0].animate.set_fill(color if q in S else CELL, 0.55 if q in S else 1) for q in st]

    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Otomat hữu hạn", 44)
        t1 = Text("NFA → DFA", font=FONT, font_size=88, color=GOLD).move_to([0, 1.4, 0])
        t2 = para("Xây dựng tập con:\nmọi NFA đều có một DFA tương đương", 34, y=-0.8)
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. NFA =====
        c = swap_cap(self, c, cap("Một NFA 4 trạng thái", 42, GOLD))
        st, ed, sa = build_nfa()
        self.play(LaggedStart(*[GrowFromCenter(s) for s in st.values()], lag_ratio=0.15), FadeIn(sa), run_time=1.0)
        self.play(*[Create(e[0]) for e in ed], *[FadeIn(e[1]) for e in ed], run_time=1.0)
        n1 = para("Nhận các chuỗi bắt đầu bằng 1\nvà kết thúc bằng 01", 32, WHITE, y=1.6)
        self.play(FadeIn(n1), run_time=0.6)
        self.wait(2.5)
        n2 = para("Không tất định: ở q1 đọc 0 thì có hai lựa chọn,\nở lại q1 hoặc sang q2", 28, BLUE, y=-0.1)
        self.play(FadeIn(n2), Indicate(ed[1], color=BLUE), Indicate(ed[2], color=BLUE), run_time=1.2)
        self.wait(2.5)
        n3 = para("Ở q0 đọc 0, ở q2 đọc 0, ở q3 đọc gì cũng không có cạnh:\nnhánh đó chết", 26, DIM, y=-1.7)
        self.play(FadeIn(n3), run_time=0.6)
        self.wait(3.0)
        n4 = para("NFA chấp nhận chuỗi nếu CÓ ÍT NHẤT MỘT cách đi\nkết thúc ở trạng thái chấp nhận (vòng đôi).", 28, GOLD, y=-3.4)
        self.play(FadeIn(n4), run_time=0.6)
        self.wait(3.5)
        self.play(FadeOut(n1), FadeOut(n2), FadeOut(n3), FadeOut(n4), run_time=0.5)

        # ===== 3. Chạy NFA bằng tập trạng thái =====
        c = swap_cap(self, c, cap("Theo dõi mọi nhánh cùng lúc", 40, GOLD))
        w = "1001"
        tp = tape(w, 1.7)
        self.play(FadeIn(tp), run_time=0.5)
        tr = trace(w)
        setl = para("Tập đang bật: {q0}", 32, GOLD, y=0.3)
        self.play(*self.set_active(st, tr[0]), FadeIn(setl), run_time=0.6)
        hist = [sname(tr[0])]
        histm = para(" → ".join(hist), 28, WHITE, y=-1.0)
        self.play(FadeIn(histm), run_time=0.4)
        self.wait(1.5)
        for i, ch in enumerate(w):
            self.play(tp[i][0].animate.set_stroke(GOLD, 5), run_time=0.3)
            hist.append(sname(tr[i + 1]))
            nh = para(" → ".join(hist), 28, WHITE, y=-1.0)
            nl = para(f"Đọc {ch}: tập đang bật {sname(tr[i + 1])}", 32, GOLD, y=0.3)
            self.play(*self.set_active(st, tr[i + 1]), Transform(setl, nl), Transform(histm, nh), run_time=0.7)
            self.wait(1.8)
            self.play(tp[i][0].animate.set_stroke(DIM, 3), run_time=0.2)
        okm = para("Tập cuối chứa q3 → chấp nhận 1001", 32, GREEN, y=-2.3)
        self.play(FadeIn(okm), run_time=0.6)
        self.wait(2.5)
        self.play(FadeOut(tp), FadeOut(okm), FadeOut(histm), run_time=0.4)
        w2 = "0101"
        tp = tape(w2, 1.7)
        self.play(FadeIn(tp), *self.set_active(st, tr[0]), Transform(setl, para("Tập đang bật: {q0}", 32, GOLD, y=0.3)), run_time=0.6)
        self.play(tp[0][0].animate.set_stroke(GOLD, 5), run_time=0.3)
        self.play(*self.set_active(st, F()), Transform(setl, para("Đọc 0: tập rỗng ∅", 32, RED, y=0.3)), run_time=0.7)
        dd = para("Mọi nhánh đều chết, đọc tiếp vẫn là ∅ → loại 0101", 28, RED, y=-1.0)
        self.play(FadeIn(dd), run_time=0.6)
        self.wait(3.0)
        self.play(FadeOut(tp), FadeOut(dd), FadeOut(setl), *self.set_active(st, F()), run_time=0.4)
        idea = para("Ý tưởng: mỗi TẬP trạng thái của NFA\nlà MỘT trạng thái của DFA", 34, GOLD, y=0.6)
        self.play(FadeIn(idea), run_time=0.7)
        self.wait(2.5)
        fm = VGroup(Text("Bắt đầu: {q0}", font=FONT, font_size=28),
                    Text("δ(S, a) = hợp các δN(q, a) với q ∈ S", font=FONT, font_size=28),
                    Text("Chấp nhận: các tập có chứa q3", font=FONT, font_size=28, color=GREEN)).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([0, -1.6, 0])
        self.play(LaggedStart(*[FadeIn(m) for m in fm], lag_ratio=0.5), run_time=1.6)
        self.wait(4.0)
        self.play(FadeOut(idea), FadeOut(fm), run_time=0.5)

        # ===== 4. Lập bảng chuyển =====
        c = swap_cap(self, c, cap("Lập bảng chuyển DFA", 42, GOLD))
        xs = [-2.3, 0.7, 2.8]
        y0, dy = 2.5, 0.62
        heads = [Text(s, font=FONT, font_size=30, color=GOLD).move_to([x, y0, 0]) for x, s in zip(xs, ["Trạng thái", "đọc 0", "đọc 1"])]
        hl = Line([-4.0, y0 - 0.32, 0], [4.0, y0 - 0.32, 0], color=DIM, stroke_width=2)
        self.play(*[FadeIn(h) for h in heads], Create(hl), run_time=0.6)
        status = para("Bắt đầu với tập {q0}", 28, WHITE, y=-1.6)
        self.play(FadeIn(status), run_time=0.4)
        rows_m = {}
        known = [ORDER[0]]

        def row_label(S, i):
            col = GREEN if S in ACC else (RED if not S else WHITE)
            t = Text(f"{NAME[S]} = {sname(S)}" if S else "∅ (chết)", font=FONT, font_size=28, color=col)
            return t.move_to([xs[0], y0 - (i + 1) * dy, 0])
        r0 = row_label(ORDER[0], 0)
        self.play(FadeIn(r0), run_time=0.5)
        rows_m[ORDER[0]] = r0
        cells = []
        for i, S in enumerate(ORDER):
            box = SurroundingRectangle(rows_m[S], color=GOLD, buff=0.08, stroke_width=3)
            self.play(Create(box), run_time=0.3)
            for j, a in enumerate(SIGMA):
                T = TRANS[(S, a)]
                parts = [f"δN({q}, {a}) = {sname(DELTA.get((q, a), set()))}" for q in sorted(S)]
                if not S:
                    expl = f"Từ ∅ đọc {a}: vẫn ∅"
                elif len(S) == 1:
                    expl = f"Từ {sname(S)} đọc {a}:  {sname(T)}"
                else:
                    expl = "  ∪  ".join(sname(DELTA.get((q, a), set())) for q in sorted(S)) + f"  =  {sname(T)}"
                    expl = f"Từ {sname(S)} đọc {a}:  " + expl
                ns = para(expl, 28, WHITE, y=-1.6)
                status = swap_cap(self, status, ns, 0.35)
                # tô sáng trên NFA
                hi = self.set_active(st, S, BLUE)
                self.play(*hi, run_time=0.4)
                self.play(*self.set_active(st, T, GOLD) if T else [m for m in self.set_active(st, F())], run_time=0.5)
                cell = Text(NAME[T] if T else "∅", font=FONT, font_size=30,
                            color=GREEN if T in ACC else (RED if not T else WHITE)).move_to([xs[1 + j], y0 - (i + 1) * dy, 0])
                self.play(FadeIn(cell, scale=1.3), run_time=0.4)
                cells.append(cell)
                if T not in known:
                    known.append(T)
                    k = len(known) - 1
                    nr = row_label(T, k)
                    newm = para(("Tập mới → thêm hàng " + (NAME[T] if T else "∅")) if T else "Tập rỗng ∅: trạng thái chết", 28, GOLD if T else RED, y=-2.4)
                    self.play(FadeIn(nr), FadeIn(newm), run_time=0.5)
                    rows_m[T] = nr
                    self.wait(2.0)
                    self.play(FadeOut(newm), run_time=0.3)
                else:
                    self.wait(1.9)
            self.play(FadeOut(box), run_time=0.2)
        done = para("Không còn tập mới: bảng xong, 5 trạng thái", 28, GREEN, y=-1.6)
        status = swap_cap(self, status, done, 0.4)
        self.play(*self.set_active(st, F()), run_time=0.3)
        self.wait(2.0)
        cnt = para("NFA có 4 trạng thái → tối đa 2⁴ = 16 tập con.\nChỉ cần những tập tới được từ {q0}: ở đây 5.", 26, DIM, y=-2.8)
        self.play(FadeIn(cnt), run_time=0.6)
        self.wait(4.0)
        self.play(FadeOut(cnt), FadeOut(status), run_time=0.4)

        # ===== 5. Vẽ DFA =====
        c = swap_cap(self, c, cap("DFA thu được", 44, GOLD))
        tbl = VGroup(*heads, hl, *rows_m.values(), *cells)
        nfa_all = VGroup(*st.values(), *ed, sa)
        self.play(FadeOut(nfa_all), tbl.animate.scale(0.85).move_to([0, 4.0, 0]), run_time=0.8)
        D = {"A": state("A", [-3.0, -2.3, 0]), "B": state("B", [-0.3, -2.3, 0]), "C": state("C", [-0.3, -5.1, 0]),
             "D": state("D", [2.9, -3.7, 0], final=True), "∅": state("∅", [-3.0, -5.1, 0])}
        dsa = Arrow(D["A"].get_center() + LEFT * 1.25, D["A"].get_center() + LEFT * 0.42, buff=0, color=WHITE,
                    stroke_width=4, tip_length=0.2, max_tip_length_to_length_ratio=0.4)
        de = [arrow(D["A"], D["B"], "1"),
              arrow(D["A"], D["∅"], "0"),
              loop(D["∅"], "0, 1", up=False),
              loop(D["B"], "1"),
              arrow(D["B"], D["C"], "0"),
              loop(D["C"], "0", up=False),
              arrow(D["C"], D["D"], "1", angle=-1.0),
              arrow(D["D"], D["C"], "0", angle=-1.0),
              arrow(D["D"], D["B"], "1")]
        self.play(LaggedStart(*[GrowFromCenter(s) for s in D.values()], lag_ratio=0.12), FadeIn(dsa), run_time=1.0)
        for e in de:
            self.play(Create(e[0]), FadeIn(e[1]), run_time=0.45)
        self.wait(1.5)
        dn = para("Mỗi trạng thái, mỗi ký tự: đúng một cạnh", 28, WHITE, y=1.3)
        self.play(FadeIn(dn), run_time=0.6)
        self.wait(2.5)

        # chạy DFA trên 1001
        w = "1001"
        tp = tape(w, 0.2, size=34).scale(0.8)
        path = ["A"]
        S = ORDER[0]
        for ch in w:
            S = TRANS[(S, ch)]
            path.append(NAME[S])
        assert path == ["A", "B", "C", "C", "D"]
        self.play(FadeIn(tp), D["A"][0].animate.set_fill(GOLD, 0.55), run_time=0.5)
        for i, ch in enumerate(w):
            self.play(tp[i][0].animate.set_stroke(GOLD, 5), D[path[i]][0].animate.set_fill(CELL, 1),
                      D[path[i + 1]][0].animate.set_fill(GOLD, 0.55), run_time=0.7)
            self.wait(1.2)
        ok = para("Dừng ở D (chứa q3) → chấp nhận, giống NFA", 28, GREEN, y=1.3)
        self.play(ReplacementTransform(dn, ok), run_time=0.5)
        self.wait(2.5)
        self.play(D["D"][0].animate.set_fill(CELL, 1), FadeOut(tp), run_time=0.4)
        # chuỗi bị loại
        w = "10110"
        tp = tape(w, 0.2, size=34).scale(0.8)
        path = ["A"]
        S = ORDER[0]
        for ch in w:
            S = TRANS[(S, ch)]
            path.append(NAME[S])
        assert path == ["A", "B", "C", "D", "B", "C"] and not dfa_accepts(w)
        nm = para("Thử 10110: kết thúc bằng 10", 28, WHITE, y=1.3)
        self.play(FadeIn(tp), ReplacementTransform(ok, nm), D["A"][0].animate.set_fill(GOLD, 0.55), run_time=0.5)
        for i, ch in enumerate(w):
            self.play(tp[i][0].animate.set_stroke(GOLD, 5), D[path[i]][0].animate.set_fill(CELL, 1),
                      D[path[i + 1]][0].animate.set_fill(GOLD, 0.55), run_time=0.7)
            self.wait(1.0)
        ok = para("Dừng ở C, không phải trạng thái chấp nhận → loại", 28, RED, y=1.3)
        self.play(ReplacementTransform(nm, ok), run_time=0.5)
        self.wait(2.5)
        self.play(D["C"][0].animate.set_fill(CELL, 1), FadeOut(tp), run_time=0.4)
        dead = para("∅ là trạng thái chết: vào rồi không ra.\nChuỗi bắt đầu bằng 0 rơi ngay vào ∅.", 28, RED, y=0.9)
        self.play(ReplacementTransform(ok, dead), D["∅"][0].animate.set_fill(RED, 0.4), run_time=0.6)
        self.wait(4.0)
        self.play(D["∅"][0].animate.set_fill(CELL, 1), FadeOut(dead), run_time=0.4)
        wipe(self, keep=[c])

        # ===== 6. Vì sao đúng, cái giá phải trả =====
        c = swap_cap(self, c, cap("Vì sao đúng và cái giá", 42, GOLD))
        p1 = para("Bất biến: sau khi đọc w, DFA ở đúng tập\ncác trạng thái NFA có thể tới bằng w.", 30, WHITE, y=3.8)
        p2 = para("Chứng minh bằng quy nạp theo độ dài w.\nDFA chấp nhận ⇔ tập đó chứa trạng thái kết thúc\n⇔ NFA chấp nhận.", 28, DIM, y=1.9)
        self.play(FadeIn(p1), run_time=0.6)
        self.wait(2.5)
        self.play(FadeIn(p2), run_time=0.6)
        self.wait(3.5)
        p3 = para("Cái giá: có thể tới 2ⁿ trạng thái", 32, RED, y=-0.2)
        p4 = para("“Ký tự thứ n tính từ cuối là 1”:\nNFA chỉ cần n + 1 trạng thái,\nDFA nhỏ nhất cần 2ⁿ trạng thái.", 28, WHITE, y=-2.0)
        self.play(FadeIn(p3), run_time=0.6)
        self.wait(1.5)
        self.play(FadeIn(p4), run_time=0.6)
        self.wait(4.0)
        p5 = para("Nên chỉ dựng các tập tới được, như vừa làm.", 28, GREEN, y=-4.0)
        self.play(FadeIn(p5), run_time=0.6)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 7. Tổng kết =====
        c = swap_cap(self, c, cap("Các bước xây dựng tập con", 40, GOLD))
        sm = VGroup(*[Text(s, font=FONT, font_size=30, color=col) for s, col in [
            ("1. Trạng thái đầu: {q0}", WHITE),
            ("2. Với mỗi tập S và ký tự a: lấy hợp", WHITE),
            ("    các trạng thái NFA đi tới được", BLUE),
            ("3. Gặp tập mới thì thêm hàng mới", WHITE),
            ("4. ∅ là trạng thái chết", RED),
            ("5. Tập chứa trạng thái kết thúc → chấp nhận", GREEN),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        sm[2].shift(RIGHT * 0.45)
        if sm.width > 7.4:
            sm.scale_to_fit_width(7.4)
        sm.move_to([0, 2.0, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.2) for m in sm], lag_ratio=0.5), run_time=3.0)
        self.wait(6.0)
