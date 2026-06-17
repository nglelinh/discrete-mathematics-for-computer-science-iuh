---
layout: post
title: "Máy Turing"
categories: chapter18
date: 2021-01-01
order: 5
required: true
lang: en
---

Năm 1936, hai năm trước khi máy tính điện tử đầu tiên ra đời, một nhà toán học người Anh tên Alan Turing đã đề xuất một mô hình tính toán đơn giản đến mức gần như tầm thường: một dải băng vô hạn chia thành các ô, một đầu đọc-ghi di chuyển trái-phải, và một bộ điều khiển hữu hạn quyết định "viết gì - đi đâu - sang trạng thái nào". Bốn mươi năm sau, mô hình đó - **máy Turing** (Turing machine, TM) - vẫn là **chuẩn mực** của khái niệm "thuật toán" trong khoa học máy tính lý thuyết. Mọi định nghĩa khác về tính toán (lambda calculus, máy đệ quy, máy Post, ngay cả mọi ngôn ngữ lập trình hiện đại) đều **tương đương** với máy Turing.

Máy Turing vượt qua hạn chế của FSM ở một điểm cốt lõi: nó có **bộ nhớ vô hạn** (dải băng). Nhờ vậy nó có thể giải các bài toán mà FSM và automat đẩy xuống không giải được, như nhận diện $$\{a^n b^n c^n : n \geq 0\}$$. Quan trọng hơn, nó cho ta một định nghĩa hình thức của **tính tính toán được** (computability), từ đó dẫn đến những phát hiện chấn động: tồn tại các bài toán **không thể giải bằng thuật toán**, đáng chú ý nhất là **bài toán dừng** (halting problem). Đó là chủ đề chính của chương 20.

