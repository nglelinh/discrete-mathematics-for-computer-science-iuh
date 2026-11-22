---
layout: post
title: "Ghi chú mở rộng: Cận chuồng bồ câu trong bộ lọc hiện đại (2022–2026)"
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

Ghi chú ứng dụng song ngữ (tiếng Anh, sau đó là tiếng Việt). Bài này **không** thay thế nội dung về nguyên lý Dirichlet hay bài ứng dụng trong khoa học máy tính.

</div>

## English

Dirichlet’s principle is why **perfect** compact membership is impossible: more pigeons (keys) than holes (bit patterns) forces a collision. Approximate membership structures accept a false-positive rate $$\varepsilon$$ and then ask how close they sit to the information-theoretic floor $$\approx n \log_2(1/\varepsilon)$$ bits for $$n$$ keys.

Graf and Lemire, “Binary Fuse Filters: Fast and Smaller Than Xor Filters,” *J. Exp. Algorithmics* 27, Article 1.5 (2022), [DOI 10.1145/3510449](https://doi.org/10.1145/3510449), report constructions within **13%** of that lower bound (about **8%** with a slower layout), beating xor filters on space and often on build time, and comparing Bloom, cuckoo, and ribbon filters.

The optional takeaway for Chapter 8: the 2022 data-structure race is a quantitative pigeonhole contest. Hash collisions in tables (already in the required lessons) are the same phenomenon with a different layout. Binary fuse filters do not repeal Dirichlet; they spend bits more carefully after you accept that some holes must be shared.

**Citations**

1. T. M. Graf and D. Lemire, “Binary Fuse Filters: Fast and Smaller Than Xor Filters,” *J. Exp. Algorithmics* 27 (2022). [DOI](https://doi.org/10.1145/3510449)

**Questions.** (1) If you demand $$\varepsilon = 0$$ and $$n > m$$ fingerprints, which theorem of this chapter applies? (2) Why is “13% above the lower bound” a pigeonhole statement rather than a machine-learning statement?

## Tiếng Việt

Nguyên lý Dirichlet giải thích vì sao không thể xây dựng một cấu trúc kiểm tra phần tử thuộc tập (membership) vừa **chính xác tuyệt đối** vừa siêu gọn: khi số khóa (bồ câu) lớn hơn số mẫu bit khả dĩ (chuồng), va chạm chắc chắn xảy ra. Các cấu trúc kiểm tra xấp xỉ chấp nhận một tỷ lệ dương tính giả $$\varepsilon$$, rồi đặt câu hỏi bộ nhớ cần dùng tiến gần đến cận dưới lý thuyết thông tin $$\approx n \log_2(1/\varepsilon)$$ bit (cho $$n$$ khóa) đến mức nào.

Trong công trình trên tạp chí *J. Exp. Algorithmics* (2022), Graf và Lemire báo cáo bộ lọc **binary fuse filter** chỉ lớn hơn cận dưới lý thuyết khoảng **13%** (hoặc khoảng **8%** nếu dùng bố cục chậm hơn), vượt qua xor filter về dung lượng bộ nhớ và thường nhanh hơn về thời gian xây dựng, đồng thời so sánh trực tiếp với các bộ lọc Bloom, cuckoo và ribbon.

Điểm đáng rút ra cho Chương 8 là cuộc đua tối ưu các cấu trúc dữ liệu bộ lọc thực chất là một bài toán chuồng bồ câu định lượng. Hiện tượng va chạm trong bảng băm (đã học ở phần bắt buộc) có cùng bản chất, chỉ khác cách tổ chức bộ nhớ. Binary fuse filter không phá vỡ nguyên lý Dirichlet; thay vào đó, khi đã chấp nhận một số ngăn chứa phải dùng chung, chúng sử dụng từng bit bộ nhớ một cách tiết kiệm hơn.

**Câu hỏi.** (1) Nếu yêu cầu $$\varepsilon = 0$$ với $$n > m$$ dấu vân tay (fingerprint), định lý nào của chương này được áp dụng? (2) Vì sao phát biểu “cao hơn cận dưới 13%” mang bản chất của nguyên lý chuồng bồ câu chứ không phải học máy?

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=V3pzxngeLqw">Bloom Filters | Algorithms You Should Know #2 | Real-world Examples</a> — ByteByteGo, tiếng Anh. Giới thiệu trực quan bộ lọc Bloom và lý do bộ nhớ bị chặn dưới bởi số phần tử cần phân biệt.
- <a href="https://www.youtube.com/watch?v=eV1haPUt0NU">Hyperloglog: Facebook&#x27;s algorithm to count distinct elements</a> — Gaurav Sen, tiếng Anh. Giới thiệu HyperLogLog để đếm lực lượng gần đúng, thuộc cùng họ cấu trúc tóm tắt (sketch) với fuse filter.
- <a href="https://www.youtube.com/watch?v=B_PexYrEcEw">HyperLogLog Hit Counter - Computerphile</a> — Computerphile, tiếng Anh. Minh họa ngắn gọn về HyperLogLog, làm rõ vì sao không cần lưu riêng từng khóa.
