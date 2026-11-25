---
layout: post
title: "Mật mã học Cơ bản"
categories: chapter15
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Mã hóa đối xứng và bất đối xứng; Caesar, Affine; RSA (tạo khóa, mã hóa và giải mã); Diffie–Hellman; chữ ký số — gắn với số học modulo và thuật toán Euclid."
---

> **Câu chuyện mở đầu:** Suốt hàng nghìn năm lịch sử, mọi hệ mật mã (từ mã dịch vòng Caesar đến máy Enigma trong Thế chiến II) đều mắc chung một điểm yếu chí mạng: **hai người phải bí mật gặp nhau trước để trao đổi chung một chìa khóa**! Nếu kẻ thù nghe lén được chìa khóa đó, toàn bộ bí mật sụp đổ. Năm 1976–1977, Diffie–Hellman và bộ ba Rivest–Shamir–Adleman (**RSA**) tạo ra phép màu **Mật mã Khóa Công khai**: *bạn công bố ổ khóa cho cả thế giới thấy để ai cũng khóa thư gửi cho bạn được, nhưng chỉ duy nhất chiếc chìa khóa bí mật trong tay bạn mới mở được!*

<div class="textbook-epigraph" markdown="1">

"We stand today on the brink of a revolution in cryptography."

<span class="epigraph-attribution">— Diffie & Hellman (1976), tinh thần</span>

</div>

Số học modulo cung cấp công cụ tính toán trên các lớp số dư, còn **mật mã học** ứng dụng những cấu trúc đó để bảo vệ tính bí mật, tính toàn vẹn và xác thực thông tin. Bài học này giới thiệu mô hình hệ mật mã, các phương pháp mã hóa cổ điển (Caesar, Affine), hệ mật RSA, giao thức trao đổi khóa Diffie–Hellman và chữ ký số, sử dụng các ví dụ số nhỏ có thể tính toán trực tiếp bằng tay.

![Luồng RSA](/discrete-mathematics-for-computer-science-iuh/img/course/Number_rsa_flow.svg)

<p class="textbook-figure-caption" data-figure="15.5">RSA: khóa công khai $$(n,e)$$, khóa riêng $$d$$; mã hóa $$C \equiv M^e \pmod n$$ và giải mã $$M \equiv C^d \pmod n$$.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phân biệt** mã hóa đối xứng và mã hóa bất đối xứng.
- **Thực hiện** mã hóa và giải mã với Caesar, Affine và RSA trên các số nhỏ.
- **Thực hiện** một vòng trao đổi khóa Diffie–Hellman với số nhỏ.
- **Giải thích** các giả thuyết bảo mật của RSA (phân tích thừa số) và bài toán logarit rời rạc (DLP).
- **Mô tả** nguyên lý chữ ký số RSA ở mức khái niệm.

**Từ khóa**: encryption, public/private key, RSA, Diffie–Hellman, Caesar, Affine, chữ ký số.

</div>

## Bản đồ kiến thức nền: Mật mã học Hiện đại dựa trên những trụ cột nào?

### 1. Mật mã Đối xứng (Symmetric) vs. Bất đối xứng (Public-Key)
- **Đối xứng (Caesar, Affine, AES):** Dùng **chung 1 khóa** để mã hóa và giải mã — siêu nhanh cho dữ liệu lớn, nhưng khó trao đổi khóa qua mạng công cộng.
- **Bất đối xứng (RSA, ECC):** Dùng cặp **(Khóa công khai $$e$$, Khóa bí mật $$d$$)** nối nhau qua một **hàm cửa sập một chiều (trapdoor one-way function)**: nhân $$p \cdot q = n$$ mất 1 micro giây, nhưng phân tích $$n$$ ngược lại thành $$p, q$$ mất hàng triệu năm!

