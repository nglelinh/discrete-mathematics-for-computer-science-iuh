---
layout: post
title: "Optional note: Transformers and the Chomsky map (2024)"
categories: chapter19
date: 2021-01-01
order: 13
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. The TACL 2024 survey places transformers on the same formal-language map as CFG/PDA. Does not replace grammars, pumping, or CYK."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite CFG, PDA, pumping for CFL, or CYK.

Bài ghi chú ứng dụng song ngữ. **Không** viết lại CFG, PDA, pumping CFL hay CYK.

</div>

## English

Chapter 19 is the Chomsky hierarchy with proofs: CFG $$=$$ PDA, pumping, CNF, CYK. The 2024 survey of Strobl et al., “What Formal Languages Can Transformers Express?,” *TACL* 12:543–561, [DOI 10.1162/tacl_a_00663](https://doi.org/10.1162/tacl_a_00663), is the matching **optional** paper for this chapter rather than a second automata rewrite.

They treat inputs as unbounded strings over a finite alphabet — the same objects as $$L \subseteq \Sigma^*$$. Results then depend on:

- encoder vs decoder (whether intermediate symbols are written);
- attention (softmax, average-hard, leftmost/rightmost-hard);
- arithmetic precision.

That is why one paper can say “transformers recognize all regular languages” and another can deny it: they did not fix the same machine. For a compiler-track student, the practical moral is unchanged: **CFGs and CYK still parse programming languages**; transformers are a different recognizer whose formal power you must cite with the survey’s hypotheses attached.

Use this after 19.10–19.12. It is a reading pointer, not a new pumping lemma.

**Citations**

1. L. Strobl, W. Merrill, G. Weiss, D. Chiang, D. Angluin, “What Formal Languages Can Transformers Express? A Survey,” *TACL* 12 (2024), pp. 543–561. [Anthology](https://aclanthology.org/2024.tacl-1.30/)

**Questions.** (1) Name one CFL this chapter’s pumping lemma excludes; would a transformer-with-scratchpad necessarily recognize it? (2) Why is CYK’s $$O(n^3)$$ bound easier to state than a transformer’s “expressivity” bound?

## Tiếng Việt

Chương 19 là Chomsky hierarchy kèm chứng minh: CFG $$=$$ PDA, pumping, CNF, CYK. Survey 2024 của Strobl et al. (*TACL*) là paper **tùy chọn** khớp chương này, không phải bản viết lại automata thứ hai.

Họ coi input là chuỗi không chặn trên bảng chữ hữu hạn — cùng đối tượng $$L \subseteq \Sigma^*$$. Kết quả phụ thuộc encoder/decoder, kiểu attention, và độ chính xác số học. Đó là lý do một bài nói “transformer nhận mọi ngôn ngữ chính quy” còn bài khác phủ nhận: họ không chốt cùng một máy.

Với sinh viên hướng compiler: **CFG và CYK vẫn parse ngôn ngữ lập trình**; transformer là bộ nhận khác, sức mạnh hình thức phải trích kèm giả thiết của survey.

Đọc sau 19.10–19.12. Đây là pointer đọc, không phải pumping lemma mới.

**Câu hỏi.** (1) Nêu một CFL mà pumping lemma loại; transformer-có-scratchpad có nhất thiết nhận nó? (2) Vì sao cận $$O(n^3)$$ của CYK dễ phát biểu hơn cận “expressivity” của transformer?
