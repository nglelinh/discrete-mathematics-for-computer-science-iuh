---
layout: post
title: "Quy tắc Cộng và Nhân"
categories: chapter07
date: 2021-01-01
order: 1
required: true
lang: en
---

# Quy tắc Cộng và Nhân

Một hệ thống có bao nhiêu cách đăng nhập, một bộ mật khẩu có bao nhiêu khả năng, một thuật toán sinh ra bao nhiêu cấu hình, đó đều là các câu hỏi đếm. Trước khi học những công thức phức tạp hơn, ta cần nắm hai nguyên tắc nền tảng nhất của tổ hợp.


Các quy tắc đếm cho ta cách ước lượng số cấu hình có thể xảy ra mà không cần liệt kê hết, đây là kỹ năng rất gần với phân tích thuật toán và kiểm thử.
**Quy tắc cộng** áp dụng khi các lựa chọn loại trừ nhau. **Quy tắc nhân** áp dụng khi một quá trình gồm nhiều bước nối tiếp. Hai ý tưởng này nghe rất cơ bản, nhưng chúng là khung xương cho hầu hết bài toán đếm sau này.

Nhiều sai lầm xảy ra không phải vì công thức khó, mà vì đọc sai cấu trúc của bài toán. Lúc nào là "hoặc", lúc nào là "và", các trường hợp có giao nhau hay không, đó mới là phần quyết định.

Trong bài này, chúng ta sẽ luyện cách nhìn bài toán đếm qua cấu trúc lựa chọn, rồi dùng quy tắc cộng và nhân để biến những tình huống thực tế thành phép đếm rõ ràng.

## Quy tắc Cộng (Addition Principle)

**Nguyên lý**: Nếu một tác vụ có thể được thực hiện theo m cách hoặc theo n cách (không trùng lặp), thì tổng số cách thực hiện tác vụ là m + n.

### Định nghĩa chính thức
Nếu A và B là hai tập hợp rời nhau (A ∩ B = ∅), thì |A ∪ B| = |A| + |B|.

### Ví dụ 1: Chọn môn học
Một sinh viên có thể chọn:
- 3 môn toán học: Giải tích, Đại số, Hình học
- 2 môn tin học: Lập trình, Cấu trúc dữ liệu

**Hỏi**: Có bao nhiêu cách chọn 1 môn học?
**Đáp án**: 3 + 2 = 5 cách

### Ví dụ 2: Đi từ A đến C
Từ thành phố A đến C có thể đi:
- Đường bộ: 4 tuyến đường
- Đường hàng không: 2 chuyến bay
- Đường thủy: 1 tuyến tàu

**Tổng số cách**: 4 + 2 + 1 = 7 cách

## Quy tắc Nhân (Multiplication Principle)

**Nguyên lý**: Nếu một tác vụ gồm k bước liên tiếp, bước thứ i có nᵢ cách thực hiện, thì tổng số cách thực hiện tác vụ là n₁ × n₂ × ... × nₖ.

### Ví dụ 3: Tạo mật khẩu
Tạo mật khẩu gồm:
- Ký tự đầu: 1 trong 26 chữ cái
- Ký tự thứ 2: 1 trong 10 chữ số
- Ký tự thứ 3: 1 trong 26 chữ cái

**Tổng số mật khẩu**: 26 × 10 × 26 = 6,760 mật khẩu

### Ví dụ 4: Đi từ A đến C qua B
- Từ A đến B: 3 cách
- Từ B đến C: 4 cách

**Tổng số cách đi từ A đến C qua B**: 3 × 4 = 12 cách

## Tích Descartes (Cartesian Product)

Tích Descartes là một khái niệm quan trọng kết nối lý thuyết tập hợp với quy tắc nhân.

### Định nghĩa

Tích Descartes của hai tập hợp A và B, ký hiệu A × B, là tập hợp tất cả các cặp có thứ tự (a, b) với a ∈ A và b ∈ B.

$$A \times B = \{(a, b) \;|\; a \in A, b \in B\}$$

### Công thức về lực lượng

Nếu |A| = m và |B| = n, thì |A × B| = m × n.

Tổng quát hơn, tích Descartes của k tập hợp A₁ × A₂ × ... × Aₖ có lực lượng:

$$|A_1 \times A_2 \times \cdots \times A_k| = |A_1| \times |A_2| \times \cdots \times |A_k|$$

### Ví dụ 5: Tích Descartes của hai tập hợp

Cho A = {a, b, c} và B = {1, 2}. Tìm A × B.

