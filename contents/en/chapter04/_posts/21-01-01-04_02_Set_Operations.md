---
layout: post
title: "Phép toán Tập hợp"
categories: chapter04
date: 2021-01-01
order: 2
required: true
lang: vi
---

# Phép toán Tập hợp

Các phép toán tập hợp cho phép chúng ta kết hợp, so sánh và biến đổi các tập hợp để tạo ra các tập hợp mới. Đây là công cụ mạnh mẽ trong toán học và khoa học máy tính.

## Các phép toán cơ bản

### 1. Hợp (Union) - ∪

**Định nghĩa**: A ∪ B = {x | x ∈ A hoặc x ∈ B}

**Ví dụ**:
- A = {1, 2, 3}, B = {3, 4, 5}
- A ∪ B = {1, 2, 3, 4, 5}

<div class="math-example">
<strong>Ví dụ thực tế</strong>: Tập hợp sinh viên học Python hoặc Java
<br>Python = {An, Bình, Chi}, Java = {Bình, Dung, Em}
<br>Python ∪ Java = {An, Bình, Chi, Dung, Em}
</div>

### 2. Giao (Intersection) - ∩

**Định nghĩa**: A ∩ B = {x | x ∈ A và x ∈ B}

**Ví dụ**:
- A = {1, 2, 3}, B = {3, 4, 5}
- A ∩ B = {3}

<div class="math-example">
<strong>Ví dụ thực tế</strong>: Sinh viên học cả Python và Java
<br>Python ∩ Java = {Bình}
</div>

### 3. Hiệu (Difference) - \

**Định nghĩa**: A \ B = {x | x ∈ A và x ∉ B}

**Ví dụ**:
- A = {1, 2, 3}, B = {3, 4, 5}
- A \ B = {1, 2}
- B \ A = {4, 5}

### 4. Phần bù (Complement) - Aᶜ

**Định nghĩa**: Aᶜ = U \ A = {x ∈ U | x ∉ A}
(với U là tập vũ trụ)

**Ví dụ**:
- U = {1, 2, 3, 4, 5}, A = {1, 3, 5}
- Aᶜ = {2, 4}

### 5. Hiệu đối xứng (Symmetric Difference) - △

**Định nghĩa**: A △ B = (A \ B) ∪ (B \ A) = (A ∪ B) \ (A ∩ B)

