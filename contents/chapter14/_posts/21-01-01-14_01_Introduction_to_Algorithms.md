---
layout: post
title: "Giới thiệu về Thuật toán"
categories: chapter14
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Định nghĩa thuật toán và các tính chất bắt buộc, cách viết mã giả, tìm kiếm tuần tự và tìm kiếm nhị phân, vết chạy (trace) và khái niệm tính đúng đắn."
---

<div class="textbook-epigraph" markdown="1">

"An algorithm must be seen to be believed."

<span class="epigraph-attribution">— Donald Knuth</span>

</div>

**Thuật toán** là một dãy bước xác định nhằm giải quyết một lớp bài toán cụ thể như tìm kiếm, sắp xếp hay tìm đường đi. Bài học này trình bày định nghĩa, các tính chất bắt buộc của thuật toán, cách biểu diễn bằng **mã giả** và hai ví dụ tìm kiếm kinh điển làm cơ sở cho việc phân tích độ phức tạp bằng Big-O ở Mục 14.2–14.3.

![Luồng thuật toán](/discrete-mathematics-for-computer-science-iuh/img/course/Algo_io_pipeline.svg)

<p class="textbook-figure-caption" data-figure="14.1">Quy trình của một thuật toán: nhận đầu vào hợp lệ, thực hiện hữu hạn bước xác định và trả về đầu ra đúng.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** thuật toán và liệt kê các tính chất cơ bản của một thuật toán.
- **Viết** mã giả cho thuật toán tìm kiếm tuần tự và tìm kiếm nhị phân.
- **Theo dõi vết chạy** (*trace*) của thuật toán trên một bộ dữ liệu đầu vào cụ thể.
- **Phân biệt** các lớp bài toán tìm kiếm, sắp xếp, tối ưu và quyết định ở mức khái niệm.
- **Giải thích** sơ lược vì sao tồn tại những bài toán không có thuật toán tổng quát (như bài toán dừng — *halting problem*).

**Từ khóa**: algorithm, input/output, pseudocode, correctness, finiteness, definiteness.

</div>

## Định nghĩa và tính chất

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Thuật toán** là một dãy **hữu hạn** các chỉ thị **chính xác** nhằm giải một **lớp** bài toán: thuật toán nhận **đầu vào** thuộc miền xác định và sinh ra **đầu ra** đúng sau một số hữu hạn bước.

</div>

| Tính chất | Ý nghĩa |
|:---|:---|
| **Đầu vào (Input)** | Nhận các giá trị thuộc miền dữ liệu hợp lệ |
| **Đầu ra (Output)** | Sinh ra kết quả tương ứng với yêu cầu bài toán |
| **Tính xác định (Definiteness)** | Mỗi bước đều rõ ràng, không mơ hồ |
| **Tính dừng (Finiteness)** | Kết thúc sau một số hữu hạn bước |
| **Tính đúng đắn (Correctness)** | Với mọi đầu vào hợp lệ, luôn trả về đầu ra chính xác |
| **Tính khả thi (Effectiveness)** | Mỗi bước đều là thao tác cơ bản có thể thực thi được |

**Không phải mọi bài toán đều có thuật toán.** Bài toán dừng (*Halting problem*, Alan Turing, 1936) chứng minh rằng không tồn tại thuật toán tổng quát nào có thể quyết định liệu một chương trình bất kỳ có dừng hay chạy vô hạn (xem Chương 18–20).

## Mã giả

Mã giả (*pseudocode*) mô tả thuật toán độc lập với ngôn ngữ lập trình cụ thể, sử dụng các cấu trúc cơ bản như phép gán, rẽ nhánh điều kiện, vòng lặp và lệnh trả về.

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

<p class="textbook-figure-caption" data-figure="14.2">Tìm kiếm nhị phân loại bỏ một nửa khoảng tìm kiếm sau mỗi bước so sánh, với điều kiện mảng đã được sắp xếp.</p>

## Vết chạy (Trace)

<div class="textbook-example" markdown="1">

**Ví dụ.** Cho mảng $$A=[2,5,8,12,16]$$ và giá trị cần tìm $$x=12$$.

