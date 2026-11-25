---

layout: post
title: "Tính chất của Hàm số"
categories: chapter06
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Sau khi tìm hiểu định nghĩa và cách biểu diễn hàm số ở mục trước, bài học này giới thiệu ba tính chất cốt lõi: đơn ánh, toàn ánh và song ánh."
---


Nếu một thuật toán nén dữ liệu không mất mát (lossless) nén hai tệp tin khác nhau thành cùng một chuỗi bit, bạn sẽ vĩnh viễn không thể giải nén về đúng bản gốc; còn nếu một hệ thống cấp mã sinh viên bỏ trống một nửa dải giá trị hoặc không phủ hết các lớp mục tiêu, ánh xạ sẽ mất cân đối. Ba tính chất **đơn ánh (injective), toàn ánh (surjective) và song ánh (bijective)** chính là ba thước đo cốt lõi cho biết một hàm có làm mất thông tin hay không, có phủ kín miền đích hay không, và liệu có thể đảo ngược hoàn hảo hay không.

Ở mục trước, chúng ta đã định nghĩa hàm số, phân biệt miền xác định với miền đích và xem các cách biểu diễn hàm. Mục này giới thiệu ba tính chất quan trọng của ánh xạ: **đơn ánh**, **toàn ánh** và **song ánh**.

Chỉ biết một ánh xạ là hàm vẫn chưa đủ để đánh giá các đặc tính cấu trúc của nó. Hàm đơn ánh bảo toàn sự phân biệt giữa các đầu vào; hàm toàn ánh phủ kín toàn bộ codomain; còn hàm song ánh thỏa mãn cả hai điều kiện, cho phép ghép cặp một–một giữa hai tập hợp. Những tính chất này xuất hiện thường xuyên trong thiết kế mã định danh, hàm băm, nén dữ liệu và các chứng minh về lực lượng tập hợp.

## Bản đồ kiến thức nền: Ba tính chất vàng và vai trò sống còn của Miền

1. **Đơn ánh (Injective / 1–1) — Không đụng độ, không mất thông tin**:
   $\forall x_1, x_2 \in A,\; f(x_1) = f(x_2) \to x_1 = x_2$ (tương đương: đầu vào khác nhau $\to$ đầu ra khác nhau). Trên tập hữu hạn, điều kiện cần là $|A| \le |B|$.

2. **Toàn ánh (Surjective / Onto) — Phủ kín toàn bộ miền đích**:
   $\forall y \in B,\; \exists x \in A,\; f(x) = y$, tức $\text{Range}(f) = \text{Codomain}(B)$. Trên tập hữu hạn, điều kiện cần là $|A| \ge |B|$.

3. **Song ánh (Bijective) = Đơn ánh + Toàn ánh — Ghép cặp 1–1 hoàn hảo**:
   Mỗi phần tử ở $B$ có **đúng một** tạo ảnh ở $A$. Đây là điều kiện cần và đủ để hàm tồn tại **hàm nghịch đảo $f^{-1}$**, đồng thời là cơ sở để chứng minh hai tập hợp có cùng lực lượng ($|A| = |B|$).

4. **Miền xác định và Miền đích quyết định tính chất của hàm**:
   Một công thức đại số đơn lẻ như $f(x) = x^2$ chưa đủ để kết luận đơn ánh hay toàn ánh—chỉ cần thu hẹp Domain hoặc Codomain, cùng công thức đó có thể biến từ "không thỏa gì cả" thành song ánh hoàn hảo!

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Kiểm tra** tính đơn ánh và tính toàn ánh của một hàm số.
- **Nhận biết** hàm song ánh (bijection).
- **Áp dụng** các tính chất này trong mã hóa, hàm băm và bài toán đảo ngược hàm.

**Từ khóa**: đơn ánh (injective), toàn ánh (surjective), song ánh (bijective).
</div>

## Đơn ánh

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Hàm $$f:A\to B$$ được gọi là **đơn ánh** (injective, one-to-one) nếu hai đầu vào khác nhau luôn cho hai đầu ra khác nhau:

<div class="textbook-equation" markdown="1">
$$x_1\ne x_2 \Rightarrow f(x_1)\ne f(x_2).$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

**Ký hiệu**: $$f:A\to B$$ cho biết miền xác định là $$A$$ và miền đích là $$B$$; $$x_1,x_2$$ thường ký hiệu hai đầu vào bất kỳ, còn $$y$$ ký hiệu một đầu ra thuộc miền đích.

