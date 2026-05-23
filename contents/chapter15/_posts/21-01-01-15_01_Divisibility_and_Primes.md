---
layout: post
title: "Tính chia hết và Số nguyên tố"
categories: chapter15
date: 2021-01-01
order: 1
required: true
lang: en
---

# Tính chia hết và Số nguyên tố

Khi máy tính mã hóa dữ liệu, sinh khóa, kiểm tra tính hợp lệ của số học modulo hay phân tích cấu trúc của các số nguyên, nó đang chạm tới một vùng rất cổ điển của toán học: **lý thuyết số**.


Lý thuyết số trong chương này không đứng riêng lẻ, nó là nền cho mã hóa, kiểm tra tính đúng đắn và nhiều cơ chế bảo mật hiện đại.
Mọi thứ thường bắt đầu từ hai khái niệm nền nhất, **tính chia hết** và **số nguyên tố**. Chúng nghe cơ bản, nhưng lại là viên gạch đầu tiên cho đồng dư, thuật toán Euclid, RSA và nhiều ứng dụng quan trọng trong khoa học máy tính.

Điểm đáng học ở đây là cấu trúc. Các số nguyên không chỉ là dãy số để tính toán, chúng có quy luật phân rã và quan hệ chia hết rất sâu. Hiểu nền đó giúp các chủ đề mật mã và thuật toán số học phía sau trở nên tự nhiên hơn nhiều.

Trong bài này, chúng ta sẽ bắt đầu từ những khái niệm nền của lý thuyết số và xem vì sao chúng lại có sức sống mạnh đến vậy trong CS hiện đại.

## Mục tiêu học tập

Hãy đọc mục tiêu như danh sách năng lực cần đạt sau bài, vì chúng cho biết bạn nên hiểu gì, làm được gì và áp dụng vào đâu.

Sau bài học này, sinh viên có thể:

- **Vận dụng** định lý chia và thuật toán chia.
- **Kiểm tra** một số có phải số nguyên tố không bằng các phương pháp cơ bản.
- **Tính** ước chung lớn nhất (GCD) bằng thuật toán Euclid.
- **Phân tích** một số ra thừa số nguyên tố.
- **Giải thích** Định lý Cơ bản của Số học.

**Từ khóa**: Chia hết (divisibility), số nguyên tố (prime), ước chung lớn nhất (GCD), thuật toán Euclid, định lý cơ bản số học.

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter15/prime_spiral.svg" alt="Xoắn ốc Ulam — các số nguyên tố được đánh dấu trên một đường xoắn ốc các số tự nhiên" width="70%" height="70%">
  <figcaption style="text-align: center;">Hình 15.1 — Xoắn ốc Ulam: các số nguyên tố (chấm đen) trên đường xoắn ốc các số tự nhiên. Một số đường chéo chứa nhiều số nguyên tố bất thường.</figcaption>
</p>
</figure>

## 1. Tính chia hết

**Định nghĩa**: Cho $$a, b \in \mathbb{Z}$$ với $$b \neq 0$$. Ta nói $$b$$ **chia hết** $$a$$, ký hiệu $$b \mid a$$, nếu tồn tại số nguyên $$c$$ sao cho $$a = bc$$.

**Ví dụ**:
- $$3 \mid 12$$ vì $$12 = 3 \times 4$$
- $$7 \nmid 20$$ vì 20 không chia hết cho 7
- $$1 \mid n$$ với mọi số nguyên $$n$$
- $$n \mid 0$$ với mọi $$n \neq 0$$

### Định lý Chia (Division Algorithm)

**Định lý**: Cho $$a \in \mathbb{Z}$$ và $$d \in \mathbb{Z}^+$$. Tồn tại duy nhất cặp số nguyên $$q$$ (thương) và $$r$$ (số dư) sao cho:

$$a = dq + r, \quad 0 \leq r < d$$

Ký hiệu: $$a \textbf{ div } d = q$$, $$a \textbf{ mod } d = r$$.

<div class="content-box example-box" markdown="1">
**Ví dụ**:
- $$a = 17, d = 5$$: $$17 = 5 \times 3 + 2$$ → $$q = 3, r = 2$$
- $$a = -17, d = 5$$: $$-17 = 5 \times (-4) + 3$$ → $$q = -4, r = 3$$ (dư luôn không âm)
</div>

<div class="content-box warning-box" markdown="1">
**Sai lầm phổ biến**: Nhiều lập trình viên nghĩ rằng `-17 % 5` trong Python cho kết quả -2. Nhưng về mặt toán học, số dư phải luôn không âm. Python thực sự trả về 3 cho `-17 % 5` — đúng theo định nghĩa toán học! Ngôn ngữ C/C++ trả về -2 (số dư âm). Đây là một cạm bẫy (pitfall) nổi tiếng.
</div>

