---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## SAT Solver & Ứng dụng

**Toán Rời Rạc**

Tiết 43 (45 phút) — Boolean Satisfiability, DPLL, Verification

---

## Mục tiêu tiết học

- Định nghĩa bài toán SAT (Boolean Satisfiability)
- Hiểu dạng CNF và vai trò trong SAT solver
- Nắm ý tưởng thuật toán DPLL
- Liên hệ SAT với kiểm thử và kiểm chứng phần mềm
- Nhận biết SAT thuộc lớp NP (giới thiệu)

---

## SAT là gì?

**SAT** (Boolean Satisfiability): Cho công thức Boolean, tồn tại phép gán giá trị cho các biến sao cho công thức **đúng** (TRUE) không?

**Đầu ra**:
- **SAT** + một nghiệm (assignment)
- **UNSAT** — không có nghiệm

**Ví dụ**:

$$(x \lor y) \land (\neg x \lor z)$$

Nghiệm: $$x = F, y = T, z = F$$ → cả hai clause đều TRUE.

---

## CNF — Dạng chuẩn cho SAT

**CNF** (Conjunctive Normal Form): Tích (AND) của các **clause** (tổng OR).

$$(p \lor q \lor \neg r) \land (\neg p \lor r) \land (q)$$

Mỗi clause = một **ràng buộc** phải thỏa.

**Tại sao CNF?**
1. Dễ biểu diễn ràng buộc
2. Dễ phát hiện mâu thuẫn
3. Đầu vào chuẩn của mọi SAT solver

**Liên hệ tiết 4–5**: DNF/CNF, quy tắc suy luận, Resolution.

---

## Ví dụ SAT / UNSAT

**SAT**:
$$(p \lor q) \land (\neg p \lor r)$$
→ $$p=F, q=T, r=F$$ ✓

**UNSAT**:
$$p \land \neg p$$
→ Không có assignment nào thỏa → luôn FALSE.

**Không gian tìm kiếm**: $$n$$ biến → $$2^{n}$$ assignment. Với $$n=100$$: $$2^{100} \approx 10^{30}$$ — không thể brute-force.

---

## Tại sao SAT quan trọng?

Nhiều bài toán thực tế **mã hóa thành SAT**:

| Lĩnh vực | Ví dụ |
|:---|:---|
| **Kiểm chứng** | Có bug nào làm crash không? |
| **Lập lịch** | Xếp ca làm thỏa ràng buộc |
| **Giải đố** | Sudoku, N-Queens |
| **Thiết kế mạch** | Mạch Boolean có đúng spec? |
| **Bảo mật** | Phân tích dependency |

**SAT solver** = công cụ giải ràng buộc logic ở quy mô công nghiệp.

---

## Backtracking — Ý tưởng cơ bản

```
SAT-Backtrack(clauses, vars, assignment):
    IF vars rỗng:
        RETURN mọi clause đều TRUE?
    var ← vars[0]
    FOR val IN {TRUE, FALSE}:
        assignment[var] ← val
        IF không có clause nào bị vi phạm:
            IF SAT-Backtrack(..., vars[1:], assignment):
                RETURN TRUE
        XÓA assignment[var]   // quay lui
    RETURN FALSE
```

**Nhược điểm**: Chậm — $$O(2^{n})$$ worst-case.

---

## DPLL — Cải tiến Backtracking

**DPLL** (Davis–Putnam–Logemann–Loveland):

1. **Unit Propagation**: Clause chỉ còn 1 literal chưa gán → **buộc** gán giá trị
2. **Pure Literal Elimination**: Biến chỉ xuất hiện dạng dương (hoặc chỉ âm) → gán an toàn
3. **Split**: Chọn biến, thử TRUE/FALSE
4. **Backtrack**: Khi conflict → quay lui

**Ví dụ Unit Propagation**:

$$(p) \land (\neg p \lor q) \land (r \lor s)$$

→ $$p = T$$ (bắt buộc) → $$q = T$$ (bắt buộc) → còn $$(r \lor s)$$.

---

## CDCL — SAT solver hiện đại

**CDCL** (Conflict-Driven Clause Learning):

- Khi gặp **conflict**, học clause mới để tránh lặp sai lầm
- **Backjumping**: Quay lui thông minh (không chỉ 1 bước)
- Dùng trong MiniSat, Glucose, CaDiCaL, **Z3** (Microsoft)

**Z3/SMT**: Mở rộng SAT — thêm số nguyên, mảng, bit-vector.

