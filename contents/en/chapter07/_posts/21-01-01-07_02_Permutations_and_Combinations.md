---
layout: post
title: "Hoán vị và Tổ hợp"
categories: chapter07
date: 2021-01-01
order: 2
required: true
lang: vi
---

# Hoán vị và Tổ hợp

Hoán vị và tổ hợp là hai khái niệm cốt lõi trong tổ hợp học, giúp chúng ta đếm số cách sắp xếp và chọn lựa các đối tượng. Đây là nền tảng cho nhiều ứng dụng trong khoa học máy tính và toán học.

## Giai thừa (Factorial)

Trước khi học hoán vị và tổ hợp, chúng ta cần hiểu về giai thừa.

**Định nghĩa**: n! = n × (n-1) × (n-2) × ... × 2 × 1

**Quy ước**: 0! = 1

**Ví dụ**:
- 3! = 3 × 2 × 1 = 6
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 0! = 1

### Tính chất của giai thừa
- n! = n × (n-1)!
- n! tăng rất nhanh: 10! = 3,628,800

## Hoán vị (Permutations)

**Định nghĩa**: Hoán vị là cách sắp xếp các đối tượng theo một thứ tự nhất định.

### 1. Hoán vị không lặp

#### Hoán vị của n đối tượng
**Công thức**: P(n) = n!

**Ví dụ**: Có bao nhiêu cách sắp xếp 4 người ngồi thành hàng?
**Giải**: P(4) = 4! = 24 cách

#### Hoán vị chập k của n đối tượng
**Công thức**: P(n,k) = n!/(n-k)!

**Ý nghĩa**: Chọn k đối tượng từ n đối tượng và sắp xếp chúng.

**Ví dụ**: Có 10 học sinh, chọn 3 em để xếp thành hàng. Có bao nhiêu cách?
**Giải**: P(10,3) = 10!/(10-3)! = 10!/7! = 10 × 9 × 8 = 720 cách

### 2. Hoán vị có lặp

Khi có các đối tượng giống nhau, ta sử dụng công thức:

**Công thức**: n!/(n₁! × n₂! × ... × nₖ!)

Trong đó:
- n: tổng số đối tượng
- nᵢ: số đối tượng loại thứ i

**Ví dụ**: Có bao nhiêu cách sắp xếp các chữ cái trong từ "BANANA"?
**Giải**: 
- Tổng: 6 chữ cái
- B: 1, A: 3, N: 2
- Kết quả: 6!/(1! × 3! × 2!) = 720/(1 × 6 × 2) = 60 cách

## Tổ hợp (Combinations)

**Định nghĩa**: Tổ hợp là cách chọn các đối tượng mà không quan tâm đến thứ tự.

### Tổ hợp chập k của n đối tượng

**Công thức**: C(n,k) = n!/(k!(n-k)!) = (n choose k)

**Ký hiệu khác**: $\binom{n}{k}$, $C_n^k$

**Ví dụ**: Từ 10 học sinh, chọn 3 em để tham gia đội tuyển. Có bao nhiêu cách?
**Giải**: C(10,3) = 10!/(3!×7!) = (10×9×8)/(3×2×1) = 120 cách

## Công cụ tương tác: Máy tính Hoán vị và Tổ hợp