## 2. Số nguyên tố

**Định nghĩa**: Số nguyên $$p > 1$$ là **số nguyên tố** (prime) nếu ước dương duy nhất của nó là 1 và chính nó. Số $$n > 1$$ không nguyên tố gọi là **hợp số** (composite).

<div class="content-box example-box" markdown="1">
- **Nguyên tố**: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...
- **Hợp số**: 4, 6, 8, 9, 10, 12, 14, 15, ...
- **Lưu ý**: 1 không phải nguyên tố cũng không phải hợp số.
</div>

### Định lý Cơ bản của Số học

**Định lý**: Mọi số nguyên $$n > 1$$ đều có thể biểu diễn **duy nhất** dưới dạng tích các số nguyên tố (không kể thứ tự):

$$n = p_1^{e_1} \times p_2^{e_2} \times \cdots \times p_k^{e_k}$$

<div class="content-box example-box" markdown="1">
- $$60 = 2^2 \times 3 \times 5$$
- $$84 = 2^2 \times 3 \times 7$$
- $$1001 = 7 \times 11 \times 13$$
</div>

<div class="content-box insight-box" markdown="1">
**Tính duy nhất**: Đây là lý do người ta gọi số nguyên tố là "nguyên tử" của số học. Giống như mọi chất đều có công thức hóa học duy nhất, mọi số đều có phân tích thừa số nguyên tố duy nhất. Điều này không hề hiển nhiên — có những cấu trúc đại số khác (như vành số phức) mà ở đó tính duy nhất không còn đúng!
</div>

### Sàng Eratosthenes

Tìm tất cả số nguyên tố $$\leq n$$:

```
THUẬT TOÁN: Sàng-Eratosthenes(n)
1. Tạo mảng prime[2..n], tất cả = TRUE
2. FOR i ← 2 TO √n DO
3.     IF prime[i] = TRUE THEN
4.         FOR j ← i*i TO n STEP i DO
5.             prime[j] ← FALSE
6.         END FOR
7.     END IF
8. END FOR
9. RETURN tất cả i có prime[i] = TRUE
```

<div class="content-box insight-box" markdown="1">
**Tại sao bắt đầu từ $$i^2$$?** Vì các bội số nhỏ hơn $$i^2$$ (như $$2i, 3i, \ldots, (i-1)i$$) đã được đánh dấu bởi các số nguyên tố nhỏ hơn $$i$$ rồi. Cải tiến này giúp sàng Eratosthenes đạt độ phức tạp $$O(n \log \log n)$$ — cực kỳ hiệu quả.
</div>

<div class="interactive-tool" markdown="1">
<div data-demo="modular-calculator"></div>
</div>
<script src="{{ '/public/js/modular-calculator.js' | relative_url }}"></script>

## 3. Ước chung Lớn nhất (GCD)

**Định nghĩa**: Cho $$a, b \in \mathbb{Z}$$, không đồng thời bằng 0. Ước chung lớn nhất của $$a$$ và $$b$$, ký hiệu $$\gcd(a, b)$$, là số nguyên dương lớn nhất $$d$$ sao cho $$d \mid a$$ và $$d \mid b$$.

<div class="content-box example-box" markdown="1">
- $$\gcd(12, 18) = 6$$
- $$\gcd(17, 23) = 1$$ → 17 và 23 là **nguyên tố cùng nhau** (relatively prime)
- $$\gcd(0, 5) = 5$$
- $$\gcd(0, 0)$$ — không xác định
</div>

### Thuật toán Euclid

Dựa trên nguyên lý: $$\gcd(a, b) = \gcd(b, a \bmod b)$$.

```
THUẬT TOÁN: Euclid(a, b)   // a ≥ b ≥ 0
1. WHILE b ≠ 0 DO
2.     r ← a MOD b
3.     a ← b
4.     b ← r
5. END WHILE
6. RETURN a
```

<div class="content-box example-box" markdown="1">
Tính $$\gcd(252, 105)$$:

| Bước | a | b | r = a mod b |
|:------|:---|---:|:---|
| 1 | 252 | 105 | 42 |
| 2 | 105 | 42 | 21 |
| 3 | 42 | 21 | 0 |
| 4 | 21 | 0 | dừng |

$$\gcd(252, 105) = 21$$
</div>

<div class="content-box insight-box" markdown="1">
**Tốc độ của Euclid**: Thuật toán Euclid chạy trong $$O(\log(\min(a,b)))$$ bước. Lý do: sau mỗi bước, tích $$a \times b$$ giảm ít nhất một nửa. Với số 2048-bit (như trong RSA), thuật toán chỉ mất tối đa khoảng 2000 bước — cực kỳ nhanh!
</div>

