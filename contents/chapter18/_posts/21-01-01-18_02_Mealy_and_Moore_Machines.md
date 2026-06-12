---
layout: post
title: "Máy Mealy và Máy Moore"
categories: chapter18
date: 2021-01-01
order: 2
required: true
lang: en
---

# Máy Mealy và Máy Moore

Một bộ điều khiển đèn giao thông cần làm nhiều việc hơn là "chấp nhận" hay "từ chối" một chuỗi sự kiện - nó phải **phát ra tín hiệu** điều khiển đèn đỏ, vàng, xanh cho phù hợp. Một bộ giải mã (decoder) trong vi xử lý không chỉ nhận chuỗi bit, nó còn phải sinh ra chuỗi bit khác làm tín hiệu điều khiển. Khi ta cần một máy hữu hạn trạng thái **xuất ra dữ liệu**, ta dùng một trong hai mô hình kinh điển: **máy Mealy** và **máy Moore**.

Cả hai đều mở rộng DFA bằng cách thêm bảng chữ cái đầu ra và hàm sinh đầu ra. Khác biệt duy nhất là **thời điểm** sinh đầu ra: máy Moore phát ra một ký hiệu ứng với mỗi trạng thái, còn máy Mealy phát ra ký hiệu ứng với mỗi **cạnh chuyển** (tức là phụ thuộc vào cả trạng thái và đầu vào). Khác biệt nhỏ này dẫn đến những hệ quả thực tế: máy Mealy thường có ít trạng thái hơn, máy Moore lại dễ phân tích thời gian hơn trong thiết kế mạch số.

## Mục tiêu học tập

Sau khi hoàn thành bài này, sinh viên có thể:

- **Định nghĩa** hình thức máy Mealy và máy Moore.
- **Vẽ** sơ đồ chuyển trạng thái cho máy Mealy và máy Moore.
- **Tính** chuỗi đầu ra của một máy khi cho chuỗi đầu vào.
- **Chuyển đổi** giữa hai mô hình Mealy và Moore.
- **Mô hình hóa** một bài toán điều khiển nhỏ bằng máy có đầu ra.

**Từ khóa**: máy Moore (Moore machine), máy Mealy (Mealy machine), máy biến đổi (transducer), bảng chữ cái đầu ra (output alphabet), hàm đầu ra (output function), mạch tuần tự (sequential circuit).

## 1. Máy Moore

**Định nghĩa**: Một **máy Moore** là một bộ sáu $$M = (Q, \Sigma, \Delta, \delta, \lambda, q_0)$$ gồm:

- $$Q$$: tập trạng thái hữu hạn.
- $$\Sigma$$: bảng chữ cái đầu vào (input alphabet).
- $$\Delta$$: bảng chữ cái đầu ra (output alphabet).
- $$\delta: Q \times \Sigma \to Q$$: hàm chuyển trạng thái.
- $$\lambda: Q \to \Delta$$: **hàm đầu ra Moore** - phát ra một ký hiệu ứng với mỗi trạng thái.
- $$q_0 \in Q$$: trạng thái khởi đầu.

Không có tập trạng thái chấp nhận vì máy Moore không "nhận diện ngôn ngữ" mà "biến đổi chuỗi".

### Cách máy Moore hoạt động

Cho đầu vào $$w = a_1 a_2 \ldots a_n$$, máy đi qua các trạng thái $$q_0, q_1, \ldots, q_n$$ (với $$q_i = \delta(q_{i-1}, a_i)$$) và phát ra chuỗi:

$$\lambda(q_0) \lambda(q_1) \ldots \lambda(q_n)$$

Lưu ý: đầu ra có độ dài $$n + 1$$, **dài hơn** đầu vào một ký hiệu - chính là $$\lambda(q_0)$$ phát ra trước khi đọc gì cả.

<div class="content-box example-box" markdown="1">
**Ví dụ 1**: Máy Moore phát hiện **mẫu `aab`** trong chuỗi trên $$\{a, b\}$$.

