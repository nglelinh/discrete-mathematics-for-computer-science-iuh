---
theme: white
css: slides/center-content.css
slideNumber: true
transition: slide
timeForPresentation: 2700
enableTimeBar: true
---

## Thuật toán & Ký hiệu Big-O

**Toán Rời Rạc**

Tiết 38 (45 phút) — Giới thiệu thuật toán & tăng trưởng hàm

---

## Mục tiêu tiết học

- Định nghĩa thuật toán và các tính chất cơ bản
- Mô tả thuật toán bằng mã giả (pseudocode)
- Hiểu ý nghĩa Big-O, Big-Omega ($$\Omega$$), Big-Theta ($$\Theta$$)
- So sánh tốc độ tăng trưởng của các hàm
- Áp dụng quy tắc ước lượng vào code thực tế

---

## Thuật toán là gì?

**Thuật toán** (algorithm) là dãy **hữu hạn** các chỉ thị chính xác để giải một lớp bài toán.

- **Đầu vào** (input): từ tập xác định
- **Đầu ra** (output): kết quả đúng theo yêu cầu

**Nguồn gốc**: Từ tên nhà toán học Al-Khwarizmi (thế kỷ IX).

**Câu hỏi cốt lõi**: Không chỉ "chạy được" mà còn "chạy được khi $$n$$ lớn"?

---

## Tính chất của thuật toán tốt

1. **Tính xác định** (definiteness): Mỗi bước rõ ràng, không mơ hồ
2. **Tính đúng đắn** (correctness): Mọi đầu vào hợp lệ → kết quả đúng
3. **Tính hữu hạn** (finiteness): Kết thúc sau hữu hạn bước
4. **Tính hiệu quả** (effectiveness): Mỗi bước thực thi được
5. **Tính tổng quát**: Giải cả lớp bài toán, không chỉ một ví dụ

---

## Mã giả — Tìm kiếm tuyến tính

```
THUẬT TOÁN: LinearSearch(A, n, x)
1. FOR i ← 1 TO n DO
2.     IF A[i] = x THEN RETURN i
3. RETURN 0   // không tìm thấy
```

```python
def linear_search(arr, x):
    for i, val in enumerate(arr):
        if val == x:
            return i
    return -1
```

**Trace**: $$A = [3, 7, 1, 9]$$, $$x = 7$$ → trả về vị trí 1 (hoặc 2 nếu đếm từ 1).

---

## Tại sao cần Big-O?

Hai thuật toán cùng đúng có thể khác nhau **rất lớn** khi $$n$$ tăng:

| $$n$$ | Bubble Sort $$O(n^{2})$$ | Merge Sort $$O(n \log n)$$ |
|:---:|:---:|:---:|
| 100 | ~5,000 | ~700 |
| 10⁶ | ~10¹² | ~2×10⁷ |

**Big-O** mô tả **giới hạn trên** của tăng trưởng — bỏ hằng số và số hạng bậc thấp.

---

## Định nghĩa Big-O

Cho $$f, g: \mathbb{N} \to \mathbb{R}^+$$. Ta nói:

$$f(n) = O(g(n))$$

nếu tồn tại $$C > 0$$ và $$n_0$$ sao cho:

$$f(n) \leq C \cdot g(n) \quad \forall n \geq n_0$$

**Ý nghĩa**: $$f$$ tăng **không nhanh hơn** $$g$$ (nhân hằng số), khi $$n$$ đủ lớn.

**Ví dụ**: $$3n^{2} + 5n + 7 = O(n^{2})$$ vì $$3n^{2} + 5n + 7 \leq 15n^{2}$$ khi $$n \geq 1$$.

---

## Quy tắc ước lượng thực tế

1. **Hằng số**: $$O(c \cdot f(n)) = O(f(n))$$ — bỏ hệ số nhân
2. **Tổng**: $$O(f(n) + g(n)) = O(\max(f(n), g(n)))$$ — lấy số hạng trội
3. **Tích**: $$O(f \cdot g) = O(f) \cdot O(g)$$

**Ví dụ**: $$2n^{3} + 100n^{2} + 50 = O(n^{3})$$

**Lưu ý**: Big-O mô tả **worst-case** trừ khi nói rõ khác.

---

## Big-Omega ($$\Omega$$) — Cận dưới

$$f(n) = \Omega(g(n))$$

nếu $$\exists C > 0, n_0$$: $$f(n) \geq C \cdot g(n)$$ với mọi $$n \geq n_0$$.

**Ý nghĩa**: $$f$$ tăng **ít nhất** nhanh bằng $$g$$.

**Ví dụ**:
- $$n^{2} + n = \Omega(n^{2})$$
- $$n \log n = \Omega(n)$$

---

## Big-Theta ($$\Theta$$) — Cận chặt

$$f(n) = \Theta(g(n))$$

**iff** $$f(n) = O(g(n))$$ **và** $$f(n) = \Omega(g(n))$$.

**Ý nghĩa**: $$f$$ và $$g$$ tăng **cùng bậc**.

**Ví dụ**:
- $$5n^{2} + 3n = \Theta(n^{2})$$
- $$n^{2} + n = O(n^{3})$$ nhưng **không** $$\Theta(n^{3})$$

