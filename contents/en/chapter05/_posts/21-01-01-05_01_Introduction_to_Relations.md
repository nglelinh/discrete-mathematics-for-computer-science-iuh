---
layout: post
title: "Giới thiệu Quan hệ"
categories: chapter05
date: 2021-01-01
order: 1
required: true
lang: vi
---

# Giới thiệu Quan hệ

Quan hệ là khái niệm cơ bản để mô tả mối liên hệ giữa các phần tử của các tập hợp. Đây là nền tảng cho cơ sở dữ liệu, thuật toán, và nhiều ứng dụng trong khoa học máy tính.

## Định nghĩa Quan hệ

**Định nghĩa**: Quan hệ R từ tập hợp A đến tập hợp B là một tập con của tích Cartesian A × B.

**Ký hiệu**: 
- R ⊆ A × B
- Nếu (a, b) ∈ R, ta viết aRb hoặc R(a, b)
- Nếu (a, b) ∉ R, ta viết a R̸ b

### Tích Cartesian
**Định nghĩa**: A × B = {(a, b) | a ∈ A và b ∈ B}

**Ví dụ**:
- A = {1, 2}, B = {x, y}
- A × B = {(1, x), (1, y), (2, x), (2, y)}
- |A × B| = |A| × |B| = 2 × 2 = 4

## Các cách biểu diễn quan hệ

### 1. Liệt kê các cặp
**Ví dụ**: R = {(1, 2), (2, 3), (3, 1)} trên tập {1, 2, 3}

### 2. Mô tả bằng tính chất
**Ví dụ**: R = {(x, y) | x < y} trên tập số thực

### 3. Ma trận quan hệ
Cho A = {a₁, a₂, ..., aₘ}, B = {b₁, b₂, ..., bₙ}

Ma trận M_R có M_R[i][j] = 1 nếu (aᵢ, bⱼ) ∈ R, ngược lại = 0

**Ví dụ**: A = {1, 2, 3}, R = {(1, 1), (2, 3), (3, 2)}

```
    1  2  3
1 [ 1  0  0 ]
2 [ 0  0  1 ]
3 [ 0  1  0 ]
```

### 4. Đồ thị có hướng (Digraph)
- Đỉnh: các phần tử của tập hợp
- Cung: các cặp trong quan hệ

## Công cụ tương tác: Trình khám phá quan hệ

<div id="relation-explorer" class="interactive-tool">
    <h4>🔍 Công cụ khám phá quan hệ</h4>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
        <div>
            <label><strong>Tập hợp A:</strong></label>
            <input type="text" id="set-a-rel" placeholder="1,2,3" style="width: 100%; padding: 8px; margin-top: 5px;">
        </div>
        <div>
            <label><strong>Tập hợp B:</strong></label>
            <input type="text" id="set-b-rel" placeholder="1,2,3" style="width: 100%; padding: 8px; margin-top: 5px;">
        </div>
    </div>
    
    <div style="margin-bottom: 20px;">
        <label><strong>Quan hệ R (các cặp cách nhau bởi dấu phẩy):</strong></label>
        <input type="text" id="relation-pairs" placeholder="(1,2),(2,3),(3,1)" style="width: 100%; padding: 8px; margin-top: 5px;">
    </div>
    
    <button onclick="analyzeRelation()" style="width: 100%; margin-bottom: 20px;">
        Phân tích quan hệ
    </button>
    
    <div id="relation-analysis" style="background: white; padding: 20px; border-radius: 8px; border: 1px solid #dee2e6;">
        <p style="color: #666; text-align: center; margin: 0;">Nhập tập hợp và quan hệ để xem phân tích</p>
    </div>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px;">
        <div id="relation-matrix" style="background: #f8f9fa; padding: 15px; border-radius: 8px;">
            <h5>Ma trận quan hệ</h5>
            <div id="matrix-display"></div>
        </div>
        <div id="relation-graph" style="background: #f8f9fa; padding: 15px; border-radius: 8px;">
            <h5>Đồ thị có hướng</h5>
            <div id="graph-display"></div>
        </div>
    </div>
