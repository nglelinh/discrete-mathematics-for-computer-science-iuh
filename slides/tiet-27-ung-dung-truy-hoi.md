---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Ứng dụng Hệ thức Truy hồi trong Thuật toán

**Toán Rời Rạc**

Tiết 27 (45 phút) — ch10 `10_04`

---

## Mục tiêu tiết học

- Phân tích **Tháp Hà Nội** và chứng minh $$H_n = 2^{n} - 1$$
- Thiết lập và giải **Merge Sort**: $$T(n) = 2T(n/2) + n$$ → $$\Theta(n \log n)$$
- So sánh Fibonacci **đệ quy** vs **memoization**
- Nắm ý tưởng **Master Theorem** cho divide-and-conquer

---

## Truy hồi = Ngôn ngữ thuật toán đệ quy

Thuật toán đệ quy mô tả bài toán lớn qua bài toán con → **HTTH** cho chi phí $$T(n)$$.

**Ba thành phần**:
1. **Bước chia**: số lời gọi con, kích thước con
2. **Bước kết hợp**: công việc ngoài đệ quy ($$f(n)$$)
3. **Điều kiện dừng**: $$T(1)$$ hoặc $$T(0)$$

---

## Tháp Hà Nội

$$H_n = 2H_{n-1} + 1, \quad H_1 = 1$$

**Độ phức tạp**: $$H_n = 2^{n} - 1 = \Theta(2^{n})$$ — **exponential**.

**Chứng minh quy nạp** $$H_n = 2^{n} - 1$$:

- **Cơ sở**: $$H_1 = 1 = 2^{1} - 1$$ ✓
- **Giả thiết**: $$H_{n-1} = 2^{n-1} - 1$$
- **Bước**: $$H_n = 2(2^{n-1}-1) + 1 = 2^{n} - 2 + 1 = 2^{n} - 1$$ ✓

**Thực tế**: $$H_{64} \approx 1.8 \times 10^{19}$$ bước — ~585 tỷ năm nếu 1 bước/giây.

---

## Merge Sort: Thiết lập HTTH

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # T(n/2)
    right = merge_sort(arr[mid:])  # T(n/2)
    return merge(left, right)      # Θ(n)
```

$$T(n) = 2T(n/2) + n, \quad T(1) = 1$$

- **2**: hai lời gọi con nửa kích thước
- **+n**: merge hai mảng nửa

---

## Merge Sort: Cây đệ quy

```
              n
           /     \
        n/2      n/2
       /  \      /  \
     ...  ...  ...  ...
