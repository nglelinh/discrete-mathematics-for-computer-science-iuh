---
layout: post
title: "Ghi chú mở rộng: Biểu diễn tập hợp gọn (2022–2026)"
categories: chapter04
date: 2021-01-01
order: 6
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. Binary fuse filters (JEA 2022) store an approximate indicator of a finite set near the information-theoretic limit. Does not replace set-theory lessons."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite unions, products, or cardinality theory.

Bài ghi chú ứng dụng song ngữ. Nội dung này **không** thay thế hay viết lại các bài về phép hợp, tích Descartes hay lý thuyết lực lượng.

</div>

## English

A finite set $$S \subseteq U$$ is fully specified by its characteristic function $$\mathbf{1}_S : U \to \{0,1\}$$. When $$\vert S\vert $$ is huge and exact membership is too expensive, systems store a **compact approximate set**: a structure that answers “$$x \in S$$?” with one-sided error.

Graf and Lemire, “Binary Fuse Filters: Fast and Smaller Than Xor Filters,” *ACM Journal of Experimental Algorithmics* 27, Article 1.5 (2022), [DOI 10.1145/3510449](https://doi.org/10.1145/3510449), construct filters within about **13%** of the information-theoretic storage lower bound (about **8%** if query speed is relaxed), with construction often more than twice as fast as xor filters. They compare Bloom, blocked Bloom, cuckoo, ribbon, and xor filters.

The discrete-math reading is direct:

- the stored object is still a representation of a **set**;
- false positives are forced by pigeonhole once the bit budget is below $$\log_2 \binom{\vert U\vert }{\vert S\vert }$$;
- engineers choose $$\vert S\vert $$, fingerprint width, and failure probability — set parameters, not a different theory.

Use this after the required set lessons and the database applications lesson. It is an optional 2022 snapshot of how production systems encode sets when RAM is the scarce resource.

**Citations**

1. T. M. Graf and D. Lemire, “Binary Fuse Filters: Fast and Smaller Than Xor Filters,” *J. Exp. Algorithmics* 27 (2022). [DOI](https://doi.org/10.1145/3510449)

**Questions.** (1) Is a binary fuse filter a subset of $$U$$, or a *lossy encoding* of one? (2) Which set operation remains cheap after you only store a filter?

## Tiếng Việt

Một tập hữu hạn $$S \subseteq U$$ được xác định hoàn toàn bởi hàm đặc trưng $$\mathbf{1}_S : U \to \{0,1\}$$. Khi $$\vert S\vert$$ rất lớn và việc lưu trữ chính xác quá tốn kém, các hệ thống thường dùng **cấu trúc biểu diễn tập xấp xỉ gọn**: trả lời câu hỏi “$$x \in S$$?” với sai số một phía (có thể dương tính giả, không có âm tính giả).

Trong bài báo trên *ACM JEA* năm 2022, Graf và Lemire đề xuất *binary fuse filter* với dung lượng lưu trữ chỉ cách cận dưới lý thuyết thông tin khoảng **13%** (còn khoảng **8%** nếu chấp nhận truy vấn chậm hơn), đồng thời có tốc độ xây dựng thường nhanh gấp hơn hai lần so với xor filter. Nhóm tác giả cũng so sánh cấu trúc này với Bloom filter, blocked Bloom, cuckoo, ribbon và xor filter.

Dưới góc nhìn toán rời rạc: đối tượng được lưu vẫn là một cách biểu diễn của **tập hợp**; dương tính giả là hệ quả tất yếu của nguyên lý chuồng bồ câu khi số bit lưu trữ nhỏ hơn $$\log_2 \binom{\vert U\vert}{\vert S\vert}$$; và các tham số kỹ sư lựa chọn — gồm $$\vert S\vert$$, độ rộng dấu vân tay (fingerprint) và xác suất sai số — vẫn là những tham số của bài toán biểu diễn tập hợp.

Bạn nên đọc phần này sau các mục tập hợp bắt buộc để thấy một ví dụ từ năm 2022 về cách hệ thống thực tế mã hóa tập hợp khi bộ nhớ RAM bị giới hạn.

**Câu hỏi.** (1) Binary fuse filter là một tập con của $$U$$ hay là một *biểu diễn nén có mất mát* của tập con đó? (2) Phép toán tập hợp nào vẫn có chi phí thấp khi hệ thống chỉ lưu giữ bộ lọc này?

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=V3pzxngeLqw">Bloom Filters | Algorithms You Should Know #2 | Real-world Examples</a> — ByteByteGo, tiếng Anh. Giới thiệu tập xấp xỉ qua Bloom filter — trả lời câu hỏi thuộc tập với sai số một phía.
- <a href="https://www.youtube.com/watch?v=kfFacplFY4Y">What Are Bloom Filters?</a> — Spanning Tree, tiếng Anh. Giải thích cách mảng bit và hàm băm mã hóa một tập lớn trong bộ nhớ nhỏ.
- <a href="https://www.youtube.com/watch?v=mPxslXpg8wA">Advanced Data Structures: Count-Min Sketches</a> — Niema Moshiri, tiếng Anh. Giới thiệu Count-Min Sketch, thuộc cùng nhóm cấu trúc dữ liệu nén tập hợp và đa tập.
