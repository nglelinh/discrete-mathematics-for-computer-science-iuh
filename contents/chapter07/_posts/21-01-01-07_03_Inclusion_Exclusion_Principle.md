---
layout: post
title: "Nguyên lý Bù trừ"
categories: chapter07
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Nguyên lý bù trừ (bao hàm–loại trừ) giúp đếm chính xác hợp của nhiều tập hợp chồng lấn và xử lý các bài toán có nhiều ràng buộc."
---


Khảo sát một lớp 35 sinh viên cho thấy 25 bạn biết Python và 20 bạn biết SQL—nếu vội vàng cộng $25 + 20 = 45$, bạn đã vô tình đếm trùng hai lần những bạn giỏi cả hai ngôn ngữ! Khi bài toán có ba, bốn hay $n$ điều kiện chồng lấn chằng chịt lên nhau, **Nguyên lý Bù trừ (Inclusion–Exclusion Principle)** cung cấp một công thức dấu đan xen (`+`, `−`, `+`, `−`) chính xác tuyệt đối để triệt tiêu mọi phần đếm lặp.

Ở mục trước, chúng ta đã học hoán vị và tổ hợp. Mục này giới thiệu **nguyên lý bù trừ** (hay bao hàm–loại trừ) — công cụ khử đếm trùng có hệ thống khi nhiều điều kiện chồng lấn lên nhau.

Khi một bài toán có nhiều điều kiện giao nhau, việc đếm theo trực giác rất dễ sai: nếu chỉ cộng số phần tử của từng nhóm riêng lẻ, các phần tử thuộc nhiều nhóm cùng lúc sẽ bị đếm lặp. Nguyên lý bù trừ giải quyết vấn đề này bằng cách cộng các tập đơn, trừ phần giao đôi, rồi tiếp tục cộng trừ đan dấu một cách có hệ thống cho đến khi mỗi phần tử được đếm đúng một lần.

## Bản đồ kiến thức nền: Bốn trụ cột làm chủ Nguyên lý Bù trừ

1. **Cơ chế khử đếm trùng bằng dấu đan xen**:
   Muốn tính lực lượng hợp $|A_1 \cup \dots \cup A_n|$: **cộng** tổng kích thước các tập đơn, **trừ** tổng các giao đôi, **cộng lại** tổng các giao ba, cứ thế đan xen dấu $(-1)^{k-1}$ cho đến giao của cả $n$ tập.

2. **Trực giác đếm số lần mỗi phần tử được tính**:
   Một phần tử thuộc đúng $m \ge 1$ tập hợp sẽ được cộng/trừ tổng cộng $\binom{m}{1} - \binom{m}{2} + \binom{m}{3} - \dots + (-1)^{m-1}\binom{m}{m} = 1 - (1 - 1)^m = \mathbf{1}$ lần—tức mọi phần tử trong hợp đều được đếm **chính xác 1 lần**, không thừa không thiếu!

3. **Dạng phần bù — Đếm phần tử KHÔNG vi phạm điều kiện nào**:
   Đặt $A_i$ là tập các phần tử *vi phạm* ràng buộc thứ $i$, khi đó số phần tử hợp lệ là:
   $$\left|\bigcap_{i=1}^{n} \overline{A_i}\right| = |U| - \left|\bigcup_{i=1}^{n} A_i\right|.$$
   Đây là dạng được dùng nhiều nhất trong bài toán mật khẩu, chia hết và phân phối.

4. **Ứng dụng kinh điển trong Toán rời rạc & CS**:
   Tính hàm phi Euler $\varphi(n)$ trong mật mã RSA, đếm số **hàm toàn ánh** từ tập $m$ phần tử sang $n$ phần tử, và đếm số **hoán vị không điểm cố định** (*derangements* $D_n$).

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Áp dụng** công thức bù trừ cho 2 tập, 3 tập và dạng tổng quát đơn giản.
- **Đếm** các phần tử không vi phạm ràng buộc nào thông qua dạng bù.
- **Nhận biết** khi nào việc cộng trực tiếp $$\vert A_i\vert $$ dẫn đến đếm trùng.

**Từ khóa**: bao hàm–loại trừ, giao tập, đếm có điều kiện.
</div>