**Giải**: A × B = {(a,1), (a,2), (b,1), (b,2), (c,1), (c,2)}. Có 3 × 2 = 6 phần tử.

### Ví dụ 6: Mã sinh viên

Một trường đại học tạo mã sinh viên gồm 2 chữ cái in hoa (A-Z) và 3 chữ số (0-9). Hỏi có bao nhiêu mã khác nhau?

**Giải**: Gọi A là tập 26 chữ cái, B là tập 10 chữ số. Mỗi mã là một phần tử của A × A × B × B × B. Số mã là 26 × 26 × 10 × 10 × 10 = 676.000.

### Mối liên hệ với quy tắc nhân

Quy tắc nhân thực chất là hệ quả trực tiếp của công thức tính lực lượng tích Descartes. Khi một tác vụ gồm k bước, với bước thứ i có nᵢ cách thực hiện, ta có thể xem mỗi cách thực hiện toàn bộ tác vụ là một phần tử của tích Descartes của k tập hợp, trong đó tập thứ i có nᵢ phần tử.

## Nguyên lý Chuồng Bồ câu (Pigeonhole Principle)

**Nguyên lý**: Nếu có $$n$$ vật thể đặt vào $$m$$ hộp, với $$n > m$$, thì ít nhất một hộp chứa từ 2 vật thể trở lên.

$$n > m \implies \exists \text{ hộp chứa } \geq 2 \text{ vật}$$

**Ví dụ 1**: Trong một lớp có 13 sinh viên, có ít nhất 2 sinh viên sinh cùng tháng (vì 13 > 12 tháng).

**Ví dụ 2**: Trong một nhóm 367 người, có ít nhất 2 người có cùng ngày sinh (vì 367 > 366 ngày trong năm).

**Nguyên lý tổng quát**: Nếu có $$n$$ vật thể đặt vào $$m$$ hộp, thì ít nhất một hộp chứa từ $$\lceil n/m \rceil$$ vật thể trở lên.

**Ví dụ 3**: Nếu có 100 sinh viên làm 3 bài kiểm tra, có ít nhất $$\lceil 100/3 \rceil = 34$$ sinh viên có cùng số bài đạt yêu cầu.

<div class="content-box example-box" markdown="1">
**Ví dụ 4 - Ứng dụng trong CS**: Một mảng gồm 10 số nguyên. Chứng minh rằng tồn tại hai phần tử có hiệu chia hết cho 9.

**Giải**: Khi chia một số nguyên cho 9, số dư chỉ có thể là 0, 1, ..., 8 (9 loại). Với 10 số, theo nguyên lý chuồng bồ câu, có ít nhất hai số cùng số dư khi chia cho 9. Hiệu của chúng chia hết cho 9.
</div>

## Công cụ tương tác: Máy tính Quy tắc Đếm

Nếu dùng công cụ này, hãy dự đoán kết quả trước rồi mới thao tác. Việc so sánh dự đoán với kết quả thật sẽ giúp khái niệm bám chắc hơn.

<div id="counting-calculator" class="interactive-tool">
    <h4>🧮 Máy tính Quy tắc Đếm</h4>
    
    <div style="margin-bottom: 20px;">
        <label><strong>Chọn loại bài toán:</strong></label>
        <select id="problem-type" onchange="updateProblemInterface()" style="width: 100%; padding: 8px; margin-top: 5px;">
            <option value="addition">Quy tắc Cộng</option>
            <option value="multiplication">Quy tắc Nhân</option>
            <option value="mixed">Kết hợp Cộng và Nhân</option>
        </select>
    </div>
    
    <div id="problem-interface">
        <!-- Interface sẽ được tạo động -->
    </div>
    
    <button onclick="calculateResult()" style="width: 100%; margin: 20px 0; padding: 12px; background: #007bff; color: white; border: none; border-radius: 6px; font-weight: bold;">
        Tính toán
    </button>
    
    <div id="calculation-result" style="background: white; padding: 20px; border-radius: 8px; border: 1px solid #dee2e6;">
        <p style="color: #666; text-align: center; margin: 0;">Chọn loại bài toán và nhập dữ liệu</p>
    </div>
    
    <div id="step-by-step" style="margin-top: 20px; background: #f8f9fa; padding: 15px; border-radius: 8px; display: none;">
        <h5>📝 Giải chi tiết:</h5>
        <div id="solution-steps"></div>
    </div>
</div>

