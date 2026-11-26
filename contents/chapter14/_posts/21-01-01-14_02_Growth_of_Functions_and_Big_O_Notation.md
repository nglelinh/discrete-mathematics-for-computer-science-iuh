---
layout: post
title: "Tăng trưởng của Hàm và Ký hiệu Big-O"
categories: chapter14
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Các ký hiệu tiệm cận Big-O, Omega và Theta; thứ tự các bậc tăng trưởng phổ biến; quy tắc tổng và tích trong phân tích độ phức tạp."
---

> **Câu chuyện mở đầu:** Giả sử thuật toán A mất $$1000n$$ phép tính còn thuật toán B chỉ mất $$n^2$$ phép tính. Với $$n = 10$$, thuật toán B nhanh gấp **100 lần** thuật toán A! Nhưng khi dữ liệu thực tế tăng lên $$n = 10^6$$, thuật toán A chạy trong $$10^9$$ bước (chưa đầy 1 giây), còn thuật toán B tốn $$10^{12}$$ bước (mất gần 15 phút)! Để không bị đánh lừa bởi các hằng số nhỏ và tốc độ phần cứng, khoa học máy tính dùng **ký hiệu tiệm cận $$O, \Omega, \Theta$$** — chiếc kính hiển vi nhìn thẳng vào **tốc độ bùng nổ khi $$n \to \infty$$**.

<div class="textbook-epigraph" markdown="1">

"Ignore machine constants — compare how cost grows with input size."

<span class="epigraph-attribution">— Asymptotic analysis spirit</span>

</div>

Khi so sánh hai thuật toán, ta không chỉ đo thời gian chạy bằng mili-giây trên một máy tính cụ thể, mà đánh giá **tốc độ tăng chi phí theo kích thước đầu vào $$n$$**. Các ký hiệu tiệm cận **Big-O** ($$O$$), **Omega** ($$\Omega$$) và **Theta** ($$\Theta$$) là ngôn ngữ chuẩn để diễn đạt tốc độ tăng trưởng này. Bài học này trình bày định nghĩa, các bậc tăng trưởng thường gặp và các quy tắc biến đổi cơ bản.

![Bậc tăng trưởng](/discrete-mathematics-for-computer-science-iuh/img/course/Algo_big_o_ladder.svg)

<p class="textbook-figure-caption" data-figure="14.3">So sánh tương đối các bậc tăng trưởng: hàm mũ và hàm giai thừa tăng vượt xa đa thức khi $$n$$ lớn.</p>

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Định nghĩa** chính xác các ký hiệu tiệm cận $$O$$, $$\Omega$$ và $$\Theta$$.
- **Chứng minh** quan hệ Big-O đơn giản trực tiếp từ định nghĩa bằng cách chọn cặp hằng số $$c, n_0$$.
- **Sắp xếp** thứ tự tăng trưởng của các hàm cơ bản: $$1$$, $$\log n$$, $$n$$, $$n\log n$$, $$n^2$$, $$2^n$$, $$n!$$.
- **Áp dụng** quy tắc tổng và quy tắc tích trên ký hiệu Big-O.
- **Giải thích** vì sao có thể bỏ qua hằng số nhân và các hạng tử bậc thấp khi $$n$$ đủ lớn.

**Từ khóa**: Big-O, Omega, Theta, asymptotic, growth rate.

</div>

### Video ngắn: Big-O và tốc độ tăng

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/big-o-growth.mp4"></video>
</div>

Video dài khoảng 2 phút 56 giây: so sánh số phép tính của $$n$$, $$n\log n$$, $$n^2$$, $$2^n$$ ($$2^{60}$$ phép tính mất khoảng 36 năm), minh họa các đường tăng trưởng và định nghĩa $$O$$ với $$c, n_0$$ trên đồ thị cho $$3n^2 + 5n + 2 \le 4n^2$$ khi $$n \ge 6$$ (cặp $$c = 10, n_0 = 1$$ trong bài cũng hợp lệ), giới thiệu $$\Omega$$ và $$\Theta$$, các quy tắc rút gọn, cách đếm bước trong vòng lặp và năm lỗi thường gặp.

