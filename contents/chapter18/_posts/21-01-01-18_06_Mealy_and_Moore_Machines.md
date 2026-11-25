---
layout: post
title: "Máy Mealy và Moore"
categories: chapter18
date: 2021-01-01
order: 6
required: true
lang: en
excerpt: "Bộ biến đổi hữu hạn trạng thái (transducer), so sánh hàm đầu ra λ(q) và ω(q,a), độ dài chuỗi ra và sự tương đương giữa máy Moore và máy Mealy."
---

> **Câu chuyện mở đầu:** DFA chỉ trả lời duy nhất "Có" hoặc "Không" sau khi đọc hết cả chuỗi. Nhưng một chiếc máy bán hàng tự động, bộ điều khiển đèn giao thông hay bộ giải mã tín hiệu mạng cần **phát ra đầu ra liên tục tại từng nhịp đồng hồ**! Đó chính là **Máy Moore** (đầu ra gắn vào trạng thái) và **Máy Mealy** (đầu ra gắn vào mũi tên chuyển trạng thái) — hai kiến trúc nền tảng của mọi mạch tuần tự số (FSM)!

<div class="textbook-epigraph" markdown="1">

"Moore outputs on states; Mealy on edges."

<span class="epigraph-attribution">— Sequential machine theory</span>

</div>

![Mealy Moore](/discrete-mathematics-for-computer-science-iuh/img/course/Automata_mealy_moore.svg)

<p class="textbook-figure-caption" data-figure="18.4">Hai kiểu bộ biến đổi (transducer) hữu hạn trạng thái: máy Moore gắn đầu ra ở trạng thái, còn máy Mealy gắn đầu ra ở cạnh chuyển.</p>

## Mục tiêu

<div class="textbook-objectives" markdown="1">

- **Định nghĩa** máy Moore và máy Mealy.
- **Tính** chuỗi đầu ra tương ứng với một chuỗi đầu vào cho trước.
- **Phác thảo** cách chuyển đổi qua lại giữa máy Moore và máy Mealy.

</div>

## Kiến thức cần nhớ: So sánh Máy Moore và Máy Mealy

### 1. Máy Moore: Đầu ra chỉ phụ thuộc Trạng thái hiện tại ($$\lambda: Q \to \Gamma$$)
- **Bản chất:** Ngay khi ở trạng thái $$q_0$$ (chưa đọc ký tự nào), máy Moore đã phát ra ký tự đầu tiên $$\lambda(q_0)$$. Vì thế với đầu vào dài $$n$$, đầu ra có độ dài **$$n + 1$$**.
- **Ưu điểm phần cứng:** An toàn, không bị nhiễu gai (glitch) từ tín hiệu đầu vào; nhưng thường phản ứng **chậm hơn 1 chu kỳ xung nhịp** và cần nhiều trạng thái hơn.

### 2. Máy Mealy: Đầu ra phụ thuộc CẢ Trạng thái lẫn Đầu vào ($$\lambda: Q \times \Sigma \to \Gamma$$)
- **Bản chất:** Đầu ra được ghi ngay trên cạnh chuyển dạng `input / output`. Với đầu vào dài $$n$$, đầu ra có độ dài đúng **$$n$$**.
- **Ưu điểm phần cứng:** Phản ứng **tức thì** trong cùng chu kỳ và thường cần **ít trạng thái hơn** Máy Moore!

### 3. Tương đương Chức năng Moore $$\leftrightarrow$$ Mealy
- **Bản chất:** Mọi máy Moore đều chuyển được sang máy Mealy tương đương (bỏ qua ký tự đầu $$\lambda(q_0)$$) và ngược lại (nhân bản trạng thái của Mealy theo từng đầu ra có thể đi vào nó — tối đa $$\lvert Q\rvert \cdot \lvert\Gamma\rvert$$ trạng thái!).

## Ví dụ tính tay làm từng bước: Bộ phát hiện chuỗi con `01` trên đầu vào `0101`

Mục tiêu: xuất `1` ngay khi vừa nhận xong chuỗi con `01`, các vị trí khác xuất `0`.
1. **Máy Mealy (chỉ cần 2 trạng thái $$q_0, q_1$$):**
   - $$q_0$$ (chưa vừa đọc `0`): `0 / 0` $$\to q_1$$; `1 / 0` $$\to q_0$$.
   - $$q_1$$ (vừa đọc `0`): `0 / 0` $$\to q_1$$; `1 / 1` $$\to q_0$$ (xuất `1` ngay!).
   - **Chạy trên `0101`:** $$q_0 \xrightarrow{0/0} q_1 \xrightarrow{1/1} q_0 \xrightarrow{0/0} q_1 \xrightarrow{1/1} q_0 \implies$$ đầu ra **`0101`** (độ dài 4!).
2. **Máy Moore (cần 3 trạng thái $$q_0[0],\; q_1[0],\; q_2[1]$$):**
   - $$q_2$$ chuyên để xuất `1` khi vừa nhận xong `01`!
   - **Chạy trên `0101`:** $$q_0[0] \xrightarrow{0} q_1[0] \xrightarrow{1} q_2[1] \xrightarrow{0} q_1[0] \xrightarrow{1} q_2[1] \implies$$ đầu ra **`00101`** (độ dài 5 — thêm đúng 1 bit khởi đầu `0`!).

### Giải thích: 4 bước chọn và chuyển đổi giữa Moore và Mealy
#### Bước 1: Kiểm tra độ dài đầu ra
Nếu đầu ra dài $$n$$ (phản ứng đồng thời với đầu vào) $$\to$$ **Mealy**; nếu dài $$n + 1$$ (có trạng thái khởi tạo ban đầu) $$\to$$ **Moore**.

