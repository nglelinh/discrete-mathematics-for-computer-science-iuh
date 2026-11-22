---
layout: post
title: "Phép toán trên Ngôn ngữ"
categories: chapter19
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Các phép toán hợp, giao, bù, nối và bao đóng sao Kleene trên ngôn ngữ; chứng minh các đẳng thức đại số ngôn ngữ cơ bản."
---

<div class="textbook-epigraph" markdown="1">

"Language operations are set operations with concatenation structure."

<span class="epigraph-attribution">— Algebra of languages</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Thực hiện** các phép toán hợp ($$\cup$$), giao ($$\cap$$), lấy bù, nối chuỗi và bao đóng sao ($$*$$) trên ngôn ngữ.
- **Chứng minh** một số đẳng thức cơ bản của đại số ngôn ngữ.

</div>

<div class="textbook-definition" id="định-nghĩa" markdown="1">

**Định nghĩa.** Cho các ngôn ngữ $$L, L_1, L_2 \subseteq \Sigma^*$$:

- **Phép nối:** $$L_1L_2=\{xy:x\in L_1,y\in L_2\}$$.
- **Bao đóng Kleene và bao đóng dương:** $$L^*=\bigcup_{k\ge 0}L^k$$ với $$L^0=\{\varepsilon\}$$, và $$L^+=LL^*$$.

</div>

## Định lý

<div class="textbook-theorem" markdown="1">

**Định lý.** Với mọi ngôn ngữ $$L, L_1, L_2, L_3$$:  
(1) $$L\emptyset=\emptyset L=\emptyset$$.  
(2) $$L\{\varepsilon\}=\{\varepsilon\}L=L$$.  
(3) $$(L_1\cup L_2)L_3=L_1L_3\cup L_2L_3$$.  
(4) $$(L^*)^*=L^*$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh (4).** Ta có $$L^*\subseteq(L^*)^*$$ vì mọi tập $$A$$ đều thỏa $$A\subseteq A^*$$. Ngược lại, để chứng minh $$(L^*)^*\subseteq L^*$$, nhận xét rằng mọi phần tử của $$(L^*)^*$$ đều là phép nối hữu hạn của các chuỗi thuộc $$L^*$$, mà mỗi chuỗi trong $$L^*$$ lại là phép nối hữu hạn của các chuỗi thuộc $$L$$, nên kết quả vẫn thuộc $$L^*$$.

</div>

## Bài tập

1. Chứng minh tính chất phân phối (3): $$(L_1\cup L_2)L_3=L_1L_3\cup L_2L_3$$.
2. Đưa ra phản ví dụ chứng minh đẳng thức $$(L_1L_2)^*=L_1^*L_2^*$$ nói chung là sai.
3. So sánh $$L^+$$ và $$L^*$$ trong trường hợp $$\varepsilon\in L$$.

## Tài liệu đọc thêm

Sipser; Hopcroft–Ullman.

## Tóm tắt

Đại số ngôn ngữ mở rộng các phép toán tập hợp bằng phép nối chuỗi và phép bao đóng sao (có tính lũy đẳng $$(L^*)^* = L^*$$).

**Bài tiếp theo:** Văn phạm tổng quát.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=6aRJQNYYz4s">Operations on Regular Languages</a> — Neso Academy, tiếng Anh. Giới thiệu các phép hợp, nối và sao được định nghĩa trong bài.
- <a href="https://www.youtube.com/watch?v=7MBpk4gJRkk">[Discrete Mathematics] Formal Languages</a> — TrevTutor, tiếng Anh. Ôn lại khái niệm ngôn ngữ như một tập chuỗi trước khi thực hiện phép toán.
- <a href="https://www.youtube.com/watch?v=s6clCKVoXig">[Discrete Mathematics] Formal Languages Examples</a> — TrevTutor, tiếng Anh. Ví dụ nhỏ để kiểm chứng các đẳng thức sau phép toán ngôn ngữ.
