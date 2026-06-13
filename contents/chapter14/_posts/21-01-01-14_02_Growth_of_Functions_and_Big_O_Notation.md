---
layout: post
title: "Tăng trưởng của Hàm và Ký hiệu Big-O"
categories: chapter14
date: 2021-01-01
order: 2
required: true
lang: en
---

Một thuật toán chạy 0.01 giây với 100 phần tử chưa chắc vẫn ổn với 10 triệu phần tử. Trong khoa học máy tính, câu hỏi quan trọng không chỉ là chương trình chạy được, mà là nó tăng chi phí như thế nào khi đầu vào lớn dần.


Phân tích thuật toán không chỉ hỏi chương trình chạy được hay không, mà còn hỏi nó còn dùng được khi dữ liệu lớn lên nhanh đến mức nào.
Đó là lúc ta cần nhìn vào **tăng trưởng của hàm** thay vì các con số riêng lẻ. **Ký hiệu Big-O** cho phép ta mô tả tốc độ tăng của thời gian hoặc bộ nhớ theo cách đủ gọn để so sánh các thuật toán với nhau.

Điều này đặc biệt quan trọng vì phần cứng nhanh hơn không xóa được một thuật toán tăng trưởng tệ. Một giải pháp $$O(n \log n)$$ và một giải pháp $$O(n^2)$$ có thể khác nhau rất lớn khi quy mô tăng lên.

Trong bài này, chúng ta sẽ học cách đọc tốc độ tăng trưởng, hiểu ý nghĩa của Big-O và dùng nó để nói về hiệu năng một cách chặt chẽ hơn.

## Mục tiêu học tập

Hãy đọc mục tiêu như danh sách năng lực cần đạt sau bài, vì chúng cho biết bạn nên hiểu gì, làm được gì và áp dụng vào đâu.

Sau bài học này, sinh viên có thể:

- **Giải thích** ý nghĩa của ký hiệu Big-O, Big-Omega, Big-Theta.
- **Phân loại** hàm vào các bậc tăng trưởng: hằng, log, tuyến tính, đa thức, mũ.
- **Xác định** Big-O của một hàm cho trước.
- **So sánh** tốc độ tăng trưởng của hai hàm.
- **Áp dụng** quy tắc ước lượng để phân tích vòng lặp.

**Từ khóa**: Big-O, Big-Omega ($$\Omega$$), Big-Theta ($$\Theta$$), tốc độ tăng trưởng (growth rate), bậc (order), trội (dominant term).

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
<div data-demo="big-o-growth-comparator"></div>
</div>
<script src="{{ '/public/js/big-o-growth-comparator.js' | relative_url }}"></script>

## Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Big-O là công cụ chuẩn trong phỏng vấn kỹ thuật và thiết kế hệ thống. Khi xây dựng hệ thống phục vụ hàng triệu người dùng, sự khác biệt giữa $$O(n)$$ và $$O(n^2)$$ là sự khác biệt giữa *chạy được* và *sập server*. Big-O còn là cơ sở để phân loại bài toán P, NP — trung tâm của lý thuyết độ phức tạp tính toán.

**Ví dụ thực tế**: Google xử lý hàng tỷ tìm kiếm mỗi ngày. Nếu thuật toán tìm kiếm của họ là $$O(n^2)$$ thay vì $$O(\log n)$$, họ sẽ cần một trung tâm dữ liệu lớn gấp hàng triệu lần. Big-O quyết định khả thi hay không khả thi.

## Bài tập

Khi làm bài tập, nên bắt đầu bằng cách xác định dữ kiện, dạng bài và công cụ phù hợp trước khi tính toán. Cách tiếp cận này thường giúp tránh sai từ bước đầu.

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

### Bài tập 6: Little-o vs Big-O vs Omega

**A.13** This exercise shows that "f = o(g)" is not always the same as "f = O(g) and f ≠ Ω(g)", even for monotonically nondecreasing functions (f(n) ≤ f(n + 1) and g(n) ≤ g(n + 1) for all n ∈ ℕ). Consider the functions f(n) = ⌊n/2⌋! and g(n) = ⌈n/2⌉!. (Here ! means factorial.)

Verify that:

(a) f ≠ o(g)

(b) f = O(g)

(c) f ≠ Ω(g)

(d) f and g are monotonically nondecreasing

<details>
<summary>Đáp án</summary>

(a) Ta có g(n) = ⌈n/2⌉!, f(n) = ⌊n/2⌋!. Với n chẵn, n = 2k: f(2k) = k!, g(2k) = k!. Khi đó tỉ số f(2k)/g(2k) = 1, không tiến về 0. Với n lẻ, n = 2k+1: f(2k+1) = k!, g(2k+1) = (k+1)!. Tỉ số f/g = k!/(k+1)! = 1/(k+1) → 0. Nhưng định nghĩa f = o(g) yêu cầu lim_{n→∞} f(n)/g(n) = 0, và dãy con n = 2k cho thấy giới hạn không thể bằng 0. Vậy f ≠ o(g).

