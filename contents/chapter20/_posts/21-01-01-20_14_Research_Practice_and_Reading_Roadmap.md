---
layout: post
title: "Thực hành Nghiên cứu và Lộ trình Đọc"
categories: chapter20
date: 2021-01-01
order: 14
required: true
lang: en
excerpt: "Tiêu chí chọn đề tài nghiên cứu độ phức tạp, cấu trúc bài báo thuật toán/hardness, thực hành với bộ giải SAT/SMT/MILP, lộ trình tự học 12 tuần và thư mục tài liệu theo tầng."
---

<div class="textbook-epigraph" markdown="1">

"A good thesis problem is open, technical, and matched to your tools."

<span class="epigraph-attribution">— Research practice</span>

</div>

Sau các bài 20.1–20.13, bạn đã có **ngôn ngữ chuẩn** để đọc bài báo chuyên ngành cùng **bộ chứng minh mẫu**. Bài cuối này hướng dẫn bước chuyển sang *thực hành nghiên cứu*: chọn đề tài phù hợp, đọc tài liệu theo tầng, viết chứng minh và thiết kế thực nghiệm.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Sàng lọc** đề tài nghiên cứu (những câu hỏi nên đặt và những hướng cần tránh).
- **Xây dựng** dàn ý cho một bài báo về thuật toán hoặc chứng minh độ khó (*hardness*).
- **Lập kế hoạch** 12 tuần tự đọc kết hợp một dự án nghiên cứu nhỏ.
- **Sử dụng** thư mục tài liệu theo ba tầng từ nền tảng đến chuyên sâu.

</div>

## Tiêu chí chọn đề tài

**Những câu hỏi nên đặt ra**

1. Trạng thái hiện tại của bài toán là gì: thuộc P, NP-complete, APX, FPT hay còn khoảng trống mở?
2. Có trường hợp đặc biệt tự nhiên nào đáng khảo sát không (như đồ thị phẳng, bậc bị chặn, đồ thị hình học)?
3. Khoảng cách giữa cận trên thuật toán và cận dưới độ khó nằm ở đâu?
4. Có sẵn bộ dữ liệu hoặc bộ chuẩn kiểm thử (*benchmark*) để đánh giá không?
5. Nhóm nghiên cứu có sẵn nền tảng công cụ phù hợp (như SDP, kernelization, PCP, SAT solver) không?

**Những hướng cần tránh**

- Chọn mục tiêu quá tầm như “chứng minh $$P\neq NP$$” cho luận văn thạc sĩ.
- Cài đặt vét cạn rồi vẽ biểu đồ mà không có thuật toán nền (*baseline*) để so sánh.
- Dùng học sâu tuyên bố “giải bài toán NP-complete” nhưng thiếu thước đo chuẩn và không đối chiếu với các bộ giải chuyên dụng.

## Cấu trúc khung một bài báo

1. Phát biểu hình thức bài toán (nêu rõ cách mã hóa đầu vào).
2. Tổng quan công trình liên quan kèm bảng trạng thái kết quả.
3. Đóng góp chính (thuật toán, chứng minh độ khó hoặc kết quả thực nghiệm).
4. Chứng minh chi tiết hoặc thiết kế thí nghiệm.
5. Giới hạn của phương pháp (dưới giả thuyết ETH, UGC hoặc quy mô dữ liệu).

**Yêu cầu tối thiểu cho phần chứng minh độ khó:** chứng minh thuộc $$NP$$, chỉ ra phép rút gọn từ bài toán nguồn (như 3SAT hoặc IS), chứng minh tương đương hai chiều Có $$\Leftrightarrow$$ Có và chỉ ra phép biến đổi $$f$$ chạy trong thời gian đa thức (theo đúng mẫu ở các bài 20.6–20.9).

## Bộ giải (*Solver*) và thực hành thực nghiệm

Các bộ giải tiêu biểu gồm: **SAT** (Kissat, Glucose), **SMT** (Z3) và **MILP** (SCIP, Gurobi). Khi báo cáo thực nghiệm, cần ghi đầy đủ giới hạn thời gian (*timeout*), hạt giống ngẫu nhiên (*seed*), cấu hình máy, phiên bản phần mềm và kết quả trên toàn bộ tập thể hiện thử nghiệm.

## Lộ trình 12 tuần (dành cho học viên/NCS năm đầu)

| Tuần | Nội dung thực hiện | Sản phẩm đầu ra |
|:---:|:---|:---|
| 1–2 | Ôn 20.1–20.6 và làm lại các bài chứng minh | Sổ tay tổng hợp bổ đề |
| 3–4 | Học 20.7–20.10 | 2 phép rút gọn viết tay hoàn chỉnh |
| 5 | Ôn 20.11 (VC tỉ lệ 2) và đọc Christofides | 1 chứng minh + 1 bản tóm tắt |
| 6 | Học 20.12 (FPT cho VC) và 1 kỹ thuật kernel | Mã nguồn thuật toán cây tìm kiếm |
| 7 | Học 20.13 (ETH và năm thế giới Impagliazzo) | Bài viết tổng hợp khoảng 1500 từ |
| 8 | Hệ thống lại Sipser và Arora–Barak | Bản tóm tắt cô đọng 4 trang |
| 9 | Chọn 1 bài toán mở quy mô nhỏ | Danh mục 15 bài báo có ghi chú |
| 10–11 | Thực hiện hướng nhỏ: hardness, thuật toán hoặc solver | Bản thảo dài 6–8 trang |
| 12 | Trình bày seminar 25 phút | Slide trình bày + danh sách câu hỏi Q&A |

