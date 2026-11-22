from common import *

# ---------- Đồ thị và các vết thuật toán (kiểm tra bằng code) ----------
POS = {"A": (-3.0, 4.3), "B": (0.0, 4.9), "C": (3.0, 4.3),
       "D": (-2.6, 1.3), "E": (0.2, 2.1), "F": (2.8, 1.1)}
W = {("A", "B"): 4, ("A", "D"): 2, ("B", "D"): 5, ("B", "E"): 3, ("B", "C"): 7,
     ("C", "E"): 6, ("C", "F"): 8, ("D", "E"): 1, ("E", "F"): 9}
V = sorted(POS)


def key(u, v):
    return (u, v) if (u, v) in W else (v, u)


def kruskal():
    parent = {v: v for v in V}

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    log, tree = [], []
    for (u, v), w in sorted(W.items(), key=lambda t: t[1]):
        if len(tree) == len(V) - 1:
            break
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
            tree.append((u, v))
            log.append(((u, v), True))
        else:
            log.append(((u, v), False))
    return log, tree


def prim(s="A"):
    S, tree, log = {s}, [], []
    while len(S) < len(V):
        cand = sorted([(w, e) for e, w in W.items() if (e[0] in S) != (e[1] in S)])
        w, e = cand[0]
        log.append(([c[1] for c in cand], e))
        tree.append(e)
        S |= set(e)
    return log, tree


K_LOG, K_TREE = kruskal()
P_LOG, P_TREE = prim()
assert [e for e, ok in K_LOG] == [("D", "E"), ("A", "D"), ("B", "E"), ("A", "B"), ("B", "D"), ("C", "E"), ("B", "C"), ("C", "F")]
assert [ok for e, ok in K_LOG] == [True, True, True, False, False, True, False, True]
assert P_TREE == [("A", "D"), ("D", "E"), ("B", "E"), ("C", "E"), ("C", "F")]
assert set(K_TREE) == set(P_TREE) and sum(W[e] for e in K_TREE) == 20
# MST duy nhất (trọng số khác nhau) – kiểm tra vét cạn mọi cây khung
from itertools import combinations


def is_tree(es):
    parent = {v: v for v in V}

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for u, v in es:
        a, b = find(u), find(v)
        if a == b:
            return False
        parent[a] = b
    return True


trees = [es for es in combinations(W, 5) if is_tree(es)]
best = min(sum(W[e] for e in es) for es in trees)
assert len(trees) == 55 and max(sum(W[e] for e in es) for es in trees) == 33
assert 10 ** 8 == 10 ** (10 - 2) and 50 ** 48 > 10 ** 81
assert best == 20 and sum(1 for es in trees if sum(W[e] for e in es) == 20) == 1
# Cut property: S = {A, D}; cây T không chứa DE; đổi AB lấy DE
T_BAD = [("A", "D"), ("A", "B"), ("B", "E"), ("C", "E"), ("C", "F")]
assert is_tree(T_BAD) and sum(W[e] for e in T_BAD) == 23
T_NEW = [e for e in T_BAD if e != ("A", "B")] + [("D", "E")]
assert is_tree(T_NEW) and sum(W[e] for e in T_NEW) == 20
CUT = [e for e in W if (e[0] in "AD") != (e[1] in "AD")]
assert sorted(CUT) == [("A", "B"), ("B", "D"), ("D", "E")]

EDGE_C = "#4a4e57"


