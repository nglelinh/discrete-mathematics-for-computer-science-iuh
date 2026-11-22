---

layout: post
title: "Ứng dụng Nâng cao của Nguyên lý Dirichlet"
categories: chapter08
date: 2021-01-01
order: 2
required: true
lang: en
excerpt: "Các biến thể mở rộng và ứng dụng nâng cao của nguyên lý Dirichlet trong lý thuyết số, hình học tổ hợp, phân tích va chạm băm, cân bằng tải và tắc nghẽn mạng."
---

Ở mục trước, chúng ta đã học phát biểu cơ bản và dạng tổng quát của nguyên lý Dirichlet. Mục này trình bày các **ứng dụng nâng cao** cùng một số biến thể mở rộng của nguyên lý trong toán học và khoa học máy tính.

Từ một ý tưởng rất đơn giản, nguyên lý Dirichlet có thể dẫn đến nhiều kết quả sâu sắc trong lý thuyết số, hình học tổ hợp và phân tích hệ thống. Ở mức độ nâng cao, câu hỏi không chỉ dừng lại ở việc có hai phần tử rơi vào cùng một ngăn hay không, mà còn xác định cận dưới về trọng số, số lượng phần tử hay cấu trúc bắt buộc phải xuất hiện. Vì vậy, bước khó nhất và quan trọng nhất là kỹ năng mô hình hóa bài toán.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Áp dụng** các biến thể có trọng số và đa chiều của nguyên lý Dirichlet.
- **Giải** các bài toán lý thuyết số, hình học và tổ hợp bằng lập luận chuồng bồ câu.
- **Liên hệ** nguyên lý với cân bằng tải, phân tích bộ nhớ đệm và đánh giá tắc nghẽn mạng.

**Từ khóa**: Dirichlet tổng quát, đa chiều, load balancing, chứng minh tồn tại.
</div>

## Các biến thể mở rộng của Nguyên lý Dirichlet

### Nguyên lý Dirichlet có trọng số

<div class="textbook-theorem" markdown="1">
**Định lý**: Nếu $$N$$ đối tượng có tổng trọng số $$W$$ được phân vào $$n$$ nhóm, thì tồn tại ít nhất một nhóm có tổng trọng số lớn hơn hoặc bằng $$W/n$$.
</div>

**Ứng dụng**: cân bằng tải (load balancing), phân phối tài nguyên và thiết kế thuật toán xấp xỉ.

### Nguyên lý Dirichlet đa chiều

<div class="textbook-theorem" markdown="1">
**Định lý**: Nếu đặt $$N$$ điểm vào một lưới $$k$$ chiều mà mỗi chiều được chia thành $$n$$ khoảng (tổng cộng $$n^k$$ ô), thì tồn tại ít nhất một ô chứa tối thiểu $$\lceil N/n^k \rceil$$ điểm.
</div>

## Ứng dụng trong Lý thuyết Số

### Định lý Dirichlet về xấp xỉ Diophantine

<div class="textbook-theorem" markdown="1">
**Định lý**: Với mọi số thực $$\alpha$$ và mọi số nguyên dương $$N$$, tồn tại các số nguyên $$p, q$$ với $$1 \le q \le N$$ sao cho:

<div class="textbook-equation" markdown="1">
$$\left\vert \alpha - p/q\right\vert  < 1/(qN)$$
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

<div class="textbook-proof" markdown="1">
**Ý tưởng chứng minh**: Xét $$N+1$$ phần lẻ $$\{0\}, \{\alpha\}, \{2\alpha\}, \ldots, \{N\alpha\}$$ nằm trong nửa khoảng $$[0,1)$$. Chia $$[0,1)$$ thành $$N$$ đoạn con bằng nhau, mỗi đoạn có độ dài $$1/N$$. Theo nguyên lý Dirichlet, có ít nhất hai giá trị $$\{i\alpha\}$$ và $$\{j\alpha\}$$ ($$0 \le i < j \le N$$) rơi vào cùng một đoạn con, từ đó suy ra tồn tại $$q = j - i$$ và $$p$$ thỏa mãn bất đẳng thức trên.
</div>

![Dirichlet — ứng dụng trong lý thuyết số](/discrete-mathematics-for-computer-science-iuh/img/course/Dirichlet.jpg)

