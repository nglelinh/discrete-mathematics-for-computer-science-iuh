---
layout: post
title: "Lớp Độ phức tạp trong Kỹ thuật Phần mềm"
categories: chapter20
date: 2021-01-01
order: 2
required: false
lang: en
---

Mỗi lần bạn chọn giữa thuật toán $$O(n \log n)$$ và vòng lặp lồng $$O(n^2)$$, hay khi product manager hỏi "tại sao không brute-force mọi tổ hợp?" — bạn đang áp dụng **lý thuyết độ phức tạp** vào quyết định kỹ thuật.

```python
def two_sum_bruteforce(nums: list[int], target: int) -> tuple[int, int] | None:
    """O(n^2) — đủ cho n ≈ 10^3, chết với n ≈ 10^6"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
    return None

def two_sum_hash(nums: list[int], target: int) -> tuple[int, int] | None:
    """O(n) — đổi thời gian lấy bộ nhớ"""
    seen: dict[int, int] = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return seen[need], i
        seen[x] = i
    return None
```

Hai hàm cùng đúng, nhưng **scale** khác nhau. Chương 20 đặt câu hỏi hình thức: lớp **P**, **NP**, **NP-complete** — và bài này dịch chúng thành quy tắc thiết kế hệ thống, chọn thuật toán, và biết khi nào phải xấp xỉ (approximation) thay vì tìm tối ưu chính xác.

## Mục tiêu học tập

Sau bài học này, sinh viên có thể:

- **Ước lượng** độ phức tạp thời gian/không gian của đoạn code và chọn cấu trúc dữ liệu phù hợp.
- **Giải thích** ý nghĩa thực dụng của P, NP, NP-hard, NP-complete cho kỹ sư phần mềm.
- **Nhận diện** bài toán tối ưu tổ hợp trong product (routing, scheduling, packing) và hạn chế brute-force.
- **Áp dụng** chiến lược: heuristic, approximation, caching, parallelization khi bài toán NP-hard.
- **Đọc** benchmark và profiling để xác nhận Big-O trên dữ liệu thực.

**Từ khóa**: độ phức tạp thời gian (time complexity), Big-O, lớp P, lớp NP, NP-complete, NP-hard, heuristic, xấp xỉ (approximation).

---

## Phần 1: Big-O trong code thực tế

### 1.1. Đếm vòng lặp và đệ quy

| Mẫu code | Độ phức tạp | Ghi chú |
|---|---|---|
| Một vòng `for` trên `n` | $$O(n)$$ | Linear scan |
| Hai vòng lồng trên `n` | $$O(n^2)$$ | Pairwise comparison |
| `sort()` rồi duyệt | $$O(n \log n)$$ | TimSort Python |
| Đệ quy chia đôi (merge sort) | $$O(n \log n)$$ | Master theorem |
| DFS trên đồ thị $$V,E$$ | $$O(V+E)$$ | Adjacency list |

```python
# O(n) — set membership
def has_duplicate(nums: list[int]) -> bool:
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False

# O(n^2) — so sánh mọi cặp
def has_duplicate_slow(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
```

