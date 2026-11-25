---

layout: post
title: "Hàm nghịch đảo và Hàm hợp"
categories: chapter06
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Sau các tính chất đơn ánh, toàn ánh và song ánh, bài học này trình bày hàm hợp và hàm nghịch đảo — nền tảng của pipeline xử lý dữ liệu và phép biến đổi khả nghịch."
---


Buổi sáng bạn đi tất trước rồi mới xỏ giày; tối về nhà bạn bắt buộc phải tháo giày trước rồi mới cởi tất—đảo ngược thứ tự đó là bất khả thi. Quy luật đời thường tưởng chừng hiển nhiên ấy chính là định lý $$(g \circ f)^{-1} = f^{-1} \circ g^{-1}$$ trong lý thuyết **hàm hợp và hàm nghịch đảo**, nền tảng cho mọi chuỗi xử lý dữ liệu (*pipeline*), phép biến đổi đồ họa 3D và cơ chế mã hóa–giải mã bảo mật.

Ở mục trước, chúng ta đã học ba tính chất đơn ánh, toàn ánh và song ánh. Mục này giới thiệu **hàm hợp** và **hàm nghịch đảo** — hai khái niệm gắn trực tiếp với chuỗi xử lý dữ liệu (pipeline) và các phép biến đổi có thể đảo ngược.

Trong phần mềm, dữ liệu hiếm khi chỉ đi qua một bước duy nhất mà thường được biến đổi theo chuỗi như phân tích (parse) – kiểm tra hợp lệ (validate) – mã hóa (encode). Hàm hợp mô tả việc ghép nhiều ánh xạ nối tiếp thành một chuỗi xử lý; còn hàm nghịch đảo trả lời câu hỏi liệu ta có thể khôi phục chính xác đầu vào ban đầu hay không. Không phải hàm nào cũng có nghịch đảo — điều kiện cần và đủ là hàm phải song ánh.

## Kiến thức cần nhớ: Bốn quy luật cốt lõi của Hàm hợp và Hàm nghịch đảo

1. **Hàm hợp $$(g \circ f)(x) = g(f(x))$$ — Luôn thực thi từ phải sang trái**:
   Đầu vào $$x$$ đi qua $$f$$ trước để ra $$f(x)$$, rồi kết quả đó làm đầu vào cho $$g$$. Để hợp được, miền giá trị của $$f$$ phải nằm gọn trong miền xác định của $$g$$: $$\text{Range}(f) \subseteq \text{Domain}(g)$$.

2. **Không giao hoán nhưng có tính kết hợp**:
   Nói chung $$g \circ f \neq f \circ g$$ (thứ tự áp dụng bước xử lý cực kỳ quan trọng!). Tuy nhiên, phép hợp luôn **kết hợp**: $$(h \circ g) \circ f = h \circ (g \circ f)$$, cho phép gom nhóm các tầng xử lý trong pipeline một cách linh hoạt.

3. **Hàm nghịch đảo $$f^{-1}$$ chỉ tồn tại khi và chỉ khi $$f$$ là Song ánh**:
   Nếu $$f: A \to B$$ là song ánh, tồn tại duy nhất $$f^{-1}: B \to A$$ sao cho $$f^{-1}(f(a)) = a$$ (hàm đồng nhất $$\mathrm{id}_A$$) và $$f(f^{-1}(b)) = b$$ ($$\mathrm{id}_B$$). Nếu $$f$$ không đơn ánh thì $$f^{-1}$$ không xác định duy nhất; nếu không toàn ánh thì có đầu vào ở $$B$$ không có ảnh ngược.

4. **Quy tắc "Đi tất – Đi giày" khi đảo ngược chuỗi hàm**:
   Khi nối tiếp hai phép biến đổi song ánh $$f$$ rồi $$g$$, phép hoàn tác phải tháo theo **thứ tự ngược lại**:
   $$(g \circ f)^{-1} = f^{-1} \circ g^{-1}.$$

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Tính** hàm hợp $$(g \circ f)(x)$$ và nhận biết hàm đồng nhất.
- **Xác định** điều kiện tồn tại và tìm hàm nghịch đảo của một hàm song ánh.
- **Áp dụng** phép hợp hàm (composition) trong pipeline dữ liệu và lập trình hàm.