<div id="combinatorics-calculator" class="interactive-tool">
    <h4>🧮 Máy tính Hoán vị và Tổ hợp</h4>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
        <div>
            <label><strong>Loại tính toán:</strong></label>
            <select id="calc-type" onchange="updateCalculatorInterface()" style="width: 100%; padding: 8px; margin-top: 5px;">
                <option value="factorial">Giai thừa (n!)</option>
                <option value="permutation">Hoán vị P(n,k)</option>
                <option value="permutation-repeat">Hoán vị có lặp</option>
                <option value="combination">Tổ hợp C(n,k)</option>
            </select>
        </div>
        <div id="quick-examples" style="background: #f8f9fa; padding: 10px; border-radius: 6px; font-size: 0.9em;">
            <!-- Ví dụ nhanh sẽ được cập nhật -->
        </div>
    </div>
    
    <div id="calculator-inputs">
        <!-- Interface sẽ được tạo động -->
    </div>
    
    <button onclick="calculateCombinatorics()" style="width: 100%; margin: 20px 0; padding: 12px; background: #28a745; color: white; border: none; border-radius: 6px; font-weight: bold;">
        Tính toán
    </button>
    
    <div id="combinatorics-result" style="background: white; padding: 20px; border-radius: 8px; border: 1px solid #dee2e6;">
        <p style="color: #666; text-align: center; margin: 0;">Chọn loại tính toán và nhập dữ liệu</p>
    </div>
    
    <div id="formula-explanation" style="margin-top: 20px; background: #e3f2fd; padding: 15px; border-radius: 8px; display: none;">
        <h5>📐 Công thức và Giải thích:</h5>
        <div id="formula-details"></div>
    </div>
</div>

<script>
function updateCalculatorInterface() {
    const calcType = document.getElementById('calc-type').value;
    const inputsDiv = document.getElementById('calculator-inputs');
    const examplesDiv = document.getElementById('quick-examples');
    
    switch(calcType) {
        case 'factorial':
            inputsDiv.innerHTML = `
                <div style="margin-bottom: 15px;">
                    <label>Nhập n:</label>
                    <input type="number" id="n-factorial" min="0" max="20" value="5" style="width: 100%; padding: 8px; margin-top: 5px;">
                    <small style="color: #666;">Giới hạn: 0 ≤ n ≤ 20</small>
                </div>
            `;
            examplesDiv.innerHTML = `
                <strong>Ví dụ:</strong><br>
                5! = 5×4×3×2×1 = 120<br>
                0! = 1 (quy ước)
            `;
            break;
            
        case 'permutation':
            inputsDiv.innerHTML = `
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                    <div>
                        <label>Tổng số đối tượng (n):</label>
                        <input type="number" id="n-perm" min="0" max="20" value="10" style="width: 100%; padding: 8px; margin-top: 5px;">
                    </div>
                    <div>
                        <label>Số đối tượng chọn (k):</label>
                        <input type="number" id="k-perm" min="0" max="20" value="3" style="width: 100%; padding: 8px; margin-top: 5px;">
                    </div>
                </div>
                <small style="color: #666; display: block; margin-top: 5px;">Điều kiện: 0 ≤ k ≤ n ≤ 20</small>
            `;
            examplesDiv.innerHTML = `
                <strong>Ví dụ:</strong><br>
                P(5,3) = 5!/(5-3)! = 60<br>
                Chọn 3 từ 5 và sắp xếp
            `;
            break;
            
        case 'permutation-repeat':
            inputsDiv.innerHTML = `
                <div style="margin-bottom: 15px;">
                    <label>Tổng số đối tượng (n):</label>
                    <input type="number" id="n-repeat" min="1" max="15" value="6" style="width: 100%; padding: 8px; margin-top: 5px;">
                </div>
                <div style="margin-bottom: 15px;">
                    <label>Số lượng từng loại (cách nhau bởi dấu phẩy):</label>
                    <input type="text" id="repeat-counts" placeholder="1,3,2" value="1,3,2" style="width: 100%; padding: 8px; margin-top: 5px;">
                    <small style="color: #666;">Ví dụ: 1,3,2 có nghĩa là loại 1 có 1 cái, loại 2 có 3 cái, loại 3 có 2 cái</small>
                </div>
            `;
            examplesDiv.innerHTML = `
                <strong>Ví dụ:</strong><br>
                BANANA: 6!/(1!×3!×2!)<br>
                B:1, A:3, N:2
            `;
            break;
            
        case 'combination':
            inputsDiv.innerHTML = `
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                    <div>
                        <label>Tổng số đối tượng (n):</label>
                        <input type="number" id="n-comb" min="0" max="20" value="10" style="width: 100%; padding: 8px; margin-top: 5px;">
                    </div>
                    <div>
                        <label>Số đối tượng chọn (k):</label>
                        <input type="number" id="k-comb" min="0" max="20" value="3" style="width: 100%; padding: 8px; margin-top: 5px;">
                    </div>
                </div>
                <small style="color: #666; display: block; margin-top: 5px;">Điều kiện: 0 ≤ k ≤ n ≤ 20</small>
            `;
            examplesDiv.innerHTML = `
                <strong>Ví dụ:</strong><br>
                C(5,3) = 5!/(3!×2!) = 10<br>
                Chọn 3 từ 5, không sắp xếp
            `;
            break;
    }
}

