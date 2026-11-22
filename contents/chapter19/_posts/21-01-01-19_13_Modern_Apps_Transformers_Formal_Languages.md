---
layout: post
title: "Ghi chú mở rộng: Transformer và phân cấp Chomsky (2024)"
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

Bài ghi chú ứng dụng song ngữ. Bài này **không** thay thế các nội dung về CFG, PDA, bổ đề bơm CFL hay thuật toán CYK.

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

Chương 19 trình bày phân cấp Chomsky kèm các chứng minh chuẩn mực: CFG $$=$$ PDA, bổ đề bơm, dạng chuẩn CNF và thuật toán CYK. Bài khảo sát năm 2024 của Strobl và cộng sự (*TACL*) là tài liệu đọc **tùy chọn** tương ứng cho chương này, không thay thế phần lý thuyết ô-tô-mát và văn phạm.

Các tác giả xét đầu vào là những chuỗi có độ dài không bị chặn trên một bảng chữ cái hữu hạn — đúng với đối tượng $$L \subseteq \Sigma^*$$ của chương. Các định lý thu được phụ thuộc trực tiếp vào kiến trúc encoder hay decoder (có sinh ký hiệu trung gian hay không), loại cơ chế chú ý (*attention*) và độ chính xác số học. Chính vì vậy, một công trình có thể khẳng định “transformer nhận được mọi ngôn ngữ chính quy” trong khi công trình khác phủ nhận: họ đang xét hai mô hình máy khác nhau.

Đối với sinh viên theo hướng trình biên dịch, kết luận thực hành không thay đổi: **CFG và các thuật toán như CYK vẫn là công cụ chuẩn để phân tích ngôn ngữ lập trình**; còn transformer là một mô hình nhận dạng khác mà mọi phát biểu về sức mạnh hình thức đều phải đi kèm giả thiết cụ thể trong bài khảo sát.

Nên đọc ghi chú này sau khi hoàn thành mục 19.10–19.12; đây là gợi ý tài liệu đọc thêm chứ không phải một bổ đề bơm mới.

**Câu hỏi.** (1) Nêu một ngôn ngữ bị bổ đề bơm CFL của chương này loại (không phải CFL); liệu một transformer có bộ nhớ nháp (*scratchpad*) có nhất thiết nhận dạng được ngôn ngữ đó không? (2) Vì sao cận thời gian $$O(n^3)$$ của thuật toán CYK dễ phát biểu chặt chẽ hơn so với cận về “sức mạnh biểu diễn” (*expressivity*) của transformer?

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=wjZofJX0v4M">Transformers, the tech behind LLMs | Deep Learning Chapter 5</a> — 3Blue1Brown, tiếng Anh. Giới thiệu kiến trúc transformer — mô hình được đặt lên bản đồ ngôn ngữ hình thức trong bài.
- <a href="https://www.youtube.com/watch?v=224plb3bCog">Chomsky Hierarchy - Computerphile</a> — Computerphile, tiếng Anh. Phân cấp Chomsky với hai cột mốc CFG và PDA của chương.
- <a href="https://www.youtube.com/watch?v=5_tfVe7ED3g">Context Free Grammar &amp; Context Free Language</a> — Neso Academy, tiếng Anh. Ôn lại CFG — lớp ngôn ngữ được đối chiếu với khả năng của transformer trong bài khảo sát.
