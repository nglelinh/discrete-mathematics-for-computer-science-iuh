---
layout: post
title: "Ứng dụng của Lý thuyết Số trong Khoa học Máy tính"
categories: chapter15
date: 2021-01-01
order: 4
required: false
lang: en
excerpt: "Hàm băm mật mã, PRNG/LCG, CRT tăng tốc RSA, ECC và mật mã hậu lượng tử — các ứng dụng thực tế của số học modulo và số nguyên tố."
---

> **Câu chuyện mở đầu:** Lý thuyết số không chỉ sống trong phòng mật mã! Ngay khi bạn quét mã vạch một cuốn sách ở thư viện (ISBN), gọi `random()` trong Python, hay lưu mật khẩu người dùng bằng hàm băm SHA-256, bạn đang trực tiếp hưởng lợi từ những đẳng thức đồng dư tinh gọn của số học modulo!

<div class="textbook-epigraph" markdown="1">

"Don't invent your own crypto — use reviewed standards."

<span class="epigraph-attribution">— Nguyên tắc kỹ nghệ bảo mật</span>

</div>

Các bài trước đã giới thiệu những công cụ số học cơ bản cùng mô hình RSA và Diffie–Hellman. Bài học này liên kết các kiến thức đó với những **ứng dụng hệ thống** quen thuộc: hàm băm mật mã, bộ sinh số giả ngẫu nhiên, tăng tốc RSA bằng CRT, mật mã đường cong elliptic (ECC) và định hướng **mật mã hậu lượng tử** ở mức khái niệm dành cho sinh viên đại học.

![Hashing modulo](/discrete-mathematics-for-computer-science-iuh/img/course/Hash_table_simple_999.svg)

<p class="textbook-figure-caption" data-figure="15.7">Phân bố bucket bằng phép chia modulo — trực giác số học cho bảng băm (khác với hàm băm mật mã).</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Nêu** các yêu cầu cốt lõi của hàm băm mật mã (kháng tiền ảnh, kháng va chạm, hiệu ứng thác lũ).
- **Mô tả** bộ sinh LCG và giải thích hạn chế của nó trong bảo mật.
- **Giải thích** cách CRT giúp tăng tốc phép lũy thừa modulo trong RSA.
- **So sánh** kích thước khóa giữa RSA và ECC ở mức bảng đối chiếu.
- **Nhận biết** mối đe dọa từ thuật toán Shor và hướng tiếp cận mật mã hậu lượng tử.

**Từ khóa**: hash, SHA-256, PRNG, LCG, CRT-RSA, ECC, post-quantum.

</div>

## Kiến thức cần nhớ: Ba ứng dụng Lý thuyết Số phổ biến nhất trong Kỹ thuật Phần mềm

### 1. Hàm băm (Hashing) & Hàm băm Mật mã (SHA-256)
- **Băm cấu trúc dữ liệu:** $$h(k) = k \bmod m$$ (chọn $$m$$ là số nguyên tố để tránh đụng độ do ước chung với mẫu dữ liệu!).
- **Băm mật mã:** Phải thỏa mãn 3 tính chất sắt đá: **một chiều** (không đảo ngược được mật khẩu từ mã băm), **kháng tiền ảnh thứ hai**, và **kháng đụng độ** (hiệu ứng tuyết lở: đổi 1 bit đầu vào làm đảo lộn ~50% bit đầu ra!).

### 2. Bộ sinh Số giả ngẫu nhiên Đồng dư Tuyến tính (LCG)
- **Bản chất:** Công thức truy hồi siêu nhẹ $$x_{n+1} = (a x_n + c) \bmod m$$. Theo **Định lý Hull–Dobell**, LCG đạt chu kỳ đầy đủ tối đa $$m$$ khi và chỉ khi: (1) $$\gcd(c, m) = 1$$, (2) $$a - 1$$ chia hết cho mọi ước nguyên tố của $$m$$, và (3) nếu $$4 \mid m$$ thì $$4 \mid (a-1)$$. *(Lưu ý: LCG tốt cho mô phỏng đơn giản nhưng TUYỆT ĐỐI không dùng cho mật mã vì dễ đoán ngược!)*

