---
layout: post
title: "Độ phức tạp của Thuật toán"
categories: chapter14
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Phân tích độ phức tạp thời gian T(n) và không gian S(n): trường hợp tốt nhất, trung bình, xấu nhất; phân tích vòng lặp và chia để trị; so sánh tìm kiếm và sắp xếp."
---

> **Câu chuyện mở đầu:** Nhìn vào hai vòng lặp `for` lồng nhau, nhiều sinh viên phản xạ ngay "$$O(n^2)$$"! Nhưng khoan đã: nếu vòng lặp trong có bước nhảy nhân đôi `j = j * 2`, tổng số bước thực ra chỉ là $$O(n \log n)$$; còn nếu vòng ngoài nhân đôi `i = i * 2` và vòng trong chạy `1..i`, tổng số bước thậm chí chỉ là **$$O(n)$$**! Phân tích độ phức tạp là nghệ thuật biến cấu trúc mã nguồn thành **tổng đại số hoặc hệ thức truy hồi** rồi tính chính xác bậc tăng trưởng.

<div class="textbook-epigraph" markdown="1">

"Count the dominant operations as a function of n — then wrap the result in Θ or O."

<span class="epigraph-attribution">— Algorithm analysis practice</span>

</div>

Sau khi có ngôn ngữ tiệm cận Big-O ở bài trước, mục này trình bày cách **tính độ phức tạp thời gian** $$T(n)$$ và **độ phức tạp không gian** $$S(n)$$ của thuật toán thông qua phân tích trường hợp xấu nhất (*worst-case*), đếm số phép toán trội trong vòng lặp và một số khuôn mẫu phổ biến như vòng lặp lồng nhau hay chia để trị.

![Thời gian và không gian](/discrete-mathematics-for-computer-science-iuh/img/course/Algo_time_space.svg)

<p class="textbook-figure-caption" data-figure="14.4">Hai đại lượng cơ bản khi đánh giá thuật toán: thời gian thực thi $$T(n)$$ (thường xét trường hợp xấu nhất) và bộ nhớ phụ $$S(n)$$.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phân biệt** phân tích trường hợp tốt nhất (*best-case*), trung bình (*average-case*) và xấu nhất (*worst-case*).
- **Phân tích** vòng lặp đơn và vòng lặp lồng nhau để suy ra biểu thức $$T(n)$$.
- **Xác định** độ phức tạp của tìm kiếm tuần tự, tìm kiếm nhị phân và sắp xếp trộn (merge sort).
- **Ước lượng** độ phức tạp không gian phụ $$S(n)$$.
- **Lựa chọn** thuật toán phù hợp dựa trên ràng buộc về kích thước đầu vào $$n$$ và dung lượng bộ nhớ.

**Từ khóa**: time complexity, space complexity, worst-case, loop analysis, divide-and-conquer.

</div>

## Kiến thức cần nhớ: Phân tích Độ phức tạp Thời gian & Không gian

### 1. Mô hình RAM & Ba kịch bản Phân tích
- **Bản chất:** Trên mô hình RAM chuẩn, mỗi phép toán cơ bản (cộng, so sánh, truy cập mảng) tốn $$O(1)$$. Ta phân biệt **tốt nhất (best-case)**, **xấu nhất (worst-case)** — chuẩn an toàn cho kỹ thuật — và **trung bình (average-case)** (dùng kỳ vọng xác suất).

### 2. Vòng lặp Lồng nhau & Tổng Chuỗi kinh điển
- Vòng lặp tuyến tính tam giác: $$\sum_{i=1}^n i = \frac{n(n+1)}{2} = \Theta(n^2)$$.
- Vòng lặp nhân đôi (cấp số nhân): $$1 + 2 + 4 + \dots + n = 2n - 1 = \Theta(n)$$!
- Tổng điều hòa: $$\sum_{i=1}^n \frac{1}{i} = \ln n + O(1) = \Theta(\log n)$$ (dùng để chứng minh Sàng Eratosthenes chạy trong $$O(n \log \log n)$$!).

### 3. Thuật toán Đệ quy & Định lý Thợ (Master Theorem)
- **Bản chất:** Với thuật toán chia để trị $$T(n) = a\,T(n/b) + f(n)$$, **Master Theorem** so sánh công việc ở lá ($$n^{\log_b a}$$) với công việc ghép ở gốc ($$f(n)$$) để đọc ngay kết quả:
  - Merge Sort: $$T(n) = 2T(n/2) + \Theta(n) \implies \Theta(n\log n)$$.
  - Binary Search: $$T(n) = T(n/2) + \Theta(1) \implies \Theta(\log n)$$.

## Ví dụ tính tay làm từng bước: Bóc tách 2 vòng lặp lồng nhau "đánh lừa trực giác"

