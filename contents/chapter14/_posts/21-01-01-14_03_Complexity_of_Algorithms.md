---
layout: post
title: "Độ phức tạp của Thuật toán"
categories: chapter14
date: 2021-01-01
order: 3
required: true
lang: en
---

Sau khi có ngôn ngữ Big-O để mô tả tăng trưởng, bước tiếp theo là dùng nó để phân tích **độ phức tạp của thuật toán** một cách có phương pháp. Đây là kỹ năng cốt lõi nếu ta muốn so sánh lời giải không chỉ bằng cảm giác.


Phân tích thuật toán không chỉ hỏi chương trình chạy được hay không, mà còn hỏi nó còn dùng được khi dữ liệu lớn lên nhanh đến mức nào.
Trong thực tế, hai đoạn code cùng cho ra kết quả đúng có thể khác nhau rất xa về thời gian chạy hoặc mức dùng bộ nhớ. Một lựa chọn hợp lý với dữ liệu nhỏ có thể trở thành nút cổ chai khi hệ thống mở rộng.

Phân tích độ phức tạp giúp ta nhìn vào cấu trúc của thuật toán, số vòng lặp, số lời gọi đệ quy, kiểu thao tác dữ liệu, rồi dự đoán chi phí trước cả khi triển khai trên quy mô lớn. Đây là một trong những kỹ năng phân tích quan trọng nhất của người làm CS.

Trong bài này, chúng ta sẽ đi từ các ví dụ quen thuộc đến cách ước lượng và so sánh độ phức tạp thời gian, không gian của các thuật toán khác nhau.

## Mục tiêu học tập

Hãy đọc mục tiêu như danh sách năng lực cần đạt sau bài, vì chúng cho biết bạn nên hiểu gì, làm được gì và áp dụng vào đâu.

Sau bài học này, sinh viên có thể:

- **Phân tích** số phép toán cơ bản của thuật toán.
- **Tính** độ phức tạp thời gian trong trường hợp tốt nhất, xấu nhất và trung bình.
- **So sánh** hai thuật toán cùng giải một bài toán.
- **Phân biệt** độ phức tạp thời gian (time complexity) và không gian (space complexity).
- **Nhận biết** các bài toán không giải được trong thời gian đa thức.

**Từ khóa**: Độ phức tạp thời gian (time complexity), độ phức tạp không gian (space complexity), trường hợp xấu nhất (worst-case), trung bình (average-case), bài toán P và NP.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter14/time_space_tradeoff.svg" alt="Minh họa sự đánh đổi giữa thời gian và không gian trong các thuật toán" width="70%" height="70%">
  <figcaption style="text-align: center;">Hình 14.3 — Sự đánh đổi giữa thời gian và không gian: thuật toán nhanh hơn thường cần nhiều bộ nhớ hơn.</figcaption>
</p>
</figure>

## 1. Phân tích Độ phức tạp Thời gian

Độ phức tạp thời gian được đo bằng số **phép toán cơ bản** (so sánh, gán, cộng trừ...) thực hiện bởi thuật toán, là hàm theo kích thước đầu vào $$n$$.

### So sánh: Tìm kiếm Tuyến tính vs. Tìm kiếm Nhị phân

<div class="content-box example-box" markdown="1">
**Bài toán**: Tìm $$x$$ trong mảng $$n$$ phần tử đã sắp xếp.

| Thuật toán | Worst-case | Best-case | Average-case |
|:---|---|---|---|
| Tuyến tính | $$O(n)$$ | $$O(1)$$ | $$O(n)$$ |
| Nhị phân | $$O(\log n)$$ | $$O(1)$$ | $$O(\log n)$$ |

Khi $$n = 10^6$$: tuyến tính cần ~500,000 phép so sánh (trung bình), nhị phân chỉ cần ~20 phép. Sự khác biệt là rất lớn!
</div>