### Video ngắn: Nguyên lý bù trừ

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/inclusion-exclusion.mp4"></video>
</div>

Video dài khoảng 3 phút 6 giây, trình bày ví dụ lớp 50 sinh viên với hai tập hợp, theo dõi số lần mỗi vùng của biểu đồ Venn ba tập được cộng hoặc trừ qua từng bước, ví dụ đếm các số từ 1 đến 100 chia hết cho 2, 3 hoặc 5 (kết quả 74, đối chiếu trên lưới 100 ô), bài tập đếm số từ 1 đến 1000 không chia hết cho 3, 5 và 7 (kết quả 457), công thức tổng quát cho $$n$$ tập, và ứng dụng đếm số cách bỏ thư sao cho không lá nào vào đúng phong bì.

## Đếm hợp của hai tập hợp

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Với hai tập hữu hạn $$A$$ và $$B$$, **hợp** $$A \cup B$$ gồm các phần tử thuộc ít nhất một trong hai tập, còn **giao** $$A \cap B$$ gồm các phần tử thuộc đồng thời cả hai tập.
</div>

<div class="textbook-theorem" markdown="1">
**Định lý**: Nếu $$A$$ và $$B$$ là hai tập hữu hạn thì
</div>

<div class="textbook-equation" markdown="1">
$$
\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh**: Khi cộng $$\lvert A \rvert + \lvert B \rvert$$, mỗi phần tử chỉ thuộc $$A$$ hoặc chỉ thuộc $$B$$ được đếm đúng một lần. Ngược lại, mỗi phần tử thuộc $$A \cap B$$ bị đếm hai lần: một lần trong $$\lvert A \rvert$$ và một lần trong $$\lvert B \rvert$$. Để mỗi phần tử trong hợp chỉ được đếm đúng một lần, ta trừ đi $$\lvert A \cap B \rvert$$.

![Phép hợp hai tập — nguyên lý bù trừ](/discrete-mathematics-for-computer-science-iuh/img/course/Venn_A_union_B.svg)

<p class="textbook-figure-caption" data-figure="7.11">$$\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert$$ — trừ phần giao để tránh đếm trùng.</p>
<div class="content-box example-box textbook-block" markdown="1">
<div class="textbook-example" markdown="1">
**Ví dụ**: Trong một lớp có 50 sinh viên, 30 sinh viên học tiếng Anh, 20 sinh viên học tiếng Pháp và 10 sinh viên học cả hai ngôn ngữ. Số sinh viên học ít nhất một ngoại ngữ là:

<div class="textbook-equation" markdown="1">
$$
30 + 20 - 10 = 40.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Ta không thể kết luận là $$50$$ chỉ vì $$30+20=50$$; phần giao gồm $$10$$ sinh viên là dữ kiện bắt buộc để loại trừ phần đếm lặp.
</div>
</div>

## Nguyên lý bù trừ cho ba tập hợp

Với ba tập hữu hạn $$A,B,C$$, công thức bù trừ có dạng:

<div class="textbook-equation" markdown="1">
{% raw %}$$
\begin{aligned}
\lvert A \cup B \cup C \rvert
&= \lvert A \rvert + \lvert B \rvert + \lvert C \rvert \\
&\quad - \lvert A \cap B \rvert - \lvert A \cap C \rvert - \lvert B \cap C \rvert \\
&\quad + \lvert A \cap B \cap C \rvert.
\end{aligned}
$${% endraw %}
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Vì sao phải cộng lại phần giao ba?** Một phần tử thuộc cả ba tập được cộng $$3$$ lần ở các tập đơn rồi bị trừ $$3$$ lần ở các giao đôi, nên tổng số lần đếm tạm thời bằng $$0$$. Do đó, ta phải cộng lại phần giao ba một lần để phần tử đó được tính đúng một lần.

![Nguyên lý bù trừ — ba tập hợp](/discrete-mathematics-for-computer-science-iuh/img/course/Inclusion-exclusion-3sets.svg)

