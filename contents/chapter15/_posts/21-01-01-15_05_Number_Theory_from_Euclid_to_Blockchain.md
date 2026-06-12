---
layout: post
title: "Lý thuyết Số: Từ Euclid đến Blockchain"
categories: chapter15
date: 2021-01-01
order: 5
required: false
lang: en
---

# Lý thuyết Số: Từ Euclid đến Blockchain

Nếu có một chương trong toán rời rạc khiến nhiều sinh viên bất ngờ nhất về sức ảnh hưởng thực tế,
đó thường là number theory.
Rất nhiều khái niệm nghe có vẻ cổ điển và xa đời sống — chia hết,
số nguyên tố,
đồng dư,
thuật toán Euclid — lại là hạ tầng của Internet security hiện đại.

Từ Euclid,
đến Gauss,
đến RSA,
Reed–Solomon,
hashing,
và zero-knowledge proofs,
number theory cho thấy một bài học lớn:
toán học thuần túy có thể chờ hàng thế kỷ trước khi bùng nổ thành công nghệ thiết yếu.

---

## Phần 1: Từ Euclid đến Gauss

### 1.1. Euclid và số nguyên tố

Euclid không biết Internet,
nhưng ông cho nhân loại một proof kinh điển về việc có vô hạn số nguyên tố.

Điểm quan trọng không chỉ là kết quả.
Điểm quan trọng là cảm giác rằng số nguyên tố là cấu trúc cơ bản,
sâu,
và khó lường.

### 1.2. Gauss và arithmetic bậc cao hơn

Carl Friedrich Gauss đưa number theory lên trình độ mới.
Các ý tưởng về modular arithmetic,
congruences,
và cấu trúc số học trở nên có hệ thống và mạnh mẽ hơn nhiều.

Ngày nay,
rất nhiều giao thức bảo mật vẫn đứng trên nền ngôn ngữ mà Gauss giúp hoàn thiện.

![Euclid và Gauss]
*Hình 1: Từ Euclid đến Gauss, number theory xây nền trí tuệ cho những công nghệ bảo mật mà thời của họ không thể hình dung.*

---

## Phần 2: RSA và an ninh của Internet

### 2.1. Ý tưởng cốt lõi của RSA

RSA dựa trên thực tế rằng:
nhân hai số nguyên tố lớn thì dễ,
nhưng phân tích tích của chúng thành thừa số lại khó hơn rất nhiều.

Đó là ví dụ hoàn hảo của asymmetry trong computation.

### 2.2. Public key cryptography thay đổi thế giới

Trước public key,
chia sẻ khóa bí mật là vấn đề khó.
RSA cho phép:

- công khai khóa mã hóa,
- giữ riêng khóa giải mã,
- xây hệ chữ ký số,
- xác thực kết nối an toàn.

HTTPS,
PKI,
email security,
software signing
đều chịu ảnh hưởng của hướng tư duy này.

### 2.3. Một ví dụ đẹp của toán thuần chuyển thành hạ tầng

Rất ít người dùng web nghĩ về modulo và số nguyên tố khi mở trình duyệt.
Nhưng chính những ý tưởng đó đang âm thầm bảo vệ kết nối của họ.

---

## Phần 3: Hashing và modular arithmetic

### 3.1. Modular arithmetic ở khắp nơi

Khi tính hash,
phân bố bucket,
xoay vòng chỉ số,
hoặc làm checksum,
ta thường gặp arithmetic modulo.

Ví dụ đơn giản:

```python
index = hash(key) % table_size
```

Đây là modular arithmetic ở dạng thực dụng nhất.

### 3.2. Hash functions không chỉ là chia lấy dư

Dĩ nhiên,
hash hiện đại phức tạp hơn rất nhiều.
Nhưng trực giác số học mô-đun vẫn hữu ích để hiểu:

- phân bố residue,
- bucket mapping,
- wrap-around,
- cyclic structures.

### 3.3. Tại sao số học mô-đun hợp với máy tính

Máy tính hữu hạn bit,
nên nhiều phép toán tự nhiên diễn ra trong không gian mô-đun nào đó.
Điều này làm number theory càng gần hardware hơn ta tưởng.

![Modular arithmetic and hashing]
*Hình 2: Đồng dư và modulo không chỉ là ký hiệu; chúng sống trong hashing, indexing, và nhiều lớp hạ tầng số học của phần mềm.*

---

