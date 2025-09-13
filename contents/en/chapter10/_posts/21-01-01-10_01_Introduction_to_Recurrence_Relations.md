---
layout: post
title: "Giới thiệu Quan hệ Truy hồi"
categories: chapter10
date: 2021-01-01
order: 1
required: true
lang: vi
---

# Giới thiệu Quan hệ Truy hồi

Quan hệ truy hồi là công cụ mạnh mẽ để mô hình hóa và giải quyết các bài toán có tính chất đệ quy. Trong khoa học máy tính, chúng xuất hiện khắp nơi: từ phân tích độ phức tạp thuật toán đến thiết kế cấu trúc dữ liệu và thuật toán động.

## Định nghĩa và Khái niệm

### Quan hệ Truy hồi

**Định nghĩa**: Quan hệ truy hồi là phương trình biểu diễn một số hạng của dãy số theo các số hạng trước đó.

**Dạng tổng quát**: 
a_n = f(a_{n-1}, a_{n-2}, ..., a_{n-k}, n)

Trong đó:
- a_n là số hạng thứ n
- f là hàm xác định
- k là bậc của quan hệ truy hồi
- Cần có k điều kiện ban đầu: a_0, a_1, ..., a_{k-1}

### Ví dụ Cơ bản

#### 1. Dãy Fibonacci
**Quan hệ**: F_n = F_{n-1} + F_{n-2}
**Điều kiện ban đầu**: F_0 = 0, F_1 = 1
**Dãy**: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

#### 2. Giai thừa
**Quan hệ**: n! = n × (n-1)!
**Điều kiện ban đầu**: 0! = 1
**Dãy**: 1, 1, 2, 6, 24, 120, 720, ...

#### 3. Tháp Hà Nội
**Quan hệ**: H_n = 2H_{n-1} + 1
**Điều kiện ban đầu**: H_1 = 1
**Dãy**: 1, 3, 7, 15, 31, 63, ...

## Phân loại Quan hệ Truy hồi

### 1. Theo Tính tuyến tính

#### Quan hệ Tuyến tính
**Dạng**: a_n = c_1 a_{n-1} + c_2 a_{n-2} + ... + c_k a_{n-k} + f(n)

**Ví dụ**: 
- a_n = 3a_{n-1} - 2a_{n-2} (thuần nhất)
- a_n = 2a_{n-1} + n (không thuần nhất)

#### Quan hệ Phi tuyến
**Ví dụ**: a_n = a_{n-1} × a_{n-2}

### 2. Theo Tính thuần nhất

#### Thuần nhất
Không có số hạng f(n): a_n = c_1 a_{n-1} + c_2 a_{n-2} + ... + c_k a_{n-k}

#### Không thuần nhất  
Có số hạng f(n): a_n = c_1 a_{n-1} + c_2 a_{n-2} + ... + c_k a_{n-k} + f(n)

## Công cụ tương tác: Khám phá Quan hệ Truy hồi

