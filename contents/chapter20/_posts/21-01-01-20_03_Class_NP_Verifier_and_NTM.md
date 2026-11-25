---
layout: post
title: "Lớp NP: Verifier và NTM"
categories: chapter20
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Hai định nghĩa tương đương của lớp NP qua bộ kiểm chứng (verifier) và máy Turing không đơn định (NTM), chứng minh P⊆NP và ví dụ chứng chỉ cho các bài toán kinh điển."
---

<div class="textbook-epigraph" markdown="1">

"NP is the class of problems with short, efficiently checkable proofs of YES answers."

<span class="epigraph-attribution">— Verifier view of NP</span>

</div>

Với bài toán người du lịch (TSP), **kiểm tra** một hành trình cho sẵn rất dễ, nhưng **tìm ra** hành trình tối ưu lại rất khó. Lớp $$NP$$ hình thức hóa đúng trực giác “mọi câu trả lời Có đều có một chứng chỉ ngắn kiểm tra được nhanh”.

![Verifier](/discrete-mathematics-for-computer-science-iuh/img/course/Complexity_verifier.svg)

<p class="textbook-figure-caption" data-figure="20.2">$$x\in L$$ khi và chỉ khi tồn tại chứng chỉ $$c$$ đủ ngắn sao cho bộ kiểm chứng $$V(x,c)=\mathrm{Yes}$$.</p>

Giải một câu đố Sudoku cỡ $$100 \times 100$$ từ đầu có thể tốn hàng thế kỷ, nhưng nếu ai đó đưa cho bạn một bảng đã điền sẵn và bảo *"Đây là lời giải!"*, bạn chỉ mất vài giây để kiểm tra từng hàng, từng cột và từng ô vuông xem có đúng không. Sự bất đối xứng kỳ lạ giữa **tự tìm lời giải** và **kiểm chứng một lời giải cho sẵn** chính là linh hồn của lớp $$NP$$ và bài toán thiên niên kỷ trị giá 1 triệu USD: **$$P \stackrel{?}{=} NP$$**.

## Kiến thức cần nhớ: Ba trụ cột của Lớp $$NP$$

1. **Định nghĩa theo Bộ kiểm chứng (Polynomial-Time Verifier)**:
   $$L \in NP$$ khi và chỉ khi tồn tại thuật toán đa thức $$V(x, c)$$ sao cho $$x \in L \iff \exists c$$ (độ dài $$\vert c \vert \le \text{poly}(\vert x \vert)$$) để $$V(x, c) = 1$$. Chuỗi $$c$$ gọi là **chứng chỉ (certificate / witness)**.
2. **Định nghĩa tương đương theo Máy Turing Không đơn định (NTM)**:
   NTM giải $$L$$ bằng đúng 2 pha: *Đoán không đơn định* chứng chỉ $$c$$ trong thời gian đa thức, rồi *kiểm chứng đơn định* bằng $$V(x, c)$$. (Lưu ý: $$NP$$ viết tắt của *Nondeterministic Polynomial*, **không phải** "Non-Polynomial"!).
3. **Chuỗi bao hàm căn bản $$P \subseteq NP \subseteq \mathrm{EXP}$$**:
   Mọi bài toán trong $$P$$ đều thuộc $$NP$$ (chỉ cần bỏ qua chứng chỉ và tự giải); mọi bài toán trong $$NP$$ đều giải được trong $$\mathrm{EXP}$$ bằng cách vét cạn tất cả $$2^{\text{poly}(n)}$$ chứng chỉ khả dĩ.

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** lớp $$NP$$ theo hai cách (bộ kiểm chứng và NTM) và **chứng minh** chúng tương đương.
- **Chứng minh** quan hệ bao hàm $$P\subseteq NP$$.
- **Xây dựng** chứng chỉ (*certificate*) và bộ kiểm chứng (*verifier*) cho SAT, chu trình Hamilton và bài toán 3-Coloring.

</div>

## Định nghĩa theo bộ kiểm chứng (*verifier*)

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Ngôn ngữ $$L\in NP$$ nếu tồn tại đa thức $$p$$ và máy Turing đơn định $$V$$ thỏa mãn:

1. $$V(x,c)$$ chạy trong thời gian $$\mathrm{poly}(\lvert x\rvert)$$ (tự động từ chối nếu $$\lvert c\rvert>p(\lvert x\rvert)$$).
2. **Tính đầy đủ:** nếu $$x\in L$$ thì tồn tại chứng chỉ $$c$$ sao cho $$V(x,c)=1$$.
3. **Tính đúng đắn:** nếu $$x\notin L$$ thì với mọi chứng chỉ $$c$$, $$V(x,c)=0$$.

</div>

## Định nghĩa theo máy Turing không đơn định (NTM)

<div class="textbook-definition" markdown="1">

**Định nghĩa.** $$NP=\bigcup_k\mathrm{NTIME}(n^k)$$, tức là tập các ngôn ngữ được chấp nhận bởi một máy Turing không đơn định trong thời gian đa thức (chấp nhận khi tồn tại ít nhất một nhánh tính toán trả lời Có).

</div>

<div class="textbook-theorem" markdown="1">

