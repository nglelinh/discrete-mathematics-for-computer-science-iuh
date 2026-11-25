---
layout: post
title: "Quy tắc Cộng và Nhân"
categories: chapter07
date: 2021-01-01
order: 1
required: true
lang: en
excerpt: "Mở đầu chương phép đếm và tổ hợp với hai nguyên tắc nền tảng: quy tắc cộng, quy tắc nhân và tích Descartes."
---


Một mật khẩu 8 ký tự gồm chữ thường và chữ số mất bao lâu để tin tặc dò vét cạn? Một bộ kiểm thử có bao nhiêu tổ hợp cấu hình cần chạy? Bạn không thể ngồi liệt kê hàng nghìn tỷ trường hợp bằng tay—nhưng chỉ với hai nguyên tắc tối giản là **Quy tắc Cộng** (chia trường hợp rời nhau) và **Quy tắc Nhân** (ghép các bước nối tiếp), bạn có thể tính chính xác kích thước của những không gian khổng lồ chỉ trong vài giây.

<div class="textbook-epigraph" markdown="1">

"Combinatorics is the art of counting without actually counting."

<span class="epigraph-attribution">— Anonymous</span>

</div>

Trong chương này, chúng ta nghiên cứu **phép đếm** và **tổ hợp** — bộ công cụ giúp tính số lượng cấu hình mà không cần liệt kê thủ công từng trường hợp. Một hệ thống có bao nhiêu cách đăng nhập, một quy tắc đặt mật khẩu tạo ra bao nhiêu khả năng, hay một thuật toán phải duyệt qua bao nhiêu cấu hình — tất cả đều là bài toán đếm. Mục 7.1 bắt đầu với hai nguyên tắc nền tảng nhất: **quy tắc cộng** và **quy tắc nhân**.

Quy tắc cộng được áp dụng khi các lựa chọn loại trừ lẫn nhau; quy tắc nhân được áp dụng khi một quá trình gồm nhiều bước thực hiện nối tiếp. Hai nguyên tắc này là nền móng cho hầu hết các kỹ thuật đếm về sau. Sai lầm trong bài toán đếm thường không đến từ công thức phức tạp, mà từ việc xác định nhầm cấu trúc bài toán: đâu là lựa chọn "hoặc" và đâu là chuỗi bước "và".

## Bản đồ kiến thức nền: Bốn nguyên lý cốt lõi của Nghệ thuật Đếm cơ bản

1. **Quy tắc Cộng (Addition Principle) — "Hoặc trường hợp này, hoặc trường hợp kia"**:
   Nếu một công việc có thể hoàn thành theo một trong $k$ phương án **đôi một rời nhau** ($A_i \cap A_j = \emptyset$), thì tổng số cách là tổng số cách của từng phương án: $|A_1 \cup \dots \cup A_k| = \sum |A_i|$.

2. **Quy tắc Nhân (Multiplication Principle) — "Làm bước 1, rồi tiếp bước 2, ..."**:
   Nếu một quy trình gồm $k$ bước nối tiếp nhau, bước thứ $i$ luôn có đúng $n_i$ lựa chọn bất kể các bước trước chọn gì, thì tổng số cách là tích $n_1 \cdot n_2 \cdots n_k$ (chính là lực lượng tích Descartes $|A_1 \times \dots \times A_k|$).

3. **Cây quyết định (Decision Tree) & Thứ tự chọn bước khó trước**:
   Khi các bước có ràng buộc ràng buộc lẫn nhau (như số chẵn không lặp chữ số), hãy luôn **chọn vị trí bị ràng buộc chặt nhất trước** (ví dụ chữ số tận cùng), hoặc vẽ nhánh cây để không bỏ sót ràng buộc phụ thuộc.

4. **Phối hợp Cộng + Nhân & Đòn bẩy Phần bù (Complement)**:
   Bài toán thực tế thường chia trường hợp lớn bằng **Quy tắc Cộng**, rồi đếm bên trong mỗi trường hợp bằng **Quy tắc Nhân**. Khi gặp cụm từ *"có ít nhất một..."*, hãy nghĩ ngay đến **đếm phần bù**: $\text{Thỏa mãn} = \text{Tổng tất cả} - \text{Không có cái nào}$.

## Mục tiêu học tập

<div class="textbook-objectives" markdown="1">

