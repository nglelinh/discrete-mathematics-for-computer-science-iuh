---

layout: post
title: "Nguyên lý Bao hàm - Loại trừ"
categories: chapter11
date: 2021-01-01
order: 3
required: true
lang: vi
excerpt: "Xây dựng nguyên lý bao hàm–loại trừ (inclusion–exclusion) để đếm chính xác hợp của nhiều tập hợp giao nhau, kèm chứng minh tổng quát và dạng bù."
---

Giả sử lớp có 30 sinh viên học Python và 25 sinh viên học SQL — tổng số sinh viên học ít nhất một trong hai môn có phải là $$30 + 25 = 55$$ không? Chỉ đúng khi không ai học cả hai! Nếu có 10 bạn học cả hai môn, phép cộng ngây thơ đã đếm nhầm 10 bạn đó hai lần, buộc ta phải trừ đi 10. **Nguyên lý Bao hàm – Loại trừ (Inclusion–Exclusion Principle)** khái quát trực giác "cộng thừa rồi trừ bớt, trừ quá lại cộng bù" này lên $$n$$ tập hợp bất kỳ.

**Mạch bài học:** Từ công thức 2 tập và 3 tập trên biểu đồ Venn $$\longrightarrow$$ công thức tổng quát với **dấu xen kẽ $$(-1)^{k-1}$$** $$\longrightarrow$$ **dạng phần bù** đếm các phần tử **không** thỏa bất kỳ tính chất cấm nào $$\longrightarrow$$ ứng dụng đếm số chia hết.

## Bản đồ kiến thức nền: Nguyên lý Bao hàm – Loại trừ đứng ở đâu trong Toán rời rạc?

- **Lý thuyết đếm với tập giao nhau (Overlapping Counting):** Quy tắc cộng cơ bản đòi hỏi các tập rời nhau đôi một. Bao hàm – Loại trừ dỡ bỏ hoàn toàn điều kiện rời nhau đó bằng cách hiệu chỉnh lần lượt theo kích thước giao bậc 2, bậc 3, ..., bậc $$n$$.
- **Chứng minh bằng Định lý Nhị thức (Binomial Cancellation):** Tại sao một phần tử thuộc đúng $$m \ge 1$$ tập hợp luôn được đếm **đúng 1 lần** trong tổng xen kẽ? Vì số lần nó bị cộng–trừ là $$\binom{m}{1} - \binom{m}{2} + \binom{m}{3} - \cdots + (-1)^{m-1}\binom{m}{m} = 1 - (1 - 1)^m = 1$$!
- **Dạng phần bù & Ràng buộc phủ định (Complementary Form):** Trong khoa học máy tính và tổ hợp, ta thường muốn đếm các đối tượng **tránh toàn bộ các điều kiện lỗi $$A_1, \dots, A_n$$**: $$\vert \overline{A_1} \cap \cdots \cap \overline{A_n} \vert = \vert U \vert - \sum \vert A_i \vert + \sum \vert A_i \cap A_j \vert - \cdots$$.

Ở Chương 4, chúng ta đã làm việc với tập hợp cùng các phép toán hợp, giao và hiệu. Mục này xây dựng **nguyên lý bao hàm–loại trừ** (inclusion–exclusion) — công thức đếm chính xác $$\vert A_1 \cup \cdots \cup A_n\vert $$ khi các tập hợp có phần giao nhau. Nếu chỉ cộng trực tiếp $$\vert A_i\vert $$, các phần tử nằm trong phần giao sẽ bị đếm trùng; nguyên lý bù trừ xen kẽ dấu theo kích thước phần giao để khử sai số đó. Công cụ này được dùng rộng rãi trong lý thuyết xác suất, truy vấn cơ sở dữ liệu (`UNION`/`INTERSECT` trong SQL) và nhiều bài toán tổ hợp có ràng buộc chồng lấn.

![Bao hàm–loại trừ ba tập](/discrete-mathematics-for-computer-science-iuh/img/course/Inclusion-exclusion-3sets.svg)

<p class="textbook-figure-caption" data-figure="11.11">Công thức bao hàm–loại trừ cho ba tập: cộng từng tập, trừ các giao đôi, rồi cộng lại giao ba.</p>
![Giao hai tập A ∩ B](/discrete-mathematics-for-computer-science-iuh/img/course/Venn_A_intersect_B.svg)

