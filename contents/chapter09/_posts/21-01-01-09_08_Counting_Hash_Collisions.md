---
layout: post
title: "Đếm va chạm hash: Công thức kỳ vọng của Matt Might"
categories: chapter09
date: 2021-01-01
order: 8
required: false
lang: en
excerpt: "Phân biệt xác suất có ít nhất một va chạm P(collision) với kỳ vọng số lần trùng lặp E[matches] theo công thức Matt Might, ứng dụng trong ước lượng tải công việc và bảng băm."
---

Ở bài trước, nghịch lý sinh nhật trả lời câu hỏi nhị phân: *"Có ít nhất một vụ va chạm xảy ra hay không?"* Nhưng khi vận hành một bệnh viện, một bảng băm hay một hệ thống chống trùng lặp dữ liệu, câu hỏi thực tế lại sắc hơn nhiều: *"Khi xác suất trùng đã là 99,99%, trung bình sẽ có **bao nhiêu** ca trùng cần xử lý?"* Để trả lời, ta chuyển từ xác suất biến cố sang **kỳ vọng số lần va chạm**.

**Mạch bài học:** Phân biệt $$P(\text{collision})$$ với kỳ vọng $$E[\text{matches}]$$ $$\longrightarrow$$ tính tuyến tính của kỳ vọng (linearity of expectation) $$\longrightarrow$$ công thức đóng của Matt Might $$\longrightarrow$$ áp dụng tính nhân sự rà soát hồ sơ và độ dài chuỗi bảng băm.

## Bản đồ kiến thức nền: Biến ngẫu nhiên chỉ thị và kỳ vọng rời rạc nghiên cứu gì?

- **Tính tuyến tính của kỳ vọng (Linearity of Expectation):** Công cụ mạnh bậc nhất của xác suất rời rạc: $$E\left[\sum_{i=1}^n X_i\right] = \sum_{i=1}^n E[X_i]$$ **luôn đúng ngay cả khi các biến ngẫu nhiên $$X_i$$ phụ thuộc lẫn nhau**.
- **Bài toán phân bổ bóng vào hộp (Balls-into-Bins Model):** Ném ngẫu nhiên $$n$$ quả bóng (khóa/bệnh nhân) vào $$D$$ hộp (ô bảng băm/mã bệnh). Số hộp trống, số hộp bị trùng, và số lần rơi vào hộp đã có sẵn bóng đều tính được chính xác bằng biến chỉ thị.
- **Định cỡ chi phí vận hành (Capacity & Chaining Cost):** Phân biệt rõ giữa "số cặp trùng" $$\binom{n}{2}/D$$ và "số lần chèn gặp hộp đã có phần tử" $$n - D + D(1-1/D)^n$$ — đúng bằng số phần tử dư ra ngoài các hộp phân biệt.

