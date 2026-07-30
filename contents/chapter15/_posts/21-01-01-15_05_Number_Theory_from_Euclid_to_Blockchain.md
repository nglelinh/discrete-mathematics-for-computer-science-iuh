---
layout: post
title: "Lý thuyết Số: Từ Euclid đến Blockchain"
categories: chapter15
date: 2021-01-01
order: 5
required: false
lang: en
excerpt: "Khảo sát: Euclid–Gauss, RSA và HTTPS, hashing, Reed–Solomon, zero-knowledge và blockchain, hậu lượng tử — tổng hợp Chương 15."
---

<div class="textbook-epigraph" markdown="1">

"Number theory is the purest mathematics — and now the quiet machinery of the Internet."

<span class="epigraph-attribution">— Tinh thần bài khảo sát 15.5</span>

</div>

Chương 15 đã lần lượt đưa ra chia hết, đồng dư, RSA/DH và các ứng dụng hệ thống. Mục bổ sung này **tổng hợp hành trình**: từ Euclid và Gauss đến hạ tầng HTTPS, hashing, mã sửa lỗi, zero-knowledge và blockchain — nhấn mạnh mối liên hệ khái niệm, không thay các mục kỹ thuật 15.1–15.4.

![Blockchain](/discrete-mathematics-for-computer-science-iuh/img/course/Blockchain.svg)

<p class="textbook-figure-caption" data-figure="15.8">Blockchain kết hợp hashing, chữ ký số và đồng thuận — lý thuyết số gặp hệ phân tán.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Tóm tắt** đường dây Euclid → Gauss → RSA/DH.
- **Giải thích** vai trò hash và chữ ký trong blockchain ở mức khái niệm.
- **Mô tả** zero-knowledge proof bằng một câu đúng.
- **Đặt** mối đe dọa lượng tử và PQC vào bối cảnh chương.

**Từ khóa**: Euclid, Gauss, RSA, HTTPS, blockchain, ECDSA, zero-knowledge, post-quantum.

</div>

## 1. Từ Euclid đến Gauss

Euclid (~300 TCN) để lại thuật toán GCD và chứng minh vô hạn số nguyên tố — hai kết quả vẫn nằm trong Mục 15.1. Điểm then chốt không chỉ là “có vô hạn nguyên tố”, mà là nhận ra số nguyên tố như **cấu trúc cơ bản** của số học.

Gauss (1777–1855), qua *Disquisitiones Arithmeticae* (1801), đưa **đồng dư** thành ngôn ngữ chuẩn. Hầu hết giao thức ở Mục 15.2–15.3 viết bằng đúng ngôn ngữ đó: $$a\equiv b\pmod n$$, lớp thặng dư, hàm $$\varphi$$.

## 2. RSA và an ninh Internet

RSA dựa trên **bất đối xứng tính toán**: nhân hai số nguyên tố lớn thì dễ; phân tích tích $$n=pq$$ thì khó (trên máy cổ điển). Public-key cryptography cho phép:

- công bố khóa mã hóa,
- giữ riêng khóa giải mã,
- chữ ký số và hạ tầng PKI.

HTTPS/TLS, ký phần mềm, email bảo mật đều chịu ảnh hưởng của mô hình này — dù triển khai hiện đại thường kết hợp ECDHE, AES, … Người dùng trình duyệt không cần nghĩ tới modulo; hạ tầng thì không thể thiếu.

## 3. Hashing và modulo thực dụng

Công thức

```python
index = hash(key) % table_size
```

là số học modulo ở dạng kỹ thuật phần mềm hàng ngày. Hash mật mã (SHA-256, …) phức tạp hơn nhiều, nhưng trực giác **lớp thặng dư**, wrap-around và phân bố bucket vẫn hữu ích. Máy tính làm việc với từ hữu hạn bit — nhiều phép toán “tự nhiên” đã là modulo $$2^w$$.

## 4. Mã sửa lỗi và Reed–Solomon

Truyền/lưu dữ liệu chịu nhiễu. **Reed–Solomon** và các mã liên quan dùng đại số trên **trường hữu hạn** (cấu trúc số học mở rộng) để phát hiện và sửa lỗi: CD/DVD, QR, lưu trữ phân tán, vệ tinh. Lý thuyết số / đại số hữu hạn không chỉ phục vụ RSA: còn phục vụ **độ tin cậy** dữ liệu.

## 5. Zero-knowledge và blockchain

**Zero-knowledge proof**: chứng minh một mệnh đề (hoặc “biết bí mật”) mà **không tiết lộ** bản thân bí mật. Các biến thể zk-SNARK / zk-STARK đưa ý tưởng này vào hệ phi tập trung.

**Blockchain** (ở mức chương trình): chuỗi khối gắn bằng hash; giao dịch được **ký** (ECDSA/RSA-like); đồng thuận quyết định chuỗi hợp lệ. Số nguyên tố, modulo và đường cong elliptic xuất hiện trong chữ ký; hash bảo toàn liên kết khối. Đây không phải giáo trình blockchain đầy đủ — chỉ chỉ ra chỗ lý thuyết số “neo” vào hệ.

## 6. Lượng tử và hậu lượng tử

Shor đe dọa RSA và nhiều hệ DLP/ECC cổ điển. Phản ứng không phải bỏ số học, mà **chọn bài toán nền mới** (lattice, code, hash-based, …) — xem Mục 15.4. An ninh dài hạn vẫn là bài toán toán học.

## 7. Kết luận chương

| Mốc | Ý tưởng | Chỗ trong khóa học |
|:---|:---|:---|
| Euclid | GCD, vô hạn nguyên tố | 15.1 |
| Gauss | Đồng dư | 15.2 |
| RSA / DH | Public key | 15.3 |
| Hash, LCG, CRT, ECC, PQC | Hệ thống | 15.4 |
| Blockchain / ZK | Hệ phân tán, riêng tư | 15.5 (khảo sát) |

Hành trình từ Euclid đến blockchain minh họa một quy luật của khoa học cơ bản: lý thuyết thuần hôm nay có thể trở thành hạ tầng kỹ thuật sau nhiều thế kỷ.

## Bài tập

### Bài tập 1

Tính $$\gcd(48,18)$$ bằng Euclid.

<details>
<summary>Đáp án</summary>

$$48=2\cdot 18+12$$, $$18=1\cdot 12+6$$, $$12=2\cdot 6+0$$ → $$\gcd=6$$.

</details>

### Bài tập 2

$$p=5$$, $$q=11$$, $$e=3$$. Tính $$n$$ và một $$d$$ hợp lệ.

<details>
<summary>Đáp án</summary>

$$n=55$$, $$\varphi=40$$, $$d=27$$ vì $$3\cdot 27=81\equiv 1\pmod{40}$$.

</details>

### Bài tập 3

Nêu một câu về vai trò modulo / số nguyên tố trong chữ ký số trên blockchain.

<details>
<summary>Đáp án</summary>

Chữ ký (ECDSA/RSA-like) dùng lũy thừa hoặc phép toán nhóm trên trường hữu hạn / đường cong; nghịch đảo modulo và độ khó DLP/factoring (tùy hệ) bảo vệ khóa riêng. Hash liên kết khối và thường băm thông điệp trước khi ký.

</details>

## Tóm tắt

Số học — từ chia hết và đồng dư đến RSA, hash, mã sửa lỗi và chữ ký — là nền im lặng của bảo mật và nhiều hệ phân tán. Chương 15 kết thúc bằng bức tranh tổng hợp; Chương 16 mở **cây** như cấu trúc dữ liệu–toán rời rạc tiếp theo.
