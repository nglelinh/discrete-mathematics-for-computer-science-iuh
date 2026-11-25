---
layout: post
title: "Tính chia hết và Số nguyên tố"
categories: chapter15
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Định lý chia, số nguyên tố, định lý cơ bản của số học, sàng Eratosthenes, ước chung lớn nhất (GCD) và thuật toán Euclid — nền tảng cho đồng dư và mật mã."
---

> **Câu chuyện mở đầu:** Suốt hai thiên niên kỷ kể từ Euclid, các nhà toán học thuần túy từng tự hào rằng **Lý thuyết Số** — đặc biệt là số nguyên tố và phép chia có dư — là ngành toán "trong sạch nhất", hoàn toàn vô dụng ngoài đời thực! Thế nhưng ngày nay, mỗi khi bạn chuyển khoản ngân hàng hay đăng nhập vào một trang web `https://`, chính **thuật toán Euclid mở rộng** (2.300 năm tuổi!) và **sự khó khăn của việc phân tích thừa số nguyên tố** đang bảo vệ dữ liệu của bạn từng mili giây!

<div class="textbook-epigraph" markdown="1">

"Mathematics is the queen of the sciences and number theory is the queen of mathematics."

<span class="epigraph-attribution">— Carl Friedrich Gauss</span>

</div>

**Lý thuyết số** nghiên cứu các tính chất của số nguyên như tính chia hết, số nguyên tố và ước chung. Trong khoa học máy tính, các cấu trúc này xuất hiện thường xuyên trong việc sinh khóa, tính toán modulo, phân tích thừa số và xây dựng nhiều giao thức bảo mật. Bài học này trình bày các khái niệm nền tảng: định lý chia, số nguyên tố, định lý cơ bản của số học, ước chung lớn nhất (GCD) và thuật toán Euclid.

![Euclid](/discrete-mathematics-for-computer-science-iuh/img/course/Euclid.jpg)

<p class="textbook-figure-caption" data-figure="15.1">Euclid (~300 TCN) — tác giả thuật toán tìm GCD và chứng minh có vô hạn số nguyên tố.</p>

![Phân tích thừa số nguyên tố](/discrete-mathematics-for-computer-science-iuh/img/course/PrimeDecompositionExample.svg)

<p class="textbook-figure-caption" data-figure="15.2">Định lý cơ bản của số học: mọi số nguyên $$n>1$$ đều phân tích duy nhất (không kể thứ tự) thành tích các lũy thừa số nguyên tố.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Áp dụng** định lý chia: $$a = dq + r$$ với $$0 \le r < d$$.
- **Phân biệt** số nguyên tố với hợp số và phát biểu định lý cơ bản của số học.
- **Tính** $$\gcd(a,b)$$ bằng thuật toán Euclid và phát biểu đồng nhất thức Bézout.
- **Mô tả** sàng Eratosthenes cùng độ phức tạp thời gian $$O(n\log\log n)$$.
- **Liên hệ** GCD và thuật toán Euclid với nghịch đảo modulo và mật mã học ở các bài sau.

**Từ khóa**: chia hết (divisibility), số nguyên tố (prime), GCD, thuật toán Euclid, định lý cơ bản số học, Bézout.

</div>

## Kiến thức cần nhớ: Tính chia hết, Số nguyên tố và Thuật toán Euclid

### 1. Thuật toán Chia & Định lý Cơ bản của Số học (FTA)
- **Bản chất:** Mọi số nguyên $$a$$ chia cho $$d > 0$$ đều có thương $$q$$ và số dư $$r$$ duy nhất ($$a = dq + r,\; 0 \le r < d$$). Định lý Cơ bản của Số học khẳng định mọi số nguyên $$n \ge 2$$ đều phân tích **duy nhất** thành tích các lũy thừa số nguyên tố — các số nguyên tố chính là **bảng tuần hoàn nguyên tử** của tập số nguyên $$\mathbb{Z}$$!

