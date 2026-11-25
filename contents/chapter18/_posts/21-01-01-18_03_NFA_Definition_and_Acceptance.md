---
layout: post
title: "NFA: Định nghĩa và Chấp nhận"
categories: chapter18
date: 2021-01-01
order: 3
required: true
lang: en
excerpt: "Hàm chuyển đa trị của NFA, khái niệm đường chạy, ngôn ngữ chấp nhận L(N), so sánh với DFA và ví dụ chuỗi kết thúc bằng 01."
---

> **Câu chuyện mở đầu:** Thiết kế DFA cho ngôn ngữ "ký tự thứ 10 tính từ cuối lên là `1`" đòi hỏi tới **$$2^{10} = 1024$$ trạng thái** — một cơn ác mộng vẽ tay! Nhưng nếu cho phép ô-tô-mát có "siêu năng lực" **đoán đúng thời điểm** và **phân thân chạy song song nhiều nhánh cùng lúc** (**NFA — Ô-tô-mát Không tất định**), bài toán đó chỉ cần đúng **11 trạng thái**! Bài học này giới thiệu sức mạnh thiết kế kỳ diệu của NFA.

<div class="textbook-epigraph" markdown="1">

"Nondeterminism is a design convenience with a deterministic cost."

<span class="epigraph-attribution">— Automata theory</span>

</div>

![NFA](/discrete-mathematics-for-computer-science-iuh/img/course/Automata_nfa_ends_01.svg)

<p class="textbook-figure-caption" data-figure="18.2">NFA nhận chuỗi kết thúc bằng 01: máy có thể “đoán” thời điểm bắt đầu khớp hậu tố.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** NFA và ngôn ngữ chấp nhận $$L(N)$$.
- **Chứng minh** một chuỗi thuộc $$L(N)$$ bằng cách chỉ ra sự tồn tại của một đường chạy chấp nhận.

</div>

## Bản đồ kiến thức nền: NFA (Không tất định) khác DFA ở điểm nào?

### 1. Hàm chuyển Trả về Tập con: $$\delta: Q \times \Sigma \to \mathcal{P}(Q)$$
- **Bản chất:** Tại trạng thái $$q$$ khi đọc ký tự $$a$$, NFA được phép có **0 mũi tên** (nhánh chết), **1 mũi tên**, hoặc **nhiều mũi tên** (phân thân đồng thời sang nhiều trạng thái!).

### 2. Hai cách hình dung tương đương về NFA
- **Cách 1 (Phân thân song song):** Theo dõi **tập hợp tất cả các trạng thái khả dĩ** $$S \subseteq Q$$ sau mỗi ký tự.
- **Cách 2 (Thần đoán may mắn):** NFA chỉ cần tồn tại **ÍT NHẤT MỘT** đường đi từ $$q_0$$ kết thúc ở một trạng thái thuộc $$F$$ là chuỗi được chấp nhận!

### 3. Bất ngờ lớn: Sức mạnh Biểu đạt NFA $$\equiv$$ DFA!
- **Bản chất:** Dù NFA gọn hơn gấp nhiều lần (có khi giảm số trạng thái theo hàm mũ!), NFA **không hề mạnh hơn DFA** về tập ngôn ngữ nhận được — mọi NFA đều đổi được sang DFA tương đương nhờ Thuật toán Xây dựng Tập con (bài 18.05)!

## Ví dụ tính tay cầm tay chỉ việc: Theo vết Tập trạng thái của NFA nhận "Kết thúc bằng `01`"

Xét NFA 3 trạng thái $$Q = \{q_0, q_1, q_2\}$$, $$F = \{q_2\}$$:
- $$\delta(q_0, 0) = \{q_0, q_1\}$$ (đoán xem `0` này có phải ký tự áp chót không!), $$\delta(q_0, 1) = \{q_0\}$$.
- $$\delta(q_1, 1) = \{q_2\}$$, $$\delta(q_1, 0) = \emptyset$$ (nhánh chết!).
- $$\delta(q_2, 0) = \delta(q_2, 1) = \emptyset$$.

Theo vết tập trạng thái khả dĩ $$\hat{\delta}(\{q_0\}, w)$$ trên chuỗi `001`:
1. Bắt đầu: $$S_0 = \{q_0\}$$.
2. Đọc `0`: $$S_1 = \delta(q_0, 0) = \{q_0, q_1\}$$.
3. Đọc `0`: $$S_2 = \delta(q_0, 0) \cup \delta(q_1, 0) = \{q_0, q_1\} \cup \emptyset = \{q_0, q_1\}$$.
4. Đọc `1`: $$S_3 = \delta(q_0, 1) \cup \delta(q_1, 1) = \{q_0\} \cup \{q_2\} = \{q_0, q_2\}$$.
Vì $$S_3 \cap F = \{q_2\} \neq \emptyset \implies$$ **CHẤP NHẬN `001`**!

### Khung giải thích: 4 bước làm chủ tư duy Không tất định (nên đọc chậm)

