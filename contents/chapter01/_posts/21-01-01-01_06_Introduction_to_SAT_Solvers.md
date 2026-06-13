---
layout: post
title: "Giới thiệu SAT Solver"
categories: chapter01
date: 2021-01-01
order: 6
required: false
lang: en
---

# Giới thiệu SAT Solver

Sau khi học về **Dạng chuẩn tắc hội (CNF)** và các **định lý về DNF/CNF**, một câu hỏi tự nhiên xuất hiện: **Làm thế nào máy tính có thể tự động kiểm tra một công thức Boolean có thỏa mãn được không?**

Câu trả lời nằm ở **SAT Solver** — một trong những công cụ quan trọng nhất của khoa học máy tính hiện đại. SAT solver không chỉ giải bài toán lý thuyết mà còn được dùng hàng ngày trong thiết kế vi mạch, kiểm chứng phần mềm, lập lịch, và trí tuệ nhân tạo.

## SAT là gì?

**Định nghĩa**: **SAT** (Boolean Satisfiability Problem) là bài toán xác định xem có tồn tại một phép gán giá trị cho các biến sao cho công thức Boolean cho kết quả đúng hay không.

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
