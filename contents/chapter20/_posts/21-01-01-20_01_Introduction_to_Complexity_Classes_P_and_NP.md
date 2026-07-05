---
layout: post
title: "Giới thiệu Lớp Phức tạp P và NP"
categories: chapter20
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: 'Trong chương này chúng ta nghiên cứu lý thuyết độ phức tạp tính toán — phân loại bài toán theo tài nguyên cần thiết để giải hoặc kiểm tra lời giải. Sắp xếp một triệu số có thể hoàn thành trong vài giây, nhưng tìm đường đi tối ưu qua 50 thành phố có thể đòi hỏi tài nguyên khổng lồ — sự khác biệt này phản ánh bản chất toán học của hai lớp bài toán. Mục 20.1 giới thiệu lớp P và NP, cùng câu hỏi mở $P \stackrel{?}{=} NP$.'
---

<div class="textbook-epigraph" markdown="1">

"The question of whether P equals NP is the deepest open problem in theoretical computer science."

<span class="epigraph-attribution">— Stephen Cook & Richard Karp (problem tradition)</span>

</div>

Trong chương này chúng ta nghiên cứu **lý thuyết độ phức tạp tính toán** — phân loại bài toán theo tài nguyên cần thiết để giải hoặc kiểm tra lời giải. Sắp xếp một triệu số có thể hoàn thành trong vài giây, nhưng tìm đường đi tối ưu qua 50 thành phố có thể đòi hỏi tài nguyên khổng lồ — sự khác biệt này phản ánh bản chất toán học của hai lớp bài toán. Mục 20.1 này giới thiệu lớp **P** và **NP**, cùng câu hỏi mở $$P \stackrel{?}{=} NP$$.

Ở chương 14 chúng ta đã dùng Big-O để so sánh thuật toán cụ thể. Ở chương 18, máy Turing cung cấp mô hình tính toán phổ quát. Bây giờ chúng ta kết hợp hai nền tảng đó: không hỏi "thuật toán A nhanh hơn B bao nhiêu?", mà hỏi "**có tồn tại** thuật toán đa thức cho bài toán này hay không?" — câu trả lời quyết định ranh giới giữa những gì máy tính có thể giải trong thời gian thực tế và những gì buộc phải dùng heuristic, xấp xỉ hoặc chấp nhận timeout.

![Bài toán P vs NP](/discrete-mathematics-for-computer-science-iuh/img/course/Complexity_classes.svg)

<p class="textbook-figure-caption" data-figure="20.1">Quan hệ giữa các lớp phức tạp: P ⊆ NP; câu hỏi mở là liệu hai lớp có trùng nhau.</p>
![So sánh độ phức tạp](/discrete-mathematics-for-computer-science-iuh/img/course/Comparison_computational_complexity.svg)

<p class="textbook-figure-caption" data-figure="20.2">Lớp P: giải trong thời gian đa thức; NP: kiểm tra lời giải (certificate) trong thời gian đa thức.</p>
![Mô hình Turing](/discrete-mathematics-for-computer-science-iuh/img/course/Example_of_a_Turing_machine.svg)