### 3. Chữ số Kiểm soát (Check Digits: ISBN, EAN, Thẻ tín dụng Luhn)
- **Bản chất:** Gắn thêm một chữ số kiểm tra thỏa mãn phương trình đồng dư có trọng số (ví dụ modulo 11 cho ISBN-10, modulo 10 cho ISBN-13/Luhn) để phát hiện **100% lỗi gõ sai 1 chữ số** và **lỗi đảo chỗ hai chữ số kề nhau**!

## Ví dụ tính tay làm từng bước

### Ví dụ 1: Kiểm tra bộ sinh LCG $$x_{n+1} = (5x_n + 3) \bmod 8$$ với hạt giống $$x_0 = 1$$
Kiểm tra điều kiện Hull–Dobell ($$m = 8, a = 5, c = 3$$): $$\gcd(3, 8) = 1$$ ✓; $$a - 1 = 4$$ chia hết cho ước nguyên tố $$2$$ và chia hết cho $$4$$ ✓ $$\implies$$ **chắc chắn đạt chu kỳ đủ 8**!
Chạy tay từng bước từ $$x_0 = 1$$:
$$
1 \to 0 \to 3 \to 2 \to 5 \to 4 \to 7 \to 6 \to 1 \dots
$$
Đúng cả 8 giá trị $$\{0,1,2,3,4,5,6,7\}$$ xuất hiện trước khi lặp lại!

### Ví dụ 2: Phát hiện lỗi gõ nhầm bằng mã kiểm tra ISBN-10 (modulo 11)
Quy tắc ISBN-10 hợp lệ: $$\sum_{i=1}^{10} i \cdot d_i \equiv 0 \pmod{11}$$.
Giả sử một mã hợp lệ bị **đảo chỗ hai chữ số kề nhau** $$d_k$$ và $$d_{k+1}$$ ($$d_k \neq d_{k+1}$$). Độ lệch tổng có trọng số thay đổi đúng một lượng:
$$
\Delta = \bigl(k\,d_{k+1} + (k+1)d_k\bigr) - \bigl(k\,d_k + (k+1)d_{k+1}\bigr) = d_k - d_{k+1}.
$$
Vì $$d_k \neq d_{k+1}$$ nằm trong $$\{0,\dots,10\}$$ nên $$1 \le \lvert d_k - d_{k+1}\rvert \le 10$$ — **không bao giờ chia hết cho số nguyên tố 11**! Do đó ISBN-10 phát hiện 100% mọi lỗi đảo chỗ hai chữ số liền kề!

### Giải thích: 4 nguyên tắc chọn công cụ Lý thuyết Số trong Phần mềm
#### Bước 1: Dùng số nguyên tố làm kích thước bảng băm và modulo kiểm tra
Số nguyên tố triệt tiêu mọi ước chung bất ngờ (như lý do ISBN-10 chọn $$p = 11$$ thay vì $$10$$!).

#### Bước 2: Phân biệt rạch ròi PRNG thông thường với CSPRNG mật mã
LCG hay Mersenne Twister tuyệt vời cho mô phỏng Monte Carlo và game, nhưng sinh khóa/token bảo mật bắt buộc phải dùng CSPRNG (như `secrets` trong Python hoặc `/dev/urandom`).

#### Bước 3: Hiểu Nghịch lý Sinh nhật (Birthday Paradox) khi đánh giá độ dài mã băm
Một hàm băm $$b$$-bit chỉ cần khoảng $$2^{b/2}$$ phép thử để tìm thấy đụng độ (đó là lý do MD5 128-bit và SHA-1 160-bit bị khai tử, phải chuyển sang SHA-256 có độ an toàn đụng độ $$2^{128}$$!).

#### Bước 4: Luôn thêm Salt khi băm mật khẩu
Băm trần `SHA256(password)` dễ bị tra ngược bằng Rainbow Table; cộng thêm chuỗi ngẫu nhiên riêng cho từng tài khoản (**salt**) và dùng hàm băm chậm (Argon2/bcrypt) mới an toàn thực sự!