1. **Vòng lặp 1:** `i` chạy `1, 2, 4, 8, ..., n` (nhân đôi); với mỗi `i`, `j` chạy từ `1` đến `i`:
   Tổng số bước chính xác (đặt $$n = 2^k$$):
   $$
   T(n) = 1 + 2 + 4 + \cdots + 2^k = 2^{k+1} - 1 = 2n - 1 = \Theta(n)!
   $$
   *(Không phải $$O(n\log n)$$ — công việc ở lần lặp cuối cùng chiếm hơn một nửa tổng thời gian!)*

2. **Vòng lặp 2 (kiểu Sàng):** `i` chạy từ `1` đến `n`; với mỗi `i`, `j` tăng bước `i` (`j = i, 2i, 3i, ..., <= n`):
   Số lần chạy của vòng trong là $$\lfloor n/i \rfloor$$, nên tổng số bước là:
   $$
   T(n) = \sum_{i=1}^n \left\lfloor \frac{n}{i} \right\rfloor \approx n\left(1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}\right) = n \cdot H_n = \Theta(n \log n)!
   $$

### Giải thích: Quy trình 4 bước tính độ phức tạp của mọi đoạn mã
#### Bước 1: Chọn phép toán cơ bản (Basic Operation)
Thường là phép so sánh (trong sắp xếp/tìm kiếm) hoặc phép nhân/cộng nằm ở vòng lặp sâu nhất.

#### Bước 2: Chuyển cấu trúc lặp thành dấu tổng $$\sum$$, cấu trúc đệ quy thành hệ thức $$T(n)$$
Đừng đoán bằng cảm giác — hãy viết tường minh cận trên, cận dưới của từng vòng `for`/`while`.

#### Bước 3: Tính gọn tổng hoặc giải truy hồi (Master Theorem / Cây đệ quy)
Dùng 3 công thức bỏ túi: tổng cấp số cộng $$\Theta(n^2)$$, tổng cấp số nhân $$\Theta(\text{số hạng lớn nhất})$$, tổng điều hòa $$\Theta(\log n)$$.

#### Bước 4: Đừng bỏ quên Độ phức tạp Bộ nhớ (Space Complexity)
Nhớ tính cả **ngăn xếp đệ quy (call stack)**: QuickSort trung bình tốn $$O(\log n)$$ không gian stack, còn Merge Sort tốn $$O(n)$$ mảng phụ!

$$
\text{Mã nguồn (Lặp / Đệ quy)}
\;\xrightarrow{\;\sum \text{ hoặc } T(n)\;}\;
\text{Tổng chuỗi / Master Theorem}
\;\xrightarrow{\;\text{Tiệm cận}\;}\;
\text{Thời gian \& Bộ nhớ }\Theta(\cdot).
$$

## Mô hình đếm phép toán

Để đo thời gian chạy mà không phụ thuộc phần cứng, ta chọn một **phép toán trội** (chẳng hạn phép so sánh khóa hoặc phép gán phần tử) và biểu diễn $$T(n)$$ là số lần thực hiện phép toán đó theo kích thước đầu vào $$n$$. Nếu không nói gì thêm, ta mặc định xét trường hợp xấu nhất.

| Trường hợp | Ý nghĩa |
|:---|:---|
| **Tốt nhất (Best-case)** | Đầu vào thuận lợi nhất cho thuật toán |
| **Trung bình (Average-case)** | Kỳ vọng chi phí trên một phân bố đầu vào |
| **Xấu nhất (Worst-case)** | Đầu vào bất lợi nhất — cung cấp cận trên đảm bảo hiệu năng |

## Phân tích vòng lặp

![Minh họa sắp xếp nổi bọt O(n²)](/discrete-mathematics-for-computer-science-iuh/img/course/Bubble_sort_animation.gif)

- Một vòng lặp chạy từ $$1$$ đến $$n$$ với thân mất $$O(1)$$ cho $$T(n) = \Theta(n)$$.
- Hai vòng lặp lồng nhau độc lập $$i, j = 1 \ldots n$$ cho $$T(n) = \Theta(n^2)$$.
- Vòng lặp trong phụ thuộc biến ngoài $$i$$ (chạy từ $$1$$ đến $$i$$) thực hiện $$\sum_{i=1}^{n} i = \frac{n(n+1)}{2} = \Theta(n^2)$$ lần.

<div class="textbook-example" markdown="1">

**Ví dụ 1.** Trong trường hợp xấu nhất, tìm kiếm tuần tự thực hiện $$n$$ phép so sánh nên có độ phức tạp $$\Theta(n)$$, trong khi tìm kiếm nhị phân thực hiện tối đa $$\lfloor\log_2 n\rfloor + 1$$ phép so sánh nên đạt $$\Theta(\log n)$$.

</div>

## Chia để trị (Divide and Conquer)

Với sắp xếp trộn (*merge sort*), mảng được chia đôi rồi trộn lại trong thời gian tuyến tính, dẫn đến hệ thức truy hồi $$T(n) = 2T(n/2) + \Theta(n)$$. Áp dụng định lý thợ (*Master Theorem*) hoặc phân tích cây đệ quy cho kết quả $$T(n) = \Theta(n\log n)$$.

