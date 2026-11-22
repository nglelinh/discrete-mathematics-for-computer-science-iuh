---
layout: post
title: "Quan hệ Truy hồi Không Thuần nhất và Ứng dụng"
categories: chapter10
date: 2021-01-01
order: 3
required: true
lang: vi
excerpt: "Giải quan hệ truy hồi tuyến tính không thuần nhất bằng nguyên lý chồng chất, phương pháp hệ số bất định, xử lý cộng hưởng và liên hệ phân tích thuật toán."
---

Ở bài trước, chúng ta đã giải quan hệ truy hồi **tuyến tính thuần nhất** bằng phương trình đặc trưng. Bài học này mở rộng sang **quan hệ truy hồi tuyến tính không thuần nhất** — trường hợp phương trình có thêm một thành phần tự do $$f(n)$$ (như hằng số, đa thức, hàm mũ $$b^n$$, …) bên cạnh các số hạng $$a_{n-i}$$.

Dạng truy hồi này phản ánh sát hơn nhiều hệ thống thực tế, nơi mỗi bước vừa kế thừa trạng thái cũ vừa chịu thêm tác động từ bên ngoài (chẳng hạn chi phí cố định, dữ liệu mới phát sinh hoặc khối lượng công việc bổ sung). Trong phân tích thuật toán, ví dụ quen thuộc nhất là hệ thức $$T(n) = 2T(n/2) + n$$ của Merge Sort, trong đó $$f(n) = n$$ biểu thị chi phí trộn dữ liệu ở mỗi tầng đệ quy. Chúng ta sẽ lần lượt tìm hiểu **nguyên lý chồng chất**, **phương pháp hệ số bất định** và cách xử lý hiện tượng **cộng hưởng** khi dạng nghiệm thử trùng với nghiệm thuần nhất.

## Dạng tổng quát

Quan hệ truy hồi tuyến tính không thuần nhất bậc $$k$$ có hệ số hằng được viết dưới dạng:

<div class="textbook-equation" markdown="1">
$$
a_n=c_1a_{n-1}+c_2a_{n-2}+\cdots+c_ka_{n-k}+f(n),
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

trong đó $$f(n)$$ không đồng nhất bằng $$0$$.

Nếu bỏ đi thành phần $$f(n)$$, ta thu được **quan hệ truy hồi thuần nhất liên kết**:

<div class="textbook-equation" markdown="1">
$$
a_n=c_1a_{n-1}+c_2a_{n-2}+\cdots+c_ka_{n-k}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

### Video ngắn: Hệ thức không thuần nhất

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/nonhomogeneous-recurrence.mp4"></video>
</div>

Video dài khoảng 2 phút 58 giây: nghiệm tổng quát bằng nghiệm thuần nhất cộng một nghiệm riêng, ba dạng vế phải với ví dụ giải trọn và kiểm tra vài số hạng đầu (hằng số: $$a_n = 4\cdot 2^n - 3$$ và tháp Hà Nội; đa thức: $$a_n = 2^{n+1} - n - 2$$; hàm mũ: $$a_n = 3^{n+1} - 2^{n+1}$$), trường hợp cộng hưởng phải nhân thêm $$n$$ ($$a_n = (n+1)2^n$$), Ví dụ 1 bậc hai của bài ($$X_2 = 14$$, $$X_3 = 52$$) và bảng đoán dạng nghiệm riêng.

## Nguyên lý chồng chất

Nghiệm tổng quát của quan hệ truy hồi tuyến tính không thuần nhất luôn có dạng:

<div class="textbook-equation" markdown="1">
$$
a_n=a_n^{(h)}+a_n^{(p)},
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

trong đó:

- $$a_n^{(h)}$$ là nghiệm tổng quát của quan hệ thuần nhất liên kết.
- $$a_n^{(p)}$$ là một nghiệm riêng bất kỳ thỏa mãn quan hệ không thuần nhất ban đầu.

