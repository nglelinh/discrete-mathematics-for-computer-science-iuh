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

class BirthdayParadox(Scene):
    def construct(self):
        timeline, end_vo, save_tl = setup_vo(self)
        t0 = self.time; timeline.append(("s1", t0))
        c = cap("Nghịch lý Ngày sinh nhật & Va chạm ID", 34, GOLD)
        self.play(FadeIn(c), run_time=0.6)

        b1 = card(7.6, 3.0, BLUE).move_to([0, 1.8, 0])
        t1 = VGroup(
            para("Chỉ cần 23 người trong phòng:", 27, GOLD, 2.5),
            para("Số cặp so sánh = C(23, 2) = 253 cặp!", 25, BLUE, 1.7),
            para("P(ít nhất 1 cặp trùng) ≈ 50,7% > 50%", 25, GREEN, 0.9),
        )
        b2 = card(7.6, 2.8, RED).move_to([0, -1.8, 0])
        t2 = VGroup(
            para("Ngưỡng 50% va chạm với N mã định danh:", 24, WHITE, -1.1),
            para("k ≈ 1,18 × √N", 30, RED, -1.9),
            para("(Không phải N/2 như trực giác đánh lừa!)", 22, DIM, -2.6),
        )
        self.play(FadeIn(b1), FadeIn(t1), run_time=1.1)
        self.play(FadeIn(b2), FadeIn(t2), run_time=1.0)
        end_vo("s1", t0, 10.5)

        wipe(self, keep=[c])
        t0 = self.time; timeline.append(("s2", t0))
        c = swap_cap(self, c, cap("Bài học thực chiến: INT32 vs UUID v4", 34, GOLD))
        b3 = card(7.6, 3.8, GREEN).move_to([0, 0.2, 0])
        t3 = VGroup(
            para("• ID 10-bit (N = 1.024): va chạm ở ~38 bản ghi", 23, BLUE, 1.2),
            para("• INT32 (N ≈ 4,29 tỷ): va chạm 50% ở ~77.163 ID!", 23, RED, 0.3),
            para("• UUID v4 (122 bit ngẫu nhiên, N ≈ 5,3×10³⁶):", 23, GREEN, -0.5),
            para("  Cần ~2,7×10¹⁸ ID mới đạt ngưỡng 50%!", 23, GOLD, -1.2),
        )
        self.play(FadeIn(b3), FadeIn(t3), run_time=1.1)
        end_vo("s2", t0, 9.5)
        save_tl()
