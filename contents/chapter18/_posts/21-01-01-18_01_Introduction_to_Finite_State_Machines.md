---
layout: post
title: "Giới thiệu Máy hữu hạn trạng thái"
categories: chapter18
date: 2021-01-01
order: 1
required: true
lang: en
---

# Giới thiệu Máy hữu hạn trạng thái

Một máy bán nước tự động chỉ "biết" vài điều: hiện đang có bao nhiêu tiền trong khe, đã chọn loại nước nào chưa, và đã đến lúc nhả hàng hay chưa. Nó không cần ghi nhớ lịch sử mua hàng của tất cả khách trước đó - nó chỉ cần biết **trạng thái hiện tại** (current state) và **đầu vào tiếp theo** (next input) là một đồng xu hay một nút bấm. Mô hình đơn giản này được gọi là **máy hữu hạn trạng thái** (finite-state machine, FSM), và nó nằm ở trung tâm của mọi thứ từ đèn giao thông, bộ điều khiển vi xử lý, đến trình phân tích từ vựng của một trình biên dịch.

Một FSM được mô tả bởi một tập trạng thái hữu hạn, một bảng chữ cái đầu vào, một hàm chuyển trạng thái $$\delta$$, một trạng thái khởi đầu $$q_0$$, và một tập trạng thái kết thúc. Sự tinh tế nằm ở chỗ: chỉ với một tập **hữu hạn** trạng thái và bộ nhớ bằng không, FSM vẫn có thể nhận diện được toàn bộ lớp **ngôn ngữ chính quy** (regular languages) - cùng lớp ngôn ngữ mà biểu thức chính quy (regular expressions) trong các công cụ như `grep` hay `sed` mô tả. Đây là cây cầu đầu tiên giữa **logic toán học** và **mô hình tính toán** mà chúng ta sẽ đi qua.

## Mục tiêu học tập

Sau khi hoàn thành bài này, sinh viên có thể:

- **Định nghĩa** hình thức máy hữu hạn trạng thái tất định (DFA) dưới dạng bộ năm $$(Q, \Sigma, \delta, q_0, F)$$.
- **Vẽ** sơ đồ chuyển trạng thái (state diagram) và **lập** bảng chuyển trạng thái (transition table) cho một DFA cho trước.
- **Thiết kế** DFA để nhận diện một ngôn ngữ chính quy đơn giản.
- **Phân biệt** máy chấp nhận (acceptor) và máy biến đổi (transducer).
- **Nhận ra** liên hệ giữa FSM, biểu thức chính quy và lớp ngôn ngữ chính quy.

**Từ khóa**: máy hữu hạn trạng thái (finite-state machine), trạng thái (state), bảng chữ cái (alphabet), hàm chuyển trạng thái (transition function), trạng thái chấp nhận (accepting state), ngôn ngữ chính quy (regular language), DFA, NFA, sơ đồ chuyển trạng thái (state diagram).

## 1. Vì sao cần mô hình tính toán hữu hạn

Trước khi định nghĩa hình thức, hãy hiểu **vì sao** ta cần một mô hình toán học cho thứ tưởng chừng đã rõ ràng là "máy tính".

- **Phân loại bài toán**: không phải bài toán nào cũng có cùng độ khó. Một số bài toán có thể giải bằng máy đơn giản chỉ có vài trạng thái; số khác đòi hỏi bộ nhớ vô hạn. Mô hình tính toán giúp ta xếp loại các bài toán theo độ phức tạp.
- **Cơ sở cho thiết kế phần cứng và phần mềm**: các mạch logic tuần tự, bộ điều khiển vi xử lý, giao thức mạng (TCP, HTTP) đều được đặc tả như FSM.
- **Nền tảng lý thuyết cho trình biên dịch**: phân tích từ vựng (lexical analysis) chuyển mã nguồn thành các token bằng cách chạy một FSM trên chuỗi ký tự.

