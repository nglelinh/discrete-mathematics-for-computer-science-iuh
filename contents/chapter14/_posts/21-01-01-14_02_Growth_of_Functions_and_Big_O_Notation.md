---
layout: post
title: "Tăng trưởng của Hàm và Ký hiệu Big-O"
categories: chapter14
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Big-O, Ω, Θ; bậc tăng trưởng; quy tắc tổng/tích; so sánh log, n, n log n, n², 2ⁿ; giới hạn hằng số."
---

<div class="textbook-epigraph" markdown="1">

"Ignore machine constants — compare how cost grows with input size."

<span class="epigraph-attribution">— Asymptotic analysis spirit</span>

</div>

So sánh thuật toán không dựa vào mili-giây trên một máy, mà vào **cách chi phí tăng theo kích thước đầu vào $$n$$**. **Big-O**, **Ω**, **Θ** là ngôn ngữ chuẩn cho phân tích tiệm cận. Mục này định nghĩa các ký hiệu, bậc thường gặp, và quy tắc thao tác.

![Bậc tăng trưởng](/discrete-mathematics-for-computer-science-iuh/img/course/Algo_big_o_ladder.svg)

<p class="textbook-figure-caption" data-figure="14.3">Thang tăng trưởng tương đối — mũ và giai thừa vượt xa đa thức khi $$n$$ lớn.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** $$O$$, $$\Omega$$, $$\Theta$$.
- **Chứng minh** quan hệ Big-O đơn giản bằng định nghĩa (hằng số $$c,n_0$$).
- **Sắp xếp** các bậc: $$1$$, $$\log n$$, $$n$$, $$n\log n$$, $$n^2$$, $$2^n$$, $$n!$$.
- **Áp dụng** quy tắc tổng và tích.
- **Giải thích** vì sao bỏ hằng số và hạng thấp.

**Từ khóa**: Big-O, Omega, Theta, asymptotic, growth rate.

</div>

## 1. Định nghĩa

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cho $$f,g:\mathbb{N}\to\mathbb{R}^+$$.

- $$f(n)=O(g(n))$$ nếu tồn tại $$c>0$$, $$n_0$$ sao cho với mọi $$n\ge n_0$$: $$f(n)\le c\,g(n)$$ (*chặn trên* tiệm cận).
- $$f(n)=\Omega(g(n))$$ nếu $$g(n)=O(f(n))$$ (*chặn dưới*).
- $$f(n)=\Theta(g(n))$$ nếu $$f=O(g)$$ và $$f=\Omega(g)$$ (*cùng bậc*).

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 1.** $$3n^2+5n+2 = O(n^2)$$: với $$n\ge 1$$, $$3n^2+5n+2\le 3n^2+5n^2+2n^2=10n^2$$. Cũng $$\Theta(n^2)$$.

</div>

## 2. Bậc thường gặp

| Bậc | Tên | Ví dụ thuật toán |
|:---|:---|:---|
| $$O(1)$$ | Hằng | Truy cập mảng theo chỉ số |
| $$O(\log n)$$ | Log | Binary search |
| $$O(n)$$ | Tuyến tính | Linear scan |
| $$O(n\log n)$$ | Linearithmic | Merge sort (tốt) |
| $$O(n^2)$$ | Bình phương | Bubble sort lồng đôi |
| $$O(2^n)$$ | Mũ | Tập con brute-force |
| $$O(n!)$$ | Giai thừa | Hoán vị brute-force |

## 3. Quy tắc

- **Tổng:** $$O(f)+O(g)=O(\max(f,g))$$ (cùng điều kiện chuẩn).
- **Tích:** $$O(f)\cdot O(g)=O(fg)$$.
- **Đa thức:** bậc cao thắng: $$an^k+\cdots=O(n^k)$$.
- **Log:** cơ số đổi chỉ nhân hằng: $$\log_2 n=\Theta(\log_{10} n)$$.

<div class="textbook-example" markdown="1">

**Ví dụ 2.** $$T(n)=n+ n\log n + 100 = O(n\log n)=\Theta(n\log n)$$ vì $$n\log n$$ chiếm ưu thế so với $$n$$ khi $$n\to\infty$$.

</div>

## 4. Thử nghiệm tương tác

<div class="interactive-demo" markdown="1">
<div data-demo="big-o-growth-comparator"></div>
</div>
<script src="{{ '/public/js/big-o-growth-comparator.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Chứng minh $$5n+20=O(n)$$ bằng định nghĩa.

<details>
<summary>Đáp án</summary>

Với $$n\ge 20$$: $$5n+20\le 5n+n=6n$$. Lấy $$c=6$$, $$n_0=20$$.

</details>

### Bài tập 2

Sắp tăng: $$2^n$$, $$n^3$$, $$\log n$$, $$n\log n$$, $$n!$$.

<details>
<summary>Đáp án</summary>

$$\log n \prec n\log n \prec n^3 \prec 2^n \prec n!$$ (với $$n$$ đủ lớn).

</details>

### Bài tập 3

$$n^2$$ có phải $$O(n^3)$$? $$n^3$$ có phải $$O(n^2)$$?

<details>
<summary>Đáp án</summary>

Có: $$n^2\le n^3$$ với $$n\ge 1$$. Không: $$n^3/n^2=n\to\infty$$ không bị chặn bởi hằng.

</details>

## Tóm tắt

1. $$O$$/$$\Omega$$/$$\Theta$$ mô tả tăng trưởng, không đo máy cụ thể.
2. Bỏ hằng số và hạng thấp khi $$n\to\infty$$.
3. Mũ ≫ đa thức — nền so sánh khả thi (Ch.20).

Trong bài tiếp theo: **phân tích** $$T(n)$$ của thuật toán cụ thể.
