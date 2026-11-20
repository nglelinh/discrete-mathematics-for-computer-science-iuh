from common import *
import itertools

# ---- dữ liệu + kiểm tra ----
NODES = {"A": (0, 4.7), "B": (-3.0, 2.1), "D": (3.0, 2.1), "C": (0, -0.5)}
BRIDGES = [("A", "B", 0.45), ("A", "B", -0.45), ("B", "C", 0.45), ("B", "C", -0.45),
           ("A", "D", 0), ("C", "D", 0), ("B", "D", 0)]
DEG = {n: sum((a == n) + (b == n) for a, b, _ in BRIDGES) for n in NODES}
assert DEG == {"A": 3, "B": 5, "D": 3, "C": 3}
assert sum(d % 2 for d in DEG.values()) == 4


def has_euler_trail():
    m = len(BRIDGES)
    def dfs(cur, used):
        if len(used) == m:
            return True
        for i, (a, b, _) in enumerate(BRIDGES):
            if i in used:
                continue
            if a == cur and dfs(b, used | {i}): return True
            if b == cur and dfs(a, used | {i}): return True
        return False
    return any(dfs(s, frozenset()) for s in NODES)
assert not has_euler_trail()
# đường đi thử (kẹt sau 6 cầu): chỉ số cầu + đỉnh đến
WALK = [(0, "B"), (2, "C"), (5, "D"), (6, "B"), (1, "A"), (4, "D")]
cur = "A"
for i, nxt in WALK:
    a, b, _ = BRIDGES[i]
    assert {a, b} == {cur, nxt}
    cur = nxt
assert len({i for i, _ in WALK}) == 6


class Konigsberg(Scene):
    def construct(self):
        P = {k: np.array([x, y, 0]) for k, (x, y) in NODES.items()}
        c = cap("Bảy cây cầu Königsberg", 38)
        self.add(c)
        brown = "#c9a26b"
        bridges = []
        for a, b, ang in BRIDGES:
            if ang == 0:
                m = Line(P[a], P[b], color=brown, stroke_width=9)
            else:
                m = ArcBetweenPoints(P[a], P[b], angle=ang, color=brown, stroke_width=9)
            bridges.append(m)
        blobs = {k: VGroup(RoundedRectangle(corner_radius=0.35, width=1.3, height=1.0,
                                            color=BLUE, fill_color="#1c3550", fill_opacity=1, stroke_width=3),
                           Text(k, font=FONT, font_size=32)).move_to(P[k]) for k in NODES}
        self.play(FadeIn(VGroup(*blobs.values())), run_time=0.8)
        self.play(LaggedStart(*[Create(b) for b in bridges], lag_ratio=0.25), run_time=2.2)
        for b in bridges:
            b.set_z_index(-1)
        q = Text("Đi qua mỗi cầu đúng 1 lần?", font=FONT, font_size=30, color=GOLD).move_to([0, -3.0, 0])
        self.play(FadeIn(q), run_time=0.5)
        self.wait(0.8)

        # ---- mô hình hoá thành đồ thị ----
        c = swap_cap(self, c, cap("Chỉ giữ lại kết nối", 38, GOLD))
        dots = {k: Dot(P[k], radius=0.2, color=BLUE) for k in NODES}
        names = {k: Text(k, font=FONT, font_size=24, color=BLACK).move_to(P[k]) for k in NODES}
        self.play(*[ReplacementTransform(blobs[k], VGroup(dots[k], names[k])) for k in NODES],
                  *[b.animate.set_color(DIM).set_stroke(width=5) for b in bridges], run_time=1.4)
        self.play(FadeOut(q), run_time=0.3)

        # ---- bậc ----
        c = swap_cap(self, c, cap("Đếm bậc mỗi đỉnh", 38))
        degl = {}
        off = {"A": UP * 0.6, "C": DOWN * 0.6, "B": LEFT * 0.7, "D": RIGHT * 0.7}
        for k in NODES:
            degl[k] = Integer(DEG[k], font_size=42, color=GOLD).move_to(P[k] + off[k])
        self.play(LaggedStart(*[FadeIn(degl[k], scale=1.5) for k in NODES], lag_ratio=0.3), run_time=1.4)
        self.play(*[dots[k].animate.set_color(RED) for k in NODES], run_time=0.6)
        cnt = Text("Cả 4 đỉnh đều có bậc lẻ", font=FONT, font_size=30, color=RED).move_to([0, -3.0, 0])
        self.play(FadeIn(cnt), run_time=0.5)
        self.wait(1.0)

        # ---- thử đi ----
        c = swap_cap(self, c, cap("Thử một lộ trình", 38, GOLD))
        self.play(FadeOut(cnt), run_time=0.3)
        used = Integer(0, font_size=36, color=GOLD)
        used_t = VGroup(Text("Cầu đã đi:", font=FONT, font_size=30), used, MathTex(r"/\,7", font_size=40)).arrange(RIGHT, buff=0.2).move_to([0, -3.0, 0])
        self.play(FadeIn(used_t), run_time=0.4)
        hero = Dot(P["A"], radius=0.26, color=GOLD).set_z_index(5)
        self.play(FadeIn(hero), run_time=0.3)
        cur = "A"
        for step, (i, nxt) in enumerate(WALK):
            path = bridges[i].copy()
            if np.linalg.norm(path.get_start() - P[cur]) > 0.1:
                path.reverse_points()
            rt = [0.9, 0.8, 0.7, 0.6, 0.55, 0.5][step]
            self.play(MoveAlongPath(hero, path), bridges[i].animate.set_color(GOLD).set_stroke(width=9),
                      ChangeDecimalToValue(used, step + 1), run_time=rt, rate_func=smooth)
            used.next_to(used_t[0], RIGHT, buff=0.2)
            used_t[2].next_to(used, RIGHT, buff=0.2)
            cur = nxt
        left = [i for i in range(7) if i not in {w[0] for w in WALK}]
        assert left == [3]
        self.play(Flash(hero, color=RED, flash_radius=0.7), bridges[3].animate.set_color(RED).set_stroke(width=9), run_time=0.8)
        stuck = Text("Kẹt! Còn 1 cầu chưa đi", font=FONT, font_size=30, color=RED).move_to([0, -4.1, 0])
        self.play(FadeIn(stuck), run_time=0.4)
        self.wait(1.0)

        # ---- định lý Euler ----
        c = swap_cap(self, c, cap("Định lý Euler (1736)", 38))
        self.play(FadeOut(used_t), FadeOut(stuck), FadeOut(hero), run_time=0.4)
        r1 = Text("Chu trình Euler  ⇔  mọi bậc chẵn", font=FONT, font_size=30).move_to([0, -3.0, 0])
        r2 = Text("Đường Euler  ⇔  0 hoặc 2 đỉnh bậc lẻ", font=FONT, font_size=30).move_to([0, -4.0, 0])
        r3 = Text("Königsberg: 4 đỉnh bậc lẻ\n⇒ không thể đi!", font=FONT, font_size=34, color=RED, line_spacing=0.8).move_to([0, -5.4, 0])
        for r in (r1, r2, r3):
            self.play(FadeIn(r, shift=UP * 0.2), run_time=0.7)
            self.wait(0.5)
        self.wait(2.0)
