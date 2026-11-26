---
layout: post
title: "Ghi chú mở rộng: Transformer và phân cấp Chomsky (2024)"
categories: chapter19
date: 2021-01-01
order: 13
required: false
lesson_type: optional
lang: vi
excerpt: "Bài ghi chú ứng dụng hiện đại (tiếng Việt) kết nối lý thuyết Toán rời rạc trong chương với các hệ thống tính toán và AI thực tế."
---

<div class="note-box" markdown="1">

**Tùy chọn.** Bài ghi chú ứng dụng mở rộng (tiếng Việt). **Không** thay thế các bài học nền tảng trong chương.

</div>

![Ngôn ngữ Hình thức & Khả năng Tổng quát hóa của LLM](/discrete-mathematics-for-computer-science-iuh/img/course/transformers_formal_languages.svg)

Nếu đưa các ngôn ngữ hình thức từ phân cấp Chomsky (chính quy, phi ngữ cảnh như dấu ngoặc Dyck, cảm ngữ cảnh như $$a^n b^n c^n$$) làm "bài kiểm tra chuẩn" cho mạng Transformer và các mô hình chuỗi hiện đại (RNN, Mamba/SSM), ta sẽ khám phá ra điều gì? Các bài báo nổi bật năm 2024 đã biến phân cấp Chomsky thành thước đo khoa học để hiểu kiến trúc mạng nơ-ron nào phù hợp với loại cấu trúc ngôn ngữ nào.

### Kiến thức cần nhớ: Ba trụ cột kết nối Phân cấp Chomsky và Mô hình Chuỗi 2024

1. **Thí nghiệm Phân cấp Chomsky trên Mạng Nơ-ron (Delétang et al.)**:
   Huấn luyện mạng trên chuỗi ngắn rồi kiểm tra khái quát hóa trên chuỗi dài hơn nhiều lần (length generalization): mạng có bộ nhớ trạng thái cố định (SSM/RNN tuyến tính) giỏi tác vụ Chính quy, trong khi kiến trúc có ngăn xếp ngoài hoặc bộ nhớ động mạnh hơn ở tác vụ Phi ngữ cảnh.
2. **Ngôn ngữ Dyck (Cân bằng ngoặc) và Độ sâu lồng nhau**:
   Ngôn ngữ Dyck-$$k$$ là bài kiểm tra kinh điển cho khả năng hiểu cấu trúc phân cấp (giống cây cú pháp code và ngôn ngữ tự nhiên). Transformer một lượt xử lý tốt Dyck có độ sâu bị chặn nhưng dễ sai khi độ sâu vượt ngưỡng huấn luyện.
3. **Ép cấu trúc bằng Văn phạm khi sinh văn bản (Grammar-Constrained Decoding)**:
   Kết hợp sức mạnh ngữ nghĩa của LLM với bộ phân tích cú pháp CFG (như `llama.cpp` GBNF hay Outlines) đảm bảo 100% đầu ra tuân thủ cú pháp SQL, JSON hoặc mã lập trình hợp lệ.

Chương 19 trình bày phân cấp Chomsky kèm các chứng minh chuẩn mực: CFG $$=$$ PDA, bổ đề bơm, dạng chuẩn CNF và thuật toán CYK. Bài khảo sát năm 2024 của Strobl và cộng sự (*TACL*) là tài liệu đọc **tùy chọn** tương ứng cho chương này, không thay thế phần lý thuyết ô-tô-mát và văn phạm.

Các tác giả xét đầu vào là những chuỗi có độ dài không bị chặn trên một bảng chữ cái hữu hạn — đúng với đối tượng $$L \subseteq \Sigma^*$$ của chương. Các định lý thu được phụ thuộc trực tiếp vào kiến trúc encoder hay decoder (có sinh ký hiệu trung gian hay không), loại cơ chế chú ý (*attention*) và độ chính xác số học. Chính vì vậy, một công trình có thể khẳng định “transformer nhận được mọi ngôn ngữ chính quy” trong khi công trình khác phủ nhận: họ đang xét hai mô hình máy khác nhau.

Đối với sinh viên theo hướng trình biên dịch, kết luận thực hành không thay đổi: **CFG và các thuật toán như CYK vẫn là công cụ chuẩn để phân tích ngôn ngữ lập trình**; còn transformer là một mô hình nhận dạng khác mà mọi phát biểu về sức mạnh hình thức đều phải đi kèm giả thiết cụ thể trong bài khảo sát.

Nên đọc ghi chú này sau khi hoàn thành mục 19.10–19.12; đây là gợi ý tài liệu đọc thêm chứ không phải một bổ đề bơm mới.

**Câu hỏi.** (1) Nêu một ngôn ngữ bị bổ đề bơm CFL của chương này loại (không phải CFL); liệu một transformer có bộ nhớ nháp (*scratchpad*) có nhất thiết nhận dạng được ngôn ngữ đó không? (2) Vì sao cận thời gian $$O(n^3)$$ của thuật toán CYK dễ phát biểu chặt chẽ hơn so với cận về “sức mạnh biểu diễn” (*expressivity*) của transformer?

### Giải thích: So sánh cơ chế ép JSON hợp lệ bằng CFG khi LLM sinh từng token

Giả sử ta yêu cầu LLM trả về JSON theo văn phạm nhỏ:
`Obj -> "{" "\"score\":" Num "}"`, `Num -> [0-9]+`.

Ở mỗi bước sinh token, bộ giải mã dùng trạng thái hiện tại của bộ phân tích cú pháp (CFG parser) làm mặt nạ (mask) trên toàn bộ từ vựng (ví dụ 50.000 token):

| Bước sinh | Chuỗi đã sinh | Token hợp lệ theo CFG | Hành động của Constrained Decoding |
| :---: | :--- | :--- | :--- |
| 1 | `""` | Chỉ `"{"` | Đặt xác suất 49.999 token còn lại bằng `0` → ép chọn `"{"` |
| 2 | `"{"` | Chỉ `"\"score\":"` | Loại bỏ mọi lời chào như `"Sure, here is..."` |
| 3 | `"{\"score\":"` | Chỉ các chữ số `0..9` | Đảm bảo giá trị chắc chắn là số, không bị sinh nhầm chữ |
| 4 | `"{\"score\":95"` | Chữ số `0..9` hoặc `"}"` | Cho phép tiếp tục số hoặc đóng ngoặc kết thúc hợp lệ |

Ví dụ làm từng bước này cho thấy lý thuyết CFG năm 1956 đang trực tiếp giải quyết bài toán kỹ thuật nóng nhất của hệ thống AI tác nhân (AI Agent) giai đoạn 2024–2026!

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=wjZofJX0v4M">Transformers, the tech behind LLMs | Deep Learning Chapter 5</a> — 3Blue1Brown, tiếng Anh. Giới thiệu kiến trúc transformer — mô hình được đặt lên bản đồ ngôn ngữ hình thức trong bài.
- <a href="https://www.youtube.com/watch?v=224plb3bCog">Chomsky Hierarchy - Computerphile</a> — Computerphile, tiếng Anh. Phân cấp Chomsky với hai cột mốc CFG và PDA của chương.
- <a href="https://www.youtube.com/watch?v=5_tfVe7ED3g">Context Free Grammar &amp; Context Free Language</a> — Neso Academy, tiếng Anh. Ôn lại CFG — lớp ngôn ngữ được đối chiếu với khả năng của transformer trong bài khảo sát.