(b) Với mọi n, ⌊n/2⌋ ≤ ⌈n/2⌉, nên ⌊n/2⌋! ≤ ⌈n/2⌉!, tức f(n) ≤ g(n) với mọi n. Chọn C = 1, n₀ = 1, ta có f(n) = O(g(n)).

(c) Nếu f = Ω(g), tồn tại C > 0, n₀ sao cho f(n) ≥ C·g(n) với mọi n ≥ n₀. Với n chẵn, f(n) = g(n) nên C ≤ 1. Với n lẻ n = 2k+1, f(2k+1) = k!, g(2k+1) = (k+1)! = (k+1)·k!. Tỉ số f/g = 1/(k+1) → 0. Vậy không tồn tại C > 0 thỏa mãn. Do đó f ≠ Ω(g).

(d) Hàm giai thừa là đơn điệu tăng, và cả floor và ceiling đều là hàm không giảm theo n. Với n bất kỳ: n+1 > n ⇒ ⌊(n+1)/2⌋ ≥ ⌊n/2⌋ và ⌈(n+1)/2⌉ ≥ ⌈n/2⌉. Kết hợp với tính đơn điệu của giai thừa, f và g đều không giảm.

</details>

### Bài tập 7: Big-O and Little-o Algebraic Properties

**A.14** Show that the following properties hold, using the definitions of big-O and little-o.

(a) For every constant $$a > 0$$ (not necessarily an integer), if $$f = O(g)$$ then $$f^a = O(g^a)$$.

(b) If $$f_1 = O(g_1)$$ and $$f_2 = o(g_2)$$ then $$f_1 f_2 = o(g_1 g_2)$$.

(c) $$O_\lor$$ is equivalent to $$O_+$$, defined as follows: $$f(m,n) = O_+(g(m,n))$$ when:

$$(\exists c > 0) (\exists n_0 \in \mathbb{N}) (\forall (m,n) \in \mathbb{N}^2) \big( m+n \ge n_0 \Rightarrow f(m,n) \le c \cdot g(m,n) \big)$$

<details>
<summary>Đáp án</summary>

(a) Từ $$f = O(g)$$, tồn tại $$C, n_0$$ sao cho $$f(n) \le C \cdot g(n)$$ với mọi $$n \ge n_0$$. Với $$a > 0$$, lũy thừa bậc $$a$$ là hàm đơn điệu tăng trên $$(0, \infty)$$, nên $$f(n)^a \le (C \cdot g(n))^a = C^a \cdot g(n)^a$$ với mọi $$n \ge n_0$$. Đặt $$C' = C^a$$, ta có $$f^a = O(g^a)$$.

(b) Từ $$f_1 = O(g_1)$$, tồn tại $$C, n_1$$ sao cho $$f_1(n) \le C \cdot g_1(n)$$ với $$n \ge n_1$$. Từ $$f_2 = o(g_2)$$, với mọi $$\varepsilon > 0$$ tồn tại $$n_2$$ sao cho $$|f_2(n)| \le \varepsilon \cdot |g_2(n)|$$ với $$n \ge n_2$$. Với $$n \ge \max(n_1, n_2)$$:

$$|f_1(n) f_2(n)| \le C \cdot g_1(n) \cdot \varepsilon \cdot g_2(n) = (C \varepsilon) \cdot g_1(n) g_2(n).$$

Vì $$\varepsilon$$ có thể chọn tùy ý nhỏ, $$C \varepsilon$$ cũng tùy ý nhỏ. Vậy $$f_1 f_2 = o(g_1 g_2)$$.

(c) Ta chứng minh hai định nghĩa tương đương.

$$(\Rightarrow)$$ Giả sử $$f = O_\lor(g)$$, nghĩa là tồn tại $$c, n_0$$ sao cho với mọi $$m,n$$, nếu $$m \ge n_0$$ hoặc $$n \ge n_0$$ thì $$f(m,n) \le c \cdot g(m,n)$$. Chọn $$n_0' = n_0$$. Với mọi $$(m,n)$$ thỏa $$m+n \ge n_0$$, ta có $$m \ge n_0$$ hoặc $$n \ge n_0$$ (nếu cả hai đều nhỏ hơn $$n_0$$ thì $$m+n < 2n_0$$, không đảm bảo). Cần chọn $$n_0' = 2n_0$$: nếu $$m+n \ge 2n_0$$ thì $$m \ge n_0$$ hoặc $$n \ge n_0$$, nên $$f(m,n) \le c \cdot g(m,n)$$. Vậy $$f = O_+(g)$$.

$$(\Leftarrow)$$ Giả sử $$f = O_+(g)$$, tồn tại $$c, n_0$$ sao cho $$m+n \ge n_0 \Rightarrow f(m,n) \le c \cdot g(m,n)$$. Chọn cùng $$c$$ và $$n_0$$. Với mọi $$(m,n)$$, nếu $$m \ge n_0$$ thì $$m+n \ge n_0$$, nên $$f(m,n) \le c \cdot g(m,n)$$. Tương tự nếu $$n \ge n_0$$. Vậy $$f = O_\lor(g)$$.

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
