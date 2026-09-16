---
layout: post
title: "Optional note: Recurrences for IO-aware algorithms (2022–2026)"
categories: chapter10
date: 2021-01-01
order: 5
required: false
lesson_type: optional
lang: vi
excerpt: "Bài tùy chọn song ngữ. FlashAttention (NeurIPS 2022) phân tích độ phức tạp IO bằng tiling — cùng họ quan hệ truy hồi chia để trị. Không viết lại lý thuyết truy hồi."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite linear recurrences or the existing algorithms/systems lesson. Tagged `lang: vi` to stay with this chapter’s theory posts (no extra EN theory split).

Bài ghi chú ứng dụng song ngữ. **Không** viết lại truy hồi tuyến tính. Gắn `lang: vi` để đi cùng các bài lý thuyết của chương (không tách EN thêm cho lý thuyết).

</div>

## English

Divide-and-conquer recurrences are how this chapter talks about algorithms: $$T(n) = a\,T(n/b) + f(n)$$. FlashAttention (Dao et al., NeurIPS 2022, [arXiv:2205.14135](https://arxiv.org/abs/2205.14135)) is a 2022 algorithm whose *interesting* cost is not only FLOPs but **IO**: reads and writes between GPU HBM and on-chip SRAM.

They tile the $$n \times n$$ attention landscape into blocks that fit in SRAM, then recompute softmax statistics in the backward pass instead of storing the full matrix. The paper analyzes IO complexity and shows the scheme is optimal for a range of SRAM sizes. Empirically: about $$3\times$$ speedup on GPT-2 (length 1K) and the first better-than-chance Path-X result (length 16K) among Transformers they compare.

For Chapter 10, treat tiling as a recurrence on block size: each block is an independent subproblem plus a linear merge of running $$m$$ / $$\ell$$ statistics (stable softmax). You already know how to write such recurrences; this note only points at a 2022 system where the recurrence is about *memory traffic*, which dominates wall-clock time on GPUs.

**Citations**

1. T. Dao et al., “FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness,” NeurIPS 2022. [DOI/proceedings](https://proceedings.neurips.cc/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html)

**Questions.** (1) Write a schematic recurrence for “process $$n$$ tokens in blocks of $$B$$.” (2) Which term is $$f(n)$$ if the bottleneck is HBM transfers, not arithmetic?

## Tiếng Việt

Quan hệ truy hồi chia để trị là cách chương này nói về thuật toán: $$T(n) = a\,T(n/b) + f(n)$$. FlashAttention (Dao et al., NeurIPS 2022) là thuật toán 2022 mà chi phí *đáng nói* không chỉ FLOP mà là **IO**: đọc/ghi giữa HBM GPU và SRAM trên chip.

Họ chia lưới attention $$n \times n$$ thành khối vừa SRAM, rồi tính lại thống kê softmax ở chiều backward thay vì lưu cả ma trận. Bài báo phân tích độ phức tạp IO và chỉ ra tính tối ưu trên một dải kích thước SRAM. Thực nghiệm: khoảng $$3\times$$ trên GPT-2 (độ dài 1K) và Path-X (16K) tốt hơn ngẫu nhiên.

Với Chương 10, hãy coi tiling là truy hồi theo kích thước khối: mỗi khối là bài toán con cộng bước trộn tuyến tính thống kê $$m$$ / $$\ell$$ (softmax ổn định). Bạn đã biết viết truy hồi; ghi chú chỉ trỏ tới hệ thống 2022 nơi truy hồi nói về *traffic bộ nhớ*, thứ chi phối thời gian tường trên GPU.

**Câu hỏi.** (1) Viết truy hồi sơ đồ cho “xử lý $$n$$ token theo khối $$B$$.” (2) Nếu nút thắt là chuyển HBM chứ không phải phép tính, $$f(n)$$ là số hạng nào?
