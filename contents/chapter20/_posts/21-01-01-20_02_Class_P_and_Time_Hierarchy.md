---
layout: post
title: "Lớp P và Time Hierarchy"
categories: chapter20
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Các bài toán tiêu biểu trong lớp P, tính đóng của P dưới các phép toán cơ bản, định lý phân cấp thời gian (Time Hierarchy) và hệ quả P ⊊ EXPTIME."
---

<div class="textbook-epigraph" markdown="1">

"P is robust — and strictly smaller than exponential time."

<span class="epigraph-attribution">— Time hierarchy spirit</span>

</div>

Sau khi định nghĩa lớp $$P$$, bài học này làm rõ ba điểm: những bài toán tiêu biểu thuộc $$P$$, tính đóng của $$P$$ dưới các phép toán ngôn ngữ cơ bản, và sự tồn tại của các ngôn ngữ nằm **ngoài** $$P$$ nhờ định lý phân cấp thời gian (dù định lý này chưa giải quyết được bài toán $$P$$ và $$NP$$).

Lớp $$P$$ là ngôi nhà của những thuật toán hiệu quả nhất mà khoa học máy tính từng khám phá — từ đường đi ngắn nhất Dijkstra, luồng cực đại, quy hoạch tuyến tính đến kiểm tra số nguyên tố AKS. Nhưng liệu *cho thêm thời gian* có thực sự giúp máy tính giải được những bài toán khó hơn hẳn không? **Định lý Phân cấp Thời gian (Time Hierarchy Theorem)** trả lời dứt khoát là CÓ — bằng đúng kỹ thuật chéo hóa mà ta đã dùng ở Bài toán Dừng, nhưng lần này có gắn thêm "đồng hồ đếm giờ".

## Kiến thức cần nhớ: Ba trụ cột của Lớp $$P$$ và Phân cấp Thời gian

![Lớp P và Định lý Phân cấp Thời gian](/discrete-mathematics-for-computer-science-iuh/img/course/class_p_time_hierarchy.svg)

1. **Những bài toán trụ cột trong $$P$$**:
   `PATH` (BFS/DFS $$O(V+E)$$), `2SAT` (đồ thị kéo theo $$O(n+m)$$), `PRIMES` (thuật toán AKS 2002), `LP` (phương pháp Ellipsoid/điểm trong), `RELPRIME` (Euclid $$O(\log^2 N)$$).
2. **Tính đóng đại số của $$P$$**:
   $$P$$ đóng dưới hợp, giao, phần bù, nối và phép hợp thành đa thức — nghĩa là ghép hai thuật toán chạy nhanh nối tiếp nhau vẫn cho một thuật toán chạy nhanh.
3. **Định lý Phân cấp Thời gian (Time Hierarchy Theorem)**:
   Nếu $$f(n)\log f(n) = o(g(n))$$ (với $$g$$ xây dựng được theo thời gian), thì $$\mathrm{TIME}(f(n)) \subsetneq \mathrm{TIME}(g(n))$$. Hệ quả trực tiếp cực kỳ mạnh: $$P \subsetneq \mathrm{EXP}$$ — chắc chắn tồn tại bài toán quyết định được nhưng **không thể** giải trong thời gian đa thức!

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Liệt kê** các bài toán tiêu biểu thuộc lớp $$P$$ kèm lý do ngắn gọn.
- **Chứng minh** một số tính chất đóng của lớp $$P$$.
- **Phát biểu** định lý phân cấp thời gian đơn định (*Deterministic Time Hierarchy*) và suy ra $$P\subsetneq\mathrm{EXPTIME}$$.

</div>

## Một số bài toán tiêu biểu trong $$P$$

| Bài toán | Lý do thuộc $$P$$ |
|:---|:---|
| Tính liên thông đồ thị (Connectivity) | BFS/DFS trong $$O(V+E)$$ |
| Đường đi ngắn nhất ($$w\ge 0$$) | Thuật toán Dijkstra |
| Ghép cặp cực đại trên đồ thị tổng quát | Thuật toán Edmonds — thời gian đa thức |
| Quy hoạch tuyến tính (Linear programming) | Khachiyan / Karmarkar (mô hình độ dài bit) |
| Kiểm tra tính nguyên tố (Primality) | Thuật toán AKS (2002) $$\in P$$ |

## Tính đóng của lớp $$P$$

<div class="textbook-theorem" markdown="1">

**Định lý.** Nếu $$A,B\in P$$ thì $$A\cup B$$, $$A\cap B$$ và $$\overline{A}$$ đều thuộc $$P$$. Hơn nữa, nếu $$L\in P$$ thì bao đóng Kleene $$L^*\in P$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh (cho bao đóng Kleene).**  
Giả sử thuật toán $$M$$ quyết định $$L$$ trong thời gian $$O(n^k)$$. Với chuỗi đầu vào $$w$$ độ dài $$n$$, ta dùng quy hoạch động với mảng $$S[0..n]$$: khởi tạo $$S[0]=\mathrm{true}$$ và tính $$S[j]=\bigvee_{i<j}\bigl(S[i]\land M(w_{i+1..j})\bigr)$$. Có $$O(n^2)$$ cặp chỉ số $$(i,j)$$, mỗi lần kiểm tra gọi $$M$$ trên chuỗi con độ dài $$\le n$$, nên tổng thời gian là $$O(n^{k+2})$$ — vẫn là đa thức.

</div>

*(Đối với hợp, giao và bù: chỉ cần chạy tuần tự hai thuật toán hoặc đảo ngược kết quả đầu ra.)*

