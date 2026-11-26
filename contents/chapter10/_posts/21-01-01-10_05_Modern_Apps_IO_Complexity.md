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

**Tùy chọn.** Bài ghi chú ứng dụng mở rộng (tiếng Việt). **Không** thay thế các bài học nền tảng trong chương.

</div>

![Phân cấp Bộ nhớ và Độ phức tạp I/O (Cache-Oblivious)](/discrete-mathematics-for-computer-science-iuh/img/course/io_complexity_hierarchy.svg)

Xuyên suốt Chương 10, quan hệ truy hồi chia để trị dạng $$T(n) = a\,T(n/b) + f(n)$$ là công cụ chủ đạo để phân tích chi phí thuật toán. **FlashAttention** (Dao et al., NeurIPS 2022, [arXiv:2205.14135](https://arxiv.org/abs/2205.14135)) cho thấy một góc nhìn hiện đại của tư duy này: trên phần cứng GPU, điểm nghẽn quyết định thường không nằm ở số phép tính số học (FLOPs) mà ở chi phí **truy xuất bộ nhớ (IO)** — tức lượng dữ liệu phải đọc và ghi qua lại giữa bộ nhớ HBM của GPU và bộ nhớ đệm SRAM trên chip.

Thay vì lưu toàn bộ ma trận attention kích thước $$n \times n$$ trên HBM, FlashAttention áp dụng kỹ thuật **chia khối (tiling)** để đưa từng khối nhỏ vừa đủ vào SRAM, đồng thời tính lại các thống kê softmax trong pha lan truyền ngược (backward pass). Khi phân tích trực tiếp độ phức tạp IO, nhóm tác giả chứng minh thuật toán đạt mức tối ưu về lưu lượng bộ nhớ trên một dải rộng các dung lượng SRAM. Về mặt thực nghiệm, FlashAttention giúp tăng tốc khoảng $$3\times$$ thời gian chạy thực tế trên GPT-2 (độ dài chuỗi 1K) và trở thành mô hình đầu tiên trong nhóm Transformer so sánh đạt kết quả vượt mức đoán ngẫu nhiên trên bài toán Path-X (độ dài chuỗi 16K).

Đặt trong bối cảnh Chương 10, kỹ thuật chia khối có thể hiểu như một hệ thức truy hồi theo kích thước khối: mỗi khối dữ liệu là một bài toán con độc lập, kết hợp với bước gộp tuyến tính để cập nhật liên tục các đại lượng thống kê $$m$$ và $$\ell$$ (nhằm đảm bảo tính ổn định số học của hàm softmax). Khung tư duy truy hồi vẫn không đổi; điểm khác biệt duy nhất là đại lượng chi phí lúc này đo lường *lưu lượng trao đổi bộ nhớ* — yếu tố chi phối trực tiếp thời gian thực thi thực tế (wall-clock time) trên GPU.

**Câu hỏi thảo luận**

1. Hãy viết dạng hệ thức truy hồi phác thảo cho quá trình xử lý $$n$$ token theo từng khối có kích thước $$B$$.
2. Khi nút thắt cổ chai nằm ở việc truyền dữ liệu với HBM thay vì phép tính số học, thành phần $$f(n)$$ trong hệ thức truy hồi biểu diễn chi phí gì?

### Kiến thức cần nhớ: Truy hồi nhận thức IO tái định hình thuật toán GPU ra sao?

- **Phân cấp bộ nhớ (Memory Hierarchy):** Trên GPU hiện đại, SRAM trên chip rất nhỏ (~20 MB) nhưng nhanh hơn HBM hàng chục lần. Chỉ đếm số phép nhân–cộng (FLOPs) sẽ bỏ sót nút thắt cổ chai thực sự: **lưu lượng byte đọc/ghi giữa HBM và SRAM**.
- **Chia khối như hệ thức truy hồi (Block Tiling Recurrence):** Chia ma trận $$N \times d$$ thành các khối nhỏ vừa khít SRAM giúp loại bỏ việc ghi ma trận trung gian $$N \times N$$ ra HBM.
- **Gộp Softmax trực tuyến (Online Softmax Merging):** Thay vì duyệt hai lượt trên HBM, FlashAttention cập nhật truy hồi hai thống kê chạy là giá trị lớn nhất theo hàng $$m$$ và tổng chuẩn hóa $$\ell$$ qua từng khối, đảm bảo kết quả **chính xác tuyệt đối** như phép tính chuẩn.

### Giải thích: Tính tay mức giảm lưu lượng HBM của FlashAttention
1. **Bước 1 — Lưu lượng HBM của Attention chuẩn:** Với độ dài chuỗi $$N = 4\,096$$ và chiều ẩn $$d = 64$$, việc lưu ma trận điểm $$S = QK^\top$$ và $$P = \text{softmax}(S)$$ kích thước $$N \times N$$ tốn lưu lượng HBM tỷ lệ $$\Theta(N^2)$$ (khoảng $$16{,}78$$ triệu phần tử cho mỗi ma trận trung gian).
2. **Bước 2 — Lưu lượng HBM khi chia khối SRAM:** Với dung lượng SRAM làm việc $$M = 65\,536$$ phần tử, tổng truy xuất HBM của FlashAttention giảm còn $$\Theta\!\left(\frac{N^2 d^2}{M}\right)$$. Thay $$d = 64 \Rightarrow d^2 = 4\,096$$, ta có $$\frac{d^2}{M} = \frac{4\,096}{65\,536} = \frac{1}{16}$$ — tức lưu lượng HBM giảm ngay **16 lần**!
3. **Bước 3 — Công thức gộp truy hồi theo khối:** Khi gộp khối 1 có $$(m_1, \ell_1)$$ với khối 2 có $$(m_2, \ell_2)$$, ta cập nhật $$m_{\text{mới}} = \max(m_1, m_2)$$ và $$\ell_{\text{mới}} = e^{m_1 - m_{\text{mới}}}\ell_1 + e^{m_2 - m_{\text{mới}}}\ell_2$$ — tư duy gộp nghiệm con quen thuộc của Chương 10, nhưng tối ưu thẳng vào chi phí bộ nhớ!

$$\text{IO chuẩn: } \Theta(Nd + N^2) \;\xrightarrow{\text{Chia khối SRAM } M}\; \text{FlashAttention IO: } \Theta\!\left(\frac{N^2 d^2}{M}\right).$$

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=LKwyHWYEIMQ">FlashAttention: Accelerate LLM training</a> — Machine Learning Studio (tiếng Anh). Giới thiệu trực quan cách FlashAttention giữ nguyên kết quả phép tính attention nhưng tối ưu hoàn toàn mô hình truy cập bộ nhớ.
- <a href="https://www.youtube.com/watch?v=OynWkEj0S-s">2.4.1 Masters Theorem in Algorithms for Dividing Function #1</a> — Abdul Bari (tiếng Anh). Nền tảng về truy hồi chia để trị, cùng tư duy phân tích với kỹ thuật chia khối trong bài.
- <a href="https://www.youtube.com/watch?v=FThvfkXWqtE">MedAI #54: FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness | Tri Dao</a> — Stanford MedAI (tiếng Anh). Chính tác giả Tri Dao giải thích cơ chế nhận thức IO (IO-awareness) trong FlashAttention.
