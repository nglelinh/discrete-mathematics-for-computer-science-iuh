from common import *
import heapq
from collections import Counter

# ---------- Toán ----------
WORD = "ABRACADABRA"
FREQ = Counter(WORD)
assert dict(FREQ) == {"A": 5, "B": 2, "R": 2, "C": 1, "D": 1}
ORDER = ["A", "B", "R", "C", "D"]
heap = [(FREQ[s], i, s) for i, s in enumerate(ORDER)]
heapq.heapify(heap)
KIDS, W, MERGES = {}, dict(FREQ), []
cnt = len(ORDER)
QSTATES = [sorted([(w, i, s) for w, i, s in heap])]
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    name = "N%d" % cnt
    KIDS[name] = (a[2], b[2])
    W[name] = a[0] + b[0]
    heapq.heappush(heap, (W[name], cnt, name))
    MERGES.append((a[2], b[2], name))
    cnt += 1
    QSTATES.append(sorted(heap))
ROOT = heap[0][2]
assert MERGES == [("C", "D", "N5"), ("B", "R", "N6"), ("N5", "N6", "N7"), ("A", "N7", "N8")] and ROOT == "N8"
CODE = {}


def walk(n, pre):
    if n in KIDS:
        walk(KIDS[n][0], pre + "0")
        walk(KIDS[n][1], pre + "1")
    else:
        CODE[n] = pre


walk(ROOT, "")
assert CODE == {"A": "0", "C": "100", "D": "101", "B": "110", "R": "111"}
TOTAL = sum(FREQ[s] * len(CODE[s]) for s in FREQ)
assert TOTAL == 23 and len(WORD) * 3 == 33 and 2 ** 2 < 5 <= 2 ** 3
assert round(100 * (33 - 23) / 33) == 30 and "%.2f" % (23 / 11) == "2.09"
ENC = "".join(CODE[ch] for ch in WORD)
assert len(ENC) == 23 and ENC == "01101110100010101101110"
for x in CODE.values():          # prefix-free
    for y in CODE.values():
        assert x == y or not y.startswith(x)
# giải mã
dec, cur, steps = [], "", []
inv = {v: k for k, v in CODE.items()}
for bit in ENC:
    cur += bit
    if cur in inv:
        dec.append(inv[cur])
        steps.append(cur)
        cur = ""
assert "".join(dec) == WORD

POS = {"N8": (-0.6, 4.8), "A": (-2.5, 3.5), "N7": (1.3, 3.5), "N5": (-0.1, 2.2), "N6": (2.7, 2.2),
       "C": (-0.8, 0.9), "D": (0.6, 0.9), "B": (2.0, 0.9), "R": (3.4, 0.9)}
COLS = {"A": GOLD, "B": BLUE, "R": GREEN, "C": RED, "D": "#c792ea"}
R = 0.42


def nd(n):
    p = POS[n]
    leaf = n not in KIDS
    col = COLS[n] if leaf else DIM
    c = Circle(R, color=col, stroke_width=4, fill_color=CELL, fill_opacity=1).move_to([p[0], p[1], 0])
    if leaf:
        t = VGroup(Text(n, font=FONT, font_size=30, color=col).move_to(c),
                   Text(str(W[n]), font=FONT, font_size=22, color=WHITE).move_to(c.get_center() + DOWN * (R + 0.25)))
    else:
        t = Text(str(W[n]), font=FONT, font_size=28).move_to(c)
    return VGroup(c, t)


def ed(p, q):
    a, b = np.array([*POS[p], 0]), np.array([*POS[q], 0])
    d = (b - a) / np.linalg.norm(b - a)
    return Line(a + d * R, b - d * R, color=DIM, stroke_width=3)


def qrow(state, y):
    items = []
    for w, _, s in state:
        lbl = s if s not in KIDS else "•"
        items.append(VGroup(RoundedRectangle(width=0.95, height=0.75, corner_radius=0.12, color=COLS.get(s, DIM), stroke_width=2),
                            Text(f"{w}", font=FONT, font_size=26)).arrange(ORIGIN))
    g = VGroup(*items).arrange(RIGHT, buff=0.15).move_to([0.6, y, 0])
    return g