</div>

<script>
function analyzeRelation() {
    const setAInput = document.getElementById('set-a-rel').value.trim();
    const setBInput = document.getElementById('set-b-rel').value.trim();
    const relationInput = document.getElementById('relation-pairs').value.trim();
    const analysisDiv = document.getElementById('relation-analysis');
    const matrixDiv = document.getElementById('matrix-display');
    const graphDiv = document.getElementById('graph-display');
    
    if (!setAInput || !setBInput || !relationInput) {
        analysisDiv.innerHTML = '<p style="color: #dc3545; text-align: center; margin: 0;">Vui lòng nhập đầy đủ thông tin!</p>';
        return;
    }
    
    try {
        // Parse input
        const setA = setAInput.split(',').map(x => x.trim()).filter(x => x);
        const setB = setBInput.split(',').map(x => x.trim()).filter(x => x);
        
        // Parse relation pairs
        const pairMatches = relationInput.match(/\([^)]+\)/g);
        if (!pairMatches) {
            throw new Error('Định dạng quan hệ không hợp lệ');
        }
        
        const relation = pairMatches.map(pair => {
            const content = pair.slice(1, -1); // Remove parentheses
            const [a, b] = content.split(',').map(x => x.trim());
            return [a, b];
        });
        
        // Validate relation
        const invalidPairs = relation.filter(([a, b]) => !setA.includes(a) || !setB.includes(b));
        if (invalidPairs.length > 0) {
            throw new Error(`Các cặp không hợp lệ: ${invalidPairs.map(p => `(${p[0]},${p[1]})`).join(', ')}`);
        }
        
        // Calculate properties
        const cartesianSize = setA.length * setB.length;
        const relationSize = relation.length;
        
        // Display analysis
        analysisDiv.innerHTML = `
            <div style="text-align: center;">
                <h5 style="color: #495057; margin-bottom: 15px;">Phân tích quan hệ R</h5>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 15px;">
                    <div>
                        <strong>Tập A:</strong> {${setA.join(', ')}}<br>
                        <strong>|A|:</strong> ${setA.length}
                    </div>
                    <div>
                        <strong>Tập B:</strong> {${setB.join(', ')}}<br>
                        <strong>|B|:</strong> ${setB.length}
                    </div>
                </div>
                <div style="background: #e3f2fd; padding: 15px; border-radius: 6px; margin: 15px 0;">
                    <strong>R = {${relation.map(([a,b]) => `(${a},${b})`).join(', ')}}</strong><br>
                    <strong>|R| = ${relationSize}</strong> / |A × B| = ${cartesianSize}
                </div>
                <div style="font-size: 0.9em; color: #666;">
                    Tỷ lệ: ${((relationSize / cartesianSize) * 100).toFixed(1)}% của tích Cartesian
                </div>
            </div>
        `;
        
        // Create matrix
        createRelationMatrix(setA, setB, relation, matrixDiv);
        
        // Create simple graph representation
        createRelationGraph(setA, setB, relation, graphDiv);
        
    } catch (error) {
        analysisDiv.innerHTML = `<p style="color: #dc3545; text-align: center; margin: 0;">Lỗi: ${error.message}</p>`;
    }
}