**Ví dụ**:
- A = {1, 2, 3}, B = {3, 4, 5}
- A △ B = {1, 2, 4, 5}

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
                <h5 style="color: #495057; margin-bottom: 15px;">Kết quả phép toán ${operationName}</h5>
                <div style="font-size: 1.1em; margin-bottom: 15px;">
                    <strong>A = {${[...setA].join(', ')}}</strong><br>
                    <strong>B = {${[...setB].join(', ')}}</strong>
                </div>
                <div style="font-size: 1.3em; color: #007bff; font-weight: bold; padding: 15px; background: #f8fbff; border-radius: 6px; border: 2px solid #007bff;">
                    A ${operationSymbol} B = {${[...result].join(', ') || '∅'}}
                </div>
                <div style="margin-top: 15px; font-size: 0.9em; color: #666;">
                    Số phần tử: |A ${operationSymbol} B| = ${result.size}
                </div>
            </div>
        `;
        
        // Tạo Venn diagram đơn giản
        createSimpleVennDiagram(setA, setB, result, operation, vennDiv);
        
    } catch (error) {
        resultDiv.innerHTML = '<p style="color: #dc3545; text-align: center; margin: 0;">Lỗi: Định dạng tập hợp không hợp lệ</p>';
    }
}

function createSimpleVennDiagram(setA, setB, result, operation, container) {
    const intersection = new Set([...setA].filter(x => setB.has(x)));
    const onlyA = new Set([...setA].filter(x => !setB.has(x)));
    const onlyB = new Set([...setB].filter(x => !setA.has(x)));
    
    let highlightClass = '';
    switch(operation) {
        case 'union': highlightClass = 'highlight-union'; break;
        case 'intersection': highlightClass = 'highlight-intersection'; break;
        case 'difference': highlightClass = 'highlight-difference-a'; break;
        case 'symmetric': highlightClass = 'highlight-symmetric'; break;
    }
    
    container.innerHTML = `
        <div style="position: relative; width: 300px; height: 200px; margin: 20px auto; background: #f8f9fa; border-radius: 8px; border: 1px solid #dee2e6;">
            <div style="position: absolute; top: 20px; left: 20px; font-weight: bold; color: #495057;">Biểu đồ Venn</div>
            
            <!-- Circle A -->
            <div style="position: absolute; top: 60px; left: 80px; width: 100px; height: 100px; border: 3px solid #007bff; border-radius: 50%; background: ${operation === 'union' || operation === 'difference' || operation === 'symmetric' ? 'rgba(0,123,255,0.2)' : 'rgba(0,123,255,0.1)'};">
                <div style="position: absolute; top: -25px; left: 10px; font-weight: bold; color: #007bff;">A</div>
            </div>
            
            <!-- Circle B -->
            <div style="position: absolute; top: 60px; left: 120px; width: 100px; height: 100px; border: 3px solid #28a745; border-radius: 50%; background: ${operation === 'union' || operation === 'symmetric' ? 'rgba(40,167,69,0.2)' : 'rgba(40,167,69,0.1)'};">
                <div style="position: absolute; top: -25px; right: 10px; font-weight: bold; color: #28a745;">B</div>
            </div>
            
            <!-- Intersection highlight -->
            ${operation === 'intersection' ? 
                '<div style="position: absolute; top: 85px; left: 145px; width: 50px; height: 50px; background: rgba(255,193,7,0.6); border-radius: 50%;"></div>' : 
                ''}
            
            <!-- Labels -->
            <div style="position: absolute; bottom: 20px; left: 20px; font-size: 0.8em; color: #666;">
                Chỉ A: {${[...onlyA].join(', ') || '∅'}}<br>
                Giao: {${[...intersection].join(', ') || '∅'}}<br>
                Chỉ B: {${[...onlyB].join(', ') || '∅'}}
            </div>
        </div>
    `;
}
</script>

## Tính chất của phép toán tập hợp

### 1. Tính chất giao hoán
- A ∪ B = B ∪ A
- A ∩ B = B ∩ A

### 2. Tính chất kết hợp
- (A ∪ B) ∪ C = A ∪ (B ∪ C)
- (A ∩ B) ∩ C = A ∩ (B ∩ C)

### 3. Tính chất phân phối
- A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)
- A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)

### 4. Định luật De Morgan
- (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ
- (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ

### 5. Tính chất với tập rỗng và tập vũ trụ
- A ∪ ∅ = A
- A ∩ ∅ = ∅
- A ∪ U = U
- A ∩ U = A

## Nguyên lý bao hàm-loại trừ

**Công thức**: |A ∪ B| = |A| + |B| - |A ∩ B|

**Mở rộng cho 3 tập hợp**:
|A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |A ∩ C| - |B ∩ C| + |A ∩ B ∩ C|

<div class="math-example">
<strong>Ví dụ</strong>: Trong lớp 40 sinh viên:
<ul>
<li>25 sinh viên học Python</li>
<li>20 sinh viên học Java</li>
<li>10 sinh viên học cả hai</li>
</ul>

<strong>Giải</strong>:
<ul>
<li>Học ít nhất một ngôn ngữ: |P ∪ J| = 25 + 20 - 10 = 35</li>
<li>Chỉ học Python: |P \ J| = 25 - 10 = 15</li>
<li>Chỉ học Java: |J \ P| = 20 - 10 = 10</li>
<li>Không học ngôn ngữ nào: 40 - 35 = 5</li>
</ul>
</div>

## Ứng dụng trong khoa học máy tính

### 1. Cơ sở dữ liệu (SQL)
```sql
-- Hợp (UNION)
SELECT student_id FROM python_students
UNION
SELECT student_id FROM java_students;

-- Giao (INTERSECT)
SELECT student_id FROM python_students
INTERSECT
SELECT student_id FROM java_students;

-- Hiệu (EXCEPT)
SELECT student_id FROM python_students
EXCEPT
SELECT student_id FROM java_students;
```

### 2. Lập trình Python
```python
# Các phép toán tập hợp trong Python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Hợp
union = A | B  # hoặc A.union(B)
print(union)   # {1, 2, 3, 4, 5, 6}

# Giao
intersection = A & B  # hoặc A.intersection(B)
print(intersection)   # {3, 4}

# Hiệu
difference = A - B  # hoặc A.difference(B)
print(difference)   # {1, 2}

# Hiệu đối xứng
symmetric_diff = A ^ B  # hoặc A.symmetric_difference(B)
print(symmetric_diff)   # {1, 2, 5, 6}
```

### 3. Thuật toán tìm kiếm
```python
def find_common_interests(user1_interests, user2_interests):
    """Tìm sở thích chung giữa hai người dùng"""
    return list(set(user1_interests) & set(user2_interests))