**Mục tiêu học tập.** Sau bài học này, sinh viên có thể:

- **Áp dụng** quy tắc cộng và quy tắc nhân trong các bài toán đếm cơ bản.
- **Phân tích** một bài toán đếm thành các trường hợp loại trừ lẫn nhau hoặc các bước nối tiếp độc lập.
- **Ước lượng** số cấu hình trong thiết kế thuật toán, mật mã và cơ sở dữ liệu.

**Từ khóa**: nguyên lý cộng, nguyên lý nhân, quy tắc tích, đếm cơ bản.
</div>

## Quy tắc Cộng (Addition Principle)

**Nguyên lý**: Nếu một tác vụ có thể được thực hiện theo $$m$$ cách hoặc theo $$n$$ cách (hai nhóm lựa chọn không trùng lặp nhau), thì tổng số cách thực hiện tác vụ là $$m + n$$.

<div class="textbook-definition" id="định-nghĩa-chính-thức" markdown="1">
**Định nghĩa chính thức**: Nếu $$A$$ và $$B$$ là hai tập hợp rời nhau ($$A \cap B = \emptyset$$), thì $$\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert$$.
</div>

![Phép hợp hai tập rời nhau](/discrete-mathematics-for-computer-science-iuh/img/course/Union_of_sets_A_and_B.svg)

<p class="textbook-figure-caption" data-figure="7.2">Quy tắc cộng áp dụng khi các lựa chọn loại trừ nhau — tương ứng với phép hợp của hai tập hợp rời nhau.</p>
<div class="textbook-example" markdown="1">
**Ví dụ 1 (Chọn môn học)**:
Một sinh viên có thể chọn 1 môn trong danh sách sau:
- 3 môn Toán học: Giải tích, Đại số, Hình học.
- 2 môn Tin học: Lập trình, Cấu trúc dữ liệu.

**Hỏi**: Có bao nhiêu cách chọn 1 môn học?
**Đáp án**: 3 + 2 = 5 cách.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ 2 (Đi từ A đến C)**:
Từ thành phố A đến thành phố C có thể di chuyển bằng:
- Đường bộ: 4 tuyến đường.
- Đường hàng không: 2 chuyến bay.
- Đường thủy: 1 tuyến tàu.

**Tổng số cách**: 4 + 2 + 1 = 7 cách.
</div>

## Quy tắc Nhân (Multiplication Principle)

**Nguyên lý**: Nếu một tác vụ gồm $$k$$ bước liên tiếp, trong đó bước thứ $$i$$ có $$n_i$$ cách thực hiện, thì tổng số cách thực hiện toàn bộ tác vụ là $$n_1 \times n_2 \times \cdots \times n_k$$.

![Tính số hoán vị — quy tắc nhân](/discrete-mathematics-for-computer-science-iuh/img/course/Permutation_count_calculation.svg)

<p class="textbook-figure-caption" data-figure="7.3">Quy tắc nhân đếm số cách chọn và sắp xếp tuần tự — nền tảng của chỉnh hợp và hoán vị.</p>
<div class="textbook-example" markdown="1">
**Ví dụ 3 (Tạo mật khẩu)**:
Tạo mật khẩu gồm 3 ký tự:
- Ký tự thứ nhất: 1 trong 26 chữ cái.
- Ký tự thứ hai: 1 trong 10 chữ số.
- Ký tự thứ ba: 1 trong 26 chữ cái.

**Tổng số mật khẩu**: 26 × 10 × 26 = 6.760 mật khẩu.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ 4 (Đi từ A đến C qua B)**:
- Từ A đến B: 3 cách.
- Từ B đến C: 4 cách.

**Tổng số cách đi từ A đến C qua B**: 3 × 4 = 12 cách.
</div>

## Tích Descartes (Cartesian Product)

Tích Descartes kết nối trực tiếp lý thuyết tập hợp với quy tắc nhân.

<div class="textbook-definition" id="định-nghĩa" markdown="1">
**Định nghĩa**: Tích Descartes của hai tập hợp $$A$$ và $$B$$, ký hiệu $$A \times B$$, là tập hợp tất cả các cặp có thứ tự $$(a, b)$$ với $$a \in A$$ và $$b \in B$$.

