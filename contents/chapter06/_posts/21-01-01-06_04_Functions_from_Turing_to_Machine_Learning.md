---
layout: post
title: "Hàm số: Từ Turing đến Học máy"
categories: chapter06
date: 2021-01-01
order: 4
required: false
lang: en
---

# Hàm số: Từ Turing đến Học máy

Ý tưởng về hàm số nghe có vẻ quen đến mức dễ bị xem nhẹ.
Ta đã thấy nó từ phổ thông:
mỗi đầu vào cho đúng một đầu ra.

Nhưng trong khoa học máy tính,
khái niệm hàm không chỉ là bài toán vẽ đồ thị.
Nó trở thành nền của functional programming,
API design,
cryptographic hash,
và cả machine learning models.

Từ tư tưởng của Church và Turing,
đến `map`, `filter`, `reduce`,
đến mô hình dự đoán xác suất,
bài học này cho thấy vì sao một khái niệm toán học cổ điển
lại sống ở trung tâm của computing hiện đại.

---

## Phần 1: Lịch sử — từ hàm toán học đến hàm tính toán

### 1.1. Hàm trước thời máy tính

Trong toán học cổ điển,
hàm giúp mô tả sự phụ thuộc:
đầu vào thay đổi,
đầu ra thay đổi theo quy luật.

Ví dụ,
$f(x)=x^2$ là cách nén vô số cặp giá trị thành một công thức ngắn.
Đây là sức mạnh lớn đầu tiên của hàm:
biến quy luật thành đối tượng có thể thao tác.

### 1.2. Church, lambda calculus, và khái niệm tính toán

Khi khoa học máy tính chưa tồn tại như một ngành độc lập,
Alonzo Church đã dùng lambda calculus để nghiên cứu computation bằng ngôn ngữ của hàm.

Ý tưởng rất táo bạo:
ta có thể biểu diễn việc tính toán như áp dụng hàm lên đối số,
rồi rút gọn biểu thức theo quy tắc chính xác.

Lambda calculus không phải ngôn ngữ lập trình thực dụng đầu tiên,
nhưng nó ảnh hưởng sâu lên Haskell,
ML,
Scala,
F#,
và nhiều ngôn ngữ hiện đại.

### 1.3. Turing và mô hình cơ học của tính toán

Alan Turing tiếp cận vấn đề từ góc khác:
thay vì bắt đầu bằng hàm trừu tượng,
ông mô hình hóa một cỗ máy thao tác ký hiệu trên băng.

Church và Turing đi hai đường,
nhưng gặp nhau ở cùng kết luận:
có một khái niệm sâu về “tính được”.

Trong đó,
hàm tính toán được (computable function)
trở thành đối tượng cốt lõi.

![Church và Turing]
*Hình 1: Church và Turing giúp biến “hàm” từ khái niệm toán học thành khái niệm trung tâm của computation.*

---

## Phần 2: Functional programming — khi chương trình được xây từ hàm

### 2.1. Khai báo điều muốn làm thay vì điều khiển từng bước

Functional programming đặt hàm ở trung tâm thiết kế chương trình.
Thay vì tập trung vào biến đổi trạng thái,
nó khuyến khích:

- pure functions,
- immutability,
- composition,
- higher-order functions.

Ý tưởng này rất hấp dẫn,
vì nó làm reasoning về chương trình dễ hơn trong nhiều tình huống.

### 2.2. `map`, `filter`, `reduce`

Ví dụ Python:

```python
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
total = sum(nums)
```

Mỗi thao tác ở đây là cách áp dụng hàm lên tập dữ liệu.
Không cần viết vòng lặp tay cho mọi việc.
Ta mô tả phép biến đổi ở mức cao hơn.

### 2.3. Composition và tái sử dụng

Khi các thành phần đều là hàm,
ta có thể ghép chúng như khối LEGO logic.

Ví dụ,
pipeline xử lý dữ liệu có thể gồm:

- parse,
- clean,
- validate,
- transform,
- aggregate.

Mỗi bước nhận input,
trả output,
và ghép nối với bước sau.
Đây là mô hình rất mạnh trong data engineering,
backend services,
và UI transformations.

### 2.4. Vì sao dân công nghiệp vẫn quan tâm functional style

Ngay cả khi không dùng Haskell,
nhiều hệ thống production vẫn mượn tinh thần functional vì:

- dễ test,
- giảm side effects,
- reasoning tốt hơn,
- hợp với concurrency,
- composition linh hoạt.

Điều đó cho thấy khái niệm hàm không chỉ sống trong giáo trình.
Nó ảnh hưởng trực tiếp đến architecture decisions.

---

## Phần 3: Machine learning models như các hàm dự đoán

### 3.1. Một mô hình học máy có thể nhìn như hàm

Ở mức trừu tượng,
model học máy là hàm:

$$
f: X \to Y
$$

Trong đó:

- $X$ là không gian đầu vào,
- $Y$ là không gian đầu ra hoặc phân phối xác suất.

Ví dụ,
mô hình nhận ảnh và trả nhãn,
nhận văn bản và trả sentiment,
nhận dữ liệu khách hàng và trả xác suất rời bỏ.

### 3.2. Input-to-prediction là tư duy hàm số ở quy mô mới

Ví dụ Python nhỏ:

```python
def predict_credit_risk(features):
    score = 0.3 * features["debt_ratio"] + 0.5 * features["late_payments"]
    return score > 0.7
```

Mô hình thật phức tạp hơn nhiều,
nhưng tinh thần không đổi:
đầu vào được ánh xạ thành đầu ra.

### 3.3. Loss function, activation function, objective function

Thế giới ML đầy các hàm:

