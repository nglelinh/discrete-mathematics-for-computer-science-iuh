---

layout: post
title: "Phép đếm: Từ Cờ bạc đến An ninh mạng"
categories: chapter07
date: 2021-01-01
order: 6
required: false
lang: en
excerpt: "Ở các mục trước chúng ta đã xây dựng bộ công cụ tổ hợp cơ bản. Mục bổ sung này trình bày ứng dụng của phép đếm từ nguồn gốc lịch sử đến an ninh mạng và phân…"
---

Ở các mục trước chúng ta đã xây dựng bộ công cụ tổ hợp cơ bản. Mục bổ sung này trình bày ứng dụng của phép đếm từ nguồn gốc lịch sử đến an ninh mạng và phân tích độ phức tạp.

Động lực ban đầu của xác suất và phép đếm đến từ các bài toán cờ bạc thế kỷ XVII; từ đó, ý tưởng đếm khả năng đã trở thành công cụ đánh giá độ mạnh mật khẩu, ước lượng xác suất va chạm và thiết kế test suite hiệu quả. Phép đếm không chỉ trả lời "có bao nhiêu cách" mà còn trả lời "vấn đề lớn đến mức nào".

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
chúng ta phải đếm rõ ràng.
Đó là tinh thần mà khoa học máy tính sau này thừa hưởng trọn vẹn.

![Blaise Pascal — nhà toán học Pháp](/discrete-mathematics-for-computer-science-iuh/img/course/Blaise_Pascal_Versailles.JPG)

<p class="textbook-figure-caption" data-figure="7.25">Blaise Pascal — từ bàn cờ bạc đến lý thuyết đếm, một câu hỏi thực tế đã khai sinh nhiều ý tưởng nền cho khoa học dữ liệu và an ninh hiện đại.</p>
![Pierre de Fermat — đồng sáng lập xác suất](/discrete-mathematics-for-computer-science-iuh/img/course/Pierre_de_Fermat.jpg)

<p class="textbook-figure-caption" data-figure="7.26">Pierre de Fermat — cùng Pascal trao đổi thư về bài toán chia tiền cược, mở ra xác suất và tổ hợp hiện đại.</p>
---

## Phần 2: Password security — đếm không gian khóa

### 2.1. Mật khẩu mạnh hay yếu trước hết là bài toán đếm

Mật khẩu dài $n$ ký tự, mỗi vị trí chọn độc lập từ bảng $a$ ký tự (quy tắc nhân — bài `07_01`):

<div class="textbook-equation" markdown="1">
$$
|\text{Passwords}| = a^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Ví dụ 8 ký tự** — hai policy phổ biến trong web app:

| Policy | $a$ | Không gian | Entropy $\approx n\log_2 a$ |
|:---|:---:|:---|:---|
| Chữ thường + số | 36 | $36^8 \approx 2.8 \times 10^{12}$ | $\approx 41$ bit |
| Hoa + thường + số + ký hiệu | 77 | $77^8 \approx 1.2 \times 10^{15}$ | $\approx 51$ bit |

Chỉ chữ thường: $26^8 \approx 2.1 \times 10^{11}$ ($\approx 37$ bit).

Ở đây, phép đếm không chỉ là toán — nó định lượng **chi phí brute-force** (số lần thử tối đa / trung bình).

### 2.2. Không gian lớn chưa chắc đủ lớn

Ví dụ,
`26^8` nghe có vẻ rất to.
Nhưng với GPU hiện đại và kỹ thuật cracking hiệu quả,
nó có thể vẫn chưa đủ trong nhiều bối cảnh.

Số lượng khả năng phải được đặt vào ngữ cảnh thực tế về tốc độ tấn công,
rate limiting,
hashing strategy,
và chính sách xác thực.

### 2.3. Entropy và tư duy tổ hợp

**Entropy** (bit) đo logarit cơ số 2 của không gian khả năng:

<div class="textbook-equation" markdown="1">
$$
H \approx \log_2(a^n) = n \log_2 a.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Mật khẩu ngẫu nhiên đều trên toàn bộ không gian mới đạt đúng $H$ bit; từ điển, pattern (`123456`, `password`) làm không gian **thực tế** nhỏ hơn rất nhiều.