<div class="textbook-equation" markdown="1">
{% raw %}$$A \times B = \{(a,b) \mid a \in A,\; b \in B\}$${% endraw %}
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
</div>

### Công thức về lực lượng

Nếu $$\lvert A \rvert = m$$ và $$\lvert B \rvert = n$$, thì $$\lvert A \times B \rvert = m \times n$$.

![Tổ hợp — chọn không xét thứ tự](/discrete-mathematics-for-computer-science-iuh/img/course/Combination.svg)

<p class="textbook-figure-caption" data-figure="7.4">Tích Descartes mở rộng quy tắc nhân cho nhiều tập hợp — mỗi cặp có thứ tự là một phần tử của tích.</p>
Tổng quát hơn, tích Descartes của $$k$$ tập hợp $$A_1 \times A_2 \times \cdots \times A_k$$ có lực lượng:

<div class="textbook-equation" markdown="1">
{% raw %}$$\lvert A_1 \times A_2 \times \cdots \times A_k \rvert = \lvert A_1 \rvert \times \lvert A_2 \rvert \times \cdots \times \lvert A_k \rvert$${% endraw %}
<span class="textbook-equation-number" aria-hidden="true"></span>
</div>
<div class="textbook-example" markdown="1">
**Ví dụ 5 (Tích Descartes của hai tập hợp)**:

Cho $$A = \{a, b, c\}$$ và $$B = \{1, 2\}$$. Tìm $$A \times B$$.

**Giải**: $$A \times B = \{(a,1), (a,2), (b,1), (b,2), (c,1), (c,2)\}$$, gồm $$3 \times 2 = 6$$ phần tử.
</div>

<div class="textbook-example" markdown="1">
**Ví dụ 6 (Mã sinh viên)**:

Một trường đại học cấp mã sinh viên gồm 2 chữ cái in hoa (A–Z) theo sau bởi 3 chữ số (0–9). Hỏi có bao nhiêu mã khác nhau?

**Giải**: Gọi $$A$$ là tập 26 chữ cái và $$B$$ là tập 10 chữ số. Mỗi mã là một phần tử của $$A \times A \times B \times B \times B$$. Tổng số mã là 26 × 26 × 10 × 10 × 10 = 676.000.
</div>

### Mối liên hệ với quy tắc nhân

Quy tắc nhân thực chất là hệ quả trực tiếp của công thức tính lực lượng tích Descartes. Khi một tác vụ gồm $$k$$ bước nối tiếp, trong đó bước thứ $$i$$ có $$n_i$$ lựa chọn, mỗi cách hoàn thành tác vụ tương ứng với một phần tử trong tích Descartes của $$k$$ tập hợp có kích thước lần lượt là $$n_1, n_2, \ldots, n_k$$.

### Thử nghiệm: cây quy tắc cộng và nhân

Tính số cách từ các nút lá lên gốc và quan sát lý do quy tắc cộng đòi hỏi các trường hợp phải rời nhau.

<div class="interactive-demo" markdown="1">
<div data-demo="rule-explainer" data-preset="outfit"></div>
</div>
<script src="{{ '/public/js/explainers/counting-explainer.js' | relative_url }}"></script>

## Kết hợp Quy tắc Cộng và Nhân

Nhiều bài toán thực tế đòi hỏi phải phối hợp đồng thời cả hai quy tắc.

<div class="textbook-example" markdown="1">
**Ví dụ 7 (Đi du lịch)**:
Từ Hà Nội đến Đà Nẵng có thể chọn một trong hai phương án:
- **Bay trực tiếp**: 3 chuyến bay.
- **Quá cảnh qua TP.HCM**:
  - Hà Nội → TP.HCM: 4 chuyến bay.
  - TP.HCM → Đà Nẵng: 2 chuyến bay.

**Giải**:
- Đi qua TP.HCM: 4 × 2 = 8 cách (quy tắc nhân).
- Tổng cộng: 3 + 8 = 11 cách (quy tắc cộng).
</div>

<div class="textbook-example" markdown="1">
**Ví dụ 8 (Tạo tài khoản)**:
Một trang web cho phép tạo tên đăng nhập (username) theo 2 định dạng:
- **Định dạng 1**: 1 chữ cái + 3 chữ số.
- **Định dạng 2**: 2 chữ cái + 2 chữ số.