### 2. Kiến trúc Toán học của Hệ mật RSA
- Chọn hai số nguyên tố lớn $$p, q$$; đặt $$n = pq$$ và $$\varphi(n) = (p-1)(q-1)$$.
- Chọn $$e$$ nguyên tố cùng nhau với $$\varphi(n)$$, tính $$d = e^{-1} \bmod \varphi(n)$$.
- **Mã hóa:** $$C = M^e \bmod n$$. **Giải mã:** $$M = C^d \bmod n$$ (đúng nhờ Định lý Euler: $$(M^e)^d = M^{ed} = M^{1 + k\varphi(n)} \equiv M \pmod n$$!).

### 3. Chữ ký Số (Digital Signatures)
- **Bản chất:** Đảo ngược vai trò khóa: người gửi ký bằng **khóa bí mật $$d$$** ($$S = h(M)^d \bmod n$$), bất kỳ ai cũng xác thực được bằng **khóa công khai $$e$$** (kiểm tra $$S^e \equiv h(M) \pmod n$$) — bảo đảm tính xác thực và chống chối bỏ!

## Ví dụ tính tay cầm tay chỉ việc: Chạy trọn vẹn RSA từ A đến Z với $$p = 5,\; q = 11$$

1. **Sinh khóa:**
   - $$n = p \cdot q = 5 \times 11 = 55$$.
   - $$\varphi(n) = (5 - 1)(11 - 1) = 4 \times 10 = 40$$.
   - Chọn khóa công khai **$$e = 3$$** ($$\gcd(3, 40) = 1$$).
   - Tìm khóa bí mật $$d = 3^{-1} \bmod 40$$: vì $$3 \times 27 = 81 = 2\cdot 40 + 1 \equiv 1 \pmod{40}$$, nên **$$d = 27$$**!
   *(Công bố $$(n, e) = (55, 3)$$; giữ kín $$d = 27$$ và hủy $$p, q, \varphi(n)$$!)*

2. **Mã hóa thông điệp $$M = 7$$:**
   $$
   C = 7^3 \bmod 55 = 343 \bmod 55 = 13 \quad (\text{vì } 55 \times 6 = 330,\; 343 - 330 = 13).
   $$

3. **Giải mã bản mã $$C = 13$$ bằng bình phương liên tiếp ($$27 = 16 + 8 + 2 + 1$$):**
   - $$13^1 \equiv 13 \pmod{55}$$
   - $$13^2 = 169 \equiv 4 \pmod{55}$$
   - $$13^4 \equiv 4^2 = 16 \pmod{55}$$
   - $$13^8 \equiv 16^2 = 256 \equiv 36 \pmod{55}$$
   - $$13^{16} \equiv 36^2 = 1296 = 23\cdot 55 + 31 \equiv 31 \pmod{55}$$
   Nhân các thành phần ứng với bit $$1$$ của $$27$$:
   $$
   13^{27} \equiv 31 \cdot 36 \cdot 4 \cdot 13 \pmod{55}.
   $$
   Tính gọn từng cặp: $$31 \cdot 36 = 1116 \equiv 16 \pmod{55}$$; $$4 \cdot 13 = 52 \equiv -3 \pmod{55}$$; cuối cùng $$16 \cdot (-3) = -48 \equiv 7 \pmod{55}$$! Thu lại **chính xác $$M = 7$$**! ✓

### Khung giải thích: Tại sao HTTPS ngoài đời thực lại kết hợp CẢ RSA/ECC lẫn AES? (nên đọc chậm)

#### Bước 1: Dùng mật mã khóa công khai (RSA/ECC) để giải bài toán trao đổi khóa & xác thực
Trong bước bắt tay TLS, máy chủ dùng chứng chỉ số (chữ ký công khai) chứng minh danh tính, và hai bên thỏa thuận một **khóa phiên bí mật tạm thời** (session key).

#### Bước 2: Chuyển sang mật mã đối xứng (AES-GCM) để mã hóa toàn bộ lưu lượng
Phép lũy thừa modulo 2048-bit chậm hơn AES hàng nghìn lần; nên ngay khi có khóa phiên chung, toàn bộ video/dữ liệu được mã hóa bằng AES ở tốc độ gigabit/giây!

