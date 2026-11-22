---

layout: post
title: "Giải Quan hệ Truy hồi bằng Hàm sinh"
categories: chapter11
date: 2021-01-01
order: 2
required: true
lang: vi
excerpt: "Áp dụng hàm sinh để giải quan hệ truy hồi theo quy trình 4 bước: chuyển hệ thức đệ quy thành phương trình đại số trên G(x), phân tích phân thức và đọc lại hệ số."
---

Ở mục trước, chúng ta đã định nghĩa hàm sinh $$G(x)=\sum a_n x^n$$. Mục này áp dụng công cụ đó để **giải quan hệ truy hồi**: thay vì xử lý từng số hạng riêng lẻ, ta chuyển cả dãy sang miền hàm, biến hệ thức đệ quy thành phương trình đại số theo $$G(x)$$, rồi khai triển lại để đọc hệ số $$a_n$$. Đây là cách **chuyển đổi biểu diễn** quen thuộc trong khoa học máy tính — tương tự việc chọn cấu trúc dữ liệu phù hợp trước khi xử lý — giúp nhiều bài toán truy hồi phức tạp trở nên dễ giải quyết hơn.

![Dãy Fibonacci](/discrete-mathematics-for-computer-science-iuh/img/course/Fibonacci_spiral.svg)

<p class="textbook-figure-caption" data-figure="11.6">Dãy Fibonacci $$F_n=F_{n-1}+F_{n-2}$$ — ví dụ kinh điển cho phương pháp giải truy hồi bằng hàm sinh.</p>
![Hàm sinh của dãy Fibonacci](/discrete-mathematics-for-computer-science-iuh/img/course/Contour_graph_of_generating_function_for_Fibonacci_numbers.png)

<p class="textbook-figure-caption" data-figure="11.7">Đồ thị đường mức của hàm sinh Fibonacci: nhân truy hồi với $$x^n$$ rồi lấy tổng theo $$n$$ giúp chuyển hệ thức đệ quy thành phương trình theo $$G(x)$$.</p>
![Khai triển chuỗi lũy thừa](/discrete-mathematics-for-computer-science-iuh/img/course/Za_by_Power_Series_Expansion.png)

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Thực hiện** quy trình 4 bước: đặt $$G(x)$$, nhân hai vế truy hồi với $$x^n$$ rồi lấy tổng, giải đại số tìm $$G(x)$$ và khai triển đọc hệ số.
- **Giải** hệ thức truy hồi tuyến tính bậc 1 và bậc 2 (như Fibonacci) bằng hàm sinh.
- **Phân tích** hàm sinh dạng phân thức hữu tỉ thành tổng các phân thức đơn giản.
- **So sánh** phương pháp hàm sinh với phương pháp phương trình đặc trưng (Chương 10).

**Từ khóa**: giải truy hồi bằng hàm sinh, nhân $$x^n$$, phân thức từng phần, Fibonacci, phương trình đặc trưng.
</div>

## Quy trình 4 bước

1. Đặt hàm sinh $$G(x)=\sum_{n\ge0}a_nx^n$$.
2. Nhân hai vế của hệ thức truy hồi với $$x^n$$ rồi lấy tổng theo $$n$$ để thiết lập phương trình theo $$G(x)$$.
3. Giải phương trình đại số để biểu diễn $$G(x)$$ dưới dạng phân thức.
4. Khai triển $$G(x)$$ thành chuỗi lũy thừa để đọc hệ số $$a_n$$.

<div class="textbook-theorem" markdown="1">
**Mấu chốt**: Phép dịch chỉ số trong hệ thức truy hồi tương ứng với việc nhân thêm $$x$$ hoặc $$x^2$$ vào hàm sinh. Nhờ đó, quan hệ đệ quy được chuyển thành phương trình đại số theo $$G(x)$$.
</div>

## Ví dụ Fibonacci

Dưới đây là minh họa đầy đủ quy trình 4 bước cho dãy Fibonacci — hệ thức truy hồi bậc 2 kinh điển có hàm sinh ở dạng phân thức hữu tỉ.

Xét dãy Fibonacci:

<div class="textbook-equation" markdown="1">
$$
F_n=F_{n-1}+F_{n-2},\qquad F_0=0,\;F_1=1.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Đặt:

<div class="textbook-equation" markdown="1">
$$
G(x)=\sum_{n\ge0}F_nx^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Nhân hai vế của hệ thức truy hồi với $$x^n$$ và lấy tổng với $$n\ge2$$:

<div class="textbook-equation" markdown="1">
$$
\sum_{n\ge2}F_nx^n=\sum_{n\ge2}F_{n-1}x^n+\sum_{n\ge2}F_{n-2}x^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Biến đổi các tổng theo $$G(x)$$:

<div class="textbook-equation" markdown="1">
$$
G(x)-F_0-F_1x=x\big(G(x)-F_0\big)+x^2G(x).
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Thay điều kiện đầu $$F_0=0$$ và $$F_1=1$$:

<div class="textbook-equation" markdown="1">
$$
G(x)-x=xG(x)+x^2G(x).
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Giải tìm $$G(x)$$, ta thu được:

<div class="textbook-equation" markdown="1">
$$
G(x)=\frac{x}{1-x-x^2}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Từ biểu thức phân thức này, ta có thể khai triển để suy ra công thức tường minh cho $$F_n$$.

## Phân thức từng phần

Khi hàm sinh có dạng phân thức hữu tỉ, ta thường phân tích nó thành tổng các phân thức đơn giản hơn. Chẳng hạn, phân thức

<div class="textbook-equation" markdown="1">
$$
\frac{x}{1-x-x^2}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
có thể được tách dựa trên nhân tử của mẫu số để thu về tổ hợp tuyến tính của hai dãy lũy thừa, khớp với kết quả từ phương trình đặc trưng.

**Nhận xét**: Phương trình đặc trưng và hàm sinh thực chất là hai cách tiếp cận khác nhau dẫn đến cùng một công thức nghiệm.

## Ví dụ truy hồi bậc 1

Giải hệ thức truy hồi:

<div class="textbook-equation" markdown="1">
$$
a_n=2a_{n-1}+1,\qquad a_0=0.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Đặt $$G(x)=\sum_{n\ge0}a_nx^n$$. Với $$n\ge1$$, nhân hai vế với $$x^n$$ rồi lấy tổng:

<div class="textbook-equation" markdown="1">
$$
\sum_{n\ge1}a_nx^n=2\sum_{n\ge1}a_{n-1}x^n+\sum_{n\ge1}x^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Chuyển về phương trình theo $$G(x)$$:

<div class="textbook-equation" markdown="1">
$$
G(x)-a_0=2xG(x)+\frac{x}{1-x}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Do $$a_0=0$$, ta rút ra:

<div class="textbook-equation" markdown="1">
$$
G(x)=\frac{x}{(1-x)(1-2x)}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Phân tích $$G(x)$$ thành tổng các phân thức đơn giản sẽ cho công thức đóng của $$a_n$$.

<div class="interactive-demo" markdown="1">
**Demo tương tác đề xuất**: Chọn một hệ thức truy hồi bậc 1 hoặc bậc 2; công cụ sẽ tự động dựng phương trình cho $$G(x)$$ và hiển thị bước chuyển từ truy hồi sang phương trình đại số.
<div data-demo="gf-recurrence-solver"></div>
</div>
<script src="{{ '/public/js/gf-recurrence-solver.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Giải hệ thức truy hồi $$a_n = 3a_{n-1}$$, $$a_0 = 2$$ bằng hàm sinh và tìm công thức đóng của $$a_n$$.

<details>
<summary>Đáp án</summary>

Đặt $$G(x) = \sum_{n\ge 0} a_n x^n$$. Nhân hai vế với $$x^n$$ và lấy tổng với $$n \ge 1$$, ta được $$G(x) - a_0 = 3x G(x)$$, suy ra $$G(x) = \frac{2}{1-3x}$$. Khai triển chuỗi hình học cho kết quả $$a_n = 2 \cdot 3^n$$.

</details>

### Bài tập 2

Với dãy Fibonacci có $$G(x) = x/(1-x-x^2)$$, giải thích vì sao nghiệm đóng có dạng tổ hợp tuyến tính của hai lũy thừa (không cần tính cụ thể giá trị số).

