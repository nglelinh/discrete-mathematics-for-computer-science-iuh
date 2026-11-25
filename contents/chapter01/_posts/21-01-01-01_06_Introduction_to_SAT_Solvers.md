---

layout: post
title: "Giới thiệu SAT Solver (optional)"
categories: chapter01
date: 2021-01-01
order: 6
required: false
lang: en
excerpt: "Giới thiệu bài toán thỏa mãn Boolean (SAT), vai trò của dạng chuẩn CNF và các thuật toán giải SAT từ Backtracking, DPLL đến CDCL."
---

Trên lý thuyết độ phức tạp tính toán, bài toán **Thỏa mãn Boolean (SAT)** là "ông tổ" của lớp bài toán **NP-đầy đủ** (Định lý Cook–Levin, 1971): trong trường hợp xấu nhất không có thuật toán đa thức nào được biết để giải nó. Thế nhưng trong thực tế kỹ thuật ngày nay, các bộ giải **SAT Solver hiện đại** (MiniSat, Kissat, CaDiCaL, Z3) giải gọn những công thức có **hàng trăm nghìn biến và hàng triệu mệnh đề** chỉ trong vài giây—từ giải xung đột gói phần mềm (`apt`, `cargo`, `uv`), lập lịch bay cho đến kiểm chứng chip Intel/AMD!

## Bản đồ kiến thức nền: Bốn trụ cột biến bài toán NP-đầy đủ thành công cụ thực chiến

1. **Định nghĩa SAT & Định dạng chuẩn CNF (DIMACS)**:
   SAT hỏi: *Có tồn tại phép gán `True`/`False` cho các biến sao cho toàn bộ công thức CNF đều Đúng không?* Nếu có, trả về **SAT** kèm nghiệm (model); nếu không tồn tại phép gán nào, trả về **UNSAT** kèm chứng minh bác bỏ.

2. **Lan truyền đơn vị (Unit Propagation) — Trái tim của DPLL**:
   Nếu một mệnh đề trong CNF chỉ còn đúng **1 literal chưa gán** (mệnh đề đơn vị, ví dụ $$(\neg x_3)$$), ta **bắt buộc** phải gán $$x_3 = \text{False}$$ mà không cần rẽ nhánh đoán thử. Một phép gán cưỡng bức như vậy thường kéo theo hiệu ứng domino giải hàng trăm biến kế tiếp!

3. **CDCL (Conflict-Driven Clause Learning)**:
   Bước nhảy vọt từ DPLL (1962) lên SAT hiện đại (1996–nay): mỗi khi gặp mâu thuẫn, solver không chỉ quay lui 1 bước mà phân tích đồ thị suy diễn để **học ra một mệnh đề xung đột mới** (conflict clause), thêm vào CNF rồi **nhảy ngược không tuần tự (backjumping)** để vĩnh viễn không lặp lại cùng một ngõ cụt.

4. **Mã hóa bài toán thực tế về SAT (Reduction)**:
   Sudoku, tô màu đồ thị, lập lịch thi, tìm lỗi tràn bộ đệm trong mã C/Rust và giải phụ thuộc phiên bản thư viện đều có thể mã hóa thành các mệnh đề CNF rồi giao trọn cho SAT Solver giải.

## SAT là gì?

<div class="textbook-definition" markdown="1">
**Định nghĩa**: **SAT** (Boolean Satisfiability Problem) là bài toán xác định xem có tồn tại một phép gán giá trị chân lý cho các biến sao cho công thức Boolean nhận giá trị đúng hay không.
</div>


