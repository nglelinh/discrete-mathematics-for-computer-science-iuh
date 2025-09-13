---
layout: post
title: "Quy nạp Toán học"
categories: chapter03
date: 2021-01-01
order: 3
required: true
lang: vi
---

# Quy nạp Toán học

Quy nạp toán học là phương pháp chứng minh mạnh mẽ và elegant, đặc biệt hữu ích để chứng minh các mệnh đề về số tự nhiên, dãy số, và cấu trúc rời rạc.

## Nguyên lý quy nạp toán học

**Ý tưởng**: Giống như hiệu ứng domino - nếu viên đầu tiên đổ và mỗi viên đổ kéo theo viên tiếp theo đổ, thì tất cả các viên sẽ đổ.

### Nguyên lý cơ bản:
Để chứng minh P(n) đúng với mọi n ≥ n₀, ta cần:

1. **Bước cơ sở** (Base case): Chứng minh P(n₀) đúng
2. **Bước quy nạp** (Inductive step): Chứng minh P(k) → P(k+1) với mọi k ≥ n₀

### Cơ sở logic:
- P(n₀) ∧ [∀k ≥ n₀: P(k) → P(k+1)] ⟹ ∀n ≥ n₀: P(n)

## Ví dụ 1: Tổng các số tự nhiên

**Định lý**: $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$ với mọi n ≥ 1.

**Chứng minh**:

**Bước cơ sở** (n = 1):
- VT = 1
- VP = $\frac{1(1+1)}{2} = 1$
- VT = VP ✓

**Bước quy nạp**: Giả sử công thức đúng với n = k, tức là:
$$\sum_{i=1}^{k} i = \frac{k(k+1)}{2}$$

Cần chứng minh công thức đúng với n = k+1:
$$\sum_{i=1}^{k+1} i = \sum_{i=1}^{k} i + (k+1) = \frac{k(k+1)}{2} + (k+1)$$

$$= \frac{k(k+1) + 2(k+1)}{2} = \frac{(k+1)(k+2)}{2}$$

Đây chính là công thức với n = k+1 ✓

**Kết luận**: Công thức đúng với mọi n ≥ 1 ∎

## Ví dụ 2: Bất đẳng thức Bernoulli

**Định lý**: $(1 + x)^n ≥ 1 + nx$ với mọi x ≥ -1 và n ∈ ℕ.

**Chứng minh**:

**Bước cơ sở** (n = 1):
- VT = $(1 + x)^1 = 1 + x$
- VP = $1 + 1 \cdot x = 1 + x$
- VT = VP ✓

**Bước quy nạp**: Giả sử $(1 + x)^k ≥ 1 + kx$.

Cần chứng minh $(1 + x)^{k+1} ≥ 1 + (k+1)x$:

$$(1 + x)^{k+1} = (1 + x)^k \cdot (1 + x) ≥ (1 + kx)(1 + x)$$

$$= 1 + x + kx + kx^2 = 1 + (k+1)x + kx^2$$

Vì $x ≥ -1$ nên $1 + x ≥ 0$, và $kx^2 ≥ 0$, do đó:
$$(1 + x)^{k+1} ≥ 1 + (k+1)x$$ ✓

**Kết luận**: Bất đẳng thức đúng với mọi n ∈ ℕ ∎

## Ví dụ 3: Ứng dụng trong khoa học máy tính

**Định lý**: Thuật toán Merge Sort có độ phức tạp O(n log n).

**Chứng minh** (ý tưởng quy nạp):

**Bước cơ sở**: Với n = 1, T(1) = O(1) = O(1 log 1) ✓

**Bước quy nạp**: Giả sử T(k) ≤ c·k log k với mọi k < n.

Với mảng kích thước n:
- Chia thành 2 mảng con kích thước n/2
- Thời gian sắp xếp mỗi mảng con: T(n/2) ≤ c·(n/2)log(n/2)
- Thời gian merge: O(n)

$$T(n) ≤ 2 \cdot c \cdot \frac{n}{2} \log\frac{n}{2} + cn = cn(\log n - 1) + cn = cn \log n$$

Vậy T(n) = O(n log n) ✓

## Quy nạp mạnh (Strong Induction)

Đôi khi ta cần sử dụng **quy nạp mạnh**, trong đó giả thiết quy nạp mạnh hơn:

### Nguyên lý:
Để chứng minh P(n) với mọi n ≥ n₀:
1. **Bước cơ sở**: P(n₀) đúng
2. **Bước quy nạp mạnh**: P(n₀) ∧ P(n₀+1) ∧ ... ∧ P(k) → P(k+1)

### Ví dụ: Định lý cơ bản của số học
**Định lý**: Mọi số nguyên n > 1 đều có thể phân tích thành tích các số nguyên tố.

