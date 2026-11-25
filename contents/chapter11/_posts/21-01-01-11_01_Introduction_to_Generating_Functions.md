---

layout: post
title: "Giới thiệu Hàm sinh"
categories: chapter11
date: 2021-01-01
order: 1
required: true
lang: vi
excerpt: "Giới thiệu hàm sinh (generating function) — công cụ đóng gói một dãy vô hạn thành một chuỗi lũy thừa hình thức để thao tác bằng đại số trong bài toán đếm và truy hồi."
---

<div class="textbook-epigraph" markdown="1">

"Generating functions are a bridge between discrete structures and continuous analysis."

<span class="epigraph-attribution">— Herbert Wilf (paraphrased)</span>

</div>


Hãy hình dung bạn có cả một dãy số vô hạn $$a_0, a_1, a_2, \dots$$ — thay vì giữ từng con số rời rạc trong đầu, bạn "treo" chúng lên một sợi dây phơi vô hạn gắn nhãn $$1, x, x^2, x^3, \dots$$ để tạo thành một biểu thức duy nhất $$G(x) = \sum_{n=0}^{\infty} a_n x^n$$. Phép đóng gói kỳ diệu ấy — gọi là **hàm sinh (generating function)** — biến những bài toán đếm tổ hợp hóc búa thành các phép nhân, chia đa thức hoàn toàn cơ học!

**Mạch bài học:** Định nghĩa **hàm sinh thường (OGF)** và **chuỗi lũy thừa hình thức** $$\longrightarrow$$ từ điển ánh xạ giữa phép toán dãy và phép toán trên $$G(x)$$ $$\longrightarrow$$ các **hàm sinh chuẩn** (cấp số nhân, nhị thức mở rộng) $$\longrightarrow$$ ứng dụng đếm nghiệm nguyên và tổ hợp có ràng buộc.

## Bản đồ kiến thức nền: Hàm sinh và chuỗi lũy thừa hình thức nghiên cứu gì?

- **Vành chuỗi lũy thừa hình thức (Formal Power Series $$\mathbb{R}[[x]]$$):** Khác với giải tích thực nơi ta phải lo bán kính hội tụ, trong tổ hợp $$x$$ chỉ là một **biến đánh dấu vị trí (placeholder)**. Ta cộng, nhân, lấy đạo hàm hình thức chuỗi lũy thừa để theo dõi hệ số $$[x^n]G(x)$$ mà không cần thay giá trị số cho $$x$$.
- **Tích chập Cauchy & Bài toán đếm phân hoạch (Convolution & Counting):** Khi nhân hai hàm sinh $$A(x)B(x)$$, hệ số của $$x^n$$ tự động là tổng tích chập $$\sum_{k=0}^n a_k b_{n-k}$$ — đúng bằng quy tắc cộng–nhân khi chọn hai thành phần độc lập có tổng kích thước bằng $$n$$!
- **Định lý Nhị thức mở rộng (Extended Binomial Theorem):** Khai triển $$(1-x)^{-k} = \sum_{n=0}^{\infty} \binom{n+k-1}{k-1} x^n$$ kết nối trực tiếp đại số hàm hữu tỷ với bài toán tổ hợp lặp (stars and bars) đã học ở Chương 7.

Trong chương này, chúng ta tìm hiểu về **hàm sinh** (generating function) — công cụ đóng gói một dãy vô hạn $$a_0, a_1, a_2, \ldots$$ vào một biểu thức duy nhất $$G(x) = \sum_{n\ge 0} a_n x^n$$ để có thể thao tác bằng các phép biến đổi đại số. Thay vì liệt kê từng số hạng rời rạc, ta làm việc trên chuỗi lũy thừa hình thức; các phép cộng, nhân, dịch chỉ số và đạo hàm trên $$G(x)$$ phản ánh trực tiếp cấu trúc của bài toán đếm hoặc hệ thức truy hồi phía sau. Dưới góc nhìn khoa học máy tính, đây là một cách **chuyển đổi biểu diễn** — tương tự việc chọn cấu trúc dữ liệu phù hợp trước khi xử lý — giúp lời giải ngắn gọn và có hệ thống hơn.

