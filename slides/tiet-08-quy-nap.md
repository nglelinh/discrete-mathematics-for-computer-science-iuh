---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Quy nạp Toán học

**Toán Rời Rạc**

Tiết 8 (45 phút) — Mathematical Induction

---

## Mục tiêu tiết học

- Hiểu trực giác domino và cấu trúc quy nạp
- Phát biểu đúng mệnh đề $$P(n)$$, bước cơ sở, giả thiết quy nạp, bước quy nạp
- Viết chứng minh quy nạp hoàn chỉnh cho công thức, bất đẳng thức, chia hết
- Mô hình hóa **bài toán con thỏ** → dãy Fibonacci và quan hệ truy hồi
- Liên hệ quy nạp với đệ quy và chứng minh thuật toán

---

## Trực giác Domino

Hãy tưởng tượng hàng domino vô hạn:

- Quân đầu **ngã** → bước cơ sở
- Mỗi quân $$k$$ làm quân $$k+1$$ ngã → bước quy nạp

Kết quả: **toàn bộ** domino ngã.

Trong quy nạp: $$P(n)$$ = "quân thứ $$n$$ đã ngã".

Chứng minh phải viết bằng ngôn ngữ toán học chính xác.

---

## Mệnh đề $$P(n)$$

**Mệnh đề quy nạp** $$P(n)$$: khẳng định phụ thuộc số tự nhiên $$n$$.

**Ví dụ**:
- $$P(n)$$: $$1+2+\cdots+n = \frac{n(n+1)}{2}$$
- $$P(n)$$: $$2^{n} > n$$
- $$P(n)$$: $$n^{3} - n$$ chia hết cho 3

**Miền giá trị**: thường $$n \ge n_0$$ ($$n_0 = 0, 1, 2, \ldots$$).

---

## Nguyên lý Quy nạp Toán học

Chứng minh $$P(n)$$ đúng với mọi $$n \ge n_0$$ bằng **hai bước**:

1. **Bước cơ sở** (Base case): chứng minh $$P(n_0)$$
2. **Bước quy nạp** (Inductive step): với $$k \ge n_0$$ bất kỳ,  
   **Giả thiết quy nạp** $$P(k)$$ → chứng minh $$P(k+1)$$

**Dạng logic**:
$$P(n_0) \land \forall k \ge n_0\,[P(k) \Rightarrow P(k+1)] \Rightarrow \forall n \ge n_0\, P(n)$$

---

## Mẫu trình bày chuẩn

1. Nêu rõ $$P(n)$$ và miền $$n \ge n_0$$
2. **Bước cơ sở**: kiểm tra $$P(n_0)$$
3. **Giả thiết quy nạp**: "Giả sử $$P(k)$$ đúng với $$k \ge n_0$$"
4. **Bước quy nạp**: chứng minh $$P(k+1)$$
5. Kết luận: theo nguyên lý quy nạp, $$P(n)$$ đúng ∀$$n \ge n_0$$. ∎

---

## Ví dụ 1: Tổng $$1+2+\cdots+n$$

**Định lý**: $$\forall n \ge 1,\; 1+2+\cdots+n = \frac{n(n+1)}{2}$$

**Bước cơ sở** ($$n=1$$): $$1 = \frac{1\cdot 2}{2} = 1$$ ✓

**Giả thiết quy nạp**: $$1+\cdots+k = \frac{k(k+1)}{2}$$

**Bước quy nạp**:
$$1+\cdots+k+(k+1) = \frac{k(k+1)}{2}+(k+1) = \frac{(k+1)(k+2)}{2}$$

Đúng dạng $$P(k+1)$$. ∎

---

## Ví dụ 2: $$ 2^{n} > n $$

**Định lý**: $$\forall n \ge 1,\; 2^{n} > n$$

**Bước cơ sở** ($$n=1$$): $$2^{1} = 2 > 1$$ ✓

**Giả thiết quy nạp**: $$2^{k} > k$$

**Bước quy nạp**:
$$2^{k+1} = 2\cdot 2^{k} > 2k \ge k+1$$ (vì $$k \ge 1$$)

Suy ra $$2^{k+1} > k+1$$. ∎

---

## Ví dụ 3: Chia hết

**Định lý**: $$\forall n \ge 0,\; n^{3} - n$$ chia hết cho 3.

**Bước cơ sở** ($$n=0$$): $$0^{3}-0=0$$ chia hết cho 3 ✓

**Giả thiết quy nạp**: $$3 \mid (k^{3}-k)$$

**Bước quy nạp**: phân tích $$(k+1)^{3}-(k+1)$$ và dùng $$k^{3}-k = 3m$$.

Kết quả: $$(k+1)^{3}-(k+1) = 3m + 3k(k+1)$$ → chia hết cho 3. ∎

---

## Bài toán con thỏ 

**Fibonacci** (1202, *Liber Abaci*): đặt **một đôi thỏ** mới sinh vào chuồng.

