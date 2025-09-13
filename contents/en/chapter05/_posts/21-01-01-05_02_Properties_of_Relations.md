---
layout: post
title: "Tính chất của Quan hệ"
categories: chapter05
date: 2021-01-01
order: 2
required: true
lang: vi
---

# Tính chất của Quan hệ

Các tính chất của quan hệ giúp chúng ta phân loại và hiểu rõ hơn về cấu trúc của các mối liên hệ. Đây là nền tảng để xây dựng các khái niệm quan trọng như quan hệ tương đương và quan hệ thứ tự.

## Các tính chất cơ bản

Cho quan hệ R trên tập hợp A (R ⊆ A × A):

### 1. Tính phản xạ (Reflexive)

**Định nghĩa**: R là phản xạ nếu ∀a ∈ A: (a, a) ∈ R

**Ví dụ**:
- ✅ "=" trên ℝ: mọi số đều bằng chính nó
- ✅ "≤" trên ℝ: mọi số đều ≤ chính nó  
- ❌ "<" trên ℝ: không có số nào < chính nó

**Trong ma trận**: Đường chéo chính toàn số 1
```
[1 ? ?]
[? 1 ?]
[? ? 1]
```

### 2. Tính đối xứng (Symmetric)

**Định nghĩa**: R là đối xứng nếu ∀a, b ∈ A: (a, b) ∈ R ⟹ (b, a) ∈ R

**Ví dụ**:
- ✅ "=" trên ℝ: nếu a = b thì b = a
- ✅ "≠" trên ℝ: nếu a ≠ b thì b ≠ a
- ❌ "<" trên ℝ: nếu a < b thì b ≮ a

**Trong ma trận**: Ma trận đối xứng qua đường chéo chính
```
[? a b]
[a ? c]
[b c ?]
```

### 3. Tính phản đối xứng (Antisymmetric)

**Định nghĩa**: R là phản đối xứng nếu ∀a, b ∈ A: (a, b) ∈ R ∧ (b, a) ∈ R ⟹ a = b

**Ví dụ**:
- ✅ "≤" trên ℝ: nếu a ≤ b và b ≤ a thì a = b
- ✅ "⊆" trên tập hợp: nếu A ⊆ B và B ⊆ A thì A = B
- ❌ "≠" trên ℝ: nếu a ≠ b và b ≠ a thì a ≠ b (không suy ra a = b)

### 4. Tính bắc cầu (Transitive)

**Định nghĩa**: R là bắc cầu nếu ∀a, b, c ∈ A: (a, b) ∈ R ∧ (b, c) ∈ R ⟹ (a, c) ∈ R

**Ví dụ**:
- ✅ "<" trên ℝ: nếu a < b và b < c thì a < c
- ✅ "⊆" trên tập hợp: nếu A ⊆ B và B ⊆ C thì A ⊆ C
- ❌ "là cha của": nếu A là cha của B và B là cha của C thì A không phải là cha của C

## Công cụ tương tác: Kiểm tra tính chất quan hệ

<div id="relation-properties-checker" class="interactive-tool">
    <h4>🔍 Công cụ kiểm tra tính chất quan hệ</h4>
    
    <div style="margin-bottom: 20px;">
        <label><strong>Tập hợp A:</strong></label>
        <input type="text" id="set-a-props" placeholder="1,2,3" style="width: 100%; padding: 8px; margin-top: 5px;">
    </div>
    
    <div style="margin-bottom: 20px;">
        <label><strong>Quan hệ R (các cặp):</strong></label>
        <input type="text" id="relation-props" placeholder="(1,1),(1,2),(2,2),(2,3),(3,3)" style="width: 100%; padding: 8px; margin-top: 5px;">
    </div>
    
    <div style="margin-bottom: 20px;">
        <label><strong>Hoặc chọn quan hệ mẫu:</strong></label>
        <select id="sample-relations" onchange="loadSampleRelation()" style="width: 100%; padding: 8px;">
            <option value="">-- Chọn quan hệ mẫu --</option>
            <option value="equality">Quan hệ bằng (=)</option>
            <option value="less-equal">Quan hệ nhỏ hơn hoặc bằng (≤)</option>
            <option value="less-than">Quan hệ nhỏ hơn (<)</option>
            <option value="divisibility">Quan hệ chia hết</option>
            <option value="friendship">Quan hệ bạn bè</option>
        </select>
    </div>
    
    <button onclick="checkProperties()" style="width: 100%; margin-bottom: 20px;">
        Kiểm tra tính chất
    </button>
    
    <div id="properties-result" style="background: white; padding: 20px; border-radius: 8px; border: 1px solid #dee2e6;">
        <p style="color: #666; text-align: center; margin: 0;">Nhập quan hệ để kiểm tra tính chất</p>
    </div>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px;">
        <div id="matrix-visualization" style="background: #f8f9fa; padding: 15px; border-radius: 8px;">
            <h5>Ma trận quan hệ</h5>
            <div id="matrix-props-display"></div>
        </div>
        <div id="graph-visualization" style="background: #f8f9fa; padding: 15px; border-radius: 8px;">
            <h5>Đồ thị quan hệ</h5>
            <div id="graph-props-display"></div>
        </div>
    </div>