<p class="textbook-figure-caption" data-figure="11.12">Phần giao bị đếm hai lần khi cộng $$\vert A\vert +\vert B\vert $$, do đó cần trừ đi $$\vert A\cap B\vert $$.</p>
![Hợp hai tập A ∪ B](/discrete-mathematics-for-computer-science-iuh/img/course/Union_of_sets_A_and_B.svg)

<p class="textbook-figure-caption" data-figure="11.13">Nguyên lý bao hàm–loại trừ cho $$\vert A\cup B\vert $$ — nền tảng của phép đếm có điều kiện chồng lấn.</p>
![De Morgan và bao hàm](/discrete-mathematics-for-computer-science-iuh/img/course/Intersections_of_two_sets_and_their_complements.svg)

<p class="textbook-figure-caption" data-figure="11.14">Dạng bù: đếm các phần tử không vi phạm điều kiện bằng cách lấy kích thước không gian mẫu trừ đi hợp các tập vi phạm.</p>
![Biểu đồ Venn ba tập](/discrete-mathematics-for-computer-science-iuh/img/course/Venn3.svg)

<p class="textbook-figure-caption" data-figure="11.15">Mô hình hóa trực quan các tập $$A_i$$ và phần giao giữa chúng trước khi áp dụng công thức.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Áp dụng** công thức bao hàm–loại trừ cho 2, 3 và $$n$$ tập hợp.
- **Chứng minh** công thức tổng quát bằng cách đếm số lần mỗi phần tử được tính.
- **Sử dụng dạng bù** để đếm các phần tử không vi phạm ràng buộc nào.
- **Liên hệ** với hàm sinh: nhiều hệ số trong $$G(x)$$ có thể tính qua bao hàm–loại trừ trên các lớp tương đương (mục 11.4–11.5).

**Từ khóa**: bao hàm–loại trừ (inclusion–exclusion), dạng bù, giao tập, đếm có ràng buộc, derangement (xem 11.4).

**Khác với Chương 7**: Mục 7.3 giới thiệu bao hàm–loại trừ cơ bản trong phép đếm; mục này (Chương 11) tập trung vào **chứng minh tổng quát**, **dạng bù** và **cầu nối sang hàm sinh** cho các bài toán nâng cao.
</div>

### Video ngắn: Nguyên lý bù trừ

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/inclusion-exclusion.mp4"></video>
</div>

Video dài khoảng 3 phút 6 giây, trình bày ví dụ lớp 50 sinh viên với hai tập hợp, theo dõi số lần mỗi vùng trong biểu đồ Venn ba tập được cộng hoặc trừ qua từng bước, tính số nguyên từ 1 đến 100 chia hết cho 2, 3 hoặc 5 (kết quả 74, đối chiếu trên lưới 100 ô), bài tập đếm số từ 1 đến 1000 không chia hết cho 3, 5 và 7 (kết quả 457), phát biểu công thức tổng quát cho $$n$$ tập và giới thiệu bài toán bỏ thư sao cho không lá nào vào đúng phong bì.

## Công thức cho hai và ba tập

<div class="textbook-definition" markdown="1">
**Định nghĩa** (hai tập): Với hai tập hữu hạn $$A, B$$,
$$\vert A \cup B\vert  = \vert A\vert  + \vert B\vert  - \vert A \cap B\vert .$$
</div>

Với hai tập hữu hạn $$A,B$$:

<div class="textbook-equation" markdown="1">
$$
|A\cup B|=|A|+|B|-|A\cap B|.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Với ba tập hữu hạn $$A,B,C$$:

<div class="textbook-equation" markdown="1">
$$
|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Giải thích**: Một phần tử thuộc đúng một tập được đếm đúng một lần; thuộc hai tập sẽ bị cộng hai lần rồi trừ một lần; thuộc cả ba tập sẽ bị cộng ba lần, trừ ba lần, rồi cộng lại một lần.

## Công thức tổng quát

<div class="textbook-definition" markdown="1">
**Định nghĩa** (tổng quát): Cho các tập hữu hạn $$A_1, \ldots, A_n$$,

