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

### Background Knowledge Map: How Graph Theory Powers Global Weather AI (GraphCast)

- **Bipartite Mapping Graphs (`Grid2Mesh` & `Mesh2Grid`):** Translating observations from a regular $$0.25^\circ$$ latitude–longitude grid (which crowds points near the poles!) onto a uniform spherical icosahedral mesh uses directed **bipartite graphs** $$G = (V_{\text{grid}} \cup V_{\text{mesh}}, E)$$.
- **Multi-Scale Mesh & Sparse Storage:** By overlaying coarse and fine icosahedral refinements onto the same vertex set, GraphCast builds a sparse multi-scale graph (small average degree, $$O(V)$$ edges) that allows long-range atmospheric signals to cross continents in just a few hops.
- **Message Passing as Differentiable BFS:** Each GNN layer updates every node's state by aggregating messages from its 1-hop neighbors. Stacking $$K$$ message-passing layers lets information propagate up to graph distance $$K$$ — the differentiable cousin of $$K$$-step Breadth-First Search!

### Deep-Dive Explanation: Hand-Verifiable Hop-Count & Memory Scaling on the Multi-Mesh (Read Slowly)

1. **Step 1 — Count the grid nodes at $$0.25^\circ$$ resolution:** Earth spans $$360^\circ$$ in longitude ($$1\,440$$ steps) and $$180^\circ$$ in latitude ($$721$$ steps including both poles), giving $$\vert V_{\text{grid}} \vert = 1\,440 \times 721 = 1\,038\,240 \approx 1.04\text{ million}$$ grid points!
2. **Step 2 — Why an adjacency matrix is impossible here:** Storing a dense adjacency matrix for $$40\,962$$ icosahedral mesh vertices alone would take $$40\,962^2 \approx 1.68 \times 10^9$$ entries (~6.7 GB in FP32 for edges alone), whereas a **sparse edge list / CSR adjacency list** with average degree ~12 stores only $$40\,962 \times 12 \approx 4.9 \times 10^5$$ edges (~4 MB — **over 1,600× smaller**).
3. **Step 3 — Why multi-scale edges beat a single fine mesh:** On a fine mesh alone, a storm signal traveling 64 grid cells would need 64 sequential layers. Adding coarse icosahedral "highway edges" shrinks the graph diameter dramatically so **16 message-passing layers** cover global weather dynamics in under one minute.

$$\vert V_{\text{grid}} \vert \approx 1.04 \times 10^6 \;\xrightarrow{\text{Grid2Mesh (Bipartite)}}\; \vert V_{\text{mesh}} \vert = 40\,962 \;\xrightarrow{16\text{ GNN hops (CSR)}}\; \text{10-day forecast } < 1\text{ min.}$$

## Tiếng Việt

GraphCast (Lam và cộng sự, *Science* 2023) là một mạng nơ-ron đồ thị (GNN) hoạt động theo kiến trúc encode–process–decode:

- **Grid2Mesh**: đồ thị hai phía ánh xạ từ lưới kinh–vĩ độ sang lưới đa phân giải (**multi-mesh**) dạng khối hai mươi mặt (icosahedral);
- **Mesh**: thực hiện truyền thông điệp (message passing) trên các đỉnh và cạnh của lưới;
- **Mesh2Grid**: đồ thị hai phía ánh xạ kết quả trở lại lưới kinh–vĩ độ.

Theo công bố, hệ thống có thể dự báo hàng trăm biến khí tượng trong 10 ngày ở độ phân giải toàn cầu $$0.25^\circ$$ trong vòng dưới một phút, đồng thời đạt độ chính xác cao hơn mô hình tất định chuẩn vận hành trên **90% trong tổng số 1380** chỉ tiêu kiểm chứng, bao gồm dự báo xoáy thuận, sông khí quyển và các hiện tượng thời tiết cực đoan.

Chương 12 đã giới thiệu cấu trúc $$G = (V,E)$$, quan hệ kề và đường đi. GraphCast cho thấy các khái niệm này có thể mở rộng lên quy mô toàn cầu: $$V$$ là tập đỉnh trên lưới phủ bề mặt Trái Đất, $$E$$ mã hóa các láng giềng cục bộ và đa tỷ lệ, còn quá trình tính toán gồm một số bước tổng hợp thông tin từ láng giềng cố định. Ngay cả khi không chuyên về khí tượng học, ta vẫn dễ nhận ra cơ chế lan truyền thông tin trên đồ thị tương tự cách mở rộng theo tầng của BFS.

