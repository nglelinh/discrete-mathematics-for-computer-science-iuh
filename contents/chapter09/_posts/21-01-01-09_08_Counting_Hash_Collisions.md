---
layout: post
title: "Đếm va chạm hash: Công thức kỳ vọng của Matt Might"
categories: chapter09
date: 2021-01-01
order: 8
required: false
lang: en
---

Thứ Tư, cuộc họp staffing cho thử nghiệm lâm sàng mới. Protocol liệt kê **500 mã bệnh** có thể đăng ký; dự kiến **1.000 bệnh nhân** trong sáu tháng đầu. Ban quản trị hỏi Dr. Phương — nhà nghiên cứu xây dựng **mạng match bệnh nhân–bệnh** — cần bao nhiêu nurse để review từng lần bệnh nhân mới “trùng” với ai đã trong mạng.

Đồng nghiệp gợi ý: *“Cứ nhân đôi số bệnh nhân là đủ.”* Dr. Phương lắc đầu. Bài trước (09_07), [Tom Archer](https://tomarcher.io/posts/birthday-paradox/) trả lời câu *“Có **ít nhất một** cặp trùng không?”* — xác suất $$P(\text{collision})$$, một con số từ 0 đến 1. Câu hỏi của cô **khác**: khi bệnh nhân thứ $$k$$ đăng ký, **bao nhiêu lần** người đó trùng mã với ai đã có? Đó là **kỳ vọng số lần match**, không phải xác suất có hay không.

Matt Might — giáo sư tại University of Utah, blogger về PL và bioinformatics — đặt đúng câu hỏi đó trong [Counting hash collisions with the birthday paradox](https://matt.might.net/articles/counting-hash-collisions/). Cùng mô hình “người lần lượt bước vào phòng”, nhưng đếm **tổng số lần người mới trùng** thay vì hỏi “có ≥1 cặp không”. Công thức kỳ vọng:

$$E[\text{matches}] = n - D + D\left(\frac{D-1}{D}\right)^n$$

Trong đó $$D$$ là kích thước không gian (ngày sinh, bucket hash, mã bệnh), $$n$$ là số phần tử đã đưa vào. Dr. Phương mở spreadsheet — cô cần con số để justify staffing, không phải party trick.

---

## Hai câu hỏi — hai con số khác nhau

Cùng setup birthday: $$D$$ “ô” có thể chọn, $$n$$ người (hoặc key, hoặc bệnh nhân) lần lượt vào. Hai câu hỏi cho **hai đại lượng khác nhau**:

| Câu hỏi | Đại lượng | Blog tham chiếu |
|:---|:---|:---|
| Có ≥1 cặp trùng? | $$P(\text{collision})$$ | tomarcher.io (09_07) |
| Trung bình bao nhiêu lần “người mới trùng”? | $$E[\text{matches}]$$ | matt.might.net |

Nhầm hai câu hỏi là nhầm quyết định. Trong phòng **23 người**, $$P(\geq 1 \text{ collision}) \approx 50\%$$ — nghĩa là *có khả năng cao* ít nhất một cặp cùng sinh nhật. Nhưng **trung bình** bao nhiêu lần người mới “đụng” vào sinh nhật đã có? Might tính ra khoảng **5** — không phải 0 hay 1, và cũng không phải “50%”.

Ví dụ Might minh họa: ba người sinh **cố ý** cùng ngày **1/7**:

- Người 1 vào: 0 match
- Người 2 vào: 1 match (trùng người 1)
- Người 3 vào: 1 match (trùng người 1 hoặc 2)
- **Tổng = 2 matches**

Nhưng chỉ **một cặp unique** nếu đếm theo kiểu “ba người cùng ngày”. Công thức Might đếm **lần người mới trùng** khi lần lượt vào phòng — không đếm unique pairs. Đó là lý do $$E$$ có thể lớn hơn nhiều so với trực giác “chỉ có vài cặp trùng”.

<div class="content-box insight-box" markdown="1">
Khi $$n \ll \sqrt{D}$$, $$E \approx \binom{n}{2}/D$$ — gần xấp xỉ birthday pairwise. Hai công thức hội tụ khi $$n$$ nhỏ; phân tách khi $$n$$ lớn. Lúc $$n$$ gần hoặc vượt $$D$$, hầu hết người mới đều match — $$E$$ tiệm cận $$n$$, trong khi $$P(\text{collision})$$ đã gần 1 từ lâu.
</div>

Dr. Phương ghi nhớ: $$P(\text{collision})$$ trả lời “có rủi ro không” — hữu ích khi thiết kế UUID hay session ID. $$E[\text{matches}]$$ trả lời “workload trung bình bao nhiêu” — hữu ích khi staffing nurse review, ước lượng chi phí chaining trong hash table, hoặc đếm số lần key mới rơi vào bucket đã có người.

---

## Dẫn chứng — từ xác suất từng bước đến cấp số nhân

Might xây công thức từng bước — không magic. Trong phòng đã có $$k-1$$ người, không gian $$D$$ ngày (hoặc bucket, hoặc mã bệnh), xác suất người thứ $$k$$ **trùng** với ít nhất một người trước đó:

$$P(\text{người } k \text{ trùng}) = 1 - \left(\frac{D-1}{D}\right)^{k-1}$$

Giải thích ngắn: $$\left(\frac{D-1}{D}\right)^{k-1}$$ là xác suất $$k-1$$ người trước **không** trùng ngày của người mới (mô hình uniform, độc lập). Lấy 1 trừ đi là xác suất có match.

Tổng kỳ vọng qua $$n$$ người — cộng xác suất match từng bước:

$$E = \sum_{k=1}^{n} \left[1 - \left(\frac{D-1}{D}\right)^{k-1}\right] = n - \sum_{k=0}^{n-1} r^k$$

với $$r = \frac{D-1}{D}$$.

Tổng cấp số nhân (đã gặp ở ch03/ch10):

$$\sum_{k=0}^{m} r^k = \frac{1-r^{m+1}}{1-r}$$

Thay $$m = n-1$$, rút gọn (chi tiết đại số trong blog Might):

$$E = n - D + D\left(\frac{D-1}{D}\right)^n$$

Kiểm tra nhanh với $$n=23, D=365$$:

$$E \approx 23 - 365 + 365 \cdot (364/365)^{23} \approx 5.0$$

Trung bình ~**5 lần** “người mới trùng sinh nhật” trong phòng 23 người — khác hẳn $$P(\geq 1 \text{ collision}) \approx 50\%$$. Cùng phòng, cùng $$D$$ và $$n$$, hai câu hỏi, hai con số. Dr. Phương nhìn lại slide staffing: cô không cần biết “50% có match” — cô cần biết nurse sẽ mở bao nhiêu hồ sơ trùng mã **trung bình** mỗi tháng.

---

## Patient matching — ước lượng workload thật

Might mô tả mạng match bệnh nhân theo mã bệnh: mỗi bệnh nhân mang một mã trong $$D$$ loại — giống “sinh nhật” trong $$D$$ ngày. Mô hình đơn giản: phân bố **gần uniform**, mỗi bệnh nhân chọn mã độc lập.

Dr. Phương nhập số dự kiến từ protocol:

- $$D = 500$$ mã bệnh,
- $$n = 1{,}000$$ bệnh nhân đã vào mạng.

$$E = 1000 - 500 + 500 \cdot \left(\frac{499}{500}\right)^{1000}$$

Xấp xỉ: $$\left(\frac{499}{500}\right)^{1000} \approx e^{-2} \approx 0.135$$ (vì $$\ln(499/500) \approx -1/500$$).

$$E \approx 1000 - 500 + 500 \times 0.135 = 1000 - 500 + 67.5 \approx 567.5$$

→ Trung bình **~568 lần** bệnh nhân mới trùng mã với ai đó đã có. Không phải “có thể có match” — mà **gần 568 lần** match khi đã có 1.000 bệnh nhân. Workload nurse review cao vì $$n \gg D$$: không gian 500 mã đã bão hòa, hầu hết người mới đều “đụng” vào mã cũ.

<div class="content-box info-box" markdown="1">
Công thức giả định mỗi bệnh nhân chọn mã **ngẫu nhiên độc lập** trong $$D$$ giá trị. Dịch tập trung (đại dịch, cluster địa lý) làm match **cao hơn** vì vài mã chiếm tỷ lệ lớn; phân bố lệch (mã hiếm vs mã phổ biến) làm match **thấp hơn** uniform. Dùng $$E$$ làm baseline, rồi điều chỉnh theo dữ liệu thực tế.
</div>

Khi scale lên — giả sử chỉ còn $$D=200$$ bệnh trong danh mục rút gọn, nhưng $$n=5000$$ bệnh nhân:

$$E = 5000 - 200 + 200 \cdot (199/200)^{5000}$$

$$(199/200)^{5000} \approx e^{-25} \approx 1.4 \times 10^{-11}$$

$$E \approx 5000 - 200 + \text{~0} \approx 4800$$

Hầu hết bệnh nhân sau giai đoạn đầu đều “match” một bệnh đã có — nurse review **không** scale tuyến tính với $$n$$. Thêm 1.000 bệnh nhân nữa không thêm ~1.000 review mới; gần như mỗi người mới đều kéo theo một lần mở hồ sơ. Dr. Phương dùng con số này trong slide: justify thêm **2 FTE** nurse review thay vì “cảm giác sẽ đông”. Might’s formula không sexy như Monte Carlo — nhưng đóng form, chứng minh được từ tổng cấp số nhân, và đổi được staffing plan trước khi trial mở cổng đăng ký.

---

## Hash buckets — cùng công thức, khác domain

Công thức Might không chỉ cho sinh nhật hay mã bệnh. Hash function **uniform** ánh xạ key vào $$D$$ bucket; insert $$n$$ key lần lượt. $$E[\text{matches}]$$ ước lượng số lần key mới rơi vào bucket **đã có** ít nhất một key — trực tiếp liên quan chi phí **chaining** (duyệt linked list trong bucket) hoặc số lần probe trong open addressing.

Ví dụ thiết kế bảng băm: $$D=1024$$ bucket, $$n=100$$ key uniform:

$$E = 100 - 1024 + 1024 \cdot (1023/1024)^{100} \approx 2.7$$

Trung bình khoảng **2,7 lần** insert “đụng” bucket không rỗng — nhỏ vì $$n \ll D$$. Khi $$n$$ tăng lên 800 cùng 1024 bucket:

$$E \approx 800 - 1024 + 1024 \cdot (1023/1024)^{800} \approx 259$$

Load factor $$\alpha = n/D \approx 0.78$$ — gần đầy — và kỳ vọng match đã lên hàng trăm. Công thức không thay thế phân tích load factor đầy đủ (variance, worst case), nhưng cho **intuition** nhanh trước khi profile thật: “với $$n$$ key và $$D$$ bucket uniform, trung bình bao nhiêu lần phải so sánh vì bucket đã có người?”

Dr. Phương nhận ra pattern: birthday paradox (09_07) hỏi **có** collision không; Might đếm **bao nhiêu lần** collision theo thứ tự insert. Cùng toán, khác output — và khác quyết định: UUID strategy vs nurse staffing vs hash table tuning.

**Đọc thêm**: [matt.might.net — Counting hash collisions](https://matt.might.net/articles/counting-hash-collisions/)

---

## Bài tập thực hành

### Bài tập 1

Phòng có $$D=365$$ ngày sinh, $$n=23$$ người vào lần lượt (mô hình uniform). Dùng công thức Might, tính $$E[\text{matches}]$$. So sánh ngắn với $$P(\geq 1 \text{ collision}) \approx 50\%$$ từ bài 09_07.

<details>
<summary>Đáp án</summary>

$$E = 23 - 365 + 365 \cdot (364/365)^{23}$$

Tính $$(364/365)^{23} \approx 0.940$$:

$$E \approx 23 - 365 + 365 \times 0.940 \approx 23 - 365 + 343.1 \approx 5.0$$

Trung bình **~5 lần** người mới trùng sinh nhật đã có. $$P(\geq 1 \text{ collision}) \approx 50\%$$ chỉ nói “có khả năng cao ít nhất một cặp trùng” — không cho biết workload **5 lần** match theo thứ tự vào phòng. Hai đại lượng bổ sung nhau, không thay thế.

</details>

### Bài tập 2

Ba người có sinh nhật **1/7**, **1/7**, **1/7** (cố ý trùng). Liệt kê số match từng bước và tổng $$E$$ theo định nghĩa Might. Có bao nhiêu **cặp unique** cùng ngày? Giải thích vì sao hai con số khác nhau.

<details>
<summary>Đáp án</summary>

- Người 1: 0 match
- Người 2: 1 match (trùng người 1)
- Người 3: 1 match (trùng người 1 hoặc 2)

**Tổng $$E = 2$$** theo Might.

**Cặp unique** cùng ngày: $$\binom{3}{2} = 3$$ cặp (1–2, 1–3, 2–3) — nhưng khi đếm “lần người mới trùng”, người 3 chỉ góp **1** lần, không góp 2 lần cho hai cặp riêng. Might đếm **sự kiện** “người $$k$$ match với ai đó trước đó”, không đếm toàn bộ unordered pairs trong tập cuối.

</details>

### Bài tập 3

Mạng match bệnh nhân: $$D=500$$ mã, $$n=1000$$ bệnh nhân uniform. Tính $$E$$ (có thể dùng xấp xỉ $$e^{-n/D}$$). Nếu mỗi match cần **15 phút** nurse review, ước lượng tổng giờ review **kỳ vọng** (coi mỗi match độc lập).

<details>
<summary>Đáp án</summary>

$$E = 1000 - 500 + 500 \cdot (499/500)^{1000}$$

$$(499/500)^{1000} \approx e^{-2} \approx 0.135$$

$$E \approx 1000 - 500 + 67.5 = 567.5$$

Tổng giờ review kỳ vọng:

$$567.5 \times 15 \text{ phút} = 8512.5 \text{ phút} \approx 142 \text{ giờ}$$

Đây là baseline uniform — dịch tập trung có thể làm $$E$$ cao hơn; phân bố lệch có thể thấp hơn.

</details>

### Bài tập 4

Hash table: $$D=1024$$ bucket, $$n=100$$ key uniform. Tính $$E[\text{matches}]$$. Nếu $$n=500$$, $$E$$ xấp xỉ bao nhiêu? Load factor $$\alpha = n/D$$ trong hai trường hợp là gì?

<details>
<summary>Đáp án</summary>

$$n=100$$:

$$E = 100 - 1024 + 1024 \cdot (1023/1024)^{100} \approx 2.7$$

$$\alpha = 100/1024 \approx 0.098$$

$$n=500$$:

$$E = 500 - 1024 + 1024 \cdot (1023/1024)^{500} \approx 159$$

$$\alpha = 500/1024 \approx 0.49$$

Khi $$\alpha$$ tăng, $$E$$ tăng nhanh — gần nửa bucket đã có key thì trung bình ~159 lần insert chạm bucket không rỗng.

</details>

---

## Tóm tắt

Matt Might đặt câu hỏi **đếm** bên cạnh câu hỏi **xác suất** của birthday paradox. Bài 09_07: *có ≥1 collision không?* → $$P(\text{collision})$$. Bài này: *trung bình bao nhiêu lần người mới trùng?* → $$E[\text{matches}] = n - D + D\left(\frac{D-1}{D}\right)^n$$, dẫn từ xác suất match từng bước và tổng cấp số nhân.

Hai con số không thay thế nhau. Phòng 23 người: ~50% có ít nhất một cặp trùng, nhưng kỳ vọng chỉ ~5 lần “người mới đụng sinh nhật cũ”. Dr. Phương dùng $$E$$ để staffing mạng match bệnh nhân — với $$D=500, n=1000$$, ~568 lần match, không scale tuyến tính khi $$n \gg D$$. Cùng công thức áp cho hash bucket: ước lượng số lần key mới rơi vào bucket đã có người trước khi profile chi tiết.

Phân biệt **$$P(\text{at least one})$$** vs **$$E[\text{number of matches}]$$** là kỹ năng đếm trong production — cùng setup, câu hỏi sai → quyết địch sai (UUID vs nurse vs hash tuning).

Bài sau scale khác hẳn: [Cloudflare](https://blog.cloudflare.com/how-cloudflare-analyzes-1m-dns-queries-per-second/) xử lý **1M DNS queries/giây**, và vì sao aggregate theo **query name** (cardinality cao) không nén được như aggregate theo **response code** — bài toán đếm **distinct values** ở quy mô edge, không còn là phòng sinh nhật hay bucket hash.