- **Tìm kiếm nhị phân**: khởi đầu $$L=1, R=5$$ → $$m=3$$ ($$A[3]=8<12$$) → cập nhật $$L=4$$ → $$m=4$$ ($$A[4]=12$$) → trả về vị trí 4 sau 2 lần so sánh.
- **Tìm kiếm tuần tự**: lần lượt so sánh với $$2, 5, 8, 12$$ → trả về vị trí 4 sau 4 lần so sánh.

</div>

## Một số lớp bài toán thường gặp

| Lớp bài toán | Câu hỏi trung tâm |
|:---|:---|
| **Tìm kiếm** | Một phần tử hoặc khóa có xuất hiện trong cấu trúc dữ liệu không? |
| **Sắp xếp** | Sắp đặt các phần tử theo một thứ tự xác định |
| **Tối ưu** | Tìm cấu hình có chi phí nhỏ nhất hoặc lớn nhất (nhiều bài thuộc lớp khó — Chương 20) |
| **Quyết định** | Trả lời Có/Không cho một tính chất (nền tảng lý thuyết P/NP) |

### Thử nghiệm: sắp xếp và tìm kiếm từng bước

Quan sát số phép so sánh và hoán đổi của ba thuật toán sắp xếp cơ bản, đồng thời so sánh trực tiếp tìm kiếm tuần tự với tìm kiếm nhị phân.

<div class="interactive-demo" markdown="1">
<div data-demo="sort-explainer" data-tab="sort"></div>
</div>
<script src="{{ '/public/js/explainers/recurrence-explainer.js' | relative_url }}"></script>

## Thử nghiệm tương tác

<div class="interactive-demo" markdown="1">
<div data-demo="algorithm-visualization"></div>
</div>
<script src="{{ '/public/js/algorithm-visualization.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Liệt kê 4 tính chất của một thuật toán và giải thích ngắn gọn tính dừng (*finiteness*).

<details>
<summary>Đáp án</summary>

Có thể nêu bốn trong sáu tính chất: đầu vào (input), đầu ra (output), tính xác định (definiteness), tính dừng (finiteness), tính đúng đắn (correctness) và tính khả thi (effectiveness). Tính dừng đòi hỏi thuật toán phải kết thúc sau một số hữu hạn bước, không rơi vào vòng lặp vô hạn với mọi đầu vào hợp lệ.

</details>

### Bài tập 2

Theo dõi vết chạy của `BINARY-SEARCH` trên mảng $$[1,3,4,7,9]$$ với giá trị cần tìm $$x=3$$.

<details>
<summary>Đáp án</summary>

Khởi đầu $$L=1, R=5$$:  
- Lần 1: $$m=3$$, $$A[3]=4>3$$ → cập nhật $$R=2$$.  
- Lần 2: $$m=1$$, $$A[1]=1<3$$ → cập nhật $$L=2$$.  
- Lần 3: $$m=2$$, $$A[2]=3$$ → tìm thấy, trả về chỉ số 2.

</details>

### Bài tập 3

Vì sao thuật toán tìm kiếm nhị phân yêu cầu mảng đầu vào phải được sắp xếp?

<details>
<summary>Đáp án</summary>

Ở mỗi bước, thuật toán so sánh $$x$$ với phần tử giữa $$A[m]$$ để loại bỏ hoàn toàn nửa trái hoặc nửa phải của mảng. Quyết định loại bỏ này chỉ đảm bảo không bỏ sót nghiệm khi toàn bộ mảng đã được sắp theo thứ tự.

</details>

## Tóm tắt

1. Thuật toán là một quy trình hữu hạn, xác định và đúng đắn cho một lớp bài toán.
2. Mã giả giúp biểu diễn thuật toán rõ ràng, độc lập với ngôn ngữ lập trình.
3. Tìm kiếm tuần tự và tìm kiếm nhị phân là hai ví dụ cơ bản để bắt đầu so sánh hiệu năng.
4. Không phải bài toán nào cũng tồn tại thuật toán tổng quát (như bài toán dừng).

Bài tiếp theo sẽ giới thiệu ký hiệu **Big-O** và tốc độ tăng trưởng của hàm số.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=0IAPZzGSbME">1. Introduction to Algorithms</a> — Abdul Bari, tiếng Anh. Giới thiệu khái niệm thuật toán và lý do cần mô tả từng bước.
- <a href="https://www.youtube.com/watch?v=FbYzBWdhMb0">1.2 Characteristics of Algorithm</a> — Abdul Bari, tiếng Anh. Trình bày các tính chất cơ bản của thuật toán.
