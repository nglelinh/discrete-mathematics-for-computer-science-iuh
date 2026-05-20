---
layout: post
title: "Giới thiệu Hàm số"
categories: chapter06
date: 2021-01-01
order: 1
required: true
lang: en
---

# Giới thiệu Hàm số

Trong lập trình, khái niệm “hàm” quen đến mức ta dễ quên rằng nó là một ý tưởng toán học rất sâu: mỗi đầu vào phải được ghép với đúng một đầu ra. Từ hàm `abs(x)` trong Python đến API biến yêu cầu người dùng thành kết quả trả về, từ bộ mã hóa dữ liệu đến mô hình machine learning, tư duy hàm xuất hiện ở khắp nơi.

Bài này đưa khái niệm đó về nền tảng rời rạc: **hàm số** như một quan hệ đặc biệt, có miền xác định, miền giá trị và quy tắc ánh xạ rõ ràng. Hiểu hàm ở mức bản chất giúp ta đọc đặc tả chính xác hơn, phân tích dependency tốt hơn và chuẩn bị cho các chủ đề về đếm, thuật toán, mật mã và cấu trúc dữ liệu.

## 1. Định nghĩa hàm số

**Định nghĩa**: Cho hai tập $$A$$ và $$B$$. Một **hàm số** $$f$$ từ $$A$$ đến $$B$$, ký hiệu $$f:A\to B$$, là một quy tắc gán cho mỗi phần tử $$x\in A$$ đúng một phần tử $$y\in B$$.

**Ký hiệu**:

- $$A$$: miền xác định (domain).
- $$B$$: miền đích hoặc đối miền (codomain).
- $$f(x)$$: giá trị của hàm tại $$x$$.
- $$f(A)=\{f(x)\mid x\in A\}$$: ảnh hoặc tập giá trị thực sự đạt được.

**Ví dụ**: Hàm $$f:\mathbb{R}\to\mathbb{R}$$, $$f(x)=x^2$$ có domain và codomain đều là $$\mathbb{R}$$, nhưng ảnh là $$[0,\infty)$$.

## 2. Hàm số như quan hệ đặc biệt

Một quan hệ $$R\subseteq A\times B$$ là hàm từ $$A$$ đến $$B$$ nếu:

1. **Tồn tại**: với mọi $$a\in A$$, tồn tại $$b\in B$$ sao cho $$(a,b)\in R$$.
2. **Duy nhất**: nếu $$(a,b_1)\in R$$ và $$(a,b_2)\in R$$ thì $$b_1=b_2$$.

**Ví dụ**: $$R=\{(1,a),(2,b),(3,b)\}$$ là hàm từ $$\{1,2,3\}$$ đến $$\{a,b\}$$. Nhưng $$S=\{(1,a),(1,b),(2,b)\}$$ không là hàm vì đầu vào 1 có hai đầu ra.

## 3. Domain, codomain và range

**Định nghĩa**:

- **Domain**: tập tất cả đầu vào hợp lệ.
- **Codomain**: tập mà đầu ra được khai báo thuộc về.
- **Range/Image**: tập đầu ra thật sự xuất hiện.

**Ví dụ**: Với $$f:\mathbb{Z}\to\mathbb{Z}$$, $$f(n)=2n$$:

- Domain: $$\mathbb{Z}$$.
- Codomain: $$\mathbb{Z}$$.
- Range: tập số chẵn.

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn phổ biến**: Codomain và range không nhất thiết giống nhau. Codomain là nơi hàm được khai báo trả về; range là phần thật sự được chạm tới.
</div>

## 4. Các cách biểu diễn hàm

### Bằng công thức

$$f(x)=3x+1.$$

### Bằng bảng

| $$x$$ | 1 | 2 | 3 |
|---|---:|---:|---:|
| $$f(x)$$ | 4 | 7 | 10 |

### Bằng tập cặp có thứ tự

$$f=\{(1,4),(2,7),(3,10)\}.$$

### Bằng sơ đồ mũi tên

Mỗi phần tử domain có đúng một mũi tên đi ra.

## 5. Hàm toàn phần và hàm bộ phận

**Định nghĩa**: Hàm trong toán rời rạc thường là **hàm toàn phần**: mọi phần tử của domain đều có ảnh. Trong lập trình, ta cũng gặp **hàm bộ phận**, tức chỉ xác định trên một phần domain.

**Ví dụ**: $$g(x)=1/x$$ là hàm từ $$\mathbb{R}\setminus\{0\}$$ đến $$\mathbb{R}$$, nhưng không là hàm toàn phần từ $$\mathbb{R}$$ đến $$\mathbb{R}$$.

## 6. Hàm trong lập trình

```python
def square(x):
    return x * x
```

Nếu xem kiểu `int -> int`, đây là một mô hình của hàm toán học. Tuy nhiên, trong lập trình thực tế còn có ngoại lệ, trạng thái toàn cục, I/O và không dừng; các yếu tố này làm hàm lập trình phức tạp hơn hàm toán học thuần túy.

## 7. Công cụ tương tác

<div class="interactive-demo" data-demo="function-arrow-checker">
  <p><strong>Demo đề xuất:</strong> kéo mũi tên từ domain sang codomain; công cụ báo khi một quan hệ không phải hàm vì thiếu đầu ra hoặc có nhiều đầu ra.</p>
</div>

## 8. Nhầm lẫn thường gặp

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn 1**: Một đầu ra có thể nhận từ nhiều đầu vào vẫn là hàm. Điều bị cấm là một đầu vào có nhiều đầu ra.

**Nhầm lẫn 2**: Quên khai báo domain. Công thức $$\sqrt{x}$$ có ý nghĩa khác nhau trên $$\mathbb{R}_{\ge0}$$ và trên $$\mathbb{R}$$.

**Nhầm lẫn 3**: Nghĩ mọi quan hệ đều là hàm. Hàm là quan hệ có ràng buộc duy nhất ở đầu vào.
</div>

## 9. Ứng dụng trong Khoa học Máy tính

- **API**: ánh xạ request hợp lệ đến response.
- **Hash function**: ánh xạ dữ liệu sang giá trị băm.
- **Database key**: ánh xạ khóa chính đến bản ghi.
- **Functional programming**: ưu tiên hàm thuần túy để dễ kiểm thử và suy luận.
- **Machine learning**: mô hình học máy là hàm xấp xỉ từ đặc trưng đầu vào đến dự đoán.

## Tóm tắt

Hàm số là quan hệ gán mỗi đầu vào đúng một đầu ra. Cần phân biệt domain, codomain và range. Hàm có thể biểu diễn bằng công thức, bảng, tập cặp hoặc sơ đồ. Trong khoa học máy tính, hàm là mô hình trung tâm của tính toán xác định.