**Từ khóa**: hàm hợp, hàm nghịch đảo, hàm đồng nhất, composition.
</div>

## Hàm hợp

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Cho $$f:A\to B$$ và $$g:B\to C$$. **Hàm hợp** của $$g$$ sau $$f$$ là hàm $$g\circ f:A\to C$$ được xác định bởi:

<div class="textbook-equation" markdown="1">
$$(g\circ f)(x)=g(f(x)).$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

**Ký hiệu**: $$g\circ f$$ đọc là "$$g$$ hợp $$f$$" hoặc "$$g$$ sau $$f$$". Khi tính giá trị, ta thực hiện $$f$$ trước rồi mới áp dụng $$g$$.

<div class="textbook-example" markdown="1">
**Ví dụ**: Với $$f(x)=2x+1$$ và $$g(x)=x^2$$, ta có:

<div class="textbook-equation" markdown="1">
$$(g\circ f)(x)=(2x+1)^2,$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$(f\circ g)(x)=2x^2+1.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Hai biểu thức này khác nhau, cho thấy phép hợp hàm không có tính giao hoán.

![Hàm hợp g∘f — ghép hai ánh xạ](/discrete-mathematics-for-computer-science-iuh/img/course/Example_for_a_composition_of_two_functions.svg)

<p class="textbook-figure-caption" data-figure="6.13">Hàm hợp $(g \circ f)(x) = g(f(x))$ — thực hiện f trước rồi đến g, cho ra ánh xạ từ A sang C.</p>
</div>

## Điều kiện để hợp được

Để hàm hợp $$g\circ f$$ xác định, mọi giá trị đầu ra $$f(x)$$ phải nằm trong miền xác định của $$g$$. Nói cách khác:

<div class="textbook-equation" markdown="1">
$$f(A)\subseteq \operatorname{dom}(g).$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-example" markdown="1">
**Ví dụ**: Nếu $$f:\mathbb{R}\to\mathbb{R}$$, $$f(x)=x^2$$ và $$g:[0,\infty)\to\mathbb{R}$$, $$g(x)=\sqrt{x}$$, thì $$g\circ f$$ xác định vì $$f(\mathbb{R})=[0,\infty) = \operatorname{dom}(g)$$.

![Điều kiện hợp — ảnh của f nằm trong domain của g](/discrete-mathematics-for-computer-science-iuh/img/course/Function_machine2.svg)

<p class="textbook-figure-caption" data-figure="6.14">Để $g \circ f$ xác định, mọi giá trị $f(x)$ phải thuộc domain của g — đầu ra của bước 1 là đầu vào của bước 2.</p>
</div>

## Tính kết hợp của hàm hợp

<div class="textbook-theorem" markdown="1">
**Định lý**: Khi các hàm hợp đều xác định, ta luôn có:

<div class="textbook-equation" markdown="1">
$$h\circ(g\circ f)=(h\circ g)\circ f.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-proof" id="chứng-minh" markdown="1">
**Chứng minh**: Với mọi $$x$$ thuộc miền xác định của $$f$$:

<div class="textbook-equation" markdown="1">
$$[h\circ(g\circ f)](x)=h((g\circ f)(x))=h(g(f(x))).$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Mặt khác:

<div class="textbook-equation" markdown="1">
$$[(h\circ g)\circ f](x)=(h\circ g)(f(x))=h(g(f(x))).$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Vì hai vế cho cùng một giá trị với mọi $$x$$, hai hàm hợp bằng nhau.
</div>