<p class="textbook-figure-caption" data-figure="7.12">Công thức bù trừ cho ba tập — cộng các tập đơn, trừ các giao đôi, rồi cộng lại giao ba.</p>
<div class="interactive-tool" data-demo="inclusion-exclusion-toggle" markdown="1">
**Mô phỏng tương tác**: Bảng gồm ba công tắc `A`, `B`, `C`. Khi chọn vị trí của một phần tử trên biểu đồ Venn, công cụ sẽ hiển thị phần tử đó được cộng và trừ bao nhiêu lần trong công thức bù trừ.
</div>

<script src="{{ '/public/js/inclusion-exclusion-toggle.js' | relative_url }}"></script>

## Công thức tổng quát cho $$n$$ tập hợp

Cho $$A_1,A_2,\ldots,A_n$$ là các tập hữu hạn. Khi đó:

<div class="textbook-equation" markdown="1">
{% raw %}$$
\begin{aligned}
\left\lvert\bigcup_{i=1}^{n} A_i\right\rvert
&= \sum_i \lvert A_i \rvert \\
&\quad - \sum_{i<j}\lvert A_i\cap A_j \rvert \\
&\quad + \sum_{i<j<k}\lvert A_i\cap A_j\cap A_k \rvert \\
&\quad - \cdots \\
&\quad + (-1)^{n+1}\lvert A_1\cap\cdots\cap A_n \rvert.
\end{aligned}
$${% endraw %}
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Viết dưới dạng rút gọn:

<div class="textbook-equation" markdown="1">
{% raw %}$$
\left\lvert\bigcup_{i=1}^{n} A_i\right\rvert
= \sum_{\emptyset \neq I \subseteq \{1,2,\ldots,n\}} (-1)^{\lvert I \rvert+1}\left\lvert\bigcap_{i\in I} A_i\right\rvert.
$${% endraw %}
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh**: Xét một phần tử $$x$$ thuộc đúng $$r$$ tập trong số $$n$$ tập đã cho ($$r \ge 1$$). Trong vế phải, phần tử $$x$$ đóng góp:

<div class="textbook-equation" markdown="1">
$$
\binom{r}{1}-\binom{r}{2}+\binom{r}{3}-\cdots+(-1)^{r+1}\binom{r}{r}.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Theo khai triển nhị thức, ta có:

<div class="textbook-equation" markdown="1">
$$
(1-1)^r = \binom{r}{0}-\binom{r}{1}+\binom{r}{2}-\cdots+(-1)^r\binom{r}{r}=0.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Suy ra tổng đan dấu bỏ đi hạng tử $$\binom{r}{0} = 1$$ có giá trị đúng bằng $$1$$. Như vậy, mọi phần tử thuộc hợp đều được đếm đúng một lần.

![Phép giao hai tập](/discrete-mathematics-for-computer-science-iuh/img/course/Venn_A_intersect_B.svg)

<p class="textbook-figure-caption" data-figure="7.13">Mỗi phần giao $$\lvert A_i \cap A_j \rvert$$ trong công thức tổng quát đại diện cho phần bị đếm trùng.</p>
## Dạng bù: đếm phần tử không vi phạm điều kiện nào

Nhiều bài toán trở nên đơn giản hơn khi ta đếm số đối tượng **vi phạm ít nhất một điều kiện**, rồi lấy tổng số đối tượng trừ đi phần vi phạm đó.

Nếu $$U$$ là tập vũ trụ chứa mọi đối tượng đang xét và $$A_i$$ là tập các đối tượng vi phạm điều kiện thứ $$i$$, thì số đối tượng hợp lệ là:

<div class="textbook-equation" markdown="1">
$$
\lvert U \rvert-\left\lvert\bigcup_i A_i\right\rvert.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-example" markdown="1">
**Ví dụ**: Có bao nhiêu số nguyên từ $$1$$ đến $$100$$ không chia hết cho $$2$$, $$3$$ hoặc $$5$$?

Gọi $$A_2,A_3,A_5$$ lần lượt là tập các số từ $$1$$ đến $$100$$ chia hết cho $$2,3,5$$. Ta có:

<div class="textbook-equation" markdown="1">
$$
\lvert A_2 \rvert=50,\quad \lvert A_3 \rvert=33,\quad \lvert A_5 \rvert=20,
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$
\lvert A_2\cap A_3 \rvert=16,\quad \lvert A_2\cap A_5 \rvert=10,\quad \lvert A_3\cap A_5 \rvert=6,
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-equation" markdown="1">
$$
\lvert A_2\cap A_3\cap A_5 \rvert=3.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Số phần tử bị loại là $$50+33+20-16-10-6+3=74$$. Do đó số các số hợp lệ là $$100-74=26$$.

