---
layout: post
title: "Tăng trưởng của Hàm và Ký hiệu Big-O"
categories: chapter14
date: 2021-01-01
order: 2
required: true
lang: en
---

# Tăng trưởng của Hàm và Ký hiệu Big-O

Một thuật toán chạy 0.01 giây với 100 phần tử nghe có vẻ tuyệt vời, nhưng nếu lên 10 triệu phần tử thì sao? Khi dữ liệu tăng, điều quan trọng không còn là vài mili giây đo được trên máy hôm nay, mà là **tốc độ tăng trưởng** của chi phí tính toán. Đó là lý do dân khoa học máy tính cần một ngôn ngữ nói về xu hướng, không chỉ về con số cụ thể.

**Big-O** và các ký hiệu tăng trưởng của hàm là ngôn ngữ đó. Chúng cho phép ta so sánh thuật toán ở quy mô lớn, bỏ qua chi tiết vụn vặt để nhìn vào yếu tố thống trị. Đây là công cụ cốt lõi cho mọi quyết định chọn cấu trúc dữ liệu, tối ưu code và thiết kế hệ thống có khả năng mở rộng.

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- **Giải thích** ý nghĩa của ký hiệu Big-O, Big-Omega, Big-Theta.
- **Phân loại** hàm vào các bậc tăng trưởng: hằng, log, tuyến tính, đa thức, mũ.
- **Xác định** Big-O của một hàm cho trước.
- **So sánh** tốc độ tăng trưởng của hai hàm.
- **Áp dụng** quy tắc ước lượng để phân tích vòng lặp.

**Từ khóa**: Big-O, Big-Omega ($$\Omega$$), Big-Theta ($$\Theta$$), tốc độ tăng trưởng (growth rate), bậc (order), trội (dominant term).

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter14/big_o_graph.svg" alt="Đồ thị so sánh tốc độ tăng trưởng của các hàm O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n)" width="80%" height="80%">
  <figcaption style="text-align: center;">Hình 14.2 — Tốc độ tăng trưởng của các hàm phổ biến. Trục tung là thời gian (số bước), trục hoành là kích thước đầu vào.</figcaption>
</p>
</figure>

## 1. Vấn đề

Xét hai thuật toán sắp xếp một mảng $$n$$ phần tử:

| Thuật toán | Số phép so sánh |
|:---|---:|
| Sắp xếp nổi bọt | $$\frac{n(n-1)}{2}$$ |
| Sắp xếp chèn | $$\frac{n(n-1)}{2}$$ (xấu nhất) |

Cả hai đều có dạng $$an^2 + bn + c$$. Hệ số $$a, b, c$$ khác nhau nhưng khi $$n$$ rất lớn, phần $$n^2$$ chi phối toàn bộ. **Big-O** là công cụ để ta bỏ qua hằng số và số hạng bậc thấp, chỉ giữ lại độ lớn chi phối.

## 2. Ký hiệu Big-O

**Định nghĩa**: Cho $$f, g: \mathbb{N} \to \mathbb{R}^+$$. Ta nói $$f(n)$$ là $$O(g(n))$$ nếu tồn tại hằng số $$C > 0$$ và $$n_0$$ sao cho:

$$f(n) \leq C \cdot g(n) \quad \forall n \geq n_0$$

**Ý nghĩa**: $$f(n)$$ tăng không nhanh hơn $$g(n)$$ (nhân với một hằng số), khi $$n$$ đủ lớn.

<div class="content-box example-box" markdown="1">
**Ví dụ**: Chứng minh $$f(n) = 3n^2 + 5n + 7$$ là $$O(n^2)$$.

Với $$n \geq 1$$: $$3n^2 + 5n + 7 \leq 3n^2 + 5n^2 + 7n^2 = 15n^2$$.

Chọn $$C = 15$$, $$n_0 = 1$$, ta có: $$f(n) \leq 15n^2$$ với mọi $$n \geq 1$$. Vậy $$f(n) = O(n^2)$$.
</div>

### Quy tắc ước lượng thực tế

