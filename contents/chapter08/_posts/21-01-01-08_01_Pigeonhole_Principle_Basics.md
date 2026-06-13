---
layout: post
title: "Nguyên lý Dirichlet cơ bản"
categories: chapter08
date: 2021-01-01
order: 1
required: true
lang: en
---

# Nguyên lý Dirichlet cơ bản

Nếu có 11 file mà chỉ 10 thư mục để chứa, ít nhất một thư mục phải nhận từ 2 file trở lên. Phát biểu nghe gần như hiển nhiên, nhưng đằng sau nó là một nguyên lý đếm cực mạnh, đủ sức giải nhiều bài toán mà thoạt nhìn chẳng liên quan gì đến "chim bồ câu và chuồng".


Nguyên lý Dirichlet thường được dùng khi ta không cần biết chính xác đối tượng nào trùng nhau, chỉ cần chứng minh chắc chắn rằng sự trùng lặp phải xảy ra.
**Nguyên lý Dirichlet** cho phép ta kết luận sự tồn tại mà không cần chỉ ra đối tượng cụ thể. Nó xuất hiện trong phân tích xung đột băm, phân phối dữ liệu, lập lịch, nén thông tin, và nhiều chứng minh tổ hợp rất gọn nhưng sắc.

Điểm hay của nguyên lý này là nó biến trực giác về "không thể phân bố đều mãi" thành một công cụ hình thức. Chỉ cần mô hình hóa đúng đâu là đồ vật, đâu là ngăn chứa, ta có thể rút ra kết luận bất ngờ từ một quan sát rất cơ bản.

Trong bài này, chúng ta sẽ học phát biểu chuẩn của nguyên lý Dirichlet và luyện cách nhận ra nó trong những bài toán tưởng như không liên quan.

## Phát biểu Nguyên lý

### Nguyên lý Dirichlet đơn giản

**Phát biểu**: Nếu n + 1 con bồ câu bay vào n cái chuồng, thì ít nhất một chuồng chứa nhiều hơn một con bồ câu.

**Phát biểu toán học**: Nếu n + 1 đối tượng được phân vào n nhóm, thì ít nhất một nhóm chứa ít nhất 2 đối tượng.

### Nguyên lý Dirichlet tổng quát

**Phát biểu**: Nếu N đối tượng được phân vào n nhóm, thì ít nhất một nhóm chứa ít nhất ⌈N/n⌉ đối tượng.

Trong đó ⌈x⌉ là hàm ceiling (làm tròn lên).

## Ví dụ cơ bản

### Ví dụ 1: Sinh nhật
Trong một lớp có 13 học sinh, chứng minh rằng ít nhất có 2 học sinh sinh trong cùng một tháng.

**Giải**:
- 13 học sinh (bồ câu)
- 12 tháng (chuồng)
- Theo nguyên lý Dirichlet: 13 > 12, nên ít nhất một tháng có ≥ 2 học sinh sinh trong đó.

### Ví dụ 2: Tóc trên đầu
Chứng minh rằng ở Hà Nội có ít nhất 2 người có cùng số sợi tóc trên đầu.

**Giải**:
- Dân số Hà Nội: ~8 triệu người
- Số sợi tóc tối đa: ~200,000 sợi
- 8,000,000 > 200,000, nên ít nhất 2 người có cùng số sợi tóc.

### Ví dụ 3: Điểm số
Trong 11 bài kiểm tra, mỗi bài được chấm từ 0-10 điểm. Chứng minh rằng có ít nhất 2 bài có cùng điểm số.

**Giải**:
- 11 bài kiểm tra
- 11 điểm số có thể (0,1,2,...,10)
- Theo nguyên lý Dirichlet: 11 = 11, nhưng nếu có 12 bài thì chắc chắn có 2 bài cùng điểm.

## Chứng minh Nguyên lý Dirichlet

### Chứng minh phản chứng

**Giả sử** mỗi chuồng chứa nhiều nhất 1 con bồ câu.

Khi đó, tổng số bồ câu ≤ n × 1 = n.

Nhưng ta có n + 1 con bồ câu, mâu thuẫn với giả thiết.

Vậy ít nhất một chuồng chứa ≥ 2 con bồ câu. ∎

### Chứng minh tổng quát

**Giả sử** mỗi nhóm chứa < ⌈N/n⌉ đối tượng.

Khi đó, mỗi nhóm chứa ≤ ⌈N/n⌉ - 1 đối tượng.

Tổng số đối tượng ≤ n × (⌈N/n⌉ - 1) < n × (N/n + 1 - 1) = N.

Mâu thuẫn! Vậy ít nhất một nhóm chứa ≥ ⌈N/n⌉ đối tượng. ∎

## Ứng dụng trong Khoa học Máy tính

### 1. Hash Tables và Collision
```python
def hash_collision_guarantee(num_keys, table_size):
    """Đảm bảo collision trong hash table"""
    if num_keys > table_size:
        return True, f"Chắc chắn có collision (≥{math.ceil(num_keys/table_size)} keys/bucket)"
    return False, "Không đảm bảo collision"

# Ví dụ: 1000 keys, 100 buckets
# Chắc chắn có bucket chứa ≥ 10 keys
```

### 2. Load Balancing
```python
def load_balancing_analysis(tasks, servers):
    """Phân tích cân bằng tải"""
    min_load_per_server = math.ceil(tasks / servers)
    return {
        'guaranteed_max_load': min_load_per_server,
        'is_perfectly_balanced': tasks % servers == 0,
        'overloaded_servers': max(0, tasks - servers * (min_load_per_server - 1))
    }
```

