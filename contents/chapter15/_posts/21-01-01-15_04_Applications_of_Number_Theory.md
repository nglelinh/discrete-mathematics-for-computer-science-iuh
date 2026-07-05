---
layout: post
title: "Ứng dụng của Lý thuyết Số trong Khoa học Máy tính"
categories: chapter15
date: 2021-01-01
order: 4
required: false
lang: en
excerpt: "Ở mục trước chúng ta đã nắm các khái niệm mật mã cơ bản. Mục này trình bày ứng dụng của lý thuyết số trong thực tế — từ RSA và hàm băm đến chữ ký số và các…"
---

Ở mục trước chúng ta đã nắm các khái niệm mật mã cơ bản. Mục này trình bày **ứng dụng của lý thuyết số** trong thực tế — từ RSA và hàm băm đến chữ ký số và các giao thức bảo mật — cho thấy cách định lý toán học được chuyển thành cơ chế bảo vệ hệ thống.

![Ứng dụng đồng dư](/discrete-mathematics-for-computer-science-iuh/img/course/modular_arithmetic.svg)

<p class="textbook-figure-caption" data-figure="15.16">Checksum, mã hóa đơn giản và xoay vòng chỉ số đều dùng arithmetic modulo.</p>
![Hashing và bucket](/discrete-mathematics-for-computer-science-iuh/img/course/Hash_table_simple_999.svg)

<p class="textbook-figure-caption" data-figure="15.17">Phân bố bucket bằng modulo — trực giác số học cho cấu trúc dữ liệu.</p>
![Chữ ký số](/discrete-mathematics-for-computer-science-iuh/img/course/rsa_key_generation.svg)

<p class="textbook-figure-caption" data-figure="15.18">Chữ ký số và xác thực danh tính — ứng dụng trực tiếp của lý thuyết số.</p>
![Kiểm tra số nguyên tố](/discrete-mathematics-for-computer-science-iuh/img/course/PrimeDecompositionExample.svg)