```

**Mỗi tầng**: tổng công việc merge = $$n$$ (chia đều).

**Số tầng**: $$\log_2 n$$ (chia đôi đến 1).

$$T(n) = n \cdot \log_2 n = \Theta(n \log n)$$

---

## Master Theorem (ý tưởng)

Dạng chuẩn:

$$T(n) = a\, T(n/b) + f(n)$$

- $$a$$: số lời gọi con
- $$b$$: hệ số chia kích thước
- $$f(n)$$: chi phí ngoài đệ quy

**Merge sort**: $$a=2, b=2, f(n)=n$$.

So sánh $$f(n)$$ với $$n^{\log_b a} = n^{1} = n$$ → **Case 2** → $$T(n) = \Theta(n \log n)$$.

*(Chi tiết đầy đủ ở tiết 38–39)*

---

## Binary Search

$$T(n) = T(n/2) + 1, \quad T(1) = 1$$

- Một lời gọi con nửa kích thước
- $$+1$$: so sánh giữa

$$n^{\log_2 1} = n^{0} = 1$$, $$f(n)=1$$ → $$T(n) = \Theta(\log n)$$.

---

## Fibonacci đệ quy ngây thơ

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

$$T(n) = T(n-1) + T(n-2) + 1 \approx F_n$$

**Độ phức tạp**: $$\Theta(\varphi^{n})$$ — **exponential** (rất chậm).

**Số lần gọi** $$fib(5)$$: cây đệ quy trùng lặp khổng lồ.

---

## Memoization (Dynamic Programming)

```python
memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
```

**Cùng HTTH** $$F_n = F_{n-1} + F_{n-2}$$, nhưng tính **một lần** mỗi $$F_k$$.

**Thời gian**: $$\Theta(n)$$, **không gian**: $$\Theta(n)$$.

**Bài học**: truy hồi + trí nhớ biến exponential → linear.

---

## So sánh độ phức tạp

| Thuật toán / Bài toán | HTTH | Kết quả |
|----------------------|------|---------|
| Tháp Hà Nội | $$H_n = 2H_{n-1}+1$$ | $$\Theta(2^{n})$$ |
| Fibonacci ngây thơ | $$T(n)=T(n-1)+T(n-2)$$ | $$\Theta(\varphi^{n})$$ |
| Fibonacci memo | bảng DP | $$\Theta(n)$$ |
| Binary search | $$T(n)=T(n/2)+1$$ | $$\Theta(\log n)$$ |
| Merge sort | $$T(n)=2T(n/2)+n$$ | $$\Theta(n \log n)$$ |

---

## Chứng minh Merge Sort bằng quy nạp (sketch)

**Giả thiết**: $$T(k) \leq ck \log k$$ với $$k < n$$.

$$T(n) = 2T(n/2) + n \leq 2 \cdot c\frac{n}{2}\log\frac{n}{2} + n = cn\log n - cn + n$$

Chọn $$c \geq 1$$ → $$T(n) \leq cn \log n$$.

**Kết luận**: $$T(n) = O(n \log n)$$; với merge $$\Theta(n)$$ → $$\Theta(n \log n)$$.

---

## Thực hành 1

Chứng minh bằng quy nạp: $$H_n = 2^{n} - 1$$ cho mọi $$n \geq 1$$.

Viết đủ 3 bước: cơ sở, giả thiết, bước quy nạp.

---

## Thực hành 2

Thiết lập HTTH cho QuickSort **trường hợp xấu** (pivot luôn min/max):

$$T(n) = T(n-1) + n$$

Giải thích vì sao là $$\Theta(n^{2})$$.

---

## Thực hành 3

Đếm số nút trong cây đệ quy Merge Sort với $$n=8$$. Xác nhận $$n \log n$$ thao tác merge tổng.

---

## Tóm tắt Tiết 27

- **Hanoi**: $$H_n = 2^{n} - 1$$, exponential
- **Merge sort**: $$T(n) = 2T(n/2) + n$$ → $$\Theta(n \log n)$$
- **Master Theorem**: so $$f(n)$$ với $$n^{\log_b a}$$
- **Fibonacci**: đệ quy ngây thơ exponential; memo $$\Theta(n)$$
- **Quy nạp**: chứng minh công thức đóng từ HTTH

---

## Liên hệ

**Liên hệ**:
- Truy hồi ↔ Big-O (tiết 38–39)
- Truy hồi ↔ DP (LCS, knapsack)
- Truy hồi ↔ Hàm sinh (tiết 28–29) — giải bằng GF

**Ứng dụng**: FFT $$T(n) = 2T(n/2) + O(n)$$; Strassen nhân ma trận.

---

## Bài tập ôn tập (1/2)

1. Chứng minh $$H_n > 2^{n-1}$$ với $$n \geq 2$$.

2. Merge sort trên mảng 16 phần tử: tối đa bao nhiêu **tầng** đệ quy?

3. So sánh số lần gọi `fib(10)` ngây thơ vs memo.

---

## Bài tập ôn tập (2/2)

4. Thiết lập HTTH cho số cách đổi tiền (tổng $$n$$, mệnh giá 1 và 2).

5. **Bài 5** $$T(n) = 3T(n/2) + n$$. Dùng Master Theorem: $$n^{\log_2 3} \approx n^{1.58}$$ → $$T(n) = ?$$
