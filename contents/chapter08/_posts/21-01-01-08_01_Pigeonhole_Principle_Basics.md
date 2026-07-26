---

layout: post
title: "Nguyên lý Dirichlet cơ bản"
categories: chapter08
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Trong chương này chúng ta nghiên cứu nguyên lý Dirichlet (nguyên lý chuồng chim) — công cụ chứng minh sự tồn tại dựa trên lập luận đếm đơn giản. Nếu có 11…"
---

<div class="textbook-epigraph" markdown="1">

"If you put infinitely many balls into finitely many boxes, some box must contain more than one ball."

<span class="epigraph-attribution">— Pigeonhole Principle (folk)</span>

</div>

Trong chương này chúng ta nghiên cứu **nguyên lý Dirichlet** (nguyên lý chuồng chim) — công cụ chứng minh sự tồn tại dựa trên lập luận đếm đơn giản. Nếu có 11 file mà chỉ 10 thư mục để chứa, ít nhất một thư mục phải nhận từ hai file trở lên. Mục 8.1 này bắt đầu từ phát biểu chuẩn và các ví dụ cơ bản.

Nguyên lý Dirichlet cho phép kết luận sự tồn tại mà không cần chỉ ra đối tượng cụ thể. Nó xuất hiện trong phân tích xung đột băm, phân phối dữ liệu, lập lịch và nhiều chứng minh tổ hợp gọn nhưng sắc. Chỉ cần mô hình hóa đúng đâu là đồ vật, đâu là ngăn chứa, chúng ta có thể rút ra kết luận mạnh từ một quan sát cơ bản.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phát biểu** nguyên lý Dirichlet đơn giản và tổng quát.
- **Áp dụng** nguyên lý để chứng minh sự tồn tại (không cần xây dựng đối tượng).
- **Mô hình hóa** bài toán thành đối tượng và ngăn chứa.
- **Giải thích** ứng dụng trong hash collision và phân phối tài nguyên.

**Từ khóa**: nguyên lý Dirichlet (pigeonhole principle), tồn tại, mô hình hóa, $$\lceil N/n \rceil$$.
</div>

## Phát biểu Nguyên lý

### Nguyên lý Dirichlet đơn giản

**Phát biểu**: Nếu n + 1 con bồ câu bay vào n cái chuồng, thì ít nhất một chuồng chứa nhiều hơn một con bồ câu.

**Phát biểu toán học**: Nếu n + 1 đối tượng được phân vào n nhóm, thì ít nhất một nhóm chứa ít nhất 2 đối tượng.

### Nguyên lý Dirichlet tổng quát

**Phát biểu**: Nếu N đối tượng được phân vào n nhóm, thì ít nhất một nhóm chứa ít nhất ⌈N/n⌉ đối tượng.

Trong đó ⌈x⌉ là hàm ceiling (làm tròn lên).

![Quá nhiều bồ câu — không thể phân bố đều](/discrete-mathematics-for-computer-science-iuh/img/course/TooManyPigeons.jpg)

<p class="textbook-figure-caption" data-figure="8.2">Phiên bản tổng quát — $N$ đối tượng vào $n$ nhóm thì ít nhất một nhóm chứa $\lceil N/n \rceil$ đối tượng.</p>
## Ví dụ cơ bản

<div class="textbook-example" markdown="1">
**Ví dụ** 1: Sinh nhật:
Trong một lớp có 13 học sinh, chứng minh rằng ít nhất có 2 học sinh sinh trong cùng một tháng.

**Giải**:
- 13 học sinh (bồ câu)
- 12 tháng (chuồng)
- Theo nguyên lý Dirichlet: 13 > 12, nên ít nhất một tháng có ≥ 2 học sinh sinh trong đó.

![Johann Peter Gustav Lejeune Dirichlet](/discrete-mathematics-for-computer-science-iuh/img/course/Dirichlet.jpg)

<p class="textbook-figure-caption" data-figure="8.3">Johann Peter Gustav Lejeune Dirichlet (1805–1859) — người hệ thống hóa nguyên lý chuồng chim trong toán học.</p>
</div>

<div class="textbook-example" markdown="1">
**Ví dụ** 2: Tóc trên đầu:
Chứng minh rằng ở Hà Nội có ít nhất 2 người có cùng số sợi tóc trên đầu.

**Giải**:
- Dân số Hà Nội: ~8 triệu người
- Số sợi tóc tối đa: ~200,000 sợi
- 8,000,000 > 200,000, nên ít nhất 2 người có cùng số sợi tóc.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ** 3: Điểm số:
Trong 11 bài kiểm tra, mỗi bài được chấm từ 0-10 điểm. Chứng minh rằng có ít nhất 2 bài có cùng điểm số.