## Kiến thức cần nhớ: Ký hiệu Tiệm cận $$O, \Omega, \Theta$$ là gì?

### 1. Bộ ba Ký hiệu Tiệm cận (Bachmann–Landau–Knuth)
- **$$f(n) = O(g(n))$$ (Chặn trên — giống dấu $$\le$$):** Tồn tại hằng số $$C > 0$$ và ngưỡng $$n_0$$ sao cho $$\lvert f(n)\rvert \le C\lvert g(n)\rvert$$ với mọi $$n \ge n_0$$.
- **$$f(n) = \Omega(g(n))$$ (Chặn dưới — giống dấu $$\ge$$):** $$\lvert f(n)\rvert \ge c\lvert g(n)\rvert$$ với mọi $$n \ge n_0$$.
- **$$f(n) = \Theta(g(n))$$ (Chặn chặt — giống dấu $$=$$):** Vừa là $$O(g(n))$$ vừa là $$\Omega(g(n))$$!

### 2. Bậc thang Tăng trưởng Kinh điển (từ chậm đến bùng nổ)
$$
O(1) < O(\log n) < O(n) < O(n\log n) < O(n^2) < O(n^3) < O(2^n) < O(n!).
$$
Lưu ý quan trọng: **đa thức bất kỳ $$n^k$$ luôn bị hàm mũ $$2^n$$ (hay $$1.001^n$$) vượt mặt** khi $$n$$ đủ lớn, và **mọi hàm logarit $$\log_a n$$ đều đồng bậc $$\Theta(\log n)$$** vì chỉ khác nhau hằng số đổi cơ số!

### 3. Quy tắc Tổng & Tích (Bỏ hằng số và số hạng bậc thấp)
- $$O(f) + O(g) = O(\max(f, g))$$ (bước chạy chậm nhất chi phối toàn bộ chương trình!).
- $$O(f) \cdot O(g) = O(f \cdot g)$$ (vòng lặp lồng nhau nhân độ phức tạp!).

## Ví dụ tính tay làm từng bước: Chứng minh trực tiếp từ định nghĩa $$3n^2 + 5n + 7 = \Theta(n^2)$$

1. **Chứng minh $$3n^2 + 5n + 7 = O(n^2)$$:** Với mọi $$n \ge 1$$, ta có $$5n \le 5n^2$$ và $$7 \le 7n^2$$, nên:
   $$
   3n^2 + 5n + 7 \le 3n^2 + 5n^2 + 7n^2 = 15n^2.
   $$
   Chọn cặp chứng nhân **$$C = 15,\; n_0 = 1$$** $$\implies 3n^2 + 5n + 7 = O(n^2)$$! ✓
2. **Chứng minh $$3n^2 + 5n + 7 = \Omega(n^2)$$:** Với mọi $$n \ge 1$$, $$5n + 7 > 0$$ nên $$3n^2 + 5n + 7 \ge 3n^2$$. Chọn **$$c = 3,\; n_0 = 1$$** $$\implies \Omega(n^2)$$! ✓
3. **Kết hợp (1) và (2):** $$3n^2 + 5n + 7 = \Theta(n^2)$$!
4. **Phản chứng $$2^{2n} \neq O(2^n)$$:** Xét tỉ số $$\frac{2^{2n}}{2^n} = 2^n \to +\infty$$ khi $$n \to \infty$$ — không thể bị chặn bởi bất kỳ hằng số $$C$$ nào! (Ngược lại, $$2^{n+10} = 1024 \cdot 2^n = \Theta(2^n)$$!)

### Giải thích: 4 bước làm chủ Ký hiệu Big-O không nhầm lẫn
#### Bước 1: Đừng nhầm Big-O với "trường hợp xấu nhất"
Big-O chỉ là **chặn trên toán học của một hàm số**! Bạn có thể dùng $$O, \Omega, \Theta$$ để mô tả trường hợp tốt nhất, trung bình, lẫn xấu nhất.