#### Bước 3: Không bao giờ dùng "Textbook RSA" trần trụi
RSA nguyên bản có tính tất định (cùng $$M$$ luôn ra cùng $$C$$) và tính nhân ($$(M_1M_2)^e = M_1^e M_2^e$$); thực tế bắt buộc thêm đệm ngẫu nhiên **OAEP** (khi mã hóa) và **PSS** (khi ký số).

#### Bước 4: Hướng tới tương lai Hậu lượng tử (bài 15.06)
Thuật toán Shor trên máy tính lượng tử quy mô lớn có thể phân tích $$n = pq$$ trong thời gian đa thức — thúc đẩy quá trình chuyển đổi sang chuẩn hậu lượng tử NIST 2024!

$$
(p, q) \to n = pq,\; ed \equiv 1 \pmod{\varphi(n)}
\;\xrightarrow{\;C = M^e \bmod n\;}\;
\text{Bản mã }C
\;\xrightarrow{\;C^d \bmod n\;}\;
M.
$$

## Hệ mật mã

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Một **hệ mật mã** gồm thuật toán **mã hóa** $$E$$ và thuật toán **giải mã** $$D$$ tác động lên bản rõ (*plaintext*) và bản mã (*ciphertext*), được điều khiển bởi **khóa**. Mục tiêu là chỉ bên nắm giữ khóa hợp lệ mới khôi phục được nội dung ban đầu.

- **Đối xứng** (*symmetric*): dùng chung một khóa bí mật $$K$$ cho cả $$E_K$$ và $$D_K$$ (ví dụ AES, ChaCha20).
- **Bất đối xứng** (*asymmetric*): sử dụng cặp khóa $$(K_{\mathrm{pub}}, K_{\mathrm{priv}})$$; thông thường mã hóa bằng khóa công khai và giải mã bằng khóa riêng (ví dụ RSA).

</div>

| Mục tiêu | Ý nghĩa |
|:---|:---|
| **Confidentiality (Bí mật)** | Bên ngoài không đọc được nội dung |
| **Integrity (Toàn vẹn)** | Phát hiện được sự sửa đổi dữ liệu (hash, MAC) |
| **Authentication (Xác thực)** | Xác minh nguồn gốc thông điệp (chữ ký số) |

## Mã hóa cổ điển

<div class="textbook-definition" markdown="1">

**Định nghĩa** (Caesar). Với bảng chữ cái được đánh số từ $$0$$ đến $$25$$ và khóa dịch chuyển $$k$$:

$$
E(x) = (x+k)\bmod 26, \qquad D(y) = (y-k)\bmod 26.
$$

</div>

<div class="textbook-definition" markdown="1">

**Định nghĩa** (Affine). Với tham số khóa $$(a,b)$$ thỏa mãn $$\gcd(a,26)=1$$:

$$
E(x)=(ax+b)\bmod 26, \qquad D(y) = a^{-1}(y-b)\bmod 26.
$$

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 1.** Với mã Caesar khóa $$k=3$$, chuỗi `HELLO` được mã hóa thành `KHOOR`. Vì chỉ có 26 khóa khả dĩ nên mã này dễ dàng bị phá bằng cách thử vét cạn (*brute-force*), cho thấy sự cần thiết của không gian khóa đủ lớn.

</div>

### Video ngắn: RSA và Diffie–Hellman

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/rsa-diffie-hellman.mp4"></video>
</div>

Video dài khoảng 3 phút 22 giây: minh họa Diffie–Hellman qua hình ảnh trộn màu rồi tính bằng số ($$p = 23$$, $$g = 5$$, hai bên cùng thu được khóa chung $$K = 2$$) và bài toán logarit rời rạc; triển khai ví dụ RSA với $$p = 61$$, $$q = 53$$ ($$n = 3233$$, $$\varphi(n) = 3120$$, $$e = 17$$, tìm $$d = 2753$$ bằng thuật toán Euclid mở rộng), mã hóa $$M = 123$$ thành $$C = 855$$ bằng bình phương liên tiếp rồi giải mã lại 123, giải thích cơ sở đúng đắn từ định lý Euler và nền tảng bảo mật của RSA.

