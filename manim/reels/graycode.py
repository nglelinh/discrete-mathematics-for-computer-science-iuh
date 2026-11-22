"""Reel K-map (bản dài): mã Gray → K-map 2, 3, 4 biến → nhóm 1/2/4/8, wrap-around, don't-care."""
from common import *
from itertools import product, combinations

MONO = "DejaVu Sans Mono"


# ---------- Mã Gray ----------
def gray_reflect(n):
    seq = ["0", "1"]
    for _ in range(n - 1):
        seq = ["0" + s for s in seq] + ["1" + s for s in reversed(seq)]
    return seq


G2 = gray_reflect(2)
G3 = gray_reflect(3)
assert G2 == ["00", "01", "11", "10"]
assert G3 == [format(i ^ (i >> 1), "03b") for i in range(8)]
for seq in (G2, G3):
    for a, b in zip(seq, seq[1:] + seq[:1]):
        assert sum(x != y for x, y in zip(a, b)) == 1
assert sum(x != y for x, y in zip("01", "10")) == 2     # thứ tự nhị phân thường: 01 → 10 đổi 2 bit


# ---------- Kiểm tra phủ tối tiểu bằng vét cạn ----------
def cubes(n):
    return ["".join(t) for t in product("01-", repeat=n)]


def cube_m(c):
    out = []
    for bits in product("01", repeat=len(c)):
        if all(cc == "-" or cc == b for cc, b in zip(c, bits)):
            out.append(int("".join(bits), 2))
    return set(out)


def minimal_covers(n, ones, dc=()):
    ones, ok = set(ones), set(ones) | set(dc)
    imps = [c for c in cubes(n) if cube_m(c) <= ok and cube_m(c) & ones]
    primes = [c for c in imps if not any(d != c and cube_m(c) < cube_m(d) for d in imps)]
    for k in range(1, len(primes) + 1):
        best, sols = None, []
        for comb in combinations(primes, k):
            if set().union(*[cube_m(c) for c in comb]) >= ones:
                lits = sum(len(c) - c.count("-") for c in comb)
                if best is None or lits < best:
                    best, sols = lits, [set(comb)]
                elif lits == best:
                    sols.append(set(comb))
        if sols:
            return sols
    return []


def check(n, ones, expect, dc=()):
    sols = minimal_covers(n, ones, dc)
    assert set(expect) in sols, (ones, expect, sols)
    return sols


# 2 biến (x, y): m = 2x + y
EX2 = [1, 2, 3]
check(2, EX2, ["1-", "-1"])                                 # x + y
# 3 biến (x, y, z): m = 4x + 2y + z ; ví dụ 2 trong bài
EX3 = [0, 1, 2, 5, 7]
S3 = check(3, EX3, ["00-", "0-0", "1-1"])                   # x̄ȳ + x̄z̄ + xz
assert len(S3) == 2 and {"00-", "-01", "0-0"} not in S3     # có phương án khác cùng chi phí
EX3W = [0, 4]
check(3, EX3W, ["-00"])                                     # ȳz̄: hàng 00 và hàng 10 kề nhau
# 4 biến (x, y, z, w): m = 8x + 4y + 2z + w
EX4A = [0, 1, 2, 3, 5, 7, 8, 9, 10, 11, 13, 15]
check(4, EX4A, ["-0--", "---1"])                            # ȳ + w
EX4B = [0, 2, 5, 7, 8, 10, 13, 15]
check(4, EX4B, ["-0-0", "-1-1"])                            # ȳw̄ + yw (4 góc + khối giữa)
# don't-care (ví dụ trong bài)
DC_ONES, DC_X = [0, 1, 3], [5, 7]
check(3, DC_ONES, ["00-", "--1"], DC_X)                     # x̄ȳ + z
check(3, DC_ONES, ["00-", "0-1"])                           # không dùng X: x̄ȳ + x̄z


def term_str(c, vars_):
    return "".join(("~" if ch == "0" else "") + v for ch, v in zip(c, vars_) if ch != "-")


