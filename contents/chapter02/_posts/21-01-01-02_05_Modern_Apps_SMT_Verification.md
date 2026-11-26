---
layout: post
title: "Ghi chú mở rộng: Bộ giải SMT và logic vị từ (2022–2026)"
categories: chapter02
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

![Quy trình Kiểm chứng Hình thức với Bộ giải SMT](/discrete-mathematics-for-computer-science-iuh/img/course/smt_verification_pipeline.svg)

Logic vị từ bổ sung cấu trúc bên trong mỗi mệnh đề thông qua vị từ, miền xác định và các lượng từ $$\forall$$, $$\exists$$. **SMT** (Satisfiability Modulo Theories) là dạng ứng dụng công nghiệp của cùng ý tưởng đó: giải SAT trên phần khung Boolean kết hợp với các bộ giải chuyên biệt cho số nguyên, bit-vector, mảng và hàm không diễn giải.

Barbosa và cộng sự (TACAS 2022) giới thiệu **cvc5** (phiên bản kế nhiệm của CVC4), đánh giá trên toàn bộ bộ chuẩn SMT-LIB và so sánh với CVC4 cũng như Z3. Bộ giải này có khả năng xuất chứng minh, xử lý số học phi tuyến và tự động cụ thể hóa lượng từ (quantifier instantiation) — biến thách thức về lượng từ lồng nhau ở Mục 2.2 thành một thủ tục tự động.

Một truy vấn kiểm chứng điển hình vẫn là một công thức logic vị từ, chẳng hạn $$\forall i.\; (0 \le i < n) \rightarrow (a[i] \ge 0)$$. Bộ giải cvc5 không thay đổi ngữ nghĩa của $$\forall$$; thay vào đó, nó giải quyết các phân mảnh (fragment) mà sự kết hợp giữa suy luận CNF và bổ đề lý thuyết đủ mạnh cho trình biên dịch, hợp đồng thông minh và công cụ kiểm chứng chương trình. Sinh viên nên đọc ghi chú này sau khi hoàn thành các mục bắt buộc về lượng từ.

**Câu hỏi.** (1) Trong một truy vấn SMT, phần nào thuộc bài toán SAT mệnh đề và phần nào thuộc các lý thuyết nền? (2) Vì sao quá trình cụ thể hóa lượng từ không đầy đủ trên một số phân mảnh logic mà giáo trình vẫn viết được?

### Kiến thức cần nhớ: SMT Solver biến Logic Vị từ thành vũ khí kiểm chứng phần mềm như thế nào?

Kiểm thử thông thường chỉ thử được vài chục đầu vào cụ thể và cầu mong không có lỗi ẩn ở biên. **SMT (Satisfiability Modulo Theories)**—với các bộ giải như Z3 và cvc5—kết hợp Logic Vị từ Chương 2 với các lý thuyết toán học chuyên biệt trên ba trụ cột:

1. **Lõi SAT + Các bộ giải lý thuyết (Kiến trúc DPLL(T))**:
   SAT xử lý cấu trúc logic ($$\land, \lor, \neg$$), còn các bộ giải lý thuyết xử lý số học nguyên/thực, **vector bit (bitvectors)** mô phỏng chính xác tràn số 32/64-bit, mảng và chuỗi ký tự.
2. **Chiến lược Phủ định để Chứng minh ($$\forall x\, P(x) \iff \text{UNSAT}(\neg P(x))$$ )**:
   Để chứng minh chương trình an toàn với *mọi* đầu vào, ta hỏi bộ giải xem có tồn tại đầu vào nào làm vi phạm an toàn ($$\neg P(x)$$) không. Trả về `UNSAT` nghĩa là đã chứng minh tuyệt đối; trả về `SAT` sẽ in ra đúng đầu vào gây lỗi!
3. **Ứng dụng thực tiễn quy mô lớn**:
   AWS dùng SMT (Zelkova/Cedar) để chứng minh chính sách phân quyền IAM không bao giờ hở quyền công khai, còn các công cụ như Kani/CBMC kiểm chứng mã Rust/C chống tràn số và truy cập ngoài biên mảng.

### Giải thích: Bắt lỗi tràn số `i32` trong tìm kiếm nhị phân bằng một câu truy vấn SMT

Công thức trung điểm quen thuộc `mid = (low + high) / 2` từng gây lỗi ẩn suốt gần 20 năm trên kiểu số nguyên có dấu 32-bit (`i32`, giá trị tối đa $$2^{31} - 1 = 2.147.483.647$$):
- **Truy vấn phủ định gửi Z3**: Tìm `low, high` thỏa $$0 \le \text{low} \le \text{high}$$ nhưng `(low + high) / 2 < 0`.
- **Z3 trả về `SAT` cùng phản ví dụ cụ thể**: $$\text{low} = 2^{30} = 1.073.741.824$$, $$\text{high} = 2^{30} = 1.073.741.824$$. Khi cộng trong 32-bit bù 2: $$2^{30} + 2^{30} = 2^{31} \equiv \mathbf{-2.147.483.648}$$ → `mid = -1.073.741.824` (vượt ngoài biên mảng!).
- **Bản sửa chuẩn**: Đổi sang `mid = low + (high - low) / 2` rồi hỏi lại đúng truy vấn phủ định đó → Z3 trả về **`UNSAT`**, chứng minh tuyệt đối không bao giờ tràn số trên toàn bộ $$2^{62}$$ cặp đầu vào hợp lệ!

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=CNQwSXKBGgw">From z3 to cvc5</a> — cvc solver, tiếng Anh. Giới thiệu quá trình phát triển trong cùng họ bộ giải từ Z3 đến cvc5 được nhắc trong bài.
- <a href="https://www.youtube.com/watch?v=EacYNe7moSs">Z3 Explained - Satisfiability Modulo Theories &amp; SMT Solvers</a> — Guided Hacking, tiếng Anh. Giải thích SMT như sự kết hợp giữa SAT và các lý thuyết, gắn với khung logic vị từ của chương.
- <a href="https://www.youtube.com/watch?v=e07bWJ2L9VY">cvc5 pythonic API</a> — cvc solver, tiếng Anh. Minh họa cách gọi lượng từ trong mã nguồn qua API Python của cvc5.