<div class="content-box warning-box textbook-block" markdown="1">
**Cẩn thận**: Policy “ít nhất 2 trong 4 loại ký tự” **không** cho $77^8$ — phải dùng nguyên lý bù trừ (bài `07_03`). Quy tắc phức tạp $\neq$ nhân đơn giản $a^n$.
</div>

![Tam giác Pascal — không gian khóa](/discrete-mathematics-for-computer-science-iuh/img/course/Pascal_triangle.svg)

<p class="textbook-figure-caption" data-figure="7.27">Entropy mật khẩu phản ánh kích thước không gian tổ hợp cần duyệt khi brute-force.</p>
### 2.4. Ước lượng thời gian brute-force

Giả sử kẻ tấn công thử $R$ mật khẩu/giây (offline, hash yếu). Thời gian trung bình duyệt một nửa không gian:

<div class="textbook-equation" markdown="1">
$$
T \approx \frac{a^n / 2}{R}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Ví dụ** $36^8$, $R = 10^9$/s:

<div class="textbook-equation" markdown="1">
$$
T \approx \frac{1.4 \times 10^{12}}{10^9} \approx 1{,}400\ \text{s} \approx 23\ \text{phút}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Với bcrypt/Argon2, rate limiting, và salt — $R$ thực tế trên server thấp hơn nhiều; con số trên là **trần lý thuyết** khi hash bị lộ.

```python
import math
a, n = 36, 8
space = a ** n
entropy_bits = n * math.log2(a)
print(space, entropy_bits)  # ~2.8e12, ~41.4
```

### 2.5. Mã PIN và mã xác nhận email

Nhiều cơ chế xác thực hàng ngày cũng là bài toán $a^n$ — chỉ với $n$ nhỏ hơn mật khẩu web.

| Loại mã | Ngữ cảnh | $a$ | $n$ | Không gian | Entropy $\approx$ |
|:---|:---|:---:|:---:|:---|:---:|
| PIN 6 số | ATM, 2FA SMS | 10 | 6 | $10^6$ | $\approx 20$ bit |
| Mã email base36 | Xác nhận đăng ký, reset mật khẩu | 36 | 6 | $36^6 \approx 2.2 \times 10^9$ | $\approx 31$ bit |

**PIN 6 số** ($10^6 = 1{,}000{,}000$): entropy thấp — chỉ $\approx 6 \log_2 10 \approx 19.9$ bit. Nếu **không khóa** sau vài lần sai và không rate-limit chặt, kẻ tấn công có thể brute-force trực tuyến:

<div class="textbook-equation" markdown="1">
$$
T \approx \frac{10^6 / 2}{R}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Với $R \approx 3.3 \times 10^3$ lần thử/giây (API không throttle), duyệt một nửa không gian mất **khoảng 5 phút**. Thực tế ATM và SMS OTP thường **khóa sau 3–5 lần sai** hoặc giới hạn theo IP — đó là biện pháp bù cho không gian nhỏ, không phải thay thế entropy.

**Mã xác nhận email 6 ký tự base36** (chữ thường + số, `0-9a-z`):

<div class="textbook-equation" markdown="1">
$$
36^6 = 2{,}176{,}782{,}336 \approx 2.2 \times 10^9,
\qquad
H \approx 6 \log_2 36 \approx 31\ \text{bit}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Lớn hơn PIN gần $36^6 / 10^6 \approx 2{,}177$ lần — vẫn **nhỏ hơn nhiều** so với mật khẩu 8 ký tự ($36^8$). Mã email thường **hết hạn** (5–15 phút) và **dùng một lần**; rủi ro chính là lộ qua email bị compromise hoặc brute-force API yếu, không phải collision.

<div class="content-box insight-box textbook-block" markdown="1">
**So sánh nhanh**: PIN — không gian $10^6$, dễ brute-force nếu không khóa. Mã email base36 — $36^6 \approx 2.2 \times 10^9$, an toàn hơn ~2000× về không gian nhưng vẫn cần TTL + rate limit.
</div>

### 2.6. Session ID — rủi ro collision

**Session ID** là giá trị ngẫu nhiên map user ↔ trạng thái trên server (cookie `sessionid`, Redis, DB). Mỗi ID là một lựa chọn từ không gian $N = 2^b$ bit (hoặc $a^n$ nếu encoding chuỗi).

