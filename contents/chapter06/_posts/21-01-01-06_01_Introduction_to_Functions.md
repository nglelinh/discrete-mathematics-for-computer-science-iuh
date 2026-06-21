---
layout: post
title: "Giới thiệu Hàm số"
categories: chapter06
date: 2021-01-01
order: 1
required: true
lang: en
---

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

![Hàm số như máy ánh xạ đầu vào → đầu ra](/discrete-mathematics-for-computer-science-iuh/img/course/Function_machine2.svg)

*Hình 6.1: Hàm số ánh xạ mỗi phần tử miền xác định đến đúng một phần tử miền đích — mô hình "hộp hàm".*

## 2. Hàm số như quan hệ đặc biệt

Một quan hệ $$R\subseteq A\times B$$ là hàm từ $$A$$ đến $$B$$ nếu:

1. **Tồn tại**: với mọi $$a\in A$$, tồn tại $$b\in B$$ sao cho $$(a,b)\in R$$.
2. **Duy nhất**: nếu $$(a,b_1)\in R$$ và $$(a,b_2)\in R$$ thì $$b_1=b_2$$.

**Ví dụ**: $$R=\{(1,a),(2,b),(3,b)\}$$ là hàm từ $$\{1,2,3\}$$ đến $$\{a,b\}$$. Nhưng $$S=\{(1,a),(1,b),(2,b)\}$$ không là hàm vì đầu vào 1 có hai đầu ra.

![Hàm song ánh — mỗi đầu vào một đầu ra](/discrete-mathematics-for-computer-science-iuh/img/course/Bijection.svg)

*Hình 6.2: Hàm là quan hệ đặc biệt — mỗi phần tử domain có đúng một mũi tên đi ra (tồn tại + duy nhất).*

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

![Sơ đồ mũi tên — biểu diễn hàm số](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

*Hình 6.3: Sơ đồ mũi tên thể hiện ánh xạ từ tập A sang tập B — mỗi phần tử A có đúng một cung đi ra.*

## 5. Hàm toàn phần và hàm bộ phận

**Định nghĩa**: Hàm trong toán rời rạc thường là **hàm toàn phần**: mọi phần tử của domain đều có ảnh. Trong lập trình, ta cũng gặp **hàm bộ phận**, tức chỉ xác định trên một phần domain.

**Ví dụ**: $$g(x)=1/x$$ là hàm từ $$\mathbb{R}\setminus\{0\}$$ đến $$\mathbb{R}$$, nhưng không là hàm toàn phần từ $$\mathbb{R}$$ đến $$\mathbb{R}$$.

![Hàm đơn ánh — không gộp hai đầu vào](/discrete-mathematics-for-computer-science-iuh/img/course/Injection.svg)

*Hình 6.4: Hàm bộ phần chỉ xác định trên một phần domain — tương tự hàm đơn ánh không cho hai đầu vào khác nhau cùng đầu ra.*

## 6. Hàm trong lập trình

```python
def square(x):
    return x * x
```

Nếu xem kiểu `int -> int`, đây là một mô hình của hàm toán học. Tuy nhiên, trong lập trình thực tế còn có ngoại lệ, trạng thái toàn cục, I/O và không dừng; các yếu tố này làm hàm lập trình phức tạp hơn hàm toán học thuần túy.

## Định lý: Số hàm từ tập hữu hạn sang tập hữu hạn

**Định lý**: Số hàm từ tập $$A$$ ($$\lvert A \rvert = n$$) sang tập $$B$$ ($$\lvert B \rvert = m$$) là $$m^n$$.

**Chứng minh**:

Mỗi hàm $$f: A \to B$$ được xác định bởi giá trị $$f(a)$$ cho từng $$a \in A$$.  
Với mỗi $$a$$, có $$m$$ lựa chọn trong $$B$$.  
Tổng số cách: $$m \times m \times \cdots \times m$$ ($$n$$ lần) $$= m^n$$.

**Hệ quả**:

- Số hàm từ $$\{0,1\}^n$$ sang $$\{0,1\}$$: $$2^{2^n}$$ (đúng bằng số hàm Boolean trên $$n$$ biến — đã gặp ở 01_01).
- Số hàm từ tập $$n$$ phần tử sang chính nó: $$n^n$$ (số hoán vị chỉ là $$n!$$).

**Ý nghĩa CS**:

- **Không gian hàm** trong machine learning rất lớn → cần regularization / inductive bias.
- **Enumeration** của tất cả hàm khả dĩ chỉ thực tế khi $$n$$ nhỏ.

## Hàm số trong AI và Machine Learning

Trong AI, mô hình thường được nhìn như một hàm ánh xạ đầu vào sang đầu ra: ảnh $$\to$$ nhãn lớp, văn bản $$\to$$ cảm xúc, hay dữ liệu lịch sử $$\to$$ giá trị dự đoán. Vì thế, bài toán classification và regression đều có thể xem là xây hàm xấp xỉ từ dữ liệu.

Neural network là hợp của nhiều hàm nhỏ: phép nhân ma trận, cộng bias và activation function như ReLU hay sigmoid. Mỗi tầng nhận đầu ra của tầng trước, nên toàn mạng là một composition of functions.

![Mạng neural — hợp của nhiều hàm](/discrete-mathematics-for-computer-science-iuh/img/course/Neural_network.svg)

*Hình 6.5: Neural network là composition of functions — mỗi tầng là một hàm ánh xạ vector đầu vào sang vector đầu ra.*

Trong recommendation systems, ta thường cần hàm $$f(user, item)\to rating$$ để dự đoán mức độ phù hợp giữa người dùng và sản phẩm.

```python
def classify(score):
    return "pass" if score >= 0.5 else "fail"

class MockModel:
    def predict(self, X):
        return [classify(x[0]) for x in X]
```

Đoạn mã trên mô phỏng kiểu `predict()` quen thuộc trong `sklearn`: nhận tập đầu vào và trả về đầu ra xác định cho từng mẫu.

## 9. Ứng dụng trong Khoa học Máy tính

- **API**: ánh xạ request hợp lệ đến response.
- **Hash function**: ánh xạ dữ liệu sang giá trị băm.
- **Database key**: ánh xạ khóa chính đến bản ghi.
- **Functional programming**: ưu tiên hàm thuần túy để dễ kiểm thử và suy luận.
- **Machine learning**: mô hình học máy là hàm xấp xỉ từ đặc trưng đầu vào đến dự đoán.

![Hash function — ánh xạ khóa → giá trị](/discrete-mathematics-for-computer-science-iuh/img/course/Database.svg)

*Hình 6.6: Hash function và database key là ví dụ hàm thực tế — ánh xạ dữ liệu đầu vào sang giá trị xác định.*

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
