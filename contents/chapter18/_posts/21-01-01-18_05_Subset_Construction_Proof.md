---
layout: post
title: "Xây dựng tập con: NFA ≡ DFA"
categories: chapter18
date: 2021-01-01
order: 5
required: true
lang: en
excerpt: "Định lý tương đương Rabin–Scott giữa NFA và DFA, chứng minh L(D)=L(N), cận trên 2^|Q| trạng thái và tối ưu chỉ xét các tập con đạt được."
---

> **Câu chuyện mở đầu:** Thoạt nhìn, NFA với khả năng "phân thân" và "đoán trước tương lai" tưởng như phải mạnh hơn DFA gấp bội. Thế nhưng năm 1959, Michael Rabin và Dana Scott đã chứng minh một định lý mang về cho họ Giải Turing: **mọi NFA $$n$$ trạng thái đều tương đương hoàn toàn với một DFA có tối đa $$2^n$$ trạng thái**! Bí quyết đẹp đến khó tin: biến **mỗi tập con các trạng thái NFA** thành **1 trạng thái đơn lẻ của DFA**!

<div class="textbook-epigraph" markdown="1">

"Powerset construction trades nondeterminism for exponentially many states."

<span class="epigraph-attribution">— Rabin–Scott</span>

</div>

![Subset](/discrete-mathematics-for-computer-science-iuh/img/course/Automata_subset_construction.svg)

<p class="textbook-figure-caption" data-figure="18.3">Mỗi trạng thái của DFA tương ứng với một tập con các trạng thái của NFA.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Xây dựng** DFA tương đương từ một NFA (có hoặc không có chuyển ε).
- **Chứng minh** đẳng thức ngôn ngữ $$L(D)=L(N)$$.
- **Nêu** cận trên số trạng thái $$2^{\lvert Q\rvert}$$ và hiện tượng bùng nổ trạng thái.

</div>

## Kiến thức cần nhớ: Thuật toán Xây dựng Tập con (Rabin–Scott, 1959)