## Phần 4: Error-correcting codes và Reed–Solomon

### 4.1. Dữ liệu truyền đi hiếm khi hoàn hảo

Khi truyền thông qua kênh nhiễu,
hoặc lưu dữ liệu lâu dài,
ta cần cách phát hiện và sửa lỗi.

### 4.2. Reed–Solomon là chiến thắng của đại số trên thực tế

Reed–Solomon codes dùng cấu trúc đại số trên trường hữu hạn.
Chúng cực kỳ hữu ích trong:

- CD/DVD,
- QR codes,
- storage systems,
- satellite communication,
- data recovery.

### 4.3. Điều thú vị với sinh viên CS

Nhiều người học number theory tưởng chương này chỉ xoay quanh primes và RSA.
Nhưng coding theory cho thấy đại số số học còn mở ra cả thế giới reliability engineering.

---

## Phần 5: Zero-knowledge proofs và blockchain

### 5.1. Chứng minh mà không lộ bí mật

Zero-knowledge proof là một trong những ý tưởng đẹp nhất của modern cryptography:
chứng minh bạn biết một bí mật hoặc một mệnh đề đúng,
nhưng không tiết lộ bản thân bí mật đó.

### 5.2. Vì sao blockchain quan tâm

Trong blockchain và systems phi tập trung,
người ta quan tâm đến:

- tính đúng đắn có thể kiểm tra công khai,
- quyền riêng tư,
- khả năng xác minh không cần tin cậy tuyệt đối.

Các biến thể như zk-SNARKs,
zk-STARKs
đang đẩy number theory vào một vùng ứng dụng cực hiện đại.

### 5.3. Đây không còn là lý thuyết xa xôi

Number theory ngày nay không chỉ bảo vệ web.
Nó còn tham gia tái thiết kế cách niềm tin kỹ thuật được xây dựng trong môi trường phi tập trung.

---

## Phần 6: Tương lai — lượng tử, hậu lượng tử, và số học mới

Quantum computing đe dọa một số hệ mật mã cổ điển như RSA.
Điều đó không làm number theory yếu đi.
Ngược lại,
nó thúc đẩy sự tìm kiếm các nền tảng toán học mới cho post-quantum cryptography.

Tương lai của an ninh số
vẫn sẽ là tương lai rất toán học.

---

## Kết luận

Từ Euclid,
Gauss,
đến RSA,
hashing,
Reed–Solomon,
và zero-knowledge proofs,
number theory cho thấy một hành trình hiếm có:
đi từ vẻ đẹp thuần túy sang giá trị công nghiệp khổng lồ.

Nó là một lời nhắc đẹp cho sinh viên khoa học máy tính:
đừng quá vội hỏi “học cái này để làm gì”.
Đôi khi câu trả lời là:
để xây cả hạ tầng của thế giới số sau vài trăm năm.

---

## Bài tập thực hành

### Bài tập 1: Ước số chung lớn nhất

Tính $$\gcd(48, 18)$$ bằng thuật toán Euclid.

<details>
<summary>Đáp án</summary>

48 = 2×18 + 12  
18 = 1×12 + 6  
12 = 2×6 + 0 → $$\gcd = 6$$

</details>

### Bài tập 2: Mã hóa RSA đơn giản

Cho $$p=5$$, $$q=11$$, $$e=3$$. Tính $$n$$ và $$d$$.

<details>
<summary>Đáp án</summary>

$$n = 55$$, $$\phi(n)=40$$, $$d=27$$ (vì $$3×27 \equiv 1 \pmod{40}$$).

</details>

### Bài tập 3: Ứng dụng Blockchain

Giải thích vai trò của số nguyên tố và modulo trong chữ ký số.

<details>
<summary>Đáp án</summary>

Chữ ký số dùng nghịch đảo modulo (RSA/ECDSA). Khó phân tích số nguyên tố lớn là nền tảng an toàn của blockchain.

</details>

## Tóm tắt

Số học là nền tảng của bảo mật hiện đại. Từ Euclid, Fermat, Euler đến RSA, elliptic curve và blockchain — các định lý và thuật toán số học cho phép chúng ta mã hóa, xác thực và xây dựng hệ thống tin cậy mà không cần tin tưởng lẫn nhau. Hiểu sâu số học giúp bạn nắm bắt được bí mật đằng sau mọi hệ thống bảo mật và tiền điện tử ngày nay.
