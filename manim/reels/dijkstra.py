from common import *
import heapq

INF = float("inf")

# ---------- Đồ thị có hướng và vết Dijkstra (kiểm tra bằng code) ----------
POS = {"s": (-2.95, 3.2), "A": (-1.0, 4.9), "B": (-1.0, 1.5),
       "C": (1.3, 4.9), "D": (1.3, 1.5), "E": (3.05, 3.2)}
W = {("s", "A"): 4, ("s", "B"): 1, ("B", "A"): 2, ("A", "C"): 1, ("B", "C"): 5,
     ("B", "D"): 8, ("C", "D"): 3, ("C", "E"): 6, ("D", "E"): 1}
DOFF = {"s": LEFT * 0.85, "A": UP * 0.62, "C": UP * 0.62, "B": DOWN * 0.62, "D": DOWN * 0.62, "E": RIGHT * 0.85}


def dijkstra(W, src, verts, allow_reopen=False):
    """Trả về (dist, parent, log). log: list các bước (u, d_u, [(v, old, new, improved, closed)], pq_after)."""
    adj = {v: [] for v in verts}
    for (u, v), w in W.items():
        adj[u].append((v, w))
    dist = {v: INF for v in verts}
    par = {v: None for v in verts}
    dist[src] = 0
    done = set()
    log = []
    while len(done) < len(verts):
        cand = [(dist[v], v) for v in verts if v not in done and dist[v] < INF]
        if not cand:
            break
        du, u = min(cand)
        done.add(u)
        rel = []
        for v, w in sorted(adj[u]):
            old = dist[v]
            closed = v in done
            imp = du + w < old and not closed
            if imp:
                dist[v] = du + w
                par[v] = u
            rel.append((v, old, du + w, imp, closed))
        pq = sorted((dist[v], v) for v in verts if v not in done and dist[v] < INF)
        log.append((u, du, rel, pq))
    return dist, par, log


def bellman_ford(W, src, verts):
    dist = {v: INF for v in verts}
    dist[src] = 0
    for _ in range(len(verts) - 1):
        for (u, v), w in W.items():
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist


VERTS = list(POS)
DIST, PAR, LOG = dijkstra(W, "s", VERTS)
assert [u for u, *_ in LOG] == ["s", "B", "A", "C", "D", "E"]
assert DIST == {"s": 0, "A": 3, "B": 1, "C": 4, "D": 7, "E": 8}
assert PAR == {"s": None, "A": "B", "B": "s", "C": "A", "D": "C", "E": "D"}
assert DIST == bellman_ford(W, "s", VERTS)
assert LOG[1][3] == [(3, "A"), (6, "C"), (9, "D")]
# đường "ít cạnh" s→B→D→E = 10 > 8
assert W[("s", "B")] + W[("B", "D")] + W[("D", "E")] == 10

# Đồ thị có cạnh âm
NPOS = {"s": (-2.8, 3.2), "A": (0.4, 4.9), "B": (0.4, 1.5), "C": (3.2, 4.9)}
NW = {("s", "A"): 2, ("s", "B"): 3, ("B", "A"): -2, ("A", "C"): 1}
NV = list(NPOS)
ND, _, NLOG = dijkstra(NW, "s", NV)
NB = bellman_ford(NW, "s", NV)
assert [u for u, *_ in NLOG] == ["s", "A", "B", "C"]
assert ND == {"s": 0, "A": 2, "B": 3, "C": 3} and NB == {"s": 0, "A": 1, "B": 3, "C": 2}
NDOFF = {"s": LEFT * 0.85, "A": UP * 0.62, "C": UP * 0.62, "B": DOWN * 0.62}

EDGE_C = "#5a5f69"


def dstr(x):
    return "∞" if x == INF else str(x)


class DG:
    def __init__(self, scene, pos, w, doff):
        self.s, self.pos, self.w, self.doff = scene, pos, w, doff
        self.vert, self.edge, self.wl, self.dl = {}, {}, {}, {}
        for v, (x, y) in pos.items():
            c = Circle(radius=0.38, color=WHITE, fill_color=CELL, fill_opacity=1, stroke_width=3).move_to([x, y, 0])
            t = Text(v, font=FONT, font_size=30).move_to(c)
            self.vert[v] = VGroup(c, t)
        for (u, v), ww in w.items():
            a = Arrow(self.vert[u].get_center(), self.vert[v].get_center(), buff=0.42, color=EDGE_C, stroke_width=5,
                      tip_length=0.24, max_tip_length_to_length_ratio=0.25, max_stroke_width_to_length_ratio=10)
            lb = Text(str(ww), font=FONT, font_size=28, color=RED if ww < 0 else WHITE)
            lb.move_to(a.get_center())
            lb.add_background_rectangle(color=config.background_color, opacity=1, buff=0.06)
            self.edge[(u, v)] = a
            self.wl[(u, v)] = lb

    def dlabel(self, v, val, color=GOLD):
        t = Text(dstr(val), font=FONT, font_size=30, color=color)
        t.move_to(self.vert[v].get_center() + self.doff[v])
        return t

    def show(self, src):
        self.s.play(LaggedStart(*[GrowFromCenter(v) for v in self.vert.values()], lag_ratio=0.1), run_time=0.8)
        self.s.play(*[GrowArrow(e) for e in self.edge.values()], run_time=0.8)
        self.s.play(*[FadeIn(l) for l in self.wl.values()], run_time=0.4)

    def show_d(self, src):
        for v in self.pos:
            self.dl[v] = self.dlabel(v, 0 if v == src else INF, GOLD if v == src else DIM)
        self.s.play(*[FadeIn(l) for l in self.dl.values()], run_time=0.6)

    def set_d(self, v, val, color=GOLD):
        n = self.dlabel(v, val, color)
        an = Transform(self.dl[v], n)
        return an


