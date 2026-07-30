---
layout: post
title: "Giới thiệu về Thuật toán"
categories: chapter14
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Định nghĩa thuật toán và tính chất; mã giả; tìm kiếm tuần tự và nhị phân; vết chạy; tính đúng đắn sơ bộ."
---

<div class="textbook-epigraph" markdown="1">

"An algorithm must be seen to be believed."

<span class="epigraph-attribution">— Donald Knuth</span>

</div>

**Thuật toán** là dãy bước xác định để giải một lớp bài toán: tìm kiếm, sắp xếp, đường đi, … Mục này định nghĩa khái niệm, các tính chất bắt buộc, cách viết **mã giả**, và hai ví dụ tìm kiếm để chuẩn bị cho phân tích Big-O (14.2–14.3).

![Luồng thuật toán](/discrete-mathematics-for-computer-science-iuh/img/course/Algo_io_pipeline.svg)

<p class="textbook-figure-caption" data-figure="14.1">Thuật toán: đầu vào hợp lệ → hữu hạn bước xác định → đầu ra đúng.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** thuật toán và liệt kê các tính chất cơ bản.
- **Viết** mã giả cho tìm kiếm tuần tự / nhị phân.
- **Vết** (trace) thuật toán trên đầu vào cụ thể.
- **Phân biệt** bài toán tìm kiếm, sắp xếp, tối ưu ở mức khái niệm.
- **Nêu** vì sao một số bài toán không có thuật toán (halting — preview).

**Từ khóa**: algorithm, input/output, pseudocode, correctness, finiteness, definiteness.

</div>

## 1. Định nghĩa và tính chất

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Thuật toán** là dãy **hữu hạn** các chỉ thị **chính xác** để giải một **lớp** bài toán: nhận **đầu vào** từ miền xác định và sinh **đầu ra** sau hữu hạn bước.

</div>

| Tính chất | Ý nghĩa |
|:---|:---|
| **Input** | Nhận giá trị thuộc miền hợp lệ |
| **Output** | Sinh kết quả liên quan bài toán |
| **Definiteness** | Mỗi bước không mơ hồ |
| **Finiteness** | Dừng sau hữu hạn bước |
| **Correctness** | Mọi input hợp lệ → output đúng |
| **Effectiveness** | Mỗi bước thực thi được (cơ bản) |

**Không phải mọi bài toán đều có thuật toán.** *Halting problem* (Turing, 1936): không có thuật toán tổng quát quyết định mọi chương trình có dừng hay không (Ch.18–20).

## 2. Mã giả

Mã giả mô tả thuật toán độc lập ngôn ngữ lập trình: gán, điều kiện, vòng lặp, trả về.

```text
LINEAR-SEARCH(A[1..n], x)
1  for i ← 1 to n do
2      if A[i] = x then return i
3  return 0   // không tìm thấy
```

```text
BINARY-SEARCH(A[1..n], x)   // A tăng dần
1  L ← 1; R ← n
2  while L ≤ R do
3      m ← ⌊(L+R)/2⌋
4      if A[m] = x then return m
5      else if A[m] < x then L ← m+1
6      else R ← m−1
7  return 0
```

![Tìm kiếm nhị phân](/discrete-mathematics-for-computer-science-iuh/img/course/Binary_search_into_array.svg)

<p class="textbook-figure-caption" data-figure="14.2">Binary search: mỗi bước loại một nửa khoảng — cần mảng đã sắp.</p>

## 3. Vết chạy

<div class="textbook-example" markdown="1">

**Ví dụ.** $$A=[2,5,8,12,16]$$, $$x=12$$.

Binary search: $$L=1,R=5$$ → $$m=3$$ ($$A[3]=8<12$$) → $$L=4$$ → $$m=4$$ ($$A[4]=12$$) → trả về 4.

Linear search: so $$2,5,8,12$$ — 4 lần so sánh.

</div>

## 4. Lớp bài toán thường gặp

| Lớp | Câu hỏi |
|:---|:---|
| **Tìm kiếm** | Phần tử / khóa có trong cấu trúc? |
| **Sắp xếp** | Hoán vị theo thứ tự |
| **Tối ưu** | Cấu hình min/max chi phí (có thể khó — Ch.20) |
| **Quyết định** | Có/Không (nền P/NP) |

## 5. Thử nghiệm tương tác

<div class="interactive-demo" markdown="1">
<div data-demo="algorithm-visualization"></div>
</div>
<script src="{{ '/public/js/algorithm-visualization.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Liệt kê 4 tính chất thuật toán và giải thích ngắn “finiteness”.

<details>
<summary>Đáp án</summary>

Ví dụ: input, output, definiteness, finiteness, correctness, effectiveness. Finiteness: sau hữu hạn bước phải dừng (không loop vô hạn trên input hợp lệ khi yêu cầu thuật toán tổng quát).

</details>

### Bài tập 2

Trace BINARY-SEARCH trên $$[1,3,4,7,9]$$, $$x=3$$.

<details>
<summary>Đáp án</summary>

$$m=3$$ ($$4>3$$) → $$R=2$$; $$m=1$$ ($$1<3$$) → $$L=2$$; $$m=2$$ ($$3$$) → trả về 2.

</details>

### Bài tập 3

Vì sao binary search cần mảng tăng?

<details>
<summary>Đáp án</summary>

Quyết định bỏ nửa trái/phải dựa trên so sánh với phần tử giữa — chỉ đúng khi thứ tự toàn cục được bảo đảm.

</details>

## Tóm tắt

1. Thuật toán = quy trình hữu hạn, xác định, đúng.
2. Mã giả độc lập ngôn ngữ.
3. Linear vs binary search — nền so sánh hiệu năng.
4. Một số bài toán không có thuật toán tổng quát.

Trong bài tiếp theo: **Big-O** và bậc tăng trưởng.