Dạng tương đương (phản đảo) thường dùng khi chứng minh:

<div class="textbook-equation" markdown="1">
$$f(x_1)=f(x_2)\Rightarrow x_1=x_2.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-example" markdown="1">
**Ví dụ**: Hàm $$f:\mathbb{R}\to\mathbb{R}$$, $$f(x)=2x+3$$ là đơn ánh.

**Chứng minh**: Giả sử $$f(x_1)=f(x_2)$$. Khi đó:

<div class="textbook-equation" markdown="1">
$$2x_1+3=2x_2+3\Rightarrow 2x_1=2x_2\Rightarrow x_1=x_2.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Vậy $$f$$ là hàm đơn ánh.

**Phản ví dụ**: Hàm $$g:\mathbb{R}\to\mathbb{R}$$, $$g(x)=x^2$$ không đơn ánh vì $$g(2)=g(-2)=4$$ nhưng $$2\ne-2$$.

![Hàm đơn ánh (injective)](/discrete-mathematics-for-computer-science-iuh/img/course/Injection.svg)

<p class="textbook-figure-caption" data-figure="6.7">Hàm đơn ánh — hai đầu vào khác nhau luôn cho hai đầu ra khác nhau; không có hai mũi tên nào cùng trỏ về một đích.</p>
</div>

## Toàn ánh

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Hàm $$f:A\to B$$ được gọi là **toàn ánh** (surjective, onto) nếu mọi phần tử của codomain đều là ảnh của ít nhất một phần tử trong domain:

<div class="textbook-equation" markdown="1">
$$\forall y\in B,\exists x\in A\text{ sao cho }f(x)=y.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**: Hàm $$f:\mathbb{R}\to\mathbb{R}$$, $$f(x)=x^3$$ là toàn ánh.

**Chứng minh**: Lấy $$y\in\mathbb{R}$$ tùy ý và chọn $$x=\sqrt[3]{y}$$. Khi đó $$f(x)=x^3=y$$. Vậy mọi $$y \in \mathbb{R}$$ đều có tiền ảnh.

**Phản ví dụ**: Hàm $$g:\mathbb{R}\to\mathbb{R}$$, $$g(x)=x^2$$ không toàn ánh vì không tồn tại $$x\in\mathbb{R}$$ sao cho $$x^2=-1$$.

![Hàm toàn ánh (surjective)](/discrete-mathematics-for-computer-science-iuh/img/course/Surjection.svg)

<p class="textbook-figure-caption" data-figure="6.8">Hàm toàn ánh — mọi phần tử trong codomain đều được chạm tới; không có phần tử đích nào bị bỏ trống.</p>
</div>

## Song ánh

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Hàm $$f:A\to B$$ được gọi là **song ánh** (bijective) nếu nó vừa đơn ánh vừa toàn ánh.
</div>

Song ánh thiết lập phép ghép cặp một–một giữa $$A$$ và $$B$$, nghĩa là mỗi phần tử $$y\in B$$ có đúng một tiền ảnh trong $$A$$.

<div class="textbook-example" markdown="1">
**Ví dụ**: Hàm $$f:\mathbb{R}\to\mathbb{R}$$, $$f(x)=x+5$$ là song ánh.

**Chứng minh**:

- Đơn ánh: $$x_1+5=x_2+5\Rightarrow x_1=x_2$$.
- Toàn ánh: với mọi $$y\in\mathbb{R}$$, chọn $$x=y-5$$ ta có $$f(x)=y$$.

Vậy $$f$$ là hàm song ánh.

![Hàm song ánh (bijective)](/discrete-mathematics-for-computer-science-iuh/img/course/Bijection.svg)

<p class="textbook-figure-caption" data-figure="6.9">Hàm song ánh vừa đơn ánh vừa toàn ánh — thiết lập ghép cặp một-một giữa hai tập và có thể đảo ngược.</p>
</div>

## Vai trò của domain và codomain

Cùng một công thức đại số có thể mang những tính chất khác nhau khi ta thay đổi domain hoặc codomain.

<div class="textbook-example" markdown="1">
**Ví dụ**: Xét công thức $$f(x)=x^2$$.

