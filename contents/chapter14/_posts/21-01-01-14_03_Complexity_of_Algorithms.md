---
layout: post
title: "Độ phức tạp của Thuật toán"
categories: chapter14
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Ở mục trước chúng ta đã học ký hiệu Big-O để mô tả tốc độ tăng trưởng. Mục này áp dụng ngôn ngữ đó để phân tích độ phức tạp thời gian và không gian của thuật…"
---

Ở mục trước chúng ta đã học ký hiệu Big-O để mô tả tốc độ tăng trưởng. Mục này áp dụng ngôn ngữ đó để phân tích **độ phức tạp thời gian và không gian** của thuật toán một cách có phương pháp — so sánh worst-case, average-case và best-case, rồi đánh giá khả năng mở rộng của các lời giải khác nhau.

![Phân loại độ phức tạp](/discrete-mathematics-for-computer-science-iuh/img/course/Comparison_computational_complexity.svg)

<p class="textbook-figure-caption" data-figure="14.11">Phân loại thuật toán theo thời gian và không gian — trụ cột phân tích hiệu năng.</p>
![Merge sort — chia để trị](/discrete-mathematics-for-computer-science-iuh/img/course/Merge_sort_algorithm_diagram.svg)

<p class="textbook-figure-caption" data-figure="14.12">Merge sort $O(n\log n)$ vs bubble sort $O(n^2)$ — cùng đúng, khác khả năng mở rộng.</p>
![Bubble sort](/discrete-mathematics-for-computer-science-iuh/img/course/Bubble_sort_animation.gif)

