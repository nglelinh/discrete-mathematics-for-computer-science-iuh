---
layout: post
title: "Ghi chú mở rộng: Chứng minh được máy kiểm chứng và AI (2022–2026)"
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

Bài ghi chú ứng dụng song ngữ. Nội dung này **không** thay thế hay viết lại các bài về chứng minh trực tiếp, phản chứng và quy nạp.

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

Các bài học bắt buộc xem một chứng minh là chuỗi hữu hạn các bước suy luận hợp lệ. Hai hệ thống công bố trong giai đoạn 2024–2025 đã đưa định nghĩa đó vào vận hành ở quy mô bài toán Olympic.

**AlphaGeometry** (*Nature*, 17/01/2024) là hệ thống chứng minh hình học lai thần kinh–ký hiệu (neuro-symbolic): mô hình ngôn ngữ đề xuất các nét dựng hình phụ, còn bộ suy diễn ký hiệu hoàn tất chuỗi lập luận. Trên tập bài IMO-AG-30, hệ thống giải được 25/30 bài; các lời giải công bố là chuỗi suy diễn mà con người có thể đọc hiểu (dùng phản chứng, chia trường hợp và biến đổi góc), chứ không phải điểm số đầu ra của mô hình hộp đen.

**AlphaProof** tìm kiếm chứng minh trong ngôn ngữ kiểm chứng **Lean**. Ngày 25/07/2024, DeepMind công bố AlphaProof kết hợp AlphaGeometry 2 đạt 28/42 điểm trên đề thi IMO 2024 (tương đương mức huy chương bạc), giải được bốn trên sáu bài sau khi các chuyên gia hình thức hóa đề bài. Bài báo đăng trên *Nature* năm 2025 mô tả tác nhân kiểu AlphaZero được huấn luyện trên hàng triệu bài toán hình thức hóa tự động, trong đó nhân (kernel) của Lean kiểm tra tính hợp lệ của từng bước chứng minh.

Nguyên lý toán rời rạc cốt lõi không thay đổi: một "chứng minh" chưa vượt qua kiểm tra của nhân kiểm chứng vẫn chỉ là phác thảo. Tìm kiếm bằng AI đề xuất các lời giải ứng viên, còn các phương pháp chứng minh của chương này quyết định liệu ứng viên đó có thực sự là một chứng minh hợp lệ hay không.

**Câu hỏi.** (1) Chiến thuật (tactic) `by contradiction` trong Lean mã hóa phương pháp chứng minh nào? (2) Vì sao bước hình thức hóa đề thi IMO (do con người hay tự động thực hiện) nằm *ngoài* phạm vi bảo đảm của nhân kiểm chứng?

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=4NlrfOl0l8U">The AI that solved IMO Geometry Problems | Guest video by @Aleph0</a> — 3Blue1Brown, tiếng Anh. Giới thiệu AlphaGeometry với suy diễn hình học có kiểm chứng, tương ứng hệ thống được nhắc trong bài.
- <a href="https://www.youtube.com/watch?v=prYaTrZUces">Automated Mathematical Proofs - Computerphile</a> — Computerphile, tiếng Anh. Trình bày việc kiểm tra chứng minh bằng máy tính, gắn với quan điểm chứng minh là dãy bước hợp lệ.
- <a href="https://www.youtube.com/watch?v=POHVMMG7pqE">10 minute Lean tutorial : proving logical propositions</a> — Xena Project, tiếng Anh. Minh họa cách Lean kiểm tra từng bước logic trong công cụ hỗ trợ chứng minh (proof assistant).