### 2. Ước chung lớn nhất (GCD) & Định lý Bézout
- **Bản chất:** Thuật toán Euclid dựa trên đẳng thức đơn giản $$\gcd(a, b) = \gcd(b, a \bmod b)$$ để tìm $$\gcd(a, b)$$ trong thời gian siêu nhanh $$O(\log b)$$ (không cần phân tích thừa số!). Chạy ngược lại (**Euclid mở rộng**) cho ngay hai hệ số Bézout $$x, y \in \mathbb{Z}$$ thỏa mãn $$ax + by = \gcd(a, b)$$ — chìa khóa tìm nghịch đảo modulo trong RSA!

### 3. Phân bố Số nguyên tố & Sàng Eratosthenes
- **Bản chất:** Có vô hạn số nguyên tố (chứng minh phản chứng tuyệt đẹp của Euclid!), mật độ giảm dần theo **Định lý Số nguyên tố** $$\pi(x) \sim x / \ln x$$, và Sàng Eratosthenes liệt kê mọi số nguyên tố $$\le N$$ trong $$O(N \log\log N)$$!

## Ví dụ tính tay làm từng bước: Chạy Thuật toán Euclid mở rộng cho $$(a, b) = (252, 198)$$

1. **Chiều xuôi (chia liên tiếp để tìm $$\gcd$$):**
   - $$252 = 1 \cdot 198 + 54$$
   - $$198 = 3 \cdot 54 + 36$$
   - $$54 = 1 \cdot 36 + 18$$
   - $$36 = 2 \cdot 18 + 0 \implies \gcd(252, 198) = 18$$!
2. **Chiều ngược (thế ngược để tìm hệ số Bézout $$252x + 198y = 18$$):**
   - Từ dòng 3: $$18 = 54 - 1\cdot 36$$.
   - Thế $$36 = 198 - 3\cdot 54$$ từ dòng 2:
     $$18 = 54 - (198 - 3\cdot 54) = 4\cdot 54 - 1\cdot 198$$.
   - Thế $$54 = 252 - 1\cdot 198$$ từ dòng 1:
     $$18 = 4(252 - 198) - 198 = 4\cdot 252 + (-5)\cdot 198!$$
   - **Kiểm tra trực tiếp bằng tay:** $$4 \times 252 - 5 \times 198 = 1008 - 990 = 18$$! ✓ (Cặp Bézout là $$x = 4,\; y = -5$$!)

### Giải thích: Tại sao Thuật toán Euclid nhanh đến khó tin?
#### Bước 1: Bất biến GCD qua phép chia lấy dư
Mọi ước chung của $$(a, b)$$ đều chia hết cho $$r = a - qb$$ và ngược lại $$\implies \gcd(a, b) = \gcd(b, r)$$.

#### Bước 2: Sau tối đa 2 bước, số dư luôn giảm ít nhất một nửa!
Thật vậy: nếu $$r \le b/2$$ thì xong ngay bước 1; nếu $$r > b/2$$ thì ở bước kế tiếp $$b \bmod r = b - r < b/2$$! Nhờ tốc độ chia đôi này, ngay cả hai số nguyên **1000 chữ số** cũng chỉ cần dưới **$$2\log_2(10^{1000}) \approx 6600$$ phép chia**!

#### Bước 3: Trường hợp xấu nhất gọi tên Dãy Fibonacci (Định lý Lamé)
Cặp số làm thuật toán Euclid chạy nhiều bước nhất (với cùng độ lớn) chính là hai số Fibonacci liên tiếp $$(F_{k+1}, F_k)$$ vì mọi thương đều bằng $$1$$!

#### Bước 4: Sự bất đối xứng vàng của Mật mã học
Tìm $$\gcd$$ hay kiểm tra một số 1000 chữ số có nguyên tố không tốn vài mili giây, nhưng **phân tích tích $$N = p \cdot q$$ của hai số nguyên tố 1000 chữ số** lại cực kỳ khó — chính khoảng cách khổng lồ này nuôi sống hệ mật mã RSA ở bài 15.03!

$$
\text{Phép chia }a = bq + r
\;\xrightarrow{\;\text{Euclid }O(\log b)\;}\;
\gcd(a, b)
\;\xrightarrow{\;\text{Thế ngược}\;}\;
ax + by = \gcd(a, b) \text{ (Bézout)}.
$$

