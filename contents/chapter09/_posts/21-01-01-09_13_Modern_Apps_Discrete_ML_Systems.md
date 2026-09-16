---
layout: post
title: "Optional note: Discrete math in 2022–2026 production systems"
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

Bài ghi chú ứng dụng song ngữ. **Không** viết lại các case study nhị phân, kiểm thử hay login.

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

Chương 9 đã nối toán rời rạc với production. Ghi chú này chỉ thêm **ba hiện vật có năm** 2022–2024.

| Năm | Hiện vật | Đối tượng rời rạc | Vì sao nằm đây |
|:---:|:---|:---|:---|
| 2022 | Binary fuse filter (Graf & Lemire) | Tập xấp xỉ | Cùng ngân sách va chạm như birthday/hash |
| 2023 | GraphCast (Lam et al., *Science*) | Đồ thị lưới + GNN | Đồ thị và message passing quy mô thời tiết |
| 2024 | Kissat tại SAT Competition | CNF / CDCL | Logic và combinatorial explosion, có huy chương |

Đọc như **mục lục đáp**, không phải chương lý thuyết mới. Mỗi dòng trỏ về chương bạn đã có (4–8, 12–13, 1).

**Câu hỏi.** (1) Case study nào ở Chương 9 dùng cùng mô hình đếm $$2^n$$ với SAT? (2) Vì sao lưới GraphCast là *đồ thị* theo nghĩa Chương 12 chứ không phải bộ giải PDE liên tục?
