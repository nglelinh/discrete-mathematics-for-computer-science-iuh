---

layout: post
title: "Ứng dụng của Nguyên lý Bao hàm - Loại trừ"
categories: chapter11
date: 2021-01-01
order: 4
required: false
lang: vi
excerpt: "Áp dụng nguyên lý bao hàm–loại trừ vào các bài toán cổ điển: sàng Legendre, hàm phi Euler, số toàn ánh, hoán vị không điểm cố định (derangement) và tô màu có ràng buộc."
---

Một công thức tưởng chỉ dùng để giải đố biểu đồ Venn lại hóa ra là "chiếc rìu đa năng" giải quyết liền bốn bài toán kinh điển của Toán học và Khoa học Máy tính: đếm số nguyên tố bằng **Sàng Legendre**, chứng minh công thức **hàm phi Euler $$\varphi(n)$$** (nền tảng của mật mã RSA), đếm số **toàn ánh** phân việc cho máy chủ, và tính xác suất không ai nhận đúng mũ của mình (**Derangements $$D_n$$**).

**Mạch bài học:** Chọn đúng **tập vi phạm $$A_i$$** $$\longrightarrow$$ **Sàng Legendre** & **Hàm phi Euler $$\varphi(n)$$** $$\longrightarrow$$ đếm **toàn ánh (onto functions)** $$\longrightarrow$$ **hoán vị không điểm cố định (derangements $$D_n$$)** và giới hạn bất ngờ $$D_n/n! \to 1/e$$.

## Kiến thức cần nhớ: Bốn bài toán kinh điển dưới cùng một lăng kính Bao hàm – Loại trừ