<div id="recurrence-explorer" class="interactive-tool">
    <h4>🔍 Khám phá Quan hệ Truy hồi</h4>
    
    <div style="margin-bottom: 20px;">
        <label><strong>Chọn loại quan hệ:</strong></label>
        <select id="recurrence-type" onchange="setupRecurrence()" style="width: 100%; padding: 8px; margin-top: 5px;">
            <option value="fibonacci">Fibonacci: F_n = F_{n-1} + F_{n-2}</option>
            <option value="hanoi">Tháp Hà Nội: H_n = 2H_{n-1} + 1</option>
            <option value="factorial">Giai thừa: n! = n × (n-1)!</option>
            <option value="geometric">Cấp số nhân: a_n = r × a_{n-1}</option>
            <option value="arithmetic">Cấp số cộng: a_n = a_{n-1} + d</option>
            <option value="custom">Tùy chỉnh</option>
        </select>
    </div>
    
    <div id="recurrence-config">
        <!-- Cấu hình sẽ được tạo động -->
    </div>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 20px 0;">
        <div>
            <label><strong>Số số hạng tính toán:</strong></label>
            <input type="number" id="num-terms" min="5" max="50" value="15" style="width: 100%; padding: 8px; margin-top: 5px;">
        </div>
        <div>
            <label><strong>Hiển thị:</strong></label>
            <select id="display-format" style="width: 100%; padding: 8px; margin-top: 5px;">
                <option value="sequence">Dãy số</option>
                <option value="table">Bảng chi tiết</option>
                <option value="graph">Biểu đồ</option>
                <option value="all">Tất cả</option>
            </select>
        </div>
    </div>
    
    <button onclick="calculateRecurrence()" style="width: 100%; margin-bottom: 20px; padding: 12px; background: #007bff; color: white; border: none; border-radius: 6px; font-weight: bold;">
        Tính toán dãy số
    </button>
    
    <div id="recurrence-results" style="background: white; padding: 20px; border-radius: 8px; border: 1px solid #dee2e6;">
        <p style="color: #666; text-align: center; margin: 0;">Chọn quan hệ truy hồi để bắt đầu</p>
    </div>
    
    <div id="recurrence-analysis" style="margin-top: 20px; background: #f8f9fa; padding: 15px; border-radius: 8px; display: none;">
        <h5>📊 Phân tích Toán học:</h5>
        <div id="analysis-content"></div>
    </div>
</div>

<script>
let recurrenceData = {
    type: 'fibonacci',
    coefficients: [],
    initialValues: [],
    nonHomogeneous: null,
    sequence: []
};

function setupRecurrence() {
    const type = document.getElementById('recurrence-type').value;
    const configDiv = document.getElementById('recurrence-config');
    
    recurrenceData.type = type;
    
    switch(type) {
        case 'fibonacci':
            configDiv.innerHTML = `
                <div style="background: #e3f2fd; padding: 15px; border-radius: 6px;">
                    <h6>Dãy Fibonacci</h6>
                    <p><strong>Quan hệ:</strong> F_n = F_{n-1} + F_{n-2}</p>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                        <div>
                            <label>F_0:</label>
                            <input type="number" id="fib-f0" value="0" style="width: 100%; padding: 6px;">
                        </div>
                        <div>
                            <label>F_1:</label>
                            <input type="number" id="fib-f1" value="1" style="width: 100%; padding: 6px;">
                        </div>
                    </div>
                </div>
            `;
            break;
            
        case 'hanoi':
            configDiv.innerHTML = `
                <div style="background: #fff3cd; padding: 15px; border-radius: 6px;">
                    <h6>Tháp Hà Nội</h6>
                    <p><strong>Quan hệ:</strong> H_n = 2H_{n-1} + 1</p>
                    <div>
                        <label>H_1 (số bước cho 1 đĩa):</label>
                        <input type="number" id="hanoi-h1" value="1" style="width: 100%; padding: 6px; margin-top: 5px;">
                    </div>
                </div>
            `;
            break;
            
        case 'factorial':
            configDiv.innerHTML = `
                <div style="background: #d4edda; padding: 15px; border-radius: 6px;">
                    <h6>Giai thừa</h6>
                    <p><strong>Quan hệ:</strong> n! = n × (n-1)!</p>
                    <div>
                        <label>0! (điều kiện ban đầu):</label>
                        <input type="number" id="fact-0" value="1" style="width: 100%; padding: 6px; margin-top: 5px;">
                    </div>
                </div>
            `;
            break;
            
        case 'geometric':
            configDiv.innerHTML = `
                <div style="background: #f8d7da; padding: 15px; border-radius: 6px;">
                    <h6>Cấp số nhân</h6>
                    <p><strong>Quan hệ:</strong> a_n = r × a_{n-1}</p>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                        <div>
                            <label>a_0 (số hạng đầu):</label>
                            <input type="number" id="geo-a0" value="1" style="width: 100%; padding: 6px; margin-top: 5px;">
                        </div>
                        <div>
                            <label>r (công bội):</label>
                            <input type="number" id="geo-r" value="2" step="0.1" style="width: 100%; padding: 6px; margin-top: 5px;">
                        </div>
                    </div>
                </div>
            `;
            break;
            
        case 'arithmetic':
            configDiv.innerHTML = `
                <div style="background: #e2e3e5; padding: 15px; border-radius: 6px;">
                    <h6>Cấp số cộng</h6>
                    <p><strong>Quan hệ:</strong> a_n = a_{n-1} + d</p>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                        <div>
                            <label>a_0 (số hạng đầu):</label>
                            <input type="number" id="arith-a0" value="1" style="width: 100%; padding: 6px; margin-top: 5px;">
                        </div>
                        <div>
                            <label>d (công sai):</label>
                            <input type="number" id="arith-d" value="3" style="width: 100%; padding: 6px; margin-top: 5px;">
                        </div>
                    </div>
                </div>
            `;
            break;
            
        case 'custom':
            configDiv.innerHTML = `
                <div style="background: #f0f0f0; padding: 15px; border-radius: 6px;">
                    <h6>Quan hệ Tùy chỉnh</h6>
                    <p><strong>Dạng:</strong> a_n = c₁a_{n-1} + c₂a_{n-2} + f(n)</p>
                    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-bottom: 10px;">
                        <div>
                            <label>c₁:</label>
                            <input type="number" id="custom-c1" value="1" step="0.1" style="width: 100%; padding: 6px;">
                        </div>
                        <div>
                            <label>c₂:</label>
                            <input type="number" id="custom-c2" value="1" step="0.1" style="width: 100%; padding: 6px;">
                        </div>
                        <div>
                            <label>f(n) (tùy chọn):</label>
                            <input type="text" id="custom-fn" placeholder="0, n, 2^n, ..." style="width: 100%; padding: 6px;">
                        </div>
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                        <div>
                            <label>a₀:</label>
                            <input type="number" id="custom-a0" value="0" style="width: 100%; padding: 6px;">
                        </div>
                        <div>
                            <label>a₁:</label>
                            <input type="number" id="custom-a1" value="1" style="width: 100%; padding: 6px;">
                        </div>
                    </div>
                </div>
            `;
            break;
    }
}

