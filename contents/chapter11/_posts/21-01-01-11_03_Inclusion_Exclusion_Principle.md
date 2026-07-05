---

layout: post
title: "Nguyên lý Bao hàm - Loại trừ"
categories: chapter11
date: 2021-01-01
order: 3
required: true
lang: vi
excerpt: "Ở Chương 4 chúng ta đã làm việc với tập hợp, hợp, giao và hiệu. Mục này xây dựng nguyên lý bao hàm–loại trừ (inclusion–exclusion) — công thức chính xác đếm…"
---

Ở Chương 4 chúng ta đã làm việc với tập hợp, hợp, giao và hiệu. Mục này xây dựng **nguyên lý bao hàm–loại trừ** (inclusion–exclusion) — công thức chính xác đếm $$|A_1 \cup \cdots \cup A_n|$$ khi các tập con có giao nhau. Cộng thẳng $$|A_i|$$ sẽ đếm trùng phần giao; nguyên lý bù trừ xen kẽ theo kích thước giao sửa sai số đó. Công cụ này xuất hiện trong xác suất, truy vấn dữ liệu (`UNION`/`INTERSECT` trong SQL) và nhiều bài toán tổ hợp có ràng buộc chồng lấn.

![Bao hàm–loại trừ ba tập](/discrete-mathematics-for-computer-science-iuh/img/course/Inclusion-exclusion-3sets.svg)

<p class="textbook-figure-caption" data-figure="11.11">Công thức bao hàm–loại trừ cho ba tập — cộng từng tập, trừ giao đôi, cộng giao ba.</p>
![Giao hai tập A ∩ B](/discrete-mathematics-for-computer-science-iuh/img/course/Venn_A_intersect_B.svg)

<p class="textbook-figure-caption" data-figure="11.12">Phần giao bị đếm hai lần khi cộng $|A|+|B|$ — phải trừ $|A\cap B|$.</p>
![Hợp hai tập A ∪ B](/discrete-mathematics-for-computer-science-iuh/img/course/Union_of_sets_A_and_B.svg)

<p class="textbook-figure-caption" data-figure="11.13">Nguyên lý bao hàm–loại trừ cho $|A\cup B|$ — nền tảng đếm có điều kiện chồng lấn.</p>
![De Morgan và bao hàm](/discrete-mathematics-for-computer-science-iuh/img/course/Intersections_of_two_sets_and_their_complements.svg)

<p class="textbook-figure-caption" data-figure="11.14">Dạng bù: đếm phần tử không vi phạm điều kiện bằng tổng không gian trừ hợp vi phạm.</p>
![Biểu đồ Venn ba tập](/discrete-mathematics-for-computer-science-iuh/img/course/Venn3.svg)

<p class="textbook-figure-caption" data-figure="11.15">Mô hình hóa trực quan các tập $A_i$ và giao của chúng trước khi áp công thức.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Áp dụng** công thức bao hàm–loại trừ cho 2, 3 và $$n$$ tập.
- **Chứng minh** công thức tổng quát bằng đếm số lần mỗi phần tử xuất hiện.
- **Dùng dạng bù** đếm phần tử không vi phạm ràng buộc.
- **Liên hệ** với hàm sinh: hệ số trong $$G(x)$$ đôi khi lấy từ IE trên các lớp tương đương (mục 11.4–11.5).

**Từ khóa**: bao hàm–loại trừ (inclusion–exclusion), dạng bù, giao tập, đếm có ràng buộc, derangement (xem 11.4).

**Khác Ch.7**: Mục 7.3 giới thiệu IE cơ bản trong đếm; mục này (Ch.11) nhấn mạnh **chứng minh tổng quát**, **dạng bù** và **cầu nối sang hàm sinh** cho bài toán nâng cao.
</div>

## Công thức cho hai và ba tập

<div class="textbook-definition" markdown="1">
**Định nghĩa** (hai tập): Với $$A, B$$ hữu hạn,
$$|A \cup B| = |A| + |B| - |A \cap B|.$$
</div>

Với hai tập hữu hạn $A,B$,

<div class="textbook-equation" markdown="1">
$$
|A\cup B|=|A|+|B|-|A\cap B|.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Với ba tập $A,B,C$,

<div class="textbook-equation" markdown="1">
$$
|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Giải thích**: Một phần tử nằm trong đúng một tập được đếm đúng một lần; nằm trong hai tập thì bị cộng hai lần rồi trừ một lần; nằm trong ba tập thì bị cộng ba lần, trừ ba lần, rồi cộng lại một lần.

## Công thức tổng quát

<div class="textbook-definition" markdown="1">
**Định nghĩa** (tổng quát): Cho các tập hữu hạn $$A_1, \ldots, A_n$$,
</div>

<div class="textbook-equation" markdown="1">
$$
\left|\bigcup_{i=1}^{n}A_i\right|
=\sum_{\emptyset\neq I\subseteq\{1,\ldots,n\}}(-1)^{|I|+1}\left|\bigcap_{i\in I}A_i\right|.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Chứng minh bằng đếm số lần**: Xét một phần tử thuộc đúng $r$ tập. Trong tổng trên, nó được tính

<div class="textbook-equation" markdown="1">
$$
\binom{r}{1}-\binom{r}{2}+\binom{r}{3}-\cdots+(-1)^{r+1}\binom{r}{r}=1.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Do đó mỗi phần tử trong hợp được đếm đúng một lần.