<p class="textbook-figure-caption" data-figure="14.13">Bubble sort minh họa vì sao $O(n^2)$ trở nên không chấp nhận được khi $n$ lớn.</p>
![Không gian quyết định](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="14.14">Độ phức tạp không gian đo bộ nhớ phụ — quan trọng trong embedded và big data.</p>
![Trường hợp xấu nhất](/discrete-mathematics-for-computer-science-iuh/img/course/Big-O-notation.png)

<p class="textbook-figure-caption" data-figure="14.15">Phân tích worst-case, average-case và best-case — ba góc nhìn đánh giá thuật toán.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phân tích** số phép toán cơ bản của thuật toán.
- **Tính** độ phức tạp thời gian trong trường hợp tốt nhất, xấu nhất và trung bình.
- **So sánh** hai thuật toán cùng giải một bài toán.
- **Phân biệt** độ phức tạp thời gian (time complexity) và không gian (space complexity).
- **Nhận biết** các bài toán không giải được trong thời gian đa thức.

**Từ khóa**: Độ phức tạp thời gian (time complexity), độ phức tạp không gian (space complexity), trường hợp xấu nhất (worst-case), trung bình (average-case), bài toán P và NP.
</div>

## 1. Phân tích Độ phức tạp Thời gian

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Độ phức tạp thời gian** của thuật toán là số **phép toán cơ bản** (so sánh, gán, cộng, trừ…) thực hiện, biểu diễn dưới dạng hàm $$T(n)$$ theo kích thước đầu vào $$n$$. Ta quy ước mỗi phép toán cơ bản mất thời gian hằng số — mô hình **máy RAM** (Random Access Machine).
</div>

<div class="textbook-definition" markdown="1">
**Định nghĩa** (ba trường hợp):

- **Best-case**: đầu vào **thuận lợi nhất** cho thuật toán.
- **Average-case**: kỳ vọng số phép toán trên phân phối đầu vào (thường giả định ngẫu nhiên đồng đều).
- **Worst-case**: đầu vào **bất lợi nhất** — thường dùng để **đảm bảo** giới hạn trên khi thiết kế hệ thống.
</div>

### Phương pháp phân tích

1. **Đếm trực tiếp**: Đếm phép toán trong vòng lặp lồng nhau (đã học ở 14.2).
2. **Quan hệ truy hồi**: Thuật toán đệ quy → $$T(n) = a\,T(n/b) + f(n)$$ (Ch.10); có thể dùng **Master Theorem** để suy ra $$O(\cdot)$$.
3. **Phân tích gộp** (amortized): Chi phí trung bình trên **chuỗi** thao tác — ví dụ `push` vào dynamic array: đôi khi $$O(n)$$ khi resize, nhưng **amortized** $$O(1)$$ mỗi lần push.

### So sánh: Tìm kiếm Tuyến tính vs. Tìm kiếm Nhị phân

<div class="textbook-example" markdown="1">
**Ví dụ**: Tìm $$x$$ trong mảng $$n$$ phần tử **đã sắp xếp**.

| Thuật toán | Worst-case | Best-case | Average-case |
|:---|:---:|:---:|:---:|
| Tuyến tính | $$O(n)$$ | $$O(1)$$ | $$O(n)$$ |
| Nhị phân | $$O(\log n)$$ | $$O(1)$$ | $$O(\log n)$$ |

Khi $$n = 10^6$$: tuyến tính cần ~500.000 phép so sánh (trung bình), nhị phân chỉ ~20 phép.
</div>

## 2. So sánh các Thuật toán Sắp xếp

| Thuật toán | Worst-case | Average-case | Best-case | Không gian | Ổn định |
|:---|---|---|---|---|---|
| Bubble Sort | $$O(n^2)$$ | $$O(n^2)$$ | $$O(n)$$ | $$O(1)$$ | Có |
| Insertion Sort | $$O(n^2)$$ | $$O(n^2)$$ | $$O(n)$$ | $$O(1)$$ | Có |
| Selection Sort | $$O(n^2)$$ | $$O(n^2)$$ | $$O(n^2)$$ | $$O(1)$$ | Không |
| Merge Sort | $$O(n \log n)$$ | $$O(n \log n)$$ | $$O(n \log n)$$ | $$O(n)$$ | Có |
| Quick Sort | $$O(n^2)$$ | $$O(n \log n)$$ | $$O(n \log n)$$ | $$O(\log n)$$ | Không |

<div class="textbook-theorem" markdown="1">
**Lưu ý thực hành**: Quick Sort có worst-case $$O(n^2)$$ nhưng average-case $$O(n \log n)$$ với pivot ngẫu nhiên; hằng số nhỏ hơn Merge Sort nên thư viện chuẩn (Python `sort`, C++ `std::sort`) thường dùng biến thể Quick Sort / introsort. **Big-O** mô tả tăng trưởng khi $$n \to \infty$$; với $$n$$ nhỏ, hằng số và cache locality quyết định.
</div>

## 3. Độ phức tạp Không gian

Bên cạnh thời gian, bộ nhớ cũng là tài nguyên cần cân nhắc:

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Độ phức tạp không gian là lượng bộ nhớ phụ (ngoài đầu vào) mà thuật toán sử dụng, đo theo $$n$$.
</div>

| Thuật toán | Không gian phụ |
|:---|---:|
| Tìm kiếm tuyến tính | $$O(1)$$ |
| Tìm kiếm nhị phân (đệ quy) | $$O(\log n)$$ (ngăn xếp đệ quy) |
| Merge Sort | $$O(n)$$ (mảng phụ) |
| Fibonacci đệ quy "ngây thơ" | $$O(n)$$ (ngăn xếp đệ quy) |

<div class="textbook-definition" markdown="1">
**Định nghĩa** (đánh đổi thời gian–không gian): **Trade-off** xảy ra khi giảm độ phức tạp thời gian bằng cách tăng bộ nhớ phụ (hoặc ngược lại). Ví dụ: memoization Fibonacci — $$O(n)$$ thời gian, $$O(n)$$ không gian; bảng băm lưu kết quả tra cứu — $$O(1)$$ amortized, $$O(n)$$ không gian.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**: Merge Sort dùng $$O(n)$$ bộ nhớ phụ để đạt $$O(n \log n)$$ thời gian. Selection Sort dùng $$O(1)$$ bộ nhớ nhưng $$O(n^2)$$ thời gian. Với dữ liệu lớn, thường ưu tiên thời gian; trên thiết bị nhúng (embedded), có thể chấp nhận chậm hơn để tiết kiệm RAM.
</div>

## 4. Giới thiệu về Độ khó của Bài toán (P và NP)

<div class="textbook-definition" markdown="1">
**Định nghĩa**:

- **Lớp P**: Tập bài toán quyết định giải được trong thời gian **đa thức** $$O(n^k)$$. Ví dụ: sắp xếp, shortest path (Dijkstra), MST.
- **Lớp NP**: Tập bài toán mà **lời giải đề xuất** có thể **kiểm tra** trong thời gian đa thức. Ví dụ: TSP (kiểm tra tour có độ dài $$\leq L$$), SAT, tô màu $$k$$ màu.
- **NP-hard**: Ít nhất khó như mọi bài trong NP; có thể không thuộc NP. **NP-complete** = thuộc NP và NP-hard.
</div>

<div class="textbook-theorem" markdown="1">
**Câu hỏi mở** $$P \stackrel{?}{=} NP$$: Liệu mọi bài toán kiểm tra nhanh có **giải** nhanh không? Đây là một trong bảy bài toán Thiên niên kỷ (Clay Institute, 1 triệu USD). Phần lớn giới hàn lâm tin $$P \neq NP$$; chưa có chứng minh.
</div>

| Bài toán | Thuật toán tốt nhất đã biết | Độ phức tạp |
|:---|---|---|
| Tìm đường đi ngắn nhất (Dijkstra) | Dijkstra | $$O(n^2)$$ |
| Tìm tập con có tổng cho trước | Duyệt toàn bộ | $$O(2^n)$$ |
| Bài toán người bán hàng (TSP) | Quy hoạch động | $$O(n^2 2^n)$$ |

**Tại sao quan trọng?** Nếu $$P = NP$$, nhiều bài tối ưu hóa hiện dùng heuristic (logistics, thiết kế thuốc, lập lịch) có thể có thuật toán đa thức tối ưu. Ch.20 sẽ mở rộng Cook–Levin và NP-completeness.

## 5. Ví dụ Phân tích: Dãy Fibonacci

```
THUẬT TOÁN: Fibonacci-đệ-quy(n)
IF n = 0 THEN RETURN 0
IF n = 1 THEN RETURN 1
RETURN Fibonacci-đệ-quy(n-1) + Fibonacci-đệ-quy(n-2)
```

<div class="textbook-example" markdown="1">
**Ví dụ** (đệ quy ngây thơ): $$T(n) = T(n-1) + T(n-2) + O(1)$$ — tương đương dãy Fibonacci. Suy ra $$T(n) = O(\phi^n)$$ với $$\phi \approx 1{,}618$$, tức **exponential** $$O(2^n)$$.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ** (quy hoạch động / memoization): Lưu $$F[0..n]$$ một lần → $$O(n)$$ thời gian, $$O(n)$$ không gian. Chỉ giữ hai giá trị cuối → $$O(n)$$ thời gian, $$O(1)$$ không gian. Cùng đúng, khác **bậc tăng trưởng** — minh họa sức mạnh của phân tích và tối ưu.
</div>

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: Đếm số bước Thuật toán</h3>
<p>Công cụ này chạy mô phỏng và đếm số phép toán thực tế của các thuật toán khác nhau trên cùng một bộ dữ liệu. Bạn sẽ thấy sự khác biệt giữa O(n), O(n log n) và O(n^2) một cách trực quan. <strong>Gợi ý thực hành:</strong> So sánh Bubble Sort và Merge Sort với n=10000 và xem tốc độ khác nhau như thế nào.</p>
<div data-demo="algorithm-complexity-analyzer"></div>
</div>
<script src="{{ '/public/js/algorithm-complexity-analyzer.js' | relative_url }}"></script>

## Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Cần chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Phân tích độ phức tạp là kỹ năng cốt lõi trong phát triển phần mềm thực tế:

- **Thiết kế API**: Backend phải xử lý hàng nghìn request mỗi giây — một thuật toán $$O(n^2)$$ có thể làm treo server.
- **Chọn cấu trúc dữ liệu**: Hash map $$O(1)$$ hay cây nhị phân $$O(\log n)$$? Lựa chọn phụ thuộc vào nhu cầu cụ thể.
- **Xử lý dữ liệu lớn**: Với dữ liệu hàng terabyte, chỉ các thuật toán gần-tuyến tính ($$O(n)$$ hoặc $$O(n\log n)$$) mới khả thi.
- **Tối ưu hóa truy vấn CSDL**: Cơ sở dữ liệu dùng chi phí ước tính để chọn kế hoạch thực thi truy vấn.

## Bài tập

### Bài tập 1

Phân tích số phép so sánh của Selection Sort. Kết luận Big-O.

<details>
<summary>Đáp án</summary>

Hai vòng lặp lồng: $$\frac{n(n-1)}{2}$$ so sánh → **$$O(n^2)$$** worst-case.
</details>

### Bài tập 2

Cho mảng 1 triệu phần tử, ước tính số bước tìm kiếm tuyến tính (trung bình) và nhị phân.

<details>
<summary>Đáp án</summary>

Tuyến tính: ~$$5 \times 10^5$$. Nhị phân: $$\lceil \log_2 10^6 \rceil = 20$$.
</details>

### Bài tập 3

Subset sum: $$n$$ số, có tập con tổng bằng $$S$$? Vì sao duyệt mọi tập con là $$O(2^n)$$?

<details>
<summary>Đáp án</summary>

Mỗi phần tử chọn/không chọn → $$2^n$$ tập con; kiểm tra mỗi tập $$O(n)$$ → $$O(n \cdot 2^n)$$, bậc domination $$O(2^n)$$.
</details>

### Bài tập 4

Viết thuật toán Fibonacci thứ $$n$$ trong $$O(n)$$ thời gian, $$O(1)$$ không gian.

<details>
<summary>Gợi ý</summary>

Vòng lặp giữ hai biến `prev`, `curr`, cập nhật theo dãy.
</details>

### Bài tập 5

Thuật toán A: $$O(n^3)$$ thời gian, $$O(n^2)$$ không gian. Thuật toán B: $$O(n^4)$$ thời gian, $$O(n)$$ không gian. Chọn khi $$n=100$$? Khi $$n=10^6$$?

<details>
<summary>Đáp án</summary>

Khi n=100:
- Thuật toán 1: $$100^3 = 10^6$$ phép tính, $$100^2 = 10000$$ đơn vị bộ nhớ.
- Thuật toán 2: $$100^4 = 10^8$$ phép tính, 100 đơn vị bộ nhớ.
→ Thuật toán 1 nhanh hơn 100 lần, nhưng cần nhiều bộ nhớ hơn. Với n nhỏ, thường chọn tốc độ.

Khi n=10^6:
- Thuật toán 1: $$10^{18}$$ phép tính (không khả thi), $$10^{12}$$ đơn vị bộ nhớ (hàng terabyte).
- Thuật toán 2: $$10^{24}$$ phép tính (càng không khả thi), $$10^6$$ đơn vị bộ nhớ (vài MB).
→ Cả hai đều không khả thi! Cần thuật toán tốt hơn như $$O(n^2)$$ hoặc $$O(n\log n)$$.

Bài học: Luôn tìm thuật toán có bậc tăng trưởng thấp nhất có thể. Khi n đủ lớn, chỉ các thuật toán gần-tuyến tính mới khả thi.
</details>

## Xem thêm / Video gợi ý

- [Big O Notation — Intuition](https://www.youtube.com/watch?v=4jZ5n8k0p0Q) — 3Blue1Brown (Growth rates visualized)

## Tóm tắt

- **Độ phức tạp thời gian**: số phép toán cơ bản theo kích thước đầu vào.
- **Ba trường hợp**: best-case, average-case, worst-case — thường dùng worst-case.
- **Độ phức tạp không gian**: bộ nhớ phụ sử dụng.
- **Đánh đổi thời gian - không gian**: thuật toán nhanh hơn thường cần nhiều bộ nhớ hơn.
- **Phương pháp**: đếm vòng lặp, truy hồi, amortized analysis.
- **P và NP**: P giải nhanh; NP kiểm tra nhanh; NP-complete là ranh giới khó.

Trong chương tiếp theo, chúng ta sẽ chuyển sang lý thuyết số — nền tảng của mật mã học hiện đại.

## Tài liệu Tham khảo

1. Thomas H. Cormen et al., *Introduction to Algorithms* (CLRS), Chương 2, 3, 34.
2. Michael Sipser, *Introduction to the Theory of Computation*, Chương 7 về NP-completeness.
3. Stephen Cook, "The P vs NP Problem," *Clay Mathematics Institute*, 2000.
