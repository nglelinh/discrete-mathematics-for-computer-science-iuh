---

layout: post
title: "Nguyên lý Dirichlet cơ bản"
categories: chapter08
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Giới thiệu nguyên lý Dirichlet (nguyên lý chuồng chim) dạng cơ bản và tổng quát, chứng minh phản chứng, so sánh với nghịch lý sinh nhật và ứng dụng trong khoa học máy tính."
---

<div class="textbook-epigraph" markdown="1">

"If you put infinitely many balls into finitely many boxes, some box must contain more than one ball."

<span class="epigraph-attribution">— Pigeonhole Principle (folk)</span>

</div>

Trong chương này, chúng ta nghiên cứu **nguyên lý Dirichlet** (còn gọi là nguyên lý chuồng chim hay chuồng bồ câu) — công cụ chứng minh sự tồn tại dựa trên một lập luận đếm đơn giản. Nếu có 11 tệp tin nhưng chỉ có 10 thư mục để lưu trữ, chắc chắn có ít nhất một thư mục chứa từ hai tệp trở lên. Mục 8.1 trình bày phát biểu cơ bản, dạng tổng quát và các ví dụ nhập môn.

Điểm đặc biệt của nguyên lý Dirichlet là cho phép khẳng định một đối tượng hoặc cấu hình chắc chắn tồn tại mà không cần chỉ ra cụ thể nó nằm ở đâu. Nguyên lý này xuất hiện thường xuyên trong phân tích va chạm hàm băm, cân bằng tải, lập lịch và các chứng minh tổ hợp. Chỉ cần xác định đúng đâu là "đối tượng" và đâu là "ngăn chứa", ta có thể rút ra những kết luận chặt chẽ từ một nhận xét rất gọn.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Phát biểu** và chứng minh nguyên lý Dirichlet dạng đơn giản và dạng tổng quát.
- **Áp dụng** nguyên lý để chứng minh sự tồn tại mà không cần xây dựng trực tiếp đối tượng.
- **Mô hình hóa** bài toán thành các đối tượng (bồ câu) và ngăn chứa (chuồng).
- **Giải thích** ứng dụng trong va chạm hàm băm (hash collision) và phân phối tài nguyên.

**Từ khóa**: nguyên lý Dirichlet (pigeonhole principle), tồn tại, mô hình hóa, $$\lceil N/n \rceil$$.
</div>

## Phát biểu Nguyên lý

### Nguyên lý Dirichlet đơn giản

**Phát biểu trực quan**: Nếu có $$n + 1$$ con bồ câu bay vào $$n$$ cái chuồng, thì ít nhất một chuồng chứa từ 2 con bồ câu trở lên.

**Phát biểu toán học**: Nếu phân bổ $$n + 1$$ đối tượng vào $$n$$ nhóm, thì tồn tại ít nhất một nhóm chứa tối thiểu 2 đối tượng.

### Nguyên lý Dirichlet tổng quát

**Phát biểu**: Nếu phân bổ $$N$$ đối tượng vào $$n$$ nhóm, thì tồn tại ít nhất một nhóm chứa ít nhất $$\lceil N/n \rceil$$ đối tượng.

Trong đó $$\lceil x \rceil$$ là hàm trần (ceiling), cho số nguyên nhỏ nhất lớn hơn hoặc bằng $$x$$.

![Quá nhiều bồ câu — không thể phân bố đều](/discrete-mathematics-for-computer-science-iuh/img/course/TooManyPigeons.jpg)

<p class="textbook-figure-caption" data-figure="8.2">Phiên bản tổng quát — khi phân bổ $$N$$ đối tượng vào $$n$$ nhóm thì ít nhất một nhóm chứa tối thiểu $$\lceil N/n \rceil$$ đối tượng.</p>
## Ví dụ cơ bản

<div class="textbook-example" markdown="1">
**Ví dụ 1 (Tháng sinh)**:
Trong một lớp gồm 13 học sinh, chứng minh rằng có ít nhất 2 học sinh sinh cùng một tháng.

