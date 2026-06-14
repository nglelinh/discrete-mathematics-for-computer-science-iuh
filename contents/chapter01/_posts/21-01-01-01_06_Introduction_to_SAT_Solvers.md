---
layout: post
title: "Giới thiệu SAT Solver (optional)"
categories: chapter01
date: 2021-01-01
order: 6
required: false
lang: en
---

Sau khi học về **Dạng chuẩn tắc hội (CNF)** và các **định lý về DNF/CNF**, một câu hỏi tự nhiên xuất hiện: **Làm thế nào máy tính có thể tự động kiểm tra một công thức Boolean có thỏa mãn được không?**

Câu trả lời nằm ở **SAT Solver** — một trong những công cụ quan trọng nhất của khoa học máy tính hiện đại. SAT solver không chỉ giải bài toán lý thuyết mà còn được dùng hàng ngày trong thiết kế vi mạch, kiểm chứng phần mềm, lập lịch, và trí tuệ nhân tạo.

## SAT là gì?

**Định nghĩa**: **SAT** (Boolean Satisfiability Problem) là bài toán xác định xem có tồn tại một phép gán giá trị cho các biến sao cho công thức Boolean cho kết quả đúng hay không.

![SAT problem](https://source.unsplash.com/800x600/?puzzle,solution,algorithm,computer)

*Hình 1.26: Bài toán SAT*

![Backtracking tree](https://source.unsplash.com/800x600/?tree,algorithm,structure,computer)

*Hình 1.27: Cây backtracking*

![DPLL algorithm](https://source.unsplash.com/800x600/?algorithm,flowchart,diagram)

*Hình 1.28: Thuật toán DPLL*

![CDCL solver](https://source.unsplash.com/800x600/?solver,algorithm,computer,science)

*Hình 1.29: Conflict-Driven Clause Learning*

![Sudoku solver](https://source.unsplash.com/800x600/?sudoku,puzzle,game,logic)

*Hình 1.30: Giải Sudoku bằng SAT solver*

**Ví dụ đơn giản**:

Cho biểu thức:

$$
(x \lor y) \land (\neg x \lor z)
$$

SAT solver sẽ tìm xem có cách gán `x, y, z` sao cho biểu thức đúng không.

**Ví dụ nghiệm**:

- $$ x = \text{FALSE} $$
- $$ y = \text{TRUE} $$
- $$ z = \text{FALSE} $$

Khi đó:

- $$ x \lor y = \text{FALSE} \lor \text{TRUE} = \text{TRUE} $$
- $$ \neg x \lor z = \text{TRUE} \lor \text{FALSE} = \text{TRUE} $$

Toàn bộ biểu thức:

$$
\text{TRUE} \land \text{TRUE} = \text{TRUE}
$$

⇒ SAT solver kết luận: **SAT** (thỏa mãn được).

### Nếu không có nghiệm thì sao?

Xét biểu thức:

$$
x \land \neg x
$$

Không có cách nào để `x` vừa đúng vừa sai. Biểu thức này **luôn sai** bất kể `x` là gì.

SAT solver sẽ trả lời: **UNSAT** (không thỏa mãn được).

---

### Minh họa trực quan: Không gian tìm kiếm

Với 3 biến, có \(2^3 = 8\) assignment có thể. SAT solver phải tìm xem có assignment nào làm CNF đúng không.

```python
# Minh họa không gian tìm kiếm
assignments = []
for p in [True, False]:
    for q in [True, False]:
        for r in [True, False]:
            assignments.append((p, q, r))
print(f"Tổng số assignment: {len(assignments)}")  # 8
```

Khi số biến tăng lên 100, không gian tìm kiếm là \(2^{100} \approx 10^{30}\). Không thể vét cạn. Cần thuật toán thông minh.

## Tại sao cần SAT solver?

Nghe có vẻ chỉ là bài toán logic, nhưng rất nhiều vấn đề thực tế có thể chuyển thành SAT.

### 1. Kiểm chứng chip (Hardware Verification)

Các công ty như Intel, AMD, NVIDIA dùng SAT solver để kiểm tra:

> "Thiết kế chip có trường hợp nào hoạt động sai không?"

Nếu SAT tìm được nghiệm → có bug.

### 2. Kiểm chứng phần mềm

Kiểm tra:

> "Có đường thực thi nào làm chương trình crash không?"

Nhiều công cụ phân tích tĩnh hiện đại dựa trên SAT/SMT.

### 3. Lập lịch

Ví dụ: 100 nhân viên, 30 ca làm, hàng trăm ràng buộc về thời gian và kỹ năng.

SAT solver tìm lịch thỏa mãn tất cả điều kiện.

### 4. Giải Sudoku

Sudoku có thể chuyển thành hàng nghìn mệnh đề CNF. Nếu SAT tìm được nghiệm → Sudoku có lời giải.

## Tại sao CNF là dạng lý tưởng cho SAT Solver?

Nhớ lại bài 01_04: mọi hàm Boolean đều có thể đưa về **CNF đầy đủ**. Điều này quan trọng vì:

1. **CNF = danh sách ràng buộc**: Mỗi clause là một điều kiện phải thỏa mãn.
2. **Dễ phát hiện mâu thuẫn**: Nếu có clause `(p)` và `(\neg p)` thì chắc chắn không thỏa mãn.
3. **Unit propagation**: Nếu clause chỉ còn 1 literal, ta buộc phải gán giá trị cho literal đó.

### Minh họa: CNF dưới góc nhìn "ràng buộc"

```python
# CNF: (p ∨ q) ∧ (¬p ∨ r) ∧ (q ∨ ¬r)
# Mỗi clause là một ràng buộc phải đúng

def check_clause(clause, assignment):
    """Kiểm tra một clause có đúng với assignment không"""
    for literal in clause:
        var = abs(literal)
        val = assignment[var]
        if literal > 0 and val:      # positive literal
            return True
        if literal < 0 and not val:  # negative literal
            return True
    return False  # clause bị vi phạm
```

## Các thuật toán SAT Solver cơ bản

### 1. Backtracking (thuật toán naïf)

Ý tưởng đơn giản: thử gán giá trị cho từng biến, nếu vi phạm ràng buộc thì quay lui.

```python
def sat_backtracking(clauses, vars, assignment):
    if not vars:  # đã gán hết biến
        return all(check_clause(c, assignment) for c in clauses)

    var = vars[0]
    for val in [True, False]:
        assignment[var] = val
        if sat_backtracking(clauses, vars[1:], assignment):
            return True
        # quay lui
        del assignment[var]
    return False
```

**Nhược điểm**: Rất chậm khi có nhiều biến (thời gian có thể tăng theo cấp số mũ).

### 2. DPLL (Davis–Putnam–Logemann–Loveland)

DPLL cải tiến backtracking bằng hai kỹ thuật then chốt:

1. **Unit Propagation**: Nếu clause chỉ còn 1 literal chưa gán, buộc phải gán giá trị cho literal đó.
2. **Pure Literal Elimination**: Nếu một biến chỉ xuất hiện dưới một dạng (chỉ dương hoặc chỉ âm), ta có thể gán giá trị an toàn.

### 3. CDCL (Conflict-Driven Clause Learning) – hiện đại nhất

CDCL là thuật toán được dùng trong hầu hết SAT solver công nghiệp hiện nay (MiniSat, Glucose, Z3, CaDiCaL...).

**Ý tưởng chính**:
- Khi gặp mâu thuẫn (conflict), solver **học** một clause mới (conflict clause) để tránh lặp lại sai lầm tương tự trong tương lai.
- Kết hợp với **backjumping** (quay lui thông minh).

## Có thể hình dung SAT solver như thế nào?

Nếu biểu thức Boolean là một **mê cung** của các điều kiện, thì SAT solver là một người dò đường cực kỳ thông minh, biết học từ các ngõ cụt để không bao giờ đi lặp lại sai lầm cũ.

Đó là lý do SAT solver trở thành một trong những công cụ nền tảng của thiết kế chip, kiểm chứng phần mềm và tối ưu hóa hiện đại.

## Đầu vào và đầu ra của SAT solver

**Đầu vào** thường ở dạng CNF:

```text
(p ∨ q) ∧ (¬p ∨ r) ∧ (q ∨ ¬r)
```

**Đầu ra**:

- `SAT` + một nghiệm (ví dụ: `p=FALSE, q=TRUE, r=FALSE`)
- hoặc `UNSAT` nếu không tồn tại nghiệm.

## Các SAT solver nổi tiếng

- **MiniSat** – nhỏ gọn, dùng nhiều trong nghiên cứu
- **Glucose** – cải tiến từ MiniSat
- **CaDiCaL** – hiệu năng cao
- **Z3** (Microsoft Research) – mở rộng SAT thành SMT, hỗ trợ số nguyên, mảng, bit-vector

## Tóm tắt

- **SAT** là bài toán kiểm tra sự thỏa mãn của công thức Boolean.
- **CNF** là dạng lý tưởng vì dễ biểu diễn ràng buộc.
- Các thuật toán chính: **Backtracking → DPLL → CDCL**.
- SAT solver được dùng rộng rãi trong **verification**, **scheduling**, **AI planning**, và **hardware design**.

Bài học này khép lại chuỗi kiến thức về **logic mệnh đề** và mở ra cánh cửa đến một trong những công cụ mạnh mẽ nhất của khoa học máy tính hiện đại.

---

## Bài tập thực hành

### Bài tập 1: Mã hóa bài toán đơn giản thành SAT

Cho công thức:

$$
(p \lor q) \land (\neg p \lor r) \land (\neg q \lor \neg r)
$$

1. Viết hàm Python kiểm tra tất cả 8 assignment.
2. Có bao nhiêu assignment thỏa mãn?

### Bài tập 2: Hiểu Unit Propagation

Xét CNF:

$$
(p) \land (\neg p \lor q) \land (r \lor s)
$$

Áp dụng unit propagation. Biến nào bị gán giá trị? Clause nào còn lại?

### Bài tập 3: Nghiên cứu

Tìm hiểu một SAT solver mã nguồn mở (MiniSat, Glucose, hoặc Z3) và thử giải một bài Sudoku 9×9 được mã hóa thành CNF.

### Bài tập 4: Chuyển bài toán thành SAT

Một cửa hàng có 3 loại đồ uống: Cà phê (C), Trà (T), Nước ngọt (N). Luật:
- Khách hàng phải chọn ít nhất một loại.
- Nếu chọn Cà phê thì không được chọn Nước ngọt.
- Hoặc chọn Trà hoặc chọn Nước ngọt (không thể thiếu cả hai).

(a) Viết các ràng buộc dưới dạng công thức logic.
(b) Chuyển công thức sang CNF.
(c) Có bao nhiêu assignment thỏa mãn?

<details>
<summary>Đáp án</summary>

(a) Ký hiệu: $$c$$: "chọn Cà phê", $$t$$: "chọn Trà", $$n$$: "chọn Nước ngọt"
    - "Ít nhất một": $$c \lor t \lor n$$
    - "Cà phê → không Nước ngọt": $$c \to \neg n \equiv \neg c \lor \neg n$$
    - "Trà hoặc Nước ngọt": $$t \lor n$$

(b) Chuyển sang CNF — cả ba đều đã là clause (tuyển của các literal):
    $$(c \lor t \lor n) \land (\neg c \lor \neg n) \land (t \lor n)$$

(c) Liệt kê tất cả 8 assignment, kiểm tra từng cái:

| c | t | n | (c∨t∨n) | (¬c∨¬n) | (t∨n) | Kết quả |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| F | F | F | F | T | F | UNSAT |
| F | F | T | T | T | T | SAT |
| F | T | F | T | T | T | SAT |
| F | T | T | T | T | T | SAT |
| T | F | F | T | T | F | UNSAT |
| T | F | T | T | F | T | UNSAT |
| T | T | F | T | T | T | SAT |
| T | T | T | T | F | T | UNSAT |

Có **4** assignment thỏa mãn.

</details>

### Bài tập 5: Mã hóa bài toán lập lịch thành SAT

Ba người A, B, C cần xếp lịch trực. Mỗi người trực một buổi (sáng hoặc chiều). Ràng buộc:
- Mỗi buổi có đúng một người trực.
- A không thể trực sáng.
- Nếu B trực sáng thì C trực chiều.

(a) Đặt biến logic phù hợp và viết các ràng buộc.
(b) Chuyển sang CNF.
(c) Dùng phương pháp brute force (liệt kê) để tìm tất cả lịch hợp lệ.

<details>
<summary>Đáp án</summary>

(a) Đặt biến:
    - $$A_s$$: "A trực sáng", $$A_c$$: "A trực chiều"
    - $$B_s$$: "B trực sáng", $$B_c$$: "B trực chiều"
    - $$C_s$$: "C trực sáng", $$C_c$$: "C trực chiều"
    
    Ràng buộc:
    1. Mỗi người trực đúng một buổi: 
       $$(A_s \oplus A_c) \land (B_s \oplus B_c) \land (C_s \oplus C_c)$$
    2. Mỗi buổi có đúng một người:
       $$(A_s \oplus B_s \oplus C_s) \land (A_c \oplus B_c \oplus C_c)$$
       (mỗi buổi có đúng 1 người trực — nghĩa là ít nhất một và không quá một)
    3. A không trực sáng: $$\neg A_s$$
    4. Nếu B trực sáng thì C trực chiều: $$B_s \to C_c \equiv \neg B_s \lor C_c$$

(b) CNF (chuyển XOR thành các clause):
    - Từ $$A_s \oplus A_c$$: $$(A_s \lor A_c) \land (\neg A_s \lor \neg A_c)$$
    - Tương tự cho B, C
    - Từ "mỗi buổi có đúng một người" cho buổi sáng (As, Bs, Cs):
      Ít nhất một: $$(A_s \lor B_s \lor C_s)$$
      Không quá một: $$(\neg A_s \lor \neg B_s) \land (\neg A_s \lor \neg C_s) \land (\neg B_s \lor \neg C_s)$$
    - Tương tự cho buổi chiều
    - $$\neg A_s$$
    - $$\neg B_s \lor C_c$$

(c) Vì $$\neg A_s$$, A chỉ có thể $$A_c$$. Từ $$A_s \oplus A_c$$ → $$A_c = T$$.
    Buổi chiều đã có A, nên $$B_c = F$$ và $$C_c = F$$.
    Từ $$B_s \oplus B_c$$ và $$B_c = F$$ → $$B_s = T$$.
    Từ $$C_s \oplus C_c$$ và $$C_c = F$$ → $$C_s = T$$.
    Kiểm tra buổi sáng: $$A_s = F, B_s = T, C_s = T$$ → có 2 người trực sáng, vi phạm "mỗi buổi đúng một người"!
    Vậy **không có lịch hợp lệ** (UNSAT).

</details>

### Bài tập 6: Hiểu thuật toán DPLL qua ví dụ

Cho CNF:
$$(p \lor q) \land (\neg p \lor r) \land (\neg q \lor \neg r) \land (q \lor \neg r)$$

Mô phỏng thuật toán DPLL từng bước:
(a) Chọn một biến để phân nhánh (split).
(b) Áp dụng unit propagation.
(c) Kết luận SAT hay UNSAT?

<details>
<summary>Đáp án</summary>

(a) Chọn p để phân nhánh.

**Nhánh p = T**:
- Clause 1: $$(T \lor q) = T$$ (loại bỏ)
- Clause 2: $$(\neg T \lor r) = (F \lor r) = r$$ → unit clause, suy ra r = T
- Với r = T:
  - Clause 3: $$(\neg q \lor \neg T) = (\neg q \lor F) = \neg q$$ → unit clause, suy ra q = F
  - Clause 4: $$(q \lor \neg T) = (q \lor F) = q$$ → unit clause, suy ra q = T
- Xung đột: q vừa phải là F (từ clause 3) vừa phải là T (từ clause 4)!
→ Nhánh p = T là **conflict**.

**Nhánh p = F**:
- Clause 1: $$(F \lor q) = q$$ → unit clause, suy ra q = T
- Clause 2: $$(\neg F \lor r) = (T \lor r) = T$$ (loại bỏ)
- Clause 3: $$(\neg T \lor \neg r) = (F \lor \neg r) = \neg r$$ → unit clause, suy ra r = F
- Clause 4: $$(T \lor \neg F) = (T \lor T) = T$$ (loại bỏ)
- Không còn clause nào → SAT!

Nghiệm: p = F, q = T, r = F.

</details>

### Bài tập 7: Mã hóa bài toán 8 quân hậu (đơn giản hóa) thành SAT

Xét bàn cờ 3×3, cần đặt 3 quân xe (rook) sao cho không quân nào ăn được quân nào (mỗi hàng và mỗi cột có đúng một quân).

Đặt biến $$x_{ij}$$ với ý nghĩa "có quân xe ở ô (hàng i, cột j)".

(a) Viết ràng buộc "mỗi hàng có ít nhất một quân".
(b) Viết ràng buộc "mỗi hàng có không quá một quân".
(c) Viết ràng buộc "mỗi cột có ít nhất một quân".
(d) Viết ràng buộc "mỗi cột có không quá một quân".
(e) Tổng số clause là bao nhiêu?

<details>
<summary>Đáp án</summary>

(a) Mỗi hàng có ít nhất một quân:
    - Hàng 1: $$x_{11} \lor x_{12} \lor x_{13}$$
    - Hàng 2: $$x_{21} \lor x_{22} \lor x_{23}$$
    - Hàng 3: $$x_{31} \lor x_{32} \lor x_{33}$$

(b) Mỗi hàng có không quá một quân (với mỗi cặp cột khác nhau):
    - Hàng 1: $$(\neg x_{11} \lor \neg x_{12}) \land (\neg x_{11} \lor \neg x_{13}) \land (\neg x_{12} \lor \neg x_{13})$$
    - Hàng 2: $$(\neg x_{21} \lor \neg x_{22}) \land (\neg x_{21} \lor \neg x_{23}) \land (\neg x_{22} \lor \neg x_{23})$$
    - Hàng 3: $$(\neg x_{31} \lor \neg x_{32}) \land (\neg x_{31} \lor \neg x_{33}) \land (\neg x_{32} \lor \neg x_{33})$$

(c) Mỗi cột có ít nhất một quân:
    - Cột 1: $$x_{11} \lor x_{21} \lor x_{31}$$
    - Cột 2: $$x_{12} \lor x_{22} \lor x_{32}$$
    - Cột 3: $$x_{13} \lor x_{23} \lor x_{33}$$

(d) Mỗi cột có không quá một quân:
    - Cột 1: $$(\neg x_{11} \lor \neg x_{21}) \land (\neg x_{11} \lor \neg x_{31}) \land (\neg x_{21} \lor \neg x_{31})$$
    - Cột 2: $$(\neg x_{12} \lor \neg x_{22}) \land (\neg x_{12} \lor \neg x_{32}) \land (\neg x_{22} \lor \neg x_{32})$$
    - Cột 3: $$(\neg x_{13} \lor \neg x_{23}) \land (\neg x_{13} \lor \neg x_{33}) \land (\neg x_{23} \lor \neg x_{33})$$

(e) Đếm:
    - "Ít nhất một" cho hàng: 3 clause
    - "Không quá một" cho hàng: 3 × 3 = 9 clause
    - "Ít nhất một" cho cột: 3 clause
    - "Không quá một" cho cột: 3 × 3 = 9 clause
    - Tổng: 3 + 9 + 3 + 9 = **24 clause**
    
    Với bài toán 8 quân hậu thực tế (8×8), số clause là:
    - 8 (mỗi hàng có quân) + 8 (mỗi cột có quân)
    - $$8 \times \binom{8}{2} = 8 \times 28 = 224$$ (không quá một quân mỗi hàng)
    - $$8 \times \binom{8}{2} = 224$$ (không quá một quân mỗi cột)
    - Tổng: 8 + 8 + 224 + 224 = **464 clause**

</details>

### Bài tập 8: Tại sao 3-SAT là NP-đầy đủ?

(a) Tại sao bài toán 2-SAT (mỗi clause có đúng 2 literal) có thể giải trong thời gian đa thức?
(b) Tại sao 3-SAT lại khó hơn?
(c) Nếu bạn có một SAT solver chạy được cho 3-SAT với 1000 biến, bạn có thể dùng nó để giải các bài toán NP-khác không?

<details>
<summary>Đáp án</summary>

(a) **2-SAT** có thể giải trong thời gian $$O(n^2)$$ bằng cách xây dựng đồ thị implication và kiểm tra đồ thị có cycle chứa cả p và ¬p không (strongly connected components). Nếu không có cycle như vậy, bài toán là SAT.
    
    Cách xây dựng: mỗi clause $$(a \lor b)$$ tương đương với $$(\neg a \to b) \land (\neg b \to a)$$. Ta tạo đỉnh cho mỗi literal và cạnh implication. Sau đó dùng thuật toán Kosaraju hoặc Tarjan để tìm SCC.

(b) **3-SAT** là NP-đầy đủ vì:
    - Nó nằm trong NP (có thể kiểm tra nghiệm trong thời gian đa thức).
    - Mọi bài toán trong NP đều có thể quy dẫn về 3-SAT trong thời gian đa thức (định lý Cook-Levin).
    - Với 3 literal mỗi clause, số tổ hợp gán trị để thử là $$2^{3} = 8$$ mỗi clause, và ta không thể xây dựng đồ thị implication đơn giản như 2-SAT.

(c) **Có** — Vì 3-SAT là NP-đầy đủ, mọi bài toán NP đều có thể quy dẫn về 3-SAT trong thời gian đa thức. Nếu có SAT solver hiệu quả cho 1000 biến, ta có thể:
    - Giải bài toán người bán hàng (TSP)
    - Tô màu đồ thị
    - Xếp lịch tối ưu
    - Các bài toán tối ưu tổ hợp khác
    
    Đây là lý do SAT solver được gọi là "cỗ máy NP" — một SAT solver nhanh có thể giải hầu hết các bài toán NP-khó trong thực tế.

</details>