![Biểu đồ Venn ba tập](/discrete-mathematics-for-computer-science-iuh/img/course/Venn3.svg)

<p class="textbook-figure-caption" data-figure="7.14">Dạng bù đếm các số không chia hết cho 2, 3 hoặc 5 bằng cách loại bỏ phần vi phạm ít nhất một điều kiện.</p>
![Birthday paradox — va chạm sớm hơn trực giác](/discrete-mathematics-for-computer-science-iuh/img/course/Birthdaymatch.svg)

<p class="textbook-figure-caption" data-figure="7.15">Nguyên lý bù trừ cũng xuất hiện khi tính xác suất hợp của nhiều biến cố, tương tự trong nghịch lý sinh nhật.</p>
</div>

### Khung giải thích (nên đọc chậm): Đếm tay bao nhiêu số nguyên từ 1 đến 120 KHÔNG chia hết cho 2, 3, hay 5

Đặt không gian mẫu $U = \{1, 2, \dots, 120\}$ ($|U| = 120$), và gọi $A_2, A_3, A_5$ lần lượt là tập các số trong $U$ chia hết cho $2, 3, 5$.

1. **Bước 1 — Tính từng tập đơn**:
   $$|A_2| = \left\lfloor \frac{120}{2} \right\rfloor = 60, \quad |A_3| = \left\lfloor \frac{120}{3} \right\rfloor = 40, \quad |A_5| = \left\lfloor \frac{120}{5} \right\rfloor = 24.$$
   $\implies$ Tổng đơn $S_1 = 60 + 40 + 24 = \mathbf{124}$.
2. **Bước 2 — Tính các giao đôi** (chia hết cho cả $p$ và $q$ $\iff$ chia hết cho $\operatorname{BCNN}(p, q)$):
   $$|A_2 \cap A_3| = \frac{120}{6} = 20, \quad |A_2 \cap A_5| = \frac{120}{10} = 12, \quad |A_3 \cap A_5| = \frac{120}{15} = 8.$$
   $\implies$ Tổng đôi $S_2 = 20 + 12 + 8 = \mathbf{40}$.
3. **Bước 3 — Tính giao cả ba**:
   $$|A_2 \cap A_3 \cap A_5| = \frac{120}{\operatorname{BCNN}(2, 3, 5)} = \frac{120}{30} = \mathbf{4}.$$
4. **Bước 4 — Hợp các số chia hết cho ít nhất một trong $\{2, 3, 5\}$**:
   $$|A_2 \cup A_3 \cup A_5| = S_1 - S_2 + S_3 = 124 - 40 + 4 = \mathbf{88}.$$
5. **Bước 5 — Lấy phần bù để tìm các số KHÔNG chia hết cho 2, 3, hay 5**:
   $$|U| - |A_2 \cup A_3 \cup A_5| = 120 - 88 = \mathbf{32}.$$

**Kiểm chứng chéo bằng Lý thuyết số**: Vì $120 = 2^3 \cdot 3 \cdot 5$, số các số nguyên tố cùng nhau với 120 chính là hàm Euler $\varphi(120) = 120\left(1 - \frac{1}{2}\right)\left(1 - \frac{1}{3}\right)\left(1 - \frac{1}{5}\right) = \mathbf{32}$—khớp tuyệt đối!

## Ứng dụng trong Khoa học Máy tính

Trong cơ sở dữ liệu, truy vấn `OR` kết hợp nhiều điều kiện có thể trả về các bản ghi trùng lặp, và hệ quản trị cần loại trùng theo cùng tư duy của nguyên lý bù trừ. Trong bảo mật, khi đếm số mật khẩu đáp ứng đồng thời nhiều yêu cầu như “có chữ hoa”, “có chữ số” và “có ký tự đặc biệt”, cách làm hiệu quả là đếm phần bù gồm các mật khẩu thiếu ít nhất một loại ký tự. Trong thiết kế thuật toán, nguyên lý bù trừ còn xuất hiện ở sàng số nguyên tố, bài toán tính xác suất lỗi của hệ thống nhiều thành phần và phân tích các cấu hình bị cấm.

