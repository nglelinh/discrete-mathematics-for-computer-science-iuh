---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Phép đếm: Từ Cờ bạc đến An ninh mạng

**Toán Rời Rạc**

Tiết 22 (45 phút) — ch07 `07_06`, ch08 `08_03`

*Bài học: [`07_06`](https://nglelinh.github.io/discrete-mathematics-for-computer-science-iuh/contents/chapter07/21/01/01/Counting_from_Gambling_to_Cybersecurity.html) · [`08_03`](https://nglelinh.github.io/discrete-mathematics-for-computer-science-iuh/contents/chapter08/21/01/01/Pigeonhole_Principle_in_Computing.html)*

---

## Mục tiêu tiết học

- Đếm **không gian mật khẩu** ($$36^{8}$$, $$77^{8}$$), **PIN** ($$10^{6}$$), **mã email** ($$36^{6}$$)
- Ước lượng **brute-force** theo **hash × phần cứng**; online vs offline
- Rủi ro **Session ID** / **CSRF** collision
- Phân biệt **chuồng bồ câu** (đảm bảo) và **birthday paradox** (xác suất)
- Liên hệ đếm với **Big-O** và kiểm thử tổ hợp

---

## Bit vector — Định nghĩa

$$U=\{1,2,\ldots,n\}$$ cố định thứ tự.

Bit $$i$$ là **1** ⟺ $$i\in B$$.

---

## Bit vector — Ví dụ

$$U=\{1,\ldots,8\}$$, vector `01101010`:

$$B=\{2,3,5,7\}$$

$$A$$ = số chẵn → $$A\cap B = \{2\}$$

---

## Lũy thừa và nhị thức

$$|\mathcal{P}(A)| = 2^{|A|}$$

---

## Mã đa định dạng — Ý tưởng

Mã gồm $$k$$ ký tự, **nhiều định dạng** (tiết 16).

Mỗi **nhánh** nhân độc lập → các nhánh **cộng**.

---

## Ví dụ SKU: Loại P

Mã **SKU** 6 ký tự — **Physical**:

2 chữ (A–Z) + 4 số → $$26^{2}\times 10^{4} = 676{,}000$$

---

## Ví dụ SKU: Loại D & Tổng

**Digital**: 6 số → $$10^{6} = 1{,}000{,}000$$

**Tổng**: $$676{,}000 + 1{,}000{,}000 = 1{,}676{,}000$$

---

## Pascal, Fermat và phép đếm

Năm **1654**, Pascal và Fermat — bài toán **chia tiền cược**.

Trong CNTT, phép đếm trả lời:

> **"Vấn đề lớn đến mức nào?"**

---

## Blaise Pascal

![Blaise Pascal](../img/course/Blaise_Pascal_Versailles.JPG)

*Hình 7.25 — Từ cờ bạc đến an ninh hiện đại.*

---

## Pierre de Fermat

![Pierre de Fermat](../img/course/Pierre_de_Fermat.jpg)

*Hình 7.26 — Đồng sáng lập xác suất.*

---

## Không gian mật khẩu

Mật khẩu dài $$n$$, mỗi vị trí $$a$$ lựa chọn:

$$|\text{Passwords}| = a^{n}$$

---

## Ví dụ: $$36^{8}$$ và $$77^{8}$$

| Policy | Không gian 8 ký tự | Entropy |
|:---|:---|:---:|
| Chữ thường + số ($$a=36$$) | $$\approx 2.8 \times 10^{12}$$ | $$\approx 41$$ bit |
| + Hoa + ký hiệu ($$a=77$$) | $$\approx 1.2 \times 10^{15}$$ | $$\approx 51$$ bit |

---

## Brute-force mật khẩu

$$T \approx \dfrac{a^{n} / 2}{R}$$ — $$R$$ = lần **thử hash**/giây.

Trung bình tìm được sau **một nửa** không gian $$a^{n}$$.

**Giả định**: hash DB bị lộ (offline); mật khẩu ngẫu nhiên đều.

---

## Tốc độ $$R$$ — hash quan trọng hơn CPU

Cùng GPU, **MD5** nhanh hơn **bcrypt** hàng **nghìn lần**.

| Hash | Ý nghĩa |
|:---|:---|
| MD5 / SHA-1 | Yếu — chỉ đo tốc độ phần cứng |
| bcrypt / Argon2 | Chậm cố ý — bảo vệ thực tế |

$$R$$ thay đổi theo **thuật toán × phần cứng × cost factor**.

---

## Cấu hình tham chiếu (2024–2025)

Ước lượng từ hashcat / Hive Systems (làm tròn dạy học):

| Cấu hình | MD5 | bcrypt cost=10 |
|:---|:---:|:---:|
| Laptop CPU (4 nhân) | $$\sim 10^{8}$$/s | $$\sim 10^{3}$$/s |
| GPU RTX 3060 | $$\sim 5 \times 10^{10}$$/s | $$\sim 5 \times 10^{4}$$/s |
| GPU RTX 4090 | $$\sim 1.5 \times 10^{11}$$/s | $$\sim 2 \times 10^{5}$$/s |
| Cụm 8× GPU (cloud) | $$\sim 10^{12}$$/s | $$\sim 10^{6}$$/s |

---

## Thời gian crack $$36^{8}$$ (offline)

Không gian $$\approx 2.8 \times 10^{12}$$; một nửa $$\approx 1.4 \times 10^{12}$$.

| Cấu hình | Hash | $$T$$ (ước lượng) |
|:---|:---|:---:|
| Laptop CPU | MD5 | **~4 giờ** |
| RTX 4090 | MD5 | **~10 giây** |
| Cụm 8× GPU | MD5 | **~1.5 giây** |
| Laptop CPU | bcrypt-10 | **~45 năm** |
| RTX 4090 | bcrypt-10 | **~80 ngày** |

---

## Thời gian crack $$77^{8}$$ (offline)

Không gian $$\approx 1.2 \times 10^{15}$$; một nửa $$\approx 6 \times 10^{14}$$.

| Cấu hình | Hash | $$T$$ (ước lượng) |
|:---|:---|:---:|
| RTX 4090 | MD5 | **~1 giờ** |
| Cụm 8× GPU | MD5 | **~10 phút** |
| RTX 4090 | bcrypt-10 | **~95 năm** |
| Laptop CPU | bcrypt-10 | **~19 000 năm** |

Policy mạnh hơn $$\Rightarrow$$ không gian lớn hơn **~430×** so $$36^{8}$$.

---

## Cách tính nhanh trên slide

Ví dụ: $$36^{8}$$, RTX 4090 + MD5, $$R = 1.5 \times 10^{11}$$/s:

$$T \approx \dfrac{1.4 \times 10^{12}}{1.5 \times 10^{11}} \approx 9.3\ \text{giây}$$

Đổi sang bcrypt-10 ($$R \approx 2 \times 10^{5}$$):

$$T \approx \dfrac{1.4 \times 10^{12}}{2 \times 10^{5}} \approx 7 \times 10^{6}\ \text{s} \approx 80\ \text{ngày}$$

---

## Online vs offline

| Kiểu tấn công | $$R$$ thực tế | $$36^{8}$$ |
|:---|:---:|:---|
| Form login (rate limit) | $$\sim 1$$–$$10$$/s | Không khả thi |
| API không khóa | $$\sim 10^{3}$$/s | Vẫn quá lớn |
| DB leak + MD5 + GPU | $$\sim 10^{11}$$/s | **Phút / giây** |
| DB leak + bcrypt + GPU | $$\sim 10^{5}$$/s | **Tháng / năm** |

**Bài học**: đếm $$a^{n}$$ + chọn hash + giới hạn online.

---

## Mã PIN 6 số (ATM, 2FA SMS)

$$a=10$$, $$n=6$$ → $$10^{6} = 1{,}000{,}000$$ khả năng.

Entropy $$\approx 6\log_2 10 \approx 20$$ bit — **rất thấp**.

---

## PIN — Brute-force

Không khóa, $$R \approx 3.3 \times 10^{3}$$/s:

$$T \approx \dfrac{10^{6}/2}{R} \approx 2.5$$ phút (một nửa); **~5 phút** toàn không gian.

ATM/SMS thường **khóa 3–5 lần sai** — bù cho $$10^{6}$$ nhỏ.

---

## Mã xác nhận email (base36)

6 ký tự `0-9a-z` → $$a=36$$, $$n=6$$:

$$36^{6} = 2{,}176{,}782{,}336 \approx 2.2 \times 10^{9}$$

Entropy $$\approx 6\log_2 36 \approx 31$$ bit.

---

## PIN vs mã email

| | PIN 6 số | Mã email base36 |
|:---|:---:|:---:|
| Không gian | $$10^{6}$$ | $$\approx 2.2 \times 10^{9}$$ |
| Entropy | $$\approx 20$$ bit | $$\approx 31$$ bit |
| Bảo vệ thực tế | Khóa sau N lần sai | TTL + one-time use |

Mã email lớn hơn PIN **~2200×** — vẫn << $$36^{8}$$ mật khẩu.

---

## Mật khẩu có điều kiện

Yêu cầu **ít nhất 2** trong 4 loại ký tự → dùng **bù trừ** (tiết 19):

$$\text{Hợp lệ} = 77^{n} - \text{(chỉ 1 loại)} - \text{(chỉ 2 loại)}$$

Chỉ 1 loại: $$10^{n} + 2\cdot26^{n} + 15^{n}$$.

**Bài học**: quy tắc phức tạp ≠ chỉ $$a^{n}$$.

---

## Entropy và ngữ cảnh thực tế

$$H \approx n \log_2 a$$ bit (mật khẩu ngẫu nhiên đều).

Từ điển, pattern → không gian **thực** << $$a^{n}$$.

GPU, hashing, rate limit quan trọng hơn con số lý thuyết.

---

## Session ID — Bài toán

Cookie / Redis map **user ↔ trạng thái**.

Mỗi session = một giá trị từ không gian $$N = 2^{b}$$.

Collision → hai user **cùng key** → hijack session.

---

## Session ID — Collision

| Công cụ | Điều kiện |
|:---|:---|
| Chuồng bồ câu | > $$N$$ session → **chắc chắn** trùng |
| Birthday | ~$$\sqrt{N}$$ session → ~50% có cặp trùng |

64-bit → ~$$2^{32}$$ session; 128-bit → ~$$2^{64}$$.

---

## Session ID — Code

```python
import secrets
session_id = secrets.token_hex(16)  # 128 bit
```

**Không** dùng `Math.random()`, timestamp, `userId` làm ID.

---

## CSRF token — Bài toán

Token gắn form → server biết request từ **trang hợp lệ**.

Cũng chọn từ không gian $$N$$; thường lưu trong session.

---

## CSRF token — Collision

Token **6 số** ($$N=10^{6}$$): ~1000 form → birthday risk cao.

Token **128-bit**: $$k=10^{6}$$ form → $$P \approx k^{2}/2^{129}$$ ≈ 0.

**Không** reuse token yếu cho mọi form.

---

## Mật khẩu vs Token

| | Mật khẩu | Session / CSRF |
|:---|:---|:---|
| Mối quan tâm | Brute-force $$a^{n}$$ | Collision, entropy thấp |
| Công cụ | Nhân, bù trừ | Dirichlet, birthday |

---

## Đếm phép toán → Big-O

```python
for i in range(n):
    for j in range(n):
        total += 1  # n^{2} lần
```

Big-O từ **đếm thao tác** — quy tắc nhân (tiết 16).

---

## So sánh độ phức tạp (1/2)

![So sánh độ phức tạp](../img/course/Comparison_computational_complexity.svg)

*Hình 7.28 — Đếm thao tác → hiểu scale.*

---

## So sánh độ phức tạp (2/2)

![Các lớp phức tạp](../img/course/Complexity_classes.svg)

*Hình 7.29 — $$n\log n$$ vs $$n^{2}$$.*

---

## Hash Collision: Hai góc nhìn

| Khái niệm | Công cụ | Khi nào |
|:---|:---|:---|
| **Đảm bảo** collision | Chuồng bồ câu | > $$2^{b}$$ input, không gian $$2^{b}$$ |
| **Xác suất** collision | Birthday paradox | ~$$\sqrt{2^{b}}$$ input → ~50% |

![Hash collision](../img/course/Pigeonhole.jpg)

*Hình 8.12 — Nhiều input hơn output → collision tất yếu.*

---

## Birthday Paradox

**23** người → xác suất 2 người **cùng sinh nhật** > 50%.

$$P \approx 1 - e^{-n^{2}/(2d)}, \quad d=365$$

Trong hash: collision **sớm hơn** trực giác (~$$\sqrt{N}$$).

![Birthday paradox](../img/course/Birthdaymatch.svg)

*Hình 7.30 / 8.14 — Va chạm sớm hơn dự đoán.*

---

## Birthday Attack

Tìm 2 input **cùng hash** (collision), không cần đảo ngược.

- Preimage brute-force: ~$$2^{b}$$ thử
- Birthday collision: ~$$2^{b/2}$$ thử

**MD5 (128 bit)**: birthday ~$$2^{64}$$ — đã bị khai thác thực tế.

---

## Nén lossless — Giới hạn logic

Không thể nén **mọi** file 1KB thành file **nhỏ hơn** 1KB mà vẫn giải nén đúng.

Số file 1KB = $$2^{8192}$$ >> số file ngắn hơn → không ánh xạ song ánh.

![Quá nhiều file](../img/course/TooManyPigeons.jpg)

*Hình 8.13 — Chuồng chim đặt giới hạn nén.*

---

## Phát hiện lỗi (Parity)

Thêm **parity bit** — tổng bit 1 chẵn/lẻ.

Số thông điệp nhận >> số mã hợp lệ → không phân biệt mọi lỗi hoàn hảo.

Nguyên lý chuồng chim: giới hạn số pattern lỗi phân biệt được với bit kiểm tra hữu hạn.

![Coding theory](../img/course/Decision_tree.svg)

*Hình 8.15 — Giới hạn coding theory.*

---

## Kiểm thử tổ hợp

5 tính năng × 2 trạng thái → test đầy đủ: $$2^{5}=32$$ ca.

**Pairwise**: mọi cặp 2 tính năng — $$\binom{5}{2}=10$$ cặp × $$2^{2}=4$$ → **40** tổ hợp cần bao phủ.

**Covering array**: bộ test nhỏ hơn nhiều, vẫn bao phủ tương tác 2 chiều.

---

## Bài tập 1: Mật khẩu

8 ký tự, chữ thường hoặc số ($$a=36$$). Bao nhiêu mật khẩu?

---

## Đáp án — Bài tập 1

$$36^{8} = 2{,}821{,}109{,}907{,}456 \approx 2.8 \times 10^{12}$$

---

## Bài tập 2: Birthday

Vì sao **23** người đã ~50% cùng sinh nhật?

---

## Đáp án — Bài tập 2

$$1-e^{-23^{2}/(2\cdot365)}\approx 0.51$$

So sánh **cặp** $$\binom{23}{2}$$, không chỉ 23/365.

---

## Bài tập 3: Kiểm thử

5 tính năng, 2 lựa chọn. Test tất cả tổ hợp **2** tính năng?

---

## Đáp án — Bài tập 3

$$\binom{5}{2}\times 4=40$$ test case

---

## Bài tập 4: Hash (08_03)

Hash **32-bit**. Ít nhất bao nhiêu input để **chắc chắn** va chạm?

---

## Đáp án — Bài tập 4

$$2^{32}+1$$ (chuồng bồ câu)

---

## Bài tập 5: Entropy

So sánh entropy (bit) mật khẩu 8 ký tự: $$a=36$$ vs $$a=77$$?

---

## Đáp án — Bài tập 5

$$8\log_2 36 \approx 41.4$$ bit · $$8\log_2 77 \approx 50.6$$ bit

Chênh ~9 bit ≈ gấp $$2^{9} \approx 512$$ lần không gian.

---

## Bài tập 6: Session 64-bit

ID 64-bit random. ~Bao nhiêu session → birthday ~50%?

---

## Đáp án — Bài tập 6

$$\sqrt{2^{64}} = 2^{32} \approx 4 \times 10^{9}$$ session.

---

## Bài tập 7: CSRF yếu

Token 6 số ($$N=10^{6}$$), 500 form đồng thời. $$P$$ collision?

---

## Đáp án — Bài tập 7

$$P \approx \binom{500}{2}/10^{6} \approx 0.12$$ (12%) — không dùng production.

---

## Bài tập 8: PIN ATM

PIN 6 số, không khóa, $$R = 3.3 \times 10^{3}$$/s.

Thời gian brute-force trung bình (một nửa $$10^{6}$$)?

---

## Đáp án — Bài tập 8

$$T \approx \dfrac{5 \times 10^{5}}{3.3 \times 10^{3}} \approx 150$$ s ≈ **2.5 phút**.

Toàn $$10^{6}$$ → **~5 phút**; ATM khóa sau vài lần sai.

---

## Bài tập 9: Mã email base36

6 ký tự base36: không gian? entropy? Lớn hơn PIN 6 số bao nhiêu lần?

---

## Đáp án — Bài tập 9

$$36^{6} \approx 2.2 \times 10^{9}$$; $$H \approx 31$$ bit.

$$36^{6}/10^{6} \approx 2177$$ — lớn hơn PIN **~2200×**.

---

## Bài tập 10: Brute-force thực tế

Mật khẩu $$36^{8}$$, hash MD5, GPU RTX 3060 ($$R \approx 5 \times 10^{10}$$/s).

Ước lượng $$T$$ (một nửa không gian)?

---

## Đáp án — Bài tập 10

$$T \approx \dfrac{1.4 \times 10^{12}}{5 \times 10^{10}} \approx 28\ \text{giây}$$

Cùng mật khẩu + **bcrypt-10** ($$R \approx 5 \times 10^{4}$$/s) → **~330 ngày**.

---

## Bản đồ kỹ năng (1/2)

| Dạng bài | Tiết | Công cụ |
|:---|:---:|:---|
| Chọn / xếp không lặp | 17 | $$P$$, $$C$$, bù |
| Chọn có lặp | 18 | Stars and bars |
| Khảo sát nhiều tập | 19 | Bao hàm–loại trừ |

---

## Bản đồ kỹ năng (2/2)

| Dạng bài | Tiết | Công cụ |
|:---|:---:|:---|
| Hệ số khai triển | 20 | $$\binom{n}{k}\alpha^{a}\beta^{b}$$ |
| Tải tối thiểu | 21 | $$\lceil N/n\rceil$$ |
| Mã, bit, scale | 22 | Nhân, $$2^{n}$$ |

**Luyện tập**: đổi ngữ cảnh và số — không học thuộc một đề.

---

## Tóm tắt Tiết 22 (1/2)

- **Brute-force**: $$T \approx (a^{n}/2)/R$$; MD5+GPU **giây–phút**; bcrypt **tháng–năm**
- **Mật khẩu / PIN / OTP**: $$36^{8}$$, $$10^{6}$$, $$36^{6}$$; $$H \approx n\log_2 a$$
- **Session / CSRF**: $$2^{b}$$; Dirichlet + birthday ~$$\sqrt{N}$$
- **Bit vector** ↔ $$2^{|A|}$$; SKU → cộng + nhân

---

## Tóm tắt Tiết 22 (2/2)

- **Pigeonhole**: hash collision **chắc chắn**
- **Birthday attack**: ~$$2^{b/2}$$ trên hash $$b$$ bit
- **Big-O**, kiểm thử tổ hợp, nén, parity

---

## Liên hệ chương trình

| Tiết | Bài | Nội dung |
|:---:|:---|:---|
| 16–20 | ch07 | Công cụ đếm nền |
| 21 | `08_01`–`08_02` | Dirichlet chứng minh tồn tại |
| **22** | `07_06`, `08_03` | Ứng dụng bảo mật, scale, kiểm thử |
| 38–39 | — | Big-O chính thức |

---

## Kết luận Tiết 22

Hệ thống thất bại vì không ai hiểu **không gian trường hợp** lớn đến mức nào.
