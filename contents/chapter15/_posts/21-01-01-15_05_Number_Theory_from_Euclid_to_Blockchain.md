---
layout: post
title: "Lý thuyết Số: Từ Euclid đến Blockchain"
categories: chapter15
date: 2021-01-01
order: 5
required: false
lang: en
excerpt: "Bài khảo sát tổng hợp Chương 15: từ Euclid và Gauss đến RSA, HTTPS, hàm băm, mã Reed–Solomon, chứng minh không tiết lộ thông tin (zero-knowledge), blockchain và hậu lượng tử."
---

<div class="textbook-epigraph" markdown="1">

"Number theory is the purest mathematics — and now the quiet machinery of the Internet."

<span class="epigraph-attribution">— Tinh thần bài khảo sát 15.5</span>

</div>

Các bài trước trong Chương 15 đã lần lượt trình bày tính chia hết, đồng dư, RSA/Diffie–Hellman và các ứng dụng hệ thống. Bài bổ sung này **tổng hợp tiến trình phát triển** từ Euclid và Gauss đến hạ tầng HTTPS, hàm băm, mã sửa lỗi, chứng minh không tiết lộ thông tin (*zero-knowledge*) và blockchain, nhằm làm rõ mối liên hệ giữa các khái niệm thay vì lặp lại chi tiết kỹ thuật của các mục 15.1–15.4.

![Blockchain](/discrete-mathematics-for-computer-science-iuh/img/course/Blockchain.svg)

<p class="textbook-figure-caption" data-figure="15.8">Blockchain kết hợp hàm băm, chữ ký số và cơ chế đồng thuận — điểm giao nhau giữa lý thuyết số và hệ phân tán.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Tóm tắt** mạch phát triển từ Euclid đến Gauss và tới RSA/Diffie–Hellman.
- **Giải thích** vai trò của hàm băm và chữ ký số trong blockchain ở mức khái niệm.
- **Mô tả** chính xác khái niệm *zero-knowledge proof* trong một câu.
- **Đặt** thách thức máy tính lượng tử và mật mã hậu lượng tử (PQC) vào bức tranh chung của chương.

**Từ khóa**: Euclid, Gauss, RSA, HTTPS, blockchain, ECDSA, zero-knowledge, post-quantum.

</div>

## Từ Euclid đến Gauss

Euclid (~300 TCN) để lại thuật toán tìm ước chung lớn nhất và chứng minh có vô hạn số nguyên tố — hai kết quả cốt lõi ở Mục 15.1. Ý nghĩa sâu xa không chỉ nằm ở việc có vô hạn số nguyên tố, mà ở chỗ xác lập số nguyên tố là **đơn vị cấu tạo cơ bản** của số học.

Gauss (1777–1855), thông qua tác phẩm *Disquisitiones Arithmeticae* (1801), đã đưa **quan hệ đồng dư** trở thành ngôn ngữ chuẩn mực của lý thuyết số. Hầu hết các giao thức ở Mục 15.2–15.3 đều được diễn đạt bằng chính ngôn ngữ này: $$a\equiv b\pmod n$$, các lớp thặng dư và hàm phi Euler $$\varphi$$.

## RSA và an ninh Internet

RSA khai thác sự **bất đối xứng về độ khó tính toán**: nhân hai số nguyên tố lớn rất dễ, nhưng phân tích tích $$n=pq$$ thành hai thừa số ban đầu lại rất khó trên máy tính cổ điển. Mật mã khóa công khai từ đó cho phép:

- công bố khóa mã hóa rộng rãi,
- giữ riêng khóa giải mã,
- xây dựng chữ ký số và hạ tầng khóa công khai (PKI).

Giao thức HTTPS/TLS, ký số phần mềm và bảo mật email đều dựa trên mô hình này, dù các triển khai hiện đại thường kết hợp thêm ECDHE, AES và nhiều thành phần khác. Người dùng cuối không cần trực tiếp thấy các phép tính modulo, nhưng hạ tầng mạng không thể vận hành an toàn nếu thiếu chúng.

## Hàm băm và phép modulo trong thực hành

Biểu thức quen thuộc trong lập trình:

```python
index = hash(key) % table_size
```

là ứng dụng trực tiếp của số học modulo trong kỹ thuật phần mềm hằng ngày. Dù hàm băm mật mã (như SHA-256) phức tạp hơn nhiều, trực giác về **lớp thặng dư**, hiện tượng quay vòng (*wrap-around*) và phân bố bucket vẫn rất hữu ích. Do máy tính biểu diễn số bằng các từ có độ dài bit hữu hạn, nhiều phép toán số học phần cứng vốn đã hoạt động theo modulo $$2^w$$.

## Mã sửa lỗi và Reed–Solomon

Khi truyền tải hoặc lưu trữ, dữ liệu luôn có nguy cơ gặp nhiễu. **Mã Reed–Solomon** và các họ mã sửa lỗi liên quan sử dụng đại số trên **trường hữu hạn** (một cấu trúc số học mở rộng) để phát hiện và sửa lỗi trên đĩa CD/DVD, mã QR, hệ thống lưu trữ phân tán và thông tin vệ tinh. Như vậy, lý thuyết số và đại số hữu hạn không chỉ phục vụ bảo mật như RSA mà còn đảm bảo **độ tin cậy** của dữ liệu.

