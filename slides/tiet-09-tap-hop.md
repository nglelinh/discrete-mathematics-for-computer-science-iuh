---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Lý thuyết Tập hợp

**Toán Rời Rạc**

Tiết 10 (45 phút) — Set Theory

---

## Mục tiêu tiết học

- Hiểu định nghĩa tập hợp và các ký hiệu cơ bản
- Biểu diễn tập bằng liệt kê, set-builder, khoảng
- Thực hiện phép toán: hợp, giao, hiệu, bù, tích Descartes
- Tính lực lượng và công thức $$|A \cup B|$$
- Nhận biết tập lũy thừa $$\mathcal{P}(A)$$ và ứng dụng CNTT
- Hiểu định lý Cantor và nghịch lý Cantor — giới hạn của "tập mọi tập"

---

## Định nghĩa Tập hợp

**Tập hợp (Set)**: Bộ sưu tập các đối tượng **riêng biệt**, **không có thứ tự**, **không lặp**.

**Ký hiệu**:
- $$A = \{1, 2, 3\}$$
- $$x \in A$$: $$x$$ thuộc $$A$$
- $$x \notin A$$: $$x$$ không thuộc $$A$$

**Ba cách mô tả**: liệt kê, $$\{x \mid P(x)\}$$, khoảng trên $$\mathbb{R}$$.