<p class="textbook-figure-caption" data-figure="8.7">Định lý Dirichlet về xấp xỉ Diophantine — chia đoạn [0,1) thành $$N$$ chuồng để ép hai phần lẻ nằm sát nhau.</p>
### Bài toán tồn tại nghiệm đồng dư

**Bài toán**: Chứng minh rằng với mọi số nguyên $$a$$ không chia hết cho số nguyên tố $$p$$, tồn tại số nguyên dương $$n$$ sao cho $$a^n \equiv 1 \pmod p$$.

<div class="textbook-proof" markdown="1">
**Ý tưởng chứng minh**: Xét dãy $$p$$ số $$a^1, a^2, \ldots, a^p \pmod p$$. Vì $$a$$ không chia hết cho $$p$$, mọi số hạng chỉ có thể nhận một trong $$p-1$$ số dư khác 0 là $$1, 2, \ldots, p-1$$. Theo nguyên lý Dirichlet, tồn tại $$1 \le i < j \le p$$ sao cho $$a^i \equiv a^j \pmod p$$, suy ra $$a^{j-i} \equiv 1 \pmod p$$.
</div>

## Ứng dụng trong Hình học và Tổ hợp

![Biểu đồ Venn — phân vùng không gian](/discrete-mathematics-for-computer-science-iuh/img/course/Venn3.svg)

<p class="textbook-figure-caption" data-figure="8.8">Phân vùng không gian thành các ô — mỗi ô là một chuồng và mỗi điểm là một bồ câu trong các bài toán hình học.</p>
### Định lý Erdős–Ko–Rado

**Bài toán**: Trong một tập gồm $$n$$ phần tử, ta có thể chọn tối đa bao nhiêu tập con gồm $$k$$ phần tử (với $$n \ge 2k$$) sao cho hai tập bất kỳ đều có giao khác rỗng?

<div class="textbook-theorem" markdown="1">
**Định lý**: Khi $$n \ge 2k$$, số lượng tập con tối đa là $$C(n-1, k-1)$$.
</div>

<div class="textbook-proof" markdown="1">
**Ý tưởng chứng minh**: Xét các hoán vị vòng tròn của $$n$$ phần tử và đếm số tập con thuộc họ xuất hiện như các cung liên tiếp độ dài $$k$$ trên mỗi vòng tròn; trên mỗi vòng tròn, nhiều nhất $$k$$ cung như vậy có thể đôi một giao nhau.
</div>

### Định lý Sperner

<div class="textbook-theorem" markdown="1">
**Định lý**: Trong tập $$n$$ phần tử, số lượng tối đa các tập con sao cho không có tập nào chứa tập nào khác là $$C(n, \lfloor n/2 \rfloor)$$.
</div>

### Bài toán Ramsey cơ bản

**Bài toán**: Trong một nhóm 6 người bất kỳ, chứng minh rằng luôn có 3 người đôi một quen nhau hoặc 3 người đôi một không quen nhau.

<div class="textbook-proof" markdown="1">
**Ý tưởng chứng minh**: Chọn một người A bất kỳ và chia 5 người còn lại thành 2 nhóm: nhóm quen A và nhóm không quen A. Theo nguyên lý Dirichlet, ít nhất một nhóm có từ 3 người trở lên; xét các mối quan hệ giữa 3 người trong nhóm đó sẽ thu được ngay bộ ba thỏa mãn.
</div>

![Ramsey theory — trật tự bắt buộc xuất hiện](/discrete-mathematics-for-computer-science-iuh/img/course/TooManyPigeons.jpg)

<p class="textbook-figure-caption" data-figure="8.9">Lý thuyết Ramsey mở rộng tinh thần chuồng chim — khi cấu trúc đủ lớn, một mẫu trật tự nhất định tất yếu phải xuất hiện.</p>
## Ứng dụng trong Khoa học Máy tính

### Thuật toán băm và va chạm

