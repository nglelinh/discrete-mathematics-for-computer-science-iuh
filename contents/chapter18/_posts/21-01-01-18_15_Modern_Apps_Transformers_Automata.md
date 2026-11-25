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

A central theoretical question in the LLM era asks: *how does a fixed-depth Transformer compare against classical automata and Turing machines?* Research from 2022–2026 uses the exact machinery of Chapter 18—DFAs, threshold circuits, and Turing tapes—to characterize both the limits of single-pass Transformers and why intermediate tokens change their computational power.

### Background Knowledge Map: Three Pillars Linking Automata to Transformers

1. **Single-Pass Transformers & Constant-Depth Circuits ($$\mathrm{TC}^0$$)**:
   A bounded-precision Transformer without scratchpad tokens maps naturally to constant-depth threshold circuits, explaining systematic length-generalization failures on sequential state-tracking tasks such as `PARITY`.
2. **Chain-of-Thought as a Turing-Machine Scratchpad**:
   Allowing the model to emit and re-read intermediate tokens turns the context window into a read/write tape, dramatically expanding expressivity toward Turing completeness under unbounded steps.
3. **Constrained Decoding via DFAs**:
   Production LLM systems compile JSON schemas or regular expressions into DFAs and mask out invalid next tokens at every decoding step according to $$\delta(q, a)$$.

