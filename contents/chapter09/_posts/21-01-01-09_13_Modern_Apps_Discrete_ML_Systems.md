---
layout: post
title: "Ghi chú mở rộng: Toán rời rạc trong các hệ thống thực tế 2022–2026"
categories: chapter09
date: 2021-01-01
order: 13
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. A short 2022–2026 pointer pack: Kissat, binary fuse filters, GraphCast — tying this applications chapter to recent deployed discrete structure. Does not replace existing case studies."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite the binary-data, testing, or login case studies.

Ghi chú ứng dụng song ngữ (tiếng Anh trước, tiếng Việt sau). Nội dung này chỉ bổ sung tài liệu tham chiếu gần đây, **không** thay thế các bài học về dữ liệu nhị phân, kiểm thử hay đăng nhập ở trên.

</div>

## English

Chapter 9 already connects discrete math to production (endianness, pools, pairwise tests, collisions). This optional note only adds **three dated artifacts** from 2022–2024 that a systems student can open next.

| Year | Artifact | Discrete object | Why it belongs here |
|:---:|:---|:---|:---|
| 2022 | Binary fuse filters (Graf & Lemire, JEA) | Approximate set | Same collision budget as birthday / hash notes |
| 2023 | GraphCast (Lam et al., *Science*) | Mesh graph + GNN | Graphs and message passing at weather scale |
| 2024 | Kissat at SAT Competition | CNF / CDCL | Logic and combinatorial explosion, now with medals |

- Graf & Lemire, [DOI 10.1145/3510449](https://doi.org/10.1145/3510449) — filters within ~13% of the storage lower bound.
- Lam et al., “Learning skillful medium-range global weather forecasting,” *Science* (2023), [DOI 10.1126/science.adi2336](https://doi.org/10.1126/science.adi2336) — 10-day global forecast, $$0.25^\circ$$, under one minute, better than the operational deterministic baseline on 90% of 1380 targets.
- SAT Competition 2024 medals: [Freiburg page](https://cca.informatik.uni-freiburg.de/sat24medals/).

Read this as a **landing index**, not a new theory chapter. Each row points at a chapter you already have (4–8, 12–13, 1).

**Questions.** (1) Which Chapter 9 case study shares its counting model with SAT’s $$2^n$$? (2) Why is GraphCast’s mesh a *graph* in the sense of Chapter 12, not a continuous PDE solver?

## Tiếng Việt

Chương 9 đã kết nối toán rời rạc với các hệ thống vận hành thực tế (endianness, connection pool, kiểm thử pairwise, va chạm băm). Ghi chú ngắn này bổ sung **ba công trình tiêu biểu** giai đoạn 2022–2024 để người học có thể tham khảo mở rộng:

| Năm | Công trình / Hệ thống | Đối tượng toán rời rạc | Lý do liên hệ với Chương 9 |
|:---:|:---|:---|:---|
| 2022 | Binary fuse filter (Graf & Lemire, JEA) | Tập hợp xấp xỉ | Cùng bài toán ngân sách va chạm như nghịch lý sinh nhật và bảng băm |
| 2023 | GraphCast (Lam et al., *Science*) | Đồ thị lưới + GNN | Đồ thị và truyền thông điệp (message passing) ở quy mô dự báo thời tiết toàn cầu |
| 2024 | Kissat tại SAT Competition | CNF / CDCL | Logic mệnh đề và bài toán bùng nổ tổ hợp trong các bộ giải SAT hiện đại |

Hãy xem bảng trên như một **chỉ mục tham khảo mở rộng**, không phải chương lý thuyết mới — mỗi dòng đều nối trực tiếp về các chương đã học trong giáo trình (Chương 1, 4–8, 12–13).

**Câu hỏi gợi mở.** (1) Tình huống nào trong Chương 9 chia sẻ cùng mô hình đếm tăng trưởng mũ $$2^n$$ với bài toán SAT? (2) Vì sao lưới dự báo của GraphCast được mô hình hóa như một *đồ thị* theo nghĩa của Chương 12 thay vì một bộ giải phương trình đạo hàm riêng (PDE) liên tục?

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=0Ud4u7c0_EE">AI Weather Forecasting: What GraphCast Actually Proved (and Didn&#x27;t)</a> — Synaptorix, tiếng Anh. Phân tích những gì GraphCast chứng minh được khi dự báo thời tiết trên đồ thị lưới.
- <a href="https://www.youtube.com/watch?v=V3pzxngeLqw">Bloom Filters | Algorithms You Should Know #2 | Real-world Examples</a> — ByteByteGo, tiếng Anh. Trình bày bộ lọc tập xấp xỉ, cùng họ cấu trúc dữ liệu với binary fuse filter.
- <a href="https://www.youtube.com/watch?v=YUqR-8rZ_gQ">Lecture 10-3 CDCL (Lecture 5 in CS433)</a> — Automated Reasoning, tiếng Anh. Giới thiệu thuật toán CDCL trên dạng chuẩn hội (CNF), cùng họ bộ giải với Kissat tại SAT Competition.
