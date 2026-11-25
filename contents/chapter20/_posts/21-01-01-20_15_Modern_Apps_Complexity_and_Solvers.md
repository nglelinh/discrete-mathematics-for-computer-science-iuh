---
layout: post
title: "Ghi chú mở rộng: NP-đầy đủ, kỷ lục SAT và OOD của mạng nơ-ron (2022–2026)"
categories: chapter20
date: 2021-01-01
order: 15
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. Kissat (SAT 2024) and CLRS-30 (ICML 2022) show the gap between worst-case NP-completeness, industrial SAT, and learned algorithms that fail out of distribution. Does not replace P/NP theory."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite Cook–Levin, reductions, FPT, or ETH.

Bài ghi chú ứng dụng song ngữ. Bài này **không** thay thế các nội dung về Cook–Levin, phép rút gọn, FPT hay ETH.

</div>

## English

Modern computational complexity presents a striking paradox: `SAT` is the canonical NP-complete problem, yet industrial **CDCL SAT solvers** routinely solve instances with millions of variables for hardware verification and computer-assisted math proofs—while neural networks trained to solve NP-hard problems often struggle with out-of-distribution (OOD) size generalization.

### Background Knowledge Map: Three Pillars of Modern Solvers & Complexity

1. **Conflict-Driven Clause Learning (CDCL)**:
   Enhances backtracking with unit propagation, conflict analysis that learns new pruning clauses, non-chronological backjumping, and restarts to exploit real-world instance structure.
2. **Certifying Solvers & DRAT Proofs**:
   When a solver returns `UNSAT`, it emits a machine-checkable proof trace (DRAT) verified by an independent trusted checker—bridging complexity theory with formal mathematics.
3. **Neural-Guided Solvers vs. OOD Limits**:
   Rather than replacing exact search end-to-end, 2022–2026 systems increasingly pair learned heuristics with exact branch-and-bound or SAT/MIP engines to preserve correctness and OOD scaling.

SAT is NP-complete (this chapter). That theorem does **not** say every instance is hard. Two 2022–2024 artifacts make the distinction teachable.

