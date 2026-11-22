---
layout: post
title: "NFA: Định nghĩa và Chấp nhận"
categories: chapter18
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Hàm chuyển đa trị của NFA, khái niệm đường chạy, ngôn ngữ chấp nhận L(N), so sánh với DFA và ví dụ chuỗi kết thúc bằng 01."
---

<div class="textbook-epigraph" markdown="1">

"Nondeterminism is a design convenience with a deterministic cost."

<span class="epigraph-attribution">— Automata theory</span>

</div>

![NFA](/discrete-mathematics-for-computer-science-iuh/img/course/Automata_nfa_ends_01.svg)

<p class="textbook-figure-caption" data-figure="18.2">NFA nhận chuỗi kết thúc bằng 01: máy có thể “đoán” thời điểm bắt đầu khớp hậu tố.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** NFA và ngôn ngữ chấp nhận $$L(N)$$.
- **Chứng minh** một chuỗi thuộc $$L(N)$$ bằng cách chỉ ra sự tồn tại của một đường chạy chấp nhận.

</div>

## Định nghĩa

<div class="textbook-definition" markdown="1">

**NFA** (*Nondeterministic Finite Automaton*) là bộ năm $$N=(Q,\Sigma,\delta,q_0,F)$$ với hàm chuyển đa trị $$\delta:Q\times\Sigma\to\mathcal{P}(Q)$$.

Chuỗi $$w = a_1a_2\ldots a_n$$ được **chấp nhận** nếu tồn tại ít nhất một dãy trạng thái $$q_0,q_1,\ldots,q_n$$ sao cho $$q_{i}\in\delta(q_{i-1},a_i)$$ với mọi $$i$$ và $$q_n\in F$$.

Ngôn ngữ của NFA là $$L(N)=\{w:\text{được chấp nhận bởi } N\}.$$

</div>

## Mở rộng $$\hat\delta$$ trên tập trạng thái

Ta mở rộng hàm chuyển sang tập trạng thái theo quy tắc $$\hat\delta(S,\varepsilon)=S$$ và $$\hat\delta(S,a)=\bigcup_{q\in S}\delta(q,a)$$, sau đó mở rộng đệ quy cho chuỗi bất kỳ. Khi đó, điều kiện chấp nhận được viết gọn là $$w\in L(N)\Leftrightarrow\hat\delta(\{q_0\},w)\cap F\neq\emptyset$$.

## Vì sao NFA thường gọn hơn DFA

Với các mẫu ngôn ngữ như “kết thúc bằng $$x$$” hoặc “chứa một trong nhiều mẫu cho trước”, NFA chỉ cần “đoán” vị trí bắt đầu khớp mẫu. Ngược lại, DFA phải ghi nhớ toàn bộ hậu tố liên quan nên thường cần nhiều trạng thái hơn trước khi tối tiểu hóa.

### Minh họa tương tác

Quan sát NFA như một tập hợp các trạng thái hoạt động song song thay đổi qua từng ký tự đầu vào:

<div class="interactive-demo" markdown="1">
<div data-demo="automata-explainer" data-preset="nfa101" data-tab="simulate"></div>
</div>
<script src="{{ '/public/js/explainers/automata-explainer.js' | relative_url }}"></script>

## Bài tập

1. Chứng minh chuỗi $$1101\in L$$ đối với NFA nhận chuỗi kết thúc bằng `01` bằng cách chỉ ra một đường chạy chấp nhận.
2. Lập bảng đầy đủ cho hàm chuyển $$\delta$$ của NFA đó.
3. Thảo luận sự khác biệt về số trạng thái giữa NFA và DFA tối tiểu.

## Tài liệu đọc thêm

Sipser §1.2.

## Tóm tắt

NFA sử dụng hàm chuyển đa trị, chấp nhận chuỗi khi tồn tại ít nhất một đường chạy kết thúc trong $$F$$, và thường giúp biểu diễn ngôn ngữ gọn gàng hơn.

**Bài tiếp theo:** ε-NFA và bao đóng epsilon.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=ehy0jGIYRtE">Non-Deterministic Finite Automata</a> — Neso Academy, tiếng Anh. Giới thiệu điểm khác biệt cốt lõi giữa NFA không đơn định và DFA.
- <a href="https://www.youtube.com/watch?v=egXhe55dAIk">Formal Definition of Non-Deterministic Finite Automata (NFA)</a> — Neso Academy, tiếng Anh. Trình bày bộ năm định nghĩa hình thức của NFA.
- <a href="https://www.youtube.com/watch?v=4bjqVsoy6bA">Non-Deterministic Finite Automata (Solved Example 1)</a> — Neso Academy, tiếng Anh. Minh họa cách một xâu được chấp nhận theo từng nhánh chuyển trạng thái.
