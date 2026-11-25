---
layout: post
title: "Ghi chú mở rộng: Bộ giải SAT trong thiết kế mạch Boolean (2022–2026)"
categories: chapter13
date: 2021-01-01
order: 8
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. Kissat/CaDiCaL (SAT 2024, CAV 2024 lineage) are the solvers that modern EDA and Boolean equivalence checking actually call. Does not replace Boolean algebra."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite K-maps, Quine–McCluskey, or the chip-history lesson.

Bài ghi chú ứng dụng song ngữ, **không** viết lại nội dung bản đồ Karnaugh, Quine–McCluskey hay bài từ Boole đến chip hiện đại.

</div>

## English

Karnaugh maps stop at a handful of variables. Industrial logic synthesis and **combinational equivalence checking** encode “are these two Boolean functions equal?” as SAT/UNSAT on a miter circuit — the same algebra as this chapter, a different search engine.

In 2024 that engine, on the public competition track, was Kissat 4.0: three main-track golds at SAT Competition 2024 ([medals](https://cca.informatik.uni-freiburg.de/sat24medals/); Biere, Faller, Fazekas, Fleury, Froleyks, Pollitt, Univ. Helsinki B-2024-1, pp. 8–10). The same group’s CaDiCaL 2.0 line (highlighted in that description; CAV 2024 system paper) emphasises incremental SAT, proof production, and interpolation — the features EDA tools need when they call a solver millions of times.

Optional reading order: Boolean algebra and gates first; this note second. You should be able to say, without new theory, why XOR-of-two-outputs $$= 0$$ is a SAT instance and why an UNSAT **proof** is what a chip team wants.

**Citations**

1. A. Biere et al., “CaDiCaL, Gimsatul, IsaSAT and Kissat Entering the SAT Competition 2024,” SAT Competition 2024, Univ. Helsinki B-2024-1, pp. 8–10. [PDF](https://cca.informatik.uni-freiburg.de/papers/BiereFallerFazekasFleuryFroleyksPollitt-SAT-Competition-2024-solvers.pdf)

**Questions.** (1) Write the miter SAT query for “$$f \equiv g$$” using XOR and a single output. (2) Why is a checked UNSAT proof closer to Chapter 13 than a neural “probably equivalent”?

### Background Knowledge Map: SAT Solvers & Formal Equivalence Checking
- **Boolean Satisfiability (SAT):** Given a Boolean formula in CNF (Conjunctive Normal Form), decide whether there exists an assignment making it `TRUE`. Although SAT is the prototypical **NP-complete** problem, modern **CDCL (Conflict-Driven Clause Learning)** solvers routinely solve formulas with millions of variables!
- **Tseitin Transformation & Miter Circuits:** Any combinational circuit $$C$$ converts in linear time into a CNF formula. To prove two circuits $$C_1, C_2$$ are 100% equivalent, wire their outputs into an **XOR gate** (a *Miter* circuit) and ask a SAT solver if `Miter = 1` is satisfiable: **UNSAT = mathematical proof of 100% equivalence!**

### Deep-Dive Explanation: From a Miter XOR Gate to a Formal Proof (Read Slowly)
1. **Step 1 (Build the Miter):** Connect identical inputs $$x$$ to both original circuit $$C_1$$ and optimized circuit $$C_2$$, and feed their outputs into $$M(x) = C_1(x) \oplus C_2(x)$$.
2. **Step 2 (Tseitin CNF encoding):** Translate every gate (e.g., $$z = x \land y$$ becomes $$(\bar{x} \lor \bar{y} \lor z) \land (x \lor \bar{z}) \land (y \lor \bar{z})$$) into linear-size clauses.
3. **Step 3 (CDCL Search):** The SAT solver searches for a counterexample input $$x^*$$ where $$M(x^*) = 1$$, learning conflict clauses to prune huge subtrees.
4. **Step 4 (Verdict):** `SAT` yields an exact bug input $$x^*$$ where $$C_1(x^*) \neq C_2(x^*)$$; `UNSAT` (with a checkable DRAT proof) certifies 100% hardware equivalence!

## Tiếng Việt

Bản đồ Karnaugh chỉ thuận tiện với vài biến. Trong tổng hợp logic công nghiệp và **kiểm tra tương đương mạch tổ hợp** (*combinational equivalence checking*), câu hỏi “hai hàm Boole có bằng nhau trên mọi đầu vào không?” được mã hóa thành bài toán SAT/UNSAT trên mạch miter — vẫn dựa trên đại số Boole của chương này nhưng sử dụng bộ giải tìm kiếm chuyên dụng.

Năm 2024, ở hạng mục công khai, bộ giải tiêu biểu là Kissat 4.0 với ba huy chương vàng ở nhánh chính của SAT Competition 2024. Dòng bộ giải CaDiCaL 2.0 của cùng nhóm tác giả (trình bày trong báo cáo cuộc thi và bài báo hệ thống CAV 2024) tập trung vào giải SAT gia tăng (*incremental SAT*), xuất chứng minh kiểm chứng được và nội suy (*interpolation*) — đúng các tính năng mà công cụ tự động hóa thiết kế điện tử (EDA) cần khi gọi bộ giải hàng triệu lần.

Thứ tự học khuyến nghị là nắm vững đại số Boole và cổng logic trước rồi đọc ghi chú này. Không cần thêm lý thuyết mới, bạn vẫn có thể giải thích vì sao kiểm tra XOR của hai ngõ ra luôn bằng $$0$$ quy về bài toán SAT, và vì sao một **chứng minh UNSAT** được kiểm chứng lại là điều đội ngũ thiết kế chip cần.

**Câu hỏi.** (1) Viết truy vấn SAT trên mạch miter để kiểm tra “$$f \equiv g$$” bằng cổng XOR và một ngõ ra duy nhất. (2) Vì sao một chứng minh UNSAT được kiểm chứng hình thức gần với tinh thần Chương 13 hơn một dự đoán kiểu “mô hình nơ-ron cho rằng hai mạch có lẽ tương đương”?

### Bản đồ kiến thức nền: Bộ giải SAT & Kiểm chứng Tương đương Mạch
- **Bài toán SAT (Boolean Satisfiability):** Kiểm tra xem một công thức Boole dạng CNF (tích các tổng) có nghiệm làm biểu thức bằng `1` không. Tuy SAT là bài toán **NP-đầy đủ**, các bộ giải hiện đại (CDCL — học mệnh đề xung đột) vẫn xử lý mượt mà mạch hàng triệu biến!
- **Mạch Miter & Biến đổi Tseitin:** Nối đầu ra của mạch gốc $$C_1$$ và mạch sau tối ưu $$C_2$$ vào một cổng **XOR** ($$M = C_1 \oplus C_2$$) rồi đưa vào bộ giải SAT: nếu kết quả là **UNSAT** (vô nghiệm), ta có một **chứng minh toán học 100%** rằng hai mạch giống hệt nhau trên cả $$2^n$$ đầu vào!

### Ví dụ tính tay cầm tay chỉ việc: Mã hóa Tseitin cho một cổng AND $$z = x \land y$$
Điều kiện $$z \leftrightarrow (x \land y)$$ tương đương với hai chiều kéo theo $$(x \land y \to z) \land (z \to x \land y)$$, viết ngay thành **3 mệnh đề CNF**:
$$
(\bar{x} + \bar{y} + z)\cdot(x + \bar{z})\cdot(y + \bar{z}) = 1.
$$
Kiểm tra bằng tay: nếu $$x = 1, y = 1$$, mệnh đề đầu ép $$z = 1$$; nếu $$x = 0$$, mệnh đề thứ hai ép $$z = 0$$! Không hề bị bùng nổ số lượng mệnh đề theo hàm mũ như cách khai triển SOP/POS thông thường!

### Khung giải thích: Quy trình 4 bước dùng SAT chứng minh mạch chip không có lỗi (nên đọc chậm)
#### Bước 1: Ghép mạch gốc $$C_1$$ và mạch tối ưu $$C_2$$ qua cổng XOR (mạch Miter)
Mục tiêu là đi tìm một đầu vào phản ví dụ $$x^*$$ sao cho $$C_1(x^*) \neq C_2(x^*)$$ (tức $$M(x^*) = 1$$).
#### Bước 2: Mã hóa mạch thành CNF tuyến tính bằng Biến đổi Tseitin
Mỗi cổng chỉ tốn 3–4 mệnh đề CNF bằng cách đặt thêm 1 biến phụ cho đầu ra của cổng đó.
#### Bước 3: Chạy bộ giải CDCL kèm chứng chỉ chứng minh (DRAT)
Mỗi lần gán thử gặp mâu thuẫn, bộ giải phân tích nguyên nhân gốc và lưu thêm một mệnh đề học được để không bao giờ lặp lại nhánh sai đó.
#### Bước 4: Đọc phán quyết SAT / UNSAT
`SAT` chỉ đích danh vector đầu vào gây bug; `UNSAT` đóng dấu kiểm định tương đương tuyệt đối trước khi đưa chip đi sản xuất!

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=uAdVzz1hKYY">Boolean Satisfiability Problem - Intro to Theoretical Computer Science</a> — Udacity, tiếng Anh. Giới thiệu bài toán SAT, nền tảng của kiểm tra tương đương mạch trong công cụ EDA.
- <a href="https://www.youtube.com/watch?v=YUqR-8rZ_gQ">Lecture 10-3 CDCL (Lecture 5 in CS433)</a> — Automated Reasoning, tiếng Anh. Giải thích thuật toán CDCL dùng trong các bộ giải như Kissat và CaDiCaL.
- <a href="https://www.youtube.com/watch?v=Usoo2j2TQio">Boolean Algebra And LUTs in FPGA</a> — nandland, tiếng Anh. Liên hệ đại số Boole với khối LUT trên FPGA trong quy trình tổng hợp mạch.