| Cách sinh | Không gian $N$ | Ghi chú |
|:---|:---|:---|
| `crypto.randomBytes(16)` (128 bit) | $2^{128}$ | Production chuẩn |
| UUID v4 (122 bit random) | $\approx 2^{122}$ | Phổ biến |
| 32-bit `rand()` / timestamp | $2^{32}$ | **Không dùng** cho session |

**Hai góc đếm** (bài `08_01`, `08_03`):

- **Chuồng bồ câu**: $> N$ session đồng thời → **chắc chắn** có hai ID trùng.
- **Birthday paradox**: chỉ cần $\approx \sqrt{N}$ session → xác suất có **cặp** trùng ~50%.

Ví dụ: ID 64-bit → ngưỡng birthday $\approx 2^{32} \approx 4 \times 10^9$. ID 128-bit → $\approx 2^{64}$ — an toàn cho web app thông thường.

**Hậu quả lập trình**: hai user cùng session key → ghi đè trạng thái → **account hijack**. Không dùng `Math.random()`, counter, hay `userId` làm session ID.

```python
# Python — đủ entropy
import secrets
session_id = secrets.token_hex(16)  # 128 bit
```

### 2.7. CSRF token — rủi ro collision

**CSRF token** gắn với form/request để server xác minh request đến từ trang hợp lệ, không phải site khác. Cũng là giá trị chọn từ không gian $N$ — thường lưu trong session hoặc ký HMAC.

| Cách làm | Rủi ro |
|:---|:---|
| `secrets.token_hex(16)` mỗi form | $N = 2^{128}$, collision không đáng lo |
| Token 6 chữ số `rand() % 10^6` | $N = 10^6$ — vài trăm form đồng thời đã có risk birthday |
| Reuse token cả phiên | Không phải bài collision ID — scope hẹp, dễ lộ qua tab cũ |

Xác suất hai token 128-bit trùng khi có $k$ form đồng thời (xấp xỉ):

<div class="textbook-equation" markdown="1">
$$
P(\text{collision}) \approx \frac{\binom{k}{2}}{2^{128}} \approx \frac{k^2}{2^{129}}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Với $k = 10^6$ request, $P$ vẫn cực nhỏ. Với $N = 10^6$ (token 6 số), $k \approx \sqrt{10^6} = 1000$ đã có nguy cơ cặp trùng đáng kể.

<div class="content-box insight-box textbook-block" markdown="1">
**So sánh nhanh**: Mật khẩu — brute-force duyệt **toàn bộ** $a^n$. Session/CSRF — attacker cần **đoán trúng một** giá trị đang active; rủi ro chính là **collision** (sinh trùng) hoặc **entropy thấp** (đoán được), không phải duyệt hết không gian.
</div>

---

## Phần 3: Đếm phép toán và Big-O

### 3.1. Thuật toán nhanh hay chậm trước hết là đếm

Trước khi có Big-O notation,
chúng ta thường bắt đầu bằng câu hỏi đơn giản hơn:
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
chúng ta khó có cảm giác đúng về độ lớn của vấn đề.

### 3.2. Từ đếm chi tiết đến asymptotic thinking

Khi input rất lớn,
chúng ta không còn quá bận tâm đến hằng số nhỏ.
Chúng ta quan tâm hàm tăng trưởng chính.

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

![So sánh các lớp độ phức tạp](/discrete-mathematics-for-computer-science-iuh/img/course/Comparison_computational_complexity.svg)

<p class="textbook-figure-caption" data-figure="7.28">Đếm thao tác là bước đầu để hiểu vì sao một thuật toán có thể thắng hay thua hoàn toàn khi dữ liệu tăng lớn.</p>
![Các lớp độ phức tạp tính toán](/discrete-mathematics-for-computer-science-iuh/img/course/Complexity_classes.svg)

<p class="textbook-figure-caption" data-figure="7.29">Big-O phản ánh hàm tăng trưởng chính — sự khác biệt giữa $n \log n$ và $n^2$ quyết định khả năng scale của hệ thống.</p>
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

![Birthday paradox — va chạm sớm hơn trực giác](/discrete-mathematics-for-computer-science-iuh/img/course/Birthdaymatch.svg)

<p class="textbook-figure-caption" data-figure="7.30">Birthday paradox minh họa vì sao hash collision xảy ra sớm hơn trực giác — chỉ cần $\sqrt{N}$ phần tử trong không gian $N$ bucket.</p>
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
chúng ta có thể tạo test suite nhỏ hơn nhiều
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