![Biểu đồ Venn 3 tập](https://commons.wikimedia.org/wiki/Special:FilePath/Venn3.svg?width=480)

---

## Các tập hợp đặc biệt

| Ký hiệu | Tên | Ý nghĩa |
|:-------:|:----|:--------|
| $$\emptyset$$ | Tập rỗng | Không chứa phần tử |
| $$U$$ | Tập vũ trụ | Miền đang xét |
| $$\mathbb{N}$$ | Số tự nhiên | $$0,1,2,\ldots$$ hoặc $$1,2,3,\ldots$$ |
| $$\mathbb{Z}$$ | Số nguyên | $$\ldots,-1,0,1,\ldots$$ |
| $$\mathbb{Q}, \mathbb{R}$$ | Hữu tỷ, thực | Phân số, số thực |

![Ký hiệu tập rỗng ∅](https://commons.wikimedia.org/wiki/Special:FilePath/Empty_set.svg?width=200)

**Tập con**: $$A \subseteq B$$ nếu $$\forall x,\; x \in A \Rightarrow x \in B$$.

![Sơ đồ các tập số ℕ, ℤ, ℚ, ℝ](https://commons.wikimedia.org/wiki/Special:FilePath/Euler_diagram_of_number_sets.svg?width=480)

---

## Tập con & Tập bằng nhau

- $$\emptyset \subseteq A$$ với mọi tập $$A$$
- $$A \subseteq A$$ (phản xạ)
- Nếu $$A \subseteq B$$ và $$B \subseteq C$$ thì $$A \subseteq C$$ (bắc cầu)

**Tập bằng nhau**: $$A = B \Leftrightarrow A \subseteq B$$ và $$B \subseteq A$$.

**Ví dụ**: $$\{x \mid x^{2}=4\} = \{-2, 2\}$$.

![Biểu đồ Venn: A ⊆ B](https://commons.wikimedia.org/wiki/Special:FilePath/Venn_A_subset_B.svg?width=420)

---

## Phép toán trên tập hợp

1. **Hợp**: $$A \cup B = \{x \mid x \in A \lor x \in B\}$$
2. **Giao**: $$A \cap B = \{x \mid x \in A \land x \in B\}$$
3. **Hiệu**: $$A \setminus B = \{x \mid x \in A \land x \notin B\}$$
4. **Phần bù**: $$A^{c}$$ (ký hiệu $$^{c}$$ = *complement*)
5. **Tích Descartes**: $$A \times B = \{(a,b) \mid a \in A,\, b \in B\}$$

---

## Biểu đồ Venn — Hợp, Giao, Hiệu

![Hợp A ∪ B](https://commons.wikimedia.org/wiki/Special:FilePath/Union_of_sets_A_and_B.svg?width=380)

![Giao A ∩ B](https://commons.wikimedia.org/wiki/Special:FilePath/Venn_A_intersect_B.svg?width=380)

![Hiệu A \ B](https://commons.wikimedia.org/wiki/Special:FilePath/Venn_A_setminus_B.svg?width=380)

---

## Phần bù — Ký hiệu $$A^{c}$$

**Ký hiệu**: $$A^{c}$$ đọc là *phần bù của $$A$$* (còn gặp $$A'$$, $$\overline{A}$$).

**Định nghĩa** (trong tập vũ trụ $$U$$):
$$A^{c} = U \setminus A = \{x \in U \mid x \notin A\}$$

**Lưu ý**: Phần bù **phụ thuộc $$U$$** — đổi miền thì đổi kết quả.

**Ví dụ**: $$U=\{1,2,3,4,5\}$$, $$A=\{1,3,5\} \Rightarrow A^{c}=\{2,4\}$$.

![Phần bù Aᶜ = U \ A](https://commons.wikimedia.org/wiki/Special:FilePath/Venn-Diagram-NOT-P.png?width=380)

---

## Tính chất & De Morgan

- Giao hoán, kết hợp; hợp hoán, kết hợp
- Phân phối: $$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$$

**Luật De Morgan**:
$$(A \cup B)^{c} = A^{c} \cap B^{c},\quad (A \cap B)^{c} = A^{c} \cup B^{c}$$

**Hiệu đối xứng**: $$A \triangle B = (A \setminus B) \cup (B \setminus A)$$.

![Luật De Morgan trên Venn](https://commons.wikimedia.org/wiki/Special:FilePath/Intersections_of_two_sets_and_their_complements.svg?width=480)

---

## Lực lượng tập hợp

**Lực lượng (cardinality)**: $$|A|$$ = số phần tử của $$A$$ (hữu hạn).

**Công thức cơ bản**:
$$|A \cup B| = |A| + |B| - |A \cap B|$$

**Tích Descartes**: $$|A \times B| = |A| \cdot |B|$$.

**Ví dụ**: $$|A|=5, |B|=4, |A \cap B|=2 \Rightarrow |A \cup B| = 7$$.

![Bao hàm–loại trừ: A ∩ B](https://commons.wikimedia.org/wiki/Special:FilePath/Venn_A_intersect_B.svg?width=420)

---

## Tập lũy thừa $$\mathcal{P}(A)$$

**Định nghĩa**: $$\mathcal{P}(A) = \{X \mid X \subseteq A\}$$ — tập mọi tập con của $$A$$.

**Ví dụ**: $$A=\{a,b\} \Rightarrow \mathcal{P}(A)=\{\emptyset,\{a\},\{b\},\{a,b\}\}$$

**Định lý**: Nếu $$|A|=n$$ thì $$|\mathcal{P}(A)| = 2^{n}$$.

**Liên hệ**: Mỗi tập con ↔ chuỗi bit độ dài $$n$$ (có/không chọn phần tử).

![Sơ đồ tập lũy thừa P(A)](https://commons.wikimedia.org/wiki/Special:FilePath/Powerset.svg?width=420)

---

## Định lý Cantor

Với **mọi** tập $$A$$ (hữu hạn hay vô hạn):
$$|\mathcal{P}(A)| > |A|$$

**Hữu hạn**: $$|A|=n \Rightarrow |\mathcal{P}(A)|=2^{n} > n$$.

**Vô hạn**: không tồn tại song ánh $$A \to \mathcal{P}(A)$$ (lập luận đường chéo).

![Lập luận đường chéo Cantor](https://commons.wikimedia.org/wiki/Special:FilePath/Diagonal_argument.svg?width=480)

---

## Nghịch lý Cantor

**Giả sử** có tập $$V$$ = "mọi tập hợp" (tập vũ trụ naive).

1. Mọi tập con của $$V$$ cũng là tập ⇒ $$\mathcal{P}(V) \subseteq V$$ ⇒ $$|\mathcal{P}(V)| \le |V|$$
2. Định lý Cantor ⇒ $$|\mathcal{P}(V)| > |V|$$ ⇒ **mâu thuẫn**

**Kết luận**: Không thể có "tập của mọi tập" trong lý thuyết tập naive.

**Bài học**: dẫn tới tiên đề hóa (ZFC); tránh tự tham chiếu trong định nghĩa (cf. Russell).

![Georg Cantor — lý thuyết tập hợp](https://commons.wikimedia.org/wiki/Special:FilePath/Georg_Cantor_1894.jpg?width=280)

---

## Ứng dụng SQL

Bảng quan hệ = tập các **bộ** (tuple); điều kiện `WHERE` = lọc tập con.

```sql
-- Sinh viên học Toán rời rạc HOẶC Lập trình
SELECT student_id FROM Enrollments
WHERE course IN ('DM', 'PROG');

-- Giao: sinh viên học CẢ HAI môn
SELECT e1.student_id
FROM Enrollments e1 JOIN Enrollments e2
  ON e1.student_id = e2.student_id
WHERE e1.course='DM' AND e2.course='PROG';
```

`UNION`, `INTERSECT`, `EXCEPT` tương ứng hợp, giao, hiệu.

---

## Tích Descartes trong SQL

`CROSS JOIN` (hoặc `FROM A, B`) = tích Descartes: mỗi dòng bảng trái ghép mọi dòng bảng phải.

```sql
CREATE TEMP TABLE Colors (color TEXT);
INSERT INTO Colors VALUES ('red'), ('blue');

CREATE TEMP TABLE Sizes (size TEXT);
INSERT INTO Sizes VALUES ('S'), ('M'), ('L');

SELECT c.color, s.size
FROM Colors c CROSS JOIN Sizes s;
-- 2 × 3 = 6 dòng: (red,S), (red,M), ...
```

**Liên hệ**: $$|A \times B| = |A| \cdot |B|$$ ↔ số dòng kết quả.

![Phép JOIN — lọc tích Descartes](https://commons.wikimedia.org/wiki/Special:FilePath/Square_join.png?width=480)

---

## Thực hành 1

Cho $$A=\{1,2,3,4\}$$, $$B=\{3,4,5,6\}$$, $$U=\{1,\ldots,10\}$$.

Tính:
1. $$A \cup B$$ và $$A \cap B$$
2. $$(A \cup B)^{c}$$ (trong $$U$$)
3. $$|A \cup B|$$ bằng công thức và đếm trực tiếp
4. Liệt kê 4 cặp trong $$A \times B$$

---

## Thực hành 2

Cho $$S=\{a,b,c\}$$.

1. Liệt kê toàn bộ $$\mathcal{P}(S)$$
2. Kiểm tra $$|\mathcal{P}(S)| = 2^{|S|}$$
3. Chứng minh bằng đếm: nếu thêm phần tử mới vào $$A$$ thì số tập con tăng gấp đôi

---

## Thực hành 3

Chứng minh bằng phần tử:
$$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$$

Gợi ý: chứng minh hai chiều ⊆ bằng định nghĩa $$\in$$.

---

## Tóm tắt Tiết 9

- Tập hợp = mô hình dữ liệu nền tảng trong toán và CNTT
- Phép toán tập ↔ phép logic (∧, ∨, ¬) qua định nghĩa phần tử
- $$|A \cup B| = |A|+|B|-|A \cap B|$$ — inclusion–exclusion cơ bản
- $$\mathcal{P}(A)$$ có $$2^{|A|}$$ phần tử — quan trọng cho đếm và Bool
- Định lý Cantor: $$|\mathcal{P}(A)| > |A|$$; nghịch lý Cantor — không có "tập mọi tập"
- $$A \times B$$ là nền của **quan hệ** (tiết 11)

---

## Liên hệ

**Chứng minh chính**: Chứng minh tập bằng nhau qua hai chiều ⊆.

**Edge case**: $$\emptyset$$, $$U$$, tập vô hạn — lực lượng khác đếm hữu hạn.

**Liên hệ**: Tập hợp ↔ Logic Boolean ↔ Quan hệ (Cartesian product).

**Ứng dụng**: Relational algebra, `HashSet`, Bloom filter, cardinality estimate.

---

## Bài tập ôn tập (1/2)

1. **Bài 1**: Cho $$|A|=12, |B|=15, |A \cap B|=5$$. Tính $$|A \cup B|$$.

2. **Bài 2**: Liệt kê $$\mathcal{P}(\{1,2,3\})$$ và tính $$|\mathcal{P}(A)|$$.

3. **Bài 3**: Chứng minh $$(A \cup B)^{c} = A^{c} \cap B^{c}$$ (De Morgan).

---

## Bài tập ôn tập (2/2)

4. **Bài 4**: Viết set-builder cho tập số nguyên chia hết cho 3 trong $$[1,20]$$.

5. **Bài 5**: Có 26 ký tự in hoa, mật khẩu dài 4 ký tự (có lặp). Tính $$|A^{4}|$$ với $$A$$ = bảng chữ cái. Giải thích liên hệ tích Descartes.