#### Bước 1: Dùng "phân thân" để thiết kế cực nhanh
Gặp điều kiện "kết thúc bằng...", "chứa mẫu...", "hoặc A hoặc B": cứ đặt tự vòng ở $$q_0$$ rồi cho nhánh rẽ ra đoán mẫu!

#### Bước 2: Dùng phép hợp tập để mô phỏng chính xác $$\hat{\delta}(S, a) = \bigcup_{p \in S} \delta(p, a)$$
Bất cứ nhánh nào gặp $$\emptyset$$ cứ lặng lẽ biến mất mà không làm hỏng các nhánh sống khác!

#### Bước 3: Kiểm tra điều kiện chấp nhận bằng giao khác rỗng
Chuỗi $$w$$ được chấp nhận $$\iff \hat{\delta}(\{q_0\}, w) \cap F \neq \emptyset$$.

#### Bước 4: Đánh đổi Thiết kế vs. Thực thi
NFA dễ thiết kế và siêu nhỏ gọn, còn DFA chạy siêu nhanh (không phải quản lý tập trạng thái) — đó là lý do trình biên dịch cho phép ta viết bằng Regex/NFA rồi tự động biên dịch sang DFA!

$$
\text{NFA }(\delta: Q\times\Sigma \to \mathcal{P}(Q))
\;\xrightarrow{\;\hat{\delta}(S, a) = \bigcup_{p\in S}\delta(p,a)\;}\;
\hat{\delta}(\{q_0\}, w) \cap F \neq \emptyset.
$$

## Định nghĩa

<div class="textbook-definition" markdown="1">

**NFA** (*Nondeterministic Finite Automaton*) là bộ năm $$N=(Q,\Sigma,\delta,q_0,F)$$ với hàm chuyển đa trị $$\delta:Q\times\Sigma\to\mathcal{P}(Q)$$.

Chuỗi $$w = a_1a_2\ldots a_n$$ được **chấp nhận** nếu tồn tại ít nhất một dãy trạng thái $$q_0,q_1,\ldots,q_n$$ sao cho $$q_{i}\in\delta(q_{i-1},a_i)$$ với mọi $$i$$ và $$q_n\in F$$.

Ngôn ngữ của NFA là $$L(N)=\{w:\text{được chấp nhận bởi } N\}.$$

</div>

## Mở rộng $$\hat\delta$$ trên tập trạng thái

Ta mở rộng hàm chuyển sang tập trạng thái theo quy tắc $$\hat\delta(S,\varepsilon)=S$$ và $$\hat\delta(S,a)=\bigcup_{q\in S}\delta(q,a)$$, sau đó mở rộng đệ quy cho chuỗi bất kỳ. Khi đó, điều kiện chấp nhận được viết gọn là $$w\in L(N)\Leftrightarrow\hat\delta(\{q_0\},w)\cap F\neq\emptyset$$.

## Vì sao NFA thường gọn hơn DFA

Với các mẫu ngôn ngữ như “kết thúc bằng $$x$$” hoặc “chứa một trong nhiều mẫu cho trước”, NFA chỉ cần “đoán” vị trí bắt đầu khớp mẫu. Ngược lại, DFA phải ghi nhớ toàn bộ hậu tố liên quan nên thường cần nhiều trạng thái hơn trước khi tối tiểu hóa.

### Minh họa tương tác

Quan sát NFA như một tập hợp các trạng thái hoạt động song song thay đổi qua từng ký tự đầu vào:

<div class="interactive-demo" markdown="1">
<div data-demo="automata-explainer" data-preset="nfa101" data-tab="simulate"></div>
</div>
<script src="{{ '/public/js/explainers/automata-explainer.js' | relative_url }}"></script>

## Bài tập

1. Chứng minh chuỗi $$1101\in L$$ đối với NFA nhận chuỗi kết thúc bằng `01` bằng cách chỉ ra một đường chạy chấp nhận.
2. Lập bảng đầy đủ cho hàm chuyển $$\delta$$ của NFA đó.
3. Thảo luận sự khác biệt về số trạng thái giữa NFA và DFA tối tiểu.

## Tài liệu đọc thêm

Sipser §1.2.

## Tóm tắt

NFA sử dụng hàm chuyển đa trị, chấp nhận chuỗi khi tồn tại ít nhất một đường chạy kết thúc trong $$F$$, và thường giúp biểu diễn ngôn ngữ gọn gàng hơn.

**Bài tiếp theo:** ε-NFA và bao đóng epsilon.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=ehy0jGIYRtE">Non-Deterministic Finite Automata</a> — Neso Academy, tiếng Anh. Giới thiệu điểm khác biệt cốt lõi giữa NFA không đơn định và DFA.
- <a href="https://www.youtube.com/watch?v=egXhe55dAIk">Formal Definition of Non-Deterministic Finite Automata (NFA)</a> — Neso Academy, tiếng Anh. Trình bày bộ năm định nghĩa hình thức của NFA.
- <a href="https://www.youtube.com/watch?v=4bjqVsoy6bA">Non-Deterministic Finite Automata (Solved Example 1)</a> — Neso Academy, tiếng Anh. Minh họa cách một xâu được chấp nhận theo từng nhánh chuyển trạng thái.
