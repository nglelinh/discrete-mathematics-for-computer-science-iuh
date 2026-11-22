---
layout: post
title: "Birthday paradox trong production: Khi ID ngẫu nhiên va chạm"
categories: chapter09
date: 2021-01-01
order: 7
required: false
lang: en
excerpt: "Phân tích nghịch lý sinh nhật (birthday paradox) khi sinh ID ngẫu nhiên 32-bit, 64-bit và UUID v4 trong hệ thống production, giải thích vì sao rủi ro va chạm tăng theo số cặp n²."
---

Ở bài trước, chúng ta đã rút gọn 324 cấu hình xuống khoảng 15 ca kiểm thử nhờ **pairwise**. Mục này xét một dạng **đếm va chạm** khác: **nghịch lý sinh nhật (birthday paradox)** — xác suất có ít nhất hai phần tử trùng nhau khi chọn ngẫu nhiên $$n$$ phần tử từ không gian $$D$$ giá trị. Ngưỡng xác suất va chạm 50% nằm ở $$n_{0.5} \approx 1{,}177\sqrt{D}$$, nhỏ hơn rất nhiều so với trực giác thông thường. Trong môi trường production, một sự cố điển hình xảy ra lúc 2 giờ sáng khi SRE nhận ngoại lệ `DuplicateKeyException` do hai phiên đăng nhập sinh ID 32-bit ngẫu nhiên trùng nhau:

```text
DuplicateKeyException: duplicate key value violates unique constraint "sessions_pkey"
```

Hai yêu cầu đăng nhập khác nhau của hai người dùng khác nhau lại nhận cùng một `session_id` — số nguyên 32-bit được tạo bằng `random.randint`. Một người vào đúng trang của mình, còn người kia có nguy cơ thấy phiên của người khác. Nhóm vận hành phải lập tức tắt cờ tính năng (feature flag) “fast session ID” trước giờ làm việc.

