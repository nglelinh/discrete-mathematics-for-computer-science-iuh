---

layout: post
title: "Giải Quan hệ Truy hồi bằng Hàm sinh"
categories: chapter11
date: 2021-01-01
order: 2
required: true
lang: vi
excerpt: "Ở mục trước chúng ta đã định nghĩa hàm sinh . Mục này áp dụng công cụ đó để giải quan hệ truy hồi: thay vì bám vào từng số hạng, chúng ta chuyển cả dãy sang…"
---

Ở mục trước chúng ta đã định nghĩa hàm sinh $$G(x)=\sum a_n x^n$$. Mục này áp dụng công cụ đó để **giải quan hệ truy hồi**: thay vì bám vào từng số hạng, chúng ta chuyển cả dãy sang miền hàm, biến quan hệ đệ quy thành phương trình đại số trên $$G(x)$$, rồi khai triển lại để đọc hệ số $$a_n$$. Đây là cách **đổi biểu diễn** phổ biến trong khoa học máy tính — tương tự chọn cấu trúc dữ liệu phù hợp trước khi xử lý — và nhiều truy hồi khó trên giấy trở nên xử lý được sau bước biến đổi này.

![Dãy Fibonacci](/discrete-mathematics-for-computer-science-iuh/img/course/Fibonacci_spiral.svg)

<p class="textbook-figure-caption" data-figure="11.6">Dãy Fibonacci $F_n=F_{n-1}+F_{n-2}$ — ví dụ kinh điển giải truy hồi bằng hàm sinh.</p>
![Hàm sinh của dãy Fibonacci](/discrete-mathematics-for-computer-science-iuh/img/course/Contour_graph_of_generating_function_for_Fibonacci_numbers.png)

<p class="textbook-figure-caption" data-figure="11.7">Đồ thị contour của hàm sinh Fibonacci — nhân truy hồi với $x^n$ rồi cộng theo $n$ biến quan hệ đệ quy thành phương trình trên $G(x)$.</p>
![Khai triển chuỗi lũy thừa](/discrete-mathematics-for-computer-science-iuh/img/course/Za_by_Power_Series_Expansion.png)

<p class="textbook-figure-caption" data-figure="11.8">Khai triển chuỗi lũy thừa — sau khi tìm $G(x)$ dạng phân thức, mở rộng lại để đọc hệ số $a_n$.</p>
![Dãy hình học](/discrete-mathematics-for-computer-science-iuh/img/course/Geometric_sequence.svg)

