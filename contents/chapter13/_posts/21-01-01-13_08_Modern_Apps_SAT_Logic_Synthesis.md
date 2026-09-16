---
layout: post
title: "Optional note: SAT engines behind Boolean design (2022–2026)"
categories: chapter13
date: 2021-01-01
order: 8
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. Kissat/CaDiCaL (SAT 2024, CAV 2024 lineage) are the solvers that modern EDA and Boolean equivalence checking actually call. Does not replace Boolean algebra."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite K-maps, Quine–McCluskey, or the chip-history lesson.

Bài ghi chú ứng dụng song ngữ. **Không** viết lại bản đồ Karnaugh, Quine–McCluskey, hay bài từ Boole đến chip.

</div>

## English

Karnaugh maps stop at a handful of variables. Industrial logic synthesis and **combinational equivalence checking** encode “are these two Boolean functions equal?” as SAT/UNSAT on a miter circuit — the same algebra as this chapter, a different search engine.

In 2024 that engine, on the public competition track, was Kissat 4.0: three main-track golds at SAT Competition 2024 ([medals](https://cca.informatik.uni-freiburg.de/sat24medals/); Biere, Faller, Fazekas, Fleury, Froleyks, Pollitt, Univ. Helsinki B-2024-1, pp. 8–10). The same group’s CaDiCaL 2.0 line (highlighted in that description; CAV 2024 system paper) emphasises incremental SAT, proof production, and interpolation — the features EDA tools need when they call a solver millions of times.

Optional reading order: Boolean algebra and gates first; this note second. You should be able to say, without new theory, why XOR-of-two-outputs $$= 0$$ is a SAT instance and why an UNSAT **proof** is what a chip team wants.

**Citations**

1. A. Biere et al., “CaDiCaL, Gimsatul, IsaSAT and Kissat Entering the SAT Competition 2024,” SAT Competition 2024, Univ. Helsinki B-2024-1, pp. 8–10. [PDF](https://cca.informatik.uni-freiburg.de/papers/BiereFallerFazekasFleuryFroleyksPollitt-SAT-Competition-2024-solvers.pdf)

**Questions.** (1) Write the miter SAT query for “$$f \equiv g$$” using XOR and a single output. (2) Why is a checked UNSAT proof closer to Chapter 13 than a neural “probably equivalent”?

## Tiếng Việt

Bản đồ Karnaugh dừng ở vài biến. Tổng hợp logic công nghiệp và **kiểm tương đương tổ hợp** mã hóa “hai hàm Boole có bằng nhau?” thành SAT/UNSAT trên mạch miter — cùng đại số chương này, khác engine tìm kiếm.

Năm 2024, trên track công khai, engine đó là Kissat 4.0: ba vàng track chính SAT Competition 2024. Dòng CaDiCaL 2.0 (nhóm cùng tác giả; mô tả trong báo cáo cuộc thi, CAV 2024) nhấn SAT incremental, xuất chứng minh và interpolation — đúng thứ công cụ EDA cần khi gọi bộ giải hàng triệu lần.

Thứ tự đọc: đại số Boole và cổng trước; ghi chú này sau. Bạn cần nói được, không cần lý thuyết mới, vì sao XOR hai ngõ ra $$= 0$$ là instance SAT và vì sao chứng minh UNSAT được kiểm mới là thứ team chip muốn.

**Câu hỏi.** (1) Viết truy vấn SAT miter cho “$$f \equiv g$$” bằng XOR và một ngõ ra. (2) Vì sao chứng minh UNSAT đã kiểm gần Chương 13 hơn câu “neural nói có lẽ tương đương”?
