---
layout: post
title: "Tính chất của Hàm số"
categories: chapter06
date: 2021-01-01
order: 2
required: true
lang: en
---

# Tính chất của Hàm số

Không phải hàm nào cũng “tốt” theo cùng một nghĩa. Có hàm làm hai đầu vào khác nhau đổ vào cùng một kết quả; có hàm bao phủ toàn bộ đầu ra; có hàm vừa phân biệt được mọi đầu vào vừa khớp kín mọi đầu ra. Trong kỹ thuật phần mềm, những khác biệt đó ảnh hưởng trực tiếp đến mã hóa dữ liệu, ánh xạ khóa, nén thông tin và thiết kế API.

Các tính chất **đơn ánh, toàn ánh, song ánh** giúp ta đo chất lượng của một phép ánh xạ. Chúng cho biết thông tin có bị mất không, mọi đích có được dùng hết không, và liệu ta có thể “đi ngược” lại từ đầu ra về đầu vào hay không. Đây là phần rất toán học nhưng cũng rất thực dụng.

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

<div class="content-box warning-box" markdown="1">
**Ghi nhớ**: Không thể kết luận đơn ánh/toàn ánh chỉ từ công thức. Phải biết domain và codomain.
</div>

## 5. Hàm hữu hạn và nguyên lý đếm

Nếu $$A$$ và $$B$$ hữu hạn:

- Nếu $$f:A\to B$$ đơn ánh thì $$|A|\le |B|$$.
- Nếu $$f:A\to B$$ toàn ánh thì $$|A|\ge |B|$$.
- Nếu $$f:A\to B$$ song ánh thì $$|A|=|B|$$.

### Chứng minh trực giác

Đơn ánh không cho phép hai phần tử của $$A$$ dùng chung một phần tử của $$B$$, nên $$B$$ phải có ít nhất đủ chỗ. Toàn ánh yêu cầu phủ hết $$B$$, nên $$A$$ phải có đủ phần tử để tạo ảnh cho mọi phần tử của $$B$$.

## 6. Công cụ tương tác

<div class="interactive-tool" data-tool="function-property-checker">
  <p><strong>Demo đề xuất:</strong> sinh viên nối mũi tên giữa hai tập hữu hạn; công cụ kiểm tra đơn ánh, toàn ánh, song ánh và giải thích bằng phần tử gây lỗi.</p>
</div>

## 7. Nhầm lẫn thường gặp

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn 1**: Đơn ánh không có nghĩa là mọi phần tử codomain đều được dùng. Đó là toàn ánh.

**Nhầm lẫn 2**: Toàn ánh vẫn cho phép nhiều đầu vào cùng một đầu ra. Điều này chỉ bị cấm bởi đơn ánh.

**Nhầm lẫn 3**: Song ánh không chỉ là "có vẻ ghép đôi"; phải chứng minh cả đơn ánh và toàn ánh.
</div>

## 8. Ứng dụng trong Khoa học Máy tính

- **Mã hóa khả nghịch** cần song ánh giữa không gian bản rõ và bản mã.
- **Hash table** thường không đơn ánh vì có va chạm.
- **Serialization** tốt nên gần song ánh: serialize rồi deserialize phải thu lại dữ liệu ban đầu.
- **Database primary key** tạo đơn ánh từ bản ghi sang khóa.
- **Load balancing** thường là toàn ánh nếu mọi server đều nhận ít nhất một job.

## Tóm tắt

Đơn ánh bảo toàn phân biệt đầu vào; toàn ánh phủ hết codomain; song ánh làm cả hai và do đó có thể đảo ngược. Khi xét các tính chất này, luôn nêu rõ domain và codomain. Với tập hữu hạn, các tính chất này liên hệ trực tiếp với so sánh lực lượng.
