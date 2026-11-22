---
layout: post
title: "Ghi chú mở rộng: Transformer và automata (2022–2026)"
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

Bài ghi chú ứng dụng song ngữ. Bài này **không** thay thế các nội dung về DFA/NFA, bổ đề bơm, Myhill–Nerode hay máy Turing.

</div>

## English

This chapter classifies machines by what languages they recognize. From 2021 onward a parallel literature asks the same question of **transformers**. Strobl, Merrill, Weiss, Chiang, and Angluin, “What Formal Languages Can Transformers Express? A Survey,” *Transactions of the ACL* 12:543–561 (2024), [DOI 10.1162/tacl_a_00663](https://doi.org/10.1162/tacl_a_00663), [ACL Anthology](https://aclanthology.org/2024.tacl-1.30/), unify results that otherwise look contradictory because papers assume different masks, precision, and encoder/decoder APIs.

A useful slogan from that survey (read the paper for caveats): with chain-of-thought / intermediate symbols, decoder-style models can simulate more powerful machines; encoder-only models with restricted attention often sit inside small circuit classes (e.g. $$\mathsf{AC}^0$$ / $$\mathsf{TC}^0$$ discussions in the survey). The optional lesson for NCS students: **regular / CFL / decidable** remain the right yardsticks. A transformer is not “beyond the Chomsky hierarchy” until you fix the computational model the survey insists on fixing.

Read Sipser-style proofs first. Then use the 2024 survey as a reading list, not as a replacement chapter.

**Citations**

1. L. Strobl et al., “What Formal Languages Can Transformers Express? A Survey,” *TACL* 12 (2024). [DOI](https://doi.org/10.1162/tacl_a_00663)

**Questions.** (1) Which Chapter 18 machine do you get if you allow a transformer unbounded scratch tokens (informally: a tape)? (2) Why must “softmax vs hard attention” be stated before quoting an expressivity theorem?

## Tiếng Việt

Chương này phân loại các mô hình máy theo lớp ngôn ngữ mà chúng nhận dạng được. Từ năm 2021 trở lại đây, một hướng nghiên cứu song song đặt câu hỏi tương tự cho kiến trúc **transformer**. Công trình khảo sát của Strobl, Merrill, Weiss, Chiang và Angluin (*TACL*, 2024) hệ thống hóa lại các kết quả vốn thoạt nhìn có vẻ mâu thuẫn do mỗi bài báo giả định cơ chế che mặt nạ (*mask*), độ chính xác số học và giao diện encoder/decoder khác nhau.

Một nhận định cô đọng từ bài khảo sát (cần đọc bài gốc để nắm đầy đủ điều kiện giả thiết): khi được phép sinh chuỗi suy nghĩ (*chain-of-thought*) hay ký hiệu nháp trung gian, mô hình dạng decoder có thể mô phỏng các lớp máy mạnh hơn; trong khi đó, mô hình chỉ có encoder với cơ chế chú ý hạn chế thường nằm trong các lớp mạch nhỏ (như $$\mathsf{AC}^0$$ hoặc $$\mathsf{TC}^0$$). Điểm cốt lõi cần ghi nhớ: các mốc **chính quy / phi ngữ cảnh / quyết định được** vẫn là thước đo chuẩn xác; không thể nói transformer “vượt phân cấp Chomsky” khi chưa chốt rõ mô hình tính toán cụ thể.

Hãy nắm vững các chứng minh cổ điển theo phong cách Sipser trước, rồi dùng bài khảo sát năm 2024 này như danh mục tài liệu đọc thêm chứ không thay thế nội dung chương.

**Câu hỏi.** (1) Nếu cho phép một transformer sử dụng số lượng token nháp không bị chặn (tương tự như một băng nhớ), mô hình đó tương ứng với loại máy nào trong Chương 18? (2) Vì sao cần nêu rõ giả thiết “softmax hay hard attention” trước khi trích dẫn một định lý về sức mạnh biểu diễn?

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=wjZofJX0v4M">Transformers, the tech behind LLMs | Deep Learning Chapter 5</a> — 3Blue1Brown, tiếng Anh. Giới thiệu kiến trúc transformer — mô hình được đối chiếu với ô-tô-mát trong bài.
- <a href="https://www.youtube.com/watch?v=Qa6csfkK7_I">Finite State Machine (Finite Automata)</a> — Neso Academy, tiếng Anh. Ôn lại DFA, lớp máy hữu hạn nằm trong bản đồ của bài khảo sát.
- <a href="https://www.youtube.com/watch?v=224plb3bCog">Chomsky Hierarchy - Computerphile</a> — Computerphile, tiếng Anh. Phân cấp Chomsky — hệ quy chiếu ngôn ngữ dùng để đánh giá sức mạnh của transformer.