Bài học này trình bày định nghĩa hàm sinh, ký hiệu trích xuất hệ số $$[x^n]G(x)$$ và các phép toán cơ bản trên hàm sinh.

![Chuỗi lũy thừa hình thức](/discrete-mathematics-for-computer-science-iuh/img/course/Laurent_series.svg)

<p class="textbook-figure-caption" data-figure="11.1">Chuỗi lũy thừa $$G(x)=\sum a_n x^n$$, trong đó mỗi hệ số $$a_n$$ mã hóa một số hạng của dãy.</p>
![Hàm sinh (generating function)](/discrete-mathematics-for-computer-science-iuh/img/course/R._V._Lapshin__Generating_functions_and_squares.png)

<p class="textbook-figure-caption" data-figure="11.2">Hàm sinh đóng gói toàn bộ dãy số vào một biểu thức duy nhất để thao tác bằng đại số.</p>
![Leonhard Euler](/discrete-mathematics-for-computer-science-iuh/img/course/Leonhard_Euler.jpg)

<p class="textbook-figure-caption" data-figure="11.3">Leonhard Euler (1707–1783), nhà toán học đặt nền móng cho lý thuyết hàm sinh và chuỗi lũy thừa.</p>
![Dãy số học](/discrete-mathematics-for-computer-science-iuh/img/course/Arithmetic_progression.svg)

<p class="textbook-figure-caption" data-figure="11.4">Cấp số cộng là một ví dụ cơ bản với các hệ số tăng tuyến tính, tương ứng với cấu trúc đếm đơn giản.</p>
![Ký hiệu tổng Σ](/discrete-mathematics-for-computer-science-iuh/img/course/Sigma_summation_notation.svg)

<p class="textbook-figure-caption" data-figure="11.5">Ký hiệu tổng Σ liên kết hàm sinh với các tổng hữu hạn và vô hạn trong toán tổ hợp.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** hàm sinh thông thường $$G(x)=\sum a_n x^n$$ và ký hiệu hệ số $$[x^n]G(x)$$.
- **Phân biệt** chuỗi lũy thừa hình thức và chuỗi hội tụ trong ngữ cảnh toán rời rạc.
- **Áp dụng** các phép cộng, nhân, dịch chỉ số và đạo hàm trên hàm sinh.
- **Nhận biết** các hàm sinh cơ bản: cấp số nhân, nhị thức và hệ số tổ hợp.
- **Giải thích** vai trò của hàm sinh trong bài toán đếm, phân tích thuật toán và mô hình trạng thái.

**Từ khóa**: hàm sinh (generating function), chuỗi lũy thừa hình thức (formal power series), hệ số $$[x^n]$$, phép nhân Cauchy, hàm sinh hình học.
</div>

## Định nghĩa hàm sinh

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Cho dãy số $$a_0, a_1, a_2, \ldots$$. **Hàm sinh thông thường** (ordinary generating function, OGF) của dãy là

$$G(x) = \sum_{n=0}^{\infty} a_n x^n = a_0 + a_1 x + a_2 x^2 + \cdots$$

Ký hiệu $$[x^n]G(x) = a_n$$ biểu thị $$a_n$$ là hệ số của $$x^n$$ trong khai triển của $$G(x)$$.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**: Dãy hằng $$1, 1, 1, \ldots$$ có hàm sinh

$$G(x) = 1 + x + x^2 + \cdots = \frac{1}{1-x}$$

(xét như chuỗi lũy thừa hình thức, hoặc như chuỗi hội tụ khi $$\vert x\vert  < 1$$).
</div>

## Chuỗi lũy thừa hình thức

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Chuỗi lũy thừa hình thức** là đối tượng đại số $$G(x) = \sum_{n \ge 0} a_n x^n$$, trong đó ta chỉ quan tâm đến dãy **hệ số** $$a_n$$ mà không cần xét miền hội tụ của biến $$x$$.
</div>

Hai chuỗi lũy thừa hình thức bằng nhau khi và chỉ khi mọi hệ số tương ứng của chúng bằng nhau. Cách tiếp cận này cho phép thực hiện các phép toán đại số (cộng, nhân, đạo hàm) trên dãy số mà không phải kiểm tra điều kiện hội tụ.