function calculateRecurrence() {
    const type = recurrenceData.type;
    const numTerms = parseInt(document.getElementById('num-terms').value);
    const displayFormat = document.getElementById('display-format').value;
    const resultsDiv = document.getElementById('recurrence-results');
    const analysisDiv = document.getElementById('recurrence-analysis');
    
    let sequence = [];
    let formula = '';
    let complexity = '';
    
    try {
        switch(type) {
            case 'fibonacci':
                const f0 = parseInt(document.getElementById('fib-f0').value);
                const f1 = parseInt(document.getElementById('fib-f1').value);
                sequence = calculateFibonacci(f0, f1, numTerms);
                formula = 'F_n = ((1+√5)/2)^n - ((1-√5)/2)^n) / √5';
                complexity = 'O(φⁿ) where φ = (1+√5)/2 ≈ 1.618';
                break;
                
            case 'hanoi':
                const h1 = parseInt(document.getElementById('hanoi-h1').value);
                sequence = calculateHanoi(h1, numTerms);
                formula = 'H_n = 2ⁿ - 1';
                complexity = 'O(2ⁿ) - exponential growth';
                break;
                
            case 'factorial':
                const fact0 = parseInt(document.getElementById('fact-0').value);
                sequence = calculateFactorial(fact0, numTerms);
                formula = 'n! = n × (n-1)!';
                complexity = 'O(n!) - factorial growth';
                break;
                
            case 'geometric':
                const geoA0 = parseFloat(document.getElementById('geo-a0').value);
                const geoR = parseFloat(document.getElementById('geo-r').value);
                sequence = calculateGeometric(geoA0, geoR, numTerms);
                formula = `a_n = ${geoA0} × ${geoR}ⁿ`;
                complexity = geoR > 1 ? `O(${geoR}ⁿ) - exponential` : geoR === 1 ? 'O(1) - constant' : 'O(1) - decreasing';
                break;
                
            case 'arithmetic':
                const arithA0 = parseFloat(document.getElementById('arith-a0').value);
                const arithD = parseFloat(document.getElementById('arith-d').value);
                sequence = calculateArithmetic(arithA0, arithD, numTerms);
                formula = `a_n = ${arithA0} + ${arithD}n`;
                complexity = 'O(n) - linear growth';
                break;
                
            case 'custom':
                const c1 = parseFloat(document.getElementById('custom-c1').value);
                const c2 = parseFloat(document.getElementById('custom-c2').value);
                const a0 = parseFloat(document.getElementById('custom-a0').value);
                const a1 = parseFloat(document.getElementById('custom-a1').value);
                const fn = document.getElementById('custom-fn').value.trim();
                
                sequence = calculateCustom(c1, c2, a0, a1, fn, numTerms);
                formula = `a_n = ${c1}a_{n-1} + ${c2}a_{n-2}` + (fn ? ` + ${fn}` : '');
                complexity = 'Depends on coefficients and f(n)';
                break;
        }
        
        recurrenceData.sequence = sequence;
        
        // Display results
        displayResults(sequence, displayFormat, resultsDiv);
        
        // Show analysis
        displayAnalysis(formula, complexity, sequence, analysisDiv);
        analysisDiv.style.display = 'block';
        
    } catch (error) {
        resultsDiv.innerHTML = `<p style="color: #dc3545; text-align: center; margin: 0;">Lỗi: ${error.message}</p>`;
        analysisDiv.style.display = 'none';
    }
}

