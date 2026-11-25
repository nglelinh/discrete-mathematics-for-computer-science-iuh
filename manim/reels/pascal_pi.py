"""Từ tam giác Pascal ra π (chuỗi Nilakantha), reel dài ~3,5 phút, VI/EN, không LaTeX.
Render: REEL_LANG=vi manim -qh pascal_pi.py PascalPi   (en: REEL_LANG=en). FAST=1 để xem nhanh.
VO_LOG=file.json ghi mốc thời gian các mục/caption; PASCAL_PADS=file.json = {"k": giây} thêm khoảng dừng cuối mục k."""
import os, json, glob, textwrap
from common import *
import manimpango
if "DejaVu Sans" not in manimpango.list_fonts():  # macOS: lấy DejaVu từ matplotlib của miniconda
    for _f in ("DejaVuSans.ttf",):
        for _p in glob.glob(os.path.expanduser("~/miniconda3/lib/python3*/site-packages/matplotlib/mpl-data/fonts/ttf/" + _f))[:1]:
            manimpango.register_font(_p)
from math import comb, pi as PI, log10
from fractions import Fraction
import mpmath as mp

LANG = os.environ.get("REEL_LANG", "vi"); VI = LANG == "vi"
config.frame_rate = 30
if os.environ.get("FAST"):
    config.pixel_width, config.pixel_height, config.frame_rate = 540, 960, 10
mp.mp.dps = 40


def L(vi, en):
    return vi if VI else en


def nf(x, d):
    s = "%.*f" % (d, x)
    return s.replace(".", ",") if VI else s


# ---------------- toán học, kiểm tra bằng assert khi import ----------------
N = 12                                         # số hàng tam giác: 0..12
DEN = [comb(2 * k + 2, 3) for k in range(1, 11)]
assert DEN == [4, 20, 56, 120, 220, 364, 560, 816, 1140, 1540]
D3 = [comb(n, 3) for n in range(3, N + 1)]
assert D3 == [1, 4, 10, 20, 35, 56, 84, 120, 165, 220]
assert [comb(n, 2) for n in range(2, 8)] == [1, 3, 6, 10, 15, 21]
assert comb(6, 3) == 20 == 1 + 3 + 6 + 10      # gậy khúc côn cầu
assert all(comb(n, 3) == sum(comb(j, 2) for j in range(2, n)) for n in range(3, 40))
assert all(comb(n, k) == comb(n - 1, k - 1) + comb(n - 1, k) for n in range(2, 30) for k in range(1, n))
for k in range(1, 400):                        # đồng nhất thức mẫu số
    assert Fraction(4, 2 * k * (2 * k + 1) * (2 * k + 2)) == Fraction(2, 3) / comb(2 * k + 2, 3)
for m in range(1, 200):                        # tách phân thức đơn giản
    assert Fraction(4, m * (m + 1) * (m + 2)) == Fraction(2, m) - Fraction(4, m + 1) + Fraction(2, m + 2)
assert Fraction(4, 24) == Fraction(1, 6) == Fraction(2, 2) - Fraction(4, 3) + Fraction(2, 4)


def term(k):
    return mp.mpf(4) / (2 * k * (2 * k + 1) * (2 * k + 2))


def SN(n):                                     # tổng riêng Nilakantha
    return 3 + sum((-1) ** (k + 1) * term(k) for k in range(1, n + 1))


def SL(n):                                     # tổng riêng Leibniz (n số hạng) nhân 4
    return 4 * sum(mp.mpf(-1) ** j / (2 * j + 1) for j in range(n))


for n in range(1, 60):                         # co lại: (1+1/2) - (1/2+1/3) + ... = 1 + (-1)^(n+1)/(n+1)
    t = sum(Fraction((-1) ** (k + 1)) * (Fraction(1, k) + Fraction(1, k + 1)) for k in range(1, n + 1))
    assert t == 1 + Fraction((-1) ** (n + 1), n + 1)
assert abs(sum((-1) ** (k + 1) * (mp.mpf(1) / (2 * k + 1)) for k in range(1, 20001)) - (1 - mp.pi / 4)) < 1e-4
assert abs(SN(2000) - mp.pi) < 4e-11
for k in range(1, 40):                         # đan dấu, sai số nhỏ hơn số hạng kế tiếp, S(k) lên xuống quanh π
    e = SN(k) - mp.pi
    assert abs(e) < term(k + 1) + mp.mpf(10) ** -30 and (e > 0) == (k % 2 == 1)
assert abs(abs(SN(1000) - mp.pi) * 1000 ** 3 - 0.25) < 0.01      # sai số ≈ 1/(4k³)
assert abs(abs(SL(1000) - mp.pi) * 1000 - 1) < 0.01              # sai số Leibniz ≈ 1/k
K10 = next(k for k in range(1, 5000) if abs(SN(k) - mp.pi) < 5e-11)
assert K10 == 1709

