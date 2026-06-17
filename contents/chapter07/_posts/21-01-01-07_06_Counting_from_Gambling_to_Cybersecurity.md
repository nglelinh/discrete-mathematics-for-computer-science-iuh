---
layout: post
title: "Phép đếm: Từ Cờ bạc đến An ninh mạng"
categories: chapter07
date: 2021-01-01
order: 6
required: false
lang: en
---

Có những lúc khoa học lớn bắt đầu từ câu hỏi rất đời thường.
Trong trường hợp của xác suất và phép đếm,
một trong những động lực đầu tiên lại đến từ cờ bạc.

Nhưng từ các ván bài thế kỷ XVII,
ý tưởng đếm khả năng đã đi rất xa:
nó trở thành công cụ để đánh giá độ mạnh mật khẩu,
phân tích độ phức tạp thuật toán,
ước lượng xác suất collision,
và thiết kế test suites hiệu quả cho hệ thống lớn.

Phép đếm không chỉ trả lời “có bao nhiêu cách”.
Nó trả lời “vấn đề lớn đến mức nào”.
Và trong computing,
quy mô thường là thứ quyết định mọi chuyện.

---

## Phần 1: Pascal, Fermat, và bài toán cờ bạc năm 1654

### 1.1. Một tranh chấp tưởng nhỏ nhưng mở ra lĩnh vực lớn

Năm 1654,
Pascal và Fermat trao đổi thư từ về một bài toán cờ bạc nổi tiếng:
làm sao chia tiền cược công bằng khi trò chơi phải dừng giữa chừng.

Đây không chỉ là câu đố giải trí.
Nó buộc con người phải đếm các khả năng tương lai một cách hệ thống.

Từ đây,
combinatorics và probability bắt đầu bước vào hình dạng hiện đại hơn.

### 1.2. Đếm như công cụ chống trực giác sai

Rất nhiều quyết định trực giác về rủi ro là sai.
Con người đánh giá kém khi số trường hợp tăng nhanh.

Pascal và Fermat cho thấy:
nếu muốn suy nghĩ nghiêm túc,
ta phải đếm rõ ràng.
Đó là tinh thần mà khoa học máy tính sau này thừa hưởng trọn vẹn.

