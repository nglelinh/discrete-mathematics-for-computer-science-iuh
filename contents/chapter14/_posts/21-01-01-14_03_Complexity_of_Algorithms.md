---
layout: post
title: "Độ phức tạp của Thuật toán"
categories: chapter14
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "T(n) và S(n); best/average/worst; phân tích vòng lặp; master theorem sơ lược; so sánh thuật toán tìm kiếm và sắp xếp."
---

<div class="textbook-epigraph" markdown="1">

"Count the dominant operations as a function of n — then wrap the result in Θ or O."

<span class="epigraph-attribution">— Algorithm analysis practice</span>

</div>

Big-O cung cấp ký hiệu; mục này **đo** độ phức tạp **thời gian** $$T(n)$$ và **không gian** $$S(n)$$ của thuật toán: worst-case, đếm phép so sánh/vòng lặp, và vài mẫu chuẩn (vòng lồng, chia để trị).

![Thời gian và không gian](/discrete-mathematics-for-computer-science-iuh/img/course/Algo_time_space.svg)

<p class="textbook-figure-caption" data-figure="14.4">Phân tích: $$T(n)$$ (thường worst-case) và bộ nhớ phụ $$S(n)$$.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phân biệt** best / average / worst-case.
- **Phân tích** vòng lặp đơn và lồng để ra $$T(n)$$.
- **Nêu** $$T(n)$$ của linear search, binary search, merge sort (ý).
- **Ước lượng** không gian phụ.
- **Chọn** thuật toán theo ràng buộc $$n$$ và bộ nhớ.

**Từ khóa**: time complexity, space complexity, worst-case, loop analysis, divide-and-conquer.

</div>

## 1. Mô hình đếm

Chọn **phép toán trội** (so sánh khóa, phép gán phần tử, …). $$T(n)$$ = số phép đó theo kích thước input $$n$$ (worst-case trừ khi nói khác).

| Case | Ý nghĩa |
|:---|:---|
| **Best** | Input “may mắn” nhất |
| **Average** | Trung bình trên phân bố input |
| **Worst** | Input xấu nhất — thường dùng để bảo đảm |

## 2. Vòng lặp

- Một vòng $$1..n$$ thân $$O(1)$$ → $$T(n)=\Theta(n)$$.
- Hai vòng lồng độc lập $$i,j=1..n$$ → $$\Theta(n^2)$$.
- Vòng trong phụ thuộc $$i$$: $$\sum_{i=1}^{n} i = \Theta(n^2)$$.

<div class="textbook-example" markdown="1">

**Ví dụ 1.** Linear search: worst $$n$$ so sánh → $$\Theta(n)$$. Binary search: khoảng $$\lfloor\log_2 n\rfloor+1$$ so sánh → $$\Theta(\log n)$$.

</div>

## 3. Chia để trị (ý)

Merge sort: $$T(n)=2T(n/2)+\Theta(n)$$ → $$T(n)=\Theta(n\log n)$$ (master theorem / cây đệ quy).

![Merge sort](/discrete-mathematics-for-computer-science-iuh/img/course/Merge_sort_algorithm_diagram.svg)

<p class="textbook-figure-caption" data-figure="14.5">Merge sort: chia đôi + trộn tuyến tính — $$\Theta(n\log n)$$ thời gian, $$\Theta(n)$$ bộ nhớ phụ điển hình.</p>

## 4. Không gian

- **In-place** (ý): $$S(n)=O(1)$$ phụ ngoài input (heap sort xấp xỉ; binary search).
- Đệ quy sâu $$h$$: stack $$O(h)$$.
- Mảng phụ kích thước $$n$$: $$S(n)=\Theta(n)$$.

## 5. Thử nghiệm tương tác

<div class="interactive-demo" markdown="1">
<div data-demo="algorithm-complexity-analyzer"></div>
</div>
<script src="{{ '/public/js/algorithm-complexity-analyzer.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Phân tích $$T(n)$$:

```text
for i ← 1 to n
  for j ← 1 to i
    op
```

<details>
<summary>Đáp án</summary>

Số lần `op`: $$\sum_{i=1}^{n} i = n(n+1)/2 = \Theta(n^2)$$.

</details>

### Bài tập 2

So sánh linear vs binary search khi $$n=10^6$$ (ý số so sánh worst).

<details>
<summary>Đáp án</summary>

Linear: $$10^6$$. Binary: $$\approx 20$$ ($$\log_2 10^6\approx 20$$). Binary cần mảng đã sắp.

</details>

### Bài tập 3

Merge sort thời gian $$\Theta(n\log n)$$ nhưng thường dùng thêm mảng phụ. Trade-off?

<details>
<summary>Đáp án</summary>

Nhanh và ổn định worst-case; đổi lấy $$S(n)=\Theta(n)$$ — quan trọng trên bộ nhớ hạn chế.

</details>

## Tóm tắt

1. Worst-case $$T(n)$$ bằng đếm phép trội.
2. Vòng lồng → đa thức; chia để trị → $$n\log n$$ điển hình.
3. Không gian phụ cũng là ràng buộc thiết kế.

Bài khảo sát: thuật toán từ lịch sử đến quy mô lớn.