function factorial(n) {
    if (n <= 1) return 1;
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

function calculateCombinatorics() {
    const calcType = document.getElementById('calc-type').value;
    const resultDiv = document.getElementById('combinatorics-result');
    const explanationDiv = document.getElementById('formula-explanation');
    const formulaDiv = document.getElementById('formula-details');
    
    let result = 0;
    let formula = '';
    let calculation = '';
    let explanation = '';
    
    try {
        switch(calcType) {
            case 'factorial':
                const n = parseInt(document.getElementById('n-factorial').value);
                if (isNaN(n) || n < 0 || n > 20) throw new Error('n phải là số nguyên từ 0 đến 20');
                
                result = factorial(n);
                formula = `${n}!`;
                calculation = n <= 5 ? 
                    `${n}! = ${Array.from({length: n}, (_, i) => n - i).join(' × ')} = ${result}` :
                    `${n}! = ${result.toLocaleString()}`;
                explanation = `Giai thừa của ${n} là tích của tất cả số nguyên dương từ 1 đến ${n}.`;
                break;
                
            case 'permutation':
                const nPerm = parseInt(document.getElementById('n-perm').value);
                const kPerm = parseInt(document.getElementById('k-perm').value);
                
                if (isNaN(nPerm) || isNaN(kPerm) || nPerm < 0 || kPerm < 0 || kPerm > nPerm || nPerm > 20) {
                    throw new Error('Điều kiện: 0 ≤ k ≤ n ≤ 20');
                }
                
                result = factorial(nPerm) / factorial(nPerm - kPerm);
                formula = `P(${nPerm},${kPerm}) = ${nPerm}!/(${nPerm}-${kPerm})!`;
                calculation = `P(${nPerm},${kPerm}) = ${nPerm}!/${nPerm - kPerm}! = ${factorial(nPerm).toLocaleString()}/${factorial(nPerm - kPerm).toLocaleString()} = ${result.toLocaleString()}`;
                explanation = `Số cách chọn ${kPerm} đối tượng từ ${nPerm} đối tượng và sắp xếp chúng theo thứ tự.`;
                break;
                
            case 'permutation-repeat':
                const nRepeat = parseInt(document.getElementById('n-repeat').value);
                const counts = document.getElementById('repeat-counts').value
                    .split(',').map(x => parseInt(x.trim())).filter(x => !isNaN(x) && x > 0);
                
                if (isNaN(nRepeat) || nRepeat <= 0 || counts.length === 0) {
                    throw new Error('Vui lòng nhập dữ liệu hợp lệ');
                }
                
                const totalCounts = counts.reduce((sum, count) => sum + count, 0);
                if (totalCounts !== nRepeat) {
                    throw new Error(`Tổng số lượng (${totalCounts}) phải bằng n (${nRepeat})`);
                }
                
                const denominator = counts.reduce((product, count) => product * factorial(count), 1);
                result = factorial(nRepeat) / denominator;
                
                formula = `${nRepeat}!/(${counts.map(c => c + '!').join(' × ')})`;
                calculation = `${nRepeat}!/(${counts.map(c => c + '!').join(' × ')}) = ${factorial(nRepeat).toLocaleString()}/${denominator.toLocaleString()} = ${result.toLocaleString()}`;
                explanation = `Số cách sắp xếp ${nRepeat} đối tượng khi có ${counts.length} loại khác nhau với số lượng tương ứng là ${counts.join(', ')}.`;
                break;
                
            case 'combination':
                const nComb = parseInt(document.getElementById('n-comb').value);
                const kComb = parseInt(document.getElementById('k-comb').value);
                
                if (isNaN(nComb) || isNaN(kComb) || nComb < 0 || kComb < 0 || kComb > nComb || nComb > 20) {
                    throw new Error('Điều kiện: 0 ≤ k ≤ n ≤ 20');
                }
                
                result = factorial(nComb) / (factorial(kComb) * factorial(nComb - kComb));
                formula = `C(${nComb},${kComb}) = ${nComb}!/(${kComb}! × ${nComb - kComb}!)`;
                calculation = `C(${nComb},${kComb}) = ${nComb}!/(${kComb}! × ${nComb - kComb}!) = ${factorial(nComb).toLocaleString()}/(${factorial(kComb).toLocaleString()} × ${factorial(nComb - kComb).toLocaleString()}) = ${result.toLocaleString()}`;
                explanation = `Số cách chọn ${kComb} đối tượng từ ${nComb} đối tượng mà không quan tâm đến thứ tự.`;
                break;
        }
        
        // Display result
        resultDiv.innerHTML = `
            <div style="text-align: center;">
                <h5 style="color: #495057; margin-bottom: 15px;">Kết quả</h5>
                <div style="font-size: 2.5em; color: #28a745; font-weight: bold; margin: 15px 0;">
                    ${result.toLocaleString()}
                </div>
                <div style="color: #666; font-size: 1.1em; margin: 10px 0;">
                    ${formula}
                </div>
            </div>
        `;
        
        // Display formula explanation
        formulaDiv.innerHTML = `
            <div style="background: white; padding: 15px; border-radius: 6px; margin-bottom: 10px;">
                <strong>Công thức:</strong> ${formula}
            </div>
            <div style="background: white; padding: 15px; border-radius: 6px; margin-bottom: 10px;">
                <strong>Tính toán:</strong> ${calculation}
            </div>
            <div style="background: white; padding: 15px; border-radius: 6px;">
                <strong>Giải thích:</strong> ${explanation}
            </div>
        `;
        explanationDiv.style.display = 'block';
        
    } catch (error) {
        resultDiv.innerHTML = `<p style="color: #dc3545; text-align: center; margin: 0;">Lỗi: ${error.message}</p>`;
        explanationDiv.style.display = 'none';
    }
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    updateCalculatorInterface();
});
</script>