**Giải**:
- 13 học sinh đóng vai trò đối tượng (bồ câu).
- 12 tháng trong năm đóng vai trò ngăn chứa (chuồng).
- Vì 13 > 12, theo nguyên lý Dirichlet chắc chắn có ít nhất một tháng có từ 2 học sinh trở lên cùng sinh.

![Johann Peter Gustav Lejeune Dirichlet](/discrete-mathematics-for-computer-science-iuh/img/course/Dirichlet.jpg)

<p class="textbook-figure-caption" data-figure="8.3">Johann Peter Gustav Lejeune Dirichlet (1805–1859) — người hệ thống hóa nguyên lý chuồng chim trong toán học.</p>
</div>

<div class="textbook-example" markdown="1">
**Ví dụ 2 (Số sợi tóc trên đầu)**:
Chứng minh rằng ở Hà Nội có ít nhất 2 người có cùng số sợi tóc trên đầu.

**Giải**:
- Dân số Hà Nội vào khoảng 8 triệu người.
- Số sợi tóc tối đa trên đầu một người vào khoảng 200.000 sợi (tức nhiều nhất khoảng 200.001 giá trị có thể, tính cả 0).
- Vì 8.000.000 > 200.001, chắc chắn tồn tại ít nhất 2 người có cùng số sợi tóc.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ 3 (Điểm kiểm tra)**:
Trong 12 bài kiểm tra, mỗi bài được chấm theo thang điểm nguyên từ 0 đến 10. Chứng minh rằng có ít nhất 2 bài có cùng điểm số.

**Giải**:
- 12 bài kiểm tra là các đối tượng.
- Thang điểm nguyên từ 0 đến 10 có 11 mức điểm có thể (0, 1, 2, …, 10).
- Vì 12 > 11, theo nguyên lý Dirichlet chắc chắn có ít nhất 2 bài đạt cùng một điểm số (nếu chỉ có 11 bài thì chưa thể đảm bảo vì 11 bài có thể nhận đủ 11 điểm khác nhau).
</div>

## Chứng minh Nguyên lý Dirichlet

<div class="textbook-proof" id="chứng-minh-phản-chứng" markdown="1">
**Chứng minh phản chứng (dạng đơn giản)**:

Giả sử ngược lại rằng mỗi chuồng chứa nhiều nhất 1 con bồ câu. Khi đó, tổng số bồ câu tối đa là $$n \times 1 = n$$. Điều này mâu thuẫn với giả thiết có $$n + 1$$ con bồ câu. Vậy phải có ít nhất một chuồng chứa từ 2 con bồ câu trở lên.
</div>

<div class="textbook-proof" id="chứng-minh-tổng-quát" markdown="1">
**Chứng minh phản chứng (dạng tổng quát)**:

Giả sử mỗi nhóm chứa ít hơn $$\lceil N/n \rceil$$ đối tượng, nghĩa là nhiều nhất $$\lceil N/n \rceil - 1$$ đối tượng. Khi đó, tổng số đối tượng ở cả $$n$$ nhóm thỏa mãn:

$$n \times (\lceil N/n \rceil - 1) < n \times (N/n + 1 - 1) = N,$$

mâu thuẫn với giả thiết có đúng $$N$$ đối tượng. Vậy ít nhất một nhóm phải chứa tối thiểu $$\lceil N/n \rceil$$ đối tượng.
</div>

### Video ngắn: Ví dụ hình học — 5 điểm trong hình vuông 2×2

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#0e0e10;" src="{{ site.baseurl }}/public/videos/reels/pigeonhole-square.mp4"></video>
</div>