<div class="textbook-equation" markdown="1">
$$
\left|\bigcup_{i=1}^{n}A_i\right|
=\sum_{\emptyset\neq I\subseteq\{1,\ldots,n\}}(-1)^{|I|+1}\left|\bigcap_{i\in I}A_i\right|.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh bằng đếm số lần**: Xét một phần tử bất kỳ thuộc đúng $$r$$ tập trong số $$A_1, \ldots, A_n$$ ($$r \ge 1$$). Trong vế phải của công thức trên, số lần phần tử này được đếm là

<div class="textbook-equation" markdown="1">
$$
\binom{r}{1}-\binom{r}{2}+\binom{r}{3}-\cdots+(-1)^{r+1}\binom{r}{r}=1.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Do đó, mỗi phần tử thuộc hợp đều được đếm đúng một lần.
</div>

<div class="textbook-theorem" markdown="1">
**Quy tắc ghi nhớ**: Dấu trong công thức xen kẽ theo số tập tham gia phép giao: cộng từng tập đơn, trừ giao hai tập, cộng giao ba tập và tiếp tục tương tự.
</div>

## Dạng bù

Thay vì đếm trực tiếp hợp của các tập, ta thường đếm số phần tử **không vi phạm điều kiện nào** bằng cách lấy tổng số phần tử của không gian mẫu trừ đi kích thước hợp của các tập vi phạm.

<div class="textbook-example" markdown="1">
**Ví dụ**: Số chuỗi nhị phân độ dài 8 chứa ít nhất một bit 0 và ít nhất một bit 1 (tức loại trừ hai chuỗi toàn 0 và toàn 1) là

<div class="textbook-equation" markdown="1">
$$
2^8-2=254.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>


## Ví dụ với điều kiện chia hết

Ta áp dụng công thức bao hàm–loại trừ cho hai tập giao nhau: mỗi tập ứng với một điều kiện chia hết, còn phần giao ứng với các số thỏa mãn đồng thời cả hai điều kiện.

Đếm các số nguyên từ 1 đến 100 chia hết cho 2 hoặc 5.

Gọi $$A$$ là tập các số chia hết cho 2 và $$B$$ là tập các số chia hết cho 5 trong đoạn từ 1 đến 100. Khi đó:

<div class="textbook-equation" markdown="1">
$$
|A|=50,\quad |B|=20,\quad |A\cap B|=10.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Suy ra:

<div class="textbook-equation" markdown="1">
$$
|A\cup B|=50+20-10=60.
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="interactive-tool" markdown="1">
**Demo tương tác đề xuất**: Công cụ cho phép bật/tắt ba tập hợp trong biểu đồ Venn và hiển thị số lần mỗi vùng được cộng hoặc trừ trong công thức.
<div data-demo="venn-ie-three-sets"></div>
</div>
<script src="{{ '/public/js/venn-ie-three-sets.js' | relative_url }}"></script>

### Minh họa tương tác

Minh họa biểu đồ Venn ở chế độ bao hàm–loại trừ giúp quan sát trực tiếp vì sao các vùng giao bị đếm dư rồi được trừ lại.

<div class="interactive-demo" markdown="1">
<div data-demo="venn-explainer" data-sets="3" data-focus="ie"></div>
</div>
<script src="{{ '/public/js/explainers/venn-explainer.js' | relative_url }}"></script>

## Ví dụ tính tay cầm tay chỉ việc: Đếm số nguyên từ 1 đến 100 KHÔNG chia hết cho 2, 3 hoặc 5

Đặt vũ trụ $$U = \{1, 2, \dots, 100\}$$ ($$\vert U \vert = 100$$), và các tập "vi phạm":
- $$A_2$$: các số chia hết cho 2; $$A_3$$: chia hết cho 3; $$A_5$$: chia hết cho 5.

1. **Đếm từng tập đơn (cộng vào phần vi phạm):**
   - $$\vert A_2 \vert = \lfloor 100/2 \rfloor = 50$$
   - $$\vert A_3 \vert = \lfloor 100/3 \rfloor = 33$$
   - $$\vert A_5 \vert = \lfloor 100/5 \rfloor = 20$$
   - Tổng bậc 1: $$S_1 = 50 + 33 + 20 = 103$$.