function calculateFibonacci(f0, f1, n) {
    const sequence = [f0, f1];
    for (let i = 2; i < n; i++) {
        sequence[i] = sequence[i-1] + sequence[i-2];
    }
    return sequence;
}

function calculateHanoi(h1, n) {
    const sequence = [0, h1]; // H_0 = 0 (0 disks), H_1 = 1
    for (let i = 2; i < n; i++) {
        sequence[i] = 2 * sequence[i-1] + 1;
    }
    return sequence;
}

function calculateFactorial(fact0, n) {
    const sequence = [fact0];
    for (let i = 1; i < n; i++) {
        sequence[i] = i * sequence[i-1];
    }
    return sequence;
}

function calculateGeometric(a0, r, n) {
    const sequence = [a0];
    for (let i = 1; i < n; i++) {
        sequence[i] = r * sequence[i-1];
    }
    return sequence;
}

function calculateArithmetic(a0, d, n) {
    const sequence = [a0];
    for (let i = 1; i < n; i++) {
        sequence[i] = sequence[i-1] + d;
    }
    return sequence;
}

function calculateCustom(c1, c2, a0, a1, fn, n) {
    const sequence = [a0, a1];
    
    for (let i = 2; i < n; i++) {
        let term = c1 * sequence[i-1] + c2 * sequence[i-2];
        
        // Add non-homogeneous term if specified
        if (fn) {
            term += evaluateFunction(fn, i);
        }
        
        sequence[i] = term;
    }
    return sequence;
}

function evaluateFunction(fn, n) {
    // Simple function evaluator for common cases
    fn = fn.toLowerCase().replace(/\s/g, '');
    
    if (fn === '0' || fn === '') return 0;
    if (fn === 'n') return n;
    if (fn === '1') return 1;
    if (fn === '2^n' || fn === '2**n') return Math.pow(2, n);
    if (fn === 'n^2' || fn === 'n**2') return n * n;
    if (fn === 'n!') return factorial(n);
    
    // Try to evaluate as a simple expression
    try {
        return eval(fn.replace(/n/g, n.toString()));
    } catch {
        return 0;
    }
}

function factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

