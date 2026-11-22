---

layout: post
title: "Bài tập Tổng hợp về Quan hệ"
categories: chapter05
date: 2021-01-01
order: 5
required: true
lang: en
excerpt: "Tổng hợp bài tập thực hành củng cố toàn bộ kiến thức Chương 5: biểu diễn quan hệ, kiểm tra bốn tính chất, quan hệ tương đương, thứ tự bộ phận, biểu đồ Hasse và bao đóng."
---

Ở mục trước, chúng ta đã học các phép toán trên quan hệ và khái niệm bao đóng. Mục này tổng hợp các bài tập nhằm củng cố toàn bộ kiến thức của Chương 5: định nghĩa và cách biểu diễn quan hệ, bốn tính chất cơ bản, quan hệ tương đương, thứ tự bộ phận, biểu đồ Hasse và bao đóng.

Việc luyện tập trên nhiều dạng bài khác nhau giúp hệ thống hóa kiến thức và nhận diện sớm các điểm dễ nhầm lẫn. Khi giải bài tập, mục tiêu không chỉ là tìm ra kết quả đúng mà còn rèn quy trình đọc đề, chọn cách biểu diễn phù hợp và kiểm tra lại lập luận bằng định nghĩa hoặc phản ví dụ.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Ôn tập** định nghĩa quan hệ, bốn tính chất cơ bản và các phép toán qua hệ thống bài tập tổng hợp.
- **Áp dụng** quy trình giải bài: đọc đề → biểu diễn quan hệ → kiểm tra từng tính chất → kết luận.
- **Nhận diện** các lỗi thường gặp khi chứng minh quan hệ tương đương, vẽ biểu đồ Hasse và tìm bao đóng.

**Từ khóa**: luyện tập quan hệ, quan hệ tương đương, thứ tự bộ phận, bao đóng, thuật toán Warshall.
</div>

## Ôn tập khái niệm cốt lõi

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một quan hệ $$R$$ từ tập $$A$$ đến tập $$B$$ là một tập con của tích Descartes $$A\times B$$. Khi $$A=B$$, ta nói $$R$$ là một quan hệ trên $$A$$.
</div>

**Ký hiệu**: Viết $$(a,b)\in R$$ hoặc $$aRb$$ để chỉ $$a$$ có quan hệ $$R$$ với $$b$$. Bốn tính chất cơ bản cần kiểm tra là phản xạ, đối xứng, phản đối xứng và bắc cầu.

<div class="textbook-example" markdown="1">
**Ví dụ**: Trên $$A=\{1,2,3\}$$, quan hệ $$R=\{(1,1),(2,2),(3,3),(1,2)\}$$ có tính phản xạ nhưng không đối xứng vì có $$(1,2)$$ nhưng thiếu $$(2,1)$$.

![Tích Cartesian — nền tảng quan hệ](/discrete-mathematics-for-computer-science-iuh/img/course/Cartesian_Product_qtl1.svg)

<p class="textbook-figure-caption" data-figure="5.25">Mọi quan hệ hai ngôi đều là một tập con của tích Descartes A × B.</p>
</div>

## Chiến lược giải bài quan hệ

**Quy trình kiểm tra đề xuất**:

1. Xác định rõ tập nền $$A$$ và tập các cặp thuộc $$R$$.
2. Kiểm tra tính phản xạ: mọi cặp $$(a,a)$$ với $$a \in A$$ đã có mặt chưa?
3. Kiểm tra tính đối xứng: với mỗi $$(a,b) \in R$$, cặp $$(b,a)$$ có thuộc $$R$$ không?
4. Kiểm tra tính phản đối xứng: có tồn tại hai phần tử khác nhau $$a \ne b$$ sao cho cả $$(a,b)$$ và $$(b,a)$$ đều thuộc $$R$$ không?
5. Kiểm tra tính bắc cầu: với mọi $$(a,b) \in R$$ và $$(b,c) \in R$$, cặp $$(a,c)$$ có thuộc $$R$$ không?
6. Kết luận loại quan hệ và nêu rõ phản ví dụ cho mỗi tính chất không thỏa mãn.

<div class="interactive-tool" data-tool="relation-practice-checker">
  <p><strong>Công cụ thực hành:</strong> nhập các cặp của một quan hệ để kiểm tra từng tính chất và xác định phản ví dụ trước khi đối chiếu đáp án.</p>
</div>

<script src="{{ '/public/js/relation-property-checker.js' | relative_url }}"></script>

