---

layout: post
title: "Phép toán Quan hệ và Bao đóng"
categories: chapter05
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Ở mục trước chúng ta đã xem quan hệ tương đương và thứ tự bộ phận. Mục này mở rộng sang các phép toán trên quan hệ và khái niệm bao đóng — công cụ chuyển từ…"
---

Ở mục trước chúng ta đã xem quan hệ tương đương và thứ tự bộ phận. Mục này mở rộng sang các **phép toán trên quan hệ** và khái niệm **bao đóng** — công cụ chuyển từ mô tả tĩnh sang thao tác chủ động trên cấu trúc liên hệ.

Trong hệ thống thực, chúng ta thường phải đảo chiều liên kết, ghép hai quan hệ thành một đường suy diễn mới, hoặc thêm các cặp còn thiếu để quan hệ đạt tính chất mong muốn. Ví dụ, từ quan hệ phụ thuộc trực tiếp giữa các module, chúng ta muốn suy ra phụ thuộc gián tiếp; từ quan hệ kết nối trong mạng, chúng ta muốn biết cặp node nào cuối cùng vẫn liên thông. Những câu hỏi đó dẫn thẳng đến bao đóng bắc cầu và thuật toán Warshall.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Thực hiện** hợp, giao, tổ hợp và nghịch đảo quan hệ.
- **Tính** bao đóng phản xạ, đối xứng, bắc cầu.
- **Giải thích** vai trò bao đóng trong suy luận và đồ thị.

**Từ khóa**: tổ hợp quan hệ, bao đóng (closure), transitive closure, Warshall.
</div>

## 1. Quan hệ ngược

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Với quan hệ $$R\subseteq A\times B$$, quan hệ ngược của $$R$$ là:
</div>