class Huffman(Scene):
    def wait(self, duration=1.0, **kw):
        super().wait(duration * 1.6, **kw)

    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Nén dữ liệu bằng cây nhị phân", 38)
        t1 = Text("Mã Huffman", font=FONT, font_size=84, color=GOLD).move_to([0, 1.6, 0])
        t2 = para("Ký tự hay gặp → mã ngắn,\nký tự hiếm → mã dài", 32, y=-0.3)
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. Đếm tần suất =====
        c = swap_cap(self, c, cap("Bước 0: đếm tần suất", 42, GOLD))
        letters = VGroup(*[Text(ch, font=FONT, font_size=56, color=COLS[ch]) for ch in WORD]).arrange(RIGHT, buff=0.12).move_to([0, 4.8, 0])
        self.play(Write(letters), run_time=1.2)
        self.wait(1.0)
        bars = VGroup()
        for i, s in enumerate(ORDER):
            x = -3.0 + i * 1.5
            b = Rectangle(width=1.0, height=0.55 * FREQ[s], color=COLS[s], fill_color=COLS[s], fill_opacity=0.35, stroke_width=3)
            b.move_to([x, 0.6 + 0.55 * FREQ[s] / 2, 0])
            lb = Text(s, font=FONT, font_size=34, color=COLS[s]).move_to([x, 0.15, 0])
            nm = Text(str(FREQ[s]), font=FONT, font_size=30).next_to(b, UP, buff=0.1)
            bars.add(VGroup(b, lb, nm))
        self.play(*[TransformFromCopy(VGroup(*[letters[i] for i, ch in enumerate(WORD) if ch == s]), bars[k][0]) for k, s in enumerate(ORDER)],
                  *[FadeIn(bars[k][1]) for k in range(5)], run_time=1.4)
        self.play(*[FadeIn(bars[k][2]) for k in range(5)], run_time=0.5)
        self.wait(1.5)
        f1 = para("Mã độ dài cố định: 5 ký tự cần 3 bit (2² = 4 < 5 ≤ 8)", 26, WHITE, y=-1.0)
        f2 = para("11 ký tự × 3 bit = 33 bit", 34, RED, y=-1.8)
        self.play(FadeIn(f1), run_time=0.6)
        self.wait(1.5)
        self.play(FadeIn(f2), run_time=0.6)
        self.wait(1.5)
        f3 = para("A xuất hiện 5 lần mà vẫn tốn 3 bit mỗi lần: phí!", 26, DIM, y=-2.7)
        self.play(FadeIn(f3), run_time=0.5)
        self.wait(2.5)
        wipe(self, keep=[c])

        # ===== 3. Xây cây =====
        c = swap_cap(self, c, cap("Gộp hai nút nhẹ nhất, lặp lại", 40, GOLD))
        nodes = {n: nd(n) for n in ORDER}
        self.play(*[GrowFromCenter(nodes[n]) for n in ORDER], run_time=0.8)
        ql = Text("Hàng đợi ưu tiên:", font=FONT, font_size=24, color=DIM).move_to([0, -0.6, 0])
        q = qrow(QSTATES[0], -1.4)
        self.play(FadeIn(ql), FadeIn(q), run_time=0.5)
        self.wait(1.5)
        notes = [
            "C(1) + D(1) = 2",
            "B(2) + R(2) = 4   (hòa thì lấy theo thứ tự)",
            "2 + 4 = 6",
            "A(5) + 6 = 11: còn một nút, đó là gốc",
        ]
        for k, ((a, b, n), nt) in enumerate(zip(MERGES, notes)):
            self.play(q[0][0].animate.set_stroke(WHITE, 5), q[1][0].animate.set_stroke(WHITE, 5),
                      nodes[a][0].animate.set_stroke(WHITE, 6), nodes[b][0].animate.set_stroke(WHITE, 6), run_time=0.5)
            m = para(nt, 26, GOLD, y=-2.4)
            self.play(FadeIn(m), run_time=0.4)
            self.wait(1.0)
            nodes[n] = nd(n)
            self.play(GrowFromCenter(nodes[n]), Create(ed(n, a)), Create(ed(n, b)),
                      nodes[a][0].animate.set_stroke(COLS.get(a, DIM), 4), nodes[b][0].animate.set_stroke(COLS.get(b, DIM), 4), run_time=0.8)
            nq = qrow(QSTATES[k + 1], -1.4)
            self.play(Transform(q, nq), run_time=0.5)
            self.wait(1.4)
            self.play(FadeOut(m), run_time=0.3)
        self.play(FadeOut(q), FadeOut(ql), run_time=0.4)
        bits = VGroup()
        for n, (l, r) in KIDS.items():
            for child, b, sh in ((l, "0", LEFT), (r, "1", RIGHT)):
                mid = (np.array([*POS[n], 0]) + np.array([*POS[child], 0])) / 2
                bits.add(Text(b, font=FONT, font_size=26, color=GOLD).move_to(mid + sh * 0.3 + UP * 0.12))
        m = para("Nhánh trái = 0, nhánh phải = 1", 28, GOLD, y=-0.8)
        self.play(FadeIn(bits), FadeIn(m), run_time=0.8)
        self.wait(1.5)
        rows = [("Ký tự", "Tần suất", "Mã", "Số bit")] + [(s, str(FREQ[s]), CODE[s], f"{FREQ[s]}×{len(CODE[s])} = {FREQ[s] * len(CODE[s])}") for s in ORDER]
        assert [r[2] for r in rows[1:]] == ["0", "110", "111", "100", "101"]
        tb = VGroup()
        xs = [-2.9, -1.3, 0.4, 2.4]
        for i, r in enumerate(rows):
            for j, s in enumerate(r):
                col = DIM if i == 0 else (COLS[r[0]] if j in (0, 2) else WHITE)
                tb.add(Text(s, font=FONT, font_size=24 if i == 0 else 28, color=col).move_to([xs[j], -1.7 - i * 0.6, 0]))
        self.play(LaggedStart(*[FadeIn(t) for t in tb], lag_ratio=0.03), run_time=1.6)
        tot = para("Tổng: 23 bit thay vì 33 (tiết kiệm 30%), trung bình 2,09 bit/ký tự", 24, GOLD, y=-5.6)
        self.play(FadeIn(tot), run_time=0.6)
        self.wait(4.0)
        self.play(FadeOut(tb), FadeOut(tot), FadeOut(m), run_time=0.5)

        # ===== 4. Mã hóa + giải mã =====
        c = swap_cap(self, c, cap("Mã hóa và giải mã", 42, GOLD))
        groups = VGroup(*[Text(CODE[ch], font=FONT, font_size=30, color=COLS[ch]) for ch in WORD]).arrange(RIGHT, buff=0.14)
        fitw(groups, 7.8).move_to([0, -0.6, 0])
        lab = para("ABRACADABRA →", 28, WHITE, y=0.0)
        lab.move_to([0, 0.05, 0])
        self.play(FadeIn(lab), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(g) for g in groups], lag_ratio=0.12), run_time=1.6)
        self.wait(1.5)
        raw = Text(ENC, font=FONT, font_size=30, color=WHITE)
        fitw(raw, 7.8).move_to([0, -1.5, 0])
        rl = para("Bỏ khoảng trắng, chỉ còn chuỗi bit:", 24, DIM, y=-2.2)
        self.play(FadeIn(raw), run_time=0.6)
        self.wait(1.0)
        rl.move_to([0, -2.2, 0])
        self.play(FadeIn(rl), run_time=0.4)
        self.wait(1.0)
        # giải mã 4 ký tự đầu bằng con trỏ trên cây
        dl = Text("Giải mã:", font=FONT, font_size=26, color=DIM).move_to([-3.0, -3.2, 0])
        self.play(FadeIn(dl), run_time=0.3)
        ptr = Dot([*POS[ROOT], 0], color=WHITE, radius=0.13)
        self.play(FadeIn(ptr), run_time=0.3)
        pos_i = 0
        outs = VGroup()
        for si, code in enumerate(steps[:5]):
            node_ = ROOT
            for bit in code:
                raw[pos_i].set_color(GOLD)
                node_ = KIDS[node_][int(bit)]
                self.play(ptr.animate.move_to([*POS[node_], 0]), run_time=0.35)
                pos_i += 1
            ch = node_
            t = Text(ch, font=FONT, font_size=34, color=COLS[ch]).move_to([-1.8 + si * 0.6, -3.2, 0])
            self.play(FadeIn(t, scale=1.4), Flash(nodes[ch], color=COLS[ch], flash_radius=0.6), run_time=0.45)
            outs.add(t)
            self.play(ptr.animate.move_to([*POS[ROOT], 0]), run_time=0.3)
        rest = VGroup(*[Text(ch, font=FONT, font_size=34, color=COLS[ch]).move_to([-1.8 + (5 + i) * 0.6, -3.2, 0]) for i, ch in enumerate(WORD[5:])])
        self.play(LaggedStart(*[FadeIn(t) for t in rest], lag_ratio=0.15), raw.animate.set_color(GOLD), run_time=1.2)
        self.play(FadeOut(ptr), run_time=0.3)
        pf = para("Không cần dấu phân cách: ký tự chỉ nằm ở lá,\nnên không mã nào là tiền tố của mã khác (prefix-free).", 24, WHITE, y=-4.6)
        self.play(FadeIn(pf), run_time=0.6)
        self.wait(4.0)
        wipe(self, keep=[c])

        # ===== 5. Vì sao tối ưu + ứng dụng =====
        c = swap_cap(self, c, cap("Vì sao tham lam lại tối ưu?", 40, GOLD))
        pts = VGroup(*[Text(s, font=FONT, font_size=28, color=col) for s, col in [
            ("Số bit = Σ tần suất × độ sâu của lá", WHITE),
            ("Hai ký tự hiếm nhất nên nằm sâu nhất,", BLUE),
            ("làm hai lá anh em: đổi chỗ không làm tổng tăng", BLUE),
            ("Gộp chúng thành một ký tự mới, bài toán", GREEN),
            ("nhỏ đi một ký tự: lặp lại (quy nạp)", GREEN),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        fitw(pts, 7.8).move_to([0, 3.6, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.2) for m in pts], lag_ratio=0.5), run_time=3.0)
        self.wait(3.5)
        ap = para("Huffman có mặt trong ZIP/gzip (DEFLATE),\nPNG, JPEG, MP3", 28, GOLD, y=0.2)
        self.play(FadeIn(ap), run_time=0.6)
        self.wait(2.0)
        sm = VGroup(*[Text(s, font=FONT, font_size=28, color=col) for s, col in [
            ("1. Đếm tần suất", WHITE),
            ("2. Gộp hai nút nhẹ nhất đến khi còn một cây", WHITE),
            ("3. Trái = 0, phải = 1: đường đi đến lá là mã", WHITE),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        fitw(sm, 7.8).move_to([0, -2.0, 0])
        self.play(LaggedStart(*[FadeIn(m) for m in sm], lag_ratio=0.4), run_time=1.8)
        self.wait(5.0)