**Quy tắc**:
- Mỗi đôi thỏ sinh **một đôi con** mỗi tháng (bắt đầu từ tháng thứ 2)
- Đôi con cần **1 tháng** trưởng thành mới sinh tiếp
- Thỏ **không chết**, không rời chuồng

**Câu hỏi**: Sau $$n$$ tháng có **bao nhiêu đôi thỏ**?

---

| Tháng $$n$$ | Số đôi $$F_n$$ | Giải thích ngắn |
|:---:|:---:|:---|
| 1 | 1 | 1 đôi ban đầu (chưa sinh) |
| 2 | 1 | vẫn 1 đôi (vừa trưởng thành) |
| 3 | 2 | 1 cũ + 1 con mới |
| 4 | 3 | 2 cũ + 1 con từ đôi trưởng thành |
| 5 | 5 | 3 cũ + 2 con mới |
| 6 | 8 | 5 cũ + 3 con mới |

---

**Nhận xét**: $$F_n = F_{n-1} + F_{n-2}$$ — mỗi tháng giữ nguyên số đôi cũ, cộng đôi con sinh ra từ các đôi **đã trưởng thành** ở tháng $$n-2$$.

---

## Bài toán con thỏ — Quy nạp & Đệ quy

**Đệ quy** = bước cơ sở + bước đệ quy → cùng cấu trúc với quy nạp.

Đệ quy: là một kỹ thuật định nghĩa hoặc lập trình — một hàm được định nghĩa bằng cách gọi lại chính nó.

---

## Ứng dụng trong CNTT

**Chứng minh vòng lặp / đệ quy**:
- Loop invariant thường chứng minh bằng quy nạp trên số bước lặp
- Độ phức tạc đệ quy: $$T(n) = T(n-1) + O(1)$$ → $$T(n)=O(n)$$

**Ví dụ**: Chứng minh hàm tính giai thừa đệ quy trả về đúng $$n!$$.

Quy nạp là công cụ chứng minh tính đúng của **mọi** kích thước đầu vào.

---

## Thực hành 1

Chứng minh bằng quy nạp:
> $$\forall n \ge 1,\; 1+3+5+\cdots+(2n-1) = n^{2}$$

Gợi ý: bước cơ sở $$n=1$$; bước quy nạp cộng số hạng $$2(k+1)-1$$.

---

## Thực hành 2

Chứng minh bằng quy nạp:
> $$\forall n \ge 1,\; n! \ge 2^{n-1}$$

Gợi ý: từ $$k! \ge 2^{k-1}$$ suy ra $$(k+1)! = (k+1)\cdot k!$$.

---

## Thực hành 3

Phân tích lỗi:
> "Vì $$P(1), P(2), P(3)$$ đều đúng nên $$P(n)$$ đúng với mọi $$n$$."

Giải thích vì sao lập luận này **không hợp lệ** và nêu điều kiện đúng.

---

## Tóm tắt Tiết 8

- **Quy nạp** = bước cơ sở + $$(P(k) \Rightarrow P(k+1))$$
- **IH** là công cụ trong bước quy nạp, không phải giả định kết luận
- Áp dụng cho công thức, bất đẳng thức, chia hết
- **Bài toán con thỏ** → $$F_n = F_{n-1}+F_{n-2}$$ → mô hình đệ quy + quy nạp
- Gần với **đệ quy**: tin base case + bước đệ quy bảo toàn tính đúng
- Không thay thế được bằng kiểm tra vài giá trị

---

## Liên hệ

**Chứng minh chính**: Mở $$P(k+1)$$ rồi chèn $$P(k)$$ (thường qua cộng/trừ một hạng).

**Edge case**: Chọn $$n_0$$ đúng — ví dụ $$2^{n} > n^{2}$$ cần $$n \ge 5$$.

**Liên hệ**: Bài toán con thỏ → Fibonacci; Quy nạp ↔ Đệ quy ↔ HTTH (tiết 24).

**Ứng dụng**: Chứng minh correctness, phân tích độ phức tạp, structural induction.

---

## Bài tập ôn tập (1/2)

1. **Bài 1**: Chứng minh $$\sum_{i=1}^{n} i^{2} = \frac{n(n+1)(2n+1)}{6}$$.

2. **Bài 2**: Chứng minh $$3 \mid (4^{n} - 1)$$ với mọi $$n \ge 0$$.

3. **Bài 3**: Chứng minh $$n! > 2^{n}$$ với mọi $$n \ge 4$$.

---

## Bài tập ôn tập (2/2)

4. **Bài 4**: Viết base case + inductive step cho: mọi xâu nhị phân độ dài $$n$$ có $$2^{n}$$ xâu.

5. **Bài 5**: Chứng minh công thức Fibonacci
   $$F_1+\cdots+F_n = F_{n+2}-1$$ bằng quy nạp.
