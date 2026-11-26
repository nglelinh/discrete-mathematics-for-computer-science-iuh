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

class QuantifiersNested(Scene):
    def construct(self):
        timeline, end_vo, save_tl = setup_vo(self)
        t0 = self.time; timeline.append(("s1", t0))
        c = cap("Lượng từ lồng nhau: ∀x ∃y ≠ ∃y ∀x", 34, GOLD)
        self.play(FadeIn(c), run_time=0.6)

        b1 = card(7.6, 2.8, BLUE).move_to([0, 2.1, 0])
        t1 = VGroup(
            para("∀x ∈ ℝ, ∃y ∈ ℝ : x + y = 0", 28, BLUE, 2.7),
            para("ĐÚNG! Với mỗi x, ta chọn y = −x", 24, WHITE, 1.9),
            para("(y được phép phụ thuộc vào x)", 22, GREEN, 1.2),
        )
        b2 = card(7.6, 2.8, RED).move_to([0, -1.6, 0])
        t2 = VGroup(
            para("∃y ∈ ℝ, ∀x ∈ ℝ : x + y = 0", 28, RED, -1.0),
            para("SAI! Không có một y cố định nào", 24, WHITE, -1.8),
            para("triệt tiêu được mọi x cùng lúc!", 22, GOLD, -2.5),
        )
        self.play(FadeIn(b1), FadeIn(t1), run_time=1.0)
        self.play(FadeIn(b2), FadeIn(t2), run_time=1.0)
        end_vo("s1", t0, 10.0)

        wipe(self, keep=[c])
        t0 = self.time; timeline.append(("s2", t0))
        c = swap_cap(self, c, cap("Phủ định lượng từ (Luật De Morgan)", 34, GOLD))
        b3 = card(7.6, 3.6, GREEN).move_to([0, 0.2, 0])
        t3 = VGroup(
            para("¬(∀x P(x))  ≡  ∃x ¬P(x)", 28, BLUE, 1.2),
            para("¬(∃x P(x))  ≡  ∀x ¬P(x)", 28, GREEN, 0.2),
            para("Quy tắc: Đẩy dấu ¬ qua lượng từ → Đổi ∀ ↔ ∃!", 24, GOLD, -0.9),
        )
        self.play(FadeIn(b3), FadeIn(t3), run_time=1.0)
        end_vo("s2", t0, 9.0)
        save_tl()
