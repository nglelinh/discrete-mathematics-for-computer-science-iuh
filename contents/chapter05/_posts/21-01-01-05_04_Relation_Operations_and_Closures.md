---

layout: post
title: "Phép toán Quan hệ và Bao đóng"
categories: chapter05
date: 2021-01-01
order: 4
required: true
lang: en
excerpt: "Trình bày quan hệ ngược, phép hợp thành quan hệ, tích ma trận Boolean, lũy thừa quan hệ, các loại bao đóng (phản xạ, đối xứng, bắc cầu) và thuật toán Warshall."
---

Ở mục trước, chúng ta đã tìm hiểu quan hệ tương đương và thứ tự bộ phận. Mục này mở rộng sang các **phép toán trên quan hệ** và khái niệm **bao đóng** — công cụ giúp biến đổi và mở rộng cấu trúc liên kết một cách có hệ thống.

Trong các hệ thống thực tế, ta thường cần đảo chiều liên kết, ghép hai quan hệ thành một bước suy diễn mới, hoặc bổ sung các cặp còn thiếu để quan hệ đạt được một tính chất mong muốn. Chẳng hạn, từ quan hệ phụ thuộc trực tiếp giữa các mô-đun, ta cần suy ra mọi phụ thuộc gián tiếp; từ quan hệ kết nối mạng, ta cần biết cặp nút nào có thể liên thông với nhau. Những bài toán đó dẫn trực tiếp đến bao đóng bắc cầu và thuật toán Warshall.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Thực hiện** phép lấy quan hệ ngược, hợp thành và lũy thừa quan hệ.
- **Tính** bao đóng phản xạ, bao đóng đối xứng và bao đóng bắc cầu (bằng lũy thừa hoặc thuật toán Warshall).
- **Giải thích** vai trò của bao đóng bắc cầu trong đồ thị, cơ sở dữ liệu và phân tích chương trình.

**Từ khóa**: hợp thành quan hệ, bao đóng (closure), bao đóng bắc cầu (transitive closure), thuật toán Warshall.
</div>

## Quan hệ ngược

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Với quan hệ $$R\subseteq A\times B$$, **quan hệ ngược** (inverse relation) của $$R$$ là:

