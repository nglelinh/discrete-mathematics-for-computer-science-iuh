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

### Background Knowledge Map: Interactive Theorem Provers (Lean 4) and AI-Assisted Formal Proofs

Every proof technique in Chapter 3—direct proof, contradiction, and mathematical induction—is no longer confined to chalkboards. In **Interactive Theorem Provers (ITPs)** like **Lean 4**, Coq, and Isabelle, mathematical proofs are compiled programs checked down to every single logical axiom by a tiny trusted kernel:

1. **Curry–Howard Correspondence ("Propositions as Types, Proofs as Programs")**:
   A theorem statement is a *type*, and a valid proof is a *program* that type-checks to that type. An implication $A \to B$ is literally a function taking a proof of $A$ and returning a proof of $B$.
2. **Small Trusted Kernel (De Bruijn Criterion)**:
   Even if an AI model generates a 500-line proof using complex heuristics, Lean's tiny kernel verifies every step from first principles. AI cannot "hallucinate" a fake proof past the kernel—it either compiles (`0` errors) or is rejected!
3. **Industrial & Mathematical Breakthroughs**:
   From proving the seL4 microkernel free of buffer overflows and null dereferences, to verifying AWS cryptographic routines, to DeepMind's AlphaProof solving International Mathematical Olympiad (IMO) problems in Lean, formal verification is becoming a mainstream engineering superpower.

### Deep-Dive Explanation: Tracing a Machine-Checked Induction Proof of $\sum_{i=0}^{n} i = \frac{n(n+1)}{2}$ in Lean-Style Logic (Read Slowly)

How does a proof assistant check induction without letting a human wave their hands? Watch the exact type obligations generated for `2 * sum(n) = n * (n + 1)`:

| Proof Obligation | Mathematical Goal | Machine Verification Step |
| :--- | :--- | :--- |
| **Base case (`n = 0`)** | $2 \cdot \text{sum}(0) = 0 \cdot (0 + 1)$ | Kernel reduces both sides by definition: `0 = 0` (`rfl` — reflexivity passes!) |
| **Inductive hypothesis (`ih`)** | Assume $2 \cdot \text{sum}(k) = k(k+1)$ | Given as an explicit local variable `ih` in the typing context |
| **Inductive step (`n = k + 1`)** | Prove $2 \cdot \text{sum}(k+1) = (k+1)(k+2)$ | Expand `sum(k+1) = sum(k) + (k+1)` → `2*sum(k) + 2*(k+1)` → rewrite via `ih` → `k*(k+1) + 2*(k+1)` → factor to `(k+1)*(k+2)` (`ring` tactic closes goal!) |

Notice the magic: if you accidentally forget the base case or assume what you are trying to prove, the compiler refuses to build—turning mathematical rigor into an automated feedback loop.

## Tiếng Việt

Các bài học bắt buộc xem một chứng minh là chuỗi hữu hạn các bước suy luận hợp lệ. Hai hệ thống công bố trong giai đoạn 2024–2025 đã đưa định nghĩa đó vào vận hành ở quy mô bài toán Olympic.

**AlphaGeometry** (*Nature*, 17/01/2024) là hệ thống chứng minh hình học lai thần kinh–ký hiệu (neuro-symbolic): mô hình ngôn ngữ đề xuất các nét dựng hình phụ, còn bộ suy diễn ký hiệu hoàn tất chuỗi lập luận. Trên tập bài IMO-AG-30, hệ thống giải được 25/30 bài; các lời giải công bố là chuỗi suy diễn mà con người có thể đọc hiểu (dùng phản chứng, chia trường hợp và biến đổi góc), chứ không phải điểm số đầu ra của mô hình hộp đen.

**AlphaProof** tìm kiếm chứng minh trong ngôn ngữ kiểm chứng **Lean**. Ngày 25/07/2024, DeepMind công bố AlphaProof kết hợp AlphaGeometry 2 đạt 28/42 điểm trên đề thi IMO 2024 (tương đương mức huy chương bạc), giải được bốn trên sáu bài sau khi các chuyên gia hình thức hóa đề bài. Bài báo đăng trên *Nature* năm 2025 mô tả tác nhân kiểu AlphaZero được huấn luyện trên hàng triệu bài toán hình thức hóa tự động, trong đó nhân (kernel) của Lean kiểm tra tính hợp lệ của từng bước chứng minh.

Nguyên lý toán rời rạc cốt lõi không thay đổi: một "chứng minh" chưa vượt qua kiểm tra của nhân kiểm chứng vẫn chỉ là phác thảo. Tìm kiếm bằng AI đề xuất các lời giải ứng viên, còn các phương pháp chứng minh của chương này quyết định liệu ứng viên đó có thực sự là một chứng minh hợp lệ hay không.