<div class="textbook-proof" markdown="1">
**Phác thảo chứng minh.** Xét toán tử tuyến tính $$L$$ được định nghĩa bởi  
$$L(a)_n = a_n - c_1 a_{n-1} - \cdots - c_k a_{n-k}$$.  
Khi đó, quan hệ không thuần nhất có thể viết gọn là $$L(a) = f$$. Giả sử $$a^{(p)}$$ là một nghiệm riêng ($$L(a^{(p)}) = f$$) và $$b$$ là một nghiệm bất kỳ của phương trình. Nhờ tính tuyến tính của $$L$$, ta có:

$$
L(b - a^{(p)}) = L(b) - L(a^{(p)}) = f - f = 0.
$$

Điều này chứng tỏ hiệu $$b - a^{(p)}$$ là nghiệm của quan hệ thuần nhất liên kết — ký hiệu là $$a^{(h)}$$. Suy ra mọi nghiệm đều có dạng $$b = a^{(h)} + a^{(p)}$$. Chiều ngược lại cũng đúng: nếu $$L(a^{(h)}) = 0$$ và $$L(a^{(p)}) = f$$ thì $$L(a^{(h)} + a^{(p)}) = f$$.
</div>

## Phương pháp hệ số bất định

Khi thành phần $$f(n)$$ có dạng quen thuộc (hằng số, đa thức, hàm mũ hoặc tích của đa thức và hàm mũ), ta có thể tìm nghiệm riêng $$a_n^{(p)}$$ bằng cách dự đoán một biểu thức cùng "họ" với $$f(n)$$ rồi thay vào phương trình để đồng nhất hệ số.

| Dạng của $$f(n)$$ | Dạng thử cho $$a_n^{(p)}$$ |
|:------------|:---------------------------|
| Hằng số $$d$$ | $$A$$ |
| Đa thức bậc $$m$$ | Đa thức tổng quát bậc $$m$$ |
| $$b^n$$ | $$A b^n$$ |
| $$n^m b^n$$ | (Đa thức tổng quát bậc $$m$$) $$\cdot b^n$$ |

**Quy tắc xử lý trùng lặp (cộng hưởng):** Nếu dạng nghiệm thử bị trùng với một thành phần trong nghiệm thuần nhất $$a_n^{(h)}$$, ta nhân dạng thử với $$n^s$$ (với $$s$$ là bội của nghiệm đặc trưng tương ứng) để đảm bảo tính độc lập tuyến tính.

### Ví dụ với hằng số

Khi $$f(n)$$ là hằng số, theo bảng trên ta chọn nghiệm riêng dạng hằng số $$a_n^{(p)} = A$$, thay vào phương trình để tìm $$A$$, sau đó ghép với nghiệm thuần nhất và sử dụng điều kiện đầu.

Giải quan hệ truy hồi:

<div class="textbook-equation" markdown="1">
$$
a_n=2a_{n-1}+3,\quad a_0=1.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

- **Nghiệm thuần nhất:** $$a_n^{(h)} = C \cdot 2^n$$.
- **Nghiệm riêng:** Thử $$a_n^{(p)} = A$$. Thay vào phương trình ta được:

<div class="textbook-equation" markdown="1">
$$
A=2A+3\Rightarrow A=-3.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

- **Nghiệm tổng quát và điều kiện đầu:** $$a_n = C \cdot 2^n - 3$$. Từ $$a_0 = 1$$ suy ra $$C - 3 = 1 \Rightarrow C = 4$$. Vậy:

<div class="textbook-equation" markdown="1">
$$
a_n=4\cdot2^n-3.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

<div class="textbook-example" markdown="1">

**Ví dụ (bậc 1 — bài toán Tháp Hà Nội):**  
Giải $$x_n = 2x_{n-1} + 1$$ với $$x_1 = 1$$.