### 1. Ý tưởng Cốt lõi: Trạng thái của DFA = Tập con trạng thái của NFA ($$Q_D = \mathcal{P}(Q_N)$$)
- **Trạng thái khởi đầu:** $$q_{0D} = \{q_0\}$$ (hoặc $$\mathrm{ECLOSE}(q_0)$$ nếu có $$\varepsilon$$).
- **Hàm chuyển tất định:** $$\delta_D(S, a) = \bigcup_{p \in S} \delta_N(p, a)$$ (luôn xác định duy nhất một tập con $$S' \in \mathcal{P}(Q_N)$$!).
- **Tập kết thúc:** $$F_D = \{S \subseteq Q_N : S \cap F_N \neq \emptyset\}$$.

### 2. Chiến lược "Chỉ sinh Trạng thái Đạt tới được" (Reachable States Only)
- **Bản chất:** Thay vì liệt kê đủ $$2^n$$ tập con (phần lớn không bao giờ đi tới!), ta dùng BFS bắt đầu từ $$\{q_0\}$$ để chỉ tạo những tập con thực sự xuất hiện — thực tế thường chỉ có vài trạng thái!

### 3. Bùng nổ Hàm mũ $$2^n$$ trong Trường hợp Xấu nhất
- **Lưu ý quan trọng:** Với ngôn ngữ "ký tự thứ $$k$$ từ cuối lên là `1`", NFA chỉ cần $$k+1$$ trạng thái nhưng **mọi DFA** bắt buộc phải có ít nhất $$2^k$$ trạng thái — cận trên $$2^n$$ là **chặt tuyệt đối**!

## Ví dụ tính tay làm từng bước: Biến NFA "Kết thúc bằng `01`" thành DFA bằng Subset Construction

Xuất phát từ NFA 3 trạng thái ở bài 18.03 ($$q_0 \xrightarrow{0} \{q_0, q_1\},\; q_0 \xrightarrow{1} \{q_0\},\; q_1 \xrightarrow{1} \{q_2\},\; F_N = \{q_2\}$$):
1. **Bắt đầu với trạng thái $$A = \{q_0\}$$:**
   - $$\delta_D(A, 0) = \{q_0, q_1\} = B$$ (trạng thái mới!).
   - $$\delta_D(A, 1) = \{q_0\} = A$$.
2. **Mở rộng trạng thái $$B = \{q_0, q_1\}$$:**
   - $$\delta_D(B, 0) = \delta(q_0, 0) \cup \delta(q_1, 0) = \{q_0, q_1\} = B$$.
   - $$\delta_D(B, 1) = \delta(q_0, 1) \cup \delta(q_1, 1) = \{q_0, q_2\} = C$$ (trạng thái mới — chứa $$q_2 \implies C \in F_D$$!).
3. **Mở rộng trạng thái $$C = \{q_0, q_2\}$$:**
   - $$\delta_D(C, 0) = \delta(q_0, 0) \cup \delta(q_2, 0) = \{q_0, q_1\} = B$$.
   - $$\delta_D(C, 1) = \delta(q_0, 1) \cup \delta(q_2, 1) = \{q_0\} = A$$.

**Kết quả:** Không còn tập con mới nào! Thay vì $$2^3 = 8$$ trạng thái, DFA tối ưu sinh ra chỉ có **đúng 3 trạng thái $$A, B, C$$**!

### Giải thích: Chứng minh 4 bước cho Định lý Rabin–Scott (NFA $$\equiv$$ DFA)
#### Bước 1: Định nghĩa $$\delta_D(S, a)$$ bằng phép hợp
Chính việc gộp mọi trạng thái NFA đang sống vào một "cái túi" $$S$$ đã triệt tiêu hoàn toàn tính không tất định!

#### Bước 2: Chứng minh quy nạp $$\hat{\delta}_D(\{q_0\}, w) = \hat{\delta}_N(q_0, w)$$
Với $$\lvert w\rvert = 0$$: hai vế đều bằng $$\{q_0\}$$. Bước quy nạp $$w \to wa$$ khớp ngay nhờ định nghĩa $$\delta_D$$.

#### Bước 3: Đối chiếu điều kiện chấp nhận
$$w \in L(D) \iff \hat{\delta}_D(\{q_0\}, w) \in F_D \iff \hat{\delta}_N(q_0, w) \cap F_N \neq \emptyset \iff w \in L(N)$$!

#### Bước 4: Tối tiểu hóa tiếp (sang bài 18.11)
Sau khi chạy Subset Construction, ta có thể chạy thêm thuật toán tối tiểu hóa Hopcroft/Myhill–Nerode để thu gọn DFA về kích thước nhỏ nhất duy nhất!

$$
\text{NFA }N\;(n\text{ trạng thái})
\;\xrightarrow{\;\text{Subset Construction (BFS)}\;}\;
\text{DFA }D\;(\le 2^n\text{ trạng thái}),\quad L(D) = L(N).
$$

## Phép xây dựng tập con (không có ε)

Từ NFA $$N=(Q_N,\Sigma,\delta_N,q_0,F_N)$$, ta xây dựng DFA $$D$$ như sau: tập trạng thái $$Q_D=\mathcal{P}(Q_N)$$ (trong thực tế chỉ cần giữ các tập con đạt được từ trạng thái đầu), trạng thái khởi đầu $$q_{D0}=\{q_0\}$$, hàm chuyển $$\delta_D(S,a)=\bigcup_{q\in S}\delta_N(q,a)$$, và tập trạng thái kết thúc $$F_D=\{S \in Q_D : S\cap F_N\neq\emptyset\}$$.

**Trường hợp có chuyển ε:** ta đặt $$q_{D0}=E(\{q_0\})$$ và $$\delta_D(S,a)=E\bigl(\bigcup_{q\in S}\delta_N(q,a)\bigr)$$.

### Video ngắn: Từ NFA sang DFA

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/nfa-to-dfa-subset-construction.mp4"></video>
</div>

Video dài khoảng 2 phút 56 giây: xét NFA nhận các chuỗi bắt đầu bằng 1 và kết thúc bằng 01, theo dõi tập trạng thái đang hoạt động khi đọc chuỗi, lập bảng chuyển DFA từng hàng, xử lý trạng thái chết $$\varnothing$$, chạy thử DFA thu được và giải thích vì sao số trạng thái có thể tăng đến $$2^n$$.

## Định lý tương đương

<div class="textbook-theorem" markdown="1">

**Định lý** (Rabin–Scott). Với mọi NFA $$N$$, luôn tồn tại một DFA $$D$$ sao cho $$L(D)=L(N)$$ và $$\lvert Q_D\rvert\le 2^{\lvert Q_N\rvert}$$.

</div>

<div class="textbook-proof" markdown="1">

**Chứng minh.**  
Bất biến: sau khi đọc bất kỳ chuỗi $$w \in \Sigma^*$$, trạng thái hiện tại của DFA $$D$$ chính là tập trạng thái $$\hat\delta_N(\{q_0\},w)$$ (hoặc phiên bản có bao đóng ε). Bất biến này được chứng minh trực tiếp bằng quy nạp theo độ dài chuỗi $$w$$.  
Do đó, $$D$$ chấp nhận $$w$$ khi và chỉ khi tập trạng thái kết thúc có giao khác rỗng với $$F_N$$, tức là khi và chỉ khi $$w\in L(N)$$. Vì mỗi trạng thái của $$D$$ là một tập con của $$Q_N$$ nên số trạng thái tối đa là $$2^{\lvert Q_N\rvert}$$.

</div>

## Bùng nổ trạng thái (*state explosion*)

Cận trên hàm mũ là chặt: tồn tại những họ ngôn ngữ mà DFA tối tiểu bắt buộc phải có $$\Omega(2^n)$$ trạng thái trong khi NFA chỉ cần $$O(n)$$ trạng thái (chẳng hạn ngôn ngữ “ký tự thứ $$n$$ tính từ cuối là 1”).

### Minh họa tương tác

Theo dõi phép xây dựng tập con từng bước để thấy bảng chuyển và sơ đồ DFA hiện dần (một NFA 4 trạng thái tạo ra DFA 8 trạng thái):

<div class="interactive-demo" markdown="1">
<div data-demo="automata-explainer" data-preset="nfa3" data-tab="subset"></div>
</div>
<script src="{{ '/public/js/explainers/automata-explainer.js' | relative_url }}"></script>

## Bài tập

1. Áp dụng phép xây dựng tập con lên NFA nhận chuỗi kết thúc bằng `01` và liệt kê các trạng thái đạt được.
2. Chứng minh rằng việc loại bỏ các tập con không đạt được từ $$q_{D0}$$ không làm thay đổi ngôn ngữ $$L(D)$$.
3. Tìm thêm một ví dụ về hiện tượng bùng nổ trạng thái (tham khảo Sipser).

## Tài liệu đọc thêm

Sipser §1.2; Hopcroft–Ullman.

## Tóm tắt

Phép xây dựng tập con (*powerset construction*) chứng minh NFA và DFA có cùng sức mạnh biểu diễn ngôn ngữ, với chi phí tối đa $$2^{\lvert Q\rvert}$$ trạng thái.

**Bài tiếp theo:** Máy Mealy và máy Moore.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=--CSVsFIDng">Conversion of NFA to DFA</a> — Neso Academy, tiếng Anh. Giới thiệu cách dựng DFA từ các tập con trạng thái của NFA.
- <a href="https://www.youtube.com/watch?v=pnyXgIXpKnc">Conversion of NFA to DFA (Example 1)</a> — Neso Academy, tiếng Anh. Ví dụ thứ nhất về phép xây dựng tập con.
- <a href="https://www.youtube.com/watch?v=i-fk9o46oVY">Conversion of NFA to DFA (Example 2)</a> — Neso Academy, tiếng Anh. Ví dụ thứ hai giúp đối chiếu với chứng minh tương đương.
