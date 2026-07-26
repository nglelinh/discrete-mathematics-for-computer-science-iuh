---

layout: post
title: "Quan hệ Tương đương và Thứ tự Bộ phận"
categories: chapter05
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Quan hệ tương đương và tập thương; thứ tự bộ phận/toàn phần, từ điển; Hasse; min/max, tối tiểu/tối đại và thứ tự tốt."
---

Ở mục trước chúng ta đã học bốn tính chất cơ bản của quan hệ. Mục này xây dựng hai lớp quan hệ đặc biệt từ các tính chất đó: **quan hệ tương đương** và **thứ tự bộ phận**.

Một số quan hệ giúp gom các đối tượng "giống nhau" theo một tiêu chí — như phân nhóm sinh viên theo lớp hay đồng dư modulo $$n$$. Một số quan hệ khác giúp sắp xếp đối tượng theo phụ thuộc hoặc bao hàm — như thứ bậc thư mục hay quan hệ chia hết. Cả hai đều xuất phát từ các tính chất đã định nghĩa, nhưng tạo ra hai kiểu cấu trúc rất khác nhau: lớp tương đương và phân hoạch ở một phía, poset và biểu đồ Hasse ở phía kia.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Xây dựng** lớp tương đương, tập thương $$A/R$$ và phân hoạch từ quan hệ tương đương.
- **Phân biệt** thứ tự toàn phần / bộ phận; định nghĩa thứ tự từ điển trên chuỗi bit.
- **Vẽ** sơ đồ Hasse; tìm phần tử nhỏ nhất/lớn nhất và tối tiểu/tối đại.
- **Nhận biết** thứ tự tốt (well-order) qua ví dụ $$(\mathbb{N},\le)$$ và $$(\mathbb{Z},\le)$$.
- **Áp dụng** modulo, phân vùng và thứ tự trong thiết kế hệ thống.

**Từ khóa**: lớp tương đương, phân hoạch, tập thương, thứ tự bộ phận, thứ tự toàn phần, thứ tự từ điển, sơ đồ Hasse, min/max, tối tiểu/tối đại, thứ tự tốt.
</div>

## 1. Quan hệ tương đương

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Quan hệ $$R$$ trên tập $$A$$ là **quan hệ tương đương** nếu thỏa ba tính chất:
</div>

1. **Phản xạ**: $$\forall a\in A,\ aRa$$.
2. **Đối xứng**: $$\forall a,b\in A,\ aRb\to bRa$$.
3. **Bắc cầu**: $$\forall a,b,c\in A,\ (aRb\land bRc)\to aRc$$.

**Ký hiệu**: Chúng ta thường viết $$a\sim b$$ thay cho $$(a,b)\in R$$ khi nói về quan hệ tương đương.

<div class="textbook-example" markdown="1">
**Ví dụ**: Quan hệ đồng dư modulo $$n$$ trên $$\mathbb{Z}$$:

<div class="textbook-equation" markdown="1">
$$a\equiv b\pmod n \quad\text{khi và chỉ khi}\quad n\mid(a-b).$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

### Chứng minh đồng dư modulo là quan hệ tương đương

- Phản xạ: $$a-a=0$$ chia hết cho $$n$$.
- Đối xứng: nếu $$n\mid(a-b)$$ thì $$n\mid-(a-b)=b-a$$.
- Bắc cầu: nếu $$n\mid(a-b)$$ và $$n\mid(b-c)$$ thì $$n\mid((a-b)+(b-c))=a-c$$.

Vậy đồng dư modulo $$n$$ là quan hệ tương đương.

![Quan hệ tương đương và phân hoạch](/discrete-mathematics-for-computer-science-iuh/img/course/Set_partitions_4__Hasse__matrices.svg)

<p class="textbook-figure-caption" data-figure="5.13">Quan hệ tương đương chia tập thành các lớp rời nhau — mỗi ma trận tương ứng một phân hoạch.</p>
## 2. Lớp tương đương và phân hoạch

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Với quan hệ tương đương $$\sim$$ trên $$A$$, **lớp tương đương** của $$a$$ là:
</div>

