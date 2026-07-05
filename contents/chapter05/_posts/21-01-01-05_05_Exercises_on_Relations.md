---

layout: post
title: "Bài tập Tổng hợp về Quan hệ"
categories: chapter05
date: 2021-01-01
order: 5
required: true
lang: en
excerpt: "Ở mục trước chúng ta đã học phép toán trên quan hệ và bao đóng. Mục này tổng hợp bài tập nhằm củng cố toàn bộ kiến thức chương 5: định nghĩa quan hệ, tính…"
---

Ở mục trước chúng ta đã học phép toán trên quan hệ và bao đóng. Mục này tổng hợp bài tập nhằm củng cố toàn bộ kiến thức chương 5: định nghĩa quan hệ, tính chất, quan hệ tương đương, thứ tự bộ phận, phép toán và bao đóng.

Một chủ đề chỉ được nắm vững khi có thể áp dụng trên nhiều dạng bài khác nhau. Phần luyện tập giúp chúng ta nối lại mạch kiến thức và phát hiện các điểm dễ nhầm lẫn. Trong khoa học máy tính, sai ở phần nền thường kéo theo sai dây chuyền ở phần mô hình hóa; vì vậy, luyện tập không chỉ để ra đáp án đúng mà còn để hình thành phản xạ đọc đề, chọn công cụ và kiểm tra lập luận.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Ôn tập** định nghĩa quan hệ, tính chất và phép toán qua bài tập tổng hợp.
- **Áp dụng** quy trình: đọc đề → mô hình hóa → kiểm tra tính chất → kết luận.
- **Nhận diện** lỗi thường gặp khi làm bài quan hệ và bao đóng.

**Từ khóa**: luyện tập quan hệ, tương đương, thứ tự, bao đóng, Warshall.
</div>

## 1. Ôn tập khái niệm cốt lõi

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một quan hệ $$R$$ từ tập $$A$$ đến tập $$B$$ là một tập con của tích Descartes $$A\times B$$. Nếu $$A=B$$, chúng ta nói $$R$$ là quan hệ trên $$A$$.
</div>

**Ký hiệu**: Viết $$(a,b)\in R$$ hoặc $$aRb$$ để nói rằng $$a$$ có quan hệ với $$b$$. Các tính chất cần kiểm tra gồm phản xạ, đối xứng, phản đối xứng và bắc cầu.

<div class="textbook-example" markdown="1">
**Ví dụ**: Trên $$A=\{1,2,3\}$$, quan hệ $$R=\{(1,1),(2,2),(3,3),(1,2)\}$$ là phản xạ nhưng không đối xứng vì có $$(1,2)$$ mà thiếu $$(2,1)$$.

![Tích Cartesian — nền tảng quan hệ](/discrete-mathematics-for-computer-science-iuh/img/course/Cartesian_Product_qtl1.svg)

<p class="textbook-figure-caption" data-figure="5.25">Mọi quan hệ đều là tập con của tích Cartesian A × B.</p>
</div>

## 2. Chiến lược giải bài quan hệ

**Quy trình đề xuất**:

1. Xác định tập nền $$A$$ và các cặp thuộc $$R$$.
2. Kiểm tra phản xạ: mọi $$(a,a)$$ có mặt chưa?
3. Kiểm tra đối xứng: nếu $$(a,b)$$ có mặt thì $$(b,a)$$ có mặt không?
4. Kiểm tra phản đối xứng: có cặp khác nhau $$a\ne b$$ mà cả hai chiều đều có không?
5. Kiểm tra bắc cầu: nếu $$(a,b)$$ và $$(b,c)$$ có mặt thì $$(a,c)$$ có mặt không?
6. Kết luận loại quan hệ và nêu phản ví dụ nếu tính chất sai.

<div class="interactive-tool" data-tool="relation-practice-checker">
  <p><strong>Demo đề xuất:</strong> sinh viên nhập các cặp của quan hệ, công cụ kiểm tra từng tính chất và yêu cầu sinh viên chỉ ra phản ví dụ trước khi xem đáp án.</p>
</div>

<script src="{{ '/public/js/relation-property-checker.js' | relative_url }}"></script>

![Đồ thị có hướng — kiểm tra tính chất](/discrete-mathematics-for-computer-science-iuh/img/course/Example_of_simple_directed_graph.svg)

<p class="textbook-figure-caption" data-figure="5.26">Khi giải bài, chuyển quan hệ sang ma trận hoặc đồ thị để kiểm tra từng tính chất có hệ thống.</p>
## 3. Bài tập về biểu diễn quan hệ

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