PI_STR = nf(float(mp.pi), 12)                  # 3.141592653590
S_TAB = [float(SN(k)) for k in range(0, 11)]
KS = sorted(set(int(10 ** x) for x in np.linspace(0, log10(2000), 80)))
_cs = np.cumsum([(-1) ** (k + 1) * 4 / (2 * k * (2 * k + 1) * (2 * k + 2)) for k in range(1, 2001)]) + 3
_cl = 4 * np.cumsum([(-1.0) ** j / (2 * j + 1) for j in range(2000)])
assert abs(_cs[-1] - float(SN(2000))) < 1e-13 and abs(_cl[-1] - float(SL(2000))) < 1e-12
ERR_N = {k: abs(_cs[k - 1] - PI) for k in KS}
ERR_L = {k: abs(_cl[k - 1] - PI) for k in KS}
ROWS_K = (10, 100, 1000, 2000)
SECS = {1: ("Tam giác Pascal", "Pascal's triangle"), 2: ("Các đường chéo của tam giác", "The diagonals"),
        3: ("Cách một số: C(2k+2, 3)", "Every other entry: C(2k+2, 3)"), 4: ("Chuỗi Nilakantha", "The Nilakantha series"),
        5: ("Vì sao tổng này bằng π?", "Why does the sum equal π?"), 6: ("Hội tụ nhanh đến đâu?", "How fast does it converge?"),
        7: ("Ghi nhớ", "Takeaway")}
_PADP = os.environ.get("PASCAL_PADS") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "vo", "pascal_pi_pads.json")
PADS = {int(k): v for k, v in json.load(open(_PADP)).items()} if VI and os.path.exists(_PADP) else {}

SKY, MINT, ORANGE, PINK = BLUE, GREEN, "#ffa94d", "#ff8ec7"


def frac(n, d, size=26, color=WHITE):
    a, b = Text(n, font=FONT, font_size=size, color=color), Text(d, font=FONT, font_size=size, color=color)
    w = max(a.width, b.width) + 0.12
    ln = Line(LEFT * w / 2, RIGHT * w / 2, color=color, stroke_width=2.2)
    a.next_to(ln, UP, buff=0.06); b.next_to(ln, DOWN, buff=0.06)
    return VGroup(a, ln, b)


def row(*parts, buff=0.14, w=7.8):
    g = VGroup(*parts).arrange(RIGHT, buff=buff)
    if g.width > w:
        g.scale_to_fit_width(w)
    return g


def T(s, size=26, color=WHITE):
    return Text(s, font=FONT, font_size=size, color=color)


def digits(s, ref, size=24, base=WHITE):
    t = Text(s, font=FONT, font_size=size, color=base)
    n = 0
    for a, b in zip(s, ref):
        if a != b:
            break
        n += 1
    ch = [c for c in s if not c.isspace()]
    for i in range(min(n, len(ch))):
        t[i].set_color(GOLD)
    return t


def pos(n, k, DX=0.6, DY=0.52, TOP=4.85):
    return np.array([(k - n / 2) * DX, TOP - n * DY, 0])