#### Bước 2: Chuyển Moore $$\to$$ Mealy (siêu dễ!)
Giữ nguyên toàn bộ trạng thái; trên mọi cạnh $$p \xrightarrow{a} q$$, gắn nhãn đầu ra chính là $$\lambda_{\text{Moore}}(q)$$ (đầu ra của trạng thái đích!).

#### Bước 3: Chuyển Mealy $$\to$$ Moore (tách trạng thái theo đầu ra đi vào)
Nếu trạng thái $$q$$ của Mealy nhận cả cạnh có đầu ra `0` lẫn cạnh có đầu ra `1` đi vào, hãy tách $$q$$ thành 2 bản sao $$q^{(0)}$$ (xuất `0`) và $$q^{(1)}$$ (xuất `1`), giữ nguyên các mũi tên đi ra!

#### Bước 4: Đánh đổi trong thiết kế mạch số (Verilog / FPGA)
Dùng **Moore** cho tín hiệu điều khiển nhạy cảm với nhiễu xung (đầu ra đồng bộ hoàn toàn theo clock); dùng **Mealy** khi cần tối ưu độ trễ 0-cycle và giảm số Flip-Flop!

$$
\text{Moore: } \lambda(q)\;(\text{dài }n+1,\text{ sạch nhiễu})
\quad\Longleftrightarrow\quad
\text{Mealy: } \lambda(q, a)\;(\text{dài }n,\text{ ít trạng thái, tức thì}).
$$

## Máy Moore

Máy Moore được định nghĩa là bộ sáu $$M=(Q,\Sigma,\Delta,\delta,\lambda,q_0)$$, trong đó hàm đầu ra $$\lambda:Q\to\Delta$$ chỉ phụ thuộc vào trạng thái hiện tại. Với chuỗi đầu vào $$a_1\ldots a_n$$, máy sinh ra chuỗi đầu ra $$\lambda(q_0)\lambda(q_1)\ldots\lambda(q_n)$$ có độ dài $$n+1$$.

## Máy Mealy

Trong máy Mealy, hàm đầu ra $$\omega:Q\times\Sigma\to\Delta$$ phụ thuộc vào cả trạng thái hiện tại lẫn ký hiệu đầu vào. Với chuỗi đầu vào $$a_1\ldots a_n$$, máy sinh ra chuỗi đầu ra $$\omega(q_0,a_1)\ldots\omega(q_{n-1},a_n)$$ có độ dài $$n$$.

## Tính tương đương giữa hai mô hình

<div class="textbook-theorem" markdown="1">

**Định lý** (Ý chính). Mọi máy Mealy đều có một máy Moore tương đương (với độ trễ đầu ra bằng 1, xét theo ký tự đầu ra khởi tạo) và ngược lại, bằng cách mở rộng không gian trạng thái để lưu thông tin đầu ra.

</div>

**Ý tưởng chuyển đổi:**  
Từ Mealy sang Moore: tách mỗi trạng thái $$q$$ thành các cặp $$(q,\mathrm{last\_out})$$ sao cho mọi cạnh đi vào đều mang cùng một giá trị đầu ra, rồi gán $$\lambda$$ theo giá trị đó.  
Từ Moore sang Mealy: định nghĩa trực tiếp $$\omega(q,a)=\lambda(\delta(q,a))$$ (bỏ qua giá trị khởi tạo $$\lambda(q_0)$$ nếu chuẩn hóa cùng độ dài $$n$$).

### Thử nghiệm: máy Mealy và Moore

Chạy máy có đầu ra theo từng ký tự để quan sát dãy đầu ra được sinh ra:

<div class="interactive-demo" markdown="1">
<div data-demo="mealy-explainer" data-preset="m11"></div>
</div>
<script src="{{ '/public/js/explainers/language-explainer.js' | relative_url }}"></script>

## Bài tập

1. Xây dựng máy Mealy đảo bit và chứng minh chuỗi đầu ra là phần bù từng bit của chuỗi đầu vào.
2. So sánh độ trễ (*latency*) giữa máy Moore và máy Mealy khi triển khai trên mạch số phần cứng.
3. Thiết kế máy Mealy hoặc máy Moore phát hiện chuỗi con `aab`.

## Tài liệu đọc thêm

Kohavi, *Switching and Finite Automata Theory*; Hopcroft–Ullman (phần ứng dụng).

## Tóm tắt

Máy Moore và máy Mealy là hai dạng bộ biến đổi hữu hạn trạng thái khác nhau ở cách gắn đầu ra và độ dài chuỗi ra, nhưng có thể mô phỏng lẫn nhau.

**Bài tiếp theo:** Biểu thức chính quy.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=0_OZKWdCixw">Mealy and Moore State Machines (Part 1)</a> — Neso Academy, tiếng Anh. Giới thiệu máy Mealy và Moore với đầu ra gắn theo bước chuyển hoặc trạng thái.
- <a href="https://www.youtube.com/watch?v=LioitkXDfmA">Construction of Mealy Machine</a> — Neso Academy, tiếng Anh. Cách dựng máy Mealy từ đặc tả đầu ra.
- <a href="https://www.youtube.com/watch?v=MFnRF07SoFo">Construction of Moore Machine</a> — Neso Academy, tiếng Anh. Cách dựng máy Moore để đối chiếu cùng một hành vi đầu vào–đầu ra.