- **Lý thuyết số & Mật mã (Legendre Sieve & Euler's Totient $$\varphi(n)$$):** Đếm các số nguyên tố cùng nhau với $$n = p_1^{e_1}\cdots p_r^{e_r}$$ chính là loại bỏ bội của từng ước nguyên tố $$p_i$$, dẫn ngay đến tích gọn $$\varphi(n) = n \prod_{i=1}^r \left(1 - \frac{1}{p_i}\right)$$ — trái tim của hệ mật RSA.
- **Ánh xạ & Số Stirling loại hai (Surjections):** Đếm số toàn ánh từ tập $$m$$ phần tử vào tập $$n$$ phần tử tương ứng bài toán phân bổ $$m$$ tác vụ phân biệt vào $$n$$ máy chủ sao cho **không máy chủ nào rảnh rỗi** (vi phạm $$A_i$$: máy chủ $$i$$ không nhận tác vụ nào).
- **Hoán vị không điểm cố định (Derangements $$D_n$$):** Đếm số hoán vị $$\pi$$ sao cho $$\pi(i) \ne i$$ với mọi $$i$$ (vi phạm $$A_i$$: phần tử $$i$$ đứng yên đúng vị trí $$i$$). Đáng kinh ngạc là xác suất một hoán vị ngẫu nhiên là derangement hội tụ cực nhanh về $$1/e \approx 36{,}79\%$$ bất kể $$n$$ lớn đến đâu!

Ở mục trước, chúng ta đã chứng minh công thức bao hàm–loại trừ tổng quát. Mục này áp dụng nguyên lý đó vào các bài toán cổ điển: **sàng Legendre**, **hàm phi Euler** $$\phi(n)$$, **số toàn ánh**, **derangement** và đếm cấu hình có ràng buộc (như tô màu đồ thị). Bước quan trọng nhất thường không nằm ở phép cộng trừ mà ở việc **mô hình hóa** chính xác các tập vi phạm $$A_i$$ và phần giao của chúng; sau khi xác định xong các tập con này, phần còn lại chỉ là thay số vào công thức đã biết.

![Ứng dụng bao hàm–loại trừ](/discrete-mathematics-for-computer-science-iuh/img/course/Inclusion-exclusion-3sets.svg)

<p class="textbook-figure-caption" data-figure="11.16">Sàng Legendre và hàm phi Euler đều tuân theo cùng cấu trúc: cộng tập đơn, trừ giao đôi và cộng lại giao bậc cao hơn.</p>
![Phân tích thừa số nguyên tố](/discrete-mathematics-for-computer-science-iuh/img/course/PrimeDecompositionExample.svg)

<p class="textbook-figure-caption" data-figure="11.17">Hàm $$\phi(n)$$ loại bỏ các số chia hết cho từng thừa số nguyên tố của $$n$$.</p>
![Cấu trúc số nguyên](/discrete-mathematics-for-computer-science-iuh/img/course/Euler_diagram_of_number_sets.svg)

<p class="textbook-figure-caption" data-figure="11.18">Đếm số nguyên tố cùng nhau, số toàn ánh và derangement đều là các bài toán đếm tiêu biểu trên tập rời rạc.</p>
![Đếm cấu hình có ràng buộc](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="11.19">Trong bài toán tô màu, mỗi cạnh vi phạm tạo thành một tập con; bao hàm–loại trừ giúp đếm số cách tô hợp lệ.</p>
![Ánh xạ và đếm](/discrete-mathematics-for-computer-science-iuh/img/course/Hash_table_simple_999.svg)

<p class="textbook-figure-caption" data-figure="11.20">Số toàn ánh đếm các ánh xạ phủ kín tập đích, có ứng dụng trong phân bố dữ liệu và bảng băm (hashing).</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Áp dụng** nguyên lý bao hàm–loại trừ vào sàng Legendre và hàm phi Euler $$\phi(n)$$.
- **Tính** số toàn ánh và số derangement bằng công thức bao hàm–loại trừ.
- **Mô hình hóa** bài toán tô màu và các bài toán có ràng buộc thành hợp của những tập vi phạm.

**Từ khóa**: sàng Legendre, hàm Euler, toàn ánh (surjection), derangement, tô màu đồ thị.
</div>

## Sàng Legendre và đếm số nguyên tố

Để đếm số nguyên tố không vượt quá $$N$$, ta đếm số các hợp số bị chia hết bởi ít nhất một số nguyên tố không vượt quá $$\sqrt N$$ rồi loại chúng khỏi tập ứng viên. Cách làm này không thay thế sàng Eratosthenes về mặt hiệu năng tính toán, nhưng minh họa rõ cách nguyên lý bao hàm–loại trừ hoạt động trên tập số nguyên.

<div class="textbook-example" markdown="1">
**Ví dụ**: Với $$N=30$$, các số nguyên tố không vượt quá $$\sqrt{30}$$ là 2, 3 và 5. Ta đếm các số chia hết cho ít nhất một trong ba số 2, 3, 5 rồi điều chỉnh để không loại nhầm chính 2, 3, 5 (và loại số 1).
</div>


## Hàm phi Euler

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$\phi(n)$$ là số các số nguyên dương không vượt quá $$n$$ và nguyên tố cùng nhau với $$n$$.
</div>


Nếu phân tích thừa số nguyên tố của $$n$$ là

<div class="textbook-equation" markdown="1">
$$
n=p_1^{\alpha_1}p_2^{\alpha_2}\cdots p_k^{\alpha_k},
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
thì

<div class="textbook-equation" markdown="1">
$$
\phi(n)=n\prod_{i=1}^{k}\left(1-\frac{1}{p_i}\right).
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Ý tưởng chứng minh**: Xét các số nguyên từ 1 đến $$n$$, sau đó loại bỏ những số chia hết cho ít nhất một thừa số nguyên tố $$p_i$$ bằng nguyên lý bao hàm–loại trừ.

## Số toàn ánh

Số ánh xạ toàn ánh từ một tập $$m$$ phần tử sang một tập $$n$$ phần tử được tính bằng bao hàm–loại trừ theo công thức:

<div class="textbook-equation" markdown="1">
$$
\text{Surj}(m,n)=\sum_{k=0}^{n}(-1)^k\binom{n}{k}(n-k)^m.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Trực giác**: Ta bắt đầu từ tổng số $$n^m$$ ánh xạ bất kỳ, sau đó trừ đi các ánh xạ bỏ sót ít nhất một giá trị đích (có $$\binom{n}{1}(n-1)^m$$ trường hợp), cộng lại phần bỏ sót ít nhất hai giá trị đích, rồi tiếp tục xen kẽ dấu như vậy.

## Hoán vị không điểm cố định

Một hoán vị của $$n$$ phần tử không có điểm cố định nào được gọi là **derangement**. Số derangement ký hiệu là $$!n$$ và thỏa mãn công thức:

<div class="textbook-equation" markdown="1">
$$
!n=n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Đây là kết quả kinh điển của nguyên lý bao hàm–loại trừ: xuất phát từ $$n!$$ hoán vị, trừ đi các hoán vị cố định ít nhất một vị trí, cộng lại các hoán vị cố định ít nhất hai vị trí, và tiếp tục cho đến $$n$$.

### Video ngắn: Derangement và hằng số $$1/e$$

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/derangement-one-over-e.mp4"></video>
</div>

Trong $$24$$ hoán vị của $$\{1,2,3,4\}$$, có đúng $$9$$ hoán vị không có phần tử nào đứng đúng vị trí ban đầu, tức $$D_4=9$$. Theo nguyên lý bao hàm–loại trừ, $$D_n=n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}$$, suy ra $$D_n/n!\to 1/e\approx 0{,}3679$$: khi $$n$$ đủ lớn, khoảng $$36{,}8\%$$ số hoán vị là derangement.

## Ứng dụng trong tô màu và ràng buộc

Trong các bài toán tô màu có ràng buộc, ta cần đếm số cách gán màu sao cho không xảy ra xung đột. Gọi $$A_i$$ là tập các cách tô vi phạm điều kiện tại cạnh thứ $$i$$. Số cách tô hợp lệ bằng tổng số cách tô tùy ý trừ đi kích thước hợp của các tập vi phạm $$A_i$$, tức là áp dụng trực tiếp dạng bù của nguyên lý bao hàm–loại trừ.

<div class="interactive-demo" markdown="1">
**Demo tương tác đề xuất**: Chọn số phần tử của tập nguồn và tập đích; công cụ sẽ hiển thị số toàn ánh bằng cách trừ dần các ánh xạ bỏ sót giá trị đích.
<div data-demo="surjection-counter"></div>
</div>
<script src="{{ '/public/js/surjection-counter.js' | relative_url }}"></script>

## Ví dụ tính tay làm từng bước: Tính tay $$\varphi(30)$$, số toàn ánh và $$D_4$$

**Ví dụ 1 — Hàm phi Euler $$\varphi(30)$$:**
Phân tích $$30 = 2 \times 3 \times 5$$. Đặt $$A_2, A_3, A_5$$ là các bội của 2, 3, 5 trong $$\{1,\dots,30\}$$.
- Bằng Bao hàm – Loại trừ:
  $$\varphi(30) = 30 - (15 + 10 + 6) + (5 + 3 + 2) - 1 = 30 - 31 + 10 - 1 = 8.$$
- Đối chiếu công thức tích: $$30\left(1-\frac{1}{2}\right)\left(1-\frac{1}{3}\right)\left(1-\frac{1}{5}\right) = 30 \cdot \frac{1}{2} \cdot \frac{2}{3} \cdot \frac{4}{5} = 8$$. (Đúng 8 số: $$1, 7, 11, 13, 17, 19, 23, 29$$.)

**Ví dụ 2 — Phân 4 tác vụ phân biệt vào 3 máy chủ sao cho không máy nào rảnh (số toàn ánh $$m=4, n=3$$):**
- Không ràng buộc: $$3^4 = 81$$ cách.
- Ít nhất 1 máy rảnh ($$k=1$$): $$\binom{3}{1} \cdot 2^4 = 3 \times 16 = 48$$.
- Ít nhất 2 máy rảnh ($$k=2$$): $$\binom{3}{2} \cdot 1^4 = 3 \times 1 = 3$$.
- Cả 3 máy rảnh ($$k=3$$): $$0$$.
- **Kết quả:** $$81 - 48 + 3 = 36$$ toàn ánh!

**Ví dụ 3 — Đếm số derangement $$D_4$$ (4 lá thư cho vào 4 phong bì sai địa chỉ hoàn toàn):**
$$D_4 = 4!\left(1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \frac{1}{4!}\right) = 24\left(1 - 1 + \frac{1}{2} - \frac{1}{6} + \frac{1}{24}\right) = 12 - 4 + 1 = 9\text{ cách.}$$
- Kiểm tra tỷ lệ: $$D_4 / 4! = 9/24 = 0{,}375$$ — mới ở $$n=4$$ mà đã sát $$1/e \approx 0{,}3679$$!

### Giải thích: Khuôn mẫu chung 3 bước của mọi ứng dụng Bao hàm – Loại trừ
1. **Bước 1 — Đặt tên chính xác tập "xấu" $$A_i$$:** Trong $$\varphi(n)$$, $$A_i$$ là "chia hết cho $$p_i$$"; trong toàn ánh, $$A_i$$ là "giá trị $$i$$ không có tiền ảnh"; trong derangement, $$A_i$$ là "người $$i$$ nhận đúng mũ của mình".
2. **Bước 2 — Khai thác tính đối xứng để rút gọn tổng:** Khi mọi giao của $$k$$ tập đều có **cùng lực lượng** $$g(k)$$ (như $$(n-k)^m$$ ở toàn ánh hay $$(n-k)!$$ ở derangement), tổng dài $$2^n$$ số hạng lập tức co gọn thành tổng $$n+1$$ số hạng: $$\sum_{k=0}^n (-1)^k \binom{n}{k} g(k)$$.
3. **Bước 3 — Nhận diện chuỗi Taylor ẩn bên trong:** Ở bài toán derangement, $$\binom{n}{k}(n-k)! = \frac{n!}{k!}$$, nên $$D_n = n! \sum_{k=0}^n \frac{(-1)^k}{k!}$$ — đúng là tổng riêng bậc $$n$$ của chuỗi Taylor cho $$e^{-1}$$, giải thích tại sao $$D_n = \text{round}(n!/e)$$ với mọi $$n \ge 1$$!

$$D_n = n!\sum_{k=0}^n \frac{(-1)^k}{k!} \approx \frac{n!}{e}, \qquad \text{Onto}(m,n) = \sum_{k=0}^n (-1)^k \binom{n}{k}(n-k)^m.$$

## Bài tập

### Bài tập 1

Tính $$\phi(12)$$ bằng công thức $$n \prod(1 - 1/p_i)$$.

<details>
<summary>Đáp án</summary>

Ta có $$12 = 2^2 \cdot 3$$, nên $$\phi(12) = 12(1 - 1/2)(1 - 1/3) = 12 \cdot \frac{1}{2} \cdot \frac{2}{3} = 4$$.

</details>

### Bài tập 2

Có bao nhiêu ánh xạ toàn ánh từ tập 3 phần tử sang tập 2 phần tử?

<details>
<summary>Đáp án</summary>

$$\text{Surj}(3,2) = 2^3 - \binom{2}{1}1^3 = 8 - 2 = 6$$.

</details>

### Bài tập 3

Tính $$!4$$ (số derangement của 4 phần tử).

<details>
<summary>Đáp án</summary>

$$!4 = 4!\left(1 - 1 + \frac{1}{2} - \frac{1}{6} + \frac{1}{24}\right) = 24 \cdot \frac{9}{24} = 9$$.

</details>

---

## Xem thêm / Video gợi ý

- <a href="https://www.youtube.com/watch?v=FMc7pZbvWKA">Logical Equivalences | Prepositional Logic | Discrete Mathematics</a> — NotesForMsc (Truth table proof + laws)
- [Discrete Math Full Course — Logic & Proofs](https://www.youtube.com/playlist?list=PLHXZ9OQGMqxersk8fUxiUMSIx0DBqsKZS) — Trefor Bazett (Complete semester playlist)


## Tóm tắt

- **Sàng Legendre**: loại bội của các số nguyên tố không vượt quá $$\sqrt N$$, minh họa cách dùng bao hàm–loại trừ trên tập số nguyên.
- **Hàm phi Euler** $$\phi(n)$$: $$\phi(n) = n \prod (1 - 1/p_i)$$, chứng minh bằng cách loại các số chia hết cho từng thừa số nguyên tố $$p_i$$.
- **Số toàn ánh**: $$\text{Surj}(m,n) = \sum_{k=0}^{n} (-1)^k \binom{n}{k}(n-k)^m$$.
- **Derangement** $$!n$$: $$!n = n! \sum_{k=0}^{n} (-1)^k/k!$$.
- **Tô màu và ràng buộc**: số cấu hình hợp lệ bằng tổng số cấu hình trừ đi hợp của các tập vi phạm.

Ở bài tiếp theo, chúng ta sẽ tổng hợp các ứng dụng mở rộng của **hàm sinh** trong phép đếm, xác suất và lý thuyết mã hóa.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=Y0CYHMqomgI">[Discrete Mathematics] Inclusion Exclusion Problems</a> — TrevTutor, tiếng Anh. Các bài toán ứng dụng nguyên lý bao hàm–loại trừ.
- <a href="https://www.youtube.com/watch?v=BOFWLhH0Igo">[Discrete Mathematics] Derangements</a> — TrevTutor, tiếng Anh. Bài toán hoán vị không điểm cố định — ứng dụng kinh điển của nguyên lý.
- <a href="https://www.youtube.com/watch?v=D1T3xy_vtxU">[Discrete Mathematics] Inclusion-Exclusion: At Least &amp; Exactly</a> — TrevTutor, tiếng Anh. Cách chuyển đổi giữa điều kiện “ít nhất” và “đúng bằng” thường gặp trong bài tập.
