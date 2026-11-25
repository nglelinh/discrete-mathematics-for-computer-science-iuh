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

Trước khi xây dựng trình biên dịch cho Python hay thiết kế một biểu thức chính quy lọc email, khoa học máy tính cần một nền móng ký hiệu tuyệt đối chặt chẽ: thế nào là một ký tự, một chuỗi rỗng khác gì với một tập ngôn ngữ rỗng, và làm sao chứng minh một tính chất đúng với *mọi* chuỗi dài tùy ý? Bài học mở đầu Chương 19 thiết lập đúng "bảng chữ cái toán học" đó cho toàn bộ lý thuyết ngôn ngữ hình thức.

## Kiến thức cần nhớ: Ba trụ cột của Chuỗi và Ngôn ngữ hình thức

1. **Bảng chữ cái ($$\Sigma$$), Chuỗi ($$w$$) và Chuỗi rỗng ($$\varepsilon$$)**:
   $$\Sigma$$ là tập hữu hạn khác rỗng các ký hiệu; $$\Sigma^*$$ là tập tất cả các chuỗi hữu hạn sinh từ $$\Sigma$$ (kể cả chuỗi rỗng $$\varepsilon$$ có độ dài $$0$$).
2. **Phép nối chuỗi (Concatenation) & Cấu trúc vị nhóm tự do (Free Monoid)**:
   Phép nối có tính kết hợp và nhận $$\varepsilon$$ làm phần tử đơn vị, nhưng **không giao hoán** ($$ab \neq ba$$). Đây là lý do đại số ngôn ngữ tinh tế hơn phép cộng số học thông thường.
3. **Ngôn ngữ là Tập con của $$\Sigma^*$$ (Phân biệt $$\emptyset$$ và $$\{\varepsilon\}$$)**:
   Một ngôn ngữ $$L \subseteq \Sigma^*$$ có thể hữu hạn hoặc vô hạn đếm được. Hiểu rõ sự khác biệt giữa tập rỗng $$\emptyset$$ (0 chuỗi) và $$\{\varepsilon\}$$ (1 chuỗi có độ dài 0) giúp tránh lỗi kinh điển ở mọi bài toán văn phạm phía sau.

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

### Giải thích: Tính tay kích thước $$\Sigma^k$$ và phân biệt $$\emptyset$$ với $$\{\varepsilon\}$$

Cho bảng chữ cái nhị phân $$\Sigma = \{0, 1\}$$ (có $$\vert \Sigma \vert = 2$$ ký hiệu):

| Tập chuỗi | Các phần tử cụ thể | Số phần tử |
| :--- | :--- | :---: |
| $$\Sigma^0$$ | $$\{\varepsilon\}$$ | $$2^0 = 1$$ |
| $$\Sigma^1$$ | $$\{0, 1\}$$ | $$2^1 = 2$$ |
| $$\Sigma^2$$ | $$\{00, 01, 10, 11\}$$ | $$2^2 = 4$$ |
| $$\Sigma^3$$ | $$\{000, 001, 010, 011, 100, 101, 110, 111\}$$ | $$2^3 = 8$$ |

**Kiểm tra bẫy kinh điển với phép nối ngôn ngữ:** Cho $$L = \{01, 1\}$$.
- $$L \cdot \{\varepsilon\} = \{01\varepsilon, 1\varepsilon\} = \{01, 1\} = L$$ (vì $$\{\varepsilon\}$$ là phần tử đơn vị, giống số $$1$$ trong phép nhân).
- $$L \cdot \emptyset = \emptyset$$ (không chọn được phần tử nào từ $$\emptyset$$, giống số $$0$$ trong phép nhân).
- Lưu ý $$\emptyset^* = \{\varepsilon\}$$ (vì bao đóng Kleene luôn chứa lũy thừa bậc 0 là $$\Sigma^0 = \{\varepsilon\}$$), còn $$\emptyset^+ = \emptyset$$!

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