- $$Q = \{q_0, q_1, q_2, q_3\}$$ ứng với việc đã thấy phần đầu nào của `aab`.
- $$\Delta = \{0, 1\}$$ (0 = chưa khớp, 1 = vừa khớp xong).
- $$\delta$$:
  - $$\delta(q_0, a) = q_1$$, $$\delta(q_0, b) = q_0$$.
  - $$\delta(q_1, a) = q_2$$, $$\delta(q_1, b) = q_0$$.
  - $$\delta(q_2, a) = q_2$$, $$\delta(q_2, b) = q_3$$.
  - $$\delta(q_3, a) = q_1$$, $$\delta(q_3, b) = q_0$$.
- $$\lambda(q_0) = \lambda(q_1) = \lambda(q_2) = 0$$, $$\lambda(q_3) = 1$$.

Đầu vào `aabab`: trạng thái đi qua $$q_0, q_1, q_2, q_3, q_1, q_0$$; đầu ra: `000100`. Vị trí số `1` ở thứ tư đánh dấu thời điểm `aab` vừa khớp xong.
</div>

## 2. Máy Mealy

**Định nghĩa**: Một **máy Mealy** là một bộ sáu $$M = (Q, \Sigma, \Delta, \delta, \omega, q_0)$$ gồm các thành phần như máy Moore, ngoại trừ:

- $$\omega: Q \times \Sigma \to \Delta$$: **hàm đầu ra Mealy** - phát ra ký hiệu ứng với mỗi cặp (trạng thái, ký hiệu đầu vào).

### Cách máy Mealy hoạt động

Cho đầu vào $$w = a_1 a_2 \ldots a_n$$, máy phát ra:

$$\omega(q_0, a_1) \omega(q_1, a_2) \ldots \omega(q_{n-1}, a_n)$$

trong đó $$q_i = \delta(q_{i-1}, a_i)$$. Đầu ra có độ dài **đúng bằng** đầu vào, không thêm ký hiệu nào.

<div class="content-box example-box" markdown="1">
**Ví dụ 2**: Máy Mealy phát hiện mẫu `aab` (giải lại Ví dụ 1).

- $$Q = \{q_0, q_1, q_2\}$$.
- $$\delta$$ tương tự như máy Moore, nhưng giảm số trạng thái:
  - $$\delta(q_0, a) = q_1$$, $$\delta(q_0, b) = q_0$$.
  - $$\delta(q_1, a) = q_2$$, $$\delta(q_1, b) = q_0$$.
  - $$\delta(q_2, a) = q_2$$, $$\delta(q_2, b) = q_0$$.
- $$\omega$$:
  - $$\omega(q_0, a) = \omega(q_0, b) = 0$$.
  - $$\omega(q_1, a) = 0$$, $$\omega(q_1, b) = 0$$.
  - $$\omega(q_2, a) = 0$$, $$\omega(q_2, b) = 1$$ (cạnh $$q_2 \xrightarrow{b/1} q_0$$ đánh dấu khớp).

Đầu vào `aabab`: trạng thái $$q_0, q_1, q_2, q_0, q_1, q_0$$; đầu ra `00100`. So với máy Moore, ta tiết kiệm 1 trạng thái.
</div>

## 3. Sơ đồ chuyển trạng thái

Hai mô hình có quy ước vẽ khác nhau:

- **Máy Moore**: ghi đầu ra **trong** nút trạng thái, ví dụ `q_3 / 1`.
- **Máy Mealy**: ghi đầu ra trên **cạnh chuyển**, dạng `a / 1` nghĩa là "đầu vào `a`, đầu ra `1`".

Cùng một bài toán biến đổi chuỗi thường có **máy Mealy nhỏ hơn** vì nó "tận dụng" được thông tin từ ký hiệu đang đọc, không phải đợi đến trạng thái kế tiếp.

## 4. Sự tương đương Mealy - Moore

**Định lý**: Mọi máy Mealy có thể chuyển thành máy Moore tương đương (sinh cùng hàm biến đổi chuỗi đầu vào - đầu ra, có thể chênh lệch một ký hiệu khởi tạo), và ngược lại.

**Ý tưởng chuyển Mealy → Moore**: với mỗi cặp (trạng thái Mealy, ký hiệu đầu ra) tạo một trạng thái Moore mới. Tổng số trạng thái Moore không vượt quá $$|Q| \cdot |\Delta|$$.

