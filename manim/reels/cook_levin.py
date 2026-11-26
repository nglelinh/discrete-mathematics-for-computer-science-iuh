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

class CookLevin(Scene):
    def construct(self):
        timeline, end_vo, save_tl = setup_vo(self)
        t0 = self.time; timeline.append(("s1", t0))
        c = cap("Định lý Cook–Levin: SAT là NP-đầy đủ", 34, GOLD)
        self.play(FadeIn(c), run_time=0.6)

        b1 = card(7.6, 2.5, BLUE).move_to([0, 2.2, 0])
        t1 = VGroup(
            para("Mục tiêu: Mọi bài toán L ∈ NP đều quy giản đa thức về SAT", 22, WHITE, 2.7),
            para("Ý tưởng: Trải toàn bộ lịch sử chạy n^k bước của NTM", 22, BLUE, 2.0),
            para("thành một Bảng tính toán (Tableau) kích thước n^k × n^k!", 22, GOLD, 1.3),
        )
        grid = VGroup(*[Square(side_length=0.55, color=DIM, stroke_width=1.5) for _ in range(16)]).arrange_in_grid(4, 4, buff=0.05).move_to([0, -0.8, 0])
        lbl_g = para("Mỗi ô (i, j) mã hóa ký tự bằng biến Boole x_{i,j,s}", 22, GREEN, -2.6)
        self.play(FadeIn(b1), FadeIn(t1), run_time=1.1)
        self.play(Create(grid), FadeIn(lbl_g), run_time=1.1)
        end_vo("s1", t0, 10.5)

        wipe(self, keep=[c])
        t0 = self.time; timeline.append(("s2", t0))
        c = swap_cap(self, c, cap("4 khối mệnh đề CNF khóa chặt Bảng tính toán", 32, GOLD))
        rows = [
            ("1. Cell (Ô)", "Mỗi ô chứa đúng 1 ký tự duy nhất", BLUE),
            ("2. Start (Bắt đầu)", "Hàng 1 chứa cấu hình đầu vào x", GREEN),
            ("3. Move (Chuyển)", "Mọi cửa sổ 2×3 tuân theo hàm chuyển δ", GOLD),
            ("4. Accept (Chấp nhận)", "Có ít nhất 1 ô chứa trạng thái q_accept", RED),
        ]
        cards = VGroup()
        for a, b, col in rows:
            box = card(7.6, 1.55, col)
            g = VGroup(para(a, 24, col, 0.25), para(b, 21, WHITE, -0.25)).move_to(box)
            cards.add(VGroup(box, g))
        cards.arrange(DOWN, buff=0.25).move_to([0, 0.2, 0])
        self.play(LaggedStart(*[FadeIn(x, shift=UP*0.18) for x in cards], lag_ratio=0.22), run_time=1.8)
        end_vo("s2", t0, 10.0)
        save_tl()
