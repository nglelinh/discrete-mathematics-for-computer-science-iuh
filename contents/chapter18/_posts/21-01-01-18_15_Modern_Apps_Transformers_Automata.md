---
layout: post
title: "Ghi chú mở rộng: Transformer và automata (2022–2026)"
categories: chapter18
date: 2021-01-01
order: 15
required: false
lesson_type: optional
lang: vi
excerpt: "Bài ghi chú ứng dụng hiện đại (tiếng Việt) kết nối lý thuyết Toán rời rạc trong chương với các hệ thống tính toán và AI thực tế."
---

<div class="note-box" markdown="1">

**Tùy chọn.** Bài ghi chú ứng dụng mở rộng (tiếng Việt). **Không** thay thế các bài học nền tảng trong chương.

</div>

![Biểu diễn Ôtômat Hữu hạn trong Kiến trúc Transformer](/discrete-mathematics-for-computer-science-iuh/img/course/transformers_automata_limits.svg)

Một câu hỏi cực kỳ hấp dẫn xuất hiện trong kỷ nguyên mô hình ngôn ngữ lớn (LLM): *Nếu một mạng Transformer có độ sâu cố định và độ chính xác dấu phẩy động hữu hạn, nó có thực sự "biết tính toán" như máy Turing hay thực chất chỉ là một máy trạng thái hữu hạn khổng lồ?* Các công trình nghiên cứu giai đoạn 2022–2026 đã dùng chính công cụ của Chương 18 (DFA, máy Turing, mạch ngưỡng) để đo chính xác trần năng lực của Transformer.

### Kiến thức cần nhớ: Ba trụ cột nối Automata cổ điển với Transformer hiện đại

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

### Giải thích: Minh họa vì sao bài toán `PARITY` dễ với DFA 2 trạng thái nhưng khó với Transformer một lượt

Xét ngôn ngữ `PARITY` gồm các chuỗi nhị phân có **số bit `1` là chẵn**:
- **Với DFA**: Chỉ cần đúng **2 trạng thái** ($$q_{\text{chẵn}}, q_{\text{lẻ}}$$). Đọc chuỗi dài 10 bit hay 10.000 bit đều dùng đúng 2 trạng thái và đạt độ chính xác **100%**.
- **Với Transformer một lượt không có CoT**: Để tính `PARITY` của chuỗi dài $$n$$ trong 1 bước, lớp attention phải tổng hợp đồng thời toàn bộ $$n$$ vị trí chỉ qua vài tầng cộng trọng số dấu phẩy động. Khi huấn luyện ở $$n \le 20$$ rồi thử ở $$n = 100$$, sai số cộng dồn làm mô hình nhanh chóng rơi xuống mức đoán ngẫu nhiên ($$50\%$$).
- **Khi bật Chain-of-Thought**: Mô hình viết ra trạng thái tích lũy sau từng bit (`0 → 1 → 1 → 0`), thực chất đang **mô phỏng trực tiếp hàm chuyển $$\delta$$ của DFA 2 trạng thái trên băng nháp văn bản** — nhờ đó khôi phục khả năng xử lý chuỗi dài vượt xa tập huấn luyện!

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=wjZofJX0v4M">Transformers, the tech behind LLMs | Deep Learning Chapter 5</a> — 3Blue1Brown, tiếng Anh. Giới thiệu kiến trúc transformer — mô hình được đối chiếu với ô-tô-mát trong bài.
- <a href="https://www.youtube.com/watch?v=Qa6csfkK7_I">Finite State Machine (Finite Automata)</a> — Neso Academy, tiếng Anh. Ôn lại DFA, lớp máy hữu hạn nằm trong bản đồ của bài khảo sát.
- <a href="https://www.youtube.com/watch?v=224plb3bCog">Chomsky Hierarchy - Computerphile</a> — Computerphile, tiếng Anh. Phân cấp Chomsky — hệ quy chiếu ngôn ngữ dùng để đánh giá sức mạnh của transformer.