1. **Industrial SAT.** Kissat 4.0 took all three main-track golds at SAT Competition 2024 ([medals](https://cca.informatik.uni-freiburg.de/sat24medals/); Biere et al., Univ. Helsinki B-2024-1, pp. 8–10). CDCL regularly solves verification CNFs with millions of variables. Worst-case completeness and median-case practice are different sentences — the course already said so; the medals are a dated exhibit.
2. **Learned algorithms.** CLRS-30 (Veličković et al., ICML 2022, [PMLR 162:22084–22102](https://proceedings.mlr.press/v162/velickovic22a.html)) shows neural executors that look accurate on small graphs and then fail when $$n$$ grows. That is an empirical **generalisation** failure, not a new complexity class — but it warns against treating a trained net as a polynomial algorithm with a proof.

Optional synthesis with 20.13 (fine-grained / average-case): competition SAT and CLRS OOD gaps are *why* those finer theories exist. This note does not add a reduction.

**Citations**

1. SAT Competition 2024 medals and Biere et al. solver description, Univ. Helsinki B-2024-1, pp. 8–10. [PDF](https://cca.informatik.uni-freiburg.de/papers/BiereFallerFazekasFleuryFroleyksPollitt-SAT-Competition-2024-solvers.pdf)
2. P. Veličković et al., “The CLRS Algorithmic Reasoning Benchmark,” ICML 2022. [PMLR](https://proceedings.mlr.press/v162/velickovic22a.html)

**Questions.** (1) State Cook–Levin and the SAT-2024 medal result as two *non-contradictory* sentences. (2) If a GNN solves 16-node CLRS BFS at 99%, what claim is still forbidden?

### Deep-Dive Explanation (Read Slowly): One Concrete Clause-Learning Step in CDCL

Consider $$C_1 = (\neg x_1 \lor x_2)$$, $$C_2 = (\neg x_1 \lor \neg x_2 \lor x_3)$$, and $$C_3 = (\neg x_1 \lor \neg x_3)$$:
1. The solver branches on $$x_1 = \text{True}$$.
2. Unit propagation forces $$x_2 = \text{True}$$ (from $$C_1$$), then $$x_3 = \text{True}$$ (from $$C_2$$), which falsifies $$C_3$$ (**conflict!**).
3. Conflict analysis deduces the learned unit clause $$C_{\text{learned}} = (\neg x_1)$$ and adds it permanently to the clause database—pruning the entire $$x_1 = \text{True}$$ half of the search tree once and for all.

## Tiếng Việt

Một nghịch lý thú vị của khoa học máy tính hiện đại: `SAT` là bài toán NP-complete kinh điển khó nhất trong lớp $$NP$$, nhưng các bộ giải **CDCL SAT solver** ngày nay lại giải gọn gàng các công thức có hàng triệu biến trong kiểm chứng chip Intel/AMD, chứng minh định lý toán học (như bài toán bộ ba Pythagore Boolean) và giải bài toán lập lịch công nghiệp. Trong khi đó, các mạng nơ-ron học giải bài toán NP-hard (như TSP hay SAT) thường gặp rào cản khái quát ngoài phân phối (OOD) khi kích thước đồ thị tăng lên.

### Kiến thức cần nhớ: Ba trụ cột của Độ phức tạp Hiện đại & Bộ giải Thực tế

1. **CDCL SAT Solver (Conflict-Driven Clause Learning)**:
   Thay vì quay lui mù quáng (DPLL), CDCL phân tích nguyên nhân mâu thuẫn để **học thêm mệnh đề mới (conflict clause)**, nhảy lùi không tuần tự (*backjumping*) và khởi động lại thông minh — khai thác triệt để cấu trúc ẩn của bài toán thực tế.
2. **Chứng chỉ không thỏa được (DRAT Proofs)**:
   Khi SAT solver báo `UNSAT` (như chứng minh một định lý toán học hay xác nhận thiết kế chip không có lỗi), nó xuất ra một tệp chứng minh DRAT có thể kiểm chứng độc lập bằng trình kiểm tra cực nhỏ — bảo đảm độ tin cậy tuyệt đối.
3. **Học máy kết hợp Bộ giải (Neural-Guided Search & OOD Limits)**:
   Mạng nơ-ron khó thay thế hoàn toàn bộ giải chính xác ở kích thước lớn ngoài tập huấn luyện (OOD), nên hướng đi hiệu quả giai đoạn 2022–2026 là dùng mạng nơ-ron làm *heuristic chọn nhánh* bên trong khung tìm kiếm chính xác (branch-and-bound / CDCL).

SAT là bài toán NP-complete (như đã chứng minh trong chương này), nhưng định lý đó **không** khẳng định rằng mọi thể hiện đầu vào đều khó giải. Hai dẫn chứng thực nghiệm giai đoạn 2022–2024 giúp phân biệt rõ điểm này:

1. **Bộ giải SAT công nghiệp.** Kissat 4.0 giành cả ba huy chương vàng ở các hạng mục chính tại SAT Competition 2024. Các bộ giải theo kiến trúc CDCL thường xuyên xử lý thành công những công thức CNF kiểm chứng phần mềm có hàng triệu biến. Tính NP-complete ở trường hợp xấu nhất và hiệu năng thực tế ở trường hợp trung vị là hai phát biểu hoàn toàn khác nhau — kết quả cuộc thi là minh chứng cụ thể cho sự phân biệt đó.
2. **Thuật toán học từ dữ liệu.** Bộ chuẩn CLRS-30 (ICML 2022) cho thấy nhiều mô hình mạng nơ-ron đạt độ chính xác cao trên đồ thị nhỏ nhưng sụp đổ khi kích thước $$n$$ tăng lên. Đây là hạn chế về khả năng **tổng quát hóa thực nghiệm** chứ không tạo ra một lớp độ phức tạp mới, đồng thời nhắc nhở rằng không thể xem một mạng đã huấn luyện là một thuật toán thời gian đa thức có chứng minh tính đúng đắn.

Liên hệ với Bài 20.13 (độ phức tạp mịn và trường hợp trung bình): khoảng cách thực tế ở các bộ giải SAT và hiện tượng sụt giảm ngoài phân phối (OOD) trên CLRS chính là *lý do* các lý thuyết phân tích sâu hơn này ra đời. Ghi chú này không bổ sung thêm phép rút gọn mới.

**Câu hỏi.** (1) Hãy phát biểu định lý Cook–Levin và kết quả huy chương của Kissat tại SAT Competition 2024 thành hai câu *không mâu thuẫn* với nhau. (2) Nếu một GNN đạt độ chính xác 99% cho bài toán BFS trên đồ thị 16 đỉnh của CLRS, nhận định nào về mặt lý thuyết thuật toán vẫn không được phép đưa ra?

### Giải thích: Minh họa 1 bước "học mệnh đề từ mâu thuẫn" (Clause Learning) trong CDCL

Xét công thức nhỏ có 3 mệnh đề:
$$C_1 = (\neg x_1 \lor x_2), \qquad C_2 = (\neg x_1 \lor \neg x_2 \lor x_3), \qquad C_3 = (\neg x_1 \lor \neg x_3).$$
1. Giả sử bộ giải quyết định thử nhánh $$x_1 = \text{True}$$.
2. Lan truyền đơn vị (Unit Propagation):
   - Từ $$C_1$$ suy bắt buộc $$x_2 = \text{True}$$.
   - Từ $$C_2$$ (với $$x_1=T, x_2=T$$) suy bắt buộc $$x_3 = \text{True}$$.
   - Thế vào $$C_3 = (\neg x_1 \lor \neg x_3)$$ → **MÂU THUẪN!**
3. **Học mệnh đề mới:** Thay vì chỉ lùi lại thử nhánh khác rồi sau này lại vô tình đặt $$x_1 = \text{True}$$ lần nữa ở một nhánh khác, CDCL rút ra ngay mệnh đề học được $$C_{\text{learned}} = (\neg x_1)$$ và bổ sung vào công thức! Từ giây phút đó, toàn bộ nửa không gian tìm kiếm có $$x_1 = \text{True}$$ bị cắt tỉa vĩnh viễn!

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=YX40hbAHx3s">P vs. NP and the Computational Complexity Zoo</a> — hackerdashery, tiếng Anh. Nhấn mạnh rằng NP-complete phản ánh độ khó trường hợp xấu nhất, không có nghĩa mọi thể hiện đều khó.
- <a href="https://www.youtube.com/watch?v=YUqR-8rZ_gQ">Lecture 10-3 CDCL (Lecture 5 in CS433)</a> — Automated Reasoning, tiếng Anh. Giải thích kiến trúc CDCL đằng sau các bộ giải SAT công nghiệp như Kissat.
- <a href="https://www.youtube.com/watch?v=DZDrRxM6RwI">Petar Veličković (DeepMind) — Neural Algorithmic Reasoning</a> — Zeta Alpha, tiếng Anh. Phân tích khả năng và giới hạn ngoài phân phối của mạng nơ-ron khi học thuật toán đồ thị.