class G:
    def __init__(self, scene):
        self.s = scene
        self.vert, self.edge, self.wl = {}, {}, {}
        for v, (x, y) in POS.items():
            c = Circle(radius=0.36, color=WHITE, fill_color=CELL, fill_opacity=1, stroke_width=3).move_to([x, y, 0])
            t = Text(v, font=FONT, font_size=30).move_to(c)
            self.vert[v] = VGroup(c, t)
        for (u, v), w in W.items():
            ln = Line(self.vert[u].get_center(), self.vert[v].get_center(), color=EDGE_C, stroke_width=5)
            lb = Text(str(w), font=FONT, font_size=28, color=WHITE)
            lb.move_to(ln.get_center())
            lb.add_background_rectangle(color=config.background_color, opacity=1, buff=0.06)
            self.edge[(u, v)] = ln
            self.wl[(u, v)] = lb
        self.all = VGroup(*self.edge.values(), *self.wl.values(), *self.vert.values())

    def show(self, rt=1.5):
        self.s.play(LaggedStart(*[GrowFromCenter(v) for v in self.vert.values()], lag_ratio=0.1), run_time=rt * 0.5)
        self.s.play(*[Create(e) for e in self.edge.values()], run_time=rt * 0.4)
        self.s.play(*[FadeIn(l) for l in self.wl.values()], run_time=rt * 0.3)
        # đưa đỉnh lên trên cạnh
        for v in self.vert.values():
            self.s.bring_to_front(v)

    def e(self, u, v):
        return self.edge[key(u, v)]

    def reset(self):
        return [ln.animate.set_stroke(EDGE_C, 5, opacity=1) for ln in self.edge.values()] + \
               [self.vert[v][0].animate.set_fill(CELL, 1).set_stroke(WHITE) for v in V]


def ename(e):
    return f"{e[0]}{e[1]}"


