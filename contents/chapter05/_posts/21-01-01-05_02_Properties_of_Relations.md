---

layout: post
title: "Tính chất của Quan hệ"
categories: chapter05
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Phân tích bốn tính chất cơ bản của quan hệ trên một tập hợp: phản xạ, đối xứng, phản đối xứng và bắc cầu, cùng cách kiểm tra trên ma trận 0-1 và đồ thị có hướng."
---


Trên Facebook, nếu An là bạn của Bình thì Bình chắc chắn là bạn của An; nhưng trên Instagram, An theo dõi Bình không hề bắt buộc Bình phải theo dõi lại; còn trong bảng môn tiên quyết ở đại học, nếu Môn A mở khóa Môn B thì Môn B không thể nào lại mở khóa ngược Môn A. Bốn tính chất **phản xạ, đối xứng, phản đối xứng và bắc cầu** chính là "bộ kính hiển vi" giúp toán học và kỹ sư phần mềm phân loại rạch ròi mọi mạng lưới quan hệ như thế.

Ở mục trước, chúng ta đã định nghĩa quan hệ, các cách biểu diễn và những ứng dụng cơ bản trong cơ sở dữ liệu và đồ thị. Mục này trình bày bốn tính chất cơ bản — **phản xạ**, **đối xứng**, **phản đối xứng** và **bắc cầu** — dùng để phân loại và phân tích cấu trúc của một quan hệ trên tập hợp.

Không phải mọi liên kết giữa các đối tượng đều có cùng bản chất: quan hệ "bằng nhau" khác quan hệ "nhỏ hơn hoặc bằng", và cả hai đều khác quan hệ "theo dõi" trên mạng xã hội. Bốn tính chất này quyết định liệu ta có thể phân nhóm phần tử thành các lớp tương đương, sắp xếp chúng theo thứ tự hay suy diễn thêm các liên kết gián tiếp hay không. Trong thiết kế dữ liệu và thuật toán, nhận diện sai tính chất của quan hệ có thể dẫn đến mô hình hóa sai ngay từ đầu.

## Bản đồ kiến thức nền: Bốn tính chất phân loại mọi Quan hệ trên tập $A$

1. **Phản xạ (Reflexive) — Mọi phần tử đều nối với chính nó**:
   $\forall a \in A,\; (a, a) \in R$. Trên ma trận $M_R$, toàn bộ **đường chéo chính phải bằng `1`**; chỉ cần thiếu một khuyên duy nhất là mất tính phản xạ.

2. **Đối xứng (Symmetric) — Mũi tên luôn đi thành cặp hai chiều**:
   $\forall a, b \in A,\; (a, b) \in R \to (b, a) \in R$. Trên ma trận, $M_R = M_R^T$ (đối xứng qua đường chéo chính).

3. **Phản đối xứng (Antisymmetric) — Cấm mũi tên hai chiều giữa hai đỉnh khác nhau**:
   $\forall a, b \in A,\; [(a, b) \in R \land (b, a) \in R] \to a = b$. Cạm bẫy kinh điển: **Phản đối xứng KHÔNG phải là phủ định của Đối xứng**! Một quan hệ có thể vừa đối xứng vừa phản đối xứng (ví dụ quan hệ bằng nhau `=`), hoặc không thỏa cả hai.

4. **Bắc cầu (Transitive) — Có đường đi 2 bước thì phải có lối tắt trực tiếp**:
   $\forall a, b, c \in A,\; [(a, b) \in R \land (b, c) \in R] \to (a, c) \in R$. Nếu không tồn tại cặp nối đuôi $(a,b)$ và $(b,c)$ nào thì tính bắc cầu tự động **đúng rỗng** (*vacuously true*).

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Kiểm tra** tính phản xạ, đối xứng, phản đối xứng và bắc cầu của một quan hệ qua tập cặp, ma trận 0-1 và đồ thị có hướng.
- **Phân biệt** đối xứng và phản đối xứng, cũng như nền tảng phân biệt quan hệ tương đương với thứ tự bộ phận.
- **Nhận diện** vai trò của các tính chất quan hệ trong lược đồ cơ sở dữ liệu và đồ thị.

