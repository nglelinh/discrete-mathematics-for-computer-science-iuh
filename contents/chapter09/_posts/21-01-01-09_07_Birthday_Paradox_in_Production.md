---
layout: post
title: "Birthday paradox trong production: Khi ID ngẫu nhiên va chạm"
categories: chapter09
date: 2021-01-01
order: 7
required: false
lang: en
---

2 giờ 17 sáng. PagerDuty gọi.

Huy — SRE ca đêm của startup **SessionHub** — mở laptop trong bóng tối phòng trọ. Grafana đỏ một góc. Log PostgreSQL lặp lại cùng một dòng:

```text
DuplicateKeyException: duplicate key value violates unique constraint "sessions_pkey"
```

Hai request đăng nhập khác nhau, hai user khác nhau, nhưng cùng `session_id` — một số nguyên 32-bit được sinh “ngẫu nhiên” bằng `random.randint`. Một user vào được dashboard; user kia thấy session của người lạ. Team rollback feature flag “fast session ID” trước khi khách enterprise thức dậy.

Huy không nghĩ tới hacker. Không nghĩ tới race condition trên một dòng DB. Anh nghĩ tới bài toán sinh nhật mà thầy dạy ở chương xác suất: trong phòng có **23 người**, xác suất hai người **cùng sinh nhật** đã vượt 50%. Trực giác bảo phải cần khoảng 183 người — một nửa 365. Trực giác sai; cùng toán học đó quyết định khi **UUID**, **64-bit ID**, hay **32-bit random** trong database **đụng nhau** — và quyết định lúc 2 giờ sáng Huy có ngủ tiếp được hay không.