This chapter classifies machines by what languages they recognize. From 2021 onward a parallel literature asks the same question of **transformers**. Strobl, Merrill, Weiss, Chiang, and Angluin, “What Formal Languages Can Transformers Express? A Survey,” *Transactions of the ACL* 12:543–561 (2024), [DOI 10.1162/tacl_a_00663](https://doi.org/10.1162/tacl_a_00663), [ACL Anthology](https://aclanthology.org/2024.tacl-1.30/), unify results that otherwise look contradictory because papers assume different masks, precision, and encoder/decoder APIs.

A useful slogan from that survey (read the paper for caveats): with chain-of-thought / intermediate symbols, decoder-style models can simulate more powerful machines; encoder-only models with restricted attention often sit inside small circuit classes (e.g. $$\mathsf{AC}^0$$ / $$\mathsf{TC}^0$$ discussions in the survey). The optional lesson for NCS students: **regular / CFL / decidable** remain the right yardsticks. A transformer is not “beyond the Chomsky hierarchy” until you fix the computational model the survey insists on fixing.

Read Sipser-style proofs first. Then use the 2024 survey as a reading list, not as a replacement chapter.

**Citations**

1. L. Strobl et al., “What Formal Languages Can Transformers Express? A Survey,” *TACL* 12 (2024). [DOI](https://doi.org/10.1162/tacl_a_00663)

**Questions.** (1) Which Chapter 18 machine do you get if you allow a transformer unbounded scratch tokens (informally: a tape)? (2) Why must “softmax vs hard attention” be stated before quoting an expressivity theorem?

### Deep-Dive Explanation (Read Slowly): Why `PARITY` Separates a 2-State DFA from a Single-Pass Transformer

Consider the regular language `PARITY` of binary strings with an even number of `1`s:
- **2-state DFA**: Tracks only $$q_{\text{even}}$$ and $$q_{\text{odd}}$$; achieves **100%** accuracy on length $$n = 10$$ and length $$n = 10{,}000$$ alike.
- **Single-pass Transformer (no CoT)**: Trained on lengths $$n \le 20$$, fixed-depth attention aggregates all positions simultaneously in finite precision and typically degrades toward random guessing ($$50\%$$) on $$n = 100$$.
- **With Chain-of-Thought**: Emitting the running parity after each bit (`0 -> 1 -> 1 -> 0`) explicitly simulates the 2-state DFA transition function $$\delta$$ on the token scratchpad, restoring accurate state tracking over much longer inputs.

## Tiếng Việt

Một câu hỏi cực kỳ hấp dẫn xuất hiện trong kỷ nguyên mô hình ngôn ngữ lớn (LLM): *Nếu một mạng Transformer có độ sâu cố định và độ chính xác dấu phẩy động hữu hạn, nó có thực sự "biết tính toán" như máy Turing hay thực chất chỉ là một máy trạng thái hữu hạn khổng lồ?* Các công trình nghiên cứu giai đoạn 2022–2026 đã dùng chính công cụ của Chương 18 (DFA, máy Turing, mạch ngưỡng) để đo chính xác trần năng lực của Transformer.

### Bản đồ kiến thức nền: Ba trụ cột nối Automata cổ điển với Transformer hiện đại

1. **Giới hạn của Transformer một lượt (Fixed-depth Forward Pass)**:
   Một lượt suy luận thẳng không sinh token trung gian tương ứng với mạch song song độ sâu hằng số ($$\mathrm{TC}^0$$), nên gặp khó khăn khi khái quát độ dài (length generalization) cho các bài toán theo dõi trạng thái tuần tự như kiểm tra chẵn lẻ (`PARITY`).
2. **Chuỗi suy nghĩ (Chain-of-Thought) như băng nháp của Máy Turing**:
   Khi cho phép mô hình sinh thêm các token trung gian rồi đọc lại chúng ở bước sau, ngữ cảnh văn bản đóng vai trò giống hệt **băng đọc/ghi của máy Turing**, nâng sức mạnh tính toán vượt xa lớp mạch độ sâu hằng số.
3. **Chế độ suy luận có cấu trúc (Constrained Decoding bằng DFA)**:
   Trong thực tế sản phẩm (như ép LLM xuất JSON đúng lược đồ), người ta biên dịch biểu thức chính quy thành DFA và ở mỗi bước sinh token chỉ giữ lại những token hợp lệ theo hàm chuyển $$\delta$$.

Chương này phân loại các mô hình máy theo lớp ngôn ngữ mà chúng nhận dạng được. Từ năm 2021 trở lại đây, một hướng nghiên cứu song song đặt câu hỏi tương tự cho kiến trúc **transformer**. Công trình khảo sát của Strobl, Merrill, Weiss, Chiang và Angluin (*TACL*, 2024) hệ thống hóa lại các kết quả vốn thoạt nhìn có vẻ mâu thuẫn do mỗi bài báo giả định cơ chế che mặt nạ (*mask*), độ chính xác số học và giao diện encoder/decoder khác nhau.

Một nhận định cô đọng từ bài khảo sát (cần đọc bài gốc để nắm đầy đủ điều kiện giả thiết): khi được phép sinh chuỗi suy nghĩ (*chain-of-thought*) hay ký hiệu nháp trung gian, mô hình dạng decoder có thể mô phỏng các lớp máy mạnh hơn; trong khi đó, mô hình chỉ có encoder với cơ chế chú ý hạn chế thường nằm trong các lớp mạch nhỏ (như $$\mathsf{AC}^0$$ hoặc $$\mathsf{TC}^0$$). Điểm cốt lõi cần ghi nhớ: các mốc **chính quy / phi ngữ cảnh / quyết định được** vẫn là thước đo chuẩn xác; không thể nói transformer “vượt phân cấp Chomsky” khi chưa chốt rõ mô hình tính toán cụ thể.

Hãy nắm vững các chứng minh cổ điển theo phong cách Sipser trước, rồi dùng bài khảo sát năm 2024 này như danh mục tài liệu đọc thêm chứ không thay thế nội dung chương.

**Câu hỏi.** (1) Nếu cho phép một transformer sử dụng số lượng token nháp không bị chặn (tương tự như một băng nhớ), mô hình đó tương ứng với loại máy nào trong Chương 18? (2) Vì sao cần nêu rõ giả thiết “softmax hay hard attention” trước khi trích dẫn một định lý về sức mạnh biểu diễn?

### Khung giải thích (nên đọc chậm): Minh họa vì sao bài toán `PARITY` dễ với DFA 2 trạng thái nhưng khó với Transformer một lượt

Xét ngôn ngữ `PARITY` gồm các chuỗi nhị phân có **số bit `1` là chẵn**:
- **Với DFA**: Chỉ cần đúng **2 trạng thái** ($$q_{\text{chẵn}}, q_{\text{lẻ}}$$). Đọc chuỗi dài 10 bit hay 10.000 bit đều dùng đúng 2 trạng thái và đạt độ chính xác **100%**.
- **Với Transformer một lượt không có CoT**: Để tính `PARITY` của chuỗi dài $$n$$ trong 1 bước, lớp attention phải tổng hợp đồng thời toàn bộ $$n$$ vị trí chỉ qua vài tầng cộng trọng số dấu phẩy động. Khi huấn luyện ở $$n \le 20$$ rồi thử ở $$n = 100$$, sai số cộng dồn làm mô hình nhanh chóng rơi xuống mức đoán ngẫu nhiên ($$50\%$$).
- **Khi bật Chain-of-Thought**: Mô hình viết ra trạng thái tích lũy sau từng bit (`0 → 1 → 1 → 0`), thực chất đang **mô phỏng trực tiếp hàm chuyển $$\delta$$ của DFA 2 trạng thái trên băng nháp văn bản** — nhờ đó khôi phục khả năng xử lý chuỗi dài vượt xa tập huấn luyện!

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=wjZofJX0v4M">Transformers, the tech behind LLMs | Deep Learning Chapter 5</a> — 3Blue1Brown, tiếng Anh. Giới thiệu kiến trúc transformer — mô hình được đối chiếu với ô-tô-mát trong bài.
- <a href="https://www.youtube.com/watch?v=Qa6csfkK7_I">Finite State Machine (Finite Automata)</a> — Neso Academy, tiếng Anh. Ôn lại DFA, lớp máy hữu hạn nằm trong bản đồ của bài khảo sát.
- <a href="https://www.youtube.com/watch?v=224plb3bCog">Chomsky Hierarchy - Computerphile</a> — Computerphile, tiếng Anh. Phân cấp Chomsky — hệ quy chiếu ngôn ngữ dùng để đánh giá sức mạnh của transformer.
