from common import *
from collections import deque

# ---------- Cây trong bài: A(B(D,E), C(-,F)) ----------
KIDS = {"A": ("B", "C"), "B": ("D", "E"), "C": (None, "F"), "D": (None, None), "E": (None, None), "F": (None, None)}
POS = {"A": (0, 4.3), "B": (-2.0, 2.8), "C": (2.0, 2.8), "D": (-3.0, 1.3), "E": (-1.0, 1.3), "F": (3.0, 1.3)}


def pre(n, K):
    return [] if n is None else [n] + pre(K[n][0], K) + pre(K[n][1], K)


def ino(n, K):
    return [] if n is None else ino(K[n][0], K) + [n] + ino(K[n][1], K)


def post(n, K):
    return [] if n is None else post(K[n][0], K) + post(K[n][1], K) + [n]


def level(r, K):
    out, q, states = [], deque([r]), []
    while q:
        states.append(list(q))
        n = q.popleft()
        out.append(n)
        for k in K[n]:
            if k is not None:
                q.append(k)
    return out, states


def euler(n, K, ev):
    if n is None:
        return
    ev.append((n, "pre"))
    euler(K[n][0], K, ev)
    ev.append((n, "in"))
    euler(K[n][1], K, ev)
    ev.append((n, "post"))


assert "".join(pre("A", KIDS)) == "ABDECF"
assert "".join(ino("A", KIDS)) == "DBEACF"
assert "".join(post("A", KIDS)) == "DEBFCA"
LV, LVQ = level("A", KIDS)
assert "".join(LV) == "ABCDEF"
assert LVQ == [["A"], ["B", "C"], ["C", "D", "E"], ["D", "E", "F"], ["E", "F"], ["F"]]
EV = []
euler("A", KIDS, EV)
for kind, f in (("pre", pre), ("in", ino), ("post", post)):
    assert [n for n, k in EV if k == kind] == f("A", KIDS)

# ---------- Cây biểu thức (3 + 4) × (5 − 2) ----------
EK = {"×": ("+", "−"), "+": ("3", "4"), "−": ("5", "2"), "3": (None, None), "4": (None, None), "5": (None, None), "2": (None, None)}
EPOS = {"×": (0, 4.4), "+": (-1.8, 3.0), "−": (1.8, 3.0), "3": (-2.7, 1.6), "4": (-0.9, 1.6), "5": (0.9, 1.6), "2": (2.7, 1.6)}
assert " ".join(pre("×", EK)) == "× + 3 4 − 5 2"
assert " ".join(post("×", EK)) == "3 4 + 5 2 − ×"
assert " ".join(ino("×", EK)) == "3 + 4 × 5 − 2"
OPS = {"+": lambda a, b: a + b, "−": lambda a, b: a - b, "×": lambda a, b: a * b}
STACK, st = [], []
for tok in post("×", EK):
    if tok in OPS:
        b, a = st.pop(), st.pop()
        st.append(OPS[tok](a, b))
    else:
        st.append(int(tok))
    STACK.append((tok, list(st)))
assert [s for _, s in STACK] == [[3], [3, 4], [7], [7, 5], [7, 5, 2], [7, 3], [21]] and (3 + 4) * (5 - 2) == 21

# ---------- BST ----------
KEYS = [8, 3, 10, 1, 6, 14, 4, 7]
BK, depth = {}, {}
for k in KEYS:
    BK[k] = [None, None]
    if k == KEYS[0]:
        depth[k] = 0
        continue
    cur, d = KEYS[0], 0
    while True:
        side = 0 if k < cur else 1
        d += 1
        if BK[cur][side] is None:
            BK[cur][side] = k
            BPAR = cur
            break
        cur = BK[cur][side]
    depth[k] = d
BK = {k: tuple(v) for k, v in BK.items()}
assert ino(8, BK) == sorted(KEYS) == [1, 3, 4, 6, 7, 8, 10, 14]
RANK = {k: i for i, k in enumerate(sorted(KEYS))}
BPOS = {k: (-3.5 + RANK[k] * 1.0, 4.6 - depth[k] * 1.25) for k in KEYS}
PARENT = {c: p for p, kids in BK.items() for c in kids if c is not None}
assert PARENT == {3: 8, 10: 8, 1: 3, 6: 3, 14: 10, 4: 6, 7: 6}