## Tính chia hết

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cho $$a, b \in \mathbb{Z}$$ với $$b \neq 0$$. Ta nói $$b$$ **chia hết** $$a$$ (hay $$a$$ chia hết cho $$b$$), ký hiệu $$b \mid a$$, nếu tồn tại $$c \in \mathbb{Z}$$ sao cho $$a = bc$$. Ngược lại, ta viết $$b \nmid a$$.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 1.**

- $$3 \mid 12$$ vì $$12 = 3 \cdot 4$$.
- $$7 \nmid 20$$.
- $$1 \mid n$$ với mọi số nguyên $$n$$; $$n \mid 0$$ với mọi $$n \neq 0$$.

</div>

### Định lý chia

<div class="textbook-theorem" markdown="1">

**Định lý** (Division algorithm). Cho $$a \in \mathbb{Z}$$ và $$d \in \mathbb{Z}^+$$. Tồn tại **duy nhất** cặp số nguyên $$q$$ (thương) và $$r$$ (số dư) sao cho

$$
a = dq + r, \qquad 0 \le r < d.
$$

Ký hiệu thường dùng là $$a \operatorname{div} d = q$$ và $$a \bmod d = r$$.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2.**

- Với $$a = 17$$, $$d = 5$$: $$17 = 5 \cdot 3 + 2$$, suy ra $$q=3$$ và $$r=2$$.
- Với $$a = -17$$, $$d = 5$$: $$-17 = 5 \cdot (-4) + 3$$, suy ra $$q=-4$$ và $$r=3$$ (số dư phải **không âm**).

Trong Python, `(-17) % 5` cho kết quả bằng $$3$$, khớp với định nghĩa toán học. Một số ngôn ngữ khác (như C/C++ với phép chia làm tròn hướng về 0) có thể trả về số dư âm, nên khi cài đặt cần chú ý thống nhất quy ước.

</div>

## Số nguyên tố

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Số nguyên $$p > 1$$ được gọi là **số nguyên tố** (*prime*) nếu các ước dương duy nhất của nó là $$1$$ và $$p$$. Số nguyên $$n > 1$$ không phải số nguyên tố được gọi là **hợp số** (*composite*). Số $$1$$ **không** là số nguyên tố và cũng **không** là hợp số.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 3.** Các số nguyên tố đầu tiên là $$2,3,5,7,11,\ldots$$; các hợp số đầu tiên là $$4,6,8,9,10,\ldots$$. Số $$2$$ là số nguyên tố chẵn duy nhất.

</div>

### Định lý cơ bản của số học

<div class="textbook-theorem" markdown="1">

**Định lý** (Fundamental theorem of arithmetic). Mọi số nguyên $$n > 1$$ đều biểu diễn được **duy nhất** (không kể thứ tự các thừa số) dưới dạng

$$
n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k},
$$

với $$p_1 < p_2 < \cdots < p_k$$ là các số nguyên tố và $$e_i \ge 1$$.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 4.** $$60 = 2^2 \cdot 3 \cdot 5$$; $$84 = 2^2 \cdot 3 \cdot 7$$; $$1001 = 7 \cdot 11 \cdot 13$$.

</div>

Tính duy nhất của phép phân tích là lý do số nguyên tố thường được ví như các “nguyên tử” của số học: mọi số nguyên $$n>1$$ đều có một cấu trúc thừa số cố định. Cần lưu ý rằng nhiều cấu trúc đại số khác **không** có tính phân tích duy nhất tương tự.

### Sàng Eratosthenes

Thuật toán tìm mọi số nguyên tố không vượt quá $$n$$:

```text
Sàng-Eratosthenes(n)
1. Đánh dấu mọi k ∈ {2..n} là “ứng viên”
2. FOR i ← 2 TO ⌊√n⌋ DO
3.     IF i còn là ứng viên THEN
4.         FOR j ← i², i²+i, i²+2i, … (≤ n) DO
5.             loại j khỏi ứng viên
6. RETURN các ứng viên còn lại
```

Ta chỉ cần bắt đầu gạch từ $$i^2$$ vì các bội nhỏ hơn là $$2i,\ldots,(i-1)i$$ đã bị loại bởi các số nguyên tố nhỏ hơn $$i$$. Độ phức tạp thời gian cổ điển của thuật toán là $$O(n \log\log n)$$.

