---
layout: post
title: "Bài toán Quyết định và Thời gian Đa thức"
categories: chapter20
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Ngôn ngữ quyết định, mã hóa input, TIME(t(n)), lớp P, Cobham–Edmonds — điểm vào lộ trình NCS."
---

<div class="textbook-epigraph" markdown="1">

"Complexity theory begins when we stop timing one program and start classifying whole families of problems."

<span class="epigraph-attribution">— Tinh thần lý thuyết độ phức tạp</span>

</div>

Để nghiên cứu “bài nào khó”, ta cần một **khung chung**: mọi instance là chuỗi bit, mọi câu hỏi rút về **Yes/No**, mọi chi phí đo bằng **số bước theo độ dài input**. Mục này cố định mô hình đó — nền cho toàn Chương 20.

![Đa thức vs mũ](/discrete-mathematics-for-computer-science-iuh/img/course/Algo_big_o_ladder.svg)

<p class="textbook-figure-caption" data-figure="20.1">Đa thức còn hy vọng khi $$n$$ lớn; mũ/giai thừa thì không — ranh giới văn hóa của $$P$$.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Mã hóa** đối tượng rời rạc thành $$x\in\{0,1\}^*$$.
- **Phát biểu** bài quyết định như ngôn ngữ $$L$$.
- **Định nghĩa** $$\mathrm{TIME}(t(n))$$ và $$P$$.
- **Giải thích** vì sao “đa thức” ổn định theo mô hình máy.

</div>

## 1. Từ bài thực tế đến chuỗi bit

Đồ thị, công thức, số nguyên: đều **mã hóa** được bằng chuỗi hữu hạn. Độ dài $$n=\lvert x\rvert$$ là tham số độ phức tạp (không phải “số đỉnh” trừ khi đã cố định encoding hợp lý — ví dụ ma trận kề $$n=\Theta(v^2)$$).

**Quy ước nghiên cứu:** encoding *reasonable* (không pad mũ vô cớ). Xem Garey–Johnson, Arora–Barak.

## 2. Bài quyết định = ngôn ngữ

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Bài quyết định** tương ứng $$L\subseteq\{0,1\}^*$$: instance Yes khi $$x\in L$$.

Bài tối ưu “$$\min c(y)$$” → quyết định “$$\exists y:\,c(y)\le K$$?”.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ.** TSP-DEC: $$(G,w,K)$$ thuộc ngôn ngữ khi tồn tại tour Hamilton độ dài $$\le K$$.

</div>

## 3. Thời gian và lớp $$P$$

<div class="textbook-definition" markdown="1">

**Định nghĩa.**  

$$
\mathrm{TIME}(t(n))
=
\{L:\exists\text{ TM tất định quyết định }L\text{ trong }\le t(\lvert x\rvert)\text{ bước}\}.
$$

$$
P=\bigcup_{k\ge 1}\mathrm{TIME}(n^k).
$$

</div>

**Cobham–Edmonds thesis (tinh thần):** các mô hình máy “hợp lý” (TM đa băng, RAM) mô phỏng nhau với overhead đa thức → $$P$$ ổn định.

## 4. Đa thức vs mũ

| Họ | Ví dụ | $$n=40$$ |
|:---|:---|:---|
| Đa thức | $$n^2$$, $$n^3\log n$$ | khả thi (tùy hằng) |
| Mũ | $$2^n$$, $$n!$$ | thường không |

$$P$$ nói *tồn tại* thuật toán đa thức — $$n^{100}\in P$$ nhưng vô dụng thực tế. NCS cần cả **lý thuyết** và **số mũ nhỏ**.

## Bài tập

1. Mã hóa đồ thị vô hướng $$n$$ đỉnh bằng ma trận kề: $$\lvert x\rvert=$$?  
2. Viết decision version của “tìm independent set lớn nhất”.  
3. Vì sao padding $$1^{2^n}$$ phá encoding “hợp lý”?

<details>
<summary>Gợi ý</summary>

1. $$\Theta(n^2)$$ bit. 2. $$(G,k)$$: $$\exists$$ IS size $$\ge k$$. 3. Làm instance “ngắn” thành dài mũ — độ phức tạp theo bit bị bóp méo.

</details>

## Đọc

Sipser (mở đầu complexity); Arora–Barak §1; Garey–Johnson §1–2.

## Tóm tắt

Quyết định · encoding · $$P=\bigcup\mathrm{TIME}(n^k)$$.

**Tiếp:** 20.2 — sâu hơn về $$P$$ và time hierarchy.
