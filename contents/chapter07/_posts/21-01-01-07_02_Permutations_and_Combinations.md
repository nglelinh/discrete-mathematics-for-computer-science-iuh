---
layout: post
title: "Hoán vị và Tổ hợp"
categories: chapter07
date: 2021-01-01
order: 2
required: true
lang: en
---

# Hoán vị và Tổ hợp

Khi tổ chức dữ liệu hay lựa chọn phương án, có lúc thứ tự là tất cả, có lúc thứ tự hoàn toàn không quan trọng. Mã OTP 123456 khác 654321, nhưng một nhóm 3 sinh viên làm bài tập thì không đổi bản chất chỉ vì đổi chỗ ngồi. Nhầm hai tình huống này là một trong những lỗi đếm phổ biến nhất.

**Hoán vị** và **tổ hợp** giúp ta phân biệt rõ “sắp xếp” với “chọn lựa”. Đây là công cụ xuất hiện từ bài toán lên lịch, sinh test case, brute-force password cho đến xác suất và thống kê. Nắm chắc chúng, bạn sẽ đếm không chỉ nhanh hơn mà còn đúng bản chất hơn.

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

**Định nghĩa**: Hoán vị là cách sắp xếp toàn bộ n đối tượng theo một thứ tự nhất định.

### Hoán vị không lặp

**Công thức**: Số hoán vị của n đối tượng phân biệt là:

$$P(n) = n!$$

**Ví dụ**: Có bao nhiêu cách sắp xếp 4 người ngồi thành hàng?

**Giải**: P(4) = 4! = 24 cách

### Hoán vị có lặp

Khi có các đối tượng giống nhau, số hoán vị giảm đi do các đối tượng cùng loại không thể phân biệt.

**Công thức**: Cho n đối tượng gồm k loại, loại thứ i có nᵢ đối tượng giống nhau (n₁ + n₂ + ... + nₖ = n). Số hoán vị có lặp là:

$$\frac{n!}{n_1! \times n_2! \times \cdots \times n_k!}$$

**Ví dụ**: Có bao nhiêu cách sắp xếp các chữ cái trong từ "BANANA"?

**Giải**: 
- Tổng: 6 chữ cái
- B: 1, A: 3, N: 2
- Kết quả: 6!/(1! × 3! × 2!) = 720/(1 × 6 × 2) = 60 cách

## Chỉnh hợp (k-Permutations)

**Định nghĩa**: Chỉnh hợp chập k của n là cách chọn k đối tượng từ n đối tượng phân biệt và sắp xếp chúng theo một thứ tự nhất định. Khác với hoán vị, chỉnh hợp chỉ lấy k đối tượng (k ≤ n) thay vì tất cả n đối tượng.

### Chỉnh hợp không lặp

**Công thức**: Số chỉnh hợp chập k của n là:

$$P(n,k) = \frac{n!}{(n-k)!} = n \times (n-1) \times \cdots \times (n-k+1)$$

**Ý nghĩa**: Chọn k đối tượng từ n đối tượng và sắp xếp chúng (thứ tự có ý nghĩa).

**Ví dụ 1**: Có 10 học sinh, chọn 3 em để xếp thành hàng (chọn và sắp xếp thứ tự). Có bao nhiêu cách?

**Giải**: P(10,3) = 10!/(10-3)! = 10!/7! = 10 × 9 × 8 = 720 cách

**Ví dụ 2**: Một cuộc thi có 8 thí sinh. Hỏi có bao nhiêu cách trao huy chương Vàng, Bạc, Đồng cho ba thí sinh khác nhau?

**Giải**: Số cách chọn 3 người từ 8 và sắp xếp thứ tự (Vàng, Bạc, Đồng) là:

P(8,3) = 8!/(8-3)! = 8!/5! = 8 × 7 × 6 = 336 cách

### Phân biệt Hoán vị và Chỉnh hợp

| Tiêu chí | Hoán vị | Chỉnh hợp |
|:---------|:---------|:-----------|
| Số đối tượng lấy ra | Tất cả n | k đối tượng (k ≤ n) |
| Thứ tự | Có ý nghĩa | Có ý nghĩa |
| Công thức | P(n) = n! | P(n,k) = n!/(n-k)! |

## Tổ hợp (Combinations)

**Định nghĩa**: Tổ hợp chập k của n là cách chọn k đối tượng từ n đối tượng phân biệt mà không quan tâm đến thứ tự.

