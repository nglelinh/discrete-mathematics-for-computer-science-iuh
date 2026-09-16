---
layout: post
title: "Optional note: Attention as an exact function (2022–2026)"
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

Bài ghi chú ứng dụng song ngữ. **Không** viết lại đơn ánh, hàm ngược, hay bài hàm số từ Turing đến học máy.

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

Attention là một **hàm** xác định rõ. Với ma trận $$Q,K,V$$ có $$n$$ hàng,

$$\mathrm{Att}(Q,K,V) = \mathrm{softmax}(QK^\top/\sqrt{d})\,V.$$

Cách tính ngây thơ materialize ma trận $$n \times n$$ — hợp của các ánh xạ tuyến tính và softmax, bậc hai theo $$n$$. Dao và cộng sự (NeurIPS 2022) giữ **cùng hàm** (softmax attention exact) nhưng đổi *thuật toán*: tiling và tính lại để giảm traffic HBM. Họ chứng minh cận IO và báo cáo khoảng $$3\times$$ nhanh hơn trên GPT-2 (độ dài 1K) so với attention chuẩn.

Chương 6 đã phân biệt hàm với thủ tục tính hàm. FlashAttention là ví dụ 2022: $$\mathrm{Att}$$ không đổi; cài đặt là một phân tích khác của cùng ánh xạ. Các phương pháp attention xấp xỉ tính một hàm *khác* để cắt FLOP — và bài báo lập luận chúng thường thua thời gian tường vì bỏ qua hệ thống phân cấp bộ nhớ.

**Câu hỏi.** (1) Theo ngôn ngữ chương này, FlashAttention là hàm mới hay thuật toán mới cho hàm cũ? (2) Vì sao “exact” quan trọng khi so với attention hạng thấp?