function createRelationMatrix(setA, setB, relation, container) {
    const relationSet = new Set(relation.map(([a, b]) => `${a},${b}`));
    
    let matrixHTML = '<table style="margin: 10px auto; border-collapse: collapse; font-family: monospace;">';
    
    // Header row
    matrixHTML += '<tr><td style="padding: 5px; border: 1px solid #ccc; background: #f0f0f0;"></td>';
    setB.forEach(b => {
        matrixHTML += `<td style="padding: 5px; border: 1px solid #ccc; background: #f0f0f0; text-align: center; font-weight: bold;">${b}</td>`;
    });
    matrixHTML += '</tr>';
    
    // Data rows
    setA.forEach(a => {
        matrixHTML += `<tr><td style="padding: 5px; border: 1px solid #ccc; background: #f0f0f0; font-weight: bold;">${a}</td>`;
        setB.forEach(b => {
            const hasRelation = relationSet.has(`${a},${b}`);
            const cellClass = hasRelation ? 'background: #d4edda; color: #155724;' : 'background: #f8d7da; color: #721c24;';
            matrixHTML += `<td style="padding: 5px; border: 1px solid #ccc; text-align: center; ${cellClass}">${hasRelation ? '1' : '0'}</td>`;
        });
        matrixHTML += '</tr>';
    });
    
    matrixHTML += '</table>';
    container.innerHTML = matrixHTML;
}

function createRelationGraph(setA, setB, relation, container) {
    const allNodes = [...new Set([...setA, ...setB])];
    const nodePositions = {};
    
    // Simple circular layout
    allNodes.forEach((node, index) => {
        const angle = (2 * Math.PI * index) / allNodes.length;
        nodePositions[node] = {
            x: 80 + 60 * Math.cos(angle),
            y: 80 + 60 * Math.sin(angle)
        };
    });
    
    let svgHTML = '<svg width="160" height="160" style="border: 1px solid #ddd; border-radius: 4px;">';
    
    // Draw edges
    relation.forEach(([a, b]) => {
        const startPos = nodePositions[a];
        const endPos = nodePositions[b];
        if (startPos && endPos) {
            svgHTML += `<line x1="${startPos.x}" y1="${startPos.y}" x2="${endPos.x}" y2="${endPos.y}" 
                        stroke="#007bff" stroke-width="2" marker-end="url(#arrowhead)"/>`;
        }
    });
    
    // Arrow marker
    svgHTML += `<defs><marker id="arrowhead" markerWidth="10" markerHeight="7" 
                refX="9" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="#007bff" />
                </marker></defs>`;
    
    // Draw nodes
    allNodes.forEach(node => {
        const pos = nodePositions[node];
        svgHTML += `<circle cx="${pos.x}" cy="${pos.y}" r="12" fill="#fff" stroke="#333" stroke-width="2"/>`;
        svgHTML += `<text x="${pos.x}" y="${pos.y + 4}" text-anchor="middle" font-size="12" font-weight="bold">${node}</text>`;
    });
    
    svgHTML += '</svg>';
    container.innerHTML = svgHTML;
}
</script>

## Các loại quan hệ đặc biệt

### 1. Quan hệ trên một tập hợp
**Định nghĩa**: Quan hệ R trên tập A là quan hệ từ A đến A (R ⊆ A × A)

**Ví dụ**:
- Quan hệ "≤" trên ℕ
- Quan hệ "chia hết" trên ℤ
- Quan hệ "tương đương" trên tập hợp các tam giác

### 2. Quan hệ rỗng và quan hệ toàn phần
- **Quan hệ rỗng**: ∅ ⊆ A × B
- **Quan hệ toàn phần**: A × B

### 3. Quan hệ ngược
**Định nghĩa**: R⁻¹ = {(b, a) | (a, b) ∈ R}

**Ví dụ**: Nếu R = {(1, 2), (2, 3)} thì R⁻¹ = {(2, 1), (3, 2)}

## Ví dụ trong khoa học máy tính

### 1. Cơ sở dữ liệu quan hệ
```sql
-- Bảng Students (ID, Name)
-- Bảng Courses (ID, Title)  
-- Bảng Enrollments (StudentID, CourseID) - Quan hệ "đăng ký"

SELECT s.Name, c.Title 
FROM Students s, Courses c, Enrollments e
WHERE s.ID = e.StudentID AND c.ID = e.CourseID;
```