**Chứng minh**:
**Bước cơ sở**: n = 2 là số nguyên tố ✓

**Bước quy nạp mạnh**: Giả sử mọi số từ 2 đến k đều phân tích được.
- Nếu k+1 là số nguyên tố: xong
- Nếu k+1 hợp số: k+1 = ab với 2 ≤ a, b ≤ k
- Theo giả thiết quy nạp: a và b đều phân tích được
- Vậy k+1 cũng phân tích được ✓

## Công cụ tương tác: Trình tạo chứng minh quy nạp

<div id="induction-builder" style="border: 2px solid #28a745; padding: 20px; margin: 20px 0; border-radius: 8px;">
    <h4>🔢 Công cụ xây dựng chứng minh quy nạp</h4>
    
    <div style="margin-bottom: 15px;">
        <label><strong>Chọn công thức để chứng minh:</strong></label>
        <select id="formula-select" style="width: 100%; padding: 5px; margin-top: 5px;">
            <option value="sum-natural">∑i = n(n+1)/2</option>
            <option value="sum-squares">∑i² = n(n+1)(2n+1)/6</option>
            <option value="sum-cubes">∑i³ = [n(n+1)/2]²</option>
            <option value="geometric">∑2^i = 2^(n+1) - 1</option>
        </select>
    </div>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
        <div>
            <h5>📋 Bước cơ sở (n=1):</h5>
            <div id="base-case" style="background: #d4edda; padding: 15px; border-radius: 5px; min-height: 100px;"></div>
        </div>
        <div>
            <h5>🔄 Bước quy nạp:</h5>
            <div id="inductive-step" style="background: #cce5ff; padding: 15px; border-radius: 5px; min-height: 100px;"></div>
        </div>
    </div>
    
    <button onclick="generateInductionProof()" style="background: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; margin-top: 15px;">
        Tạo chứng minh quy nạp
    </button>
    
    <div id="induction-result" style="margin-top: 15px;"></div>
</div>

<script>
function generateInductionProof() {
    const formula = document.getElementById('formula-select').value;
    const baseCaseDiv = document.getElementById('base-case');
    const inductiveStepDiv = document.getElementById('inductive-step');
    const resultDiv = document.getElementById('induction-result');
    
    let baseCase = "";
    let inductiveStep = "";
    let formulaText = "";
    
    switch(formula) {
        case 'sum-natural':
            formulaText = "∑(i=1 to n) i = n(n+1)/2";
            baseCase = `
                <strong>n = 1:</strong><br>
                VT = 1<br>
                VP = 1(1+1)/2 = 1<br>
                VT = VP ✓
            `;
            inductiveStep = `
                <strong>Giả sử đúng với n = k:</strong><br>
                ∑(i=1 to k) i = k(k+1)/2<br><br>
                <strong>Chứng minh với n = k+1:</strong><br>
                ∑(i=1 to k+1) i = ∑(i=1 to k) i + (k+1)<br>
                = k(k+1)/2 + (k+1)<br>
                = (k+1)(k+2)/2 ✓
            `;
            break;
            
        case 'sum-squares':
            formulaText = "∑(i=1 to n) i² = n(n+1)(2n+1)/6";
            baseCase = `
                <strong>n = 1:</strong><br>
                VT = 1² = 1<br>
                VP = 1·2·3/6 = 1<br>
                VT = VP ✓
            `;
            inductiveStep = `
                <strong>Giả sử đúng với n = k:</strong><br>
                ∑i² = k(k+1)(2k+1)/6<br><br>
                <strong>Chứng minh với n = k+1:</strong><br>
                ∑(i=1 to k+1) i² = k(k+1)(2k+1)/6 + (k+1)²<br>
                = (k+1)[k(2k+1) + 6(k+1)]/6<br>
                = (k+1)(k+2)(2k+3)/6 ✓
            `;
            break;
            
        case 'sum-cubes':
            formulaText = "∑(i=1 to n) i³ = [n(n+1)/2]²";
            baseCase = `
                <strong>n = 1:</strong><br>
                VT = 1³ = 1<br>
                VP = [1·2/2]² = 1<br>
                VT = VP ✓
            `;
            inductiveStep = `
                <strong>Giả sử đúng với n = k:</strong><br>
                ∑i³ = [k(k+1)/2]²<br><br>
                <strong>Chứng minh với n = k+1:</strong><br>
                ∑(i=1 to k+1) i³ = [k(k+1)/2]² + (k+1)³<br>
                = (k+1)²[k²/4 + (k+1)]<br>
                = [(k+1)(k+2)/2]² ✓
            `;
            break;
            
        case 'geometric':
            formulaText = "∑(i=0 to n) 2^i = 2^(n+1) - 1";
            baseCase = `
                <strong>n = 0:</strong><br>
                VT = 2⁰ = 1<br>
                VP = 2¹ - 1 = 1<br>
                VT = VP ✓
            `;
            inductiveStep = `
                <strong>Giả sử đúng với n = k:</strong><br>
                ∑(i=0 to k) 2^i = 2^(k+1) - 1<br><br>
                <strong>Chứng minh với n = k+1:</strong><br>
                ∑(i=0 to k+1) 2^i = (2^(k+1) - 1) + 2^(k+1)<br>
                = 2·2^(k+1) - 1 = 2^(k+2) - 1 ✓
            `;
            break;
    }
    
    baseCaseDiv.innerHTML = baseCase;
    inductiveStepDiv.innerHTML = inductiveStep;
    
    resultDiv.innerHTML = `
        <div style="background: #d1ecf1; padding: 15px; border-radius: 5px; border-left: 4px solid #17a2b8;">
            <strong>✅ Chứng minh hoàn thành!</strong><br>
            Công thức <code>${formulaText}</code> đã được chứng minh bằng quy nạp toán học.<br>
            <em>Cả bước cơ sở và bước quy nạp đều thành công.</em>
        </div>
    `;
}
</script>