Chia hình vuông $$2\times2$$ thành $$4$$ ô vuông nhỏ $$1\times1$$ (đóng vai trò các "chuồng"). Khi đặt $$5$$ điểm (các "chim") vào hình vuông, theo nguyên lý Dirichlet chắc chắn có ít nhất một ô chứa từ 2 điểm trở lên, và khoảng cách giữa hai điểm cùng ô không vượt quá độ dài đường chéo $$\sqrt2$$. Video minh họa ba cách đặt điểm khác nhau — ở mọi trường hợp đều xuất hiện một cặp điểm thỏa mãn.

## Nghịch lý sinh nhật — xác suất và sự đảm bảo

Nguyên lý Dirichlet trả lời câu hỏi *khi nào trùng lặp chắc chắn xảy ra*. Trong khi đó, **nghịch lý sinh nhật** (birthday paradox) trả lời câu hỏi *khi nào xác suất trùng lặp đã lớn* — với kết quả trái trực giác: chỉ cần **23** người, xác suất có ít nhất hai người cùng ngày sinh đã vượt **50%**, dù phải có tới **367** người mới *đảm bảo chắc chắn* theo nguyên lý Dirichlet.

Lý do nằm ở chỗ ta so sánh tất cả các **cặp** $$(i,j)$$ chứ không so từng người với một ngày cố định. Số cặp có thể tạo từ $$n$$ người là $$\binom{n}{2} = n(n-1)/2$$; với $$n=23$$ đã có tới 253 cặp, và mỗi cặp đều có xác suất $$1/365$$ trùng ngày sinh.

Công thức chính xác (với $$n \le 365$$):

$$P(\text{có trùng}) = 1 - \dfrac{365!}{(365-n)!\,365^n} \approx 1 - e^{-n(n-1)/(2\cdot 365)}.$$

![Birthday paradox — xác suất trùng theo số người](/discrete-mathematics-for-computer-science-iuh/img/course/Birthdaymatch.svg)

<p class="textbook-figure-caption" data-figure="8.4">Đồ thị nghịch lý sinh nhật: trục hoành là số người $$n$$, trục tung là xác suất có ít nhất một cặp trùng ngày sinh ($$d=365$$). Tại $$n\approx 23$$ xác suất đạt khoảng $$50\%$$ và tại $$n\approx 57$$ đạt khoảng $$99\%$$ — sớm hơn rất nhiều so với ngưỡng đảm bảo Dirichlet $$n=367$$.</p>

Trong không gian băm kích thước $$N=2^b$$, lập luận tương tự cho *ngưỡng sinh nhật (birthday bound)*: chỉ cần khoảng $$\sqrt{N}=2^{b/2}$$ mẫu là xác suất va chạm đã xấp xỉ 50%, trong khi nguyên lý Dirichlet chỉ đảm bảo chắc chắn từ $$N+1$$ mẫu trở lên.

## Ứng dụng trong Khoa học Máy tính

### Bảng băm và va chạm (Hash Tables & Collision)
```python
def hash_collision_guarantee(num_keys, table_size):
    """Đảm bảo collision trong hash table"""
    if num_keys > table_size:
        return True, f"Chắc chắn có collision (≥{math.ceil(num_keys/table_size)} keys/bucket)"
    return False, "Không đảm bảo collision"

# Ví dụ: 1000 keys, 100 buckets
# Chắc chắn có bucket chứa ≥ 10 keys
```

### Cân bằng tải (Load Balancing)
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

### Thuật toán ngẫu nhiên và tấn công sinh nhật
```python
def birthday_attack_probability(hash_bits):
    """Ước lượng ngưỡng tấn công sinh nhật trong hàm băm"""
    hash_space = 2 ** hash_bits
    # Theo nghịch lý sinh nhật (birthday bound): cần ~√(hash_space) lần thử để xác suất va chạm ~50%
    return math.sqrt(hash_space)

# SHA-256 (256 bits): cần ~2^128 lần thử để xác suất va chạm ~50% (đảm bảo chắc chắn theo Dirichlet cần 2^256 + 1)
```

![Cây quyết định — phân tích không gian trạng thái](/discrete-mathematics-for-computer-science-iuh/img/course/Decision_tree.svg)

