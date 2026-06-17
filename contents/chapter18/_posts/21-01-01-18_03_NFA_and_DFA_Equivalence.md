---
layout: post
title: "NFA và Sự tương đương với DFA"
categories: chapter18
date: 2021-01-01
order: 3
required: true
lang: en
---

Hãy tưởng tượng bạn cần thiết kế một máy nhận diện các chuỗi trên $$\{0, 1\}$$ **kết thúc bằng `01`**. Với DFA, bạn phải cẩn thận ghi nhớ "mình vừa đọc gì" bằng các trạng thái: chưa thấy gì, vừa thấy `0`, vừa thấy `01`. Nếu yêu cầu phức tạp hơn - "chứa **một trong các mẫu** `01`, `100`, `1110`" - DFA sẽ phình ra rất nhanh. Thay vào đó, nếu cho phép máy "đoán" mẫu nào sẽ xuất hiện và "chạy nhiều khả năng song song", ta được một mô hình gọn hơn nhiều: **automat hữu hạn không tất định** (Nondeterministic Finite Automaton, NFA).

NFA nghe có vẻ "mạnh hơn" DFA vì nó có khả năng đoán đúng - nhưng một định lý đẹp khẳng định rằng **NFA và DFA tương đương về sức biểu đạt**: cùng nhận diện đúng lớp ngôn ngữ chính quy. Cái giá là số trạng thái: chuyển từ NFA sang DFA có thể làm số trạng thái tăng theo cấp số mũ. Bài này sẽ trình bày định nghĩa NFA, thuật toán **xây dựng tập con** (subset construction) chuyển NFA về DFA, và hệ quả thực tế trong cài đặt biểu thức chính quy.