**Từ khóa**: phản xạ, đối xứng, phản đối xứng, bắc cầu, quan hệ tương đương, thứ tự bộ phận.
</div>

## Các tính chất cơ bản

Xét quan hệ $$R$$ trên tập hợp $$A$$ ($$R \subseteq A \times A$$):

### Tính phản xạ (Reflexive)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$R$$ có tính **phản xạ** nếu $$\forall a \in A: (a, a) \in R$$.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**:
- ✅ Quan hệ "`=`" trên $$\mathbb{R}$$: mọi số đều bằng chính nó.
- ✅ Quan hệ "`≤`" trên $$\mathbb{R}$$: mọi số đều nhỏ hơn hoặc bằng chính nó.
- ❌ Quan hệ "`<`" trên $$\mathbb{R}$$: không có số nào nhỏ hơn chính nó.

**Trên ma trận quan hệ**: Toàn bộ đường chéo chính bằng 1:
```
[1 ? ?]
[? 1 ?]
[? ? 1]
```

**Trên đồ thị có hướng**: Mọi đỉnh đều có khuyên (loop) quay về chính nó.

![Đồ thị có hướng — tính phản xạ](/discrete-mathematics-for-computer-science-iuh/img/course/Example_of_simple_directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.7">Trong đồ thị có hướng, tính phản xạ tương ứng với việc mỗi đỉnh đều có khuyên (loop) quay về chính nó.</p>
</div>

#### Minh họa trực quan: Phân biệt Phản xạ và Phản đối xứng

| Tính chất | Ý nghĩa | Điều kiện |
|:---|:---|:---|
| **Phản xạ** | Mọi phần tử đều liên hệ với chính nó | $$aRa$$ luôn đúng với mọi $$a \in A$$ |
| **Phản đối xứng** | Nếu liên hệ hai chiều thì hai phần tử phải bằng nhau | $$aRb \land bRa \Rightarrow a = b$$ |

### Tính đối xứng (Symmetric)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$R$$ có tính **đối xứng** nếu $$\forall a, b \in A: (a, b) \in R \implies (b, a) \in R$$.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**:
- ✅ Quan hệ "`=`" trên $$\mathbb{R}$$: nếu $$a = b$$ thì $$b = a$$.
- ✅ Quan hệ "`≠`" trên $$\mathbb{R}$$: nếu $$a \neq b$$ thì $$b \neq a$$.
- ❌ Quan hệ "`<`" trên $$\mathbb{R}$$: nếu $$a < b$$ thì không thể có $$b < a$$.

**Trên ma trận quan hệ**: Ma trận đối xứng qua đường chéo chính ($$m_{ij} = m_{ji}$$):
```
[? a b]
[a ? c]
[b c ?]
```

![Đồ thị vô hướng — tính đối xứng](/discrete-mathematics-for-computer-science-iuh/img/course/Undirected_graph.svg)

<p class="textbook-figure-caption" data-figure="5.8">Quan hệ đối xứng thường được biểu diễn bằng đồ thị vô hướng — mỗi cạnh thể hiện liên kết hai chiều.</p>
</div>

<div class="content-box insight-box textbook-block" markdown="1">
**Trong khoa học máy tính**: Quan hệ "hai máy tính có kết nối mạng trực tiếp" là đối xứng. Ngược lại, quan hệ "thư mục cha chứa thư mục con" không đối xứng (nếu thư mục A chứa B thì B không thể chứa A).
</div>

### Tính phản đối xứng (Antisymmetric)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$R$$ có tính **phản đối xứng** nếu $$\forall a, b \in A: (a, b) \in R \land (b, a) \in R \implies a = b$$.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**:
- ✅ Quan hệ "`≤`" trên $$\mathbb{R}$$: nếu $$a \le b$$ và $$b \le a$$ thì $$a = b$$.
- ✅ Quan hệ "`⊆`" trên họ các tập hợp: nếu $$A \subseteq B$$ và $$B \subseteq A$$ thì $$A = B$$.
- ❌ Quan hệ "`≠`" trên $$\mathbb{R}$$: với $$1 \neq 2$$ ta có cả $$(1,2)$$ và $$(2,1)$$ nhưng $$1 \neq 2$$.
</div>

<div class="content-box warning-box textbook-block" markdown="1">
![Đồ thị có hướng — tính phản đối xứng](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.9">Tính phản đối xứng không cho phép hai phần tử phân biệt liên hệ hai chiều với nhau.</p>
**Lưu ý quan trọng**: Đối xứng và phản đối xứng **không phải** là hai khái niệm phủ định của nhau. Một quan hệ có thể vừa đối xứng vừa phản đối xứng (ví dụ quan hệ "`=`"), và cũng có thể không đối xứng lẫn không phản đối xứng (ví dụ $$R = \{(1,2), (2,1), (1,3)\}$$ có cả $$(1,2)$$ và $$(2,1)$$ nên không phản đối xứng, nhưng có $$(1,3)$$ mà thiếu $$(3,1)$$ nên không đối xứng).
</div>

### Tính bắc cầu (Transitive)

<div class="textbook-definition" markdown="1">
**Định nghĩa**: $$R$$ có tính **bắc cầu** nếu $$\forall a, b, c \in A: (a, b) \in R \land (b, c) \in R \implies (a, c) \in R$$.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**:
- ✅ Quan hệ "`<`" trên $$\mathbb{R}$$: nếu $$a < b$$ và $$b < c$$ thì $$a < c$$.
- ✅ Quan hệ "`⊆`" trên họ các tập hợp: nếu $$A \subseteq B$$ và $$B \subseteq C$$ thì $$A \subseteq C$$.
- ❌ Quan hệ "là cha của": nếu A là cha của B và B là cha của C thì A là ông chứ không phải cha của C.
</div>

<div class="content-box insight-box textbook-block" markdown="1">
**Tính bắc cầu trong khoa học máy tính**: Quan hệ "phụ thuộc" giữa các gói phần mềm đòi hỏi suy diễn bắc cầu khi xây dựng cây phụ thuộc: nếu gói A phụ thuộc B và B phụ thuộc C thì trình quản lý gói phải cài đặt cả C.
</div>

![Đường đi gián tiếp — tính bắc cầu](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.10">Tính bắc cầu bảo đảm mọi đường đi độ dài 2 dạng a → b → c đều có cung trực tiếp (a, c).</p>
### Bảng tổng kết nhanh

| Tính chất | Điều kiện | Ma trận | Đồ thị |
|-----------|-----------|---------|--------|
| Phản xạ | $$(a,a) \in R$$ với mọi $$a$$ | Đường chéo chính toàn 1 | Mọi đỉnh đều có khuyên |
| Đối xứng | $$(a,b) \in R \implies (b,a) \in R$$ | Đối xứng qua đường chéo | Mọi cung giữa hai đỉnh đều có chiều ngược |
| Phản đối xứng | $$(a,b), (b,a) \in R \implies a=b$$ | Không có cặp 1 đối xứng ngoài đường chéo | Không có cặp cung ngược chiều giữa hai đỉnh khác nhau |
| Bắc cầu | $$(a,b), (b,c) \in R \implies (a,c) \in R$$ | Kiểm tra bằng tích Boolean / Warshall | Có đường đi $$a \to b \to c$$ thì có cung $$(a,c)$$ |

![Ma trận quan hệ và ma trận kề](/discrete-mathematics-for-computer-science-iuh/img/course/Set_partitions_4__Hasse__matrices.svg)

<p class="textbook-figure-caption" data-figure="5.11">Ma trận 0-1 mã hóa quan hệ: phần tử ở hàng i, cột j bằng 1 khi và chỉ khi (aᵢ, aⱼ) thuộc quan hệ.</p>

## Kiểm tra tính chất trên ma trận quan hệ

Khi $$R$$ là quan hệ trên $$A=\{a_1,\ldots,a_n\}$$ với ma trận $$M_R=[m_{ij}]$$ ($$m_{ij}=1 \iff (a_i,a_j)\in R$$), ta có thể kiểm tra trực tiếp các tính chất từ $$M_R$$:

<div class="textbook-definition" markdown="1">

**Tiêu chí trên ma trận:**

1. **Phản xạ**: $$m_{ii}=1$$ với mọi $$i$$ (đường chéo chính toàn số 1).
2. **Đối xứng**: $$m_{ij}=m_{ji}$$ với mọi $$i,j$$ ($$M_R$$ là ma trận đối xứng).
3. **Phản đối xứng**: với mọi $$i\neq j$$, ta có $$m_{ij}=0$$ hoặc $$m_{ji}=0$$ (tức $$m_{ij}m_{ji}=0$$).
4. **Bắc cầu**: nếu $$m_{ik}=1$$ và $$m_{kj}=1$$ thì phải có $$m_{ij}=1$$. Với $$n$$ lớn, việc kiểm tra thường thực hiện bằng tích ma trận Boolean hoặc thuật toán Warshall (mục 5.4).

</div>

<div class="textbook-example" markdown="1">

**Ví dụ.** Xét quan hệ trên $$A=\{1,2,3\}$$ có ma trận:

$$
M_R=\begin{pmatrix}1&1&0\\0&1&1\\0&0&1\end{pmatrix}.
$$

- Đường chéo chính toàn số 1 ⇒ **phản xạ**.
- $$m_{12}=1$$ nhưng $$m_{21}=0$$ ⇒ **không đối xứng**; đồng thời không có cặp $$1$$–$$1$$ đối xứng nào ngoài đường chéo ⇒ **phản đối xứng**.
- Có $$(1,2)$$ và $$(2,3)$$ nhưng $$m_{13}=0$$ ⇒ **không bắc cầu**.

</div>

**Lưu ý thực hành.** Tính phản xạ, đối xứng và phản đối xứng có thể kiểm tra trực tiếp trên ma trận rất nhanh. Ngược lại, tính bắc cầu dễ bỏ sót khi kiểm tra thủ công với $$n$$ lớn — đó là lý do thuật toán Warshall được giới thiệu ở mục 5.4.

### Khung giải thích (nên đọc chậm): Chẩn đoán tay 4 tính chất trên 3 quan hệ $3 \times 3$ dễ bẫy nhất

Xét tập $A = \{1, 2, 3\}$ với ba quan hệ sau:
- $R_1 = \{(1,1), (2,2), (3,3), (1,2)\}$
- $R_2 = \{(1,1), (2,2), (3,3)\}$ (quan hệ đồng nhất)
- $R_3 = \{(1,2), (2,3)\}$

Ta kiểm tra chậm từng tiêu chí (dùng phản ví dụ cụ thể mỗi khi kết luận **Sai**):

| Quan hệ | Phản xạ? | Đối xứng? | Phản đối xứng? | Bắc cầu? |
| :--- | :---: | :---: | :---: | :---: |
| **$R_1$** | **Đúng** (đủ $(1,1),(2,2),(3,3)$) | **Sai** (có $(1,2)$ nhưng thiếu $(2,1)$) | **Đúng** (không có cặp $a \neq b$ nào đi 2 chiều) | **Đúng** (mọi cặp nối đuôi như $(1,1)\&(1,2)$ đều cho $(1,2)\in R_1$) |
| **$R_2$** | **Đúng** | **Đúng** ($M_{R_2} = I = I^T$) | **Đúng** (không có cặp $a \neq b$ nào để vi phạm!) | **Đúng** |
| **$R_3$** | **Sai** (thiếu $(1,1)$) | **Sai** (có $(1,2)$, thiếu $(2,1)$) | **Đúng** (không có cặp 2 chiều nào) | **Sai** (có $(1,2)$ và $(2,3)$ nhưng thiếu $(1,3)$!) |

**Điểm sáng cần nhớ**: Nhìn dòng $R_2$, bạn thấy ngay bằng chứng sống động rằng một quan hệ có thể **vừa đối xứng, vừa phản đối xứng** cùng lúc—bởi vì các phần tử trên đường chéo chính $(a, a)$ không bao giờ vi phạm tính phản đối xứng!

## Ứng dụng kỹ thuật: Khóa chính và phép chiếu

Trong cơ sở dữ liệu, các tính chất của quan hệ giúp bảo đảm tính nhất quán của dữ liệu. Một **khóa chính** (primary key) phải xác định duy nhất mỗi bản ghi, tức không có hai hàng khác nhau nào mang cùng giá trị khóa. Nếu không gian giá trị khóa nhỏ hơn số bản ghi cần lưu, nguyên lý chuồng bồ câu cho thấy xung đột khóa là tất yếu; vì vậy khóa chính cần có miền giá trị đủ lớn và ổn định.

**Phép chiếu** (projection, ký hiệu $$\pi$$) trong đại số quan hệ chọn ra một số thuộc tính từ mỗi bộ của quan hệ:

```sql
SELECT DISTINCT student_id
FROM Enrollments;
```

Câu lệnh này thực hiện phép chiếu $$\pi_{\text{student\_id}}(\text{Enrollments})$$, trong đó `DISTINCT` loại bỏ các giá trị trùng lặp sau khi bỏ bớt các cột khác.

![Phép chiếu trong cơ sở dữ liệu](/discrete-mathematics-for-computer-science-iuh/img/course/Database.svg)

<p class="textbook-figure-caption" data-figure="5.12">Khóa chính xác định duy nhất mỗi bản ghi; phép chiếu trích xuất một tập con các thuộc tính từ mỗi bộ.</p>
```python
enrollments = {("S01", "CS101"), ("S01", "MATH101"), ("S02", "CS101")}
projection = {student_id for (student_id, _) in enrollments}
```

Trong đoạn mã trên, `projection` là kết quả chiếu quan hệ hai ngôi `enrollments` xuống thành phần thứ nhất.


## Công cụ tương tác

Nhập các cặp của một quan hệ để kiểm tra tính phản xạ, đối xứng, phản đối xứng và bắc cầu.
<div class="interactive-demo" markdown="1">
<div data-demo="relation-classifier"></div>
</div>
<script src="{{ '/public/js/relation-properties-checker.js' | relative_url }}"></script>

### Minh họa tương tác

Quan sát từng tính chất (phản xạ, đối xứng, phản đối xứng, bắc cầu) kèm chứng cứ hoặc phản ví dụ cụ thể trên quan hệ minh họa.

<div class="interactive-demo" markdown="1">
<div data-demo="relation-explainer" data-preset="sym" data-focus="props"></div>
</div>
<script src="{{ '/public/js/explainers/relation-explainer.js' | relative_url }}"></script>

## Bài tập thực hành

### Bài tập 1: Nhận diện tính chất

Xác định các tính chất của quan hệ $$R = \{(1,1), (1,2), (2,2), (2,3), (3,3)\}$$ trên $$A = \{1, 2, 3\}$$.

<details>
<summary>Đáp án</summary>

- Phản xạ: ✅ (có đủ $$(1,1), (2,2), (3,3)$$ cho mọi phần tử của $$A$$).
- Đối xứng: ❌ (có $$(1,2)$$ nhưng không có $$(2,1)$$).
- Phản đối xứng: ✅ (không có cặp đối xứng nào giữa hai phần tử khác nhau).
- Bắc cầu: ❌ (có $$(1,2)$$ và $$(2,3)$$ nhưng không có $$(1,3)$$).

Kết luận: $$R$$ có tính phản xạ và phản đối xứng, nhưng không đối xứng và không bắc cầu.
</details>

### Bài tập 2: So sánh hai quan hệ

So sánh bốn tính chất của quan hệ "`≤`" và "`<`" trên $$\mathbb{R}$$.

<details>
<summary>Đáp án</summary>

| Tính chất | ≤ | < |
|-----------|---|---|
| Phản xạ | ✅ ($$a \le a$$) | ❌ ($$a \not< a$$) |
| Đối xứng | ❌ ($$1 \le 2$$ nhưng $$2 \not\le 1$$) | ❌ ($$1 < 2$$ nhưng $$2 \not< 1$$) |
| Phản đối xứng | ✅ ($$a \le b \land b \le a \Rightarrow a = b$$) | ✅ ($$a < b \land b < a$$ không bao giờ xảy ra, nên đúng một cách rỗng) |
| Bắc cầu | ✅ ($$a \le b \land b \le c \Rightarrow a \le c$$) | ✅ ($$a < b \land b < c \Rightarrow a < c$$) |
</details>

### Bài tập 3: Đọc tính chất từ ma trận

Cho quan hệ trên $$A=\{a,b,c\}$$ với ma trận:

$$
M_R=\begin{pmatrix}1&1&1\\1&1&0\\0&0&1\end{pmatrix}.
$$

Xác định tính phản xạ, đối xứng, phản đối xứng và bắc cầu. Nếu không bắc cầu, hãy chỉ ra một bộ ba làm phản ví dụ.

<details>
<summary>Đáp án</summary>

- Phản xạ: ✅ (đường chéo chính toàn số 1).
- Đối xứng: ❌ ($$m_{13}=1$$ nhưng $$m_{31}=0$$).
- Phản đối xứng: ❌ (có $$m_{12}=m_{21}=1$$ với $$a \neq b$$).
- Bắc cầu: ❌ — xét bộ ba $$(b, a, c)$$: ta có $$(b,a) \in R$$ ($$m_{21}=1$$) và $$(a,c) \in R$$ ($$m_{13}=1$$), nhưng $$(b,c) \notin R$$ ($$m_{23}=0$$).

</details>

## Xem thêm / Video gợi ý

- [Relations and Functions](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — Trefor Bazett (Equivalence relations)

## Tóm tắt

- **Phản xạ**: mọi phần tử đều liên hệ với chính nó (đường chéo chính ma trận toàn 1).
- **Đối xứng**: $$aRb \implies bRa$$ (ma trận đối xứng qua đường chéo chính).
- **Phản đối xứng**: không có hai phần tử khác nhau liên hệ hai chiều ($$m_{ij}m_{ji}=0$$ với mọi $$i\neq j$$).
- **Bắc cầu**: $$aRb \land bRc \implies aRc$$ (kiểm tra bằng đường đi độ dài 2 hoặc thuật toán Warshall).
- Bốn tính chất này là cơ sở xây dựng **quan hệ tương đương** (phản xạ + đối xứng + bắc cầu) và **quan hệ thứ tự bộ phận** (phản xạ + phản đối xứng + bắc cầu).

Trong bài tiếp theo, chúng ta sẽ tìm hiểu chi tiết hai lớp quan hệ đặc biệt này cùng ứng dụng của chúng.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=q0xN_N7l_Kw">Reflexive, Symmetric, and Transitive Relations on a Set</a> — Dr. Trefor Bazett, tiếng Anh. Giới thiệu ba tính chất phản xạ, đối xứng và bắc cầu trên một tập hợp.
- <a href="https://www.youtube.com/watch?v=TctNssYMXJE">You need to check EVERY spot for reflexivity, symmetry, and transitivity</a> — Dr. Trefor Bazett, tiếng Anh. Nhấn mạnh yêu cầu kiểm tra đầy đủ mọi cặp phần tử khi xét tính chất quan hệ.
- <a href="https://www.youtube.com/watch?v=qujnPIPjKrA">[Discrete Mathematics] Relations Examples</a> — TrevTutor, tiếng Anh. Các ví dụ nhận diện tính chất trên những quan hệ cụ thể.
