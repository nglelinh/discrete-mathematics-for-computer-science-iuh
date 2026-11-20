from common import *
from math import pi

N = 100
# kiểm tra: với k nguyên, i -> k*i mod N là hàm trên Z_N; số điểm bất động liên quan gcd(k-1, N)
assert all((2 * i) % N == (i + i) % N for i in range(N))
assert sum(1 for i in range(N) if (3 * i) % N == i) == 2  # gcd(2,100)=2


class Cardioid(Scene):
    def construct(self):
        c = cap("Bảng cửu chương theo modulo", 36)
        self.add(c)
        R = 3.5
        C = np.array([0, 1.5, 0])
        circ = Circle(radius=R, color=DIM, stroke_width=2).move_to(C)
        P = lambda ang: C + R * np.array([np.cos(ang), np.sin(ang), 0])
        dots = VGroup(*[Dot(P(pi / 2 + 2 * pi * i / N), radius=0.04, color=BLUE) for i in range(N)])
        K = ValueTracker(1.0)

        def lines():
            k = K.get_value()
            g = VGroup()
            for i in range(N):
                a = pi / 2 + 2 * pi * i / N
                b = pi / 2 + 2 * pi * k * i / N
                g.add(Line(P(a), P(b), stroke_width=1.6, color=GOLD, stroke_opacity=0.75))
            return g
        lm = always_redraw(lines)

        n_t = MathTex(r"n=100", font_size=44).move_to([-2.0, -3.1, 0])
        rule = MathTex(r"i\ \longrightarrow\ k\cdot i \pmod{n}", font_size=48).move_to([0, -4.3, 0])
        k_lab = MathTex(r"k=", font_size=44).move_to([1.1, -3.1, 0])
        k_num = DecimalNumber(1.0, num_decimal_places=2, font_size=44, color=GOLD)
        k_num.add_updater(lambda m: (m.set_value(K.get_value()), m.next_to(k_lab, RIGHT, buff=0.12)))
        self.play(Create(circ), FadeIn(dots), run_time=1.2)
        self.add(lm)
        self.play(FadeIn(n_t), FadeIn(k_lab), FadeIn(k_num), FadeIn(rule), run_time=0.6)

        names = {2: "k = 2: hình tim (cardioid)", 3: "k = 3: nephroid (2 điểm nhọn)",
                 4: "k = 4: 3 điểm nhọn", 5: "k = 5: 4 điểm nhọn"}
        note = Text("", font=FONT, font_size=30, color=GOLD).move_to([0, -5.5, 0])
        for k, rt in [(2, 3.2), (3, 3.0), (4, 2.6), (5, 2.4)]:
            self.play(K.animate.set_value(k), run_time=rt, rate_func=smooth)
            nt = Text(names[k], font=FONT, font_size=30, color=GOLD).move_to([0, -5.5, 0])
            if k == 2:
                c = swap_cap(self, c, cap("k = 2: hình tim!", 40, GOLD))
            elif k == 3:
                c = swap_cap(self, c, cap("Tăng k: hình dạng đổi theo", 34))
            self.play(Transform(note, nt) if k > 2 else FadeIn(note.become(nt)), run_time=0.4)
            self.wait(0.7)
        c = swap_cap(self, c, cap("Quy luật sau mỗi phép nhân", 34))
        self.play(K.animate.set_value(10), run_time=4.5, rate_func=linear)
        end = Text("k − 1 điểm nhọn", font=FONT, font_size=30, color=GOLD).move_to([0, -5.5, 0])
        self.play(Transform(note, end), run_time=0.5)
        self.wait(2.0)
