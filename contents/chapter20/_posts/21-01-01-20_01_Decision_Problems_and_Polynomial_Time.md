---
layout: post
title: "Bài toán Quyết định và Thời gian Đa thức"
categories: chapter20
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Mô hình hóa bài toán quyết định dưới dạng ngôn ngữ hình thức, mã hóa đầu vào, định nghĩa TIME(t(n)), lớp P và luận đề Cobham–Edmonds."
---

<div class="textbook-epigraph" markdown="1">

"Complexity theory begins when we stop timing one program and start classifying whole families of problems."

<span class="epigraph-attribution">— Tinh thần lý thuyết độ phức tạp</span>

</div>

Để nghiên cứu một cách chặt chẽ “bài toán nào khó”, ta cần một **khung chuẩn hóa**: mọi thể hiện đầu vào được biểu diễn thành chuỗi bit, mọi câu hỏi quy về dạng **Có/Không (Yes/No)** và chi phí được đo bằng **số bước tính toán theo độ dài đầu vào**. Bài học này thiết lập khung đó làm nền tảng cho toàn bộ Chương 20.

![Đa thức vs mũ](/discrete-mathematics-for-computer-science-iuh/img/course/Algo_big_o_ladder.svg)

<p class="textbook-figure-caption" data-figure="20.1">Thời gian đa thức còn khả thi khi $$n$$ lớn, còn thời gian mũ hay giai thừa thì không — ranh giới kinh điển của lớp $$P$$.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Mã hóa** các đối tượng rời rạc thành chuỗi bit $$x\in\{0,1\}^*$$.
- **Phát biểu** bài toán quyết định dưới dạng một ngôn ngữ hình thức $$L$$.
- **Định nghĩa** lớp thời gian $$\mathrm{TIME}(t(n))$$ và lớp $$P$$.
- **Giải thích** vì sao khái niệm “thời gian đa thức” ổn định trên các mô hình máy tính chuẩn.

</div>

## Từ bài toán thực tế đến chuỗi bit

Mọi đối tượng rời rạc như đồ thị, công thức logic hay số nguyên đều có thể **mã hóa** thành chuỗi hữu hạn. Độ dài đầu vào $$n=\lvert x\rvert$$ (tính theo số bit) mới là tham số chính thức của độ phức tạp — không phải “số đỉnh”, trừ khi đã cố định một cách mã hóa hợp lý (ví dụ ma trận kề có kích thước $$n=\Theta(v^2)$$).

**Quy ước nghiên cứu:** cách mã hóa phải *hợp lý* (*reasonable*), chẳng hạn biểu diễn số ở hệ cơ số $$\ge 2$$ và không chèn đệm độ dài hàm mũ một cách vô cớ (xem Garey–Johnson, Arora–Barak).

## Bài toán quyết định và ngôn ngữ

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Một **bài toán quyết định** tương ứng với một ngôn ngữ $$L\subseteq\{0,1\}^*$$: đầu vào $$x$$ có câu trả lời Có (Yes) khi và chỉ khi $$x\in L$$.

Một bài toán tối ưu dạng “tìm $$\min c(y)$$” luôn có thể chuyển về bài toán quyết định bằng cách thêm ngưỡng $$K$$: “tồn tại $$y$$ sao cho $$c(y)\le K$$ hay không?”.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ.** Phiên bản quyết định TSP-DEC nhận bộ $$(G,w,K)$$ và trả lời Có khi và chỉ khi tồn tại một hành trình Hamilton có tổng độ dài $$\le K$$.

</div>

## Lớp thời gian và lớp $$P$$

<div class="textbook-definition" markdown="1">

**Định nghĩa.**

$$
\mathrm{TIME}(t(n))
=
\{L:\exists\text{ máy Turing đơn định quyết định }L\text{ trong }\le t(\lvert x\rvert)\text{ bước}\}.
$$

$$
P=\bigcup_{k\ge 1}\mathrm{TIME}(n^k).
$$

</div>

**Luận đề Cobham–Edmonds (ý chính):** các mô hình máy tính tuần tự “hợp lý” (như máy Turing nhiều băng, máy RAM) đều có thể mô phỏng lẫn nhau với chi phí phụ chỉ ở mức đa thức, do đó định nghĩa lớp $$P$$ là ổn định và không phụ thuộc chi tiết cài đặt máy.

## Đa thức so với hàm mũ

| Họ hàm | Ví dụ | Khi $$n=40$$ |
|:---|:---|:---|
| Đa thức | $$n^2$$, $$n^3\log n$$ | Thường khả thi (tùy hằng số) |
| Hàm mũ / giai thừa | $$2^n$$, $$n!$$ | Thường không khả thi |

Lớp $$P$$ chỉ khẳng định *sự tồn tại* của một thuật toán thời gian đa thức: một thuật toán chạy trong $$n^{100}$$ vẫn thuộc $$P$$ về mặt lý thuyết nhưng không dùng được trong thực tế. Vì vậy nghiên cứu thuật toán vừa cần phân loại lý thuyết vừa cần giảm số mũ thực tế.

## Bài tập

1. Nếu mã hóa một đồ thị vô hướng $$n$$ đỉnh bằng ma trận kề thì độ dài mã hóa $$\lvert x\rvert$$ là bao nhiêu?
2. Viết phiên bản bài toán quyết định tương ứng với bài toán “tìm tập độc lập lớn nhất” (*maximum independent set*).
3. Giải thích vì sao việc đệm thêm chuỗi $$1^{2^n}$$ vào đầu vào lại phá vỡ tính “hợp lý” của phép mã hóa.

<details>
<summary>Gợi ý</summary>

1. $$\Theta(n^2)$$ bit.  
2. Cho cặp $$(G,k)$$: hỏi có tồn tại tập độc lập kích thước $$\ge k$$ hay không.  
3. Việc đệm độ dài hàm mũ biến một thể hiện ngắn thành đầu vào dài cấp số mũ, làm sai lệch hoàn toàn thước đo độ phức tạp theo độ dài bit.

</details>

## Tài liệu đọc thêm

Sipser (phần mở đầu về độ phức tạp); Arora–Barak §1; Garey–Johnson §1–2.

## Tóm tắt

Bài toán quyết định được biểu diễn như ngôn ngữ hình thức trên chuỗi bit, còn lớp $$P=\bigcup_{k\ge 1}\mathrm{TIME}(n^k)$$ đại diện cho các bài toán giải được trong thời gian đa thức.

**Bài tiếp theo:** 20.2 — Lớp $$P$$ và Định lý phân cấp thời gian (*Time Hierarchy*).

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=YX40hbAHx3s">P vs. NP and the Computational Complexity Zoo</a> — hackerdashery, tiếng Anh. Giới thiệu trực quan về bài toán quyết định và các lớp độ phức tạp thời gian.
- <a href="https://www.youtube.com/watch?v=__vX2sjlpXU">Big-O notation in 5 minutes</a> — Michael Sambol, tiếng Anh. Ôn lại tăng trưởng đa thức và các bậc lớn hơn theo độ dài đầu vào.
- <a href="https://www.youtube.com/watch?v=uAdVzz1hKYY">Boolean Satisfiability Problem - Intro to Theoretical Computer Science</a> — Udacity, tiếng Anh. SAT dưới dạng bài toán quyết định Có/Không.