#### Bước 2: Dùng phép tính giới hạn $$\lim_{n\to\infty} f(n)/g(n)$$ để so sánh siêu nhanh
- Nếu giới hạn $$= 0 \implies f = o(g)$$ (nhỏ hơn chặt).
- Nếu giới hạn $$= L \in (0, \infty) \implies f = \Theta(g)$$ (đồng bậc!).
- Nếu giới hạn $$= +\infty \implies g = o(f)$$.

#### Bước 3: Luôn kiểm tra cặp chứng nhân $$(C, n_0)$$ khi chứng minh chặt
Đừng chỉ nói "bỏ bậc thấp"; hãy thay mọi số hạng $$n^k$$ ($$k < d$$) bằng $$n^d$$ (với $$n \ge 1$$) để chỉ ra hằng số $$C$$ tường minh.

#### Bước 4: Đừng quên hằng số ẩn trong thực tế kỹ thuật
Khi $$n$$ nhỏ (ví dụ $$n \le 32$$), Insertion Sort $$O(n^2)$$ với hằng số cực bé thường chạy nhanh hơn Merge Sort $$O(n\log n)$$ — đó là lý do `Timsort` (Python) và `Introsort` (C++) kết hợp cả hai!

$$
\text{Hàm chi phí }T(n)
\;\xrightarrow{\;\exists C, n_0:\; T(n) \le C g(n)\;}\;
O(g(n)) \;/\; \Omega(g(n)) \;/\; \Theta(g(n)).
$$

## Định nghĩa các ký hiệu tiệm cận

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Cho hai hàm $$f, g : \mathbb{N} \to \mathbb{R}^+$$:

- $$f(n) = O(g(n))$$ nếu tồn tại các hằng số $$c > 0$$ và $$n_0$$ sao cho với mọi $$n \ge n_0$$ ta có $$f(n) \le c\,g(n)$$ (*chặn trên* tiệm cận).
- $$f(n) = \Omega(g(n))$$ nếu $$g(n) = O(f(n))$$ (*chặn dưới* tiệm cận).
- $$f(n) = \Theta(g(n))$$ nếu đồng thời $$f(n) = O(g(n))$$ và $$f(n) = \Omega(g(n))$$ (*cùng bậc* tăng trưởng).

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 1.** Chứng minh $$3n^2+5n+2 = O(n^2)$$: với mọi $$n \ge 1$$, ta có $$3n^2+5n+2 \le 3n^2+5n^2+2n^2 = 10n^2$$, nên chọn $$c=10, n_0=1$$. Hơn nữa, vì $$3n^2+5n+2 \ge 3n^2$$ với mọi $$n \ge 1$$, ta cũng có $$3n^2+5n+2 = \Theta(n^2)$$.

</div>

## Các bậc tăng trưởng thường gặp

![Biểu đồ các bậc tăng trưởng Big-O](/discrete-mathematics-for-computer-science-iuh/img/course/Big-O-notation.png)

![So sánh các lớp hàm Big-O phổ biến](/discrete-mathematics-for-computer-science-iuh/img/course/BigOnotation_popular.svg)

| Bậc | Tên gọi | Ví dụ thuật toán |
|:---|:---|:---|
| $$O(1)$$ | Hằng số | Truy cập phần tử mảng theo chỉ số |
| $$O(\log n)$$ | Lôgarit | Tìm kiếm nhị phân (binary search) |
| $$O(n)$$ | Tuyến tính | Tìm kiếm tuần tự (linear scan) |
| $$O(n\log n)$$ | Tuyến tính–lôgarit | Sắp xếp trộn (merge sort) |
| $$O(n^2)$$ | Bậc hai | Sắp xếp nổi bọt (bubble sort) với hai vòng lặp lồng nhau |
| $$O(2^n)$$ | Hàm mũ | Duyệt vét cạn tất cả tập con |
| $$O(n!)$$ | Giai thừa | Duyệt vét cạn tất cả hoán vị |

