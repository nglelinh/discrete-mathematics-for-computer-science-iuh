---
layout: post
title: "Optional note: NP-completeness, SAT medals, neural OOD (2022–2026)"
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

Bài ghi chú ứng dụng song ngữ. **Không** viết lại Cook–Levin, rút gọn, FPT hay ETH.

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

SAT là NP-đầy đủ (chương này). Định lý **không** nói mọi instance đều khó. Hai hiện vật 2022–2024 giúp phân biệt điều đó khi dạy.

1. **SAT công nghiệp.** Kissat 4.0 thắng cả ba vàng track chính SAT Competition 2024. CDCL thường xuyên giải CNF kiểm chứng hàng triệu biến. Đầy đủ worst-case và thực hành median-case là hai câu khác nhau — giáo trình đã nói; huy chương là hiện vật có ngày.
2. **Thuật toán học.** CLRS-30 (ICML 2022) cho thấy bộ thực thi neural trông chính xác trên đồ thị nhỏ rồi thất bại khi $$n$$ tăng. Đó là thất bại **tổng quát hóa**, không phải lớp phức tạp mới — nhưng nó cảnh báo đừng coi mạng đã huấn luyện là thuật toán đa thức có chứng minh.

Tổng hợp tùy chọn với 20.13 (fine-grained / average-case): SAT thi đấu và lỗ hổng OOD của CLRS chính là *lý do* các lý thuyết mịn hơn tồn tại. Ghi chú không thêm phép rút gọn.

**Câu hỏi.** (1) Phát biểu Cook–Levin và kết quả huy chương SAT 2024 thành hai câu *không mâu thuẫn*. (2) Nếu GNN giải BFS CLRS 16 đỉnh 99%, tuyên bố nào vẫn bị cấm?
