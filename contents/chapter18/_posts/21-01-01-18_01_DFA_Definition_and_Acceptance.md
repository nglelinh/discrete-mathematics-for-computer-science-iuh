---
layout: post
title: "Định nghĩa DFA và Ngôn ngữ Chấp nhận"
categories: chapter18
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Bộ năm định nghĩa DFA, hàm chuyển mở rộng δ̂, ngôn ngữ chấp nhận L(M), biểu diễn bằng sơ đồ/bảng và tính duy nhất của đường chạy."
---

> **Câu chuyện mở đầu:** Trước khi có trình biên dịch, công cụ tìm kiếm Regex hay giao thức mạng TCP, các nhà toán học cần một mô hình máy tính tối giản nhất có thể: **bộ nhớ chỉ chứa đúng hữu hạn trạng thái**, đọc từng ký tự từ trái sang phải, không được quay lại và không có RAM mở rộng! Đó chính là **Ô-tô-mát hữu hạn tất định (DFA)** — viên gạch đầu tiên của Lý thuyết Tính toán và Ngôn ngữ Hình thức!

<div class="textbook-epigraph" markdown="1">

"A finite automaton is a mathematical model of computation with a finite amount of memory."

<span class="epigraph-attribution">— Hopcroft & Ullman spirit</span>

</div>

Máy hữu hạn trạng thái là một mô hình tính toán sử dụng **bộ nhớ hữu hạn**, được biểu diễn bằng tập các trạng thái. Bài học này trình bày định nghĩa hình thức của **ô-tô-mát hữu hạn đơn định (DFA)** và ngôn ngữ mà nó chấp nhận — nền tảng cho toàn bộ chương về ô-tô-mát.

![DFA chẵn 1](/discrete-mathematics-for-computer-science-iuh/img/course/Automata_dfa_even_ones.svg)

<p class="textbook-figure-caption" data-figure="18.1">DFA kiểm tra tính chẵn lẻ: chấp nhận các chuỗi nhị phân có số bit 1 là số chẵn.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** DFA bằng bộ năm $$M=(Q,\Sigma,\delta,q_0,F)$$.
- **Mở rộng** hàm chuyển sang $$\hat\delta$$ trên chuỗi và định nghĩa ngôn ngữ $$L(M)$$.
- **Chứng minh** tính duy nhất của đường chạy trên DFA.

</div>

## Bản đồ kiến thức nền: DFA là gì và nằm ở đâu trên Thang Chomsky?

### 1. Bộ 5 thành phần $$M = (Q, \Sigma, \delta, q_0, F)$$
- **Bản chất:** $$Q$$ là tập hữu hạn trạng thái (bộ nhớ!), $$\Sigma$$ là bảng chữ cái đầu vào, $$\delta: Q \times \Sigma \to Q$$ là hàm chuyển trạng thái **tất định** (tại mỗi trạng thái, với mỗi ký tự chỉ có **đúng 1** mũi tên đi ra!), $$q_0$$ là trạng thái khởi đầu, và $$F \subseteq Q$$ là tập trạng thái kết thúc (chấp nhận).

### 2. Hàm chuyển mở rộng $$\hat{\delta}(q, w)$$ & Ngôn ngữ Chấp nhận $$L(M)$$
- **Bản chất:** Đọc hết chuỗi $$w = a_1 a_2 \dots a_n$$ bằng quy nạp $$\hat{\delta}(q, wa) = \delta(\hat{\delta}(q, w), a)$$. Chuỗi $$w$$ được chấp nhận khi và chỉ khi trạng thái dừng cuối cùng nằm trong $$F$$!

### 3. Nền móng của Trình biên dịch (Lexical Analyzer) & Giao thức
- **Ứng dụng:** Bộ tách từ khóa/biến/số trong trình biên dịch (Lexer) và máy trạng thái giao thức mạng (TCP state machine) đều chạy trực tiếp trên DFA với tốc độ siêu nhanh **$$O(\lvert w\rvert)$$** và bộ nhớ **$$O(1)$$**!

## Ví dụ tính tay cầm tay chỉ việc: Chạy DFA kiểm tra "Số lượng bit `1` là CHẴN"