**Công thức**: Số tổ hợp chập k của n là:

$$C(n,k) = \binom{n}{k} = \frac{n!}{k!(n-k)!}$$

**Ký hiệu khác**: $C_n^k$ cũng được sử dụng trong một số tài liệu.

**Ví dụ 1**: Từ 10 học sinh, chọn 3 em để tham gia đội tuyển. Có bao nhiêu cách?

**Giải**: C(10,3) = 10!/(3!×7!) = (10×9×8)/(3×2×1) = 120 cách

**Ví dụ 2**: Một lớp có 12 nam và 8 nữ. Có bao nhiêu cách chọn một nhóm 4 người có đúng 2 nam?

**Giải**: 
- Chọn 2 nam từ 12 nam: C(12,2) = 66 cách
- Chọn 2 nữ từ 8 nữ: C(8,2) = 28 cách
- Theo quy tắc nhân: 66 × 28 = 1.848 cách

## Tổ hợp lặp (Combinations with Repetition)

**Định nghĩa**: Tổ hợp lặp chập k từ n loại đối tượng là cách chọn k đối tượng (không quan tâm thứ tự) từ n loại, trong đó mỗi loại có thể được chọn nhiều lần.

**Công thức**: Số tổ hợp lặp chập k từ n loại là:

$$C_R(n,k) = C(n+k-1,k) = \binom{n+k-1}{k} = \frac{(n+k-1)!}{k!(n-1)!}$$

**Ví dụ 1**: Một cửa hàng bán 4 loại bánh: A, B, C, D. Bạn muốn mua 5 cái bánh. Hỏi có bao nhiêu cách chọn?

**Giải**: Đây là tổ hợp lặp chập 5 từ 4 loại:

C_R(4,5) = C(4+5-1,5) = C(8,5) = C(8,3) = 56 cách

**Ví dụ 2**: Có bao nhiêu nghiệm nguyên không âm của phương trình x₁ + x₂ + x₃ = 6?

**Giải**: Mỗi nghiệm tương ứng với một tổ hợp lặp chập 6 từ 3 loại:

C_R(3,6) = C(3+6-1,6) = C(8,6) = C(8,2) = 28 nghiệm

## Công thức Nhị thức Newton (Binomial Theorem)

**Định lý**: Với mọi số nguyên $$n \geq 0$$:

$$(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} x^{n-k} y^k = \binom{n}{0} x^n + \binom{n}{1} x^{n-1} y + \binom{n}{2} x^{n-2} y^2 + \cdots + \binom{n}{n} y^n$$

**Ví dụ 1**: Khai triển $$(x + y)^3$$:
$$(x + y)^3 = \binom{3}{0}x^3 + \binom{3}{1}x^2 y + \binom{3}{2}xy^2 + \binom{3}{3}y^3 = x^3 + 3x^2 y + 3xy^2 + y^3$$

**Ví dụ 2**: Tìm hệ số của $$x^3 y^2$$ trong khai triển $$(x + y)^5$$:
Hệ số là $$\binom{5}{2} = 10$$.

**Hệ quả quan trọng**:
- Tổng các hệ số: $$\sum_{k=0}^{n} \binom{n}{k} = 2^n$$ (cho $$x = y = 1$$)
- Tổng các hệ số đan dấu: $$\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0$$ (cho $$x = 1, y = -1$$)

## Hoán vị lặp và Tổ hợp lặp (Repeated Permutations & Combinations)

Những công thức này được dùng khi các đối tượng có thể được chọn nhiều lần.

### Hoán vị lặp

Khi có $$n$$ đối tượng gồm $$k$$ loại, loại thứ $$i$$ có $$n_i$$ đối tượng giống nhau ($$\sum n_i = n$$):

Số hoán vị lặp = $$\frac{n!}{n_1! \times n_2! \times \cdots \times n_k!}$$

**Ví dụ**: Số cách sắp xếp các chữ cái trong từ "BANANA":
$$\frac{6!}{1! \times 3! \times 2!} = \frac{720}{1 \times 6 \times 2} = 60$$

### Tổ hợp lặp (Combinations with Repetition)

Số cách chọn $$k$$ đối tượng từ $$n$$ loại (mỗi loại không giới hạn số lượng, không quan tâm thứ tự):