![Blaise Pascal — nhà toán học Pháp](https://commons.wikimedia.org/wiki/Special:FilePath/Blaise_Pascal_Versailles.JPG?width=640)

*Hình 7.25: Blaise Pascal — từ bàn cờ bạc đến lý thuyết đếm, một câu hỏi thực tế đã khai sinh nhiều ý tưởng nền cho khoa học dữ liệu và an ninh hiện đại.*

![Pierre de Fermat — đồng sáng lập xác suất](https://commons.wikimedia.org/wiki/Special:FilePath/Pierre_de_Fermat.jpg?width=640)

*Hình 7.26: Pierre de Fermat — cùng Pascal trao đổi thư về bài toán chia tiền cược, mở ra xác suất và tổ hợp hiện đại.*

---

## Phần 2: Password security — đếm không gian khóa

### 2.1. Mật khẩu mạnh hay yếu trước hết là bài toán đếm

Giả sử mật khẩu dài 8 ký tự,
mỗi ký tự có thể là chữ thường tiếng Anh.
Số khả năng là:

$$
26^8
$$

Nếu cho phép cả chữ hoa,
số,
và ký hiệu,
không gian tăng mạnh.

Ở đây,
phép đếm không chỉ là toán.
Nó là cách định lượng chi phí brute-force attack.

### 2.2. Không gian lớn chưa chắc đủ lớn

Ví dụ,
`26^8` nghe có vẻ rất to.
Nhưng với GPU hiện đại và kỹ thuật cracking hiệu quả,
nó có thể vẫn chưa đủ trong nhiều bối cảnh.

Đây là bài học quan trọng:
số lượng khả năng phải được đặt vào ngữ cảnh thực tế về tốc độ tấn công,
rate limiting,
hashing strategy,
và chính sách xác thực.

### 2.3. Entropy và tư duy tổ hợp

Khi nói về password entropy,
ta đang dùng trực giác tổ hợp để đo mức khó đoán.
Một mật khẩu dài hơn,
đa dạng ký tự hơn,
và ít dự đoán hơn
thường tương ứng với không gian lớn hơn cần duyệt.

![Tam giác Pascal — không gian khóa](https://commons.wikimedia.org/wiki/Special:FilePath/Pascal_triangle.svg?width=640)

*Hình 7.27: Entropy mật khẩu phản ánh kích thước không gian tổ hợp cần duyệt khi brute-force.*

---

## Phần 3: Đếm phép toán và Big-O

### 3.1. Thuật toán nhanh hay chậm trước hết là đếm

Trước khi có Big-O notation,
ta thường bắt đầu bằng câu hỏi đơn giản hơn:
thuật toán này thực hiện bao nhiêu phép toán khi input kích thước `n`?

Ví dụ:

```python
for i in range(n):
    for j in range(n):
        total += 1
```

Ở đây,
số lần tăng `total` là $n^2$.

Nếu không biết đếm,
ta khó có cảm giác đúng về độ lớn của vấn đề.

### 3.2. Từ đếm chi tiết đến asymptotic thinking

Khi input rất lớn,
ta không còn quá bận tâm đến hằng số nhỏ.
Ta quan tâm hàm tăng trưởng chính.

Nhưng Big-O không rơi từ trời xuống.
Nó mọc lên từ phân tích đếm các bước cơ bản.

### 3.3. Tại sao điều này quan trọng ở công nghiệp

Sự khác biệt giữa $n \log n$ và $n^2$
có thể là:

- truy vấn chạy trong mili giây hay phút,
- sản phẩm scale được hay sập,
- chi phí cloud chấp nhận được hay bùng nổ.

Vì vậy,
phép đếm là điểm xuất phát của performance engineering.

![So sánh các lớp độ phức tạp](https://commons.wikimedia.org/wiki/Special:FilePath/Comparison_computational_complexity.svg?width=640)

*Hình 7.28: Đếm thao tác là bước đầu để hiểu vì sao một thuật toán có thể thắng hay thua hoàn toàn khi dữ liệu tăng lớn.*

![Các lớp độ phức tạp tính toán](https://commons.wikimedia.org/wiki/Special:FilePath/Complexity_classes.svg?width=640)

*Hình 7.29: Big-O phản ánh hàm tăng trưởng chính — sự khác biệt giữa $n \log n$ và $n^2$ quyết định khả năng scale của hệ thống.*

---

## Phần 4: Hash collisions và birthday paradox

### 4.1. Trực giác con người kém với va chạm

Nhiều người ngạc nhiên khi biết rằng trong nhóm chỉ 23 người,
xác suất có hai người cùng ngày sinh đã vượt 50%.
Đó là birthday paradox.

Điều này liên quan chặt đến hashing.

### 4.2. Collision là hệ quả tất yếu của phép đếm

Nếu số phần tử được băm vào hữu hạn bucket,
thì khi thêm đủ nhiều phần tử,
collision là không tránh khỏi.

Vấn đề không phải “có collision không”.
Vấn đề là:

- collision xảy ra sớm đến đâu,
- xác suất là bao nhiêu,
- hệ thống chịu được đến mức nào.

### 4.3. Ứng dụng trong bảo mật

Trong cryptographic hash,
birthday attack khai thác trực giác collision để giảm chi phí tấn công so với brute force hoàn toàn.

Điều này cho thấy:
đếm không chỉ dùng để ước lượng hiệu năng.
Nó còn là cách hiểu bề mặt tấn công của hệ thống bảo mật.

![Birthday paradox — va chạm sớm hơn trực giác](https://commons.wikimedia.org/wiki/Special:FilePath/Birthdaymatch.svg?width=640)

*Hình 7.30: Birthday paradox minh họa vì sao hash collision xảy ra sớm hơn trực giác — chỉ cần $\sqrt{N}$ phần tử trong không gian $N$ bucket.*

---

## Phần 5: Combinatorial testing và covering arrays

### 5.1. Không thể test mọi tổ hợp cấu hình

Một hệ thống thật có thể có:

- nhiều trình duyệt,
- nhiều hệ điều hành,
- nhiều loại tài khoản,
- nhiều chế độ bật/tắt tính năng,
- nhiều vùng dữ liệu.

Nếu thử mọi tổ hợp,
số lượng test cases bùng nổ rất nhanh.

### 5.2. Covering array là thỏa hiệp thông minh

Combinatorial testing dùng ý tưởng:
không cần thử toàn bộ tổ hợp bậc cao,
nhưng nên đảm bảo mọi tương tác 2 chiều,
3 chiều,
hoặc mức đã chọn
đều được bao phủ ít nhất một lần.

Đó là nơi covering arrays xuất hiện.

### 5.3. Vì sao cách này hiệu quả

Trong thực tế,
nhiều bug sinh ra từ tương tác giữa số ít yếu tố,
không phải từ mọi chiều cùng lúc.

Nhờ phép đếm và thiết kế tổ hợp,
ta có thể tạo test suite nhỏ hơn nhiều
nhưng vẫn giữ xác suất bắt lỗi tốt.

---

## Phần 6: Tương lai — đếm trong thế giới quy mô lớn

Khi hệ thống càng lớn,
phép đếm càng quan trọng:

- search spaces trong AI,
- key spaces trong security,
- state spaces trong verification,
- configuration spaces trong distributed systems,
- sample spaces trong experimentation.

Không phải lúc nào ta cũng đếm chính xác được.
Nhưng ngay cả ước lượng tổ hợp đúng
cũng đủ để cứu ta khỏi nhiều quyết định ngây thơ.

---

## Kết luận

Từ Pascal và Fermat,
đến password cracking,
Big-O,
birthday paradox,
và combinatorial testing,
phép đếm luôn xuất hiện ở nơi con người cần hiểu quy mô của khả năng.

Trong khoa học máy tính,
đó là chuyện sống còn.
Vì một hệ thống không thất bại chỉ vì nó sai logic.
Nhiều khi,
nó thất bại vì không ai hiểu không gian trường hợp của nó lớn đến mức nào.

---

## Bài tập thực hành

### Bài tập 1: Mật khẩu

Một mật khẩu gồm 8 ký tự, mỗi ký tự là chữ cái thường hoặc chữ số (36 khả năng). Hỏi có bao nhiêu mật khẩu?

<details>
<summary>Đáp án</summary>

$$36^8 \approx 1.1 \times 10^{12}$$ mật khẩu.

</details>

### Bài tập 2: Birthday paradox

Với 23 người, xác suất có ít nhất 2 người cùng sinh nhật khoảng 50%. Giải thích tại sao con số này nhỏ hơn dự đoán trực giác.

<details>
<summary>Đáp án</summary>

Sử dụng công thức xấp xỉ $$1 - e^{-n^2/2d}$$ với $$d=365$$. Với $$n=23$$ ta được ~0.5.

</details>

### Bài tập 3: Kiểm thử tổ hợp

Có 5 tính năng, mỗi tính năng có 2 lựa chọn. Cần test tất cả tổ hợp 2 tính năng. Hỏi cần bao nhiêu test case?

<details>
<summary>Đáp án</summary>

Số cặp tính năng: $$\binom{5}{2} = 10$$. Mỗi cặp 4 tổ hợp → 40 test case.

</details>

## Tóm tắt

Tổ hợp và xác suất là công cụ đếm và dự đoán rủi ro. Từ sòng bạc đến mật khẩu, kiểm thử phần mềm và phân tích thuật toán — khả năng đếm chính xác giúp chúng ta thiết kế hệ thống an toàn và hiệu quả hơn.
