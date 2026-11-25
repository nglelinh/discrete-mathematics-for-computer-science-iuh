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


Vì sao các mô hình ngôn ngữ lớn (LLM) trước năm 2022 thường bị nghẽn cứng khi đọc văn bản dài vài chục nghìn từ? Công thức **Attention** trông cực kỳ gọn gàng trên giấy, nhưng cách tính trực tiếp tạo ra ma trận khổng lồ $$n \times n$$ làm tắc nghẽn băng thông bộ nhớ GPU. **FlashAttention (NeurIPS 2022)** đã tạo nên bước ngoặt tốc độ gấp $$3\times$$ mà **không sửa đổi một bit nào của hàm toán học**—minh chứng hoàn hảo cho ranh giới giữa *bản thân hàm số* và *thuật toán tính hàm số đó*.

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite injections, inverses, or the existing ML history lesson.

Ghi chú ứng dụng song ngữ (tiếng Anh, sau đó là tiếng Việt). Bài này **không** thay thế nội dung về đơn ánh, hàm nghịch đảo hay bài học về hàm số từ Turing đến học máy.

</div>

## Bản đồ kiến thức nền: Ba trụ cột nhìn Cơ chế Attention dưới lăng kính Lý thuyết Hàm

1. **Attention là một Hàm hợp (Composition of Functions) xác định chặt chẽ**:
   $$\mathrm{Att}(Q, K, V) = \mathrm{softmax}(QK^\top / \sqrt{d})\,V$$ ghép nối ba ánh xạ liên tiếp: tính độ tương đồng tuyến tính $$QK^\top / \sqrt{d}$$, chuẩn hóa từng hàng thành phân phối xác suất bằng $$\mathrm{softmax}$$, rồi lấy tổng trọng số trên các vector giá trị $$V$$.

2. **Tách bạch Hàm số (*What*) khỏi Thuật toán (*How*)**:
   Trong Toán rời rạc Chương 6, hai thuật toán khác nhau tính ra cùng một cặp $$(x, f(x))$$ trên mọi đầu vào thì định nghĩa **cùng một hàm số**. FlashAttention thay đổi cách tổ chức tính toán (chia khối *tiling* trên bộ nhớ SRAM siêu nhanh + tính lại *recomputation*) để xuất ra **chính xác cùng một ma trận đầu ra**.

3. **Tối ưu IO chính xác vs. Attention xấp xỉ**:
   Các phương pháp attention hạng thấp (low-rank / sparse) cố tình thay đổi sang một **hàm số khác** để cắt giảm số phép nhân FLOPs, nhưng thường vẫn chậm hơn trên GPU thực tế vì nút cổ chai thật sự nằm ở băng thông đọc/ghi bộ nhớ HBM ($$O(n^2)$$) chứ không phải tốc độ tính toán.

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

### Khung giải thích (nên đọc chậm): Tính tay đầy đủ hàm Attention cho $$n = 2$$ token ($$d = 4$$) và thấy nút cổ chai bộ nhớ

Giả sử câu có $$n = 2$$ token với chiều $$d = 4$$ (nên $$\sqrt{d} = 2$$), và các ma trận đầu vào:
$$Q = \begin{pmatrix} 2 & 0 & 0 & 0 \\ 0 & 2 & 0 & 0 \end{pmatrix}, \qquad K = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{pmatrix}, \qquad V = \begin{pmatrix} 10 & 0 \\ 0 & 20 \end{pmatrix}.$$

1. **Bước 1 — Ma trận điểm tương đồng $$S = \frac{QK^\top}{\sqrt{d}}$$**:
   $$QK^\top = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} \implies S = \frac{1}{2}\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}.$$
2. **Bước 2 — Áp dụng $$\mathrm{softmax}$$ theo từng hàng** (với $$e^1 \approx 2{,}718$$, $$e^0 = 1$$, tổng hàng $$\approx 3{,}718$$):
   $$\frac{e^1}{e^1 + e^0} \approx \mathbf{0{,}731}, \qquad \frac{e^0}{e^1 + e^0} \approx \mathbf{0{,}269} \implies P \approx \begin{pmatrix} 0{,}731 & 0{,}269 \\ 0{,}269 & 0{,}731 \end{pmatrix}.$$
3. **Bước 3 — Tổng trọng số với $$V$$ ($$O = PV$$)**:
   - Token 1: $$(0{,}731 \times 10,\; 0{,}269 \times 20) = \mathbf{(7{,}31,\; 5{,}38)}$$.
   - Token 2: $$(0{,}269 \times 10,\; 0{,}731 \times 20) = \mathbf{(2{,}69,\; 14{,}62)}$$.

**So sánh bộ nhớ khi mở rộng lên $$n = 16{,}384$$ token (FP16 — 2 byte/số)**:
Cách tính trực tiếp buộc phải ghi và đọc toàn bộ ma trận $$S$$ và $$P$$ kích thước $$n \times n$$ ra bộ nhớ HBM chậm, tốn $$16{,}384^2 \times 2 \approx \mathbf{536{,}9\text{ MB}}$$ cho **mỗi đầu attention**. FlashAttention chia $$Q, K, V$$ thành các khối nhỏ vừa khít SRAM nội chip, cộng dồn hệ số chuẩn hóa trực tuyến (*online softmax*) để cho ra **đúng từng chữ số `(7,31; 5,38)`** mà chỉ dùng bộ nhớ HBM tuyến tính $$O(n)$$!

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=eMlx5fFNoYc">Attention in transformers, step-by-step | Deep Learning Chapter 6</a> — 3Blue1Brown, tiếng Anh. Trình bày attention như một hàm của $$Q, K, V$$, khớp với công thức trong bài.
- <a href="https://www.youtube.com/watch?v=LKwyHWYEIMQ">FlashAttention: Accelerate LLM training</a> — Machine Learning Studio, tiếng Anh. Giải thích cách FlashAttention tính đúng cùng hàm attention nhưng theo từng khối để giảm chi phí IO.
- <a href="https://www.youtube.com/watch?v=fjJOgb-E41w">Attention mechanism: Overview</a> — Google Cloud Tech, tiếng Anh. Sơ đồ tổng quan ngắn gọn về cơ chế attention trước khi đọc phần phân tích IO.