<div class="interactive-tool" markdown="1">
**Demo tương tác đề xuất**: Người học nhập hai số nguyên, công cụ chạy thuật toán Euclid từng bước và hiển thị ước chung lớn nhất.
<div data-demo="euclidean-algorithm"></div>
</div>
<script src="{{ '/public/js/euclidean-algorithm.js' | relative_url }}"></script>

### Đồng nhất thức Bézout

Tồn tại số nguyên $$s, t$$ sao cho: $$\gcd(a, b) = s \cdot a + t \cdot b$$.

Thuật toán Euclid mở rộng tính $$s, t$$ đồng thời với GCD — công cụ then chốt để tính nghịch đảo modulo trong mật mã RSA.

## Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Số nguyên tố là nền tảng của mật mã học hiện đại (RSA, Diffie-Hellman), hàm băm (hash function), sinh số giả ngẫu nhiên, và kiểm tra tính toàn vẹn dữ liệu (checksum). Thuật toán Euclid chạy trong $$O(\log(\min(a,b)))$$ — cực kỳ nhanh, được dùng trong mọi thư viện mật mã.

**Một ứng dụng thú vị**: Khi bạn kết nối đến một trang web HTTPS, trình duyệt của bạn đang dùng số học modulo và thuật toán Euclid hàng trăm lần — để xác thực chứng chỉ, trao đổi khóa, và mã hóa dữ liệu. Tất cả diễn ra trong chưa đầy một giây.

<div class="interactive-tool" markdown="1" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
<h3 style="color: #6f42c1;">🔬 Công cụ Tương tác: Sàng Eratosthenes</h3>
<p>Công cụ trực quan hóa quá trình sàng Eratosthenes. Bạn sẽ thấy từng bước — các số được đánh dấu và loại bỏ dần. <strong>Hãy thử:</strong> Tìm tất cả số nguyên tố từ 1 đến 200 và quan sát mô hình xuất hiện của chúng.</p>
</div>

## Bài tập

Khi làm bài tập, nên bắt đầu bằng cách xác định dữ kiện, dạng bài và công cụ phù hợp trước khi tính toán. Cách tiếp cận này thường giúp tránh sai từ bước đầu.

1. Tìm thương và số dư của $$a = -45$$ chia cho $$d = 7$$.
2. Dùng sàng Eratosthenes tìm tất cả số nguyên tố từ 1 đến 100.
3. Tính $$\gcd(12345, 54321)$$ bằng thuật toán Euclid.
4. Phân tích $$360$$ và $$504$$ ra thừa số nguyên tố.
5. **Thử thách**: Chứng minh rằng có vô hạn số nguyên tố (định lý Euclid).

<details>
<summary>Hướng dẫn bài 5</summary>

Giả sử chỉ có hữu hạn số nguyên tố: $$p_1, p_2, \ldots, p_k$$. Xét số:

$$N = p_1 \times p_2 \times \cdots \times p_k + 1$$

- N > 1, nên N phải có ít nhất một ước nguyên tố $$p$$.
- Nếu $$p$$ là một trong các $$p_i$$, thì $$p \mid N$$ và $$p \mid p_1 \times p_2 \times \cdots \times p_k$$.
- Suy ra $$p \mid (N - p_1 \times p_2 \times \cdots \times p_k) = 1$$. Vô lý!

Vậy giả sử sai. Có vô hạn số nguyên tố. □

Đây là một trong những chứng minh đẹp nhất trong toán học — chỉ vài dòng nhưng đã đứng vững hơn 2300 năm.
</details>

## Tóm tắt

- **Chia hết**: $$b \mid a$$ nếu tồn tại $$c$$ sao cho $$a = bc$$.
- **Định lý chia**: $$a = dq + r, 0 \leq r < d$$.
- **Số nguyên tố**: chỉ chia hết cho 1 và chính nó.
- **Định lý Cơ bản**: phân tích thừa số nguyên tố là duy nhất.
- **GCD**: ước chung lớn nhất, tính bằng thuật toán Euclid $$O(\log(\min(a,b)))$$.
- **Thuật toán Euclid**: $$\gcd(a, b) = \gcd(b, a \bmod b)$$.

Trong bài tiếp theo, chúng ta sẽ tìm hiểu về số học modulo — "đồng hồ số học" và nền tảng của mật mã hiện đại.

## Tài liệu Tham khảo

1. Euclid, *Elements*, Quyển VII, ~300 TCN — chứa thuật toán Euclid gốc và chứng minh về vô hạn số nguyên tố.
2. G.H. Hardy và E.M. Wright, *An Introduction to the Theory of Numbers*, Oxford University Press — kinh điển về lý thuyết số.
3. "The Prime Pages" (primes.utm.edu) — cơ sở dữ liệu lớn nhất về số nguyên tố và các kỷ lục.
