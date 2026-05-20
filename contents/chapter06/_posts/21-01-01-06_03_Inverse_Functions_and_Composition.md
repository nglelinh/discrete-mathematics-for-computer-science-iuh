---
layout: post
title: "Hàm nghịch đảo và Hàm hợp"
categories: chapter06
date: 2021-01-01
order: 3
required: true
lang: en
---

# Hàm nghịch đảo và Hàm hợp

Trong một hệ thống lớn, dữ liệu hiếm khi đi qua đúng một bước. Nó được chuẩn hóa, mã hóa, ánh xạ, rồi chuyển tiếp qua nhiều tầng xử lý. Vì thế, hai câu hỏi quan trọng luôn xuất hiện: có thể đảo ngược phép biến đổi này không, và nếu ghép nhiều phép biến đổi lại thì kết quả cuối cùng ra sao?

**Hàm ngược** và **hợp hàm** trả lời trực tiếp hai câu hỏi đó. Chúng đứng sau quy trình mã hóa–giải mã, pipeline xử lý dữ liệu, chuyển đổi kiểu, và rất nhiều cấu trúc trong toán rời rạc. Nắm chắc phần này giúp bạn nhìn các phép biến đổi như những khối lắp ghép có quy luật, không phải các thao tác rời rạc không liên quan.

## 1. Hàm hợp

**Định nghĩa**: Cho $$f:A\to B$$ và $$g:B\to C$$. **Hàm hợp** của $$g$$ sau $$f$$ là hàm $$g\circ f:A\to C$$ xác định bởi:

$$(g\circ f)(x)=g(f(x)).$$

**Ký hiệu**: $$g\circ f$$ đọc là "g hợp f" hoặc "g sau f". Tính $$f$$ trước, rồi tính $$g$$.

**Ví dụ**: Với $$f(x)=2x+1$$ và $$g(x)=x^2$$:

$$(g\circ f)(x)=(2x+1)^2,$$

$$(f\circ g)(x)=2x^2+1.$$

Hai biểu thức thường khác nhau; phép hợp không giao hoán.

## 2. Điều kiện để hợp được

Để $$g\circ f$$ xác định, mọi giá trị $$f(x)$$ phải thuộc domain của $$g$$. Nói cách khác:

$$f(A)\subseteq \operatorname{dom}(g).$$

**Ví dụ**: Nếu $$f:\mathbb{R}\to\mathbb{R}$$, $$f(x)=x^2$$ và $$g:[0,\infty)\to\mathbb{R}$$, $$g(x)=\sqrt{x}$$, thì $$g\circ f$$ xác định vì $$f(\mathbb{R})=[0,\infty)$$.

## 3. Tính kết hợp của hàm hợp

**Định lý**: Nếu các hàm hợp xác định, thì:

$$h\circ(g\circ f)=(h\circ g)\circ f.$$

### Chứng minh

Với mọi $$x$$ trong domain của $$f$$:

$$[h\circ(g\circ f)](x)=h((g\circ f)(x))=h(g(f(x))).$$

Mặt khác:

$$[(h\circ g)\circ f](x)=(h\circ g)(f(x))=h(g(f(x))).$$

Hai vế cho cùng giá trị với mọi $$x$$, nên hai hàm bằng nhau.

## 4. Hàm đồng nhất

**Định nghĩa**: Hàm đồng nhất trên $$A$$ là $$id_A:A\to A$$, $$id_A(x)=x$$.

**Tính chất**:

$$f\circ id_A=f,$$

$$id_B\circ f=f$$

với $$f:A\to B$$.

Hàm đồng nhất đóng vai trò phần tử trung hòa của phép hợp.

## 5. Hàm nghịch đảo

**Định nghĩa**: Với $$f:A\to B$$, một hàm $$g:B\to A$$ được gọi là **hàm nghịch đảo** của $$f$$ nếu:

$$g\circ f=id_A$$

và

$$f\circ g=id_B.$$