</div>

<script>
function loadSampleRelation() {
    const sample = document.getElementById('sample-relations').value;
    const setInput = document.getElementById('set-a-props');
    const relationInput = document.getElementById('relation-props');
    
    switch(sample) {
        case 'equality':
            setInput.value = '1,2,3';
            relationInput.value = '(1,1),(2,2),(3,3)';
            break;
        case 'less-equal':
            setInput.value = '1,2,3';
            relationInput.value = '(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)';
            break;
        case 'less-than':
            setInput.value = '1,2,3';
            relationInput.value = '(1,2),(1,3),(2,3)';
            break;
        case 'divisibility':
            setInput.value = '1,2,3,6';
            relationInput.value = '(1,1),(1,2),(1,3),(1,6),(2,2),(2,6),(3,3),(3,6),(6,6)';
            break;
        case 'friendship':
            setInput.value = 'A,B,C';
            relationInput.value = '(A,B),(B,A),(B,C),(C,B)';
            break;
    }
}

function checkProperties() {
    const setAInput = document.getElementById('set-a-props').value.trim();
    const relationInput = document.getElementById('relation-props').value.trim();
    const resultDiv = document.getElementById('properties-result');
    const matrixDiv = document.getElementById('matrix-props-display');
    const graphDiv = document.getElementById('graph-props-display');
    
    if (!setAInput || !relationInput) {
        resultDiv.innerHTML = '<p style="color: #dc3545; text-align: center; margin: 0;">Vui lòng nhập đầy đủ thông tin!</p>';
        return;
    }
    
    try {
        // Parse input
        const setA = setAInput.split(',').map(x => x.trim()).filter(x => x);
        
        // Parse relation pairs
        const pairMatches = relationInput.match(/\([^)]+\)/g);
        if (!pairMatches) {
            throw new Error('Định dạng quan hệ không hợp lệ');
        }
        
        const relation = pairMatches.map(pair => {
            const content = pair.slice(1, -1);
            const [a, b] = content.split(',').map(x => x.trim());
            return [a, b];
        });
        
        // Check properties
        const properties = analyzeRelationProperties(setA, relation);
        
        // Display results
        displayPropertyResults(setA, relation, properties, resultDiv);
        
        // Create visualizations
        createMatrix(setA, relation, matrixDiv, properties);
        createGraph(setA, relation, graphDiv, properties);
        
    } catch (error) {
        resultDiv.innerHTML = `<p style="color: #dc3545; text-align: center; margin: 0;">Lỗi: ${error.message}</p>`;
    }
}

function analyzeRelationProperties(setA, relation) {
    const relationSet = new Set(relation.map(([a, b]) => `${a},${b}`));
    
    // Check reflexive
    const reflexive = setA.every(a => relationSet.has(`${a},${a}`));
    
    // Check symmetric
    const symmetric = relation.every(([a, b]) => relationSet.has(`${b},${a}`));
    
    // Check antisymmetric
    const antisymmetric = relation.every(([a, b]) => {
        if (a !== b && relationSet.has(`${b},${a}`)) {
            return false;
        }
        return true;
    });
    
    // Check transitive
    let transitive = true;
    for (const [a, b] of relation) {
        for (const [c, d] of relation) {
            if (b === c && !relationSet.has(`${a},${d}`)) {
                transitive = false;
                break;
            }
        }
        if (!transitive) break;
    }
    
    return { reflexive, symmetric, antisymmetric, transitive };
}