## Các phép toán cơ bản

| Phép toán trên dãy | Tác động lên $$G(x)$$ |
|:---|:---|
| $$b_n = a_n + c_n$$ | $$B(x) = A(x) + C(x)$$ |
| $$b_n = \sum_{k=0}^{n} a_k c_{n-k}$$ (tích chập) | $$B(x) = A(x) \cdot C(x)$$ |
| $$b_n = a_{n-1}$$ ($$n \ge 1$$), $$b_0 = 0$$ | $$B(x) = x \cdot A(x)$$ |
| $$b_n = (n+1) a_{n+1}$$ | $$B(x) = A'(x)$$ |

<div class="textbook-theorem" markdown="1">
**Định lý** (phép nhân Cauchy): Nếu $$A(x) = \sum a_n x^n$$ và $$C(x) = \sum c_n x^n$$ thì hệ số của $$x^n$$ trong tích $$A(x) \cdot C(x)$$ là

$$[x^n](A \cdot C) = \sum_{k=0}^{n} a_k c_{n-k}$$

Đây chính là công thức **tích chập** — cơ sở cho các bài toán đếm có cấu trúc (chọn $$k$$ phần tử từ cấu hình A và $$n-k$$ phần tử từ cấu hình C).
</div>

<div class="textbook-example" markdown="1">
**Ví dụ** (dịch chỉ số): Dãy Fibonacci thỏa mãn hệ thức $$F_n = F_{n-1} + F_{n-2}$$. Khi nhân hai vế với $$x^n$$ rồi lấy tổng theo $$n$$, phép dịch chỉ số $$F_{n-1}$$ tương ứng với việc nhân $$G(x)$$ với $$x$$, còn dịch chỉ số $$F_{n-2}$$ tương ứng với việc nhân $$G(x)$$ với $$x^2$$. Nội dung này sẽ được trình bày chi tiết ở mục 11.2.
</div>

## Hàm sinh chuẩn

Các công thức dưới đây xuất hiện thường xuyên trong các bài toán hàm sinh:

| Dãy $$a_n$$ | Hàm sinh $$G(x)$$ |
|:---|:---|
| $$1, 1, 1, \ldots$$ | $$\dfrac{1}{1-x}$$ |
| $$0, 1, 2, 3, \ldots$$ ($$a_n = n$$) | $$\dfrac{x}{(1-x)^2}$$ |
| $$\binom{n+k}{k}$$ | $$\dfrac{1}{(1-x)^{k+1}}$$ |
| $$1, 0, 1, 0, \ldots$$ | $$\dfrac{1}{1-x^2}$$ |

<div class="textbook-example" markdown="1">
**Ví dụ** (đếm cách đổi tiền): Có bao nhiêu cách tạo tổng giá trị $$n$$ từ các đồng xu mệnh giá 1đ và 2đ? Mỗi cách chọn tương ứng với một tổ hợp các đồng 1đ và 2đ, nên hàm sinh của bài toán là tích

$$G(x) = \frac{1}{1-x} \cdot \frac{1}{1-x^2}$$

Hệ số $$[x^n]G(x)$$ cho biết trực tiếp đáp số mà không cần liệt kê từng phương án.
</div>

## Ứng dụng trong Khoa học Máy tính

Hàm sinh được dùng để đếm cấu hình, phân tích thuật toán, mô hình hóa trạng thái động và tìm công thức cho số cách phân rã một đối tượng tổ hợp. Trong lập trình sinh ngẫu nhiên và tính toán ký hiệu, hàm sinh còn cho phép xác định phân phối kích thước của các đối tượng được tạo ra.

```python
def coeffs(seq):
    return " + ".join(f"{a}x^{i}" if i else str(a) for i, a in enumerate(seq))

print(coeffs([1, 1, 1, 1]))
```


## Công cụ tương tác

