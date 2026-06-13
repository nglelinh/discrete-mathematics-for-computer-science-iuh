---
layout: post
title: "Giới thiệu Tập hợp"
categories: chapter04
date: 2021-01-01
order: 1
required: true
lang: en
---

# Giới thiệu Tập hợp

Khi viết truy vấn SQL, lọc người dùng theo vai trò, gom các node đã thăm trong thuật toán, hay mô tả tập ký tự hợp lệ của một bộ phân tích cú pháp, ta đang làm việc với cùng một ý tưởng rất nền tảng: **tập hợp**.


Tư duy tập hợp giúp ta mô tả dữ liệu, miền giá trị và ràng buộc một cách chính xác, nên phần này là nền cho cả lập trình lẫn mô hình hóa.
Tập hợp cho phép ta nói chính xác cái gì thuộc về một nhóm và cái gì không. Nghe đơn giản, nhưng đây là ngôn ngữ đứng phía sau dữ liệu, quan hệ, hàm số, xác suất, đồ thị và rất nhiều mô hình mà khoa học máy tính dùng hằng ngày.

Nếu thiếu tư duy tập hợp, nhiều phát biểu kỹ thuật sẽ trở nên mơ hồ. Hai điều kiện tưởng giống nhau có thể khác hoàn toàn chỉ vì miền phần tử khác nhau. Một lỗi nhỏ trong cách mô tả tập đầu vào cũng có thể kéo theo sai lệch trong thiết kế thuật toán hay chứng minh.

Trong bài này, chúng ta sẽ xây nền từ khái niệm phần tử, cách ký hiệu tập hợp, đến những kiểu tập quen thuộc mà bạn sẽ gặp xuyên suốt phần còn lại của môn học.

## Mục tiêu học tập

Hãy đọc mục tiêu như danh sách năng lực cần đạt sau bài, vì chúng cho biết bạn nên hiểu gì, làm được gì và áp dụng vào đâu.

Sau bài học này, sinh viên có thể:

- **Định nghĩa** được khái niệm tập hợp và các phần tử.
- **Sử dụng** thành thạo các ký hiệu: $$\in$$, $$\notin$$, $$\subseteq$$, $$\emptyset$$.
- **Biểu diễn** tập hợp bằng ba cách: liệt kê, mô tả tính chất, và khoảng số.
- **Phân biệt** các tập hợp số quan trọng: $$\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$$.
- **Xác định** quan hệ tập con, tập hợp bằng nhau, và lực lượng tập hợp.
- **Áp dụng** khái niệm tập hợp trong lập trình Python.

## Định nghĩa Tập hợp

Phần này đặt lại ngôn ngữ chung của bài học. Nắm chắc định nghĩa trước sẽ giúp các ví dụ và định lý phía sau trở nên dễ theo dõi hơn.

**Định nghĩa**: Tập hợp là một bộ sưu tập các đối tượng riêng biệt, được gọi là các **phần tử** hay **thành phần** của tập hợp.

> Cantor đã định nghĩa tập hợp một cách trực quan: "Một tập hợp là sự kết hợp thành một tổng thể của những đối tượng xác định, phân biệt của trực giác hay tư duy của chúng ta."

### Ký hiệu:
- Tập hợp: A, B, C, ... (chữ cái in hoa)
- Phần tử: a, b, c, ... (chữ cái thường)
- Quan hệ thuộc: a ∈ A (a thuộc A)
- Quan hệ không thuộc: a ∉ A (a không thuộc A)

#### Minh họa trực quan: ∈ vs ⊆

**Quy tắc nhanh**:
- $$\in$$: "là phần tử của" → dùng với **phần tử**
- $$\subseteq$$: "là tập con của" → dùng với **tập hợp**

**Bảng so sánh**:

| Biểu thức | Đúng/Sai | Lý do |
|:---:|:---:|:---|
| $$1 \in \{1,2\}$$ | Đúng | 1 là phần tử |
| $$1 \subseteq \{1,2\}$$ | Sai | 1 không phải tập hợp |
| $$\{1\} \subseteq \{1,2\}$$ | Đúng | {1} là tập con |
| $$\{1,2\} \in \{1,2\}$$ | Sai | {1,2} không phải phần tử |

**Mẹo nhớ**: 
- $$\in$$ = "thuộc về" (phần tử)
- $$\subseteq$$ = "bên trong" (tập hợp)

## Cách biểu diễn tập hợp

### 1. Liệt kê (Roster Method)

Liệt kê tất cả các phần tử trong dấu ngoặc nhọn. Đây là cách trực quan nhất, phù hợp với tập có ít phần tử.

**Ví dụ**:
- A = {1, 2, 3, 4, 5}
- B = {a, e, i, o, u} (các nguyên âm)
- C = {đỏ, xanh, vàng}

