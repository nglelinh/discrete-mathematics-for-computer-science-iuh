---
layout: post
title: "Bảng chữ cái, Chuỗi và Ngôn ngữ"
categories: chapter19
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Định nghĩa bảng chữ cái Σ, chuỗi w, chuỗi rỗng ε, bao đóng Σ*, ngôn ngữ hình thức L và các tính chất cơ bản của phép nối chuỗi."
---

<div class="textbook-epigraph" markdown="1">

"A language is a set of strings over an alphabet."

<span class="epigraph-attribution">— Formal language theory</span>

</div>

![Σ*](/discrete-mathematics-for-computer-science-iuh/img/course/Lang_sigma_star.svg)

<p class="textbook-figure-caption" data-figure="19.1">Ngôn ngữ hình thức là một tập con $$L\subseteq\Sigma^*$$.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** bảng chữ cái (*alphabet*), chuỗi (*string*) và ngôn ngữ hình thức (*language*).
- **Chứng minh** các đẳng thức cơ bản về phép nối chuỗi và độ dài chuỗi.

</div>

## Định nghĩa

<div class="textbook-definition" markdown="1">

- **Bảng chữ cái** $$\Sigma$$ là một tập hữu hạn khác rỗng các ký hiệu.
- **Chuỗi** (*string*) là một dãy hữu hạn các ký hiệu thuộc $$\Sigma$$; chuỗi rỗng ký hiệu là $$\varepsilon$$ và độ dài của chuỗi $$w$$ ký hiệu là $$\lvert w\rvert$$.
- Tập tất cả các chuỗi hữu hạn trên $$\Sigma$$ là $$\Sigma^*=\bigcup_{k\ge 0}\Sigma^k$$, với $$\Sigma^0=\{\varepsilon\}$$.
- **Ngôn ngữ hình thức** trên $$\Sigma$$ là một tập con bất kỳ $$L\subseteq\Sigma^*$$.

</div>

<div class="textbook-theorem" markdown="1">

**Định lý.** Với mọi chuỗi $$x, y, z, w \in \Sigma^*$$, ta có: $$\lvert xy\rvert=\lvert x\rvert+\lvert y\rvert$$, tính kết hợp $$(xy)z=x(yz)$$ và phần tử đơn vị $$w\varepsilon=\varepsilon w=w$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.** Suy trực tiếp từ định nghĩa dãy hữu hạn và phép nối hai dãy ký hiệu.

</div>

## Bài tập

1. Liệt kê tất cả các chuỗi trong $$\Sigma^{\le 2}$$ với $$\Sigma=\{a,b\}$$.
2. Chứng minh độ dài của chuỗi đảo ngược bằng độ dài chuỗi ban đầu: $$\lvert w^R\rvert=\lvert w\rvert$$.
3. Phân biệt rõ hai ngôn ngữ $$\emptyset$$ và $$\{\varepsilon\}$$.

## Tài liệu đọc thêm

Sipser §0–1; Hopcroft §1.

## Tóm tắt

Ngôn ngữ hình thức được xây dựng từ ba khái niệm cơ sở: bảng chữ cái $$\Sigma$$, chuỗi hữu hạn và tập con $$L\subseteq\Sigma^*$$.

**Bài tiếp theo:** Các phép toán trên ngôn ngữ.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=7MBpk4gJRkk">[Discrete Mathematics] Formal Languages</a> — TrevTutor, tiếng Anh. Giới thiệu bảng chữ cái, chuỗi và ngôn ngữ hình thức.
- <a href="https://www.youtube.com/watch?v=s6clCKVoXig">[Discrete Mathematics] Formal Languages Examples</a> — TrevTutor, tiếng Anh. Các ví dụ về ngôn ngữ con của $$\Sigma^*$$.
- <a href="https://www.youtube.com/watch?v=58N2N7zJGrQ">Introduction to Theory of Computation</a> — Neso Academy, tiếng Anh. Đặt ngôn ngữ hình thức vào tổng thể lý thuyết tính toán.
