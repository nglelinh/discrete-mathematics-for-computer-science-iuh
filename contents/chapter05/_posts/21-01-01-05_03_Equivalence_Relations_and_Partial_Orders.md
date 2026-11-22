---

layout: post
title: "Quan hệ Tương đương và Thứ tự Bộ phận"
categories: chapter05
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Trình bày quan hệ tương đương, lớp tương đương và tập thương; thứ tự bộ phận, thứ tự toàn phần, thứ tự từ điển, biểu đồ Hasse, phần tử nhỏ nhất/lớn nhất, tối tiểu/tối đại và thứ tự tốt."
---

Ở mục trước, chúng ta đã học bốn tính chất cơ bản của quan hệ. Mục này xây dựng hai lớp quan hệ quan trọng từ các tính chất đó: **quan hệ tương đương** và **quan hệ thứ tự bộ phận**.

Một số quan hệ dùng để gom các đối tượng "tương đương nhau" theo một tiêu chí, như phân nhóm sinh viên theo lớp hay quan hệ đồng dư modulo $$n$$. Ngược lại, một số quan hệ khác dùng để sắp xếp đối tượng theo sự phụ thuộc hoặc bao hàm, như cấu trúc thư mục hay quan hệ chia hết. Tuy đều bắt nguồn từ bốn tính chất cơ bản, hai lớp quan hệ này tạo ra hai cấu trúc hoàn toàn khác nhau: lớp tương đương và phân hoạch ở một phía, tập sắp thứ tự bộ phận (poset) và biểu đồ Hasse ở phía kia.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Xây dựng** lớp tương đương, tập thương $$A/R$$ và phân hoạch từ một quan hệ tương đương.
- **Phân biệt** thứ tự toàn phần và thứ tự bộ phận; định nghĩa thứ tự từ điển trên chuỗi bit.
- **Vẽ** biểu đồ Hasse; xác định phần tử nhỏ nhất/lớn nhất và phần tử tối tiểu/tối đại.
- **Nhận biết** thứ tự tốt (well-order) qua các ví dụ như $$(\mathbb{N},\le)$$ và $$(\mathbb{Z},\le)$$.
- **Áp dụng** đồng dư modulo, phân hoạch và quan hệ thứ tự trong thiết kế hệ thống.

**Từ khóa**: lớp tương đương, phân hoạch, tập thương, thứ tự bộ phận, thứ tự toàn phần, thứ tự từ điển, biểu đồ Hasse, min/max, tối tiểu/tối đại, thứ tự tốt.
</div>

### Video ngắn: Quan hệ tương đương và thứ tự bộ phận

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/equivalence-partial-order.mp4"></video>
</div>

Video dài khoảng 2 phút 27 giây, tóm lược ba tính chất của quan hệ tương đương, ví dụ đồng dư modulo 3 trên $$\{0,\dots,11\}$$ chia thành ba lớp tạo phân hoạch, thứ tự bộ phận, từng bước dựng biểu đồ Hasse cho quan hệ chia hết trên các ước của 12 (bỏ khuyên và cạnh bắc cầu), phần tử không so sánh được, phân biệt nhỏ nhất/lớn nhất với tối tiểu/tối đại, và cấu trúc hình lập phương của các ước của 30 tương ứng với $$(\mathcal{P}(\{a,b,c\}), \subseteq)$$.

## Quan hệ tương đương

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Quan hệ $$R$$ trên tập $$A$$ là **quan hệ tương đương** nếu thỏa mãn đồng thời ba tính chất:

1. **Phản xạ**: $$\forall a\in A,\ aRa$$.
2. **Đối xứng**: $$\forall a,b\in A,\ aRb\to bRa$$.
3. **Bắc cầu**: $$\forall a,b,c\in A,\ (aRb\land bRc)\to aRc$$.
</div>

**Ký hiệu**: Khi xét quan hệ tương đương, ta thường viết $$a\sim b$$ thay cho $$(a,b)\in R$$.

<div class="textbook-example" markdown="1">
**Ví dụ**: Quan hệ đồng dư modulo $$n$$ trên $$\mathbb{Z}$$:

<div class="textbook-equation" markdown="1">
$$a\equiv b\pmod n \quad\text{khi và chỉ khi}\quad n\mid(a-b).$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-proof" id="chứng-minh-đồng-dư-modulo-là-quan-hệ-tương-đương" markdown="1">
**Chứng minh đồng dư modulo là quan hệ tương đương**:

- Phản xạ: $$a-a=0$$ chia hết cho $$n$$.
- Đối xứng: nếu $$n\mid(a-b)$$ thì $$n\mid -(a-b)=b-a$$.
- Bắc cầu: nếu $$n\mid(a-b)$$ và $$n\mid(b-c)$$ thì $$n\mid((a-b)+(b-c))=a-c$$.

Vậy đồng dư modulo $$n$$ là một quan hệ tương đương trên $$\mathbb{Z}$$.
</div>

![Quan hệ tương đương và phân hoạch](/discrete-mathematics-for-computer-science-iuh/img/course/Set_partitions_4__Hasse__matrices.svg)

<p class="textbook-figure-caption" data-figure="5.13">Quan hệ tương đương chia tập hợp thành các lớp rời nhau — mỗi ma trận khối tương ứng với một phân hoạch.</p>
## Lớp tương đương và phân hoạch

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Với quan hệ tương đương $$\sim$$ trên $$A$$, **lớp tương đương** của phần tử $$a \in A$$ là tập hợp:

<div class="textbook-equation" markdown="1">
$$[a]=\{x\in A\mid x\sim a\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-theorem" markdown="1">
**Định lý**: Mỗi quan hệ tương đương trên $$A$$ tạo ra một phân hoạch của $$A$$ thành các lớp tương đương đôi một rời nhau; ngược lại, mỗi phân hoạch của $$A$$ xác định duy nhất một quan hệ tương đương.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**: Trên $$\mathbb{Z}$$ theo quan hệ đồng dư modulo 3, có đúng ba lớp tương đương:

- $$[0]=\{\ldots,-6,-3,0,3,6,\ldots\}$$.
- $$[1]=\{\ldots,-5,-2,1,4,7,\ldots\}$$.
- $$[2]=\{\ldots,-4,-1,2,5,8,\ldots\}$$.

![Lưới phân hoạch theo modulo](/discrete-mathematics-for-computer-science-iuh/img/course/Hasse_diagram_of_powerset_of_3.svg)

<p class="textbook-figure-caption" data-figure="5.14">Phân hoạch chia tập nền thành các lớp tương đương rời nhau, gắn chặt với cấu trúc thứ tự của họ các tập con.</p>
</div>

**Tập thương.** Tập hợp tất cả các lớp tương đương được ký hiệu là $$A/R=\{[a]_R\mid a\in A\}$$ và gọi là **tập thương** (quotient set) của $$A$$ theo $$R$$. Mỗi phần tử $$x\in[a]_R$$ là một **đại diện** của lớp $$[a]_R$$.

Với quan hệ đồng dư modulo $$m$$, tập thương $$\mathbb{Z}/R$$ gồm đúng $$m$$ lớp:

$$
\mathbb{Z}_m=\bigl\{[0]_m,[1]_m,\ldots,[m-1]_m\bigr\}.
$$

Đây chính là tập các "số nguyên modulo $$m$$" thường dùng trong số học máy tính và mật mã học.

<div class="textbook-theorem" markdown="1">
**Mệnh đề** (hai lớp tương đương hoặc trùng nhau hoặc rời nhau). Cho quan hệ tương đương $$R$$ trên $$A$$ và hai phần tử $$a,b\in A$$. Ba điều kiện sau tương đương:

1. $$aRb$$;
2. $$[a]_R=[b]_R$$;
3. $$[a]_R\cap[b]_R\neq\emptyset$$.

</div>

Hệ quả trực tiếp là hai lớp tương đương bất kỳ hoặc **trùng nhau**, hoặc **rời nhau**, và hợp của tất cả các lớp bằng $$A$$ — đó chính là định nghĩa của một phân hoạch.

## Quan hệ thứ tự bộ phận

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Quan hệ $$R$$ trên $$A$$ là một **thứ tự bộ phận** (partial order) nếu thỏa mãn:

1. **Phản xạ**: $$\forall a\in A,\ aRa$$.
2. **Phản đối xứng**: nếu $$aRb$$ và $$bRa$$ thì $$a=b$$.
3. **Bắc cầu**: nếu $$aRb$$ và $$bRc$$ thì $$aRc$$.
</div>

Cặp $$(A,R)$$ được gọi là một **tập sắp thứ tự bộ phận** (poset — partially ordered set).

<div class="textbook-example" markdown="1">
**Ví dụ**:

- $$(\mathcal{P}(S),\subseteq)$$ là một poset.
- $$(\mathbb{N},\mid)$$ với quan hệ chia hết là một poset.
- Quan hệ "mô-đun A phải biên dịch trước mô-đun B" (kèm quy ước mỗi mô-đun đứng trước chính nó) tạo thành thứ tự bộ phận khi không có vòng phụ thuộc.
</div>

## Thứ tự toàn phần, thứ tự bộ phận và tính so sánh được

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Trong poset $$(S,\preceq)$$, hai phần tử $$a,b$$ được gọi là **so sánh được** nếu $$a\preceq b$$ hoặc $$b\preceq a$$; ngược lại, chúng **không so sánh được**.

Nếu mọi cặp phần tử của $$S$$ đều so sánh được thì $$(S,\preceq)$$ là **thứ tự toàn phần** (total / linear order). Ngược lại, ta nói $$\preceq$$ chỉ là **thứ tự bộ phận** (bán phần).
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**:

- $$(\mathbb{Z}^+,\le)$$ là thứ tự toàn phần.
- $$(\mathbb{Z}^+,\mid)$$ **không** là thứ tự toàn phần vì $$5$$ và $$7$$ không so sánh được.
- $$(\mathcal{P}(A),\subseteq)$$ không toàn phần khi $$\lvert A\rvert\ge 2$$: chẳng hạn với $$A=\{a,b\}$$, hai tập $$\{a\}$$ và $$\{b\}$$ không so sánh được.

![Thứ tự bộ phận trên tập lũy thừa](/discrete-mathematics-for-computer-science-iuh/img/course/Hasse_diagram_of_powerset_of_3.svg)

<p class="textbook-figure-caption" data-figure="5.15">Poset $$(\mathcal{P}(S), \subseteq)$$ — không phải mọi cặp phần tử đều so sánh được (chẳng hạn {a} và {b}).</p>
</div>

### Thứ tự từ điển trên chuỗi bit

Trong tin học, nhiều thao tác như sắp xếp (`sort`), so sánh khóa hay cây tiền tố (trie) đòi hỏi một thứ tự toàn phần trên chuỗi bit $$\{0,1\}^n$$.

**Thứ tự tọa độ (product order).** Định nghĩa:

$$
a_1a_2\ldots a_n\le b_1b_2\ldots b_n
\quad\text{khi và chỉ khi}\quad
a_i\le b_i\text{ với mọi }i.
$$

Theo cách này, $$0110$$ và $$1000$$ **không so sánh được**, nên đây chỉ là thứ tự bộ phận.

**Thứ tự từ điển (lexicographic order).** So sánh hai chuỗi từ trái sang phải; tại vị trí khác nhau **đầu tiên** $$k$$, chuỗi có bit nhỏ hơn đứng trước. Trên $$\{0,1\}^n$$, thứ tự từ điển là **thứ tự toàn phần** và trùng với thứ tự số nguyên khi đọc chuỗi như số nhị phân. Đây chính là cách hàm `strcmp` hoặc phép sắp xếp chuỗi vận hành.

<div class="textbook-example" markdown="1">
**Ví dụ**: Trên các chuỗi bit độ dài 3, thứ tự từ điển là:

$$000\prec 001\prec 010\prec 011\prec 100\prec 101\prec 110\prec 111.$$

Ngược lại, theo thứ tự tọa độ, $$010$$ và $$100$$ không so sánh được.
</div>

## Biểu đồ Hasse

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Biểu đồ Hasse biểu diễn trực quan một poset hữu hạn bằng ba quy tắc:

- Bỏ tất cả các khuyên phản xạ.
- Bỏ tất cả các cạnh suy ra được từ tính bắc cầu (chỉ giữ lại các **cạnh phủ**: $$a$$ phủ $$b$$ nếu $$b\prec a$$ và không tồn tại $$c$$ thỏa mãn $$b \prec c \prec a$$).
- Vẽ phần tử lớn hơn ở phía trên để không cần ghi mũi tên hướng lên.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**: Xét poset các ước nguyên dương của 12 theo quan hệ chia hết: $$\{1,2,3,4,6,12\}$$. Các cạnh phủ là: $$1-2$$, $$1-3$$, $$2-4$$, $$2-6$$, $$3-6$$, $$4-12$$, $$6-12$$.

![Biểu đồ Hasse đơn giản](/discrete-mathematics-for-computer-science-iuh/img/course/Simple_hasse_diagram.svg)

<p class="textbook-figure-caption" data-figure="5.16">Biểu đồ Hasse loại bỏ khuyên phản xạ và các cạnh bắc cầu, chỉ giữ lại các quan hệ phủ trực tiếp.</p>
</div>

Hai ví dụ biểu đồ Hasse quen thuộc khác là $$(\mathcal{P}(\{a,b,c\}),\subseteq)$$ và tập các chuỗi bit độ dài 3 với thứ tự tọa độ — cả hai đều có dạng hình lập phương 3 chiều.

## Phần tử nhỏ nhất, lớn nhất và thứ tự tốt

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Trong poset $$(S,\preceq)$$:

- $$a$$ là **phần tử nhỏ nhất** (minimum, min) nếu $$a\preceq x$$ với mọi $$x\in S$$;
- $$a$$ là **phần tử lớn nhất** (maximum, max) nếu $$x\preceq a$$ với mọi $$x\in S$$.
</div>

Nếu tồn tại, phần tử nhỏ nhất (và tương tự, phần tử lớn nhất) là **duy nhất**, ký hiệu $$\min(S)$$ và $$\max(S)$$.

<div class="textbook-example" markdown="1">
**Ví dụ**:

- $$S=\{m\in\mathbb{Z}\mid m^2<100\}$$ với $$\le$$: $$\min(S)=-9$$, $$\max(S)=9$$.
- $$A=\{x\in\mathbb{R}\mid x^2<100\}$$ với $$\le$$: không có min và cũng không có max vì khoảng mở $$(-10, 10)$$ không chứa hai đầu mút.
- $$(\mathcal{P}(B),\subseteq)$$: $$\min=\emptyset$$, $$\max=B$$.
</div>

<div class="textbook-definition" markdown="1">
**Định nghĩa** (thứ tự tốt / well-order). Poset $$(S,\preceq)$$ được gọi là **sắp tốt** (well-ordered) nếu **mọi** tập con khác rỗng của $$S$$ đều có phần tử nhỏ nhất.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**:

- $$(\mathbb{N},\le)$$ (và $$(\mathbb{Z}^+,\le)$$) là thứ tự tốt — đây là cơ sở cho quy nạp toán học và cho việc chứng minh vòng lặp có biến đếm giảm nghiêm ngặt trên $$\mathbb{N}$$ luôn dừng.
- $$(\mathbb{Z},\le)$$ **không** là thứ tự tốt vì chính $$\mathbb{Z}$$ (cũng như tập các số nguyên âm) không có phần tử nhỏ nhất.
</div>

**Liên hệ khoa học máy tính.** Khi chứng minh một thuật toán luôn kết thúc bằng cách chỉ ra một đại lượng không âm giảm nghiêm ngặt sau mỗi bước lặp (termination measure trên $$\mathbb{N}$$), ta đang sử dụng tính sắp tốt của tập số tự nhiên.

## Phần tử tối tiểu và tối đại

Khác với min/max là "đáy/đỉnh toàn cục", một poset có thể không có min hay max nhưng vẫn có các phần tử "đáy/đỉnh cục bộ".

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Trong poset $$(S,\preceq)$$:

- $$a$$ là **phần tử tối tiểu** (minimal) nếu không tồn tại $$x\in S$$ ($$x\neq a$$) sao cho $$x\preceq a$$;
- $$a$$ là **phần tử tối đại** (maximal) nếu không tồn tại $$x\in S$$ ($$x\neq a$$) sao cho $$a\preceq x$$.
</div>

**Nhận xét quan trọng:**

1. Phần tử tối tiểu và tối đại **không nhất thiết duy nhất**.
2. Nếu tồn tại phần tử nhỏ nhất thì nó là phần tử tối tiểu **duy nhất**; tương tự, phần tử lớn nhất (nếu có) là phần tử tối đại duy nhất.
3. Trên biểu đồ Hasse: phần tử tối tiểu là đỉnh không có cạnh đi xuống; phần tử tối đại là đỉnh không có cạnh đi lên.

<div class="textbook-example" markdown="1">
**Ví dụ 1.** Xét $$S=\{1,2,3\}$$ với:

$$
R=\{(1,1),(2,2),(3,3),(1,2),(3,2)\}.
$$

Đây là một poset có hai phần tử tối tiểu là $$1$$ và $$3$$, một phần tử tối đại là $$2$$ (đồng thời là $$\max$$). Tập này không có $$\min$$ vì không có phần tử nào nhỏ hơn hoặc bằng cả ba phần tử.

**Ví dụ 2.** Xét poset $$(\{2,4,5,10,12,20,25\},\mid)$$:

- Các phần tử tối tiểu: $$2$$ và $$5$$.
- Các phần tử tối đại: $$12$$, $$20$$ và $$25$$.

Poset này không có phần tử nhỏ nhất và cũng không có phần tử lớn nhất.

**Ví dụ 3.** Tập các chuỗi bit độ dài 3 với thứ tự tọa độ có phần tử tối tiểu duy nhất là $$000$$ và tối đại duy nhất là $$111$$ (chúng đồng thời là $$\min$$ và $$\max$$).
</div>

**Sự tồn tại trên poset hữu hạn.** Trong mọi poset **hữu hạn** khác rỗng, luôn tồn tại ít nhất một phần tử tối tiểu và ít nhất một phần tử tối đại. Thật vậy, xuất phát từ một phần tử $$a_0$$ bất kỳ: nếu $$a_0$$ chưa tối tiểu thì tồn tại $$a_1 \prec a_0$$; quá trình này không thể kéo dài vô hạn trong tập hữu hạn nên phải dừng tại một phần tử tối tiểu. Lập luận tương tự theo chiều tăng cho phần tử tối đại.

## Định lý: Quan hệ tương đương ⇔ Phân hoạch

<div class="textbook-theorem" markdown="1">
**Định lý**: Cho tập hợp $$A$$.  
- Nếu $$R$$ là một quan hệ tương đương trên $$A$$, thì họ các lớp tương đương của $$R$$ tạo thành một **phân hoạch** của $$A$$ (các tập con khác rỗng, đôi một rời nhau và có hợp bằng $$A$$).  
- Ngược lại, nếu $$\{A_i\}$$ là một phân hoạch của $$A$$, thì quan hệ "$$a$$ và $$b$$ cùng thuộc một tập $$A_i$$" là một quan hệ tương đương trên $$A$$.
</div>

<div class="textbook-proof" markdown="1">
**Chứng minh** (ý chính):

1. Nếu $$R$$ là quan hệ tương đương: mỗi $$a \in A$$ thuộc lớp $$[a]$$ nên hợp các lớp bằng $$A$$ và mọi lớp đều khác rỗng. Nếu $$a \in [b] \cap [c]$$ thì $$aRb$$ và $$aRc$$, theo đối xứng và bắc cầu suy ra $$bRc$$, do đó $$[b] = [c]$$; vậy hai lớp khác nhau luôn rời nhau.
2. Ngược lại, nếu $$\{A_i\}$$ là phân hoạch: quan hệ "cùng thuộc một $$A_i$$" rõ ràng có tính phản xạ, đối xứng và bắc cầu.
</div>

**Hệ quả trong khoa học máy tính**:
- **Bảng băm (hash table)**: mỗi ngăn chứa (bucket) ứng với một lớp tương đương các khóa có cùng giá trị băm.
- **Phân mảnh cơ sở dữ liệu (database sharding)**: mỗi shard là một lớp trong phân hoạch tập bản ghi.
- **Tương đương kiểu (type equivalence)** trong trình biên dịch.

![Định lý: quan hệ tương đương ⇔ phân hoạch](/discrete-mathematics-for-computer-science-iuh/img/course/Set_partitions_4__Hasse__matrices.svg)

<p class="textbook-figure-caption" data-figure="5.17">Mỗi quan hệ tương đương tương ứng duy nhất với một phân hoạch của tập nền, và ngược lại.</p>
## Ứng dụng trong Khoa học Máy tính

- **Union-Find (Disjoint Set Union)**: quản lý các lớp tương đương trong bài toán tìm thành phần liên thông.
- **Kiểm tra kiểu (Type checking)**: gom các biểu thức tương đương về kiểu dữ liệu.
- **Đồ thị phụ thuộc (Dependency graph)**: thứ tự bộ phận mô hình hóa quan hệ phụ thuộc giữa các tác vụ.
- **Quản lý phiên bản (Version control)**: lịch sử commit tạo thành đồ thị có hướng không chu trình (DAG), được xét qua quan hệ tổ tiên.

![Đồ thị phụ thuộc — thứ tự bộ phận](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.18">Đồ thị phụ thuộc là một poset — sắp xếp tô-pô (topological sort) mở rộng thứ tự bộ phận đó thành trình tự thực thi hợp lệ.</p>
## Tổ chức dữ liệu và AI

Quan hệ tương đương tạo ra **phân hoạch**, nên rất phù hợp với các bài toán gom nhóm dữ liệu như ngăn băm, phân mảnh dữ liệu theo khóa hay phân nhóm người dùng theo thuộc tính chung. Trong xử lý dữ liệu lớn, mỗi lớp tương đương có thể được xử lý độc lập như một phân vùng (partition).

Quan hệ thứ tự bộ phận xuất hiện khi không phải mọi cặp đối tượng đều so sánh được với nhau. Hàng đợi ưu tiên, lập lịch tác vụ theo điều kiện "phải hoàn thành trước" và đồ thị phụ thuộc gói trong `npm` hay `pip` đều dựa trên thứ tự bộ phận. Khi mọi phần tử đều so sánh được, ta có **thứ tự toàn phần** — cơ sở của thuật toán sắp xếp và cây tìm kiếm nhị phân.

Trong hệ thống gợi ý, tương tác giữa người dùng và sản phẩm thường được lưu dưới dạng ma trận user–item. Dù quan hệ này không phải quan hệ tương đương hay thứ tự, việc biểu diễn dữ liệu theo tập các cặp vẫn là nền tảng để tìm người dùng tương đồng và tính điểm gợi ý.


## Công cụ tương tác

Vẽ biểu đồ Hasse cho một thứ tự bộ phận nhỏ: chỉ giữ các cạnh phủ và ẩn các cạnh suy ra từ tính bắc cầu.
<div class="interactive-demo" markdown="1">
<div data-demo="hasse-diagram"></div>
</div>
<script src="{{ '/public/js/hasse-diagram.js' | relative_url }}"></script>

### Minh họa tương tác

Quan sát các lớp tương đương của quan hệ đồng dư và biểu đồ Hasse của thứ tự bộ phận (chẳng hạn quan hệ chia hết).

<div class="interactive-demo" markdown="1">
<div data-demo="relation-explainer" data-preset="div" data-focus="hasse"></div>
</div>
<script src="{{ '/public/js/explainers/relation-explainer.js' | relative_url }}"></script>

## Bài tập thực hành

### Bài tập 1: Kiểm tra quan hệ tương đương

Xét quan hệ $$R$$ trên $$\mathbb{Z}$$ định nghĩa bởi $$aRb \iff a - b$$ chia hết cho 3. Chứng minh $$R$$ là một quan hệ tương đương.

<details>
<summary>Đáp án</summary>

- Phản xạ: $$a-a=0$$ chia hết cho 3 với mọi $$a \in \mathbb{Z}$$.
- Đối xứng: nếu $$a-b$$ chia hết cho 3 thì $$b-a = -(a-b)$$ cũng chia hết cho 3.
- Bắc cầu: nếu $$a-b$$ và $$b-c$$ cùng chia hết cho 3 thì $$a-c = (a-b)+(b-c)$$ cũng chia hết cho 3.

</details>

### Bài tập 2: Phân hoạch

Tìm các lớp tương đương của quan hệ "có cùng số dư khi chia cho 4" trên tập $$\{0,1,2,3,4,5,6,7\}$$.

<details>
<summary>Đáp án</summary>

Bốn lớp tương đương là: $$\{0,4\}$$, $$\{1,5\}$$, $$\{2,6\}$$ và $$\{3,7\}$$.

</details>

### Bài tập 3: Biểu đồ Hasse

Vẽ biểu đồ Hasse cho tập $$\{1,2,3,6,12\}$$ với quan hệ chia hết.

<details>
<summary>Đáp án</summary>

Các cạnh phủ (từ dưới lên trên) là: $$(1, 2)$$, $$(1, 3)$$, $$(2, 6)$$, $$(3, 6)$$ và $$(6, 12)$$, tạo thành hai nhánh nối chung tại $$1$$ và $$6$$:

- $$1 \to 2 \to 6 \to 12$$
- $$1 \to 3 \to 6 \to 12$$

*(Lưu ý: không vẽ cạnh trực tiếp $$1 \to 6$$, $$1 \to 12$$, $$2 \to 12$$ hay $$3 \to 12$$ vì chúng suy ra được từ tính bắc cầu.)*

</details>

### Bài tập 4: Min/max và tối tiểu/tối đại

Cho poset $$(\{2,4,5,10,12,20,25\},\mid)$$.

1. Tìm tất cả các phần tử tối tiểu và tối đại.
2. Poset này có phần tử nhỏ nhất (min) và lớn nhất (max) không?
3. Hai phần tử $$4$$ và $$5$$ có so sánh được không?

<details>
<summary>Đáp án</summary>

1. Tối tiểu: $$2, 5$$. Tối đại: $$12, 20, 25$$.
2. Không có min (không có phần tử nào là ước của mọi phần tử còn lại) và không có max (không có phần tử nào là bội của mọi phần tử còn lại).
3. Không, vì $$4\nmid 5$$ và $$5\nmid 4$$.

</details>

### Bài tập 5: Thứ tự tốt và thứ tự từ điển

(a) Trong hai poset $$(\mathbb{N},\le)$$ và $$(\mathbb{Z},\le)$$, poset nào có thứ tự tốt? Giải thích.  
(b) Trên $$\{0,1\}^2$$, liệt kê các chuỗi theo thứ tự từ điển và chỉ ra hai chuỗi không so sánh được theo thứ tự tọa độ (product order).

<details>
<summary>Đáp án</summary>

(a) $$(\mathbb{N},\le)$$ là thứ tự tốt; $$(\mathbb{Z},\le)$$ không phải vì tập $$\mathbb{Z}$$ không có phần tử nhỏ nhất.  
(b) Thứ tự từ điển: $$00\prec 01\prec 10\prec 11$$. Theo thứ tự tọa độ, $$01$$ và $$10$$ không so sánh được.

</details>

## Xem thêm / Video gợi ý

- [Relations and Functions](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — Trefor Bazett (Equivalence relations)

## Tóm tắt

- **Quan hệ tương đương** (phản xạ + đối xứng + bắc cầu) tạo ra các lớp tương đương, tập thương $$A/R$$ và một phân hoạch của $$A$$.
- **Thứ tự bộ phận** (phản xạ + phản đối xứng + bắc cầu) trở thành **thứ tự toàn phần** khi mọi cặp phần tử đều so sánh được.
- **Thứ tự từ điển** trên chuỗi bit là thứ tự toàn phần, còn thứ tự tọa độ nói chung chỉ là thứ tự bộ phận.
- **Biểu đồ Hasse** loại bỏ khuyên phản xạ và các cạnh bắc cầu, chỉ giữ lại các cạnh phủ.
- **Min/max** (toàn cục, duy nhất nếu tồn tại) khác với **tối tiểu/tối đại** (cục bộ, có thể có nhiều phần tử).
- **Thứ tự tốt**: mọi tập con khác rỗng đều có phần tử nhỏ nhất — đúng với $$(\mathbb{N},\le)$$, sai với $$(\mathbb{Z},\le)$$.
- Ứng dụng khoa học máy tính: Union-Find, kiểm tra kiểu, đồ thị phụ thuộc, bảng băm và sắp xếp tô-pô.

Trong bài tiếp theo, chúng ta sẽ học các phép toán trên quan hệ và khái niệm bao đóng.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=T6RUxvJR8i4">Equivalence Relations  - Reflexive, Symmetric, and Transitive</a> — Dr. Trefor Bazett, tiếng Anh. Giới thiệu quan hệ tương đương qua ba tính chất phản xạ, đối xứng và bắc cầu.
- <a href="https://www.youtube.com/watch?v=R36F8CWAi2k">PARTIAL ORDERS - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Trình bày thứ tự bộ phận và cách đọc các quan hệ thứ tự.
- <a href="https://www.youtube.com/watch?v=q0xN_N7l_Kw">Reflexive, Symmetric, and Transitive Relations on a Set</a> — Dr. Trefor Bazett, tiếng Anh. Ôn lại ba tính chất cần kiểm tra trước khi kết luận quan hệ tương đương.