class PascalPi(Scene):
    # ---------- hạ tầng: caption dưới, mục, log ----------
    def setup(self):
        self._ev = []; self._sec = 0; self.cm = None; self.titlem = None; self._until = 0.0

    def _log(self, kind, val):
        self._ev.append([round(self.renderer.time, 3), kind, val])

    def settle(self):
        rest = self._until - self.renderer.time
        if rest > 0.01:
            self.wait(rest)

    def sec(self, i):
        self.settle()
        if self._sec and PADS.get(self._sec, 0) > 0:
            self.wait(PADS[self._sec])
        self._sec = i; self._log("stage", i)
        new = cap(L(*SECS[i]), 36, GOLD if i in (3, 4) else WHITE)
        if self.titlem is None:
            self.play(FadeIn(new), run_time=0.4)
        else:
            self.play(ReplacementTransform(self.titlem, new), run_time=0.45)
        self.titlem = new

    def say(self, vi, en, nar, hold=None, size=27):
        """vi/en = phụ đề trên màn hình (ngắn); nar = lời thoại tiếng Việt (để lồng tiếng), quyết định thời gian giữ."""
        self.settle()
        t = L(vi, en); self._log("say", [t, nar])
        m = para(textwrap.fill(t, 40), size, WHITE, y=-5.45)
        if m.get_top()[1] > -4.55:
            m.shift(DOWN * (m.get_top()[1] + 4.55))
        if self.cm is None:
            self.play(FadeIn(m), run_time=0.35)
        else:
            self.play(FadeOut(self.cm), FadeIn(m), run_time=0.35)
        self.cm = m
        self._until = self.renderer.time + (hold if hold is not None else max(max(1.8, 1.0 + 0.052 * len(t)), len(nar) / 13.0 + 0.3))

    def clear_cap(self):
        self.settle()
        if self.cm is not None:
            self.play(FadeOut(self.cm), run_time=0.3); self.cm = None

    def wipe_keep(self, keep=()):
        wipe(self, keep=[self.titlem] + list(keep) + ([self.cm] if self.cm else []), rt=0.5)

    def tear_down(self):
        self.settle()
        if self._sec and PADS.get(self._sec, 0) > 0:
            self.wait(PADS[self._sec])
        self._log("end", None)
        if os.environ.get("VO_LOG"):
            json.dump(self._ev, open(os.environ["VO_LOG"], "w"), ensure_ascii=False, indent=0)

    # ---------- dựng ----------
    def construct(self):
        cells = {}

        def mk(n, k):
            c = Circle(radius=0.24, color=DIM, stroke_width=1.6, fill_color=CELL, fill_opacity=1)
            num = Text(str(comb(n, k)), font=FONT, font_size=17, color=WHITE)
            if num.width > 0.4:
                num.scale_to_fit_width(0.4)
            g = VGroup(c, num); g.move_to(pos(n, k)); cells[(n, k)] = g
            return g
        rows = [VGroup(*[mk(n, k) for k in range(n + 1)]) for n in range(N + 1)]

        # ===== 1. Tam giác Pascal =====
        self.sec(1)
        self.say('Tam giác Pascal: hàng trên cùng là 1, mỗi hàng bắt đầu và kết thúc bằng 1.', "Pascal's triangle: the top row is 1, and every row starts and ends with 1.", 'Đây là tam giác Pascal. Hàng trên cùng chỉ có số 1, và mỗi hàng bên dưới đều bắt đầu, kết thúc bằng 1.')
        for n in range(5):
            self.play(FadeIn(rows[n], shift=DOWN * 0.12), run_time=0.6)
        self.settle()
        self.say('Số ở giữa bằng tổng hai số ngay phía trên. Ví dụ hàng 4: 3 + 3 = 6.', 'Each inner number is the sum of the two above it. Row 4: 3 + 3 = 6.', 'Số ở giữa bằng tổng hai số đứng ngay phía trên nó. Hàng ba có hai số ba, nên hàng bốn có số ba cộng ba bằng sáu.')
        for p in ((3, 1), (3, 2)):
            self.play(cells[p][0].animate.set_fill(GOLD, 0.35).set_stroke(GOLD, 2.5), run_time=0.4)
        self.play(cells[(4, 2)][0].animate.set_fill(GREEN, 0.5).set_stroke(GREEN, 2.5), Indicate(cells[(4, 2)][1], color=GREEN), run_time=0.8)
        eq = T("3 + 3 = 6", 34, GOLD).move_to([0, -0.9, 0]); self.play(FadeIn(eq), run_time=0.4)
        self.settle()
        rule = T(L("C(n, k) = C(n−1, k−1) + C(n−1, k)", "C(n, k) = C(n−1, k−1) + C(n−1, k)"), 28, WHITE).move_to([0, -2.3, 0])
        self.say('C(n, k) = C(n−1, k−1) + C(n−1, k), với C(n, k) là số cách chọn k phần tử trong n phần tử.', 'C(n, k) = C(n−1, k−1) + C(n−1, k), where C(n, k) is the number of ways to choose k items from n.', 'Viết gọn: tổ hợp chập k của n bằng tổ hợp chập k trừ một của n trừ một, cộng tổ hợp chập k của n trừ một. Số này nằm ở hàng n, vị trí k, đếm từ không.')
        self.play(FadeIn(rule), FadeOut(eq), *[cells[p][0].animate.set_fill(CELL, 1).set_stroke(DIM, 1.6) for p in ((3, 1), (3, 2), (4, 2))], run_time=0.6)
        self.settle()
        self.say('Dựng tiếp đến hàng 12. Chỉ cần phép cộng.', 'We build on to row 12. Only additions are needed.', 'Cứ thế dựng tiếp đến hàng mười hai, mà chỉ cần phép cộng.')
        self.play(LaggedStart(*[FadeIn(rows[n], shift=DOWN * 0.1) for n in range(5, N + 1)], lag_ratio=0.35), run_time=3.2)
        self.settle()
        self.play(FadeOut(rule), run_time=0.3)

        # ===== 2. Các đường chéo =====
        self.sec(2)
        diag_col = {0: SKY, 1: MINT, 2: ORANGE, 3: GOLD}
        info = {0: ("Đường chéo 0: 1, 1, 1, 1, …", "Diagonal 0: 1, 1, 1, 1, …"),
                1: ("Đường chéo 1: 1, 2, 3, 4, … (số tự nhiên)", "Diagonal 1: 1, 2, 3, 4, … (counting numbers)"),
                2: ("Đường chéo 2: 1, 3, 6, 10, 15, … (số tam giác)", "Diagonal 2: 1, 3, 6, 10, 15, … (triangular numbers)"),
                3: ("Đường chéo 3: 1, 4, 10, 20, 35, 56, …", "Diagonal 3: 1, 4, 10, 20, 35, 56, …")}
        say2 = {0: ('Mỗi đường chéo chạy xuống, song song với cạnh trái. Đường chéo 0 toàn số 1.', 'Each diagonal runs down parallel to the left edge. Diagonal 0 is all 1s.', 'Mỗi đường chéo chạy xuống, song song với cạnh trái. Đường chéo đầu tiên toàn số một.'), 1: ('Đường chéo 1 là các số tự nhiên: C(n, 1) = n.', 'Diagonal 1 is the counting numbers: C(n, 1) = n.', 'Đường chéo thứ hai là các số tự nhiên.'), 2: ('Đường chéo 2 là số tam giác 1, 3, 6, 10, … bằng C(n, 2): số cặp trong n phần tử.', 'Diagonal 2 holds the triangular numbers 1, 3, 6, 10, … equal to C(n, 2): pairs among n items.', 'Đường chéo thứ ba là số tam giác một, ba, sáu, mười, bằng số cặp chọn từ n phần tử.'), 3: ('Đường chéo 3 là C(n, 3): 1, 4, 10, 20, 35, … số bộ ba trong n phần tử. Đây là dãy ta cần.', 'Diagonal 3 is C(n, 3): 1, 4, 10, 20, 35, … triples among n items. This is the sequence we need.', 'Đường chéo tiếp theo là số bộ ba chọn từ n phần tử: một, bốn, mười, hai mươi, ba mươi lăm. Đây là dãy ta cần.')}
        lab = None
        for j in range(4):
            self.say(*say2[j])
            newl = T(L(*info[j]), 27, diag_col[j]).move_to([0, -2.4, 0])
            anims = [cells[(n, j)][0].animate.set_fill(diag_col[j], 0.4).set_stroke(diag_col[j], 2.6) for n in range(max(j, 0), N + 1)]
            self.play(*anims, (FadeIn(newl) if lab is None else ReplacementTransform(lab, newl)), run_time=0.9)
            lab = newl
            self.settle()
        self.say('Gậy khúc côn cầu: mỗi số bằng tổng các số trên đường chéo bên cạnh, ví dụ 20 = 1 + 3 + 6 + 10.', 'Hockey stick: each number is the sum along the neighbouring diagonal, e.g. 20 = 1 + 3 + 6 + 10.', 'Vì sao? Lấy số hai mươi ở hàng sáu: nó bằng một cộng ba cộng sáu cộng mười. Đó là đồng nhất thức cây gậy khúc côn cầu.')
        hs = [(2, 2), (3, 2), (4, 2), (5, 2)]
        self.play(*[cells[p][0].animate.set_fill(ORANGE, 0.9).set_stroke(WHITE, 3) for p in hs], *[cells[p][1].animate.set_color(BLACK) for p in hs],
                  cells[(6, 3)][0].animate.set_fill(GOLD, 0.95).set_stroke(WHITE, 3), cells[(6, 3)][1].animate.set_color(BLACK), run_time=1.0)
        hk = T("C(6, 3) = 20 = 1 + 3 + 6 + 10", 30, GOLD).move_to([0, -3.1, 0]); self.play(FadeIn(hk), run_time=0.5)
        hk2 = T(L("C(n, 3) = C(2, 2) + C(3, 2) + … + C(n−1, 2)", "C(n, 3) = C(2, 2) + C(3, 2) + … + C(n−1, 2)"), 26).move_to([0, -3.8, 0]); self.play(FadeIn(hk2), run_time=0.5)
        self.settle()
        self.play(FadeOut(hk), FadeOut(hk2), FadeOut(lab), run_time=0.4)

        # ===== 3. Cách một số =====
        self.sec(3)
        evens = [(n, 3) for n in (4, 6, 8, 10, 12)]
        self.say('Lấy cách một hàng: n = 4, 6, 8, 10, 12 cho 4, 20, 56, 120, 220.', 'Take every other row: n = 4, 6, 8, 10, 12 gives 4, 20, 56, 120, 220.', 'Giờ lấy dãy này cách một hàng: hàng bốn, sáu, tám, mười, mười hai, được bốn, hai mươi, năm mươi sáu, một trăm hai mươi, hai trăm hai mươi.')
        dim_anims = []
        for (n, k), g in cells.items():
            if (n, k) not in evens:
                dim_anims += [g[0].animate.set_fill(CELL, 1).set_stroke(DIM, 1.2), g[1].animate.set_color(DIM)]
        self.play(*dim_anims, run_time=0.8)
        self.play(*[cells[p][0].animate.set_fill(GOLD, 0.95).set_stroke(WHITE, 2.5) for p in evens], *[cells[p][1].animate.set_color(BLACK) for p in evens], run_time=0.8)
        self.play(*[Indicate(cells[p], color=WHITE, scale_factor=1.3) for p in evens], run_time=1.0)
        lst = T("C(2k+2, 3):  4,  20,  56,  120,  220,  …", 30, GOLD).move_to([0, -2.4, 0]); self.play(FadeIn(lst), run_time=0.5)
        self.settle()
        self.say('Cách một hàng nghĩa là n = 2k + 2, và C(2k+2, 3) = (2k+2)(2k+1)(2k) / 6.', 'Every other row means n = 2k + 2, and C(2k+2, 3) = (2k+2)(2k+1)(2k) / 6.', 'Cách một hàng nghĩa là n bằng hai k cộng hai, và số này bằng hai k cộng hai, nhân hai k cộng một, nhân hai k, chia sáu.')
        e1 = T("C(2k+2, 3) = (2k+2)(2k+1)(2k) / 6", 29).move_to([0, -3.2, 0]); self.play(FadeIn(e1), run_time=0.5)
        self.settle()
        self.say('Đảo lại: 4 chia ba số liên tiếp bằng hai phần ba chia C(2k+2, 3). Thử k = 1: cả hai vế là 1/6.', 'Flip it: 4 over three consecutive numbers equals two thirds over C(2k+2, 3). Check k = 1: both sides are 1/6.', 'Đảo lại, bốn chia ba số liên tiếp bằng hai phần ba chia số trên tam giác Pascal. Thử k bằng một: cả hai vế đều là một phần sáu.')
        self.play(FadeOut(e1), FadeOut(lst), run_time=0.4)
        idn = row(frac("4", "2k(2k+1)(2k+2)", 24), T("=", 28), frac("2", "3", 24), T("×", 28), frac("1", "C(2k+2, 3)", 24), buff=0.2).move_to([0, -2.7, 0])
        self.play(FadeIn(idn), run_time=0.6)
        chk = T("k = 1:   4/24 = 1/6   và   (2/3)/4 = 1/6", 25, GREEN).move_to([0, -3.85, 0]); self.play(FadeIn(chk), run_time=0.5)
        self.settle()
        self.clear_cap()

        # ===== 4. Chuỗi Nilakantha =====
        self.sec(4)
        self.wipe_keep()
        series = row(T("π = 3 +", 28), frac("2", "3", 24), T("(", 30), frac("1", "4", 24), T("−", 28), frac("1", "20", 24), T("+", 28), frac("1", "56", 24), T("−", 28), frac("1", "120", 24), T("+ …", 28), T(")", 30), buff=0.13)
        series.move_to([0, 4.85, 0])
        self.say('Thêm dấu cộng trừ xen kẽ ta được chuỗi Nilakantha, nhà toán học Ấn Độ, thế kỷ 15.', 'Add alternating signs and we get the series of Nilakantha, an Indian mathematician, 15th century.', 'Thêm dấu cộng trừ xen kẽ, ta có chuỗi của Nilakantha, nhà toán học Ấn Độ thế kỷ mười lăm: pi bằng ba cộng hai phần ba nhân một phần bốn trừ một phần hai mươi, và cứ thế.')
        self.play(FadeIn(series), run_time=0.8)
        self.settle()
        # bảng
        hdr = [T("k", 24, DIM), T("C(2k+2, 3)", 24, DIM), L(T("số hạng", 24, DIM), T("term", 24, DIM)), T("S(k)", 24, DIM)]
        xs = [-3.1, -1.5, 0.6, 2.9]
        for h, x in zip(hdr, xs):
            h.move_to([x, 3.55, 0])
        self.play(*[FadeIn(h) for h in hdr], run_time=0.4)
        self.say('Tính tay: k, số trên tam giác Pascal, số hạng, rồi tổng riêng S(k).', 'By hand: k, the Pascal number, the term, then the partial sum S(k).', 'Mình tính tay vài số hạng: k, số trên tam giác Pascal, số hạng hai phần ba chia số đó, và tổng riêng.')
        tab = VGroup()
        for k in range(1, 9):
            y = 3.55 - 0.55 * k
            sgn = "+" if k % 2 == 1 else "−"
            cs = [T(str(k), 24).move_to([xs[0], y, 0]), T(str(DEN[k - 1]), 24, GOLD).move_to([xs[1], y, 0]),
                  T("%s %s" % (sgn, nf(float(mp.mpf(2) / 3 / DEN[k - 1]), 6)), 24).move_to([xs[2], y, 0]),
                  T(nf(S_TAB[k], 7), 24, GREEN if k % 2 == 1 else PINK).move_to([xs[3], y, 0])]
            tab.add(*cs)
            self.play(*[FadeIn(c, shift=UP * 0.08) for c in cs], run_time=0.55)
            if k == 2:
                self.settle()
                self.say('k = 1: 3,1667. k = 2: 3,1333. Giá trị nhảy lên xuống quanh π.', 'k = 1: 3.1667. k = 2: 3.1333. The value jumps above and below π.', 'Với k bằng một được ba phẩy một sáu sáu bảy. Với k bằng hai còn ba phẩy một ba ba ba. Giá trị nhảy lên xuống quanh pi.')
        self.settle()
        self.play(FadeOut(tab), *[FadeOut(h) for h in hdr], run_time=0.5)
        # đồ thị zigzag
        ax = Axes(x_range=[0, 10.6, 1], y_range=[3.12, 3.18, 0.02], x_length=6.9, y_length=5.6,
                  axis_config={"color": DIM, "stroke_width": 2, "include_tip": False, "include_ticks": False}).move_to([0.25, 1.2, 0])
        pil = DashedLine(ax.c2p(0, PI), ax.c2p(10.6, PI), color=GOLD, stroke_width=3)
        pil_t = T("π = " + nf(PI, 5) + "…", 24, GOLD).next_to(pil, RIGHT, buff=-1.9).shift(UP * 0.28)
        ytl = [T(nf(v, 2), 20, DIM).next_to(ax.c2p(0, v), LEFT, buff=0.1) for v in (3.12, 3.14, 3.16, 3.18)]
        xtl = [T(str(v), 20, DIM).next_to(ax.c2p(v, 3.12), DOWN, buff=0.1) for v in (1, 5, 10)]
        self.say('Các điểm rơi lần lượt trên và dưới π, dao động thu hẹp dần. π luôn nằm giữa hai tổng riêng liên tiếp.', 'Points land alternately above and below π and the swings shrink. π always lies between two consecutive partial sums.', 'Vẽ ra, các điểm rơi lần lượt trên và dưới pi. Dấu đan xen, số hạng giảm dần, nên pi luôn nằm giữa hai tổng riêng liên tiếp.')
        self.play(Create(ax), Create(pil), FadeIn(pil_t), *[FadeIn(t) for t in ytl + xtl], run_time=1.0)
        pts = [ax.c2p(k, S_TAB[k]) for k in range(1, 11)]
        zig = VMobject(color=WHITE, stroke_width=2.5).set_points_as_corners(pts)
        self.play(Create(zig), run_time=2.0)
        dots = VGroup(*[Dot(p, radius=0.09, color=(GREEN if (i + 1) % 2 == 1 else PINK)) for i, p in enumerate(pts)])
        self.play(LaggedStart(*[FadeIn(d, scale=1.6) for d in dots], lag_ratio=0.12), run_time=1.4)
        self.settle()
        self.clear_cap()

        # ===== 5. Chứng minh =====
        self.sec(5)
        self.wipe_keep()
        yy = 4.6

        def lines(spec, y0=4.3, gap=1.0):
            out = []
            for i, (s, col, size) in enumerate(spec):
                out.append(T(s, size, col).move_to([0, y0 - gap * i, 0]))
                if out[-1].width > 7.8:
                    out[-1].scale_to_fit_width(7.8)
            return out

        def show(ls, rt=0.55):
            for m in ls:
                self.play(FadeIn(m, shift=UP * 0.08), run_time=rt)
        self.say('Bước 1: đặt m = 2k và tách số hạng thành phân thức đơn giản. Thử m = 2: cả hai vế là 1/6.', 'Step 1: put m = 2k and split each term into simple fractions. Test m = 2: both sides are 1/6.', 'Vì sao đúng bằng pi? Bước một: đặt m bằng hai k, tách số hạng thành phân thức đơn giản, hai trên m, trừ bốn trên m cộng một, cộng hai trên m cộng hai. Thử m bằng hai: cả hai vế là một phần sáu.')
        st1 = lines([(L("Bước 1: tách phân thức (m = 2k)", "Step 1: partial fractions (m = 2k)"), GOLD, 33),
                     ("4 / [m(m+1)(m+2)]", WHITE, 33), ("= 2/m − 4/(m+1) + 2/(m+2)", WHITE, 33),
                     (L("Thử m = 2:  4/24 = 1/6", "Test m = 2:  4/24 = 1/6"), GREEN, 29), ("2/2 − 4/3 + 2/4 = 1/6  ✓", GREEN, 29)])
        show(st1); self.settle()
        self.say('Bước 2: hai phần chẵn gom lại, cộng đan dấu thì triệt tiêu từng cặp, chỉ còn 1.', 'Step 2: group the even parts; with alternating signs they cancel in pairs and leave 1.', 'Bước hai: gom hai phần mẫu chẵn thành một trên k cộng một trên k cộng một. Cộng đan dấu thì triệt tiêu từng cặp, chỉ còn số một.')
        self.play(*[FadeOut(m) for m in st1], run_time=0.4)
        st2 = lines([(L("Bước 2: hai phần chẵn", "Step 2: the even parts"), GOLD, 33),
                     ("2/(2k) + 2/(2k+2) = 1/k + 1/(k+1)", WHITE, 31),
                     ("(1 + 1/2) − (1/2 + 1/3) + (1/3 + 1/4) − …", WHITE, 29),
                     (L("các số hạng triệt tiêu từng cặp", "terms cancel in pairs"), DIM, 26), ("= 1", GOLD, 34)])
        show(st2); self.settle()
        self.say('Bước 3: phần −4/(2k+1) bằng π − 4, nhờ chuỗi Leibniz π/4 = 1 − 1/3 + 1/5 − …', "Step 3: the −4/(2k+1) part equals π − 4, thanks to Leibniz's series π/4 = 1 − 1/3 + 1/5 − …", 'Bước ba: phần còn lại là trừ bốn trên hai k cộng một. Theo chuỗi Leibniz, nó bằng trừ bốn nhân một trừ pi chia bốn, tức pi trừ bốn.')
        self.play(*[FadeOut(m) for m in st2], run_time=0.4)
        st3 = lines([(L("Bước 3: phần −4/(2k+1)", "Step 3: the −4/(2k+1) part"), GOLD, 33),
                     ("−4 (1/3 − 1/5 + 1/7 − …)", WHITE, 33),
                     (L("Leibniz: 1 − 1/3 + 1/5 − … = π/4", "Leibniz: 1 − 1/3 + 1/5 − … = π/4"), SKY, 29),
                     (L("nên 1/3 − 1/5 + … = 1 − π/4", "so 1/3 − 1/5 + … = 1 − π/4"), SKY, 29),
                     ("−4 (1 − π/4) = π − 4", GOLD, 34)])
        show(st3); self.settle()
        self.say('1 + (π − 4) = π − 3, nên 3 + (π − 3) = π.', '1 + (π − 4) = π − 3, so 3 + (π − 3) = π.', 'Cộng lại: một cộng pi trừ bốn bằng pi trừ ba, nên ba cộng pi trừ ba đúng bằng pi.')
        self.play(*[FadeOut(m) for m in st3], run_time=0.4)
        st4 = lines([(L("Cộng ba phần:", "Add the three parts:"), GOLD, 33), ("1 + (π − 4) = π − 3", WHITE, 32), ("3 + (π − 3) = π", GOLD, 42), ("✓", GREEN, 40)], gap=1.25)
        show(st4); self.settle()
        self.clear_cap()

        # ===== 6. Tốc độ hội tụ =====
        self.sec(6)
        self.wipe_keep()
        ax2 = Axes(x_range=[0, 3.5, 1], y_range=[-11, 0.3, 2], x_length=6.6, y_length=5.0,
                   axis_config={"color": DIM, "stroke_width": 2, "include_tip": False, "include_ticks": False}).move_to([0.35, 2.0, 0])
        xl = [T(v, 20, DIM).next_to(ax2.c2p(e, -11), DOWN, buff=0.1) for e, v in ((0, "1"), (1, "10"), (2, "100"), (3, "1000"))]
        yl = [T("10⁻%d" % (-e) if e else "1", 20, DIM).next_to(ax2.c2p(0, e), LEFT, buff=0.1) for e in (-2, -4, -6, -8, -10)]
        axt = T(L("k (số số hạng)", "k (number of terms)"), 22, DIM).next_to(ax2, DOWN, buff=0.4)
        ayt = T(L("sai số |S − π|", "error |S − π|"), 22, DIM).next_to(ax2, UP, buff=0.15)
        cn = VMobject(color=GOLD, stroke_width=4).set_points_smoothly([ax2.c2p(log10(k), log10(ERR_N[k])) for k in KS])
        cl = VMobject(color=SKY, stroke_width=4).set_points_smoothly([ax2.c2p(log10(k), log10(ERR_L[k])) for k in KS])
        lg = VGroup(T("Nilakantha", 22, GOLD), T("Leibniz", 22, SKY)).arrange(RIGHT, buff=0.7).next_to(ax2, DOWN, buff=0.85)
        self.say('So với chuỗi Leibniz: sai số theo số số hạng k, trên thang log.', "Compared with Leibniz's series: error against the number of terms k, on a log scale.", 'Hội tụ nhanh đến đâu? So với chuỗi Leibniz: đường xanh hạ rất chậm, đường vàng của Nilakantha dốc hơn nhiều.')
        self.play(Create(ax2), *[FadeIn(t) for t in xl + yl], FadeIn(axt), FadeIn(ayt), run_time=1.0)
        self.play(Create(cl), run_time=1.8); self.play(Create(cn), run_time=1.8); self.play(FadeIn(lg), run_time=0.4)
        self.settle()
        self.say('Sai số Leibniz ≈ 1/k, sai số Nilakantha ≈ 1/(4k³). Tăng k gấp 10: thêm 3 chữ số so với 1.', 'Leibniz error ≈ 1/k, Nilakantha error ≈ 1/(4k³). Multiply k by 10: 3 more digits versus 1.', 'Sai số Leibniz cỡ một trên k. Nilakantha có ba thừa số dưới mẫu, và nhờ đan dấu sai số chỉ cỡ một trên bốn k mũ ba. Tăng k gấp mười, Nilakantha thêm ba chữ số, Leibniz thêm một.')
        self.settle()
        self.play(*[FadeOut(m) for m in self.mobjects if m not in (self.titlem, self.cm)], run_time=0.5)
        rs = []
        hd = row(T("k", 24, DIM), T("Nilakantha", 24, GOLD), T("Leibniz", 24, SKY), buff=1.2).move_to([0, 4.7, 0])
        xs2 = [-3.2, -0.2, 2.6]
        for t, x in zip(hd, xs2):
            t.move_to([x, 4.7, 0])
        self.add(hd)
        for i, k in enumerate(ROWS_K):
            y = 3.9 - 0.9 * i
            a = T("k = %d" % k, 24).move_to([xs2[0], y, 0])
            b = digits(nf(float(SN(k)), 11), PI_STR, 24).move_to([xs2[1], y, 0])
            c = digits(nf(float(SL(k)), 11), PI_STR, 24).move_to([xs2[2], y, 0])
            rs += [a, b, c]
        ref = T("π = " + PI_STR + "…", 24, GOLD).move_to([0.2, 0.2, 0]); rs.append(ref)
        self.say('Chữ số vàng là chữ số đã đúng. Sau 1000 số hạng: 9 chữ số thập phân so với 2.', 'Gold digits are correct. After 1000 terms: 9 correct decimals versus 2.', 'Chữ số vàng là chữ số đúng. Sau một nghìn số hạng, Nilakantha đúng chín chữ số thập phân, Leibniz mới đúng hai.')
        self.play(FadeIn(hd), LaggedStart(*[FadeIn(m) for m in rs], lag_ratio=0.12), run_time=2.2)
        self.settle()
        bnd = VGroup(T(L("Sai số ≈ 1/(4k³)", "Error ≈ 1/(4k³)"), 28, GOLD), T(L("Cần k = %d để đúng 10 chữ số" % K10, "k = %d gives 10 correct decimals" % K10), 26, WHITE),
                     T(L("Vẫn chưa phải cách tính π hiệu quả nhất", "Still not the most efficient way to compute π"), 24, DIM)).arrange(DOWN, buff=0.4).move_to([0, -1.9, 0])
        self.say('Cần k = 1709 để đúng 10 chữ số: nhanh hơn Leibniz nhiều, nhưng chưa phải cách nhanh nhất.', 'k = 1709 gives 10 correct decimals: far faster than Leibniz, but not the fastest way.', 'Công bằng mà nói, cần một nghìn bảy trăm lẻ chín số hạng mới đúng mười chữ số: nhanh hơn Leibniz nhiều, nhưng chưa phải nhanh nhất.')
        self.play(FadeIn(bnd, shift=UP * 0.1), run_time=0.8)
        self.settle()
        self.clear_cap()

        # ===== 7. Ghi nhớ =====
        self.sec(7)
        self.wipe_keep()
        pts7 = [(L("• Mỗi số trong tam giác Pascal bằng tổng hai số phía trên.", "• Each Pascal number is the sum of the two above it."), WHITE),
                (L("• C(n, 3) nằm trên đường chéo thứ tư; lấy cách một số thì có C(2k+2, 3).", "• C(n, 3) lies on the fourth diagonal; every other one is C(2k+2, 3)."), GOLD),
                (L("• 4/(2k(2k+1)(2k+2)) = (2/3) / C(2k+2, 3).", "• 4/(2k(2k+1)(2k+2)) = (2/3) / C(2k+2, 3)."), WHITE),
                (L("• π = 3 + (2/3)(1/4 − 1/20 + 1/56 − …), chứng minh bằng tách phân thức và chuỗi Leibniz.", "• π = 3 + (2/3)(1/4 − 1/20 + 1/56 − …), proved by partial fractions and Leibniz's series."), GOLD),
                (L("• Sai số cỡ 1/(4k³): nhanh hơn Leibniz nhiều, nhưng vẫn cần cả nghìn số hạng.", "• Error about 1/(4k³): far faster than Leibniz, yet still thousands of terms."), WHITE)]
        self.say('Pascal chứa sẵn các mẫu số của chuỗi Nilakantha. Sai số giảm như 1/k³.', "Pascal's triangle already holds the denominators of the Nilakantha series. The error falls like 1/k³.", 'Tóm lại: tam giác Pascal chứa sẵn các mẫu số của chuỗi Nilakantha. Tách phân thức và chuỗi Leibniz cho đúng pi, sai số giảm như một chia k mũ ba.')
        y = 4.5
        for s_, col in pts7:
            p = Text(textwrap.fill(s_, 38), font=FONT, font_size=27, color=col, line_spacing=1.1)
            if p.width > 7.7:
                p.scale_to_fit_width(7.7)
            p.move_to([-3.85 + p.width / 2, y - p.height / 2, 0]); y -= p.height + 0.4
            self.play(FadeIn(p, shift=UP * 0.12), run_time=0.5); self.wait(1.0)
        self.settle()
        self.wait(1.5)