**Ý tưởng chuyển Moore → Mealy**: định nghĩa $$\omega(q, a) = \lambda(\delta(q, a))$$. Đầu ra trên cạnh đến trạng thái $$q'$$ chính là $$\lambda(q')$$.

<div class="content-box info-box" markdown="1">
**So sánh thực tế**

| Tiêu chí | Máy Moore | Máy Mealy |
|---|---|---|
| Đầu ra phụ thuộc vào | Trạng thái | Trạng thái + đầu vào |
| Số trạng thái | Thường nhiều hơn | Thường ít hơn |
| Phản ứng | Trễ một chu kỳ | Tức thời (cùng chu kỳ) |
| Phân tích thời gian (timing) | Dễ hơn | Khó hơn |
| Vẽ sơ đồ | Đầu ra trong nút | Đầu ra trên cạnh |

Trong thiết kế ASIC/FPGA, kỹ sư thường bắt đầu bằng Mealy để tiết kiệm tài nguyên, rồi chuyển sang Moore khi cần phân tích timing rõ ràng.
</div>

## 5. Ứng dụng: mạch tuần tự và bộ điều khiển

- **Bộ cộng tuần tự (serial adder)**: nhận hai chuỗi bit và phát ra chuỗi bit tổng. Trạng thái lưu **bit nhớ** (carry); đầu ra là bit tổng. Đây là một máy Mealy 2 trạng thái cổ điển.
- **Bộ điều khiển đèn giao thông**: trạng thái biểu diễn pha đèn (đỏ, xanh, vàng cho mỗi hướng); đầu vào là bộ đếm thời gian; đầu ra là tín hiệu điều khiển đèn.
- **Bộ phát hiện chuỗi (sequence detector)**: dùng trong giao thức truyền tin để phát hiện chuỗi mở đầu (preamble) hoặc mẫu lỗi.
- **Phân tích từ vựng nâng cao**: một số trình biên dịch dùng máy Moore để gắn nhãn loại token ngay khi DFA chuyển trạng thái.

## Tổng kết

- **Máy Moore** phát đầu ra theo **trạng thái**: $$\lambda: Q \to \Delta$$.
- **Máy Mealy** phát đầu ra theo **cạnh chuyển**: $$\omega: Q \times \Sigma \to \Delta$$.
- Hai mô hình có **sức mạnh biểu đạt tương đương**, nhưng Mealy thường gọn hơn.
- Cả hai là nền tảng của thiết kế **mạch tuần tự** và **bộ điều khiển nhúng**.

## Bài tập

1. Vẽ máy Mealy thực hiện **bộ cộng tuần tự** hai số nhị phân (đọc các bit từ thấp đến cao). Trạng thái biểu diễn bit nhớ (carry).
2. Cho máy Moore ở Ví dụ 1. Chuyển nó về máy Mealy theo công thức $$\omega(q, a) = \lambda(\delta(q, a))$$ và so sánh số trạng thái.
3. Thiết kế máy Moore biến đổi chuỗi nhị phân: với mỗi bit đầu vào, phát ra bit `1` nếu trạng thái hiện tại đã thấy **chẵn** số `1`, ngược lại phát `0`.
4. Một máy Mealy có 3 trạng thái và bảng chữ cái $$\{0, 1\}$$. Có tối đa bao nhiêu hàm chuyển $$\delta$$ khác nhau? Có tối đa bao nhiêu hàm đầu ra $$\omega$$ khác nhau (với $$\Delta = \{0, 1\}$$)?
5. Mô hình hóa một **đèn giao thông hai pha** (Đỏ - Xanh) đơn giản bằng máy Moore với đầu vào là tín hiệu "đến giờ chuyển pha".

<div class="content-box note-box" markdown="1">
**Tài liệu tham khảo**

- Rosen, K. H. (2019). *Discrete Mathematics and Its Applications*, 8th ed. Section 13.2.
- Sipser, M. (2013). *Introduction to the Theory of Computation*, 3rd ed. Chapter 1 (mở rộng).
- Hopcroft, J., Motwani, R., & Ullman, J. (2007). *Introduction to Automata Theory, Languages, and Computation*, 3rd ed. Chapter 2.
- Mano, M. M., & Ciletti, M. D. (2018). *Digital Design*, 6th ed. (góc nhìn mạch số).
</div>