def pq_group(pq, y=-1.9):
    if not pq:
        return para("(rỗng)", 28, DIM, y=y)
    boxes = []
    for i, (d, v) in enumerate(pq):
        t = Text(f"{v} : {d}", font=FONT, font_size=30, color=GOLD if i == 0 else WHITE)
        b = SurroundingRectangle(t, buff=0.16, corner_radius=0.12, color=GOLD if i == 0 else DIM, stroke_width=3)
        boxes.append(VGroup(b, t))
    g = VGroup(*boxes).arrange(RIGHT, buff=0.25).move_to([0, y, 0])
    if g.width > 7.8:
        g.scale_to_fit_width(7.8)
    return g


class Dijkstra(Scene):
    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Đường đi ngắn nhất", 44)
        t1 = Text("Dijkstra", font=FONT, font_size=96, color=GOLD).move_to([0, 1.4, 0])
        t2 = para("Từ một đỉnh nguồn đến mọi đỉnh,\nkhi mọi trọng số đều không âm", 34, y=-0.8)
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. Bài toán =====
        c = swap_cap(self, c, cap("Bài toán", 44, GOLD))
        g = DG(self, POS, W, DOFF)
        g.show("s")
        p1 = para("Đồ thị có hướng, số trên cạnh là độ dài.\nTìm đường ngắn nhất từ s đến mọi đỉnh.", 30, WHITE, y=-0.3)
        self.play(FadeIn(p1), run_time=0.6)
        self.wait(2.5)
        path = [("s", "B"), ("B", "D"), ("D", "E")]
        self.play(*[g.edge[e].animate.set_color(BLUE) for e in path], run_time=0.6)
        p2 = para("s → B → D → E: chỉ 3 cạnh, dài 1 + 8 + 1 = 10", 28, BLUE, y=-2.0)
        self.play(FadeIn(p2), run_time=0.6)
        self.wait(2.5)
        p3 = para("Liệu có đường dài hơn về số cạnh\nnhưng ngắn hơn về tổng độ dài?", 28, DIM, y=-3.6)
        self.play(FadeIn(p3), run_time=0.6)
        self.wait(2.5)
        self.play(*[g.edge[e].animate.set_color(EDGE_C) for e in path], FadeOut(p1), FadeOut(p2), FadeOut(p3), run_time=0.5)

        # ===== 3. Ý tưởng =====
        c = swap_cap(self, c, cap("Hai thao tác", 44, GOLD))
        g.show_d("s")
        i1 = para("d[v]: độ dài đường tốt nhất tìm được tới v.\nBan đầu d[s] = 0, các đỉnh khác ∞.", 28, WHITE, y=-0.3)
        self.play(FadeIn(i1), run_time=0.6)
        self.wait(3.0)
        i2 = para("Relax cạnh u → v:", 30, BLUE, y=-1.8)
        i3 = para("nếu d[u] + w(u,v) < d[v]  thì  d[v] ← d[u] + w(u,v)", 28, WHITE, y=-2.5)
        self.play(FadeIn(i2), FadeIn(i3), run_time=0.7)
        self.wait(3.0)
        i4 = para("Chốt: lấy đỉnh chưa chốt có d nhỏ nhất.\nTừ lúc đó d của nó không đổi nữa.", 28, GREEN, y=-3.9)
        self.play(FadeIn(i4), run_time=0.7)
        self.wait(3.0)
        i5 = para("Các đỉnh chờ nằm trong hàng đợi ưu tiên theo d.", 26, DIM, y=-5.2)
        self.play(FadeIn(i5), run_time=0.6)
        self.wait(2.5)
        self.play(FadeOut(i1), FadeOut(i2), FadeOut(i3), FadeOut(i4), FadeOut(i5), run_time=0.5)

        # ===== 4. Chạy từng bước =====
        c = swap_cap(self, c, cap("Chạy Dijkstra từ s", 42, GOLD))
        pql = para("Hàng đợi ưu tiên (đỉnh : d)", 24, DIM, y=-1.25)
        pq = pq_group([(0, "s")])
        donel = para("Đã chốt: (chưa có)", 28, GREEN, y=-3.0)
        rule = para("Relax: d[v] ← min(d[v], d[u] + w)", 26, DIM, y=-5.9)
        self.play(FadeIn(pql), FadeIn(pq), FadeIn(donel), FadeIn(rule), run_time=0.6)
        status = para("Bắt đầu: chỉ có s trong hàng đợi", 28, WHITE, y=-0.3)
        self.play(FadeIn(status), run_time=0.5)
        self.wait(1.5)
        done = []
        prev_pq = [(0, "s")]
        for (u, du, rel, pqa) in LOG:
            assert prev_pq[0] == (du, u)
            msg = para(f"Lấy {u} (d = {du}) ra khỏi hàng đợi và chốt", 28, GREEN, y=-0.3)
            status = swap_cap(self, status, msg, 0.4)
            done.append(u)
            ndone = para("Đã chốt: " + ", ".join(done), 28, GREEN, y=-3.0)
            npq0 = pq_group(prev_pq[1:])
            self.play(g.vert[u][0].animate.set_fill(GREEN, 0.45).set_stroke(GREEN),
                      g.set_d(u, du, GREEN), Transform(donel, ndone), ReplacementTransform(pq, npq0), run_time=0.6)
            pq = npq0
            prev_pq = pqa
            self.wait(1.2)
            if not rel:
                msg = para(f"{u} không có cạnh đi ra", 28, DIM, y=-0.3)
                status = swap_cap(self, status, msg, 0.4)
                self.wait(1.0)
            for v, old, new, imp, closed in rel:
                e = g.edge[(u, v)]
                calc = para(f"{u} → {v}:  {du} + {W[(u, v)]} = {new}  so với d[{v}] = {dstr(old)}", 28, WHITE, y=-4.4)
                self.play(e.animate.set_color(GOLD), FadeIn(calc), run_time=0.5)
                self.wait(1.4)
                if imp:
                    res = para(f"{new} < {dstr(old)}  →  cập nhật d[{v}] = {new}", 28, GOLD, y=-4.4)
                    self.play(ReplacementTransform(calc, res), g.set_d(v, new, GOLD), run_time=0.6)
                    self.wait(1.3)
                    self.play(FadeOut(res), e.animate.set_color(EDGE_C), run_time=0.3)
                else:
                    res = para(f"Không nhỏ hơn → giữ nguyên", 28, DIM, y=-4.4)
                    self.play(ReplacementTransform(calc, res), run_time=0.5)
                    self.wait(1.0)
                    self.play(FadeOut(res), e.animate.set_color(EDGE_C), run_time=0.3)
            npq = pq_group(pqa)
            self.play(ReplacementTransform(pq, npq), run_time=0.6)
            pq = npq
            self.wait(1.2)
        fin = para("Hàng đợi rỗng: xong", 30, GREEN, y=-0.3)
        status = swap_cap(self, status, fin, 0.4)
        self.wait(2.0)
        self.play(FadeOut(pql), FadeOut(pq), FadeOut(rule), run_time=0.4)

        # ===== 5. Cây đường đi ngắn nhất =====
        c = swap_cap(self, c, cap("Cây đường đi ngắn nhất", 42, GOLD))
        tree = [(PAR[v], v) for v in VERTS if PAR[v]]
        self.play(*[g.edge[e].animate.set_color(GREEN).set_stroke(width=8) for e in tree],
                  *[g.edge[e].animate.set_opacity(0.25) for e in W if e not in tree],
                  *[g.wl[e].animate.set_opacity(0.3) for e in W if e not in tree], run_time=0.8)
        t1 = para("Mỗi đỉnh nhớ cạnh cuối cùng làm d của nó giảm\n(đỉnh cha). Các cạnh đó tạo thành một cây.", 28, WHITE, y=-0.3)
        self.play(ReplacementTransform(status, t1), run_time=0.6)
        self.wait(3.0)
        pe = para("Tới E:  s → B → A → C → D → E\n1 + 2 + 1 + 3 + 1 = 8", 30, GOLD, y=-4.4)
        self.play(FadeOut(donel), FadeIn(pe), run_time=0.6)
        self.wait(2.0)
        cmp = para("5 cạnh nhưng ngắn hơn đường 3 cạnh (dài 10)", 28, DIM, y=-5.8)
        self.play(FadeIn(cmp), run_time=0.6)
        self.wait(3.5)
        self.play(FadeOut(pe), FadeOut(cmp), FadeOut(t1), run_time=0.4)

        # ===== 6. Vì sao đúng =====
        c = swap_cap(self, c, cap("Vì sao chốt là đúng?", 42, GOLD))
        w1 = para("Khi chốt u, d[u] nhỏ nhất trong các đỉnh đang chờ.", 28, WHITE, y=-0.4)
        w2 = para("Một đường khác tới u phải rời tập đã chốt qua\nmột đỉnh đang chờ x, với d[x] ≥ d[u].", 28, WHITE, y=-1.9)
        w3 = para("Đi tiếp từ x tới u chỉ cộng thêm cạnh ≥ 0,\nnên không thể ngắn hơn d[u].", 28, WHITE, y=-3.6)
        w4 = para("Điểm mấu chốt: mọi trọng số không âm", 30, GOLD, y=-5.2)
        for m in [w1, w2, w3, w4]:
            self.play(FadeIn(m), run_time=0.6)
            self.wait(2.5)
        self.wait(1.5)
        wipe(self, keep=[c])

        # ===== 7. Cạnh âm =====
        c = swap_cap(self, c, cap("Khi có cạnh âm", 44, RED))
        ng = DG(self, NPOS, NW, NDOFF)
        ng.show("s")
        ng.show_d("s")
        st = para("Cạnh B → A có trọng số −2", 30, RED, y=-0.3)
        self.play(FadeIn(st), run_time=0.5)
        self.wait(1.5)
        for (u, du, rel, pqa) in NLOG:
            msg = para(f"Chốt {u} với d = {du}", 28, GREEN, y=-0.3)
            st = swap_cap(self, st, msg, 0.4)
            self.play(ng.vert[u][0].animate.set_fill(GREEN, 0.45).set_stroke(GREEN), ng.set_d(u, du, GREEN), run_time=0.5)
            self.wait(1.0)
            for v, old, new, imp, closed in rel:
                e = ng.edge[(u, v)]
                if imp:
                    calc = para(f"{u} → {v}:  d[{v}] = {new}", 28, GOLD, y=-1.6)
                    self.play(e.animate.set_color(GOLD), FadeIn(calc), ng.set_d(v, new, GOLD), run_time=0.6)
                    self.wait(1.2)
                    self.play(FadeOut(calc), e.animate.set_color(EDGE_C), run_time=0.3)
                elif closed:
                    calc = para(f"{u} → {v}:  {du} + ({NW[(u, v)]}) = {new} < {old}\nnhưng {v} đã chốt, không được sửa!", 28, RED, y=-1.9)
                    self.play(e.animate.set_color(RED), FadeIn(calc), run_time=0.6)
                    self.wait(3.0)
                    self.play(FadeOut(calc), run_time=0.3)
        res = para("Dijkstra cho:   d[A] = 2,   d[C] = 3", 30, GOLD, y=-1.8)
        tru = para("Đúng ra:   s → B → A = 3 − 2 = 1,   d[C] = 2", 30, GREEN, y=-2.7)
        self.play(FadeIn(res), run_time=0.6)
        self.wait(1.5)
        self.play(FadeIn(tru), run_time=0.6)
        self.wait(2.5)
        ex = para("A bị chốt quá sớm. Cạnh âm làm một đường\nđi vòng sau này lại rẻ hơn, phá điểm mấu chốt.", 28, WHITE, y=-4.2)
        self.play(FadeIn(ex), run_time=0.6)
        self.wait(3.0)
        bf = para("Có cạnh âm: dùng Bellman–Ford, O(VE),\nphát hiện được cả chu trình âm.", 28, BLUE, y=-5.7)
        self.play(FadeIn(bf), run_time=0.6)
        self.wait(4.0)
        wipe(self, keep=[c])

        # ===== 8. Tổng kết =====
        c = swap_cap(self, c, cap("Tóm tắt", 44, GOLD))
        sm = VGroup(*[Text(s, font=FONT, font_size=30, color=col) for s, col in [
            ("1. d[s] = 0, các đỉnh khác ∞", WHITE),
            ("2. Lấy đỉnh có d nhỏ nhất ra và chốt", GREEN),
            ("3. Relax mọi cạnh đi ra từ đỉnh đó", BLUE),
            ("4. Lặp đến khi hàng đợi rỗng", WHITE),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.45).move_to([0, 3.0, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.2) for m in sm], lag_ratio=0.5), run_time=2.4)
        self.wait(2.0)
        cx = para("Binary heap: O((V + E) log V)", 30, GOLD, y=-0.2)
        ap = para("Dùng trong định tuyến mạng, bản đồ, game.\nChỉ đúng khi mọi trọng số ≥ 0.", 28, DIM, y=-1.8)
        self.play(FadeIn(cx), run_time=0.6)
        self.wait(1.5)
        self.play(FadeIn(ap), run_time=0.6)
        self.wait(5.0)