$$
\text{Số học modulo }\mathbb{Z}_m
\;\longrightarrow\;
\text{Bảng băm }\&\text{ SHA-256} \;\vert\; \text{LCG (Hull–Dobell)} \;\vert\; \text{Mã kiểm tra ISBN/Luhn}.
$$

## Hàm băm mật mã

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Hàm băm mật mã** $$H$$ ánh xạ một thông điệp có độ dài tùy ý sang chuỗi **digest** có độ dài cố định (ví dụ 256 bit), thỏa mãn các yêu cầu tiêu chuẩn sau:

1. **Tất định**: cùng một đầu vào luôn cho cùng một đầu ra.
2. **Preimage resistance (Kháng tiền ảnh)**: cho trước $$h$$, rất khó tìm được $$m$$ sao cho $$H(m)=h$$.
3. **Collision resistance (Kháng va chạm)**: rất khó tìm được hai đầu vào khác nhau $$m_1\neq m_2$$ sao cho $$H(m_1)=H(m_2)$$.
4. **Avalanche (Hiệu ứng thác lũ)**: một thay đổi nhỏ ở đầu vào tạo ra thay đổi lớn ở giá trị digest.

</div>

Cần phân biệt rõ: hàm $$h(k)=k \bmod m$$ dùng trong bảng băm cấu trúc dữ liệu **không** đáp ứng các tính chất trên. Hàm băm mật mã (như SHA-256, SHA-3) sử dụng nhiều vòng trộn bit phức tạp chứ không chỉ một phép modulo đơn lẻ.

<div class="textbook-example" markdown="1">

**Ví dụ 1** (Hiệu ứng avalanche). Chỉ khác nhau chữ hoa/chữ thường ở ký tự đầu tiên:

```text
SHA256("Hello") = 185f8db3…1969
SHA256("hello") = 2cf24dba…9824
```

Hai giá trị digest khác nhau hoàn toàn, không thể suy ra mức độ “gần nhau” của hai bản rõ từ đầu ra băm.

</div>

Hàm băm mật mã được ứng dụng rộng rãi để kiểm tra toàn vẹn tệp tin, định danh commit trong Git, cơ chế proof-of-work và bước băm trước khi ký (*hash-then-sign*) trong chữ ký số.

## Sinh số giả ngẫu nhiên (PRNG)

Máy tính số hoạt động theo cơ chế tất định nên không thể tự tạo ra tính ngẫu nhiên thuần túy; **PRNG** sinh ra dãy số có vẻ ngẫu nhiên từ một giá trị khởi tạo (*seed*).

### Linear Congruential Generator (LCG)

<div class="textbook-definition" markdown="1">

**Định nghĩa** (LCG). Bộ sinh tuyến tính đồng dư tạo dãy theo công thức

$$
x_{n+1} = (a x_n + c) \bmod m
$$

với các hằng số $$a,c,m$$ và giá trị hạt giống $$x_0$$. Chu kỳ tối đa của dãy không vượt quá $$m$$; điều kiện Hull–Dobell xác định khi nào dãy đạt chu kỳ đầy đủ.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2.** Với $$a=5$$, $$c=1$$, $$m=8$$ và $$x_0=0$$, ta thu được dãy:

$$
1,6,7,4,5,2,3,0,\ldots
$$

Dãy này có chu kỳ bằng $$m=8$$.

</div>

**Cảnh báo.** LCG **không** đủ an toàn cho mục đích mật mã vì dãy số dễ bị dự đoán chỉ sau vài giá trị quan sát. Khi sinh khóa, nonce hoặc salt, cần dùng **CSPRNG** (như `/dev/urandom`, thư viện `secrets` trong Python hoặc API bảo mật của hệ điều hành).

## Dùng CRT tăng tốc RSA

Thay vì tính trực tiếp $$S = M^d \bmod n$$ với $$n=pq$$ rất lớn, ta có thể tách thành hai phép tính trên các modulus nhỏ hơn:

$$
S_p = M^{d \bmod (p-1)} \bmod p, \qquad
S_q = M^{d \bmod (q-1)} \bmod q,
$$