- $$f:\mathbb{R}\to\mathbb{R}$$: không đơn ánh, không toàn ánh.
- $$f:\mathbb{R}\to[0,\infty)$$: không đơn ánh, nhưng toàn ánh.
- $$f:[0,\infty)\to[0,\infty)$$: song ánh.

![Cùng công thức, khác tính chất theo domain/codomain](/discrete-mathematics-for-computer-science-iuh/img/course/Function_machine2.svg)

<p class="textbook-figure-caption" data-figure="6.10">Domain và codomain quyết định tính chất của hàm — cùng công thức $$f(x)=x^2$$ nhưng thay đổi domain/codomain sẽ cho kết quả đơn ánh, toàn ánh hay song ánh khác nhau.</p>
</div>

### Khung giải thích (nên đọc chậm): Cùng một công thức $f(x) = x^2$ biến hóa qua 4 lựa chọn Miền khác nhau

Hãy theo dõi sát cách một công thức duy nhất $f(x) = x^2$ thay đổi toàn bộ tính chất chỉ bằng việc đổi Domain và Codomain:

| Hàm số $f(x) = x^2$ | Đơn ánh? | Toàn ánh? | Song ánh? | Lý do cụ thể |
| :--- | :---: | :---: | :---: | :--- |
| **1. $\mathbb{R} \to \mathbb{R}$** | **Không** | **Không** | **Không** | $f(-2) = f(2) = 4$ (đụng độ); $y = -1$ không có $x \in \mathbb{R}$ nào thỏa $x^2 = -1$. |
| **2. $\mathbb{R}_{\ge 0} \to \mathbb{R}$** | **Có** | **Không** | **Không** | Với $x_1, x_2 \ge 0$, $x_1^2 = x_2^2 \implies x_1 = x_2$; nhưng $y = -1$ vẫn bị bỏ trống. |
| **3. $\mathbb{R} \to \mathbb{R}_{\ge 0}$** | **Không** | **Có** | **Không** | Mọi $y \ge 0$ đều có tạo ảnh $x = \sqrt{y}$; nhưng vẫn còn đụng độ $f(-2) = f(2)$. |
| **4. $\mathbb{R}_{\ge 0} \to \mathbb{R}_{\ge 0}$** | **Có** | **Có** | **Có** | Vừa không đụng độ, vừa phủ kín mọi $y \ge 0$ $\implies$ có nghịch đảo $f^{-1}(y) = \sqrt{y}$! |

**Mẹo kiểm tra nhanh trên bài thi tập hữu hạn**: Trước khi xét chi tiết từng phần tử của $f: A \to B$, hãy liếc ngay kích thước $|A|$ và $|B|$:
- Nếu $|A| > |B|$ (nhiều chim hơn chuồng) $\implies$ chắc chắn **không thể đơn ánh** (Nguyên lý Chuồng bồ câu!).
- Nếu $|A| < |B|$ (quá ít mũi tên để chạm hết đích) $\implies$ chắc chắn **không thể toàn ánh**.

## Ứng dụng trong Khoa học Máy tính

- **Mã hóa khả nghịch**: cần song ánh giữa không gian bản rõ và không gian bản mã để có thể giải mã chính xác.
- **Bảng băm (Hash table)**: hàm băm thường không đơn ánh vì miền khóa lớn hơn số ngăn chứa, dẫn đến va chạm (collision).
- **Tuần tự hóa (Serialization)**: một cơ chế tốt cần hoạt động như ánh xạ khả nghịch — serialize rồi deserialize phải khôi phục đúng dữ liệu ban đầu.
- **Khóa chính cơ sở dữ liệu (Database primary key)**: tạo ánh xạ đơn ánh từ bản ghi sang khóa định danh.
- **Cân bằng tải (Load balancing)**: ánh xạ tác vụ sang máy chủ là toàn ánh khi mọi máy chủ đều nhận được ít nhất một tác vụ.

![Mã hóa khả nghịch cần song ánh](/discrete-mathematics-for-computer-science-iuh/img/course/Bijection.svg)

<p class="textbook-figure-caption" data-figure="6.11">Mã hóa/giải mã và serialization cần tính song ánh — encode rồi decode phải thu lại đúng dữ liệu ban đầu.</p>
![Hash table — gần đơn ánh để giảm va chạm](/discrete-mathematics-for-computer-science-iuh/img/course/Injection.svg)