### 2. Mô tả tính chất (Set-Builder Notation)

Mô tả tập hợp bằng tính chất của các phần tử. Cách này hữu ích khi tập có quá nhiều phần tử hoặc vô hạn.

**Cú pháp**: {x | P(x)} hoặc {x : P(x)}
Đọc: "Tập hợp các x sao cho P(x)"

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter04/venn-set-representation.svg" alt="Minh họa ba cách biểu diễn tập hợp" width="70%" height="70%">
  <figcaption style="text-align: center;">Hình 4.1: Ba cách biểu diễn tập hợp: liệt kê (trái), mô tả tính chất (giữa), và biểu đồ Venn (phải)</figcaption>
</p>
</figure>

**Ví dụ**:
- A = {x | x là số nguyên và 1 ≤ x ≤ 5}
- B = {x | x^2 = 4}
- C = {n ∈ ℕ | n là số chẵn}

### 3. Sử dụng khoảng (cho số thực)

**Ví dụ**:
- [0, 1] = {x ∈ ℝ | 0 ≤ x ≤ 1}
- (0, 1) = {x ∈ ℝ | 0 < x < 1}
- [0, ∞) = {x ∈ ℝ | x ≥ 0}

<div class="content-box note-box" markdown="1">
**Lưu ý**: Dấu ngoặc vuông `[ ]` nghĩa là "bao gồm điểm đầu/cuối", dấu ngoặc tròn `( )` nghĩa là "không bao gồm". Trong Python, `range(1, 5)` cho {1, 2, 3, 4} -- tương tự nửa khoảng $$[1, 5)$$.
</div>

## Các tập hợp số quan trọng

Trong toán rời rạc, chúng ta thường xuyên làm việc với các tập hợp số sau:

| Ký hiệu | Tên | Định nghĩa | Ghi chú |
|---------|-----|------------|---------|
| ℕ | Số tự nhiên | {1, 2, 3, 4, ...} | Có tài liệu lấy ℕ = {0, 1, 2, ...} |
| ℕ₀ | Số tự nhiên và 0 | {0, 1, 2, 3, ...} | Rõ ràng hơn |
| ℤ | Số nguyên | {..., -2, -1, 0, 1, 2, ...} | |
| ℚ | Số hữu tỷ | {p/q | p, q ∈ ℤ, q ≠ 0} | Số thập phân vô hạn tuần hoàn |
| ℝ | Số thực | Tất cả số thực | Gồm hữu tỷ + vô tỷ |
| ℂ | Số phức | {a + bi | a, b ∈ ℝ} | i² = -1 |

<div class="content-box insight-box" markdown="1">
**Bao hàm** (inclusion): Các tập hợp số lồng nhau:
$$\mathbb{N} \subset \mathbb{N}_0 \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$$

Minh họa: Mọi số tự nhiên đều là số nguyên, mọi số nguyên đều là số hữu tỷ, v.v.
</div>

## Khái niệm cơ bản

### 1. Tập hợp rỗng (Empty Set)

**Định nghĩa**: Tập hợp không chứa phần tử nào.
**Ký hiệu**: ∅ hoặc {}

> Một câu chuyện vui trong toán học: Khi được hỏi "Tập hợp rỗng có gì đặc biệt?", một sinh viên trả lời: "Nó chứa tất cả những thứ không tồn tại!"

**Ví dụ**:
- {x ∈ ℝ | x² = -1} = ∅
- {x ∈ ℕ | x < 0} = ∅

<div class="content-box warning-box" markdown="1">
**Lỗi thường gặp**: ∅ ≠ {∅}. Tập rỗng không chứa gì cả. Nhưng {∅} là tập hợp **chứa** tập rỗng, nên nó có một phần tử! Đây là một trong những điểm tinh tế hay gây nhầm lẫn nhất.
- |∅| = 0 (tập rỗng không có phần tử)
- |{∅}| = 1 (tập chứa tập rỗng có một phần tử)
</div>

### 2. Tập hợp con (Subset)

**Định nghĩa**: A ⊆ B nếu mọi phần tử của A đều thuộc B.

**Ký hiệu**:
- A ⊆ B: A là tập con của B
- A ⊂ B: A là tập con thực sự của B (A ⊆ B và A ≠ B)

**Tính chất**:
- ∅ ⊆ A với mọi tập hợp A
- A ⊆ A với mọi tập hợp A
- Nếu A ⊆ B và B ⊆ C thì A ⊆ C (bắc cầu)

<div class="content-box example-box" markdown="1">
**Ví dụ trực quan**: Cho A = {a, b}, hãy liệt kê tất cả tập con của A.