<div class="content-box info-box" markdown="1">
**Bộ nhớ là gì?**

Một FSM **không có bộ nhớ tự do** - tất cả thông tin nó có ở thời điểm bất kỳ đều nằm gọn trong "trạng thái hiện tại". Nếu cần ghi nhớ "đã thấy bao nhiêu chữ `a`" với số lượng tùy ý, FSM không làm được. Đây là **giới hạn cơ bản** sẽ dẫn ta đến các mô hình mạnh hơn (automat đẩy xuống, máy Turing) ở các bài sau.
</div>

## 2. Định nghĩa hình thức DFA

**Định nghĩa**: Một **automat hữu hạn tất định** (Deterministic Finite Automaton, DFA) là một bộ năm $$M = (Q, \Sigma, \delta, q_0, F)$$ gồm:

- $$Q$$: tập **trạng thái** (state) hữu hạn, khác rỗng.
- $$\Sigma$$: **bảng chữ cái đầu vào** (input alphabet) hữu hạn, khác rỗng.
- $$\delta: Q \times \Sigma \to Q$$: **hàm chuyển trạng thái** (transition function). Với mỗi cặp $$(q, a)$$ trong đó $$q$$ là trạng thái và $$a$$ là ký hiệu đầu vào, $$\delta(q, a)$$ là trạng thái kế tiếp.
- $$q_0 \in Q$$: **trạng thái khởi đầu** (start state).
- $$F \subseteq Q$$: tập **trạng thái chấp nhận** (accepting state hoặc final state).

Từ "tất định" (deterministic) nhấn mạnh: với mỗi cặp (trạng thái, ký hiệu) chỉ có **đúng một** trạng thái kế tiếp.

### Cách máy hoạt động

Cho chuỗi đầu vào $$w = a_1 a_2 \ldots a_n$$ với $$a_i \in \Sigma$$. Máy:

1. Bắt đầu ở trạng thái $$q_0$$.
2. Đọc ký hiệu $$a_1$$, chuyển sang trạng thái $$q_1 = \delta(q_0, a_1)$$.
3. Đọc $$a_2$$, chuyển sang $$q_2 = \delta(q_1, a_2)$$.
4. Tiếp tục đến hết chuỗi, dừng ở trạng thái $$q_n$$.
5. Nếu $$q_n \in F$$ thì **chấp nhận** $$w$$; ngược lại **từ chối**.

### Mở rộng hàm chuyển ra chuỗi

Để gọn, ta định nghĩa **hàm chuyển mở rộng** $$\hat{\delta}: Q \times \Sigma^* \to Q$$ đệ quy:

$$\hat{\delta}(q, \varepsilon) = q, \quad \hat{\delta}(q, wa) = \delta(\hat{\delta}(q, w), a)$$

trong đó $$\varepsilon$$ là chuỗi rỗng. Khi đó $$w$$ được chấp nhận khi và chỉ khi $$\hat{\delta}(q_0, w) \in F$$.

## 3. Sơ đồ và bảng chuyển trạng thái

Có hai cách biểu diễn DFA thường dùng:

**Sơ đồ chuyển trạng thái (state diagram)**: đồ thị có hướng, mỗi trạng thái là một nút; mỗi chuyển $$\delta(q, a) = q'$$ là một cạnh có hướng từ $$q$$ đến $$q'$$ gắn nhãn $$a$$. Trạng thái khởi đầu được đánh dấu bằng một mũi tên vào; trạng thái chấp nhận được vẽ bằng vòng tròn đôi.

**Bảng chuyển trạng thái (transition table)**: bảng có hàng là trạng thái, cột là ký hiệu, ô là trạng thái kế tiếp.

<div class="content-box example-box" markdown="1">
**Ví dụ 1**: DFA nhận diện các chuỗi nhị phân có **chẵn số chữ `1`**.

