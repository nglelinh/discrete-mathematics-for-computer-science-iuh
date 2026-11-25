---
layout: post
title: "Ghi chú mở rộng: Toán rời rạc trong các hệ thống thực tế 2022–2026"
categories: chapter09
date: 2021-01-01
order: 13
required: false
lesson_type: optional
lang: en
excerpt: "Optional bilingual note. A short 2022–2026 pointer pack: Kissat, binary fuse filters, GraphCast — tying this applications chapter to recent deployed discrete structure. Does not replace existing case studies."
---

<div class="note-box" markdown="1">

**Optional / Tùy chọn.** Bilingual application note (English, then Vietnamese). It does **not** rewrite the binary-data, testing, or login case studies.

Ghi chú ứng dụng song ngữ (tiếng Anh trước, tiếng Việt sau). Nội dung này chỉ bổ sung tài liệu tham chiếu gần đây, **không** thay thế các bài học về dữ liệu nhị phân, kiểm thử hay đăng nhập ở trên.

</div>

## English

Chapter 9 already connects discrete math to production (endianness, pools, pairwise tests, collisions). This optional note only adds **three dated artifacts** from 2022–2024 that a systems student can open next.

| Year | Artifact | Discrete object | Why it belongs here |
|:---:|:---|:---|:---|
| 2022 | Binary fuse filters (Graf & Lemire, JEA) | Approximate set | Same collision budget as birthday / hash notes |
| 2023 | GraphCast (Lam et al., *Science*) | Mesh graph + GNN | Graphs and message passing at weather scale |
| 2024 | Kissat at SAT Competition | CNF / CDCL | Logic and combinatorial explosion, now with medals |