## Ước chung lớn nhất (GCD)

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cho $$a, b \in \mathbb{Z}$$ không đồng thời bằng 0. **Ước chung lớn nhất** $$\gcd(a,b)$$ là số nguyên dương lớn nhất $$d$$ sao cho $$d \mid a$$ và $$d \mid b$$. Nếu $$\gcd(a,b)=1$$, ta nói $$a$$ và $$b$$ **nguyên tố cùng nhau** (*coprime* hoặc *relatively prime*).

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 5.** $$\gcd(12,18)=6$$; $$\gcd(17,23)=1$$; $$\gcd(0,5)=5$$. Theo quy ước trên, cặp $$(0,0)$$ không xác định GCD.

</div>

### Thuật toán Euclid

<div class="textbook-theorem" markdown="1">

**Định lý** (Euclid). Với $$b > 0$$,

$$
\gcd(a,b) = \gcd(b,\, a \bmod b).
$$

Quá trình này được lặp lại cho đến khi số dư bằng 0; ước chung lớn nhất chính là số còn lại khác 0.

</div>

![Euclid từng bước](/discrete-mathematics-for-computer-science-iuh/img/course/Number_euclid_steps.svg)

<p class="textbook-figure-caption" data-figure="15.3">Các bước của thuật toán Euclid cho $$\gcd(252,105)=21$$.</p>

<div class="textbook-example" markdown="1">

**Ví dụ 6.** Tính $$\gcd(252,105)$$:

| Bước | $$a$$ | $$b$$ | $$a \bmod b$$ |
|:---:|:---:|:---:|:---:|
| 1 | 252 | 105 | 42 |
| 2 | 105 | 42 | 21 |
| 3 | 42 | 21 | 0 |

Kết quả: $$\gcd(252,105) = 21$$.

</div>

Số bước thực hiện của thuật toán thuộc $$O(\log \min(\vert a\vert ,\vert b\vert ))$$, đủ nhanh để xử lý các số nguyên dài hàng nghìn bit trong các thư viện mật mã.

### Video ngắn: Euclid lát hình chữ nhật

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/euclid-gcd-tiling.mp4"></video>
</div>

Hình chữ nhật kích thước $$252\times105$$ được lát dần bằng các hình vuông lớn nhất có thể: $$252=2\cdot105+42$$, $$105=2\cdot42+21$$ và $$42=2\cdot21+0$$. Cạnh của hình vuông cuối cùng chính là $$\gcd(252,105)=21$$, nhờ đó toàn bộ hình chữ nhật ban đầu có thể lát kín bằng các ô vuông $$21\times21$$.

### Đồng nhất thức Bézout

<div class="textbook-theorem" markdown="1">

**Định lý** (Bézout). Tồn tại các số nguyên $$s,t \in \mathbb{Z}$$ sao cho

$$
\gcd(a,b) = sa + tb.
$$

</div>

Thuật toán **Euclid mở rộng** tính đồng thời cả $$s,t$$ và $$\gcd(a,b)$$. Đây là công cụ then chốt để tìm **nghịch đảo modulo** khi $$\gcd(a,n)=1$$ (Mục 15.2) cũng như tạo khóa trong hệ mật RSA (Mục 15.3).

## Thử nghiệm tương tác

Bạn có thể thử nghiệm với máy tính modulo cơ bản và theo dõi thuật toán Euclid từng bước (kèm hệ số Bézout) dưới đây:

<div class="interactive-demo" markdown="1">
<div data-demo="modular-calculator"></div>
</div>
<script src="{{ '/public/js/modular-calculator.js' | relative_url }}"></script>

<div class="interactive-demo" markdown="1">
<div data-demo="euclidean-algorithm"></div>
</div>
<script src="{{ '/public/js/euclidean-algorithm.js' | relative_url }}"></script>

## Liên hệ khoa học máy tính

- **RSA và Diffie–Hellman**: dựa trên số nguyên tố lớn, GCD và thuật toán Euclid mở rộng.
- **Checksum và mã ISBN**: sử dụng tổ hợp tuyến tính theo modulo $$m$$.
- **HTTPS**: trình duyệt thực hiện nhiều phép tính modulo và Euclid trong quá trình bắt tay TLS — thuộc cùng lớp thuật toán được giới thiệu trong bài này và các mục 15.2–15.3.