## Định lý phân cấp thời gian (*Time Hierarchy*)

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Hàm $$t(n)$$ được gọi là **xây dựng được theo thời gian** (*time-constructible*) nếu tồn tại máy Turing nhận đầu vào $$1^n$$, chạy trong khoảng $$O(t(n))$$ bước và ghi ra giá trị nhị phân của $$t(n)$$.

</div>

<div class="textbook-theorem" markdown="1">

**Định lý** (Hartmanis–Stearns). Nếu $$t_1,t_2$$ là các hàm xây dựng được theo thời gian và $$t_1(n)\log t_1(n)=o(t_2(n))$$ thì

$$
\mathrm{TIME}(t_1(n))\subsetneq\mathrm{TIME}(t_2(n)).
$$

</div>

**Ý tưởng chứng minh:** dùng lập luận đường chéo (*diagonalization*) — xây dựng một máy Turing chạy trong thời gian $$t_2$$ để mô phỏng mọi máy chạy trong thời gian $$t_1$$ rồi đảo ngược kết quả (xem Sipser hoặc Arora–Barak).

<div class="textbook-lemma" markdown="1">

**Hệ quả.** $$P\subsetneq\mathrm{EXPTIME}=\bigcup_k\mathrm{TIME}(2^{n^k})$$.

</div>

**Lưu ý nghiên cứu.** Định lý phân cấp thời gian **không** tách được $$P$$ khỏi $$NP$$ vì kỹ thuật đường chéo đơn giản có tính tương đối hóa (*relativize*), chưa đủ tinh tế để phân biệt tính đơn định và không đơn định.

### Giải thích: Hiểu cơ chế "Chéo hóa có đồng hồ" trong Định lý Phân cấp Thời gian

Vì sao ta chứng minh được $$\mathrm{TIME}(n^2) \subsetneq \mathrm{TIME}(n^4)$$ một cách chặt chẽ?
1. Ta xây một máy Turing $$D$$ chạy trong thời gian $$O(n^4)$$ nhận mã nguồn $$\langle M \rangle$$ làm đầu vào (độ dài $$n = \vert \langle M \rangle \vert$$).
2. $$D$$ đặt một **đồng hồ đếm ngược** $$T = n^3$$ bước, rồi dùng máy Turing phổ dụng mô phỏng $$M(\langle M \rangle)$$ từng bước một (phụ phí mô phỏng thêm thừa số $$\log n$$, tổng cộng vẫn nhỏ hơn $$n^4$$).
3. Nếu $$M(\langle M \rangle)$$ dừng trước khi hết giờ: $$D$$ **lật ngược đáp án** (nếu $$M$$ chấp nhận thì $$D$$ từ chối và ngược lại). Nếu hết $$n^3$$ bước mà $$M$$ chưa dừng: $$D$$ tự động từ chối.

**Kiểm tra mâu thuẫn:** Giả sử có máy $$M^*$$ chạy trong $$c \cdot n^2$$ bước giải được ngôn ngữ $$L(D)$$. Chọn phiên bản đệm dài của $$\langle M^* \rangle$$ sao cho $$n > c$$ (tức $$c \cdot n^2 < n^3$$). Khi chạy $$D(\langle M^* \rangle)$$, đồng hồ $$n^3$$ **đủ giờ** để mô phỏng trọn vẹn $$M^*(\langle M^* \rangle)$$ rồi lật ngược đáp án — mâu thuẫn! Do đó $$L(D) \in \mathrm{TIME}(n^4) \setminus \mathrm{TIME}(n^2)$$.

## Bài tập

1. Chứng minh chi tiết: nếu $$A,B\in P$$ thì $$A\cap B\in P$$.
2. Giải thích vì sao một thuật toán chạy trong $$O(n^{100})$$ thuộc lớp $$P$$ nhưng hầu như vô dụng trong thực tế.
3. Đọc phần phác thảo chứng minh phân cấp thời gian trong Sipser và so sánh kỹ thuật đường chéo với kỹ thuật của Cook–Levin.

## Tài liệu đọc thêm

Arora–Barak §1.4 (Time Hierarchy); Sipser (phần nâng cao về phân cấp thời gian).

## Tóm tắt

Lớp $$P$$ đóng dưới các phép toán cơ bản và định lý phân cấp thời gian chứng minh tồn tại các bài toán nằm ngoài $$P$$ ($$P \subsetneq \mathrm{EXPTIME}$$), dù chưa giải quyết câu hỏi $$P$$ so với $$NP$$.

**Bài tiếp theo:** 20.3 — Lớp $$NP$$: bộ kiểm chứng (*verifier*) và máy Turing không đơn định (NTM).

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=XV6f7XYUMg8">What Makes P vs. NP So Hard? (P ≠ EXPTIME, Time Hierarchy, Baker-Gill-Solovay)</a> — Undefined Behavior, tiếng Anh. Giải thích cách phân cấp thời gian tách $$P$$ khỏi lớp hàm mũ và vì sao tách $$P$$ với $$NP$$ lại khó.
- <a href="https://www.youtube.com/watch?v=l2aXF0B2E9M">What is the Time Hierarchy Theorem? - Easy Theory</a> — Easy Theory, tiếng Anh. Trình bày định lý phân cấp thời gian tương ứng với mục 3 của bài.
- <a href="https://www.youtube.com/watch?v=YX40hbAHx3s">P vs. NP and the Computational Complexity Zoo</a> — hackerdashery, tiếng Anh. Vị trí của lớp $$P$$ trong bản đồ các lớp độ phức tạp.
