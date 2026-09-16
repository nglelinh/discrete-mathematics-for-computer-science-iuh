---
layout: post
title: "Optional note: Compact set representations (2022–2026)"
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

Bài ghi chú ứng dụng song ngữ. **Không** viết lại hợp, tích Descartes hay lý thuyết lực lượng.

</div>

## English

A finite set $$S \subseteq U$$ is fully specified by its characteristic function $$\mathbf{1}_S : U \to \{0,1\}$$. When $$|S|$$ is huge and exact membership is too expensive, systems store a **compact approximate set**: a structure that answers “$$x \in S$$?” with one-sided error.

Graf and Lemire, “Binary Fuse Filters: Fast and Smaller Than Xor Filters,” *ACM Journal of Experimental Algorithmics* 27, Article 1.5 (2022), [DOI 10.1145/3510449](https://doi.org/10.1145/3510449), construct filters within about **13%** of the information-theoretic storage lower bound (about **8%** if query speed is relaxed), with construction often more than twice as fast as xor filters. They compare Bloom, blocked Bloom, cuckoo, ribbon, and xor filters.

The discrete-math reading is direct:

- the stored object is still a representation of a **set**;
- false positives are forced by pigeonhole once the bit budget is below $$\log_2 \binom{|U|}{|S|}$$;
- engineers choose $$|S|$$, fingerprint width, and failure probability — set parameters, not a different theory.

Use this after the required set lessons and the database applications lesson. It is an optional 2022 snapshot of how production systems encode sets when RAM is the scarce resource.

**Citations**

1. T. M. Graf and D. Lemire, “Binary Fuse Filters: Fast and Smaller Than Xor Filters,” *J. Exp. Algorithmics* 27 (2022). [DOI](https://doi.org/10.1145/3510449)

**Questions.** (1) Is a binary fuse filter a subset of $$U$$, or a *lossy encoding* of one? (2) Which set operation remains cheap after you only store a filter?

## Tiếng Việt

Tập hữu hạn $$S \subseteq U$$ được xác định bởi hàm đặc trưng $$\mathbf{1}_S$$. Khi $$|S|$$ rất lớn, hệ thống lưu **tập xấp xỉ gọn**: trả lời “$$x \in S$$?” với sai một phía.

Graf và Lemire (JEA 2022) xây *binary fuse filter* cách cận dưới lưu trữ lý thuyết thông tin khoảng **13%** (khoảng **8%** nếu chấp nhận truy vấn chậm hơn), xây thường nhanh hơn xor filter hơn hai lần. Họ so với Bloom, blocked Bloom, cuckoo, ribbon và xor.

Cách đọc toán rời rạc: đối tượng lưu vẫn là biểu diễn của một **tập**; dương tính giả bị buộc bởi chuồng bồ câu khi ngân sách bit thấp hơn $$\log_2 \binom{|U|}{|S|}$$; kỹ sư chọn $$|S|$$, độ rộng fingerprint và xác suất lỗi — vẫn là tham số tập hợp.

Đọc sau các mục tập hợp bắt buộc. Đây là ảnh chụp 2022 của cách hệ thống production mã hóa tập khi RAM là tài nguyên hiếm.

**Câu hỏi.** (1) Binary fuse filter là tập con của $$U$$ hay là *mã hóa mất mát* của một tập? (2) Phép toán tập nào vẫn rẻ sau khi chỉ còn filter?