1. **Quy tắc hằng số**: $$O(c \cdot f(n)) = O(f(n))$$ — bỏ hằng số nhân.
2. **Quy tắc tổng**: $$O(f(n) + g(n)) = O(\max(f(n), g(n)))$$ — lấy số hạng lớn nhất.
3. **Quy tắc tích**: $$O(f(n) \cdot g(n)) = O(f(n)) \cdot O(g(n))$$

## 3. Ký hiệu Big-Omega và Big-Theta

**Big-Omega (cận dưới)**:

$$f(n) = \Omega(g(n))$$ nếu $$\exists C > 0, n_0: f(n) \geq C \cdot g(n) \; \forall n \geq n_0$$

$$f(n)$$ tăng *ít nhất* nhanh bằng $$g(n)$$.

**Big-Theta (cận chặt)**:

$$f(n) = \Theta(g(n))$$ nếu $$f(n) = O(g(n))$$ và $$f(n) = \Omega(g(n))$$.

<div class="content-box example-box" markdown="1">
**Ví dụ**: $$f(n) = 5n^2 + 3n$$:
- Là $$O(n^2)$$ (cận trên)
- Là $$\Omega(n^2)$$ (cận dưới, vì $$5n^2 + 3n \geq 5n^2$$)
- Vậy $$f(n) = \Theta(n^2)$$
</div>

<div class="content-box insight-box" markdown="1">
**Phân biệt ba ký hiệu**: 
- **Big-O** là cận trên — "không tệ hơn". Dùng nhiều nhất trong thực tế.
- **Big-Omega** là cận dưới — "không tốt hơn".
- **Big-Theta** là cận chặt — "chính xác là bậc này".

Trong giao tiếp hàng ngày, người ta thường nói Big-O nhưng thực ra muốn nói Big-Theta.
</div>

## 4. Các Bậc Tăng trưởng Phổ biến

| Bậc | Tên | Ví dụ thuật toán | $$n=100$$ | $$n=10^6$$ |
|:-----|:-----|:---|---|---:|
| $$O(1)$$ | Hằng | Truy xuất mảng | 1 | 1 |
| $$O(\log n)$$ | Logarit | Tìm kiếm nhị phân | ~7 | ~20 |
| $$O(n)$$ | Tuyến tính | Tìm kiếm tuyến tính | 100 | $$10^6$$ |
| $$O(n \log n)$$ | n-log-n | Sắp xếp trộn (Merge Sort) | ~664 | ~20 × 10^6 |
| $$O(n^2)$$ | Bình phương | Sắp xếp nổi bọt | 10,000 | $$10^{12}$$ |
| $$O(2^n)$$ | Hàm mũ | Bài toán người bán hàng (duyệt toàn bộ) | ~$$10^{30}$$ | Không khả thi |

<div class="content-box warning-box" markdown="1">
**Cảnh báo**: Thuật toán $$O(2^n)$$ với $$n = 100$$ có thể mất hàng tỷ năm. Phân biệt được bậc tăng trưởng là kỹ năng sống còn trong phỏng vấn và công việc thực tế.

Để hình dung: nếu $$O(2^n)$$ chạy mất 1 giây với n=50, thì với n=100 nó mất khoảng 35 triệu năm!
</div>

## 5. Ước lượng Big-O từ Mã nguồn

**Quy tắc**:
- Lệnh đơn (gán, so sánh, trả về): $$O(1)$$
- Vòng lặp lặp $$n$$ lần: $$O(n)$$
- Vòng lặp lồng nhau: nhân số lần lặp
- Lệnh if-else: lấy nhánh lớn nhất
- Gọi hàm: tính Big-O của hàm được gọi

```
FOR i ← 1 TO n DO           ← vòng ngoài: n lần
    FOR j ← 1 TO n DO       ← vòng trong: n lần
        a[i][j] ← i + j     ← O(1)
    END FOR
END FOR
```

Tổng: $$n \times n \times O(1) = O(n^2)$$

<div class="content-box example-box" markdown="1">
**Ví dụ phân tích tìm kiếm nhị phân**:

```
WHILE left ≤ right DO
    mid ← (left + right) // 2
    IF a[mid] = x THEN RETURN mid
    ELSE IF a[mid] < x THEN left ← mid + 1
    ELSE right ← mid - 1
END WHILE
```