Các tập con: ∅, {a}, {b}, {a, b}. Có tất cả 4 tập con.

Trong Python:
```python
A = {'a', 'b'}
# Có thể kiểm tra:
print({'a'}.issubset(A))  # True
print({'c'}.issubset(A))  # False
```
</div>

### 3. Tập hợp bằng nhau

**Định nghĩa**: A = B nếu A ⊆ B và B ⊆ A.

Đây là cách chứng minh hai tập hợp bằng nhau phổ biến nhất: chứng minh tập này là con của tập kia và ngược lại.

### 4. Lực lượng (Cardinality)

**Định nghĩa**: Số phần tử của tập hợp A, ký hiệu |A| hoặc #A.

**Ví dụ**:
- |{1, 2, 3}| = 3
- |∅| = 0
- |ℕ| = ∞ (vô hạn đếm được -- sẽ học chi tiết ở bài 4.3)

<div class="content-box insight-box" markdown="1">
**Lực lượng trong CS**: Khi bạn gọi `len(set([1, 2, 3]))` trong Python, kết quả 3 chính là lực lượng của tập hợp đó. Trong cơ sở dữ liệu, `SELECT COUNT(*) FROM table` cũng là tính lực lượng.
</div>

## Công cụ tương tác: Trình khám phá tập hợp

Nếu dùng công cụ này, hãy dự đoán kết quả trước rồi mới thao tác. Việc so sánh dự đoán với kết quả thật sẽ giúp khái niệm bám chắc hơn.

<div id="set-explorer" style="border: 2px solid #6f42c1; padding: 20px; margin: 20px 0; border-radius: 8px;">
    <h4>🔍 Công cụ khám phá tập hợp</h4>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 15px;">
        <div>
            <label><strong>Tập hợp A:</strong></label>
            <input type="text" id="set-a" placeholder="Ví dụ: 1,2,3,4" style="width: 100%; padding: 8px; margin-top: 5px;">
        </div>
        <div>
            <label><strong>Tập hợp B:</strong></label>
            <input type="text" id="set-b" placeholder="Ví dụ: 3,4,5,6" style="width: 100%; padding: 8px; margin-top: 5px;">
        </div>
    </div>
    
    <div style="text-align: center; margin: 15px 0;">
        <button onclick="analyzeSet()" style="background: #6f42c1; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">
            Phân tích tập hợp
        </button>
    </div>
    
    <div id="set-analysis" style="background: #f8f9fa; padding: 15px; border-radius: 5px; min-height: 100px;">
        <p style="color: #666; font-style: italic;">Nhập các tập hợp và nhấn "Phân tích tập hợp" để xem kết quả</p>
    </div>
</div>

<script>
function analyzeSet() {
    const setAInput = document.getElementById('set-a').value.trim();
    const setBInput = document.getElementById('set-b').value.trim();
    const analysisDiv = document.getElementById('set-analysis');
    
    if (!setAInput || !setBInput) {
        analysisDiv.innerHTML = '<p style="color: #dc3545;">Vui lòng nhập cả hai tập hợp!</p>';
        return;
    }
    
    try {
        // Parse sets
        const setA = new Set(setAInput.split(',').map(x => x.trim()).filter(x => x));
        const setB = new Set(setBInput.split(',').map(x => x.trim()).filter(x => x));
        
        // Calculate properties
        const cardinalityA = setA.size;
        const cardinalityB = setB.size;
        
        // Check subset relationships
        const aSubsetB = [...setA].every(x => setB.has(x));
        const bSubsetA = [...setB].every(x => setA.has(x));
        const equal = aSubsetB && bSubsetA;
        
        // Find intersection and union
        const intersection = new Set([...setA].filter(x => setB.has(x)));
        const union = new Set([...setA, ...setB]);
        
        let result = `
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                <div>
                    <h5>`;
        
        if (equal) {
            result += `A = B (Hai tập bằng nhau)`;
        } else if (aSubsetB) {
            result += `A ⊆ B (A là tập con của B)`;
        } else if (bSubsetA) {
            result += `B ⊆ A (B là tập con của A)`;
        } else {
            result += `A và B không có quan hệ bao hàm`;
        }
        
        result += `</h5>
                    <p><strong>Tập A</strong>: ${[...setA].join(', ')}}</p>
                    <p><strong>Tập B</strong>: ${[...setB].join(', ')}}</p>
                    <p><strong>|A|</strong> = ${cardinalityA}</p>
                    <p><strong>|B|</strong> = ${cardinalityB}</p>
                    <p><strong>Giao</strong> A ∩ B = ${[...intersection].join(', ')}}</p>
                    <p><strong>Hợp</strong> A ∪ B = ${[...union].join(', ')}}</p>
                </div>
            </div>`;
        
        analysisDiv.innerHTML = result;
    } catch (e) {
        analysisDiv.innerHTML = `<p style="color: #dc3545;">Lỗi: ${e.message}</p>`;
    }
}
</script>

