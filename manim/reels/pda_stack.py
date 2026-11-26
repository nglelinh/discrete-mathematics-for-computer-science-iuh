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

class PDAStack(Scene):
    def construct(self):
        timeline, end_vo, save_tl = setup_vo(self)
        t0 = self.time; timeline.append(("s1", t0))
        c = cap("Ôtômat Đẩy xuống (PDA) & Ngôn ngữ aⁿbⁿ", 33, GOLD)
        self.play(FadeIn(c), run_time=0.6)

        b1 = card(7.6, 2.7, RED).move_to([0, 2.0, 0])
        t1 = VGroup(
            para("DFA chỉ có bộ nhớ hữu hạn (Q trạng thái)", 24, WHITE, 2.6),
            para("⇒ Không thể đếm số chữ 'a' lớn tùy ý!", 24, RED, 1.8),
            para("aⁿbⁿ KHÔNG phải ngôn ngữ chính quy.", 23, GOLD, 1.1),
        )
        b2 = card(7.6, 2.9, GREEN).move_to([0, -1.5, 0])
        t2 = VGroup(
            para("Thêm 1 Ngăn xếp (Stack LIFO) ⇒ PDA:", 25, GREEN, -0.8),
            para("1. Đọc 'a' → PUSH A vào đỉnh ngăn xếp", 23, BLUE, -1.6),
            para("2. Đọc 'b' → POP A ra khỏi ngăn xếp", 23, BLUE, -2.3),
        )
        self.play(FadeIn(b1), FadeIn(t1), run_time=1.0)
        self.play(FadeIn(b2), FadeIn(t2), run_time=1.1)
        end_vo("s1", t0, 10.5)

        wipe(self, keep=[c])
        t0 = self.time; timeline.append(("s2", t0))
        c = swap_cap(self, c, cap("Hai chế độ chấp nhận tương đương nhau", 34, GOLD))
        b3 = card(7.6, 3.4, BLUE).move_to([0, 0.2, 0])
        t3 = VGroup(
            para("• Chấp nhận bằng Trạng thái kết (Final State)", 23, BLUE, 1.0),
            para("• Chấp nhận bằng Ngăn xếp rỗng (Empty Stack)", 23, GREEN, 0.1),
            para("Định lý: Hai định nghĩa sinh CÙNG lớp CFL,", 23, GOLD, -0.7),
            para("và tương đương hoàn toàn với Văn phạm CFG!", 23, WHITE, -1.4),
        )
        self.play(FadeIn(b3), FadeIn(t3), run_time=1.0)
        end_vo("s2", t0, 9.0)
        save_tl()