### Minh họa tương tác

Minh họa thuật toán Euclid và hệ thức Bézout từng bước, kèm sàng nguyên tố ở thẻ "Sàng":

<div class="interactive-demo" markdown="1">
<div data-demo="numtheory-explainer" data-tab="euclid"></div>
</div>
<script src="{{ '/public/js/explainers/numtheory-explainer.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Tìm thương $$q$$ và số dư $$r$$ khi chia $$a = -45$$ cho $$d = 7$$.

<details>
<summary>Đáp án</summary>

Ta cần tìm $$q, r$$ sao cho $$-45 = 7q + r$$ với $$0 \le r < 7$$. Chọn $$q = -7$$, ta có $$7\cdot(-7) = -49$$ và $$-45 - (-49) = 4$$. Vậy $$q=-7$$ và $$r=4$$.

</details>

### Bài tập 2

Dùng sàng Eratosthenes để liệt kê tất cả các số nguyên tố $$\le 30$$.

<details>
<summary>Đáp án</summary>

$$2,3,5,7,11,13,17,19,23,29$$.

</details>

### Bài tập 3

Tính $$\gcd(12345, 54321)$$ bằng thuật toán Euclid (trình bày các bước chia chính).

<details>
<summary>Đáp án</summary>

$$54321 = 4\cdot 12345 + 4941$$,  
$$12345 = 2\cdot 4941 + 2463$$,  
$$4941 = 2\cdot 2463 + 15$$,  
$$2463 = 164\cdot 15 + 3$$,  
$$15 = 5\cdot 3 + 0$$.  
Vậy $$\gcd(12345, 54321) = 3$$.

</details>

### Bài tập 4

Phân tích $$360$$ và $$504$$ ra thừa số nguyên tố.

<details>
<summary>Đáp án</summary>

$$360 = 2^3 \cdot 3^2 \cdot 5$$,  
$$504 = 2^3 \cdot 3^2 \cdot 7$$.

</details>

### Bài tập 5

Chứng minh có vô hạn số nguyên tố (định lý Euclid).

<details>
<summary>Đáp án</summary>

Giả sử chỉ có hữu hạn số nguyên tố là $$p_1,\ldots,p_k$$. Đặt

$$
N = p_1 p_2 \cdots p_k + 1.
$$

Vì $$N > 1$$ nên $$N$$ có ít nhất một ước nguyên tố $$p$$. Nếu $$p = p_i$$ với một chỉ số $$i$$ nào đó thì $$p \mid N$$ và $$p \mid p_1\cdots p_k$$, suy ra $$p \mid 1$$ — điều này vô lý. Vậy giả sử ban đầu là sai, nghĩa là có vô hạn số nguyên tố.

</details>

## Tóm tắt

1. **Tính chia hết** $$b\mid a$$ và **định lý chia** với số dư không âm $$0\le r < d$$.
2. **Số nguyên tố, hợp số** và **định lý cơ bản của số học** về tính phân tích duy nhất.
3. **Sàng Eratosthenes** dùng để liệt kê mọi số nguyên tố $$\le n$$.
4. **Ước chung lớn nhất (GCD)** tính qua thuật toán Euclid; **đồng nhất thức Bézout** là nền tảng cho nghịch đảo modulo.

Bài học tiếp theo sẽ trình bày về **đồng dư**, các phép toán modulo, nghịch đảo modulo, định lý số dư Trung Hoa (CRT) và lũy thừa modulo nhanh.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=K2YmMpulFA4">DIVISIBILITY - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giới thiệu về tính chia hết, ước và bội.
- <a href="https://www.youtube.com/watch?v=Dorm0_UyKFw">[Discrete Mathematics] Primes and GCD</a> — TrevTutor, tiếng Anh. Số nguyên tố và ước chung lớn nhất.
- <a href="https://www.youtube.com/watch?v=inUkhh8-h-I">Proof: There are infinitely many primes numbers</a> — Dr. Trefor Bazett, tiếng Anh. Chứng minh có vô hạn số nguyên tố.
