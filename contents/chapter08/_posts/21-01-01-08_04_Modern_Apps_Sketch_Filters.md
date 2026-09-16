---
layout: post
title: "Optional note: Pigeonhole bounds in modern filters (2022–2026)"
categories: chapter08
date: 2021-01-01
order: 4
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. Binary fuse filters (JEA 2022) sit a few percent above the pigeonhole / information-theoretic floor for set sketches. Does not replace Dirichlet theory."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite the pigeonhole principle or the existing computing applications lesson.

Bài ghi chú ứng dụng song ngữ. **Không** viết lại nguyên lý Dirichlet hay bài ứng dụng trong khoa học máy tính.

</div>

## English

Dirichlet’s principle is why **perfect** compact membership is impossible: more pigeons (keys) than holes (bit patterns) forces a collision. Approximate membership structures accept a false-positive rate $$\varepsilon$$ and then ask how close they sit to the information-theoretic floor $$\approx n \log_2(1/\varepsilon)$$ bits for $$n$$ keys.

Graf and Lemire, “Binary Fuse Filters: Fast and Smaller Than Xor Filters,” *J. Exp. Algorithmics* 27, Article 1.5 (2022), [DOI 10.1145/3510449](https://doi.org/10.1145/3510449), report constructions within **13%** of that lower bound (about **8%** with a slower layout), beating xor filters on space and often on build time, and comparing Bloom, cuckoo, and ribbon filters.

The optional takeaway for Chapter 8: the 2022 data-structure race is a quantitative pigeonhole contest. Hash collisions in tables (already in the required lessons) are the same phenomenon with a different layout. Binary fuse filters do not repeal Dirichlet; they spend bits more carefully after you accept that some holes must be shared.

**Citations**

1. T. M. Graf and D. Lemire, “Binary Fuse Filters: Fast and Smaller Than Xor Filters,” *J. Exp. Algorithmics* 27 (2022). [DOI](https://doi.org/10.1145/3510449)

**Questions.** (1) If you demand $$\varepsilon = 0$$ and $$n > m$$ fingerprints, which theorem of this chapter applies? (2) Why is “13% above the lower bound” a pigeonhole statement rather than a machine-learning statement?

## Tiếng Việt

Nguyên lý Dirichlet giải thích vì sao thành viên tập **hoàn hảo** và siêu gọn là bất khả: nhiều chim hơn lỗ buộc va chạm. Cấu trúc thành viên xấp xỉ chấp nhận tỷ lệ dương tính giả $$\varepsilon$$ rồi hỏi chúng cách sàn lý thuyết thông tin $$\approx n \log_2(1/\varepsilon)$$ bit bao xa.

Graf và Lemire (JEA 2022) báo cáo binary fuse filter cách cận dưới **13%** (khoảng **8%** nếu layout chậm hơn), thắng xor filter về không gian và thường cả thời gian xây, đồng thời so với Bloom, cuckoo và ribbon.

Bài học tùy chọn: cuộc đua cấu trúc dữ liệu 2022 là cuộc thi chuồng bồ câu định lượng. Va chạm bảng băm (đã có trong mục bắt buộc) là cùng hiện tượng, khác layout. Binary fuse không bãi bỏ Dirichlet; chúng tiêu bit cẩn thận hơn sau khi chấp nhận một số lỗ phải dùng chung.

**Câu hỏi.** (1) Nếu đòi $$\varepsilon = 0$$ và $$n > m$$ fingerprint, định lý nào của chương áp dụng? (2) Vì sao “cao hơn cận dưới 13%” là phát biểu chuồng bồ câu chứ không phải học máy?