function displayPropertyResults(setA, relation, properties, container) {
    const { reflexive, symmetric, antisymmetric, transitive } = properties;
    
    // Determine relation type
    let relationType = '';
    if (reflexive && symmetric && transitive) {
        relationType = '🎯 <strong>Quan hệ tương đương</strong>';
    } else if (reflexive && antisymmetric && transitive) {
        relationType = '📊 <strong>Quan hệ thứ tự (một phần)</strong>';
    } else if (antisymmetric && transitive) {
        relationType = '📈 <strong>Quan hệ thứ tự nghiêm ngặt</strong>';
    } else {
        relationType = '🔍 <strong>Quan hệ thông thường</strong>';
    }
    
    container.innerHTML = `
        <div style="text-align: center;">
            <h5 style="color: #495057; margin-bottom: 15px;">Kết quả phân tích</h5>
            <div style="background: #f8f9fa; padding: 15px; border-radius: 6px; margin-bottom: 15px;">
                <strong>A = {${setA.join(', ')}}</strong><br>
                <strong>R = {${relation.map(([a,b]) => `(${a},${b})`).join(', ')}}</strong>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 15px;">
                <div style="background: ${reflexive ? '#d4edda' : '#f8d7da'}; padding: 12px; border-radius: 6px;">
                    <strong style="color: ${reflexive ? '#155724' : '#721c24'};">
                        ${reflexive ? '✅' : '❌'} Phản xạ
                    </strong>
                </div>
                <div style="background: ${symmetric ? '#d4edda' : '#f8d7da'}; padding: 12px; border-radius: 6px;">
                    <strong style="color: ${symmetric ? '#155724' : '#721c24'};">
                        ${symmetric ? '✅' : '❌'} Đối xứng
                    </strong>
                </div>
                <div style="background: ${antisymmetric ? '#d4edda' : '#f8d7da'}; padding: 12px; border-radius: 6px;">
                    <strong style="color: ${antisymmetric ? '#155724' : '#721c24'};">
                        ${antisymmetric ? '✅' : '❌'} Phản đối xứng
                    </strong>
                </div>
                <div style="background: ${transitive ? '#d4edda' : '#f8d7da'}; padding: 12px; border-radius: 6px;">
                    <strong style="color: ${transitive ? '#155724' : '#721c24'};">
                        ${transitive ? '✅' : '❌'} Bắc cầu
                    </strong>
                </div>
            </div>
            
            <div style="background: #e3f2fd; padding: 15px; border-radius: 6px; border-left: 4px solid #1976d2;">
                ${relationType}
            </div>
        </div>
    `;
}

function createMatrix(setA, relation, container, properties) {
    const relationSet = new Set(relation.map(([a, b]) => `${a},${b}`));
    
    let matrixHTML = '<table style="margin: 10px auto; border-collapse: collapse; font-family: monospace; font-size: 12px;">';
    
    // Header row
    matrixHTML += '<tr><td style="padding: 4px; border: 1px solid #ccc; background: #f0f0f0;"></td>';
    setA.forEach(b => {
        matrixHTML += `<td style="padding: 4px; border: 1px solid #ccc; background: #f0f0f0; text-align: center; font-weight: bold;">${b}</td>`;
    });
    matrixHTML += '</tr>';
    
    // Data rows
    setA.forEach((a, i) => {
        matrixHTML += `<tr><td style="padding: 4px; border: 1px solid #ccc; background: #f0f0f0; font-weight: bold;">${a}</td>`;
        setA.forEach((b, j) => {
            const hasRelation = relationSet.has(`${a},${b}`);
            let cellStyle = 'padding: 4px; border: 1px solid #ccc; text-align: center;';
            
            // Highlight diagonal for reflexive
            if (i === j && properties.reflexive) {
                cellStyle += ' background: #fff3cd; border: 2px solid #ffc107;';
            } else if (hasRelation) {
                cellStyle += ' background: #d4edda; color: #155724;';
            } else {
                cellStyle += ' background: #f8d7da; color: #721c24;';
            }
            
            matrixHTML += `<td style="${cellStyle}">${hasRelation ? '1' : '0'}</td>`;
        });
        matrixHTML += '</tr>';
    });
    
    matrixHTML += '</table>';
    
    // Add property explanations
    let explanation = '<div style="font-size: 11px; margin-top: 10px; color: #666;">';
    if (properties.reflexive) {
        explanation += '🟡 Đường chéo: Phản xạ<br>';
    }
    if (properties.symmetric) {
        explanation += '🔄 Đối xứng qua đường chéo<br>';
    }
    explanation += '</div>';
    
    container.innerHTML = matrixHTML + explanation;
}