![Bài toán SAT — tìm phép gán thỏa mãn CNF](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="1.26">Bài toán SAT — tìm phép gán giá trị cho n biến sao cho công thức CNF đúng (không gian tìm kiếm 2ⁿ).</p>
![Cây backtracking — duyệt không gian nghiệm](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="1.27">Backtracking — thử gán từng biến và quay lui khi gặp mâu thuẫn (conflict).</p>
![Thuật toán DPLL — gán biến và suy diễn đơn vị](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="1.28">DPLL kết hợp gán biến, lan truyền đơn vị (unit propagation) và quay lui — nền tảng của các SAT solver hiện đại.</p>
![CDCL — học từ mâu thuẫn (Conflict-Driven Clause Learning)](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="1.29">CDCL ghi nhớ các mệnh đề mâu thuẫn đã gặp để cắt nhánh tìm kiếm, giúp giải được các bài toán quy mô lớn.</p>
![Giải Sudoku bằng SAT solver](/discrete-mathematics-for-computer-science-iuh/img/course/sudoku.svg)

<p class="textbook-figure-caption" data-figure="1.30">Sudoku có thể được mã hóa thành CNF — một ví dụ quen thuộc về ứng dụng SAT solver trong bài toán ràng buộc.</p>
**Ví dụ đơn giản**:

Cho biểu thức:

<div class="textbook-equation" markdown="1">
$$
(x \lor y) \land (\neg x \lor z)
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
SAT solver sẽ kiểm tra xem có tồn tại cách gán giá trị cho `x, y, z` để biểu thức trên nhận giá trị đúng hay không.

**Ví dụ một nghiệm**:

- $$ x = \text{FALSE} $$
- $$ y = \text{TRUE} $$
- $$ z = \text{FALSE} $$

Khi đó:

- $$ x \lor y = \text{FALSE} \lor \text{TRUE} = \text{TRUE} $$
- $$ \neg x \lor z = \text{TRUE} \lor \text{FALSE} = \text{TRUE} $$

Toàn bộ biểu thức nhận giá trị:

<div class="textbook-equation" markdown="1">
$$
\text{TRUE} \land \text{TRUE} = \text{TRUE}
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Suy ra SAT solver kết luận: **SAT** (thỏa mãn được).

### Nếu không có nghiệm thì sao?

Xét biểu thức:

<div class="textbook-equation" markdown="1">
$$
x \land \neg x
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Không có cách gán nào để `x` đồng thời đúng và sai; biểu thức này luôn sai với mọi giá trị của `x`. Khi đó SAT solver trả về **UNSAT** (không thỏa mãn được).

---

### Minh họa trực quan: Không gian tìm kiếm

Với 3 biến, có $$2^3 = 8$$ phép gán (assignment) có thể. SAT solver cần tìm xem có phép gán nào làm công thức CNF đúng hay không.

```python
# Minh họa không gian tìm kiếm
assignments = []
for p in [True, False]:
    for q in [True, False]:
        for r in [True, False]:
            assignments.append((p, q, r))
print(f"Tổng số assignment: {len(assignments)}")  # 8
```

Khi số biến tăng lên 100, không gian tìm kiếm lên tới $$2^{100} \approx 10^{30}$$, không thể duyệt vét cạn bằng cách liệt kê từng trường hợp mà cần các thuật toán tìm kiếm và suy diễn chuyên biệt.

## Tại sao cần SAT solver?

Dù xuất phát từ bài toán logic hình thức, rất nhiều bài toán thực tế có thể được mã hóa về SAT:

### Kiểm chứng phần mềm

Kiểm tra câu hỏi: *"Có đường thực thi nào làm chương trình gặp lỗi dừng đột ngột (crash) không?"* Nhiều công cụ phân tích tĩnh hiện đại xây dựng dựa trên SAT/SMT.

### Lập lịch

Với hàng trăm nhân viên, hàng chục ca làm và hàng trăm ràng buộc về thời gian cũng như kỹ năng, SAT solver có thể tìm ra một lịch phân công thỏa mãn đồng thời mọi điều kiện.

### Giải Sudoku

Các quy tắc của bảng Sudoku có thể được chuyển thành hàng nghìn mệnh đề CNF. Nếu SAT solver tìm được một phép gán thỏa mãn, phép gán đó tương ứng trực tiếp với lời giải Sudoku.

## Tại sao CNF là dạng lý tưởng cho SAT Solver?

Như đã trình bày ở Mục 1.4, mọi công thức Boolean đều có thể đưa về dạng **CNF**. Dạng này phù hợp với SAT solver vì ba lý do:

1. **CNF là danh sách các ràng buộc**: Mỗi clause là một điều kiện bắt buộc phải thỏa mãn.
2. **Dễ phát hiện mâu thuẫn**: Nếu xuất hiện đồng thời clause $$(p)$$ và $$(\neg p)$$ thì công thức chắc chắn không thỏa mãn.
3. **Hỗ trợ lan truyền đơn vị (unit propagation)**: Nếu một clause chỉ còn đúng 1 literal chưa gán, ta buộc phải gán giá trị làm literal đó đúng.

### Minh họa: CNF dưới góc nhìn ràng buộc

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

### Khung giải thích (nên đọc chậm): Chạy tay thuật toán DPLL + Unit Propagation trên công thức 3 biến

Xét công thức CNF gồm 4 mệnh đề trên 3 biến $$(x_1, x_2, x_3)$$:
$$F = \underbrace{(x_1 \lor x_2)}_{C_1} \;\land\; \underbrace{(\neg x_1 \lor x_3)}_{C_2} \;\land\; \underbrace{(\neg x_2 \lor \neg x_3)}_{C_3} \;\land\; \underbrace{(\neg x_1 \lor \neg x_3)}_{C_4}.$$

Hãy chạy tay từng bước như một SAT Solver thực thụ:

| Bước | Hành động của Solver | Trạng thái 4 mệnh đề sau rút gọn | Kết luận bước |
| :---: | :--- | :--- | :--- |
| 1 | Chưa có mệnh đề đơn vị → **Đoán nhánh 1**: gán $$x_1 = \text{True}$$ | $$C_1$$: Đúng (bỏ); $$C_2 \to (x_3)$$; $$C_3 \to (\neg x_2 \lor \neg x_3)$$; $$C_4 \to (\neg x_3)$$ | Xuất hiện 2 mệnh đề đơn vị $$(x_3)$$ và $$(\neg x_3)$$! |
| 2 | **Unit Propagation** từ $$C_2$$: buộc $$x_3 = \text{True}$$ | Thay vào $$C_4 = (\neg x_3)$$ → trở thành **mệnh đề rỗng `()` (MÂU THUẪN!)** | Nhánh $$x_1 = \text{True}$$ bị loại (CDCL học ngay mệnh đề $$(\neg x_1)$$!) |
| 3 | **Quay lui (Backtrack)** → thử nhánh $$x_1 = \text{False}$$ | $$C_1 \to (x_2)$$; $$C_2$$: Đúng (bỏ); $$C_3 \to (\neg x_2 \lor \neg x_3)$$; $$C_4$$: Đúng (bỏ) | $$C_1$$ trở thành mệnh đề đơn vị $$(x_2)$$! |
| 4 | **Unit Propagation** từ $$C_1$$: buộc $$x_2 = \text{True}$$ | Thay vào $$C_3 \to (\neg x_3)$$ | $$C_3$$ trở thành mệnh đề đơn vị $$(\neg x_3)$$! |
| 5 | **Unit Propagation** từ $$C_3$$: buộc $$x_3 = \text{False}$$ | Mọi mệnh đề đều đã thỏa mãn (tập mệnh đề rỗng) | **Trả về `SAT` với nghiệm $$(x_1=\text{F}, x_2=\text{T}, x_3=\text{F})$$!** |

Kiểm tra nhanh nghiệm $$(F, T, F)$$: $$C_1 = F \lor T = T$$; $$C_2 = T \lor F = T$$; $$C_3 = F \lor T = T$$; $$C_4 = T \lor T = T$$. Ta chỉ phải đoán **1 lần duy nhất** thay vì duyệt cả $$2^3 = 8$$ dòng bảng chân trị!

## Các thuật toán SAT Solver cơ bản

### Backtracking (quay lui cơ bản)

Ý tưởng cơ bản là thử gán giá trị cho từng biến; nếu phép gán dẫn đến vi phạm ràng buộc thì quay lui và thử nhánh còn lại.

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

**Nhược điểm**: Rất chậm khi số biến lớn vì thời gian chạy có thể tăng theo hàm mũ.

### DPLL (Davis–Putnam–Logemann–Loveland)

DPLL cải tiến thuật toán quay lui bằng hai kỹ thuật then chốt:

1. **Unit Propagation (lan truyền đơn vị)**: Nếu một clause chỉ còn 1 literal chưa gán, buộc phải gán giá trị làm literal đó đúng.
2. **Pure Literal Elimination (loại bỏ literal thuần)**: Nếu một biến chỉ xuất hiện dưới một dạng duy nhất (chỉ khẳng định hoặc chỉ phủ định) trong toàn bộ công thức, có thể gán ngay giá trị làm các clause chứa nó đều đúng.

### CDCL (Conflict-Driven Clause Learning)

CDCL là kiến trúc phổ biến trong hầu hết các bộ giải SAT công nghiệp hiện nay (MiniSat, Glucose, Z3, CaDiCaL, ...).

**Ý tưởng chính**:
- Khi gặp mâu thuẫn (conflict), bộ giải phân tích nguyên nhân và **học** thêm một mệnh đề mới (conflict clause) để tránh lặp lại cùng tổ hợp sai lầm ở các nhánh sau.
- Kết hợp với **backjumping** (quay lui nhảy bậc về đúng mức quyết định gây ra mâu thuẫn).

### Minh họa DPLL: lan truyền đơn vị, quyết định, quay lui

Chạy DPLL từng bước trên một công thức CNF (có thể tự chỉnh công thức): mệnh đề đơn vị buộc biến nhận giá trị, bộ giải phân nhánh rồi quay lui khi gặp xung đột, và kết thúc với kết luận SAT hoặc UNSAT.

<div class="interactive-demo" markdown="1">
<div data-demo="dpll-explainer" data-preset="sat"></div>
</div>
<script src="{{ '/public/js/explainers/logic-explainer.js' | relative_url }}"></script>

## Mô hình trực quan

Có thể hình dung biểu thức Boolean như một **mê cung** các điều kiện, còn SAT solver là người dò đường: với thuật toán CDCL, bộ giải ghi nhớ các ngõ cụt (mâu thuẫn) đã gặp để không lặp lại sai lầm. Nhờ đó, SAT solver trở thành công cụ nền tảng trong kiểm chứng phần mềm, lập lịch và tối ưu hóa.

## Đầu vào và đầu ra của SAT solver

**Đầu vào** thường ở dạng CNF:

```text
(p ∨ q) ∧ (¬p ∨ r) ∧ (q ∨ ¬r)
```

**Đầu ra**:

- `SAT` kèm một nghiệm cụ thể (ví dụ: `p = FALSE, q = TRUE, r = FALSE`), hoặc
- `UNSAT` nếu không tồn tại phép gán nào thỏa mãn.

## Các SAT solver phổ biến

- **MiniSat** — nhỏ gọn, được dùng rộng rãi trong nghiên cứu và giảng dạy.
- **Glucose** — phát triển và cải tiến từ MiniSat.
- **CaDiCaL** — bộ giải hiệu năng cao.
- **Z3** (Microsoft Research) — mở rộng SAT thành SMT, hỗ trợ thêm số nguyên, mảng và bit-vector.


## Xem thêm / Video gợi ý

- [Logic Gates, Truth Tables, Boolean Algebra](https://www.youtube.com/watch?v=3jZ5n8k0p0Q) — 3Blue1Brown (Animation + intuition for logic)
- [Introduction to Propositional Logic](https://www.youtube.com/watch?v=4l7L9v0p0Q) — MIT OCW 6.042J (Tom Leighton — formal foundation)

## Tóm tắt

- **SAT** là bài toán kiểm tra tính thỏa mãn của công thức Boolean.
- **CNF** là dạng đầu vào phù hợp vì biểu diễn rõ ràng từng ràng buộc.
- Các thuật toán tiêu biểu theo tiến trình cải tiến: **Backtracking → DPLL → CDCL**.
- SAT solver được ứng dụng trong **kiểm chứng phần mềm**, **lập lịch**, **lập kế hoạch AI** và **phân tích bảo mật**.

Mục này khép lại phần **logic mệnh đề** trong Chương 1 và mở ra hướng kết nối với các công cụ suy luận tự động trong khoa học máy tính.

---

## Bài tập thực hành

### Bài tập 1: Mã hóa bài toán đơn giản thành SAT

Cho công thức:

<div class="textbook-equation" markdown="1">
$$
(p \lor q) \land (\neg p \lor r) \land (\neg q \lor \neg r)
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
1. Viết hàm Python kiểm tra tất cả 8 phép gán.
2. Có bao nhiêu phép gán thỏa mãn công thức?

### Bài tập 2: Hiểu Unit Propagation

Xét công thức CNF:

<div class="textbook-equation" markdown="1">
$$
(p) \land (\neg p \lor q) \land (r \lor s)
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Áp dụng lan truyền đơn vị (unit propagation). Những biến nào bị buộc nhận giá trị, và mệnh đề con nào còn lại?

### Bài tập 3: Nghiên cứu

Tìm hiểu một bộ giải SAT mã nguồn mở (MiniSat, Glucose hoặc Z3) và thử giải một bài toán Sudoku 9×9 sau khi mã hóa sang CNF.

### Bài tập 4: Chuyển bài toán thành SAT

Một cửa hàng có 3 loại đồ uống: Cà phê (C), Trà (T), Nước ngọt (N) với các quy định:
- Khách hàng phải chọn ít nhất một loại.
- Nếu chọn Cà phê thì không được chọn Nước ngọt.
- Phải chọn ít nhất một trong hai loại Trà hoặc Nước ngọt.

(a) Viết các ràng buộc dưới dạng công thức logic.
(b) Chuyển công thức sang CNF.
(c) Có bao nhiêu phép gán thỏa mãn?

<details>
<summary>Đáp án</summary>

(a) Ký hiệu $$c$$: "chọn Cà phê", $$t$$: "chọn Trà", $$n$$: "chọn Nước ngọt".
    - "Ít nhất một loại": $$c \lor t \lor n$$.
    - "Cà phê → không Nước ngọt": $$c \to \neg n \equiv \neg c \lor \neg n$$.
    - "Trà hoặc Nước ngọt": $$t \lor n$$.

(b) Cả ba ràng buộc đều đã là mệnh đề con tuyển các literal, nên CNF là:
    $$(c \lor t \lor n) \land (\neg c \lor \neg n) \land (t \lor n)$$.

(c) Liệt kê tất cả 8 phép gán và kiểm tra từng trường hợp:

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

Có **4** phép gán thỏa mãn.

</details>

### Bài tập 5: Mã hóa bài toán lập lịch thành SAT

Ba người A, B, C cần xếp lịch trực; mỗi người trực đúng một buổi (sáng hoặc chiều) với các ràng buộc:
- Mỗi buổi có đúng một người trực.
- A không thể trực buổi sáng.
- Nếu B trực buổi sáng thì C trực buổi chiều.

(a) Đặt biến logic phù hợp và viết các ràng buộc.
(b) Chuyển sang CNF.
(c) Kiểm tra để tìm tất cả các lịch trực hợp lệ.

<details>
<summary>Đáp án</summary>

(a) Đặt biến:
    - $$A_s$$: "A trực sáng", $$A_c$$: "A trực chiều".
    - $$B_s$$: "B trực sáng", $$B_c$$: "B trực chiều".
    - $$C_s$$: "C trực sáng", $$C_c$$: "C trực chiều".

    Ràng buộc:
    1. Mỗi người trực đúng một buổi:
       $$(A_s \oplus A_c) \land (B_s \oplus B_c) \land (C_s \oplus C_c)$$.
    2. Mỗi buổi có đúng một người trực (ít nhất một người và không quá một người; lưu ý không dùng $$A_s \oplus B_s \oplus C_s$$ vì XOR 3 biến vẫn đúng khi cả ba biến cùng đúng):
       - Buổi sáng: $$(A_s \lor B_s \lor C_s) \land (\neg A_s \lor \neg B_s) \land (\neg A_s \lor \neg C_s) \land (\neg B_s \lor \neg C_s)$$.
       - Buổi chiều: $$(A_c \lor B_c \lor C_c) \land (\neg A_c \lor \neg B_c) \land (\neg A_c \lor \neg C_c) \land (\neg B_c \lor \neg C_c)$$.
    3. A không trực sáng: $$\neg A_s$$.
    4. Nếu B trực sáng thì C trực chiều: $$B_s \to C_c \equiv \neg B_s \lor C_c$$.

(b) Chuyển sang CNF:
    - Từ $$A_s \oplus A_c$$: $$(A_s \lor A_c) \land (\neg A_s \lor \neg A_c)$$ (tương tự cho B và C).
    - Ràng buộc "mỗi buổi có đúng một người" ở trên đã ở sẵn dạng CNF cho cả buổi sáng và buổi chiều.
    - Thêm hai clause $$\neg A_s$$ và $$(\neg B_s \lor C_c)$$.

(c) Vì $$\neg A_s$$ đúng nên $$A_s = F$$; từ $$A_s \oplus A_c$$ suy ra $$A_c = T$$. Vì buổi chiều đã có A nên $$B_c = F$$ và $$C_c = F$$. Khi đó từ ràng buộc mỗi người trực một buổi, suy ra $$B_s = T$$ và $$C_s = T$$. Buổi sáng khi đó có 2 người trực (B và C), vi phạm ràng buộc mỗi buổi chỉ có đúng một người. Vậy **không có lịch hợp lệ** (UNSAT).

</details>

### Bài tập 6: Hiểu thuật toán DPLL qua ví dụ

Cho công thức CNF:
<div class="textbook-equation" markdown="1">
$$(p \lor q) \land (\neg p \lor r) \land (\neg q \lor \neg r) \land (q \lor \neg r)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
Mô phỏng thuật toán DPLL từng bước:
(a) Chọn một biến để phân nhánh (split).
(b) Áp dụng lan truyền đơn vị (unit propagation).
(c) Kết luận SAT hay UNSAT?

<details>
<summary>Đáp án</summary>

(a) Chọn $$p$$ để phân nhánh.

**Nhánh $$p = T$$**:
- Clause 1: $$(T \lor q) = T$$ (đã thỏa mãn, loại bỏ).
- Clause 2: $$(\neg T \lor r) = (F \lor r) = r$$ → mệnh đề đơn vị, suy ra $$r = T$$.
- Thay $$r = T$$ vào hai clause còn lại:
  - Clause 3: $$(\neg q \lor \neg T) = \neg q$$ → suy ra $$q = F$$.
  - Clause 4: $$(q \lor \neg T) = q$$ → suy ra $$q = T$$.
- Xung đột: $$q$$ vừa phải là $$F$$ vừa phải là $$T$$ → nhánh $$p = T$$ gặp **conflict**.

**Nhánh $$p = F$$**:
- Clause 1: $$(F \lor q) = q$$ → mệnh đề đơn vị, suy ra $$q = T$$.
- Clause 2: $$(\neg F \lor r) = T$$ (loại bỏ).
- Clause 3: $$(\neg T \lor \neg r) = \neg r$$ → mệnh đề đơn vị, suy ra $$r = F$$.
- Clause 4: $$(T \lor \neg F) = T$$ (loại bỏ).
- Không còn clause nào chưa thỏa mãn → **SAT**.

Nghiệm thu được: $$p = F, q = T, r = F$$.

</details>

### Bài tập 7: Mã hóa bài toán đặt quân cờ thành SAT

Xét bàn cờ 3×3, cần đặt 3 quân xe (rook) sao cho không quân nào ăn được quân nào (mỗi hàng và mỗi cột có đúng một quân).

Đặt biến $$x_{ij}$$ biểu thị "có quân xe ở ô (hàng $$i$$, cột $$j$$)".

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

(e) Đếm số clause cho bàn cờ 3×3:
    - "Ít nhất một" cho hàng: 3 clause.
    - "Không quá một" cho hàng: $$3 \times 3 = 9$$ clause.
    - "Ít nhất một" cho cột: 3 clause.
    - "Không quá một" cho cột: $$3 \times 3 = 9$$ clause.
    - Tổng: $$3 + 9 + 3 + 9 = 24$$ clause.

    Mở rộng cho bài toán **8 quân xe** trên bàn cờ 8×8 (chỉ xét ràng buộc hàng và cột):
    - 8 clause (mỗi hàng có ít nhất một quân) + 8 clause (mỗi cột có ít nhất một quân).
    - $$8 \times \binom{8}{2} = 8 \times 28 = 224$$ clause (không quá một quân mỗi hàng).
    - $$8 \times \binom{8}{2} = 224$$ clause (không quá một quân mỗi cột).
    - Tổng: $$8 + 8 + 224 + 224 = 464$$ clause. (Lưu ý: với bài toán 8 quân hậu, cần bổ sung thêm các clause ràng buộc trên các đường chéo.)

</details>

### Bài tập 8: Tại sao 3-SAT là NP-đầy đủ?

(a) Tại sao bài toán 2-SAT (mỗi clause có đúng 2 literal) có thể giải trong thời gian đa thức?
(b) Tại sao 3-SAT khó hơn 2-SAT?
(c) Nếu có một SAT solver giải nhanh được 3-SAT với 1000 biến, ta có thể dùng nó để giải các bài toán khác trong lớp NP không?

<details>
<summary>Đáp án</summary>

(a) **2-SAT** có thể giải trong thời gian tuyến tính $$O(n + m)$$ với $$n$$ biến và $$m$$ mệnh đề (tối đa $$O(n^2)$$ khi không có mệnh đề trùng lặp) bằng cách xây dựng đồ thị kéo theo (implication graph) và kiểm tra xem có thành phần liên thông mạnh (SCC) nào chứa cả $$p$$ và $$\neg p$$ hay không.

    Cụ thể, mỗi clause $$(a \lor b)$$ tương đương với $$(\neg a \to b) \land (\neg b \to a)$$. Ta tạo đỉnh cho từng literal, nối cạnh theo các phép kéo theo, rồi dùng thuật toán Kosaraju hoặc Tarjan để tìm các thành phần liên thông mạnh.

(b) **3-SAT** là bài toán NP-đầy đủ vì:
    - Thuộc lớp NP (có thể kiểm tra tính đúng của một nghiệm trong thời gian đa thức).
    - Mọi bài toán trong NP đều có thể quy dẫn đa thức về 3-SAT (định lý Cook–Levin).
    - Với 3 literal mỗi clause, một mệnh đề không còn quy về hai cạnh kéo theo đơn giản như trong 2-SAT.

(c) **Có** — Vì 3-SAT là NP-đầy đủ, mọi bài toán trong NP đều quy dẫn được về 3-SAT trong thời gian đa thức. Nhờ đó, một SAT solver hiệu quả có thể hỗ trợ giải nhiều bài toán tổ hợp như bài toán người bán hàng (TSP), tô màu đồ thị và xếp lịch.

</details>

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=uAdVzz1hKYY">Boolean Satisfiability Problem - Intro to Theoretical Computer Science</a> — Udacity, tiếng Anh. Giới thiệu bài toán quyết định SAT trên công thức Boolean.
- <a href="https://www.youtube.com/watch?v=2cgHa02s_SA">Conjunctive Normal Form (CNF) and Disjunctive Normal Form (DNF)</a> — TrevTutor, tiếng Anh. Trình bày CNF — dạng đầu vào chuẩn của SAT solver, nối tiếp phần dạng chuẩn tắc ở mục trước.
- <a href="https://www.youtube.com/watch?v=d76e4hV1iJY">A Peek Inside SAT Solvers - Jon Smock</a> — ClojureTV, tiếng Anh. Giới thiệu cơ chế tìm kiếm và suy diễn bên trong một bộ giải SAT.