<div class="textbook-theorem" markdown="1">
**Quy tắc nhớ**: Dấu xen kẽ theo kích thước giao: tập đơn cộng, giao đôi trừ, giao ba cộng, rồi tiếp tục như vậy.
</div>

## Dạng bù

Thay vì đếm phần hợp trực tiếp, ta thường đếm số phần tử **không vi phạm điều kiện nào** bằng cách lấy tổng không gian mẫu trừ đi hợp của các tập vi phạm.

<div class="textbook-example" markdown="1">
**Ví dụ**: Số chuỗi nhị phân độ dài 8 có ít nhất một bit 0 và ít nhất một bit 1 là

<div class="textbook-equation" markdown="1">
$$
2^8-2=254.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>


## Ví dụ với chia hết

Ta áp dụng công thức bao hàm–loại trừ cho hai tập giao nhau: mỗi tập mô tả một điều kiện chia hết, giao tương ứng phần tử thỏa cả hai.

Đếm các số từ 1 đến 100 chia hết cho 2 hoặc 5.

Gọi $A$ là tập số chia hết cho 2, $B$ là tập số chia hết cho 5. Khi đó

<div class="textbook-equation" markdown="1">
$$
|A|=50,\quad |B|=20,\quad |A\cap B|=10.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Vậy

<div class="textbook-equation" markdown="1">
$$
|A\cup B|=50+20-10=60.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="interactive-tool" markdown="1">
**Demo tương tác đề xuất**: Công cụ cho phép bật/tắt ba tập trong sơ đồ Venn và hiển thị số lần mỗi vùng được cộng hoặc trừ trong công thức.
<div data-demo="venn-ie-three-sets"></div>
</div>
<script src="{{ '/public/js/venn-ie-three-sets.js' | relative_url }}"></script>

## Bài tập

### Bài tập 1

Trong lớp 30 học sinh, 18 học Toán, 15 học Lý, 8 học cả hai. Hỏi có bao nhiêu học sinh học ít nhất một trong hai môn?

<details>
<summary>Đáp án</summary>

$$|A \cup B| = 18 + 15 - 8 = 25$$.

</details>

### Bài tập 2

Đếm số nguyên từ 1 đến 1000 **không** chia hết cho 2, 3 và 5.

<details>
<summary>Đáp án</summary>

Dạng bù: $$1000 - |A_2 \cup A_3 \cup A_5|$$ với $$|A_2|=500$$, $$|A_3|=333$$, $$|A_5|=200$$, giao đôi 166, 100, 66, giao ba 33. IE: $$500+333+200-166-100-66+33=734$$ vi phạm. Đáp số: $$1000 - 734 = 266$$.

</details>

### Bài tập 3

Giải thích vì sao trong chứng minh IE, phần tử thuộc đúng $$r$$ tập được đếm đúng một lần (công thức $$\binom{r}{1} - \binom{r}{2} + \cdots = 1$$).

<details>
<summary>Đáp án</summary>

Đó là khai triển $$(1-1)^r$$ với dấu $$(-1)^{k+1}$$ trên $$\binom{r}{k}$$ — tổng binô âm bằng 0 trừ hạng $$k=0$$; ở đây ta bắt đầu từ $$k=1$$ nên còn 1.

</details>

### Bài tập 4

Có bao nhiêu hoán vị của $$\{1,\ldots,5\}$$ **không** có điểm cố định (derangement)? (Gợi ý: dùng dạng bù với $$A_i$$ = “vị trí $$i$$ cố định”.)

<details>
<summary>Đáp án</summary>

$$5! - \binom{5}{1}4! + \binom{5}{2}3! - \binom{5}{3}2! + \binom{5}{4}1! - \binom{5}{5}0! = 120 - 120 + 60 - 20 + 5 - 1 = 44$$. (Công thức đầy đủ ở mục 11.4.)

</details>

---

## Xem thêm / Video gợi ý

- <a href="https://www.youtube.com/watch?v=FMc7pZbvWKA">Logical Equivalences | Prepositional Logic | Discrete Mathematics</a> — NotesForMsc (Truth table proof + laws)
- [Discrete Math Full Course — Logic & Proofs](https://www.youtube.com/playlist?list=PLHXZ9OQGMqxersk8fUxiUMSIx0DBqsKZS) — Trefor Bazett (Complete semester playlist)


## Tóm tắt

- Hai tập: $$|A \cup B| = |A| + |B| - |A \cap B|$$; ba tập: công thức cộng–trừ giao đôi, giao ba.
- Công thức tổng quát: $$|\bigcup A_i| = \sum (-1)^{|I|+1} |\bigcap_{i\in I} A_i|$$.
- **Chứng minh đếm số lần**: phần tử thuộc đúng $$r$$ tập được đếm đúng một lần.
- **Dạng bù**: đếm phần tử không vi phạm = không gian mẫu trừ hợp các tập vi phạm.
- Ứng dụng cơ bản: đếm số chia hết cho 2 hoặc 5 trong $$1..100$$.

Trong bài tiếp theo, chúng ta áp dụng nguyên lý vào sàng Legendre, hàm Euler $$\phi(n)$$, số toàn ánh và derangement.