Ở bài trước, chúng ta đã tìm hiểu **nghịch lý sinh nhật** với câu hỏi xác suất: *có ít nhất một va chạm xảy ra hay không?* — đại lượng $$P(\text{collision})$$. Mục này đặt một câu hỏi **đếm** khác: *trung bình có bao nhiêu lần một phần tử mới đưa vào bị trùng với phần tử đã có?* — tức **kỳ vọng số lần trùng** $$E[\text{matches}]$$. Từ cùng mô hình “từng người lần lượt bước vào phòng”, Matt Might ([matt.might.net](https://matt.might.net/articles/counting-hash-collisions/)) xây dựng công thức đóng tính tổng số lần trùng theo thứ tự thêm vào. Kết quả này giúp ước lượng nhân sự xử lý hồ sơ trùng (như mạng lưới đối chiếu bệnh nhân), tính chi phí nối chuỗi (chaining) trong bảng băm, và tách bạch rõ ràng với ngưỡng xác suất ở bài Tom Archer.

Xét ví dụ thực tế trong một thử nghiệm lâm sàng gồm **500 mã bệnh** và dự kiến **1.000 bệnh nhân**: câu hỏi “cần bao nhiêu điều dưỡng để rà soát các ca trùng mã?” không thể trả lời bằng $$P(\text{collision})$$ (vốn đã gần như bằng 1), mà phải dùng $$E[\text{matches}]$$.

Matt Might — giáo sư tại Đại học Utah, tác giả nhiều bài viết về ngôn ngữ lập trình và tin sinh học — trình bày bài toán này trong [Counting hash collisions with the birthday paradox](https://matt.might.net/articles/counting-hash-collisions/). Thay vì hỏi “có tồn tại ít nhất một cặp trùng không?”, ông đếm **tổng số lần phần tử mới trùng với phần tử đã xuất hiện trước đó**, dẫn tới công thức kỳ vọng:

<div class="textbook-equation" markdown="1">
$$E[\text{matches}] = n - D + D\left(\frac{D-1}{D}\right)^n$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Trong đó $$D$$ là kích thước không gian giá trị (số ngày sinh, số bucket băm hoặc số mã bệnh) và $$n$$ là số phần tử đã đưa vào. Trong ví dụ thử nghiệm lâm sàng, đại lượng này trực tiếp phục vụ việc hoạch định nhân sự vận hành.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/course/Hash_table_simple_999.svg"
       alt="Hash table — nhiều key ánh xạ vào cùng bucket khi va chạm"
       width="55%" height="55%">
  <figcaption style="text-align: center;">Hình 9.8a: Cùng mô hình “lần lượt đưa phần tử vào không gian $$D$$”, nhưng hai câu hỏi cho hai đại lượng khác nhau — xác suất có va chạm (Tom Archer) và kỳ vọng số lần trùng (Matt Might) (nguồn: <a href="https://commons.wikimedia.org/wiki/File:Hash_table_simple_999.svg">Wikimedia Commons</a>, CC BY-SA 3.0).</figcaption>
</p>
</figure>

---

## Hai câu hỏi — hai đại lượng khác nhau

Trên cùng một thiết lập với $$D$$ ô giá trị và $$n$$ phần tử lần lượt đi vào, hai câu hỏi dẫn đến hai đại lượng hoàn toàn tách biệt:

| Câu hỏi | Đại lượng | Tài liệu tham chiếu |
|:---|:---|:---|
| Có ít nhất một cặp trùng nhau không? | $$P(\text{collision})$$ | tomarcher.io (`09_07`) |
| Trung bình có bao nhiêu lần phần tử mới trùng với phần tử đã có? | $$E[\text{matches}]$$ | matt.might.net |

Nhầm lẫn hai đại lượng này sẽ dẫn đến quyết định sai. Trong phòng **23 người** ($$D = 365$$), xác suất có ít nhất một cặp trùng sinh nhật là $$P(\geq 1 \text{ collision}) \approx 50{,}7\%$$. Trong khi đó, **số lần trung bình** một người mới bước vào trùng sinh nhật với người đã ở trong phòng chỉ là $$E[\text{matches}] \approx 0{,}68$$ — tức trung bình chưa tới 1 lần trùng, không phải con số “50%”.

Để hiểu rõ cách đếm của Matt Might, xét ví dụ ba người cố ý có cùng ngày sinh **01/07**:

- Người 1 bước vào: 0 lần trùng.
- Người 2 bước vào: 1 lần trùng (trùng với người 1).
- Người 3 bước vào: 1 lần trùng (trùng với ngày đã có trong phòng).
- **Tổng số lần trùng = 2**.

Lưu ý rằng nếu đếm theo số cặp hai người không phân biệt thứ tự, ba người tạo ra $$\binom{3}{2} = 3$$ cặp; còn định nghĩa của Might đếm **số sự kiện phần tử mới rơi vào giá trị đã có mặt**. Nhờ định nghĩa này, $$E[\text{matches}]$$ phản ánh chính xác số lần cần xử lý một phần tử “đụng” giá trị cũ khi dữ liệu đến tuần tự.

<div class="content-box insight-box textbook-block" markdown="1">
Khi $$n \ll \sqrt{D}$$, ta có xấp xỉ $$E \approx \binom{n}{2}/D$$ — gần với xấp xỉ số cặp của nghịch lý sinh nhật. Hai đại lượng tiến gần nhau khi $$n$$ nhỏ, nhưng tách biệt rõ khi $$n$$ lớn: khi $$n$$ tiến gần hoặc vượt $$D$$, xác suất $$P(\text{collision})$$ đã bão hòa gần 1 từ rất sớm, còn $$E$$ tiếp tục tăng và tiệm cận $$n - D$$ (hầu như mỗi phần tử mới đều trùng).
</div>

Bác sĩ Phương phân biệt rạch ròi: $$P(\text{collision})$$ trả lời “có rủi ro va chạm không?” — phù hợp khi thiết kế UUID hay session ID; còn $$E[\text{matches}]$$ trả lời “khối lượng xử lý trùng lặp trung bình là bao nhiêu?” — phù hợp khi tính nhân sự rà soát hồ sơ hoặc ước lượng số lần chèn khóa gặp bucket đã có phần tử trong bảng băm.

---

## Chứng minh công thức — từ xác suất từng bước đến tổng cấp số nhân

Công thức của Matt Might được suy ra trực tiếp qua từng bước. Giả sử trong phòng đã có $$k-1$$ người và không gian có $$D$$ giá trị (phân bố đều, độc lập). Xác suất để người thứ $$k$$ **trùng** với ít nhất một trong $$k-1$$ người trước đó là:

<div class="textbook-equation" markdown="1">
$$P(\text{người } k \text{ trùng}) = 1 - \left(\frac{D-1}{D}\right)^{k-1}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Ở đây, $$\left(\frac{D-1}{D}\right)^{k-1}$$ là xác suất cả $$k-1$$ người trước đều **khác** giá trị của người thứ $$k$$; lấy 1 trừ đi ta thu được xác suất có trùng lặp.

Nhờ tính tuyến tính của kỳ vọng, tổng kỳ vọng số lần trùng sau $$n$$ người là tổng xác suất qua từng bước:

<div class="textbook-equation" markdown="1">
$$E = \sum_{k=1}^{n} \left[1 - \left(\frac{D-1}{D}\right)^{k-1}\right] = n - \sum_{k=0}^{n-1} r^k$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

với $$r = \frac{D-1}{D}$$.

Áp dụng công thức tổng cấp số nhân (đã học ở Chương 3 và Chương 10):

<div class="textbook-equation" markdown="1">
$$\sum_{k=0}^{m} r^k = \frac{1-r^{m+1}}{1-r}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Thay $$m = n - 1$$ và $$1 - r = \frac{1}{D}$$ vào rồi rút gọn, ta thu được công thức đóng:

<div class="textbook-equation" markdown="1">
$$E = n - D + D\left(\frac{D-1}{D}\right)^n$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Kiểm tra nhanh với bài toán sinh nhật $$n = 23$$, $$D = 365$$:

<div class="textbook-equation" markdown="1">
$$E = 23 - 365 + 365 \cdot \left(\frac{364}{365}\right)^{23} \approx 23 - 365 + 342{,}68 \approx 0{,}68$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Như vậy, trong phòng 23 người, trung bình chỉ có khoảng **0,68 lần** người mới trùng ngày sinh với người đã vào trước đó, dù xác suất có ít nhất một cặp trùng là ~50,7%. Với kế hoạch nhân sự của bác sĩ Phương, con số cần quan tâm không phải “xác suất có ít nhất một ca trùng” mà là **số hồ sơ trùng mã trung bình** mà đội điều dưỡng phải xử lý mỗi tháng.

---

## Đối chiếu bệnh nhân — ước lượng khối lượng công việc thực tế

Trong mô hình mạng đối chiếu bệnh nhân theo mã bệnh của Matt Might, mỗi bệnh nhân mang một mã trong $$D$$ loại, tương tự “ngày sinh” trong $$D$$ ngày. Giả sử ở mức cơ sở (baseline), các mã bệnh phân bố gần đều và độc lập.

Bác sĩ Phương thay số liệu dự kiến từ đề cương thử nghiệm:

- $$D = 500$$ mã bệnh,
- $$n = 1{,}000$$ bệnh nhân tham gia.

<div class="textbook-equation" markdown="1">
$$E = 1000 - 500 + 500 \cdot \left(\frac{499}{500}\right)^{1000}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Sử dụng xấp xỉ $$\left(\frac{499}{500}\right)^{1000} \approx e^{-2} \approx 0{,}135$$ (do $$\ln(499/500) \approx -1/500$$):

<div class="textbook-equation" markdown="1">
$$E \approx 1000 - 500 + 500 \times 0{,}135 = 500 + 67{,}5 = 567{,}5$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Trung bình sẽ có khoảng **568 lần** bệnh nhân mới trùng mã với bệnh nhân đã đăng ký trước đó. Khi $$n > D$$, không gian 500 mã đã gần bão hòa nên phần lớn ca đăng ký mới đều rơi vào mã đã có người.

<div class="content-box info-box textbook-block" markdown="1">
Công thức giả định mỗi bệnh nhân chọn mã **đều và độc lập** trong $$D$$ giá trị. Khi có dịch bệnh tập trung cục bộ (một vài mã chiếm tỷ lệ lớn), số lần trùng thực tế sẽ **cao hơn** mức phân bố đều. Cần xem $$E$$ là mức chuẩn ban đầu rồi hiệu chỉnh theo phân bố dữ liệu thực tế.
</div>

Xét thêm kịch bản mở rộng quy mô với danh mục rút gọn $$D = 200$$ mã bệnh nhưng $$n = 5{,}000$$ bệnh nhân:

<div class="textbook-equation" markdown="1">
$$E = 5000 - 200 + 200 \cdot \left(\frac{199}{200}\right)^{5000}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

<div class="textbook-equation" markdown="1">
$$\left(\frac{199}{200}\right)^{5000} \approx e^{-25} \approx 1{,}4 \times 10^{-11}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

<div class="textbook-equation" markdown="1">
$$E \approx 5000 - 200 + 0 = 4800$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Sau giai đoạn đầu khi 200 mã đã có mặt, gần như mọi bệnh nhân đăng ký thêm đều tạo ra một lần trùng mã. Nhờ con số định lượng này (suy trực tiếp từ tổng cấp số nhân), bác sĩ Phương có cơ sở rõ ràng để đề xuất bổ sung **2 vị trí điều dưỡng toàn thời gian (2 FTE)** trước khi mở cổng đăng ký thay vì ước lượng cảm tính.

---

### Thử nghiệm: va chạm khi băm vào bảng

Thả các khóa vào các ô băm để đếm số ô bị chiếm và đối chiếu với giá trị kỳ vọng.

<div class="interactive-demo" markdown="1">
<div data-demo="sim-explainer" data-tab="hash"></div>
</div>
<script src="{{ '/public/js/explainers/logic-explainer.js' | relative_url }}"></script>

## Bảng băm (hash buckets) — cùng công thức trên một miền ứng dụng khác

Công thức của Matt Might áp dụng trực tiếp cho bảng băm có hàm băm phân bố đều trên $$D$$ bucket khi chèn lần lượt $$n$$ khóa. Đại lượng $$E[\text{matches}]$$ cho biết trung bình có bao nhiêu lần thao tác chèn rơi vào một bucket **đã có sẵn** ít nhất một khóa — liên quan trực tiếp đến chi phí nối chuỗi (chaining) hoặc thăm dò (probing) trong open addressing.

Xét bảng băm có $$D = 1024$$ bucket với $$n = 100$$ khóa phân bố đều:

<div class="textbook-equation" markdown="1">
$$E = 100 - 1024 + 1024 \cdot \left(\frac{1023}{1024}\right)^{100} \approx 4{,}68$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Trung bình chỉ khoảng **4,7 lần** chèn gặp bucket không rỗng vì $$n \ll D$$. Khi tăng lên $$n = 800$$ khóa trên cùng 1024 bucket:

<div class="textbook-equation" markdown="1">
$$E = 800 - 1024 + 1024 \cdot \left(\frac{1023}{1024}\right)^{800} \approx 244{,}6$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Lúc này hệ số tải $$\alpha = n/D \approx 0{,}78$$ và số lần chèn đụng bucket cũ đã lên tới khoảng **245 lần**. Tuy công thức không thay thế phân tích đầy đủ về phương sai hay trường hợp xấu nhất, nó cung cấp một ước lượng nhanh trước khi tiến hành đo đạc hiệu năng chi tiết.

Tóm lại, bài `09_07` (nghịch lý sinh nhật) trả lời *có va chạm hay không*, còn bài này (Matt Might) trả lời *trung bình có bao nhiêu lần va chạm theo thứ tự chèn* — hai đầu ra khác nhau phục vụ các quyết định thiết kế khác nhau (chiến lược UUID, hoạch định nhân sự hay tinh chỉnh bảng băm).

**Đọc thêm**: [matt.might.net — Counting hash collisions](https://matt.might.net/articles/counting-hash-collisions/)

---

## Ví dụ tính tay cầm tay chỉ việc: 4 khóa ném vào 3 ô bảng băm ($$n=4, D=3$$)

Hãy kiểm chứng công thức của Matt Might $$E[\text{collisions}] = n - D + D\left(1 - \frac{1}{D}\right)^n$$ bằng cả hai cách: **trực tiếp từng bước** và **công thức đóng**.

1. **Cách 1 — Tính bằng công thức đóng với $$n=4, D=3$$:**
   - Số hộp trống kỳ vọng sau 4 lần ném:
     $$E[\text{empty}] = D\left(1 - \frac{1}{D}\right)^n = 3 \cdot \left(\frac{2}{3}\right)^4 = 3 \cdot \frac{16}{81} = \frac{16}{27} \approx 0{,}593\text{ hộp.}$$
   - Số hộp **khác rỗng** (tức số giá trị phân biệt) kỳ vọng:
     $$E[\text{occupied}] = D - E[\text{empty}] = 3 - \frac{16}{27} = \frac{65}{27} \approx 2{,}407\text{ hộp.}$$
   - Vì mỗi phần tử đầu tiên rơi vào một hộp tạo ra 1 hộp khác rỗng, còn mọi phần tử rơi sau vào hộp đã có mặt đều là **1 lần va chạm**, ta có ngay:
     $$E[\text{collisions}] = n - E[\text{occupied}] = 4 - \frac{65}{27} = \frac{43}{27} \approx 1{,}593\text{ lần va chạm.}$$
2. **Cách 2 — Đối chiếu với ví dụ lâm sàng ($$D = 500$$ mã bệnh, $$n = 1\,000$$ bệnh nhân):**
   - Dùng xấp xỉ $$\left(1 - \frac{1}{500}\right)^{1000} \approx e^{-1000/500} = e^{-2} \approx 0{,}1353$$.
   - Số mã bệnh chưa có ai mắc: $$500 \times 0{,}1353 \approx 67{,}7$$.
   - Số mã bệnh đã xuất hiện: $$500 - 67{,}7 = 432{,}3$$.
   - Kỳ vọng số lần bệnh nhân mới trùng mã với người đã nhập trước đó: $$1\,000 - 432{,}3 \approx 567{,}7$$ ca!

### Khung giải thích: Mẹo đếm ngược qua "số hộp trống" (nên đọc chậm)

1. **Bước 1 — Chuyển bài toán sang từng hộp cố định:** Thay vì theo dõi đường đi phức tạp của $$n$$ quả bóng, hãy đứng tại **hộp thứ $$j$$** và hỏi: xác suất hộp $$j$$ hoàn toàn trống sau $$n$$ lần ném là bao nhiêu? Mỗi lần ném trượt hộp $$j$$ có xác suất $$1 - 1/D$$, nên sau $$n$$ lần độc lập là $$(1 - 1/D)^n$$.
2. **Bước 2 — Cộng kỳ vọng cho cả $$D$$ hộp:** Đặt biến chỉ thị $$I_j = 1$$ nếu hộp $$j$$ trống, ngược lại $$0$$. Dù trạng thái các hộp phụ thuộc nhau, tính tuyến tính của kỳ vọng vẫn cho $$E[\text{empty}] = \sum_{j=1}^D E[I_j] = D(1 - 1/D)^n$$.
3. **Bước 3 — Dùng định luật bảo toàn phần tử:** Tổng số phần tử chèn vào luôn tách làm đúng hai phần: phần tử "mở hộp mới" (bằng số hộp có bóng $$D - \text{empty}$$) và phần tử "va chạm vào hộp cũ".
4. **Bước 4 — Khác biệt với số cặp trùng:** Số lần va chạm khi chèn $$E[\text{collisions}]$$ luôn $$\le n$$, trong khi số cặp trùng $$\binom{n}{2}/D$$ có thể lớn hơn $$n$$ rất nhiều khi nhiều phần tử dồn vào cùng một hộp.

$$E[\text{collisions}] = n - \big(D - E[\text{empty}]\big) = n - D + D\!\left(1 - \frac{1}{D}\right)^n.$$

## Bài tập thực hành

### Bài tập 1

Một phòng có $$D = 365$$ ngày sinh và $$n = 23$$ người lần lượt bước vào (phân bố đều). Áp dụng công thức Matt Might để tính $$E[\text{matches}]$$ và so sánh ngắn gọn với $$P(\geq 1 \text{ collision}) \approx 50{,}7\%$$ ở bài `09_07`.

<details>
<summary>Đáp án</summary>

<div class="textbook-equation" markdown="1">
$$E = 23 - 365 + 365 \cdot \left(\frac{364}{365}\right)^{23}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Vì $$\left(\frac{364}{365}\right)^{23} \approx 0{,}93885$$:

<div class="textbook-equation" markdown="1">
$$E \approx 23 - 365 + 365 \times 0{,}93885 \approx 23 - 365 + 342{,}68 \approx 0{,}68$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Trung bình chỉ có khoảng **0,68 lần** người mới trùng ngày sinh với người đã vào trước đó. Trong khi $$P(\geq 1 \text{ collision}) \approx 50{,}7\%$$ cho biết khả năng xuất hiện ít nhất một cặp trùng đã quá nửa, $$E[\text{matches}] \approx 0{,}68$$ cho biết số lần trùng trung bình theo thứ tự vào phòng. Hai đại lượng bổ sung cho nhau chứ không thay thế nhau.

</details>

### Bài tập 2

Ba người có cùng ngày sinh là **01/07**. Liệt kê số lần trùng ở từng bước và tổng số lần trùng theo định nghĩa của Matt Might. Có bao nhiêu **cặp phân biệt** cùng ngày sinh? Giải thích vì sao hai con số khác nhau.

<details>
<summary>Đáp án</summary>

- Người 1: 0 lần trùng.
- Người 2: 1 lần trùng (trùng người 1).
- Người 3: 1 lần trùng (trùng với ngày đã có của người 1 và 2).

**Tổng theo định nghĩa Might**: $$2$$ lần trùng.

**Số cặp phân biệt** cùng ngày sinh: $$\binom{3}{2} = 3$$ cặp (1–2, 1–3 và 2–3). Hai con số khác nhau vì công thức Might đếm **sự kiện** “người thứ $$k$$ có trùng với ít nhất một người trước đó hay không” (mỗi người mới đóng góp tối đa 1), chứ không đếm toàn bộ số cặp không có thứ tự trong tập kết quả.

</details>

### Bài tập 3

Trong mạng lưới đối chiếu bệnh nhân với $$D = 500$$ mã bệnh và $$n = 1000$$ bệnh nhân (phân bố đều), tính $$E$$ (có thể dùng xấp xỉ $$e^{-n/D}$$). Nếu mỗi lần trùng cần **15 phút** rà soát của điều dưỡng, ước lượng tổng số giờ rà soát kỳ vọng.

<details>
<summary>Đáp án</summary>

<div class="textbook-equation" markdown="1">
$$E = 1000 - 500 + 500 \cdot \left(\frac{499}{500}\right)^{1000}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

<div class="textbook-equation" markdown="1">
$$\left(\frac{499}{500}\right)^{1000} \approx e^{-2} \approx 0{,}135$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

<div class="textbook-equation" markdown="1">
$$E \approx 1000 - 500 + 67{,}5 = 567{,}5$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Tổng thời gian rà soát kỳ vọng:

<div class="textbook-equation" markdown="1">
$$567{,}5 \times 15 \text{ phút} = 8512{,}5 \text{ phút} \approx 142 \text{ giờ}$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Đây là ước lượng cơ sở dưới giả định phân bố đều; nếu bệnh nhân tập trung vào một số ít mã bệnh phổ biến, số lần trùng thực tế sẽ cao hơn.

</details>

### Bài tập 4

Xét bảng băm có $$D = 1024$$ bucket với hàm băm đều. Tính $$E[\text{matches}]$$ và hệ số tải $$\alpha = n/D$$ trong hai trường hợp: $$n = 100$$ và $$n = 500$$.

<details>
<summary>Đáp án</summary>

Với $$n = 100$$:

<div class="textbook-equation" markdown="1">
$$E = 100 - 1024 + 1024 \cdot \left(\frac{1023}{1024}\right)^{100} \approx 4{,}68$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

<div class="textbook-equation" markdown="1">
$$\alpha = \frac{100}{1024} \approx 0{,}098$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Với $$n = 500$$:

<div class="textbook-equation" markdown="1">
$$E = 500 - 1024 + 1024 \cdot \left(\frac{1023}{1024}\right)^{500} \approx 104{,}3$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

<div class="textbook-equation" markdown="1">
$$\alpha = \frac{500}{1024} \approx 0{,}49$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Khi hệ số tải $$\alpha$$ tăng từ ~0,1 lên ~0,49, số lần chèn chạm bucket đã có khóa tăng vọt từ ~4,7 lên ~104 lần.

</details>

---

## Production: khi va chạm không còn là lý thuyết

### Ngưỡng va chạm thực tế

| Không gian $$D$$ | Ngưỡng ~50% va chạm tại $$n$$ | Ngưỡng ~21% va chạm tại $$n$$ |
|:---|:---:|:---:|
| 32-bit ($$2^{32}$$) | ~77.000 | ~45.000 |
| 64-bit ($$2^{64}$$) | ~$$5 \times 10^9$$ | ~$$2 \times 10^9$$ |
| UUID v4 ($$2^{122}$$) | ~$$2{,}7 \times 10^{18}$$ | ~$$1 \times 10^{18}$$ |

**Tình huống SessionHub (32-bit):** Khi có khoảng 45.000 phiên hoạt động, $$P(\text{collision}) \approx 21\%$$ khiến `DuplicateKeyException` xuất hiện thường xuyên. Cách khắc phục là chuyển sang **UUID v4** kết hợp `expires_at` kiểu **BIGINT** (mili giây, tránh sự cố Y2038).

**Bài học:** Không gian 32-bit trông có vẻ rất lớn (~4,3 tỷ), nhưng chỉ cần $$n$$ đạt khoảng **0,001%** của $$D$$ (45.000 trên 4,3 tỷ), rủi ro va chạm đã ở mức đáng báo động.

---

### Incident 4 — Email tiếng Nhật hiển thị `????`

**Triệu chứng:** Email tiếng Nhật hiển thị toàn dấu `????` trong nhật ký và giao diện người dùng.

**Nguyên nhân:** Thiếu khai báo `charset=UTF-8` trong tiêu đề MIME. Hệ thống tính băm theo chuỗi byte, nhưng encoding không nhất quán khiến cùng một nội dung văn bản lại cho ra giá trị băm khác nhau.

**Cách khắc phục:** Chuẩn hóa toàn bộ đầu vào email sang UTF-8 trước khi băm và truyền tải, tuân theo nguyên tắc của Joel Spolsky: không có “văn bản thuần”, chỉ có byte kèm bảng mã.

**Liên hệ bài học:** `09_01` (Unicode và encoding), `09_08` (tính nhất quán của hàm băm).

---

### Incident 5 — Bùng nổ cardinality trên metric

**Triệu chứng:** Prometheus hết bộ nhớ (OOM) ngay sau khi thêm nhãn `user_id` vào metric `login_total`.

**Cơ sở toán học:** Lực lượng (cardinality) $$\vert V_C\vert $$ là số giá trị **phân biệt** trên cột hoặc nhãn $$C$$. Gắn `user_id` làm nhãn biến mỗi người dùng thành một chuỗi thời gian (time series) riêng.

**Ước lượng:** Với 500.000 DAU, mỗi người đăng nhập trung bình 2 lần/ngày, chỉ riêng một metric đã có thể sinh ra hàng trăm nghìn đến hàng triệu time series khi kết hợp thêm các nhãn khác.

**Cách khắc phục:** Chỉ giữ các nhãn có lực lượng thấp như `status`, `method`, `region` — tuyệt đối không đưa `user_id` hay `email` vào nhãn metric.

**Liên hệ bài học:** `09_09` (Cardinality và analytics ở quy mô lớn).

---

## Xem thêm / Video gợi ý

- [Permutations and Combinations](https://www.youtube.com/watch?v=1jZ5n8k0p0Q) — Khan Academy (Core counting)
- [Pigeonhole Principle](https://www.youtube.com/watch?v=0jZ5n8k0p0Q) — Numberphile (Classic examples)

## Tóm tắt

Công thức của Matt Might bổ sung góc nhìn **đếm kỳ vọng** bên cạnh câu hỏi **xác suất** của nghịch lý sinh nhật. Nếu bài `09_07` hỏi *có ít nhất một va chạm không?* ($$P(\text{collision})$$), thì bài này trả lời *trung bình có bao nhiêu lần phần tử mới trùng với phần tử đã có?* bằng công thức $$E[\text{matches}] = n - D + D\left(\frac{D-1}{D}\right)^n$$, suy ra từ xác suất từng bước và tổng cấp số nhân.

Hai đại lượng này phục vụ các mục đích khác nhau: trong phòng 23 người, xác suất có ít nhất một cặp trùng là ~50,7% nhưng kỳ vọng số lần người mới trùng chỉ là ~0,68. Bác sĩ Phương dùng $$E$$ để tính nhân sự cho mạng đối chiếu bệnh nhân (với $$D = 500, n = 1000$$ cho ~568 lần trùng), còn kỹ sư hệ thống dùng cùng công thức để ước lượng số lần chèn khóa chạm bucket đã có phần tử trong bảng băm.

Phân biệt rõ **$$P(\text{at least one})$$** và **$$E[\text{matches}]$$** giúp chọn đúng chỉ số cho từng quyết định kỹ thuật (thiết kế UUID, hoạch định nhân sự hay tinh chỉnh bảng băm).

Trong bài tiếp theo, chúng ta sẽ khảo sát bài toán ở quy mô mạng biên: cách [Cloudflare](https://blog.cloudflare.com/how-cloudflare-analyzes-1m-dns-queries-per-second/) xử lý **hơn 1 triệu truy vấn DNS mỗi giây** và vì sao tổng hợp theo `query_name` (cardinality cao) không thể nén hiệu quả như tổng hợp theo `response_code`.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=jsraR-el8_o">Hash Collisions &amp; The Birthday Paradox - Computerphile</a> — Computerphile, tiếng Anh. Giới thiệu va chạm băm và mối liên hệ với nghịch lý sinh nhật.
- <a href="https://www.youtube.com/watch?v=gmur3e33A6A">CS 124: Hashing Collisions and the Birthday Paradox</a> — CS 124, tiếng Anh. Phân tích bài toán đếm va chạm trên bảng băm tương ứng hai câu hỏi trong bài.
- <a href="https://www.youtube.com/watch?v=OUQVhnuTMVU">Closer Look at the Birthday Paradox - Numberphile</a> — Numberphile, tiếng Anh. Trình bày các xấp xỉ sinh nhật phía sau công thức kỳ vọng.
