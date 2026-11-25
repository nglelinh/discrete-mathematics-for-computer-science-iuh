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

Ở Chương 10, muốn giải truy hồi tuyến tính bạn phải ghi nhớ riêng nhiều trường hợp: thuần nhất, không thuần nhất, nghiệm bội, cộng hưởng... Nhưng khi bước sang miền **hàm sinh**, tất cả những quy tắc rời rạc ấy bỗng hợp nhất thành **một quy trình đại số duy nhất gồm 4 bước** — không cần đoán dạng nghiệm riêng và tự động xử lý gọn cả điều kiện đầu ngay từ dòng đầu tiên!

**Mạch bài học:** Quy trình 4 bước chuyển truy hồi sang phương trình theo $$G(x)$$ $$\longrightarrow$$ giải đại số tìm biểu thức đóng của $$G(x)$$ $$\longrightarrow$$ **phân tách phân thức từng phần (partial fractions)** $$\longrightarrow$$ đọc ngược hệ số $$a_n = [x^n]G(x)$$.

## Bản đồ kiến thức nền: Hàm sinh biến đổi bài toán truy hồi như thế nào?

- **Phép biến đổi miền (Transform Method):** Giống biến đổi Laplace trong phương trình vi phân hay biến đổi Z trong xử lý tín hiệu số, hàm sinh chuyển phép **dịch chỉ số** ($$a_{n-1} \mapsto x G(x)$$) thành phép **nhân với $$x$$** — biến phương trình truy hồi thành phương trình đại số bậc nhất theo $$G(x)$$.
- **Phân tách phân thức từng phần (Partial Fraction Decomposition):** Mọi hàm hữu tỷ thực sự $$\frac{P(x)}{Q(x)}$$ đều tách được thành tổng các phân thức sơ cấp dạng $$\frac{A}{(1 - rx)^m}$$, mà mỗi phân thức sơ cấp đều có khai triển chuỗi lũy thừa đóng tường minh!
- **Thống nhất mọi trường hợp của Chương 10:** Nghiệm bội và cộng hưởng không còn là "luật ngoại lệ" phải học thuộc — chúng tự nhiên xuất hiện dưới dạng mẫu số bậc cao $$(1 - rx)^2$$, lập tức sinh ra thừa số $$(n+1)r^n$$ khi khai triển bằng nhị thức mở rộng.

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

## Ví dụ tính tay cầm tay chỉ việc: Giải $$a_n = 3a_{n-1} + 2^n$$ ($$n \ge 1$$), $$a_0 = 1$$ bằng Hàm sinh

Hãy chạy trọn 4 bước mà **không cần** tách nghiệm thuần nhất hay đoán nghiệm riêng:

1. **Bước 1 — Nhân hai vế với $$x^n$$ rồi lấy tổng từ $$n = 1$$ đến $$\infty$$:**
   $$\sum_{n=1}^{\infty} a_n x^n = 3 \sum_{n=1}^{\infty} a_{n-1} x^n + \sum_{n=1}^{\infty} 2^n x^n.$$
2. **Bước 2 — Biểu diễn từng tổng qua $$G(x) = \sum_{n=0}^{\infty} a_n x^n$$:**
   - Vế trái: $$G(x) - a_0 = G(x) - 1$$.
   - Tổng thứ nhất vế phải: $$3x \sum_{n=1}^{\infty} a_{n-1} x^{n-1} = 3x G(x)$$.
   - Tổng thứ hai vế phải: $$\frac{2x}{1 - 2x}$$ (vì tổng bắt đầu từ $$n=1$$, tức $$2x + 4x^2 + 8x^3 + \cdots$$).
   - Ghép lại thành phương trình đại số:
     $$G(x) - 1 = 3x G(x) + \frac{2x}{1 - 2x} \iff (1 - 3x)G(x) = 1 + \frac{2x}{1 - 2x} = \frac{1}{1 - 2x}.$$
   - Suy ra biểu thức đóng gọn bất ngờ:
     $$G(x) = \frac{1}{(1 - 3x)(1 - 2x)}.$$
3. **Bước 3 — Tách phân thức từng phần:**
   Đặt $$\frac{1}{(1 - 3x)(1 - 2x)} = \frac{A}{1 - 3x} + \frac{B}{1 - 2x}$$.
   - Nhân quy đồng: $$A(1 - 2x) + B(1 - 3x) = 1$$.
   - Thay $$x = \frac{1}{3}$$: $$A\left(1 - \frac{2}{3}\right) = 1 \Rightarrow A = 3$$.
   - Thay $$x = \frac{1}{2}$$: $$B\left(1 - \frac{3}{2}\right) = 1 \Rightarrow B = -2$$.
   - Vậy $$G(x) = \frac{3}{1 - 3x} - \frac{2}{1 - 2x}$$.
4. **Bước 4 — Khai triển chuỗi hình học và đọc hệ số $$[x^n]$$:**
   $$G(x) = 3\sum_{n=0}^{\infty} 3^n x^n - 2\sum_{n=0}^{\infty} 2^n x^n = \sum_{n=0}^{\infty} \left(3^{n+1} - 2^{n+1}\right) x^n \;\Longrightarrow\; a_n = 3^{n+1} - 2^{n+1}.$$
   - **Kiểm tra tay:** $$n=0 \Rightarrow 3 - 2 = 1$$ (khớp $$a_0$$); $$n=1 \Rightarrow 9 - 4 = 5$$ (truy hồi: $$3(1)+2=5$$); $$n=2 \Rightarrow 27 - 8 = 19$$ (truy hồi: $$3(5)+4=19$$). Hoàn toàn chính xác!

### Khung giải thích: Tại sao phương pháp hàm sinh là "cỗ máy tự động" (nên đọc chậm)

1. **Bước 1 — Cẩn thận chỉ số bắt đầu của tổng:** Luôn kiểm tra hệ thức truy hồi đúng từ $$n = 1$$ hay $$n = 2$$, và trừ đúng các số hạng đầu ($$a_0$$, $$a_1 x$$) khi viết vế trái theo $$G(x)$$.
2. **Bước 2 — Gom mọi số hạng chứa $$G(x)$$ về một vế:** Hệ số đứng trước $$G(x)$$ chính là đa thức nghịch đảo của đa thức đặc trưng (ví dụ $$1 - 3x$$ ứng với $$r = 3$$).
3. **Bước 3 — Tách về hai mẫu số chuẩn duy nhất:** Nhớ hai công thức tra bảng: $$\frac{1}{1 - rx} = \sum r^n x^n$$ và $$\frac{1}{(1 - rx)^k} = \sum \binom{n+k-1}{k-1} r^n x^n$$.
4. **Bước 4 — Tự kiểm tra 3 số hạng đầu:** Thế $$n = 0, 1, 2$$ vào công thức vừa tìm và đối chiếu với truy hồi gốc — bất kỳ sai dấu nhỏ nào khi tách phân thức sẽ lộ ngay lập tức.

$$\text{Truy hồi } a_n \;\xrightarrow{\sum \cdot x^n}\; \text{PT đại số } G(x) \;\xrightarrow{\text{Partial Fractions}}\; \sum \frac{A_i}{(1 - r_i x)^{m_i}} \;\xrightarrow{[x^n]}\; \text{Công thức đóng } a_n.$$

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