<script>
function updateProblemInterface() {
    const problemType = document.getElementById('problem-type').value;
    const interfaceDiv = document.getElementById('problem-interface');
    
    switch(problemType) {
        case 'addition':
            interfaceDiv.innerHTML = `
                <div style="background: #e8f4fd; padding: 15px; border-radius: 6px; margin-bottom: 15px;">
                    <strong>Quy tắc Cộng:</strong> Đếm số cách thực hiện khi có nhiều lựa chọn độc lập
                </div>
                <div style="margin-bottom: 15px;">
                    <label>Số lựa chọn (cách nhau bởi dấu phẩy):</label>
                    <input type="text" id="addition-choices" placeholder="3,2,4,1" style="width: 100%; padding: 8px; margin-top: 5px;">
                    <small style="color: #666;">Ví dụ: 3,2,4,1 có nghĩa là có 3 cách cho lựa chọn 1, 2 cách cho lựa chọn 2, v.v.</small>
                </div>
            `;
            break;
            
        case 'multiplication':
            interfaceDiv.innerHTML = `
                <div style="background: #fff3cd; padding: 15px; border-radius: 6px; margin-bottom: 15px;">
                    <strong>Quy tắc Nhân:</strong> Đếm số cách thực hiện khi có nhiều bước liên tiếp
                </div>
                <div style="margin-bottom: 15px;">
                    <label>Số cách cho mỗi bước (cách nhau bởi dấu phẩy):</label>
                    <input type="text" id="multiplication-steps" placeholder="26,10,26" style="width: 100%; padding: 8px; margin-top: 5px;">
                    <small style="color: #666;">Ví dụ: 26,10,26 có nghĩa là bước 1 có 26 cách, bước 2 có 10 cách, bước 3 có 26 cách</small>
                </div>
            `;
            break;
            
        case 'mixed':
            interfaceDiv.innerHTML = `
                <div style="background: #d4edda; padding: 15px; border-radius: 6px; margin-bottom: 15px;">
                    <strong>Kết hợp:</strong> Sử dụng cả quy tắc cộng và nhân
                </div>
                <div style="margin-bottom: 15px;">
                    <label>Mô tả bài toán:</label>
                    <select id="mixed-example" style="width: 100%; padding: 8px; margin-top: 5px;">
                        <option value="travel">Đi từ A đến C (qua B hoặc trực tiếp)</option>
                        <option value="password">Tạo mật khẩu với nhiều định dạng</option>
                        <option value="menu">Chọn món ăn từ menu</option>
                    </select>
                </div>
                <div id="mixed-parameters">
                    <!-- Sẽ được cập nhật dựa trên lựa chọn -->
                </div>
            `;
            updateMixedParameters();
            break;
    }
}

function updateMixedParameters() {
    const example = document.getElementById('mixed-example')?.value;
    const parametersDiv = document.getElementById('mixed-parameters');
    
    if (!parametersDiv) return;
    
    switch(example) {
        case 'travel':
            parametersDiv.innerHTML = `
                <div style="margin-bottom: 10px;">
                    <label>Từ A đến B:</label>
                    <input type="number" id="a-to-b" value="3" style="width: 100%; padding: 6px;">
                </div>
                <div style="margin-bottom: 10px;">
                    <label>Từ B đến C:</label>
                    <input type="number" id="b-to-c" value="4" style="width: 100%; padding: 6px;">
                </div>
                <div style="margin-bottom: 10px;">
                    <label>Từ A trực tiếp đến C:</label>
                    <input type="number" id="a-to-c" value="2" style="width: 100%; padding: 6px;">
                </div>
            `;
            break;
            
        case 'password':
            parametersDiv.innerHTML = `
                <div style="margin-bottom: 10px;">
                    <label>Định dạng 1 - Chữ cái + Số:</label>
                    <input type="text" id="format1" value="26,10" style="width: 100%; padding: 6px;">
                </div>
                <div style="margin-bottom: 10px;">
                    <label>Định dạng 2 - Số + Chữ cái + Số:</label>
                    <input type="text" id="format2" value="10,26,10" style="width: 100%; padding: 6px;">
                </div>
            `;
            break;
            
        case 'menu':
            parametersDiv.innerHTML = `
                <div style="margin-bottom: 10px;">
                    <label>Món khai vị:</label>
                    <input type="number" id="appetizer" value="5" style="width: 100%; padding: 6px;">
                </div>
                <div style="margin-bottom: 10px;">
                    <label>Món chính:</label>
                    <input type="number" id="main" value="8" style="width: 100%; padding: 6px;">
                </div>
                <div style="margin-bottom: 10px;">
                    <label>Món tráng miệng:</label>
                    <input type="number" id="dessert" value="4" style="width: 100%; padding: 6px;">
                </div>
            `;
            break;
    }
}

