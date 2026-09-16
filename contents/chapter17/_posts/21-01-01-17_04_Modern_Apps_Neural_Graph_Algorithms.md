---
layout: post
title: "Optional note: Neural graph algorithms (2022–2026)"
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

Bài ghi chú ứng dụng song ngữ. **Không** viết lại Dijkstra, sắp xếp topo, tô màu hay ghép cặp.

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

Chương 17 là thuật toán đồ thị cổ điển. Hai hướng gần đây hỏi liệu thủ tục message passing **học được** có *bắt chước* các thuật toán đó — hoặc thay bộ giải số trên đồ thị rất lớn.

**CLRS-30** (Veličković et al., ICML 2022) cung cấp quỹ đạo (input, hint, output) cho 30 thuật toán giáo khoa, gồm các routine đồ thị. GNN encode–process–decode dự đoán đáp án và con trỏ trung gian. Quan sát lặp lại: điểm in-distribution trên đồ thị 16 đỉnh có thể cao trong khi test **OOD** 64 đỉnh sụp — “mạng chạy Dijkstra” không có nghĩa “mạng *là* Dijkstra.”

**GraphCast** (*Science* 2023) không tuyên bố cài Dijkstra; nó tuyên bố message passing học trên multi-mesh là toán tử thời tiết 10 ngày hữu ích. Hai trích dẫn tách **trung thành thuật toán** (CLRS) khỏi **mô hình số hình đồ thị** (GraphCast).

**Câu hỏi.** (1) “Hint” CLRS nào tương ứng mảng khoảng cách Dijkstra sau $$k$$ lần relax? (2) Vì sao sụt accuracy OOD chặn tuyên bố GNN đã học thuật toán?