**Giải**:
- Định dạng 1: 26 × 10 × 10 × 10 = 26.000 tên đăng nhập.
- Định dạng 2: 26 × 26 × 10 × 10 = 67.600 tên đăng nhập.
- Tổng cộng: 26.000 + 67.600 = 93.600 tên đăng nhập.
</div>

### Khung giải thích (nên đọc chậm): Đếm tay mã PIN 4 chữ số bằng chia trường hợp (Cộng + Nhân) và kỹ thuật Phần bù

**Bài toán A — Có bao nhiêu số tự nhiên chẵn gồm 4 chữ số đôi một khác nhau?**
*(Chữ số đầu $d_1 \in \{1..9\}$, chữ số cuối $d_4 \in \{0, 2, 4, 6, 8\}$.)*

Vì lựa chọn $d_4 = 0$ hay $d_4 \neq 0$ làm thay đổi số cách chọn $d_1$, ta bắt buộc phải **chia 2 trường hợp rời nhau** (Quy tắc Cộng):
1. **Trường hợp 1 ($d_4 = 0$ — 1 cách)**:
   - Chọn $d_1 \in \{1..9\}$: **9 cách** (không lo trùng `0`).
   - Chọn $d_2$ (bỏ $d_4, d_1$): **8 cách**; chọn $d_3$: **7 cách**.
   - Số cách (Quy tắc Nhân): $1 \times 9 \times 8 \times 7 = \mathbf{504}$.
2. **Trường hợp 2 ($d_4 \in \{2, 4, 6, 8\}$ — 4 cách)**:
   - Chọn $d_1$: phải khác `0` và khác $d_4$ $\implies$ **8 cách**.
   - Chọn $d_2$: lúc này chữ số `0` được phép dùng trở lại, chỉ trừ $d_4$ và $d_1$ $\implies$ **8 cách**.
   - Chọn $d_3$: trừ 3 chữ số đã dùng $\implies$ **7 cách**.
   - Số cách (Quy tắc Nhân): $4 \times 8 \times 8 \times 7 = \mathbf{1{,}792}$.
3. **Tổng hợp (Quy tắc Cộng)**: $504 + 1{,}792 = \mathbf{2{,}296}$ số.

**Bài toán B — Có bao nhiêu mã PIN 4 chữ số (từ `0000` đến `9999`, được lặp) chứa ít nhất một chữ số `9`?**
Thay vì chia tới 15 trường hợp vị trí của chữ số `9`, ta dùng **Phần bù**:
- Tổng số mã PIN bất kỳ: $10^4 = \mathbf{10{,}000}$.
- Số mã PIN **không chứa chữ số `9` nào** (mỗi vị trí chọn từ 9 chữ số `{0..8}`): $9^4 = \mathbf{6{,}561}$.
- Kết quả: $10{,}000 - 6{,}561 = \mathbf{3{,}439}$ mã PIN!

## Ứng dụng trong Khoa học Máy tính

### Phân tích thuật toán
```python
def count_operations(n):
    """Đếm số phép toán trong thuật toán"""
    # Vòng lặp ngoài: n lần
    # Vòng lặp trong: n lần
    # Mỗi lần: 1 phép toán
    return n * n * 1  # Quy tắc nhân: O(n²)

def count_paths(graph, start, end):
    """Đếm số đường đi trong đồ thị"""
    # Sử dụng quy tắc cộng cho các đường đi khác nhau
    # Sử dụng quy tắc nhân cho chuỗi cạnh liên tiếp
    pass
```

### Mật mã học
```python
def password_strength(length, charset_size):
    """Tính số mật khẩu có thể tạo"""
    # Mỗi vị trí có charset_size lựa chọn
    # Tổng cộng length vị trí
    return charset_size ** length  # Quy tắc nhân

# Ví dụ: Mật khẩu 8 ký tự, bao gồm chữ và số
strength = password_strength(8, 36)  # 36^8 ≈ 2.8 × 10^12
```

### Cơ sở dữ liệu
```sql
-- Đếm số bản ghi có thể tạo từ các bảng
-- Sử dụng quy tắc nhân cho JOIN
SELECT COUNT(*) FROM 
    (SELECT COUNT(*) as users FROM Users) u,
    (SELECT COUNT(*) as orders FROM Orders) o;
```

## Bài tập thực hành

