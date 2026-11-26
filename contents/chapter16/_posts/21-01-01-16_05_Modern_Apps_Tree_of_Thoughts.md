---
layout: post
title: "Ghi chú mở rộng: Cây tìm kiếm cho mô hình ngôn ngữ (2023–2026)"
categories: chapter16
date: 2021-01-01
order: 5
required: false
lesson_type: optional
lang: vi
excerpt: "Bài ghi chú ứng dụng hiện đại (tiếng Việt) kết nối lý thuyết Toán rời rạc trong chương với các hệ thống tính toán và AI thực tế."
---

<div class="note-box" markdown="1">

**Tùy chọn.** Bài ghi chú ứng dụng mở rộng (tiếng Việt). **Không** thay thế các bài học nền tảng trong chương.

</div>

![Cây Suy nghĩ (Tree of Thoughts) trong Suy luận AI](/discrete-mathematics-for-computer-science-iuh/img/course/tree_of_thoughts_search.svg)

Cây có gốc vốn là mô hình quen thuộc của kỹ thuật quay lui (*backtracking*): mỗi nút biểu diễn một phần lời giải ban đầu, các nút con là những bước mở rộng hợp lệ, còn DFS/BFS quyết định thứ tự duyệt. Yao và cộng sự (NeurIPS 2023) đã áp dụng chính mô hình này vào quá trình suy luận của mô hình ngôn ngữ lớn (LLM).

Mỗi trạng thái được biểu diễn dưới dạng $$s = [x, z_{1\cdots i}]$$ (đầu vào kèm chuỗi bước suy nghĩ đã sinh ra). Bài báo xác định bốn lựa chọn thiết kế — cách phân tách một bước suy nghĩ, cách mở rộng nhánh, cách chấm điểm trạng thái và thuật toán tìm kiếm — rồi triển khai cụ thể bằng BFS (cho bài toán Game of 24) và DFS có cắt tỉa (cho trò chơi ô chữ nhỏ). Kết quả nổi bật: GPT-4 kết hợp chuỗi suy nghĩ (*chain-of-thought*) chỉ giải được **4%** bài toán Game of 24, trong khi Tree of Thoughts (ToT) đạt **74%**.

Liên hệ với nội dung chương: ToT không đưa ra một định nghĩa cây mới mà là *tìm kiếm trên cây* (dựa trên chính các phép duyệt đã học) kết hợp với bộ đánh giá heuristic. Nếu Huffman và BST phục vụ mã hóa và quản lý khóa có thứ tự, thì ToT khai phá cây trạng thái khi các nhánh mở rộng mang bản chất ngôn ngữ thay vì số học.

**Câu hỏi.** (1) Vẽ cây trạng thái ToT cho một ví dụ Game of 24 có hệ số nhánh bằng 3 và độ sâu bằng 2. (2) Phép duyệt nào tương ứng với chiến lược “mở rộng mọi bước suy nghĩ ở độ sâu hiện tại và giữ lại $$b$$ nhánh tốt nhất”?

### Kiến thức cần nhớ: Cây Suy luận (Tree-of-Thoughts) cho Mô hình Ngôn ngữ Lớn
- **Hạn chế của Chain-of-Thought (Chuỗi suy nghĩ):** Sinh văn bản tuyến tính một chiều giống như đi trong mê cung mà **không được quay lui** — chỉ cần sai một bước tính nhỏ ở đầu, toàn bộ lời giải phía sau sụp đổ!
- **Tree-of-Thoughts (ToT, 2023–2026):** Biến quá trình suy luận thành một **cây tìm kiếm thực thụ** (chương 16!): mỗi nút là một trạng thái tư duy trung gian, kết hợp **BFS/DFS, cắt tỉa nhánh chết và quay lui (backtracking)** cùng hàm lượng giá!

### Ví dụ tính tay làm từng bước: Cây suy luận giải bài toán "Game of 24" với `(4, 9, 10, 13)`
Mục tiêu: dùng cộng, trừ, nhân, chia đúng 4 số `(4, 9, 10, 13)` để ra **24**:
1. **Tầng 1 (Sinh nhánh từ gốc):**
   - Nhánh A: `13 - 9 = 4` $$\to$$ còn `(4, 4, 10)` (*Khả thi!*).
   - Nhánh B: `4 × 9 = 36` $$\to$$ còn `(10, 13, 36)` (*Trung bình*).
   - Nhánh C: `13 × 10 = 130` $$\to$$ còn `(4, 9, 130)` (*Cắt tỉa ngay vì quá lớn!*).
2. **Tầng 2 (Mở rộng nhánh A `(4, 4, 10)`):**
   - `10 - 4 = 6` $$\to$$ còn `(4, 6)` (*Chắc chắn ra 24!*).
3. **Tầng 3 (Đích):** `4 × 6 = 24` $$\implies$$ lời giải hoàn chỉnh: **$$(10 - (13 - 9)) \times 4 = 24$$** (hoặc $$(10 - 4) \times (13 - 9) = 24$$)!

### Giải thích: 4 bước nối Lý thuyết Cây Chương 16 với AI Suy luận
#### Bước 1: Định nghĩa "nút" là một bước tư duy hoàn chỉnh (không phải từng từ rời)
Giúp độ sâu cây $$d$$ chỉ khoảng 3–10 tầng thay vì hàng trăm token.
#### Bước 2: Chọn chiến lược duyệt BFS (Beam Search) hay DFS (Backtracking)
BFS giữ lại top-$$b$$ nhánh tốt nhất ở mỗi tầng; DFS đào sâu 1 nhánh và quay lui ngay khi hàm đánh giá báo "ngõ cụt".
#### Bước 3: Kiểm soát bùng nổ tổ hợp $$O(b^d)$$
Cắt tỉa sớm bằng bộ kiểm chứng (verifier / trình biên dịch / trình chạy code) để không lãng phí tài nguyên tính toán.
#### Bước 4: Đánh đổi thời gian suy luận lấy độ thông minh (Test-Time Compute Scaling)
Các mô hình suy luận hiện đại (2024–2026) chứng minh rằng **cấp thêm ngân sách duyệt cây lúc suy luận** giúp giải được những bài toán toán học và lập trình mà sinh một mạch không thể làm nổi!

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=MXBxNUnC7iY">Tree of Thoughts: Deliberate Problem Solving with Large Language Models \| Paper Summary</a> — Lucas Soares \| Automata Learning Lab, tiếng Anh. Tóm tắt bài báo Tree of Thoughts về cây các lời giải trung gian và cách duyệt.
- <a href="https://www.youtube.com/watch?v=ut5kp56wW_4">Tree of Thoughts: Deliberate Problem Solving with Large Language Models (Full Paper Review)</a> — Yannic Kilcher, tiếng Anh. Phân tích chi tiết bài báo về tìm kiếm có chủ đích trên cây suy nghĩ.
- <a href="https://www.youtube.com/watch?v=z_OwSnFY_5s">[Discrete Mathematics] Tree Directories and Traversals</a> — TrevTutor, tiếng Anh. Ôn lại các phép duyệt cây cổ điển (BFS/DFS) làm nền tảng cho phương pháp này.