function displayResults(sequence, format, container) {
    let html = '';
    
    if (format === 'sequence' || format === 'all') {
        html += `
            <div style="margin-bottom: 20px;">
                <h5>📋 Dãy số:</h5>
                <div style="background: #f8f9fa; padding: 15px; border-radius: 6px; font-family: monospace; word-break: break-all;">
                    ${sequence.map((val, idx) => `a${idx} = ${val}`).join(', ')}
                </div>
            </div>
        `;
    }
    
    if (format === 'table' || format === 'all') {
        html += `
            <div style="margin-bottom: 20px;">
                <h5>📊 Bảng chi tiết:</h5>
                <div style="max-height: 300px; overflow-y: auto;">
                    <table style="width: 100%; border-collapse: collapse; font-size: 0.9em;">
                        <thead>
                            <tr style="background: #e9ecef;">
                                <th style="border: 1px solid #dee2e6; padding: 8px;">n</th>
                                <th style="border: 1px solid #dee2e6; padding: 8px;">aₙ</th>
                                <th style="border: 1px solid #dee2e6; padding: 8px;">Tỷ lệ aₙ/aₙ₋₁</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${sequence.map((val, idx) => `
                                <tr>
                                    <td style="border: 1px solid #dee2e6; padding: 8px; text-align: center;">${idx}</td>
                                    <td style="border: 1px solid #dee2e6; padding: 8px; text-align: center;">${val}</td>
                                    <td style="border: 1px solid #dee2e6; padding: 8px; text-align: center;">
                                        ${idx > 0 ? (val / sequence[idx-1]).toFixed(3) : '-'}
                                    </td>
                                </tr>
                            `).join('')}
                        </tbody>
                    </table>
                </div>
            </div>
        `;
    }
    
    if (format === 'graph' || format === 'all') {
        html += `
            <div style="margin-bottom: 20px;">
                <h5>📈 Biểu đồ:</h5>
                <canvas id="recurrence-chart" width="400" height="250" style="width: 100%; max-width: 400px; height: 250px; border: 1px solid #dee2e6; border-radius: 6px;"></canvas>
            </div>
        `;
    }
    
    container.innerHTML = html;
    
    // Draw chart if needed
    if (format === 'graph' || format === 'all') {
        setTimeout(() => drawRecurrenceChart(sequence), 100);
    }
}

function drawRecurrenceChart(sequence) {
    const canvas = document.getElementById('recurrence-chart');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    const padding = 40;
    
    // Clear canvas
    ctx.clearRect(0, 0, width, height);
    
    // Find min/max values
    const maxVal = Math.max(...sequence);
    const minVal = Math.min(...sequence);
    const range = maxVal - minVal || 1;
    
    // Draw axes
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(padding, height - padding);
    ctx.lineTo(width - padding, height - padding);
    ctx.moveTo(padding, padding);
    ctx.lineTo(padding, height - padding);
    ctx.stroke();
    
    // Draw data points and lines
    ctx.strokeStyle = '#007bff';
    ctx.fillStyle = '#007bff';
    ctx.lineWidth = 2;
    
    ctx.beginPath();
    sequence.forEach((val, idx) => {
        const x = padding + (idx / (sequence.length - 1)) * (width - 2 * padding);
        const y = height - padding - ((val - minVal) / range) * (height - 2 * padding);
        
        if (idx === 0) {
            ctx.moveTo(x, y);
        } else {
            ctx.lineTo(x, y);
        }
        
        // Draw point
        ctx.save();
        ctx.beginPath();
        ctx.arc(x, y, 3, 0, 2 * Math.PI);
        ctx.fill();
        ctx.restore();
    });
    ctx.stroke();
    
    // Add labels
    ctx.fillStyle = '#333';
    ctx.font = '12px Arial';
    ctx.fillText('n', width / 2 - 10, height - 10);
    
    ctx.save();
    ctx.translate(15, height / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.fillText('aₙ', -10, 0);
    ctx.restore();
}

function displayAnalysis(formula, complexity, sequence, container) {
    const analysisContent = document.getElementById('analysis-content');
    
    // Calculate growth rate
    const ratios = [];
    for (let i = 1; i < Math.min(sequence.length, 10); i++) {
        if (sequence[i-1] !== 0) {
            ratios.push(sequence[i] / sequence[i-1]);
        }
    }
    
    const avgRatio = ratios.length > 0 ? ratios.reduce((a, b) => a + b) / ratios.length : 0;
    
    analysisContent.innerHTML = `
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
            <div>
                <strong>Công thức tổng quát:</strong><br>
                <code style="background: #e9ecef; padding: 4px 8px; border-radius: 4px;">${formula}</code>
            </div>
            <div>
                <strong>Độ phức tạp:</strong><br>
                <code style="background: #e9ecef; padding: 4px 8px; border-radius: 4px;">${complexity}</code>
            </div>
        </div>
        <div style="margin-top: 15px;">
            <strong>Phân tích tăng trưởng:</strong><br>
            <div style="background: #f8f9fa; padding: 10px; border-radius: 4px; margin-top: 5px;">
                Tỷ lệ tăng trưởng trung bình: ${avgRatio.toFixed(3)}<br>
                Giá trị lớn nhất: ${Math.max(...sequence)}<br>
                Số hạng cuối: a${sequence.length-1} = ${sequence[sequence.length-1]}
            </div>
        </div>
    `;
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    setupRecurrence();
});
</script>