function calculateResult() {
    const problemType = document.getElementById('problem-type').value;
    const resultDiv = document.getElementById('calculation-result');
    const stepsDiv = document.getElementById('step-by-step');
    const solutionDiv = document.getElementById('solution-steps');
    
    let result = 0;
    let steps = [];
    
    try {
        switch(problemType) {
            case 'addition':
                const choices = document.getElementById('addition-choices').value
                    .split(',').map(x => parseInt(x.trim())).filter(x => !isNaN(x));
                
                if (choices.length === 0) throw new Error('Vui lòng nhập số lựa chọn hợp lệ');
                
                result = choices.reduce((sum, choice) => sum + choice, 0);
                steps = [
                    'Áp dụng quy tắc cộng:',
                    `Tổng số cách = ${choices.join(' + ')}`,
                    `= ${result} cách`
                ];
                break;
                
            case 'multiplication':
                const stepCounts = document.getElementById('multiplication-steps').value
                    .split(',').map(x => parseInt(x.trim())).filter(x => !isNaN(x));
                
                if (stepCounts.length === 0) throw new Error('Vui lòng nhập số bước hợp lệ');
                
                result = stepCounts.reduce((product, count) => product * count, 1);
                steps = [
                    'Áp dụng quy tắc nhân:',
                    `Tổng số cách = ${stepCounts.join(' × ')}`,
                    `= ${result} cách`
                ];
                break;
                
            case 'mixed':
                const example = document.getElementById('mixed-example').value;
                switch(example) {
                    case 'travel':
                        const aToB = parseInt(document.getElementById('a-to-b').value) || 0;
                        const bToC = parseInt(document.getElementById('b-to-c').value) || 0;
                        const aToC = parseInt(document.getElementById('a-to-c').value) || 0;
                        
                        const viaB = aToB * bToC;
                        result = viaB + aToC;
                        
                        steps = [
                            'Phân tích bài toán:',
                            '• Đi qua B: Áp dụng quy tắc nhân',
                            `  Số cách = ${aToB} × ${bToC} = ${viaB} cách`,
                            '• Đi trực tiếp: ' + aToC + ' cách',
                            '• Tổng cộng: Áp dụng quy tắc cộng',
                            `  Tổng số cách = ${viaB} + ${aToC} = ${result} cách`
                        ];
                        break;
                        
                    case 'password':
                        const format1 = document.getElementById('format1').value
                            .split(',').map(x => parseInt(x.trim()));
                        const format2 = document.getElementById('format2').value
                            .split(',').map(x => parseInt(x.trim()));
                        
                        const count1 = format1.reduce((p, c) => p * c, 1);
                        const count2 = format2.reduce((p, c) => p * c, 1);
                        result = count1 + count2;
                        
                        steps = [
                            'Tính số mật khẩu cho mỗi định dạng:',
                            `• Định dạng 1: ${format1.join(' × ')} = ${count1}`,
                            `• Định dạng 2: ${format2.join(' × ')} = ${count2}`,
                            'Tổng số mật khẩu:',
                            `${count1} + ${count2} = ${result} mật khẩu`
                        ];
                        break;
                        
                    case 'menu':
                        const appetizer = parseInt(document.getElementById('appetizer').value) || 0;
                        const main = parseInt(document.getElementById('main').value) || 0;
                        const dessert = parseInt(document.getElementById('dessert').value) || 0;
                        
                        result = appetizer * main * dessert;
                        steps = [
                            'Chọn thực đơn gồm 3 món:',
                            'Áp dụng quy tắc nhân:',
                            `Số cách chọn = ${appetizer} × ${main} × ${dessert}`,
                            `= ${result} cách`
                        ];
                        break;
                }
                break;
        }
        
        // Display result
        resultDiv.innerHTML = `
            <div style="text-align: center;">
                <h5 style="color: #495057; margin-bottom: 15px;">Kết quả</h5>
                <div style="font-size: 2em; color: #007bff; font-weight: bold; margin: 15px 0;">
                    ${result.toLocaleString()} cách
                </div>
                <div style="color: #666; font-size: 0.9em;">
                    ${problemType === 'addition' ? 'Quy tắc Cộng' : 
                      problemType === 'multiplication' ? 'Quy tắc Nhân' : 'Kết hợp Cộng và Nhân'}
                </div>
            </div>
        `;
        
        // Display steps
        solutionDiv.innerHTML = steps.map(step => 
            `<div style="margin: 8px 0; padding: 8px; background: white; border-left: 3px solid #007bff; border-radius: 3px;">${step}</div>`
        ).join('');
        stepsDiv.style.display = 'block';
        
    } catch (error) {
        resultDiv.innerHTML = `<p style="color: #dc3545; text-align: center; margin: 0;">Lỗi: ${error.message}</p>`;
        stepsDiv.style.display = 'none';
    }
}

