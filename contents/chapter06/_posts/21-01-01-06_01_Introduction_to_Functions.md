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

Từ một user ID trả về hồ sơ người dùng, từ một chuỗi đầu vào trả về giá trị băm, hay từ một chỉ số mảng lấy ra đúng một phần tử, ta đều đang dùng cùng một ý tưởng: mỗi đầu vào hợp lệ phải được gắn với **một** đầu ra xác định.


Trong khoa học máy tính, hàm số xuất hiện ở khắp nơi, từ ánh xạ đầu vào sang đầu ra đến biến đổi dữ liệu và mô hình hóa trạng thái.
Đó chính là tinh thần của **hàm số**. Trong toán rời rạc, hàm là một dạng quan hệ rất đặc biệt. Trong khoa học máy tính, nó là mô hình phía sau lời gọi hàm, ánh xạ khóa và giá trị, biến đổi dữ liệu, mã hóa và rất nhiều cơ chế xử lý thông tin khác.

Điều quan trọng không nằm ở ký hiệu, mà ở tính xác định. Nếu cùng một đầu vào sinh ra nhiều đầu ra khác nhau, ta không còn hàm nữa. Nhận ra ranh giới này giúp ta mô hình hóa đúng và tránh nhầm lẫn giữa quan hệ tổng quát với hàm số.

Trong bài này, chúng ta sẽ đi từ định nghĩa hình thức của hàm đến miền xác định, miền giá trị và cách nhìn hàm như một công cụ ánh xạ trong toán lẫn lập trình.

## 1. Định nghĩa hàm số

Phần này đặt lại ngôn ngữ chung của bài học. Nắm chắc định nghĩa trước sẽ giúp các ví dụ và định lý phía sau trở nên dễ theo dõi hơn.

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

Nếu dùng công cụ này, hãy dự đoán kết quả trước rồi mới thao tác. Việc so sánh dự đoán với kết quả thật sẽ giúp khái niệm bám chắc hơn.

<div class="interactive-demo" data-demo="function-arrow-checker">
  <p><strong>Demo đề xuất:</strong> kéo mũi tên từ domain sang codomain; công cụ báo khi một quan hệ không phải hàm vì thiếu đầu ra hoặc có nhiều đầu ra.</p>
</div>

<script src="{{ '/public/js/function-arrow-checker.js' | relative_url }}"></script>

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

## Hàm số trong AI và Machine Learning

Trong AI, mô hình thường được nhìn như một hàm ánh xạ đầu vào sang đầu ra: ảnh $$\to$$ nhãn lớp, văn bản $$\to$$ cảm xúc, hay dữ liệu lịch sử $$\to$$ giá trị dự đoán. Vì thế, bài toán classification và regression đều có thể xem là xây hàm xấp xỉ từ dữ liệu.

Neural network là hợp của nhiều hàm nhỏ: phép nhân ma trận, cộng bias và activation function như ReLU hay sigmoid. Mỗi tầng nhận đầu ra của tầng trước, nên toàn mạng là một composition of functions.

Trong recommendation systems, ta thường cần hàm $$f(user, item)\to rating$$ để dự đoán mức độ phù hợp giữa người dùng và sản phẩm.

```python
def classify(score):
    return "pass" if score >= 0.5 else "fail"

class MockModel:
    def predict(self, X):
        return [classify(x[0]) for x in X]
```

Đoạn mã trên mô phỏng kiểu `predict()` quen thuộc trong `sklearn`: nhận tập đầu vào và trả về đầu ra xác định cho từng mẫu.

## Bài tập thực hành

### Bài tập 1: Kiểm tra hàm

Xét quan hệ $$R = \{(1,2),(2,4),(3,6)\}$$ trên $$\N$$.  
Hỏi $$R$$ có phải là hàm không? Giải thích.

<details>
<summary>Đáp án</summary>

Có, vì mỗi phần tử domain chỉ ánh xạ đến đúng một giá trị.

</details>

### Bài tập 2: Xác định domain, codomain, range

Cho hàm $$f: \N \to \N$$, $$f(x) = x^2 + 1$$.  
Xác định domain, codomain và range.

<details>
<summary>Đáp án</summary>

- Domain: $$\N$$
- Codomain: $$\N$$
- Range: $$\{2,5,10,17,...\}$$ (các số có dạng $$n^2+1$$)

</details>

### Bài tập 3: Hàm trong Python

Viết hàm Python tương ứng với $$f(x) = 2x + 1$$ và kiểm tra với input 3.

<details>
<summary>Đáp án</summary>

```python
def f(x):
    return 2 * x + 1

print(f(3))  # 7
```

</details>

## Tóm tắt

Trước khi rời bài, hãy kiểm tra xem bạn có thể tự nhắc lại ý chính, điều kiện áp dụng và một ví dụ tiêu biểu mà không cần nhìn tài liệu hay không.

Hàm số là quan hệ gán mỗi đầu vào đúng một đầu ra. Cần phân biệt domain, codomain và range. Hàm có thể biểu diễn bằng công thức, bảng, tập cặp hoặc sơ đồ. Trong khoa học máy tính, hàm là mô hình trung tâm của tính toán xác định.
