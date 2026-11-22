from common import *
from math import gcd
import random

# ---------- Toán ----------
def nz(n):                      # song ánh ℕ = {1,2,...} → ℤ
    return n // 2 if n % 2 == 0 else -(n - 1) // 2


ZL = [nz(n) for n in range(1, 10)]
assert ZL == [0, 1, -1, 2, -2, 3, -3, 4, -4]
assert len({nz(n) for n in range(1, 2001)}) == 2000 and set(range(-999, 1001)) == {nz(n) for n in range(1, 2001)}

ZZ = []
for s in range(2, 7):
    ps = range(1, s) if s % 2 == 1 else range(s - 1, 0, -1)
    for p in ps:
        ZZ.append((p, s - p))
assert len(ZZ) == 15
RED_Q = [(p, q) for p, q in ZZ if gcd(p, q) == 1]
SKIP = [(p, q) for p, q in ZZ if gcd(p, q) > 1]
assert SKIP == [(2, 2), (4, 2), (3, 3), (2, 4)]
QLIST = ["%d/%d" % t for t in RED_Q]
assert QLIST == ["1/1", "1/2", "2/1", "3/1", "1/3", "1/4", "2/3", "3/2", "4/1", "5/1", "1/5"]
assert len({p / q for p, q in RED_Q}) == len(RED_Q)

rnd = random.Random(7)
ROWS = [[rnd.randint(0, 1) for _ in range(10)] for _ in range(8)]
DIAG = [ROWS[k][k] for k in range(8)]
NEW = [1 - b for b in DIAG]
for k in range(8):
    assert NEW[k] != ROWS[k][k] and NEW != ROWS[k][:8]

DEC = ["0,1415926…", "0,5000000…", "0,7182818…", "0,3333333…"]
digs = [d[2 + k] for k, d in enumerate(DEC)]
assert digs == ["1", "0", "8", "3"]
DNEW = "0," + "".join("4" if x == "5" else "5" for x in digs) + "…"
assert DNEW == "0,5555…"
DEC = ["0,1415926…", "0,5500000…", "0,7152818…", "0,3335333…"]
digs = [d[2 + k] for k, d in enumerate(DEC)]
assert digs == ["1", "5", "5", "5"]
DNEW = "0," + "".join("4" if x == "5" else "5" for x in digs) + "…"
assert DNEW == "0,5444…"
assert all(DNEW[2 + k] != DEC[k][2 + k] for k in range(4))

HALT = [[1, 0, 1, 1, 0], [0, 0, 1, 0, 1], [1, 1, 1, 0, 0], [0, 1, 0, 1, 1], [1, 0, 0, 1, 0]]
HD = [1 - HALT[k][k] for k in range(5)]
assert HD == [0, 1, 0, 0, 1] and all(HD[k] != HALT[k][k] for k in range(5))
SUB = "₁₂₃₄₅₆₇₈₉"


def cell(txt, p, w=0.55, h=0.5, col=WHITE, size=26, stroke=DIM):
    r = Rectangle(width=w, height=h, color=stroke, stroke_width=1.5).move_to([p[0], p[1], 0])
    return VGroup(r, Text(txt, font=FONT, font_size=size, color=col).move_to(r))