Không phải lúc nào chúng ta cũng đếm chính xác được.
Nhưng ngay cả ước lượng tổ hợp đúng
cũng đủ để cứu chúng ta khỏi nhiều quyết định ngây thơ.

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

$$36^8 \approx 2.8 \times 10^{12}$$ mật khẩu.

</details>

### Bài tập 2: Birthday paradox

Với 23 người, xác suất có ít nhất 2 người cùng sinh nhật khoảng 50%. Giải thích tại sao con số này nhỏ hơn dự đoán trực giác.

<details>
<summary>Đáp án</summary>

Sử dụng công thức xấp xỉ $$1 - e^{-n^2/2d}$$ với $$d=365$$. Với $$n=23$$ chúng ta được ~0.5.

</details>

### Bài tập 3: Kiểm thử tổ hợp

Có 5 tính năng, mỗi tính năng có 2 lựa chọn. Cần test tất cả tổ hợp 2 tính năng. Hỏi cần bao nhiêu test case?

<details>
<summary>Đáp án</summary>

Số cặp tính năng: $$\binom{5}{2} = 10$$. Mỗi cặp 4 tổ hợp → 40 test case.

</details>

### Bài tập 4: Entropy mật khẩu

So sánh entropy (bit) của mật khẩu 8 ký tự: (a) $a=36$, (b) $a=77$.

<details>
<summary>Đáp án</summary>

(a) $8 \log_2 36 \approx 41.4$ bit. (b) $8 \log_2 77 \approx 50.6$ bit. Chênh $\approx 9$ bit $\approx$ gấp $2^9 \approx 512$ lần không gian.

</details>

### Bài tập 5: Session ID

Session ID 64-bit ngẫu nhiên. Khoảng bao nhiêu session active thì xác suất collision (birthday) đáng kể (~50%)?

<details>
<summary>Đáp án</summary>

Ngưỡng birthday $\approx \sqrt{2^{64}} = 2^{32} \approx 4 \times 10^9$ session.

</details>

### Bài tập 6: CSRF token yếu

CSRF token 6 chữ số ($N = 10^6$). Có 500 form đồng thời. Xấp xỉ xác suất có hai token trùng?

<details>
<summary>Đáp án</summary>

$P \approx \binom{500}{2} / 10^6 \approx 124{,}750 / 10^6 \approx 0.12$ (12%) — quá cao cho production.

</details>

### Bài tập 7: PIN ATM

PIN 6 số ($10^6$ khả năng). Không khóa tài khoản, thử $R = 3.3 \times 10^3$ lần/giây. Ước lượng thời gian brute-force trung bình (một nửa không gian)?

<details>
<summary>Đáp án</summary>

$T \approx \dfrac{10^6/2}{3.3 \times 10^3} \approx 150$ s $\approx$ **2.5 phút** (một nửa); toàn bộ $10^6$ mất $\approx 5$ phút. Thực tế ATM khóa sau vài lần sai.

</details>

### Bài tập 8: Mã email base36

Mã xác nhận 6 ký tự base36. Tính không gian và entropy (bit). So với PIN 6 số, lớn hơn bao nhiêu lần?

<details>
<summary>Đáp án</summary>

$36^6 = 2{,}176{,}782{,}336 \approx 2.2 \times 10^9$; $H \approx 6 \log_2 36 \approx 31$ bit. Tỷ lệ $36^6 / 10^6 \approx 2{,}177$ — lớn hơn PIN gần **2200×**.

</details>

## Xem thêm / Video gợi ý

- [Permutations and Combinations](https://www.youtube.com/watch?v=1jZ5n8k0p0Q) — Khan Academy (Core counting)
- [Pigeonhole Principle](https://www.youtube.com/watch?v=0jZ5n8k0p0Q) — Numberphile (Classic examples)

## Tóm tắt

- **Mật khẩu / PIN / mã OTP**: $a^n$; entropy $\approx n\log_2 a$; PIN $10^6$ yếu nếu không khóa; mã email $36^6 \approx 2.2 \times 10^9$.
- **Session ID / CSRF**: không gian $2^b$; collision chắc chắn (Dirichlet) hoặc sớm (birthday ~$\sqrt{N}$); dùng CSPRNG đủ bit.
- Tổ hợp và xác suất là công cụ đếm rủi ro — từ mật khẩu, token web, kiểm thử đến Big-O và hash collision.
