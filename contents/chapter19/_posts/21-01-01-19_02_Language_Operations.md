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

Nếu các ngôn ngữ là những viên gạch, thì các phép toán hợp, giao, bù, nối và bao đóng Kleene chính là lớp vữa ghép chúng thành các biểu thức chính quy, bộ phân tích từ vựng và ngôn ngữ lập trình phức tạp. Quan trọng hơn, câu hỏi *"Lớp ngôn ngữ $$\mathcal{C}$$ có đóng dưới phép toán này không?"* là một trong những vũ khí mạnh nhất để chứng minh một ngôn ngữ không thuộc lớp chính quy hay phi ngữ cảnh.

## Kiến thức cần nhớ: Ba nhóm phép toán trên Ngôn ngữ

1. **Phép toán tập hợp (Boolean)**:
   Hợp ($$L_1 \cup L_2$$), giao ($$L_1 \cap L_2$$), hiệu và phần bù ($$\overline{L} = \Sigma^* \setminus L$$). Lưu ý phần bù luôn phụ thuộc vào bảng chữ cái $$\Sigma$$ đã cố định.
2. **Phép toán chuỗi mở rộng (Nối, Đảo ngược, Bao đóng Kleene)**:
   Phép nối $$L_1 L_2$$, lũy thừa $$L^k$$, bao đóng $$L^* = \bigcup_{k \ge 0} L^k$$ và $$L^+ = \bigcup_{k \ge 1} L^k$$ tạo ra các ngôn ngữ vô hạn từ tập hữu hạn.
3. **Đồng cấu (Homomorphism) & Tính đóng (Closure Properties)**:
   Thay từng ký tự bằng một chuỗi theo ánh xạ $$h: \Sigma \to \Gamma^*$$. Tính đóng giúp xây dựng ngôn ngữ phức tạp từ ngôn ngữ đơn giản hoặc chứng minh phản chứng (ví dụ dùng giao với ngôn ngữ chính quy).

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

### Giải thích: Kiểm chứng bằng tay sự khác biệt giữa $$(L_1 \cup L_2)^*$$ và $$L_1^* \cup L_2^*$$

Cho hai ngôn ngữ cực nhỏ $$L_1 = \{a\}$$ và $$L_2 = \{b\}$$:
- $$L_1^* = \{\varepsilon, a, aa, aaa, \ldots\}$$ (chỉ toàn chữ `a`).
- $$L_2^* = \{\varepsilon, b, bb, bbb, \ldots\}$$ (chỉ toàn chữ `b`).
- Do đó $$L_1^* \cup L_2^* = \{\varepsilon, a, b, aa, bb, \ldots\}$$ — **không chứa** chuỗi trộn lẫn như `ab` hay `ba`!
- Ngược lại, $$(L_1 \cup L_2)^* = \{a, b\}^*$$ chứa **mọi** chuỗi trên $$\{a, b\}$$, bao gồm `ab`, `ba`, `aba`, `bab`...

**Phép kiểm tra đồng cấu (Homomorphism):** Định nghĩa $$h(0) = ab$$, $$h(1) = c$$. Khi đó với $$w = 010$$, ta tính từng ký tự rồi nối lại:
$$h(010) = h(0)h(1)h(0) = ab \cdot c \cdot ab = \text{abcab}.$$
Phép thử nhỏ này giúp tránh nhầm lẫn giữa phân phối phép nối và phép bao đóng Kleene trong các bài chứng minh đại số ngôn ngữ.

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