// Initialize interface
document.addEventListener('DOMContentLoaded', () => {
    updateProblemInterface();
    
    // Add event listener for mixed example changes
    document.addEventListener('change', (e) => {
        if (e.target.id === 'mixed-example') {
            updateMixedParameters();
        }
    });
});
</script>

## Kết hợp Quy tắc Cộng và Nhân

Nhiều bài toán thực tế cần kết hợp cả hai quy tắc.

### Ví dụ 5: Đi du lịch
Từ Hà Nội đến Đà Nẵng có thể:
- **Bay trực tiếp**: 3 chuyến bay
- **Đi qua TP.HCM**: 
  - Hà Nội → TP.HCM: 4 chuyến bay
  - TP.HCM → Đà Nẵng: 2 chuyến bay

**Giải**:
- Đi qua TP.HCM: 4 × 2 = 8 cách (quy tắc nhân)
- Tổng cộng: 3 + 8 = 11 cách (quy tắc cộng)

### Ví dụ 6: Tạo tài khoản
Một website cho phép tạo username theo 2 định dạng:
- **Định dạng 1**: 1 chữ cái + 3 chữ số
- **Định dạng 2**: 2 chữ cái + 2 chữ số

**Giải**:
- Định dạng 1: 26 × 10 × 10 × 10 = 26,000 username
- Định dạng 2: 26 × 26 × 10 × 10 = 67,600 username
- Tổng cộng: 26,000 + 67,600 = 93,600 username

## Ứng dụng trong Khoa học Máy tính

### 1. Phân tích Thuật toán
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

### 2. Mật mã học
```python
def password_strength(length, charset_size):
    """Tính số mật khẩu có thể tạo"""
    # Mỗi vị trí có charset_size lựa chọn
    # Tổng cộng length vị trí
    return charset_size ** length  # Quy tắc nhân

# Ví dụ: Mật khẩu 8 ký tự, bao gồm chữ và số
strength = password_strength(8, 36)  # 36^8 ≈ 2.8 × 10^12
```

### 3. Cơ sở dữ liệu
```sql
-- Đếm số bản ghi có thể tạo từ các bảng
-- Sử dụng quy tắc nhân cho JOIN
SELECT COUNT(*) FROM 
    (SELECT COUNT(*) as users FROM Users) u,
    (SELECT COUNT(*) as orders FROM Orders) o;
```

## Bài tập thực hành

### Bài tập 1: Quy tắc Cộng
1. Một sinh viên có thể chọn 1 trong 5 môn toán, 1 trong 3 môn lý, hoặc 1 trong 4 môn hóa. Hỏi có bao nhiêu cách chọn?

2. Từ thành phố A đến B có 3 đường bộ, 2 đường sắt, và 1 đường hàng không. Có bao nhiêu cách đi?

### Bài tập 2: Quy tắc Nhân
1. Tạo mã số gồm 2 chữ cái đầu và 3 chữ số cuối. Có bao nhiêu mã số khác nhau?

2. Một bữa ăn gồm 1 món khai vị (4 loại), 1 món chính (6 loại), và 1 món tráng miệng (3 loại). Có bao nhiêu cách chọn thực đơn?

### Bài tập 3: Kết hợp
1. Từ A đến C có thể đi trực tiếp (2 cách) hoặc qua B (A→B có 3 cách, B→C có 4 cách). Tổng cộng có bao nhiêu cách?

2. Tạo mật khẩu theo 2 định dạng:
   - Định dạng 1: 3 chữ cái + 2 chữ số
   - Định dạng 2: 2 chữ số + 3 chữ cái
   
   Có bao nhiêu mật khẩu khác nhau?

<details>
<summary>Đáp án</summary>

**Bài tập 1:**
1. 5 + 3 + 4 = 12 cách
2. 3 + 2 + 1 = 6 cách

**Bài tập 2:**
1. 26 × 26 × 10 × 10 × 10 = 676,000 mã số
2. 4 × 6 × 3 = 72 cách

**Bài tập 3:**
1. 2 + (3 × 4) = 2 + 12 = 14 cách
2. (26³ × 10²) + (10² × 26³) = 1,757,600 + 1,757,600 = 3,515,200 mật khẩu

</details>

