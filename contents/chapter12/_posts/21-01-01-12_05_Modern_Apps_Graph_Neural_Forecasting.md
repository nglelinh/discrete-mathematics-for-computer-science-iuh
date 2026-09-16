---
layout: post
title: "Optional note: Graphs that forecast the weather (2022–2026)"
categories: chapter12
date: 2021-01-01
order: 5
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. GraphCast (Science 2023) runs message passing on a multi-mesh graph. Does not replace basic graph theory."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite definitions, representations, or Euler/Hamilton lessons.

Bài ghi chú ứng dụng song ngữ. **Không** viết lại định nghĩa, biểu diễn, hay Euler/Hamilton.

</div>

## English

GraphCast (Lam, Sanchez-Gonzalez, Willson, et al., “Learning skillful medium-range global weather forecasting,” *Science*, 2023, [DOI 10.1126/science.adi2336](https://doi.org/10.1126/science.adi2336); preprint [arXiv:2212.12794](https://arxiv.org/abs/2212.12794)) is a GNN with the classical encode–process–decode pattern:

- **Grid2Mesh** — bipartite graph from the latitude–longitude grid to an icosahedral **multi-mesh**;
- **Mesh** — message passing on mesh vertices and edges;
- **Mesh2Grid** — bipartite graph back to the grid.

The published system predicts hundreds of variables for 10 days at $$0.25^\circ$$ globally in under one minute, and outperforms the operational deterministic baseline on **90% of 1380** verification targets, with gains on cyclones, atmospheric rivers, and extremes.

Chapter 12 already defined $$G = (V,E)$$, adjacency, and walks. GraphCast is a 2023 reminder that those objects scale: $$V$$ is a mesh of the Earth, $$E$$ encodes local (and multi-scale) neighbourhoods, and “algorithm” is a fixed number of neighbourhood aggregations. You do not need to learn meteorology to see BFS-like diffusion of information across a graph.

**Citations**

1. R. Lam et al., “Learning skillful medium-range global weather forecasting,” *Science* (2023). [DOI](https://doi.org/10.1126/science.adi2336)

**Questions.** (1) Is Grid2Mesh a simple undirected graph, a bipartite graph, or a multigraph — and why? (2) Which Chapter 12 representation would you store for a static icosahedral mesh?

## Tiếng Việt

GraphCast (Lam và cộng sự, *Science* 2023) là GNN theo mẫu encode–process–decode:

- **Grid2Mesh** — đồ thị hai phía từ lưới vĩ–kinh độ sang **multi-mesh** icosahedral;
- **Mesh** — message passing trên đỉnh và cạnh lưới;
- **Mesh2Grid** — đồ thị hai phía trở lại lưới.

Hệ thống công bố dự báo hàng trăm biến trong 10 ngày, độ phân giải $$0.25^\circ$$ toàn cầu, dưới một phút, và thắng baseline deterministic vận hành trên **90% trong 1380** mục kiểm tra, kể cả bão, sông khí quyển và cực đoan.

Chương 12 đã định nghĩa $$G = (V,E)$$, kề và đường đi. GraphCast là lời nhắc 2023 rằng các đối tượng đó mở được quy mô: $$V$$ là lưới Trái Đất, $$E$$ mã hóa láng giềng (đa tỷ lệ), “thuật toán” là một số bước kết tập láng giềng cố định. Không cần khí tượng để thấy khuếch tán kiểu BFS trên đồ thị.

**Câu hỏi.** (1) Grid2Mesh là đồ thị vô hướng đơn, hai phía, hay đa đồ thị — vì sao? (2) Biểu diễn Chương 12 nào bạn sẽ lưu cho mesh icosahedral tĩnh?
