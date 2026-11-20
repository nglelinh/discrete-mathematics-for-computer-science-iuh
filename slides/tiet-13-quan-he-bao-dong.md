---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Phép toán Quan hệ & Bao đóng

**Toán Rời Rạc**

Tiết 13 (45 phút) — ch05 `05_04`

---

## Mục tiêu tiết học

- Thực hiện hợp, giao, nghịch đảo và hợp thành quan hệ
- Hiểu lũy thừa quan hệ và ý nghĩa đường đi trong đồ thị
- Tính bao đóng phản xạ, đối xứng, bắc cầu
- Áp dụng Warshall vào truy vấn reachability
- Liên hệ với CSDL, phân quyền và call graph

---

## Hợp & Giao quan hệ

Với $$R, S \subseteq A \times B$$ (cùng miền):

- $$R \cup S$$: cặp thuộc **ít nhất một** trong hai quan hệ
- $$R \cap S$$: cặp thuộc **cả hai**

**Ví dụ** ($$A=\{1,2\}$$, $$B=\{a,b\}$$):

- $$R=\{(1,a),(2,b)\}$$, $$S=\{(1,b),(2,b)\}$$
- $$R \cup S = \{(1,a),(1,b),(2,b)\}$$
- $$R \cap S = \{(2,b)\}$$

---

## Quan hệ Nghịch đảo

**Định nghĩa**: Với $$R \subseteq A \times B$$:

$$R^{-1} = \{(b,a) \mid (a,b) \in R\}$$

**Ví dụ**: $$R$$ = "sinh viên học môn" → $$R^{-1}$$ = "môn có sinh viên".

**Tính chất**:

- $$(R^{-1})^{-1} = R$$
- Nếu $$R$$ đối xứng thì $$R^{-1} = R$$

---

## Ví dụ: Nghịch đảo trong CSDL

$$R$$ = "sinh viên học môn":

$$R = \{(An, Toan), (Binh, Ly), (Chi, Toan)\}$$

$$R^{-1}$$ = "môn có sinh viên":

$$R^{-1} = \{(Toan, An), (Ly, Binh), (Toan, Chi)\}$$

**SQL**: `SELECT course FROM enroll WHERE student='An'`

↔ truy vấn ngược `SELECT student FROM enroll WHERE course='Toan'`.

---

## Hợp thành Quan hệ

Cho $$R \subseteq A \times B$$, $$S \subseteq B \times C$$:

$$S \circ R = \{(a,c) \mid \exists b \in B,\ (a,b) \in R \land (b,c) \in S\}$$

Đọc: **"S sau R"** — thực hiện $$R$$ trước, rồi $$S$$.

**Ví dụ**: $$R=\{(1,2),(2,3)\}$$, $$S=\{(2,4),(3,5)\}$$

$$S \circ R = \{(1,4),(2,5)\}$$

---

## Ví dụ: Hợp thành — thứ tự quan trọng

$$R=\{(1,2),(2,3)\}$$, $$S=\{(2,1),(3,3)\}$$

**Tính $$S \circ R$$** (làm $$R$$ trước, rồi $$S$$):

- $$(1,2)\in R$$, $$(2,1)\in S$$ → $$(1,1)$$
- $$(2,3)\in R$$, $$(3,3)\in S$$ → $$(2,3)$$

$$S \circ R = \{(1,1),(2,3)\}$$

**Lưu ý**: $$R \circ S = \{(2,2)\}$$ — **khác hẳn** $$S \circ R$$.

---

## Ma trận & Tích Boolean

Ma trận 0-1 của $$R$$ (hàng = đầu, cột = cuối):

$$M_R[i,j]=1 \Leftrightarrow (i,j)\in R$$

**Hợp thành** = tích Boolean:

$$M_{S\circ R}[i,j] = \bigvee_k \big(M_R[i,k] \land M_S[k,j]\big)$$

**Ví dụ** $$R: 1\to2\to3$$, $$S: 2\to4,\ 3\to5$$:

$$M_{S\circ R} = M_R \cdot M_S \Rightarrow (1,4),\ (2,5)$$

---

## Lũy thừa Quan hệ

Với quan hệ $$R$$ trên tập $$A$$:

- $$R ^ 1 = R$$
- $$R ^ {n+1} = R ^ n \circ R$$

**Ý nghĩa**: $$(a,b) \in R^{k}$$ ⟺ có đường đi độ dài $$k$$ từ $$a$$ đến $$b$$ trong đồ thị của $$R$$.

---

## Ví dụ: Lũy thừa trên chuỗi

$$R=\{(1,2),(2,3),(3,4)\}$$ trên $$\{1,2,3,4\}$$

| Lũy thừa | Cặp mới (ngoài các bậc trước) |
|:---:|:---|
| $$R^{1}$$ | $$(1,2),(2,3),(3,4)$$ |
| $$R^{2}$$ | $$(1,3),(2,4)$$ |
| $$R^{3}$$ | $$(1,4)$$ |
| $$R^{4}$$ | $$\emptyset$$ |

$$R^+ = R \cup R^{2} \cup R^{3}$$ — mọi cặp có đường đi **≥ 1** bước.

---

## Bao đóng — Khái niệm

**Bao đóng** của $$R$$ theo tính chất $$P$$ là quan hệ **nhỏ nhất** chứa $$R$$ và có tính chất $$P$$.

Ba bao đóng cơ bản:

1. **Phản xạ** (reflexive)
2. **Đối xứng** (symmetric)
3. **Bắc cầu** (transitive)

---

## Bao đóng Phản xạ & Đối xứng

**Phản xạ** — thêm mọi vòng $$(a,a)$$ còn thiếu:

$$R_{ref} = R \cup \{(a,a) \mid a \in A\}$$