def recommend_new_interests(user_interests, popular_interests):
    """Gợi ý sở thích mới"""
    return list(set(popular_interests) - set(user_interests))
```

## Bài tập thực hành

### Bài tập 1: Tính toán cơ bản
Cho A = {1, 2, 3, 4, 5}, B = {4, 5, 6, 7}, C = {5, 6, 7, 8, 9}. Tính:

1. A ∪ B ∪ C
2. A ∩ B ∩ C
3. (A ∪ B) \ C
4. A △ B
5. |A ∪ B ∪ C|

### Bài tập 2: Chứng minh tính chất
Chứng minh các tính chất sau:

1. A \ B = A ∩ Bᶜ
2. A △ B = (A ∪ B) \ (A ∩ B)
3. (A \ B) ∪ (B \ A) = (A ∪ B) \ (A ∩ B)

### Bài tập 3: Ứng dụng thực tế
Một công ty có 100 nhân viên:
- 60 người biết tiếng Anh
- 40 người biết tiếng Nhật  
- 25 người biết cả hai thứ tiếng
- 15 người không biết ngôn ngữ nào

Hỏi:
1. Có bao nhiêu người chỉ biết tiếng Anh?
2. Có bao nhiêu người chỉ biết tiếng Nhật?
3. Dữ liệu có nhất quán không?

<details>
<summary>Đáp án Bài tập 1</summary>

1. A ∪ B ∪ C = {1, 2, 3, 4, 5, 6, 7, 8, 9}
2. A ∩ B ∩ C = {5}
3. (A ∪ B) \ C = {1, 2, 3, 4}
4. A △ B = {1, 2, 3, 6, 7}
5. |A ∪ B ∪ C| = 9

</details>

<details>
<summary>Đáp án Bài tập 3</summary>

1. Chỉ tiếng Anh: 60 - 25 = 35 người
2. Chỉ tiếng Nhật: 40 - 25 = 15 người
3. Tổng: 35 + 25 + 15 + 15 = 90 ≠ 100. Dữ liệu không nhất quán!

</details>

## Biểu đồ Venn

Biểu đồ Venn là công cụ trực quan để biểu diễn các phép toán tập hợp:

<div class="venn-diagram">
    <svg width="400" height="250" style="background: white; border-radius: 8px;">
        <!-- Circle A -->
        <circle cx="150" cy="125" r="80" fill="rgba(0,123,255,0.3)" stroke="#007bff" stroke-width="2"/>
        <text x="120" y="80" fill="#007bff" font-weight="bold" font-size="16">A</text>
        
        <!-- Circle B -->
        <circle cx="250" cy="125" r="80" fill="rgba(40,167,69,0.3)" stroke="#28a745" stroke-width="2"/>
        <text x="280" y="80" fill="#28a745" font-weight="bold" font-size="16">B</text>
        
        <!-- Labels -->
        <text x="120" y="140" text-anchor="middle" font-size="12">Chỉ A</text>
        <text x="200" y="140" text-anchor="middle" font-size="12">A ∩ B</text>
        <text x="280" y="140" text-anchor="middle" font-size="12">Chỉ B</text>
        
        <!-- Universe -->
        <rect x="20" y="20" width="360" height="210" fill="none" stroke="#666" stroke-width="1"/>
        <text x="30" y="35" fill="#666" font-size="12">U (Tập vũ trụ)</text>
    </svg>
</div>

## Tóm tắt

**Các phép toán tập hợp cơ bản**:
- **Hợp (∪)**: Tất cả phần tử thuộc A hoặc B
- **Giao (∩)**: Phần tử thuộc cả A và B
- **Hiệu (\)**: Phần tử thuộc A nhưng không thuộc B
- **Phần bù (ᶜ)**: Phần tử không thuộc A
- **Hiệu đối xứng (△)**: Phần tử thuộc A hoặc B nhưng không thuộc cả hai

**Tính chất quan trọng**:
- Giao hoán, kết hợp, phân phối
- Định luật De Morgan
- Nguyên lý bao hàm-loại trừ

**Ứng dụng**: Cơ sở dữ liệu, lập trình, thuật toán, phân tích dữ liệu

Trong bài tiếp theo, chúng ta sẽ học về **Quan hệ** - cách mô tả mối liên hệ giữa các phần tử của các tập hợp khác nhau.