- **Nghiệm thuần nhất:** $$x_n^{(h)} = A \cdot 2^n$$.
- **Nghiệm riêng:** Thử hằng số $$x_n^{(p)} = C$$. Thay vào phương trình: $$C = 2C + 1 \Rightarrow C = -1$$.
- **Nghiệm tổng quát:** $$x_n = A \cdot 2^n - 1$$.
- **Áp dụng điều kiện đầu:** Từ $$x_1 = 1$$ ta có $$2A - 1 = 1 \Rightarrow A = 1$$.

Vậy $$x_n = 2^n - 1$$, tạo ra dãy số $$1, 3, 7, 15, \dots$$ đúng như kết quả của bài toán Tháp Hà Nội.

</div>

## Ví dụ với đa thức

Khi $$f(n)$$ là đa thức bậc $$m$$, ta thường chọn nghiệm riêng là một đa thức cùng bậc $$m$$. Tuy nhiên, nếu $$r = 1$$ là nghiệm của phương trình đặc trưng (tức hằng số đã là một nghiệm thuần nhất), ta cần nhân thêm $$n$$ vào đa thức thử để tránh trùng lặp.

Xét quan hệ truy hồi:

<div class="textbook-equation" markdown="1">
$$
a_n=a_{n-1}+n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Phương trình thuần nhất liên kết $$a_n = a_{n-1}$$ có nghiệm đặc trưng $$r = 1$$, nên $$a_n^{(h)} = C$$ (hằng số). Vì $$f(n) = n$$ là đa thức bậc nhất nhưng bị cộng hưởng với nghiệm thuần nhất hằng số, ta nhân thêm $$n$$ và thử $$a_n^{(p)} = n(An + B) = An^2 + Bn$$. Thay vào phương trình:

<div class="textbook-equation" markdown="1">
$$
An^2+Bn=A(n-1)^2+B(n-1)+n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Khai triển và đồng nhất hệ số hai vế cho ta $$2A = 1$$ và $$B - A = 0$$, suy ra $$A = \frac{1}{2}$$ và $$B = \frac{1}{2}$$. Do đó:

<div class="textbook-equation" markdown="1">
$$
a_n^{(p)}=\frac{n(n+1)}{2}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Với $$a_0 = 0$$ thì $$C = 0$$, và ta thu lại công thức tổng Gauss quen thuộc $$1 + 2 + \cdots + n = \frac{n(n+1)}{2}$$.

![Dãy số học — tổng $$1+2+\cdots+n$$](/discrete-mathematics-for-computer-science-iuh/img/course/Arithmetic_progression.svg)

<p class="textbook-figure-caption" data-figure="10.13">Quan hệ truy hồi $$a_n = a_{n-1} + n$$ có nghiệm riêng bậc hai — chính là công thức tổng Gauss.</p>

<div class="textbook-example" markdown="1">

**Ví dụ (tổng bình phương — cộng hưởng đa thức):**  
Đặt $$a_n = 1^2 + 2^2 + \cdots + n^2$$ với $$n \ge 1$$ và $$a_0 = 0$$. Khi đó dãy thỏa mãn:
$$a_n = a_{n-1} + n^2.$$

- **Nghiệm thuần nhất:** $$a_n^{(h)} = C$$ (ứng với nghiệm đặc trưng $$r = 1$$).
- **Nghiệm riêng:** Do $$f(n) = n^2$$ là đa thức bậc 2 và hằng số đã nằm trong nghiệm thuần nhất, ta nhân thêm $$n$$ và thử dạng bậc 3:
  $$a_n^{(p)} = n(qn^2 + sn + t) = qn^3 + sn^2 + tn.$$
  Thay vào $$a_n - a_{n-1} = n^2$$ rồi đồng nhất hệ số, ta thu được:
  $$a_n^{(p)} = \frac{n(n+1)(2n+1)}{6}.$$
