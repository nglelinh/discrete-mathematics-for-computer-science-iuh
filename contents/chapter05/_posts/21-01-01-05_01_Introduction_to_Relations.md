---
layout: post
title: "Giới thiệu Quan hệ"
categories: chapter05
date: 2021-01-01
order: 1
required: true
lang: en
---

# Giới thiệu Quan hệ

Biết từng đối tượng riêng lẻ là chưa đủ; điều quan trọng hơn nhiều là chúng **liên hệ với nhau thế nào**. Trong mạng xã hội có quan hệ “theo dõi”, trong cơ sở dữ liệu có quan hệ giữa khóa chính và khóa ngoại, trong toán học có quan hệ “nhỏ hơn”, “bằng nhau”, “chia hết”. Chính mạng lưới liên kết đó mới tạo nên cấu trúc thật của bài toán.

**Quan hệ** là công cụ để mô tả các kết nối ấy một cách chính xác. Khi học quan hệ, ta bắt đầu chuyển từ tư duy “phần tử nào nằm trong tập” sang tư duy “phần tử này gắn với phần tử kia ra sao”. Đây là nền tảng cho database, đồ thị, machine learning trên mạng, và nhiều cấu trúc tổ chức dữ liệu trong khoa học máy tính.

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

<div class="content-box insight-box" markdown="1">
**Tích Cartesian trong CS**: Tích Cartesian là nền tảng của phép JOIN trong SQL. Khi bạn viết `SELECT * FROM A, B`, bạn nhận được tích Cartesian A × B. Thực tế, phép `CROSS JOIN` trong SQL chính là tích Cartesian.
</div>

### Quan hệ trên một tập hợp

Khi A = B, ta nói R là **quan hệ trên A** (R ⊆ A × A). Đây là trường hợp quan trọng nhất -- chúng ta sẽ tập trung vào loại quan hệ này.

**Ví dụ**: Quan hệ "≤" trên ℝ là quan hệ trên tập số thực. Quan hệ "⊆" trên tập lũy thừa của S là quan hệ trên 𝒫(S).

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
- Cung (mũi tên): các cặp trong quan hệ

<div class="content-box warning-box" markdown="1">
**Lỗi thường gặp**: Khi biểu diễn quan hệ bằng ma trận, nhớ rằng hàng là phần tử nguồn (từ A), cột là phần tử đích (đến B). Với quan hệ trên cùng tập A (A = B), hàng và cột cùng một tập, và ma trận là vuông.
</div>

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
        <p style="color: #666; text-align: center; margin: 0;">Nhập thông tin để khám phá quan hệ</p>
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
        const setA = setAInput.split(',').map(x => x.trim()).filter(x => x);
        const setB = setBInput.split(',').map(x => x.trim()).filter(x => x);
        
        const pairMatches = relationInput.match(/\([^)]+\)/g);
        if (!pairMatches) {
            throw new Error('Định dạng quan hệ không hợp lệ');
        }
        
        const relation = pairMatches.map(pair => {
            const content = pair.slice(1, -1);
            const [a, b] = content.split(',').map(x => x.trim());
            return [a, b];
        });
        
        const invalidPairs = relation.filter(([a, b]) => !setA.includes(a) || !setB.includes(b));
        if (invalidPairs.length > 0) {
            throw new Error(`Các cặp không hợp lệ: ${invalidPairs.map(p => `(${p[0]},${p[1]})`).join(', ')}`);
        }
        
        const cartesianSize = setA.length * setB.length;
        const relationSize = relation.length;
        
        analysisDiv.innerHTML = `
            <div style="text-align: center;">
                <h5 style="color: #495057; margin-bottom: 15px;">Phân tích quan hệ R</h5>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                    <div>
                        <p><strong>Tập A</strong>: {${setA.join(', ')}}</p>
                        <p><strong>Tập B</strong>: ${setB.join(', ')}}</p>
                        <p><strong>|A × B|</strong> = ${cartesianSize}</p>
                    </div>
                    <div>
                        <p><strong>|R|</strong> = ${relationSize}</p>
                        <p><strong>R</strong> = {${relation.map(p => `(${p[0]},${p[1]})`).join(', ')}}</p>
                    </div>
                </div>
            </div>
        `;
        
        // Matrix display
        let matrixHTML = '<table style="border-collapse: collapse; margin: 10px auto;">';
        matrixHTML += '<tr><td></td>';
        for (let b of setB) matrixHTML += `<td style="border: 1px solid #ddd; padding: 5px; text-align: center; font-weight: bold;">${b}</td>`;
        matrixHTML += '</tr>';
        for (let a of setA) {
            matrixHTML += `<tr><td style="border: 1px solid #ddd; padding: 5px; text-align: center; font-weight: bold;">${a}</td>`;
            for (let b of setB) {
                const val = relation.some(([ra, rb]) => ra === a && rb === b) ? 1 : 0;
                matrixHTML += `<td style="border: 1px solid #ddd; padding: 5px; text-align: center;">${val}</td>`;
            }
            matrixHTML += '</tr>';
        }
        matrixHTML += '</table>';
        matrixDiv.innerHTML = matrixHTML;
        
        // Simple ASCII graph
        let graphHTML = '<div style="font-family: monospace; font-size: 14px; line-height: 1.6;">';
        graphHTML += '<strong>Đồ thị có hướng:</strong><br>';
        for (let [a, b] of relation) {
            graphHTML += `${a} → ${b}<br>`;
        }
        graphHTML += '</div>';
        graphDiv.innerHTML = graphHTML;
        
    } catch (e) {
        analysisDiv.innerHTML = `<p style="color: #dc3545; text-align: center; margin: 0;">Lỗi: ${e.message}</p>`;
    }
}
</script>

