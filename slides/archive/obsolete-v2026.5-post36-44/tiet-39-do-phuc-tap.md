---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Độ phức tạp Thuật toán

**Toán Rời Rạc**

Tiết 39 (45 phút) — Phân tích thời gian & không gian

---

## Mục tiêu tiết học

- Phân biệt độ phức tạp thời gian và không gian
- Phân tích vòng lặp đơn, lồng nhau và có điều kiện
- Phân tích đệ quy — Fibonacci, Merge Sort
- Hiểu worst-case, average-case, best-case
- Nhận biết bài toán P và NP (giới thiệu)

---

## Hai chiều phân tích

| | Thời gian (Time) | Không gian (Space) |
|:---|:---|:---|
| **Đo gì** | Số phép toán cơ bản | Bộ nhớ phụ (ngoài input) |
| **Đơn vị** | So sánh, gán, cộng... | Byte, ô nhớ, độ sâu stack |
| **Ví dụ** | Merge Sort $$O(n \log n)$$ | Merge Sort $$O(n)$$ mảng phụ |

**Câu hỏi kép**: Thuật toán này mất bao lâu? Cần bao nhiêu RAM?

---

## Ba trường hợp phân tích

- **Best-case**: Đầu vào "thuận lợi" nhất → chi phí tối thiểu
- **Average-case**: Trung bình trên phân phối đầu vào
- **Worst-case**: Đầu vào "xấu" nhất → chi phí tối đa

**Thông lệ**: Dùng **worst-case** khi nói Big-O (trừ khi ghi chú khác).

**Ví dụ**: Tìm kiếm tuyến tính — best $$O(1)$$, worst & average $$O(n)$$.

---

## Phân tích vòng lặp đơn

```python
# O(n)
for i in range(n):
    print(A[i])

# O(log n) — i nhân đôi mỗi lần
i = 1
while i < n:
    i *= 2
```

**Quy tắc**: Mỗi vòng lặp nhân hệ số vào tổng chi phí.

**Vòng lặp giảm một nửa**: $$n \to n/2 \to n/4 \to \cdots$$ → $$\log_2 n$$ lần.

---

## Vòng lặp lồng nhau

```python
# O(n²)
for i in range(n):
    for j in range(n):
        total += A[i] * A[j]

# O(n³)
for i in range(n):
    for j in range(n):
        for k in range(n):
            work()
```

**Công thức**: $$k$$ vòng lặp lồng, mỗi vòng $$n$$ lần → $$O(n^{k})$$.

**Biến thể**: Vòng trong `range(i, n)` → vẫn $$O(n^{2})$$ (tam giác: $$n(n+1)/2$$).

---

## Vòng lặp có điều kiện & chia để trị

```python
# O(n log n) — Merge Sort style
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # T(n/2)
    right = merge_sort(arr[mid:])   # T(n/2)
    return merge(left, right)       # O(n)
```

**Phương trình truy hồi**: $$T(n) = 2T(n/2) + O(n) \Rightarrow T(n) = O(n \log n)$$

---

## Phân tích đệ quy — Phương pháp

**Bước 1**: Viết phương trình truy hồi $$T(n)$$

**Bước 2**: Xác định trường hợp cơ sở (base case)

**Bước 3**: Giải (thay thế, Master Theorem, hoặc cây đệ quy)

**Ví dụ đơn giản**:
```
T(n) = T(n-1) + O(1), T(1) = O(1)
→ T(n) = O(n)
```

---

## Fibonacci — So sánh hai cách

**Đệ quy ngây thơ**:
```
FIB(n):
  IF n ≤ 1 RETURN n
  RETURN FIB(n-1) + FIB(n-2)
```
→ $$T(n) = T(n-1) + T(n-2) + O(1) \approx O(\phi^{n})$$ với $$\phi \approx 1.618$$ → **$$O(2^{n})$$**

**Quy hoạch động (memoization)**:
```python
def fib_dp(n, memo={}):
    if n <= 1: return n
    if n not in memo:
        memo[n] = fib_dp(n-1) + fib_dp(n-2)
    return memo[n]
```
→ **$$O(n)$$** thời gian, **$$O(n)$$** không gian.

---

## So sánh thuật toán sắp xếp

| Thuật toán | Worst | Average | Space | Ổn định |
|:---|:---:|:---:|:---:|:---:|
| Bubble Sort | $$O(n^{2})$$ | $$O(n^{2})$$ | $$O(1)$$ | Có |
| Insertion Sort | $$O(n^{2})$$ | $$O(n^{2})$$ | $$O(1)$$ | Có |
| Merge Sort | $$O(n \log n)$$ | $$O(n \log n)$$ | $$O(n)$$ | Có |
| Quick Sort | $$O(n^{2})$$ | $$O(n \log n)$$ | $$O(\log n)$$ | Không |