2. **Đếm các giao đôi (trừ phần bị đếm trùng):**
   - $$\vert A_2 \cap A_3 \vert = \lfloor 100/6 \rfloor = 16$$
   - $$\vert A_2 \cap A_5 \vert = \lfloor 100/10 \rfloor = 10$$
   - $$\vert A_3 \cap A_5 \vert = \lfloor 100/15 \rfloor = 6$$
   - Tổng bậc 2: $$S_2 = 16 + 10 + 6 = 32$$.
3. **Đếm giao ba (cộng bù lại phần vừa bị trừ sạch):**
   - $$\vert A_2 \cap A_3 \cap A_5 \vert = \lfloor 100/30 \rfloor = 3$$ (gồm 30, 60, 90).
   - Tổng bậc 3: $$S_3 = 3$$.
4. **Áp dụng công thức Bao hàm – Loại trừ:**
   - Số chia hết cho ít nhất một trong 2, 3, 5:
     $$\vert A_2 \cup A_3 \cup A_5 \vert = S_1 - S_2 + S_3 = 103 - 32 + 3 = 74.$$
   - Số **KHÔNG** chia hết cho cả 2, 3 và 5 (dạng phần bù):
     $$\vert \overline{A_2} \cap \overline{A_3} \cap \overline{A_5} \vert = 100 - 74 = 26\text{ số!}$$

### Khung giải thích: Tại sao dấu cộng–trừ xen kẽ luôn triệt tiêu chính xác sai số (nên đọc chậm)

1. **Bước 1 — Theo dõi số phận của một phần tử nằm trong đúng $$m$$ tập:** Giả sử số `30` nằm trong cả $$A_2, A_3, A_5$$ ($$m = 3$$). Trong $$S_1$$ nó được cộng $$\binom{3}{1} = 3$$ lần; trong $$-S_2$$ nó bị trừ $$\binom{3}{2} = 3$$ lần (tạm về 0); đến $$+S_3$$ nó được cộng lại $$\binom{3}{3} = 1$$ lần — tổng cuối cùng là $$3 - 3 + 1 = 1$$!
2. **Bước 2 — Quy tắc đảo ngược bài toán sang tập vi phạm:** Khi đề bài yêu cầu "không có tính chất nào trong $$P_1, \dots, P_n$$", hãy định nghĩa $$A_i$$ là tập **vi phạm** điều kiện $$i$$ — vì phần giao $$A_i \cap A_j$$ (đồng thời vi phạm cả $$i$$ và $$j$$) luôn dễ đếm hơn nhiều so với hợp trực tiếp.
3. **Bước 3 — Bất đẳng thức Bonferroni khi không tính hết được:** Nếu $$n$$ quá lớn ($$2^n$$ số hạng), chỉ cần dừng ở bậc lẻ ta có **cận trên** ($$S_1$$, $$S_1 - S_2 + S_3$$), còn dừng ở bậc chẵn ta có **cận dưới** ($$S_1 - S_2$$) — rất hữu ích trong ước lượng xác suất và truy vấn CSDL!

$$\left\vert \bigcup_{i=1}^n A_i \right\vert = \sum_{k=1}^n (-1)^{k-1} \sum_{1 \le i_1 < \cdots < i_k \le n} \left\vert A_{i_1} \cap \cdots \cap A_{i_k} \right\vert.$$

## Bài tập

### Bài tập 1

Trong một lớp có 30 học sinh, 18 em học Toán, 15 em học Lý và 8 em học cả hai môn. Hỏi có bao nhiêu học sinh học ít nhất một trong hai môn?

<details>
<summary>Đáp án</summary>

$$\vert A \cup B\vert  = 18 + 15 - 8 = 25$$ học sinh.

</details>

### Bài tập 2

Đếm số nguyên từ 1 đến 1000 **không** chia hết cho bất kỳ số nào trong 2, 3 và 5.

<details>
<summary>Đáp án</summary>