![Máy Turing](https://commons.wikimedia.org/wiki/Special:FilePath/Example_of_a_Turing_machine.svg?width=640)

*Hình 18.21: Máy Turing: băng vô hạn, đầu đọc/ghi, bảng chuyển — mô hình tính toán phổ quát.*

![Máy Turing phổ quát](https://commons.wikimedia.org/wiki/Special:FilePath/Universal_Turing_machine.svg?width=640)

*Hình 18.22: Máy Turing phổ quát mô phỏng mọi máy Turing — nền lý thuyết tính toán.*

![So sánh với FSM](https://commons.wikimedia.org/wiki/Special:FilePath/Finite_state_machine.svg?width=640)

*Hình 18.23: FSM có trạng thái hữu hạn; máy Turing có bộ nhớ vô hạn trên băng.*

![Bài toán quyết định](https://commons.wikimedia.org/wiki/Special:FilePath/DFA_example.svg?width=640)

*Hình 18.24: Máy Turing giải bài toán quyết định: dừng và chấp nhận hoặc từ chối chuỗi.*

![Giới hạn tính toán](https://commons.wikimedia.org/wiki/Special:FilePath/Decision_tree.svg?width=640)

*Hình 18.25: Bài toán dừng (halting problem) — không giải được bằng thuật toán, chứng minh bằng máy Turing.*

## Mục tiêu học tập

Sau khi hoàn thành bài này, sinh viên có thể:

- **Định nghĩa** hình thức máy Turing dưới dạng bộ bảy $$(Q, \Sigma, \Gamma, \delta, q_0, q_{\text{accept}}, q_{\text{reject}})$$.
- **Mô phỏng** hoạt động của một TM trên một đầu vào nhỏ.
- **Thiết kế** TM đơn giản để giải bài toán cơ bản (tăng nhị phân, $$a^n b^n c^n$$).
- **Phát biểu** luận đề Church-Turing và ý nghĩa của nó.
- **Liệt kê** các biến thể TM (đa băng, không tất định) và biết chúng tương đương về sức mạnh.

**Từ khóa**: máy Turing (Turing machine), dải băng (tape), đầu đọc-ghi (head), bảng chữ cái băng (tape alphabet), cấu hình (configuration), luận đề Church-Turing (Church-Turing thesis), máy Turing phổ dụng (universal Turing machine), tính tính toán được (computability).

## 1. Hạn chế của FSM và lý do cần TM

FSM có bộ nhớ bằng không (ngoài tập trạng thái hữu hạn). Hệ quả: nó không thể đếm tùy ý.

- Không thể nhận diện $$\{0^n 1^n : n \geq 0\}$$ (đã chứng minh ở bài 18.4).
- Không thể nhận diện các biểu thức số học có ngoặc cân bằng.

**Automat đẩy xuống** (Pushdown Automaton, PDA) bổ sung ngăn xếp vô hạn - đủ để nhận diện ngôn ngữ phi ngữ cảnh (chương 19), nhưng vẫn không nhận diện được $$\{a^n b^n c^n\}$$.

**Máy Turing** trang bị một dải băng vô hạn cả hai chiều, đầu đọc-ghi tự do di chuyển - đây là mô hình tính toán **mạnh nhất** mà ta biết.

## 2. Định nghĩa hình thức

**Định nghĩa**: Một **máy Turing** là một bộ bảy $$M = (Q, \Sigma, \Gamma, \delta, q_0, q_{\text{accept}}, q_{\text{reject}})$$ gồm:

- $$Q$$: tập trạng thái hữu hạn.
- $$\Sigma$$: bảng chữ cái đầu vào (input alphabet), không chứa **ký hiệu trắng** $$\sqcup$$.
- $$\Gamma$$: bảng chữ cái băng (tape alphabet), $$\Sigma \subseteq \Gamma$$ và $$\sqcup \in \Gamma$$.
- $$\delta: Q \setminus \{q_{\text{accept}}, q_{\text{reject}}\} \times \Gamma \to Q \times \Gamma \times \{L, R\}$$: hàm chuyển trạng thái.
- $$q_0 \in Q$$: trạng thái khởi đầu.
- $$q_{\text{accept}}, q_{\text{reject}}$$: hai trạng thái dừng (halting state).

Ý nghĩa của $$\delta(q, a) = (q', b, D)$$: ở trạng thái $$q$$ đọc $$a$$, máy chuyển sang $$q'$$, **viết** $$b$$ lên ô hiện tại (đè lên $$a$$), và **di chuyển** đầu sang trái ($$L$$) hoặc phải ($$R$$).

### Hoạt động

1. Đầu vào $$w \in \Sigma^*$$ được ghi liên tục trên băng, các ô còn lại chứa $$\sqcup$$.
2. Đầu đọc-ghi ở ô đầu tiên, trạng thái là $$q_0$$.
3. Mỗi bước: đọc ký hiệu trên ô hiện tại, tra cứu $$\delta$$, viết, di chuyển, đổi trạng thái.
4. Dừng khi vào $$q_{\text{accept}}$$ (chấp nhận) hoặc $$q_{\text{reject}}$$ (từ chối).
5. Nếu chạy mãi không dừng: TM **lặp vô hạn** (loop) - đây là trường hợp đặc biệt cần lưu ý!

## 3. Cấu hình và ngôn ngữ

**Định nghĩa**: **Cấu hình** (configuration) của TM tại một thời điểm là bộ ba: nội dung băng, vị trí đầu, trạng thái hiện tại. Thường viết dạng $$uqv$$ - nghĩa là băng chứa $$uv$$, đầu ở ký hiệu đầu tiên của $$v$$, trạng thái $$q$$.

Quan hệ "một bước chuyển": $$C_1 \vdash C_2$$ nếu áp dụng $$\delta$$ đúng một lần.

**Ngôn ngữ chấp nhận**: $$L(M) = \{w \in \Sigma^* : q_0 w \vdash^* u q_{\text{accept}} v\}$$.

### Hai lớp ngôn ngữ liên quan đến TM

- **Recursively enumerable** (đếm được đệ quy / Turing-recognizable): tồn tại TM chấp nhận đúng các chuỗi trong $$L$$; có thể loop trên các chuỗi ngoài $$L$$.
- **Recursive** (đệ quy / decidable): tồn tại TM **luôn dừng** với mọi đầu vào, chấp nhận $$L$$ và từ chối phần còn lại.

Mọi ngôn ngữ decidable đều recognizable; chiều ngược lại **sai**. Bài toán dừng là ví dụ kinh điển: recognizable nhưng không decidable (sẽ chứng minh ở chương 20).

## 4. Ví dụ

<div class="content-box example-box" markdown="1">
**Ví dụ 1**: TM tăng số nhị phân lên 1.

Đầu vào: chuỗi bit, đầu ở bit thấp nhất (bên phải).

- $$q_0$$: di chuyển sang phải đến cuối chuỗi. Khi gặp $$\sqcup$$, lùi 1 ô và sang $$q_1$$.
- $$q_1$$: nếu đọc `0`, viết `1`, vào $$q_{\text{accept}}$$. Nếu đọc `1`, viết `0`, di chuyển trái, ở lại $$q_1$$ (lan truyền nhớ).
- Nếu lùi đến đầu chuỗi mà vẫn `1`: viết `1` ở bên trái, vào $$q_{\text{accept}}$$.

Ví dụ `1011` $$\to$$ `1100`.
</div>

<div class="content-box example-box" markdown="1">
**Ví dụ 2**: TM nhận diện $$L = \{a^n b^n c^n : n \geq 0\}$$ - không chính quy, **không** phi ngữ cảnh.

Ý tưởng: lặp - mỗi lần xóa một `a`, một `b`, một `c`. Khi băng còn trắng và mỗi loại đều khớp: chấp nhận.

- $$q_0$$: đọc `a`, viết `X`, di chuyển phải, sang $$q_1$$.
- $$q_1$$: bỏ qua `a` và `Y` (đã đánh dấu), đến `b` đầu tiên, viết `Y`, sang $$q_2$$.
- $$q_2$$: bỏ qua `b` và `Z`, đến `c` đầu tiên, viết `Z`, sang $$q_3$$.
- $$q_3$$: quay về đầu chuỗi (tìm `X` phải nhất), sang $$q_0$$.
- Khi $$q_0$$ thấy `Y` (hết `a` chưa đánh dấu): kiểm tra hết `b`, `c`. Nếu đều đã đánh dấu, chấp nhận; ngược lại từ chối.

TM này dùng bộ nhớ tuyến tính so với đầu vào, dừng sau $$O(n^2)$$ bước.
</div>

## 5. Luận đề Church-Turing

**Luận đề Church-Turing (Church-Turing thesis)**: Mọi quy trình tính toán "trực giác là hiệu quả" (effective procedure / algorithm) đều có thể mô phỏng bởi một máy Turing.

Đây không phải là một định lý có thể chứng minh - khái niệm "thuật toán" trực giác không hình thức. Nó là một **luận đề khoa học**, được chấp nhận vì:

- Mọi mô hình tính toán hình thức được đề xuất từ 1936 đến nay (lambda calculus, hàm đệ quy partial, máy Post, máy đếm, mọi ngôn ngữ lập trình Turing-complete) đều chứng minh **tương đương** với máy Turing.
- Không ai từng tìm ra "thuật toán trực giác" mà máy Turing không mô phỏng được.

<div class="content-box insight-box" markdown="1">
**Ý nghĩa**: luận đề Church-Turing cho phép ta nói "thuật toán" và "máy Turing" gần như đồng nghĩa khi làm lý thuyết. Khi muốn chứng minh **không có thuật toán** giải bài toán nào đó, ta chứng minh không có máy Turing giải nó. Đây là cách Turing chứng minh **bài toán dừng không quyết định được** năm 1936.
</div>

## 6. Biến thể máy Turing

Tất cả các biến thể sau đều **tương đương** với TM gốc về sức biểu đạt:

- **TM đa băng (multi-tape TM)**: nhiều dải băng song song, mỗi băng có đầu riêng. Mô phỏng TM 1 băng nhưng có thể nhanh hơn theo đa thức (giảm độ phức tạp thời gian).
- **TM không tất định (NTM)**: hàm $$\delta$$ trả về tập các (trạng thái, ký hiệu, hướng). Tương đương về sức mạnh, nhưng có thể nhanh hơn theo cấp số mũ. Liên hệ với lớp NP.
- **TM 2 chiều**: băng vô hạn hai chiều thay vì một chiều. Tương đương.
- **Máy đếm, máy Post, lambda calculus, hàm đệ quy partial**: đều tương đương với TM (định lý Kleene-Turing-Church).

## 7. Máy Turing phổ dụng

**Định nghĩa**: Một **máy Turing phổ dụng** (Universal Turing Machine, UTM) là một TM $$U$$ nhận đầu vào dạng $$(\langle M \rangle, w)$$ (mã hóa của một TM $$M$$ và đầu vào $$w$$), và mô phỏng chạy $$M$$ trên $$w$$.

UTM là **mô hình toán học** của khái niệm "máy tính chương trình lưu trữ" (stored-program computer): cùng một phần cứng có thể chạy bất kỳ phần mềm nào nếu phần mềm được mã hóa thành dữ liệu trên dải băng. Đây là ý tưởng nền tảng của kiến trúc Von Neumann mà mọi máy tính hiện đại đều dựa vào.

<div class="content-box info-box" markdown="1">
**Tính phổ dụng và bài toán dừng**

Sự tồn tại của UTM dẫn trực tiếp đến bài toán dừng:

$$\text{HALT} = \{(\langle M \rangle, w) : M \text{ dừng trên đầu vào } w\}$$

Nếu HALT decidable, ta có một thuật toán quyết định mọi câu hỏi "chương trình này có dừng không". Turing chứng minh **không tồn tại** thuật toán đó - lập luận phản chứng dựa vào lý luận chéo (diagonal argument) tương tự định lý Cantor.
</div>

## Tổng kết

- **TM** = $$(Q, \Sigma, \Gamma, \delta, q_0, q_{\text{accept}}, q_{\text{reject}})$$ với băng vô hạn và đầu đọc-ghi tự do.
- Hai lớp: **recognizable** (TM có thể chấp nhận nhưng có thể loop) và **decidable** (TM luôn dừng).
- **Luận đề Church-Turing**: mọi thuật toán trực giác đều mô phỏng được bằng TM.
- Mọi biến thể TM (đa băng, không tất định) đều tương đương về sức biểu đạt.
- **UTM** là mô hình toán học của máy tính chương trình lưu trữ.
- TM là cơ sở cho lớp **độ phức tạp tính toán** mà ta sẽ học ở chương 20.

## Bài tập

1. Mô phỏng từng bước TM ở Ví dụ 1 với đầu vào `1111`. Liệt kê cấu hình sau mỗi bước.
2. Thiết kế TM nhận diện $$L = \{w \in \{0, 1\}^* : w \text{ là chuỗi palindrome}\}$$.
3. Thiết kế TM tính phép cộng hai số nhị phân (đầu vào `a + b`, đầu ra `a + b`).
4. Vẽ sơ đồ chuyển trạng thái rút gọn cho TM ở Ví dụ 2.
5. Chứng minh: nếu $$L$$ decidable thì $$\Sigma^* \setminus L$$ cũng decidable.
6. Chứng minh: nếu $$L$$ và $$\Sigma^* \setminus L$$ đều recognizable thì $$L$$ decidable. (Đây là một kết quả quan trọng cho chương 20.)
7. Giải thích vì sao **không** có "thuật toán" quyết định liệu hai TM bất kỳ có chấp nhận cùng ngôn ngữ.

<div class="content-box note-box" markdown="1">
**Tài liệu tham khảo**

- Rosen, K. H. (2019). *Discrete Mathematics and Its Applications*, 8th ed. Section 13.5.
- Sipser, M. (2013). *Introduction to the Theory of Computation*, 3rd ed. Chapter 3.
- Hopcroft, J., Motwani, R., & Ullman, J. (2007). *Introduction to Automata Theory*, 3rd ed. Chapter 8.
- Turing, A. M. (1936). "On computable numbers, with an application to the Entscheidungsproblem." *Proceedings of the London Mathematical Society*, 2(42), 230-265. (bài báo gốc)
</div>