- $$Q = \{q_0, q_1\}$$ (q_0: đã thấy chẵn số 1; q_1: đã thấy lẻ số 1).
- $$\Sigma = \{0, 1\}$$.
- $$\delta$$:
  - $$\delta(q_0, 0) = q_0$$, $$\delta(q_0, 1) = q_1$$.
  - $$\delta(q_1, 0) = q_1$$, $$\delta(q_1, 1) = q_0$$.
- $$q_0$$ khởi đầu, $$F = \{q_0\}$$.

Chuỗi `1100`: $$q_0 \to q_1 \to q_0 \to q_0 \to q_0 \in F$$, **chấp nhận**.

Chuỗi `101`: $$q_0 \to q_1 \to q_1 \to q_0 \in F$$, **chấp nhận**. (Chuỗi này có 2 chữ `1`, là số chẵn.)

Chuỗi `111`: $$q_0 \to q_1 \to q_0 \to q_1 \notin F$$, **từ chối**.
</div>

<div class="content-box example-box" markdown="1">
**Ví dụ 2**: DFA nhận diện các chuỗi trên bảng chữ cái $$\{a, b\}$$ **kết thúc bằng `ab`**.

- $$Q = \{q_0, q_1, q_2\}$$.
- $$q_0$$: chưa thấy gì hữu ích; $$q_1$$: vừa thấy `a`; $$q_2$$: vừa thấy `ab`.
- $$\delta$$:
  - $$\delta(q_0, a) = q_1$$, $$\delta(q_0, b) = q_0$$.
  - $$\delta(q_1, a) = q_1$$, $$\delta(q_1, b) = q_2$$.
  - $$\delta(q_2, a) = q_1$$, $$\delta(q_2, b) = q_0$$.
- $$F = \{q_2\}$$.

Chuỗi `aab`: $$q_0 \to q_1 \to q_1 \to q_2 \in F$$, **chấp nhận**.

Chuỗi `bba`: $$q_0 \to q_0 \to q_0 \to q_1 \notin F$$, **từ chối**.
</div>

## 4. Ngôn ngữ chấp nhận bởi DFA

**Định nghĩa**: **Ngôn ngữ chấp nhận** bởi DFA $$M$$, ký hiệu $$L(M)$$, là tập các chuỗi mà $$M$$ chấp nhận:

$$L(M) = \{w \in \Sigma^* : \hat{\delta}(q_0, w) \in F\}$$

**Định nghĩa**: Một ngôn ngữ $$L$$ được gọi là **chính quy** (regular) nếu tồn tại một DFA chấp nhận nó.