Mỗi vòng lặp, không gian tìm kiếm giảm một nửa: $$n \to n/2 \to n/4 \to \ldots \to 1$$. Số vòng lặp $$k$$ thỏa $$n/2^k \approx 1 \implies k \approx \log_2 n$$. Vậy $$T(n) = O(\log n)$$.
</div>

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: So sánh Tốc độ Tăng trưởng</h3>
<p>Nhập hai hàm và xem đồ thị so sánh của chúng. Công cụ tự động tìm điểm giao nhau và cho biết hàm nào "thắng" khi n đủ lớn. <strong>Hãy thử:</strong> So sánh $$1000n$$ và $$n^2$$. Với n nhỏ, $$n^2$$ thắng, nhưng sau điểm giao nhau, mọi thứ đảo ngược!</p>
</div>

## Ứng dụng trong Khoa học Máy tính

Big-O là công cụ chuẩn trong phỏng vấn kỹ thuật và thiết kế hệ thống. Khi xây dựng hệ thống phục vụ hàng triệu người dùng, sự khác biệt giữa $$O(n)$$ và $$O(n^2)$$ là sự khác biệt giữa *chạy được* và *sập server*. Big-O còn là cơ sở để phân loại bài toán P, NP — trung tâm của lý thuyết độ phức tạp tính toán.

**Ví dụ thực tế**: Google xử lý hàng tỷ tìm kiếm mỗi ngày. Nếu thuật toán tìm kiếm của họ là $$O(n^2)$$ thay vì $$O(\log n)$$, họ sẽ cần một trung tâm dữ liệu lớn gấp hàng triệu lần. Big-O quyết định khả thi hay không khả thi.

## Bài tập

1. Chứng minh $$f(n) = 7n^3 + 2n^2 + 4$$ là $$O(n^3)$$.
2. Sắp xếp các hàm sau theo thứ tự tăng dần của Big-O: $$n!,\; 2^n,\; n^3,\; n^2,\; n\log n,\; n,\; \log n,\; 1$$
3. Phân tích Big-O của thuật toán sắp xếp nổi bọt (có 2 vòng lặp lồng).
4. Cho biết số bước của tìm kiếm nhị phân khi $$n = 1,000,000$$.
5. **Thử thách**: Chứng minh rằng $$n! = O(n^n)$$. Gợi ý: So sánh từng thừa số.

<details>
<summary>Đáp án bài 5</summary>

$$n! = 1 \times 2 \times 3 \times \ldots \times n \leq n \times n \times n \times \ldots \times n = n^n$$

Vậy với mọi $$n \geq 1$$, $$n! \leq 1 \cdot n^n$$. Chọn $$C = 1, n_0 = 1$$, ta có $$n! = O(n^n)$$.

Đây là một cận trên rất rộng. Cận chặt hơn (công thức Stirling) cho biết $$n! \sim \sqrt{2\pi n}(n/e)^n$$.
</details>

## Tóm tắt

- **Big-O** $$f(n) = O(g(n))$$: $$f$$ tăng không nhanh hơn $$g$$ (cận trên).
- **Big-Omega** $$f(n) = \Omega(g(n))$$: $$f$$ tăng ít nhất nhanh bằng $$g$$ (cận dưới).
- **Big-Theta** $$f(n) = \Theta(g(n))$$: $$f$$ và $$g$$ cùng bậc (cận chặt).
- **Bậc phổ biến**: $$O(1) < O(\log n) < O(n) < O(n\log n) < O(n^2) < O(2^n) < O(n!)$$
- **Quy tắc**: bỏ hằng số, lấy số hạng trội, nhân vòng lặp lồng.

Trong bài tiếp theo, chúng ta sẽ áp dụng Big-O để phân tích độ phức tạp của các thuật toán cụ thể.

## Tài liệu Tham khảo

1. Thomas H. Cormen et al., *Introduction to Algorithms* (CLRS), Chương 3: "Growth of Functions".
2. Donald E. Knuth, "Big Omicron and Big Omega and Big Theta," *ACM SIGACT News*, 1976 — bài báo kinh điển về các ký hiệu tiệm cận.
