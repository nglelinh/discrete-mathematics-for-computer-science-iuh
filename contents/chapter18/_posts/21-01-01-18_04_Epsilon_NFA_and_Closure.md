---
layout: post
title: "ε-NFA và Epsilon-closure"
categories: chapter18
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Chuyển trạng thái ε, định nghĩa bao đóng epsilon E(S), thuật toán tính bao đóng và điều kiện chấp nhận của ε-NFA."
---

<div class="textbook-epigraph" markdown="1">

"ε-moves stitch machines together — Kleene’s algebra becomes automata."

<span class="epigraph-attribution">— Thompson construction spirit</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** ε-NFA và bao đóng epsilon $$E(S)$$.
- **Chứng minh** các tính chất cơ bản của phép lấy bao đóng.
- **Tính** $$E(S)$$ bằng thuật toán DFS hoặc BFS trên các cạnh ε.

</div>

## Định nghĩa

Trong ε-NFA, hàm chuyển được mở rộng để cho phép dịch chuyển mà không cần đọc ký hiệu đầu vào: $$\delta:Q\times(\Sigma\cup\{\varepsilon\})\to\mathcal{P}(Q)$$.

<div class="textbook-definition" markdown="1">

**Bao đóng epsilon** (*epsilon-closure*) $$E(S)$$ là tập tất cả các trạng thái có thể đi tới từ ít nhất một trạng thái trong $$S$$ chỉ bằng không hoặc nhiều bước chuyển ε (luôn bao gồm chính $$S$$).

</div>

<div class="textbook-theorem" markdown="1">

**Định lý.** Với mọi tập trạng thái $$S, T \subseteq Q$$, ta có $$E(E(S))=E(S)$$, $$S\subseteq E(S)$$, và nếu $$S\subseteq T$$ thì $$E(S)\subseteq E(T)$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.** Ba tính chất trên suy trực tiếp từ bản chất bao đóng phản xạ và bắc cầu của quan hệ “có đường đi chỉ gồm các cạnh ε”.

</div>

## Điều kiện chấp nhận

Khi đang ở tập trạng thái $$S$$ và đọc ký hiệu $$a \in \Sigma$$, tập trạng thái mới là $$S' = E\bigl(\bigcup_{q\in S}\delta(q,a)\bigr)$$. Máy bắt đầu từ tập trạng thái $$E(\{q_0\})$$ và chấp nhận chuỗi nếu tập trạng thái cuối cùng có giao khác rỗng với $$F$$.

## Thuật toán tính bao đóng

Để tính $$E(S)$$, ta dùng ngăn xếp (DFS) hoặc hàng đợi (BFS) khởi tạo từ $$S$$, chỉ duyệt dọc theo các cạnh ε và đánh dấu các trạng thái đã thăm. Độ phức tạp thời gian là $$O(\lvert Q\rvert+\lvert E_\varepsilon\rvert)$$.

### Minh họa tương tác

Quan sát hoạt động của ε-NFA và cách tính bao đóng ε ngay từ trạng thái khởi đầu:

<div class="interactive-demo" markdown="1">
<div data-demo="automata-explainer" data-preset="enfa" data-tab="simulate"></div>
</div>
<script src="{{ '/public/js/explainers/automata-explainer.js' | relative_url }}"></script>

## Bài tập

1. Chứng minh đầy đủ ba tính chất của phép toán $$E(S)$$ trong định lý trên.
2. Vẽ một ε-NFA nhận hợp của hai DFA bằng cách tạo một trạng thái khởi đầu mới nối bằng cạnh ε tới hai trạng thái khởi đầu cũ.
3. Giải thích trực giác vì sao bước chuyển ε không làm tăng sức mạnh biểu diễn của ô-tô-mát hữu hạn (chuẩn bị cho phép xây dựng tập con ở bài sau).

## Tài liệu đọc thêm

Sipser; Hopcroft–Ullman (phần khử chuyển ε).

## Tóm tắt

Bao đóng epsilon $$E(S)$$ cho phép định nghĩa chặt chẽ việc chấp nhận chuỗi trên ε-NFA và là công cụ thuận tiện để ghép nối các ô-tô-mát thành phần.

**Bài tiếp theo:** Xây dựng tập con (*subset construction*).

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=84oNUttWlN4">Epsilon NFA</a> — Neso Academy, tiếng Anh. Giới thiệu bước chuyển ε và lý do cần khái niệm epsilon-closure.
- <a href="https://www.youtube.com/watch?v=WSGcmaHNBFM">Conversion of Epsilon NFA to NFA</a> — Neso Academy, tiếng Anh. Cách khử chuyển ε để thu được NFA thông thường.
- <a href="https://www.youtube.com/watch?v=I6GFKekMr7s">Conversion of Epsilon NFA to NFA - Examples (Part 1)</a> — Neso Academy, tiếng Anh. Ví dụ cụ thể về tính bao đóng và dựng lại bảng chuyển trạng thái.