<p class="textbook-figure-caption" data-figure="8.5">Nguyên lý chuồng chim giúp chứng minh sự tồn tại mà không cần liệt kê — rất hữu ích trong phân tích thuật toán và mật mã học.</p>

### Minh hoạ tương tác

Minh hoạ nguyên lý chuồng bồ câu: điều chỉnh số bồ câu và số chuồng để quan sát chuồng buộc phải chứa ít nhất $$\lceil n/k \rceil$$ con.

<div class="interactive-demo" markdown="1">
<div data-demo="counting-explainer" data-tab="pigeon"></div>
</div>
<script src="{{ '/public/js/explainers/counting-explainer.js' | relative_url }}"></script>

## Bài tập thực hành

### Bài tập 1: Cơ bản
1. Trong 367 người, chứng minh rằng có ít nhất 2 người sinh cùng ngày trong năm.
2. Chọn 5 điểm bất kỳ trong hình vuông cạnh 2 (kích thước 2×2). Chứng minh rằng tồn tại 2 điểm có khoảng cách không vượt quá $$\sqrt{2}$$.
3. Trong 11 số nguyên bất kỳ, chứng minh rằng có ít nhất 2 số có cùng chữ số tận cùng.

### Bài tập 2: Trung bình
1. Chứng minh rằng trong 6 người bất kỳ, luôn có 3 người đôi một quen nhau hoặc 3 người đôi một không quen nhau.
2. Trong một dãy gồm 101 số nguyên, chứng minh rằng tồn tại một đoạn con liên tiếp có tổng chia hết cho 100.
3. Chọn 51 số nguyên khác nhau từ 1 đến 100. Chứng minh rằng có ít nhất 2 số mà số này chia hết cho số kia.

### Bài tập 3: Nâng cao
1. Trong mặt phẳng có 5 điểm sao cho không có 3 điểm nào thẳng hàng. Chứng minh rằng tồn tại 4 điểm tạo thành một tứ giác lồi.
2. Cho $$2n + 1$$ số thực bất kỳ. Chứng minh rằng có thể chọn ra $$n + 1$$ số sao cho trung bình cộng của chúng lớn hơn hoặc bằng trung bình cộng của toàn bộ $$2n + 1$$ số.
3. Trong một bảng $$n \times n$$, mỗi ô ghi số 1 hoặc -1. Chứng minh rằng có 2 hàng hoặc 2 cột có tích vô hướng không âm ($$\ge 0$$).

<details>
<summary>Đáp án Bài tập 1</summary>

1. **367 người, 366 ngày** (tính cả ngày 29/2 năm nhuận): vì 367 > 366, theo nguyên lý Dirichlet chắc chắn có ít nhất 2 người sinh cùng ngày.
2. **Chia hình vuông 2×2 thành 4 ô vuông nhỏ 1×1**: có 5 điểm đặt vào 4 ô nên tồn tại ít nhất một ô chứa từ 2 điểm trở lên; khoảng cách giữa hai điểm trong cùng ô không vượt quá độ dài đường chéo $$\sqrt{2}$$.
3. **11 số nguyên, 10 chữ số tận cùng (0–9)**: vì 11 > 10, theo nguyên lý Dirichlet chắc chắn có ít nhất 2 số có cùng chữ số tận cùng.

</details>

## Các biến thể của Nguyên lý Dirichlet

### Nguyên lý Dirichlet dạng mạnh
Nếu phân bổ $$N$$ đối tượng vào $$n$$ nhóm với $$N > kn$$, thì tồn tại ít nhất một nhóm chứa nhiều hơn $$k$$ đối tượng (tức tối thiểu $$k + 1$$ đối tượng).

### Nguyên lý Dirichlet liên tục
Nếu $$N$$ đối tượng được phân bố trên một đoạn có độ dài $$L$$, thì khi chia thành $$n$$ đoạn con bằng nhau, tồn tại ít nhất một đoạn con dài $$L/n$$ chứa ít nhất $$N/n$$ đối tượng.