```python
class PigeonholeHashAnalysis:
    def __init__(self, hash_bits, num_inputs):
        self.hash_space = 2 ** hash_bits
        self.num_inputs = num_inputs
    
    def guaranteed_collisions(self):
        """Số collision tối thiểu được đảm bảo"""
        if self.num_inputs <= self.hash_space:
            return 0
        return self.num_inputs - self.hash_space
    
    def birthday_bound(self):
        """Số input cần để có 50% xác suất collision"""
        return int(math.sqrt(math.pi * self.hash_space / 2))
    
    def pigeonhole_bound(self):
        """Số input cần để đảm bảo collision"""
        return self.hash_space + 1

# Ví dụ: MD5 (128 bits)
md5_analysis = PigeonholeHashAnalysis(128, 2**65)
print(f"Birthday attack: ~2^64 attempts")
print(f"Pigeonhole guarantee: 2^128 + 1 attempts")
```

![Birthday attack — va chạm hash](/discrete-mathematics-for-computer-science-iuh/img/course/Birthdaymatch.svg)

<p class="textbook-figure-caption" data-figure="8.10">Phân tích va chạm hàm băm kết hợp nguyên lý chuồng chim và ngưỡng sinh nhật — hai công cụ nền tảng trong mật mã học.</p>
### Cân bằng tải và hệ thống phân tán

```python
def optimal_load_distribution(tasks, servers):
    """Phân phối tải tối ưu theo nguyên lý Dirichlet"""
    base_load = tasks // servers
    extra_tasks = tasks % servers
    
    # Theo nguyên lý Dirichlet:
    # - (servers - extra_tasks) servers có base_load tasks
    # - extra_tasks servers có (base_load + 1) tasks
    
    return {
        'min_load': base_load,
        'max_load': base_load + (1 if extra_tasks > 0 else 0),
        'servers_with_extra': extra_tasks,
        'load_imbalance': 1 if extra_tasks > 0 else 0
    }

def cache_hit_analysis(cache_size, access_pattern_size):
    """Phân tích cache hit theo nguyên lý Dirichlet"""
    if access_pattern_size <= cache_size:
        return "Perfect caching possible"
    
    guaranteed_misses = access_pattern_size - cache_size
    return f"At least {guaranteed_misses} cache misses guaranteed"
```

### Định tuyến mạng và tắc nghẽn

```python
def network_congestion_analysis(packets, links, link_capacity):
    """Phân tích tắc nghẽn mạng"""
    total_capacity = links * link_capacity
    
    if packets > total_capacity:
        return {
            'status': 'Guaranteed congestion',
            'overload': packets - total_capacity,
            'min_congested_links': math.ceil((packets - total_capacity) / link_capacity)
        }
    
    # Theo nguyên lý Dirichlet
    max_load_per_link = math.ceil(packets / links)
    congested_links = 0 if max_load_per_link <= link_capacity else links
    
    return {
        'status': 'Possible congestion',
        'max_load_per_link': max_load_per_link,
        'potentially_congested_links': congested_links
    }
```

## Bài tập Nâng cao

### Bài tập 1: Lý thuyết Số
1. Chứng minh rằng với mọi số nguyên dương $$n$$, tồn tại một bội số dương của $$n$$ chỉ gồm các chữ số 0 và 1.
2. Cho $$p$$ là số nguyên tố lẻ. Chứng minh rằng tồn tại số nguyên $$a$$ sao cho $$a^2 \equiv -1 \pmod p$$ khi và chỉ khi $$p \equiv 1 \pmod 4$$.

### Bài tập 2: Hình học
1. Cho 5 điểm trong hình vuông đơn vị (cạnh bằng 1). Chứng minh rằng tồn tại 2 điểm có khoảng cách không vượt quá $$\sqrt{2}/2$$.
2. Trong hình vuông đơn vị có 9 điểm sao cho không có 3 điểm nào thẳng hàng. Chứng minh rằng tồn tại 3 điểm tạo thành một tam giác có diện tích không vượt quá $$1/8$$ (do đó cũng không vượt quá $$1/4$$).

### Bài tập 3: Khoa học Máy tính
1. Một bảng băm có 1.000 ngăn chứa (bucket). Cần tối thiểu bao nhiêu khóa để đảm bảo có ít nhất một ngăn chứa từ 5 khóa trở lên?
2. Trong một hệ thống phân tán có 10 máy chủ cần xử lý 97 tác vụ, nếu phân bổ đều nhất có thể thì tải tối thiểu và tải tối đa của mỗi máy chủ là bao nhiêu?
3. Chứng minh rằng mọi thuật toán sắp xếp dựa trên so sánh đều cần ít nhất $$\lceil \log_2(n!) \rceil$$ phép so sánh trong trường hợp xấu nhất.

