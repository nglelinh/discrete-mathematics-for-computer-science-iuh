---
layout: post
title: "Hàm sinh trong Phép đếm và Mã hóa"
categories: chapter11
date: 2021-01-01
order: 5
required: false
lang: en
---

Trong nhiều phần của toán rời rạc,
ta đếm bằng cách liệt kê,
dùng công thức,
hoặc dựng recurrence.
Nhưng đến một lúc,
ta cần công cụ mạnh hơn:
một cách gói cả dãy số vô hạn vào một biểu thức duy nhất.

Đó là lúc generating functions xuất hiện.
Nghe trừu tượng,
nhưng chúng từng được Euler dùng đầy sức mạnh,
và ngày nay vẫn liên hệ tới combinatorics,
probability,
algorithm analysis,
và coding theory.

---

![Euler và hàm sinh](https://commons.wikimedia.org/wiki/Special:FilePath/Leonhard_Euler.jpg?width=640)

*Hình 11.21: Euler biến các dãy số thành đối tượng đại số, mở ra một trong những công cụ đẹp nhất của tổ hợp học.*

![Hàm sinh xác suất (PGF)](https://commons.wikimedia.org/wiki/Special:FilePath/Generating_function.svg?width=640)

*Hình 11.22: Hàm sinh xác suất biến phân phối rời rạc thành đối tượng có thể vi phân, nhân và phân tích.*

![Đếm tổ hợp bằng hệ số](https://commons.wikimedia.org/wiki/Special:FilePath/Power_series.svg?width=640)

*Hình 11.23: Nhân các chuỗi hình thức — hệ số của $x^n$ cho số cách đạt tổng $n$.*

![Giải truy hồi bằng hàm sinh](https://commons.wikimedia.org/wiki/Special:FilePath/Fibonacci_spiral.svg?width=640)

*Hình 11.24: Truy hồi khó trở nên phương trình đại số sau khi chuyển sang miền hàm sinh.*

![Weight enumerator trong mã hóa](https://commons.wikimedia.org/wiki/Special:FilePath/Decision_tree.svg?width=640)

*Hình 11.25: Đa thức đếm codeword theo trọng số Hamming — họ hàng gần của hàm sinh trong coding theory.*

## Phần 1: Euler và cú nhảy năm 1748

### 1.1. Euler nhìn dãy số như đối tượng đại số

Leonhard Euler là bậc thầy của việc nhìn ra cấu trúc ẩn trong những thứ tưởng rời rạc.
Thay vì chỉ xem dãy số là danh sách,
ông xem chúng như hệ số của một power series.

Ví dụ,
dãy $a_0, a_1, a_2, ...$
có thể được đóng gói thành:

$$
A(x)=a_0+a_1x+a_2x^2+\cdots
$$

Ý tưởng đó mở cánh cửa cực lớn.

### 1.2. Vì sao cách nhìn này mạnh

Khi biến bài toán đếm thành bài toán thao tác biểu thức,
ta có thể dùng đại số,
giải tích hình thức,
và biến đổi chuỗi để rút kết quả đếm.

Đây là kiểu “đổi ngôn ngữ để bài toán dễ hơn”
mà khoa học máy tính rất quen thuộc.

---

## Phần 2: Đếm tổ hợp bằng hàm sinh

### 2.1. Hệ số là câu trả lời đếm

Giả sử ta muốn biết có bao nhiêu cách tạo tổng nào đó từ các lựa chọn nhỏ.
Generating function cho phép mã hóa mỗi lựa chọn thành một thừa số,
rồi lấy hệ số thích hợp.

Ví dụ,
nếu mỗi giá trị có thể chọn 0, 1, 2, ... lần,
ta gặp dạng:

$$
1+x+x^2+x^3+\cdots = \frac{1}{1-x}
$$

Khi nhân nhiều chuỗi như vậy,
hệ số của $x^n$ nói số cách đạt tổng $n$.

### 2.2. Partition problems

Một ví dụ cổ điển:
đếm số cách phân tích một số nguyên thành tổng các số dương.

Đây là kiểu bài toán mà liệt kê tay rất nhanh trở nên bất lực,
nhưng generating functions lại đặc biệt tự nhiên.

### 2.3. Vì sao dân CS nên quan tâm

Không phải ai cũng cần giải partition identities mỗi ngày.
Nhưng generating functions rèn một kỹ năng rất quý:
thấy cách mã hóa cấu trúc rời rạc vào biểu diễn đại số để thao tác mạnh hơn.

---

## Phần 3: Probability generating functions

### 3.1. Khi xác suất cũng được đóng gói bằng chuỗi

Nếu biến ngẫu nhiên rời rạc $X$ nhận các giá trị không âm,
ta có probability generating function:

$$
G_X(s)=\sum_{k\ge0} P(X=k)s^k
$$

Nhờ đó,
phân phối xác suất được gói lại thành một object đại số thuận tiện.

### 3.2. Tại sao cách này hữu ích

PGF giúp:

- tính kỳ vọng,
- xử lý tổng các biến độc lập,
- nghiên cứu branching processes,
- suy ra các tính chất phân phối.

Ở đây,
ta lại thấy pattern quen thuộc:
một cấu trúc phức tạp được biến thành hàm để thao tác dễ hơn.

### 3.3. Cầu nối sang queueing và stochastic systems

Trong các hệ thống như hàng đợi,
traffic processes,
và mô hình ngẫu nhiên theo thời gian,
generating functions từng là công cụ chuẩn để phân tích phân phối trạng thái.

---

## Phần 4: Giải recurrence khó bằng generating functions

### 4.1. Khi recurrence không còn dễ đoán nghiệm

Một số recurrence đơn giản có thể giải trực tiếp.
Nhưng nhiều recurrence phức tạp hơn
trở nên dễ xử lý nếu ta nhân cả hai vế với $x^n$,
cộng theo `n`,
và biến toàn bộ bài toán thành quan hệ giữa các generating functions.

### 4.2. Ý tưởng chuyển miền biểu diễn

Đây là tư duy rất “computer science”:
đổi representation để thao tác tốt hơn.

Giống như FFT đổi miền thời gian sang miền tần số,
generating functions đổi bài toán dãy số sang bài toán hàm chuỗi.

### 4.3. Ứng dụng trong algorithm analysis

Khi phân tích các thuật toán đếm,
process ngẫu nhiên,
hoặc cấu trúc tổ hợp phức,
generating functions thường cho biểu thức gọn và insight sâu hơn so với tính tay từng bước.

---

## Phần 5: Coding theory và đếm codewords

### 5.1. Mã hóa không chỉ là biến bit thành bit

Coding theory cần hiểu:

- có bao nhiêu codewords,
- phân bố trọng số ra sao,
- khoảng cách Hamming thế nào,
- khả năng phát hiện/sửa lỗi mạnh đến đâu.

### 5.2. Weight enumerator như một loại generating function

Một mã có thể gắn với đa thức đếm số codewords theo trọng số.
Đây là họ hàng rất gần của generating functions.

Nhờ các đa thức như vậy,
ta phân tích được cấu trúc của mã,
khả năng chống lỗi,
và đôi khi suy ra các đẳng thức sâu.

### 5.3. Từ lý thuyết đến truyền thông và lưu trữ

Error-correcting codes đi vào:

- đĩa quang,
- truyền vệ tinh,
- QR codes,
- bộ nhớ,
- truyền dữ liệu qua kênh nhiễu.

Generating functions ở đây giúp đếm và hiểu không gian cấu trúc của mã,
không chỉ giải bài toán đẹp trên giấy.

---

## Phần 6: Tương lai — symbolic methods trong computing

Dù ngày nay có nhiều công cụ số mạnh,
symbolic methods như generating functions
vẫn hữu ích trong:

- analytic combinatorics,
- performance models,
- probabilistic analysis,
- code structure studies,
- algorithmic counting.

Chúng nhắc ta rằng:
đôi khi insight lớn đến từ việc chọn biểu diễn đúng,
không chỉ từ tăng sức tính toán.

---

## Kết luận

Từ Euler,
đến partition problems,
probability generating functions,
recurrence solving,
và coding theory,
hàm sinh cho thấy một ý tưởng rất đẹp:
hãy gói cấu trúc rời rạc vào dạng hàm,
và để đại số làm phần việc nặng.

Đó là bài học vượt ngoài riêng chương 11.
Đó là một phong cách tư duy sẽ còn gặp lại nhiều lần trong khoa học máy tính.

---

## Bài tập thực hành

### Bài tập 1: Viết hàm sinh

Viết hàm sinh cho số cách chọn k phần tử từ n loại (không phân biệt thứ tự).

<details>
<summary>Đáp án</summary>

$$\frac{1}{(1-x)^n}$$ (hàm sinh cho tổ hợp với lặp lại).

</details>

### Bài tập 2: Giải recurrence bằng hàm sinh

Dùng hàm sinh giải $$a_n = a_{n-1} + a_{n-2}$$, $$a_0=0$$, $$a_1=1$$.

<details>
<summary>Đáp án</summary>

Hàm sinh: $$G(x) = \frac{x}{1-x-x^2}$$.  
Hệ số của $$x^n$$ chính là $$F_n$$ (Fibonacci).

</details>

### Bài tập 3: Ứng dụng mã hóa

Giải thích vai trò của hàm sinh trong lý thuyết mã (weight enumerator).

<details>
<summary>Đáp án</summary>

Weight enumerator polynomial mô tả phân bố trọng số của mã, giúp đánh giá khả năng phát hiện/sửa lỗi.

</details>

## Tóm tắt

Hàm sinh là công cụ mạnh mẽ để giải bài đếm và recurrence. Từ tổ hợp, phân hoạch, đến lý thuyết mã và xác suất — hàm sinh biến bài toán phức tạp thành bài toán đại số. Hiểu cách xây dựng và khai thác hàm sinh giúp chúng ta giải quyết nhiều bài toán tổ hợp một cách thanh lịch và có hệ thống.
