from common import *
from math import pi

# ---- dữ liệu (kiểm tra bằng số) ----
N = 6
EDGES = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(0,3),(1,4)]
DEG = [sum(1 for e in EDGES if v in e) for v in range(N)]
assert sum(DEG) == 2 * len(EDGES) == 16
assert sum(d % 2 for d in DEG) % 2 == 0 and sum(d % 2 for d in DEG) == 4
LABELS = "ABCDEF"


class Handshake(Scene):
    def construct(self):
        c = cap("Định lý bắt tay", 44)
        self.add(c)
        center = np.array([0, 2.2, 0])
        R = 2.4
        pos = [center + R * np.array([np.sin(i * pi / 3 + pi / 6 * 0), np.cos(i * pi / 3), 0]) for i in range(N)]
        dots = VGroup(*[Dot(p, radius=0.2, color=BLUE) for p in pos])
        labs = VGroup(*[Text(LABELS[i], font=FONT, font_size=26, color=BLACK).move_to(pos[i]) for i in range(N)])
        edges = [Line(pos[a], pos[b], color=DIM, stroke_width=4) for a, b in EDGES]
        self.play(LaggedStart(*[Create(e) for e in edges], lag_ratio=0.1), run_time=1.6)
        self.play(FadeIn(dots), FadeIn(labs), run_time=0.6)

        # nhãn bậc cạnh mỗi đỉnh
        degs = []
        for i in range(N):
            d = pos[i] - center
            d = d / np.linalg.norm(d)
            t = Integer(0, font_size=40, color=GOLD).move_to(pos[i] + d * 0.62)
            degs.append(t)
        self.play(*[FadeIn(t) for t in degs], run_time=0.4)

        e_lab = MathTex(r"|E|=", font_size=48).move_to([-1.2, -1.9, 0])
        e_num = Integer(0, font_size=48).next_to(e_lab, RIGHT, buff=0.15)
        s_lab = MathTex(r"\textstyle\sum\deg(v)=", font_size=48).move_to([-1.0, -3.3, 0])
        s_num = Integer(0, font_size=48, color=GOLD).next_to(s_lab, RIGHT, buff=0.15)
        self.play(FadeIn(e_lab), FadeIn(e_num), FadeIn(s_lab), FadeIn(s_num), run_time=0.5)
        c = swap_cap(self, c, cap("Mỗi cạnh có hai đầu", 38, GOLD))

        cnt = [0] * N
        total = 0
        durs = [1.5, 1.2, 1.0, 0.8, 0.7, 0.6, 0.5, 0.45]
        for k, (a, b) in enumerate(EDGES):
            cnt[a] += 1
            cnt[b] += 1
            total += 2
            e_new = edges[k].copy().set_color(GOLD).set_stroke(width=8)
            self.play(
                Transform(edges[k], e_new),
                Indicate(dots[a], color=GOLD, scale_factor=1.4),
                Indicate(dots[b], color=GOLD, scale_factor=1.4),
                ChangeDecimalToValue(degs[a], cnt[a]),
                ChangeDecimalToValue(degs[b], cnt[b]),
                ChangeDecimalToValue(e_num, k + 1),
                ChangeDecimalToValue(s_num, total),
                run_time=durs[k])
            for t in (e_num, s_num):
                pass
            e_num.next_to(e_lab, RIGHT, buff=0.15)
            s_num.next_to(s_lab, RIGHT, buff=0.15)
            self.play(edges[k].animate.set_color(DIM).set_stroke(width=4), run_time=0.1)

        eq = MathTex(r"\sum_{v}\deg(v)=2\,|E|", font_size=56, color=GOLD).move_to([0, -4.9, 0])
        self.play(Write(eq), run_time=0.8)
        c = swap_cap(self, c, cap("Số đỉnh bậc lẻ luôn là số chẵn", 32))
        odd = [i for i in range(N) if DEG[i] % 2]
        self.play(*[dots[i].animate.set_color(RED) for i in odd],
                  *[Indicate(degs[i], color=RED, scale_factor=1.5) for i in odd], run_time=1.2)
        note = Text("4 đỉnh bậc lẻ (chẵn!)", font=FONT, font_size=30, color=RED).move_to([0, -6.0, 0])
        self.play(FadeIn(note), run_time=0.5)
        self.wait(2.0)
        c = swap_cap(self, c, cap("Không có đồ thị 3 đỉnh cùng bậc 3", 30))
        note2 = Text("3 + 3 + 3 = 9 là số lẻ", font=FONT, font_size=30, color=RED).move_to(note)
        self.play(ReplacementTransform(note, note2), run_time=0.6)
        self.wait(3.0)