### Bài tập 1: Quy tắc Cộng
1. Một sinh viên có thể chọn 1 trong 5 môn Toán, 1 trong 3 môn Lý, hoặc 1 trong 4 môn Hóa. Hỏi có bao nhiêu cách chọn?

2. Từ thành phố A đến thành phố B có 3 tuyến đường bộ, 2 tuyến đường sắt và 1 đường hàng không. Có bao nhiêu cách di chuyển?

### Bài tập 2: Quy tắc Nhân
1. Tạo mã số gồm 2 chữ cái đứng đầu và 3 chữ số đứng cuối. Có bao nhiêu mã số khác nhau?

2. Một bữa ăn gồm 1 món khai vị (4 lựa chọn), 1 món chính (6 lựa chọn) và 1 món tráng miệng (3 lựa chọn). Có bao nhiêu cách chọn thực đơn?

### Bài tập 3: Kết hợp
1. Từ A đến C có thể đi trực tiếp (2 cách) hoặc đi qua B (từ A đến B có 3 cách, từ B đến C có 4 cách). Tổng cộng có bao nhiêu cách đi?

2. Tạo mật khẩu theo 2 định dạng:
   - Định dạng 1: 3 chữ cái + 2 chữ số.
   - Định dạng 2: 2 chữ số + 3 chữ cái.

   Có bao nhiêu mật khẩu khác nhau?

<details>
<summary>Đáp án</summary>

**Bài tập 1:**
1. 5 + 3 + 4 = 12 cách.
2. 3 + 2 + 1 = 6 cách.

**Bài tập 2:**
1. 26 × 26 × 10 × 10 × 10 = 676.000 mã số.
2. 4 × 6 × 3 = 72 cách.

**Bài tập 3:**
1. 2 + (3 × 4) = 2 + 12 = 14 cách.
2. (26³ × 10²) + (10² × 26³) = 1.757.600 + 1.757.600 = 3.515.200 mật khẩu.

</details>

---

## Xem thêm / Video gợi ý

- <a href="https://www.youtube.com/watch?v=FMc7pZbvWKA">Logical Equivalences | Prepositional Logic | Discrete Mathematics</a> — NotesForMsc (Truth table proof + laws)
- [Discrete Math Full Course — Logic & Proofs](https://www.youtube.com/playlist?list=PLHXZ9OQGMqxersk8fUxiUMSIx0DBqsKZS) — Trefor Bazett (Complete semester playlist)

## Tóm tắt

- **Quy tắc cộng**: nếu tác vụ có thể thực hiện theo $$m$$ cách hoặc $$n$$ cách (loại trừ lẫn nhau), tổng số cách là $$m + n$$; tương ứng $$\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert$$ khi $$A \cap B = \emptyset$$.
- **Quy tắc nhân**: nếu tác vụ gồm $$k$$ bước nối tiếp với bước thứ $$i$$ có $$n_i$$ cách, tổng số cách là $$n_1 \times n_2 \times \cdots \times n_k$$.
- **Phân biệt cấu trúc**: quan hệ "hoặc" gợi ý quy tắc cộng; quan hệ "và" (các bước tuần tự) gợi ý quy tắc nhân.
- **Ứng dụng trong Khoa học Máy tính**: ước lượng không gian mật khẩu, số đường đi, cấu hình hệ thống và không gian tìm kiếm.

Trong bài tiếp theo, chúng ta sẽ học về hoán vị và tổ hợp.

## Video tham khảo

- **Nên xem trước:** <a href="https://www.youtube.com/watch?v=8JiWWvEoaoc">RULE of SUM and RULE of PRODUCT - DISCRETE MATHEMATICS</a> — TrevTutor, tiếng Anh. Giới thiệu trực quan quy tắc cộng và quy tắc nhân.
- <a href="https://www.youtube.com/watch?v=t0us-MXrFZg">[Discrete Mathematics] Rule of Sum and Rule of Product Examples</a> — TrevTutor, tiếng Anh. Bài tập rèn luyện cách phân biệt khi nào cộng và khi nào nhân.
- <a href="https://www.youtube.com/watch?v=gLfpNYg9Hyk">The summation rule for disjoint unions</a> — Dr. Trefor Bazett, tiếng Anh. Trình bày quy tắc cộng dưới góc nhìn hợp các tập rời nhau.