<p class="textbook-figure-caption" data-figure="11.9">Truy hồi bậc 1 thường cho hàm sinh chứa nhân tử $1/(1-rx)$ — dãy hình học.</p>
![Cây quyết định phân tích](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="11.10">Phân tích truy hồi theo từng bước — tư duy hệ thống giống duyệt cây trong thuật toán.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Thực hiện** quy trình 4 bước: đặt $$G(x)$$, nhân truy hồi, giải đại số, khai triển hệ số.
- **Giải** truy hồi tuyến tính bậc 1 và bậc 2 (Fibonacci) bằng hàm sinh.
- **Phân tích** hàm sinh dạng phân thức hữu tỉ thành phần đơn.
- **So sánh** phương pháp hàm sinh với phương trình đặc trưng (Ch.10).

**Từ khóa**: giải truy hồi bằng hàm sinh, nhân $$x^n$$, phân thức từng phần, Fibonacci, phương trình đặc trưng.
</div>

## Quy trình 4 bước

1. Đặt hàm sinh $G(x)=\sum_{n\ge0}a_nx^n$.
2. Nhân truy hồi với $x^n$ rồi cộng theo $n$ để tạo phương trình cho $G(x)$.
3. Giải đại số để tìm $G(x)$ dưới dạng phân thức.
4. Khai triển lại để đọc hệ số $a_n$.

<div class="textbook-theorem" markdown="1">
**Mấu chốt**: Dịch chỉ số trong truy hồi tương ứng với nhân thêm $$x$$ hoặc $$x^2$$ trong hàm sinh. Quan hệ đệ quy biến thành phương trình đại số trên $$G(x)$$.
</div>

## Ví dụ Fibonacci

Dưới đây là minh họa đầy đủ quy trình 4 bước vừa nêu, áp dụng cho dãy Fibonacci — truy hồi bậc 2 kinh điển mà hàm sinh biến thành phân thức hữu tỉ.

Xét dãy Fibonacci

<div class="textbook-equation" markdown="1">
$$
F_n=F_{n-1}+F_{n-2},\qquad F_0=0,\;F_1=1.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Đặt

<div class="textbook-equation" markdown="1">
$$
G(x)=\sum_{n\ge0}F_nx^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Nhân hai vế truy hồi với $x^n$ và cộng từ $n\ge2$:

<div class="textbook-equation" markdown="1">
$$
\sum_{n\ge2}F_nx^n=\sum_{n\ge2}F_{n-1}x^n+\sum_{n\ge2}F_{n-2}x^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Ta viết lại:

<div class="textbook-equation" markdown="1">
$$
G(x)-F_0-F_1x=x\big(G(x)-F_0\big)+x^2G(x).
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Vì $F_0=0$ và $F_1=1$,

<div class="textbook-equation" markdown="1">
$$
G(x)-x=xG(x)+x^2G(x).
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Suy ra

<div class="textbook-equation" markdown="1">
$$
G(x)=\frac{x}{1-x-x^2}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Từ đó, ta có thể khai triển phân thức để thu được công thức tường minh cho $F_n$.

## Phân thức từng phần

Nếu hàm sinh là phân thức hữu tỉ, ta thường phân tích thành tổng các phân thức đơn giản hơn. Ví dụ

<div class="textbook-equation" markdown="1">
$$
\frac{x}{1-x-x^2}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
có thể phân tích theo nghiệm của mẫu số để thu lại dạng kết hợp hai lũy thừa, khớp với kết quả từ phương trình đặc trưng.

**Nhận xét**: Phương trình đặc trưng và hàm sinh thực chất là hai con đường khác nhau dẫn tới cùng một nghiệm.

## Ví dụ truy hồi bậc 1

Giải

<div class="textbook-equation" markdown="1">
$$
a_n=2a_{n-1}+1,\qquad a_0=0.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Đặt $G(x)=\sum_{n\ge0}a_nx^n$. Với $n\ge1$,

<div class="textbook-equation" markdown="1">
$$
\sum_{n\ge1}a_nx^n=2\sum_{n\ge1}a_{n-1}x^n+\sum_{n\ge1}x^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Ta có

<div class="textbook-equation" markdown="1">
$$
G(x)-a_0=2xG(x)+\frac{x}{1-x}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Vì $a_0=0$,

<div class="textbook-equation" markdown="1">
$$
G(x)=\frac{x}{(1-x)(1-2x)}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Phân tích thành phần đơn sẽ cho công thức đóng của $a_n$.

<div class="interactive-demo" markdown="1">
**Demo tương tác đề xuất**: Chọn một truy hồi bậc 1 hoặc bậc 2, công cụ tự động dựng phương trình cho $G(x)$ và hiển thị bước chuyển từ truy hồi sang phương trình đại số.
<div data-demo="gf-recurrence-solver"></div>
</div>
<script src="{{ '/public/js/gf-recurrence-solver.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Giải truy hồi $$a_n = 3a_{n-1}$$, $$a_0 = 2$$ bằng hàm sinh. Tìm công thức đóng $$a_n$$.

<details>
<summary>Đáp án</summary>

$$G(x) = \sum a_n x^n$$. Nhân truy hồi: $$G(x) - a_0 = 3x G(x)$$, suy ra $$G(x) = \frac{2}{1-3x}$$. Vậy $$a_n = 2 \cdot 3^n$$.

</details>

### Bài tập 2

Với Fibonacci, từ $$G(x) = x/(1-x-x^2)$$, giải thích vì sao nghiệm đóng có dạng tổ hợp hai lũy thừa (không cần tính số).

<details>
<summary>Đáp án</summary>

Mẫu $$1 - x - x^2 = 0$$ có hai nghiệm $$r_1, r_2$$. Phân tích thành phần đơn cho $$\frac{A}{1-r_1 x} + \frac{B}{1-r_2 x}$$, khai triển mỗi số hạng là $$r_i^n$$ — trùng kết quả phương trình đặc trưng Ch.10.

</details>

### Bài tập 3

Truy hồi $$a_n = a_{n-1} + n$$, $$a_0 = 0$$. Tìm $$G(x)$$.

<details>
<summary>Đáp án</summary>

$$G(x) = x G(x) + \frac{x}{(1-x)^2}$$ (vì $$\sum n x^n = x/(1-x)^2$$). Suy ra $$G(x) = \frac{x}{(1-x)^3}$$, tức $$a_n = \binom{n+1}{2}$$.

</details>

### Bài tập 4

So sánh ưu/nhược điểm của hàm sinh và phương trình đặc trưng khi giải truy hồi bậc 2.

<details>
<summary>Đáp án</summary>

**Đặc trưng**: nhanh, trực tiếp cho $$a_n$$ nếu nghiệm đơn. **Hàm sinh**: mạnh hơn khi truy hồi có $$f(n)$$ phức tạp, khi cần hàm sinh xác suất, hoặc khi đếm kết hợp truy hồi — đổi sang đại số trên $$G(x)$$.

</details>

---

## Xem thêm / Video gợi ý

- [Injective, Surjective, Bijective](https://www.youtube.com/watch?v=2jZ5n8k0p0Q) — 3Blue1Brown (Visual explanation)

## Tóm tắt

- **Quy trình 4 bước**: đặt $$G(x)=\sum a_n x^n$$; nhân truy hồi với $$x^n$$ và cộng; giải đại số; khai triển lấy hệ số.
- Dịch chỉ số trong truy hồi tương ứng nhân $$x$$ hoặc $$x^2$$ trong hàm sinh.
- Fibonacci: $$G(x) = x/(1-x-x^2)$$ — tương đương phương trình đặc trưng.
- **Phân thức từng phần** trên hàm sinh hữu tỉ để đọc công thức đóng $$a_n$$.
- Truy hồi bậc 1 không thuần nhất: ví dụ $$a_n=2a_{n-1}+1$$ cho $$G(x)=x/((1-x)(1-2x))$$.

Trong bài tiếp theo, chúng ta học **nguyên lý bao hàm–loại trừ** — công cụ đếm khi các tập con có giao nhau.
