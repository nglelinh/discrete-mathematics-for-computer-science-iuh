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

SAT is NP-complete (this chapter). That theorem does **not** say every instance is hard. Two 2022–2024 artifacts make the distinction teachable.

1. **Industrial SAT.** Kissat 4.0 took all three main-track golds at SAT Competition 2024 ([medals](https://cca.informatik.uni-freiburg.de/sat24medals/); Biere et al., Univ. Helsinki B-2024-1, pp. 8–10). CDCL regularly solves verification CNFs with millions of variables. Worst-case completeness and median-case practice are different sentences — the course already said so; the medals are a dated exhibit.
2. **Learned algorithms.** CLRS-30 (Veličković et al., ICML 2022, [PMLR 162:22084–22102](https://proceedings.mlr.press/v162/velickovic22a.html)) shows neural executors that look accurate on small graphs and then fail when $$n$$ grows. That is an empirical **generalisation** failure, not a new complexity class — but it warns against treating a trained net as a polynomial algorithm with a proof.

Optional synthesis with 20.13 (fine-grained / average-case): competition SAT and CLRS OOD gaps are *why* those finer theories exist. This note does not add a reduction.

**Citations**

1. SAT Competition 2024 medals and Biere et al. solver description, Univ. Helsinki B-2024-1, pp. 8–10. [PDF](https://cca.informatik.uni-freiburg.de/papers/BiereFallerFazekasFleuryFroleyksPollitt-SAT-Competition-2024-solvers.pdf)
2. P. Veličković et al., “The CLRS Algorithmic Reasoning Benchmark,” ICML 2022. [PMLR](https://proceedings.mlr.press/v162/velickovic22a.html)

**Questions.** (1) State Cook–Levin and the SAT-2024 medal result as two *non-contradictory* sentences. (2) If a GNN solves 16-node CLRS BFS at 99%, what claim is still forbidden?

## Tiếng Việt

SAT là bài toán NP-complete (như đã chứng minh trong chương này), nhưng định lý đó **không** khẳng định rằng mọi thể hiện đầu vào đều khó giải. Hai dẫn chứng thực nghiệm giai đoạn 2022–2024 giúp phân biệt rõ điểm này:

1. **Bộ giải SAT công nghiệp.** Kissat 4.0 giành cả ba huy chương vàng ở các hạng mục chính tại SAT Competition 2024. Các bộ giải theo kiến trúc CDCL thường xuyên xử lý thành công những công thức CNF kiểm chứng phần mềm có hàng triệu biến. Tính NP-complete ở trường hợp xấu nhất và hiệu năng thực tế ở trường hợp trung vị là hai phát biểu hoàn toàn khác nhau — kết quả cuộc thi là minh chứng cụ thể cho sự phân biệt đó.
2. **Thuật toán học từ dữ liệu.** Bộ chuẩn CLRS-30 (ICML 2022) cho thấy nhiều mô hình mạng nơ-ron đạt độ chính xác cao trên đồ thị nhỏ nhưng sụp đổ khi kích thước $$n$$ tăng lên. Đây là hạn chế về khả năng **tổng quát hóa thực nghiệm** chứ không tạo ra một lớp độ phức tạp mới, đồng thời nhắc nhở rằng không thể xem một mạng đã huấn luyện là một thuật toán thời gian đa thức có chứng minh tính đúng đắn.

Liên hệ với Bài 20.13 (độ phức tạp mịn và trường hợp trung bình): khoảng cách thực tế ở các bộ giải SAT và hiện tượng sụt giảm ngoài phân phối (OOD) trên CLRS chính là *lý do* các lý thuyết phân tích sâu hơn này ra đời. Ghi chú này không bổ sung thêm phép rút gọn mới.

**Câu hỏi.** (1) Hãy phát biểu định lý Cook–Levin và kết quả huy chương của Kissat tại SAT Competition 2024 thành hai câu *không mâu thuẫn* với nhau. (2) Nếu một GNN đạt độ chính xác 99% cho bài toán BFS trên đồ thị 16 đỉnh của CLRS, nhận định nào về mặt lý thuyết thuật toán vẫn không được phép đưa ra?

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=YX40hbAHx3s">P vs. NP and the Computational Complexity Zoo</a> — hackerdashery, tiếng Anh. Nhấn mạnh rằng NP-complete phản ánh độ khó trường hợp xấu nhất, không có nghĩa mọi thể hiện đều khó.
- <a href="https://www.youtube.com/watch?v=YUqR-8rZ_gQ">Lecture 10-3 CDCL (Lecture 5 in CS433)</a> — Automated Reasoning, tiếng Anh. Giải thích kiến trúc CDCL đằng sau các bộ giải SAT công nghiệp như Kissat.
- <a href="https://www.youtube.com/watch?v=DZDrRxM6RwI">Petar Veličković (DeepMind) — Neural Algorithmic Reasoning</a> — Zeta Alpha, tiếng Anh. Phân tích khả năng và giới hạn ngoài phân phối của mạng nơ-ron khi học thuật toán đồ thị.