sau đó ghép lại thành $$S$$ bằng Định lý số dư Trung Hoa (CRT). Vì $$p$$ và $$q$$ chỉ dài xấp xỉ một nửa số bit của $$n$$, chi phí tính lũy thừa giảm đáng kể — trong thực tế thường tăng tốc khoảng **3–4 lần** so với việc tính trực tiếp theo modulo $$n$$.

## ECC và mật mã hậu lượng tử

### Đường cong elliptic (ECC)

ECC hoạt động trên nhóm các điểm thuộc một đường cong elliptic định nghĩa trên trường hữu hạn. Ở cùng một mức bảo mật cổ điển ước lượng, khóa ECC **ngắn hơn nhiều** so với khóa RSA:

| Mức bảo mật (ước lượng bit) | RSA (bit modulus) | ECC (bit) |
|:---:|:---:|:---:|
| 128 | ~3072 | ~256 |
| 256 | ~15360 | ~512 |

ECC được sử dụng rộng rãi trong TLS, Bitcoin (ECDSA) và nhiều hệ thống di động. Chi tiết về cấu trúc nhóm điểm nằm ngoài phạm vi chương này; điểm cần nắm là ECC giữ **cùng nguyên lý** mật mã bất đối xứng (dựa trên một bài toán rời rạc khó) nhưng xây dựng trên cấu trúc đại số khác với RSA.

### Máy tính lượng tử và mật mã hậu lượng tử

Thuật toán **Shor** trên máy tính lượng tử có thể phân tích thừa số nguyên tố và giải bài toán logarit rời rạc trong thời gian đa thức, đe dọa trực tiếp RSA cũng như nhiều hệ ECC và Diffie–Hellman cổ điển. **Mật mã hậu lượng tử** (*post-quantum cryptography*, PQC) tập trung xây dựng các thành phần mật mã dựa trên những bài toán được tin là kháng lại máy tính lượng tử, chẳng hạn:

- mật mã dựa trên mạng tinh thể (*lattice-based*, như Kyber, Dilithium do NIST chuẩn hóa),
- mật mã dựa trên mã sửa lỗi (*code-based*),
- chữ ký số dựa trên hàm băm (*hash-based signatures*),
- mật mã đa biến (*multivariate*).

Cần hiểu rằng việc RSA-2048 vẫn đang được sử dụng phổ biến hiện nay **không** mâu thuẫn với yêu cầu chuẩn bị lộ trình chuyển đổi sang PQC cho những hệ thống có vòng đời nhiều thập kỷ.

## Thử nghiệm tương tác

Thử nghiệm phân bố bucket theo modulo, chữ số kiểm tra ISBN và bộ sinh LCG:

<div class="interactive-demo" markdown="1">
<div data-demo="number-theory-apps"></div>
</div>
<script src="{{ '/public/js/number-theory-apps.js' | relative_url }}"></script>

## Nguyên tắc kỹ nghệ

Lý thuyết số hiện diện từ chỉ số bảng băm, mã kiểm tra (checksum) cho tới giao thức TLS. Sinh viên khoa học máy tính không nhất thiết phải trở thành chuyên gia mật mã, nhưng cần nắm vững các nguyên tắc thực hành cơ bản: **không** dùng MD5 hay SHA-1 cho các hệ thống bảo mật mới, **không** tự thiết kế thuật toán mã hóa riêng và luôn **chọn các thư viện** đã qua thẩm định (như libsodium, OpenSSL API hiện đại, WebCrypto, …).

### Minh họa tương tác

Minh họa thuật toán lũy thừa modulo nhanh (bình phương liên tiếp) — nền tảng của RSA và kiểm tra tính nguyên tố:

<div class="interactive-demo" markdown="1">
<div data-demo="numtheory-explainer" data-tab="fastexp"></div>
</div>
<script src="{{ '/public/js/explainers/numtheory-explainer.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

So sánh giá trị digest SHA-256 của hai chuỗi chỉ khác nhau một ký tự (bằng công cụ trực tuyến hoặc thư viện lập trình) và nhận xét về hiện tượng avalanche.

