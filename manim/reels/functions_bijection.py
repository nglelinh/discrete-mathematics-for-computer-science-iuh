# -*- coding: utf-8 -*-
from common import *
import os, json

def card(w, h, color=BLUE):
    return RoundedRectangle(width=w, height=h, corner_radius=0.22,
                            fill_color=CELL, fill_opacity=0.95,
                            stroke_color=color, stroke_width=2.5)

def setup_vo(scene):
    vo_durs = json.load(open(os.environ["VO_DUR_JSON"])) if os.environ.get("VO_DUR_JSON") else {}
    tl_path = os.environ.get("VO_TIMELINE_JSON")
    timeline = []
    def end_vo(sid, t0, fb):
        dur = vo_durs.get(sid)
        if dur is not None:
            rem = dur - (scene.time - t0) + 0.45
            if rem > 0.05:
                scene.wait(rem)
        else:
            scene.wait(fb)
    def save_tl():
        if tl_path:
            with open(tl_path, "w") as f:
                json.dump({"timeline": timeline, "total": float(scene.time)}, f)
    return timeline, end_vo, save_tl

class FunctionsBijection(Scene):
    def construct(self):
        timeline, end_vo, save_tl = setup_vo(self)
        t0 = self.time; timeline.append(("s1", t0))
        c = cap("Đơn ánh, Toàn ánh và Song ánh", 36, GOLD)
        self.play(FadeIn(c), run_time=0.6)

        rows = [
            ("Đơn ánh (Injective)", "f(a) = f(b) ⇒ a = b  (Không đụng hàng)", BLUE),
            ("Toàn ánh (Surjective)", "Mọi y ∈ B đều có x ∈ A sao cho f(x) = y", GREEN),
            ("Song ánh (Bijective)", "Vừa đơn ánh vừa toàn ánh ⇒ Có hàm ngược f⁻¹", GOLD),
        ]
        cards = VGroup()
        for t_a, t_b, col in rows:
            box = card(7.6, 2.0, col)
            g = VGroup(para(t_a, 26, col, 0.35), para(t_b, 22, WHITE, -0.35)).move_to(box)
            cards.add(VGroup(box, g))
        cards.arrange(DOWN, buff=0.32).move_to([0, 0.3, 0])
        self.play(LaggedStart(*[FadeIn(x, shift=UP*0.18) for x in cards], lag_ratio=0.25), run_time=1.8)
        end_vo("s1", t0, 10.0)

        wipe(self, keep=[c])
        t0 = self.time; timeline.append(("s2", t0))
        c = swap_cap(self, c, cap("Đổi miền A, B → Tính chất đổi ngay!", 34, GOLD))
        b = card(7.6, 3.8, RED).move_to([0, 0.2, 0])
        t = VGroup(
            para("Cùng công thức f(x) = x²:", 28, GOLD, 1.3),
            para("• f: ℝ → ℝ : Không đơn ánh, không toàn ánh", 23, RED, 0.4),
            para("• f: [0, ∞) → ℝ : Đơn ánh (chưa toàn ánh)", 23, BLUE, -0.3),
            para("• f: [0, ∞) → [0, ∞) : Song ánh (f⁻¹(y) = √y)!", 23, GREEN, -1.0),
        )
        self.play(FadeIn(b), FadeIn(t), run_time=1.1)
        end_vo("s2", t0, 9.5)
        save_tl()
