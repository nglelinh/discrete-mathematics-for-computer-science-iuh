---
layout: post
title: "Lý thuyết Xác suất Cơ bản"
categories: chapter09
date: 2021-01-01
order: 1
required: true
lang: en
---

# Lý thuyết Xác suất Cơ bản

Trong kỹ thuật phần mềm, ta không phải lúc nào cũng dự đoán được kết quả chính xác của một sự kiện đơn lẻ. Gói tin có thể mất, người dùng có thể bấm nhầm, cảm biến có thể nhiễu, thuật toán ngẫu nhiên có thể cho kết quả khác nhau qua từng lần chạy. Khi đó, thay vì hỏi "điều gì chắc chắn xảy ra", ta hỏi "điều gì có khả năng xảy ra đến mức nào".


Xác suất giúp ta chuyển từ trực giác mơ hồ sang đánh giá định lượng, điều rất quan trọng khi phân tích thuật toán ngẫu nhiên, dữ liệu nhiễu và rủi ro hệ thống.
**Xác suất** là ngôn ngữ để làm việc với sự không chắc chắn đó. Nó là nền cho thống kê, machine learning, mô phỏng, đánh giá rủi ro và rất nhiều quyết định tự động trong hệ thống hiện đại.

Điều quan trọng là xác suất không thay thế tư duy logic, nó bổ sung cho logic. Ta vẫn cần mô hình đúng không gian khả năng xảy ra, biến cố và quan hệ giữa các biến cố trước khi tính toán bất kỳ con số nào.

Trong bài học này, chúng ta sẽ xây những khái niệm đầu tiên của lý thuyết xác suất để có nền vững cho các công cụ mạnh hơn ở các bài sau.

## Khái niệm Cơ bản

### Thí nghiệm và Không gian Mẫu

**Thí nghiệm ngẫu nhiên**: Một quá trình có kết quả không thể dự đoán trước.

**Không gian mẫu (Sample Space)** Ω: Tập hợp tất cả các kết quả có thể của thí nghiệm.

**Biến cố (Event)**: Tập con của không gian mẫu.

### Ví dụ

**Thí nghiệm**: Tung một đồng xu
- Không gian mẫu: Ω = {H, T} (Head, Tail)
- Biến cố A = "Ra mặt ngửa" = {H}

**Thí nghiệm**: Tung hai xúc xắc
- Không gian mẫu: Ω = {(i,j) | 1 ≤ i,j ≤ 6}, |Ω| = 36
- Biến cố B = "Tổng bằng 7" = {(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)}

## Định nghĩa Xác suất

### Định nghĩa Cổ điển (Laplace)

Với không gian mẫu hữu hạn và các kết quả đồng khả năng:

**P(A) = |A| / |Ω|**

### Tiên đề Kolmogorov

1. **Không âm**: P(A) ≥ 0 với mọi biến cố A
2. **Chuẩn hóa**: P(Ω) = 1
3. **Cộng tính**: Nếu A ∩ B = ∅ thì P(A ∪ B) = P(A) + P(B)

### Tính chất Cơ bản

- P(∅) = 0
- P(A^c) = 1 - P(A)
- 0 ≤ P(A) ≤ 1
- Nếu A ⊆ B thì P(A) ≤ P(B)

## Quy tắc Xác suất

### Quy tắc Cộng

**Cho hai biến cố A và B**:

P(A ∪ B) = P(A) + P(B) - P(A ∩ B)

**Trường hợp đặc biệt** (A và B xung khắc):
P(A ∪ B) = P(A) + P(B)

### Quy tắc Nhân

**Xác suất có điều kiện**: P(A|B) = P(A ∩ B) / P(B)

**Quy tắc nhân tổng quát**: P(A ∩ B) = P(A|B) × P(B)

**Trường hợp độc lập**: P(A ∩ B) = P(A) × P(B)

## Ví dụ Tính toán

### Ví dụ 1: Tung hai đồng xu
Tìm xác suất có ít nhất một mặt ngửa.

**Giải**:
- Ω = {HH, HT, TH, TT}, |Ω| = 4
- A = "ít nhất một H" = {HH, HT, TH}
- P(A) = 3/4 = 0.75

**Cách khác**: P(A) = 1 - P(A^c) = 1 - P(TT) = 1 - 1/4 = 3/4

### Ví dụ 2: Rút bài
Từ bộ 52 lá, rút 2 lá. Tìm xác suất cả hai đều là Ace.

**Giải**:
- Cách 1: P = C(4,2)/C(52,2) = 6/1326 = 1/221
- Cách 2: P = (4/52) × (3/51) = 12/2652 = 1/221

### Ví dụ 3: Bài toán sinh nhật
Trong 23 người, xác suất có ít nhất 2 người sinh cùng ngày là bao nhiêu?

**Giải**:
P(ít nhất 2 người cùng sinh nhật) = 1 - P(tất cả khác sinh nhật)

P(tất cả khác) = (365/365) × (364/365) × ... × (343/365) ≈ 0.493

P(ít nhất 2 cùng) ≈ 1 - 0.493 = 0.507 > 50%

## Ứng dụng trong Khoa học Máy tính

### 1. Thuật toán Randomized

