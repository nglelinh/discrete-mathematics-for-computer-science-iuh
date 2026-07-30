---
layout: post
title: "Ứng dụng của Lý thuyết Số trong Khoa học Máy tính"
categories: chapter15
date: 2021-01-01
order: 4
required: false
lang: en
excerpt: "Hàm băm mật mã, PRNG/LCG, CRT tăng tốc RSA, ECC và mật mã hậu lượng tử — ứng dụng thực tế của modulo và số nguyên tố."
---

<div class="textbook-epigraph" markdown="1">

"Don't invent your own crypto — use reviewed standards."

<span class="epigraph-attribution">— Nguyên tắc kỹ nghệ bảo mật</span>

</div>

Các mục trước đã cung cấp công cụ số học và mô hình RSA / Diffie–Hellman. Mục này gắn chúng với **ứng dụng hệ thống**: hàm băm, sinh số giả ngẫu nhiên, tăng tốc RSA bằng CRT, đường cong elliptic (ECC) và định hướng **mật mã hậu lượng tử** — ở mức khái niệm phù hợp sinh viên đại học, không thay giáo trình chuyên sâu.

![Hashing modulo](/discrete-mathematics-for-computer-science-iuh/img/course/Hash_table_simple_999.svg)

<p class="textbook-figure-caption" data-figure="15.7">Phân bố bucket bằng modulo — trực giác số học cho bảng băm (không phải hash mật mã).</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Nêu** yêu cầu của hàm băm mật mã (preimage, collision, avalanche).
- **Mô tả** LCG và giới hạn khi dùng cho mật mã.
- **Giải thích** CRT tăng tốc lũy thừa modulo RSA.
- **So sánh** kích thước khóa RSA vs ECC ở mức bảng.
- **Nhận biết** mối đe dọa Shor và hướng post-quantum.

**Từ khóa**: hash, SHA-256, PRNG, LCG, CRT-RSA, ECC, post-quantum.

</div>

## 1. Hàm băm mật mã

<div class="textbook-definition" markdown="1">

**Định nghĩa.** **Hàm băm mật mã** $$H$$ ánh xạ thông điệp độ dài tùy ý sang **digest** độ dài cố định (ví dụ 256 bit). Yêu cầu tiêu chuẩn:

1. **Tất định**: cùng đầu vào → cùng đầu ra.
2. **Preimage resistance**: cho $$h$$, khó tìm $$m$$ với $$H(m)=h$$.
3. **Collision resistance**: khó tìm $$m_1\neq m_2$$ với $$H(m_1)=H(m_2)$$.
4. **Avalanche**: thay đổi nhỏ đầu vào → thay đổi lớn digest.

</div>

Phân biệt: $$h(k)=k \bmod m$$ trong bảng băm cấu trúc dữ liệu **không** đủ các tính chất trên. Hash mật mã (SHA-256, SHA-3) dùng phép trộn phức tạp, không chỉ một phép modulo.

<div class="textbook-example" markdown="1">

**Ví dụ 1** (avalanche). Chỉ khác hoa/thường ở chữ cái đầu:

```text
SHA256("Hello") = 185f8db3…1969
SHA256("hello") = 2cf24dba…9824
```

Hai digest hoàn toàn khác — không suy ra “gần nhau” trên plaintext.

</div>

Ứng dụng: toàn vẹn file, commit Git, proof-of-work, và bước hash-then-sign trong chữ ký số.

## 2. Sinh số giả ngẫu nhiên (PRNG)

Máy tính số tất định không “tự sinh” entropy thuần; **PRNG** sinh dãy trông ngẫu nhiên từ seed.

### Linear Congruential Generator (LCG)

<div class="textbook-definition" markdown="1">

**Định nghĩa** (LCG). Dãy

$$
x_{n+1} = (a x_n + c) \bmod m
$$

với hằng số $$a,c,m$$ và seed $$x_0$$. Chu kỳ tối đa $$\le m$$; điều kiện Hull–Dobell cho chu kỳ đầy đủ.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2.** $$a=5$$, $$c=1$$, $$m=8$$, $$x_0=0$$:

$$
1,6,7,4,5,2,3,0,\ldots
$$

chu kỳ $$=m=8$$.

</div>

**Cảnh báo.** LCG **không** đủ cho mật mã (dễ dự đoán sau vài quan sát). Khóa, nonce, salt cần **CSPRNG** (`/dev/urandom`, `secrets` trong Python, API hệ điều hành).

## 3. CRT tăng tốc RSA

Thay vì tính $$S = M^d \bmod n$$ trực tiếp với $$n=pq$$ lớn, có thể tính

$$
S_p = M^{d \bmod (p-1)} \bmod p, \qquad
S_q = M^{d \bmod (q-1)} \bmod q,
$$

rồi ghép $$S$$ bằng CRT. Vì $$p,q$$ khoảng một nửa số bit của $$n$$, chi phí lũy thừa giảm đáng kể — thực tế thường tăng tốc khoảng **3–4 lần** so với một lũy thừa modulo $$n$$ thuần.