- **Điều kiện đầu:** Với $$a_0 = 0$$ thì $$C = 0$$, nên:
  $$a_n = \frac{n(n+1)(2n+1)}{6}.$$

</div>

## Ví dụ quan hệ truy hồi bậc hai không thuần nhất

<div class="textbook-example" markdown="1">

**Ví dụ 1 ($$f(n) = 3^n$$, phần thuần nhất có nghiệm kép $$r = 1$$):**  
Giải $$X_n = 2X_{n-1} - X_{n-2} + 3^n$$ với $$X_0 = 1$$, $$X_1 = 3$$.

1. **Nghiệm thuần nhất:** Phương trình đặc trưng $$r^2 - 2r + 1 = (r - 1)^2 = 0$$ có nghiệm kép $$r = 1$$, nên $$X_n^{(h)} = A + Bn$$.
2. **Nghiệm riêng:** Vì cơ số $$3$$ không phải nghiệm của phương trình đặc trưng, ta thử $$X_n^{(p)} = C \cdot 3^n$$. Thay vào quan hệ truy hồi:
   $$C \cdot 3^n = 2C \cdot 3^{n-1} - C \cdot 3^{n-2} + 3^n.$$
   Chia cả hai vế cho $$3^{n-2}$$:
   $$9C = 6C - C + 9 \Rightarrow 4C = 9 \Rightarrow C = \dfrac{9}{4}.$$
   Vậy $$X_n^{(p)} = \dfrac{9}{4}\,3^n$$.
3. **Nghiệm tổng quát và điều kiện đầu:**  
   $$X_n = A + Bn + \dfrac{9}{4}\,3^n.$$
   - Với $$n = 0$$: $$A + \dfrac{9}{4} = 1 \Rightarrow A = -\dfrac{5}{4}$$.
   - Với $$n = 1$$: $$-\dfrac{5}{4} + B + \dfrac{27}{4} = 3 \Rightarrow B = -\dfrac{5}{2}$$.

   Vậy công thức đóng là:
   $$X_n = -\dfrac{5}{4} - \dfrac{5}{2}n + \dfrac{9}{4}\,3^n.$$

   *Kiểm tra với $$n = 2$$:* Từ truy hồi ta có $$X_2 = 2\cdot 3 - 1 + 9 = 14$$; thay vào công thức cũng cho $$-\dfrac{5}{4} - 5 + \dfrac{9}{4}\cdot 9 = 14$$ ✓.

</div>

<div class="textbook-example" markdown="1">

**Ví dụ 2 ($$f(n) = n^2$$, truy hồi bậc hai):**  
Tìm nghiệm tổng quát của $$a_n = 2a_{n-1} + a_{n-2} + n^2$$.

1. **Nghiệm thuần nhất:** Phương trình đặc trưng $$r^2 - 2r - 1 = 0$$ có hai nghiệm phân biệt $$r = 1 \pm \sqrt{2}$$, nên:
   $$a_n^{(h)} = C_1(1+\sqrt{2})^n + C_2(1-\sqrt{2})^n.$$
2. **Nghiệm riêng:** Vì $$r = 1$$ không phải nghiệm đặc trưng, ta thử đa thức bậc hai $$a_n^{(p)} = An^2 + Bn + C$$. Thay vào $$a_n - 2a_{n-1} - a_{n-2} = n^2$$, khai triển $$(n-1)^2$$, $$(n-2)^2$$ và đồng nhất hệ số hai vế, ta giải được:
   $$A = -\dfrac{1}{2},\quad B = -2,\quad C = -\dfrac{5}{2}.$$
3. **Nghiệm tổng quát:**
   $$a_n = C_1(1+\sqrt{2})^n + C_2(1-\sqrt{2})^n - \dfrac{n^2}{2} - 2n - \dfrac{5}{2},$$
   trong đó $$C_1, C_2$$ sẽ được xác định khi có đủ hai điều kiện đầu.

</div>

## Trường hợp cộng hưởng