<div class="textbook-equation" markdown="1">
$$R^{-1}=\{(b,a)\in B\times A\mid (a,b)\in R\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-example" markdown="1">
**Ví dụ**: Nếu $$R=\{(\text{An},\text{Toán}),(\text{Bình},\text{Lý}),(\text{Chi},\text{Toán})\}$$ biểu diễn quan hệ "sinh viên học môn", thì $$R^{-1}$$ biểu diễn quan hệ "môn có sinh viên theo học":

<div class="textbook-equation" markdown="1">
$$R^{-1}=\{(\text{Toán},\text{An}),(\text{Lý},\text{Bình}),(\text{Toán},\text{Chi})\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

**Tính chất**:

<div class="textbook-equation" markdown="1">
$$(R^{-1})^{-1}=R.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Ngoài ra, $$R$$ đối xứng khi và chỉ khi $$R^{-1}=R$$.

![Quan hệ ngược — đảo chiều cung](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.19">Quan hệ ngược $$R^{-1}$$ đảo hướng mọi cung: (a, b) ∈ R tương ứng với (b, a) ∈ R⁻¹.</p>
## Hợp thành quan hệ

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Cho $$R\subseteq A\times B$$ và $$S\subseteq B\times C$$. **Hợp thành** $$S\circ R$$ là quan hệ từ $$A$$ đến $$C$$ xác định bởi:

<div class="textbook-equation" markdown="1">
$$S\circ R=\{(a,c)\mid \exists b\in B,\ (a,b)\in R\land (b,c)\in S\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

**Ký hiệu**: $$S\circ R$$ đọc là "$$S$$ sau $$R$$" — ta đi qua quan hệ $$R$$ trước rồi tiếp tục qua $$S$$.

<div class="textbook-example" markdown="1">
**Ví dụ**: Cho $$R=\{(1,2),(2,3)\}$$ và $$S=\{(2,1),(3,3)\}$$. Khi đó:

- Vì $$(1,2)\in R$$ và $$(2,1)\in S$$ nên $$(1,1)\in S\circ R$$.
- Vì $$(2,3)\in R$$ và $$(3,3)\in S$$ nên $$(2,3)\in S\circ R$$.

Vậy $$S\circ R=\{(1,1),(2,3)\}$$.

![Hợp thành quan hệ — ghép hai bước](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.20">Hợp thành $$S \circ R$$ ghép hai bước liên tiếp: (a, c) ∈ S∘R khi tồn tại phần tử trung gian b sao cho (a, b) ∈ R và (b, c) ∈ S.</p>
</div>

## Ma trận quan hệ và tích Boolean

Nếu $$R$$ và $$S$$ được biểu diễn bằng các ma trận 0-1 là $$M_R$$ và $$M_S$$, thì ma trận của hợp thành $$S\circ R$$ được tính bằng tích Boolean:

<div class="textbook-equation" markdown="1">
$$M_{S\circ R}[i,j]=\bigvee_k(M_R[i,k]\land M_S[k,j]).$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Trong phép nhân này, phép nhân số học được thay bằng phép `AND` ($$\land$$), còn phép cộng được thay bằng phép `OR` ($$\lor$$).

![Ma trận quan hệ và tích Boolean](/discrete-mathematics-for-computer-science-iuh/img/course/Set_partitions_4__Hasse__matrices.svg)

<p class="textbook-figure-caption" data-figure="5.21">Tích Boolean giữa hai ma trận 0-1 cho ra ma trận của quan hệ hợp thành.</p>
## Lũy thừa quan hệ

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Với quan hệ $$R$$ trên tập $$A$$:

- $$R^1=R$$.
- $$R^{n+1}=R^n\circ R$$ với mọi $$n \ge 1$$.
</div>

**Ý nghĩa**: $$(a,b)\in R^k$$ khi và chỉ khi tồn tại một đường đi có hướng độ dài $$k$$ từ $$a$$ đến $$b$$ trong đồ thị của $$R$$.

![Lũy thừa quan hệ — đường đi nhiều bước](/discrete-mathematics-for-computer-science-iuh/img/course/Example_of_simple_directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.22">$$R^k$$ gồm các cặp (a, b) có đường đi độ dài đúng k từ a đến b trong đồ thị của R.</p>
## Bao đóng

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **Bao đóng** (closure) của quan hệ $$R$$ theo một tính chất $$P$$ là quan hệ nhỏ nhất (theo quan hệ bao hàm) chứa $$R$$ và thỏa mãn tính chất $$P$$.
</div>

### Bao đóng phản xạ

Bổ sung tất cả các cặp $$(a,a)$$ còn thiếu:

<div class="textbook-equation" markdown="1">
$$R_{\text{ref}}=R\cup\{(a,a)\mid a\in A\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Bao đóng đối xứng

Bổ sung chiều ngược cho mọi cặp trong $$R$$:

<div class="textbook-equation" markdown="1">
$$R_{\text{sym}}=R\cup R^{-1}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
### Bao đóng bắc cầu

Bổ sung tất cả các cặp biểu diễn đường đi gián tiếp. Trên tập hữu hạn $$A$$ có $$n$$ phần tử:

<div class="textbook-equation" markdown="1">
$$R^+=R\cup R^2\cup\cdots\cup R^n.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Bao đóng phản xạ–bắc cầu là:

<div class="textbook-equation" markdown="1">
$$R^*=I_A\cup R^+,$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
trong đó $$I_A=\{(a,a)\mid a\in A\}$$.

![Bao đóng bắc cầu — thêm cung gián tiếp](/discrete-mathematics-for-computer-science-iuh/img/course/Directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.23">Bao đóng phản xạ–bắc cầu $$R^*$$ thêm mọi cặp (a, c) có đường đi từ a đến c, kể cả các khuyên phản xạ.</p>
## Thuật toán Warshall

**Ý tưởng**: Thuật toán Warshall tính bao đóng bắc cầu trực tiếp từ ma trận kề $$M$$. Lần lượt cho phép từng đỉnh $$k$$ làm đỉnh trung gian, ta cập nhật:

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

<p class="textbook-figure-caption" data-figure="5.24">Thuật toán Warshall tính bao đóng bắc cầu trên ma trận kề, trả lời bài toán liên thông (reachability) giữa mọi cặp đỉnh.</p>
## Ứng dụng trong Khoa học Máy tính

- **Đồ thị**: Bao đóng bắc cầu trả lời bài toán khả năng đi tới (reachability) giữa mọi cặp đỉnh.
- **Cơ sở dữ liệu**: Các truy vấn đệ quy như "tìm toàn bộ cấp dưới của một quản lý" thực chất tính bao đóng bắc cầu.
- **Trình biên dịch**: Phân tích đồ thị lời gọi (call graph) để xác định hàm nào có thể gọi gián tiếp đến hàm nào.
- **Bảo mật**: Quan hệ kế thừa quyền truy cập theo thứ bậc vai trò cần tính bao đóng bắc cầu.


## Công cụ tương tác

Chạy thuật toán Warshall theo từng vòng lặp $$k$$ để quan sát quá trình tính bao đóng bắc cầu từ ma trận kề.
<div class="interactive-demo" markdown="1">
<div data-demo="relation-closure-warshall"></div>
</div>
<script src="{{ '/public/js/warshall-visualizer.js' | relative_url }}"></script>

### Minh họa tương tác

Quan sát bao đóng phản xạ, bao đóng đối xứng và các bước chạy thuật toán Warshall cho bao đóng bắc cầu.

<div class="interactive-demo" markdown="1">
<div data-demo="relation-explainer" data-preset="next" data-focus="warshall"></div>
</div>
<script src="{{ '/public/js/explainers/relation-explainer.js' | relative_url }}"></script>

## Bài tập thực hành

### Bài tập 1: Tính quan hệ hợp thành

Cho $$R = \{(1,2),(2,3)\}$$ và $$S = \{(2,4),(3,5)\}$$. Tính $$R \circ S$$ và $$S \circ R$$.

<details>
<summary>Đáp án</summary>

- $$R \circ S = \emptyset$$ (không có phần tử trung gian $$b$$ nào thỏa mãn $$(a,b) \in S$$ và $$(b,c) \in R$$).
- $$S \circ R = \{(1,4),(2,5)\}$$ (vì $$(1,2)\in R, (2,4)\in S$$ và $$(2,3)\in R, (3,5)\in S$$).

</details>

### Bài tập 2: Bao đóng

Tìm bao đóng phản xạ–bắc cầu của quan hệ $$R = \{(1,2),(2,3)\}$$ trên tập $$\{1,2,3\}$$.

<details>
<summary>Đáp án</summary>

Bao đóng phản xạ–bắc cầu là: $$\{(1,1),(2,2),(3,3),(1,2),(2,3),(1,3)\}$$.

</details>

### Bài tập 3: Bước cập nhật của thuật toán Warshall

Cho một ma trận quan hệ kích thước $$3 \times 3$$, viết công thức cập nhật tổng quát của thuật toán Warshall ở bước thứ $$k$$.

<details>
<summary>Đáp án</summary>

Ở mỗi bước $$k \in \{0, 1, 2\}$$, cập nhật mọi phần tử $$W[i, j] = W[i, j] \lor (W[i, k] \land W[k, j])$$ (viết gọn dạng ma trận là $$W \leftarrow W \lor (W[:,k] \land W[k,:])$$).

</details>

## Xem thêm / Video gợi ý

- [Relations and Functions](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — Trefor Bazett (Equivalence relations)

## Tóm tắt

- **Quan hệ ngược** $$R^{-1}$$ đảo chiều mọi cặp của $$R$$ và thỏa mãn $$(R^{-1})^{-1} = R$$.
- **Hợp thành** $$S \circ R$$ ghép hai bước liên tiếp thành một, tính được bằng tích Boolean của hai ma trận 0-1.
- **Lũy thừa quan hệ** $$R^k$$ chứa các cặp có đường đi độ dài $$k$$.
- **Bao đóng** bổ sung ít cặp nhất có thể để đạt tính chất phản xạ, đối xứng hoặc bắc cầu; $$R^* = I_A \cup R^+$$.
- **Thuật toán Warshall** tính bao đóng bắc cầu (khả năng đi tới) trên tập hữu hạn với ma trận kề.

Trong bài tiếp theo, chúng ta sẽ luyện tập tổng hợp các kiến thức của Chương 5 về quan hệ.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=_-p8zhizock">Warshall&#x27;s Algorithm (Finding the Transitive Closure)</a> — Neso Academy, tiếng Anh. Giới thiệu cách tính bao đóng bắc cầu bằng thuật toán Warshall.
- <a href="https://www.youtube.com/watch?v=hKCqske0rAE">Warshalls Algorithm</a> — GVSUmath, tiếng Anh. Minh họa từng bước thuật toán Warshall trên ma trận quan hệ.
- <a href="https://www.youtube.com/watch?v=cQiyDUiIcOQ">Relations and their Inverses</a> — Dr. Trefor Bazett, tiếng Anh. Trình bày quan hệ ngược, một phép toán quan trọng của bài học.