## So sánh Hoán vị và Tổ hợp

| Khía cạnh | Hoán vị | Tổ hợp |
|-----------|---------|--------|
| **Thứ tự** | Quan trọng | Không quan trọng |
| **Công thức** | P(n,k) = n!/(n-k)! | C(n,k) = n!/(k!(n-k)!) |
| **Ví dụ** | Sắp xếp học sinh | Chọn đội tuyển |
| **Kết quả** | P(n,k) ≥ C(n,k) | C(n,k) ≤ P(n,k) |

### Mối quan hệ
P(n,k) = k! × C(n,k)

**Giải thích**: Mỗi tổ hợp có thể sắp xếp thành k! hoán vị.

## Tính chất của Tổ hợp

### 1. Tính đối xứng
C(n,k) = C(n,n-k)

**Ví dụ**: C(10,3) = C(10,7) = 120

### 2. Tam giác Pascal
C(n,k) = C(n-1,k-1) + C(n-1,k)

**Tam giác Pascal**:
```
        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1
```

### 3. Tổng các tổ hợp
∑(k=0 to n) C(n,k) = 2ⁿ

**Ví dụ**: C(3,0) + C(3,1) + C(3,2) + C(3,3) = 1 + 3 + 3 + 1 = 8 = 2³

## Ứng dụng trong Khoa học Máy tính

### 1. Thuật toán tìm kiếm
```python
def binary_search_complexity(n):
    """Độ phức tạp tìm kiếm nhị phân"""
    # Số lần chia đôi tối đa
    return math.ceil(math.log2(n))

def combination_search(items, k):
    """Tìm tất cả tổ hợp k phần tử"""
    # Số tổ hợp cần kiểm tra
    return math.comb(len(items), k)
```