Khi tồn tại, ta viết $$g=f^{-1}$$.

**Định lý**: Hàm $$f:A\to B$$ có nghịch đảo hai phía khi và chỉ khi $$f$$ là song ánh.

### Chứng minh ý chính

Nếu $$f$$ có nghịch đảo, thì mỗi $$y\in B$$ được đạt bởi $$x=f^{-1}(y)$$, nên $$f$$ toàn ánh. Nếu $$f(x_1)=f(x_2)$$, áp dụng $$f^{-1}$$ hai vế được $$x_1=x_2$$, nên $$f$$ đơn ánh. Vậy $$f$$ song ánh.

Ngược lại, nếu $$f$$ song ánh, mỗi $$y\in B$$ có đúng một tiền ảnh $$x\in A$$. Định nghĩa $$f^{-1}(y)=x$$. Hàm này thỏa hai điều kiện nghịch đảo.

## 6. Tìm hàm nghịch đảo

**Ví dụ**: Tìm nghịch đảo của $$f:\mathbb{R}\to\mathbb{R}$$, $$f(x)=3x-2$$.

Đặt $$y=3x-2$$. Giải theo $$x$$:

$$x=\frac{y+2}{3}.$$

Vậy:

$$f^{-1}(y)=\frac{y+2}{3}.$$

Đổi biến thường viết:

$$f^{-1}(x)=\frac{x+2}{3}.$$

## 7. Khi nào không có nghịch đảo?

Hàm $$f:\mathbb{R}\to\mathbb{R}$$, $$f(x)=x^2$$ không có nghịch đảo trên toàn $$\mathbb{R}$$ vì không đơn ánh: $$f(2)=f(-2)$$. Nếu hạn chế domain thành $$[0,\infty)$$ và codomain $$[0,\infty)$$, hàm trở thành song ánh và có nghịch đảo $$f^{-1}(x)=\sqrt{x}$$.

## 8. Công cụ tương tác

<div class="interactive-demo" data-demo="composition-inverse-pipeline">
  <p><strong>Demo đề xuất:</strong> kéo các hàm vào pipeline để xem $$g\circ f$$, thử thêm hàm nghịch đảo và quan sát khi pipeline trở về hàm đồng nhất.</p>
</div>

## 9. Nhầm lẫn thường gặp

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn 1**: Tính $$g\circ f$$ theo thứ tự trái sang phải. Thực ra $$f$$ chạy trước.

**Nhầm lẫn 2**: Nghĩ mọi hàm đều có nghịch đảo. Chỉ song ánh mới có nghịch đảo hai phía.

**Nhầm lẫn 3**: Ký hiệu $$f^{-1}$$ cho hàm nghịch đảo không giống $$1/f(x)$$. Ví dụ $$f(x)=x+1$$ thì $$f^{-1}(x)=x-1$$, không phải $$1/(x+1)$$.
</div>

## 10. Ứng dụng trong Khoa học Máy tính

```python
def clean(s):
    return s.strip().lower()

def tokenize(s):
    return s.split()

result = tokenize(clean("  Discrete Math  "))
```

- **Pipeline dữ liệu**: mỗi bước là một hàm, toàn pipeline là hàm hợp.
- **Mật mã học**: mã hóa và giải mã phải là hai hàm nghịch đảo trên không gian thông điệp hợp lệ.
- **Serialization**: `decode(encode(x)) = x` là điều kiện nghịch đảo một phía quan trọng.
- **Lập trình hàm**: composition giúp xây dựng chương trình lớn từ hàm nhỏ.

## Tóm tắt

Hàm hợp ghép các biến đổi theo thứ tự xác định và có tính kết hợp nhưng không giao hoán. Hàm đồng nhất là phần tử trung hòa. Hàm nghịch đảo tồn tại chính xác khi hàm ban đầu là song ánh; nó mô hình hóa thao tác undo, decode, deserialize và các biến đổi không mất thông tin.