**Kết quả**: Giải được hàng **triệu** biến trong thực tế (không phải mọi instance).

---

## SAT ↔ Kiểm thử phần mềm

**Câu hỏi kiểm chứng**: "Có input nào làm `balance < 0` sau giao dịch không?"

**Mã hóa**:
- Biến Boolean: điều kiện nhánh, giá trị bit
- Ràng buộc: logic chương trình + spec
- SAT solver tìm **counterexample** (input gây lỗi)

**Equivalence partitioning** (tiết 12): Chia input thành lớp — SAT tìm input **trong lớp** vi phạm spec.

**Formal verification**: Coq, Dafny, TLA+ — chứng minh đúng cho mọi input.

---

## SAT ↔ Boolean & Mạch logic

**Tiết 30–35**: Đại số Boolean, Karnaugh, Quine-McCluskey.

**Mạch logic**: Spec = hàm Boolean → kiểm tra mạch có đúng?

```
Spec: F(a,b,c) = (a∧b)∨(¬a∧c)
Mạch:  G(a,b,c) = ...
CNF:   (F ↔ G) có nghiệm? → mạch SAI
       (F ↔ G) UNSAT?     → mạch ĐÚNG
```

**SAT solver** thay thế duyệt $$2^{n}$$ tổ hợp đầu vào.

---

## Mã hóa bài toán thành SAT

**Sudoku 9×9**: ~729 biến, hàng nghìn clause.

**Lập lịch 3 người**: Biến $$A_s, B_s, C_s, ...$$ + ràng buộc XOR, implication.

**Quy trình**:
1. Đặt biến logic cho quyết định
2. Viết ràng buộc dạng logic
3. Chuyển sang CNF
4. Gọi SAT solver → SAT/UNSAT + nghiệm

---

## Thực hành 1

Cho CNF: $$(p \lor q) \land (\neg p \lor r) \land (\neg q \lor \neg r)$$

1. Liệt kê 8 assignment ($$p, q, r$$)
2. Tìm assignment thỏa mãn (hoặc chứng minh UNSAT)
3. Có bao nhiêu nghiệm?

---

## Thực hành 2

CNF: $$(p) \land (\neg p \lor q) \land (r \lor s)$$

Áp dụng **unit propagation** từng bước:

1. Clause nào là unit clause?
2. Gán biến nào? Giá trị gì?
3. Clause còn lại sau propagation?

---

## Thực hành 3

Cửa hàng: C (Cà phê), T (Trà), N (Nước ngọt).

- Chọn ít nhất một: $$c \lor t \lor n$$
- Cà phê → không Nước ngọt: $$\neg c \lor \neg n$$
- Trà hoặc Nước ngọt: $$t \lor n$$

1. Viết CNF (đã là CNF)
2. Tìm một nghiệm hợp lệ
3. Có bao nhiêu nghiệm? (đếm hoặc liệt kê)

---

## Tóm tắt Tiết 43

- **SAT**: tồn tại assignment làm CNF đúng?
- **CNF**: tích các clause — đầu vào chuẩn
- **DPLL**: unit propagation + split + backtrack
- **CDCL/Z3**: SAT solver công nghiệp
- Ứng dụng: verification, scheduling, Sudoku, mạch logic

---

## Liên hệ

**Độ khó**: SAT NP-complete; 2-SAT giải được $$O(n^{2})$$; 3-SAT NP-hard.

**Edge case**: CNF rỗng = SAT; clause rỗng = UNSAT.

**Liên hệ**: Logic (tiết 2–5) ↔ Boolean (tiết 30–35) ↔ SAT (tiết 43) ↔ P/NP (tiết 39, 45).

---

## Bài tập ôn tập (1/2)

1. **Cơ bản**: Phân biệt kết quả SAT và UNSAT. Cho ví dụ mỗi loại.

2. **CNF**: Chuyển $$(p \to q) \land (q \to r)$$ sang CNF.

3. **Unit propagation**: $$(x) \land (\neg x \lor y) \land (\neg y \lor z)$$ — gán biến nào?

---

## Bài tập ôn tập (2/2)

4. **Ứng dụng**: Nêu 2 lý do SAT solver hữu ích trong kiểm thử phần mềm.

5. **Bài 5**: Mã hóa bài toán: "Đặt 2 quân trên hàng/cột 2×2, không cùng hàng, không cùng cột." Đặt biến, viết ít nhất 4 clause CNF.
