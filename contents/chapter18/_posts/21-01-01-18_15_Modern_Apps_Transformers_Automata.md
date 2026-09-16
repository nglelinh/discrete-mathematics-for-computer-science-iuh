---
layout: post
title: "Optional note: Transformers versus automata (2022–2026)"
categories: chapter18
date: 2021-01-01
order: 15
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. Strobl et al. (TACL 2024) survey which formal languages transformer variants can recognize — a 2022–2024 map onto DFA/NFA/TM. Does not replace automata theory."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite DFA/NFA, pumping, Myhill–Nerode, or Turing machines.

Bài ghi chú ứng dụng song ngữ. **Không** viết lại DFA/NFA, pumping, Myhill–Nerode hay máy Turing.

</div>

## English

This chapter classifies machines by what languages they recognize. From 2021 onward a parallel literature asks the same question of **transformers**. Strobl, Merrill, Weiss, Chiang, and Angluin, “What Formal Languages Can Transformers Express? A Survey,” *Transactions of the ACL* 12:543–561 (2024), [DOI 10.1162/tacl_a_00663](https://doi.org/10.1162/tacl_a_00663), [ACL Anthology](https://aclanthology.org/2024.tacl-1.30/), unify results that otherwise look contradictory because papers assume different masks, precision, and encoder/decoder APIs.

A useful slogan from that survey (read the paper for caveats): with chain-of-thought / intermediate symbols, decoder-style models can simulate more powerful machines; encoder-only models with restricted attention often sit inside small circuit classes (e.g. $$\mathsf{AC}^0$$ / $$\mathsf{TC}^0$$ discussions in the survey). The optional lesson for NCS students: **regular / CFL / decidable** remain the right yardsticks. A transformer is not “beyond the Chomsky hierarchy” until you fix the computational model the survey insists on fixing.

Read Sipser-style proofs first. Then use the 2024 survey as a reading list, not as a replacement chapter.

**Citations**

1. L. Strobl et al., “What Formal Languages Can Transformers Express? A Survey,” *TACL* 12 (2024). [DOI](https://doi.org/10.1162/tacl_a_00663)

**Questions.** (1) Which Chapter 18 machine do you get if you allow a transformer unbounded scratch tokens (informally: a tape)? (2) Why must “softmax vs hard attention” be stated before quoting an expressivity theorem?

## Tiếng Việt

Chương này phân loại máy theo ngôn ngữ chúng nhận. Từ khoảng 2021, một dòng bài song song hỏi cùng câu cho **transformer**. Strobl, Merrill, Weiss, Chiang và Angluin (*TACL* 2024) thống nhất các kết quả trông mâu thuẫn vì mỗi bài giả định mask, độ chính xác và API encoder/decoder khác nhau.

Slogan hữu ích (đọc bài để thấy caveat): khi có chain-of-thought / ký hiệu trung gian, mô hình kiểu decoder mô phỏng máy mạnh hơn; encoder-only với attention hạn chế thường nằm trong lớp mạch nhỏ ($$\mathsf{AC}^0$$ / $$\mathsf{TC}^0$$ trong survey). Bài học tùy chọn: **regular / CFL / decidable** vẫn là thước đúng. Transformer không “vượt Chomsky” cho đến khi bạn chốt mô hình tính toán — đúng điều survey buộc phải chốt.

Đọc chứng minh kiểu Sipser trước. Rồi dùng survey 2024 như danh mục đọc, không phải chương thay thế.

**Câu hỏi.** (1) Máy Chương 18 nào bạn nhận nếu cho transformer scratch token không chặn (tạm hiểu: một băng)? (2) Vì sao phải nêu “softmax hay hard attention” trước khi trích định lý expressivity?