R = 0.42


def node(lbl, p, col=BLUE, size=32):
    c = Circle(R, color=col, stroke_width=4, fill_color=CELL, fill_opacity=1).move_to([p[0], p[1], 0])
    return VGroup(c, Text(str(lbl), font=FONT, font_size=size).move_to(c))


def edge(p, q):
    a, b = np.array([p[0], p[1], 0]), np.array([q[0], q[1], 0])
    d = (b - a) / np.linalg.norm(b - a)
    return Line(a + d * R, b - d * R, color=DIM, stroke_width=3)


def build(K, P, root, col=BLUE, size=32):
    nodes = {n: node(n, P[n], col, size) for n in K}
    edges = [edge(P[n], P[k]) for n in K for k in K[n] if k is not None]
    return nodes, VGroup(*edges)


class TreeTraversal(Scene):
    def wait(self, duration=1.0, **kw):
        super().wait(duration * 1.3, **kw)

    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Cây nhị phân", 44)
        t1 = Text("Duyệt cây", font=FONT, font_size=90, color=GOLD).move_to([0, 1.6, 0])
        t2 = para("Preorder, Inorder, Postorder và Level-order:\nthăm mọi nút, mỗi nút đúng một lần", 30, y=-0.4)
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. Ba thứ tự DFS =====
        c = swap_cap(self, c, cap("Ba thứ tự DFS: khác nhau ở lúc thăm gốc", 34, GOLD))
        nodes, edges = build(KIDS, POS, "A")
        self.play(Create(edges), *[GrowFromCenter(m) for m in nodes.values()], run_time=1.2)
        rules = VGroup(*[Text(s, font=FONT, font_size=28, color=col) for s, col in [
            ("Preorder (NLR):  Gốc → Trái → Phải", BLUE),
            ("Inorder (LNR):  Trái → Gốc → Phải", GREEN),
            ("Postorder (LRN):  Trái → Phải → Gốc", GOLD),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([0, -0.4, 0])
        for m in rules:
            self.play(FadeIn(m, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(1.4)
        self.wait(1.0)
        self.play(FadeOut(rules), run_time=0.4)

        # Euler tour
        tip = para("Mẹo: đi vòng quanh cây sát mép, bắt đầu bên trái gốc.\nGặp cạnh trái, đáy, phải của nút thì ghi vào dòng tương ứng.", 24, DIM, y=0.1)
        self.play(FadeIn(tip), run_time=0.6)
        self.wait(2.5)
        OFF = {"pre": np.array([-0.62, 0.1, 0]), "in": np.array([0, -0.62, 0]), "post": np.array([0.62, 0.1, 0])}
        COL = {"pre": BLUE, "in": GREEN, "post": GOLD}
        rowy = {"pre": -1.3, "in": -2.2, "post": -3.1}
        rl = VGroup(*[Text(s, font=FONT, font_size=26, color=COL[k]).move_to([-2.6, rowy[k], 0]) for k, s in
                      (("pre", "Preorder:"), ("in", "Inorder:"), ("post", "Postorder:"))])
        self.play(FadeIn(rl), run_time=0.5)
        cnt = {"pre": 0, "in": 0, "post": 0}
        pts = [np.array([POS[n][0], POS[n][1], 0]) + OFF[k] for n, k in EV]
        dot = Dot(pts[0], color=WHITE, radius=0.11)
        trail = VMobject(color=WHITE, stroke_width=2, stroke_opacity=0.5)
        trail.set_points_as_corners([pts[0], pts[0]])
        self.add(trail)
        self.play(FadeIn(dot), run_time=0.3)
        for i, ((n, k), p) in enumerate(zip(EV, pts)):
            if i > 0:
                new = trail.copy()
                new.set_points_as_corners(list(trail.get_anchors()) + [p]) if False else None
                seg = Line(pts[i - 1], p, color=WHITE, stroke_width=2, stroke_opacity=0.45)
                self.play(dot.animate.move_to(p), Create(seg), run_time=0.35)
            flag = Dot(p, color=COL[k], radius=0.09)
            letter = Text(n, font=FONT, font_size=32, color=COL[k]).move_to([-1.0 + cnt[k] * 0.75, rowy[k], 0])
            cnt[k] += 1
            self.play(FadeIn(flag, scale=1.5), FadeIn(letter, shift=UP * 0.15), run_time=0.3)
        self.play(FadeOut(dot), run_time=0.3)
        self.wait(1.0)
        ok = para("A B D E C F   ·   D B E A C F   ·   D E B F C A", 24, WHITE, y=-4.2)
        self.play(FadeIn(ok), run_time=0.5)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 3. Cây biểu thức =====
        c = swap_cap(self, c, cap("Cây biểu thức (3 + 4) × (5 − 2)", 38, GOLD))
        en, ee = build(EK, EPOS, "×")
        for k in ("×", "+", "−"):
            en[k][0].set_color(GOLD)
        self.play(Create(ee), *[GrowFromCenter(m) for m in en.values()], run_time=1.2)
        lines = [
            ("Preorder → tiền tố:", "× + 3 4 − 5 2", BLUE),
            ("Inorder → trung tố:", "(3 + 4) × (5 − 2)", GREEN),
            ("Postorder → hậu tố:", "3 4 + 5 2 − ×", GOLD),
        ]
        y = 0.3
        for a, b, col in lines:
            la = Text(a, font=FONT, font_size=24, color=DIM).move_to([-2.0, y, 0])
            lb = Text(b, font=FONT, font_size=30, color=col).move_to([1.9, y, 0])
            self.play(FadeIn(la), FadeIn(lb), run_time=0.6)
            self.wait(1.6)
            y -= 0.75
        n1 = para("Inorder cần thêm ngoặc để giữ đúng cấu trúc cây", 22, DIM, y=-2.0)
        self.play(FadeIn(n1), run_time=0.5)
        self.wait(2.0)
        # Stack evaluation
        sub = para("Tính hậu tố bằng ngăn xếp:", 26, WHITE, y=-2.9)
        self.play(FadeIn(sub), run_time=0.5)
        toks = post("×", EK)
        tk = VGroup(*[Text(t, font=FONT, font_size=34).move_to([-3.0 + i * 1.0, -3.8, 0]) for i, t in enumerate(toks)])
        self.play(FadeIn(tk), run_time=0.5)
        stack_g = VGroup()
        base_y = -6.2
        for i, (tok, st_) in enumerate(STACK):
            tk[i].set_color(GOLD)
            new = VGroup()
            for j, v in enumerate(st_):
                b = Rectangle(width=1.2, height=0.5, color=BLUE, stroke_width=2).move_to([2.8, base_y + 0.55 * j, 0])
                new.add(VGroup(b, Text(str(v), font=FONT, font_size=26).move_to(b)))
            self.play(Transform(stack_g, new) if len(stack_g) else FadeIn(new), run_time=0.45)
            if not len(stack_g):
                stack_g = new
            note = "đẩy " + tok if tok not in OPS else "lấy 2 số, tính, đẩy kết quả"
            nt = Text(note, font=FONT, font_size=22, color=DIM).move_to([-1.2, -4.8, 0])
            self.play(FadeIn(nt), run_time=0.25)
            self.wait(0.9)
            self.play(FadeOut(nt), run_time=0.2)
            tk[i].set_color(DIM)
        res = para("Kết quả: 21", 36, GOLD, y=-5.6)
        res.move_to([-1.4, -5.6, 0])
        self.play(FadeIn(res), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 4. BST + inorder =====
        c = swap_cap(self, c, cap("Inorder trên cây tìm kiếm nhị phân", 36, GOLD))
        q = para("Chèn lần lượt: 8, 3, 10, 1, 6, 14, 4, 7", 28, WHITE, y=5.5)
        self.play(FadeIn(q), run_time=0.5)
        bn = {}
        for k in KEYS:
            m = node(k, BPOS[k], BLUE, 28)
            anims = [GrowFromCenter(m)]
            if k in PARENT:
                anims.append(Create(edge(BPOS[PARENT[k]], BPOS[k])))
            self.play(*anims, run_time=0.45)
            bn[k] = m
            self.wait(0.3)
        n1 = para("Nhỏ hơn đi trái, lớn hơn đi phải", 24, DIM, y=-0.3)
        self.play(FadeIn(n1), run_time=0.5)
        self.wait(1.5)
        out = []
        for i, k in enumerate(ino(8, BK)):
            self.play(bn[k][0].animate.set_fill(GREEN, 0.6), run_time=0.3)
            t = Text(str(k), font=FONT, font_size=34, color=GREEN).move_to([-3.4 + i * 0.97, -1.5, 0])
            self.play(TransformFromCopy(bn[k][1], t), run_time=0.4)
            out.append(t)
        self.wait(1.0)
        r = para("Inorder của BST luôn là dãy tăng dần", 30, GOLD, y=-2.7)
        self.play(FadeIn(r), run_time=0.6)
        self.wait(1.5)
        w = para("Vì: mọi khóa bên trái < gốc < mọi khóa bên phải,\nvà Inorder in hết bên trái, rồi gốc, rồi bên phải.", 24, DIM, y=-3.9)
        self.play(FadeIn(w), run_time=0.5)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 5. Level-order =====
        c = swap_cap(self, c, cap("Level-order: duyệt theo mức bằng hàng đợi", 34, GOLD))
        nodes, edges = build(KIDS, POS, "A")
        self.play(Create(edges), *[GrowFromCenter(m) for m in nodes.values()], run_time=1.0)
        ql = Text("Hàng đợi:", font=FONT, font_size=26, color=DIM).move_to([-2.9, -0.2, 0])
        ol = Text("Đã thăm:", font=FONT, font_size=26, color=DIM).move_to([-2.9, -1.4, 0])
        self.play(FadeIn(ql), FadeIn(ol), run_time=0.4)
        qg = VGroup()
        visited = VGroup()
        for i, (n, qs) in enumerate(zip(LV, LVQ)):
            newq = VGroup(*[VGroup(Square(0.62, color=BLUE, stroke_width=2), Text(x, font=FONT, font_size=26)).move_to([-1.3 + j * 0.72, -0.2, 0]) for j, x in enumerate(qs)])
            if len(qg):
                self.play(Transform(qg, newq), run_time=0.4)
            else:
                qg = newq
                self.play(FadeIn(qg), run_time=0.4)
            self.wait(0.4)
            self.play(nodes[n][0].animate.set_fill(GOLD, 0.6), qg[0].animate.set_color(GOLD), run_time=0.35)
            v = Text(n, font=FONT, font_size=32, color=GOLD).move_to([-1.3 + i * 0.72, -1.4, 0])
            self.play(FadeIn(v, shift=DOWN * 0.2), run_time=0.3)
            visited.add(v)
            self.wait(0.5)
        self.play(FadeOut(qg), run_time=0.3)
        r = para("Lấy nút đầu hàng đợi, thăm nó, đẩy các con vào cuối.", 24, WHITE, y=-2.6)
        self.play(FadeIn(r), run_time=0.5)
        self.wait(1.5)
        r2 = para("Đây chính là BFS (Chương 12) trên cây.\nMọi cách duyệt đều O(n): mỗi nút vào/ra đúng một lần.", 24, DIM, y=-3.8)
        self.play(FadeIn(r2), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 6. Tóm tắt =====
        c = swap_cap(self, c, cap("Chọn cách duyệt nào?", 42, GOLD))
        sm = VGroup(*[Text(s, font=FONT, font_size=28, color=col) for s, col in [
            ("Preorder: sao chép / lưu cây, biểu thức tiền tố", BLUE),
            ("Inorder: BST → dãy đã sắp xếp", GREEN),
            ("Postorder: xóa cây, tính biểu thức từ lá lên", GOLD),
            ("Level-order: theo từng mức, gần gốc trước", RED),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.55)
        fitw(sm, 7.8).move_to([0, 2.6, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.2) for m in sm], lag_ratio=0.5), run_time=2.6)
        self.wait(2.0)
        e = para("Bài tiếp theo (16.4): cây Huffman, nơi đường đi\ntrái/phải trong cây trở thành mã 0/1.", 26, DIM, y=-1.2)
        self.play(FadeIn(e), run_time=0.6)
        self.wait(5.0)