# ---------- Lưới K-map ----------
class KMap:
    def __init__(self, rows, cols, rvar, cvar, mfun, cell=1.15, center=(0, 2.2), size=36):
        self.rows, self.cols, self.mfun, self.cell = rows, cols, mfun, cell
        nr, nc = len(rows), len(cols)
        cx, cy = center
        self.x0 = cx - (nc - 1) * cell / 2
        self.y0 = cy + (nr - 1) * cell / 2
        self.sq, self.val, self.idx = {}, {}, {}
        g = VGroup()
        for i in range(nr):
            for j in range(nc):
                p = self.pos(i, j)
                s = Square(cell, color=DIM, stroke_width=2).move_to(p)
                m = mfun(rows[i], cols[j])
                ix = Text(str(m), font=FONT, font_size=17, color=DIM).move_to(p + np.array([-cell / 2 + 0.17, cell / 2 - 0.15, 0]))
                self.sq[(i, j)], self.idx[(i, j)] = s, ix
                g.add(s, ix)
        self.rl = VGroup(*[Text(r, font=MONO, font_size=28, color=BLUE).move_to(self.pos(i, 0) + LEFT * (cell * 0.5 + 0.45)) for i, r in enumerate(rows)])
        self.cl = VGroup(*[Text(c, font=MONO, font_size=28, color=GOLD).move_to(self.pos(0, j) + UP * (cell * 0.5 + 0.32)) for j, c in enumerate(cols)])
        corner = self.pos(0, 0) + np.array([-cell * 0.5 - 0.45, cell * 0.5 + 0.32, 0])
        self.vl = VGroup(Text(rvar, font=FONT, font_size=26, color=BLUE), Text("\\", font=FONT, font_size=26, color=DIM),
                         Text(cvar, font=FONT, font_size=26, color=GOLD)).arrange(RIGHT, buff=0.04).move_to(corner + LEFT * 0.15 + UP * 0.05)
        self.grid = g
        self.size = size

    def pos(self, i, j):
        return np.array([self.x0 + j * self.cell, self.y0 - i * self.cell, 0])

    def cell_of(self, m):
        for (i, j) in self.sq:
            if self.mfun(self.rows[i], self.cols[j]) == m:
                return (i, j)

    def all(self):
        return VGroup(self.grid, self.rl, self.cl, self.vl)

    def fill(self, ones, dc=()):
        anims = []
        for (i, j) in self.sq:
            m = self.mfun(self.rows[i], self.cols[j])
            s = "1" if m in ones else ("X" if m in dc else "0")
            col = WHITE if s == "1" else (GOLD if s == "X" else "#4a4e57")
            t = Text(s, font=FONT, font_size=self.size, color=col).move_to(self.pos(i, j))
            self.val[(i, j)] = t
            anims.append(FadeIn(t))
        return anims

    def piece(self, r0, r1, c0, c1, color, pad=0.1, open_=()):
        w = (c1 - c0 + 1) * self.cell - 2 * pad
        h = (r1 - r0 + 1) * self.cell - 2 * pad
        ctr = (self.pos(r0, c0) + self.pos(r1, c1)) / 2
        rr = RoundedRectangle(width=w, height=h, corner_radius=0.25, color=color, stroke_width=6).move_to(ctr)
        # kéo phần hở ra ngoài mép lưới để báo hiệu wrap-around
        sh = {"L": LEFT, "R": RIGHT, "U": UP, "D": DOWN}
        for o in open_:
            rr.stretch(1 + 0.35 / (w if o in "LR" else h), 0 if o in "LR" else 1, about_edge=-sh[o])
        return rr


def gray_col(seq, x, y0, dy, size=32):
    return [Text(s, font=MONO, font_size=size).move_to([x, y0 - i * dy, 0]) for i, s in enumerate(seq)]


