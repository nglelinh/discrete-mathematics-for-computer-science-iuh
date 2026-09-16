---
layout: post
title: "Optional note: Algorithms discovered by RL (2022–2026)"
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

Bài ghi chú ứng dụng song ngữ. **Không** viết lại Big-O, phân tích worst-case, hay bài từ al-Khwarizmi đến quy mô toàn cầu.

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

Chương 14 hỏi thuật toán có đúng không và $$T(n)$$ tăng ra sao. AlphaDev (*Nature*, 07/06/2023) giữ tính đúng và đánh **độ trễ hệ số hằng** ở tầng assembly.

Họ đặt “sinh routine sort đúng” thành trò chơi một người, huấn luyện RL, và ra sort cố định cho 3, 4, 5 phần tử (kèm bản độ dài biến thiên). DeepMind báo cáo libc++ nhanh hơn tới khoảng **70%** trên dãy ngắn và khoảng **1.7%** khi dài hơn 250.000 phần tử. Các routine đã vào LLVM libc++.

Tiệm cận chúng vẫn là sort $$\Theta(1)$$ cho một số khóa cố định; câu chuyện Big-O của khóa học không đổi. Tin 2023 là *cài đặt* của một primitive được gọi hàng nghìn tỷ lần vẫn cải thiện được, và sự cải thiện được kiểm tính đúng trước khi ship.

**Câu hỏi.** (1) Vì sao AlphaDev thắng `sort3` của người mà không thắng $$\Theta(n\log n)$$ của mergesort? (2) Tiêu chí Chương 14 nào là “độ trễ branchless trên Skylake”, tiêu chí nào là “hoán vị khóa đúng”?