## Hệ mật RSA

**Bài toán trao đổi khóa.** Mã hóa đối xứng đòi hỏi hai bên phải chia sẻ trước cùng một khóa bí mật $$K$$, điều rất khó thực hiện qua kênh truyền có thể bị nghe lén. Mã hóa khóa công khai giải quyết vấn đề này bằng cách cho phép công bố rộng rãi $$K_{\mathrm{pub}}$$ và chỉ giữ bí mật $$K_{\mathrm{priv}}$$.

<div class="textbook-definition" markdown="1">

**Định nghĩa** (RSA — Rivest, Shamir, Adleman, 1977). Hệ mật bất đối xứng dựa trên độ khó của bài toán **phân tích thừa số nguyên tố**. Khóa công khai là $$(n,e)$$ và khóa riêng là $$d$$ thỏa mãn $$ed \equiv 1 \pmod{\varphi(n)}$$.

</div>

**Quy trình tạo khóa**

1. Chọn hai số nguyên tố lớn $$p,q$$.
2. Tính $$n = pq$$ và $$\varphi(n)=(p-1)(q-1)$$.
3. Chọn số mũ công khai $$e$$ sao cho $$\gcd(e,\varphi(n))=1$$ (thường chọn $$e=65537$$).
4. Tính $$d = e^{-1} \bmod \varphi(n)$$ bằng thuật toán Euclid mở rộng.
5. Công khai $$(n,e)$$ và giữ bí mật $$d$$ (cùng với $$p,q$$).

**Mã hóa và giải mã** (với thông điệp $$0 \le M < n$$):

$$
C \equiv M^e \pmod n, \qquad M \equiv C^d \pmod n.
$$

<div class="textbook-theorem" markdown="1">

**Định lý** (Tính đúng đắn của RSA). Nếu $$ed \equiv 1 \pmod{\varphi(n)}$$ và $$\gcd(M,n)=1$$ thì $$C^d \equiv M^{ed} \equiv M \pmod n$$ nhờ định lý Euler $$M^{\varphi(n)}\equiv 1 \pmod n$$. (Kết quả này cũng mở rộng được cho mọi $$M$$ khi $$n=pq$$ là tích hai số nguyên tố phân biệt.)

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2** (Số nhỏ). Chọn $$p=61$$, $$q=53$$, ta có $$n=3233$$ và $$\varphi(n)=3120$$. Chọn $$e=17$$, tính được $$d=2753$$.  
Với thông điệp $$M=123$$: bản mã là $$C = 123^{17}\bmod 3233 = 855$$; khi giải mã bằng $$855^{2753}\bmod 3233$$, ta khôi phục đúng $$M=123$$.

</div>

**Giả thuyết bảo mật.** Từ khóa công khai $$(n,e)$$, việc suy ra khóa riêng $$d$$ về thực chất đòi hỏi phân tích $$n=pq$$ — bài toán được tin là rất khó với kích thước $$n$$ từ 2048 bit trở lên trên máy tính cổ điển. Tuy nhiên, thuật toán Shor trên máy tính lượng tử có thể đe dọa tính an toàn của RSA (xem Mục 15.4).

### Thử nghiệm: kiểm tra nguyên tố Miller–Rabin

Tìm nhân chứng cho hợp số, quan sát số Carmichael và các cơ sở “nói dối”:

<div class="interactive-demo" markdown="1">
<div data-demo="crypto-explainer" data-tab="miller" data-n="561" data-a="2"></div>
</div>

## Trao đổi khóa Diffie–Hellman