## Zero-knowledge và blockchain

**Chứng minh không tiết lộ thông tin (*zero-knowledge proof*)** cho phép một bên chứng minh rằng một mệnh đề là đúng (hoặc mình nắm giữ một bí mật) mà **không tiết lộ** bất kỳ thông tin nào về bản thân bí mật đó. Các biến thể như zk-SNARK và zk-STARK đã đưa ý tưởng này vào nhiều hệ thống phi tập trung.

Ở mức tổng quan, **blockchain** là chuỗi các khối được liên kết bằng hàm băm; các giao dịch được **ký số** (theo cơ chế ECDSA hoặc tương tự RSA), còn cơ chế đồng thuận quyết định chuỗi hợp lệ. Số nguyên tố, phép toán modulo và đường cong elliptic xuất hiện trong chữ ký số, trong khi hàm băm đảm bảo tính toàn vẹn của liên kết giữa các khối. Mục này không thay thế một giáo trình chuyên sâu về blockchain, mà chỉ chỉ rõ những điểm lý thuyết số gắn trực tiếp vào kiến trúc hệ thống.

## Lượng tử và hậu lượng tử

Thuật toán Shor đe dọa RSA cũng như nhiều hệ dựa trên DLP và ECC cổ điển. Hướng giải quyết không phải là từ bỏ lý thuyết số, mà là **chuyển sang những bài toán nền tảng mới** (mạng tinh thể, mã sửa lỗi, hàm băm, …) như đã nêu ở Mục 15.4. Bảo mật dài hạn về bản chất vẫn là một bài toán toán học.

## Kết luận chương

| Mốc | Ý tưởng chính | Vị trí trong khóa học |
|:---|:---|:---|
| Euclid | GCD, vô hạn số nguyên tố | 15.1 |
| Gauss | Quan hệ đồng dư | 15.2 |
| RSA / DH | Mật mã khóa công khai | 15.3 |
| Hash, LCG, CRT, ECC, PQC | Ứng dụng hệ thống | 15.4 |
| Blockchain / ZK | Hệ phân tán và quyền riêng tư | 15.5 (khảo sát) |

Tiến trình từ Euclid đến blockchain minh họa một quy luật phổ biến của khoa học cơ bản: những kết quả toán học thuần túy có thể trở thành nền tảng hạ tầng kỹ thuật sau nhiều thế kỷ.

## Bài tập

### Bài tập 1

Tính $$\gcd(48,18)$$ bằng thuật toán Euclid.

<details>
<summary>Đáp án</summary>

$$48=2\cdot 18+12$$, $$18=1\cdot 12+6$$, $$12=2\cdot 6+0$$, suy ra $$\gcd(48,18)=6$$.

</details>

### Bài tập 2

Cho $$p=5$$, $$q=11$$, $$e=3$$. Tính $$n$$ và một giá trị $$d$$ hợp lệ.

<details>
<summary>Đáp án</summary>

Ta có $$n=55$$, $$\varphi(n)=40$$ và $$d=27$$ vì $$3\cdot 27=81\equiv 1\pmod{40}$$.

</details>

### Bài tập 3

Nêu ngắn gọn trong một câu vai trò của phép modulo hoặc số nguyên tố trong chữ ký số trên blockchain.

<details>
<summary>Đáp án</summary>

Chữ ký số (ECDSA hoặc tương tự RSA) sử dụng phép lũy thừa hoặc phép toán nhóm trên trường hữu hạn/đường cong elliptic, trong đó nghịch đảo modulo cùng độ khó của DLP hoặc phân tích thừa số giúp bảo vệ khóa riêng, còn hàm băm dùng để liên kết các khối và băm thông điệp trước khi ký.

</details>

## Tóm tắt

Lý thuyết số — từ tính chia hết và đồng dư đến RSA, hàm băm, mã sửa lỗi và chữ ký số — đóng vai trò nền tảng cho bảo mật và nhiều hệ phân tán hiện đại. Chương 15 khép lại bằng cái nhìn tổng hợp này; Chương 16 sẽ tiếp tục với **cây**, một cấu trúc dữ liệu và toán rời rạc quan trọng khác.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=cOwyHTiW4KE">EUCLIDEAN ALGORITHM - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Ôn lại thuật toán Euclid, điểm khởi đầu của tiến trình lịch sử trong bài.
- <a href="https://www.youtube.com/watch?v=JD72Ry60eP4">Prime Numbers &amp; RSA Encryption Algorithm - Computerphile</a> — Computerphile, tiếng Anh. Hệ mật RSA, chặng phát triển của mật mã khóa công khai trước hạ tầng mạng hiện đại.
- <a href="https://www.youtube.com/watch?v=bBC-nXj3Ng4">But how does bitcoin actually work?</a> — 3Blue1Brown, tiếng Anh. Giải thích cách Bitcoin sử dụng hàm băm và chữ ký số, tương ứng với phần blockchain ở cuối bài.
