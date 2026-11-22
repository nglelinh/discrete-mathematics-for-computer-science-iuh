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

## Tiếng Việt

Chương 14 đặt ra hai câu hỏi cốt lõi: thuật toán có đúng đắn không và thời gian chạy $$T(n)$$ tăng trưởng như thế nào? Hệ thống AlphaDev (*Nature*, 07/06/2023) giữ nguyên yêu cầu về tính đúng đắn và tối ưu hóa **độ trễ ở mức hệ số hằng** ngay tại tầng hợp ngữ (assembly).

Nhóm nghiên cứu mô hình hóa bài toán “tạo một đoạn mã sắp xếp đúng” thành trò chơi một người chơi, huấn luyện tác nhân học tăng cường (RL) và tìm ra các đoạn mã sắp xếp mới cho dãy cố định 3, 4 và 5 phần tử (cùng các biến thể độ dài thay đổi). Theo báo cáo của DeepMind, các đoạn mã này giúp hàm sắp xếp trong thư viện LLVM libc++ nhanh hơn tới khoảng **70%** đối với dãy ngắn và khoảng **1,7%** đối với dãy dài trên 250.000 phần tử; các đoạn mã `sort3`/`sort4`/`sort5` này đã được tích hợp vào LLVM libc++.

Về mặt tiệm cận, các phép sắp xếp cho số phần tử cố định vẫn có độ phức tạp $$\Theta(1)$$, nên lý thuyết Big-O của chương này không thay đổi. Điểm đáng chú ý của kết quả năm 2023 là phần *cài đặt cụ thể* của một thao tác cơ bản được gọi hàng nghìn tỷ lần mỗi ngày vẫn có thể tối ưu thêm, và tính đúng đắn của đoạn mã mới đã được kiểm chứng tự động trước khi phát hành.

**Câu hỏi.** (1) Vì sao AlphaDev có thể cải thiện tốc độ của `sort3` so với mã do con người viết nhưng không làm thay đổi cận $$\Theta(n\log n)$$ của sắp xếp trộn? (2) Trong các tiêu chí ở Chương 14, “độ trễ không rẽ nhánh trên kiến trúc Skylake” và “hoán vị đúng thứ tự các khóa” lần lượt tương ứng với tiêu chí nào?

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=Gnx6EgpW6kY">AlphaDev | Daniel Mankowitz and Andrea Michi</a> — ICARL, tiếng Anh. Phần trình bày của hai tác giả Daniel Mankowitz và Andrea Michi về AlphaDev.
- <a href="https://www.youtube.com/watch?v=__vX2sjlpXU">Big-O notation in 5 minutes</a> — Michael Sambol, tiếng Anh. Ôn lại khái niệm Big-O để thấy việc tối ưu hằng số không làm thay đổi bậc tăng trưởng.