Xét quan hệ truy hồi:

<div class="textbook-equation" markdown="1">
$$
a_n=2a_{n-1}+2^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Phần thuần nhất có nghiệm $$a_n^{(h)} = C \cdot 2^n$$. Nếu ta thử nghiệm riêng dạng $$a_n^{(p)} = A \cdot 2^n$$, biểu thức này trùng hoàn toàn với nghiệm thuần nhất nên khi thay vào phương trình, $$A$$ sẽ bị triệt tiêu (dẫn đến mâu thuẫn $$0 = 2^n$$). Để khắc phục, ta nhân thêm $$n$$ vào dạng nghiệm thử:

<div class="textbook-equation" markdown="1">
$$
a_n^{(p)}=A n 2^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Hiện tượng này được gọi là **cộng hưởng** (resonance): tác động bên ngoài $$f(n)$$ có cùng dạng tăng trưởng với dao động hoặc tốc độ tăng tự nhiên của hệ thuần nhất.

<div class="interactive-tool" markdown="1">
**Công cụ tương tác**: Bạn có thể chọn dạng của $$f(n)$$ cùng các nghiệm đặc trưng để xem công cụ gợi ý dạng nghiệm riêng tương ứng, tự động cảnh báo khi xảy ra cộng hưởng và nhân thêm nhân tử $$n$$.
<div data-demo="characteristic-solver"></div>
</div>
<script src="{{ '/public/js/characteristic-solver.js' | relative_url }}"></script>

## Ứng dụng trong phân tích thuật toán

Trong lập trình và thiết kế hệ thống, quan hệ truy hồi không thuần nhất là công cụ quen thuộc để đánh giá chi phí tính toán. Chẳng hạn, hệ thức:

<div class="textbook-equation" markdown="1">
$$
T(n)=2T(n/2)+n
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

mô tả thời gian chạy của nhiều thuật toán chia để trị như Merge Sort. Dù chỉ số giảm theo phép chia $$n/2$$ thay vì $$n-1$$, tư tưởng vẫn tương tự: tổng chi phí gồm phần gọi đệ quy và phần công việc bổ sung $$f(n) = n$$ ở mỗi tầng. Kết quả $$T(n) = \Theta(n\log n)$$ cho thấy thành phần không thuần nhất ảnh hưởng trực tiếp đến bậc độ phức tạp cuối cùng.

![Dãy hình học — thành phần $$f(n)$$ trong truy hồi](/discrete-mathematics-for-computer-science-iuh/img/course/Geometric_sequence.svg)

<p class="textbook-figure-caption" data-figure="10.14">Thành phần $$f(n)$$ trong truy hồi không thuần nhất phản ánh tác động bên ngoài: chi phí cố định, dữ liệu mới hoặc khối lượng xử lý bổ sung ở mỗi bước.</p>

Với truy hồi tuyến tính theo chỉ số $$n-1$$, số phép gán tích lũy trong một vòng lặp lồng nhau thường có dạng:

<div class="textbook-equation" markdown="1">
$$
a_n=a_{n-1}+2n+1,
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

trong đó nghiệm riêng bậc hai cho ta tổng chi phí tăng theo bậc $$\Theta(n^2)$$.

### Minh hoạ tương tác

Quan sát cách kết hợp nghiệm thuần nhất và nghiệm riêng trong hệ thức truy hồi không thuần nhất qua minh họa dưới đây:

<div class="interactive-demo" markdown="1">
<div data-demo="recurrence-explainer" data-mode="linear" data-preset="nonhom"></div>
</div>
<script src="{{ '/public/js/explainers/recurrence-explainer.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Giải $$a_n = 2a_{n-1} + 3$$ với $$a_0 = 0$$ bằng phương pháp hệ số bất định.

<details>
<summary>Đáp án</summary>

