---
layout: post
title: "Ghi chú mở rộng: NP-đầy đủ, kỷ lục SAT và OOD của mạng nơ-ron (2022–2026)"
categories: chapter20
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

![Độ phức tạp NP-Khó và Sức mạnh Bộ giải Thực tế (SAT/MIP)](/discrete-mathematics-for-computer-science-iuh/img/course/complexity_modern_solvers.svg)

Một nghịch lý thú vị của khoa học máy tính hiện đại: `SAT` là bài toán NP-complete kinh điển khó nhất trong lớp $$NP$$, nhưng các bộ giải **CDCL SAT solver** ngày nay lại giải gọn gàng các công thức có hàng triệu biến trong kiểm chứng chip Intel/AMD, chứng minh định lý toán học (như bài toán bộ ba Pythagore Boolean) và giải bài toán lập lịch công nghiệp. Trong khi đó, các mạng nơ-ron học giải bài toán NP-hard (như TSP hay SAT) thường gặp rào cản khái quát ngoài phân phối (OOD) khi kích thước đồ thị tăng lên.

### Kiến thức cần nhớ: Ba trụ cột của Độ phức tạp Hiện đại & Bộ giải Thực tế

1. **CDCL SAT Solver (Conflict-Driven Clause Learning)**:
   Thay vì quay lui mù quáng (DPLL), CDCL phân tích nguyên nhân mâu thuẫn để **học thêm mệnh đề mới (conflict clause)**, nhảy lùi không tuần tự (*backjumping*) và khởi động lại thông minh — khai thác triệt để cấu trúc ẩn của bài toán thực tế.
2. **Chứng chỉ không thỏa được (DRAT Proofs)**:
   Khi SAT solver báo `UNSAT` (như chứng minh một định lý toán học hay xác nhận thiết kế chip không có lỗi), nó xuất ra một tệp chứng minh DRAT có thể kiểm chứng độc lập bằng trình kiểm tra cực nhỏ — bảo đảm độ tin cậy tuyệt đối.
3. **Học máy kết hợp Bộ giải (Neural-Guided Search & OOD Limits)**:
   Mạng nơ-ron khó thay thế hoàn toàn bộ giải chính xác ở kích thước lớn ngoài tập huấn luyện (OOD), nên hướng đi hiệu quả giai đoạn 2022–2026 là dùng mạng nơ-ron làm *heuristic chọn nhánh* bên trong khung tìm kiếm chính xác (branch-and-bound / CDCL).

SAT là bài toán NP-complete (như đã chứng minh trong chương này), nhưng định lý đó **không** khẳng định rằng mọi thể hiện đầu vào đều khó giải. Hai dẫn chứng thực nghiệm giai đoạn 2022–2024 giúp phân biệt rõ điểm này:

1. **Bộ giải SAT công nghiệp.** Kissat 4.0 giành cả ba huy chương vàng ở các hạng mục chính tại SAT Competition 2024. Các bộ giải theo kiến trúc CDCL thường xuyên xử lý thành công những công thức CNF kiểm chứng phần mềm có hàng triệu biến. Tính NP-complete ở trường hợp xấu nhất và hiệu năng thực tế ở trường hợp trung vị là hai phát biểu hoàn toàn khác nhau — kết quả cuộc thi là minh chứng cụ thể cho sự phân biệt đó.
2. **Thuật toán học từ dữ liệu.** Bộ chuẩn CLRS-30 (ICML 2022) cho thấy nhiều mô hình mạng nơ-ron đạt độ chính xác cao trên đồ thị nhỏ nhưng sụp đổ khi kích thước $$n$$ tăng lên. Đây là hạn chế về khả năng **tổng quát hóa thực nghiệm** chứ không tạo ra một lớp độ phức tạp mới, đồng thời nhắc nhở rằng không thể xem một mạng đã huấn luyện là một thuật toán thời gian đa thức có chứng minh tính đúng đắn.

Liên hệ với Bài 20.13 (độ phức tạp mịn và trường hợp trung bình): khoảng cách thực tế ở các bộ giải SAT và hiện tượng sụt giảm ngoài phân phối (OOD) trên CLRS chính là *lý do* các lý thuyết phân tích sâu hơn này ra đời. Ghi chú này không bổ sung thêm phép rút gọn mới.

**Câu hỏi.** (1) Hãy phát biểu định lý Cook–Levin và kết quả huy chương của Kissat tại SAT Competition 2024 thành hai câu *không mâu thuẫn* với nhau. (2) Nếu một GNN đạt độ chính xác 99% cho bài toán BFS trên đồ thị 16 đỉnh của CLRS, nhận định nào về mặt lý thuyết thuật toán vẫn không được phép đưa ra?

### Giải thích: Minh họa 1 bước "học mệnh đề từ mâu thuẫn" (Clause Learning) trong CDCL

Xét công thức nhỏ có 3 mệnh đề:
$$C_1 = (\neg x_1 \lor x_2), \qquad C_2 = (\neg x_1 \lor \neg x_2 \lor x_3), \qquad C_3 = (\neg x_1 \lor \neg x_3).$$
1. Giả sử bộ giải quyết định thử nhánh $$x_1 = \text{True}$$.
2. Lan truyền đơn vị (Unit Propagation):
   - Từ $$C_1$$ suy bắt buộc $$x_2 = \text{True}$$.
   - Từ $$C_2$$ (với $$x_1=T, x_2=T$$) suy bắt buộc $$x_3 = \text{True}$$.
   - Thế vào $$C_3 = (\neg x_1 \lor \neg x_3)$$ → **MÂU THUẪN!**
3. **Học mệnh đề mới:** Thay vì chỉ lùi lại thử nhánh khác rồi sau này lại vô tình đặt $$x_1 = \text{True}$$ lần nữa ở một nhánh khác, CDCL rút ra ngay mệnh đề học được $$C_{\text{learned}} = (\neg x_1)$$ và bổ sung vào công thức! Từ giây phút đó, toàn bộ nửa không gian tìm kiếm có $$x_1 = \text{True}$$ bị cắt tỉa vĩnh viễn!

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=YX40hbAHx3s">P vs. NP and the Computational Complexity Zoo</a> — hackerdashery, tiếng Anh. Nhấn mạnh rằng NP-complete phản ánh độ khó trường hợp xấu nhất, không có nghĩa mọi thể hiện đều khó.
- <a href="https://www.youtube.com/watch?v=YUqR-8rZ_gQ">Lecture 10-3 CDCL (Lecture 5 in CS433)</a> — Automated Reasoning, tiếng Anh. Giải thích kiến trúc CDCL đằng sau các bộ giải SAT công nghiệp như Kissat.
- <a href="https://www.youtube.com/watch?v=DZDrRxM6RwI">Petar Veličković (DeepMind) — Neural Algorithmic Reasoning</a> — Zeta Alpha, tiếng Anh. Phân tích khả năng và giới hạn ngoài phân phối của mạng nơ-ron khi học thuật toán đồ thị.