<details>
<summary>Gợi ý Bài tập 1</summary>

1. **Xét dãy $$n$$ số $$1, 11, 111, \ldots, \underbrace{11\ldots1}_{n\text{ chữ số }1}$$**: nếu có một số chia hết cho $$n$$ thì xong; ngược lại, $$n$$ số chỉ nhận các số dư trong $$n-1$$ giá trị $$1, 2, \ldots, n-1$$, nên có hai số cùng số dư khi chia cho $$n$$ và hiệu của chúng là bội số dương của $$n$$ chỉ gồm chữ số 1 và 0.
2. **Sử dụng định lý Wilson**: $$(p-1)! \equiv -1 \pmod p$$ kết hợp với tính chất của thặng dư bậc hai theo modulo $$p$$.

</details>

## Kỹ thuật Chứng minh Nâng cao

### Nguyên lý Dirichlet xác suất

<div class="textbook-theorem" markdown="1">
**Định lý**: Khi phân bổ ngẫu nhiên đều $$N$$ quả bóng vào $$n$$ hộp ($$n \ge 2$$), xác suất để có ít nhất một hộp chứa từ 2 quả bóng trở lên thỏa mãn cận dưới:
</div>

$$P(\max \ge 2) \ge 1 - n\left(1 - \frac{1}{n}\right)^N.$$

### Nguyên lý Dirichlet mang tính xây dựng (Constructive)

Bên cạnh chứng minh sự tồn tại thuần túy, trong nhiều bài toán lập trình ta có thể thiết kế thuật toán trực tiếp tìm ra nhóm thỏa mãn tính chất cần thiết.

```python
def constructive_pigeonhole(objects, groups, property_checker):
    """Tìm nhóm thỏa mãn tính chất theo nguyên lý Dirichlet"""
    group_assignments = {}
    
    for obj in objects:
        # Assign object to group based on some hash/property
        group_id = hash(obj) % groups
        
        if group_id not in group_assignments:
            group_assignments[group_id] = []
        group_assignments[group_id].append(obj)
        
        # Check if current group satisfies the property
        if property_checker(group_assignments[group_id]):
            return group_id, group_assignments[group_id]
    
    # By pigeonhole principle, some group must satisfy the property
    return max(group_assignments.items(), key=lambda x: len(x[1]))
```

## Xem thêm / Video gợi ý

- [Pigeonhole Principle — Advanced](https://www.youtube.com/watch?v=9jZ5n8k0p0Q) — 3Blue1Brown (Generalized version)

## Tóm tắt

**Nguyên lý Dirichlet nâng cao** mở rộng khả năng suy luận sang nhiều lĩnh vực:

- **Lý thuyết số**: xấp xỉ Diophantine, đồng dư thức và chứng minh tồn tại nghiệm.
- **Hình học và tổ hợp**: bài toán Ramsey, định lý Erdős–Ko–Rado, định lý Sperner và phân vùng không gian.
- **Khoa học máy tính**: va chạm hàm băm và tấn công sinh nhật, cân bằng tải, phân tích bộ nhớ đệm và tắc nghẽn mạng.
- **Kỹ thuật chứng minh**: phân biệt chứng minh tồn tại với thuật toán xây dựng, biến thể xác suất và mở rộng đa chiều.

Trong **Chương 9: Ứng dụng Toán Rời Rạc trong CNTT Hiện đại**, chúng ta sẽ gắn các khái niệm đã học vào các tình huống thực tế từ hệ thống sản xuất.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=pPuvnD4PYNE">[Discrete Mathematics] Pigeonhole Principle Examples</a> — TrevTutor, tiếng Anh. Trình bày các ví dụ nâng cao vận dụng nguyên lý Dirichlet.
- <a href="https://www.youtube.com/watch?v=TCZ3YwbcDaw">The Pigeon Hole Principle: 7 gorgeous proofs</a> — Mathologer, tiếng Anh. Giới thiệu bảy chứng minh điển hình cho thấy sức mạnh của dạng tổng quát.
- <a href="https://www.youtube.com/watch?v=NdnByi_tK6Q">A Hairy Problem (and a Feathery Solution) - Numberphile</a> — Numberphile, tiếng Anh. Ví dụ kinh điển về số sợi tóc minh họa trực quan mô hình chuồng bồ câu.