Xét DFA 2 trạng thái $$Q = \{q_{\text{chẵn}}, q_{\text{lẻ}}\}$$, $$q_0 = q_{\text{chẵn}}$$, $$F = \{q_{\text{chẵn}}\}$$:
- Đọc `0`: giữ nguyên trạng thái; đọc `1`: đổi giữa $$q_{\text{chẵn}} \leftrightarrow q_{\text{lẻ}}$$.

Chạy tay hàm chuyển mở rộng $$\hat{\delta}$$ trên hai chuỗi:
1. **Chuỗi `10110`:**
   $$q_{\text{chẵn}} \xrightarrow{1} q_{\text{lẻ}} \xrightarrow{0} q_{\text{lẻ}} \xrightarrow{1} q_{\text{chẵn}} \xrightarrow{1} q_{\text{lẻ}} \xrightarrow{0} q_{\text{lẻ}} \notin F \implies$$ **TỪ CHỐI** (có 3 bit `1` — lẻ!).
2. **Chuỗi `1010`:**
   $$q_{\text{chẵn}} \xrightarrow{1} q_{\text{lẻ}} \xrightarrow{0} q_{\text{lẻ}} \xrightarrow{1} q_{\text{chẵn}} \xrightarrow{0} q_{\text{chẵn}} \in F \implies$$ **CHẤP NHẬN** (2 bit `1` — chẵn!).

### Khung giải thích: 4 bước đọc và kiểm tra một DFA (nên đọc chậm)

#### Bước 1: Kiểm tra tính "Tất định và Đầy đủ"
Tại **mọi** trạng thái $$q \in Q$$ và **mọi** ký tự $$a \in \Sigma$$, phải có **đúng 1** mũi tên gắn nhãn $$a$$ đi ra (không thiếu, không thừa!).

#### Bước 2: Gán ý nghĩa (bất biến) cho từng trạng thái
Mỗi trạng thái của DFA là một "ngăn nhớ" tóm tắt toàn bộ quá khứ đã đọc (ví dụ: *"số bit 1 đã đọc tới lúc này là chẵn hay lẻ?"*).

#### Bước 3: Chạy thử trên chuỗi rỗng $$\varepsilon$$ và các chuỗi ngắn
Nhớ rằng $$\varepsilon \in L(M) \iff q_0 \in F$$! Luôn kiểm tra $$\varepsilon$$ trước tiên.

#### Bước 4: Nhận diện giới hạn bộ nhớ hữu hạn
Vì $$Q$$ hữu hạn, DFA chỉ nhớ được thông tin theo modulo hoặc mẫu cố định — không thể đếm vô hạn như $$0^n 1^n$$ (sẽ chứng minh chặt ở bài 18.09!).

$$
\text{Chuỗi }w \in \Sigma^*
\;\xrightarrow{\;\hat{\delta}(q_0, w)\;}\;
q_{\text{cuối}} \in Q
\;\xrightarrow{\;q_{\text{cuối}} \in F?\;}\;
\text{Chấp nhận / Từ chối trong }O(\lvert w\rvert).
$$

## Định nghĩa

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Một **DFA** là bộ năm $$M=(Q,\Sigma,\delta,q_0,F)$$, trong đó $$Q$$ (tập trạng thái) và $$\Sigma$$ (bảng chữ cái) là các tập hữu hạn khác rỗng; $$\delta:Q\times\Sigma\to Q$$ là hàm chuyển **toàn phần**; $$q_0\in Q$$ là trạng thái khởi đầu; và $$F\subseteq Q$$ là tập các trạng thái kết thúc (chấp nhận).

</div>

## Hàm chuyển mở rộng

<div class="textbook-definition" markdown="1">

**Định nghĩa.** Hàm chuyển mở rộng $$\hat\delta:Q\times\Sigma^*\to Q$$ được định nghĩa đệ quy như sau:

$$
\hat\delta(q,\varepsilon)=q,\qquad
\hat\delta(q,wa)=\delta\bigl(\hat\delta(q,w),a\bigr).
$$

</div>

<div class="textbook-theorem" markdown="1">

