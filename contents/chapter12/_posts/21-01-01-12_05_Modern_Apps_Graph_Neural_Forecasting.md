---
layout: post
title: "Ghi chú mở rộng: Đồ thị dự báo thời tiết (2022–2026)"
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

Bài ghi chú ứng dụng song ngữ, **không** viết lại phần định nghĩa đồ thị, biểu diễn đồ thị hay bài toán Euler/Hamilton.

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

GraphCast (Lam và cộng sự, *Science* 2023) là một mạng nơ-ron đồ thị (GNN) hoạt động theo kiến trúc encode–process–decode:

- **Grid2Mesh**: đồ thị hai phía ánh xạ từ lưới kinh–vĩ độ sang lưới đa phân giải (**multi-mesh**) dạng khối hai mươi mặt (icosahedral);
- **Mesh**: thực hiện truyền thông điệp (message passing) trên các đỉnh và cạnh của lưới;
- **Mesh2Grid**: đồ thị hai phía ánh xạ kết quả trở lại lưới kinh–vĩ độ.

Theo công bố, hệ thống có thể dự báo hàng trăm biến khí tượng trong 10 ngày ở độ phân giải toàn cầu $$0.25^\circ$$ trong vòng dưới một phút, đồng thời đạt độ chính xác cao hơn mô hình tất định chuẩn vận hành trên **90% trong tổng số 1380** chỉ tiêu kiểm chứng, bao gồm dự báo xoáy thuận, sông khí quyển và các hiện tượng thời tiết cực đoan.

Chương 12 đã giới thiệu cấu trúc $$G = (V,E)$$, quan hệ kề và đường đi. GraphCast cho thấy các khái niệm này có thể mở rộng lên quy mô toàn cầu: $$V$$ là tập đỉnh trên lưới phủ bề mặt Trái Đất, $$E$$ mã hóa các láng giềng cục bộ và đa tỷ lệ, còn quá trình tính toán gồm một số bước tổng hợp thông tin từ láng giềng cố định. Ngay cả khi không chuyên về khí tượng học, ta vẫn dễ nhận ra cơ chế lan truyền thông tin trên đồ thị tương tự cách mở rộng theo tầng của BFS.

**Câu hỏi.** (1) Grid2Mesh là đồ thị vô hướng đơn, đồ thị hai phía hay đa đồ thị — giải thích vì sao? (2) Bạn sẽ chọn cách biểu diễn nào trong Chương 12 để lưu trữ một lưới icosahedral tĩnh?

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=0Ud4u7c0_EE">AI Weather Forecasting: What GraphCast Actually Proved (and Didn&#x27;t)</a> — Synaptorix, tiếng Anh. Phân tích những kết quả thực tế của GraphCast khi chạy truyền thông điệp trên đồ thị đa lưới.
- <a href="https://www.youtube.com/watch?v=1DmNdMUbDkg">Message Passing: How Graph Neural Networks Actually Work</a> — The Synthetic Mind, tiếng Anh. Giải thích cơ chế truyền thông điệp (message passing) trong mạng nơ-ron đồ thị.
