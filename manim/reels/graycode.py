from common import *

MONO = "DejaVu Sans Mono"


def gray_reflect(n):
    seq = ["0", "1"]
    for _ in range(n - 1):
        seq = ["0" + s for s in seq] + ["1" + s for s in reversed(seq)]
    return seq


G3 = gray_reflect(3)
assert G3 == [format(i ^ (i >> 1), "03b") for i in range(8)]
assert G3 == ["000", "001", "011", "010", "110", "111", "101", "100"]
for seq in (gray_reflect(2), G3):
    for a, b in zip(seq, seq[1:] + seq[:1]):          # kể cả cặp cuối-đầu (vòng)
        assert sum(x != y for x, y in zip(a, b)) == 1


def code(s, color_first=True, size=34):
    t = Text(s, font=MONO, font_size=size)
    if color_first and len(s) > 1:
        t[0].set_color(BLUE if s[0] == "0" else GOLD)
    return t


class GrayCode(Scene):
    def construct(self):
        c = cap("Mã Gray", 44)
        self.add(c)
        xs = [-2.6, 0.0, 2.6]
        y0, dy = 3.7, 0.62
        heads = [Text(t, font=FONT, font_size=26, color=DIM).move_to([x, 4.7, 0]) for x, t in zip(xs, ["1 bit", "2 bit", "3 bit"])]
        cols = []
        c1 = [code("0", False).move_to([xs[0], y0, 0]), code("1", False).move_to([xs[0], y0 - dy, 0])]
        self.play(FadeIn(heads[0]), *[FadeIn(m) for m in c1], run_time=0.8)
        cols.append(c1)
        c = swap_cap(self, c, cap("Phản chiếu, rồi thêm 0 và 1", 34, GOLD))
        prev = c1
        mirrors = []
        for level in (1, 2):
            n_prev = len(prev)
            seq = gray_reflect(level + 1)
            line_y = y0 - (n_prev - 0.5) * dy
            mirror = DashedLine([xs[level] - 0.9, line_y, 0], [xs[level] + 0.9, line_y, 0], color=GOLD, stroke_width=3)
            news = []
            mirrors.append(mirror)
            for i, s in enumerate(seq):
                news.append(code(s).move_to([xs[level], y0 - i * dy, 0]))
            src_idx = list(range(n_prev)) + list(reversed(range(n_prev)))
            anims = []
            for i, m in enumerate(news):
                anims.append(TransformFromCopy(prev[src_idx[i]], m))
            self.play(FadeIn(heads[level]), Create(mirror), LaggedStart(*anims, lag_ratio=0.12), run_time=1.0 + 0.9 * level)
            self.wait(0.5)
            cols.append(news)
            prev = news
        self.wait(0.6)
        c = swap_cap(self, c, cap("Hai mã kề nhau khác đúng 1 bit", 32))
        # tô cặp liên tiếp
        last = cols[2]
        for i in range(7):
            a, b = last[i], last[i + 1]
            diff = [k for k in range(3) if G3[i][k] != G3[i + 1][k]][0]
            box = SurroundingRectangle(VGroup(a, b), color=GOLD, buff=0.08, stroke_width=3)
            self.play(Create(box), a[diff].animate.set_color(RED), b[diff].animate.set_color(RED), run_time=0.45)
            self.play(FadeOut(box), a[diff].animate.set_color(WHITE), b[diff].animate.set_color(WHITE), run_time=0.15)

        # ---- khối lập phương ----
        self.play(*[FadeOut(m) for m in sum(cols, [])], *[FadeOut(h) for h in heads], *[FadeOut(m) for m in mirrors], run_time=0.6)
        c = swap_cap(self, c, cap("Đi dọc các cạnh của khối lập phương", 32, GOLD))
        S = 3.2
        dep = np.array([1.5, 1.5, 0])
        origin = np.array([-2.5, -0.8, 0])
        pos = {}
        for s in G3:
            x, y, z = (int(ch) for ch in s)
            pos[s] = origin + np.array([x * S, y * S, 0]) + z * dep
        edges = {}
        for a in G3:
            for b in G3:
                if a < b and sum(p != q for p, q in zip(a, b)) == 1:
                    edges[(a, b)] = Line(pos[a], pos[b], color=DIM, stroke_width=3)
        assert len(edges) == 12
        dots = {s: Dot(pos[s], radius=0.13, color=BLUE) for s in G3}
        labs = {}
        for s in G3:
            off = np.array([0.0, 0.0, 0]) + (DOWN * 0.4 if s[1] == "0" else UP * 0.4)
            labs[s] = Text(s, font=MONO, font_size=24).move_to(pos[s] + off)
        self.play(*[Create(e) for e in edges.values()], run_time=1.0)
        self.play(*[FadeIn(d) for d in dots.values()], *[FadeIn(l) for l in labs.values()], run_time=0.6)
        hero = Dot(pos[G3[0]], radius=0.22, color=GOLD).set_z_index(5)
        self.play(FadeIn(hero), run_time=0.3)
        order = G3 + [G3[0]]
        for i in range(8):
            a, b = order[i], order[i + 1]
            e = edges[tuple(sorted((a, b)))]
            self.play(hero.animate.move_to(pos[b]), e.animate.set_color(GOLD).set_stroke(width=7),
                      dots[b].animate.set_color(GOLD), run_time=0.55)
        seqtxt = Text("000 → 001 → 011 → 010\n→ 110 → 111 → 101 → 100 → 000", font=MONO, font_size=26, line_spacing=0.9, color=GOLD).move_to([0, -3.9, 0])
        self.play(FadeIn(seqtxt), run_time=0.6)
        note = Text("8 mã, mỗi bước đổi 1 bit, quay về điểm đầu", font=FONT, font_size=26, color=DIM).move_to([0, -5.2, 0])
        self.play(FadeIn(note), run_time=0.5)
        k = Text("Dùng cho trục của K-map", font=FONT, font_size=30).move_to([0, -6.1, 0])
        self.play(FadeIn(k), run_time=0.5)
        self.wait(2.5)
