---
layout: post
title: "Optional note: Generating functions meet 2022 filters"
categories: chapter11
date: 2021-01-01
order: 6
required: false
lesson_type: optional
lang: vi
excerpt: "Bài tùy chọn song ngữ. Cận lưu trữ của binary fuse filter (JEA 2022) là bài toán đếm / hàm sinh thông tin — cùng họ công cụ với hàm sinh và bao hàm–loại trừ. Không viết lại lý thuyết."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite generating-function algebra or inclusion–exclusion. Tagged `lang: vi` with this chapter’s theory posts.

Bài ghi chú ứng dụng song ngữ. **Không** viết lại đại số hàm sinh hay bao hàm–loại trừ.

</div>

## English

Ordinary generating functions package a counting sequence $$(a_n)$$ as $$A(x) = \sum a_n x^n$$. Space lower bounds for approximate sets are the same kind of count: how many distinct filters of $$m$$ bits can you have, and how many $$n$$-element sets must they separate up to false-positive rate $$\varepsilon$$?

Graf and Lemire (JEA 2022, [DOI 10.1145/3510449](https://doi.org/10.1145/3510449)) show binary fuse filters land within **13%** (resp. **8%**) of that information-theoretic floor. The floor itself is a counting / generating-function statement: the number of representable “yes” patterns cannot be smaller than the number of sets you claim to distinguish. Inclusion–exclusion (this chapter) appears when you estimate collision probabilities across several hash locations — the same union bound / exact-count tension you used for derangements.

This optional note does not derive a new GF identity. It points at a 2022 structure whose *headline number* (percent above the bound) is meaningless unless you can read it as a counting argument.

**Citations**

1. T. M. Graf and D. Lemire, “Binary Fuse Filters: Fast and Smaller Than Xor Filters,” *J. Exp. Algorithmics* 27 (2022). [DOI](https://doi.org/10.1145/3510449)

**Questions.** (1) Which generating function would encode “number of $$m$$-bit filters”? (2) Where does inclusion–exclusion enter a false-positive calculation with three hash positions?

## Tiếng Việt

Hàm sinh thường gói dãy đếm $$(a_n)$$ thành $$A(x) = \sum a_n x^n$$. Cận dưới không gian cho tập xấp xỉ là cùng kiểu đếm: có bao nhiêu filter $$m$$ bit phân biệt được, và phải tách bao nhiêu tập $$n$$ phần tử với tỷ lệ dương tính giả $$\varepsilon$$?

Graf và Lemire (JEA 2022) cho thấy binary fuse filter cách sàn lý thuyết thông tin **13%** (hoặc **8%**). Bản thân sàn là phát biểu đếm / hàm sinh: số mẫu “yes” biểu diễn được không thể nhỏ hơn số tập bạn tuyên bố phân biệt. Bao hàm–loại trừ xuất hiện khi ước lượng xác suất va chạm trên nhiều vị trí băm — cùng căng thẳng bound hợp / đếm đúng như bài toán derangement.

Ghi chú không dựng đồng nhất thức GF mới. Nó trỏ tới cấu trúc 2022 mà *số headline* (phần trăm trên cận) vô nghĩa nếu không đọc được như lập luận đếm.

**Câu hỏi.** (1) Hàm sinh nào mã hóa “số filter $$m$$ bit”? (2) Bao hàm–loại trừ vào đâu trong tính dương tính giả với ba vị trí băm?