class GrayCode(Scene):
    def wait(self, duration=1.0, **kw):
        super().wait(duration * 1.6, **kw)

    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Rút gọn hàm Boole", 44)
        t1 = Text("Bản đồ\nKarnaugh", font=FONT, font_size=84, color=GOLD, line_spacing=1.0).move_to([0, 1.5, 0])
        t2 = para("Khoanh nhóm các ô 1 trên một lưới\nsắp theo mã Gray", 34, y=-1.3)
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. Mã Gray =====
        c = swap_cap(self, c, cap("Mã Gray: phản chiếu rồi thêm 0, 1", 36, GOLD))
        xs = [-2.6, 0.0, 2.6]
        y0, dy = 4.6, 0.6
        heads = [Text(t, font=FONT, font_size=26, color=DIM).move_to([x, 5.4, 0]) for x, t in zip(xs, ["1 bit", "2 bit", "3 bit"])]
        prev = gray_col(["0", "1"], xs[0], y0, dy)
        cols = [prev]
        self.play(FadeIn(heads[0]), *[FadeIn(m) for m in prev], run_time=0.7)
        mirrors = []
        for level in (1, 2):
            n_prev = len(prev)
            seq = gray_reflect(level + 1)
            line_y = y0 - (n_prev - 0.5) * dy
            mirror = DashedLine([xs[level] - 0.9, line_y, 0], [xs[level] + 0.9, line_y, 0], color=GOLD, stroke_width=3)
            news = gray_col(seq, xs[level], y0, dy)
            for m, s in zip(news, seq):
                m[0].set_color(BLUE if s[0] == "0" else GOLD)
            src = list(range(n_prev)) + list(reversed(range(n_prev)))
            self.play(FadeIn(heads[level]), Create(mirror), LaggedStart(*[TransformFromCopy(prev[src[i]], m) for i, m in enumerate(news)], lag_ratio=0.12), run_time=1.2 + 0.8 * level)
            mirrors.append(mirror)
            cols.append(news)
            prev = news
            self.wait(0.8)
        n1 = para("Hai mã liền nhau khác đúng 1 bit,\nkể cả mã cuối với mã đầu", 30, WHITE, y=-0.6)
        self.play(FadeIn(n1), run_time=0.6)
        last = cols[2]
        for i in range(8):
            a, b = last[i], last[(i + 1) % 8]
            d = [k for k in range(3) if G3[i][k] != G3[(i + 1) % 8][k]][0]
            self.play(a[d].animate.set_color(RED), b[d].animate.set_color(RED), run_time=0.25)
            self.play(a[d].animate.set_color(BLUE if G3[i][0] == "0" or d else GOLD) if d == 0 else a[d].animate.set_color(WHITE),
                      b[d].animate.set_color(WHITE) if d else b[d].animate.set_color(BLUE if G3[(i + 1) % 8][0] == "0" else GOLD), run_time=0.15)
        n2 = para("Thứ tự nhị phân thường thì không:\n01 → 10 đổi cả 2 bit", 28, DIM, y=-2.3)
        self.play(FadeIn(n2), run_time=0.6)
        self.wait(2.5)
        wipe(self, keep=[c])

        # khối lập phương
        c = swap_cap(self, c, cap("Mã Gray 3 bit: đi dọc cạnh khối lập phương", 32, GOLD))
        S, dep, origin = 3.0, np.array([1.4, 1.4, 0]), np.array([-2.4, 0.4, 0])
        pos = {s: origin + np.array([int(s[0]) * S, int(s[1]) * S, 0]) + int(s[2]) * dep for s in G3}
        edges = {}
        for a in G3:
            for b in G3:
                if a < b and sum(p != q for p, q in zip(a, b)) == 1:
                    edges[(a, b)] = Line(pos[a], pos[b], color=DIM, stroke_width=3)
        assert len(edges) == 12
        dots = {s: Dot(pos[s], radius=0.12, color=BLUE) for s in G3}
        labs = {s: Text(s, font=MONO, font_size=24).move_to(pos[s] + (DOWN if s[1] == "0" else UP) * 0.38) for s in G3}
        self.play(*[Create(e) for e in edges.values()], run_time=0.8)
        self.play(*[FadeIn(d) for d in dots.values()], *[FadeIn(l) for l in labs.values()], run_time=0.5)
        hero = Dot(pos[G3[0]], radius=0.2, color=GOLD).set_z_index(5)
        self.play(FadeIn(hero), run_time=0.3)
        order = G3 + [G3[0]]
        for i in range(8):
            a, b = order[i], order[i + 1]
            self.play(hero.animate.move_to(pos[b]), edges[tuple(sorted((a, b)))].animate.set_color(GOLD).set_stroke(width=7), run_time=0.45)
        k = para("K-map dùng thứ tự này cho trục:\nhai ô cạnh nhau chỉ khác một biến", 30, WHITE, y=-4.3)
        self.play(FadeIn(k), run_time=0.6)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 3. Ý tưởng gộp =====
        c = swap_cap(self, c, cap("Vì sao cần khác đúng một biến?", 38, GOLD))
        law = bexpr("xy + x~y = x", 50).move_to([0, 3.6, 0])
        self.play(FadeIn(law), run_time=0.6)
        self.wait(1.5)
        e1 = bexpr("~x~yz + ~xyz = ~xz", 40).move_to([0, 2.0, 0])
        e2 = para("y đổi giá trị trong nhóm → y bị triệt", 30, GREEN, y=1.0)
        self.play(FadeIn(e1), run_time=0.6)
        self.play(FadeIn(e2), run_time=0.6)
        self.wait(2.5)
        e3 = para("Gộp 2 ô bỏ 1 biến, 4 ô bỏ 2 biến, 8 ô bỏ 3 biến.\nNhóm phải có 1, 2, 4, 8… ô và là hình chữ nhật.", 28, WHITE, y=-0.8)
        self.play(FadeIn(e3), run_time=0.7)
        self.wait(4.0)
        wipe(self, keep=[c])

        # ===== 4. Hai biến =====
        c = swap_cap(self, c, cap("K-map hai biến", 42, GOLD))
        km = KMap(["0", "1"], ["0", "1"], "x", "y", lambda r, cc: 2 * int(r) + int(cc), cell=1.5, center=(0.3, 3.0), size=44)
        self.play(FadeIn(km.all()), run_time=0.8)
        f = bexpr("F = ~xy + x~y + xy", 36).move_to([0, 0.4, 0])
        self.play(FadeIn(f), run_time=0.5)
        self.play(*km.fill(EX2), run_time=0.7)
        self.wait(1.5)
        g1 = km.piece(0, 1, 1, 1, BLUE)
        g2 = km.piece(1, 1, 0, 1, GREEN, pad=0.18)
        r1 = para("Cột y = 1: x đổi → còn y", 30, BLUE, y=-0.6)
        self.play(Create(g1), FadeIn(r1), run_time=0.7)
        self.wait(2.0)
        r2 = para("Hàng x = 1: y đổi → còn x", 30, GREEN, y=-1.4)
        self.play(Create(g2), FadeIn(r2), run_time=0.7)
        self.wait(2.0)
        r3 = para("Ô 11 nằm trong cả hai nhóm: được phép", 28, DIM, y=-2.3)
        res = para("F = x + y", 44, GOLD, y=-3.6)
        self.play(FadeIn(r3), run_time=0.5)
        self.wait(1.5)
        self.play(FadeIn(res), run_time=0.6)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 5. Ba biến =====
        c = swap_cap(self, c, cap("K-map ba biến", 42, GOLD))
        km = KMap(G2, ["0", "1"], "xy", "z", lambda r, cc: 4 * int(r[0]) + 2 * int(r[1]) + int(cc), cell=1.15, center=(0.4, 3.0))
        self.play(FadeIn(km.all()), run_time=0.8)
        n = para("Hàng xy theo thứ tự Gray: 00, 01, 11, 10.\nSố nhỏ ở góc là chỉ số minterm.", 26, DIM, y=-0.2)
        self.play(FadeIn(n), run_time=0.5)
        self.wait(2.5)
        f = para("F = Σm(0, 1, 2, 5, 7)", 34, WHITE, y=-1.2)
        self.play(FadeOut(n), FadeIn(f), *km.fill(EX3), run_time=0.8)
        self.wait(1.5)
        groups = [((0, 0, 0, 1), BLUE, "00-", "hàng 00: z đổi"),
                  ((0, 1, 0, 0), GREEN, "0-0", "cột z = 0, hàng 00 và 01: y đổi"),
                  ((2, 3, 1, 1), RED, "1-1", "cột z = 1, hàng 11 và 10: y đổi")]
        ys = [-2.2, -3.0, -3.8]
        terms = []
        for k_, ((r0, r1, c0, c1), col, cube, why) in enumerate(groups):
            pc = km.piece(r0, r1, c0, c1, col, pad=0.1 + 0.06 * k_)
            t = VGroup(bexpr(term_str(cube, "xyz"), 34, col), Text("  " + why, font=FONT, font_size=24, color=DIM)).arrange(RIGHT, buff=0.3)
            fitw(t).move_to([0, ys[k_], 0])
            self.play(Create(pc), FadeIn(t), run_time=0.7)
            terms.append(cube)
            self.wait(2.0)
        res = bexpr("F = ~x~y + ~x~z + xz", 42, GOLD).move_to([0, -5.0, 0])
        self.play(FadeIn(res), run_time=0.6)
        self.wait(1.5)
        alt = para("(Cũng tối tiểu: thay x̄ȳ bằng ȳz, cùng 3 hạng 6 literal)", 22, DIM, y=-5.9)
        alt = VGroup(Text("Phương án khác cùng chi phí: thay", font=FONT, font_size=24, color=DIM), bexpr("~x~y", 24, DIM),
                     Text("bằng", font=FONT, font_size=24, color=DIM), bexpr("~yz", 24, DIM)).arrange(RIGHT, buff=0.15).move_to([0, -5.9, 0])
        self.play(FadeIn(alt), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # wrap-around 3 biến
        c = swap_cap(self, c, cap("Mép trên kề mép dưới", 42, GOLD))
        km = KMap(G2, ["0", "1"], "xy", "z", lambda r, cc: 4 * int(r[0]) + 2 * int(r[1]) + int(cc), cell=1.15, center=(0.4, 3.0))
        self.play(FadeIn(km.all()), *km.fill(EX3W), run_time=0.8)
        f = para("F = Σm(0, 4)", 34, WHITE, y=-1.2)
        self.play(FadeIn(f), run_time=0.4)
        hl = [km.rl[0].animate.set_color(RED), km.rl[3].animate.set_color(RED)]
        w1 = para("Hàng 00 và hàng 10 chỉ khác bit x:\nchúng kề nhau, như cuộn lưới thành ống", 28, WHITE, y=-2.4)
        self.play(*hl, FadeIn(w1), run_time=0.6)
        self.wait(2.5)
        p1 = km.piece(0, 0, 0, 0, GREEN, open_="U")
        p2 = km.piece(3, 3, 0, 0, GREEN, open_="D")
        self.play(Create(p1), Create(p2), run_time=0.7)
        r = VGroup(Text("F =", font=FONT, font_size=40, color=GOLD), bexpr("~y~z", 40, GOLD)).arrange(RIGHT, buff=0.2).move_to([0, -4.0, 0])
        self.play(FadeIn(r), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 6. Bốn biến =====
        c = swap_cap(self, c, cap("K-map bốn biến", 42, GOLD))
        mf4 = lambda r, cc: 8 * int(r[0]) + 4 * int(r[1]) + 2 * int(cc[0]) + int(cc[1])
        km = KMap(G2, G2, "xy", "zw", mf4, cell=1.05, center=(0.45, 3.0), size=32)
        self.play(FadeIn(km.all()), run_time=0.8)
        n = para("Hàng xy và cột zw đều theo Gray.\nCột trái kề cột phải, hàng trên kề hàng dưới.", 26, DIM, y=-0.4)
        self.play(FadeIn(n), run_time=0.5)
        self.wait(3.0)
        f = para("F = Σm(0, 1, 2, 3, 5, 7, 8, 9, 10, 11, 13, 15)", 28, WHITE, y=-0.6)
        self.play(FadeOut(n), FadeIn(f), *km.fill(EX4A), run_time=0.8)
        self.wait(1.5)
        g8a = km.piece(0, 3, 1, 2, BLUE, pad=0.12)
        t1 = para("8 ô ở hai cột giữa (zw = 01, 11): w = 1 → w", 26, BLUE, y=-1.6)
        self.play(Create(g8a), FadeIn(t1), run_time=0.7)
        self.wait(2.5)
        g8b = [km.piece(0, 0, 0, 3, GREEN, pad=0.2, open_="U"), km.piece(3, 3, 0, 3, GREEN, pad=0.2, open_="D")]
        t2 = VGroup(Text("8 ô ở hàng 00 và hàng 10 (wrap): y = 0 →", font=FONT, font_size=26, color=GREEN), bexpr("~y", 26, GREEN)).arrange(RIGHT, buff=0.15)
        fitw(t2).move_to([0, -2.4, 0])
        self.play(*[Create(p) for p in g8b], FadeIn(t2), run_time=0.8)
        self.wait(2.5)
        r = VGroup(Text("F =", font=FONT, font_size=44, color=GOLD), bexpr("~y + w", 44, GOLD)).arrange(RIGHT, buff=0.2).move_to([0, -3.7, 0])
        tt = para("12 minterm, mỗi cái 4 literal → 2 literal", 26, DIM, y=-4.7)
        self.play(FadeIn(r), run_time=0.5)
        self.play(FadeIn(tt), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # bốn góc
        c = swap_cap(self, c, cap("Bốn góc cũng là một nhóm", 40, GOLD))
        km = KMap(G2, G2, "xy", "zw", mf4, cell=1.05, center=(0.45, 3.0), size=32)
        f = para("F = Σm(0, 2, 5, 7, 8, 10, 13, 15)", 30, WHITE, y=-0.6)
        self.play(FadeIn(km.all()), *km.fill(EX4B), FadeIn(f), run_time=0.8)
        self.wait(1.5)
        corners = [km.piece(0, 0, 0, 0, GREEN, open_="UL"), km.piece(0, 0, 3, 3, GREEN, open_="UR"),
                   km.piece(3, 3, 0, 0, GREEN, open_="DL"), km.piece(3, 3, 3, 3, GREEN, open_="DR")]
        t1 = VGroup(Text("4 góc: m0, m2, m8, m10 → y = 0, w = 0 →", font=FONT, font_size=26, color=GREEN), bexpr("~y~w", 26, GREEN)).arrange(RIGHT, buff=0.15)
        fitw(t1).move_to([0, -1.6, 0])
        self.play(*[Create(p) for p in corners], FadeIn(t1), run_time=0.8)
        self.wait(3.0)
        mid = km.piece(1, 2, 1, 2, BLUE)
        t2 = para("Khối 2×2 ở giữa: y = 1, w = 1 → yw", 26, BLUE, y=-2.4)
        self.play(Create(mid), FadeIn(t2), run_time=0.7)
        self.wait(2.5)
        r = VGroup(Text("F =", font=FONT, font_size=44, color=GOLD), bexpr("~y~w + yw", 44, GOLD)).arrange(RIGHT, buff=0.2).move_to([0, -3.7, 0])
        self.play(FadeIn(r), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 7. Don't-care =====
        c = swap_cap(self, c, cap("Ô don't-care (X)", 42, GOLD))
        km = KMap(G2, ["0", "1"], "xy", "z", lambda r, cc: 4 * int(r[0]) + 2 * int(r[1]) + int(cc), cell=1.15, center=(0.4, 3.0))
        f = para("F = 1 tại m0, m1, m3;  không quan tâm tại m5, m7", 26, WHITE, y=-0.9)
        self.play(FadeIn(km.all()), *km.fill(DC_ONES, DC_X), FadeIn(f), run_time=0.8)
        self.wait(2.0)
        a1 = km.piece(0, 0, 0, 1, BLUE)
        a2 = km.piece(0, 1, 1, 1, RED, pad=0.18)
        t1 = VGroup(Text("Bỏ qua X:", font=FONT, font_size=28, color=DIM), bexpr("F = ~x~y + ~xz", 30, WHITE)).arrange(RIGHT, buff=0.25).move_to([0, -1.9, 0])
        self.play(Create(a1), Create(a2), FadeIn(t1), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(a2), run_time=0.3)
        a3 = km.piece(0, 3, 1, 1, GREEN, pad=0.18)
        t2 = VGroup(Text("Coi X là 1:", font=FONT, font_size=28, color=GREEN), bexpr("F = ~x~y + z", 34, GOLD)).arrange(RIGHT, buff=0.25).move_to([0, -2.9, 0])
        self.play(Create(a3), FadeIn(t2), run_time=0.8)
        self.wait(2.0)
        t3 = para("X được dùng khi nó làm nhóm to hơn,\nnhưng không bắt buộc phải phủ X.", 26, DIM, y=-4.3)
        self.play(FadeIn(t3), run_time=0.5)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 8. Tóm tắt =====
        c = swap_cap(self, c, cap("Quy tắc khoanh nhóm", 42, GOLD))
        sm = VGroup(*[Text(s, font=FONT, font_size=30, color=col) for s, col in [
            ("1. Chỉ khoanh ô 1 (và X nếu có lợi)", WHITE),
            ("2. Nhóm có 1, 2, 4, 8… ô, hình chữ nhật", WHITE),
            ("3. Nhóm càng to càng tốt", GREEN),
            ("4. Các nhóm được chồng lên nhau", WHITE),
            ("5. Mọi ô 1 phải nằm trong ít nhất một nhóm", WHITE),
            ("6. Mép đối diện và bốn góc là kề nhau", BLUE),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        fitw(sm, 7.6).move_to([0, 2.4, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.2) for m in sm], lag_ratio=0.45), run_time=3.0)
        self.wait(2.0)
        rd = para("Đọc nhóm: biến đổi giá trị thì bỏ,\nbiến luôn 1 giữ nguyên, biến luôn 0 lấy bù.", 28, GOLD, y=-2.4)
        self.play(FadeIn(rd), run_time=0.6)
        self.wait(5.0)