## Phương pháp Giải Quan hệ Truy hồi

### 1. Phương pháp Đặc trưng (Characteristic Method)

Cho quan hệ tuyến tính thuần nhất bậc k:
a_n = c_1 a_{n-1} + c_2 a_{n-2} + ... + c_k a_{n-k}

**Bước 1**: Lập phương trình đặc trưng
r^k = c_1 r^{k-1} + c_2 r^{k-2} + ... + c_k

**Bước 2**: Tìm nghiệm r_1, r_2, ..., r_k

**Bước 3**: Viết nghiệm tổng quát
- Nếu các nghiệm phân biệt: a_n = A_1 r_1^n + A_2 r_2^n + ... + A_k r_k^n
- Nếu có nghiệm bội: thêm các số hạng n^i r^n

**Bước 4**: Sử dụng điều kiện ban đầu để tìm các hằng số A_i

### Ví dụ: Giải dãy Fibonacci

**Quan hệ**: F_n = F_{n-1} + F_{n-2}, F_0 = 0, F_1 = 1

**Phương trình đặc trưng**: r^2 = r + 1 ⟹ r^2 - r - 1 = 0

**Nghiệm**: r_1 = (1+√5)/2 ≈ 1.618, r_2 = (1-√5)/2 ≈ -0.618

**Nghiệm tổng quát**: F_n = A r_1^n + B r_2^n

**Áp dụng điều kiện ban đầu**:
- F_0 = A + B = 0 ⟹ B = -A
- F_1 = A r_1 + B r_2 = 1 ⟹ A(r_1 - r_2) = 1 ⟹ A = 1/√5

**Nghiệm cuối cùng**: F_n = (r_1^n - r_2^n)/√5

### 2. Phương pháp Hàm sinh (Generating Functions)

**Định nghĩa**: Hàm sinh của dãy {a_n} là:
G(x) = Σ(n=0 to ∞) a_n x^n

**Ứng dụng**: Chuyển quan hệ truy hồi thành phương trình đại số cho G(x).

## Ứng dụng trong Khoa học Máy tính

### 1. Phân tích Độ phức tạp Thuật toán

```python
def merge_sort_complexity():
    """
    Merge Sort: T(n) = 2T(n/2) + O(n)
    Giải: T(n) = O(n log n)
    """
    pass

def fibonacci_recursive(n):
    """
    Fibonacci đệ quy: T(n) = T(n-1) + T(n-2) + O(1)
    Giải: T(n) = O(φⁿ) where φ = (1+√5)/2
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def binary_search_complexity():
    """
    Binary Search: T(n) = T(n/2) + O(1)
    Giải: T(n) = O(log n)
    """
    pass
```

