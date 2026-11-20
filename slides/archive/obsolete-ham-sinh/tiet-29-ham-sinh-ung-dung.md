---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Hàm sinh — Giải HTTH & Đếm

**Toán Rời Rạc**

Tiết 29 (45 phút) — Ứng dụng hàm sinh

---

## Mục tiêu tiết học

- Áp dụng quy trình 4 bước giải truy hồi bằng hàm sinh
- Giải Fibonacci và truy hồi bậc 1 không thuần nhất
- Dùng phân thức từng phần đọc hệ số $$a_n$$
- Đếm tổ hợp và phân hoạch bằng hàm sinh
- Liên hệ với phương trình đặc trưng

---

## Quy trình 4 bước

1. Đặt $$G(x) = \sum_{n \ge 0} a_n x^{n}$$
2. Nhân truy hồi với $$x^{n}$$, cộng theo $$n$$
3. Giải đại số → $$G(x)$$ dạng phân thức
4. Khai triển / phân tích → công thức $$a_n$$

**Mấu chốt**: Dịch chỉ số ↔ nhân $$x$$, $$x^{2}$$ trên $$G(x)$$.

---

## Ví dụ Fibonacci — Thiết lập

Truy hồi: $$F_n = F_{n-1} + F_{n-2}$$, $$F_0 = 0$$, $$F_1 = 1$$.

Đặt $$G(x) = \sum_{n \ge 0} F_n x^{n}$$.

Nhân với $$x^{n}$$, cộng $$n \ge 2$$:

$$\sum_{n \ge 2} F_n x^{n} = x\sum_{n \ge 2} F_{n-1} x^{n-1} + x^{2}\sum_{n \ge 2} F_{n-2} x^{n-2}$$

---

## Ví dụ Fibonacci — Giải

Viết lại bằng $$G(x)$$:

$$G(x) - F_0 - F_1 x = x(G(x) - F_0) + x^{2} G(x)$$

Vì $$F_0 = 0$$, $$F_1 = 1$$:

$$G(x) - x = xG(x) + x^{2} G(x)$$

$$G(x) = \frac{x}{1 - x - x^{2}}$$

---

## Phân thức từng phần

Nếu $$G(x) = \frac{P(x)}{Q(x)}$$ với $$\deg P < \deg Q$$:

1. Phân tích $$Q(x)$$ thành nhân tử
2. Tách thành $$\frac{A}{1-r_1 x} + \frac{B}{1-r_2 x} + \cdots$$
3. Khai triển: $$\frac{1}{1-rx} = \sum r^{n} x^{n}$$

**Fibonacci**: Mẫu $$1 - x - x^{2} = 0$$ có nghiệm $$\varphi$$, $$\hat{\varphi}$$ → công thức Binet.

---

## Định lý — Hai con đường

**Phương trình đặc trưng** (tiết 19) và **hàm sinh** cho cùng nghiệm truy hồi tuyến tính.

| Phương pháp | Ưu điểm |
|:---|:---|
| Đặc trưng | Nhanh, trực tiếp |
| Hàm sinh | Mạnh với HTTH phức tạp, không thuần nhất |

**Edge case**: Nghiệm kép → thêm hệ số $$n$$ trong khai triển.

---

## Ví dụ — Truy hồi bậc 1 không thuần nhất

$$a_n = 2a_{n-1} + 1$$, $$a_0 = 0$$.

$$G(x) - a_0 = 2xG(x) + \sum_{n \ge 1} x^{n} = 2xG(x) + \frac{x}{1-x}$$

$$G(x) = \frac{x}{(1-x)(1-2x)}$$

Phân tích: $$G(x) = \frac{-1}{1-x} + \frac{1}{1-2x}$$ → $$a_n = 2^{n} - 1$$.

---

## Đếm tổ hợp — Tổ hợp có lặp

Chọn $$k$$ phần tử từ $$n$$ loại (không phân biệt thứ tự, có lặp):

$$\frac{1}{(1-x)^{n}}$$

Hệ số của $$x^{k}$$: $$\binom{n+k-1}{k}$$ (stars and bars).

**Liên hệ**: Cùng kết quả với công thức tổ hợp lặp ở Chương 7.

---

## Đếm — Bài toán phân hoạch (Partition)

Đếm số cách viết $$n$$ thành tổng các số nguyên dương:

$$\prod_{k \ge 1} \frac{1}{1 - x^{k}}$$

**Ý tưởng Euler**: Mỗi số $$k$$ chọn 0, 1, 2, … lần → thừa số $$\frac{1}{1-x^{k}}$$.

Ví dụ $$n = 4$$: $$4, 3+1, 2+2, 2+1+1, 1+1+1+1$$ → 5 cách.

---

## Hàm sinh xác suất (PGF) — Giới thiệu

Biến ngẫu nhiên rời rạc $$X \ge 0$$:

$$G_X(s) = \sum_{k \ge 0} P(X = k) s^{k}$$

**Tính chất**: $$G_X(1) = 1$$; kỳ vọng $$E[X] = G'_X(1)$$.

**Ứng dụng**: Hàng đợi, phân tích thuật toán ngẫu nhiên.

---

## Ứng dụng trong CNTT

- **Phân tích đệ quy**: Chuyển HTTH → GF → công thức đóng
- **Sinh test case**: Đếm cấu hình đầu vào hợp lệ
- **Coding theory**: Weight enumerator đếm codeword theo trọng số Hamming
- **Symbolic methods**: Analytic combinatorics trong compiler / parser

---

## Thực hành 1

Dùng hàm sinh giải:

$$a_n = 3a_{n-1}$$, $$a_0 = 2$$

Kiểm tra bằng tính trực tiếp $$a_n = 2 \cdot 3^{n}$$.

---

## Thực hành 2

Giải bằng hàm sinh:

$$a_n = a_{n-1} + a_{n-2}$$, $$a_0 = 1$$, $$a_1 = 1$$

So sánh với dãy Fibonacci (dịch chỉ số).

---

## Tóm tắt Tiết 29

- **4 bước**: đặt $$G(x)$$ → nhân-cộng → giải → khai triển
- **Fibonacci**: $$G(x) = \frac{x}{1-x-x^{2}}$$
- **Phân thức từng phần** đọc hệ số $$a_n$$
- **Đếm**: nhân GF = convolution; phân hoạch = tích $$\prod \frac{1}{1-x^{k}}$$

---

## Liên hệ

**Chứng minh ý tưởng**: Nhân $$x^{n}$$ và cộng biến truy hồi thành phương trình trên $$G(x)$$.

**Edge case**: Điều kiện đầu quyết định hằng số trong nghiệm tường minh.

**Liên hệ**: HTTH (ch10) ↔ Hàm sinh (ch11) ↔ Đại số Boole / SAT (ch13).

---

## Bài tập ôn tập (1/2)

1. **Cơ bản**: Nêu 4 bước giải truy hồi bằng hàm sinh.

2. **Tính toán**: Tìm $$G(x)$$ cho $$a_n = 4a_{n-1} - 4a_{n-2}$$, $$a_0=1$$, $$a_1=4$$.

3. **Fibonacci**: Từ $$G(x) = \frac{x}{1-x-x^{2}}$$, giải thích vì sao hệ số là $$F_n$$.

---

## Bài tập ôn tập (2/2)

4. **Đếm**: Viết GF cho số cách đổi $$n$$ bằng xu 1₫ và 3₫.

5. **Bài 5**: Giải $$a_n = a_{n-1} + 2^{n}$$, $$a_0 = 0$$ bằng hàm sinh.