<p class="textbook-figure-caption" data-figure="6.12">Hàm băm tốt cần hạn chế trùng lặp đầu ra — hai đầu vào khác nhau cho cùng đầu ra sẽ gây va chạm (collision) trong bảng băm.</p>

## Công cụ tương tác

Nối mũi tên từ miền xác định sang miền đích, sau đó kiểm tra xem ánh xạ có đơn ánh, toàn ánh hay song ánh không.
<div class="interactive-demo" markdown="1">
<div data-demo="function-arrow-checker"></div>
</div>
<script src="{{ '/public/js/function-arrow-checker.js' | relative_url }}"></script>
<div class="interactive-demo" markdown="1">
<div data-demo="function-property-checker"></div>
</div>
<script src="{{ '/public/js/function-property-checker.js' | relative_url }}"></script>

### Minh hoạ tương tác

Minh hoạ tính đơn ánh và toàn ánh của hàm số, kèm chỉ báo phần tử vi phạm cụ thể.

<div class="interactive-demo" markdown="1">
<div data-demo="function-explainer" data-preset="surj" data-focus="props"></div>
</div>
<script src="{{ '/public/js/explainers/function-explainer.js' | relative_url }}"></script>

## Bài tập thực hành

### Bài tập 1: Kiểm tra tính chất

Xét hàm $$f: \R \to \R$$, $$f(x) = x^2$$. Hỏi $$f$$ có phải là đơn ánh hay toàn ánh không? Giải thích.

<details>
<summary>Đáp án</summary>

- Không đơn ánh vì $$f(2) = f(-2) = 4$$ nhưng $$2 \ne -2$$.
- Không toàn ánh vì không tồn tại $$x \in \R$$ sao cho $$f(x) = -1$$.

</details>

### Bài tập 2: Tìm hàm song ánh

Tìm một hàm song ánh từ $$\{1,2,3\}$$ sang $$\{a,b,c\}$$.

<details>
<summary>Đáp án</summary>

$$f(1)=a, f(2)=b, f(3)=c$$ (hoặc bất kỳ hoán vị nào khác của $$\{a,b,c\}$$).

</details>

### Bài tập 3: Ứng dụng

Giải thích tại sao hàm băm tốt thường được thiết kế để giảm thiểu việc hai đầu vào khác nhau cho cùng một đầu ra (gần như đơn ánh trên tập dữ liệu thực tế).

<details>
<summary>Đáp án</summary>

Để giảm thiểu va chạm (collision). Nếu nhiều đầu vào khác nhau cùng ánh xạ vào một giá trị băm, bảng băm sẽ phát sinh xung đột và làm giảm hiệu năng tra cứu.

</details>

## Xem thêm / Video gợi ý

- [Injective, Surjective, Bijective](https://www.youtube.com/watch?v=2jZ5n8k0p0Q) — 3Blue1Brown (Visual explanation)

## Tóm tắt

- **Đơn ánh**: $$x_1 \ne x_2 \Rightarrow f(x_1) \ne f(x_2)$$; không gộp hai đầu vào khác nhau về cùng một đầu ra.
- **Toàn ánh**: mọi $$y \in B$$ đều có ít nhất một tiền ảnh trong $$A$$.
- **Song ánh**: vừa đơn ánh vừa toàn ánh, thiết lập ghép cặp một–một giữa hai tập hợp.
- **Domain và codomain** quyết định tính chất của hàm — cùng một công thức nhưng khác miền có thể cho tính chất khác nhau.
- **Ứng dụng trong Khoa học Máy tính**: mã hóa khả nghịch, khóa chính, bảng băm, serialization.

Trong bài tiếp theo, chúng ta sẽ tìm hiểu hàm hợp và hàm nghịch đảo.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=bZred_Ksz2k">INJECTIVE, SURJECTIVE, and BIJECTIVE FUNCTIONS - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giới thiệu trực quan về đơn ánh, toàn ánh và song ánh.
- <a href="https://www.youtube.com/watch?v=VaDja04e59M">[Discrete Mathematics] Surjective Functions Examples</a> — TrevTutor, tiếng Anh. Luyện tập nhận diện hàm toàn ánh qua các ví dụ cụ thể.
- <a href="https://www.youtube.com/watch?v=Kn-LrdgHVhQ">[Discrete Mathematics] Functions Examples</a> — TrevTutor, tiếng Anh. Bổ sung thêm ví dụ phân loại tính chất hàm số.