---

## So sánh tăng trưởng

Thứ tự (chậm → nhanh):

$$O(1) < O(\log n) < O(n) < O(n \log n) < O(n^{2}) < O(n^{3}) < O(2^{n}) < O(n!)$$

**Quy tắc vàng**: Khi $$n \to \infty$$, hàm mũ **luôn** thắng đa thức.

**Liên hệ tiết 37**: BFS/DFS trên đồ thị $$O(V + E)$$ — tuyến tính theo kích thước đồ thị.

---

## Bảng các bậc phổ biến

| Big-O | Tên | Ví dụ thuật toán |
|:---|:---|:---|
| $$O(1)$$ | Hằng | Truy xuất mảng, hash hit |
| $$O(\log n)$$ | Logarit | Tìm kiếm nhị phân |
| $$O(n)$$ | Tuyến tính | Duyệt mảng, BFS |
| $$O(n \log n)$$ | Linearithmic | Merge Sort |
| $$O(n^{2})$$ | Bình phương | Bubble Sort, lồng 2 vòng |
| $$O(2^{n})$$ | Mũ | Duyệt tập con |

---

## Ví dụ code — So sánh tìm kiếm

```python
# O(n) — tìm kiếm tuyến tính
def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

# O(log n) — tìm kiếm nhị phân (mảng đã sắp xếp)
def binary_search(a, x):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x: return mid
        elif a[mid] < x: lo = mid + 1
        else: hi = mid - 1
    return -1
```

Với $$n = 10^{6}$$: tuyến tính ~500K so sánh; nhị phân ~20 so sánh.

---

## Ứng dụng trong Khoa học Máy tính

- **Chọn thuật toán**: API backend cần $$O(n \log n)$$ thay vì $$O(n^{2})$$
- **Cấu trúc dữ liệu**: Hash map $$O(1)$$ vs cây nhị phân $$O(\log n)$$
- **Database**: Query planner ước lượng chi phí JOIN
- **Bảo mật**: Thuật toán mã hóa cần lũy thừa modulo $$O(\log e)$$

**Edge case**: $$n$$ nhỏ → hằng số quan trọng; Insertion Sort có thể nhanh hơn Merge Sort.

---

## Thực hành 1

Xác định Big-O của các hàm sau (chỉ nêu bậc trội):

1. $$f(n) = 7n^{3} + 2n^{2} + 100$$
2. $$f(n) = 3\log n + 50$$
3. $$f(n) = n^{2} + n \log n + 1$$

---

## Thực hành 2

Phân tích đoạn code:

```python
total = 0
for i in range(n):
    for j in range(i, n):
        total += 1
```

1. Đếm số lần lặp (gợi ý: $$\sum_{i=0}^{n-1}(n-i)$$)
2. Kết luận Big-O
3. Nếu vòng trong là `range(n)` thay vì `range(i, n)` thì Big-O là gì?

---

## Thực hành 3

Cho $$f(n) = 2n^{2} + 10n$$ và $$g(n) = n^{2}$$:

1. Chứng minh $$f(n) = O(g(n))$$ (tìm $$C, n_0$$)
2. $$f(n) = \Omega(g(n))$$?
3. Kết luận: $$f(n) = \Theta(g(n))$$?

---

## Tóm tắt Tiết 38

- **Thuật toán**: hữu hạn, xác định, đúng, hiệu quả
- **Big-O**: giới hạn trên — "không nhanh hơn"
- **$$\Omega$$**: giới hạn dưới — "ít nhất nhanh bằng"
- **$$\Theta$$**: cận chặt — cùng bậc tăng trưởng
- Bỏ hằng số, lấy số hạng trội khi ước lượng

---

## Liên hệ

**Định nghĩa chính**: Big-O là công cụ **so sánh** thuật toán, không phải đo thời gian tuyệt đối.

**Edge case**: $$O(n)$$ với hằng số lớn có thể chậm hơn $$O(n^{2})$$ khi $$n$$ rất nhỏ.

**Liên hệ**: Đồ thị BFS/DFS (tiết 37) ↔ Big-O (tiết 38) ↔ Phân tích chi tiết (tiết 39).

---

## Bài tập ôn tập (1/2)

1. **Cơ bản**: Sắp xếp 5 hàm theo tăng trưởng: $$n^{2}$$, $$2^{n}$$, $$\log n$$, $$n \log n$$, $$n$$.

2. **Big-O**: Tìm Big-O của $$f(n) = 4n^{4} + n^{2} \log n + 1000$$.

3. **Code**: Vòng lặp `for i in range(n): for j in range(n):` có Big-O gì? Giải thích.

---

## Bài tập ôn tập (2/2)

4. **$$\Theta$$**: $$f(n) = n \log n$$ có phải $$\Theta(n^{2})$$ không? Giải thích ngắn.

5. **Bài 5**: Hai thuật toán A: $$O(n^{2})$$, B: $$O(n \log n)$$. Với $$n = 1000$$, A mất 1ms. Ước lượng thời gian B? Với $$n = 10^{6}$$ thì sao?
