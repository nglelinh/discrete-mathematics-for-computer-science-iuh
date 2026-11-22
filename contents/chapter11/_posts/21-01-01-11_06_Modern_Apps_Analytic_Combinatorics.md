---
layout: post
title: "Ghi chú mở rộng: Hàm sinh gặp bộ lọc năm 2022"
categories: chapter11
date: 2021-01-01
order: 6
required: false
lesson_type: optional
lang: vi
excerpt: "Bài ghi chú tùy chọn song ngữ: cận lưu trữ của binary fuse filter (JEA 2022) nhìn từ góc độ bài toán đếm, hàm sinh và nguyên lý bao hàm–loại trừ."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite generating-function algebra or inclusion–exclusion. Tagged `lang: vi` with this chapter’s theory posts.

Bài ghi chú ứng dụng song ngữ, **không** viết lại phần lý thuyết đại số hàm sinh hay nguyên lý bao hàm–loại trừ.

</div>

## English

Ordinary generating functions package a counting sequence $$(a_n)$$ as $$A(x) = \sum a_n x^n$$. Space lower bounds for approximate sets are the same kind of count: how many distinct filters of $$m$$ bits can you have, and how many $$n$$-element sets must they separate up to false-positive rate $$\varepsilon$$?

Graf and Lemire (JEA 2022, [DOI 10.1145/3510449](https://doi.org/10.1145/3510449)) show binary fuse filters land within **13%** (resp. **8%**) of that information-theoretic floor. The floor itself is a counting / generating-function statement: the number of representable “yes” patterns cannot be smaller than the number of sets you claim to distinguish. Inclusion–exclusion (this chapter) appears when you estimate collision probabilities across several hash locations — the same union bound / exact-count tension you used for derangements.

This optional note does not derive a new GF identity. It points at a 2022 structure whose *headline number* (percent above the bound) is meaningless unless you can read it as a counting argument.

**Citations**

1. T. M. Graf and D. Lemire, “Binary Fuse Filters: Fast and Smaller Than Xor Filters,” *J. Exp. Algorithmics* 27 (2022). [DOI](https://doi.org/10.1145/3510449)

**Questions.** (1) Which generating function would encode “number of $$m$$-bit filters”? (2) Where does inclusion–exclusion enter a false-positive calculation with three hash positions?

## Tiếng Việt

Hàm sinh thông thường đóng gói một dãy đếm $$(a_n)$$ thành $$A(x) = \sum a_n x^n$$. Cận dưới về dung lượng lưu trữ cho cấu trúc biểu diễn tập xấp xỉ cũng thuộc cùng dạng bài toán đếm này: có bao nhiêu bộ lọc $$m$$ bit phân biệt nhau, và chúng cần phân tách bao nhiêu tập $$n$$ phần tử với tỷ lệ dương tính giả không vượt quá $$\varepsilon$$?

Graf và Lemire (JEA 2022) chỉ ra rằng bộ lọc binary fuse chỉ vượt cận dưới lý thuyết thông tin khoảng **13%** (hoặc **8%**). Bản thân cận dưới đó là một lập luận đếm / hàm sinh: số mẫu trạng thái “có” biểu diễn được không thể nhỏ hơn số tập hợp mà bộ lọc cần phân biệt. Nguyên lý bao hàm–loại trừ xuất hiện khi ước lượng xác suất va chạm trên nhiều vị trí băm — tương tự mối quan hệ giữa cận hợp (union bound) và phép đếm chính xác trong bài toán derangement.

Ghi chú này không xây dựng thêm đồng nhất thức hàm sinh mới, mà giới thiệu một cấu trúc dữ liệu năm 2022 trong đó con số tiêu biểu (phần trăm vượt trên cận dưới) chỉ thực sự có ý nghĩa khi được hiểu dưới góc độ lập luận đếm.

**Câu hỏi.** (1) Hàm sinh nào có thể mã hóa “số lượng bộ lọc $$m$$ bit”? (2) Nguyên lý bao hàm–loại trừ xuất hiện ở bước nào khi tính tỷ lệ dương tính giả với ba vị trí băm?

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=-drdeNMoe8w">GENERATING FUNCTIONS - Discrete Mathematics</a> — TrevTutor, tiếng Anh. Giới thiệu hàm sinh — công cụ đếm có cùng bản chất với cận lưu trữ của bộ lọc.
- <a href="https://www.youtube.com/watch?v=V3pzxngeLqw">Bloom Filters | Algorithms You Should Know #2 | Real-world Examples</a> — ByteByteGo, tiếng Anh. Minh họa Bloom filter và ngân sách bit khi biểu diễn tập xấp xỉ.
- <a href="https://www.youtube.com/watch?v=eV1haPUt0NU">Hyperloglog: Facebook&#x27;s algorithm to count distinct elements</a> — Gaurav Sen, tiếng Anh. Bài toán ước lượng lực lượng tập hợp, cùng hướng tiếp cận lý thuyết thông tin với fuse filter.