**Định lý** (Tính duy nhất của đường chạy). Với mọi trạng thái $$q \in Q$$ và mọi chuỗi $$w \in \Sigma^*$$, tồn tại duy nhất một dãy trạng thái khi DFA đọc chuỗi $$w$$ xuất phát từ $$q$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.** Quy nạp theo độ dài $$\lvert w\rvert$$: ở mỗi bước, vì hàm chuyển $$\delta$$ là hàm toàn phần và đơn trị nên trạng thái kế tiếp luôn được xác định duy nhất.

</div>

## Ngôn ngữ chấp nhận

<div class="textbook-definition" markdown="1">

Ngôn ngữ được chấp nhận bởi DFA $$M$$ là

$$L(M)=\{w\in\Sigma^*:\hat\delta(q_0,w)\in F\}.$$

Một ngôn ngữ được gọi là **chính quy** (*regular*) nếu tồn tại một DFA $$M$$ sao cho $$L=L(M)$$ (các bài sau sẽ chứng minh sự tương đương với NFA và biểu thức chính quy).

</div>

## Biểu diễn DFA

DFA thường được biểu diễn theo hai cách trực quan: bằng **sơ đồ trạng thái** (vòng tròn đôi đánh dấu trạng thái thuộc $$F$$, mũi tên không có nguồn chỉ vào $$q_0$$) hoặc bằng **bảng chuyển trạng thái** (mỗi hàng ứng với một trạng thái, mỗi cột ứng với một ký hiệu đầu vào).

## Công cụ tương tác

Chạy thử một DFA trên chuỗi đầu vào theo từng ký tự để quan sát trạng thái hiện tại và quyết định chấp nhận hay từ chối:

<div class="interactive-demo" markdown="1">
<div data-demo="dfa-simulator"></div>
</div>
<script src="{{ '/public/js/dfa-simulator.js' | relative_url }}"></script>

### Minh họa tương tác

Minh họa chạy DFA từng ký tự trên chuỗi đầu vào và cho phép chỉnh sửa trực tiếp máy trạng thái:

<div class="interactive-demo" markdown="1">
<div data-demo="automata-explainer" data-preset="dfa01" data-tab="simulate"></div>
</div>
<script src="{{ '/public/js/explainers/automata-explainer.js' | relative_url }}"></script>

## Bài tập

1. Chứng minh tính chất $$\hat\delta(q,xy)=\hat\delta\bigl(\hat\delta(q,x),y\bigr)$$ với mọi $$x,y \in \Sigma^*$$.
2. Với DFA kiểm tra tính chẵn lẻ ở Hình 18.1, hãy chứng minh tính đúng đắn bằng bất biến: “trạng thái hiện tại phản ánh tính chẵn lẻ của số bit 1 đã đọc”.
3. Giải thích vì sao hàm chuyển $$\delta$$ phải là hàm toàn phần trong định nghĩa DFA chuẩn.

## Tài liệu đọc thêm

Sipser §1.1; Hopcroft–Ullman; Kozen, *Automata and Computability*.

## Tóm tắt

Bài học đã định nghĩa bộ năm DFA, hàm chuyển mở rộng $$\hat\delta$$, ngôn ngữ chấp nhận $$L(M)$$ và khẳng định tính duy nhất của đường chạy trên DFA.

**Bài tiếp theo:** 18.2 — Thiết kế DFA và chứng minh tính đúng đắn.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=Qa6csfkK7_I">Finite State Machine (Finite Automata)</a> — Neso Academy, tiếng Anh. Giới thiệu ô-tô-mát hữu hạn đơn định và cách đọc sơ đồ trạng thái.
- <a href="https://www.youtube.com/watch?v=58N2N7zJGrQ">Introduction to Theory of Computation</a> — Neso Academy, tiếng Anh. Đặt DFA vào bức tranh chung của lý thuyết tính toán mở đầu chương.
- <a href="https://www.youtube.com/watch?v=40i4PKpM0cI">Deterministic Finite Automata (Example 1)</a> — Neso Academy, tiếng Anh. Ví dụ một DFA chấp nhận ngôn ngữ cụ thể, minh họa trực tiếp định nghĩa chấp nhận.