![Big-O notation — so sánh tốc độ tăng trưởng](https://commons.wikimedia.org/wiki/Special:FilePath/Big_O_notation.svg?width=640)

*Hình 20.6: Big-O — $$O(n)$$, $$O(n \log n)$$, $$O(n^2)$$ tách nhau rõ khi $$n$$ lớn; chọn sai hàm là lỗi kiến trúc, không chỉ micro-optimization.*

### 1.2. Ẩn hằng số vẫn quan trọng ở scale vừa

Big-O bỏ hằng số, nhưng $$10^6$$ lần $$O(n)$$ với $$n=10^4$$ vẫn chạy được; $$O(2^n)$$ với $$n=40$$ đã là tỷ tỷ phép. **Luôn ước lượng $$n$$** trong production.

<div class="content-box insight-box" markdown="1">
**Nhận xét**: Profile trước khi tối ưu — nhưng nếu thuật toán là $$O(n^2)$$ và $$n$$ tăng gấp 10 mỗi năm, profile chỉ xác nhận bạn cần đổi thuật toán, không chỉ đổi CPU.
</div>

---

## Phần 2: P và NP — bản dịch cho kỹ sư

### 2.1. P: giải nhanh (đa thức)

**P** = bài toán có thuật toán thời gian đa thức theo kích thước input.

Ví dụ thực dụng trong P:

- shortest path (Dijkstra với heap)
- sorting, searching có cấu trúc
- matching bipartite (Hopcroft–Karp)
- linear programming (interior point, đa thức trong thực hành)

### 2.2. NP: kiểm tra lời giải nhanh

**NP** = given **certificate** (lời giải đề xuất), verify trong thời gian đa thức.

- **SAT**: gán true/false cho biến — kiểm tra mỗi clause $$O(1)$$, tổng đa thức.
- **Hamilton cycle**: danh sách đỉnh — kiểm tra đúng cycle trong đa thức.
- **Subset sum**: tập con — cộng và so sánh target.

Tìm lời giải từ đầu có thể khó; **kiểm tra** thường dễ hơn — đó là asymmetry cốt lõi.

![Stephen Cook — định nghĩa NP-complete (định lý Cook–Levin)](https://commons.wikimedia.org/wiki/Special:FilePath/Stephen_Cook.jpg?width=640)

*Hình 20.7: Stephen Cook — SAT là NP-complete đầu tiên; mọi bài NP có thể rút gọn về SAT (trong lý thuyết); trong thực tế, SAT solver vẫn xử lý được nhiều instance engineering.*

### 2.3. NP-complete và NP-hard

- **NP-complete**: thuộc NP, và mọi bài NP **rút gọn đa thức** về nó.
- **NP-hard**: ít nhất hard như NP-complete, có thể không thuộc NP (ví dụ halting).

**Quy tắc product**: nếu bài toán của bạn là biến thể Traveling Salesman, Bin Packing, Job Scheduling với ràng buộc tổ hợp — giả định **không** có thuật toán đa thức tối ưu toàn cục (trừ khi P = NP).

![Richard Karp — 21 bài NP-complete kinh điển](https://commons.wikimedia.org/wiki/Special:FilePath/Richard_Karp.jpg?width=640)

*Hình 20.8: Richard Karp — danh sách 21 bài NP-complete; nhiều tên xuất hiện trong logistics, lập lịch, và tối ưu hóa sản phẩm.*

---

## Phần 3: Khi brute-force thất bại

### 3.1. Số lượng tổ hợp

$$C(n,2) = \frac{n(n-1)}{2} \approx O(n^2)$$ — chấp nhận được với $$n \approx 10^4$$.

$$2^n$$ — $$n=30$$ ≈ một tỷ; $$n=50$$ vượt khả năng brute-force trên một máy.

```python
import itertools

def tsp_bruteforce(dist: list[list[int]]) -> list[int]:
    n = len(dist)
    best_cost = float("inf")
    best_path = []
    for perm in itertools.permutations(range(1, n)):
        path = [0] + list(perm) + [0]
        cost = sum(dist[path[i]][path[i+1]] for i in range(n))
        if cost < best_cost:
            best_cost, best_path = cost, path
    return best_path, best_cost
```

Chỉ dùng khi $$n \le 10$$ trong demo — production dùng heuristic (Christofides, 2-opt) hoặc ILP solver với time limit.

### 3.2. Chiến lược kỹ thuật khi NP-hard

| Chiến lược | Ví dụ |
|---|---|
| Heuristic / greedy | Nearest neighbor TSP |
| Approximation algorithm | Đảm bảo tỷ lệ so với optimal |
| Fixed-parameter | $$n$$ nhỏ, $$k$$ tham số cố định |
| SAT/ILP solver + timeout | Planning, scheduling |
| Cache + incremental | Recompute khi input thay ít |
| Chuyển bài toán | Relax constraint, solve, repair |

<div class="content-box warning-box" markdown="1">
**Cẩn thận**: "Chạy được trên test" ≠ "scale được". Demo $$n=8$$ che giấu $$O(n!)$$. Luôn document giới hạn input và fallback khi vượt ngưỡng.
</div>

---

## Phần 4: Engineering workflow

### 4.1. Checklist trước khi ship thuật toán

1. **Input size** $$n$$ worst-case là bao nhiêu?
2. **Time** và **space** Big-O?
3. Có **structure** khai thác được không (sorted, sparse, DAG)?
4. Bài toán có **NP-hard** known reduction không?
5. Cần **optimal** hay **good enough** trong SLA?

### 4.2. Profiling xác nhận

```python
import time

def bench(fn, *args, repeat=3):
    t0 = time.perf_counter()
    for _ in range(repeat):
        fn(*args)
    return (time.perf_counter() - t0) / repeat
```

Đo với $$n$$ tăng gấp đôi: thời gian ×4 gợi ý $$O(n^2)$$; ×2 gợi ý $$O(n)$$ hoặc $$O(n \log n)$$.

## Công cụ tương tác

<div data-demo="big-o-growth-comparator"></div>

---

## Bài tập thực hành

### Bài tập 1: Phân tích Big-O

Cho `nested` duyệt ma trận `n x n` và in phần tử. Độ phức tạp?

<details>
<summary>Đáp án</summary>

$$O(n^2)$$ — hai vòng chỉ số hàng và cột.

</details>

### Bài tập 2: Chọn thuật toán

Tìm cặp chỉ số `two sum` với `nums` dài $$10^6$$. Chọn brute-force hay hash? Ước lượng thời gian thứ tự.

<details>
<summary>Đáp án</summary>

Hash $$O(n)$$ — một pass, ~$$10^6$$ bước. Brute-force $$O(n^2)$$ ~$$10^{12}$$ — không chấp nhận được.

</details>

### Bài tập 3: P hay NP?

Phân loại: (a) kiểm tra chuỗi có phải palindrome; (b) tìm tour TSP tối thiểu; (c) kiểm tra tour cho trước có hợp lệ TSP.

<details>
<summary>Đáp án</summary>

(a) P — duyệt hai đầu $$O(n)$$. (c) NP — verify tour $$O(n)$$. (b) NP-hard optimization — tìm optimal không có thuật toán đa thức nếu P ≠ NP.

</details>

### Bài tập 4: $$2^n$$ scale

Brute-force subset với $$n=25$$. Số subset? Có thực tế trên laptop hiện đại không?

<details>
<summary>Đáp án</summary>

$$2^{25} = 33{,}554{,}432$$ — có thể vài giây nếu mỗi subset xử lý nhanh; $$n=40$$ → $$2^{40} \approx 10^{12}$$ — không thực tế.

</details>

### Bài tập 5: Viết hash two-sum

Hoàn thiện `two_sum_hash` trả về **chỉ số** đầu tiên tìm được, hoặc `None`.

<details>
<summary>Đáp án</summary>

Xem Phần mở đầu — lưu `seen[value] = index`, khi gặp `need in seen` trả `(seen[need], i)`.

</details>

### Bài tập 6: Reduction trực giác

Giải thích vì sao "tìm clique kích thước $$k$$" trên đồ thị khó khiến "tìm đoàn bạn tối đa trong mạng xã hội" (mọi người quen nhau) cũng khó.

<details>
<summary>Đáp án</summary>

Clique là bài NP-complete cổ điển. Mô hình mạng xã hội là đồ thị; tìm clique lớn nhất là biến thể optimization NP-hard — cần heuristic (greedy, community detection) thay vì exact cho graph lớn.

</details>

### Bài tập 7: Approximation

TSP trên 100 thành phố: tại sao dùng 2-opt local search thay vì exact?

<details>
<summary>Đáp án</summary>

Exact TSP NP-hard; $$100!$$ không khả thi. 2-opt cải thiện dần tour trong thời gian đa thức thực tế, đủ tốt cho logistics với SLA vài giây.

</details>

### Bài tập 8: Product decision

PM yêu cầu "tối ưu lịch giao hàng cho 500 đơn, 50 xe, ràng buộc cửa sổ thời gian" — optimal mọi instance. Phản biện kỹ thuật ngắn gọn.

<details>
<summary>Đáp án</summary>

Bài vehicle routing với time window là NP-hard. Với 500 đơn, exact solver có thể timeout; đề xuất: ILP/OR-Tools với time limit, heuristic initial solution, metric "within 5% of lower bound", và fallback manual override — document trade-off optimal vs SLA.

</details>

## Tóm tắt

- **Big-O** + ước lượng $$n$$ quyết định thuật toán có ship được không.
- **P**: giải đa thức; **NP**: kiểm tra certificate đa thức — asymmetry quan trọng trong crypto và verification.
- **NP-complete/NP-hard**: đừng hứa optimal đa thức cho mọi instance trừ khi có cấu trúc đặc biệt.
- **Engineering**: heuristic, approximation, solver + timeout, profiling — công cụ khi lý thuyết nói "khó".
- **P = NP?** Vẫn mở — nhưng thiết kế hệ thống an toàn giả định **không** có phép màu đa thức cho mọi bài tối ưu tổ hợp.

Chúng ta đã hoàn thành hành trình từ logic mệnh đề đến độ phức tạp — mỗi chương gắn với một lát cắt thực tế trong kỹ thuật phần mềm hiện đại.