```python
# Tìm kiếm nhị phân (giả mã)
def binary_search(a, x, left, right):
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

Phân tích: mỗi vòng lặp giảm không gian tìm kiếm xuống một nửa → $$O(\log n)$$.

### Các Mức Độ phức tạp Phổ biến

| Độ phức tạp | Ví dụ | $$n=10$$ | $$n=1000$$ | $$n=10^6$$ |
|:---|---|---|---|---|
| $$O(1)$$ | Truy xuất phần tử trong mảng | 1 | 1 | 1 |
| $$O(\log n)$$ | Tìm kiếm nhị phân | 4 | 10 | 20 |
| $$O(n)$$ | Tìm max/min | 10 | 1,000 | $$10^6$$ |
| $$O(n \log n)$$ | Merge Sort, Quick Sort (TB) | 33 | 10,000 | $$2 \times 10^7$$ |
| $$O(n^2)$$ | Bubble Sort, Selection Sort | 100 | $$10^6$$ | $$10^{12}$$ |
| $$O(2^n)$$ | Duyệt tập con (subset) | 1024 | $$\sim 10^{301}$$ | Không khả thi |

<div class="content-box insight-box" markdown="1">
**Một cách nhìn trực quan**: Nếu 1 phép toán mất 1 nano-giây:
- $$O(n)$$ với n=10^6: 1 milli-giây
- $$O(n^2)$$ với n=10^6: 11.5 ngày
- $$O(2^n)$$ với n=50: 13 ngày
- $$O(2^n)$$ với n=60: 36 năm
- $$O(2^n)$$ với n=100: hơn 300 tỷ năm (lâu hơn tuổi vũ trụ!)
</div>

## 2. So sánh các Thuật toán Sắp xếp

| Thuật toán | Worst-case | Average-case | Best-case | Không gian | Ổn định |
|:---|---|---|---|---|---|
| Bubble Sort | $$O(n^2)$$ | $$O(n^2)$$ | $$O(n)$$ | $$O(1)$$ | Có |
| Insertion Sort | $$O(n^2)$$ | $$O(n^2)$$ | $$O(n)$$ | $$O(1)$$ | Có |
| Selection Sort | $$O(n^2)$$ | $$O(n^2)$$ | $$O(n^2)$$ | $$O(1)$$ | Không |
| Merge Sort | $$O(n \log n)$$ | $$O(n \log n)$$ | $$O(n \log n)$$ | $$O(n)$$ | Có |
| Quick Sort | $$O(n^2)$$ | $$O(n \log n)$$ | $$O(n \log n)$$ | $$O(\log n)$$ | Không |

<div class="content-box warning-box" markdown="1">
**Lưu ý**: Quick Sort có worst-case $$O(n^2)$$ nhưng trong thực tế thường nhanh hơn Merge Sort do hằng số nhỏ hơn và ít sử dụng bộ nhớ hơn. Đừng chỉ nhìn Big-O — hằng số cũng quan trọng với $$n$$ nhỏ. Đây là lý do tại sao Python, Java, và C++ đều dùng Quick Sort (hoặc biến thể) trong thư viện chuẩn.
</div>

## 3. Độ phức tạp Không gian

Bên cạnh thời gian, bộ nhớ cũng là tài nguyên cần cân nhắc:

**Định nghĩa**: Độ phức tạp không gian là lượng bộ nhớ phụ (ngoài đầu vào) mà thuật toán sử dụng, đo theo $$n$$.

| Thuật toán | Không gian phụ |
|:---|---:|
| Tìm kiếm tuyến tính | $$O(1)$$ |
| Tìm kiếm nhị phân (đệ quy) | $$O(\log n)$$ (ngăn xếp đệ quy) |
| Merge Sort | $$O(n)$$ (mảng phụ) |
| Fibonacci đệ quy "ngây thơ" | $$O(n)$$ (ngăn xếp đệ quy) |

<div class="content-box example-box" markdown="1">
**Đánh đổi Không gian - Thời gian**: Merge Sort dùng $$O(n)$$ bộ nhớ phụ để đạt $$O(n \log n)$$ thời gian. Selection Sort dùng $$O(1)$$ bộ nhớ phụ nhưng mất $$O(n^2)$$ thời gian. Kỹ sư cần cân nhắc *đánh đổi* (trade-off) này. Trong thực tế, khi bộ nhớ rẻ và dữ liệu lớn, người ta thường chọn thời gian nhanh hơn.
</div>

## 4. Giới thiệu về Độ khó của Bài toán (P và NP)

Không phải bài toán nào cũng có thuật toán hiệu quả:

- **Lớp P**: Các bài toán giải được trong thời gian đa thức (polynomial time). Ví dụ: sắp xếp, tìm kiếm, đường đi ngắn nhất.
- **Lớp NP**: Các bài toán mà *lời giải* có thể kiểm tra trong thời gian đa thức. Ví dụ: bài toán người bán hàng (TSP), SAT, tô màu đồ thị.
- **Câu hỏi $$P \stackrel{?}{=} NP$$**: Liệu mọi bài toán kiểm tra được nhanh có giải được nhanh không? Đây là một trong bảy bài toán Thiên niên kỷ của Viện Toán học Clay, với giải thưởng 1 triệu USD.

| Bài toán | Thuật toán tốt nhất đã biết | Độ phức tạp |
|:---|---|---|
| Tìm đường đi ngắn nhất (Dijkstra) | Dijkstra | $$O(n^2)$$ |
| Tìm tập con có tổng cho trước | Duyệt toàn bộ | $$O(2^n)$$ |
| Bài toán người bán hàng (TSP) | Quy hoạch động | $$O(n^2 2^n)$$ |

<div class="content-box insight-box" markdown="1">
**Tại sao P vs NP quan trọng?** Nếu $$P = NP$$, thì mọi bài toán có lời giải kiểm tra nhanh (như TSP, SAT) đều có thuật toán giải nhanh. Điều này sẽ cách mạng hóa y học (thiết kế thuốc), logistics (tối ưu vận chuyển), AI (học máy) và nhiều lĩnh vực khác. Phần lớn các nhà khoa học tin rằng $$P \neq NP$$, nhưng chưa ai chứng minh được.
</div>

## 5. Ví dụ Phân tích: Dãy Fibonacci

```
THUẬT TOÁN: Fibonacci-đệ-quy(n)
IF n = 0 THEN RETURN 0
IF n = 1 THEN RETURN 1
RETURN Fibonacci-đệ-quy(n-1) + Fibonacci-đệ-quy(n-2)
```

Phân tích: $$T(n) = T(n-1) + T(n-2) + O(1)$$ — đây chính là dãy Fibonacci! $$T(n) \approx \phi^n$$, với $$\phi \approx 1.618$$ (tỷ lệ vàng). Vậy độ phức tạp là $$O(2^n)$$.

**Fibonacci dùng mảng (quy hoạch động)**: lưu kết quả trung gian → $$O(n)$$ thời gian, $$O(n)$$ không gian (có thể giảm xuống $$O(1)$$ bằng cách chỉ giữ 2 giá trị cuối).

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: Đếm số bước Thuật toán</h3>
<p>Công cụ này chạy mô phỏng và đếm số phép toán thực tế của các thuật toán khác nhau trên cùng một bộ dữ liệu. Bạn sẽ thấy sự khác biệt giữa O(n), O(n log n) và O(n^2) một cách trực quan. <strong>Hãy thử:</strong> So sánh Bubble Sort và Merge Sort với n=10000 và xem tốc độ khác nhau như thế nào.</p>
<div data-demo="algorithm-complexity-analyzer"></div>
</div>
<script src="{{ '/public/js/algorithm-complexity-analyzer.js' | relative_url }}"></script>

## Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Phân tích độ phức tạp là kỹ năng cốt lõi trong phát triển phần mềm thực tế:

- **Thiết kế API**: Backend phải xử lý hàng nghìn request mỗi giây — một thuật toán $$O(n^2)$$ có thể làm treo server.
- **Chọn cấu trúc dữ liệu**: Hash map $$O(1)$$ hay cây nhị phân $$O(\log n)$$? Lựa chọn phụ thuộc vào nhu cầu cụ thể.
- **Xử lý dữ liệu lớn**: Với dữ liệu hàng terabyte, chỉ các thuật toán gần-tuyến tính ($$O(n)$$ hoặc $$O(n\log n)$$) mới khả thi.
- **Tối ưu hóa truy vấn CSDL**: Cơ sở dữ liệu dùng chi phí ước tính để chọn kế hoạch thực thi truy vấn.

## Bài tập

Khi làm bài tập, nên bắt đầu bằng cách xác định dữ kiện, dạng bài và công cụ phù hợp trước khi tính toán. Cách tiếp cận này thường giúp tránh sai từ bước đầu.

1. Phân tích số phép so sánh của Selection Sort. Kết luận Big-O.
2. Cho mảng 1 triệu phần tử, ước tính số bước của tìm kiếm tuyến tính (trung bình) và tìm kiếm nhị phân.
3. Bài toán "subset sum": cho tập $$n$$ số, có tập con nào tổng bằng $$S$$ không? Tại sao giải pháp "duyệt tất cả tập con" có độ phức tạp $$O(2^n)$$?
4. Viết thuật toán tìm số Fibonacci thứ $$n$$ trong $$O(n)$$ và $$O(1)$$ không gian.
5. **Thử thách**: Một thuật toán mất $$O(n^3)$$ thời gian và $$O(n^2)$$ không gian. Một thuật toán khác mất $$O(n^4)$$ thời gian và $$O(n)$$ không gian. Bạn chọn cái nào khi $$n=100$$? Khi $$n=10^6$$?

<details>
<summary>Hướng dẫn bài 5</summary>

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

## Tóm tắt

- **Độ phức tạp thời gian**: số phép toán cơ bản theo kích thước đầu vào.
- **Ba trường hợp**: best-case, average-case, worst-case — thường dùng worst-case.
- **Độ phức tạp không gian**: bộ nhớ phụ sử dụng.
- **Đánh đổi thời gian - không gian**: thuật toán nhanh hơn thường cần nhiều bộ nhớ hơn.
- **P và NP**: P là bài toán giải được nhanh; NP là bài toán kiểm tra được nhanh.

Trong chương tiếp theo, chúng ta sẽ chuyển sang lý thuyết số — nền tảng của mật mã học hiện đại.

## Tài liệu Tham khảo

1. Thomas H. Cormen et al., *Introduction to Algorithms* (CLRS), Chương 2, 3, 34.
2. Michael Sipser, *Introduction to the Theory of Computation*, Chương 7 về NP-completeness.
3. Stephen Cook, "The P vs NP Problem," *Clay Mathematics Institute*, 2000.
