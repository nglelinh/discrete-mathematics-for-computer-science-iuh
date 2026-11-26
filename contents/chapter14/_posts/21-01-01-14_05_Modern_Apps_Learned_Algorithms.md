---
layout: post
title: "Ghi chú mở rộng: Thuật toán do học tăng cường tìm ra (2022–2026)"
categories: chapter14
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

![Thuật toán Tăng cường Học máy (Algorithms with Predictions)](/discrete-mathematics-for-computer-science-iuh/img/course/learned_algorithms_aug.svg)

Chương 14 đặt ra hai câu hỏi cốt lõi: thuật toán có đúng đắn không và thời gian chạy $$T(n)$$ tăng trưởng như thế nào? Hệ thống AlphaDev (*Nature*, 07/06/2023) giữ nguyên yêu cầu về tính đúng đắn và tối ưu hóa **độ trễ ở mức hệ số hằng** ngay tại tầng hợp ngữ (assembly).

Nhóm nghiên cứu mô hình hóa bài toán “tạo một đoạn mã sắp xếp đúng” thành trò chơi một người chơi, huấn luyện tác nhân học tăng cường (RL) và tìm ra các đoạn mã sắp xếp mới cho dãy cố định 3, 4 và 5 phần tử (cùng các biến thể độ dài thay đổi). Theo báo cáo của DeepMind, các đoạn mã này giúp hàm sắp xếp trong thư viện LLVM libc++ nhanh hơn tới khoảng **70%** đối với dãy ngắn và khoảng **1,7%** đối với dãy dài trên 250.000 phần tử; các đoạn mã `sort3`/`sort4`/`sort5` này đã được tích hợp vào LLVM libc++.

Về mặt tiệm cận, các phép sắp xếp cho số phần tử cố định vẫn có độ phức tạp $$\Theta(1)$$, nên lý thuyết Big-O của chương này không thay đổi. Điểm đáng chú ý của kết quả năm 2023 là phần *cài đặt cụ thể* của một thao tác cơ bản được gọi hàng nghìn tỷ lần mỗi ngày vẫn có thể tối ưu thêm, và tính đúng đắn của đoạn mã mới đã được kiểm chứng tự động trước khi phát hành.

**Câu hỏi.** (1) Vì sao AlphaDev có thể cải thiện tốc độ của `sort3` so với mã do con người viết nhưng không làm thay đổi cận $$\Theta(n\log n)$$ của sắp xếp trộn? (2) Trong các tiêu chí ở Chương 14, “độ trễ không rẽ nhánh trên kiến trúc Skylake” và “hoán vị đúng thứ tự các khóa” lần lượt tương ứng với tiêu chí nào?

### Kiến thức cần nhớ: Học Tăng cường Khám phá Thuật toán Mới (2022–2026)
- **Biến thiết kế thuật toán thành trò chơi:** AlphaTensor (2022) và AlphaDev (2023) mô hình hóa từng phép nhân ma trận hay từng lệnh hợp ngữ CPU như một "nước đi" trong trò chơi cờ vây, dùng Mạng nơ-ron + Tìm kiếm cây Monte Carlo (MCTS) để tìm chuỗi nước đi ngắn nhất nhưng vẫn **đúng 100% trên mọi đầu vào**.
- **Thành tựu thực tế:** Phá kỷ lục 53 năm của Strassen cho nhân ma trận $$4\times 4$$ trên $$\mathbb{F}_2$$ (từ 49 xuống **47** phép nhân) và rút gọn các mạng sắp xếp cỡ nhỏ (`sort3, sort4, sort5`) tích hợp thẳng vào thư viện chuẩn LLVM `libc++`!

### Ví dụ tính tay làm từng bước: Vì sao giảm từ 8 xuống 7 phép nhân ma trận $$2\times 2$$ lại đổi cả bậc tiệm cận?
Với nhân hai ma trận $$n \times n$$ bằng chia để trị thành 4 khối $$\frac{n}{2} \times \frac{n}{2}$$:
- Cách cổ điển (8 phép nhân con): $$T(n) = 8T(n/2) + O(n^2) \implies \Theta(n^{\log_2 8}) = \Theta(n^3)$$.
- Thuật toán Strassen (7 phép nhân con): $$T(n) = 7T(n/2) + O(n^2) \implies \Theta(n^{\log_2 7}) \approx \Theta(n^{2.807})$$!
- Nếu hạ được $$4\times 4$$ từ $$49$$ xuống $$47$$ (AlphaTensor trên $$\mathbb{F}_2$$): số mũ giảm từ $$\log_4 49 \approx 2.807$$ xuống $$\log_4 47 \approx 2.777$$!

### Giải thích: 4 bước kết hợp AI với Lý thuyết Thuật toán Cổ điển
#### Bước 1: Mã hóa bài toán thành không gian trạng thái rời rạc
Với nhân ma trận là tensor bậc 3 (cỡ $$n^2 \times n^2 \times n^2$$); với sắp xếp là trạng thái thanh ghi CPU và tập lệnh hợp ngữ.
#### Bước 2: Dùng Học tăng cường (MCTS) tìm kiếm chuỗi thao tác ngắn hơn con người từng nghĩ ra
AI không bị ràng buộc bởi thói quen thiết kế đối xứng của con người nên phát hiện được những chuỗi lệnh "lạ mắt" nhưng ngắn hơn.
#### Bước 3: Kiểm chứng tính đúng tuyệt đối (Formal Verification)
Mọi thuật toán do AI tìm ra đều phải được kiểm tra 100% bằng đại số tensor hoặc bộ giải SMT/kiểm thử vét cạn trên miền nhỏ trước khi đưa vào thư viện chuẩn.
#### Bước 4: Đánh giá đúng vai trò của Big-O vs. Hằng số thực tế
AlphaDev tối ưu **hằng số** cho kích thước cố định ($$n=3,4,5$$) — vốn được gọi hàng nghìn tỷ lần mỗi ngày ở tầng lá của QuickSort/Introsort — bổ trợ hoàn hảo cho phân tích tiệm cận của Chương 14!

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=Gnx6EgpW6kY">AlphaDev | Daniel Mankowitz and Andrea Michi</a> — ICARL, tiếng Anh. Phần trình bày của hai tác giả Daniel Mankowitz và Andrea Michi về AlphaDev.
- <a href="https://www.youtube.com/watch?v=__vX2sjlpXU">Big-O notation in 5 minutes</a> — Michael Sambol, tiếng Anh. Ôn lại khái niệm Big-O để thấy việc tối ưu hằng số không làm thay đổi bậc tăng trưởng.
