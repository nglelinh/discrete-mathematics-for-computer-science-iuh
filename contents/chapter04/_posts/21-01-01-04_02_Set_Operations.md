---
layout: post
title: "Phép toán Tập hợp"
categories: chapter04
date: 2021-01-01
order: 2
required: true
lang: en
---

# Phép toán Tập hợp

Có dữ liệu khách hàng VIP, dữ liệu khách đã mua hàng, dữ liệu khách đang hoạt động. Câu hỏi thực tế luôn là: ai vừa VIP **và** đã mua, ai thuộc nhóm này **hoặc** nhóm kia, ai nằm trong danh sách nhưng chưa được xử lý? Những thao tác nghe rất nghiệp vụ ấy thực ra đều là phép toán trên tập hợp.

Bài này biến các thao tác “lọc”, “gộp”, “loại trừ”, “so phần chung” thành ngôn ngữ chính xác bằng **hợp, giao, hiệu, phần bù**. Khi nắm được chúng, bạn không chỉ giải bài tập tập hợp mà còn đọc truy vấn dữ liệu tốt hơn, hiểu cách bộ lọc hoạt động và mô hình hóa các bài toán phân loại một cách gọn gàng hơn.

## Các phép toán cơ bản

### 1. Hợp (Union) -- ∪

**Định nghĩa**: A ∪ B = {x | x ∈ A hoặc x ∈ B}

Phép hợp gom tất cả phần tử thuộc ít nhất một trong hai tập. Từ "hoặc" ở đây theo nghĩa bao hàm (inclusive or): có thể thuộc A, hoặc B, hoặc cả hai.

**Ví dụ**:
- A = {1, 2, 3}, B = {3, 4, 5}
- A ∪ B = {1, 2, 3, 4, 5}

<div class="math-example">
<strong>Ví dụ thực tế</strong>: Tập hợp sinh viên học Python hoặc Java
<br>Python = {An, Bình, Chi}, Java = {Bình, Dung, Em}
<br>Python ∪ Java = {An, Bình, Chi, Dung, Em}
</div>

```python
# Hợp trong Python
Python = {"An", "Bình", "Chi"}
Java = {"Bình", "Dung", "Em"}
print(Python | Java)        # {'An', 'Bình', 'Chi', 'Dung', 'Em'}
print(Python.union(Java))   # Tương tự
```

### 2. Giao (Intersection) -- ∩

**Định nghĩa**: A ∩ B = {x | x ∈ A và x ∈ B}

Giao chỉ gồm các phần tử thuộc **đồng thời** cả hai tập.

**Ví dụ**:
- A = {1, 2, 3}, B = {3, 4, 5}
- A ∩ B = {3}

<div class="math-example">
<strong>Ví dụ thực tế</strong>: Sinh viên học cả Python và Java
<br>Python ∩ Java = {Bình}
</div>

```python
print(Python & Java)          # {'Bình'}
print(Python.intersection(Java))
```

**Tính chất**: Nếu A ∩ B = ∅, ta nói A và B **rời nhau** (disjoint).

### 3. Hiệu (Difference) -- \

**Định nghĩa**: A \ B = {x | x ∈ A và x ∉ B}

Hiệu lấy các phần tử thuộc A nhưng không thuộc B. **Không giao hoán**: A \ B ≠ B \ A (trừ khi A = B).

**Ví dụ**:
- A = {1, 2, 3}, B = {3, 4, 5}
- A \ B = {1, 2}
- B \ A = {4, 5}

```python
print(Python - Java)    # {'An', 'Chi'} -- học Python nhưng không học Java
print(Java - Python)    # {'Dung', 'Em'} -- học Java nhưng không học Python
```

### 4. Phần bù (Complement) -- Aᶜ

**Định nghĩa**: Aᶜ = U \ A = {x ∈ U | x ∉ A}
(với U là tập vũ trụ -- universal set)

Phần bù phụ thuộc vào tập vũ trụ U. Nếu thay đổi U, phần bù thay đổi theo.

**Ví dụ**:
- U = {1, 2, 3, 4, 5}, A = {1, 3, 5}
- Aᶜ = {2, 4}

<div class="content-box warning-box" markdown="1">
**Lỗi thường gặp**: Nhiều sinh viên quên mất tập vũ trụ khi nói về phần bù. Aᶜ không có ý nghĩa nếu không biết U là gì. Trong Python, "phần bù" của một set không phải là phép toán có sẵn -- bạn phải xác định U trước:
```python
U = {1, 2, 3, 4, 5}
A = {1, 3, 5}
complement = U - A
print(complement)  # {2, 4}
```
</div>

### 5. Hiệu đối xứng (Symmetric Difference) -- △

**Định nghĩa**: A △ B = (A \ B) ∪ (B \ A) = (A ∪ B) \ (A ∩ B)

Hiệu đối xứng lấy các phần tử thuộc đúng một trong hai tập (không thuộc cả hai).

**Ví dụ**:
- A = {1, 2, 3}, B = {3, 4, 5}
- A △ B = {1, 2, 4, 5}