![Diffie–Hellman](/discrete-mathematics-for-computer-science-iuh/img/course/Number_diffie_hellman.svg)

<p class="textbook-figure-caption" data-figure="15.6">Hai bên tính ra cùng một khóa chung $$K = g^{ab}\bmod p$$ mà không cần gửi trực tiếp $$a$$ hay $$b$$.</p>

<div class="textbook-definition" markdown="1">

**Định nghĩa** (Diffie–Hellman, 1976). Giao thức trao đổi khóa trên kênh công khai sử dụng tham số công khai gồm số nguyên tố $$p$$ và phần tử sinh $$g$$. Alice giữ bí mật $$a$$ và gửi $$A=g^a\bmod p$$; Bob giữ bí mật $$b$$ và gửi $$B=g^b\bmod p$$; cả hai bên cùng tính được khóa chung $$K=g^{ab}\bmod p$$. Độ an toàn của giao thức dựa trên giả thuyết bài toán **logarit rời rạc** (DLP) là khó giải.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 3.** Cho $$p=23$$, $$g=5$$, $$a=6$$ và $$b=15$$.  
Ta có $$A=5^6\bmod 23=8$$ và $$B=5^{15}\bmod 23=19$$.  
Cả hai tính khóa chung: $$K=19^6\bmod 23=2$$ và $$K=8^{15}\bmod 23=2$$.

</div>

### Thử nghiệm: trao đổi khóa Diffie–Hellman

Mô phỏng Alice, Bob và Eve với $$p$$ nhỏ: hai bên thu được cùng một khóa chung trong khi Eve phải dò bài toán logarit rời rạc.

<div class="interactive-demo" markdown="1">
<div data-demo="crypto-explainer" data-tab="dh"></div>
</div>

## Chữ ký số

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Trong **chữ ký số**, người gửi ký thông điệp bằng khóa **riêng** $$S=\mathrm{Sign}(M,K_{\mathrm{priv}})$$ và người nhận xác minh bằng khóa **công khai**. Mục tiêu của chữ ký số là đảm bảo **nguồn gốc** và **tính toàn vẹn**, không nhất thiết che giấu nội dung thông điệp.

</div>

Với RSA (ở mô hình đơn giản), chữ ký được tính bằng $$S \equiv M^d \pmod n$$ và xác minh bằng cách kiểm tra $$S^e \equiv M \pmod n$$. Trong thực tế, người ta ký lên **giá trị băm** (như SHA-256) của tài liệu thay vì ký trực tiếp lên tệp kích thước lớn.

## Thử nghiệm tương tác

<div class="interactive-demo" markdown="1">
<div data-demo="rsa-simulator"></div>
</div>
<script src="{{ '/public/js/rsa-simulator.js' | relative_url }}"></script>

### Minh họa tương tác

Minh họa RSA trên số nhỏ: tạo khóa, mã hóa và giải mã từng bước.

<div class="interactive-demo" markdown="1">
<div data-demo="numtheory-explainer" data-tab="rsa"></div>
</div>
<script src="{{ '/public/js/explainers/numtheory-explainer.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Mã hóa chuỗi `MATH` bằng mã Caesar với khóa $$k=5$$.

<details>
<summary>Đáp án</summary>

Dịch mỗi chữ cái tiến 5 vị trí: M → R, A → F, T → Y, H → M. Bản mã thu được là **RFYM**.

</details>

### Bài tập 2

Với mã Affine có $$a=7$$, $$b=3$$, hãy nêu công thức giải mã (tìm nghịch đảo của 7 modulo 26).

<details>
<summary>Đáp án</summary>

Vì $$7\cdot 15=105\equiv 1\pmod{26}$$ nên $$a^{-1}\equiv 15 \pmod{26}$$.  
Công thức giải mã là $$D(y)=15(y-3)\bmod 26$$.

</details>

### Bài tập 3

Cho $$p=3$$, $$q=11$$, $$e=7$$. Tính $$n$$, $$\varphi(n)$$, $$d$$ và mã hóa thông điệp $$M=5$$.