**Thực tế**: Quick Sort thường nhanh hơn Merge Sort do hằng số nhỏ — nhưng worst-case tệ.

---

## Độ phức tạp không gian

| Thuật toán | Không gian phụ |
|:---|:---:|
| Tìm kiếm tuyến tính | $$O(1)$$ |
| Tìm kiếm nhị phân (đệ quy) | $$O(\log n)$$ stack |
| Merge Sort | $$O(n)$$ mảng phụ |
| DFS (đồ thị) | $$O(V)$$ visited/stack |
| BFS (đồ thị) | $$O(V)$$ queue |

**Đánh đổi**: Nhanh hơn ($$O(n \log n)$$) thường tốn thêm bộ nhớ ($$O(n)$$).

---

## Trade-off Thời gian ↔ Không gian

**Ví dụ**: Fibonacci
- Đệ quy: $$O(2^{n})$$ thời gian, $$O(n)$$ stack
- DP mảng: $$O(n)$$ thời gian, $$O(n)$$ bộ nhớ
- DP tối ưu: $$O(n)$$ thời gian, **$$O(1)$$** bộ nhớ (chỉ giữ 2 giá trị)

```python
def fib_o1_space(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

---

## Giới thiệu P và NP

- **Lớp P**: Bài toán giải được trong thời gian **đa thức** $$O(n^{k})$$
  - Sắp xếp, tìm kiếm, BFS, GCD
- **Lớp NP**: Lời giải **kiểm tra** được trong thời gian đa thức
  - SAT, TSP, tô màu đồ thị, Hamilton
- **$$P \stackrel{?}{=} NP$$**: Một trong bảy bài toán Thiên niên kỷ (giải thưởng $1M)

**Lưu ý**: NP ≠ "không giải được" — chỉ chưa biết thuật toán đa thức.

---

## Ứng dụng thực tế

- **API thiết kế**: $$O(n^{2})$$ trên 10⁶ request → treo server
- **Embedded**: Giới hạn RAM → ưu tiên $$O(1)$$ space
- **Big Data**: Chỉ $$O(n)$$ hoặc $$O(n \log n)$$ khả thi với terabyte
- **CSDL**: Optimizer chọn plan JOIN dựa trên ước lượng chi phí

**Trực quan**: $$O(n^{2})$$ với $$n = 10^{6}$$ ≈ 11.5 ngày (1 ns/op); $$O(n)$$ ≈ 1 ms.

---

## Thực hành 1

Phân tích Big-O:

```python
def mystery(n):
    i = n
    while i > 1:
        i = i // 2
    return i
```

1. Mỗi vòng lặp $$i$$ giảm bao nhiêu?
2. Có bao nhiêu lần lặp?
3. Kết luận time complexity.

---

## Thực hành 2

```python
def sum_matrix(M, n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += M[i][j]
    return total
```

1. Time complexity?
2. Space complexity (không tính ma trận input)?
3. Nếu thêm mảng phụ `temp[n][n]` để lưu kết quả trung gian thì space?

---

## Thực hành 3

So sánh hai hàm đếm số nguyên tố $$\leq n$$:

- **A**: Kiểm tra từng số bằng chia thử → $$O(n\sqrt{n})$$
- **B**: Sàng Eratosthenes → $$O(n \log \log n)$$

Với $$n = 10^{6}$$, giải thích vì sao chọn B trong thực tế.

---

## Tóm tắt Tiết 39

- **Time**: đếm phép toán cơ bản theo $$n$$
- **Space**: bộ nhớ phụ (stack, mảng tạm, queue...)
- **Vòng lặp**: nhân hệ số; giảm một nửa → $$\log n$$
- **Đệ quy**: viết $$T(n)$$, tránh lặp tính toán (DP)
- **P / NP**: giải nhanh vs kiểm tra nhanh

---

## Liên hệ

**Kỹ năng chính**: Đếm số hạng trội trong phương trình truy hồi.

**Edge case**: Quick Sort worst $$O(n^{2})$$ khi pivot luôn min/max; dùng random pivot.

**Liên hệ**: Big-O (tiết 38) → Phân tích chi tiết (tiết 39) → SAT/NP (tiết 43).

---

## Bài tập ôn tập (1/2)

1. **Vòng lặp**: `for i in range(n): for j in range(i):` — Big-O?

2. **Đệ quy**: `T(n) = T(n/2) + O(1)` — giải và kết luận.

3. **Space**: DFS trên đồ thị $$V$$ đỉnh, $$E$$ cạnh — time và space?

---

## Bài tập ôn tập (2/2)

4. **So sánh**: Selection Sort vs Merge Sort — time, space, khi nào dùng cái nào?

5. **Bài 5**: Thuật toán A: $$O(n^{3})$$ time, $$O(n^{2})$$ space. B: $$O(n^{4})$$ time, $$O(n)$$ space. Chọn khi $$n=100$$? Khi $$n=10^{6}$$? Giải thích.