![Tính kết hợp — (h∘g)∘f = h∘(g∘f)](/discrete-mathematics-for-computer-science-iuh/img/course/Example_for_a_composition_of_two_functions.svg)

<p class="textbook-figure-caption" data-figure="6.15">Phép hợp có tính kết hợp nhưng không giao hoán — thứ tự ghép hàm ảnh hưởng trực tiếp đến kết quả.</p>
## Hàm đồng nhất

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Hàm đồng nhất trên tập $$A$$ là ánh xạ $$id_A:A\to A$$ xác định bởi $$id_A(x)=x$$.
</div>

**Tính chất**: Với mọi hàm $$f:A\to B$$, ta có:

<div class="textbook-equation" markdown="1">
$$f\circ id_A=f,$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$id_B\circ f=f.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Như vậy, hàm đồng nhất đóng vai trò phần tử trung hòa đối với phép hợp hàm.

![Hàm đồng nhất id(x) = x](/discrete-mathematics-for-computer-science-iuh/img/course/Bijection.svg)

<p class="textbook-figure-caption" data-figure="6.16">Hàm đồng nhất $id_A$ là phần tử trung hòa — $f \circ id = id \circ f = f$.</p>
## Hàm nghịch đảo

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Cho hàm $$f:A\to B$$. Một hàm $$g:B\to A$$ được gọi là **hàm nghịch đảo** của $$f$$ nếu thỏa mãn đồng thời:

<div class="textbook-equation" markdown="1">
$$g\circ f=id_A$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

và

<div class="textbook-equation" markdown="1">
$$f\circ g=id_B.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Khi hàm nghịch đảo tồn tại, ta ký hiệu $$g=f^{-1}$$.

<div class="textbook-theorem" markdown="1">
**Định lý**: Hàm $$f:A\to B$$ có hàm nghịch đảo hai phía khi và chỉ khi $$f$$ là song ánh.
</div>

<div class="textbook-proof" id="chứng-minh-ý-chính" markdown="1">
**Chứng minh (ý chính)**: Nếu $$f$$ có nghịch đảo $$f^{-1}$$, thì với mọi $$y\in B$$, chọn $$x=f^{-1}(y)$$ ta được $$f(x)=y$$, suy ra $$f$$ toàn ánh. Ngoài ra, nếu $$f(x_1)=f(x_2)$$, tác động $$f^{-1}$$ lên hai vế cho $$x_1=x_2$$, suy ra $$f$$ đơn ánh. Vậy $$f$$ song ánh.

Ngược lại, nếu $$f$$ song ánh, mỗi $$y\in B$$ có đúng một tiền ảnh $$x\in A$$. Định nghĩa $$f^{-1}(y)=x$$; hàm này thỏa mãn cả hai điều kiện của hàm nghịch đảo.
</div>

![Hàm nghịch đảo — chỉ tồn tại khi song ánh](/discrete-mathematics-for-computer-science-iuh/img/course/Bijection.svg)

<p class="textbook-figure-caption" data-figure="6.17">Hàm nghịch đảo $f^{-1}$ tồn tại khi và chỉ khi f song ánh — cho phép đảo chiều mũi tên mà không làm mất thông tin.</p>
## Tìm hàm nghịch đảo

<div class="textbook-example" markdown="1">
**Ví dụ**: Tìm hàm nghịch đảo của $$f:\mathbb{R}\to\mathbb{R}$$, $$f(x)=3x-2$$.

Đặt $$y=3x-2$$ rồi giải theo $$x$$:

<div class="textbook-equation" markdown="1">
$$x=\frac{y+2}{3}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Do đó:

<div class="textbook-equation" markdown="1">
$$f^{-1}(y)=\frac{y+2}{3}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Đổi lại tên biến độc lập thành $$x$$, ta thường viết:

<div class="textbook-equation" markdown="1">
$$f^{-1}(x)=\frac{x+2}{3}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

## Khi nào không có nghịch đảo?