**Câu hỏi.** (1) Grid2Mesh là đồ thị vô hướng đơn, đồ thị hai phía hay đa đồ thị — giải thích vì sao? (2) Bạn sẽ chọn cách biểu diễn nào trong Chương 12 để lưu trữ một lưới icosahedral tĩnh?

### Bản đồ kiến thức nền: Lý thuyết đồ thị vận hành mô hình dự báo thời tiết GraphCast ra sao?

- **Đồ thị hai phía (`Grid2Mesh` & `Mesh2Grid`):** Lưới kinh–vĩ độ $$0{,}25^\circ$$ bị dồn dày bất thường ở hai cực Trái Đất; GraphCast dùng đồ thị hai phía để chuyển dữ liệu sang một lưới khối hai mươi mặt (icosahedral mesh) phủ đều toàn cầu.
- **Đa lưới thưa & Biểu diễn CSR:** Chồng nhiều cấp độ lưới thô–mịn trên cùng tập đỉnh tạo ra đồ thị thưa ($$\vert E \vert = O(\vert V \vert)$$) có cả cạnh ngắn cục bộ lẫn "đường cao tốc" xuyên lục địa, phù hợp lưu bằng danh sách cạnh / CSR thay vì ma trận kề.
- **Truyền thông điệp như BFS khả vi:** Mỗi lớp GNN cập nhật trạng thái đỉnh từ láng giềng cách 1 bước; xếp chồng $$K$$ lớp cho phép thông tin khí tượng lan xa đúng bán kính $$K$$ bước trên đồ thị — phiên bản khả vi của duyệt BFS $$K$$ tầng!

### Khung giải thích: Tính tay quy mô đỉnh và lợi ích nén bộ nhớ của lưới GraphCast (nên đọc chậm)

1. **Bước 1 — Đếm số đỉnh lưới kinh–vĩ độ ở độ phân giải $$0{,}25^\circ$$:** Kinh độ $$360^\circ / 0{,}25^\circ = 1\,440$$ điểm, vĩ độ $$180^\circ / 0{,}25^\circ + 1 = 721$$ điểm $$\Rightarrow \vert V_{\text{grid}} \vert = 1\,440 \times 721 = 1\,038\,240$$ đỉnh!
2. **Bước 2 — So sánh ma trận kề vs. danh sách kề trên lưới 40.962 đỉnh:** Ma trận kề dày đặc cần $$40\,962^2 \approx 1{,}68$$ tỷ ô (~6,7 GB), trong khi danh sách cạnh / CSR với bậc trung bình ~12 chỉ tốn ~490.000 cạnh (~4 MB) — **nhỏ hơn hơn 1.600 lần**!
3. **Bước 3 — Sức mạnh của cạnh đa tỷ lệ:** Nhờ các cạnh dài từ lưới thô rút ngắn đường kính đồ thị, chỉ **16 bước truyền thông điệp** đã đủ kết nối luồng khí quyển tầm xa và chạy dự báo 10 ngày dưới 1 phút.

$$\vert V_{\text{grid}} \vert \approx 1{,}04 \times 10^6 \;\xrightarrow{\text{Grid2Mesh (Hai phía)}}\; \vert V_{\text{mesh}} \vert = 40\,962 \;\xrightarrow{16\text{ tầng GNN (CSR)}}\; \text{Dự báo 10 ngày } < 1\text{ phút.}$$

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=0Ud4u7c0_EE">AI Weather Forecasting: What GraphCast Actually Proved (and Didn&#x27;t)</a> — Synaptorix, tiếng Anh. Phân tích những kết quả thực tế của GraphCast khi chạy truyền thông điệp trên đồ thị đa lưới.
- <a href="https://www.youtube.com/watch?v=1DmNdMUbDkg">Message Passing: How Graph Neural Networks Actually Work</a> — The Synthetic Mind, tiếng Anh. Giải thích cơ chế truyền thông điệp (message passing) trong mạng nơ-ron đồ thị.