Lớp ngôn ngữ chính quy có nhiều **đặc trưng tương đương**: chúng cũng đúng là các ngôn ngữ chấp nhận bởi NFA (bài tiếp theo), bởi biểu thức chính quy (bài sau nữa), và bởi văn phạm chính quy (chương 19). Đây là **định lý Kleene** (Kleene's theorem) - một trong những kết quả đẹp nhất của lý thuyết automat.

<div class="content-box insight-box" markdown="1">
**Trực giác**: một DFA chỉ có thể "đếm" trong giới hạn số trạng thái hữu hạn của nó. Vì vậy nó có thể đếm modulo (như Ví dụ 1) hoặc "ghi nhớ" một mẫu cuối cùng có độ dài cố định (Ví dụ 2), nhưng **không** thể đếm "có bao nhiêu chữ `a` đứng trước cũng có bấy nhiêu chữ `b` đứng sau" vì số $$n$$ có thể vô hạn.
</div>

## 5. Máy chấp nhận và máy biến đổi

DFA ở trên là một **máy chấp nhận** (acceptor): với mỗi chuỗi đầu vào, máy chỉ trả lời "có" hoặc "không" (chấp nhận / từ chối).

Tổng quát hơn, một **máy biến đổi** (transducer) sinh ra một chuỗi đầu ra cho mỗi chuỗi đầu vào. Hai loại transducer kinh điển ta sẽ học ở bài 18.2:

- **Máy Moore**: đầu ra phụ thuộc vào **trạng thái** hiện tại.
- **Máy Mealy**: đầu ra phụ thuộc vào **trạng thái và ký hiệu đầu vào**.

Cả hai đều rất hữu ích cho thiết kế mạch số tuần tự.

## 6. Ứng dụng thực tế

- **Phân tích từ vựng (lexical analysis)**: trình biên dịch C dùng DFA để nhận biết từ khóa (`if`, `else`, `return`), tên biến, số, dấu chấm câu.
- **Khớp mẫu (pattern matching)**: lệnh `grep`, `awk` chuyển biểu thức chính quy thành DFA để quét tệp văn bản hiệu quả.
- **Giao thức mạng**: máy trạng thái TCP (LISTEN, SYN_SENT, ESTABLISHED, FIN_WAIT, ...) là một FSM.
- **Bộ điều khiển nhúng**: đèn giao thông, máy giặt, lò vi sóng đều là FSM.
- **Xử lý ngôn ngữ tự nhiên**: gắn nhãn từ loại (POS tagging) bằng các mô hình trạng thái ẩn (HMM) cũng dựa trên ý tưởng FSM.

## Tổng kết

- **DFA** là bộ năm $$(Q, \Sigma, \delta, q_0, F)$$; chấp nhận chuỗi $$w$$ khi $$\hat{\delta}(q_0, w) \in F$$.
- Ngôn ngữ được chấp nhận bởi DFA gọi là **ngôn ngữ chính quy**.
- DFA có thể biểu diễn bằng **sơ đồ chuyển trạng thái** hoặc **bảng chuyển trạng thái**.
- Giới hạn cơ bản: DFA không có bộ nhớ ngoài tập trạng thái hữu hạn, do đó không nhận diện được mọi ngôn ngữ.
- Bài tiếp theo: máy có đầu ra (Moore, Mealy) và biến thể không tất định (NFA).

## Bài tập

1. Thiết kế DFA trên bảng chữ cái $$\{0, 1\}$$ nhận diện các chuỗi **chia hết cho 3** khi đọc dưới dạng số nhị phân (đọc từ bit cao xuống bit thấp).
2. Thiết kế DFA nhận diện các chuỗi trên $$\{a, b\}$$ **có chứa đúng hai chữ `a`**.
3. Cho DFA ở Ví dụ 2. Bổ sung trạng thái bẫy (trap state) nếu cần, sau đó lập bảng chuyển trạng thái đầy đủ.
4. Giải thích vì sao DFA **không** thể nhận diện ngôn ngữ $$L = \{0^n 1^n : n \geq 0\}$$. Gợi ý: dùng nguyên lý chuồng bồ câu trên số trạng thái.
5. Cho hai DFA $$M_1, M_2$$ trên cùng bảng chữ cái. Mô tả cách xây dựng DFA tích $$M_1 \times M_2$$ với trạng thái là cặp $$(q_1, q_2)$$, sao cho ngôn ngữ chấp nhận là $$L(M_1) \cap L(M_2)$$.
6. Một máy bán nước nhận đồng xu 1000đ và 5000đ, chai nước giá 10000đ. Mô hình hóa máy bằng FSM với trạng thái biểu diễn số tiền tích lũy.

<div class="content-box note-box" markdown="1">
**Tài liệu tham khảo**

- Rosen, K. H. (2019). *Discrete Mathematics and Its Applications*, 8th ed. Chapter 13, Sections 13.2-13.3.
- Sipser, M. (2013). *Introduction to the Theory of Computation*, 3rd ed. Chapter 1, Sections 1.1-1.2.
- Hopcroft, J., Motwani, R., & Ullman, J. (2007). *Introduction to Automata Theory, Languages, and Computation*, 3rd ed. Chapter 2.
</div>
