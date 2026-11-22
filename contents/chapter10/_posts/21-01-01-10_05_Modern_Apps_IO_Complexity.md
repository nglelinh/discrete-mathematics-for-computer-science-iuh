---
layout: post
title: "Ghi chú mở rộng: Hệ thức truy hồi cho thuật toán tính đến IO (2022–2026)"
categories: chapter10
date: 2021-01-01
order: 5
required: false
lesson_type: optional
lang: vi
excerpt: "Bài đọc mở rộng song ngữ về FlashAttention (NeurIPS 2022) — minh họa cách phân tích độ phức tạp IO bằng kỹ thuật chia khối (tiling) theo tư duy truy hồi chia để trị."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** This is a bilingual application note (English followed by Vietnamese). It extends the algorithms and systems discussion rather than rewriting linear recurrence theory, and is tagged `lang: vi` to stay grouped with this chapter’s main posts.

Đây là bài đọc ứng dụng mở rộng dạng song ngữ (không thay thế phần lý thuyết truy hồi tuyến tính). Bài được gắn nhãn `lang: vi` để hiển thị cùng nhóm bài lý thuyết của Chương 10.

</div>

## English

Throughout Chapter 10, divide-and-conquer recurrences of the form $$T(n) = a\,T(n/b) + f(n)$$ serve as our main lens for analyzing algorithms. **FlashAttention** (Dao et al., NeurIPS 2022, [arXiv:2205.14135](https://arxiv.org/abs/2205.14135)) illustrates a modern twist on this idea: on GPU hardware, the decisive bottleneck is often not arithmetic operations (FLOPs), but **IO** — reading and writing data between high-bandwidth memory (HBM) and fast on-chip SRAM.

Rather than materializing the full $$n \times n$$ attention matrix in HBM, FlashAttention splits it into tiles that fit inside SRAM and recomputes softmax normalization statistics during the backward pass. By analyzing IO complexity directly, the authors prove that their tiling scheme is IO-optimal across a broad range of SRAM capacities. Empirically, it delivers roughly a $$3\times$$ wall-clock speedup on GPT-2 (sequence length 1K) and achieves the first better-than-chance performance on Path-X (sequence length 16K) among the Transformer baselines evaluated.

From the perspective of Chapter 10, tiling can be viewed as a recurrence over block sizes: each block forms a self-contained subproblem, followed by a linear merge that updates running softmax statistics ($$m$$ and $$\ell$$) for numerical stability. The core recurrence framework remains the same — only the cost model shifts from counting arithmetic steps to counting *memory traffic*, which dominates real wall-clock runtime on modern GPUs.

**Citations**

1. T. Dao et al., “FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness,” NeurIPS 2022. [DOI/proceedings](https://proceedings.neurips.cc/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html)

**Discussion Questions**

1. Write a schematic recurrence for processing $$n$$ tokens in blocks of size $$B$$.
2. If HBM memory transfers are the primary bottleneck rather than arithmetic, what does the non-recursive term $$f(n)$$ represent?

## Tiếng Việt

Xuyên suốt Chương 10, quan hệ truy hồi chia để trị dạng $$T(n) = a\,T(n/b) + f(n)$$ là công cụ chủ đạo để phân tích chi phí thuật toán. **FlashAttention** (Dao et al., NeurIPS 2022, [arXiv:2205.14135](https://arxiv.org/abs/2205.14135)) cho thấy một góc nhìn hiện đại của tư duy này: trên phần cứng GPU, điểm nghẽn quyết định thường không nằm ở số phép tính số học (FLOPs) mà ở chi phí **truy xuất bộ nhớ (IO)** — tức lượng dữ liệu phải đọc và ghi qua lại giữa bộ nhớ HBM của GPU và bộ nhớ đệm SRAM trên chip.

Thay vì lưu toàn bộ ma trận attention kích thước $$n \times n$$ trên HBM, FlashAttention áp dụng kỹ thuật **chia khối (tiling)** để đưa từng khối nhỏ vừa đủ vào SRAM, đồng thời tính lại các thống kê softmax trong pha lan truyền ngược (backward pass). Khi phân tích trực tiếp độ phức tạp IO, nhóm tác giả chứng minh thuật toán đạt mức tối ưu về lưu lượng bộ nhớ trên một dải rộng các dung lượng SRAM. Về mặt thực nghiệm, FlashAttention giúp tăng tốc khoảng $$3\times$$ thời gian chạy thực tế trên GPT-2 (độ dài chuỗi 1K) và trở thành mô hình đầu tiên trong nhóm Transformer so sánh đạt kết quả vượt mức đoán ngẫu nhiên trên bài toán Path-X (độ dài chuỗi 16K).

Đặt trong bối cảnh Chương 10, kỹ thuật chia khối có thể hiểu như một hệ thức truy hồi theo kích thước khối: mỗi khối dữ liệu là một bài toán con độc lập, kết hợp với bước gộp tuyến tính để cập nhật liên tục các đại lượng thống kê $$m$$ và $$\ell$$ (nhằm đảm bảo tính ổn định số học của hàm softmax). Khung tư duy truy hồi vẫn không đổi; điểm khác biệt duy nhất là đại lượng chi phí lúc này đo lường *lưu lượng trao đổi bộ nhớ* — yếu tố chi phối trực tiếp thời gian thực thi thực tế (wall-clock time) trên GPU.

**Câu hỏi thảo luận**

1. Hãy viết dạng hệ thức truy hồi phác thảo cho quá trình xử lý $$n$$ token theo từng khối có kích thước $$B$$.
2. Khi nút thắt cổ chai nằm ở việc truyền dữ liệu với HBM thay vì phép tính số học, thành phần $$f(n)$$ trong hệ thức truy hồi biểu diễn chi phí gì?

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=LKwyHWYEIMQ">FlashAttention: Accelerate LLM training</a> — Machine Learning Studio (tiếng Anh). Giới thiệu trực quan cách FlashAttention giữ nguyên kết quả phép tính attention nhưng tối ưu hoàn toàn mô hình truy cập bộ nhớ.
- <a href="https://www.youtube.com/watch?v=OynWkEj0S-s">2.4.1 Masters Theorem in Algorithms for Dividing Function #1</a> — Abdul Bari (tiếng Anh). Nền tảng về truy hồi chia để trị, cùng tư duy phân tích với kỹ thuật chia khối trong bài.
- <a href="https://www.youtube.com/watch?v=FThvfkXWqtE">MedAI #54: FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness | Tri Dao</a> — Stanford MedAI (tiếng Anh). Chính tác giả Tri Dao giải thích cơ chế nhận thức IO (IO-awareness) trong FlashAttention.
