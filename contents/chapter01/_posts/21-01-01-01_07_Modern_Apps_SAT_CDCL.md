---
layout: post
title: "Optional note: Modern SAT engines (2022–2026)"
categories: chapter01
date: 2021-01-01
order: 7
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. Recent SAT competition engines (Kissat, CaDiCaL) show how CNF, resolution, and CDCL from this chapter scale to industrial instances in 2022–2026. Does not replace the SAT introduction."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite the propositional-logic theory or the existing SAT introduction. Read those first.

Bài ghi chú ứng dụng song ngữ (tiếng Anh, rồi tiếng Việt). **Không** viết lại lý thuyết logic mệnh đề hay bài giới thiệu SAT. Hãy đọc các mục bắt buộc trước.

</div>

## English

Chapter 1 already treats CNF, resolution, and SAT as a decision problem. What changed after 2022 is not the definition of satisfiability — it is the engineering of **CDCL** solvers that still implement those same discrete objects at industrial scale.

The SAT Competition 2024 main track (SAT'24, Pune) was dominated by Kissat 4.0: first place in SAT, UNSAT, and SAT+UNSAT ([University of Freiburg notice](https://news.vm.uni-freiburg.de/en/newsarchive/kissat-triumphs-in-the-sat-2024-competition); [medal page](https://cca.informatik.uni-freiburg.de/sat24medals/)). The accompanying solver description is Biere, Faller, Fazekas, Fleury, Froleyks, and Pollitt, “CaDiCaL, Gimsatul, IsaSAT and Kissat Entering the SAT Competition 2024,” in *SAT Competition 2024: Solver, Benchmark and Proof Checker Descriptions*, University of Helsinki CS Report B-2024-1, pp. 8–10.

Kissat and CaDiCaL remain **exact** solvers: they search the $$2^n$$ assignment space of a CNF, learn clauses from conflicts (resolution), and emit machine-checkable proofs (DRAT/LRAT). The lesson for this course is concrete: the truth table of Section 1.3 is unusable at $$n \approx 10^6$$ variables, but the *same* Boolean algebra plus CDCL heuristics solves instances that encode verification, scheduling, and cryptanalysis.

If you already read the optional SAT introduction, treat this note as an update: the 2024 medals are evidence that propositional logic is still a production technology, not only a homework calculus.

**Citations**

1. A. Biere et al., “CaDiCaL, Gimsatul, IsaSAT and Kissat Entering the SAT Competition 2024,” SAT Competition 2024 proceedings, Univ. Helsinki Report B-2024-1, pp. 8–10. [PDF](https://cca.informatik.uni-freiburg.de/papers/BiereFallerFazekasFleuryFroleyksPollitt-SAT-Competition-2024-solvers.pdf)
2. SAT Competition 2024 medals, University of Freiburg. <https://cca.informatik.uni-freiburg.de/sat24medals/>

**Questions.** (1) Why is a learned conflict clause a resolution consequence of the input CNF? (2) Why does a DRAT proof matter more than a solver merely printing `UNSAT`?

## Tiếng Việt

Chương 1 đã xây CNF, phép giải (resolution) và SAT như bài toán quyết định. Điểm mới sau 2022 không phải định nghĩa tính thỏa được — mà là các bộ giải **CDCL** triển khai đúng các đối tượng rời rạc đó trên quy mô công nghiệp.

Tại SAT Competition 2024 (SAT'24, Pune), Kissat 4.0 thắng cả ba hạng mục chính: SAT, UNSAT và SAT+UNSAT. Mô tả kỹ thuật nằm trong Biere và cộng sự, *SAT Competition 2024*, University of Helsinki Report B-2024-1, tr. 8–10. Kissat/CaDiCaL vẫn là bộ giải **chính xác**: chúng duyệt không gian $$2^n$$ phép gán của một CNF, học mệnh đề từ xung đột (resolution), và xuất chứng minh kiểm được (DRAT/LRAT).

Bảng chân trị ở Mục 1.3 không dùng được khi $$n$$ cỡ triệu biến, nhưng cùng đại số Boole cộng heuristic CDCL vẫn giải được các instance mã hóa kiểm chứng, lập lịch và phân tích mật mã. Nếu đã đọc bài giới thiệu SAT, hãy xem ghi chú này như bản cập nhật 2024: logic mệnh đề vẫn là công nghệ production.

**Câu hỏi.** (1) Vì sao mệnh đề học từ xung đột là hệ quả resolution của CNF đầu vào? (2) Vì sao chứng minh DRAT quan trọng hơn việc bộ giải chỉ in `UNSAT`?
