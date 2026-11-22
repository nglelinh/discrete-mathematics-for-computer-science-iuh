from common import *
from collections import deque

# ---------- Đồ thị & thuật toán ----------
EDGES = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "E"), ("C", "F"), ("D", "G")]
V = "ABCDEFG"
ADJ = {v: sorted([b for a, b in EDGES if a == v] + [a for a, b in EDGES if b == v]) for v in V}
POS = {"A": (0, 4.6), "B": (-1.8, 3.3), "C": (1.8, 3.3), "D": (-2.8, 1.8), "E": (0, 1.8), "F": (2.8, 1.8), "G": (-2.8, 0.3)}


def bfs(s):
    dist, par, order, ev = {s: 0}, {}, [], []
    q = deque([s])
    ev.append(("push", s, list(q)))
    while q:
        u = q.popleft()
        order.append(u)
        ev.append(("pop", u, list(q)))
        for w in ADJ[u]:
            if w not in dist:
                dist[w], par[w] = dist[u] + 1, u
                q.append(w)
                ev.append(("push", w, list(q)))
    return order, dist, par, ev


BO, BDIST, BPAR, BEV = bfs("A")
assert "".join(BO) == "ABCDEFG"
assert BDIST == {"A": 0, "B": 1, "C": 1, "D": 2, "E": 2, "F": 2, "G": 3}
BTREE = {frozenset((v, p)) for v, p in BPAR.items()}
assert BTREE == {frozenset(e) for e in ["AB", "AC", "BD", "BE", "CF", "DG"]}
assert {frozenset(e) for e in EDGES} - BTREE == {frozenset("CE")}

DO, DPAR, DEV, BACK = [], {}, [], []


def dfs(u, p=None):
    DO.append(u)
    DEV.append(("push", u))
    for w in ADJ[u]:
        if w not in DO:
            DPAR[w] = u
            dfs(w, u)
        elif w != p and (w, u) not in BACK and (u, w) not in BACK:
            BACK.append((u, w))
    DEV.append(("pop", u))


dfs("A")
assert "".join(DO) == "ABDGECF"
DTREE = {frozenset((v, p)) for v, p in DPAR.items()}
assert DTREE == {frozenset(e) for e in ["AB", "BD", "DG", "BE", "EC", "CF"]}
assert BACK == [("C", "A")]
# chu trình: đi từ C ngược cha về A
cyc = ["C"]
while cyc[-1] != "A":
    cyc.append(DPAR[cyc[-1]])
assert cyc == ["C", "E", "B", "A"]
# đường ngắn nhất A → G theo cây BFS
path = ["G"]
while path[-1] != "A":
    path.append(BPAR[path[-1]])
assert path[::-1] == ["A", "B", "D", "G"]
def stack_order(s):
    st, vis, order = [s], {s}, []
    while st:
        u = st.pop()
        order.append(u)
        for w in ADJ[u]:
            if w not in vis:
                vis.add(w)
                st.append(w)
    return "".join(order)


assert stack_order("A") == "ACFEBDG"
# thành phần liên thông
EX = EDGES + [("H", "I"), ("I", "J")]
VX = "ABCDEFGHIJK"
AX = {v: [b for a, b in EX if a == v] + [a for a, b in EX if b == v] for v in VX}
seen, comps = set(), []
for v in VX:
    if v not in seen:
        comp, st = [], [v]
        seen.add(v)
        while st:
            u = st.pop()
            comp.append(u)
            for w in AX[u]:
                if w not in seen:
                    seen.add(w)
                    st.append(w)
        comps.append(sorted(comp))
assert comps == [list("ABCDEFG"), list("HIJ"), ["K"]]


def key(a, b):
    return frozenset((a, b))


