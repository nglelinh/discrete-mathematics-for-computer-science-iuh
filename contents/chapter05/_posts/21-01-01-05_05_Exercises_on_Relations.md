---
layout: post
title: "Bài tập Tổng hợp về Quan hệ"
categories: chapter05
date: 2021-01-01
order: 5
required: true
lang: en
---

# Bài tập Tổng hợp về Quan hệ

Sau khi đã học định nghĩa, tính chất, quan hệ tương đương, thứ tự bộ phận và closure, điều quan trọng không còn là “nhớ tên khái niệm” mà là nhận ra chúng trong bài toán mới. Một quan hệ cho trước có thể trông lộn xộn, nhưng chỉ cần hỏi đúng vài câu, cấu trúc của nó sẽ hiện ra.

Bài luyện tập này là nơi biến lý thuyết thành phản xạ. Bạn sẽ phải tự phân tích, tự kiểm tra tính chất, tự quyết định nên dùng ma trận, đồ thị hay suy luận ký hiệu. Đây cũng là kiểu kỹ năng rất gần với công việc thực tế: không ai đưa sẵn nhãn cho dữ liệu, ta phải tự khám phá cấu trúc của nó.

## 1. Ôn tập khái niệm cốt lõi

**Định nghĩa**: Một quan hệ $$R$$ từ tập $$A$$ đến tập $$B$$ là một tập con của tích Descartes $$A\times B$$. Nếu $$A=B$$, ta nói $$R$$ là quan hệ trên $$A$$.

**Ký hiệu**: Viết $$(a,b)\in R$$ hoặc $$aRb$$ để nói rằng $$a$$ có quan hệ với $$b$$. Các tính chất cần kiểm tra gồm phản xạ, đối xứng, phản đối xứng và bắc cầu.

**Ví dụ**: Trên $$A=\{1,2,3\}$$, quan hệ $$R=\{(1,1),(2,2),(3,3),(1,2)\}$$ là phản xạ nhưng không đối xứng vì có $$(1,2)$$ mà thiếu $$(2,1)$$.

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

## 3. Bài tập về biểu diễn quan hệ

### Bài 1

Cho $$A=\{1,2,3\}$$ và $$B=\{x,y\}$$. Hãy liệt kê $$A\times B$$ và quan hệ:

$$R=\{(a,b)\mid a\in A, b\in B, a\text{ lẻ}\}.$$

<details>
<summary>Đáp án và giải thích</summary>

$$A\times B=\{(1,x),(1,y),(2,x),(2,y),(3,x),(3,y)\}.$$

Vì $$a$$ lẻ nên $$a=1$$ hoặc $$a=3$$. Do đó:

$$R=\{(1,x),(1,y),(3,x),(3,y)\}.$$
</details>

### Bài 2

Cho quan hệ $$R=\{(1,1),(1,3),(2,1),(3,2)\}$$ trên $$A=\{1,2,3\}$$. Viết ma trận quan hệ theo thứ tự hàng/cột $$1,2,3$$.

<details>
<summary>Đáp án và giải thích</summary>

Ma trận là:

```text
    1 2 3
1 [ 1 0 1 ]
2 [ 1 0 0 ]
3 [ 0 1 0 ]
```

Mỗi hàng là phần tử xuất phát, mỗi cột là phần tử đích.
</details>

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

$$R\cup\{(1,1),(2,2),(3,3)\}.$$

Bao đóng bắc cầu: vì có đường $$1\to2\to3$$ nên thêm $$(1,3)$$. Do đó:

$$R^+=\{(1,2),(2,3),(1,3)\}.$$
</details>

### Bài 10

Cho $$R=\{(a,b),(b,c),(c,a)\}$$. Bao đóng bắc cầu có chứa $$(a,a)$$ không?

<details>
<summary>Đáp án và giải thích</summary>

Có. Vì có đường đi $$a\to b\to c\to a$$, nên $$(a,a)$$ thuộc bao đóng bắc cầu. Tương tự $$(b,b)$$ và $$(c,c)$$ cũng thuộc bao đóng bắc cầu.
</details>

## 8. Ứng dụng trong Khoa học Máy tính

Các bài tập trên tương ứng trực tiếp với tác vụ CS:

- Ma trận quan hệ là ma trận kề của đồ thị.
- Quan hệ tương đương là nền tảng của union-find.
- Thứ tự bộ phận dùng trong topological sort.
- Bao đóng bắc cầu dùng trong reachability và truy vấn phân cấp.

## 9. Nhầm lẫn thường gặp

<div class="content-box warning-box" markdown="1">
**Nhầm lẫn 1**: Kiểm tra bắc cầu bằng mắt mà không xét tất cả chuỗi hai bước. Hãy tìm mọi $$(a,b)$$ và $$(b,c)$$ rồi kiểm tra $$(a,c)$$.

**Nhầm lẫn 2**: Kết luận quan hệ tương đương chỉ vì các phần tử được chia nhóm. Vẫn phải chứng minh phản xạ, đối xứng và bắc cầu hoặc chỉ ra phân hoạch rõ ràng.

**Nhầm lẫn 3**: Vẽ biểu đồ Hasse nhưng giữ cả cạnh bắc cầu. Biểu đồ Hasse chỉ giữ quan hệ phủ.
</div>

## Tóm tắt

Khi giải bài quan hệ, luôn kiểm tra từng tính chất bằng định nghĩa và phản ví dụ cụ thể. Quan hệ tương đương cần phản xạ, đối xứng, bắc cầu; thứ tự bộ phận cần phản xạ, phản đối xứng, bắc cầu. Bao đóng là thao tác thêm tối thiểu các cặp để đạt tính chất mong muốn.