<p class="textbook-figure-caption" data-figure="20.3">Máy Turing đo độ phức tạp thời gian — nền định nghĩa hình thức lớp P và NP.</p>
![Rút gọn đa thức](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="20.4">Rút gọn đa thức: chuyển instance bài toán A sang instance bài toán B trong thời gian đa thức, giữ nguyên câu trả lời Có/Không.</p>
## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau khi hoàn thành bài này, sinh viên sẽ:

- **Phân biệt** độ phức tạp thời gian đa thức và mũ, và giải thích vì sao ranh giới này có ý nghĩa thực tế.
- **Định nghĩa** hình thức lớp **P** và lớp **NP** dưới dạng bài toán quyết định.
- **Hiểu** đặc trưng theo bộ kiểm tra (verifier characterization) của NP.
- **Nắm** khái niệm rút gọn đa thức (polynomial-time reduction) và NP-đầy đủ (NP-complete).
- **Phát biểu** câu hỏi $$P \stackrel{?}{=} NP$$ và hệ quả đối với mật mã học, tối ưu hóa và trí tuệ nhân tạo.

**Từ khóa**: lớp P, lớp NP, bài toán quyết định (decision problem), bộ kiểm tra (verifier), certificate, rút gọn đa thức (polynomial-time reduction), NP-đầy đủ (NP-complete), NP-hard, định lý Cook–Levin, $$P \stackrel{?}{=} NP$$.
</div>

## Ôn tập Big-O, $$\Theta$$ và $$\Omega$$

Chương 14 đã giới thiệu ký hiệu tăng trưởng. Trong lý thuyết độ phức tạp, chúng ta quan tâm đặc biệt đến hai họ hàm:

| Họ hàm | Ví dụ | Ý nghĩa trong thực tế |
|:---|:---|:---|
| **Đa thức** | $$O(n)$$, $$O(n^2)$$, $$O(n^3 \log n)$$ | Khả thi khi $$n$$ lớn (vài triệu, vài tỷ) |
| **Mũ** | $$O(2^n)$$, $$O(n!)$$ | Chỉ khả thi khi $$n$$ nhỏ (thường $$n < 30$$) |

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một hàm $$f(n)$$ là **đa thức** (polynomial) nếu tồn tại hằng số $$k$$ sao cho $$f(n) = O(n^k)$$. Thời gian **đa thức** (polynomial time) nghĩa là số bước máy Turing (hoặc số phép cơ bản) được giới hạn bởi một đa thức theo kích thước input.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ** (so sánh bậc tăng trưởng):

Với $$n = 1000$$:

- $$n^2 = 10^6$$ — vài mili-giây trên CPU hiện đại.
- $$2^n \approx 10^{300}$$ — lớn hơn số nguyên tử trong vũ trụ quan sát được.

Vì vậy, khi nói một bài toán "thuộc P", chúng ta đang nói: **có thuật toán** mà thời gian chạy là đa thức theo kích thước input được mã hóa hợp lý — không phải mũ.
</div>

**Lưu ý quan trọng**: Big-O bỏ qua hằng số và số hạng bậc thấp. Thuật toán $$O(n^3)$$ vẫn thuộc P dù chậm hơn $$O(n)$$; nhưng $$O(2^n)$$ **không** thuộc P vì mũ không bị bao bởi bất kỳ $$n^k$$ nào.

## Bài toán quyết định và mã hóa đầu vào

Lý thuyết độ phức tạp thường nghiên cứu **bài toán quyết định** — chỉ trả lời Có hoặc Không.

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Một **bài toán quyết định** là tập ngôn ngữ $$L \subseteq \Sigma^*$$ trên bảng chữ cái $$\Sigma$$. Với input $$w \in \Sigma^*$$, câu hỏi là: $$w \in L$$ không?
</div>

<div class="textbook-example" markdown="1">
**Ví dụ** (bài toán quyết định):

| Tên | Câu hỏi | Input mã hóa |
|:---|:---|:---|
| **PATH** | Có đường đi từ $$s$$ đến $$t$$ trong đồ thị $$G$$ không? | Mã hóa $$G$$, $$s$$, $$t$$ dưới dạng chuỗi nhị phân |
| **PRIMES** | Số $$p$$ cho trước có phải số nguyên tố không? | Mã hóa $$p$$ ở hệ nhị phân |
| **SAT** | Công thức logic mệnh đề có thỏa mãn không? | Mã hóa công thức dạng CNF |
</div>

**Kích thước input** $$|w|$$ là độ dài chuỗi mã hóa (thường hệ nhị phân). Đây là thước đo duy nhất dùng trong định nghĩa P và NP — không dùng "số đỉnh" hay "số bit của một số" riêng lẻ nếu chúng không phản ánh độ dài chuỗi mã hóa đầy đủ.

**Máy Turing** (chương 18) là mô hình chuẩn để đo thời gian: mỗi bước chuyển trạng thái tính là một đơn vị thời gian. Theo **luận đề Church–Turing**, mọi mô hình tính toán "hợp lý" (RAM, Python, C++) đều có thể mô phỏng bởi TM với overhead đa thức — nên phân loại P/NP không phụ thuộc ngôn ngữ lập trình cụ thể.

## Lớp P — thời gian đa thức tất định

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Lớp **P** (polynomial time) là tập các bài toán quyết định $$L$$ mà tồn tại máy Turing **tất định** $$M$$ và đa thức $$p(n)$$ sao cho: với mọi input $$w$$ có $$|w| = n$$, $$M$$ dừng sau tối đa $$p(n)$$ bước và chấp nhận $$w$$ khi và chỉ khi $$w \in L$$.
</div>

Nói ngắn gọn: **P** = những bài toán **có thể giải** trong thời gian đa thức.

<div class="textbook-example" markdown="1">
**Ví dụ** (bài toán trong P):

- **PATH**: BFS hoặc DFS trên đồ thị — $$O(|V| + |E|)$$, đa thức theo kích thước mã hóa đồ thị.
- **MATCHING** (cặp ghép trên đồ thị hai phía): thuật toán Hopcroft–Karp — $$O(E\sqrt{V})$$.
- **PRIMES** (Miller–Rabin, AKS): kiểm tra tính nguyên tố trong thời gian đa thức theo số bit của $$p$$.
- **Sắp xếp**, **tìm kiếm nhị phân**, **nhân ma trận** (Strassen), **shortest path** (Dijkstra với heap).
</div>

<div class="content-box insight-box textbook-block" markdown="1">
**Nhận xét**: Thuộc P không có nghĩa là "chạy nhanh trên mọi input". Thuật toán $$O(n^3)$$ với $$n = 10^6$$ vẫn có thể timeout trong sản phẩm — nhưng về mặt lý thuyết, ta **biết** cách giải chính xác trong thời gian đa thức. Đó là điểm khác biệt với NP-hard.
</div>

## Lớp NP — kiểm tra nhanh hơn tìm kiếm?

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Lớp **NP** (nondeterministic polynomial time) là tập các bài toán quyết định $$L$$ mà tồn tại máy Turing **không tất định** $$N$$ và đa thức $$p(n)$$ sao cho: $$w \in L$$ khi và chỉ khi **tồn tại** một nhánh tính toán của $$N$$ chấp nhận $$w$$ trong tối đa $$p(|w|)$$ bước.
</div>

Định nghĩa trên dùng máy không tất định (NTM). Trong thực hành, định nghĩa tương đương và trực quan hơn là **đặc trưng bộ kiểm tra**:

<div class="textbook-theorem" markdown="1">
**Định lý** (đặc trưng bộ kiểm tra): $$L \in NP$$ khi và chỉ khi tồn tại đa thức $$p(n)$$ và thuật toán tất định **Verify** chạy trong thời gian đa thức sao cho:

$$w \in L \iff \exists\, \text{certificate } c,\; |c| \leq p(|w|),\; \text{Verify}(w, c) = \text{chấp nhận}$$
</div>

**Certificate** (chứng cứ, lời giải đề xuất) là thông tin ngắn mà nếu đúng, ta có thể **kiểm tra** nhanh. Tìm certificate từ đầu có thể khó; kiểm tra thường dễ.

<div class="textbook-example" markdown="1">
**Ví dụ** (NP và certificate):

| Bài toán | Certificate | Cách verify |
|:---|:---|:---|
| **SAT** | Gán true/false cho mỗi biến | Kiểm tra mỗi clause trong $$O(1)$$, tổng đa thức |
| **HAMILTON-PATH** | Danh sách đỉnh tạo đường Hamilton | Kiểm tra cạnh liên tiếp, không lặp đỉnh |
| **SUBSET-SUM** | Tập con các số | Cộng và so sánh với target |
| **CLIQUE** | Tập $$k$$ đỉnh | Kiểm tra mọi cặp có cạnh |

Mỗi bài trên: nếu ai đó **đưa** cho ta certificate, ta verify trong thời gian đa thức — đó là định nghĩa thực dụng của NP.
</div>

**Quan hệ cơ bản**: $$P \subseteq NP$$. Nếu ta giải được bài toán trong thời gian đa thức, ta cũng có thể verify (chạy lại thuật toán giải và so sánh). Câu hỏi mở: liệu mọi bài **kiểm tra nhanh** cũng **giải nhanh** được?

## SAT và định lý Cook–Levin

**SAT** (Boolean satisfiability): cho công thức logic mệnh đề ở dạng CNF, hỏi có tồn tại gán giá trị chân lý làm công thức đúng không?

Đây là bài toán đầu tiên được chứng minh **NP-đầy đủ** — kết quả nền tảng của Stephen Cook (1971) và độc lập Leonid Levin.

![Stephen Cook — định lý Cook–Levin](/discrete-mathematics-for-computer-science-iuh/img/course/stephen_cook.svg)

<p class="textbook-figure-caption" data-figure="20.5">Stephen Cook (sinh 1939) — định lý Cook–Levin (1971): SAT là NP-đầy đủ.</p>
![Richard Karp — 21 bài NP-complete](/discrete-mathematics-for-computer-science-iuh/img/course/richard_karp.svg)

<p class="textbook-figure-caption" data-figure="20.6">Richard Karp (sinh 1935) — mở rộng danh sách 21 bài NP-complete cổ điển bằng rút gọn từ SAT.</p>
<div class="textbook-theorem" markdown="1">
**Định lý** (Cook–Levin): Bài toán **SAT** là **NP-đầy đủ** (NP-complete).
</div>

Ý nghĩa: SAT không chỉ thuộc NP — nó còn là bài toán **"khó nhất"** trong NP theo nghĩa rút gọn đa thức (mục sau). Nếu ai đó tìm được thuật toán đa thức cho SAT, thì **mọi** bài trong NP đều có thuật toán đa thức — tức là $$P = NP$$.

<div class="textbook-example" markdown="1">
**Ví dụ** (instance SAT nhỏ):

Công thức CNF: $$(x \lor y) \land (\neg x \lor z) \land (\neg y \lor \neg z)$$

Certificate: $$x = \text{true}$$, $$y = \text{false}$$, $$z = \text{true}$$.

Verify: $$(x \lor y)$$ đúng; $$(\neg x \lor z)$$ đúng vì $$z$$ đúng; $$(\neg y \lor \neg z)$$ đúng vì $$\neg y$$ đúng. Cả ba clause thỏa — công thức **thỏa mãn**, đáp án Có.
</div>

## Rút gọn đa thức và NP-đầy đủ

<div class="textbook-definition" markdown="1">
**Định nghĩa**: Cho hai bài toán quyết định $$A$$ và $$B$$. Một **rút gọn đa thức** (polynomial-time reduction) từ $$A$$ sang $$B$$, ký hiệu $$A \leq_p B$$, là hàm $$f$$ tính được trong thời gian đa thức sao cho:

$$w \in A \iff f(w) \in B$$

với mọi input $$w$$.
</div>

Nếu $$A \leq_p B$$ và $$B \in P$$, thì $$A \in P$$. Ngược lại, nếu $$A$$ là NP-hard và $$A \leq_p B$$, thì $$B$$ cũng NP-hard.

<div class="textbook-definition" markdown="1">
**Định nghĩa**:

- **NP-hard**: mọi bài $$L \in NP$$ đều thỏa $$L \leq_p A$$ (có thể $$A \notin NP$$).
- **NP-complete**: $$A \in NP$$ **và** $$A$$ là NP-hard.
</div>

Sau Cook–Levin, Richard Karp (1972) chứng minh hàng loạt bài NP-complete bằng cách rút gọn từ SAT hoặc **3-SAT** (mỗi clause đúng 3 literal):

| Bài toán | Mô tả ngắn | Rút gọn từ |
|:---|:---|:---|
| **3-SAT** | SAT với mỗi clause 3 literal | SAT |
| **CLIQUE** | Đồ thị có clique kích thước $$k$$? | 3-SAT |
| **VERTEX-COVER** | Tập phủ đỉnh kích thước $$k$$? | CLIQUE |
| **SUBSET-SUM** | Tập con có tổng bằng $$t$$? | 3-SAT |
| **HAMILTON-PATH** | Đồ thị có đường Hamilton? | 3-SAT |
| **TSP** (decision) | Tour có tổng chi phí $$\leq B$$? | HAMILTON-PATH |

<div class="textbook-example" markdown="1">
**Ví dụ** (ý tưởng rút gọn CLIQUE từ 3-SAT — trực giác):

Cho công thức 3-SAT với $$m$$ clause và $$n$$ biến. Xây đồ thị $$G$$: mỗi **clause gadget** tạo một nhóm 3 đỉnh (ứng với 3 literal); nối cạnh giữa các literal **không mâu thuẫn** (không có $$x$$ và $$\neg x$$). Công thức thỏa mãn ⟺ $$G$$ có clique kích thước $$m$$ (chọn đúng một literal mỗi clause, không mâu thuẫn).

Chi tiết chứng minh dài — ở đây ta chỉ cần nhớ: **một lần rút gọn đúng** đủ để kế thừa NP-hardness.
</div>

<div class="content-box note-box textbook-block" markdown="1">
**Tài liệu tham khảo**

- Rosen, K. H. (2019). *Discrete Mathematics and Its Applications* (8th ed.), Ch. 3.3 và 13.5.
- Sipser, M. (2012). *Introduction to the Theory of Computation* (3rd ed.), Ch. 7.
- Cormen, T. H. et al. (2022). *Introduction to Algorithms* (4th ed.), Ch. 34: NP-Completeness.
</div>

## Câu hỏi $$P \stackrel{?}{=} NP$$ và hệ quả

<div class="textbook-theorem" markdown="1">
**Câu hỏi mở** (Millennium Prize — Clay Mathematics Institute): $$P = NP$$ hay $$P \neq NP$$?
</div>

**Nếu $$P = NP$$** (ít người tin):

- Mật mã đối xứng và nhiều hệ thống bảo mật dựa trên bài toán NP-hard sẽ suy yếu.
- Tối ưu hóa tổ hợp (lịch trình, routing, packing) có thể giải chính xác đa thức.
- Sáng tạo "máy móc" — nhiều bài sáng tạo có thể coi là tìm certificate.

**Nếu $$P \neq NP$$** (giả định an toàn của hầu hết nhà khoa học):

- Có bài **kiểm tra nhanh** nhưng **không có** thuật toán giải đa thức tổng quát.
- Heuristic, approximation, SAT-solver, ILP với time limit là công cụ thực tế — không phải "tạm thời" mà là **thiết kế đúng**.

<div class="textbook-example" markdown="1">
**Ví dụ** (hệ quả thực tế):

- **RSA**: nhân hai số nguyên tố lớn dễ (P); phân tích ngược khó (believed ∉ P) — nền mật mã công khai.
- **Lập lịch CPU / container orchestration**: bài scheduling tổng quát NP-hard — Kubernetes dùng heuristic, không tối ưu toàn cục.
- **Kiểm thử tổ hợp**: $$2^n$$ tổ hợp input — NP-hard; dùng coverage heuristic và fuzzing thay vì exhaustive.
</div>

Các hướng nghiên cứu liên quan: **NP-intermediate** (bài trong NP nhưng chưa biết P hay NP-complete, ví dụ đồ thị đẳng cấu), **parameterized complexity** (FPT khi tham số $$k$$ nhỏ), **approximation algorithms** (đảm bảo tỷ lệ gần optimal), và **quantum computing** (BQP — không giải quyết trực tiếp P vs NP).

## Bài tập

### Bài tập 1: Phân loại bậc tăng trưởng

Sắp xếp các hàm sau theo thứ tự tăng dần (chậm → nhanh): $$n^{100}$$, $$2^n$$, $$n \log n$$, $$n!$$, $$1000$$.

<details>
<summary>Đáp án</summary>

$$1000 < n \log n < n^{100} < 2^n < n!$$ (với $$n$$ đủ lớn). Hằng số $$O(1)$$; log-linear chậm hơn mọi đa thức bậc cố định; mũ chậm hơn giai thừa.

</details>

### Bài tập 2: Bài toán quyết định

Chuyển bài toán tối ưu sau thành bài toán quyết định: "Tìm đường đi ngắn nhất từ $$s$$ đến $$t$$ trong đồ thị có trọng số không âm."

<details>
<summary>Đáp án</summary>

**SHORTEST-PATH** (decision): Cho $$G$$, $$s$$, $$t$$, và ngưỡng $$k$$ — hỏi có đường đi từ $$s$$ đến $$t$$ với tổng trọng số $$\leq k$$ không? Bài tối ưu giải được bằng cách tìm kiếm nhị phân trên $$k$$ hoặc chạy Dijkstra một lần (trong P).

</details>

### Bài tập 3: P hay NP?

Phân loại (giả định kiến thức chuẩn): (a) Kiểm tra ma trận có phải đối xứng; (b) Tìm clique lớn nhất; (c) Kiểm tra tour TSP cho trước có tổng chi phí $$\leq B$$.

<details>
<summary>Đáp án</summary>

(a) **P** — duyệt $$O(n^2)$$ phần tử so sánh đối xứng. (c) **NP** — certificate là danh sách đỉnh, verify $$O(n)$$. (b) **NP-hard** (optimization) — tìm optimal; quyết định "có clique $$\geq k$$" là NP-complete.

</details>

### Bài tập 4: Đặc trưng verifier

Cho bài **SUBSET-SUM**: input là tập số $$S = \{a_1, \ldots, a_n\}$$ và target $$t$$. Mô tả certificate và thuật toán verify.

<details>
<summary>Đáp án</summary>

Certificate: tập chỉ số $$I \subseteq \{1,\ldots,n\}$$ (hoặc bit-mask). Verify: tính $$\sum_{i \in I} a_i$$ và so sánh với $$t$$ — $$O(n)$$, đa thức. Vậy SUBSET-SUM ∈ NP.

</details>

### Bài tập 5: Rút gọn đa thức

Giả sử đã biết **3-SAT** là NP-complete và có rút gọn đa thức **3-SAT** $$\leq_p$$ **CLIQUE**. Điều gì suy ra về CLIQUE?

<details>
<summary>Đáp án</summary>

CLIQUE là **NP-hard** (vì bài NP-complete rút gọn về nó). Nếu thêm chứng minh CLIQUE ∈ NP (có verifier đa thức), thì CLIQUE là **NP-complete**.

</details>

### Bài tập 6: $$P = NP$$?

Giả sử $$P = NP$$. Điều gì xảy ra với bài **PRIMES** (kiểm tra số nguyên tố) và bài **INTEGER-FACTORING** (phân tích số nguyên thành thừa số)?

<details>
<summary>Đáp án</summary>

PRIMES đã biết ∈ P (AKS, 2002). INTEGER-FACTORING chưa biết ∈ P hay NP-complete; hiện believed ∉ P. Nếu $$P = NP$$, mọi bài trong NP có thuật toán đa thức — **có thể** factoring cũng ∈ P, làm suy yếu RSA. Đây là lý do giả định $$P \neq NP$$ quan trọng cho bảo mật, dù chưa chứng minh.

</details>

## Xem thêm / Video gợi ý

- <a href="https://www.youtube.com/watch?v=4jZ5n8k0p0Q">Big O Notation — Intuition</a> — 3Blue1Brown (Growth rates visualized)

## Tóm tắt

- **Big-O / đa thức vs mũ**: ranh giới lý thuyết quyết định bài toán có scalable hay không.
- **Bài toán quyết định** + mã hóa input + máy Turing: nền định nghĩa hình thức.
- **P**: giải trong thời gian đa thức (PATH, MATCHING, PRIMES, …).
- **NP**: kiểm tra certificate trong thời gian đa thức; $$P \subseteq NP$$.
- **Cook–Levin**: SAT là NP-complete đầu tiên; **Karp**: mở rộng danh sách bằng rút gọn đa thức.
- **Rút gọn** $$A \leq_p B$$: chuyển hardness; 3-SAT → CLIQUE → VERTEX-COVER → …
- **$$P \stackrel{?}{=} NP$$**: câu hỏi mở; thiết kế hệ thống an toàn nên giả định $$P \neq NP$$.

Trong bài tiếp theo, chúng ta dịch lý thuyết P/NP sang quyết định thiết kế sản phẩm — Big-O trên code thực, heuristic, profiling và khi nào không hứa optimal đa thức với khách hàng (mục 20.2, Lớp Độ phức tạp trong Kỹ thuật Phần mềm).