### 2. Thuật toán Quy hoạch Động

```python
def fibonacci_dp(n):
    """Fibonacci với quy hoạch động - O(n)"""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]  # Quan hệ truy hồi
    
    return dp[n]

def climbing_stairs(n):
    """
    Số cách leo n bậc thang (mỗi lần leo 1 hoặc 2 bậc)
    Quan hệ: ways(n) = ways(n-1) + ways(n-2)
    """
    if n <= 2:
        return n
    
    prev2, prev1 = 1, 2
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1
```

### 3. Cấu trúc Dữ liệu

```python
class BinaryTreeCount:
    """Đếm số cây nhị phân với n nút"""
    
    def catalan_number(self, n):
        """
        Số Catalan: C_n = C_0*C_{n-1} + C_1*C_{n-2} + ... + C_{n-1}*C_0
        Quan hệ truy hồi phi tuyến
        """
        if n <= 1:
            return 1
        
        catalan = [0] * (n + 1)
        catalan[0] = catalan[1] = 1
        
        for i in range(2, n + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i-1-j]
        
        return catalan[n]

def tower_of_hanoi(n, source, destination, auxiliary):
    """
    Tháp Hà Nội: H(n) = 2H(n-1) + 1
    Số bước: 2ⁿ - 1
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return 1
    
    steps = 0
    steps += tower_of_hanoi(n-1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    steps += 1
    steps += tower_of_hanoi(n-1, auxiliary, destination, source)
    
    return steps
```

## Bài tập thực hành

### Bài tập 1: Thiết lập Quan hệ Truy hồi
1. Một người leo cầu thang n bậc, mỗi lần có thể leo 1, 2 hoặc 3 bậc. Thiết lập quan hệ truy hồi cho số cách leo.

2. Số cách chia n đồng xu giống nhau vào k hộp khác nhau sao cho mỗi hộp có ít nhất 1 đồng xu.

3. Số cách sắp xếp n người vào hàng sao cho không có 2 người cao liền kề.

### Bài tập 2: Giải Quan hệ Truy hồi
1. Giải: a_n = 5a_{n-1} - 6a_{n-2}, a_0 = 1, a_1 = 0

2. Giải: a_n = 2a_{n-1} + 3^n, a_0 = 1

3. Giải: a_n = a_{n-1} + 2a_{n-2} + 2^n, a_0 = 0, a_1 = 1

### Bài tập 3: Ứng dụng
1. Phân tích độ phức tạp của thuật toán QuickSort trong trường hợp xấu nhất.

2. Tính số phép toán cần thiết để tính a^n bằng thuật toán "fast exponentiation".

3. Đếm số cây nhị phân tìm kiếm khác nhau với n nút.

<details>
<summary>Đáp án Bài tập 1</summary>

1. **f(n) = f(n-1) + f(n-2) + f(n-3)**, f(0)=1, f(1)=1, f(2)=2
2. **S(n,k) = k·S(n-1,k) + S(n-1,k-1)** (Số Stirling loại 2)
3. **a_n = a_{n-1} + a_{n-2}** (tương tự Fibonacci)

</details>

## Tóm tắt

**Quan hệ Truy hồi** là công cụ mạnh mẽ để:

**Mô hình hóa**:
- Thuật toán đệ quy và độ phức tạp
- Cấu trúc dữ liệu động
- Bài toán đếm tổ hợp

**Phương pháp giải**:
- Phương trình đặc trưng cho quan hệ tuyến tính
- Hàm sinh cho quan hệ phức tạp
- Quy hoạch động cho tính toán hiệu quả

**Ứng dụng CS**:
- Algorithm analysis (merge sort, quicksort)
- Dynamic programming (Fibonacci, climbing stairs)
- Data structures (binary trees, graphs)
- Combinatorial problems (Catalan numbers)

Trong bài tiếp theo, chúng ta sẽ học về **Hàm sinh** - công cụ mạnh mẽ để giải các quan hệ truy hồi phức tạp và bài toán đếm nâng cao.