**Câu hỏi.** (1) Chiến thuật (tactic) `by contradiction` trong Lean mã hóa phương pháp chứng minh nào? (2) Vì sao bước hình thức hóa đề thi IMO (do con người hay tự động thực hiện) nằm *ngoài* phạm vi bảo đảm của nhân kiểm chứng?

### Bản đồ kiến thức nền: Trợ lý chứng minh hình thức (Lean 4) & Kỷ nguyên AI chứng minh định lý

Mọi kỹ thuật chứng minh ở Chương 3 (trực tiếp, phản chứng, quy nạp) nay đã bước ra khỏi bảng phấn để trở thành mã nguồn được máy tính kiểm chứng tuyệt đối trong các hệ thống như **Lean 4**, Coq và Isabelle:

1. **Tương ứng Curry–Howard ("Mệnh đề là Kiểu dữ liệu, Chứng minh là Chương trình")**:
   Một định lý được viết như một kiểu (*type*), và một chứng minh hợp lệ là một chương trình biên dịch khớp đúng kiểu đó. Phép kéo theo $A \to B$ chính là một hàm nhận bằng chứng của $A$ và trả về bằng chứng của $B$.
2. **Nhân kiểm chứng siêu nhỏ (Trusted Kernel — Tiêu chuẩn De Bruijn)**:
   Dù AI có đề xuất lời giải phức tạp thế nào, nhân kiểm chứng nhỏ gọn của Lean vẫn soát lại từng bước logic cơ bản. AI **không thể "ảo giác"** qua mặt trình biên dịch: hoặc chứng minh biên dịch sạch 100%, hoặc bị từ chối ngay!
3. **Đột phá công nghiệp & toán học**:
   Từ vi nhân hệ điều hành **seL4** được chứng minh không lỗi bộ nhớ, thư viện mật mã của AWS, đến **AlphaProof** giải toán Olympic IMO bằng Lean 4, chứng minh hình thức đang mở ra chuẩn mực độ tin cậy cao nhất cho phần mềm và toán học.

### Khung giải thích (nên đọc chậm): Máy tính kiểm tra bài chứng minh quy nạp $2\sum_{i=0}^{n} i = n(n+1)$ từng bước như thế nào?

Khi bạn viết chứng minh quy nạp trong Lean 4, bộ kiểm tra kiểu tự động sinh ra đúng 2 mục tiêu bắt buộc (không thể bỏ sót):
- **Mục tiêu 1 (Cơ sở $n = 0$)**: Cần chứng minh $2 \cdot \text{sum}(0) = 0 \cdot 1$. Nhân tự rút gọn hai vế về `0 = 0` → khớp bằng tính phản xạ (`rfl`).
- **Mục tiêu 2 (Bước quy nạp $n = k + 1$ với giả thiết `ih`: $2 \cdot \text{sum}(k) = k(k+1)$)**:
  1. Khai triển định nghĩa đệ quy: $2 \cdot (\text{sum}(k) + (k + 1)) = 2 \cdot \text{sum}(k) + 2(k + 1)$.
  2. Thay thế đúng bằng biến giả thiết `ih`: $k(k+1) + 2(k+1)$.
  3. Gom nhân tử đại số: $(k+1)(k+2)$ → khớp 100% vế phải!

Nếu bạn quên kiểm tra $n = 0$ hay lỡ dùng biến chưa chứng minh, trình biên dịch lập tức báo lỗi đỏ—biến sự chặt chẽ toán học thành một bộ kiểm tra tự động không thể sai sót.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=4NlrfOl0l8U">The AI that solved IMO Geometry Problems | Guest video by @Aleph0</a> — 3Blue1Brown, tiếng Anh. Giới thiệu AlphaGeometry với suy diễn hình học có kiểm chứng, tương ứng hệ thống được nhắc trong bài.
- <a href="https://www.youtube.com/watch?v=prYaTrZUces">Automated Mathematical Proofs - Computerphile</a> — Computerphile, tiếng Anh. Trình bày việc kiểm tra chứng minh bằng máy tính, gắn với quan điểm chứng minh là dãy bước hợp lệ.
- <a href="https://www.youtube.com/watch?v=POHVMMG7pqE">10 minute Lean tutorial : proving logical propositions</a> — Xena Project, tiếng Anh. Minh họa cách Lean kiểm tra từng bước logic trong công cụ hỗ trợ chứng minh (proof assistant).
