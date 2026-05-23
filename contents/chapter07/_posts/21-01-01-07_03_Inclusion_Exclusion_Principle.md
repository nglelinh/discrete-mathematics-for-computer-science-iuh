---
layout: post
title: "Nguyên lý Bù trừ"
categories: chapter07
date: 2021-01-01
order: 3
required: true
lang: en
---

# Nguyên lý Bù trừ

Khi nhiều điều kiện chồng lấn lên nhau, việc đếm bằng trực giác rất dễ sai. Ta cộng số phần tử của từng nhóm riêng lẻ, rồi vô tình đếm lặp những phần tử thuộc nhiều nhóm cùng lúc. Đây là lỗi rất thường gặp trong phân tích dữ liệu và cả trong xác suất.


Các quy tắc đếm cho ta cách ước lượng số cấu hình có thể xảy ra mà không cần liệt kê hết, đây là kỹ năng rất gần với phân tích thuật toán và kiểm thử.
**Nguyên lý bù trừ** cho ta một cách sửa sai có hệ thống. Ta cộng những gì cần có, trừ đi phần đã đếm trùng, và nếu nhiều lớp chồng lấn phức tạp hơn thì tiếp tục cộng trừ theo nhịp đúng.

Điều làm nguyên lý này quan trọng là nó không chỉ giải bài toán trên giấy. Nó xuất hiện khi đếm bản ghi thỏa nhiều điều kiện, khi tính xác suất hợp của nhiều biến cố, hay khi phân tích số cấu hình hợp lệ trong một hệ thống có ràng buộc giao nhau.

Trong bài này, chúng ta sẽ học cách dùng nguyên lý bù trừ từ trường hợp hai tập đơn giản đến các tình huống phức tạp hơn, nơi trực giác rất dễ đánh lừa chúng ta.

## 1. Đếm hợp của hai tập hợp

**Định nghĩa**: Với hai tập hữu hạn $A$ và $B$, **hợp** $A \cup B$ gồm các phần tử thuộc ít nhất một trong hai tập. **Giao** $A \cap B$ gồm các phần tử thuộc cả hai tập.

**Định lý**: Nếu $A$ và $B$ hữu hạn thì

$$
|A \cup B| = |A| + |B| - |A \cap B|.
$$

**Chứng minh**: Khi tính $|A| + |B|$, mỗi phần tử chỉ thuộc $A$ hoặc chỉ thuộc $B$ được đếm đúng một lần. Mỗi phần tử thuộc $A \cap B$ được đếm hai lần: một lần trong $|A|$ và một lần trong $|B|$. Vì trong hợp ta chỉ muốn đếm nó một lần, ta trừ đi $|A \cap B|$. Do đó công thức đúng.

<div class="content-box example-box" markdown="1">
**Ví dụ**: Trong một lớp có 50 sinh viên, 30 sinh viên học tiếng Anh, 20 sinh viên học tiếng Pháp, 10 sinh viên học cả hai. Số sinh viên học ít nhất một ngoại ngữ là

$$
30 + 20 - 10 = 40.
$$

Không thể trả lời $50$ chỉ vì $30+20=50$; con số $10$ ở phần giao là thông tin bắt buộc.
</div>

## 2. Nguyên lý bù trừ cho ba tập hợp

Với ba tập $A,B,C$, công thức là

$$
\begin{aligned}
|A \cup B \cup C|
&= |A| + |B| + |C| \\
&\quad - |A \cap B| - |A \cap C| - |B \cap C| \\
&\quad + |A \cap B \cap C|.
\end{aligned}
$$

**Tại sao phải cộng lại giao ba?** Một phần tử nằm trong cả ba tập được đếm $3$ lần ở bước cộng tập đơn, bị trừ $3$ lần ở bước trừ giao đôi, nên tổng tạm thời là $0$. Ta phải cộng lại một lần để nó được đếm đúng một lần.

<div class="interactive-tool" data-demo="inclusion-exclusion-toggle" markdown="1">
**Mô phỏng tương tác đề xuất**: Một bảng có ba công tắc `A`, `B`, `C`. Khi chọn vị trí của một phần tử trong sơ đồ Venn, công cụ hiển thị phần tử đó được cộng/trừ bao nhiêu lần trong công thức bù trừ.
</div>

<script src="{{ '/public/js/inclusion-exclusion-toggle.js' | relative_url }}"></script>

## 3. Công thức tổng quát cho $n$ tập hợp

Cho $A_1,A_2,\ldots,A_n$ là các tập hữu hạn. Khi đó

$$
\left|\bigcup_{i=1}^{n} A_i\right|
= \sum_i |A_i|
- \sum_{i<j}|A_i\cap A_j|
+ \sum_{i<j<k}|A_i\cap A_j\cap A_k|
- \cdots
+ (-1)^{n+1}|A_1\cap\cdots\cap A_n|.
$$

Dạng compact hơn:

$$
\left|\bigcup_{i=1}^{n} A_i\right|
= \sum_{\emptyset \neq I \subseteq \{1,2,\ldots,n\}} (-1)^{|I|+1}\left|\bigcap_{i\in I} A_i\right|.
$$

**Khối chứng minh**: Xét một phần tử $x$ thuộc đúng $r$ trong $n$ tập. Trong vế phải, $x$ đóng góp

$$
\binom{r}{1}-\binom{r}{2}+\binom{r}{3}-\cdots+(-1)^{r+1}\binom{r}{r}.
$$

Theo khai triển nhị thức,

$$
(1-1)^r = \binom{r}{0}-\binom{r}{1}+\binom{r}{2}-\cdots+(-1)^r\binom{r}{r}=0.
$$