<div class="textbook-equation" markdown="1">
$$R^{-1}=\{(b,a)\in B\times A\mid (a,b)\in R\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-example" markdown="1">
**Ví dụ**: Nếu $$R=\{(An,Toan),(Binh,Ly),(Chi,Toan)\}$$ biểu diễn "sinh viên học môn", thì $$R^{-1}$$ biểu diễn "môn có sinh viên":

<div class="textbook-equation" markdown="1">
$$R^{-1}=\{(Toan,An),(Ly,Binh),(Toan,Chi)\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

**Tính chất**:

<div class="textbook-equation" markdown="1">
$$(R^{-1})^{-1}=R.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Nếu $$R$$ đối xứng thì $$R^{-1}=R$$.

![Quan hệ ngược — đảo chiều cung](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.19">Quan hệ ngược $$R^{-1}$$ đảo hướng mọi cung — từ (a, b) ∈ R suy ra (b, a) ∈ R⁻¹.</p>
## 2. Hợp thành quan hệ

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Cho $$R\subseteq A\times B$$ và $$S\subseteq B\times C$$. Hợp thành $$S\circ R$$ là quan hệ từ $$A$$ đến $$C$$:
</div>

<div class="textbook-equation" markdown="1">
$$S\circ R=\{(a,c)\mid \exists b\in B,\ (a,b)\in R\land (b,c)\in S\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
**Ký hiệu**: $$S\circ R$$ đọc là "$$S$$ sau $$R$$"; thực hiện $$R$$ trước rồi $$S$$.

<div class="textbook-example" markdown="1">
**Ví dụ**: $$R=\{(1,2),(2,3)\}$$, $$S=\{(2,1),(3,3)\}$$. Khi đó:

- $$(1,2)\in R$$ và $$(2,1)\in S$$ nên $$(1,1)\in S\circ R$$.
- $$(2,3)\in R$$ và $$(3,3)\in S$$ nên $$(2,3)\in S\circ R$$.

Vậy $$S\circ R=\{(1,1),(2,3)\}$$.

![Hợp thành quan hệ — ghép hai bước](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.20">Hợp thành $$S \circ R$$ ghép hai quan hệ: (a, c) ∈ S∘R khi tồn tại b sao cho (a, b) ∈ R và (b, c) ∈ S.</p>
</div>

## 3. Ma trận quan hệ và tích Boolean

Nếu $$R$$ và $$S$$ được biểu diễn bằng ma trận 0-1, thì ma trận của $$S\circ R$$ được tính bằng tích Boolean:

<div class="textbook-equation" markdown="1">
$$M_{S\circ R}[i,j]=\bigvee_k(M_R[i,k]\land M_S[k,j]).$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Ở đây phép nhân thường được thay bằng AND, phép cộng thường được thay bằng OR.

![Ma trận quan hệ và tích Boolean](/discrete-mathematics-for-computer-science-iuh/img/course/Set_partitions_4__Hasse__matrices.svg)

<p class="textbook-figure-caption" data-figure="5.21">Tích Boolean của hai ma trận quan hệ tính hợp thành — AND thay nhân, OR thay cộng.</p>
## 4. Lũy thừa quan hệ

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Với quan hệ $$R$$ trên $$A$$:
</div>

- $$R^1=R$$.
- $$R^{n+1}=R^n\circ R$$.

**Ý nghĩa**: $$(a,b)\in R^k$$ nếu tồn tại đường đi độ dài $$k$$ từ $$a$$ đến $$b$$ trong đồ thị của $$R$$.

![Lũy thừa quan hệ — đường đi nhiều bước](/discrete-mathematics-for-computer-science-iuh/img/course/Example_of_simple_directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.22">$$R^k$$ chứa các cặp (a, b) có đường đi độ dài k từ a đến b trong đồ thị của R.</p>
## 5. Bao đóng

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Bao đóng của quan hệ $$R$$ theo một tính chất là quan hệ nhỏ nhất chứa $$R$$ và có tính chất đó.
</div>

### Bao đóng phản xạ

Thêm mọi cặp $$(a,a)$$ còn thiếu:

<div class="textbook-equation" markdown="1">
$$R_{ref}=R\cup\{(a,a)\mid a\in A\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Bao đóng đối xứng

Thêm chiều ngược cho mọi cặp:

<div class="textbook-equation" markdown="1">
$$R_{sym}=R\cup R^{-1}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Bao đóng bắc cầu

Thêm các cặp biểu diễn đường đi gián tiếp. Với tập hữu hạn $$A$$ có $$n$$ phần tử:

<div class="textbook-equation" markdown="1">
$$R^+=R\cup R^2\cup\cdots\cup R^n.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Bao đóng phản xạ-bắc cầu là:

<div class="textbook-equation" markdown="1">
$$R^*=I_A\cup R^+,$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
trong đó $$I_A=\{(a,a)\mid a\in A\}$$.

![Bao đóng bắc cầu — thêm cung gián tiếp](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.23">Bao đóng bắc cầu $$R^*$$ thêm mọi cặp (a, c) có đường đi từ a đến c, kể cả vòng phản xạ.</p>
## 6. Thuật toán Warshall
**Ý tưởng**: Warshall tính bao đóng bắc cầu từ ma trận kề. Cho phép từng đỉnh $$k$$ làm đỉnh trung gian, cập nhật:

<div class="textbook-equation" markdown="1">
$$M[i,j]=M[i,j]\lor(M[i,k]\land M[k,j]).$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
```python
def warshall(M):
    n = len(M)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                M[i][j] = M[i][j] or (M[i][k] and M[k][j])
    return M
```

![Thuật toán Warshall — reachability](/discrete-mathematics-for-computer-science-iuh/img/course/Example_of_simple_directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.24">Warshall tính bao đóng bắc cầu trên ma trận kề — trả lời truy vấn reachability giữa mọi cặp đỉnh.</p>
## 9. Ứng dụng trong Khoa học Máy tính

- **Đồ thị**: bao đóng bắc cầu trả lời truy vấn reachability.
- **Cơ sở dữ liệu**: truy vấn đệ quy như "tất cả cấp dưới của một quản lý" dùng transitive closure.
- **Compiler**: phân tích call graph để biết hàm nào có thể gọi gián tiếp hàm nào.
- **Bảo mật**: quan hệ quyền truy cập kế thừa cần bao đóng theo cây vai trò.

## Bài tập thực hành

### Bài tập 1: Tính quan hệ hợp thành

Cho $$R = \{(1,2),(2,3)\}$$ và $$S = \{(2,4),(3,5)\}$$. Tính $$R \circ S$$ và $$S \circ R$$.

<details>
<summary>Đáp án</summary>

- $$R \circ S = \{(2,4),(3,5)\}$$ (không có cặp nào thỏa)
- $$S \circ R = \{(1,4),(2,5)\}$$

</details>

### Bài tập 2: Bao đóng

Tìm bao đóng phản xạ và bắc cầu nhỏ nhất của quan hệ $$R = \{(1,2),(2,3)\}$$ trên $$\{1,2,3\}$$.

<details>
<summary>Đáp án</summary>

Bao đóng phản xạ + bắc cầu: $$\{(1,1),(2,2),(3,3),(1,2),(2,3),(1,3)\}$$

</details>

### Bài tập 3: Ma trận Warshall

Cho ma trận quan hệ 3×3, áp dụng thuật toán Warshall một bước.

<details>
<summary>Đáp án</summary>

Thực hiện $$W = W \lor (W[:,k] \land W[k,:])$$ với mỗi k.

</details>

## Xem thêm / Video gợi ý

- [Relations and Functions](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — Trefor Bazett (Equivalence relations)

## Tóm tắt

- **Quan hệ ngược** $$R^{-1}$$: đảo chiều mọi cặp; $$(R^{-1})^{-1} = R$$
- **Hợp thành** $$S \circ R$$: ghép hai bước thành một; tính bằng tích Boolean trên ma trận 0-1
- **Lũy thừa quan hệ** $$R^k$$: các cặp có đường đi độ dài $$k$$
- **Bao đóng**: thêm tối thiểu các cặp để đạt tính chất phản xạ, đối xứng hoặc bắc cầu; $$R^* = I_A \cup R^+$$
- **Warshall**: thuật toán cổ điển tính bao đóng bắc cầu (reachability) trên tập hữu hạn

Trong bài tiếp theo, chúng ta sẽ luyện tập tổng hợp các khái niệm về quan hệ.