### Nguyên lý Dirichlet xác suất
Khi phân bổ ngẫu nhiên $$N$$ đối tượng vào $$n$$ nhóm, xác suất để mọi nhóm đều chứa không quá $$k$$ đối tượng giảm rất nhanh (theo hàm mũ) khi $$N$$ tăng lên.

## Hệ quả thường dùng trong Khoa học Máy tính

<div class="textbook-theorem" markdown="1">
**Định lý (dạng tổng quát)**: Nếu $$N$$ đối tượng được phân vào $$n$$ nhóm, thì ít nhất một nhóm chứa ít nhất $$\lceil N/n \rceil$$ đối tượng.
</div>

<div class="textbook-lemma" markdown="1">
**Hệ quả**:
- Nếu $$N > n(k-1)$$, thì ít nhất một nhóm chứa ít nhất $$k$$ đối tượng.
</div>

**Ý nghĩa trong Khoa học Máy tính**:
- **Va chạm băm (Hash collision)**: chèn $$n+1$$ khóa vào bảng băm gồm $$n$$ ngăn chứa thì chắc chắn xảy ra va chạm.
- **Cân bằng tải (Load balancing)**: phân bổ $$N$$ tác vụ lên $$n$$ máy chủ thì ít nhất một máy chủ phải nhận từ $$\lceil N/n \rceil$$ tác vụ trở lên.


## Công cụ tương tác

Đặt $$n$$ đồ vật vào $$m$$ hộp và quan sát thời điểm một hộp buộc phải chứa ít nhất hai (hoặc $$k$$) đồ vật.
<div class="interactive-demo" markdown="1">
<div data-demo="pigeonhole-visualizer"></div>
</div>
<script src="{{ '/public/js/pigeonhole-visualizer.js' | relative_url }}"></script>

## Xem thêm / Video gợi ý

- [Pigeonhole Principle — Advanced](https://www.youtube.com/watch?v=9jZ5n8k0p0Q) — 3Blue1Brown (Generalized version)

## Tóm tắt

**Nguyên lý Dirichlet** là công cụ ngắn gọn nhưng hiệu quả để chứng minh sự tồn tại:

- **Phát biểu cơ bản**: phân bổ $$N$$ đối tượng vào $$n$$ nhóm với $$N > n$$ thì ít nhất 1 nhóm chứa $$\ge 2$$ đối tượng.
- **Phát biểu tổng quát**: phân bổ $$N$$ đối tượng vào $$n$$ nhóm thì ít nhất 1 nhóm chứa $$\ge \lceil N/n \rceil$$ đối tượng.
- **Ứng dụng**: bảng băm và va chạm, cân bằng tải trong hệ thống phân tán, thuật toán ngẫu nhiên, mật mã học và chứng minh tồn tại trong tổ hợp.
- **Kỹ thuật chứng minh**: thường dùng lập luận phản chứng hoặc đếm trực tiếp.

Trong bài tiếp theo, chúng ta sẽ tìm hiểu **Ứng dụng nâng cao của Nguyên lý Dirichlet** trong lý thuyết số, hình học và khoa học máy tính.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=2-mxYrCNX60">PIGEONHOLE PRINCIPLE - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giới thiệu nguyên lý chuồng bồ câu và các phát biểu cơ bản.
- <a href="https://www.youtube.com/watch?v=B2A2pGrDG8I">What Is the Pigeonhole Principle?</a> — Spanning Tree, tiếng Anh. Xây dựng trực giác về nguyên lý trước khi đi vào các bài chứng minh.
- <a href="https://www.youtube.com/watch?v=YKsHlxnWylc">Pigeonhole Principle (1 of 2: Establishing a pattern)</a> — Eddie Woo, tiếng Anh. Cách xác định "chim" và "chuồng" qua các ví dụ đếm cơ bản.