Suy ra tổng xen kẽ không có hạng $\binom{r}{0}$ bằng $1$. Vậy mỗi phần tử thuộc hợp được đếm đúng một lần.

## 4. Dạng bù: đếm phần tử không vi phạm điều kiện nào

Nhiều bài toán dễ hơn nếu đếm số đối tượng **vi phạm ít nhất một điều kiện**, rồi lấy tổng trừ đi số đó.

Nếu $U$ là không gian tất cả đối tượng và $A_i$ là tập các đối tượng vi phạm điều kiện thứ $i$, thì số đối tượng hợp lệ là

$$
|U|-\left|\bigcup_i A_i\right|.
$$

**Ví dụ**: Có bao nhiêu số từ $1$ đến $100$ không chia hết cho $2$, $3$, hoặc $5$?

Gọi $A_2,A_3,A_5$ lần lượt là các số chia hết cho $2,3,5$. Ta có

$$
|A_2|=50,\quad |A_3|=33,\quad |A_5|=20,
$$

$$
|A_2\cap A_3|=16,\quad |A_2\cap A_5|=10,\quad |A_3\cap A_5|=6,
$$

$$
|A_2\cap A_3\cap A_5|=3.
$$

Do đó số bị loại là $50+33+20-16-10-6+3=74$. Số hợp lệ là $100-74=26$.

## 5. Ghi chú dễ nhầm

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn thường gặp**:

- Chỉ trừ giao đôi trong bài toán ba tập mà quên cộng giao ba.
- Dùng công thức cho tập rời nhau trong khi các tập có giao nhau.
- Đếm giao bằng cách lấy ước chung sai: số chia hết cho $2$ và $6$ là số chia hết cho $\operatorname{lcm}(2,6)=6$, không phải $12$.
- Quên xác định không gian nền $U$ khi dùng dạng bù.
</div>

## 6. Ứng dụng trong Khoa học Máy tính

Phần ứng dụng là nơi khái niệm toán học được gắn lại với bài toán thật trong lập trình và hệ thống. Hãy chú ý mô hình nào được giữ lại và mô hình nào đã được lược bỏ.

Trong cơ sở dữ liệu, truy vấn `OR` giữa nhiều điều kiện có thể tạo ra bản ghi trùng. Hệ quản trị phải loại trùng tương tự nguyên lý bù trừ. Trong bảo mật, khi đếm số mật khẩu thỏa các điều kiện “có chữ hoa”, “có chữ số”, “có ký tự đặc biệt”, cách hiệu quả là đếm phần bù: mật khẩu thiếu ít nhất một loại ký tự. Trong thuật toán, bù trừ xuất hiện trong sàng số nguyên tố, tính xác suất lỗi của hệ thống nhiều thành phần và phân tích các cấu hình bị cấm.

```python
from itertools import combinations

def inclusion_exclusion(sizes):
    # sizes[k] chứa tổng kích thước các giao của đúng k tập, k bắt đầu từ 1
    return sum(((-1) ** (k + 1)) * value for k, value in sizes.items())

print(inclusion_exclusion({1: 50 + 33 + 20, 2: 16 + 10 + 6, 3: 3}))
```

## Bài tập thực hành

### Bài tập 1: Ba câu lạc bộ

Một lớp có 80 sinh viên. Có 35 sinh viên tham gia CLB Lập trình, 30 tham gia CLB Toán, 25 tham gia CLB Robot. Có 12 sinh viên tham gia cả Lập trình và Toán, 10 tham gia cả Lập trình và Robot, 8 tham gia cả Toán và Robot, và 5 tham gia cả ba. Hỏi có bao nhiêu sinh viên tham gia ít nhất một CLB?

<details>
<summary>Đáp án</summary>

$$
35+30+25-12-10-8+5=65.
$$

Có 65 sinh viên tham gia ít nhất một CLB.

</details>

### Bài tập 2: Mật khẩu

Có bao nhiêu chuỗi nhị phân độ dài 8 chứa ít nhất một số 0 và ít nhất một số 1?

<details>
<summary>Đáp án</summary>

Tổng số chuỗi là $2^8=256$. Chuỗi không có số 0 chỉ có một chuỗi `11111111`; chuỗi không có số 1 chỉ có một chuỗi `00000000`. Vậy số cần tìm là $256-2=254$.

</details>

### Bài tập 3: Chia hết

Tìm số nguyên dương không vượt quá $1000$ chia hết cho $3$ hoặc $5$ hoặc $7$.

<details>
<summary>Đáp án</summary>

Các số lượng đơn: $333,200,142$. Giao đôi: chia hết cho $15,21,35$ lần lượt là $66,47,28$. Giao ba: chia hết cho $105$ là $9$. Do đó

$$
333+200+142-66-47-28+9=543.
$$

</details>

## Tóm tắt

- **Nguyên lý bù trừ** sửa sai cho việc đếm trùng trong hợp các tập hợp.
- **Dấu xen kẽ**: cộng tập đơn, trừ giao đôi, cộng giao ba, và tiếp tục như vậy.
- **Dạng bù** đặc biệt hữu ích khi đếm các đối tượng không vi phạm điều kiện nào.
- **Chứng minh phần tử** cho thấy mỗi phần tử thuộc hợp được đếm đúng một lần.
- **Ứng dụng CS** gồm truy vấn dữ liệu, kiểm tra mật khẩu, sàng số, xác suất lỗi và phân tích cấu hình bị cấm.

Trong bài tiếp theo, chúng ta sẽ học về hệ số nhị thức và các đồng nhất thức tổ hợp.