Bài này không phải party trick. Nó là lý do GitHub mở rộng integer ID, lý do không dùng INT32 random cho bất cứ thứ gì sống quá một quý, và anchor thực tế cho paradox đã nhắc ở ch07 và ch08. Tom Archer viết [The Birthday Paradox in Production](https://tomarcher.io/posts/birthday-paradox/) (2024) kèm code Python, Monte Carlo, và case study GitHub — bài đọc mà Huy bookmark ngay sau incident.

Nếu bạn mới học năm 1 hoặc năm 2, hãy đọc theo một ý chính: **rủi ro va chạm không tỉ lệ với “còn bao nhiêu slot trống”, mà tỉ lệ với số cặp so sánh — và số cặp tăng theo $$n^2$$.**

---

## Trực giác sai — “còn nhiều chỗ trống” không cứu bạn

Hãy tưởng tượng bạn sinh ID ngẫu nhiên trong không gian $$d$$ giá trị. Trực giác thường hỏi: “Mình mới dùng $$n$$ cái, còn $$(d-n)$$ cái trống — sao đã va chạm?” Câu trả lời: va chạm không xảy ra vì “lấp đầy” không gian. Va chạm xảy ra vì mỗi ID mới phải **so với tất cả ID cũ** — và với $$n$$ item, số cặp so sánh là $$\binom{n}{2} = \frac{n(n-1)}{2}$$, tức tỉ lệ **$$n^2$$**, không phải $$n$$.

### UUID v4 — “vô hạn” nhưng không phải không bao giờ

UUID v4 mang **122 bit** ngẫu nhiên (phần còn lại là version và variant cố định) → không gian $$d = 2^{122}$$.

Trực giác: phải sinh hàng tỷ tỷ ID mới lo. Thực tế, ngưỡng xác suất va chạm 50% xảy ra khi $$n \approx 2.7 \times 10^{18}$$ — tức chỉ khoảng **0.0000000000000000008%** không gian đã được “dùng” theo nghĩa birthday. Với tốc độ **1 tỷ ID/giây**, Tom Archer ước cần ~**86 năm** mới chạm ngưỡng 50%. Thoải mái cho hầu hết hệ thống — nhưng **không vô hạn**. UUID v4 an toàn decades; nó không phải lý do để bỏ qua toán.

### 32-bit — thảm họa đến nhanh hơn bạn nghĩ

Với $$d = 2^{32} \approx 4.3 \times 10^9$$, ngưỡng 50% va chạm:

$$n_{0.5} \approx 1.177 \sqrt{d} \approx 77\,000$$

Startup tăng 1.000 user/ngày, mỗi user một session ID 32-bit ngẫu nhiên — vài tháng đã vào vùng rủi ro đáng kể. Incident của Huy xảy ra khi team có ~**45.000** session active và bật sinh ID nhanh hơn — chưa tới 77k nhưng đã vượt ngưỡng “1-in-million” (khoảng **12.000** cho 32-bit). DuplicateKeyException lúc 2 giờ sáng không phải “hiếm”; nó là hệ quả có thể tính trước.

![Birthday paradox — Tom Archer](/discrete-mathematics-for-computer-science-iuh/img/course/birthday-paradox.png)

*Hình 9.14: Va chạm không phụ thuộc “lấp đầy” không gian — mà số **cặp** so sánh (nguồn: [tomarcher.io](https://tomarcher.io/posts/birthday-paradox/)).*

<div class="content-box insight-box" markdown="1">
Gấp đôi số item ($$n \to 2n$$) → gấp bốn số cặp ($$\binom{2n}{2} \approx 4\binom{n}{2}$$). Đó là lý do rủi ro “nhảy” nhanh hơn trực giác khi traffic tăng — không phải vì “hết slot”, mà vì “quá nhiều cặp trùng”.
</div>

---

## Mô hình toán — từ sinh nhật đến session_id

Có $$n$$ item, mỗi item chọn ngẫu nhiên (gần uniform) một giá trị trong không gian $$d$$. Hỏi: xác suất **ít nhất một cặp trùng**?

### Công thức chính xác

Xác suất **không** có va chạm:

$$P(\text{no collision}) = \frac{d!}{(d-n)! \cdot d^n}$$

Ý tưởng: người thứ nhất chọn tự do ($$d$$ cách), người thứ hai tránh ngày đã có ($$d-1$$ cách), … nhân tất cả rồi chia cho $$d^n$$ (mọi cách chọn độc lập).

Xác suất **có** va chạm:

$$P(\text{collision}) = 1 - P(\text{no collision})$$

Ví dụ cổ điển $$d = 365$$, $$n = 23$$: $$P(\text{collision}) \approx 0.51$$ — hơn 50%.

### Xấp xỉ production

Khi $$d$$ lớn và $$n \ll d$$, dùng xấp xỉ mũ:

$$P(\text{collision}) \approx 1 - e^{-\frac{n(n-1)}{2d}}$$

Mẫu số $$2d$$ chính là chỗ $$\binom{n}{2}$$ xuất hiện — rủi ro tỉ lệ **$$n^2$$**, không $$n$$. Không phải “còn 4 tỷ slot trống” quyết định; **bao nhiêu cặp** bạn vô tình so sánh mới quyết định.

Ngưỡng 50% (giải gần đúng từ xấp xỉ):

$$n_{0.5} \approx \sqrt{2d \ln 2} \approx 1.177\sqrt{d}$$

| Hệ thống | $$d$$ | ~50% collision tại $$n$$ |
|:---|:---:|:---:|
| 32-bit | $$2^{32}$$ | ~77,000 |
| 64-bit | $$2^{64}$$ | ~5×10⁹ |
| UUID v4 | $$2^{122}$$ | ~2.7×10¹⁸ |

Huy nhìn bảng và hiểu vì sao CTO từng nói “INT32 random tiết kiệm index” nghe hợp lý lúc MVP 500 user — nhưng không scale: 64-bit và UUID không phải “phung phí”, chúng là **biên an toàn** cho số cặp so sánh.

---

## Tom Archer — từ blog đến code chạy được

Tom Archer tổng hợp scenarios production:

| Scenario | Hệ | Rủi ro |
|:---|:---|:---|
| Startup MVP, 32-bit random, 10K items | INT32 | **Vượt** ngưỡng 1-in-million |
| SaaS 10M users, 64-bit | INT64 | An toàn nhiều năm |
| Distributed logs 100B events, UUID | UUID v4 | An toàn decades |

**GitHub** mở rộng integer ID khi scale — minh chứng “clever 32-bit scheme” thành migration nightmare. Chiến lược ID là quyết định kiến trúc ngay từ đầu, không phải detail implement sau khi đã có 45.000 session trong DB.

Huy chạy lại công thức trên laptop — không cần cluster Monte Carlo để thấy nguy hiểm, nhưng blog Archer dùng cả hai để khớp trực giác với số:

```python
import math

def collision_prob(n: int, d: int) -> float:
    if n <= 1:
        return 0.0
    if n > d:
        return 1.0
    exp = -(n * (n - 1)) / (2 * d)
    return 1 - math.exp(exp)

def threshold_50(d: int) -> int:
    return math.ceil(1.177 * math.sqrt(d))

print(collision_prob(23, 365))          # ~0.51
print(collision_prob(12_000, 2**32))    # ~1.7e-6 (1-in-million ballpark)
print(threshold_50(2**32))              # ~77163
```

Monte Carlo (theo blog): mô phỏng 10.000 trial — mỗi trial sinh $$n$$ số ngẫu nhiên trong $$[0, d)$$, đếm tỉ lệ có ít nhất một trùng. Kết quả khớp xấp xỉ mũ — cách kiểm chứng khi bạn không tin đại số.

Cùng công thức áp dụng cho **hash table**: $$d$$ bucket, $$n$$ key inserted, load factor $$\alpha = n/d$$. Chuồng bồ câu (ch08) đảm bảo collision **tồn tại** khi $$n > d$$; birthday paradox ước lượng **khi nào** collision **có khả năng cao** trước khi bucket đầy — hai câu hỏi khác nhau, cùng nền đếm.

<div class="content-box warning-box" markdown="1">
`random.randint` trong Python **không** đảm bảo phân bố uniform trên toàn bộ không gian 32-bit nếu bạn giới hạn range nhỏ hơn — nhưng khi đã dùng đủ $$2^{32}$$ giá trị, birthday bound vẫn áp dụng. Đừng nhầm “hash code” hoặc “random trông lớn” với “không gian đủ rộng”.
</div>

---

## Sau incident — từ INT32 sang UUID

Sáng hôm sau, Huy tham gia post-mortem. Team migrate `session_id` sang **UUID v4** — sinh độc lập trên nhiều node, không cần coordinator trung tâm, không tranh slot trong 77k ngưỡng 32-bit. Một dòng ghi trong doc nội bộ: *“Chúng ta nhầm ‘còn nhiều slot’ với ‘ít cặp trùng’.”*

PagerDuty không gọi lại tuần đó. Nhưng Huy giữ đoạn Python trong repo `tools/collision_estimator.py` — mỗi lần PM hỏi “random 32-bit có đủ không?”, anh nhập $$n$$ dự kiến và $$d$$, trả lời bằng số thay vì cảm giác.

**Đọc thêm:** [tomarcher.io — Birthday Paradox in Production](https://tomarcher.io/posts/birthday-paradox/)

---

## Bài tập thực hành

### Bài tập 1

Trong phòng có 23 người, mỗi người sinh nhật ngẫu nhiên uniform trong 365 ngày (bỏ qua năm nhuận). Dùng xấp xỉ $$P(\text{collision}) \approx 1 - e^{-n(n-1)/(2d)}$$, tính xác suất ít nhất một cặp trùng sinh nhật. So sánh với trực giác “cần ~183 người mới 50%”.

<details>
<summary>Đáp án</summary>

Với $$n = 23$$, $$d = 365$$:

$$\frac{n(n-1)}{2d} = \frac{23 \times 22}{2 \times 365} = \frac{506}{730} \approx 0.693$$

$$P(\text{collision}) \approx 1 - e^{-0.693} \approx 1 - 0.50 = 0.50$$

Xác suất ~**50%** — đúng paradox cổ điển. Trực giác “183 người” nhầm với câu hỏi *“có người nào sinh vào **một ngày cố định** không?”* (xác suất $$\approx 1 - (364/365)^n$$, 50% khi $$n \approx 253$$). Birthday paradox hỏi *“có **cặp** nào trùng không?”* — số cặp $$\binom{23}{2} = 253$$ so sánh, nên 23 người đã đủ.

</details>

### Bài tập 2

Hệ thống dùng `session_id` 32-bit random uniform ($$d = 2^{32}$$). Tính (a) $$n_{0.5}$$ — số session tại đó xác suất va chạm ~50%; (b) $$n$$ tương ứng xác suất ~$$10^{-6}$$ (1-in-million). Incident Huy có ~45.000 session — so sánh với hai ngưỡng.

<details>
<summary>Đáp án</summary>

(a) $$n_{0.5} \approx 1.177 \sqrt{2^{32}} \approx 77\,163$$.

(b) Giải $$1 - e^{-n(n-1)/(2d)} \approx 10^{-6}$$ → $$e^{-n(n-1)/(2d)} \approx 1 - 10^{-6}$$ → $$n(n-1)/(2d) \approx 10^{-6}$$ → $$n \approx \sqrt{2d \times 10^{-6}} \approx \sqrt{2 \times 4.3 \times 10^9 \times 10^{-6}} \approx 2\,900$$.

Chính xác hơn với code: `collision_prob(12_000, 2**32) ≈ 1.7e-6` — ngưỡng 1-in-million nằm quanh **10k–12k**.

Với $$n = 45\,000$$: $$P \approx 1 - e^{-45000 \times 44999 / (2 \times 2^{32})} \approx 1 - e^{-0.235} \approx 0.21$$ — tức ~**21%** mỗi lần “đổ đầy” 45k ID mới (hoặc tương đương mức rủi ro tích lũy theo mô hình sinh). Đã vượt xa 1-in-million; DuplicateKeyException không còn là “cực kỳ hiếm”.

</details>

### Bài tập 3

Viết hàm Python `threshold_p(d: int, p: float) -> int` trả về $$n$$ nhỏ nhất sao cho $$P(\text{collision}) \geq p$$, dùng xấp xỉ mũ. Dùng hàm tìm $$n$$ cho $$d = 2^{64}$$ với $$p = 0.5$$. UUID v4 có $$d = 2^{122}$$ — $$n_{0.5}$$ xấp xỉ bao nhiêu?

<details>
<summary>Đáp án</summary>

Từ $$1 - e^{-n(n-1)/(2d)} \geq p$$ suy ra $$n \gtrsim \sqrt{-2d \ln(1-p)}$$. Với $$p = 0.5$$: $$n \gtrsim \sqrt{2d \ln 2} \approx 1.177\sqrt{d}$$.

```python
import math

def threshold_p(d: int, p: float) -> int:
    if p <= 0:
        return 1
    if p >= 1:
        return d + 1
    n_approx = math.sqrt(-2 * d * math.log(1 - p))
    n = max(2, int(math.ceil(n_approx)))
    while collision_prob(n - 1, d) >= p:
        n -= 1
    while collision_prob(n, d) < p:
        n += 1
    return n
```

- $$d = 2^{64}$$, $$p = 0.5$$: $$n_{0.5} \approx 5 \times 10^9$$ (khoảng 5 tỷ).
- $$d = 2^{122}$$: $$n_{0.5} \approx 1.177 \times 2^{61} \approx 2.7 \times 10^{18}$$.

64-bit an toàn cho SaaS hàng chục triệu user; UUID thêm margin cho distributed log hàng trăm tỷ event.

</details>

### Bài tập 4

Traffic tăng gấp đôi: từ 30.000 lên 60.000 session 32-bit random (cùng không gian $$d$$). (a) Số cặp so sánh tăng bao nhiêu lần? (b) Xác suất va chạm (xấp xỉ) tăng bao nhiêu lần? (c) Giải thích một câu vì sao “gấp đôi user” không phải “gấp đôi rủi ro”.

<details>
<summary>Đáp án</summary>

(a) $$\binom{30\,000}{2} = 449\,985\,000$$; $$\binom{60\,000}{2} = 1\,799\,970\,000$$. Tỉ lệ $$\approx 4.00$$ — gấp **bốn** lần.

(b) Trong xấp xỉ, $$P \approx 1 - e^{-k}$$ với $$k = n(n-1)/(2d)$$. $$k$$ tỉ lệ $$n^2$$ nên cũng gấp ~4. Với $$d = 2^{32}$$:
- $$n = 30\,000$$: $$P \approx 0.094$$
- $$n = 60\,000$$: $$P \approx 0.33$$

Tỉ số $$0.33 / 0.094 \approx 3.5$$ — không đúng 4 vì hàm mũ **phi tuyến**; nhưng $$k$$ trong exponent gấp đúng 4.

(c) Rủi ro va chạm do **số cặp** ($$\propto n^2$$), không do số item ($$\propto n$$). Gấp đôi scale → gấp bốn cặp trùng tiềm năng → rủi ro tăng mạnh hơn trực giác “còn nhiều slot”.

</details>

---

## Tóm tắt

Birthday paradox trong production là câu chuyện **đếm cặp**, không phải **đếm slot trống**. Khi sinh ID ngẫu nhiên trong không gian $$d$$ giá trị, xác suất ít nhất một va chạm xấp xỉ $$1 - e^{-n(n-1)/(2d)}$$ — mẫu số chứa $$n^2$$ qua $$\binom{n}{2}$$. Ngưỡng 50% ở $$n_{0.5} \approx 1.177\sqrt{d}$$: **32-bit** (~77k) nguy hiểm cho session và user ID sống lâu; **64-bit** (~5 tỷ) đủ cho nhiều SaaS; **UUID v4** (~$$2.7 \times 10^{18}$$) cho distributed system và log quy mô cực lớn — an toàn decades nhưng không “vô hạn”.

Incident lúc 2 giờ sáng của Huy minh họa điểm then chốt: 45.000 session 32-bit đã vượt ngưỡng 1-in-million; DuplicateKeyException là hệ quả có thể ước lượng, không phải “xui”. Tom Archer blog và vài dòng Python đủ để trả lời PM trước khi bật feature flag. Cùng toán cho hash bucket (ch08): pigeonhole khi $$n > d$$; birthday khi $$n \ll d$$ nhưng vẫn đủ cặp để rủi ro đáng kể.

Bài sau đặt câu hỏi **khác**: không phải “có ≥1 collision không?” mà “**trung bình bao nhiêu lần** match?” — công thức kỳ vọng của [Matt Might](https://matt.might.net/articles/counting-hash-collisions/) cho biết khi người thứ $$k$$ bước vào phòng, họ trùng sinh nhật với ai đã có bao nhiêu lần — con số staffing nurse review, không chỉ xác suất 0 hay 1.