Áp dụng dạng bù: $$1000 - \vert A_2 \cup A_3 \cup A_5\vert $$, trong đó $$\vert A_2\vert =500$$, $$\vert A_3\vert =333$$, $$\vert A_5\vert =200$$; các giao đôi lần lượt là $$\vert A_2 \cap A_3\vert = 166$$, $$\vert A_2 \cap A_5\vert = 100$$, $$\vert A_3 \cap A_5\vert = 66$$; giao ba là $$\vert A_2 \cap A_3 \cap A_5\vert = 33$$. Theo công thức bao hàm–loại trừ: $$500+333+200-166-100-66+33=734$$ số chia hết cho ít nhất một trong ba số. Đáp số: $$1000 - 734 = 266$$.

</details>

### Bài tập 3

Giải thích vì sao trong chứng minh nguyên lý bao hàm–loại trừ, một phần tử thuộc đúng $$r$$ tập được đếm đúng một lần (tức là $$\binom{r}{1} - \binom{r}{2} + \cdots + (-1)^{r+1}\binom{r}{r} = 1$$).

<details>
<summary>Đáp án</summary>

Theo khai triển nhị thức Newton, $$(1-1)^r = \sum_{k=0}^{r} (-1)^k \binom{r}{k} = 0$$. Khi tách hạng tử $$k=0$$ (bằng $$\binom{r}{0} = 1$$) sang vế kia và đổi dấu, ta thu được $$\binom{r}{1} - \binom{r}{2} + \cdots + (-1)^{r+1}\binom{r}{r} = 1$$.

</details>

### Bài tập 4

Có bao nhiêu hoán vị của $$\{1,\ldots,5\}$$ **không** có điểm cố định (derangement)? (Gợi ý: dùng dạng bù với $$A_i$$ là tập các hoán vị giữ cố định vị trí $$i$$.)

<details>
<summary>Đáp án</summary>

$$5! - \binom{5}{1}4! + \binom{5}{2}3! - \binom{5}{3}2! + \binom{5}{4}1! - \binom{5}{5}0! = 120 - 120 + 60 - 20 + 5 - 1 = 44$$. (Công thức tổng quát được trình bày ở mục 11.4.)

</details>

---

## Xem thêm / Video gợi ý

- <a href="https://www.youtube.com/watch?v=FMc7pZbvWKA">Logical Equivalences | Prepositional Logic | Discrete Mathematics</a> — NotesForMsc (Truth table proof + laws)
- [Discrete Math Full Course — Logic & Proofs](https://www.youtube.com/playlist?list=PLHXZ9OQGMqxersk8fUxiUMSIx0DBqsKZS) — Trefor Bazett (Complete semester playlist)


## Tóm tắt

- Công thức cho hai tập: $$\vert A \cup B\vert  = \vert A\vert  + \vert B\vert  - \vert A \cap B\vert $$; với ba tập, ta cộng các tập đơn, trừ các giao đôi và cộng lại giao ba.
- Công thức tổng quát: $$\vert \bigcup A_i\vert  = \sum (-1)^{\vert I\vert +1} \vert \bigcap_{i\in I} A_i\vert $$.
- **Chứng minh bằng đếm số lần**: mỗi phần tử thuộc đúng $$r$$ tập đều được đếm đúng một lần.
- **Dạng bù**: số phần tử không vi phạm điều kiện bằng kích thước không gian mẫu trừ đi hợp các tập vi phạm.
- Ứng dụng cơ bản: đếm số chia hết cho 2 hoặc 5 trong đoạn $$1..100$$.

Trong bài tiếp theo, chúng ta sẽ áp dụng nguyên lý này vào sàng Legendre, hàm Euler $$\phi(n)$$, số toàn ánh và derangement.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=GS7dIWA6Hpo">INCLUSION-EXCLUSION PRINCIPLE - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Trình bày phát biểu nguyên lý bao hàm–loại trừ.
- <a href="https://www.youtube.com/watch?v=41TcebW7-4c">Counting with Triple Intersections // Example &amp; Formula</a> — Dr. Trefor Bazett, tiếng Anh. Minh họa công thức mở rộng cho giao của ba tập hợp.
- <a href="https://www.youtube.com/watch?v=D1T3xy_vtxU">[Discrete Mathematics] Inclusion-Exclusion: At Least &amp; Exactly</a> — TrevTutor, tiếng Anh. Kỹ thuật đếm điều kiện “ít nhất” và “đúng bằng” bằng nguyên lý bù trừ.