```python
import random

def quicksort_randomized(arr):
    """QuickSort với pivot ngẫu nhiên"""
    if len(arr) <= 1:
        return arr
    
    # Chọn pivot ngẫu nhiên - giảm xác suất worst case
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort_randomized(left) + middle + quicksort_randomized(right)

def monte_carlo_pi(n):
    """Ước lượng π bằng phương pháp Monte Carlo"""
    inside_circle = 0
    
    for _ in range(n):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x*x + y*y <= 1:
            inside_circle += 1
    
    # P(điểm trong hình tròn) = π/4
    return 4 * inside_circle / n
```

### 2. Hash Functions và Bloom Filters

```python
class BloomFilter:
    def __init__(self, size, hash_functions):
        self.size = size
        self.bit_array = [0] * size
        self.hash_functions = hash_functions
    
    def add(self, item):
        for hash_func in self.hash_functions:
            index = hash_func(item) % self.size
            self.bit_array[index] = 1
    
    def contains(self, item):
        for hash_func in self.hash_functions:
            index = hash_func(item) % self.size
            if self.bit_array[index] == 0:
                return False  # Chắc chắn không có
        return True  # Có thể có (false positive possible)
    
    def false_positive_rate(self, n_items):
        """Tính xác suất false positive"""
        k = len(self.hash_functions)
        m = self.size
        n = n_items
        
        # P(false positive) ≈ (1 - e^(-kn/m))^k
        return (1 - math.exp(-k * n / m)) ** k
```

### 3. Load Testing và Performance Analysis

```python
def simulate_server_load(arrival_rate, service_rate, simulation_time):
    """Mô phỏng tải server bằng quy trình Poisson"""
    import numpy as np
    
    # Thời gian giữa các request (exponential distribution)
    inter_arrival_times = np.random.exponential(1/arrival_rate, 
                                               int(simulation_time * arrival_rate * 2))
    
    # Thời gian xử lý (exponential distribution)  
    service_times = np.random.exponential(1/service_rate, len(inter_arrival_times))
    
    # Tính toán thống kê
    arrival_times = np.cumsum(inter_arrival_times)
    queue_lengths = []
    response_times = []
    
    # Simulation logic...
    return {
        'average_queue_length': np.mean(queue_lengths),
        'average_response_time': np.mean(response_times),
        'server_utilization': arrival_rate / service_rate
    }
```

## Bài tập thực hành

### Bài tập 1: Cơ bản
1. Tung 3 đồng xu. Tính xác suất có đúng 2 mặt ngửa.
2. Từ bộ bài 52 lá, rút 1 lá. Tính P(Ace hoặc bài Cơ).
3. Hộp có 5 bi đỏ và 3 bi xanh. Rút 2 bi không hoàn lại. Tính P(cả hai đều đỏ).

### Bài tập 2: Trung bình
1. Trong lớp 30 học sinh, xác suất có ít nhất 2 người sinh cùng tháng là bao nhiêu?
2. Mật khẩu gồm 4 chữ số. Tính xác suất có ít nhất 2 chữ số giống nhau.
3. Tung xúc xắc đến khi ra mặt 6. Tính xác suất cần đúng 3 lần tung.

### Bài tập 3: Ứng dụng
1. Hash table có 1000 slot. Sau khi thêm 50 key, ước tính xác suất collision.
2. Thuật toán randomized có xác suất thành công 0.7. Chạy 5 lần độc lập, tính P(ít nhất 1 lần thành công).
3. Server xử lý request với tỷ lệ lỗi 1%. Trong 100 request, tính P(có từ 2 lỗi trở lên).

<details>
<summary>Đáp án Bài tập 1</summary>

1. **P(đúng 2 H) = C(3,2) × (1/2)³ = 3/8 = 0.375**
2. **P(Ace ∪ Cơ) = P(Ace) + P(Cơ) - P(Ace Cơ) = 4/52 + 13/52 - 1/52 = 16/52 = 4/13**
3. **P(cả hai đỏ) = (5/8) × (4/7) = 20/56 = 5/14**

</details>

## Tóm tắt

Trước khi rời bài, hãy kiểm tra xem bạn có thể tự nhắc lại ý chính, điều kiện áp dụng và một ví dụ tiêu biểu mà không cần nhìn tài liệu hay không.

**Xác suất Cơ bản** cung cấp nền tảng cho:

**Khái niệm chính**:
- Không gian mẫu Ω và biến cố A ⊆ Ω
- P(A) = |A|/|Ω| (trường hợp đồng khả năng)
- Tiên đề Kolmogorov: P(A) ≥ 0, P(Ω) = 1, tính cộng

**Quy tắc tính toán**:
- Quy tắc cộng: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
- Quy tắc nhân: P(A ∩ B) = P(A|B) × P(B)
- Độc lập: P(A ∩ B) = P(A) × P(B)

**Ứng dụng CS**:
- Thuật toán randomized và Monte Carlo
- Hash functions và Bloom filters
- Performance analysis và load testing
- Machine learning và AI

Trong bài tiếp theo, chúng ta sẽ học về **Biến ngẫu nhiên và Phân phối xác suất** - công cụ mạnh mẽ để mô hình hóa các hiện tượng ngẫu nhiên phức tạp.
