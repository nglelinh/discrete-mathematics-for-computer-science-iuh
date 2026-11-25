---
layout: post
title: "Ghi chú mở rộng: Thuật toán do học tăng cường tìm ra (2022–2026)"
categories: chapter14
date: 2021-01-01
order: 5
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. AlphaDev (Nature 2023) found faster sort3/4/5 assembly now in LLVM libc++. Does not replace Big-O theory."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite Big-O, worst-case analysis, or the historical algorithms lesson.

Bài ghi chú ứng dụng song ngữ, **không** viết lại phần lý thuyết Big-O, phân tích trường hợp xấu nhất hay bài khảo sát từ Al-Khwarizmi đến quy mô toàn cầu.

</div>

## English

Chapter 14 asks whether an algorithm is correct and how $$T(n)$$ grows. AlphaDev (Mankowitz et al., “Faster sorting algorithms discovered using deep reinforcement learning,” *Nature* 618:257–263, 7 June 2023, [DOI 10.1038/s41586-023-06004-9](https://doi.org/10.1038/s41586-023-06004-9)) keeps correctness and attacks **constant-factor latency** at the assembly level.

They formulate “emit a correct sort routine” as a single-player game, train an RL agent, and obtain new fixed sorts for 3, 4 and 5 elements (plus variable-length variants). DeepMind’s companion note reports up to about **70%** faster libc++ sorting on short sequences and about **1.7%** on sequences longer than 250,000 elements. The routines landed in LLVM libc++ (`sort3`/`sort4`/`sort5` branchless paths; see the [llvm-project commit](https://github.com/llvm/llvm-project/commit/194d1965d2c841fa81e107d19e27fae1467e7f11)).

Asymptotically these are still $$\Theta(1)$$ sorts of a constant number of keys; the course’s Big-O story does not change. The 2023 news is that the *implementation* of a primitive called trillions of times was still improvable, and that improvement was machine-checked for functional correctness before it shipped.

**Citations**

1. D. J. Mankowitz et al., “Faster sorting algorithms discovered using deep reinforcement learning,” *Nature* 618 (2023). [DOI](https://doi.org/10.1038/s41586-023-06004-9)
2. DeepMind, “AlphaDev discovers faster sorting algorithms,” 7 June 2023. [Blog](https://deepmind.google/blog/alphadev-discovers-faster-sorting-algorithms/)

**Questions.** (1) Why can AlphaDev beat a human `sort3` without beating mergesort’s $$\Theta(n\log n)$$? (2) Which Chapter 14 criterion is “branchless latency on Skylake,” and which is “permutes keys correctly”?

### Background Knowledge Map: Reinforcement Learning Meets Classic Algorithms
- **Algorithm Discovery as a Game (AlphaTensor 2022, AlphaDev 2023):** Represent choosing the next elementary operation (a bilinear rank-1 matrix step or a CPU assembly instruction) as a move in a single-player game, scored by correctness + latency/operation count.
- **Concrete Breakthroughs:** AlphaTensor lowered $$4\times 4$$ matrix multiplication over $$\mathbb{F}_2$$ from Strassen’s 49 multiplications (1969) to **47**; AlphaDev trimmed 1–2 assembly instructions off fixed-length sorting networks (`sort3`, `sort4`, `sort5`) merged into LLVM `libc++`!

### Deep-Dive Explanation: Why Strassen’s $$7$$ Multiplications Beats $$8$$ (Read Slowly)
1. **Step 1 (Base Case $$2\times 2$$):** Standard schoolbook $$2\times 2$$ matrix multiplication uses **8** scalar multiplications ($$O(n^3)$$ recursively).
2. **Step 2 (Strassen 1969):** Uses **7** clever bilinear products, dropping recursive complexity to $$O(n^{\log_2 7}) \approx O(n^{2.807})$$!
3. **Step 3 (AlphaTensor 2022):** Framed $$4\times 4$$ multiplication as decomposing a 3D tensor into rank-1 outer products, discovering a **47-product** scheme over $$\mathbb{F}_2$$ (beating $$7^2 = 49$$!).
4. **Step 4 (Caveat):** RL optimizes small fixed sizes and constants brilliantly, while proving asymptotic optimality still relies on mathematical analysis!

## Tiếng Việt

Chương 14 đặt ra hai câu hỏi cốt lõi: thuật toán có đúng đắn không và thời gian chạy $$T(n)$$ tăng trưởng như thế nào? Hệ thống AlphaDev (*Nature*, 07/06/2023) giữ nguyên yêu cầu về tính đúng đắn và tối ưu hóa **độ trễ ở mức hệ số hằng** ngay tại tầng hợp ngữ (assembly).

Nhóm nghiên cứu mô hình hóa bài toán “tạo một đoạn mã sắp xếp đúng” thành trò chơi một người chơi, huấn luyện tác nhân học tăng cường (RL) và tìm ra các đoạn mã sắp xếp mới cho dãy cố định 3, 4 và 5 phần tử (cùng các biến thể độ dài thay đổi). Theo báo cáo của DeepMind, các đoạn mã này giúp hàm sắp xếp trong thư viện LLVM libc++ nhanh hơn tới khoảng **70%** đối với dãy ngắn và khoảng **1,7%** đối với dãy dài trên 250.000 phần tử; các đoạn mã `sort3`/`sort4`/`sort5` này đã được tích hợp vào LLVM libc++.

Về mặt tiệm cận, các phép sắp xếp cho số phần tử cố định vẫn có độ phức tạp $$\Theta(1)$$, nên lý thuyết Big-O của chương này không thay đổi. Điểm đáng chú ý của kết quả năm 2023 là phần *cài đặt cụ thể* của một thao tác cơ bản được gọi hàng nghìn tỷ lần mỗi ngày vẫn có thể tối ưu thêm, và tính đúng đắn của đoạn mã mới đã được kiểm chứng tự động trước khi phát hành.

**Câu hỏi.** (1) Vì sao AlphaDev có thể cải thiện tốc độ của `sort3` so với mã do con người viết nhưng không làm thay đổi cận $$\Theta(n\log n)$$ của sắp xếp trộn? (2) Trong các tiêu chí ở Chương 14, “độ trễ không rẽ nhánh trên kiến trúc Skylake” và “hoán vị đúng thứ tự các khóa” lần lượt tương ứng với tiêu chí nào?

### Bản đồ kiến thức nền: Học Tăng cường Khám phá Thuật toán Mới (2022–2026)
- **Biến thiết kế thuật toán thành trò chơi:** AlphaTensor (2022) và AlphaDev (2023) mô hình hóa từng phép nhân ma trận hay từng lệnh hợp ngữ CPU như một "nước đi" trong trò chơi cờ vây, dùng Mạng nơ-ron + Tìm kiếm cây Monte Carlo (MCTS) để tìm chuỗi nước đi ngắn nhất nhưng vẫn **đúng 100% trên mọi đầu vào**.
- **Thành tựu thực tế:** Phá kỷ lục 53 năm của Strassen cho nhân ma trận $$4\times 4$$ trên $$\mathbb{F}_2$$ (từ 49 xuống **47** phép nhân) và rút gọn các mạng sắp xếp cỡ nhỏ (`sort3, sort4, sort5`) tích hợp thẳng vào thư viện chuẩn LLVM `libc++`!

### Ví dụ tính tay cầm tay chỉ việc: Vì sao giảm từ 8 xuống 7 phép nhân ma trận $$2\times 2$$ lại đổi cả bậc tiệm cận?
Với nhân hai ma trận $$n \times n$$ bằng chia để trị thành 4 khối $$\frac{n}{2} \times \frac{n}{2}$$:
- Cách cổ điển (8 phép nhân con): $$T(n) = 8T(n/2) + O(n^2) \implies \Theta(n^{\log_2 8}) = \Theta(n^3)$$.
- Thuật toán Strassen (7 phép nhân con): $$T(n) = 7T(n/2) + O(n^2) \implies \Theta(n^{\log_2 7}) \approx \Theta(n^{2.807})$$!
- Nếu hạ được $$4\times 4$$ từ $$49$$ xuống $$47$$ (AlphaTensor trên $$\mathbb{F}_2$$): số mũ giảm từ $$\log_4 49 \approx 2.807$$ xuống $$\log_4 47 \approx 2.777$$!

### Khung giải thích: 4 bước kết hợp AI với Lý thuyết Thuật toán Cổ điển (nên đọc chậm)
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