<details>
<summary>Đáp án</summary>

Ta có $$n=33$$, $$\varphi(n)=20$$ và $$d=3$$ (vì $$7\cdot 3=21\equiv 1\pmod{20}$$).  
Tính bản mã $$C=5^7\bmod 33$$ từng bước: $$5^1=5$$, $$5^2=25$$, $$5^3=125\equiv 26$$, $$5^4\equiv 26\cdot 5=130\equiv 31$$, $$5^5\equiv 31\cdot 5=155\equiv 23$$, $$5^6\equiv 23\cdot 5=115\equiv 16$$, $$5^7\equiv 16\cdot 5=80\equiv 14 \pmod{33}$$.  
Vậy $$C = 14$$.

</details>

### Bài tập 4

Trong giao thức Diffie–Hellman với $$p=29$$, $$g=2$$, $$a=12$$ và $$b=8$$, hãy tính $$A$$, $$B$$ và khóa chung $$K$$.

<details>
<summary>Đáp án</summary>

Ta có $$A=2^{12}\bmod 29=7$$ và $$B=2^8\bmod 29=24$$.  
Khóa chung là $$K=B^{12}\bmod 29=A^8\bmod 29=7$$ (vì $$7^2=49\equiv 20$$, $$7^4\equiv 400\equiv 23\equiv -6$$, suy ra $$7^8\equiv 36\equiv 7 \pmod{29}$$).

</details>

### Bài tập 5

Eve chặn được bản mã $$C=15$$ cùng khóa công khai $$(n,e)=(33,7)$$. Hãy phân tích $$n$$, tìm khóa riêng $$d$$ và giải mã bản rõ $$M$$.

<details>
<summary>Đáp án</summary>

Phân tích $$33=3\cdot 11$$, suy ra $$\varphi(33)=20$$ và $$d=3$$.  
Giải mã $$M=15^3\bmod 33$$: ta có $$15^2=225\equiv 27$$, nên $$15^3\equiv 27\cdot 15=405\equiv 9\pmod{33}$$.  
Vậy $$M=9$$. Ví dụ này cho thấy với $$n$$ nhỏ, RSA không an toàn.

</details>

## Tóm tắt

1. Phân biệt mã hóa đối xứng và bất đối xứng cùng ba mục tiêu CIA ở mức khái niệm.
2. Mã Caesar và Affine hoạt động trên modulo 26 với không gian khóa nhỏ.
3. **RSA**: dùng khóa $$(n,e)$$ và $$d$$; định lý Euler đảm bảo tính đúng đắn, còn độ an toàn dựa trên bài toán phân tích thừa số.
4. **Diffie–Hellman**: trao đổi khóa chung $$g^{ab}\bmod p$$; độ an toàn dựa trên bài toán logarit rời rạc (DLP).
5. **Chữ ký số**: ký bằng khóa riêng và xác minh bằng khóa công khai.

Trong bài tiếp theo, ta sẽ tìm hiểu về hàm băm mật mã, PRNG, kỹ thuật dùng CRT tăng tốc RSA, ECC và mật mã hậu lượng tử.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=GSIDS_lvRv4">Public Key Cryptography - Computerphile</a> — Computerphile, tiếng Anh. Giới thiệu về mật mã khóa công khai trước khi đi vào từng thuật toán cụ thể.
- <a href="https://www.youtube.com/watch?v=JD72Ry60eP4">Prime Numbers &amp; RSA Encryption Algorithm - Computerphile</a> — Computerphile, tiếng Anh. Giải thích RSA từ số nguyên tố và lũy thừa modulo, sát trọng tâm bài học.
- <a href="https://www.youtube.com/watch?v=4zahvcJ9glg">The RSA Encryption Algorithm (1 of 2: Computing an Example)</a> — Eddie Woo, tiếng Anh. Minh họa một ví dụ RSA tính tay từng bước.