function createGraph(setA, relation, container, properties) {
    const nodeCount = setA.length;
    const radius = Math.min(60, 80 - nodeCount * 5);
    const centerX = 80, centerY = 80;
    
    const nodePositions = {};
    setA.forEach((node, index) => {
        const angle = (2 * Math.PI * index) / nodeCount;
        nodePositions[node] = {
            x: centerX + radius * Math.cos(angle),
            y: centerY + radius * Math.sin(angle)
        };
    });
    
    let svgHTML = '<svg width="160" height="160" style="border: 1px solid #ddd; border-radius: 4px;">';
    
    // Add arrow marker
    svgHTML += `<defs>
        <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
            <polygon points="0 0, 8 3, 0 6" fill="#007bff" />
        </marker>
    </defs>`;
    
    // Draw edges
    relation.forEach(([a, b]) => {
        const startPos = nodePositions[a];
        const endPos = nodePositions[b];
        
        if (a === b) {
            // Self-loop
            const loopX = startPos.x + 15;
            const loopY = startPos.y - 15;
            svgHTML += `<circle cx="${loopX}" cy="${loopY}" r="8" fill="none" stroke="#28a745" stroke-width="2" marker-end="url(#arrowhead)"/>`;
        } else {
            // Regular edge
            const color = properties.symmetric ? '#ffc107' : '#007bff';
            svgHTML += `<line x1="${startPos.x}" y1="${startPos.y}" x2="${endPos.x}" y2="${endPos.y}" 
                        stroke="${color}" stroke-width="2" marker-end="url(#arrowhead)"/>`;
        }
    });
    
    // Draw nodes
    setA.forEach(node => {
        const pos = nodePositions[node];
        svgHTML += `<circle cx="${pos.x}" cy="${pos.y}" r="12" fill="#fff" stroke="#333" stroke-width="2"/>`;
        svgHTML += `<text x="${pos.x}" y="${pos.y + 4}" text-anchor="middle" font-size="10" font-weight="bold">${node}</text>`;
    });
    
    svgHTML += '</svg>';
    
    // Add legend
    let legend = '<div style="font-size: 11px; margin-top: 10px; color: #666;">';
    if (properties.reflexive) {
        legend += '🟢 Vòng tròn: Phản xạ<br>';
    }
    if (properties.symmetric) {
        legend += '🟡 Cung vàng: Đối xứng<br>';
    }
    legend += '</div>';
    
    container.innerHTML = svgHTML + legend;
}
</script>

## Ví dụ chi tiết

### Ví dụ 1: Quan hệ "≤" trên {1, 2, 3}

R = {(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)}

**Kiểm tra tính chất**:
- ✅ **Phản xạ**: (1,1), (2,2), (3,3) ∈ R
- ❌ **Đối xứng**: (1,2) ∈ R nhưng (2,1) ∉ R
- ✅ **Phản đối xứng**: Không có cặp (a,b) và (b,a) với a ≠ b
- ✅ **Bắc cầu**: (1,2) ∈ R, (2,3) ∈ R và (1,3) ∈ R

**Kết luận**: Đây là **quan hệ thứ tự một phần**.

### Ví dụ 2: Quan hệ "bạn bè" trên {A, B, C, D}

R = {(A,B), (B,A), (B,C), (C,B), (C,D), (D,C)}

**Kiểm tra tính chất**:
- ❌ **Phản xạ**: (A,A) ∉ R
- ✅ **Đối xứng**: Mọi cặp (x,y) đều có (y,x)
- ❌ **Phản đối xứng**: (A,B) ∈ R và (B,A) ∈ R nhưng A ≠ B
- ❌ **Bắc cầu**: (A,B) ∈ R, (B,C) ∈ R nhưng (A,C) ∉ R

## Ứng dụng trong khoa học máy tính