```python
from itertools import combinations

def inclusion_exclusion(sizes):
    # sizes[k] chứa tổng kích thước các giao của đúng k tập, k bắt đầu từ 1
    return sum(((-1) ** (k + 1)) * value for k, value in sizes.items())

print(inclusion_exclusion({1: 50 + 33 + 20, 2: 16 + 10 + 6, 3: 3}))
```

### Minh hoạ tương tác

Minh hoạ biểu đồ Venn ở chế độ bao hàm–loại trừ: so sánh $$\lvert A \cup B \cup C \rvert$$ tính trực tiếp với kết quả từ công thức bù trừ.

<div class="interactive-demo" markdown="1">
<div data-demo="venn-explainer" data-sets="3" data-focus="ie"></div>
</div>
<script src="{{ '/public/js/explainers/venn-explainer.js' | relative_url }}"></script>

## Bài tập thực hành

### Bài tập 1: Ba câu lạc bộ

Một lớp có 80 sinh viên, trong đó 35 sinh viên tham gia CLB Lập trình, 30 tham gia CLB Toán và 25 tham gia CLB Robot. Có 12 sinh viên tham gia cả Lập trình và Toán, 10 tham gia cả Lập trình và Robot, 8 tham gia cả Toán và Robot, và 5 sinh viên tham gia cả ba CLB. Hỏi có bao nhiêu sinh viên tham gia ít nhất một CLB?

<details>
<summary>Đáp án</summary>

<div class="textbook-equation" markdown="1">
$$
35+30+25-12-10-8+5=65.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Có 65 sinh viên tham gia ít nhất một CLB.

</details>

### Bài tập 2: Mật khẩu

Có bao nhiêu chuỗi nhị phân độ dài 8 chứa ít nhất một chữ số 0 và ít nhất một chữ số 1?

<details>
<summary>Đáp án</summary>

Tổng số chuỗi nhị phân độ dài 8 là $$2^8=256$$. Chuỗi không chứa chữ số 0 chỉ có một chuỗi `11111111`; chuỗi không chứa chữ số 1 chỉ có một chuỗi `00000000`. Vậy số chuỗi thỏa mãn là $$256-2=254$$.

</details>

### Bài tập 3: Chia hết

Tìm số lượng các số nguyên dương không vượt quá $$1000$$ chia hết cho $$3$$, $$5$$ hoặc $$7$$.

<details>
<summary>Đáp án</summary>

Số lượng các tập đơn lần lượt là $$333, 200, 142$$. Số lượng các giao đôi (chia hết cho $$15, 21, 35$$) lần lượt là $$66, 47, 28$$. Giao ba (chia hết cho $$105$$) có $$9$$ số. Do đó:

<div class="textbook-equation" markdown="1">
$$
333+200+142-66-47-28+9=543.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</details>

### Bài tập 4: Mật khẩu nhiều loại ký tự

**A.15** Suppose passwords are strings where the alphabet has 10 digits, 26 lower-case letters, 26 upper-case letters, and 15 special symbols.

(a) How many length-$$n$$ passwords contain at least two of the four types of characters?

(b) How many length-$$n$$ passwords have no two adjacent identical characters?

(c) How many length-$$n$$ passwords contain at least two of the four types of characters **and** have no two adjacent identical characters?

<details>
<summary>Đáp án</summary>

Đặt bốn loại ký tự là: D = chữ số (10), L = chữ thường (26), U = chữ hoa (26), S = ký tự đặc biệt (15). Tổng kích thước bảng chữ cái là $$10+26+26+15 = 77$$ (giả sử $$n \ge 1$$).

(a) Dùng dạng bù. Tổng số mật khẩu độ dài $$n$$ là $$77^n$$.

Một mật khẩu không có "ít nhất hai loại ký tự" tức là chỉ dùng đúng **một** loại ký tự (vì $$n \ge 1$$). Bốn tập hợp mật khẩu chỉ dùng 1 loại là rời nhau từng đôi một, có tổng kích thước:

<div class="textbook-equation" markdown="1">
$$
10^n + 26^n + 26^n + 15^n = 10^n + 2 \cdot 26^n + 15^n.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

Do đó, số mật khẩu chứa **ít nhất hai loại ký tự** là:

<div class="textbook-equation" markdown="1">
$$
77^n - \left(10^n + 2 \cdot 26^n + 15^n\right).
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

(b) Mật khẩu không có hai ký tự kề nhau giống nhau: ký tự đầu tiên có 77 cách chọn, mỗi ký tự tiếp theo có 76 cách chọn (khác ký tự đứng ngay trước nó). Vậy tổng số mật khẩu là $$77 \times 76^{n-1}$$.

(c) Kết hợp cả hai điều kiện. Gọi $$A$$ là tập mật khẩu có ít nhất hai loại ký tự và $$B$$ là tập mật khẩu không có hai ký tự kề nhau giống nhau. Ta cần tính $$\lvert A \cap B \rvert = \lvert B \rvert - \lvert\bar{A} \cap B \rvert$$, trong đó $$\bar{A}$$ là tập mật khẩu chỉ dùng đúng 1 loại ký tự.

Tính $$\lvert\bar{A} \cap B \rvert$$: với mỗi loại có $$k$$ ký tự ($$k \ge 2$$), số mật khẩu chỉ dùng loại đó và không có hai ký tự kề giống nhau là $$k \times (k-1)^{n-1}$$. Cụ thể:

- Chỉ dùng chữ số: $$10 \times 9^{n-1}$$
- Chỉ dùng chữ thường: $$26 \times 25^{n-1}$$
- Chỉ dùng chữ hoa: $$26 \times 25^{n-1}$$
- Chỉ dùng ký tự đặc biệt: $$15 \times 14^{n-1}$$

Tổng $$\lvert\bar{A} \cap B \rvert = 10 \times 9^{n-1} + 2 \cdot 26 \times 25^{n-1} + 15 \times 14^{n-1}$$.

Vậy kết quả là: $$\lvert A \cap B \rvert = 77 \times 76^{n-1} - \big(10 \times 9^{n-1} + 52 \times 25^{n-1} + 15 \times 14^{n-1}\big)$$.

</details>

## Xem thêm / Video gợi ý

- [Logic Gates, Truth Tables, Boolean Algebra](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — 3Blue1Brown (Animation + intuition for logic)
- [Introduction to Propositional Logic](https://www.youtube.com/watch?v=4l7L9v0p0Q) — MIT OCW 6.042J (Tom Leighton — formal foundation)

## Tóm tắt

- **Nguyên lý bù trừ** khử sai số do đếm trùng khi tính lực lượng hợp của nhiều tập hợp.
- **Quy tắc đan dấu**: cộng các tập đơn, trừ các giao đôi, cộng các giao ba và tiếp tục tương tự.
- **Dạng bù** rất thuận tiện khi cần đếm số đối tượng không vi phạm bất kỳ điều kiện nào.
- **Chứng minh theo phần tử** cho thấy mỗi phần tử thuộc hợp đều được đếm đúng một lần.
- **Ứng dụng trong Khoa học Máy tính**: truy vấn cơ sở dữ liệu, kiểm tra chính sách mật khẩu, sàng số nguyên tố, xác suất lỗi hệ thống và phân tích cấu hình bị cấm.

Trong bài tiếp theo, chúng ta sẽ học về hệ số nhị thức và các đồng nhất thức tổ hợp.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=GS7dIWA6Hpo">INCLUSION-EXCLUSION PRINCIPLE - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Trình bày công thức bao hàm–loại trừ từ cơ bản đến tổng quát.
- <a href="https://www.youtube.com/watch?v=U_kOuvs6zcw">Counting formula for two intersecting sets: N(A union B)=N(A)+N(B)-N(A intersect B)</a> — Dr. Trefor Bazett, tiếng Anh. Trường hợp hai tập giao nhau, làm nền tảng cho nguyên lý bù trừ.
- <a href="https://www.youtube.com/watch?v=Y0CYHMqomgI">[Discrete Mathematics] Inclusion Exclusion Problems</a> — TrevTutor, tiếng Anh. Luyện tập các bài toán bù trừ cho nhiều tập hợp.