### 3. Thuật toán Randomized
```python
def birthday_attack_probability(hash_bits):
    """Tính xác suất collision trong hash function"""
    hash_space = 2 ** hash_bits
    # Theo nguyên lý Dirichlet: cần √(hash_space) attempts
    return math.sqrt(hash_space)

# SHA-256 (256 bits): cần ~2^128 attempts để guarantee collision
```

## Bài tập thực hành

### Bài tập 1: Cơ bản
1. Trong 367 người, chứng minh rằng có ít nhất 2 người sinh cùng ngày.
2. Chọn 5 điểm bất kỳ trong hình vuông 2×2. Chứng minh rằng có 2 điểm cách nhau ≤ √2.
3. Trong 10 số nguyên bất kỳ, chứng minh rằng có 2 số có cùng chữ số cuối.

### Bài tập 2: Trung bình
1. Chứng minh rằng trong 6 người bất kỳ, có 3 người quen nhau hoặc 3 người không quen nhau.
2. Trong dãy 101 số nguyên, chứng minh rằng có một đoạn con liên tiếp có tổng chia hết cho 100.
3. Cho 51 số nguyên từ 1 đến 100. Chứng minh rằng có 2 số mà một số chia hết cho số kia.

### Bài tập 3: Nâng cao
1. Trong mặt phẳng có 5 điểm, không có 3 điểm thẳng hàng. Chứng minh rằng có 4 điểm tạo thành tứ giác lồi.
2. Cho 2n + 1 số thực. Chứng minh rằng có thể chọn n + 1 số sao cho trung bình cộng ≥ trung bình cộng của tất cả.
3. Trong bảng n×n, mỗi ô chứa số 1 hoặc -1. Chứng minh rằng có 2 hàng hoặc 2 cột có tích vô hướng ≥ 0.

<details>
<summary>Đáp án Bài tập 1</summary>

1. **367 người, 366 ngày** → Theo nguyên lý Dirichlet: 367 > 366
2. **Chia hình vuông thành 4 ô 1×1** → 5 điểm, 4 ô → có ô chứa ≥ 2 điểm → khoảng cách ≤ đường chéo = √2
3. **10 số, 10 chữ số cuối (0-9)** → Theo nguyên lý Dirichlet: 10 = 10, nhưng nếu có 11 số thì chắc chắn

</details>

## Các biến thể của Nguyên lý Dirichlet

### 1. Nguyên lý Dirichlet mạnh
Nếu N đối tượng được phân vào n nhóm và N > kn, thì ít nhất một nhóm chứa > k đối tượng.

### 2. Nguyên lý Dirichlet liên tục
Nếu N đối tượng được phân bố liên tục trên độ dài L, thì có đoạn độ dài L/n chứa ≥ N/n đối tượng.

### 3. Nguyên lý Dirichlet xác suất
Nếu phân bố ngẫu nhiên N đối tượng vào n nhóm, xác suất để mỗi nhóm chứa ≤ k đối tượng giảm exponentially khi N tăng.

## Định lý Dirichlet tổng quát – Chứng minh

**Định lý**: Nếu \( N \) đối tượng được phân vào \( n \) nhóm, thì ít nhất một nhóm chứa ít nhất \( \lceil N/n \rceil \) đối tượng.

**Chứng minh** (phản chứng):

Giả sử mọi nhóm chứa nhiều nhất \( \lceil N/n \rceil - 1 \) đối tượng.  
Tổng số đối tượng ≤ \( n(\lceil N/n \rceil - 1) < N \), mâu thuẫn.

Do đó, ít nhất một nhóm phải chứa ≥ \( \lceil N/n \rceil \) đối tượng.

**Hệ quả** (dạng hay dùng trong CS):
- Nếu \( N > n(k-1) \), thì ít nhất một nhóm chứa ≥ \( k \) đối tượng.

**Ý nghĩa CS**:
- **Hash collision**: \( n+1 \) khóa vào bảng \( n \) ô → chắc chắn có va chạm.
- **Load balancing**: \( N \) tác vụ, \( n \) máy → ít nhất một máy nhận ≥ \( \lceil N/n \rceil \) tác vụ.

## Tóm tắt

Trước khi rời bài, hãy kiểm tra xem bạn có thể tự nhắc lại ý chính, điều kiện áp dụng và một ví dụ tiêu biểu mà không cần nhìn tài liệu hay không.

**Nguyên lý Dirichlet** là công cụ chứng minh mạnh mẽ:

**Phát biểu cơ bản**: N đối tượng, n nhóm (N > n) → ít nhất 1 nhóm có ≥ 2 đối tượng

**Phát biểu tổng quát**: N đối tượng, n nhóm → ít nhất 1 nhóm có ≥ ⌈N/n⌉ đối tượng

**Ứng dụng**:
- Hash tables và collision detection
- Load balancing trong hệ thống phân tán  
- Thuật toán randomized và cryptography
- Chứng minh tồn tại trong tổ hợp

**Kỹ thuật chứng minh**: Thường dùng phản chứng hoặc đếm trực tiếp

Trong bài tiếp theo, chúng ta sẽ học về **Nguyên lý Dirichlet nâng cao** với các ứng dụng phức tạp hơn trong lý thuyết số và hình học.
