---
layout: post
title: "Ghi chú mở rộng: Thuật toán đồ thị bằng mạng nơ-ron (2022–2026)"
categories: chapter17
date: 2021-01-01
order: 4
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. CLRS-30 (ICML 2022) asks GNNs to execute Dijkstra, BFS, and other textbook graph algorithms; GraphCast (2023) is message passing at Earth scale. Does not replace shortest-path theory."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite Dijkstra, topological sort, or coloring/matching.

Bài ghi chú ứng dụng song ngữ. Bài này **không** thay thế các nội dung về Dijkstra, sắp xếp topo, tô màu hay ghép cặp.

</div>

## English

Chapter 17 is classical graph algorithms: shortest paths, topo order, matching. Two recent lines ask whether a **learned** message-passing procedure can *imitate* those algorithms — or replace a numerical solver on a huge graph.

**CLRS-30.** Veličković et al., “The CLRS Algorithmic Reasoning Benchmark,” *ICML 2022*, PMLR 162:22084–22102, [paper](https://proceedings.mlr.press/v162/velickovic22a.html), ship trajectories (inputs, hints, outputs) for 30 textbook algorithms, including graph routines. Encode–process–decode GNNs predict both the answer and intermediate pointers. A recurring finding: in-distribution scores on 16-node graphs can look strong while **out-of-distribution** 64-node tests collapse — so “the network ran Dijkstra” is not the same as “the network *is* Dijkstra.” Library: [github.com/deepmind/clrs](https://github.com/deepmind/clrs).

**GraphCast** (Lam et al., *Science* 2023, [DOI 10.1126/science.adi2336](https://doi.org/10.1126/science.adi2336)) is not claiming to implement Dijkstra; it *is* claiming that learned message passing on a multi-mesh is a useful 10-day weather operator. Together, the two citations separate **algorithmic fidelity** (CLRS) from **graph-shaped numerical models** (GraphCast).

**Citations**

1. P. Veličković et al., “The CLRS Algorithmic Reasoning Benchmark,” ICML 2022. [PMLR](https://proceedings.mlr.press/v162/velickovic22a.html)
2. R. Lam et al., “Learning skillful medium-range global weather forecasting,” *Science* (2023). [DOI](https://doi.org/10.1126/science.adi2336)

**Questions.** (1) Which CLRS “hint” would correspond to Dijkstra’s distance array after $$k$$ relaxations? (2) Why does an OOD accuracy drop block the claim that the GNN learned the algorithm?

## Tiếng Việt

Chương 17 tập trung vào các thuật toán đồ thị cổ điển. Hai hướng nghiên cứu gần đây đặt câu hỏi liệu một cơ chế truyền thông điệp (*message passing*) **được học từ dữ liệu** có thể *mô phỏng* những thuật toán đó, hay thậm chí thay thế bộ giải số trên các đồ thị quy mô rất lớn hay không.

**CLRS-30** (Veličković và cộng sự, ICML 2022) cung cấp các chuỗi thực thi (gồm đầu vào, gợi ý trung gian *hint* và đầu ra) cho 30 thuật toán kinh điển, bao gồm nhiều thuật toán đồ thị. Mạng nơ-ron đồ thị (GNN) theo kiến trúc encode–process–decode dự đoán đồng thời cả kết quả cuối lẫn các con trỏ trạng thái trung gian. Một kết quả thường lặp lại là mô hình đạt điểm cao trên phân phối huấn luyện (đồ thị 16 đỉnh) nhưng giảm mạnh khi kiểm thử **ngoài phân phối (OOD)** trên đồ thị 64 đỉnh — cho thấy việc “mạng chạy ra kết quả giống Dijkstra” không đồng nghĩa với việc “mạng *chính là* thuật toán Dijkstra”.

**GraphCast** (*Science*, 2023) không tuyên bố cài đặt Dijkstra mà chứng minh rằng cơ chế truyền thông điệp học được trên lưới đa tầng (*multi-mesh*) có thể đóng vai trò một toán tử dự báo thời tiết 10 ngày hiệu quả. Đặt cạnh nhau, hai công trình này phân tách rõ **độ trung thành về thuật toán** (CLRS) với **mô hình số mang cấu trúc đồ thị** (GraphCast).

**Câu hỏi.** (1) Gợi ý (*hint*) nào trong CLRS tương ứng với mảng khoảng cách của Dijkstra sau $$k$$ bước relax? (2) Vì sao sự sụt giảm độ chính xác trên dữ liệu OOD lại bác bỏ nhận định rằng GNN đã thực sự “học được” thuật toán?

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=aFnHYEv71U4">An Introduction to Graph Neural Networks</a> — DataMListic, tiếng Anh. Giới thiệu tổng quan về mạng nơ-ron đồ thị (GNN), mô hình được dùng để học thuật toán đồ thị.
- <a href="https://www.youtube.com/watch?v=DZDrRxM6RwI">Petar Veličković (DeepMind) — Neural Algorithmic Reasoning</a> — Zeta Alpha, tiếng Anh. Bài nói về hướng nghiên cứu *neural algorithmic reasoning* và bộ chuẩn CLRS được trích dẫn trong bài.
- <a href="https://www.youtube.com/watch?v=0Ud4u7c0_EE">AI Weather Forecasting: What GraphCast Actually Proved (and Didn&#x27;t)</a> — Synaptorix, tiếng Anh. Phân tích GraphCast — ứng dụng truyền thông điệp trên đồ thị ở quy mô dự báo thời tiết toàn cầu.
