---
layout: post
title: "Cây Phân tích và Sự Mơ hồ"
categories: chapter19
date: 2021-01-01
order: 7
required: true
lang: en
excerpt: "Cây phân tích (parse tree), tương ứng với dẫn xuất trái nhất, định nghĩa văn phạm mơ hồ và ví dụ kinh điển như biểu thức số học và dangling else."
---

<div class="textbook-epigraph" markdown="1">

"Ambiguity is multiple stories for one string."

<span class="epigraph-attribution">— Parsing theory</span>

</div>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Vẽ** cây phân tích (*parse tree*) từ một dẫn xuất của văn phạm phi ngữ cảnh.
- **Định nghĩa** văn phạm mơ hồ (*ambiguous grammar*).
- **Chứng minh** một văn phạm cụ thể là mơ hồ bằng cách chỉ ra hai cây phân tích khác nhau cho cùng một chuỗi.

</div>

## Cây phân tích (*parse tree*)

Trong cây phân tích của một CFG, mỗi nút trong là một ký hiệu không kết thúc, các nút con của nó tương ứng với vế phải của luật sinh được áp dụng, còn các nút lá mang ký hiệu kết thúc hoặc $$\varepsilon$$. Chuỗi đọc các nút lá từ trái sang phải gọi là kết quả (*yield*) của cây.

<div class="textbook-theorem" markdown="1">

**Định lý** (Ý chính). Tồn tại tương ứng một–một giữa các dẫn xuất trái nhất (*leftmost derivations*) và các cây phân tích của một chuỗi.

</div>

## Sự mơ hồ (*ambiguity*)

<div class="textbook-definition" markdown="1">

Một văn phạm $$G$$ được gọi là **mơ hồ** (*ambiguous*) nếu tồn tại ít nhất một chuỗi $$w \in L(G)$$ có từ hai dẫn xuất trái nhất khác nhau trở lên (tương đương với từ hai cây phân tích khác nhau trở lên).

</div>

**Ví dụ.** Với văn phạm $$E\to E+E\mid\mathrm{id}$$, chuỗi $$\mathrm{id}+\mathrm{id}+\mathrm{id}$$ có hai cây phân tích khác nhau tùy theo cách nhóm ngoặc trái hay phải. Một ví dụ kinh điển khác trong ngôn ngữ lập trình C/Java là hiện tượng **dangling else** trong cấu trúc `if-else` lồng nhau.

### Minh họa cây phân tích và sự mơ hồ

Theo dõi dẫn xuất trái nhất dựng cây phân tích từng bước; với các văn phạm mơ hồ (biểu thức số học, dangling else), bạn có thể chuyển đổi qua lại giữa các cây phân tích khác nhau của cùng một chuỗi:

<div class="interactive-demo" markdown="1">
<div data-demo="derive-explainer" data-preset="expr-amb"></div>
</div>
<script src="{{ '/public/js/explainers/language-explainer.js' | relative_url }}"></script>

## Bài tập

1. Vẽ hai cây phân tích khác nhau cho chuỗi $$\mathrm{id}+\mathrm{id}*\mathrm{id}$$ khi phép `*` và `+` chưa được phân tầng độ ưu tiên.
2. Viết lại một văn phạm không mơ hồ cho biểu thức chứa `+` và `*` với quy tắc kết hợp trái và `*` ưu tiên cao hơn `+`.
3. Tìm hiểu khái niệm ngôn ngữ mơ hồ nội tại (*inherent ambiguity*).

## Tài liệu đọc thêm

Aho–Sethi–Ullman (*Compilers: Principles, Techniques, and Tools* — Dragon Book); Sipser.

## Tóm tắt

Cây phân tích thể hiện cấu trúc cú pháp của chuỗi; việc loại bỏ sự mơ hồ bằng cách thiết kế phân tầng độ ưu tiên là yêu cầu thiết yếu khi xây dựng trình phân tích cú pháp.

**Bài tiếp theo:** Ô-tô-mát đẩy xuống (PDA).

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=u4-rpIlV9NI">Derivation Tree (Left &amp; Right Derivation Trees)</a> — Neso Academy, tiếng Anh. Giới thiệu cây dẫn xuất trái và cây dẫn xuất phải.
- <a href="https://www.youtube.com/watch?v=wQjppolFdas">Ambiguous Grammar</a> — Neso Academy, tiếng Anh. Giải thích văn phạm mơ hồ khi một chuỗi có từ hai cây phân tích trở lên.
- <a href="https://www.youtube.com/watch?v=ejXgLRSIxsA">Derivations from a Grammar</a> — Neso Academy, tiếng Anh. Mối liên hệ giữa từng bước dẫn xuất và từng nhánh của cây phân tích.