Hàm $$f:\mathbb{R}\to\mathbb{R}$$, $$f(x)=x^2$$ không có nghịch đảo trên toàn $$\mathbb{R}$$ vì nó không đơn ánh (chẳng hạn $$f(2)=f(-2)$$) và cũng không toàn ánh. Tuy nhiên, nếu thu hẹp cả domain lẫn codomain về $$[0,\infty)$$, hàm trở thành song ánh và có nghịch đảo là $$f^{-1}(x)=\sqrt{x}$$.

### Giải thích: Tính tay $$g \circ f$$, $$f \circ g$$ và kiểm chứng quy tắc $$(g \circ f)^{-1} = f^{-1} \circ g^{-1}$$

Cho hai hàm song ánh trên $$\mathbb{R}$$: $$f(x) = 2x + 3$$ và $$g(x) = x - 5$$.

1. **Tính hai chiều hàm hợp và thử tại $$x = 4$$**:
   - $$(g \circ f)(x) = g(f(x)) = g(2x + 3) = (2x + 3) - 5 = \mathbf{2x - 2}$$.
     Thử $$x = 4$$: $$f(4) = 11 \xrightarrow{g} g(11) = \mathbf{6}$$ (khớp $$2(4) - 2 = 6$$).
   - $$(f \circ g)(x) = f(g(x)) = f(x - 5) = 2(x - 5) + 3 = \mathbf{2x - 7}$$.
     Thử $$x = 4$$: $$g(4) = -1 \xrightarrow{f} f(-1) = \mathbf{1}$$ (khớp $$2(4) - 7 = 1$$).
   $$\implies$$ Vì $$6 \neq 1$$, ta thấy ngay $$g \circ f \neq f \circ g$$!
2. **Tìm hàm nghịch đảo từng hàm**:
   - Đặt $$y = 2x + 3 \implies x = \frac{y - 3}{2} \implies f^{-1}(y) = \frac{y - 3}{2}$$.
   - Đặt $$y = x - 5 \implies x = y + 5 \implies g^{-1}(y) = y + 5$$.
3. **Kiểm chứng quy tắc $$(g \circ f)^{-1} = f^{-1} \circ g^{-1}$$**:
   - **Cách 1 (đảo trực tiếp $$h(x) = 2x - 2$$)**: Đặt $$y = 2x - 2 \implies h^{-1}(y) = \mathbf{\frac{y + 2}{2}}$$.
   - **Cách 2 (hợp ngược $$f^{-1} \circ g^{-1}$$)**:
     $$(f^{-1} \circ g^{-1})(y) = f^{-1}(g^{-1}(y)) = f^{-1}(y + 5) = \frac{(y + 5) - 3}{2} = \mathbf{\frac{y + 2}{2}}.$$
   Thử hoàn tác từ kết quả $$y = 6$$: $$g^{-1}(6) = 11 \xrightarrow{f^{-1}} f^{-1}(11) = \frac{11 - 3}{2} = \mathbf{4}$$ — quay chính xác về giá trị $$x = 4$$ ban đầu! (Nếu bạn thử ngược sai thứ tự $$g^{-1}(f^{-1}(6)) = \frac{3}{2} + 5 = 6{,}5 \neq 4$$ sẽ sai ngay!)

## Ứng dụng trong Khoa học Máy tính

```python
def clean(s):
    return s.strip().lower()

def tokenize(s):
    return s.split()

result = tokenize(clean("  Discrete Math  "))
```

![Pipeline dữ liệu — chuỗi hàm hợp](/discrete-mathematics-for-computer-science-iuh/img/course/Function_machine2.svg)

