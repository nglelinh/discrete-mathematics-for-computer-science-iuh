---
layout: post
title: "Ghi chú mở rộng: Bộ giải SMT và logic vị từ (2022–2026)"
categories: chapter02
date: 2021-01-01
order: 5
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. cvc5 (TACAS 2022) and industrial SMT show how quantifiers and theories implement the predicate logic of this chapter. Does not replace the theory lessons."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite quantifiers, inference rules, or the existing programming/database lesson.

Bài ghi chú ứng dụng song ngữ. **Không** thay thế các bài học về lượng từ, quy tắc suy diễn hay logic vị từ trong lập trình và cơ sở dữ liệu.

</div>

## English

Predicate logic adds structure inside a proposition: predicates, domains, and $$\forall$$ / $$\exists$$. **SMT** (satisfiability modulo theories) is the industrial form of that idea — SAT on a Boolean skeleton, plus dedicated solvers for integers, bit-vectors, arrays, and uninterpreted functions.

Barbosa et al., “cvc5: A Versatile and Industrial-Strength SMT Solver,” *TACAS 2022*, LNCS 13243, pp. 415–442, [DOI 10.1007/978-3-030-99524-9_24](https://doi.org/10.1007/978-3-030-99524-9_24) ([PDF](https://cvc5.github.io/papers/2022/BarbosaBBKLMMMN-TACAS22.pdf)), describe cvc5 as the successor of CVC4. They evaluate it on the full SMT-LIB corpus and compare against CVC4 and Z3. The solver produces proofs, handles nonlinear arithmetic, and instantiates quantifiers — exactly the nested-quantifier difficulty from Section 2.2, now as an automated procedure.

A typical verification query is still a predicate-logic sentence, for example

<div class="textbook-equation" markdown="1">
$$
\forall i.\; (0 \le i < n) \rightarrow (a[i] \ge 0).
$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>

cvc5 does not change the meaning of $$\forall$$. It decides fragments where the combination of CNF reasoning and theory lemmas is complete enough for compilers, smart contracts, and program verifiers. Read this after the required quantifier lessons; it is an optional map from $$\forall$$/$$\exists$$ to a 2022-era production solver.

**Citations**

1. H. Barbosa et al., “cvc5: A Versatile and Industrial-Strength SMT Solver,” TACAS 2022, LNCS 13243, pp. 415–442. [DOI](https://doi.org/10.1007/978-3-030-99524-9_24)

**Questions.** (1) Which part of an SMT query is propositional SAT, and which part is a theory? (2) Why is quantifier instantiation incomplete for some fragments you can still write in this chapter?

### Background Knowledge Map: How SMT Solvers Turn Predicate Logic Into Automated Software Verification

Traditional testing checks a handful of concrete inputs (`x = 0, 5, -1`) and hopes no hidden bug lurks at `x = 2_147_483_647`. **SMT (Satisfiability Modulo Theories)** solvers—such as Z3 and cvc5—bridge Chapter 2's predicate logic directly into production software verification across three pillars:

1. **Boolean SAT Core + Theory Solvers (DPLL(T))**:
   An SMT solver pairs a fast SAT engine (handling logical connectives $$\land, \lor, \neg$$) with specialized decision procedures for mathematical theories: linear integer/real arithmetic ($$\mathbb{Z}, \mathbb{R}$$), fixed-width **bitvectors** (32-bit/64-bit wraparound arithmetic), arrays, and strings.
2. **Negate-and-Check Verification (Proving by Finding Counterexamples)**:
   To prove a safety property $$P(x)$$ holds for **all** inputs ($$\forall x\, P(x)$$), the solver asks whether its negation $$\exists x\, \neg P(x)$$ is satisfiable. `UNSAT` is a mathematical proof that no bug exists; `SAT` hands you the exact crashing input!
3. **Industrial Impact**:
   AWS uses SMT (Zelkova & Cedar) to verify millions of IAM access policies every second, while Rust/C verification tools (Kani, CBMC) translate code paths into bitvector SMT queries to catch integer overflows and out-of-bounds memory accesses before deployment.

### Deep-Dive Explanation: Catching a Classic 32-Bit Binary-Search Overflow With an SMT Query (Read Slowly)

For nearly 20 years, Java's standard library binary search computed the midpoint as `mid = (low + high) / 2`—and silently overflowed on arrays larger than $$2^{30}$$ elements! Watch how an SMT solver catches this in milliseconds on signed 32-bit bitvectors (`i32`, max value $$2^{31} - 1 = 2{,}147{,}483{,}647$$):

- **Precondition**: $$0 \le \text{low} \le \text{high} \le 2{,}147{,}483{,}647$$.
- **Safety property we want**: $$\text{low} + \text{high}$$ does not wrap negative (i.e. $$\text{mid} \ge 0$$).
- **Negated SMT query ($$\exists$$ bug)**: Ask Z3 for `low, high: BitVec(32)` satisfying `0 <= low <= high` AND `(low + high) / 2 < 0`.
- **Solver output (`SAT` — Concrete Counterexample)**:
  $$\text{low} = 1{,}073{,}741{,}824 \; (2^{30}), \qquad \text{high} = 1{,}073{,}741{,}824 \; (2^{30}).$$
  In 32-bit two's complement, $$2^{30} + 2^{30} = 2^{31} \equiv \mathbf{-2{,}147{,}483{,}648}$$ (`0x8000_0000`), so `mid = -1_073_741_824` → instant array-index crash!
- **Verified fix**: Rewrite `mid = low + (high - low) / 2` and re-run the exact same negated query → Z3 returns **`UNSAT`**, proving mathematically that the fix never overflows for **all** $$2^{62}$$ valid `(low, high)` pairs!

## Tiếng Việt

Logic vị từ bổ sung cấu trúc bên trong mỗi mệnh đề thông qua vị từ, miền xác định và các lượng từ $$\forall$$, $$\exists$$. **SMT** (Satisfiability Modulo Theories) là dạng ứng dụng công nghiệp của cùng ý tưởng đó: giải SAT trên phần khung Boolean kết hợp với các bộ giải chuyên biệt cho số nguyên, bit-vector, mảng và hàm không diễn giải.

Barbosa và cộng sự (TACAS 2022) giới thiệu **cvc5** (phiên bản kế nhiệm của CVC4), đánh giá trên toàn bộ bộ chuẩn SMT-LIB và so sánh với CVC4 cũng như Z3. Bộ giải này có khả năng xuất chứng minh, xử lý số học phi tuyến và tự động cụ thể hóa lượng từ (quantifier instantiation) — biến thách thức về lượng từ lồng nhau ở Mục 2.2 thành một thủ tục tự động.

Một truy vấn kiểm chứng điển hình vẫn là một công thức logic vị từ, chẳng hạn $$\forall i.\; (0 \le i < n) \rightarrow (a[i] \ge 0)$$. Bộ giải cvc5 không thay đổi ngữ nghĩa của $$\forall$$; thay vào đó, nó giải quyết các phân mảnh (fragment) mà sự kết hợp giữa suy luận CNF và bổ đề lý thuyết đủ mạnh cho trình biên dịch, hợp đồng thông minh và công cụ kiểm chứng chương trình. Sinh viên nên đọc ghi chú này sau khi hoàn thành các mục bắt buộc về lượng từ.

**Câu hỏi.** (1) Trong một truy vấn SMT, phần nào thuộc bài toán SAT mệnh đề và phần nào thuộc các lý thuyết nền? (2) Vì sao quá trình cụ thể hóa lượng từ không đầy đủ trên một số phân mảnh logic mà giáo trình vẫn viết được?

### Bản đồ kiến thức nền: SMT Solver biến Logic Vị từ thành vũ khí kiểm chứng phần mềm như thế nào?

Kiểm thử thông thường chỉ thử được vài chục đầu vào cụ thể và cầu mong không có lỗi ẩn ở biên. **SMT (Satisfiability Modulo Theories)**—với các bộ giải như Z3 và cvc5—kết hợp Logic Vị từ Chương 2 với các lý thuyết toán học chuyên biệt trên ba trụ cột:

1. **Lõi SAT + Các bộ giải lý thuyết (Kiến trúc DPLL(T))**:
   SAT xử lý cấu trúc logic ($$\land, \lor, \neg$$), còn các bộ giải lý thuyết xử lý số học nguyên/thực, **vector bit (bitvectors)** mô phỏng chính xác tràn số 32/64-bit, mảng và chuỗi ký tự.
2. **Chiến lược Phủ định để Chứng minh ($$\forall x\, P(x) \iff \text{UNSAT}(\neg P(x))$$ )**:
   Để chứng minh chương trình an toàn với *mọi* đầu vào, ta hỏi bộ giải xem có tồn tại đầu vào nào làm vi phạm an toàn ($$\neg P(x)$$) không. Trả về `UNSAT` nghĩa là đã chứng minh tuyệt đối; trả về `SAT` sẽ in ra đúng đầu vào gây lỗi!
3. **Ứng dụng thực tiễn quy mô lớn**:
   AWS dùng SMT (Zelkova/Cedar) để chứng minh chính sách phân quyền IAM không bao giờ hở quyền công khai, còn các công cụ như Kani/CBMC kiểm chứng mã Rust/C chống tràn số và truy cập ngoài biên mảng.

### Khung giải thích (nên đọc chậm): Bắt lỗi tràn số `i32` trong tìm kiếm nhị phân bằng một câu truy vấn SMT

Công thức trung điểm quen thuộc `mid = (low + high) / 2` từng gây lỗi ẩn suốt gần 20 năm trên kiểu số nguyên có dấu 32-bit (`i32`, giá trị tối đa $$2^{31} - 1 = 2.147.483.647$$):
- **Truy vấn phủ định gửi Z3**: Tìm `low, high` thỏa $$0 \le \text{low} \le \text{high}$$ nhưng `(low + high) / 2 < 0`.
- **Z3 trả về `SAT` cùng phản ví dụ cụ thể**: $$\text{low} = 2^{30} = 1.073.741.824$$, $$\text{high} = 2^{30} = 1.073.741.824$$. Khi cộng trong 32-bit bù 2: $$2^{30} + 2^{30} = 2^{31} \equiv \mathbf{-2.147.483.648}$$ → `mid = -1.073.741.824` (vượt ngoài biên mảng!).
- **Bản sửa chuẩn**: Đổi sang `mid = low + (high - low) / 2` rồi hỏi lại đúng truy vấn phủ định đó → Z3 trả về **`UNSAT`**, chứng minh tuyệt đối không bao giờ tràn số trên toàn bộ $$2^{62}$$ cặp đầu vào hợp lệ!

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=CNQwSXKBGgw">From z3 to cvc5</a> — cvc solver, tiếng Anh. Giới thiệu quá trình phát triển trong cùng họ bộ giải từ Z3 đến cvc5 được nhắc trong bài.
- <a href="https://www.youtube.com/watch?v=EacYNe7moSs">Z3 Explained - Satisfiability Modulo Theories &amp; SMT Solvers</a> — Guided Hacking, tiếng Anh. Giải thích SMT như sự kết hợp giữa SAT và các lý thuyết, gắn với khung logic vị từ của chương.
- <a href="https://www.youtube.com/watch?v=e07bWJ2L9VY">cvc5 pythonic API</a> — cvc solver, tiếng Anh. Minh họa cách gọi lượng từ trong mã nguồn qua API Python của cvc5.