class BfsDfs(Scene):
    def wait(self, duration=1.0, **kw):
        super().wait(duration * 2.0, **kw)

    def graph(self, pos=POS, edges=EDGES, scale=1.0, shift=(0, 0), r=0.36):
        nodes, lines = {}, {}
        sh = np.array([shift[0], shift[1], 0])
        for v, (x, y) in pos.items():
            c_ = Circle(radius=r * scale, color=WHITE, stroke_width=3, fill_color=CELL, fill_opacity=1).move_to(np.array([x * scale, y * scale, 0]) + sh)
            t = Text(v, font=FONT, font_size=int(28 * scale + 2), color=WHITE).move_to(c_)
            nodes[v] = VGroup(c_, t).set_z_index(2)
        for a, b in edges:
            lines[key(a, b)] = Line(nodes[a].get_center(), nodes[b].get_center(), color=DIM, stroke_width=3)
        return nodes, lines

    def panel(self, items, y, col, label):
        g = VGroup()
        lab = Text(label, font=FONT, font_size=22, color=col).move_to([-3.95, y + 0.6, 0], aligned_edge=LEFT)
        g.add(lab)
        for i, v in enumerate(items):
            b = Square(0.62, color=col, stroke_width=3).move_to([-3.6 + i * 0.72, y, 0])
            g.add(VGroup(b, Text(v, font=FONT, font_size=26, color=WHITE).move_to(b)))
        return g

    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Duyệt đồ thị", 44)
        t1 = Text("BFS\nvs DFS", font=FONT, font_size=90, color=GOLD, line_spacing=1.0).move_to([0, 2.0, 0])
        t2 = para("Cùng một đồ thị, hai cách đi:\nhàng đợi (queue) và ngăn xếp (stack)", 30, y=-1.0)
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. BFS =====
        c = swap_cap(self, c, cap("BFS: duyệt theo bề rộng", 42, BLUE))
        nodes, lines = self.graph()
        self.play(*[Create(l) for l in lines.values()], *[FadeIn(n) for n in nodes.values()], run_time=1.0)
        n0 = para("Xét láng giềng theo thứ tự chữ cái. Bắt đầu từ A", 24, DIM, y=-0.3)
        self.play(FadeIn(n0), run_time=0.5)
        self.wait(1.0)
        qp = self.panel([], -1.5, BLUE, "Hàng đợi: vào ở cuối, lấy ra ở đầu")
        self.play(FadeIn(qp), run_time=0.4)
        olab = Text("Thứ tự thăm:", font=FONT, font_size=24, color=GOLD).move_to([-3.95, -2.9, 0], aligned_edge=LEFT)
        self.play(FadeIn(olab), FadeOut(n0), run_time=0.4)
        order = VGroup()
        dl = {}
        for kind, v, q in BEV:
            self.remove(qp)
            qp = self.panel(q, -1.5, BLUE, "Hàng đợi: vào ở cuối, lấy ra ở đầu")
            self.add(qp)
            anims = []
            if kind == "push":
                anims.append(nodes[v][0].animate.set_fill(BLUE, 0.5))
                if v in BPAR:
                    anims.append(lines[key(v, BPAR[v])].animate.set_color(BLUE).set_stroke(width=6))
                d = Text(str(BDIST[v]), font=FONT, font_size=22, color=GOLD).next_to(nodes[v], UR, buff=0.02)
                dl[v] = d
                anims.append(FadeIn(d))
            else:
                anims.append(nodes[v][0].animate.set_fill(GOLD, 0.8))
                t = Text(v, font=FONT, font_size=30, color=GOLD).move_to([-1.4 + len(order) * 0.62, -2.9, 0])
                order.add(t)
                anims.append(FadeIn(t, shift=DOWN * 0.2))
            self.play(*anims, run_time=0.8)
        self.wait(1.0)
        b1 = para("Thăm theo từng lớp: khoảng cách 0 → 1 → 2 → 3\n(số vàng = số cạnh ít nhất từ A)", 24, WHITE, y=-4.1)
        self.play(FadeIn(b1), run_time=0.5)
        self.wait(2.0)
        self.play(lines[key("C", "E")].animate.set_color(RED), run_time=0.4)
        b2 = para("Cạnh C–E không thuộc cây BFS: E đã được B thêm vào trước", 22, RED, y=-5.2)
        self.play(FadeIn(b2), run_time=0.5)
        self.wait(2.5)
        wipe(self, keep=[c])

        # ===== 3. Đường đi ngắn nhất =====
        c = swap_cap(self, c, cap("Cây BFS = đường đi ngắn nhất", 40, BLUE))
        nodes, lines = self.graph()
        for k_, l in lines.items():
            if k_ in BTREE:
                l.set_color(BLUE).set_stroke(width=5)
        self.play(*[Create(l) for l in lines.values()], *[FadeIn(n) for n in nodes.values()], run_time=0.8)
        lv = VGroup(*[Text(f"lớp {d}", font=FONT, font_size=22, color=DIM).move_to([3.4, y, 0]) for d, y in ((0, 4.6), (1, 3.3), (2, 1.8), (3, 0.3))])
        self.play(FadeIn(lv), run_time=0.5)
        s1 = para("Muốn đi từ A đến G: lần ngược theo cha trong cây BFS", 24, WHITE, y=-0.8)
        self.play(FadeIn(s1), run_time=0.5)
        self.wait(1.0)
        for a, b in [("G", "D"), ("D", "B"), ("B", "A")]:
            self.play(lines[key(a, b)].animate.set_color(GOLD).set_stroke(width=8), nodes[a][0].animate.set_fill(GOLD, 0.7), nodes[b][0].animate.set_fill(GOLD, 0.7), run_time=0.6)
        s2 = para("A → B → D → G: 3 cạnh, đúng bằng khoảng cách của G", 26, GOLD, y=-1.9)
        self.play(FadeIn(s2), run_time=0.5)
        self.wait(2.0)
        s3 = para("Vì BFS xong hết lớp d rồi mới sang lớp d + 1, đỉnh nào\ncũng được chạm tới lần đầu bằng đường ngắn nhất", 24, WHITE, y=-3.2)
        self.play(FadeIn(s3), run_time=0.5)
        self.wait(2.5)
        s4 = para("Chỉ đúng khi mọi cạnh có cùng trọng số.\nCó trọng số: dùng Dijkstra.", 24, DIM, y=-4.8)
        self.play(FadeIn(s4), run_time=0.5)
        self.wait(2.5)
        wipe(self, keep=[c])

        # ===== 4. DFS =====
        c = swap_cap(self, c, cap("DFS: duyệt theo chiều sâu", 42, GREEN))
        nodes, lines = self.graph()
        self.play(*[Create(l) for l in lines.values()], *[FadeIn(n) for n in nodes.values()], run_time=1.0)
        n0 = para("Đi sâu nhất có thể, hết đường thì quay lui", 24, DIM, y=-0.3)
        self.play(FadeIn(n0), run_time=0.5)
        sp = self.panel([], -1.5, GREEN, "Ngăn xếp (lời gọi đệ quy): vào và ra ở đỉnh")
        self.play(FadeIn(sp), run_time=0.4)
        olab = Text("Thứ tự thăm:", font=FONT, font_size=24, color=GOLD).move_to([-3.95, -2.9, 0], aligned_edge=LEFT)
        self.play(FadeIn(olab), FadeOut(n0), run_time=0.4)
        stack, order = [], VGroup()
        for kind, v in DEV:
            anims = []
            if kind == "push":
                stack.append(v)
                anims.append(nodes[v][0].animate.set_fill(GREEN, 0.6))
                if v in DPAR:
                    anims.append(lines[key(v, DPAR[v])].animate.set_color(GREEN).set_stroke(width=6))
                t = Text(v, font=FONT, font_size=30, color=GOLD).move_to([-1.4 + len(order) * 0.62, -2.9, 0])
                order.add(t)
                anims.append(FadeIn(t, shift=DOWN * 0.2))
            else:
                stack.pop()
                anims.append(nodes[v][0].animate.set_fill(GOLD, 0.8))
            self.remove(sp)
            sp = self.panel(stack, -1.5, GREEN, "Ngăn xếp (lời gọi đệ quy): vào và ra ở đỉnh")
            self.add(sp)
            self.play(*anims, run_time=0.8)
            if kind == "push" and v == "C":
                bl = DashedLine(nodes["C"].get_center(), nodes["A"].get_center(), color=RED, stroke_width=6)
                self.play(lines[key("C", "A")].animate.set_opacity(0), Create(bl), run_time=0.6)
                bn = para("Tại C: A đã thăm và không phải cha của C ⇒ cạnh ngược!", 22, RED, y=-0.3)
                self.play(FadeIn(bn), run_time=0.4)
                self.wait(1.5)
                self.play(FadeOut(bn), run_time=0.3)
        self.wait(1.0)
        d1 = para("Thứ tự DFS: A B D G E C F  (BFS: A B C D E F G)", 24, WHITE, y=-4.0)
        self.play(FadeIn(d1), run_time=0.5)
        self.wait(2.5)
        wipe(self, keep=[c])

        # ===== 5. Cạnh ngược = chu trình =====
        c = swap_cap(self, c, cap("Cạnh ngược ⇒ có chu trình", 40, RED))
        nodes, lines = self.graph()
        for k_, l in lines.items():
            if k_ in DTREE:
                l.set_color(GREEN).set_stroke(width=5)
        lines[key("A", "C")] = DashedLine(nodes["C"].get_center(), nodes["A"].get_center(), color=RED, stroke_width=6)
        self.play(*[Create(l) for l in lines.values()], *[FadeIn(n) for n in nodes.values()], run_time=0.8)
        s1 = para("Cây DFS (xanh) + cạnh ngược C–A (đỏ)", 24, WHITE, y=-0.6)
        self.play(FadeIn(s1), run_time=0.5)
        self.wait(1.0)
        s2 = para("Lần theo cha từ C về A: C → E → B → A,\nrồi đóng lại bằng cạnh ngược", 24, WHITE, y=-1.8)
        self.play(FadeIn(s2), run_time=0.5)
        for a, b in [("C", "E"), ("E", "B"), ("B", "A")]:
            self.play(lines[key(a, b)].animate.set_color(GOLD).set_stroke(width=8), nodes[a][0].animate.set_fill(GOLD, 0.6), nodes[b][0].animate.set_fill(GOLD, 0.6), run_time=0.5)
        self.play(Indicate(lines[key("A", "C")], color=GOLD), run_time=0.6)
        s3 = para("Chu trình A – B – E – C – A", 30, GOLD, y=-3.2)
        self.play(FadeIn(s3), run_time=0.5)
        self.wait(1.5)
        s4 = para("Đồ thị vô hướng có chu trình ⇔ DFS gặp cạnh ngược.\nKhông có cạnh ngược nào ⇒ đồ thị là rừng (các cây)", 22, WHITE, y=-4.5)
        self.play(FadeIn(s4), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 5b. Code =====
        c = swap_cap(self, c, cap("Trong code: chỉ khác một dòng", 40, GOLD))
        src = ("q = deque([s]); visited = {s}\n"
               "while q:\n"
               "    u = q.popleft()      # BFS\n"
               "    tham(u)\n"
               "    for v in ke[u]:\n"
               "        if v not in visited:\n"
               "            visited.add(v)\n"
               "            q.append(v)")
        code = Text(src, font="Menlo", font_size=22, color=WHITE, line_spacing=1.15)
        fitw(code, 7.6).move_to([0, 3.2, 0])
        box = SurroundingRectangle(code, color=BLUE, buff=0.2, corner_radius=0.1)
        self.play(FadeIn(code), Create(box), run_time=0.8)
        self.wait(2.0)
        e1 = para("popleft(): lấy đỉnh vào sớm nhất ⇒ hàng đợi ⇒ BFS\nThứ tự: A B C D E F G", 24, BLUE, y=0.2)
        self.play(FadeIn(e1), run_time=0.5)
        self.wait(2.0)
        e2 = para("Đổi thành pop(): lấy đỉnh vào muộn nhất ⇒ ngăn xếp\n⇒ luôn đi tiếp từ đỉnh mới nhất: duyệt theo chiều sâu\nThứ tự: A C F E B D G", 24, GREEN, y=-1.7)
        self.play(FadeIn(e2), run_time=0.5)
        self.wait(2.5)
        e3 = para("Khác thứ tự bản đệ quy (A B D G E C F) vì ở đây\nđánh dấu lúc đưa vào và đẩy láng giềng theo thứ tự xuôi.\nCả hai vẫn là DFS hợp lệ, đều O(V + E)", 22, DIM, y=-3.8)
        self.play(FadeIn(e3), run_time=0.5)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 6. So sánh song song =====
        c = swap_cap(self, c, cap("Đặt cạnh nhau", 44, GOLD))
        for side, tree, col, title, ordr in [(-2.05, BTREE, BLUE, "BFS · queue", "A B C D E F G"), (2.05, DTREE, GREEN, "DFS · stack", "A B D G E C F")]:
            nd, ln = self.graph(scale=0.6, shift=(side, 1.2), r=0.42)
            for k_, l in ln.items():
                if k_ in tree:
                    l.set_color(col).set_stroke(width=5)
                else:
                    l.set_color(RED).set_opacity(0.5)
            tt = Text(title, font=FONT, font_size=28, color=col).move_to([side, 5.0, 0])
            oo = Text(ordr, font=FONT, font_size=22, color=WHITE).move_to([side, 0.6, 0])
            self.play(FadeIn(tt), *[Create(l) for l in ln.values()], *[FadeIn(n) for n in nd.values()], FadeIn(oo), run_time=0.9)
            self.wait(1.0)
        rows = [("", "BFS", "DFS"), ("cấu trúc", "hàng đợi", "ngăn xếp / đệ quy"), ("cây", "rộng, thấp", "dài, sâu"),
                ("mạnh ở", "đường ngắn nhất", "chu trình, sắp xếp tô pô"), ("bộ nhớ", "cả một lớp", "một nhánh")]
        tb = VGroup()
        for i, (a, b, d) in enumerate(rows):
            y = -0.5 - i * 0.8
            tb.add(VGroup(Text(a, font=FONT, font_size=22, color=DIM).move_to([-3.2, y, 0]),
                          Text(b, font=FONT, font_size=22, color=BLUE).move_to([-0.6, y, 0]),
                          Text(d, font=FONT, font_size=22, color=GREEN).move_to([2.5, y, 0])))
        for r in tb:
            self.play(FadeIn(r), run_time=0.4)
            self.wait(0.8)
        cx = para("Cả hai đều O(V + E): mỗi đỉnh vào một lần,\nmỗi cạnh được xét hai lần (mỗi đầu một lần)", 24, GOLD, y=-4.9)
        self.play(FadeIn(cx), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 7. Thành phần liên thông =====
        c = swap_cap(self, c, cap("Đếm thành phần liên thông", 40, GOLD))
        px = dict(POS)
        px.update({"H": (1.4, 0.3), "I": (2.6, 0.3), "J": (3.6, 1.0), "K": (3.4, 4.6)})
        nodes, lines = self.graph(pos=px, edges=EX)
        self.play(*[Create(l) for l in lines.values()], *[FadeIn(n) for n in nodes.values()], run_time=1.0)
        s1 = para("Duyệt lần lượt từng đỉnh; gặp đỉnh chưa thăm thì\nbắt đầu một lần BFS/DFS mới = một thành phần mới", 24, WHITE, y=-0.9)
        self.play(FadeIn(s1), run_time=0.5)
        self.wait(1.5)
        cnt = None
        for i, (comp, col) in enumerate(zip(comps, [BLUE, GREEN, RED])):
            anims = [nodes[v][0].animate.set_fill(col, 0.7) for v in comp]
            anims += [lines[k_].animate.set_color(col) for k_ in lines if k_ <= set(comp)]
            nc = para(f"Số thành phần: {i + 1}", 30, GOLD, y=-2.6)
            if cnt is not None:
                self.remove(cnt)
            cnt = nc
            self.play(*anims, FadeIn(cnt), run_time=0.8)
            self.wait(0.8)
        s2 = para("{A…G}, {H, I, J}, {K}: 3 thành phần", 26, WHITE, y=-3.4)
        self.play(FadeIn(s2), run_time=0.5)
        self.wait(1.5)
        s3 = para("Ứng dụng: nhóm bạn bè trong mạng xã hội,\nvùng tô màu (flood fill), kiểm tra mạng còn liên thông", 22, DIM, y=-4.7)
        self.play(FadeIn(s3), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 8. Tóm tắt =====
        c = swap_cap(self, c, cap("Tóm tắt", 44, GOLD))
        sm = VGroup(*[Text(s, font=FONT, font_size=30, color=col, line_spacing=1.1) for s, col in [
            ("BFS = hàng đợi: đi theo lớp", BLUE),
            ("→ đường đi ít cạnh nhất", BLUE),
            ("DFS = ngăn xếp: đi sâu rồi quay lui", GREEN),
            ("→ cạnh ngược báo có chu trình", GREEN),
            ("Cả hai: O(V + E), đếm được\nthành phần liên thông", GOLD),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        fitw(sm, 7.8).move_to([0, 1.8, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.2) for m in sm], lag_ratio=0.5), run_time=3.0)
        self.wait(6.0)