- Nghiệm thuần nhất: $$a_n^{(h)} = c \cdot 2^n$$.
- Thử nghiệm riêng hằng số $$a_n^{(p)} = A$$. Thay vào phương trình: $$A = 2A + 3 \Rightarrow A = -3$$.
- Nghiệm tổng quát: $$a_n = c \cdot 2^n - 3$$. Với $$a_0 = 0 \Rightarrow c = 3$$.
- Vậy $$a_n = 3 \cdot 2^n - 3$$.

</details>

### Bài tập 2

Giải $$a_n = a_{n-1} + 2n$$ với $$a_0 = 1$$.

<details>
<summary>Đáp án</summary>

- Nghiệm thuần nhất: $$a_n^{(h)} = c$$ (ứng với nghiệm đặc trưng $$r = 1$$).
- Vì $$f(n) = 2n$$ là đa thức bậc nhất và bị cộng hưởng với nghiệm thuần nhất hằng số ($$r = 1$$), ta nhân thêm $$n$$ và thử nghiệm riêng $$a_n^{(p)} = An^2 + Bn$$.
- Thay vào phương trình: $$An^2 + Bn = A(n-1)^2 + B(n-1) + 2n \Rightarrow 2An + (B - A) = 2n$$.
- Đồng nhất hệ số: $$2A = 2 \Rightarrow A = 1$$ và $$B - A = 0 \Rightarrow B = 1$$.
- Nghiệm tổng quát: $$a_n = c + n^2 + n$$. Từ $$a_0 = 1 \Rightarrow c = 1$$.
- Vậy $$a_n = n^2 + n + 1$$. (Kiểm tra: $$a_1 = 1 + 2 = 3$$, công thức cho $$1 + 1 + 1 = 3$$ ✓.)

</details>

### Bài tập 3

Giải thích hiện tượng **cộng hưởng**: vì sao khi giải $$a_n = 2a_{n-1} + 2^n$$, ta phải thử nghiệm riêng $$a_n^{(p)} = A n 2^n$$ thay vì $$A 2^n$$?

<details>
<summary>Đáp án</summary>

Vì $$r = 2$$ là nghiệm của phương trình đặc trưng $$r - 2 = 0$$, nên $$2^n$$ đã là nghiệm của phần thuần nhất. Nếu thử $$a_n^{(p)} = A 2^n$$, vế trái và vế phải sẽ triệt tiêu $$A$$ khi thay vào phương trình. Do đó ta phải nhân thêm $$n$$ (hoặc $$n^s$$ nếu $$r$$ là nghiệm bội $$s$$) để nghiệm thử độc lập tuyến tính với nghiệm thuần nhất.

</details>

### Bài tập 4 (bậc 1 — Tháp Hà Nội)

Giải $$x_n = 2x_{n-1} + 1$$ với $$x_1 = 1$$. Tìm công thức đóng và tính giá trị $$x_5$$.

<details>
<summary>Đáp án</summary>

Công thức đóng là $$x_n = 2^n - 1$$; suy ra $$x_5 = 2^5 - 1 = 31$$.

</details>

### Bài tập 5 (tổng bình phương)

Xét $$a_n = a_{n-1} + n^2$$ với $$a_0 = 0$$. Hãy giải bằng phương pháp hệ số bất định (lưu ý cộng hưởng với $$r = 1$$) và đối chiếu với công thức tổng $$\sum_{k=1}^n k^2$$.

<details>
<summary>Đáp án</summary>

$$a_n = \dfrac{n(n+1)(2n+1)}{6}$$.

</details>

### Bài tập 6 (bậc 2 với thành phần $$3^n$$)

Giải $$X_n = 2X_{n-1} - X_{n-2} + 3^n$$ với $$X_0 = 1$$, $$X_1 = 3$$ theo đầy đủ ba bước (tìm nghiệm thuần nhất, tìm nghiệm riêng và áp dụng điều kiện đầu).

<details>
<summary>Đáp án</summary>