Cho quan hệ $$R=\{(1,1),(1,3),(2,1),(3,2)\}$$ trên $$A=\{1,2,3\}$$. Viết ma trận quan hệ theo thứ tự hàng/cột $$1,2,3$$.

<details>
<summary>Đáp án và giải thích</summary>

Ma trận là (hàng/cột theo thứ tự $$1,2,3$$):

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
Mỗi hàng là phần tử xuất phát, mỗi cột là phần tử đích: ô $$(i,j)=1$$ khi $$(i,j)\in R$$.
</details>

![Ma trận quan hệ](/discrete-mathematics-for-computer-science-iuh/img/course/Set_partitions_4__Hasse__matrices.svg)

<p class="textbook-figure-caption" data-figure="5.27">Ma trận quan hệ — hàng i, cột j bằng 1 khi (aᵢ, aⱼ) thuộc R.</p>
## 4. Bài tập về tính chất

### Bài 3

Xét $$R=\{(1,1),(2,2),(3,3),(1,2),(2,1)\}$$ trên $$A=\{1,2,3\}$$. Quan hệ này có phản xạ, đối xứng, phản đối xứng, bắc cầu không?

<details>
<summary>Đáp án và giải thích</summary>

- Phản xạ: có $$(1,1),(2,2),(3,3)$$ nên đúng.
- Đối xứng: $$(1,2)$$ và $$(2,1)$$ cùng có; các vòng tự đối xứng, nên đúng.
- Phản đối xứng: sai vì $$1\ne2$$ nhưng có cả $$(1,2)$$ và $$(2,1)$$.
- Bắc cầu: đúng. Thành phần $$\{1,2\}$$ có đủ các cặp cần thiết, và $$3$$ chỉ liên hệ với chính nó.
</details>

![So sánh tính phản xạ, đối xứng, bắc cầu](/discrete-mathematics-for-computer-science-iuh/img/course/Undirected_graph.svg)

<p class="textbook-figure-caption" data-figure="5.28">Đối xứng ↔ đồ thị vô hướng; bắc cầu ↔ đường đi gián tiếp suy ra cung trực tiếp.</p>
### Bài 4

Cho $$R=\{(1,2),(2,3),(1,3)\}$$ trên $$A=\{1,2,3\}$$. Quan hệ có bắc cầu không? Có phản xạ không?

<details>
<summary>Đáp án và giải thích</summary>

Bắc cầu đúng vì $$(1,2)$$ và $$(2,3)$$ kéo theo $$(1,3)$$, cặp này đã có. Phản xạ sai vì thiếu $$(1,1),(2,2),(3,3)$$.
</details>

## 5. Bài tập về quan hệ tương đương

### Bài 5

Trên $$\mathbb{Z}$$, định nghĩa $$aRb$$ khi $$a-b$$ chia hết cho 4. Chứng minh $$R$$ là quan hệ tương đương và liệt kê các lớp tương đương.

<details>
<summary>Đáp án và giải thích</summary>

- Phản xạ: $$a-a=0$$ chia hết cho 4.
- Đối xứng: nếu $$4\mid(a-b)$$ thì $$4\mid(b-a)$$.
- Bắc cầu: nếu $$4\mid(a-b)$$ và $$4\mid(b-c)$$ thì $$4\mid(a-c)$$.

Các lớp tương đương là $$[0],[1],[2],[3]$$ theo số dư modulo 4.
</details>

### Bài 6

Quan hệ "có cùng độ dài" trên tập các xâu nhị phân có phải quan hệ tương đương không?

<details>
<summary>Đáp án và giải thích</summary>

Có. Mỗi xâu có cùng độ dài với chính nó; nếu xâu $$u$$ cùng độ dài với $$v$$ thì $$v$$ cùng độ dài với $$u$$; nếu $$u$$ cùng độ dài với $$v$$ và $$v$$ cùng độ dài với $$w$$ thì $$u$$ cùng độ dài với $$w$$.
</details>

![Quan hệ tương đương — lớp và phân hoạch](/discrete-mathematics-for-computer-science-iuh/img/course/Set_partitions_4__Hasse__matrices.svg)

<p class="textbook-figure-caption" data-figure="5.29">Quan hệ tương đương phải thỏa phản xạ, đối xứng và bắc cầu — tạo ra các lớp tương đương rời nhau.</p>
## 6. Bài tập về thứ tự bộ phận

### Bài 7

Xét quan hệ chia hết $$\mid$$ trên $$A=\{1,2,3,6\}$$. Chứng minh đây là thứ tự bộ phận và nêu các cặp phủ trong biểu đồ Hasse.

<details>
<summary>Đáp án và giải thích</summary>