Phân tích sau sự cố cho thấy nguyên nhân không phải tấn công mạng hay lỗi tranh chấp (race condition) trên một dòng DB, mà là **birthday paradox**: trong một phòng chỉ cần **23 người**, xác suất có ít nhất hai người **cùng ngày sinh** đã vượt 50%, dù trực giác thường ước lượng cần khoảng 183 người (một nửa của 365). Chính mô hình toán học đó quyết định thời điểm **UUID**, **ID 64-bit** hay **ID 32-bit ngẫu nhiên** trong cơ sở dữ liệu bắt đầu **va chạm**. Đó cũng là lý do GitHub phải mở rộng kích thước số nguyên định danh và lý do không nên dùng số ngẫu nhiên 32-bit cho định danh tồn tại lâu dài, như Tom Archer phân tích trong [bài viết chuyên sâu](https://tomarcher.io/posts/birthday-paradox/) (2024). Ý cốt lõi cần nắm là: **rủi ro va chạm không tỷ lệ với “còn bao nhiêu ô trống”, mà tỷ lệ với số cặp so sánh — đại lượng tăng theo $$n^2$$.**

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/course/Birthdaymatch.svg"
       alt="Đồ thị xác suất không trùng sinh nhật giảm nhanh khi số người trong phòng tăng"
       width="55%" height="55%">
  <figcaption style="text-align: center;">Hình 9.7a: Va chạm phụ thuộc vào số *cặp* so sánh (~$$n^2$$) chứ không phải số ô còn trống — không gian 32-bit đã rất rủi ro quanh ~77.000 phần tử, còn UUID v4 an toàn trong nhiều thập kỷ (nguồn: <a href="https://commons.wikimedia.org/wiki/File:Birthdaymatch.svg">Guillaume Jacquenot / Wikimedia Commons</a>, CC BY-SA 3.0).</figcaption>
</p>
</figure>

---

## Trực giác dễ nhầm — “còn nhiều ô trống” không ngăn được va chạm

Xét việc sinh ID ngẫu nhiên trong không gian gồm $$d$$ giá trị. Trực giác thường đặt câu hỏi: “Mới dùng $$n$$ giá trị, vẫn còn $$d - n$$ ô trống, sao đã trùng?” Thực tế, va chạm không đợi đến khi không gian gần đầy. Mỗi ID mới sinh ra đều được đối chiếu với **toàn bộ các ID đã tồn tại**; với $$n$$ phần tử, tổng số cặp có thể trùng nhau là $$\binom{n}{2} = \frac{n(n-1)}{2}$$, tức tăng theo **$$n^2$$** chứ không phải $$n$$.

### UUID v4 — rất lớn nhưng không phải vô hạn

UUID v4 chứa **122 bit** ngẫu nhiên (6 bit còn lại cố định cho thông tin version và variant), tương ứng không gian $$d = 2^{122}$$.

Ngưỡng xác suất va chạm 50% xảy ra tại $$n \approx 2{,}71 \times 10^{18}$$ — tức mới chiếm khoảng **$$5{,}1 \times 10^{-17}\%$$** tổng không gian giá trị. Nếu sinh liên tục ở tốc độ **1 tỷ ID mỗi giây**, Tom Archer ước tính cần khoảng **86 năm** mới chạm ngưỡng 50%. Biên an toàn này đủ rộng cho hầu hết hệ thống phân tán trong nhiều thập kỷ, nhưng về bản chất vẫn là không gian hữu hạn.

### Không gian 32-bit — rủi ro tăng nhanh hơn nhiều so với trực giác

Với $$d = 2^{32} \approx 4{,}29 \times 10^9$$, ngưỡng xác suất va chạm 50% chỉ là:

<div class="textbook-equation" markdown="1">
$$n_{0.5} \approx 1.177 \sqrt{d} \approx 77\,000$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Nếu một hệ thống tăng thêm 1.000 người dùng mỗi ngày và cấp cho mỗi người một session ID 32-bit ngẫu nhiên, chỉ sau vài tháng hệ thống đã tiến vào vùng rủi ro cao. Trong sự cố của Huy, hệ thống đang có khoảng **45.000** phiên hoạt động — chưa chạm mốc 77.000 nhưng xác suất va chạm đã lên tới khoảng **21%** (vượt xa ngưỡng 1 phần triệu, vốn chỉ nằm quanh **93** phần tử trên không gian 32-bit). Do đó, `DuplicateKeyException` lúc 2 giờ sáng không phải sự cố hiếm gặp mà là hệ quả có thể tính trước bằng toán học.

![Birthday paradox — Tom Archer](/discrete-mathematics-for-computer-science-iuh/img/course/birthday-paradox.png)

<p class="textbook-figure-caption" data-figure="9.14">Va chạm không phụ thuộc vào mức độ “lấp đầy” không gian mà phụ thuộc vào số **cặp** so sánh (nguồn: [tomarcher.io](https://tomarcher.io/posts/birthday-paradox/)).</p>

<div class="content-box insight-box textbook-block" markdown="1">
Tăng gấp đôi số phần tử ($$n \to 2n$$) làm tăng gấp bốn lần số cặp so sánh ($$\binom{2n}{2} \approx 4\binom{n}{2}$$). Vì vậy, khi lưu lượng tăng trưởng, rủi ro va chạm leo thang nhanh hơn nhiều so với trực giác tuyến tính.
</div>

---

## Mô hình toán học — từ ngày sinh nhật đến `session_id`

Giả sử ta chọn độc lập và đều (uniform) $$n$$ phần tử trong một không gian có $$d$$ giá trị. Ta cần tính xác suất để có **ít nhất một cặp trùng nhau**.

### Công thức chính xác

Xác suất **không** có bất kỳ va chạm nào:

<div class="textbook-equation" markdown="1">
$$P(\text{no collision}) = \frac{d!}{(d-n)! \cdot d^n}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Cách lập luận: phần tử đầu tiên có $$d$$ lựa chọn, phần tử thứ hai phải tránh giá trị đầu nên còn $$d-1$$ lựa chọn, tiếp tục như vậy rồi chia cho tổng số $$d^n$$ cách chọn độc lập.

Xác suất **có ít nhất một** va chạm là phần bù:

<div class="textbook-equation" markdown="1">
$$P(\text{collision}) = 1 - P(\text{no collision})$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Với bài toán cổ điển $$d = 365$$ và $$n = 23$$, ta thu được $$P(\text{collision}) \approx 0{,}507$$ — vượt quá 50%.

### Công thức xấp xỉ cho hệ thống production

Khi $$d$$ lớn và $$n \ll d$$, dùng xấp xỉ hàm mũ $$1 - x \approx e^{-x}$$ ta thu được:

<div class="textbook-equation" markdown="1">
$$P(\text{collision}) \approx 1 - e^{-\frac{n(n-1)}{2d}}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Tử số $$\frac{n(n-1)}{2}$$ chính là số cặp $$\binom{n}{2}$$ — cho thấy trực tiếp rủi ro tỷ lệ với **$$n^2$$**, không phải $$n$$.

Từ công thức trên, giải phương trình $$P(\text{collision}) = 0{,}5$$ cho ra ngưỡng 50%:

<div class="textbook-equation" markdown="1">
$$n_{0.5} \approx \sqrt{2d \ln 2} \approx 1.177\sqrt{d}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

| Không gian ID | $$d$$ | Ngưỡng ~50% va chạm tại $$n$$ |
|:---|:---:|:---:|
| 32-bit | $$2^{32}$$ | ~77.000 |
| 64-bit | $$2^{64}$$ | ~$$5 \times 10^9$$ |
| UUID v4 | $$2^{122}$$ | ~$$2{,}7 \times 10^{18}$$ |

Nhìn vào bảng này, Huy thấy rõ vì sao giải pháp “dùng INT32 ngẫu nhiên cho gọn chỉ mục” tuy chạy ổn ở giai đoạn MVP 500 người dùng nhưng sẽ nhanh chóng gặp sự cố khi mở rộng. Việc chọn 64-bit hay UUID v4 không phải sự lãng phí bộ nhớ mà là **biên an toàn cần thiết** trước tốc độ tăng bậc hai của số cặp.

---

### Thử nghiệm: nghịch lý sinh nhật

Điều chỉnh số người hoặc số ngày để quan sát xác suất trùng nhau và so sánh kết quả mô phỏng ngẫu nhiên với công thức giải tích.

<div class="interactive-demo" markdown="1">
<div data-demo="sim-explainer" data-tab="birthday"></div>
</div>
<script src="{{ '/public/js/explainers/logic-explainer.js' | relative_url }}"></script>

## Tom Archer — từ phân tích lý thuyết đến mã kiểm chứng

Tom Archer tóm lược một số kịch bản phổ biến trong production:

| Kịch bản | Không gian ID | Mức rủi ro |
|:---|:---|:---|
| Startup MVP, 32-bit ngẫu nhiên, 10.000 phần tử | INT32 | **Vượt xa** ngưỡng 1 phần triệu (~1,2% xác suất trùng) |
| SaaS 10 triệu người dùng, 64-bit | INT64 | An toàn trong nhiều năm |
| Nhật ký phân tán 100 tỷ sự kiện, UUID | UUID v4 | An toàn trong nhiều thập kỷ |

Việc **GitHub** phải nâng cấp định danh số nguyên khi mở rộng là minh chứng rõ ràng rằng chọn kiểu 32-bit ban đầu sẽ tạo ra chi phí chuyển đổi (migration) rất lớn về sau. Chiến lược định danh là quyết định kiến trúc ngay từ đầu, không phải chi tiết nhỏ có thể để lại sau khi cơ sở dữ liệu đã có hàng chục nghìn bản ghi.

Huy viết đoạn mã Python ngắn để kiểm chứng trực tiếp các ngưỡng rủi ro:

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

print(collision_prob(23, 365))          # ~0.500 (chính xác là ~0.507)
print(collision_prob(93, 2**32))        # ~9.96e-7 (~1 phần triệu)
print(collision_prob(12_000, 2**32))    # ~0.0166 (~1.7%)
print(threshold_50(2**32))              # ~77163
```

Bên cạnh công thức xấp xỉ, bài viết của Tom Archer còn dùng mô phỏng **Monte Carlo** (chạy 10.000 lượt thử, mỗi lượt sinh $$n$$ số ngẫu nhiên trong $$[0, d)$$ rồi đếm tỷ lệ lượt có ít nhất một cặp trùng) để đối chiếu — kết quả thực nghiệm khớp chặt với công thức hàm mũ.

Cùng mô hình này cũng áp dụng cho **bảng băm (hash table)** gồm $$d$$ bucket và $$n$$ khóa (hệ số tải $$\alpha = n/d$$). Nguyên lý chuồng bồ câu (Chương 8) khẳng định va chạm **chắc chắn xảy ra** khi $$n > d$$, còn nghịch lý sinh nhật ước lượng **khi nào** va chạm đã **có xác suất cao** ngay cả lúc $$n \ll d$$.

<div class="content-box warning-box textbook-block" markdown="1">
Hàm `random.randint` trong Python sẽ có không gian giá trị nhỏ hơn nữa nếu bị giới hạn phạm vi hẹp; ngay cả khi dùng đủ toàn bộ $$2^{32}$$ giá trị phân bố đều, giới hạn birthday vẫn có hiệu lực. Không nên nhầm giữa “giá trị ngẫu nhiên trông lớn” với “không gian định danh đủ rộng”.
</div>

---

## Sau sự cố — chuyển từ INT32 sang UUID v4

Trong buổi tổng kết sự cố (post-mortem) sáng hôm sau, nhóm quyết định chuyển `session_id` sang **UUID v4**: mỗi pod có thể sinh định danh độc lập mà không cần máy chủ điều phối tập trung, đồng thời thoát khỏi ngưỡng va chạm ~77.000 của không gian 32-bit. Ghi chú trong tài liệu nội bộ nêu rõ bài học: *“Chúng ta đã nhầm giữa ‘còn nhiều ô trống’ và ‘ít cặp có thể trùng’.”*

Huy lưu lại đoạn mã ước lượng trong `tools/collision_estimator.py` để mỗi khi có đề xuất dùng ID 32-bit ngẫu nhiên, nhóm chỉ cần nhập $$n$$ và $$d$$ dự kiến nhằm ra quyết định bằng số liệu thay vì cảm tính.

**Đọc thêm:** [tomarcher.io — Birthday Paradox in Production](https://tomarcher.io/posts/birthday-paradox/)

---

## Bài tập thực hành

### Bài tập 1

Trong phòng có 23 người, mỗi người có ngày sinh phân bố đều trong 365 ngày (bỏ qua năm nhuận). Dùng công thức xấp xỉ $$P(\text{collision}) \approx 1 - e^{-n(n-1)/(2d)}$$, tính xác suất có ít nhất một cặp cùng ngày sinh và so sánh với trực giác “cần khoảng 183 người”.

<details>
<summary>Đáp án</summary>

Với $$n = 23$$ và $$d = 365$$:

<div class="textbook-equation" markdown="1">
$$\frac{n(n-1)}{2d} = \frac{23 \times 22}{2 \times 365} = \frac{506}{730} \approx 0.693$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

<div class="textbook-equation" markdown="1">
$$P(\text{collision}) \approx 1 - e^{-0.693} \approx 1 - 0.50 = 0.50$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Xác suất xấp xỉ **50%** (tính chính xác là 50,7%). Trực giác “183 người” nhầm sang một câu hỏi khác là *“có ai trùng với **một ngày cố định cho trước** không?”* (với câu hỏi này, xác suất là $$1 - (364/365)^n$$, đạt 50% khi $$n \approx 253$$). Nghịch lý sinh nhật hỏi về **bất kỳ cặp nào** trùng nhau: 23 người đã tạo ra $$\binom{23}{2} = 253$$ cặp so sánh, nên xác suất vượt 50%.

</details>

### Bài tập 2

Một hệ thống sinh `session_id` ngẫu nhiên đều 32-bit ($$d = 2^{32}$$). Tính: (a) ngưỡng $$n_{0.5}$$ để xác suất va chạm xấp xỉ 50%; (b) ngưỡng $$n$$ để xác suất va chạm xấp xỉ $$10^{-6}$$ (1 phần triệu). So sánh hai ngưỡng này với con số ~45.000 phiên trong sự cố của Huy.

<details>
<summary>Đáp án</summary>

(a) Ngưỡng 50%: $$n_{0.5} \approx 1{,}177 \sqrt{2^{32}} \approx 77\,163$$.

(b) Giải $$1 - e^{-n(n-1)/(2d)} \approx 10^{-6}$$ ta có $$\frac{n(n-1)}{2d} \approx 10^{-6}$$, suy ra:

$$n \approx \sqrt{2d \times 10^{-6}} \approx \sqrt{2 \times 4{,}295 \times 10^9 \times 10^{-6}} \approx \sqrt{8\,590} \approx 93$$

Kiểm tra trực tiếp bằng công thức: `collision_prob(93, 2**32) ≈ 9.96e-7` (xấp xỉ đúng 1 phần triệu).

Với $$n = 45\,000$$: $$P \approx 1 - e^{-45000 \times 44999 / (2 \times 2^{32})} \approx 1 - e^{-0.2357} \approx 0{,}21$$ — tức xác suất va chạm đã lên tới **~21%**, vượt rất xa ngưỡng 1 phần triệu; vì vậy `DuplicateKeyException` là điều dễ dàng xảy ra.

</details>

### Bài tập 3

Viết hàm Python `threshold_p(d: int, p: float) -> int` trả về giá trị $$n$$ nhỏ nhất sao cho $$P(\text{collision}) \geq p$$ theo xấp xỉ hàm mũ. Dùng hàm này để ước lượng $$n_{0.5}$$ cho $$d = 2^{64}$$ và cho UUID v4 ($$d = 2^{122}$$).

<details>
<summary>Đáp án</summary>

Từ $$1 - e^{-n(n-1)/(2d)} \geq p$$, suy ra $$n \gtrsim \sqrt{-2d \ln(1-p)}$$. Riêng với $$p = 0{,}5$$, công thức rút về $$n \gtrsim \sqrt{2d \ln 2} \approx 1{,}177\sqrt{d}$$.

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

- Với $$d = 2^{64}$$, $$p = 0{,}5$$: $$n_{0.5} \approx 5{,}06 \times 10^9$$ (khoảng 5 tỷ).
- Với $$d = 2^{122}$$, $$p = 0{,}5$$: $$n_{0.5} \approx 1{,}177 \times 2^{61} \approx 2{,}71 \times 10^{18}$$.

Do đó, định danh 64-bit đủ an toàn cho các hệ thống SaaS hàng chục triệu người dùng, còn UUID v4 cung cấp biên an toàn cho hệ thống nhật ký phân tán quy mô hàng trăm tỷ sự kiện.

</details>

### Bài tập 4

Lưu lượng hệ thống tăng gấp đôi từ 30.000 lên 60.000 phiên 32-bit ngẫu nhiên (cùng không gian $$d = 2^{32}$$). (a) Số cặp so sánh tăng bao nhiêu lần? (b) Xác suất va chạm (theo xấp xỉ mũ) tăng bao nhiêu lần? (c) Giải thích ngắn gọn vì sao “gấp đôi người dùng” không đồng nghĩa với “gấp đôi rủi ro”.

<details>
<summary>Đáp án</summary>

(a) $$\binom{30\,000}{2} = 449\,985\,000$$ và $$\binom{60\,000}{2} = 1\,799\,970\,000$$. Tỷ lệ xấp xỉ **4,00** — số cặp tăng **gấp bốn lần**.

(b) Trong công thức $$P \approx 1 - e^{-k}$$ với $$k = \frac{n(n-1)}{2d}$$, số mũ $$k$$ tăng gấp 4 lần. Cụ thể với $$d = 2^{32}$$:
- Tại $$n = 30\,000$$: $$k \approx 0{,}1048 \Rightarrow P \approx 0{,}0995 \approx 10\%$$.
- Tại $$n = 60\,000$$: $$k \approx 0{,}4191 \Rightarrow P \approx 0{,}342 \approx 34\%$$.

Tỷ số xác suất là $$0{,}342 / 0{,}0995 \approx 3{,}44$$ — nhỏ hơn 4 đôi chút do hàm mũ có tính phi tuyến (bão hòa dần về 1), nhưng đại lượng $$k$$ trong số mũ tăng đúng gấp 4 lần.

(c) Rủi ro va chạm phụ thuộc vào **số cặp** ($$\propto n^2$$) chứ không phải số phần tử ($$\propto n$$), nên khi quy mô tăng gấp đôi, số cặp có thể trùng tăng gấp bốn và xác suất va chạm tăng vọt nhanh hơn nhiều so với trực giác tuyến tính.

</details>

---

## Xem thêm / Video gợi ý

- [Logic Gates, Truth Tables, Boolean Algebra](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — 3Blue1Brown (Animation + intuition for logic)
- [Introduction to Propositional Logic](https://www.youtube.com/watch?v=4l7L9v0p0Q) — MIT OCW 6.042J (Tom Leighton — formal foundation)

## Tóm tắt

Nghịch lý sinh nhật trong hệ thống production là bài toán **đếm số cặp**, không phải đếm số ô còn trống. Khi sinh $$n$$ định danh ngẫu nhiên đều trong không gian $$d$$ giá trị, xác suất có ít nhất một va chạm xấp xỉ $$1 - e^{-n(n-1)/(2d)}$$, với ngưỡng 50% tại $$n_{0.5} \approx 1{,}177\sqrt{d}$$. Do đó, **32-bit** (~77.000) quá rủi ro cho định danh phiên hay người dùng sống lâu; **64-bit** (~5 tỷ) phù hợp cho nhiều hệ thống SaaS; còn **UUID v4** (~$$2{,}7 \times 10^{18}$$) đáp ứng tốt các hệ thống phân tán và nhật ký quy mô lớn.

Sự cố lúc 2 giờ sáng của Huy cho thấy ở mức 45.000 phiên 32-bit, xác suất trùng đã lên tới ~21%, vượt rất xa ngưỡng 1 phần triệu (~93 phiên). Cùng mô hình toán học này cũng giúp phân biệt hai câu hỏi trong bảng băm (Chương 8): nguyên lý chuồng bồ câu xét trường hợp chắc chắn trùng ($$n > d$$), còn nghịch lý sinh nhật ước lượng thời điểm rủi ro trùng trở nên đáng kể khi $$n \ll d$$.

Trong bài tiếp theo, chúng ta sẽ chuyển sang một câu hỏi **khác**: không chỉ hỏi “có ít nhất một va chạm không?” mà hỏi “**trung bình có bao nhiêu lần** trùng lặp?” — công thức kỳ vọng của [Matt Might](https://matt.might.net/articles/counting-hash-collisions/) dùng để ước lượng khối lượng công việc thực tế như phân bổ nhân sự rà soát hồ sơ.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=KtT_cgMzHx8">Check your intuition: The birthday problem - David Knuffke</a> — TED-Ed, tiếng Anh. Xây dựng trực giác về bài toán sinh nhật và lý do va chạm xuất hiện sớm hơn dự đoán.
- <a href="https://www.youtube.com/watch?v=ofTb57aZHZs">The Birthday Paradox</a> — Vsauce2, tiếng Anh. Minh họa nghịch lý sinh nhật qua các ví dụ đếm trước khi áp dụng cho session ID.
- <a href="https://www.youtube.com/watch?v=OUQVhnuTMVU">Closer Look at the Birthday Paradox - Numberphile</a> — Numberphile, tiếng Anh. Trình bày công thức xấp xỉ dùng để ước lượng xác suất trùng ID ngẫu nhiên.
