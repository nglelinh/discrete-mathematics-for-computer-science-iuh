---

layout: post
title: "Tính chất của Hàm số"
categories: chapter06
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Ở mục trước chúng ta đã định nghĩa hàm số, miền xác định, miền đích và các cách biểu diễn. Mục này giới thiệu ba tính chất quan trọng: đơn ánh, toàn ánh và…"
---

Ở mục trước chúng ta đã định nghĩa hàm số, miền xác định, miền đích và các cách biểu diễn. Mục này giới thiệu ba tính chất quan trọng: **đơn ánh**, **toàn ánh** và **song ánh**.

Biết một ánh xạ là hàm vẫn chưa đủ để đánh giá sức mạnh của nó. Hàm đơn ánh bảo toàn sự phân biệt giữa các đầu vào; hàm toàn ánh phủ hết codomain; hàm song ánh thỏa cả hai và cho phép ghép cặp một-một giữa hai tập. Các tính chất này xuất hiện trong thiết kế mã định danh, băm, nén dữ liệu và chứng minh về lực lượng tập hợp.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Kiểm tra** tính đơn ánh và toàn ánh.
- **Nhận biết** hàm song phương (bijection).
- **Áp dụng** trong mã hóa, hash và đảo ngược hàm.

**Từ khóa**: đơn ánh (injective), toàn ánh (surjective), song phương (bijective).
</div>

## 1. Đơn ánh

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Hàm $$f:A\to B$$ là **đơn ánh** (injective, one-to-one) nếu hai đầu vào khác nhau luôn cho hai đầu ra khác nhau:
</div>

<div class="textbook-equation" markdown="1">
$$x_1\ne x_2 \Rightarrow f(x_1)\ne f(x_2).$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Ký hiệu**: $$f:A\to B$$ cho biết domain là $$A$$ và codomain là $$B$$; $$x_1,x_2$$ thường ký hiệu hai đầu vào bất kỳ, còn $$y$$ ký hiệu một đầu ra trong codomain.

Dạng tương đương thường dùng để chứng minh:

<div class="textbook-equation" markdown="1">
$$f(x_1)=f(x_2)\Rightarrow x_1=x_2.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-example" markdown="1">
**Ví dụ**: $$f:\mathbb{R}\to\mathbb{R}$$, $$f(x)=2x+3$$ là đơn ánh.

**Chứng minh**: Giả sử $$f(x_1)=f(x_2)$$. Khi đó:

<div class="textbook-equation" markdown="1">
$$2x_1+3=2x_2+3\Rightarrow 2x_1=2x_2\Rightarrow x_1=x_2.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Vậy $$f$$ đơn ánh.

**Phản ví dụ**: $$g:\mathbb{R}\to\mathbb{R}$$, $$g(x)=x^2$$ không đơn ánh vì $$g(2)=g(-2)=4$$ nhưng $$2\ne-2$$.

![Hàm đơn ánh (injective)](/discrete-mathematics-for-computer-science-iuh/img/course/Injection.svg)

<p class="textbook-figure-caption" data-figure="6.7">Hàm đơn ánh — hai đầu vào khác nhau luôn cho hai đầu ra khác nhau; không có hai mũi tên trùng đích.</p>
</div>

## 2. Toàn ánh

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Hàm $$f:A\to B$$ là **toàn ánh** (surjective, onto) nếu mọi phần tử của codomain đều được đạt tới:
</div>

<div class="textbook-equation" markdown="1">
$$\forall y\in B,\exists x\in A\text{ sao cho }f(x)=y.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-example" markdown="1">
**Ví dụ**: $$f:\mathbb{R}\to\mathbb{R}$$, $$f(x)=x^3$$ là toàn ánh.

**Chứng minh**: Lấy $$y\in\mathbb{R}$$ tùy ý. Chọn $$x=\sqrt[3]{y}$$. Khi đó $$f(x)=x^3=y$$. Vậy mọi $$y$$ đều có tiền ảnh.

**Phản ví dụ**: $$g:\mathbb{R}\to\mathbb{R}$$, $$g(x)=x^2$$ không toàn ánh vì không có $$x\in\mathbb{R}$$ nào thỏa $$x^2=-1$$.

![Hàm toàn ánh (surjective)](/discrete-mathematics-for-computer-science-iuh/img/course/Surjection.svg)

<p class="textbook-figure-caption" data-figure="6.8">Hàm toàn ánh — mọi phần tử codomain đều được chạm tới; không có phần tử đích bị bỏ trống.</p>
</div>

## 3. Song ánh

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Hàm $$f:A\to B$$ là **song ánh** (bijective) nếu vừa đơn ánh vừa toàn ánh.
</div>

Song ánh thiết lập sự ghép cặp một-một giữa $$A$$ và $$B$$. Khi đó mỗi $$y\in B$$ có đúng một tiền ảnh trong $$A$$.