<p class="textbook-figure-caption" data-figure="6.18">Pipeline xử lý dữ liệu là hàm hợp — tokenize ∘ clean ánh xạ chuỗi thô sang danh sách token (thực hiện clean trước rồi mới tokenize).</p>
- **Pipeline dữ liệu**: mỗi bước xử lý là một hàm, và toàn bộ pipeline là hàm hợp của các bước đó.
- **Mật mã học**: mã hóa và giải mã phải là hai hàm nghịch đảo của nhau trên không gian thông điệp hợp lệ.
- **Tuần tự hóa (Serialization)**: điều kiện `decode(encode(x)) = x` là yêu cầu nghịch đảo một phía quan trọng để bảo toàn dữ liệu.
- **Lập trình hàm**: phép hợp hàm cho phép xây dựng chương trình phức tạp từ các hàm nhỏ, độc lập.


## Công cụ tương tác

Ghép hai hàm thành $$g \circ f$$ trên đường ống xử lý và quan sát ánh xạ kết quả.
<div class="interactive-demo" markdown="1">
<div data-demo="function-composition-pipeline"></div>
</div>
<script src="{{ '/public/js/function-composition-pipeline.js' | relative_url }}"></script>

### Minh hoạ tương tác

Minh hoạ hàm nghịch đảo của một song ánh và phép hợp $$g \circ f$$ giữa hai hàm số.

<div class="interactive-demo" markdown="1">
<div data-demo="function-explainer" data-preset="bij" data-focus="compose"></div>
</div>
<script src="{{ '/public/js/explainers/function-explainer.js' | relative_url }}"></script>

## Bài tập thực hành

### Bài tập 1: Tính hàm hợp

Cho $$f(x) = 2x$$ và $$g(x) = x+3$$. Tính $$f \circ g$$ và $$g \circ f$$.

<details>
<summary>Đáp án</summary>

- $(f \circ g)(x) = 2(x+3) = 2x+6$
- $(g \circ f)(x) = 2x+3$

</details>

### Bài tập 2: Kiểm tra hàm nghịch đảo

Hàm $$f(x) = 3x + 1$$ có nghịch đảo trên $$\R$$ không? Nếu có, hãy tìm $$f^{-1}$$.

<details>
<summary>Đáp án</summary>

Có, vì $f$ là song ánh trên $\R$. Hàm nghịch đảo là $f^{-1}(x) = \frac{x-1}{3}$.

</details>

### Bài tập 3: Ứng dụng

Viết hàm Python minh họa phép hợp (composition) của hai hàm.

<details>
<summary>Đáp án</summary>

```python
def compose(f, g):
    return lambda x: f(g(x))

h = compose(lambda x: x*2, lambda x: x+1)
print(h(3))  # 8
```

</details>

## Xem thêm / Video gợi ý

- [Injective, Surjective, Bijective](https://www.youtube.com/watch?v=2jZ5n8k0p0Q) — 3Blue1Brown (Visual explanation)

## Tóm tắt

- **Hàm hợp** $$(g \circ f)(x) = g(f(x))$$: áp dụng $$f$$ trước rồi đến $$g$$; phép hợp có tính kết hợp nhưng không giao hoán.
- **Hàm đồng nhất** $$id_A$$: phần tử trung hòa của phép hợp hàm.
- **Hàm nghịch đảo** $$f^{-1}$$: tồn tại khi và chỉ khi $$f$$ là song ánh.
- **Ứng dụng trong Khoa học Máy tính**: pipeline dữ liệu, mật mã học, serialization, lập trình hàm.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=1cvQhfZGF7Q">[Discrete Mathematics] Inverse Function Examples</a> — TrevTutor, tiếng Anh. Giới thiệu hàm nghịch đảo và điều kiện tồn tại qua ví dụ.
- <a href="https://www.youtube.com/watch?v=kEUVTLpdG0k">[Discrete Mathematics] Inverses Examples 2</a> — TrevTutor, tiếng Anh. Thêm ví dụ rèn luyện cách tìm hàm nghịch đảo.
- <a href="https://www.youtube.com/watch?v=bZred_Ksz2k">INJECTIVE, SURJECTIVE, and BIJECTIVE FUNCTIONS - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giải thích vì sao tính song ánh đảm bảo hàm nghịch đảo xác định trên toàn miền.