$$C_R(n, k) = \binom{n + k - 1}{k}$$

**Ví dụ**: Một tiệm kem có 5 vị. Có bao nhiêu cách chọn 3 cây kem?
$$C_R(5, 3) = \binom{5 + 3 - 1}{3} = \binom{7}{3} = 35$$

## Bảng tổng kết các công thức

| Khái niệm | Chọn k từ n? | Thứ tự? | Lặp? | Công thức |
|:-----------|:------------:|:-------:|:----:|:----------|
| Hoán vị | n (tất cả) | Có | Không | n! |
| Hoán vị có lặp | n (tất cả) | Có | Có | n!/(n₁!×...×nₖ!) |
| Chỉnh hợp | k ≤ n | Có | Không | n!/(n-k)! |
| Tổ hợp | k ≤ n | Không | Không | n!/(k!(n-k)!) |
| Tổ hợp lặp | k bất kỳ | Không | Có | C(n+k-1, k) |

## Bài tập có lời giải

### Bài tập 1: Xếp sách lên kệ

Có 5 cuốn sách Toán, 4 cuốn sách Lý và 3 cuốn sách Hóa. Có bao nhiêu cách xếp 12 cuốn sách lên kệ sao cho các cuốn cùng môn đứng cạnh nhau?

**Giải**: 
- Coi mỗi bộ môn là một khối: có 3! = 6 cách sắp xếp thứ tự các môn
- Trong mỗi môn: Toán có 5! = 120 cách, Lý có 4! = 24 cách, Hóa có 3! = 6 cách
- Tổng số: 3! × 5! × 4! × 3! = 6 × 120 × 24 × 6 = 103.680 cách

### Bài tập 2: Chọn ủy ban

Một lớp có 15 nam và 12 nữ. Cần chọn một ủy ban gồm 5 người. Có bao nhiêu cách chọn nếu ủy ban phải có ít nhất 2 nữ?

**Giải**: Ta tính tổng số cách chọn có 2 nữ, 3 nữ, 4 nữ và 5 nữ:
- 2 nữ + 3 nam: C(12,2) × C(15,3) = 66 × 455 = 30.030
- 3 nữ + 2 nam: C(12,3) × C(15,2) = 220 × 105 = 23.100
- 4 nữ + 1 nam: C(12,4) × C(15,1) = 495 × 15 = 7.425
- 5 nữ + 0 nam: C(12,5) × C(15,0) = 792 × 1 = 792

Tổng số: 30.030 + 23.100 + 7.425 + 792 = 61.347 cách

### Bài tập 3: Thành lập số

Từ các chữ số 0, 1, 2, 3, 4, 5 có thể lập được bao nhiêu số tự nhiên có 4 chữ số khác nhau?

**Giải**: 
- Chữ số đầu tiên (hàng nghìn) không thể là 0: có 5 cách chọn (1, 2, 3, 4, 5)
- Sau khi chọn chữ số đầu, còn 3 vị trí với 5 chữ số còn lại
- Số cách chọn và sắp xếp 3 vị trí còn lại: P(5,3) = 5!/2! = 60
- Tổng số: 5 × 60 = 300 số

## Bài tập tự luyện

1. Có bao nhiêu cách sắp xếp 5 học sinh ngồi vào một hàng ghế có 5 chỗ?

2. Một hộp có 10 viên bi đỏ và 8 viên bi xanh. Có bao nhiêu cách chọn 4 viên bi trong đó có ít nhất 1 viên bi đỏ?

3. Từ các chữ số 1, 2, 3, 4, 5, 6, 7 có thể lập được bao nhiêu số chẵn có 4 chữ số khác nhau?

4. Có bao nhiêu cách xếp 3 quyển sách Toán, 2 quyển sách Văn và 4 quyển sách Anh lên kệ sao cho các quyển cùng môn không nhất thiết đứng cạnh nhau?

5. Một nhóm có 10 nam và 7 nữ. Cần chọn ra 5 người sao cho số nam nhiều hơn số nữ. Hỏi có bao nhiêu cách chọn?

6. Tìm số nghiệm nguyên không âm của phương trình x₁ + x₂ + x₃ + x₄ = 8.

7. Một cửa hàng kem có 5 vị khác nhau. Bạn muốn mua 3 cây kem, mỗi cây có thể chọn bất kỳ vị nào. Có bao nhiêu cách chọn?

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