### 2. Đồ thị trong thuật toán
```python
# Quan hệ "kề nhau" trong đồ thị
adjacency_relation = {
    (1, 2), (2, 3), (3, 4), (4, 1), (2, 4)
}

# Biểu diễn bằng danh sách kề
def relation_to_adjacency_list(relation, vertices):
    adj_list = {v: [] for v in vertices}
    for (u, v) in relation:
        adj_list[u].append(v)
    return adj_list
```

### 3. Quan hệ thứ tự trong sắp xếp
```python
# Quan hệ "nhỏ hơn hoặc bằng"
def is_sorted(arr):
    """Kiểm tra mảng có thỏa mãn quan hệ thứ tự không"""
    for i in range(len(arr) - 1):
        if not (arr[i] <= arr[i + 1]):  # Quan hệ ≤
            return False
    return True
```

## Bài tập thực hành

### Bài tập 1: Xây dựng quan hệ
Cho A = {1, 2, 3, 4}, xây dựng các quan hệ sau:

1. R₁ = {(a, b) | a < b}
2. R₂ = {(a, b) | a chia hết cho b}
3. R₃ = {(a, b) | a + b = 5}
4. Tính |R₁|, |R₂|, |R₃|

### Bài tập 2: Ma trận quan hệ
Cho quan hệ R = {(1, 2), (2, 1), (2, 3), (3, 3)} trên A = {1, 2, 3}:

1. Vẽ ma trận quan hệ M_R
2. Tìm quan hệ ngược R⁻¹
3. Vẽ đồ thị có hướng của R

### Bài tập 3: Ứng dụng thực tế
Một mạng xã hội có 5 người dùng {A, B, C, D, E}. Quan hệ "theo dõi" được cho bởi:
Follow = {(A,B), (A,C), (B,C), (C,D), (D,E), (E,A)}

1. Ai theo dõi nhiều người nhất?
2. Ai được theo dõi nhiều nhất?
3. Có chu trình theo dõi nào không?

<details>
<summary>Đáp án Bài tập 1</summary>

1. R₁ = {(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)}, |R₁| = 6
2. R₂ = {(2,1), (3,1), (4,1), (4,2)}, |R₂| = 4  
3. R₃ = {(1,4), (2,3), (3,2), (4,1)}, |R₃| = 4

</details>

## Tính chất cơ bản của quan hệ

### 1. Miền và Tập ảnh
- **Miền (Domain)**: dom(R) = {a ∈ A | ∃b ∈ B: (a,b) ∈ R}
- **Tập ảnh (Range)**: ran(R) = {b ∈ B | ∃a ∈ A: (a,b) ∈ R}

### 2. Hợp thành quan hệ
**Định nghĩa**: Cho R ⊆ A × B và S ⊆ B × C
S ∘ R = {(a, c) | ∃b ∈ B: (a,b) ∈ R và (b,c) ∈ S}

**Ví dụ**:
- R = {(1,2), (2,3)} ⊆ {1,2} × {2,3}
- S = {(2,a), (3,b)} ⊆ {2,3} × {a,b}
- S ∘ R = {(1,a), (2,b)}

## Tóm tắt

**Quan hệ** là công cụ mạnh mẽ để:
- **Mô tả** mối liên hệ giữa các đối tượng
- **Biểu diễn** bằng ma trận, đồ thị, hoặc liệt kê
- **Ứng dụng** trong cơ sở dữ liệu, thuật toán, mạng

**Khái niệm chính**:
- Quan hệ R ⊆ A × B
- Ma trận quan hệ và đồ thị có hướng
- Quan hệ ngược R⁻¹
- Hợp thành quan hệ S ∘ R

Trong bài tiếp theo, chúng ta sẽ học về **các tính chất của quan hệ** như phản xạ, đối xứng, và bắc cầu - nền tảng cho quan hệ tương đương và thứ tự.