![Đồ thị có hướng — kiểm tra tính chất](/discrete-mathematics-for-computer-science-iuh/img/course/Example_of_simple_directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.26">Chuyển quan hệ sang ma trận 0-1 hoặc đồ thị có hướng giúp kiểm tra từng tính chất một cách có hệ thống.</p>
## Bài tập về biểu diễn quan hệ

### Bài 1

Cho $$A=\{1,2,3\}$$ và $$B=\{x,y\}$$. Hãy liệt kê $$A\times B$$ và quan hệ:

<div class="textbook-equation" markdown="1">
$$R=\{(a,b)\mid a\in A, b\in B, a\text{ lẻ}\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<details>
<summary>Đáp án và giải thích</summary>

<div class="textbook-equation" markdown="1">
$$A\times B=\{(1,x),(1,y),(2,x),(2,y),(3,x),(3,y)\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Vì $$a$$ lẻ nên $$a=1$$ hoặc $$a=3$$. Do đó:

<div class="textbook-equation" markdown="1">
$$R=\{(1,x),(1,y),(3,x),(3,y)\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</details>

### Bài 2

Cho quan hệ $$R=\{(1,1),(1,3),(2,1),(3,2)\}$$ trên $$A=\{1,2,3\}$$. Viết ma trận quan hệ theo thứ tự hàng và cột $$1,2,3$$.

<details>
<summary>Đáp án và giải thích</summary>

Ma trận quan hệ (hàng và cột theo thứ tự $$1,2,3$$) là:

<div class="textbook-equation" markdown="1">
$$
\begin{array}{c|ccc}
 & 1 & 2 & 3 \\
\hline
1 & 1 & 0 & 1 \\
2 & 1 & 0 & 0 \\
3 & 0 & 1 & 0
\end{array}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Mỗi hàng ứng với phần tử nguồn và mỗi cột ứng với phần tử đích: ô $$(i,j)=1$$ khi $$(i,j)\in R$$.
</details>

![Ma trận quan hệ](/discrete-mathematics-for-computer-science-iuh/img/course/Set_partitions_4__Hasse__matrices.svg)

<p class="textbook-figure-caption" data-figure="5.27">Ma trận quan hệ — phần tử tại hàng i, cột j bằng 1 khi và chỉ khi (aᵢ, aⱼ) ∈ R.</p>
## Bài tập về tính chất

### Bài 3

Xét $$R=\{(1,1),(2,2),(3,3),(1,2),(2,1)\}$$ trên $$A=\{1,2,3\}$$. Quan hệ này có phản xạ, đối xứng, phản đối xứng và bắc cầu không?

<details>
<summary>Đáp án và giải thích</summary>

- Phản xạ: có, vì đủ ba cặp $$(1,1),(2,2),(3,3)$$.
- Đối xứng: có, vì $$(1,2)$$ và $$(2,1)$$ cùng có mặt, còn các cặp trên đường chéo tự đối xứng.
- Phản đối xứng: không, vì $$1\ne 2$$ nhưng cả $$(1,2)$$ và $$(2,1)$$ đều thuộc $$R$$.
- Bắc cầu: có, vì mọi chuỗi hợp lệ trên $$\{1,2\}$$ đều đóng (chẳng hạn $$(1,2)$$ và $$(2,1)$$ kéo theo $$(1,1) \in R$$, $$(2,1)$$ và $$(1,2)$$ kéo theo $$(2,2) \in R$$), còn $$3$$ chỉ liên hệ với chính nó.
</details>

![So sánh tính phản xạ, đối xứng, bắc cầu](/discrete-mathematics-for-computer-science-iuh/img/course/Undirected_graph.svg)

<p class="textbook-figure-caption" data-figure="5.28">Quan hệ đối xứng tương ứng với đồ thị vô hướng; tính bắc cầu đòi hỏi mọi đường đi độ dài 2 đều có cung trực tiếp.</p>
### Bài 4

Cho $$R=\{(1,2),(2,3),(1,3)\}$$ trên $$A=\{1,2,3\}$$. Quan hệ này có bắc cầu không? Có phản xạ không?

<details>
<summary>Đáp án và giải thích</summary>

- Bắc cầu: có, vì cặp đường đi duy nhất độ dài 2 là $$(1,2)$$ và $$(2,3)$$, và cặp $$(1,3)$$ đã có mặt trong $$R$$.
- Phản xạ: không, vì thiếu các cặp $$(1,1),(2,2),(3,3)$$.
</details>

## Bài tập về quan hệ tương đương

### Bài 5

Trên $$\mathbb{Z}$$, định nghĩa $$aRb$$ khi $$a-b$$ chia hết cho 4. Chứng minh $$R$$ là quan hệ tương đương và liệt kê các lớp tương đương.

<details>
<summary>Đáp án và giải thích</summary>

- Phản xạ: $$a-a=0$$ chia hết cho 4.
- Đối xứng: nếu $$4\mid(a-b)$$ thì $$4\mid(b-a)$$.
- Bắc cầu: nếu $$4\mid(a-b)$$ và $$4\mid(b-c)$$ thì $$4\mid(a-c)$$.

Bốn lớp tương đương tương ứng với bốn số dư khi chia cho 4 là $$[0],[1],[2],[3]$$.
</details>

### Bài 6

Quan hệ "có cùng độ dài" trên tập các xâu nhị phân có phải là quan hệ tương đương không?

<details>
<summary>Đáp án và giải thích</summary>

Có. Mỗi xâu có cùng độ dài với chính nó (phản xạ); nếu xâu $$u$$ cùng độ dài với $$v$$ thì $$v$$ cùng độ dài với $$u$$ (đối xứng); và nếu $$u$$ cùng độ dài với $$v$$, $$v$$ cùng độ dài với $$w$$ thì $$u$$ cùng độ dài với $$w$$ (bắc cầu).
</details>

![Quan hệ tương đương — lớp và phân hoạch](/discrete-mathematics-for-computer-science-iuh/img/course/Set_partitions_4__Hasse__matrices.svg)

<p class="textbook-figure-caption" data-figure="5.29">Quan hệ tương đương thỏa mãn đồng thời phản xạ, đối xứng và bắc cầu, phân hoạch tập nền thành các lớp rời nhau.</p>
## Bài tập về thứ tự bộ phận

### Bài 7

Xét quan hệ chia hết $$\mid$$ trên $$A=\{1,2,3,6\}$$. Chứng minh đây là một thứ tự bộ phận và nêu các cặp phủ trong biểu đồ Hasse.

<details>
<summary>Đáp án và giải thích</summary>

Quan hệ chia hết trên tập số nguyên dương có tính phản xạ ($$a\mid a$$), phản đối xứng (nếu $$a\mid b$$ và $$b\mid a$$ với $$a,b>0$$ thì $$a=b$$) và bắc cầu (nếu $$a\mid b$$ và $$b\mid c$$ thì $$a\mid c$$).

Các cặp phủ trong biểu đồ Hasse là: $$(1,2), (1,3), (2,6), (3,6)$$.
</details>

### Bài 8

Trong poset $$(\mathcal{P}(\{a,b,c\}),\subseteq)$$, hai phần tử $$\{a,b\}$$ và $$\{b,c\}$$ có so sánh được với nhau không?

<details>
<summary>Đáp án và giải thích</summary>

Không. Ta có $$\{a,b\}\nsubseteq\{b,c\}$$ (vì $$a \notin \{b,c\}$$) và $$\{b,c\}\nsubseteq\{a,b\}$$ (vì $$c \notin \{a,b\}$$).
</details>

## Bài tập về bao đóng

### Bài 9

Cho $$R=\{(1,2),(2,3)\}$$ trên $$A=\{1,2,3\}$$. Tìm bao đóng phản xạ và bao đóng bắc cầu của $$R$$.

<details>
<summary>Đáp án và giải thích</summary>

Bao đóng phản xạ:

<div class="textbook-equation" markdown="1">
$$R_{\text{ref}} = R\cup\{(1,1),(2,2),(3,3)\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Bao đóng bắc cầu: vì có đường đi $$1\to 2\to 3$$ nên cần bổ sung cặp $$(1,3)$$. Do đó:

<div class="textbook-equation" markdown="1">
$$R^+=\{(1,2),(2,3),(1,3)\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</details>

### Bài 10

Cho $$R=\{(a,b),(b,c),(c,a)\}$$. Bao đóng bắc cầu của $$R$$ có chứa cặp $$(a,a)$$ không?

<details>
<summary>Đáp án và giải thích</summary>

Có. Vì tồn tại đường đi độ dài 3 là $$a\to b\to c\to a$$, cặp $$(a,a)$$ thuộc bao đóng bắc cầu $$R^+$$. Tương tự, $$(b,b)$$ và $$(c,c)$$ cũng thuộc $$R^+$$.
</details>

![Biểu đồ Hasse — thứ tự bộ phận](/discrete-mathematics-for-computer-science-iuh/img/course/Simple_hasse_diagram.svg)

<p class="textbook-figure-caption" data-figure="5.30">Biểu đồ Hasse giúp nhận diện các cặp phủ và các cặp phần tử không so sánh được trong poset.</p>
## Ứng dụng trong Khoa học Máy tính

Các dạng bài tập trên tương ứng trực tiếp với nhiều kỹ thuật trong khoa học máy tính:

- Ma trận quan hệ chính là ma trận kề của đồ thị.
- Quan hệ tương đương là cơ sở lý thuyết của cấu trúc dữ liệu Union-Find.
- Thứ tự bộ phận là nền tảng của thuật toán sắp xếp tô-pô (topological sort).
- Bao đóng bắc cầu giải bài toán liên thông (reachability) và các truy vấn phân cấp.

## Bài tập thực hành bổ sung

### Bài tập 1: Kiểm tra tính chất

Cho quan hệ $$R = \{(1,1),(2,2),(3,3),(1,2),(2,1)\}$$ trên $$\{1,2,3\}$$.  
Xác định các tính chất: phản xạ, đối xứng và bắc cầu.

<details>
<summary>Đáp án</summary>

- Phản xạ: Có (chứa đủ các cặp chéo $$(1,1),(2,2),(3,3)$$).
- Đối xứng: Có (có cả $$(1,2)$$ và $$(2,1)$$).
- Bắc cầu: Có (các tổ hợp giữa $$(1,2)$$ và $$(2,1)$$ tạo ra $$(1,1)$$ và $$(2,2)$$, đều đã thuộc $$R$$).

</details>

### Bài tập 2: Đếm quan hệ tương đương

Tìm tất cả các quan hệ tương đương trên tập $$A = \{a,b\}$$.

<details>
<summary>Đáp án</summary>

Có đúng 2 quan hệ tương đương (tương ứng 2 phân hoạch của $$\{a,b\}$$): quan hệ đồng nhất $$\{(a,a),(b,b)\}$$ và quan hệ toàn phần $$\{(a,a),(b,b),(a,b),(b,a)\}$$.

</details>

### Bài tập 3: Biểu đồ Hasse của tập lũy thừa

Vẽ biểu đồ Hasse cho tập lũy thừa của $$\{1,2,3\}$$ theo quan hệ bao hàm $$\subseteq$$.

<details>
<summary>Đáp án</summary>

Các mức từ dưới lên trên (mỗi cạnh nối hai tập hơn kém nhau đúng 1 phần tử):

- Mức 0: $$\emptyset$$
- Mức 1: $$\{1\}, \{2\}, \{3\}$$ (đều phủ $$\emptyset$$)
- Mức 2: $$\{1,2\}$$ phủ $$\{1\}, \{2\}$$; $$\{1,3\}$$ phủ $$\{1\}, \{3\}$$; $$\{2,3\}$$ phủ $$\{2\}, \{3\}$$
- Mức 3: $$\{1,2,3\}$$ phủ $$\{1,2\}, \{1,3\}, \{2,3\}$$

</details>

## Xem thêm / Video gợi ý

- [Relations and Functions](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — Trefor Bazett (Equivalence relations)

## Tóm tắt

- Khi giải bài toán quan hệ, luôn kiểm tra từng tính chất theo đúng định nghĩa và đưa ra phản ví dụ cụ thể khi tính chất không đúng.
- **Quan hệ tương đương** đòi hỏi phản xạ, đối xứng và bắc cầu; **thứ tự bộ phận** đòi hỏi phản xạ, phản đối xứng và bắc cầu.
- **Bao đóng** là thao tác bổ sung ít cặp nhất để quan hệ đạt tính chất yêu cầu.
- Ma trận 0-1 và đồ thị có hướng giúp kiểm tra tính chất có hệ thống và hạn chế sai sót.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=TctNssYMXJE">You need to check EVERY spot for reflexivity, symmetry, and transitivity</a> — Dr. Trefor Bazett, tiếng Anh. Lưu ý kiểm tra đầy đủ mọi cặp phần tử trước khi kết luận tính chất của quan hệ.
- <a href="https://www.youtube.com/watch?v=qujnPIPjKrA">[Discrete Mathematics] Relations Examples</a> — TrevTutor, tiếng Anh. Các ví dụ luyện nhận dạng tính chất quan hệ, sát với dạng bài tập trong chương.
- <a href="https://www.youtube.com/watch?v=YLrQWK2VBro">Can You Prove that R is an equivalence relation iff R is circular and reflexive</a> — TrevTutor, tiếng Anh. Chứng minh quan hệ tương đương dựa trên điều kiện phản xạ và tính tuần hoàn.
