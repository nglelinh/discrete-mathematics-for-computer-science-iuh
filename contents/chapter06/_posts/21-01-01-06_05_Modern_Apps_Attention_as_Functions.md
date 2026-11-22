---
layout: post
title: "Ghi chú mở rộng: Attention như một hàm chính xác (2022–2026)"
categories: chapter06
date: 2021-01-01
order: 5
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. FlashAttention (NeurIPS 2022) computes the same attention function with an IO-aware algorithm. Does not replace function theory."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite injections, inverses, or the existing ML history lesson.

Ghi chú ứng dụng song ngữ (tiếng Anh, sau đó là tiếng Việt). Bài này **không** thay thế nội dung về đơn ánh, hàm nghịch đảo hay bài học về hàm số từ Turing đến học máy.

</div>

## English

Attention is a well-defined **function**. Given matrices $$Q,K,V$$ with $$n$$ rows (tokens) and head dimension $$d$$,

<div class="textbook-equation" markdown="1">
$$
\mathrm{Att}(Q,K,V) = \mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d}}\right) V.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Naïve evaluation materializes the $$n \times n$$ matrix $$QK^\top$$ — composition of linear maps and softmax, quadratic in $$n$$. Dao, Fu, Ermon, Rudra, and Ré, “FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness,” *NeurIPS 2022*, [proceedings](https://proceedings.neurips.cc/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html), keep **the same function** (exact softmax attention) but change the *algorithm*: tiling plus recomputation so GPU HBM traffic drops. They prove an IO-complexity bound and report, among other figures, about $$3\times$$ wall-clock speedup on GPT-2 (length 1K) versus standard attention.

Chapter 6 already distinguishes a function from a procedure that computes it. FlashAttention is a 2022 exhibit of that distinction: $$\mathrm{Att}$$ is unchanged; the implementation is a different factorization of the same map. Approximate attention methods, by contrast, compute a *different* function in order to cut FLOPs — and the paper argues they often lose wall-clock time because they ignore the memory hierarchy.

**Citations**

1. T. Dao et al., “FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness,” NeurIPS 2022. [arXiv:2205.14135](https://arxiv.org/abs/2205.14135)

**Questions.** (1) In the language of this chapter, is FlashAttention a new function or a new algorithm for an old function? (2) Why does “exact” matter when comparing it to low-rank attention?

## Tiếng Việt

Attention là một **hàm số** được định nghĩa chặt chẽ. Với các ma trận $$Q,K,V$$ gồm $$n$$ hàng (tương ứng $$n$$ token) và số chiều mỗi đầu attention là $$d$$,

$$\mathrm{Att}(Q,K,V) = \mathrm{softmax}(QK^\top/\sqrt{d})\,V.$$

Cách tính trực tiếp (ngây thơ) tạo ra và lưu toàn bộ ma trận $$n \times n$$ của tích $$QK^\top$$ trong bộ nhớ — là phép hợp của các ánh xạ tuyến tính với hàm softmax, có độ phức tạp bậc hai theo $$n$$. Trong công trình tại NeurIPS 2022, Dao và cộng sự giữ nguyên **cùng một hàm** (softmax attention chính xác) nhưng thay đổi *thuật toán* tính toán: áp dụng kỹ thuật chia khối (tiling) kết hợp tính lại (recomputation) nhằm giảm lưu lượng truyền dữ liệu với bộ nhớ HBM của GPU. Các tác giả chứng minh cận độ phức tạp IO và báo cáo tốc độ thực thi thực tế nhanh hơn khoảng $$3\times$$ trên mô hình GPT-2 (độ dài chuỗi 1K) so với cài đặt attention chuẩn.

Chương 6 đã phân biệt giữa bản thân hàm số và thủ tục dùng để tính hàm đó. FlashAttention là một minh họa cụ thể cho sự phân biệt này: ánh xạ $$\mathrm{Att}$$ không hề thay đổi, chỉ có cách cài đặt được tổ chức lại cho cùng một hàm. Ngược lại, các phương pháp attention xấp xỉ tính một hàm *khác* để giảm số phép tính dấu phẩy động (FLOPs), và bài báo chỉ ra rằng chúng thường vẫn chậm hơn về thời gian thực thi thực tế (wall-clock time) do bỏ qua hệ thống phân cấp bộ nhớ.

**Câu hỏi.** (1) Theo ngôn ngữ của chương này, FlashAttention là một hàm mới hay một thuật toán mới cho hàm cũ? (2) Vì sao tính chất “chính xác” (exact) lại quan trọng khi so sánh FlashAttention với attention hạng thấp (low-rank attention)?

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=eMlx5fFNoYc">Attention in transformers, step-by-step | Deep Learning Chapter 6</a> — 3Blue1Brown, tiếng Anh. Trình bày attention như một hàm của $$Q, K, V$$, khớp với công thức trong bài.
- <a href="https://www.youtube.com/watch?v=LKwyHWYEIMQ">FlashAttention: Accelerate LLM training</a> — Machine Learning Studio, tiếng Anh. Giải thích cách FlashAttention tính đúng cùng hàm attention nhưng theo từng khối để giảm chi phí IO.
- <a href="https://www.youtube.com/watch?v=fjJOgb-E41w">Attention mechanism: Overview</a> — Google Cloud Tech, tiếng Anh. Sơ đồ tổng quan ngắn gọn về cơ chế attention trước khi đọc phần phân tích IO.