- Graf & Lemire, [DOI 10.1145/3510449](https://doi.org/10.1145/3510449) — filters within ~13% of the storage lower bound.
- Lam et al., “Learning skillful medium-range global weather forecasting,” *Science* (2023), [DOI 10.1126/science.adi2336](https://doi.org/10.1126/science.adi2336) — 10-day global forecast, $$0.25^\circ$$, under one minute, better than the operational deterministic baseline on 90% of 1380 targets.
- SAT Competition 2024 medals: [Freiburg page](https://cca.informatik.uni-freiburg.de/sat24medals/).

Read this as a **landing index**, not a new theory chapter. Each row points at a chapter you already have (4–8, 12–13, 1).

**Questions.** (1) Which Chapter 9 case study shares its counting model with SAT’s $$2^n$$? (2) Why is GraphCast’s mesh a *graph* in the sense of Chapter 12, not a continuous PDE solver?

### Background Knowledge Map: Where Do Deployed Discrete Structures Live in 2022–2026 Systems?

- **Approximate Membership & Information Theory (Binary Fuse Filters):** Instead of storing full keys, modern static filters solve linear systems over finite fields (XOR/peeling hypergraphs) to stay within ~8%–13% of the information-theoretic lower bound $$\log_2(1/\varepsilon)$$ bits per key.
- **Discrete Geometric Graphs & Message Passing (GraphCast):** Discretizing Earth's atmosphere onto an icosahedral multi-mesh turns global weather prediction into a fixed number of graph neighborhood aggregations — bypassing tiny explicit PDE time-step constraints.
- **Propositional Logic & Conflict-Driven Search (Kissat / CDCL):** Modern SAT solvers routinely decide Boolean formulas with hundreds of thousands of variables by learning conflict clauses that prune exponential $$2^n$$ search trees.

### Deep-Dive Explanation: A Hand-Verifiable Bit-Budget Calculation (Read Slowly)

1. **Step 1 — Compute the information-theoretic floor:** Suppose you need a static filter for $$n = 1\,000\,000$$ keys with false-positive rate $$\varepsilon = 2^{-8} \approx 0.39\%$$. Information theory demands at least $$\log_2(1/\varepsilon) = 8$$ bits per key, or $$1.00\text{ MB}$$ total.
2. **Step 2 — Compare Bloom vs. Binary Fuse Filter:** A classic Bloom filter requires $$\approx 1.44 \log_2(1/\varepsilon) = 1.44 \times 8 = 11.52$$ bits/key ($$1.44\text{ MB}$$, a 44% overhead). A 3-wise binary fuse filter uses roughly $$1.13 \times 8 = 9.04$$ bits/key ($$1.13\text{ MB}$$), saving over **21%** of RAM while answering queries with fewer cache misses.
3. **Step 3 — See the common thread:** Whether choosing 9.04 bits/key in a filter, pruning clauses in Kissat, or aggregating neighbors on GraphCast's mesh, production systems win by choosing the tightest discrete model for their hardware budget.

$$\text{Bloom: } 1.44\log_2(1/\varepsilon) \;\xrightarrow{\text{Binary Fuse (2022)}}\; \approx 1.08\text{–}1.13\log_2(1/\varepsilon)\text{ bits/key.}$$

## Tiếng Việt

Chương 9 đã kết nối toán rời rạc với các hệ thống vận hành thực tế (endianness, connection pool, kiểm thử pairwise, va chạm băm). Ghi chú ngắn này bổ sung **ba công trình tiêu biểu** giai đoạn 2022–2024 để người học có thể tham khảo mở rộng:

| Năm | Công trình / Hệ thống | Đối tượng toán rời rạc | Lý do liên hệ với Chương 9 |
|:---:|:---|:---|:---|
| 2022 | Binary fuse filter (Graf & Lemire, JEA) | Tập hợp xấp xỉ | Cùng bài toán ngân sách va chạm như nghịch lý sinh nhật và bảng băm |
| 2023 | GraphCast (Lam et al., *Science*) | Đồ thị lưới + GNN | Đồ thị và truyền thông điệp (message passing) ở quy mô dự báo thời tiết toàn cầu |
| 2024 | Kissat tại SAT Competition | CNF / CDCL | Logic mệnh đề và bài toán bùng nổ tổ hợp trong các bộ giải SAT hiện đại |

Hãy xem bảng trên như một **chỉ mục tham khảo mở rộng**, không phải chương lý thuyết mới — mỗi dòng đều nối trực tiếp về các chương đã học trong giáo trình (Chương 1, 4–8, 12–13).

**Câu hỏi gợi mở.** (1) Tình huống nào trong Chương 9 chia sẻ cùng mô hình đếm tăng trưởng mũ $$2^n$$ với bài toán SAT? (2) Vì sao lưới dự báo của GraphCast được mô hình hóa như một *đồ thị* theo nghĩa của Chương 12 thay vì một bộ giải phương trình đạo hàm riêng (PDE) liên tục?

### Bản đồ kiến thức nền: Ba trụ cột toán rời rạc trong hệ thống 2022–2026

- **Tập hợp xấp xỉ & Lý thuyết thông tin (Binary Fuse Filter):** Thay vì lưu toàn bộ khóa gốc, các bộ lọc tĩnh hiện đại giải hệ tuyến tính trên đồ thị băm để nén bộ nhớ xuống sát cận dưới lý thuyết thông tin $$\log_2(1/\varepsilon)$$ bit/khóa (chỉ vượt khoảng 8%–13%).
- **Đồ thị lưới đa phân giải & Truyền thông điệp (GraphCast):** Rời rạc hóa khí quyển Trái Đất thành lưới đa diện hai mươi mặt giúp biến bài toán dự báo toàn cầu thành hữu hạn vòng tổng hợp thông tin từ các đỉnh láng giềng trên đồ thị.
- **Logic mệnh đề & Tìm kiếm học từ xung đột (Kissat / CDCL):** Các bộ giải SAT hiện đại giải được công thức Boole hàng trăm nghìn biến bằng cách học mệnh đề xung đột (conflict clause learning) để cắt bỏ phần lớn không gian tìm kiếm $$2^n$$.

### Khung giải thích: Tính tay ngân sách bit của Binary Fuse Filter so với Bloom Filter (nên đọc chậm)

1. **Bước 1 — Cận dưới lý thuyết thông tin:** Với $$n = 1\,000\,000$$ khóa và tỷ lệ dương tính giả $$\varepsilon = 2^{-8} \approx 0{,}39\%$$, mọi bộ lọc đều cần ít nhất $$\log_2(1/\varepsilon) = 8$$ bit/khóa (tương đương $$1{,}00\text{ MB}$$).
2. **Bước 2 — So sánh trực tiếp:** Bloom filter cổ điển tốn $$\approx 1{,}44 \times 8 = 11{,}52$$ bit/khóa ($$1{,}44\text{ MB}$$, dư 44%). Binary fuse filter chỉ cần khoảng $$1{,}13 \times 8 = 9{,}04$$ bit/khóa ($$1{,}13\text{ MB}$$), tiết kiệm hơn **21%** bộ nhớ RAM mà vẫn tra cứu nhanh hơn.
3. **Bước 3 — Mẫu số chung của kỹ thuật hệ thống:** Cả ba công trình 2022–2024 đều chứng minh rằng chọn đúng mô hình toán rời rạc (tập xấp xỉ, đồ thị lưới, mệnh đề CNF) quyết định trực tiếp giới hạn tốc độ và bộ nhớ của phần mềm hiện đại.

$$\text{Bloom: } 1{,}44\log_2(1/\varepsilon) \;\xrightarrow{\text{Binary Fuse (2022)}}\; \approx 1{,}08\text{–}1{,}13\log_2(1/\varepsilon)\text{ bit/khóa.}$$

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=0Ud4u7c0_EE">AI Weather Forecasting: What GraphCast Actually Proved (and Didn&#x27;t)</a> — Synaptorix, tiếng Anh. Phân tích những gì GraphCast chứng minh được khi dự báo thời tiết trên đồ thị lưới.
- <a href="https://www.youtube.com/watch?v=V3pzxngeLqw">Bloom Filters | Algorithms You Should Know #2 | Real-world Examples</a> — ByteByteGo, tiếng Anh. Trình bày bộ lọc tập xấp xỉ, cùng họ cấu trúc dữ liệu với binary fuse filter.
- <a href="https://www.youtube.com/watch?v=YUqR-8rZ_gQ">Lecture 10-3 CDCL (Lecture 5 in CS433)</a> — Automated Reasoning, tiếng Anh. Giới thiệu thuật toán CDCL trên dạng chuẩn hội (CNF), cùng họ bộ giải với Kissat tại SAT Competition.