<div class="textbook-equation" markdown="1">
$$[a]=\{x\in A\mid x\sim a\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-theorem" markdown="1">
**Định lý**: Mỗi quan hệ tương đương trên $$A$$ tạo ra một phân hoạch của $$A$$ thành các lớp tương đương rời nhau; ngược lại, mỗi phân hoạch xác định một quan hệ tương đương.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**: Trên $$\mathbb{Z}$$ với modulo 3, có ba lớp:

- $$[0]=\{\ldots,-6,-3,0,3,6,\ldots\}$$.
- $$[1]=\{\ldots,-5,-2,1,4,7,\ldots\}$$.
- $$[2]=\{\ldots,-4,-1,2,5,8,\ldots\}$$.

![Lưới phân hoạch theo modulo](/discrete-mathematics-for-computer-science-iuh/img/course/Hasse_diagram_of_powerset_of_3.svg)

<p class="textbook-figure-caption" data-figure="5.14">Phân hoạch tạo các lớp tương đương rời nhau — tương tự cách sắp xếp phần tử theo cấu trúc thứ tự.</p>
</div>

**Tập thương.** Tập tất cả các lớp tương đương được ký hiệu $$A/R=\{[a]_R\mid a\in A\}$$ và gọi là **tập thương** (quotient set) của $$A$$ theo $$R$$. Mỗi phần tử $$x\in[a]_R$$ là một **đại diện** của lớp $$[a]_R$$.

Với đồng dư modulo $$m$$, tập thương $$\mathbb{Z}/R$$ có đúng $$m$$ lớp:

$$
\mathbb{Z}_m=\bigl\{[0]_m,[1]_m,\ldots,[m-1]_m\bigr\}.
$$

Đây chính là “số nguyên modulo $$m$$” dùng trong số học máy tính và mật mã.

<div class="textbook-theorem" markdown="1">
**Mệnh đề** (lớp trùng hoặc rời). Cho quan hệ tương đương $$R$$ trên $$A$$ và $$a,b\in A$$. Ba điều kiện sau tương đương:

1. $$aRb$$;
2. $$[a]_R=[b]_R$$;
3. $$[a]_R\cap[b]_R\neq\emptyset$$.

</div>

Hệ quả: các lớp hoặc **trùng nhau**, hoặc **rời nhau**; hợp của chúng bằng $$A$$ — đó chính là phân hoạch.

## 3. Quan hệ thứ tự bộ phận

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Quan hệ $$R$$ trên $$A$$ là **thứ tự bộ phận** (partial order) nếu thỏa:
</div>

1. **Phản xạ**: $$aRa$$.
2. **Phản đối xứng**: nếu $$aRb$$ và $$bRa$$ thì $$a=b$$.
3. **Bắc cầu**: nếu $$aRb$$ và $$bRc$$ thì $$aRc$$.

Khi đó cặp $$(A,R)$$ được gọi là một **poset**.

<div class="textbook-example" markdown="1">
**Ví dụ**:

- $$(\mathcal{P}(S),\subseteq)$$ là poset.
- $$(\mathbb{N},\mid)$$ với quan hệ chia hết là poset.
- Quan hệ "module A phải biên dịch trước module B" thường là thứ tự bộ phận nếu không có vòng phụ thuộc.
</div>

## 4. Thứ tự toàn phần, bộ phận và so sánh được

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Trong poset $$(S,\preceq)$$, hai phần tử $$a,b$$ gọi là **so sánh được** nếu $$a\preceq b$$ hoặc $$b\preceq a$$; nếu không, chúng **không so sánh được**.

Nếu mọi cặp phần tử của $$S$$ đều so sánh được thì $$(S,\preceq)$$ là **thứ tự toàn phần** (total / linear order). Ngược lại ta nói $$\preceq$$ là **thứ tự bán phần** (bộ phận).
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**:

- $$(\mathbb{Z}^+,\le)$$ là thứ tự toàn phần.
- $$(\mathbb{Z}^+,\mid)$$ **không** toàn phần: $$5$$ và $$7$$ không so sánh được.
- $$(\mathcal{P}(A),\subseteq)$$ không toàn phần khi $$\lvert A\rvert\ge 2$$: với $$S=\{a,b\}$$, hai tập $$\{a\}$$ và $$\{b\}$$ không so sánh được.

![Thứ tự bộ phận trên tập lũy thừa](/discrete-mathematics-for-computer-science-iuh/img/course/Hasse_diagram_of_powerset_of_3.svg)

<p class="textbook-figure-caption" data-figure="5.15">Poset $$(\mathcal{P}(S), \subseteq)$$ — không phải mọi cặp phần tử đều so sánh được (ví dụ {a} và {b}).</p>
</div>

### Thứ tự từ điển trên chuỗi bit

Trong tin học ta cần **một** thứ tự toàn phần trên chuỗi bit (sort, so sánh khóa, trie). Có nhiều cách định nghĩa “$$\le$$” trên $$\{0,1\}^n$$.

**Thứ tự tọa độ (product order).** Đặt

$$
a_1a_2\ldots a_n\le b_1b_2\ldots b_n
\quad\text{khi và chỉ khi}\quad
a_i\le b_i\text{ với mọi }i.
$$

Với định nghĩa này, $$0110$$ và $$1000$$ **không so sánh được** — đây vẫn là thứ tự bộ phận.

**Thứ tự từ điển (lexicographic order).** So sánh từ trái sang phải: tại vị trí khác nhau **đầu tiên** $$k$$, chuỗi có bit nhỏ hơn đứng trước. Trên $$\{0,1\}^n$$, thứ tự từ điển là **toàn phần** và trùng với thứ tự số nguyên khi đọc chuỗi như nhị phân. Đây là thứ tự `strcmp` / `sort` dùng hằng ngày.

<div class="textbook-example" markdown="1">
**Ví dụ**: Trên chuỗi độ dài 3, thứ tự từ điển:

$$000\prec 001\prec 010\prec 011\prec 100\prec 101\prec 110\prec 111.$$

Còn với product order, $$010$$ và $$100$$ không so sánh được.
</div>

## 5. Biểu đồ Hasse

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Biểu đồ Hasse là cách vẽ poset bằng cách:
</div>

- Bỏ các vòng phản xạ.
- Bỏ các cạnh suy ra từ bắc cầu (chỉ giữ **cạnh phủ**: $$a$$ phủ $$b$$ khi $$b\prec a$$ và không có $$c$$ “ở giữa”).
- Vẽ phần tử lớn hơn ở phía trên.

<div class="textbook-example" markdown="1">
**Ví dụ**: Poset các ước dương của 12 theo quan hệ chia hết gồm $$\{1,2,3,4,6,12\}$$. Các cạnh phủ là: $$1-2$$, $$1-3$$, $$2-4$$, $$2-6$$, $$3-6$$, $$4-12$$, $$6-12$$.

![Biểu đồ Hasse đơn giản](/discrete-mathematics-for-computer-science-iuh/img/course/Simple_hasse_diagram.svg)

<p class="textbook-figure-caption" data-figure="5.16">Biểu đồ Hasse bỏ vòng phản xạ và các cạnh suy ra từ bắc cầu, chỉ giữ các cặp phủ trực tiếp.</p>
</div>

Các ví dụ Hasse quen thuộc khác: $$(\mathcal{P}(\{a,b,c\}),\subseteq)$$ (lưới Boolean 3 chiều) và các chuỗi bit độ dài 3 với product order (cũng là hình lập phương).

## 6. Phần tử nhỏ nhất, lớn nhất và thứ tự tốt

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Trong poset $$(S,\preceq)$$,

- $$a$$ là **phần tử nhỏ nhất** (minimum, min) nếu $$a\preceq x$$ với mọi $$x\in S$$;
- $$a$$ là **phần tử lớn nhất** (maximum, max) nếu $$x\preceq a$$ với mọi $$x\in S$$.
</div>

Nếu tồn tại, min (lần lượt max) là **duy nhất**. Ký hiệu $$\min(S)$$, $$\max(S)$$.

<div class="textbook-example" markdown="1">
**Ví dụ**:

- $$S=\{m\in\mathbb{Z}\mid m^2<100\}$$ với $$\le$$: $$\min(S)=-9$$, $$\max(S)=9$$.
- $$A=\{x\in\mathbb{R}\mid x^2<100\}$$ với $$\le$$: **không** có min cũng không có max (mở).
- $$(\mathcal{P}(B),\subseteq)$$: $$\min=\emptyset$$, $$\max=B$$.
</div>

<div class="textbook-definition" markdown="1">
**Định nghĩa** (thứ tự tốt / well-order). Poset $$(S,\preceq)$$ gọi là **sắp tốt** (well-ordered) nếu **mọi** tập con khác rỗng của $$S$$ đều có phần tử nhỏ nhất.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**:

- $$(\mathbb{N},\le)$$ (hoặc $$\mathbb{Z}^+$$) là sắp tốt — đây là nền tảng cho quy nạp và “mọi vòng lặp giảm biến đếm đều dừng”.
- $$(\mathbb{Z},\le)$$ **không** sắp tốt: chính $$\mathbb{Z}$$ không có phần tử nhỏ nhất; tập các số chẵn âm cũng không.
</div>

**Liên hệ CS.** Khi chứng minh thuật toán kết thúc bằng “measure” trên $$\mathbb{N}$$, ta đang dùng tính well-order của số tự nhiên.

## 7. Phần tử tối tiểu và tối đại

Min/max là “đáy/đỉnh toàn cục”. Trong poset có thể không có min/max nhưng vẫn có các “đáy/đỉnh cục bộ”.

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Trong poset $$(S,\preceq)$$,

- $$a$$ là **tối tiểu** (minimal) nếu không tồn tại $$x\in S$$, $$x\neq a$$, sao cho $$x\preceq a$$;
- $$a$$ là **tối đại** (maximal) nếu không tồn tại $$x\in S$$, $$x\neq a$$, sao cho $$a\preceq x$$.
</div>

**Nhận xét quan trọng.**

1. Tối tiểu / tối đại **không nhất thiết duy nhất**.
2. Nếu tồn tại phần tử nhỏ nhất thì nó là tối tiểu **duy nhất**; tương tự max là tối đại duy nhất.
3. Trên Hasse: tối tiểu = đỉnh không có cạnh đi xuống; tối đại = đỉnh không có cạnh đi lên.

<div class="textbook-example" markdown="1">
**Ví dụ 1.** $$S=\{1,2,3\}$$ với

$$
R=\{(1,1),(2,2),(3,3),(1,2),(3,2)\}.
$$

Đây là poset. Tối tiểu: $$1$$ và $$3$$; tối đại: $$2$$. Không có min (vì không phần tử nào $$\preceq$$ cả ba).

**Ví dụ 2.** Poset $$(\{2,4,5,10,12,20,25\},\mid)$$:

- Tối tiểu: $$2$$, $$5$$;
- Tối đại: $$12$$, $$20$$, $$25$$.

Không có min/max toàn cục.

**Ví dụ 3.** Chuỗi bit độ dài 3 với product order (hoặc từ điển trên Hasse lập phương): tối tiểu duy nhất $$000$$, tối đại duy nhất $$111$$ — chúng cũng là min và max.
</div>

**Sự tồn tại trên poset hữu hạn.** Trong poset **hữu hạn** khác rỗng, luôn tồn tại ít nhất một tối tiểu và một tối đại. Chứng minh phác: xuất phát từ $$a_0$$ bất kỳ; nếu không tối tiểu thì có $$a_1\prec a_0$$; chuỗi giảm nghiêm ngặt không thể vô hạn trong tập hữu hạn, nên dừng ở tối tiểu. Tối đại tương tự theo chiều tăng.

## Định lý: Quan hệ tương đương ⇔ Phân hoạch

<div class="textbook-theorem" markdown="1">
**Định lý**: Cho tập \( A \).  
- Nếu \( R \) là quan hệ tương đương trên \( A \), thì các lớp tương đương của \( R \) tạo thành một **phân hoạch** của \( A \) (các tập con rời nhau, hợp lại bằng \( A \)).  
- Ngược lại, nếu \( \{A_i\} \) là một phân hoạch của \( A \), thì quan hệ “cùng nằm trong một \( A_i \)” là một quan hệ tương đương.
</div>

**Chứng minh** (chiều thuận):

1. **Phản xạ**: \( a R a \) vì \( a \) cùng lớp với chính nó.  
2. **Đối xứng**: Nếu \( a R b \) thì \( a, b \) cùng lớp ⇒ \( b R a \).  
3. **Bắc cầu**: Nếu \( a R b \) và \( b R c \) thì cả ba cùng lớp ⇒ \( a R c \).  
4. Các lớp rời nhau: nếu \( a \in [b] \cap [c] \) thì \( b R c \), nên \( [b] = [c] \).  
5. Hợp các lớp = \( A \): mọi \( a \) thuộc lớp \( [a] \).

Chiều ngược cũng dễ chứng minh tương tự.

**Hệ quả CS**:
- **Hash table**: mỗi bucket là một lớp tương đương (cùng hash).
- **Database sharding**: mỗi shard là một lớp.
- **Type equivalence** trong compiler.

![Định lý: quan hệ tương đương ⇔ phân hoạch](/discrete-mathematics-for-computer-science-iuh/img/course/Set_partitions_4__Hasse__matrices.svg)

<p class="textbook-figure-caption" data-figure="5.17">Mỗi quan hệ tương đương tương ứng duy nhất với một phân hoạch, và ngược lại.</p>
## 8. Ứng dụng trong Khoa học Máy tính

- **Union-Find**: quản lý các lớp tương đương trong bài toán thành phần liên thông.
- **Type checking**: các biểu thức cùng kiểu tạo thành nhóm tương đương theo kiểu.
- **Dependency graph**: thứ tự bộ phận mô hình hóa quan hệ phụ thuộc giữa task.
- **Version control**: lịch sử commit tạo DAG, thường được xem qua quan hệ tổ tiên.

![Đồ thị phụ thuộc — thứ tự bộ phận](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.18">Dependency graph là poset — dùng topological sort để sắp xếp tác vụ theo thứ tự phụ thuộc.</p>
## Tổ chức dữ liệu và AI

Quan hệ tương đương tạo ra **phân hoạch** nên rất hợp với bài toán gom nhóm dữ liệu: hash bucket, data sharding theo khóa, hoặc chia người dùng thành các nhóm có cùng thuộc tính. Trong xử lý dữ liệu lớn, mỗi lớp tương đương có thể được xử lý như một partition độc lập.

Quan hệ thứ tự bộ phận xuất hiện khi không phải mọi đối tượng đều so sánh trực tiếp được. Priority queue và task scheduling dựa trên quan hệ “phải làm trước”, còn dependency graph trong `npm` hay `pip` dùng thứ tự này để giải bài toán cài đặt gói.

Khi mọi phần tử đều so sánh được, chúng ta có **thứ tự toàn phần**. Đây là nền tảng của sorting algorithms, binary search trees và mọi cấu trúc cần sắp xếp tuyến tính.

Trong recommendation systems, quan hệ giữa người dùng và sản phẩm thường được lưu như ma trận user-item. Quan hệ này không phải tương đương hay thứ tự, nhưng ý tưởng tổ chức dữ liệu theo tập cặp vẫn là nền để suy ra người dùng giống nhau, sản phẩm liên quan và điểm gợi ý.

## Bài tập thực hành

### Bài tập 1: Kiểm tra quan hệ tương đương

Xét quan hệ $$R$$ trên $$\Z$$: $$aRb \iff a - b$$ chia hết cho 3. Chứng minh $$R$$ là quan hệ tương đương.

<details>
<summary>Đáp án</summary>

- Phản xạ: $$a-a=0$$ chia hết cho 3.
- Đối xứng: Nếu $$a-b$$ chia hết cho 3 thì $$b-a = -(a-b)$$ cũng chia hết.
- Bắc cầu: Nếu $$a-b$$ và $$b-c$$ chia hết cho 3 thì $$a-c$$ cũng chia hết.

</details>

### Bài tập 2: Phân hoạch

Tìm các lớp tương đương của quan hệ "cùng số dư khi chia 4" trên tập $$\{0,1,2,3,4,5,6,7\}$$.

<details>
<summary>Đáp án</summary>

Lớp: [0,4], [1,5], [2,6], [3,7].

</details>

### Bài tập 3: Thứ tự bộ phận

Vẽ Hasse diagram cho tập $$\{1,2,3,6,12\}$$ với quan hệ chia hết.

<details>
<summary>Đáp án</summary>

1 → 2 → 6 → 12  
1 → 3 → 6 → 12  
1 → 6 → 12 (các cạnh bao hàm rút gọn)

</details>

### Bài tập 4: Min/max và tối tiểu/tối đại

Cho poset $$(\{2,4,5,10,12,20,25\},\mid)$$.

1. Tìm tất cả phần tử tối tiểu và tối đại.
2. Có min và max không?
3. $$4$$ và $$5$$ so sánh được không?

<details>
<summary>Đáp án</summary>

1. Tối tiểu: $$2,5$$. Tối đại: $$12,20,25$$.
2. Không có min (không phần tử nào chia hết mọi phần tử khác theo nghĩa “nhỏ nhất toàn cục”); không có max.
3. Không: $$4\nmid 5$$ và $$5\nmid 4$$.

</details>

### Bài tập 5: Thứ tự tốt và từ điển

(a) $$(\mathbb{N},\le)$$ và $$(\mathbb{Z},\le)$$ — cái nào sắp tốt? Giải thích.  
(b) Trên $$\{0,1\}^2$$, liệt kê thứ tự từ điển và cho hai chuỗi không so sánh được theo product order.

<details>
<summary>Đáp án</summary>

(a) $$(\mathbb{N},\le)$$ sắp tốt; $$(\mathbb{Z},\le)$$ không ($$\mathbb{Z}$$ không có min).  
(b) Từ điển: $$00\prec 01\prec 10\prec 11$$. Product order: $$01$$ và $$10$$ không so sánh được.

</details>

## Xem thêm / Video gợi ý

- [Relations and Functions](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — Trefor Bazett (Equivalence relations)

## Tóm tắt

- **Quan hệ tương đương**: phản xạ + đối xứng + bắc cầu; tạo lớp, tập thương $$A/R$$ và phân hoạch
- **Định lý**: mỗi quan hệ tương đương tương ứng duy nhất với một phân hoạch, và ngược lại
- **Thứ tự bộ phận**: phản xạ + phản đối xứng + bắc cầu; toàn phần khi mọi cặp so sánh được
- **Thứ tự từ điển** trên chuỗi bit là toàn phần; product order thường chỉ bộ phận
- **Hasse**: bỏ vòng và cạnh bắc cầu, chỉ giữ cạnh phủ
- **Min/max** (toàn cục, duy nhất nếu có) ≠ **tối tiểu/tối đại** (cục bộ, có thể nhiều)
- **Thứ tự tốt**: mọi tập con khác rỗng có min — $$(\mathbb{N},\le)$$ có, $$(\mathbb{Z},\le)$$ không
- **Ứng dụng CS**: union-find, type checking, dependency graph, hash bucket, topological sort

Trong bài tiếp theo, chúng ta sẽ học phép toán trên quan hệ và bao đóng.