<div class="textbook-example" markdown="1">
**Ví dụ**: $$f:\mathbb{R}\to\mathbb{R}$$, $$f(x)=x+5$$ là song ánh.

**Chứng minh**:

- Đơn ánh: $$x_1+5=x_2+5\Rightarrow x_1=x_2$$.
- Toàn ánh: với $$y\in\mathbb{R}$$, chọn $$x=y-5$$ thì $$f(x)=y$$.

Vậy $$f$$ song ánh.

![Hàm song ánh (bijective)](/discrete-mathematics-for-computer-science-iuh/img/course/Bijection.svg)

<p class="textbook-figure-caption" data-figure="6.9">Hàm song ánh vừa đơn ánh vừa toàn ánh — thiết lập ghép cặp một-một giữa hai tập, có thể đảo ngược.</p>
</div>

## 4. Vai trò của domain và codomain

Cùng một công thức có thể có tính chất khác nhau nếu domain/codomain khác nhau.

<div class="textbook-example" markdown="1">
**Ví dụ**: $$f(x)=x^2$$.

- $$f:\mathbb{R}\to\mathbb{R}$$: không đơn ánh, không toàn ánh.
- $$f:\mathbb{R}\to[0,\infty)$$: không đơn ánh, nhưng toàn ánh.
- $$f:[0,\infty)\to[0,\infty)$$: song ánh.

![Cùng công thức, khác tính chất theo domain/codomain](/discrete-mathematics-for-computer-science-iuh/img/course/Function_machine2.svg)

<p class="textbook-figure-caption" data-figure="6.10">Domain và codomain quyết định tính chất — cùng $$f(x)=x^2$$ nhưng khác domain/codomain cho kết quả đơn/toàn/song ánh khác nhau.</p>
</div>

## 8. Ứng dụng trong Khoa học Máy tính

- **Mã hóa khả nghịch** cần song ánh giữa không gian bản rõ và bản mã.
- **Hash table** thường không đơn ánh vì có va chạm.
- **Serialization** tốt nên gần song ánh: serialize rồi deserialize phải thu lại dữ liệu ban đầu.
- **Database primary key** tạo đơn ánh từ bản ghi sang khóa.
- **Load balancing** thường là toàn ánh nếu mọi server đều nhận ít nhất một job.

![Mã hóa khả nghịch cần song ánh](/discrete-mathematics-for-computer-science-iuh/img/course/Bijection.svg)

<p class="textbook-figure-caption" data-figure="6.11">Mã hóa/giải mã và serialization cần song ánh — encode rồi decode phải thu lại dữ liệu ban đầu.</p>
![Hash table — gần đơn ánh để giảm va chạm](/discrete-mathematics-for-computer-science-iuh/img/course/Injection.svg)

<p class="textbook-figure-caption" data-figure="6.12">Hash function tốt nên gần đơn ánh — hai input khác nhau cho cùng output gây collision trong bảng băm.</p>
## Bài tập thực hành

### Bài tập 1: Kiểm tra tính chất

Xét $$f: \R \to \R$$, $$f(x) = x^2$$.  
Hỏi $$f$$ có phải đơn ánh? Toàn ánh? Giải thích.

<details>
<summary>Đáp án</summary>

- Không đơn ánh ($$f(2) = f(-2)$$)
- Không toàn ánh (không có $$x$$ nào cho $$f(x) = -1$$)

</details>

### Bài tập 2: Tìm hàm song ánh

Tìm một hàm song ánh từ $$\{1,2,3\}$$ sang $$\{a,b,c\}$$.

<details>
<summary>Đáp án</summary>

$$f(1)=a, f(2)=b, f(3)=c$$ (bất kỳ hoán vị nào cũng được).

</details>

### Bài tập 3: Ứng dụng

Giải thích tại sao hàm băm tốt thường được thiết kế gần như đơn ánh.

<details>
<summary>Đáp án</summary>

Để giảm va chạm (collision). Nếu hai input khác nhau cho cùng output thì dễ xảy ra xung đột trong bảng băm.

</details>

## Xem thêm / Video gợi ý

- [Injective, Surjective, Bijective](https://www.youtube.com/watch?v=2jZ5n8k0p0Q) — 3Blue1Brown (Visual explanation)

## Tóm tắt

- **Đơn ánh**: $$x_1 \ne x_2 \Rightarrow f(x_1) \ne f(x_2)$$; không gộp hai đầu vào khác nhau
- **Toàn ánh**: mọi $$y \in B$$ đều có tiền ảnh
- **Song ánh**: vừa đơn ánh vừa toàn ánh; thiết lập ghép cặp một-một
- **Domain và codomain** quyết định tính chất — cùng công thức có thể khác tính chất
- **Ứng dụng CS**: mã hóa khả nghịch, primary key, hash table, serialization

Trong bài tiếp theo, chúng ta sẽ học hàm hợp và hàm nghịch đảo.