## Ứng dụng trong Khoa học Máy tính

### 1. Cơ sở dữ liệu quan hệ
Mô hình quan hệ (relational model) do Edgar Codd đề xuất năm 1970 là nền tảng của hầu hết cơ sở dữ liệu hiện đại. Mỗi bảng (table) là một quan hệ, mỗi hàng là một bộ (tuple), và mỗi cột là một thuộc tính.

### 2. Đồ thị và mạng xã hội
Quan hệ "bạn bè" trên Facebook là quan hệ hai ngôi. Đồ thị có hướng của quan hệ giúp phân tích mạng xã hội: ai là người có ảnh hưởng, ai kết nối các nhóm.

### 3. Lý thuyết đồ thị
Mọi đồ thị có hướng đều biểu diễn một quan hệ. Đồ thị vô hướng biểu diễn quan hệ đối xứng.

## Bài tập thực hành

### Bài tập 1: Tích Cartesian

Cho A = {1, 2, 3} và B = {a, b}. Tính A × B và |A × B|.

<details>
<summary>Đáp án</summary>

A × B = {(1, a), (1, b), (2, a), (2, b), (3, a), (3, b)}

|A × B| = 3 × 2 = 6
</details>

### Bài tập 2: Ma trận quan hệ

Viết ma trận quan hệ cho R = {(1, 2), (2, 1), (1, 3)} trên A = {1, 2, 3}.

<details>
<summary>Đáp án</summary>

```
    1  2  3
1 [ 0  1  1 ]
2 [ 1  0  0 ]
3 [ 0  0  0 ]
```
</details>

### Bài tập 3: Tìm quan hệ từ ma trận

Cho ma trận quan hệ sau trên A = {a, b, c}:
```
   a  b  c
a [1 0 1]
b [0 1 0]
c [0 1 1]
```

Liệt kê các cặp của R.

<details>
<summary>Đáp án</summary>

R = {(a, a), (a, c), (b, b), (c, b), (c, c)}
</details>

## Tóm tắt

- **Quan hệ** R từ A đến B là tập con của A × B
- Biểu diễn: **liệt kê**, **mô tả**, **ma trận**, **đồ thị có hướng**
- **Quan hệ trên A**: R ⊆ A × A
- **Tích Cartesian**: A × B, lực lượng |A| × |B|
- Ứng dụng: cơ sở dữ liệu quan hệ (SQL JOIN), đồ thị, mạng xã hội

Trong bài tiếp theo, chúng ta sẽ xem xét bốn tính chất cơ bản của quan hệ: phản xạ, đối xứng, phản đối xứng, và bắc cầu -- chìa khóa để phân loại quan hệ.