<p class="textbook-figure-caption" data-figure="15.19">Miller–Rabin và các test xác suất — ứng dụng đồng dư trong bảo mật.</p>
![Mã sửa lỗi](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="15.20">Reed–Solomon và Hamming — đại số hữu hạn bảo vệ dữ liệu truyền thông và lưu trữ.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Liệt kê** các ứng dụng của số nguyên tố và modulo trong CS.
- **Hiểu** nguyên lý hoạt động của hàm băm và checksum.
- **Giải thích** cách sinh số giả ngẫu nhiên bằng đồng dư tuyến tính.
- **Mô tả** ứng dụng của Định lý Số dư Trung Hoa trong tính toán song song.
- **Nhận thức** về mật mã hậu lượng tử.

**Từ khóa**: Hàm băm (hash), MD5, SHA, số giả ngẫu nhiên (PRNG), mã hóa đường cong elliptic (ECC), mật mã hậu lượng tử (post-quantum).
</div>

## 1. Hàm băm Mật mã

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Hàm băm mật mã** $$H$$ ánh xạ thông điệp độ dài tùy ý thành **digest** cố định (ví dụ 256 bit). Yêu cầu:

1. **Tất định**: cùng đầu vào → cùng đầu ra.
2. **Preimage resistance**: cho $$h$$, khó tìm $$m$$ với $$H(m) = h$$.
3. **Collision resistance**: khó tìm $$m_1 \neq m_2$$ với $$H(m_1) = H(m_2)$$.
4. **Avalanche effect**: thay đổi nhỏ đầu vào → thay đổi lớn đầu ra.
</div>

<div class="textbook-example" markdown="1">
**SHA-256** (Bitcoin, TLS):
```
SHA256("Hello") = 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
SHA256("hello") = 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```
Chỉ khác H/h mà kết quả hoàn toàn khác.
</div>

## 2. Sinh Số Giả Ngẫu nhiên (PRNG)

Máy tính là thiết bị tất định — không thể sinh số "thực sự" ngẫu nhiên. PRNG dùng công thức toán để sinh dãy số *trông* ngẫu nhiên.

### Linear Congruential Generator (LCG)

<div class="textbook-equation" markdown="1">
$$x_{n+1} = (a \cdot x_n + c) \bmod m$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
trong đó $$a, c, m$$ là các hằng số chọn cẩn thận.

<div class="textbook-definition" markdown="1">
**Định nghĩa** (LCG): **Bộ sinh số giả ngẫu nhiên tuyến tính đồng dư**:
$$x_{n+1} = (a \cdot x_n + c) \bmod m$$
với hằng số $$a, c, m$$ chọn theo tiêu chuẩn (Hull–Dobell).
</div>

<div class="textbook-example" markdown="1">
Với $$a = 5, c = 1, m = 8, x_0 = 0$$:
<div class="textbook-equation" markdown="1">
$$x_1 = 1, x_2 = 6, x_3 = 7, x_4 = 4, x_5 = 5, x_6 = 2, x_7 = 3, x_8 = 0, \ldots$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Chu kỳ $$= m = 8$$.
</div>

**Cảnh báo**: LCG không đủ cho mật mã — dùng **CSPRNG** (`/dev/urandom`, `secrets` trong Python).

## 3. CRT trong Tính toán Song song

Định lý Số dư Trung Hoa cho phép tách một phép tính modulo số lớn $$N$$ thành các phép tính modulo các thừa số nhỏ hơn:

Thay vì tính $$(a \times b) \bmod N$$ trực tiếp với $$N$$ 2048-bit, chúng ta tính riêng modulo $$p$$ và $$q$$, rồi dùng CRT để gộp kết quả. Điều này tăng tốc RSA gấp 4 lần.

<div class="content-box example-box textbook-block" markdown="1">
**Ứng dụng trong RSA**: Khi Bob ký một tài liệu, anh chúng ta tính $$S = M^d \bmod n$$. Dùng CRT, thay vì tính trực tiếp modulo $$n$$ (cỡ 2048-bit), Bob tính:
- $$S_p = M^{d \bmod (p-1)} \bmod p$$
- $$S_q = M^{d \bmod (q-1)} \bmod q$$
- Sau đó kết hợp bằng CRT để được $$S$$.

Kết quả: nhanh hơn ~4 lần!
</div>

## 4. Nâng cao: ECC và Mật mã Hậu Lượng tử

### Elliptic Curve Cryptography (ECC)

Dùng cấu trúc đại số của đường cong elliptic, cung cấp cùng mức bảo mật với RSA nhưng với khóa ngắn hơn nhiều:

| Mức bảo mật (bits) | RSA Key Size | ECC Key Size |
|:---|---|---:|
| 128 | 3072 | 256 |
| 256 | 15360 | 512 |

ECC được dùng trong Bitcoin (ECDSA), iMessage, TLS 1.3.

### Mối đe dọa: Máy tính Lượng tử

Thuật toán Shor (cho máy tính lượng tử) có thể phân tích thừa số trong thời gian đa thức — phá vỡ RSA hoàn toàn. **Mật mã hậu lượng tử** (Post-Quantum Cryptography) đang phát triển các hệ mật kháng lượng tử, dựa trên:
- Mạng (lattice-based) — ứng viên hàng đầu
- Mã hóa dựa trên mã sửa lỗi (code-based)
- Hàm băm (hash-based signatures)
- Đa thức nhiều biến (multivariate)

NIST (Viện Tiêu chuẩn Mỹ) đã chọn các thuật toán hậu lượng tử đầu tiên vào năm 2022-2024, bao gồm CRYSTALS-Kyber (mã hóa) và CRYSTALS-Dilithium (chữ ký số).

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: Tính toán Hash</h3>
<p>Công cụ này cho phép sinh viên nhập một thông điệp và xem giá trị hash của nó dùng SHA-256. Quan sát hiệu ứng lan truyền (avalanche effect): thay đổi một ký tự sẽ làm thay đổi hoàn toàn giá trị hash. <strong>Gợi ý thực hành:</strong> So sánh hash của "cat" và "cat " (thêm một khoảng trắng ở cuối).</p>
<div data-demo="number-theory-apps"></div>
</div>
<script src="{{ '/public/js/number-theory-apps.js' | relative_url }}"></script>

## Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Cần chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Lý thuyết số hiện diện trong mọi lớp của stack công nghệ: từ trình biên dịch (tối ưu hóa modulo), cơ sở dữ liệu (hash indexing), đến tầng ứng dụng (mã hóa, chữ ký số). Sinh viên CS không cần trở thành chuyên gia mật mã, nhưng *phải* hiểu đủ để không mắc lỗi bảo mật cơ bản — như dùng MD5 (đã bị phá) hay tự "phát minh" thuật toán mã hóa.

**Nguyên tắc vàng của mật mã học**: Không bao giờ tự phát minh thuật toán mã hóa. Luôn dùng thư viện chuẩn, đã được kiểm chứng bởi cộng đồng bảo mật.

## Bài tập

Khi làm bài tập, nên bắt đầu bằng cách xác định dữ kiện, dạng bài và công cụ phù hợp trước khi tính toán. Cách tiếp cận này thường giúp tránh sai từ bước đầu.

1. Tính SHA-256 của một chuỗi ký tự (dùng công cụ online). Thay đổi một ký tự, so sánh kết quả.
2. Với LCG: $$a = 7, c = 3, m = 10, x_0 = 2$$, sinh 10 số đầu tiên. Nhận xét về chu kỳ.
3. Tại sao RSA với khóa 2048-bit vẫn an toàn năm 2024 nhưng có thể không an toàn năm 2035?
4. **Thử thách nghiên cứu**: Tìm hiểu về CRYSTALS-Kyber — thuật toán mã hóa hậu lượng tử được NIST chuẩn hóa. So sánh kích thước khóa của nó với RSA và ECC.

<details>
<summary>Hướng dẫn bài 4</summary>

CRYSTALS-Kyber là thuật toán mã hóa dựa trên mạng (lattice-based). So sánh kích thước khóa:

| Thuật toán | Khóa công khai | Bản mã |
|:---|:---|---:|
| RSA-3072 | 3072 bits | 3072 bits |
| ECC-256 | 256 bits | 512 bits |
| Kyber-512 | 800 bytes | 768 bytes |
| Kyber-768 | 1184 bytes | 1088 bytes |

Kyber có khóa lớn hơn ECC nhưng nhỏ hơn RSA. Tuy nhiên, Kyber được thiết kế để kháng lại tấn công từ máy tính lượng tử — một ưu điểm vô giá trong tương lai.
</details>

## Xem thêm / Video gợi ý

- [Logic Gates, Truth Tables, Boolean Algebra](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — 3Blue1Brown (Animation + intuition for logic)
- [Introduction to Propositional Logic](https://www.youtube.com/watch?v=4l7L9v0p0Q) — MIT OCW 6.042J (Tom Leighton — formal foundation)

## Tóm tắt

- **Hàm băm**: một chiều, chống va chạm — dùng cho xác thực và toàn vẹn dữ liệu.
- **PRNG**: sinh số giả ngẫu nhiên bằng $$x_{n+1} = (ax_n + c) \bmod m$$.
- **CRT**: tăng tốc RSA gấp ~4 lần bằng tính toán song song.
- **ECC**: cùng bảo mật với RSA nhưng khóa ngắn hơn nhiều.
- **Hậu lượng tử**: thế hệ mật mã tiếp theo, kháng máy tính lượng tử.
- **Nguyên tắc vàng**: không tự phát minh mật mã.

Đây là bài cuối cùng của chương Lý thuyết Số và Mật mã. Trong chương tiếp theo, chúng ta sẽ chuyển sang cấu trúc dữ liệu cây (trees) — một trong những cấu trúc quan trọng nhất trong khoa học máy tính.

## Tài liệu Tham khảo

1. NIST, "Post-Quantum Cryptography Standardization," 2022-2024 — quy trình chuẩn hóa mật mã hậu lượng tử.
2. Daniel J. Bernstein, "Introduction to Post-Quantum Cryptography," 2009.
3. Alfred J. Menezes et al., *Handbook of Applied Cryptography* — tài liệu tham khảo tự do (có online).
4. Satoshi Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System," 2008 — ứng dụng của hash và chữ ký số trong tiền mã hóa.