```python
print(Python ^ Java)   # {'An', 'Chi', 'Dung', 'Em'} 
# Hoặc:
print(Python.symmetric_difference(Java))
```

## Các hằng đẳng thức tập hợp quan trọng

Giống như đại số có các hằng đẳng thức (a + b)² = a² + 2ab + b², lý thuyết tập hợp cũng có những hằng đẳng thức giúp biến đổi và đơn giản hóa biểu thức:

| Luật | Công thức |
|------|-----------|
| Giao hoán | A ∪ B = B ∪ A, A ∩ B = B ∩ A |
| Kết hợp | (A ∪ B) ∪ C = A ∪ (B ∪ C), (A ∩ B) ∩ C = A ∩ (B ∩ C) |
| Phân phối | A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C), A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) |
| De Morgan | (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ, (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ |
| Bù đôi | (Aᶜ)ᶜ = A |
| Phần tử trung hòa | A ∪ ∅ = A, A ∩ U = A |
| Phần tử nuốt | A ∪ U = U, A ∩ ∅ = ∅ |
| Lũy đẳng | A ∪ A = A, A ∩ A = A |

<div class="content-box insight-box" markdown="1">
**Luật De Morgan** là một trong những công cụ mạnh nhất để biến đổi biểu thức tập hợp. Nó cho phép "phân phối" phép bù vào trong dấu ngoặc, đồng thời đổi ∪ thành ∩ và ngược lại. Trong lập trình, De Morgan tương ứng với việc đảo ngược điều kiện logic:

```python
# (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ
not (x in A or x in B) == (x not in A) and (x not in B)

# (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
not (x in A and x in B) == (x not in A) or (x not in B)
```
</div>

## Công cụ tương tác: Trực quan hóa phép toán tập hợp

<div id="set-operations-visualizer" class="interactive-tool">
    <h4>🎨 Trực quan hóa phép toán tập hợp</h4>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin-bottom: 20px;">
        <div>
            <label><strong>Tập A:</strong></label>
            <input type="text" id="set-a-ops" placeholder="1,2,3,4" style="width: 100%; padding: 8px;">
        </div>
        <div>
            <label><strong>Tập B:</strong></label>
            <input type="text" id="set-b-ops" placeholder="3,4,5,6" style="width: 100%; padding: 8px;">
        </div>
        <div>
            <label><strong>Phép toán:</strong></label>
            <select id="operation-select" style="width: 100%; padding: 8px;">
                <option value="union">A ∪ B (Hợp)</option>
                <option value="intersection">A ∩ B (Giao)</option>
                <option value="difference">A \ B (Hiệu)</option>
                <option value="symmetric">A △ B (Hiệu đối xứng)</option>
            </select>
        </div>
    </div>
    
    <button onclick="visualizeOperation()" style="width: 100%; margin-bottom: 20px;">
        Thực hiện phép toán
    </button>
    
    <div id="operation-result" style="background: white; padding: 20px; border-radius: 8px; border: 1px solid #dee2e6;">
        <p style="color: #666; text-align: center; margin: 0;">Nhập tập hợp và chọn phép toán để xem kết quả</p>
    </div>
    
    <div id="venn-diagram" style="margin-top: 20px; text-align: center;">
        <!-- Venn diagram sẽ được tạo bằng JavaScript -->
    </div>
</div>

<script>
function visualizeOperation() {
    const setAInput = document.getElementById('set-a-ops').value.trim();
    const setBInput = document.getElementById('set-b-ops').value.trim();
    const operation = document.getElementById('operation-select').value;
    const resultDiv = document.getElementById('operation-result');
    const vennDiv = document.getElementById('venn-diagram');
    
    if (!setAInput || !setBInput) {
        resultDiv.innerHTML = '<p style="color: #dc3545; text-align: center; margin: 0;">Vui lòng nhập cả hai tập hợp!</p>';
        return;
    }
    
    try {
        const setA = new Set(setAInput.split(',').map(x => x.trim()).filter(x => x));
        const setB = new Set(setBInput.split(',').map(x => x.trim()).filter(x => x));
        
        let result = new Set();
        let operationName = '';
        let operationSymbol = '';
        
        switch(operation) {
            case 'union':
                result = new Set([...setA, ...setB]);
                operationName = 'Hợp';
                operationSymbol = '∪';
                break;
            case 'intersection':
                result = new Set([...setA].filter(x => setB.has(x)));
                operationName = 'Giao';
                operationSymbol = '∩';
                break;
            case 'difference':
                result = new Set([...setA].filter(x => !setB.has(x)));
                operationName = 'Hiệu';
                operationSymbol = '\\';
                break;
            case 'symmetric':
                const diff1 = new Set([...setA].filter(x => !setB.has(x)));
                const diff2 = new Set([...setB].filter(x => !setA.has(x)));
                result = new Set([...diff1, ...diff2]);
                operationName = 'Hiệu đối xứng';
                operationSymbol = '△';
                break;
        }
        
        resultDiv.innerHTML = `
            <div style="text-align: center;">
                <h5>Kết quả: A ${operationSymbol} B</h5>
                <p><strong>A</strong> = {${[...setA].join(', ')}}</p>
                <p><strong>B</strong> = ${[...setB].join(', ')}}</p>
                <div style="font-size: 1.2em; margin-top: 10px; padding: 10px; background: #e8f5e9; border-radius: 5px;">
                    <strong>${operationName}:</strong> ${[...result].join(', ')}}
                </div>
                <p style="margin-top: 10px; color: #666;">|Kết quả| = ${result.size}</p>
            </div>
        `;
    } catch (e) {
        resultDiv.innerHTML = '<p style="color: #dc3545;">Lỗi khi xử lý. Vui lòng kiểm tra lại dữ liệu nhập.</p>';
    }
}
</script>

## Ứng dụng trong Khoa học Máy tính

### 1. Cơ sở dữ liệu (SQL)

Các phép toán tập hợp tương ứng trực tiếp với các truy vấn SQL:

| Phép toán tập hợp | SQL | Ý nghĩa |
|-------------------|-----|---------|
| A ∪ B | `SELECT * FROM A UNION SELECT * FROM B` | Hợp |
| A ∩ B | `SELECT * FROM A INTERSECT SELECT * FROM B` | Giao |
| A \ B | `SELECT * FROM A EXCEPT SELECT * FROM B` | Hiệu |

### 2. Lọc dữ liệu trong Python

```python
# Giả sử có hai danh sách người dùng
all_users = {"user1", "user2", "user3", "user4", "user5"}
premium_users = {"user1", "user3", "user5"}

# Người dùng chưa phải premium (phần bù)
free_users = all_users - premium_users
print(free_users)  # {'user2', 'user4'}

# Người dùng đăng ký ít nhất một dịch vụ
service_a = {"user1", "user2", "user3"}
service_b = {"user3", "user4", "user5"}
at_least_one = service_a | service_b
both = service_a & service_b
exactly_one = service_a ^ service_b
```

### 3. Bloom Filter

Bloom filter là cấu trúc dữ liệu xác suất dùng để kiểm tra "một phần tử có thuộc tập hợp không". Nó là ứng dụng thông minh của phép toán tập hợp và hàm băm, tiết kiệm bộ nhớ nhưng có thể cho kết quả dương tính giả (false positive).

## Bài tập thực hành

### Bài tập 1: Tính toán cơ bản

Cho U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, A = {1, 2, 3, 4, 5}, B = {4, 5, 6, 7, 8}. Tính:

a) A ∪ B
b) A ∩ B
c) A \ B
d) B \ A
e) Aᶜ

