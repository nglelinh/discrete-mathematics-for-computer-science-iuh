---
layout: post
title: "Optional note: Machine-checked proofs and AI (2022–2026)"
categories: chapter03
date: 2021-01-01
order: 5
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. AlphaGeometry (Nature 2024) and AlphaProof (IMO 2024 / Nature 2025) use formal deduction — the same proof methods — inside Lean or a geometry engine. Does not replace the proof-method lessons."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite direct proof, contradiction, or induction.

Bài ghi chú ứng dụng song ngữ. **Không** viết lại chứng minh trực tiếp, phản chứng hay quy nạp.

</div>

## English

The required lessons treat a proof as a finite chain of licensed steps. Two 2024–2025 systems make that definition operational at olympiad scale.

**AlphaGeometry** (Trinh, Wu, Le, He, Luong, *Nature*, 17 January 2024, [DOI 10.1038/s41586-023-06747-5](https://doi.org/10.1038/s41586-023-06747-5)) is a neuro-symbolic geometry prover: a language model proposes auxiliary constructions; a symbolic engine closes the deduction. On IMO-AG-30 it solved 25 of 30 problems. The published proofs are human-readable deduction chains — contradiction, case splits, and angle-chasing — not a black-box score.

**AlphaProof** searches for proofs in **Lean**. DeepMind reported (25 July 2024) that AlphaProof plus AlphaGeometry 2 scored 28/42 on the 2024 IMO problems (silver-medal range), solving four of six after experts formalized the statements. The journal paper is “Olympiad-level formal mathematical reasoning with reinforcement learning,” *Nature* (2025), [DOI 10.1038/s41586-025-09833-y](https://doi.org/10.1038/s41586-025-09833-y): an AlphaZero-style agent trains on millions of auto-formalized problems; Lean’s kernel checks every step.

The discrete-math point is unchanged: a “proof” that a kernel cannot check is still only a sketch. AI search proposes candidates; the methods of this chapter decide whether a candidate is a proof.

**Citations**

1. T. H. Trinh et al., “Solving olympiad geometry without human demonstrations,” *Nature* (2024). [DOI](https://doi.org/10.1038/s41586-023-06747-5)
2. DeepMind, “AI achieves silver-medal standard solving International Mathematical Olympiad problems,” 25 July 2024. [Blog](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/)
3. AlphaProof team, “Olympiad-level formal mathematical reasoning with reinforcement learning,” *Nature* (2025). [DOI](https://doi.org/10.1038/s41586-025-09833-y)

**Questions.** (1) Which proof method is a Lean tactic `by contradiction` encoding? (2) Why does formalizing the IMO statement (human or auto) sit *outside* the kernel’s guarantee?

## Tiếng Việt

Các mục bắt buộc coi chứng minh là chuỗi hữu hạn bước được phép. Hai hệ thống 2024–2025 biến định nghĩa đó thành quy trình ở quy mô olympic.

**AlphaGeometry** (*Nature*, 17/01/2024) là bộ chứng minh hình học neuro-symbolic: mô hình ngôn ngữ đề xuất dựng hình phụ; engine ký hiệu khép mạch suy diễn. Trên bộ IMO-AG-30 nó giải 25/30 bài; chứng minh xuất bản là chuỗi suy diễn đọc được, không phải điểm số hộp đen.

**AlphaProof** tìm chứng minh trong **Lean**. DeepMind (25/07/2024) báo cáo AlphaProof kết hợp AlphaGeometry 2 đạt 28/42 trên đề IMO 2024 (ngưỡng bạc), giải bốn trên sáu bài sau khi chuyên gia formalize đề. Bài *Nature* 2025 mô tả agent kiểu AlphaZero huấn luyện trên hàng triệu bài auto-formalize; kernel Lean kiểm từng bước.

Điểm toán rời rạc không đổi: “chứng minh” mà kernel không kiểm được vẫn chỉ là phác thảo. AI đề xuất ứng viên; các phương pháp của chương này quyết định ứng viên có phải chứng minh hay không.

**Câu hỏi.** (1) Tactic `by contradiction` trong Lean mã hóa phương pháp nào? (2) Vì sao bước formalize đề IMO nằm *ngoài* bảo đảm của kernel?