$$X_n = -\dfrac{5}{4} - \dfrac{5}{2}n + \dfrac{9}{4}\,3^n$$ (xem chi tiết các bước biến đổi ở Ví dụ 1 trong mục ví dụ bậc hai).

</details>

### Bài tập 7 (thử thách)

Giải $$a_n = 2a_{n-1} + a_{n-2} + n^2$$ với $$a_0 = 0$$, $$a_1 = 1$$ (sử dụng nghiệm riêng đã tìm ở Ví dụ 2, sau đó giải hệ để tìm $$C_1, C_2$$).

<details>
<summary>Đáp án</summary>

- Nghiệm riêng: $$a_n^{(p)} = -\dfrac{n^2}{2} - 2n - \dfrac{5}{2}$$.
- Nghiệm tổng quát: $$a_n = C_1(1+\sqrt{2})^n + C_2(1-\sqrt{2})^n - \dfrac{n^2}{2} - 2n - \dfrac{5}{2}$$.
- Thay điều kiện đầu để lập hệ phương trình tìm $$C_1, C_2$$:
  - Với $$n = 0$$: $$C_1 + C_2 - \dfrac{5}{2} = 0 \Rightarrow C_1 + C_2 = \dfrac{5}{2}$$.
  - Với $$n = 1$$: $$C_1(1+\sqrt{2}) + C_2(1-\sqrt{2}) - \dfrac{1}{2} - 2 - \dfrac{5}{2} = 1 \Rightarrow C_1(1+\sqrt{2}) + C_2(1-\sqrt{2}) = 6$$.

</details>

---

## Xem thêm / Video gợi ý

- <a href="https://www.youtube.com/watch?v=ghSnXV4RHiI">Solving non-homogeneous recurrence relations</a> — Các ví dụ minh họa giải chi tiết.
- Tài liệu gốc của khóa học: `material/Chuong 3. He Thuc Hoi Quy.pdf` (trình bày truy hồi bậc 1–2, nghiệm bội, nghiệm phức và phương trình không thuần nhất).

## Tóm tắt

- **Quan hệ truy hồi tuyến tính không thuần nhất**: $$a_n = c_1 a_{n-1} + \cdots + c_k a_{n-k} + f(n)$$ với $$f(n) \not\equiv 0$$.
- **Nguyên lý chồng chất**: Mọi nghiệm tổng quát đều viết được dưới dạng $$a_n = a_n^{(h)} + a_n^{(p)}$$ (tổng của nghiệm thuần nhất tổng quát và một nghiệm riêng).
- **Phương pháp hệ số bất định**: Dự đoán $$a_n^{(p)}$$ cùng họ hàm với $$f(n)$$ (hằng số, đa thức, $$b^n$$, $$n^m b^n$$).
- **Cộng hưởng**: Khi dạng thử trùng với nghiệm thuần nhất, cần nhân thêm $$n$$ (hoặc $$n^s$$ ứng với bội của nghiệm đặc trưng).
- **Ứng dụng**: Là công cụ cốt lõi để phân tích các thuật toán chia để trị như $$T(n) = 2T(n/2) + n$$ và các vòng lặp tích lũy.

Trong bài tiếp theo, chúng ta sẽ tổng hợp các ứng dụng tiêu biểu của hệ thức truy hồi trong thuật toán và hệ thống phần mềm thực tế.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=EfF_XSEX1Sk">NON-HOMOGENEOUS RECURRENCE RELATIONS - Discrete Mathematics</a> — TrevTutor (tiếng Anh). Giới thiệu trực quan nguyên lý kết hợp nghiệm thuần nhất và nghiệm riêng.
- <a href="https://www.youtube.com/watch?v=UVuSLfdcT_Y">[Discrete Mathematics] Nonhomogeneous Recurrence Relation Examples</a> — TrevTutor (tiếng Anh). Giải chi tiết trọn vẹn nhiều ví dụ truy hồi không thuần nhất.