![Ví dụ NFA](https://commons.wikimedia.org/wiki/Special:FilePath/NFA_example.svg?width=640)

*Hình 18.11: NFA cho phép nhiều chuyển trên cùng ký hiệu và chuyển $\varepsilon$ — không tất định.*

![Ví dụ DFA](https://commons.wikimedia.org/wiki/Special:FilePath/DFA_example.svg?width=640)

*Hình 18.12: DFA: mỗi $(q,a)$ có đúng một trạng thái kế — dễ mô phỏng và hiện thực.*

![Tương đương NFA và DFA](https://commons.wikimedia.org/wiki/Special:FilePath/Finite_state_machine.svg?width=640)

*Hình 18.13: Mọi NFA có DFA tương đương — xây bằng tập lũy thừa trạng thái (subset construction).*

![Xây dựng DFA từ NFA](https://commons.wikimedia.org/wiki/Special:FilePath/Decision_tree.svg?width=640)

*Hình 18.14: Subset construction: mỗi trạng thái DFA là tập con trạng thái NFA.*

![Ngôn ngữ chính quy](https://commons.wikimedia.org/wiki/Special:FilePath/Example_of_a_Turing_machine.svg?width=640)

*Hình 18.15: NFA và DFA nhận diện cùng lớp ngôn ngữ chính quy (regular languages).*

## Mục tiêu học tập

Sau khi hoàn thành bài này, sinh viên có thể:

- **Định nghĩa** hình thức NFA và $$\varepsilon$$-NFA.
- **Vẽ** NFA cho một ngôn ngữ chính quy đơn giản, ngắn hơn DFA tương ứng.
- **Áp dụng** thuật toán xây dựng tập con để chuyển NFA về DFA tương đương.
- **Tính** đóng $$\varepsilon$$ (epsilon-closure) của một tập trạng thái.
- **Giải thích** vì sao chuyển NFA → DFA có thể gây bùng nổ số trạng thái.

**Từ khóa**: NFA (nondeterministic finite automaton), $$\varepsilon$$-NFA, hàm chuyển đa trị (multi-valued transition), xây dựng tập con (subset construction), đóng epsilon (epsilon-closure), bùng nổ trạng thái (state explosion).

## 1. NFA: Định nghĩa hình thức

**Định nghĩa**: Một **automat hữu hạn không tất định** (NFA) là một bộ năm $$N = (Q, \Sigma, \delta, q_0, F)$$ với mọi thành phần như DFA, **trừ** hàm chuyển trạng thái:

$$\delta: Q \times \Sigma \to \mathcal{P}(Q)$$

trong đó $$\mathcal{P}(Q)$$ là tập lũy thừa (power set) của $$Q$$. Tức là $$\delta(q, a)$$ là một **tập con** của $$Q$$, có thể rỗng, có thể chứa nhiều phần tử.

### Hai đặc tính của NFA so với DFA

1. **Đa khả năng**: với cùng (trạng thái, ký hiệu), NFA có thể chuyển đến **nhiều** trạng thái cùng lúc.
2. **Vắng chuyển dịch**: tập $$\delta(q, a)$$ có thể rỗng, nghĩa là "không có cách nào hợp lệ" từ đây.

### Quy tắc chấp nhận

NFA chấp nhận chuỗi $$w$$ khi **tồn tại ít nhất một** đường chạy từ $$q_0$$, đọc hết $$w$$, và kết thúc ở một trạng thái thuộc $$F$$. Ta hình dung NFA "chạy song song" tất cả các khả năng và chấp nhận nếu có một nhánh nào đó đến đích.

<div class="content-box example-box" markdown="1">
**Ví dụ 1**: NFA trên $$\{0, 1\}$$ nhận diện các chuỗi **kết thúc bằng `01`**.

- $$Q = \{q_0, q_1, q_2\}$$.
- $$\delta$$:
  - $$\delta(q_0, 0) = \{q_0, q_1\}$$ (đoán: hoặc tiếp tục đọc, hoặc bắt đầu khớp `01`).
  - $$\delta(q_0, 1) = \{q_0\}$$.
  - $$\delta(q_1, 1) = \{q_2\}$$.
  - $$\delta(q_1, 0) = \emptyset$$.
  - $$\delta(q_2, 0) = \emptyset$$, $$\delta(q_2, 1) = \emptyset$$.
- $$F = \{q_2\}$$.

Chuỗi `1001`: một đường chạy là $$q_0 \to q_0 \to q_1 \to q_0 \to q_0$$ (không đến $$q_2$$). Một đường khác: $$q_0 \to q_0 \to q_0 \to q_1 \to q_2 \in F$$, **chấp nhận**.

NFA này chỉ có 3 trạng thái; DFA tương ứng cần 3 trạng thái cũng vậy, nhưng với mẫu phức tạp hơn (như "chứa một trong `aabb`, `ababc`, `caacb`"), NFA tiết kiệm rất nhiều.
</div>

## 2. $$\varepsilon$$-NFA: Cho phép chuyển dịch tự do

Đôi khi ta muốn máy chuyển trạng thái mà **không đọc ký hiệu nào**. Ta định nghĩa **$$\varepsilon$$-NFA** với hàm chuyển mở rộng:

$$\delta: Q \times (\Sigma \cup \{\varepsilon\}) \to \mathcal{P}(Q)$$

trong đó $$\varepsilon$$ là chuỗi rỗng. Chuyển $$\varepsilon$$ giúp viết NFA gọn hơn nhiều khi ghép các phần.

### Đóng epsilon

**Định nghĩa**: **Đóng epsilon** (epsilon-closure) của một trạng thái $$q$$, ký hiệu $$E(q)$$, là tập tất cả các trạng thái có thể đến được từ $$q$$ chỉ bằng các chuyển $$\varepsilon$$. Hình thức:

$$E(q) = \{q\} \cup \bigcup_{p \in \delta(q, \varepsilon)} E(p)$$

Mở rộng ra tập: $$E(S) = \bigcup_{q \in S} E(q)$$.

## 3. Thuật toán xây dựng tập con (Subset Construction)

**Mục tiêu**: cho NFA $$N = (Q_N, \Sigma, \delta_N, q_0, F_N)$$, xây dựng DFA $$D$$ chấp nhận **cùng ngôn ngữ**.

**Ý tưởng**: trạng thái của DFA $$D$$ là **tập con** của $$Q_N$$, biểu diễn "tất cả các trạng thái NFA có thể đang ở cùng lúc" sau khi đọc một tiền tố.

### Xây dựng $$D = (Q_D, \Sigma, \delta_D, q_{0D}, F_D)$$

- $$Q_D = \mathcal{P}(Q_N)$$ (trên lý thuyết; thực tế chỉ giữ các tập **đến được**).
- $$q_{0D} = E(\{q_0\})$$ (với $$\varepsilon$$-NFA) hoặc $$\{q_0\}$$ (với NFA thường).
- $$\delta_D(S, a) = E\left(\bigcup_{q \in S} \delta_N(q, a)\right)$$ - hợp tất cả các trạng thái có thể đến, rồi lấy đóng $$\varepsilon$$ (nếu có).
- $$F_D = \{S \in Q_D : S \cap F_N \neq \emptyset\}$$ - tập con chứa ít nhất một trạng thái chấp nhận.

### Quy trình thuật toán

1. Khởi tạo $$q_{0D}$$, đưa vào hàng đợi `unmarked`.
2. Lấy tập $$S$$ ra khỏi hàng đợi, đánh dấu đã xử lý.
3. Với mỗi $$a \in \Sigma$$, tính $$T = \delta_D(S, a)$$. Nếu $$T$$ chưa có trong $$Q_D$$, thêm vào và đẩy vào hàng đợi.
4. Lặp đến khi hàng đợi rỗng.

<div class="content-box example-box" markdown="1">
**Ví dụ 2**: Chuyển NFA Ví dụ 1 về DFA.

Bắt đầu $$\{q_0\}$$:
- $$\delta_D(\{q_0\}, 0) = \delta_N(q_0, 0) = \{q_0, q_1\}$$.
- $$\delta_D(\{q_0\}, 1) = \{q_0\}$$.

Tiếp $$\{q_0, q_1\}$$:
- Trên `0`: $$\delta_N(q_0, 0) \cup \delta_N(q_1, 0) = \{q_0, q_1\} \cup \emptyset = \{q_0, q_1\}$$.
- Trên `1`: $$\delta_N(q_0, 1) \cup \delta_N(q_1, 1) = \{q_0\} \cup \{q_2\} = \{q_0, q_2\}$$.

Tiếp $$\{q_0, q_2\}$$:
- Trên `0`: $$\{q_0, q_1\}$$.
- Trên `1`: $$\{q_0\}$$.

Không có tập mới. DFA có 3 trạng thái: $$\{q_0\}, \{q_0, q_1\}, \{q_0, q_2\}$$, với $$\{q_0, q_2\}$$ là chấp nhận. Trùng kích thước với NFA.
</div>

## 4. Định lý tương đương

**Định lý (Rabin-Scott, 1959)**: Với mỗi NFA $$N$$ tồn tại DFA $$D$$ sao cho $$L(N) = L(D)$$.

**Hệ quả**: Lớp ngôn ngữ chấp nhận bởi DFA bằng lớp ngôn ngữ chấp nhận bởi NFA. Cả hai đều là **lớp ngôn ngữ chính quy**.

### Cái giá: bùng nổ trạng thái

Trong trường hợp xấu nhất, một NFA $$n$$ trạng thái có thể cần DFA $$2^n$$ trạng thái.

<div class="content-box example-box" markdown="1">
**Ví dụ 3 (Bùng nổ)**: Ngôn ngữ $$L_n$$ trên $$\{0, 1\}$$ gồm các chuỗi mà **ký tự thứ $$n$$ từ cuối là `1`**.

- NFA cho $$L_n$$ chỉ cần $$n + 1$$ trạng thái: đoán "đây là ký tự thứ $$n$$ từ cuối" và đếm xuống.
- DFA cho $$L_n$$ phải nhớ $$n$$ ký tự cuối cùng, cần ít nhất $$2^n$$ trạng thái.

Đây là ví dụ cổ điển cho thấy NFA gọn hơn DFA theo cấp số mũ.
</div>

<div class="content-box warning-box" markdown="1">
**Hệ quả thực tiễn**: trình khớp regex thường chọn giữa **mô phỏng NFA trực tiếp** (chậm hơn theo độ dài chuỗi nhưng không cần dựng DFA lớn) và **dựng DFA trước** (nhanh khi khớp nhưng có thể tốn bộ nhớ khổng lồ). Đây là một sự đánh đổi không gian - thời gian kinh điển trong cài đặt lý thuyết ngôn ngữ chính quy.
</div>

## 5. Khi nào dùng NFA

NFA hữu ích khi:

- **Mô tả ngôn ngữ**: viết NFA dễ hơn DFA cho các mẫu phức tạp (ví dụ: hợp các mẫu).
- **Chuyển từ biểu thức chính quy**: thuật toán Thompson (bài 18.4) chuyển regex thành $$\varepsilon$$-NFA rất tự nhiên.
- **Mô phỏng song song**: cài đặt khớp regex bằng cách duy trì tập trạng thái hiện tại.

DFA hữu ích khi:

- **Khớp nhanh** trên chuỗi rất dài.
- **Phân tích tính chất** ngôn ngữ (đếm trạng thái, kiểm tra rỗng).
- **Tối thiểu hóa** (minimization) để được dạng chuẩn duy nhất.

## Tổng kết

- **NFA** cho phép $$\delta(q, a)$$ trả về một **tập** trạng thái; chấp nhận nếu **tồn tại** đường chạy đến trạng thái chấp nhận.
- **$$\varepsilon$$-NFA** cho phép chuyển dịch không cần đọc ký hiệu.
- **Subset construction** chuyển NFA về DFA: trạng thái DFA = tập con của trạng thái NFA.
- **NFA và DFA tương đương về sức biểu đạt** (cùng lớp ngôn ngữ chính quy), nhưng có thể chênh nhau theo cấp số mũ về số trạng thái.

## Bài tập

1. Vẽ NFA 3 trạng thái nhận diện các chuỗi trên $$\{a, b\}$$ **chứa chuỗi con `aba`**.
2. Áp dụng subset construction để chuyển NFA bài 1 thành DFA. So sánh số trạng thái.
3. Cho NFA với $$\varepsilon$$-chuyển: $$q_0 \xrightarrow{\varepsilon} q_1$$, $$q_1 \xrightarrow{a} q_2$$. Tính $$E(q_0)$$.
4. Chứng minh rằng NFA $$n$$ trạng thái cho ngôn ngữ "ký tự thứ $$n$$ từ cuối là `1`" cần ít nhất $$2^n$$ trạng thái khi chuyển sang DFA. Gợi ý: dùng nguyên lý chuồng bồ câu trên các chuỗi đầu vào khác nhau.
5. Viết NFA và DFA cùng nhận diện ngôn ngữ "chứa `01` hoặc kết thúc bằng `10`". So sánh độ phức tạp.
6. Cài đặt subset construction bằng giả mã.

<div class="content-box note-box" markdown="1">
**Tài liệu tham khảo**

- Rosen, K. H. (2019). *Discrete Mathematics and Its Applications*, 8th ed. Section 13.3.
- Sipser, M. (2013). *Introduction to the Theory of Computation*, 3rd ed. Sections 1.2, 1.3.
- Hopcroft, J., Motwani, R., & Ullman, J. (2007). *Introduction to Automata Theory*, 3rd ed. Chapter 2.
- Rabin, M. O., & Scott, D. (1959). "Finite automata and their decision problems." *IBM Journal of Research and Development*, 3(2), 114-125. (bài báo gốc về tương đương NFA-DFA)
</div>