![Merge sort](/discrete-mathematics-for-computer-science-iuh/img/course/Merge_sort_algorithm_diagram.svg)

<p class="textbook-figure-caption" data-figure="14.5">Sắp xếp trộn (merge sort): chia đôi mảng và trộn tuyến tính, đạt thời gian $$\Theta(n\log n)$$ và dùng bộ nhớ phụ $$\Theta(n)$$.</p>

## Độ phức tạp không gian

- **Tại chỗ (In-place)**: chỉ dùng lượng bộ nhớ phụ hằng số $$S(n) = O(1)$$ ngoài dữ liệu đầu vào (ví dụ tìm kiếm nhị phân lặp, heapsort).
- **Ngăn xếp đệ quy**: thuật toán đệ quy có độ sâu $$h$$ tiêu tốn $$O(h)$$ bộ nhớ trên ngăn xếp gọi hàm.
- **Mảng phụ**: khi cần cấp phát thêm mảng kích thước $$n$$ (như merge sort chuẩn), độ phức tạp không gian là $$S(n) = \Theta(n)$$.

## Thử nghiệm tương tác

<div class="interactive-demo" markdown="1">
<div data-demo="algorithm-complexity-analyzer"></div>
</div>
<script src="{{ '/public/js/algorithm-complexity-analyzer.js' | relative_url }}"></script>


## Công cụ tương tác

Chọn cấu trúc vòng lặp (một lớp hoặc hai lớp) với $$n$$ nhỏ để quan sát số bước thực thi khớp với các công thức $$n$$, $$n(n+1)/2$$ hay $$n^2$$.
<div class="interactive-demo" markdown="1">
<div data-demo="summation-loop-visualizer"></div>
</div>
<script src="{{ '/public/js/summation-loop-visualizer.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Phân tích độ phức tạp thời gian $$T(n)$$ của đoạn mã giả sau:

```text
for i ← 1 to n
  for j ← 1 to i
    op
```

<details>
<summary>Đáp án</summary>

Số lần thực hiện thao tác `op` là $$\sum_{i=1}^{n} i = \frac{n(n+1)}{2} = \Theta(n^2)$$.

</details>

### Bài tập 2

So sánh số phép so sánh trong trường hợp xấu nhất giữa tìm kiếm tuần tự và tìm kiếm nhị phân khi $$n=10^6$$.

<details>
<summary>Đáp án</summary>

Tìm kiếm tuần tự cần tới $$10^6$$ phép so sánh, còn tìm kiếm nhị phân chỉ cần khoảng $$20$$ phép so sánh (do $$\log_2 10^6 \approx 19{,}93$$), với điều kiện mảng đã được sắp xếp trước.

</details>

### Bài tập 3

Sắp xếp trộn (merge sort) có độ phức tạp thời gian $$\Theta(n\log n)$$ nhưng thường cần thêm mảng phụ. Đánh đổi ở đây là gì?

<details>
<summary>Đáp án</summary>

Merge sort đảm bảo thời gian $$\Theta(n\log n)$$ ổn định ngay cả trong trường hợp xấu nhất, nhưng phải đánh đổi bằng chi phí bộ nhớ phụ $$S(n)=\Theta(n)$$ — yếu tố cần cân nhắc trên các hệ thống có bộ nhớ hạn chế.

</details>

## Tóm tắt

1. Độ phức tạp thời gian $$T(n)$$ (thường ở trường hợp xấu nhất) được xác định bằng cách đếm số lần thực hiện phép toán trội.
2. Vòng lặp lồng nhau thường dẫn tới độ phức tạp đa thức; các thuật toán chia để trị như merge sort thường đạt $$\Theta(n\log n)$$.
3. Độ phức tạp không gian phụ $$S(n)$$ là ràng buộc quan trọng song song với thời gian chạy.

Bài tiếp theo khảo sát sự phát triển của thuật toán từ lịch sử đến các hệ thống quy mô lớn.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=A03oI0znAoc">1.8.1 Asymptotic Notations Big Oh - Omega - Theta #1</a> — Abdul Bari, tiếng Anh. Ôn lại các ký hiệu tiệm cận dùng trong phân tích thuật toán.
- <a href="https://www.youtube.com/watch?v=NI4OKSvGAgM">1.9 Properties of Asymptotic Notations</a> — Abdul Bari, tiếng Anh. Các tính chất của ký hiệu tiệm cận khi cộng và nhân bậc tăng trưởng.
- <a href="https://www.youtube.com/watch?v=OynWkEj0S-s">2.4.1 Masters Theorem in Algorithms for Dividing Function #1</a> — Abdul Bari, tiếng Anh. Áp dụng định lý thợ cho các thuật toán chia để trị.
