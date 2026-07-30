---
layout: post
title: "Thực hành Nghiên cứu và Lộ trình Đọc"
categories: chapter20
date: 2021-01-01
order: 14
required: true
lang: en
excerpt: "Checklist chọn đề tài; khung paper hardness/algorithm; solver thực nghiệm; lộ trình 12 tuần NCS; thư mục tổng."
---

<div class="textbook-epigraph" markdown="1">

"A good thesis problem is open, technical, and matched to your tools."

<span class="epigraph-attribution">— Research practice</span>

</div>

Sau 20.1–20.13, bạn có **ngôn ngữ** để đọc paper và **bộ chứng minh mẫu**. Mục cuối: *bắt tay làm nghiên cứu* — chọn bài, đọc, viết, thực nghiệm.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Lọc** đề tài (tránh / nên).
- **Viết** outline paper thuật toán/hardness.
- **Lên kế hoạch** 12 tuần đọc + mini-project.
- **Dùng** thư mục theo tầng.

</div>

## 1. Checklist đề tài

**Nên hỏi**

1. Status: P / NPC / APX / FPT / open gap?  
2. Special case tự nhiên (planar, degree, geometric)?  
3. Gap upper bound vs hardness?  
4. Có dữ liệu / benchmark không?  
5. Lab có kỹ thuật (SDP, kernel, PCP, SAT) không?

**Tránh**

- “Chứng minh $$P\neq NP$$” làm mục tiêu luận văn ThS.  
- Brute-force + chart không baseline.  
- DL “giải NPC” không metric/so solver.

## 2. Khung paper

1. Problem formal (encoding).  
2. Related work + status table.  
3. Contribution (alg / hardness / experiments).  
4. Proofs hoặc experiment design.  
5. Limits (ETH, UGC, instance size).

**Hardness section tối thiểu:** ∈NP + reduction từ 3SAT/IS + Yes⇔Yes + poly $$f$$ (như 20.6–20.9).

## 3. Solver / thực nghiệm

SAT: Kissat/Glucose; SMT: Z3; MILP: SCIP/Gurobi.  
Báo cáo: timeout, seed, machine, version, all instances.

## 4. Lộ trình 12 tuần (NCS năm 1)

| Tuần | Việc | Deliverable |
|:---:|:---|:---|
| 1–2 | 20.1–20.6 + bài chứng minh | Sổ lemma |
| 3–4 | 20.7–20.10 | 2 reduction viết tay |
| 5 | 20.11 VC-2 + đọc Christofides | 1 proof + 1 summary |
| 6 | 20.12 FPT VC + 1 kernel | Code search tree |
| 7 | 20.13 ETH + five worlds | Essay 1500 từ |
| 8 | Sipser/Arora–Barak ôn | Cheat-sheet 4 trang |
| 9 | Chọn 1 open problem nhỏ | 15 paper annotated |
| 10–11 | Mini: hardness *hoặc* alg *hoặc* solver | Draft 6–8 trang |
| 12 | Seminar talk 25 phút | Slide + Q&A list |

## 5. Thư mục theo tầng

**Tầng A (bắt buộc)**  
Sipser; Arora–Barak; Garey–Johnson; CLRS (NPC chapter).

**Tầng B (chọn 1 nhánh)**  
- Approx: Vazirani; Williamson–Shmoys.  
- FPT: Cygan et al.; Downey–Fellows.  
- Fine-grained: Williams surveys.  
- Crypto: Goldreich; Katz–Lindell.  
- Solvers: Handbook of Satisfiability.

**Tầng C (khảo sát)**  
Fortnow CACM; Aaronson P vs NP; Wigderson *Mathematics and Computation*; Impagliazzo 1995.

**Primary sources**  
Cook 1971; Karp 1972; Levin 1973; Ladner 1975.

## 6. Bản đồ Chương 20 (toàn bộ)

| # | Bài | Kỹ năng nghiên cứu |
|:---:|:---|:---|
| 1 | Quyết định & poly time | Encoding |
| 2 | $$P$$ & hierarchy | Đóng, diagonal |
| 3 | $$NP$$ verifier | Certificate |
| 4 | $$\mathrm{coNP}$$ | Cấu trúc |
| 5 | $$\le_p$$ | So sánh khó |
| 6 | NPC | Checklist hardness |
| 7 | Cook–Levin | Tableau |
| 8 | 3SAT | Source problem |
| 9 | IS/CLIQUE/VC | Graph reductions |
| 10 | HC/TSP | Routing hardness |
| 11 | Xấp xỉ | Ratio proofs |
| 12 | FPT | Parameter |
| 13 | ETH / average | Modern map |
| 14 | Research practice | **Bắt tay làm** |

## Bài tập cuối chương

1. **Portfolio:** 3 chứng minh (≤ₚ bắc cầu; VC-2; 3SAT→IS) PDF gọn.  
2. **Literature map:** 1 bài Garey–Johnson + 5 citation gần đây.  
3. **Proposal 4 trang** theo khung §2.  
4. **Seminar:** 25 phút Cook–Levin *hoặc* một rút gọn gadget.

## Tóm tắt

Đọc xong 20.1–20.14: bạn **viết được** hardness/alg cơ bản, **đọc được** paper complexity, **chọn được** đề mở *vừa sức* — điều kiện cần để bắt đầu nghiên cứu (cùng advisor và seminar lab).

Chúc làm việc tốt.