- loss functions,
- activation functions,
- kernel functions,
- scoring functions,
- objective functions.

Nói cách khác,
ngay cả khi mô hình rất hiện đại,
ngôn ngữ cơ bản để mô tả nó vẫn là ngôn ngữ của hàm.

![Mô hình học máy như hàm ánh xạ]
*Hình 2: Từ input đến prediction, machine learning có thể được hiểu như họ các hàm được học từ dữ liệu.*

---

## Phần 4: Cryptographic hash functions

### 4.1. Hash function không phải hàm ngẫu nhiên

Cryptographic hash function nhận input bất kỳ độ dài
và trả digest kích thước cố định.

Ví dụ:

```python
import hashlib

message = b"discrete mathematics"
digest = hashlib.sha256(message).hexdigest()
print(digest)
```

Đây là hàm theo nghĩa rất chính xác:
cùng input,
cùng output.

### 4.2. Nhưng nó cần nhiều tính chất đặc biệt

Một hash tốt cho bảo mật không chỉ “tính ra giá trị”.
Nó còn cần:

- khó đảo ngược,
- khó tìm collision,
- nhạy với thay đổi nhỏ ở input,
- phân bố output đều.

Đó là ví dụ đẹp cho thấy:
trong computing,
hàm không chỉ là ánh xạ.
Nó còn mang specification rất cụ thể.

### 4.3. Ứng dụng của hash

Hash functions sống trong:

- lưu mật khẩu,
- kiểm tra tính toàn vẹn,
- chữ ký số,
- blockchain,
- content addressing,
- deduplication,
- distributed systems.

Chúng là ví dụ mạnh cho việc một định nghĩa toán học đơn giản
có thể trở thành thành phần hạ tầng cực quan trọng.

---

## Phần 5: API design như đặc tả hàm

### 5.1. Một API tốt giống một hàm tốt

Khi thiết kế API,
ta đang làm điều gần với định nghĩa hàm:

- input là gì,
- output là gì,
- preconditions ra sao,
- errors khi nào,
- side effects có không.

Ví dụ:

```python
def transfer_money(sender_id, receiver_id, amount):
    ...
```

Hàm này tưởng đơn giản,
nhưng specification cần rõ:

- `amount` phải dương,
- sender phải đủ tiền,
- giao dịch phải atomic,
- lỗi phải rollback.

### 5.2. Hàm mơ hồ tạo hệ thống mơ hồ

Rất nhiều bug sản phẩm không đến từ thuật toán khó.
Chúng đến từ specification mờ:

- input nào hợp lệ,
- null được hiểu ra sao,
- timezone xử lý thế nào,
- idempotency có được đảm bảo không.

Nhìn API như hàm được đặc tả tốt
giúp kỹ sư viết code chính xác hơn,
review tốt hơn,
và tài liệu hóa rõ hơn.

### 5.3. Pure interface, messy world

Dĩ nhiên,
phần mềm thật có side effects.
Nhưng chính vì thế,
việc giữ phần interface càng “giống hàm” càng tốt
lại càng có giá trị.

Nó giảm bất ngờ,
giảm lỗi tích hợp,
và làm reasoning dễ hơn cho cả người viết lẫn người dùng API.

---

## Phần 6: Tương lai — function thinking trong hệ thống phức tạp

Khi hệ thống lớn lên,
tư duy hàm càng hữu ích:

- serverless functions,
- data pipelines,
- ML inference endpoints,
- reactive programming,
- deterministic transforms,
- verified interfaces.

Ngay cả trong distributed systems đầy side effects,
kỹ sư giỏi vẫn thường cố đẩy nhiều phần nhất có thể về dạng “hàm sạch, dễ reason”.

---

## Kết luận

Hàm số không chỉ là chủ đề của đại số phổ thông.
Trong khoa học máy tính,
nó là cách ta hiểu computation,
tổ chức chương trình,
thiết kế API,
xây mô hình học máy,
và đảm bảo tính toàn vẹn dữ liệu.

Từ Church và Turing,
đến Haskell,
SHA-256,
và prediction services,
khái niệm hàm đã trở thành một trong những chiếc xương sống bền nhất của computing.

---

## Bài tập thực hành

### Bài tập 1: Hàm đệ quy

Viết hàm đệ quy tính $$f(n) = n!$$ và giải thích tại sao đây là hàm tính toán được theo Turing.

<details>
<summary>Đáp án</summary>

```python
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n-1)
```

Hàm này có thể được tính bằng máy Turing (có thuật toán hữu hạn).

</details>

### Bài tập 2: Hàm băm

Giải thích tại sao hàm băm SHA-256 là toàn ánh nhưng không đơn ánh trên thực tế.

<details>
<summary>Đáp án</summary>

Toàn ánh vì output là 256-bit (có $$2^{256}$$ giá trị). Không đơn ánh vì domain lớn hơn nhiều (các file có kích thước bất kỳ).

</details>

### Bài tập 3: Hàm trong ML

Trong mô hình học máy, hàm dự đoán $$f: \R^n \to \R$$ thường không phải song ánh. Tại sao?

<details>
<summary>Đáp án</summary>

Vì nhiều input khác nhau có thể cho cùng output (nhiều điểm dữ liệu có cùng nhãn hoặc giá trị dự đoán).

</details>

## Tóm tắt

Hàm là trung tâm của tính toán: từ máy Turing, lambda calculus, lập trình hàm, đến mô hình học máy. Hiểu rõ các tính chất đơn ánh, toàn ánh, song ánh và phép hợp giúp chúng ta thiết kế hệ thống chính xác, dễ đảo ngược và dễ kiểm chứng. Hàm nghịch đảo là chìa khóa của undo, giải mã và khôi phục dữ liệu.