<details>
<summary>Đáp án</summary>

Hai giá trị digest khác nhau hoàn toàn (về mặt kỳ vọng, khoảng một nửa số bit bị lật đối với hàm băm tốt). Không thể suy ra mức độ giống nhau của hai bản rõ dựa trên giá trị digest.

</details>

### Bài tập 2

Cho bộ sinh LCG với $$a=7$$, $$c=3$$, $$m=10$$ và $$x_0=2$$. Hãy sinh 10 số đầu tiên và nhận xét về chu kỳ của dãy.

<details>
<summary>Đáp án</summary>

Áp dụng $$x_{n+1}=(7x_n+3)\bmod 10$$, ta thu được dãy lặp lại $$2,7,2,7,\ldots$$. Dãy chỉ có chu kỳ bằng 2, **không** đạt chu kỳ tối đa $$m=10$$ do lựa chọn tham số kém.

</details>

### Bài tập 3

Vì sao RSA-2048 vẫn được sử dụng rộng rãi trong thập niên 2020 nhưng lộ trình chuyển đổi sang PQC vẫn cần thiết?

<details>
<summary>Đáp án</summary>

Trên máy tính cổ điển, việc phân tích thừa số một modulus 2048 bit vẫn vượt xa khả năng tính toán thực tế. Tuy nhiên, nếu máy tính lượng tử đủ lớn xuất hiện, thuật toán Shor có thể phá vỡ RSA; dữ liệu mã hóa hôm nay có nguy cơ bị thu thập trước để giải mã về sau (*harvest now, decrypt later*). Vì vậy, các hệ thống cần chuẩn bị sớm cho lộ trình PQC.

</details>

### Bài tập 4

So sánh ngắn gọn kích thước khóa công khai của RSA-3072, ECC-256 và Kyber-512 ở mức bậc lớn.

<details>
<summary>Đáp án</summary>

| Hệ mật | Khóa công khai (xấp xỉ) |
|:---|:---|
| RSA-3072 | ~3072 bit |
| ECC-256 | ~256 bit |
| Kyber-512 | cỡ hàng trăm byte (lớn hơn ECC, thường nhỏ hơn RSA-3072) |

Kyber được thiết kế theo hướng kháng lượng tử, còn RSA và ECC cổ điển không kháng được thuật toán Shor.

</details>

## Tóm tắt

1. **Hàm băm mật mã** khác với phép chia lấy dư trong bảng băm; nó đòi hỏi kháng tiền ảnh, kháng va chạm và hiệu ứng avalanche.
2. **LCG** minh họa ứng dụng của số học modulo, nhưng bảo mật thực tế bắt buộc phải dùng **CSPRNG**.
3. **CRT** tăng tốc phép lũy thừa RSA bằng cách tính riêng theo modulo $$p$$ và $$q$$ rồi ghép kết quả.
4. **ECC** cho kích thước khóa ngắn hơn đáng kể so với RSA ở cùng mức bảo mật ước lượng.
5. **PQC** là hướng chuẩn bị cho kỷ nguyên hậu lượng tử; trong thực hành kỹ thuật không nên tự phát minh thuật toán mật mã.

Bài khảo sát 15.5 sẽ kết nối tiến trình lịch sử từ Euclid đến blockchain, trước khi Chương 16 chuyển sang cấu trúc **cây**.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=e8DtzQkjOMQ">The Chinese Remainder Theorem (Solved Example 1)</a> — Neso Academy, tiếng Anh. Ví dụ giải Định lý số dư Trung Hoa, hỗ trợ cho phần dùng CRT tăng tốc RSA.
- <a href="https://www.youtube.com/watch?v=NF1pwjL9-DE">Elliptic Curves - Computerphile</a> — Computerphile, tiếng Anh. Giải thích về đường cong elliptic cho phần ECC.
- <a href="https://www.youtube.com/watch?v=jsraR-el8_o">Hash Collisions &amp; The Birthday Paradox - Computerphile</a> — Computerphile, tiếng Anh. Va chạm hàm băm và nghịch lý ngày sinh, liên quan trực tiếp đến mục hàm băm mật mã.