<details>
<summary>Đáp án</summary>

Gọi $$r_1, r_2$$ là hai nghiệm của phương trình đặc trưng $$r^2 - r - 1 = 0$$ (khi đó $$1/r_1, 1/r_2$$ là nghiệm của mẫu $$1 - x - x^2 = 0$$), ta phân tích được mẫu số thành $$1 - x - x^2 = (1 - r_1 x)(1 - r_2 x)$$. Phân tích phân thức từng phần cho dạng $$\frac{A}{1-r_1 x} + \frac{B}{1-r_2 x}$$, và khi khai triển thành chuỗi lũy thừa, hệ số của $$x^n$$ là $$A r_1^n + B r_2^n$$ — trùng khớp với kết quả từ phương trình đặc trưng ở Chương 10.

</details>

### Bài tập 3

Cho hệ thức truy hồi $$a_n = a_{n-1} + n$$, $$a_0 = 0$$. Tìm hàm sinh $$G(x)$$.

<details>
<summary>Đáp án</summary>

Ta có $$G(x) = x G(x) + \frac{x}{(1-x)^2}$$ (do $$\sum_{n\ge 1} n x^n = \frac{x}{(1-x)^2}$$). Suy ra $$G(x) = \frac{x}{(1-x)^3}$$, nên $$a_n = \binom{n+1}{2}$$.

</details>

### Bài tập 4

So sánh ưu điểm và hạn chế của phương pháp hàm sinh so với phương trình đặc trưng khi giải truy hồi bậc 2.

<details>
<summary>Đáp án</summary>

**Phương trình đặc trưng**: nhanh và trực tiếp để viết ra $$a_n$$ đối với truy hồi tuyến tính hệ số hằng, đặc biệt khi nghiệm đơn. **Hàm sinh**: linh hoạt hơn khi truy hồi có vế tự do $$f(n)$$ phức tạp, khi cần làm việc với hàm sinh xác suất hoặc kết hợp bài toán đếm với truy hồi thông qua biến đổi đại số trên $$G(x)$$.

</details>

---

## Xem thêm / Video gợi ý

- [Injective, Surjective, Bijective](https://www.youtube.com/watch?v=2jZ5n8k0p0Q) — 3Blue1Brown (Visual explanation)

## Tóm tắt

- **Quy trình 4 bước**: đặt $$G(x)=\sum a_n x^n$$; nhân truy hồi với $$x^n$$ rồi lấy tổng; giải phương trình đại số tìm $$G(x)$$; khai triển để đọc hệ số.
- Phép dịch chỉ số trong truy hồi tương ứng với việc nhân $$x$$ hoặc $$x^2$$ vào hàm sinh.
- Dãy Fibonacci có $$G(x) = x/(1-x-x^2)$$, cho kết quả tương đương phương trình đặc trưng.
- **Phân tích phân thức từng phần** giúp chuyển hàm sinh hữu tỉ về các chuỗi chuẩn để đọc công thức đóng $$a_n$$.
- Với truy hồi bậc 1 không thuần nhất, chẳng hạn $$a_n=2a_{n-1}+1$$, ta thu được $$G(x)=x/((1-x)(1-2x))$$.

Ở bài tiếp theo, chúng ta sẽ tìm hiểu **nguyên lý bao hàm–loại trừ** — công cụ đếm khi các tập hợp có phần giao nhau.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=Xf-mnh65CaU">RECURRENCE RELATIONS using GENERATING FUNCTIONS - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giới thiệu cách giải quan hệ truy hồi bằng hàm sinh.
- <a href="https://www.youtube.com/watch?v=fyDQlPNQ_y0">[Discrete Mathematics] Partial Fraction Decomposition</a> — TrevTutor, tiếng Anh. Kỹ thuật phân tích phân thức từng phần cho bước rút hệ số.
- <a href="https://www.youtube.com/watch?v=ZyUb5UxBA9Q">[Discrete Mathematics] Coefficient Extraction and Extended Binomial Theorem</a> — TrevTutor, tiếng Anh. Cách trích xuất hệ số và áp dụng định lý nhị thức mở rộng.