## Bài tập thực hành

### Bài tập 1: Nhận diện phần tử

Cho A = {1, 3, 5, 7, 9}. Xác định tính đúng sai của các khẳng định sau:

a) 3 ∈ A
b) 2 ∈ A
c) 6 ∉ A
d) ∅ ∈ A

<details>
<summary>Đáp án</summary>

a) ✅ Đúng. 3 có trong tập A.
b) ❌ Sai. 2 không có trong tập A.
c) ✅ Đúng. 6 không thuộc A.
d) ❌ Sai. ∅ (tập rỗng) không phải là phần tử của A. Các phần tử của A đều là số, không phải tập hợp.
</details>

### Bài tập 2: Biểu diễn tập hợp

Viết tập hợp sau dưới dạng liệt kê và dạng mô tả tính chất:

a) Tập các số tự nhiên chẵn nhỏ hơn 10
b) Tập các ước số của 12

<details>
<summary>Đáp án</summary>

a) Liệt kê: {0, 2, 4, 6, 8}
   Mô tả: A = {n ∈ ℕ₀ | n là số chẵn và n < 10} hoặc A = {2k | k ∈ ℕ₀, 2k < 10}

b) Liệt kê: {1, 2, 3, 4, 6, 12}
   Mô tả: B = {n ∈ ℕ | n chia hết 12}
</details>

### Bài tập 3: Quan hệ tập con

Cho A = {1, 2, 3, 4}. Tìm tất cả tập con của A có đúng 2 phần tử.

<details>
<summary>Đáp án</summary>

Có 6 tập con: {1,2}, {1,3}, {1,4}, {2,3}, {2,4}, {3,4}.

Công thức: Với tập có |A| = n, số tập con có đúng k phần tử là C(n,k) = n!/(k!(n-k)!).
Ở đây: C(4,2) = 4!/(2!2!) = 6.
</details>

### Bài tập 4: Lập trình

Viết hàm Python `is_subset(A, B)` kiểm tra A có phải tập con của B không.

<details>
<summary>Đáp án</summary>

```python
def is_subset(A, B):
    """Kiểm tra A có phải tập con của B không"""
    for element in A:
        if element not in B:
            return False
    return True

# Kiểm tra
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print(is_subset(A, B))  # True

# Cách ngắn hơn:
print(A.issubset(B))  # True
```
</details>

## Định lý: Số tập con của một tập hữu hạn

**Định lý**: Một tập hợp hữu hạn \( A \) có đúng \( 2^{|A|} \) tập con (bao gồm cả ∅ và \( A \)).

**Chứng minh**:

Giả sử \( A = \{a_1, a_2, \dots, a_n\} \), \( |A| = n \).

1. Mỗi tập con \( B \subseteq A \) được xác định bởi việc chọn hoặc không chọn từng phần tử \( a_i \).

2. Với mỗi \( a_i \), có đúng 2 lựa chọn:
   - \( a_i \in B \)
   - \( a_i \notin B \)

3. Do đó, tổng số tập con là:
   $$
   2 \times 2 \times \cdots \times 2 \quad (n \text{ lần}) = 2^n.
   $$

**Hệ quả**:
- \( |A| = 0 \) (tập rỗng): có \( 2^0 = 1 \) tập con (chính nó).
- \( |A| = 1 \): có 2 tập con.
- \( |A| = 10 \): có \( 2^{10} = 1024 \) tập con.
- \( |A| = 20 \): đã có hơn 1 triệu tập con.

**Ý nghĩa trong Khoa học Máy tính**:
- **Không gian trạng thái** của một hệ thống \( n \) bit có \( 2^n \) trạng thái.
- **Tập con** xuất hiện trong thiết kế thuật toán (subset sum, knapsack), database (power set indexing), và AI (feature selection).

## Tóm tắt

- **Tập hợp** là khái niệm nền tảng của toán học, gồm các phần tử riêng biệt
- Ba cách biểu diễn: **liệt kê**, **mô tả tính chất**, **khoảng số**
- **Tập rỗng** ∅: tập không có phần tử nào
- **Tập con** A ⊆ B: mọi phần tử của A đều thuộc B
- **Lực lượng** |A|: số phần tử của tập hữu hạn A
- Các tập hợp số: ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ

Trong bài tiếp theo, chúng ta sẽ tìm hiểu các phép toán trên tập hợp: hợp, giao, hiệu, phần bù và hiệu đối xứng -- những công cụ mạnh mẽ để kết hợp và biến đổi các tập hợp.