**Giải**:
- 11 bài kiểm tra
- 11 điểm số có thể (0,1,2,...,10)
- Theo nguyên lý Dirichlet: 11 = 11, nhưng nếu có 12 bài thì chắc chắn có 2 bài cùng điểm.
</div>

## Chứng minh Nguyên lý Dirichlet

### Chứng minh phản chứng

**Giả sử** mỗi chuồng chứa nhiều nhất 1 con bồ câu.

Khi đó, tổng số bồ câu ≤ n × 1 = n.

Nhưng chúng ta có n + 1 con bồ câu, mâu thuẫn với giả thiết.

Vậy ít nhất một chuồng chứa ≥ 2 con bồ câu. ∎

### Chứng minh tổng quát

**Giả sử** mỗi nhóm chứa < ⌈N/n⌉ đối tượng.

Khi đó, mỗi nhóm chứa ≤ ⌈N/n⌉ - 1 đối tượng.

Tổng số đối tượng ≤ n × (⌈N/n⌉ - 1) < n × (N/n + 1 - 1) = N.

Mâu thuẫn! Vậy ít nhất một nhóm chứa ≥ ⌈N/n⌉ đối tượng. ∎

## Birthday paradox — xác suất vs đảm bảo

Nguyên lý Dirichlet trả lời câu *khi nào chắc chắn trùng*. **Nghịch lý sinh nhật** (birthday paradox) trả lời câu *khi nào xác suất trùng đã lớn* — và kết quả bất ngờ: với chỉ khoảng **23** người, xác suất có ít nhất hai người cùng ngày sinh đã **> 50%** (trong khi phải đợi **367** người mới *đảm bảo* trùng theo Dirichlet).

Lý do: ta đếm **cặp** $$(i,j)$$, không so từng người với một mốc cố định. Số cặp là $$\binom{n}{2} = n(n-1)/2$$; với $$n=23$$ đã có 253 cặp, mỗi cặp “có cơ hội” $$1/365$$ trùng ngày.

Công thức chính xác ($$n \le 365$$):

$$P(\text{có trùng}) = 1 - \dfrac{365!}{(365-n)!\,365^n} \approx 1 - e^{-n(n-1)/(2\cdot 365)}.$$

![Birthday paradox — xác suất trùng theo số người](/discrete-mathematics-for-computer-science-iuh/img/course/Birthdaymatch.svg)

<p class="textbook-figure-caption" data-figure="8.4">Đồ thị birthday paradox: trục hoành = số người $$n$$, trục tung = xác suất có ít nhất một cặp cùng ngày sinh ($$d=365$$). Khoảng $$n\approx 23$$ đã cho $$P\approx 50\%$$; $$n\approx 57$$ cho $$P\approx 99\%$$ — va chạm “cặp” xảy ra sớm hơn trực giác, khác ngưỡng đảm bảo Dirichlet $$n=367$$.</p>

Trong không gian hash $$N=2^b$$, cùng ý tưởng cho *birthday bound*: khoảng $$\sqrt{N}=2^{b/2}$$ mẫu đã đủ để xác suất collision ~50%, trong khi Dirichlet chỉ *đảm bảo* khi có $$N+1$$ mẫu.

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

![Cây quyết định — phân tích không gian trạng thái](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="8.5">Nguyên lý chuồng chim giúp chứng minh sự tồn tại mà không cần liệt kê — rất hữu ích trong phân tích thuật toán và cryptography.</p>
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

<div class="textbook-theorem" markdown="1">
**Định lý**: Nếu \( N \) đối tượng được phân vào \( n \) nhóm, thì ít nhất một nhóm chứa ít nhất \( \lceil N/n \rceil \) đối tượng.
</div>

**Chứng minh** (phản chứng):

Giả sử mọi nhóm chứa nhiều nhất \( \lceil N/n \rceil - 1 \) đối tượng.  
Tổng số đối tượng ≤ \( n(\lceil N/n \rceil - 1) < N \), mâu thuẫn.

Do đó, ít nhất một nhóm phải chứa ≥ \( \lceil N/n \rceil \) đối tượng.

**Hệ quả** (dạng hay dùng trong CS):
- Nếu \( N > n(k-1) \), thì ít nhất một nhóm chứa ≥ \( k \) đối tượng.

**Ý nghĩa CS**:
- **Hash collision**: \( n+1 \) khóa vào bảng \( n \) ô → chắc chắn có va chạm.
- **Load balancing**: \( N \) tác vụ, \( n \) máy → ít nhất một máy nhận ≥ \( \lceil N/n \rceil \) tác vụ.

## Xem thêm / Video gợi ý

- [Pigeonhole Principle — Advanced](https://www.youtube.com/watch?v=9jZ5n8k0p0Q) — 3Blue1Brown (Generalized version)

## Tóm tắt
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