### 2. Mật mã học
```python
def brute_force_time(password_length, charset_size):
    """Thời gian brute force mật khẩu"""
    # Số mật khẩu có thể: charset_size^password_length
    total_passwords = charset_size ** password_length
    return total_passwords / (2 * 1000000)  # Giây (1M mật khẩu/giây)

def key_combinations(key_bits):
    """Số khóa mã hóa có thể"""
    return 2 ** key_bits
```

### 3. Phân tích thuật toán
```python
def subset_generation(n):
    """Số tập con của tập n phần tử"""
    return 2 ** n  # Mỗi phần tử có 2 lựa chọn: có hoặc không

def permutation_sort_complexity(n):
    """Độ phức tạp worst-case của permutation sort"""
    return factorial(n)  # Kiểm tra tất cả hoán vị
```

## Bài tập thực hành

### Bài tập 1: Giai thừa
1. Tính: 7!, 0!, 1!
2. So sánh: 10! và 3⁶
3. Tìm n sao cho n! > 1000

### Bài tập 2: Hoán vị
1. Có bao nhiêu cách sắp xếp 6 cuốn sách trên kệ?
2. Từ 8 học sinh, chọn 3 em làm lớp trường, lớp phó, thư ký. Có bao nhiêu cách?
3. Có bao nhiêu cách sắp xếp chữ cái trong từ "COMPUTER"?

### Bài tập 3: Tổ hợp
1. Từ 12 người, chọn 5 người vào đội bóng. Có bao nhiêu cách?
2. Một hộp có 10 bi đỏ và 8 bi xanh. Chọn 4 bi bất kỳ. Có bao nhiêu cách?
3. Chứng minh: C(n,0) + C(n,1) + ... + C(n,n) = 2ⁿ

### Bài tập 4: Ứng dụng
1. Một mật khẩu gồm 8 ký tự (chữ và số). Có bao nhiêu mật khẩu khác nhau?
2. Trong một lớp 30 học sinh, chọn 1 lớp trưởng và 2 lớp phó. Có bao nhiêu cách?
3. Tạo đội tuyển 11 người từ 20 cầu thủ, trong đó có 1 thủ môn cố định. Có bao nhiêu cách chọn 10 người còn lại?

<details>
<summary>Đáp án</summary>

**Bài tập 1:**
1. 7! = 5,040; 0! = 1; 1! = 1
2. 10! = 3,628,800 > 3⁶ = 729
3. n = 7 (vì 6! = 720 < 1000 < 5040 = 7!)

**Bài tập 2:**
1. 6! = 720 cách
2. P(8,3) = 8!/(8-3)! = 336 cách
3. 8! = 40,320 cách (tất cả chữ cái khác nhau)

**Bài tập 3:**
1. C(12,5) = 792 cách
2. C(18,4) = 3,060 cách
3. Sử dụng khai triển nhị thức (1+1)ⁿ = 2ⁿ

**Bài tập 4:**
1. 36⁸ ≈ 2.8 × 10¹² mật khẩu
2. 30 × C(29,2) = 30 × 406 = 12,180 cách
3. C(19,10) = 92,378 cách

</details>

## Tóm tắt

**Giai thừa**: n! = n × (n-1) × ... × 1
- Cơ sở cho hoán vị và tổ hợp

**Hoán vị**: Sắp xếp có thứ tự
- P(n,k) = n!/(n-k)!
- Quan tâm đến thứ tự

**Tổ hợp**: Chọn lựa không thứ tự  
- C(n,k) = n!/(k!(n-k)!)
- Không quan tâm đến thứ tự

**Ứng dụng**: Mật mã, thuật toán, phân tích độ phức tạp

Trong bài tiếp theo, chúng ta sẽ học về **Nguyên lý Bao hàm-Loại trừ** - công cụ mạnh mẽ để đếm các tập hợp có giao nhau.
