---
layout: post
title: "Tính chất của Hàm số"
categories: chapter06
date: 2021-01-01
order: 2
required: true
lang: en
---

Biết một ánh xạ là hàm vẫn chưa đủ để hiểu nó mạnh đến đâu. Trong nhiều bài toán, điều quan trọng là xem hàm có làm mất thông tin không, có bao phủ hết miền đích không, và có thể đảo ngược được không.


Trong khoa học máy tính, hàm số xuất hiện ở khắp nơi, từ ánh xạ đầu vào sang đầu ra đến biến đổi dữ liệu và mô hình hóa trạng thái.
Đó là lý do các tính chất như **đơn ánh**, **toàn ánh** và **song ánh** trở nên rất quan trọng. Chúng xuất hiện trong thiết kế mã định danh, băm hoàn hảo, nén và giải nén dữ liệu, ánh xạ địa chỉ bộ nhớ, cũng như nhiều chứng minh về số lượng phần tử giữa các tập hợp.

Một hàm đơn ánh nói rằng các đầu vào khác nhau không bị gộp mất. Một hàm toàn ánh nói rằng mọi giá trị ở đầu ra đều thật sự được chạm tới. Khi cả hai cùng đúng, ta có song ánh, một tình huống cực kỳ đẹp vì nó cho phép ghép cặp chính xác giữa hai tập.

Trong bài học này, chúng ta sẽ học cách kiểm tra các tính chất đó và hiểu vì sao chúng là chìa khóa cho nhiều khái niệm sâu hơn ở phía sau.

## 1. Đơn ánh

**Định nghĩa**: Hàm $$f:A\to B$$ là **đơn ánh** (injective, one-to-one) nếu hai đầu vào khác nhau luôn cho hai đầu ra khác nhau:

$$x_1\ne x_2 \Rightarrow f(x_1)\ne f(x_2).$$

**Ký hiệu**: $$f:A\to B$$ cho biết domain là $$A$$ và codomain là $$B$$; $$x_1,x_2$$ thường ký hiệu hai đầu vào bất kỳ, còn $$y$$ ký hiệu một đầu ra trong codomain.

Dạng tương đương thường dùng để chứng minh:

$$f(x_1)=f(x_2)\Rightarrow x_1=x_2.$$

**Ví dụ**: $$f:\mathbb{R}\to\mathbb{R}$$, $$f(x)=2x+3$$ là đơn ánh.

**Chứng minh**: Giả sử $$f(x_1)=f(x_2)$$. Khi đó:

$$2x_1+3=2x_2+3\Rightarrow 2x_1=2x_2\Rightarrow x_1=x_2.$$

Vậy $$f$$ đơn ánh.

**Phản ví dụ**: $$g:\mathbb{R}\to\mathbb{R}$$, $$g(x)=x^2$$ không đơn ánh vì $$g(2)=g(-2)=4$$ nhưng $$2\ne-2$$.

## 2. Toàn ánh

**Định nghĩa**: Hàm $$f:A\to B$$ là **toàn ánh** (surjective, onto) nếu mọi phần tử của codomain đều được đạt tới:

$$\forall y\in B,\exists x\in A\text{ sao cho }f(x)=y.$$

**Ví dụ**: $$f:\mathbb{R}\to\mathbb{R}$$, $$f(x)=x^3$$ là toàn ánh.

**Chứng minh**: Lấy $$y\in\mathbb{R}$$ tùy ý. Chọn $$x=\sqrt[3]{y}$$. Khi đó $$f(x)=x^3=y$$. Vậy mọi $$y$$ đều có tiền ảnh.

**Phản ví dụ**: $$g:\mathbb{R}\to\mathbb{R}$$, $$g(x)=x^2$$ không toàn ánh vì không có $$x\in\mathbb{R}$$ nào thỏa $$x^2=-1$$.

## 3. Song ánh

**Định nghĩa**: Hàm $$f:A\to B$$ là **song ánh** (bijective) nếu vừa đơn ánh vừa toàn ánh.

Song ánh thiết lập sự ghép cặp một-một giữa $$A$$ và $$B$$. Khi đó mỗi $$y\in B$$ có đúng một tiền ảnh trong $$A$$.

**Ví dụ**: $$f:\mathbb{R}\to\mathbb{R}$$, $$f(x)=x+5$$ là song ánh.

**Chứng minh**:

- Đơn ánh: $$x_1+5=x_2+5\Rightarrow x_1=x_2$$.
- Toàn ánh: với $$y\in\mathbb{R}$$, chọn $$x=y-5$$ thì $$f(x)=y$$.

Vậy $$f$$ song ánh.

## 4. Vai trò của domain và codomain

Cùng một công thức có thể có tính chất khác nhau nếu domain/codomain khác nhau.

**Ví dụ**: $$f(x)=x^2$$.

- $$f:\mathbb{R}\to\mathbb{R}$$: không đơn ánh, không toàn ánh.
- $$f:\mathbb{R}\to[0,\infty)$$: không đơn ánh, nhưng toàn ánh.
- $$f:[0,\infty)\to[0,\infty)$$: song ánh.



## 8. Ứng dụng trong Khoa học Máy tính

- **Mã hóa khả nghịch** cần song ánh giữa không gian bản rõ và bản mã.
- **Hash table** thường không đơn ánh vì có va chạm.
- **Serialization** tốt nên gần song ánh: serialize rồi deserialize phải thu lại dữ liệu ban đầu.
- **Database primary key** tạo đơn ánh từ bản ghi sang khóa.
- **Load balancing** thường là toàn ánh nếu mọi server đều nhận ít nhất một job.

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

## Tóm tắt

Trước khi rời bài, hãy kiểm tra xem bạn có thể tự nhắc lại ý chính, điều kiện áp dụng và một ví dụ tiêu biểu mà không cần nhìn tài liệu hay không.

Đơn ánh bảo toàn phân biệt đầu vào; toàn ánh phủ hết codomain; song ánh làm cả hai và do đó có thể đảo ngược. Khi xét các tính chất này, luôn nêu rõ domain và codomain. Với tập hữu hạn, các tính chất này liên hệ trực tiếp với so sánh lực lượng.