class Mst(Scene):
    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Cây khung nhỏ nhất", 44)
        t1 = Text("MST", font=FONT, font_size=110, color=GOLD).move_to([0, 1.6, 0])
        t2 = para("Nối mọi đỉnh với tổng chi phí nhỏ nhất.\nHai thuật toán tham lam: Kruskal và Prim", 34, y=-0.8)
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. Bài toán =====
        c = swap_cap(self, c, cap("Bài toán", 44, GOLD))
        g = G(self)
        g.show()
        p1 = para("6 thành phố, số trên cạnh là chi phí kéo cáp", 30, WHITE, y=0.0)
        self.play(FadeIn(p1), run_time=0.6)
        self.wait(2.0)
        p2 = para("Cần chọn một tập cạnh sao cho:\n• mọi đỉnh liên thông với nhau\n• tổng chi phí nhỏ nhất", 30, WHITE, y=-2.0)
        self.play(FadeIn(p2), run_time=0.7)
        self.wait(3.0)
        p3 = para("Tập tối ưu không có chu trình (bỏ được một cạnh\ncủa chu trình mà vẫn liên thông), nên nó là cây:\nđúng 6 − 1 = 5 cạnh. Gọi là cây khung nhỏ nhất.", 26, DIM, y=-4.6)
        self.play(FadeIn(p3), run_time=0.7)
        self.wait(5.0)
        self.play(FadeOut(p1), FadeOut(p2), FadeOut(p3), run_time=0.5)

        # ===== 2b. Thử hết? =====
        c = swap_cap(self, c, cap("Thử hết mọi cây khung?", 42, GOLD))
        b1 = para("Đồ thị nhỏ này đã có 55 cây khung,\ntổng chi phí từ 20 đến 33.", 30, WHITE, y=-0.2)
        self.play(FadeIn(b1), run_time=0.7)
        self.wait(3.0)
        b2 = para("Đồ thị đầy đủ n đỉnh có nⁿ⁻² cây khung (Cayley):", 28, DIM, y=-2.0)
        b3 = VGroup(Text("n = 10:   10⁸ = 100 triệu cây", font=FONT, font_size=30),
                    Text("n = 50:   50⁴⁸ > 10⁸¹ cây", font=FONT, font_size=30, color=RED)).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to([0, -3.4, 0])
        self.play(FadeIn(b2), run_time=0.6)
        self.play(LaggedStart(*[FadeIn(m) for m in b3], lag_ratio=0.6), run_time=1.4)
        self.wait(3.0)
        b4 = para("Cần cách chọn cạnh thông minh hơn: tham lam,\nmỗi bước lấy cạnh rẻ nhất mà vẫn an toàn.", 28, GREEN, y=-5.3)
        self.play(FadeIn(b4), run_time=0.7)
        self.wait(3.5)
        self.play(FadeOut(b1), FadeOut(b2), FadeOut(b3), FadeOut(b4), run_time=0.5)

        # ===== 3. Kruskal =====
        c = swap_cap(self, c, cap("Kruskal: cạnh nhẹ trước", 42, GOLD))
        r = para("Xét cạnh theo trọng số tăng dần.\nCạnh nào tạo chu trình thì bỏ.", 30, WHITE, y=0.1)
        self.play(FadeIn(r), run_time=0.6)
        self.wait(2.0)
        order = sorted(W.items(), key=lambda t: t[1])
        items = []
        for i, (e, w) in enumerate(order):
            col, row = (0, i) if i < 5 else (1, i - 5)
            t = Text(f"{ename(e)}  {w}", font=FONT, font_size=30).move_to([-2.4 + col * 3.6, -1.6 - row * 0.62, 0], aligned_edge=LEFT)
            t.align_to([-2.9 + col * 3.6, 0, 0], LEFT)
            items.append(t)
        self.play(LaggedStart(*[FadeIn(t) for t in items], lag_ratio=0.08), run_time=1.2)
        comps = [{v} for v in V]

        def comp_text(cs):
            s = "  ".join("{" + ",".join(sorted(x)) + "}" for x in sorted(cs, key=lambda x: sorted(x)[0]))
            return para(s, 28, BLUE, y=-5.1)
        ct = comp_text(comps)
        ctl = para("Các thành phần (Union–Find):", 24, DIM, y=-4.6)
        tot = para("Tổng: 0", 30, GOLD, y=-5.9)
        self.play(FadeIn(ct), FadeIn(ctl), FadeIn(tot), run_time=0.6)
        self.wait(1.0)
        total = 0
        cur = r
        tree_edges = []
        for i, (e, ok) in enumerate(K_LOG):
            arrow = Text("▶", font=FONT, font_size=24, color=GOLD).next_to(items[i], LEFT, buff=0.15)
            ln = g.e(*e)
            self.play(FadeIn(arrow), ln.animate.set_stroke(GOLD, 9), run_time=0.5)
            if ok:
                total += W[e]
                a = next(x for x in comps if e[0] in x)
                b = next(x for x in comps if e[1] in x)
                comps = [x for x in comps if x is not a and x is not b] + [a | b]
                msg = para(f"{e[0]} và {e[1]} ở hai thành phần khác nhau → lấy", 28, GREEN, y=0.1)
                mark = Text("✓", font=FONT, font_size=30, color=GREEN).next_to(items[i], RIGHT, buff=0.25)
                cur = swap_cap(self, cur, msg, 0.4)
                nct = comp_text(comps)
                self.play(ln.animate.set_stroke(GREEN, 9), FadeIn(mark), ReplacementTransform(ct, nct),
                          Transform(tot, para(f"Tổng: {total}", 30, GOLD, y=-5.9)), run_time=0.7)
                ct = nct
                tree_edges.append(e)
                self.wait(2.4)
            else:
                msg = para(f"{e[0]} và {e[1]} đã cùng thành phần → tạo chu trình, bỏ", 28, RED, y=0.1)
                cur = swap_cap(self, cur, msg, 0.4)
                # tìm đường trong cây giữa hai đầu để tô chu trình
                path = self.tree_path(tree_edges, e[0], e[1])
                self.play(ln.animate.set_stroke(RED, 9), *[g.e(*p).animate.set_stroke(RED, 9) for p in path], run_time=0.6)
                self.wait(2.0)
                mark = Text("✗", font=FONT, font_size=30, color=RED).next_to(items[i], RIGHT, buff=0.25)
                self.play(ln.animate.set_stroke(RED, 4, opacity=0.35), *[g.e(*p).animate.set_stroke(GREEN, 9) for p in path],
                          FadeIn(mark), items[i].animate.set_opacity(0.5), run_time=0.6)
                self.wait(1.0)
            self.play(FadeOut(arrow), run_time=0.2)
        stop = para("Đã đủ 5 cạnh: dừng, khỏi xét EF 9", 28, GOLD, y=0.1)
        cur = swap_cap(self, cur, stop, 0.4)
        self.play(items[8].animate.set_opacity(0.35), run_time=0.4)
        self.wait(2.5)
        res = para("Cây khung nhỏ nhất: DE, AD, BE, CE, CF  –  tổng 20", 28, GREEN, y=0.1)
        cur = swap_cap(self, cur, res, 0.5)
        self.wait(3.0)
        self.play(*[FadeOut(m) for m in items + [cur, ct, ctl, tot]], *[FadeOut(m) for m in self.mobjects if isinstance(m, Text) and m.text in ("✓", "✗")], run_time=0.5)
        self.play(*g.reset(), run_time=0.6)

        # ===== 4. Prim =====
        c = swap_cap(self, c, cap("Prim: lớn dần từ một đỉnh", 42, GOLD))
        r = para("Bắt đầu từ A. Mỗi bước lấy cạnh nhẹ nhất\nđi từ tập S ra ngoài S.", 30, WHITE, y=0.1)
        self.play(FadeIn(r), run_time=0.6)
        self.wait(2.0)
        S = {"A"}
        self.play(g.vert["A"][0].animate.set_fill(BLUE, 0.4), run_time=0.5)
        st = para("S = {A}", 32, BLUE, y=-1.4)
        tot = para("Tổng: 0", 30, GOLD, y=-5.6)
        self.play(FadeIn(st), FadeIn(tot), run_time=0.5)
        total = 0
        cur = r
        cl = None
        for cand, e in P_LOG:
            s = "Cạnh ra khỏi S: " + ", ".join(f"{ename(x)} {W[x]}" for x in sorted(cand, key=lambda x: W[x]))
            ncl = para(s, 28, WHITE, y=-2.6)
            self.play(*[g.e(*x).animate.set_stroke(GOLD, 8) for x in cand],
                      (ReplacementTransform(cl, ncl) if cl else FadeIn(ncl)), run_time=0.7)
            cl = ncl
            self.wait(2.2)
            nv = e[0] if e[1] in S else e[1]
            total += W[e]
            msg = para(f"Nhẹ nhất: {ename(e)} ({W[e]}) → thêm đỉnh {nv} vào S", 28, GREEN, y=0.1)
            cur = swap_cap(self, cur, msg, 0.4)
            S.add(nv)
            others = [x for x in cand if x != e]
            # cạnh có cả hai đầu trong S không bao giờ được chọn nữa
            inner = [x for x in W if x[0] in S and x[1] in S and x not in P_TREE]
            self.play(g.e(*e).animate.set_stroke(GREEN, 9), g.vert[nv][0].animate.set_fill(BLUE, 0.4),
                      *[g.e(*x).animate.set_stroke(EDGE_C, 5) for x in others if x not in inner],
                      *[g.e(*x).animate.set_stroke(RED, 4, opacity=0.35) for x in inner],
                      Transform(st, para("S = {" + ", ".join(sorted(S)) + "}", 32, BLUE, y=-1.4)),
                      Transform(tot, para(f"Tổng: {total}", 30, GOLD, y=-5.6)), run_time=0.8)
            self.wait(2.6)
        same = para("Cùng 5 cạnh, cùng tổng 20 như Kruskal", 30, GREEN, y=-3.9)
        self.play(FadeOut(cl), FadeIn(same), run_time=0.6)
        self.wait(2.0)
        note = para("Thứ tự chọn khác nhau: Prim lấy AD trước DE.\nTrọng số khác nhau đôi một thì MST là duy nhất.", 26, DIM, y=-4.8)
        self.play(FadeIn(note), run_time=0.6)
        self.wait(4.0)
        self.play(*[FadeOut(m) for m in [cur, st, tot, same, note]], run_time=0.5)
        self.play(*g.reset(), run_time=0.6)

        # ===== 5. Tính chất lát cắt =====
        c = swap_cap(self, c, cap("Vì sao tham lam lại đúng?", 42, GOLD))
        r = para("Tính chất lát cắt: chia đỉnh thành S và phần còn lại.\nCạnh nhẹ nhất băng qua lát cắt luôn nằm trong MST.", 26, WHITE, y=0.1)
        self.play(FadeIn(r), run_time=0.7)
        self.wait(2.0)
        blob = Ellipse(width=2.0, height=4.4, color=BLUE, fill_color=BLUE, fill_opacity=0.12, stroke_width=3).move_to([-2.8, 2.8, 0]).rotate(-0.12)
        sl = Text("S", font=FONT, font_size=34, color=BLUE).move_to([-3.9, 5.0, 0])
        self.play(FadeIn(blob), FadeIn(sl), run_time=0.6)
        self.play(*[g.e(*x).animate.set_stroke(GOLD, 8) for x in CUT], run_time=0.6)
        cl = para("Cạnh băng qua: AB 4, BD 5, DE 1. Nhẹ nhất: DE", 28, GOLD, y=-1.3)
        self.play(FadeIn(cl), run_time=0.6)
        self.play(g.e("D", "E").animate.set_stroke(GREEN, 10), run_time=0.5)
        self.wait(2.5)
        self.play(*[g.e(*x).animate.set_stroke(EDGE_C, 5) for x in CUT if x != ("D", "E")], g.e("D", "E").animate.set_stroke(EDGE_C, 5), run_time=0.4)
        # phản chứng bằng phép đổi cạnh
        q = para("Giả sử có cây T không chứa DE, tổng 23:", 28, WHITE, y=-1.3)
        self.play(ReplacementTransform(cl, q), *[g.e(*x).animate.set_stroke(BLUE, 8) for x in T_BAD], run_time=0.8)
        self.wait(2.0)
        q2 = para("Thêm DE vào T thì có chu trình D–E–B–A–D.\nChu trình đi ra khỏi S rồi phải quay lại,\nnên còn một cạnh khác băng qua lát cắt: AB.", 26, WHITE, y=-3.0)
        self.play(g.e("D", "E").animate.set_stroke(GREEN, 9), FadeIn(q2), run_time=0.7)
        self.play(*[Indicate(g.e(*x), color=RED, scale_factor=1.0) for x in [("D", "E"), ("B", "E"), ("A", "B"), ("A", "D")]], run_time=1.2)
        self.wait(2.5)
        q3 = para("Bỏ AB (4), giữ DE (1): vẫn là cây khung,\ntổng giảm từ 23 xuống 20.", 28, GREEN, y=-5.2)
        self.play(g.e("A", "B").animate.set_stroke(RED, 4, opacity=0.35), FadeIn(q3), run_time=0.7)
        self.play(*[g.e(*x).animate.set_stroke(GREEN, 9) for x in T_NEW], run_time=0.6)
        self.wait(3.5)
        self.play(FadeOut(q), FadeOut(q2), FadeOut(q3), FadeOut(blob), FadeOut(sl), run_time=0.5)
        k = para("Kruskal: cạnh nối hai thành phần khác nhau là cạnh\nnhẹ nhất ra khỏi một thành phần → an toàn.\nPrim: cạnh nhẹ nhất ra khỏi S → an toàn.", 26, WHITE, y=-2.4)
        self.play(FadeIn(k), run_time=0.7)
        self.wait(5.0)
        wipe(self, keep=[c])

        # ===== 6. So sánh =====
        c = swap_cap(self, c, cap("Kruskal hay Prim?", 44, GOLD))

        def col(title, color, lines):
            t = Text(title, font=FONT, font_size=42, color=color)
            b = VGroup(*[Text(s, font=FONT, font_size=28) for s in lines]).arrange(DOWN, buff=0.28)
            return VGroup(t, b).arrange(DOWN, buff=0.4)
        kr = col("Kruskal", GREEN, ["Sắp xếp mọi cạnh, duyệt tăng dần", "Union–Find để phát hiện chu trình", "O(E log E)", "Hợp với đồ thị thưa"]).move_to([0, 3.4, 0])
        pr = col("Prim", BLUE, ["Mở rộng tập S từ một đỉnh", "Hàng đợi ưu tiên cho cạnh ra khỏi S", "O(E log V) với binary heap", "Hợp với đồ thị dày"]).move_to([0, -1.2, 0])
        self.play(FadeIn(kr), run_time=0.8)
        self.wait(2.5)
        self.play(FadeIn(pr), run_time=0.8)
        self.wait(2.5)
        end = para("Cả hai cho cùng một tổng nhỏ nhất.\nĐừng nhầm với đường đi ngắn nhất (Dijkstra).", 28, DIM, y=-4.9)
        self.play(FadeIn(end), run_time=0.7)
        self.wait(5.0)

    @staticmethod
    def tree_path(tree, a, b):
        adj = {}
        for u, v in tree:
            adj.setdefault(u, []).append(v)
            adj.setdefault(v, []).append(u)
        prev = {a: None}
        st = [a]
        while st:
            x = st.pop()
            for y in adj.get(x, []):
                if y not in prev:
                    prev[y] = x
                    st.append(y)
        path, x = [], b
        while prev.get(x) is not None:
            path.append((prev[x], x))
            x = prev[x]
        return path