## Các biến thể của quy nạp

### 1. Quy nạp với nhiều bước cơ sở
Đôi khi cần nhiều trường hợp cơ sở:

**Ví dụ**: Dãy Fibonacci F(n) = F(n-1) + F(n-2)
- Bước cơ sở: F(1) = 1, F(2) = 1
- Bước quy nạp: F(k+1) = F(k) + F(k-1)

### 2. Quy nạp ngược (Backward Induction)
Chứng minh từ n lớn về n nhỏ.

### 3. Quy nạp cấu trúc (Structural Induction)
Áp dụng cho cấu trúc đệ quy như cây, danh sách.

## Bài tập thực hành

### Bài tập 1: Chứng minh công thức tổng
Sử dụng quy nạp để chứng minh:

1. $\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$

2. $\sum_{i=1}^{n} i^3 = \left[\frac{n(n+1)}{2}\right]^2$

3. $\sum_{i=0}^{n} 3^i = \frac{3^{n+1} - 1}{2}$

### Bài tập 2: Bất đẳng thức
Chứng minh bằng quy nạp:

1. $2^n > n^2$ với mọi n ≥ 5
2. $n! > 2^n$ với mọi n ≥ 4  
3. $1 + \frac{1}{2} + \frac{1}{3} + ... + \frac{1}{2^n} > 1 + \frac{n}{2}$ với n ≥ 1

### Bài tập 3: Ứng dụng trong khoa học máy tính
1. Chứng minh rằng thuật toán tìm kiếm nhị phân có độ phức tạp O(log n)
2. Chứng minh tính đúng đắn của thuật toán tính lũy thừa nhanh
3. Chứng minh rằng cây nhị phân đầy đủ có 2^h - 1 nút với chiều cao h

<details>
<summary>Gợi ý Bài tập 2.1</summary>

Bước cơ sở: n = 5, kiểm tra 2⁵ = 32 > 25 = 5²
Bước quy nạp: Giả sử 2^k > k², chứng minh 2^(k+1) > (k+1)²
Sử dụng: 2^(k+1) = 2·2^k > 2k² và chứng minh 2k² > (k+1)² với k ≥ 5

</details>

## Lỗi thường gặp trong quy nạp

### 1. Thiếu bước cơ sở
❌ **Sai**: Chỉ chứng minh bước quy nạp
✅ **Đúng**: Phải có cả bước cơ sở và bước quy nạp

### 2. Sử dụng sai giả thiết quy nạp
❌ **Sai**: Giả sử điều cần chứng minh với n = k+1
✅ **Đúng**: Chỉ giả sử với n = k, rồi chứng minh cho n = k+1

### 3. Bước quy nạp không đầy đủ
❌ **Sai**: Không chỉ ra rõ ràng cách từ P(k) suy ra P(k+1)
✅ **Đúng**: Mỗi bước biến đổi phải được giải thích

## Tóm tắt

**Quy nạp toán học** gồm:
1. **Bước cơ sở**: Chứng minh P(n₀)
2. **Bước quy nạp**: Chứng minh P(k) → P(k+1)

**Ưu điểm**:
- Mạnh mẽ cho các mệnh đề về số tự nhiên
- Cấu trúc rõ ràng và có hệ thống
- Phù hợp với tư duy đệ quy

**Ứng dụng**:
- Chứng minh công thức tổng, tích
- Phân tích độ phức tạp thuật toán
- Chứng minh tính đúng đắn của thuật toán đệ quy

Trong bài tiếp theo, chúng ta sẽ chuyển sang **Lý thuyết Tập hợp** - nền tảng của toán học hiện đại và khoa học máy tính.