<details>
<summary>Đáp án</summary>

a) A ∪ B = {1, 2, 3, 4, 5, 6, 7, 8}
b) A ∩ B = {4, 5}
c) A \ B = {1, 2, 3}
d) B \ A = {6, 7, 8}
e) Aᶜ = U \ A = {6, 7, 8, 9, 10}
</details>

### Bài tập 2: De Morgan

Chứng minh (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ bằng cách lấy phần tử bất kỳ.

<details>
<summary>Đáp án</summary>

Lấy x ∈ (A ∪ B)ᶜ. Khi đó x ∉ (A ∪ B), nghĩa là x ∉ A và x ∉ B. Vậy x ∈ Aᶜ và x ∈ Bᶜ, suy ra x ∈ Aᶜ ∩ Bᶜ.

Ngược lại: Lấy x ∈ Aᶜ ∩ Bᶜ. Khi đó x ∈ Aᶜ và x ∈ Bᶜ, nghĩa là x ∉ A và x ∉ B, suy ra x ∉ (A ∪ B), tức x ∈ (A ∪ B)ᶜ.

Vậy (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ. ∎
</details>

### Bài tập 3: Xác định tên

Hãy xác định phép toán tập hợp thích hợp cho mỗi tình huống:

a) Tìm sinh viên đăng ký ít nhất một trong hai môn học
b) Tìm sinh viên đăng ký cả hai môn
c) Tìm sinh viên đăng ký môn thứ nhất nhưng không đăng ký môn thứ hai
d) Tìm sinh viên đăng ký đúng một trong hai môn

<details>
<summary>Đáp án</summary>

a) Hợp (∪)
b) Giao (∩)
c) Hiệu (\)
d) Hiệu đối xứng (△)
</details>

## Tóm tắt

- **Hợp** A ∪ B: gom tất cả phần tử của cả hai tập
- **Giao** A ∩ B: phần tử chung của cả hai tập
- **Hiệu** A \ B: phần tử của A nhưng không thuộc B
- **Phần bù** Aᶜ: phần tử trong U nhưng không thuộc A
- **Hiệu đối xứng** A △ B: phần tử thuộc đúng một trong hai tập
- Các phép toán tuân theo luật: giao hoán, kết hợp, phân phối, De Morgan
- Ứng dụng thực tế: SQL queries, lọc dữ liệu, Bloom filter

Trong bài tiếp theo, chúng ta sẽ tìm hiểu về lực lượng tập hợp, tập lũy thừa, nguyên lý bao hàm -- loại trừ và khái niệm về tập vô hạn đếm được / không đếm được.