**Đối xứng** — thêm chiều ngược:

$$R_{sym} = R \cup R^{-1}$$

**Ví dụ**: $$R=\{(1,2),(2,3)\}$$ trên $$\{1,2,3\}$$

- $$R_{ref}$$ thêm $$(1,1),(2,2),(3,3)$$
- $$R_{sym}$$ thêm $$(2,1),(3,2)$$

---

## Ví dụ: Ba bao đóng — cùng một $$R$$

$$R=\{(1,2),(3,1)\}$$ trên $$A=\{1,2,3\}$$

| Bao đóng | Thêm vào $$R$$ |
|:---|:---|
| Phản xạ | $$(1,1),(2,2),(3,3)$$ |
| Đối xứng | $$(2,1),(1,3)$$ |
| Bắc cầu | $$(3,2)$$ — vì $$3\to1\to2$$ |

**Kết hợp** phản xạ + đối xứng + bắc cầu → quan hệ tương đương (tiết 12).

---

## Bao đóng Bắc cầu

Thêm các cặp biểu diễn đường đi gián tiếp.

Với $$A$$ hữu hạn, $$|A| = n$$:

$$R^+ = R \cup R^{2} \cup \cdots \cup R^{n}$$

**Bao đóng phản xạ-bắc cầu**:

$$R^* = I_A \cup R^+,\quad I_A = \{(a,a) \mid a \in A\}$$

**Ví dụ**: $$R=\{(1,2),(2,3)\}$$ → $$R^+$$ thêm $$(1,3)$$.

$$R^* = I_A \cup R^+$$ thêm cả vòng phản xạ — đỉnh **đến được chính nó** (đường đi độ dài 0).

---

## Warshall — Ví dụ 3×3

$$M = \begin{bmatrix} 0&1&0 \\ 0&0&1 \\ 1&0&0 \end{bmatrix}$$
(chu trình $$1\to2\to3\to1$$)

Sau Warshall, $$M[0][2]=1$$ vì đường $$1\to2\to3$$.

**Ý nghĩa**: mọi ô $$M[i][j]=1$$ ⟺ $$j$$ đến được từ $$i$$ trong $$R^*$$.

```python
M[i][j] |= M[i][k] & M[k][j]  # cho mỗi k, i, j
```

---

## Ứng dụng: CSDL & Phân quyền

**CSDL** — "tất cả cấp dưới của quản lý A":

```sql
WITH RECURSIVE sub AS (
  SELECT id FROM emp WHERE mgr = 'A'
  UNION
  SELECT e.id FROM emp e JOIN sub s ON e.mgr = s.id
) SELECT * FROM sub;
```

↔ bao đóng bắc cầu của quan hệ "quản lý trực tiếp".

**Phân quyền**: user → role → permission; quyền hiệu lực = $$R_{role} \circ R_{perm}$$ rồi lấy $$R^*$$.

---

## Thực hành 1

Cho $$R=\{(a,b),(b,c),(c,d)\}$$ trên $$A=\{a,b,c,d\}$$.

1. Tính $$R^{-1}$$
2. Tính $$R^{2} = R \circ R$$
3. Liệt kê các cặp trong $$R^+$$

---

## Thực hành 2

Cho ma trận quan hệ trên 4 đỉnh:

$$M = \begin{bmatrix} 0&1&0&0 \\ 0&0&1&0 \\ 0&0&0&1 \\ 0&0&0&0 \end{bmatrix}$$

1. Tính $$R^*$$ (bao đóng phản xạ-bắc cầu)
2. Đỉnh nào có thể đến đỉnh 4?

---

## Thực hành 3

Trong hệ thống phân quyền:

- $$R$$ = "user A được cấp quyền trực tiếp cho role B"
- Cần biết user có quyền gián tiếp qua kế thừa role

Mô tả bằng hợp thành / bao đóng bắc cầu.

---

## Tóm tắt Tiết 13

- **Hợp/Giao**: phép toán tập trên cặp có thứ tự
- **Nghịch đảo**: đảo chiều cung
- **Hợp thành**: ghép hai bước thành một ($$S \circ R$$)
- **Bao đóng**: thêm tối thiểu cặp để đạt tính chất mong muốn
- **Warshall**: tính $$R^*$$ hiệu quả trên tập hữu hạn

---

## Liên hệ

**Điểm then chốt**: Hợp thành ≠ hợp tập — thứ tự và đỉnh trung gian quan trọng.

**Liên hệ**:
- Tiết 12: tương đương = bao đóng phản xạ-đối xứng-bắc cầu
- Tiết 15: hàm hợp tương tự hợp thành quan hệ

**Edge case**: $$R \circ S \neq S \circ R$$ (không giao hoán).

---

## Bài tập ôn tập (1/2)

1. **Bài 1**: Cho $$R=\{(1,2),(2,3)\}$$, $$S=\{(2,1),(3,3)\}$$. Tính $$R \cup S$$, $$R \cap S$$, $$S \circ R$$.

2. **Bài 2**: Tìm bao đóng phản xạ, đối xứng, bắc cầu của $$R=\{(1,2),(3,1)\}$$ trên $$\{1,2,3\}$$.

3. **Bài 3**: Với $$R$$ như bài 2, tính $$R^*$$.

---

## Bài tập ôn tập (2/2)

4. **Bài 4**: Ma trận $$M$$ 3×3 có $$M[0][1]=M[1][2]=1$$, còn lại 0. Viết code Warshall hoặc tính tay $$R^*$$.

5. **Bài 5**: Trong đồ thị module phụ thuộc, giải thích tại sao phát hiện vòng lặp phụ thuộc = kiểm tra $$(a,a) \in R^+$$ với $$a \neq$$ vòng phản xạ tầng thấp.