## 4. ECC và mật mã hậu lượng tử

### Đường cong elliptic (ECC)

ECC dùng nhóm điểm trên đường cong elliptic trên trường hữu hạn. Cùng mức bảo mật “cổ điển” ước lượng, khóa ECC **ngắn hơn nhiều** so với RSA:

| Mức bảo mật (ước lượng bits) | RSA (bit modulus) | ECC (bit) |
|:---:|:---:|:---:|
| 128 | ~3072 | ~256 |
| 256 | ~15360 | ~512 |

ECC xuất hiện trong TLS, Bitcoin (ECDSA), nhiều hệ di động. Chi tiết nhóm điểm nằm ngoài phạm vi chương này; điểm quan trọng: **cùng tinh thần** bất đối xứng (bài toán rời rạc khó) nhưng cấu trúc khác RSA.

### Máy lượng tử và post-quantum

Thuật toán **Shor** (máy lượng tử) phân tích thừa số và giải DLP trong thời gian đa thức — đe dọa RSA và nhiều hệ ECC/DH cổ điển. **Mật mã hậu lượng tử** (*post-quantum cryptography*, PQC) tìm primitive dựa trên bài toán được tin kháng lượng tử, ví dụ:

- lattice-based (Kyber, Dilithium — chuẩn hóa NIST),
- code-based,
- hash-based signatures,
- multivariate.

Sinh viên cần biết: “RSA 2048 vẫn dùng rộng rãi hôm nay” **không** mâu thuẫn với việc chuẩn bị lộ trình PQC cho hệ thống sống nhiều thập kỷ.

## 5. Thử nghiệm tương tác

Hash bucket modulo, ISBN check digit và LCG:

<div class="interactive-demo" markdown="1">
<div data-demo="number-theory-apps"></div>
</div>
<script src="{{ '/public/js/number-theory-apps.js' | relative_url }}"></script>

## 6. Nguyên tắc kỹ nghệ

Lý thuyết số có mặt từ chỉ số hash, checksum đến TLS. Sinh viên CS không cần trở thành nhà mật mã, nhưng cần đủ để **không** dùng MD5/SHA-1 cho bảo mật mới, **không** tự chế cipher, và **chọn thư viện** đã review (libsodium, OpenSSL API hiện đại, WebCrypto, …).

## Bài tập

### Bài tập 1

So sánh digest SHA-256 của hai chuỗi chỉ khác một ký tự (công cụ online hoặc thư viện). Nêu hiện tượng avalanche.

<details>
<summary>Đáp án</summary>

Hai digest khác hẳn (khoảng một nửa bit lật về kỳ vọng với hash tốt). Không suy ra quan hệ gần giữa plaintext từ digest.

</details>

### Bài tập 2

LCG: $$a=7$$, $$c=3$$, $$m=10$$, $$x_0=2$$. Sinh 10 số đầu; nhận xét chu kỳ.

<details>
<summary>Đáp án</summary>

$$x_{n+1}=(7x_n+3)\bmod 10$$:  
$$2,7,2,7,\ldots$$ — chu kỳ 2, **không** đạt $$m=10$$ (tham số kém).

</details>

### Bài tập 3

Vì sao RSA-2048 vẫn được dùng rộng rãi năm 2020s nhưng lộ trình PQC vẫn cần thiết?

<details>
<summary>Đáp án</summary>

Trên máy cổ điển, factoring 2048-bit vẫn rất tốn kém. Máy lượng tử đủ lớn (khi/ nếu xuất hiện) phá RSA bằng Shor; dữ liệu mã hóa hôm nay có thể bị lưu để giải sau (*harvest now, decrypt later*). Hệ thống cần chuẩn bị PQC.

</details>

### Bài tập 4

So sánh gọn kích thước khóa RSA-3072, ECC-256 và Kyber-512 (bậc lớn).

<details>
<summary>Đáp án</summary>

| Hệ | Khóa công khai (xấp xỉ) |
|:---|:---|
| RSA-3072 | ~3072 bit |
| ECC-256 | ~256 bit |
| Kyber-512 | cỡ hàng trăm byte (lớn hơn ECC, thường nhỏ hơn RSA-3072) |

Kyber hướng kháng lượng tử; RSA/ECC cổ điển thì không (trước Shor).

</details>

## Tóm tắt

1. **Hash mật mã** ≠ modulo bucket; cần preimage / collision / avalanche.
2. **LCG** minh họa modulo; **CSPRNG** cho bảo mật.
3. **CRT** tăng tốc lũy thừa RSA modulo $$p$$ và $$q$$.
4. **ECC**: khóa ngắn hơn RSA cùng mức ước lượng.
5. **PQC**: chuẩn bị sau lượng tử; không tự phát minh crypto.

Bài khảo sát 15.5 nối lịch sử từ Euclid đến blockchain; Chương 16 chuyển sang **cây**.
