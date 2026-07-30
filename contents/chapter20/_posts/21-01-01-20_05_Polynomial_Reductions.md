---
layout: post
title: "Rút gọn Đa thức (Karp Reduction)"
categories: chapter20
date: 2021-01-01
order: 5
required: true
lang: en
excerpt: "Định nghĩa A≤ₚB; chứng minh phản xạ, bắc cầu, bảo toàn P; Karp vs Cook reduction."
---

<div class="textbook-epigraph" markdown="1">

"Reductions are the comparative method of complexity theory."

<span class="epigraph-attribution">— Karp tradition</span>

</div>

Rút gọn là **công cụ so sánh độ khó**: biến instance $$A$$ thành instance $$B$$ nhanh, giữ Yes/No.

![Reduction](/discrete-mathematics-for-computer-science-iuh/img/course/Complexity_reduction.svg)

<p class="textbook-figure-caption" data-figure="20.3">$$x\in A\Leftrightarrow f(x)\in B$$, $$f$$ poly-time.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** $$A\le_p B$$.
- **Chứng minh** phản xạ, bắc cầu, “$$B\in P\Rightarrow A\in P$$”.
- **Phân biệt** Karp (many-one) và Cook (Turing).

</div>

## 1. Định nghĩa Karp

<div class="textbook-definition" markdown="1">

**Định nghĩa.** $$A\le_p B$$ nếu ∃ $$f$$ tính poly-time:

$$
\forall x:\quad x\in A\iff f(x)\in B.
$$

</div>

## 2. Định lý

<div class="textbook-theorem" markdown="1">

**Định lý** (phản xạ). $$A\le_p A$$ với $$f=\mathrm{id}$$.

</div>

<div class="textbook-theorem" markdown="1">

**Định lý** (bắc cầu). $$A\le_p B$$, $$B\le_p C$$ ⇒ $$A\le_p C$$.

</div>

**Chứng minh.** $$h=g\circ f$$. Tính đúng theo $$\Leftrightarrow$$.  
$$\lvert f(x)\rvert\le\mathrm{poly}(\lvert x\rvert)$$ vì mỗi bước viết ≤1 ký hiệu. Thời gian $$g(f(x))$$ poly theo $$\lvert f(x)\rvert$$ ⇒ poly theo $$\lvert x\rvert$$. $$\square$$

<div class="textbook-theorem" markdown="1">

**Định lý** (bảo toàn $$P$$). Nếu $$A\le_p B$$ và $$B\in P$$ thì $$A\in P$$.

</div>

**Chứng minh.** Tính $$y=f(x)$$; quyết định $$y\in B$$; trả về. $$\square$$

<div class="textbook-theorem" markdown="1">

**Hệ quả.** $$A\le_p B$$, $$A\notin P$$ ⇒ $$B\notin P$$.

</div>

## 3. Karp vs Cook

| | Karp (many-one) | Cook (Turing) |
|:---|:---|:---|
| Số lần hỏi $$B$$ | 1 (sau $$f$$) | nhiều |
| Dùng cho NPC cổ điển | **Có** | hiếm khi làm định nghĩa NPC |

Mọi Karp là Cook; ngược lại không tầm thường.

## Bài tập

1. Chứng minh bắc cầu với chặn: $$f$$ thời gian $$n^2$$, $$g$$ thời gian $$m^3$$.  
2. Chứng minh $$A\le_p B\Rightarrow\overline{A}\le_p\overline{B}$$.  
3. Đưa ví dụ “ý” Cook reduction không phải many-one (thảo luận).

## Đọc

Sipser; Arora–Barak §2.2; Garey–Johnson §5.

## Tóm tắt

$$\le_p$$ · truyền · kéo $$P$$ · xương sống NPC.

**Tiếp:** 20.6 — NP-hard / NP-complete.