Chia hết phản xạ vì $$a\mid a$$. Phản đối xứng vì nếu $$a\mid b$$ và $$b\mid a$$ với số dương thì $$a=b$$. Bắc cầu vì nếu $$a\mid b$$ và $$b\mid c$$ thì $$a\mid c$$.

Các cặp phủ: $$(1,2),(1,3),(2,6),(3,6)$$.
</details>

### Bài 8

Trong $$(\mathcal{P}(\{a,b,c\}),\subseteq)$$, hai phần tử $$\{a,b\}$$ và $$\{b,c\}$$ có so sánh được không?

<details>
<summary>Đáp án và giải thích</summary>

Không. $$\{a,b\}\nsubseteq\{b,c\}$$ vì thiếu $$a$$, và $$\{b,c\}\nsubseteq\{a,b\}$$ vì thiếu $$c$$.
</details>

## 7. Bài tập về bao đóng

### Bài 9

Cho $$R=\{(1,2),(2,3)\}$$ trên $$A=\{1,2,3\}$$. Tìm bao đóng phản xạ và bao đóng bắc cầu.

<details>
<summary>Đáp án và giải thích</summary>

Bao đóng phản xạ:

<div class="textbook-equation" markdown="1">
$$R\cup\{(1,1),(2,2),(3,3)\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Bao đóng bắc cầu: vì có đường $$1\to2\to3$$ nên thêm $$(1,3)$$. Do đó:

<div class="textbook-equation" markdown="1">
$$R^+=\{(1,2),(2,3),(1,3)\}.$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</details>

### Bài 10

Cho $$R=\{(a,b),(b,c),(c,a)\}$$. Bao đóng bắc cầu có chứa $$(a,a)$$ không?

<details>
<summary>Đáp án và giải thích</summary>

Có. Vì có đường đi $$a\to b\to c\to a$$, nên $$(a,a)$$ thuộc bao đóng bắc cầu. Tương tự $$(b,b)$$ và $$(c,c)$$ cũng thuộc bao đóng bắc cầu.
</details>

![Biểu đồ Hasse — thứ tự bộ phận](/discrete-mathematics-for-computer-science-iuh/img/course/Simple_hasse_diagram.svg)

<p class="textbook-figure-caption" data-figure="5.30">Hasse diagram giúp nhận diện các cặp phủ và phần tử không so sánh được trong poset.</p>
## 8. Ứng dụng trong Khoa học Máy tính
Các bài tập trên tương ứng trực tiếp với tác vụ CS:

- Ma trận quan hệ là ma trận kề của đồ thị.
- Quan hệ tương đương là nền tảng của union-find.
- Thứ tự bộ phận dùng trong topological sort.
- Bao đóng bắc cầu dùng trong reachability và truy vấn phân cấp.

## Bài tập thực hành

### Bài tập 1: Kiểm tra tính chất

Cho quan hệ $$R = \{(1,1),(2,2),(3,3),(1,2),(2,1)\}$$ trên $$\{1,2,3\}$$.  
Xác định các tính chất: phản xạ, đối xứng, bắc cầu.

<details>
<summary>Đáp án</summary>

- Phản xạ: Có (có cặp chéo)
- Đối xứng: Có
- Bắc cầu: Có (vì chỉ có 1-2 và 2-1)

</details>

### Bài tập 2: Tìm lớp tương đương

Tìm tất cả quan hệ tương đương trên tập $$\{a,b\}$$.

<details>
<summary>Đáp án</summary>

Có 2 quan hệ tương đương: quan hệ đồng nhất và quan hệ toàn phần.

</details>

### Bài tập 3: Hasse diagram

Vẽ Hasse diagram cho tập con của $$\{1,2,3\}$$ theo quan hệ chứa.

<details>
<summary>Đáp án</summary>

∅ → {1} → {1,2} → {1,2,3}  
∅ → {2} → {2,3} → {1,2,3}  
∅ → {3} → {1,3} → {1,2,3}  
(và các nhánh khác)

</details>

## Xem thêm / Video gợi ý

- [Relations and Functions](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — Trefor Bazett (Equivalence relations)

## Tóm tắt

- Khi giải bài quan hệ, luôn kiểm tra từng tính chất bằng định nghĩa và phản ví dụ cụ thể
- **Quan hệ tương đương** cần phản xạ, đối xứng, bắc cầu; **thứ tự bộ phận** cần phản xạ, phản đối xứng, bắc cầu
- **Bao đóng** là thao tác thêm tối thiểu các cặp để đạt tính chất mong muốn
- Ma trận quan hệ và đồ thị có hướng là công cụ kiểm tra có hệ thống