**Định lý** (Tính tương đương). Hai định nghĩa của lớp $$NP$$ thông qua bộ kiểm chứng và thông qua NTM là tương đương nhau.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.**  
*Từ NTM sang verifier:* chọn chứng chỉ $$c$$ là dãy các lựa chọn không đơn định (hoặc chuỗi cấu hình) dọc theo một nhánh chấp nhận; bộ kiểm chứng $$V$$ mô phỏng đơn định theo dãy đó, kiểm tra từng bước chuyển $$\delta$$ hợp lệ và kết thúc ở trạng thái chấp nhận.  
*Từ verifier sang NTM:* máy không đơn định đoán trước một chuỗi $$c$$ có độ dài $$\le p(\lvert x\rvert)$$, sau đó chạy bộ kiểm chứng đơn định $$V(x,c)$$.

</div>

## Quan hệ $$P\subseteq NP$$

<div class="textbook-theorem" markdown="1">

**Định lý.** $$P\subseteq NP$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.** Nếu $$L\in P$$ thì tồn tại thuật toán đơn định thời gian đa thức $$A$$ quyết định $$L$$. Đặt bộ kiểm chứng $$V(x,c):=A(x)$$ (bỏ qua chứng chỉ $$c$$). Khi đó tính đầy đủ, tính đúng đắn và thời gian đa thức đều thỏa mãn hiển nhiên.

</div>

## Ví dụ chứng chỉ cho một số bài toán kinh điển

| Bài toán | Chứng chỉ $$c$$ | Thao tác của bộ kiểm chứng $$V$$ |
|:---|:---|:---|
| SAT | Một phép gán chân trị cho các biến | Thay vào công thức và tính giá trị đúng/sai |
| Chu trình Hamilton | Một hoán vị các đỉnh | Kiểm tra có đủ $$n$$ cạnh hợp lệ tạo thành chu trình kín |
| 3-Coloring | Phép gán màu trong $$\{1,2,3\}^V$$ | Kiểm tra mọi cạnh đều nối hai đỉnh khác màu |
| Subset Sum | Một tập con các phần tử | Cộng các phần tử và so sánh với tổng mục tiêu |

### Giải thích: Thiết kế tay cặp (Chứng chỉ $$c$$, Bộ kiểm chứng $$V$$) cho 3 bài toán kinh điển

| Bài toán quyết định | Đầu vào $$x$$ | Chứng chỉ $$c$$ (kích thước đa thức) | Thuật toán kiểm chứng $$V(x, c)$$ | Thời gian kiểm chứng |
| :--- | :--- | :--- | :--- | :---: |
| **`SAT`** | Công thức CNF $$\varphi$$ có $$n$$ biến, $$m$$ mệnh đề | Phép gán $$n$$ bit $$(b_1, \dots, b_n) \in \{0,1\}^n$$ | Thay từng bit vào $$\varphi$$, kiểm tra mọi mệnh đề đều Đúng | $$O(n + m)$$ |
| **`CLIQUE`** | Đồ thị $$G=(V,E)$$ và số nguyên $$k$$ | Tập $$k$$ đỉnh $$S = \{v_1, \dots, v_k\} \subseteq V$$ | Kiểm tra đủ $$k$$ đỉnh phân biệt và mọi cặp $$(u,v) \in S$$ đều có cạnh | $$O(k^2)$$ |
| **`SUBSET-SUM`** | Tập số nguyên $$A = \{a_1,\dots,a_n\}$$ và đích $$t$$ | Tập chỉ số $$I \subseteq \{1,\dots,n\}$$ | Cộng các số $$\sum_{i \in I} a_i$$ và so sánh có bằng $$t$$ không | $$O(n \log t)$$ |

**Cảnh báo lỗi kinh điển:** Nếu bạn chỉ dùng thuật toán quay lui vét cạn để tìm nghiệm mà không chỉ ra chứng chỉ $$c$$ ngắn, bạn chưa chứng minh được bài toán thuộc $$NP$$. Trong mọi bài chứng minh $$A \in NP$$, chỉ cần viết đúng 3 dòng: (1) $$c$$ là gì, (2) vì sao $$\vert c \vert = \text{poly}(\vert x \vert)$$, và (3) bộ kiểm chứng $$V(x, c)$$ chạy đa thức ra sao.

## Bài tập

1. Viết giả mã bộ kiểm chứng cho bài toán chu trình Hamilton (HC) và phân tích thời gian chạy.
2. Giải thích vì sao chứng minh $$P\subseteq NP$$ không suy ra được gì về chiều ngược lại $$NP\subseteq P$$.
3. Với bài toán quyết định một số nguyên có phải là hợp số (Composite), chứng chỉ $$c$$ là gì?

## Tài liệu đọc thêm

Sipser (phần $$NP$$); Arora–Barak §2.1.

## Tóm tắt

Lớp $$NP$$ gồm các bài toán có chứng chỉ ngắn kiểm tra được trong thời gian đa thức; hai định nghĩa qua verifier và NTM tương đương nhau, và luôn có $$P\subseteq NP$$.

**Bài tiếp theo:** 20.4 — Lớp $$\mathrm{coNP}$$ và các hệ quả cấu trúc.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=YX40hbAHx3s">P vs. NP and the Computational Complexity Zoo</a> — hackerdashery, tiếng Anh. Giới thiệu lớp $$NP$$ dưới góc nhìn chứng chỉ ngắn kiểm tra nhanh.
- <a href="https://www.youtube.com/watch?v=gQnPM6sydkk">Nondeterministic Turing Machine (Part 1)</a> — Neso Academy, tiếng Anh. Máy Turing không đơn định tương ứng với định nghĩa NTM trong bài.
- <a href="https://www.youtube.com/watch?v=e2cF8a5aAhE">8. NP-Hard and NP-Complete Problems</a> — Abdul Bari, tiếng Anh. Kết nối khái niệm bộ kiểm chứng sang lớp NP-complete.