Nhập một dãy ngắn để xem hàm sinh tương ứng và thử khai triển một vài số hạng đầu.
<div class="interactive-demo" markdown="1">
<div data-demo="generating-function-explorer"></div>
</div>
<script src="{{ '/public/js/generating-function-explorer.js' | relative_url }}"></script>

## Ví dụ tính tay cầm tay chỉ việc: Đếm số cách đổi 4 đồng bằng hàm sinh

Giả sử bạn muốn chọn **tổng cộng 4 viên kẹo** từ 3 loại (Dâu, Cam, Chanh) với ràng buộc:
- Kẹo Dâu: chọn tối đa **2 viên** ($$0, 1, 2$$).
- Kẹo Cam: chọn số **chẵn** viên ($$0, 2, 4, \dots$$).
- Kẹo Chanh: chọn bao nhiêu cũng được ($$0, 1, 2, \dots$$).

1. **Bước 1 — Dịch từng ràng buộc thành một nhân tử hàm sinh:**
   - Dâu: $$1 + x + x^2 = \frac{1 - x^3}{1 - x}$$.
   - Cam: $$1 + x^2 + x^4 + \cdots = \frac{1}{1 - x^2}$$.
   - Chanh: $$1 + x + x^2 + \cdots = \frac{1}{1 - x}$$.
2. **Bước 2 — Nhân 3 nhân tử lại để tìm hệ số $$[x^4]$$:**
   Vì ta chỉ cần hệ số của $$x^4$$, mọi số hạng bậc $$> 4$$ có thể bỏ qua ngay khi nhân tay:
   $$G(x) = (1 + x + x^2)(1 + x^2 + x^4 + \cdots)(1 + x + x^2 + x^3 + x^4 + \cdots).$$
   - Nhân hai ngoặc đầu (giữ đến $$x^4$$):
     $$(1 + x + x^2)(1 + x^2 + x^4) = 1 + x + 2x^2 + x^3 + 2x^4 + \cdots$$
   - Nhân tiếp với $$(1 + x + x^2 + x^3 + x^4)$$ và chỉ gom các tích tạo ra $$x^4$$:
     $$[x^4]G(x) = 1\cdot 1 + 1\cdot 1 + 2\cdot 1 + 1\cdot 1 + 2\cdot 1 = 1 + 1 + 2 + 1 + 2 = 7\text{ cách!}$$
3. **Bước 3 — Kiểm chứng bằng cách liệt kê tay 7 bộ (Dâu, Cam, Chanh) có tổng = 4:**
   $$(0,0,4),\; (0,2,2),\; (0,4,0),\; (1,0,3),\; (1,2,1),\; (2,0,2),\; (2,2,0)$$ — đúng **7 cách**, không thiếu, không trùng!

### Khung giải thích: Vì sao "đóng gói dãy thành hàm" lại mạnh đến vậy (nên đọc chậm)

1. **Bước 1 — Biến số mũ thành "bộ đếm tổng":** Quy tắc $$x^a \cdot x^b = x^{a+b}$$ tự động thực hiện phép cộng ràng buộc (tổng số viên kẹo = 4) mà bạn không phải chia trường hợp thủ công.
2. **Bước 2 — Biến hệ số thành "số cách chọn":** Mỗi lần cùng một số mũ $$x^4$$ xuất hiện từ các nhánh nhân khác nhau, phép cộng đa thức tự động gom chúng lại thành tổng số cách hợp lệ.
3. **Bước 3 — Rút gọn vô hạn thành hữu hạn:** Chuỗi vô hạn $$1 + x + x^2 + \cdots$$ thu gọn thành phân thức tí hon $$\frac{1}{1-x}$$, giúp ta dùng toàn bộ kỹ thuật đại số (rút gọn, tách phân thức, đạo hàm) để xử lý những bài toán đếm mà cách liệt kê thuần túy hoàn toàn bất lực.

$$(a_n)_{n\ge 0} \;\xleftrightarrow{\text{đóng gói}}\; G(x) = \sum_{n=0}^{\infty} a_n x^n \;\xrightarrow{\text{nhân đại số}}\; [x^n]\big(A(x)B(x)\big) = \sum_{k=0}^n a_k b_{n-k}.$$

## Bài tập

### Bài tập 1