class Cantor(Scene):
    def wait(self, duration=1.0, **kw):
        super().wait(duration * 1.75, **kw)

    def construct(self):
        # ===== 1. Mở đầu =====
        c = cap("Lực lượng của tập vô hạn", 40)
        t1 = Text("Đường chéo\nCantor", font=FONT, font_size=84, color=GOLD, line_spacing=1.0).move_to([0, 1.8, 0])
        t2 = para("Có vô hạn \"lớn hơn\" vô hạn không?", 32, y=-0.6)
        self.play(FadeIn(c), Write(t1), run_time=1.2)
        self.play(FadeIn(t2), run_time=0.8)
        self.wait(2.5)
        self.play(FadeOut(t1), FadeOut(t2), run_time=0.5)

        # ===== 2. Đếm được = xếp hàng được; ℕ ↔ ℤ =====
        c = swap_cap(self, c, cap("Đếm được = xếp được thành một hàng", 36, GOLD))
        d = para("Tập A đếm được nếu có thể đánh số các phần tử\nthành a₁, a₂, a₃, … mà không bỏ sót phần tử nào", 26, WHITE, y=5.0)
        self.play(FadeIn(d), run_time=0.7)
        self.wait(2.0)
        q = para("ℤ có \"gấp đôi\" ℕ không?", 32, GOLD, y=3.6)
        self.play(FadeIn(q), run_time=0.5)
        self.wait(1.2)
        top = VGroup(*[cell(str(n), (-3.6 + (n - 1) * 0.9, 2.4), 0.75, 0.6, BLUE, 28) for n in range(1, 10)])
        bot = VGroup(*[cell(str(z).replace("-", "−"), (-3.6 + i * 0.9, 0.8), 0.75, 0.6, GOLD, 28) for i, z in enumerate(ZL)])
        lab1 = Text("ℕ", font=FONT, font_size=30, color=BLUE).move_to([-3.6, 3.2, 0])
        lab2 = Text("ℤ", font=FONT, font_size=30, color=GOLD).move_to([-3.6, 0.0, 0])
        self.play(FadeIn(top), FadeIn(lab1), run_time=0.6)
        arrows = VGroup()
        for i in range(9):
            a = Arrow(top[i].get_bottom(), bot[i].get_top(), buff=0.05, color=DIM, stroke_width=3, max_tip_length_to_length_ratio=0.25)
            arrows.add(a)
            self.play(GrowArrow(a), FadeIn(bot[i]), run_time=0.3)
        self.play(FadeIn(lab2), run_time=0.3)
        r = para("0, 1, −1, 2, −2, 3, −3, …  mỗi số nguyên có đúng một số thứ tự", 24, WHITE, y=-0.9)
        self.play(FadeIn(r), run_time=0.6)
        self.wait(2.0)
        f = para("n chẵn → n/2,   n lẻ → −(n − 1)/2:  một song ánh ℕ → ℤ", 26, GOLD, y=-1.8)
        self.play(FadeIn(f), run_time=0.6)
        self.wait(2.0)
        k = para("Với tập vô hạn, \"tập con thật sự\" vẫn có thể cùng lực lượng", 24, DIM, y=-2.8)
        self.play(FadeIn(k), run_time=0.5)
        self.wait(2.5)
        wipe(self, keep=[c])

        # ===== 2b. Khách sạn Hilbert =====
        c = swap_cap(self, c, cap("Khách sạn Hilbert", 44, GOLD))
        h0 = para("Khách sạn có vô hạn phòng 1, 2, 3, … và đã kín chỗ", 26, WHITE, y=5.1)
        self.play(FadeIn(h0), run_time=0.6)
        rooms = VGroup(*[cell(str(n), (-3.5 + (n - 1) * 0.88, 3.6), 0.78, 0.7, BLUE, 26, BLUE) for n in range(1, 9)])
        guests = VGroup(*[Dot(rooms[i].get_center() + DOWN * 0.75, radius=0.14, color=GOLD) for i in range(8)])
        self.play(FadeIn(rooms), FadeIn(guests), run_time=0.8)
        self.wait(1.5)
        h1 = para("Một khách mới đến: khách phòng n chuyển sang phòng n + 1", 24, WHITE, y=1.9)
        self.play(FadeIn(h1), run_time=0.5)
        self.play(*[guests[i].animate.shift(RIGHT * 0.88) for i in range(8)], run_time=1.0)
        nd = Dot(rooms[0].get_center() + DOWN * 0.75, radius=0.14, color=GREEN)
        self.play(FadeIn(nd, scale=2), run_time=0.5)
        h2 = para("Phòng 1 trống cho khách mới: |ℕ| + 1 = |ℕ|", 26, GREEN, y=1.0)
        self.play(FadeIn(h2), run_time=0.5)
        self.wait(2.0)
        rooms2 = VGroup(*[cell(str(n), (-3.5 + (n - 1) * 0.88, -0.6), 0.78, 0.7, BLUE, 26, BLUE) for n in range(1, 9)])
        h3 = para("Vô hạn khách mới đến: khách phòng n chuyển sang phòng 2n", 24, WHITE, y=0.2)
        self.play(FadeIn(rooms2), FadeIn(h3), run_time=0.6)
        g2 = VGroup(*[Dot(rooms2[2 * i + 1].get_center() + DOWN * 0.75, radius=0.14, color=GOLD) for i in range(4)])
        self.play(LaggedStart(*[FadeIn(d_, shift=DOWN * 0.3) for d_ in g2], lag_ratio=0.2), run_time=0.8)
        g3 = VGroup(*[Dot(rooms2[2 * i].get_center() + DOWN * 0.75, radius=0.14, color=GREEN) for i in range(4)])
        self.play(LaggedStart(*[FadeIn(d_, scale=2) for d_ in g3], lag_ratio=0.2), run_time=0.8)
        h4 = para("Các phòng lẻ 1, 3, 5, … trống hết cho khách mới:\nsố chẵn và số tự nhiên \"nhiều như nhau\"", 24, GREEN, y=-2.6)
        self.play(FadeIn(h4), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 3. ℚ đếm được: đường zigzag =====
        c = swap_cap(self, c, cap("Ngay cả ℚ cũng đếm được", 40, GOLD))
        P = {}
        grid = VGroup()
        for p in range(1, 6):
            for qq in range(1, 6):
                P[(p, qq)] = np.array([-2.4 + (qq - 1) * 1.2, 4.5 - (p - 1) * 1.1, 0])
                grid.add(Text(f"{p}/{qq}", font=FONT, font_size=28).move_to(P[(p, qq)]))
        rl = Text("tử số ↓", font=FONT, font_size=20, color=DIM).move_to([-3.6, 4.5, 0])
        cl = Text("mẫu số →", font=FONT, font_size=20, color=DIM).move_to([2.4, 5.3, 0])
        self.play(FadeIn(grid, lag_ratio=0.02), FadeIn(rl), FadeIn(cl), run_time=1.2)
        e = para("Mọi phân số dương p/q đều nằm ở đâu đó trong bảng vô hạn này", 24, WHITE, y=-1.0)
        self.play(FadeIn(e), run_time=0.5)
        self.wait(1.5)
        e2 = para("Đi theo từng hàng thì không bao giờ xuống được hàng 2.\nĐi theo đường chéo thì đến được mọi ô.", 24, DIM, y=-2.0)
        self.play(FadeIn(e2), run_time=0.5)
        self.wait(1.5)
        idx = 0
        nums = VGroup()
        lst = []
        for i, t in enumerate(ZZ):
            if i:
                self.play(Create(Line(P[ZZ[i - 1]], P[t], buff=0.38, color=BLUE, stroke_width=3).set_z_index(-1)), run_time=0.25)
            g = grid[(t[0] - 1) * 5 + t[1] - 1]
            if t in SKIP:
                self.play(g.animate.set_color(RED).set_opacity(0.35), run_time=0.25)
            else:
                idx += 1
                self.play(g.animate.set_color(GOLD), run_time=0.2)
                n = Text(str(idx), font=FONT, font_size=18, color=GREEN).move_to(P[t] + np.array([-0.05, 0.36, 0]))
                nums.add(n)
                self.add(n)
        self.wait(1.0)
        s = para("Bỏ qua phân số không tối giản (2/2, 4/2, 3/3, 2/4 …)\nvì đã gặp giá trị đó rồi", 24, RED, y=-3.2)
        self.play(FadeIn(s), run_time=0.5)
        self.wait(1.5)
        l = para(", ".join(QLIST) + ", …", 26, GOLD, y=-4.4)
        self.play(FadeIn(l), run_time=0.6)
        self.wait(1.5)
        l2 = para("Thêm 0 và các số âm xen kẽ như với ℤ: |ℚ| = |ℕ| = ℵ₀", 26, WHITE, y=-5.3)
        self.play(FadeIn(l2), run_time=0.5)
        self.wait(3.0)
        wipe(self, keep=[c])

        # ===== 4. Đường chéo trên dãy nhị phân =====
        c = swap_cap(self, c, cap("Dãy nhị phân vô hạn: thử liệt kê", 38, GOLD))
        g0 = para("Giả sử có một danh sách s₁, s₂, s₃, … chứa MỌI dãy 0/1 vô hạn", 24, WHITE, y=5.3)
        self.play(FadeIn(g0), run_time=0.6)
        cells = {}
        rows = VGroup()
        for i in range(8):
            rlab = Text("s" + SUB[i], font=FONT, font_size=26, color=BLUE).move_to([-3.4, 4.3 - i * 0.62, 0])
            row = VGroup(rlab)
            for j in range(10):
                cc = cell(str(ROWS[i][j]), (-2.6 + j * 0.6, 4.3 - i * 0.62), 0.55, 0.52, WHITE, 24)
                cells[(i, j)] = cc
                row.add(cc)
            row.add(Text("…", font=FONT, font_size=26, color=DIM).move_to([3.5, 4.3 - i * 0.62, 0]))
            rows.add(row)
        self.play(LaggedStart(*[FadeIn(r_) for r_ in rows], lag_ratio=0.15), run_time=1.8)
        vd = Text("⋮", font=FONT, font_size=30, color=DIM).move_to([-3.4, -0.7, 0])
        self.play(FadeIn(vd), run_time=0.3)
        self.wait(1.0)
        e = para("Nhìn đường chéo: bit thứ k của dãy thứ k", 26, GOLD, y=-1.4)
        self.play(FadeIn(e), run_time=0.5)
        boxes = VGroup()
        for k in range(8):
            b = SurroundingRectangle(cells[(k, k)], color=GOLD, buff=0.02, stroke_width=4)
            boxes.add(b)
            self.play(Create(b), cells[(k, k)][1].animate.set_color(GOLD), run_time=0.25)
        self.wait(1.2)
        e2 = para("Lật từng bit đường chéo (0 ↔ 1) để được dãy mới d:", 26, WHITE, y=-2.3)
        self.play(FadeIn(e2), run_time=0.5)
        dl = Text("d", font=FONT, font_size=30, color=GREEN).move_to([-3.4, -3.2, 0])
        drow = VGroup(*[cell(str(NEW[j]), (-2.6 + j * 0.6, -3.2), 0.55, 0.52, GREEN, 24, GREEN) for j in range(8)])
        self.play(FadeIn(dl), run_time=0.3)
        for j in range(8):
            self.play(TransformFromCopy(cells[(j, j)], drow[j]), run_time=0.3)
        self.add(Text("…", font=FONT, font_size=26, color=DIM).move_to([2.3, -3.2, 0]))
        self.wait(1.2)
        msg = para("", 26, RED, y=-4.3)
        self.add(msg)
        for k in range(4):
            nm = para(f"d ≠ s{SUB[k]}: khác nhau ở bit thứ {k + 1}", 26, RED, y=-4.3)
            self.play(Transform(msg, nm), rows[k][0].animate.set_color(RED), Indicate(cells[(k, k)], color=RED), Indicate(drow[k], color=RED), run_time=0.7)
            self.wait(0.6)
        nm = para("… d khác MỌI dãy trong danh sách", 28, RED, y=-4.3)
        self.play(Transform(msg, nm), run_time=0.5)
        self.wait(1.5)
        cn = para("Mâu thuẫn: danh sách không chứa hết.\nTập các dãy 0/1 vô hạn KHÔNG đếm được.", 28, GOLD, y=-5.4)
        self.play(FadeIn(cn), run_time=0.6)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 5. Sang số thực =====
        c = swap_cap(self, c, cap("Cùng ý tưởng với số thực trong (0, 1)", 36, GOLD))
        ds = VGroup()
        for i, s_ in enumerate(DEC):
            t = Text(f"r{SUB[i]} = " + s_, font=FONT, font_size=32).move_to([0, 4.6 - i * 0.8, 0])
            ds.add(t)
        self.play(LaggedStart(*[FadeIn(t) for t in ds], lag_ratio=0.2), run_time=1.2)
        for i, t in enumerate(ds):
            t[len(f"r{SUB[i]}=") + 2 + i].set_color(GOLD)
        self.wait(1.0)
        rule = para("Quy tắc: chữ số đường chéo là 5 thì đổi thành 4, khác 5 thì đổi thành 5", 24, WHITE, y=1.2)
        self.play(FadeIn(rule), run_time=0.5)
        self.wait(1.5)
        nw = para("x = " + DNEW, 36, GREEN, y=0.2)
        self.play(FadeIn(nw), run_time=0.6)
        self.wait(1.5)
        w = para("(Chỉ dùng 4 và 5 để tránh trường hợp 0,4999… = 0,5)", 22, DIM, y=-0.6)
        self.play(FadeIn(w), run_time=0.5)
        self.wait(1.5)
        cmp_ = VGroup(*[Text(s, font=FONT, font_size=30, color=col) for s, col in [
            ("|ℕ| = |ℤ| = |ℚ| = ℵ₀", BLUE), ("|ℕ| < |ℝ|", GOLD), ("dãy 0/1 ↔ tập con của ℕ:  |ℕ| < |P(ℕ)|", WHITE)]]).arrange(DOWN, buff=0.4)
        fitw(cmp_).move_to([0, -2.4, 0])
        self.play(LaggedStart(*[FadeIn(m) for m in cmp_], lag_ratio=0.5), run_time=1.8)
        self.wait(2.0)
        tw = para("Định lý Cantor: |A| < |P(A)| với mọi A,\nnên có vô số \"cỡ\" vô hạn khác nhau", 24, DIM, y=-4.4)
        self.play(FadeIn(tw), run_time=0.5)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 6. Bài toán dừng =====
        c = swap_cap(self, c, cap("Đường chéo trong tin học: bài toán dừng", 34, GOLD))
        p1 = para("Mỗi chương trình là một chuỗi ký tự hữu hạn,\nnên các chương trình đếm được: P₁, P₂, P₃, …", 26, WHITE, y=5.1)
        self.play(FadeIn(p1), run_time=0.6)
        self.wait(2.0)
        p2 = para("Bảng: hàng = chương trình, cột = đầu vào; 1 = dừng, 0 = chạy mãi", 24, DIM, y=3.9)
        self.play(FadeIn(p2), run_time=0.5)
        hc = {}
        tb = VGroup()
        for j in range(5):
            tb.add(Text(str(j + 1), font=FONT, font_size=22, color=DIM).move_to([-1.6 + j * 0.8, 3.2, 0]))
        for i in range(5):
            tb.add(Text("P" + SUB[i], font=FONT, font_size=26, color=BLUE).move_to([-2.6, 2.5 - i * 0.7, 0]))
            for j in range(5):
                cc = cell(str(HALT[i][j]), (-1.6 + j * 0.8, 2.5 - i * 0.7), 0.7, 0.6, WHITE, 26)
                hc[(i, j)] = cc
                tb.add(cc)
        self.play(FadeIn(tb), run_time=0.8)
        self.play(*[hc[(k, k)][1].animate.set_color(GOLD) for k in range(5)], *[Create(SurroundingRectangle(hc[(k, k)], color=GOLD, buff=0.02)) for k in range(5)], run_time=0.8)
        d1 = para("Giả sử có chương trình H đoán đúng mọi ô của bảng.\nDựng D: trên đầu vào n, D làm NGƯỢC với ô (n, n).", 24, WHITE, y=-1.2)
        self.play(FadeIn(d1), run_time=0.6)
        self.wait(2.0)
        drow = VGroup(Text("D", font=FONT, font_size=26, color=GREEN).move_to([-2.6, -2.6, 0]),
                      *[cell(str(HD[j]), (-1.6 + j * 0.8, -2.6), 0.7, 0.6, GREEN, 26, GREEN) for j in range(5)])
        self.play(FadeIn(drow), run_time=0.7)
        self.wait(1.5)
        d2 = para("D cũng là một chương trình nên phải trùng\nvới một hàng nào đó, chẳng hạn hàng k.\nNhưng D khác hàng k ở ô (k, k): mâu thuẫn!", 26, RED, y=-4.1)
        self.play(FadeIn(d2), run_time=0.6)
        self.wait(2.5)
        d3 = para("Vậy không có chương trình H nào như thế:\nbài toán dừng không giải được (Turing, 1936)", 26, GOLD, y=-5.7)
        self.play(FadeIn(d3), run_time=0.5)
        self.wait(3.5)
        wipe(self, keep=[c])

        # ===== 7. Tóm tắt =====
        c = swap_cap(self, c, cap("Tóm tắt", 44, GOLD))
        sm = VGroup(*[Text(s, font=FONT, font_size=30, color=col, line_spacing=1.1) for s, col in [
            ("Đếm được: liệt kê thành dãy,\nkhông sót phần tử nào", WHITE),
            ("ℕ, ℤ, ℚ đều đếm được\n(cùng lực lượng ℵ₀)", BLUE),
            ("Đường chéo: từ danh sách bất kỳ,\ndựng một phần tử nằm ngoài danh sách", GOLD),
            ("⇒ dãy 0/1, P(ℕ), ℝ không đếm được", GOLD),
            ("Cùng kỹ thuật: bài toán dừng\nkhông giải được", GREEN),
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        fitw(sm, 7.8).move_to([0, 1.6, 0])
        self.play(LaggedStart(*[FadeIn(m, shift=RIGHT * 0.2) for m in sm], lag_ratio=0.5), run_time=3.0)
        self.wait(6.0)