## Thư mục tài liệu theo tầng

**Tầng A (nền tảng bắt buộc):** Sipser; Arora–Barak; Garey–Johnson; CLRS (chương NP-Completeness).

**Tầng B (chọn theo nhánh chuyên sâu):**  
- Thuật toán xấp xỉ: Vazirani; Williamson–Shmoys.  
- Độ phức tạp tham số hóa (FPT): Cygan et al.; Downey–Fellows.  
- Độ phức tạp mịn: các bài khảo sát của V. Vassilevska Williams.  
- Mật mã học lý thuyết: Goldreich; Katz–Lindell.  
- Bộ giải SAT: *Handbook of Satisfiability*.

**Tầng C (bài khảo sát và tổng quan):** Fortnow (CACM); Aaronson (*P vs NP*); Wigderson (*Mathematics and Computation*); Impagliazzo (1995).

**Công trình gốc kinh điển:** Cook (1971); Karp (1972); Levin (1973); Ladner (1975).

## Bản đồ tổng quan Chương 20

| STT | Bài học | Kỹ năng nghiên cứu rèn luyện |
|:---:|:---|:---|
| 1 | Bài toán quyết định và thời gian đa thức | Mã hóa đầu vào |
| 2 | Lớp $$P$$ và Time Hierarchy | Tính đóng, lập luận đường chéo |
| 3 | Lớp $$NP$$: Verifier và NTM | Thiết kế chứng chỉ |
| 4 | $$\mathrm{coNP}$$ và hệ quả cấu trúc | Phân tích cấu trúc lớp |
| 5 | Rút gọn đa thức $$\le_p$$ | So sánh độ khó bài toán |
| 6 | NP-hard và NP-complete | Quy trình chứng minh hardness |
| 7 | Định lý Cook–Levin | Xây dựng bảng cấu hình (tableau) |
| 8 | Rút gọn SAT → 3SAT | Làm chủ bài toán nguồn |
| 9 | IS, CLIQUE, Vertex Cover | Rút gọn trên đồ thị |
| 10 | Chu trình Hamilton và TSP | Độ khó bài toán định tuyến |
| 11 | Thuật toán xấp xỉ | Chứng minh tỉ số xấp xỉ |
| 12 | Parameterized Complexity (FPT) | Phân tích theo tham số |
| 13 | ETH, fine-grained, average-case | Bản đồ độ phức tạp hiện đại |
| 14 | Thực hành nghiên cứu | Triển khai dự án nghiên cứu |

## Bài tập cuối chương

1. **Hồ sơ chứng minh:** biên soạn một tệp PDF gọn gồm 3 chứng minh đầy đủ (tính bắc cầu của $$\le_p$$, xấp xỉ tỉ lệ 2 cho VC và rút gọn $$3\mathrm{SAT}\le_p\mathrm{IS}$$).
2. **Bản đồ tài liệu:** chọn 1 bài toán từ danh mục Garey–Johnson và khảo sát 5 trích dẫn nghiên cứu gần đây về nó.
3. **Đề cương 4 trang:** viết đề cương nghiên cứu theo cấu trúc khung bài báo ở trên.
4. **Trình bày seminar:** chuẩn bị bài nói 25 phút về định lý Cook–Levin hoặc một phép rút gọn dùng gadget.

## Tóm tắt

Hoàn thành các bài 20.1–20.14 giúp bạn có thể tự viết chứng minh độ khó và thuật toán cơ bản, đọc hiểu bài báo độ phức tạp và chọn được hướng mở vừa sức để bắt đầu nghiên cứu cùng giảng viên hướng dẫn.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=YX40hbAHx3s">P vs. NP and the Computational Complexity Zoo</a> — hackerdashery, tiếng Anh. Ôn lại bản đồ các lớp độ phức tạp để định vị trạng thái của đề tài (P, NPC hay còn mở).
- <a href="https://www.youtube.com/watch?v=pQsdygaYcE4">P vs NP Explained: Computer Science&#x27;s Biggest Puzzle</a> — Quanta Magazine, tiếng Anh. Câu chuyện về bài toán mở $$P$$ và $$NP$$ trong bối cảnh nghiên cứu.
- <a href="https://www.youtube.com/watch?v=hNesYirH8gM">Algorithms for NP-Hard Problems (Section 23.5: The Exponential Time Hypothesis)</a> — Tim Roughgarden Lectures, tiếng Anh. Giả thuyết ETH như một ví dụ về giả thiết nghiên cứu cần nắm chính xác phát biểu.