Tìm hàm sinh của dãy $$a_n = 2$$ với mọi $$n \ge 0$$.

<details>
<summary>Đáp án</summary>

<div class="textbook-equation" markdown="1">
$$
G(x)=\sum_{n\ge0}2x^n=\frac{2}{1-x}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</details>

### Bài tập 2

Tìm hàm sinh của dãy $$a_n=n$$.

<details>
<summary>Đáp án</summary>

Áp dụng công thức chuẩn:

<div class="textbook-equation" markdown="1">
$$
\sum_{n\ge1}nx^n=\frac{x}{(1-x)^2}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</details>

### Bài tập 3

Giải thích vì sao phép dịch chuỗi bằng cách nhân với $$x$$ lại hữu ích khi xử lý hệ thức truy hồi.

<details>
<summary>Đáp án</summary>

Nhờ phép nhân với $$x$$ hoặc $$x^2$$, các số hạng dịch chỉ số như $$a_{n-1}$$, $$a_{n-2}$$ trong hệ thức truy hồi được biểu diễn trực tiếp qua hàm sinh $$G(x)$$. Qua đó, hệ thức truy hồi chuyển thành một phương trình đại số theo $$G(x)$$.

</details>

### Bài tập 4

Cho $$A(x) = 1 + x$$ và $$C(x) = 1 + x + x^2$$. Tính hệ số $$[x^2](A \cdot C)$$ bằng công thức tích chập.

<details>
<summary>Đáp án</summary>

$$[x^2](A \cdot C) = a_0 c_2 + a_1 c_1 + a_2 c_0 = 1 \cdot 1 + 1 \cdot 1 + 0 \cdot 1 = 2$$. Kiểm tra lại bằng khai triển trực tiếp: $$(1+x)(1+x+x^2) = 1 + 2x + 2x^2 + x^3$$.

</details>

### Bài tập 5

Cho dãy số tam giác $$a_n = \binom{n+2}{2}$$. Tìm hàm sinh $$G(x)$$.

<details>
<summary>Đáp án</summary>

$$\sum_{n \ge 0} \binom{n+2}{2} x^n = \frac{1}{(1-x)^3}$$ — đây là hàm sinh của hệ số nhị thức với $$k = 2$$.

</details>

## Xem thêm / Video gợi ý

- [Injective, Surjective, Bijective](https://www.youtube.com/watch?v=2jZ5n8k0p0Q) — 3Blue1Brown (Visual explanation)

## Tóm tắt

- Hàm sinh thông thường: $$G(x)=\sum_{n\ge 0} a_n x^n$$; ký hiệu hệ số $$[x^n]G(x)=a_n$$.
- Chuỗi lũy thừa **hình thức** cho phép thao tác trên hệ số mà không cần xét điều kiện hội tụ.
- Một số hàm sinh chuẩn: $$1+x+x^2+\cdots = 1/(1-x)$$; $$\sum nx^n = x/(1-x)^2$$.
- Các phép cộng, nhân, dịch chỉ số và đạo hàm mã hóa trực tiếp các thao tác trên dãy số.
- Trong khoa học máy tính, hàm sinh hỗ trợ đếm cấu hình, phân tích thuật toán và mô hình hóa trạng thái động.

Ở bài tiếp theo, chúng ta sẽ dùng hàm sinh để **giải quan hệ truy hồi** theo quy trình bốn bước.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=-drdeNMoe8w">GENERATING FUNCTIONS - Discrete Mathematics</a> — TrevTutor, tiếng Anh. Giới thiệu hàm sinh thông thường: chuyển dãy số thành chuỗi lũy thừa hình thức.
- <a href="https://www.youtube.com/watch?v=YB7qnuo-GRY">A brief introduction to generating functions</a> — YY Ahn, tiếng Anh. Tổng quan ngắn trước khi đi vào các phép nhân chuỗi.
- <a href="https://www.youtube.com/watch?v=bOXCLR3Wric">Olympiad level counting  (Generating functions)</a> — 3Blue1Brown, tiếng Anh. Minh họa kỹ thuật đếm thông qua hệ số của hàm sinh.