## Các quy tắc cơ bản

- **Quy tắc tổng:** $$O(f) + O(g) = O(\max(f, g))$$.
- **Quy tắc tích:** $$O(f) \cdot O(g) = O(fg)$$.
- **Đa thức:** chỉ giữ hạng tử bậc cao nhất, tức $$a_k n^k + \cdots + a_0 = O(n^k)$$ (với $$a_k > 0$$).
- **Lôgarit:** đổi cơ số chỉ nhân thêm một hằng số dương, nên $$\log_2 n = \Theta(\log_{10} n)$$.

<div class="textbook-example" markdown="1">

**Ví dụ 2.** Với $$T(n) = n + n\log n + 100$$, vì $$n\log n$$ tăng nhanh hơn $$n$$ và hằng số $$100$$ khi $$n \to \infty$$, ta có $$T(n) = O(n\log n) = \Theta(n\log n)$$.

</div>

## Thử nghiệm tương tác

<div class="interactive-demo" markdown="1">
<div data-demo="big-o-growth-comparator"></div>
</div>
<script src="{{ '/public/js/big-o-growth-comparator.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Chứng minh $$5n+20=O(n)$$ trực tiếp bằng định nghĩa.

<details>
<summary>Đáp án</summary>

Với mọi $$n \ge 20$$, ta có $$5n + 20 \le 5n + n = 6n$$. Do đó chọn $$c = 6$$ và $$n_0 = 20$$ thỏa mãn định nghĩa Big-O.

</details>

### Bài tập 2

Sắp xếp các hàm sau theo thứ tự bậc tăng trưởng tăng dần: $$2^n$$, $$n^3$$, $$\log n$$, $$n\log n$$, $$n!$$.

<details>
<summary>Đáp án</summary>

$$\log n \prec n\log n \prec n^3 \prec 2^n \prec n!$$ (khi $$n$$ đủ lớn).

</details>

### Bài tập 3

Hàm $$n^2$$ có thuộc $$O(n^3)$$ không? Ngược lại, $$n^3$$ có thuộc $$O(n^2)$$ không?

<details>
<summary>Đáp án</summary>

- $$n^2 = O(n^3)$$ là **đúng**, vì $$n^2 \le n^3$$ với mọi $$n \ge 1$$ (chọn $$c=1, n_0=1$$).  
- $$n^3 = O(n^2)$$ là **sai**, vì tỉ số $$n^3/n^2 = n \to \infty$$ không thể bị chặn trên bởi bất kỳ hằng số $$c$$ nào.

</details>

## Tóm tắt

1. Các ký hiệu $$O$$, $$\Omega$$ và $$\Theta$$ mô tả tốc độ tăng trưởng tiệm cận của hàm, độc lập với cấu hình phần cứng cụ thể.
2. Khi $$n \to \infty$$, ta bỏ qua hằng số nhân và các hạng tử bậc thấp hơn.
3. Hàm mũ tăng nhanh hơn nhiều so với hàm đa thức — ranh giới quan trọng khi đánh giá tính khả thi của thuật toán (Chương 20).

Bài tiếp theo sẽ áp dụng các ký hiệu này để **phân tích độ phức tạp** $$T(n)$$ và $$S(n)$$ của các thuật toán cụ thể.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=__vX2sjlpXU">Big-O notation in 5 minutes</a> — Michael Sambol, tiếng Anh. Tóm tắt trực quan về ký hiệu Big-O trong 5 phút.
- <a href="https://www.youtube.com/watch?v=A03oI0znAoc">1.8.1 Asymptotic Notations Big Oh - Omega - Theta #1</a> — Abdul Bari, tiếng Anh. Giải thích chi tiết cả ba ký hiệu tiệm cận Big-O, Omega và Theta.
- <a href="https://www.youtube.com/watch?v=BgLTDT03QtU">Big-O Notation - For Coding Interviews</a> — NeetCode, tiếng Anh. Cách xác định bậc tăng trưởng từ các cấu trúc vòng lặp quen thuộc.