### 1. Cơ sở dữ liệu - Khóa ngoại
```sql
-- Quan hệ "tham chiếu" phải có tính chất:
-- - Phản đối xứng: Không có tham chiếu vòng
-- - Bắc cầu: Tham chiếu gián tiếp

CREATE TABLE Orders (
    id INT PRIMARY KEY,
    customer_id INT REFERENCES Customers(id)
);
```

### 2. Thuật toán sắp xếp
```python
def is_valid_comparison(relation):
    """Kiểm tra quan hệ có thể dùng để sắp xếp không"""
    # Cần có tính phản đối xứng và bắc cầu
    return (is_antisymmetric(relation) and 
            is_transitive(relation))

def merge_sort(arr, compare_relation):
    """Sắp xếp dựa trên quan hệ thứ tự"""
    if not is_valid_comparison(compare_relation):
        raise ValueError("Quan hệ không hợp lệ cho sắp xếp")
    # ... thuật toán merge sort
```

### 3. Mạng xã hội - Phân tích mối quan hệ
```python
def analyze_social_network(friendship_relation):
    """Phân tích mạng xã hội"""
    properties = {
        'symmetric': is_symmetric(friendship_relation),
        'transitive': is_transitive(friendship_relation)
    }
    
    if properties['symmetric'] and properties['transitive']:
        return "Mạng có tính cộng đồng cao"
    elif properties['symmetric']:
        return "Mạng bạn bè cân bằng"
    else:
        return "Mạng có quan hệ một chiều"
```

## Bài tập thực hành

### Bài tập 1: Xác định tính chất
Cho các quan hệ sau trên A = {1, 2, 3, 4}, xác định tính chất của mỗi quan hệ:

1. R₁ = {(1,1), (2,2), (3,3), (4,4), (1,2), (2,3)}
2. R₂ = {(1,2), (2,1), (3,4), (4,3)}  
3. R₃ = {(1,1), (1,2), (1,3), (1,4), (2,2), (2,3), (2,4), (3,3), (3,4), (4,4)}

### Bài tập 2: Xây dựng quan hệ
Trên tập A = {a, b, c}, xây dựng:

1. Quan hệ vừa đối xứng vừa bắc cầu nhưng không phản xạ
2. Quan hệ phản xạ và bắc cầu nhưng không đối xứng
3. Quan hệ có đúng 2 trong 4 tính chất

### Bài tập 3: Ứng dụng thực tế
Một hệ thống phân quyền có 4 vai trò: Admin, Manager, User, Guest.
Quan hệ "có quyền cao hơn hoặc bằng" được định nghĩa:
- Admin ≥ Manager ≥ User ≥ Guest
- Mỗi vai trò ≥ chính nó

1. Viết quan hệ dưới dạng tập hợp các cặp
2. Kiểm tra tính chất của quan hệ này
3. Quan hệ này thuộc loại nào?

<details>
<summary>Đáp án Bài tập 1</summary>

1. R₁: Phản xạ ✅, Đối xứng ❌, Phản đối xứng ❌, Bắc cầu ❌
2. R₂: Phản xạ ❌, Đối xứng ✅, Phản đối xứng ❌, Bắc cầu ❌  
3. R₃: Phản xạ ✅, Đối xứng ❌, Phản đối xứng ✅, Bắc cầu ✅ → **Quan hệ thứ tự**

</details>

## Tóm tắt

**Bốn tính chất cơ bản của quan hệ**:

1. **Phản xạ**: ∀a: (a,a) ∈ R
2. **Đối xứng**: (a,b) ∈ R ⟹ (b,a) ∈ R  
3. **Phản đối xứng**: (a,b) ∈ R ∧ (b,a) ∈ R ⟹ a = b
4. **Bắc cầu**: (a,b) ∈ R ∧ (b,c) ∈ R ⟹ (a,c) ∈ R

**Các loại quan hệ đặc biệt**:
- **Quan hệ tương đương**: Phản xạ + Đối xứng + Bắc cầu
- **Quan hệ thứ tự**: Phản xạ + Phản đối xứng + Bắc cầu

**Ứng dụng**: Cơ sở dữ liệu, thuật toán sắp xếp, mạng xã hội, hệ thống phân quyền

Trong bài tiếp theo, chúng ta sẽ tìm hiểu sâu hơn về **Quan hệ tương đương** và cách chúng phân chia tập hợp thành các lớp tương đương.
