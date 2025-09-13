---
layout: post
title: "Lý thuyết Xác suất Cơ bản"
categories: chapter09
date: 2021-01-01
order: 1
required: true
lang: vi
---

# Lý thuyết Xác suất Cơ bản

Xác suất là ngành toán học nghiên cứu về sự không chắc chắn và ngẫu nhiên. Trong khoa học máy tính, xác suất đóng vai trò quan trọng trong thuật toán ngẫu nhiên, machine learning, mật mã học và phân tích hiệu suất hệ thống.

## Khái niệm Cơ bản

### Thí nghiệm và Không gian Mẫu

**Thí nghiệm ngẫu nhiên**: Một quá trình có kết quả không thể dự đoán trước.

**Không gian mẫu (Sample Space)** Ω: Tập hợp tất cả các kết quả có thể của thí nghiệm.

**Biến cố (Event)**: Tập con của không gian mẫu.

### Ví dụ

**Thí nghiệm**: Tung một đồng xu
- Không gian mẫu: Ω = {H, T} (Head, Tail)
- Biến cố A = "Ra mặt ngửa" = {H}

**Thí nghiệm**: Tung hai xúc xắc
- Không gian mẫu: Ω = {(i,j) | 1 ≤ i,j ≤ 6}, |Ω| = 36
- Biến cố B = "Tổng bằng 7" = {(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)}

## Định nghĩa Xác suất

### Định nghĩa Cổ điển (Laplace)

Với không gian mẫu hữu hạn và các kết quả đồng khả năng:

**P(A) = |A| / |Ω|**

### Tiên đề Kolmogorov

1. **Không âm**: P(A) ≥ 0 với mọi biến cố A
2. **Chuẩn hóa**: P(Ω) = 1
3. **Cộng tính**: Nếu A ∩ B = ∅ thì P(A ∪ B) = P(A) + P(B)

### Tính chất Cơ bản

- P(∅) = 0
- P(A^c) = 1 - P(A)
- 0 ≤ P(A) ≤ 1
- Nếu A ⊆ B thì P(A) ≤ P(B)

## Công cụ tương tác: Mô phỏng Xác suất

<div id="probability-simulator" class="interactive-tool">
    <h4>🎲 Mô phỏng Thí nghiệm Xác suất</h4>
    
    <div style="margin-bottom: 20px;">
        <label><strong>Chọn thí nghiệm:</strong></label>
        <select id="experiment-type" onchange="setupExperiment()" style="width: 100%; padding: 8px; margin-top: 5px;">
            <option value="coin">Tung đồng xu</option>
            <option value="dice">Tung xúc xắc</option>
            <option value="two-dice">Tung hai xúc xắc</option>
            <option value="cards">Rút bài từ bộ 52 lá</option>
            <option value="balls">Rút bi từ hộp</option>
        </select>
    </div>
    
    <div id="experiment-config">
        <!-- Cấu hình thí nghiệm sẽ được tạo động -->
    </div>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin: 20px 0;">
        <div>
            <label><strong>Số lần thực hiện:</strong></label>
            <input type="number" id="num-trials" min="1" max="10000" value="1000" style="width: 100%; padding: 8px; margin-top: 5px;">
        </div>
        <div>
            <label><strong>Tốc độ mô phỏng:</strong></label>
            <select id="simulation-speed" style="width: 100%; padding: 8px; margin-top: 5px;">
                <option value="1">Rất nhanh (1ms)</option>
                <option value="10">Nhanh (10ms)</option>
                <option value="50" selected>Vừa (50ms)</option>
                <option value="100">Chậm (100ms)</option>
            </select>
        </div>
        <div>
            <label><strong>Hiển thị:</strong></label>
            <select id="display-mode" style="width: 100%; padding: 8px; margin-top: 5px;">
                <option value="realtime">Thời gian thực</option>
                <option value="batch">Theo lô</option>
                <option value="final">Chỉ kết quả cuối</option>
            </select>
        </div>
    </div>
    
    <div style="display: flex; gap: 10px; margin-bottom: 20px;">
        <button onclick="startSimulation()" id="sim-start-btn" style="flex: 1; padding: 12px; background: #28a745; color: white; border: none; border-radius: 6px; font-weight: bold;">
            ▶️ Bắt đầu Mô phỏng
        </button>
        <button onclick="pauseSimulation()" id="sim-pause-btn" style="flex: 1; padding: 12px; background: #ffc107; color: #212529; border: none; border-radius: 6px; font-weight: bold;" disabled>
            ⏸️ Tạm dừng
        </button>
        <button onclick="resetSimulation()" style="flex: 1; padding: 12px; background: #6c757d; color: white; border: none; border-radius: 6px; font-weight: bold;">
            🔄 Đặt lại
        </button>
    </div>
    
    <div id="simulation-results" style="background: white; padding: 20px; border-radius: 8px; border: 1px solid #dee2e6;">
        <div id="theoretical-probability" style="background: #e3f2fd; padding: 15px; border-radius: 6px; margin-bottom: 15px;">
            <h5 style="margin: 0 0 10px 0; color: #1976d2;">📊 Xác suất Lý thuyết</h5>
            <div id="theoretical-values">Chọn thí nghiệm để xem xác suất lý thuyết</div>
        </div>
        
        <div id="experimental-results" style="background: #f8f9fa; padding: 15px; border-radius: 6px; margin-bottom: 15px;">
            <h5 style="margin: 0 0 10px 0; color: #495057;">🧪 Kết quả Thực nghiệm</h5>
            <div id="experimental-values">Chưa có dữ liệu</div>
        </div>
        
        <div id="convergence-chart" style="background: #fff; padding: 15px; border-radius: 6px; border: 1px solid #dee2e6;">
            <h5 style="margin: 0 0 10px 0; color: #495057;">📈 Biểu đồ Hội tụ</h5>
            <canvas id="probability-chart" width="400" height="200" style="width: 100%; max-width: 400px; height: 200px;"></canvas>
        </div>
    </div>
</div>

<script>
let simulationConfig = {
    type: 'coin',
    trials: 0,
    maxTrials: 1000,
    results: {},
    isRunning: false,
    intervalId: null,
    chartData: []
};

function setupExperiment() {
    const type = document.getElementById('experiment-type').value;
    const configDiv = document.getElementById('experiment-config');
    const theoreticalDiv = document.getElementById('theoretical-values');
    
    simulationConfig.type = type;
    simulationConfig.results = {};
    simulationConfig.chartData = [];
    
    switch(type) {
        case 'coin':
            configDiv.innerHTML = `
                <div style="background: #f8f9fa; padding: 15px; border-radius: 6px;">
                    <h6>Cấu hình: Tung đồng xu</h6>
                    <p>Biến cố quan tâm: Xuất hiện mặt ngửa (H)</p>
                </div>
            `;
            theoreticalDiv.innerHTML = `
                <div><strong>P(H) = 1/2 = 0.5</strong></div>
                <div><strong>P(T) = 1/2 = 0.5</strong></div>
                <div style="margin-top: 10px; font-size: 0.9em; color: #666;">
                    Không gian mẫu: Ω = {H, T}
                </div>
            `;
            break;
            
        case 'dice':
            configDiv.innerHTML = `
                <div style="background: #f8f9fa; padding: 15px; border-radius: 6px;">
                    <h6>Cấu hình: Tung xúc xắc</h6>
                    <label>Biến cố quan tâm:</label>
                    <select id="dice-event" style="width: 100%; padding: 6px; margin-top: 5px;">
                        <option value="6">Ra mặt 6</option>
                        <option value="even">Ra số chẵn (2,4,6)</option>
                        <option value="greater-4">Ra số > 4</option>
                    </select>
                </div>
            `;
            updateDiceTheoretical();
            break;
            
        case 'two-dice':
            configDiv.innerHTML = `
                <div style="background: #f8f9fa; padding: 15px; border-radius: 6px;">
                    <h6>Cấu hình: Tung hai xúc xắc</h6>
                    <label>Biến cố quan tâm:</label>
                    <select id="two-dice-event" style="width: 100%; padding: 6px; margin-top: 5px;">
                        <option value="sum-7">Tổng = 7</option>
                        <option value="sum-11">Tổng = 11</option>
                        <option value="double">Hai mặt giống nhau</option>
                        <option value="sum-even">Tổng chẵn</option>
                    </select>
                </div>
            `;
            updateTwoDiceTheoretical();
            break;
            
        case 'cards':
            configDiv.innerHTML = `
                <div style="background: #f8f9fa; padding: 15px; border-radius: 6px;">
                    <h6>Cấu hình: Rút bài từ bộ 52 lá</h6>
                    <label>Biến cố quan tâm:</label>
                    <select id="card-event" style="width: 100%; padding: 6px; margin-top: 5px;">
                        <option value="ace">Rút được Ace</option>
                        <option value="heart">Rút được bài Cơ</option>
                        <option value="face">Rút được J, Q, K</option>
                        <option value="red">Rút được bài đỏ</option>
                    </select>
                </div>
            `;
            updateCardTheoretical();
            break;
            
        case 'balls':
            configDiv.innerHTML = `
                <div style="background: #f8f9fa; padding: 15px; border-radius: 6px;">
                    <h6>Cấu hình: Rút bi từ hộp</h6>
                    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-bottom: 10px;">
                        <div>
                            <label>Bi đỏ:</label>
                            <input type="number" id="red-balls" min="0" max="50" value="5" style="width: 100%; padding: 4px;">
                        </div>
                        <div>
                            <label>Bi xanh:</label>
                            <input type="number" id="blue-balls" min="0" max="50" value="3" style="width: 100%; padding: 4px;">
                        </div>
                        <div>
                            <label>Bi vàng:</label>
                            <input type="number" id="yellow-balls" min="0" max="50" value="2" style="width: 100%; padding: 4px;">
                        </div>
                    </div>
                    <label>Biến cố quan tâm:</label>
                    <select id="ball-event" style="width: 100%; padding: 6px; margin-top: 5px;">
                        <option value="red">Rút được bi đỏ</option>
                        <option value="blue">Rút được bi xanh</option>
                        <option value="yellow">Rút được bi vàng</option>
                    </select>
                </div>
            `;
            updateBallTheoretical();
            break;
    }
    
    // Add event listeners for dynamic updates
    setTimeout(() => {
        const selects = configDiv.querySelectorAll('select');
        const inputs = configDiv.querySelectorAll('input');
        
        selects.forEach(select => {
            select.addEventListener('change', updateTheoreticalProbability);
        });
        
        inputs.forEach(input => {
            input.addEventListener('input', updateTheoreticalProbability);
        });
    }, 100);
}

function updateDiceTheoretical() {
    const event = document.getElementById('dice-event')?.value || '6';
    const theoreticalDiv = document.getElementById('theoretical-values');
    
    let probability, description;
    switch(event) {
        case '6':
            probability = 1/6;
            description = 'P(mặt 6) = 1/6 ≈ 0.167';
            break;
        case 'even':
            probability = 3/6;
            description = 'P(chẵn) = 3/6 = 1/2 = 0.5';
            break;
        case 'greater-4':
            probability = 2/6;
            description = 'P(> 4) = 2/6 = 1/3 ≈ 0.333';
            break;
    }
    
    theoreticalDiv.innerHTML = `
        <div><strong>${description}</strong></div>
        <div style="margin-top: 10px; font-size: 0.9em; color: #666;">
            Không gian mẫu: Ω = {1, 2, 3, 4, 5, 6}, |Ω| = 6
        </div>
    `;
}

function updateTwoDiceTheoretical() {
    const event = document.getElementById('two-dice-event')?.value || 'sum-7';
    const theoreticalDiv = document.getElementById('theoretical-values');
    
    let probability, description;
    switch(event) {
        case 'sum-7':
            probability = 6/36;
            description = 'P(tổng = 7) = 6/36 = 1/6 ≈ 0.167';
            break;
        case 'sum-11':
            probability = 2/36;
            description = 'P(tổng = 11) = 2/36 = 1/18 ≈ 0.056';
            break;
        case 'double':
            probability = 6/36;
            description = 'P(hai mặt giống nhau) = 6/36 = 1/6 ≈ 0.167';
            break;
        case 'sum-even':
            probability = 18/36;
            description = 'P(tổng chẵn) = 18/36 = 1/2 = 0.5';
            break;
    }
    
    theoreticalDiv.innerHTML = `
        <div><strong>${description}</strong></div>
        <div style="margin-top: 10px; font-size: 0.9em; color: #666;">
            Không gian mẫu: |Ω| = 36 (6×6 kết quả)
        </div>
    `;
}

function updateCardTheoretical() {
    const event = document.getElementById('card-event')?.value || 'ace';
    const theoreticalDiv = document.getElementById('theoretical-values');
    
    let probability, description;
    switch(event) {
        case 'ace':
            probability = 4/52;
            description = 'P(Ace) = 4/52 = 1/13 ≈ 0.077';
            break;
        case 'heart':
            probability = 13/52;
            description = 'P(Cơ) = 13/52 = 1/4 = 0.25';
            break;
        case 'face':
            probability = 12/52;
            description = 'P(J,Q,K) = 12/52 = 3/13 ≈ 0.231';
            break;
        case 'red':
            probability = 26/52;
            description = 'P(đỏ) = 26/52 = 1/2 = 0.5';
            break;
    }
    
    theoreticalDiv.innerHTML = `
        <div><strong>${description}</strong></div>
        <div style="margin-top: 10px; font-size: 0.9em; color: #666;">
            Bộ bài chuẩn: 52 lá (4 chất × 13 lá)
        </div>
    `;
}

function updateBallTheoretical() {
    const red = parseInt(document.getElementById('red-balls')?.value || 5);
    const blue = parseInt(document.getElementById('blue-balls')?.value || 3);
    const yellow = parseInt(document.getElementById('yellow-balls')?.value || 2);
    const total = red + blue + yellow;
    const event = document.getElementById('ball-event')?.value || 'red';
    
    const theoreticalDiv = document.getElementById('theoretical-values');
    
    let count, probability, description;
    switch(event) {
        case 'red':
            count = red;
            probability = red / total;
            description = `P(bi đỏ) = ${red}/${total} ≈ ${probability.toFixed(3)}`;
            break;
        case 'blue':
            count = blue;
            probability = blue / total;
            description = `P(bi xanh) = ${blue}/${total} ≈ ${probability.toFixed(3)}`;
            break;
        case 'yellow':
            count = yellow;
            probability = yellow / total;
            description = `P(bi vàng) = ${yellow}/${total} ≈ ${probability.toFixed(3)}`;
            break;
    }
    
    theoreticalDiv.innerHTML = `
        <div><strong>${description}</strong></div>
        <div style="margin-top: 10px; font-size: 0.9em; color: #666;">
            Tổng số bi: ${total} (${red} đỏ + ${blue} xanh + ${yellow} vàng)
        </div>
    `;
}

function updateTheoreticalProbability() {
    switch(simulationConfig.type) {
        case 'dice':
            updateDiceTheoretical();
            break;
        case 'two-dice':
            updateTwoDiceTheoretical();
            break;
        case 'cards':
            updateCardTheoretical();
            break;
        case 'balls':
            updateBallTheoretical();
            break;
    }
}

function performSingleTrial() {
    switch(simulationConfig.type) {
        case 'coin':
            return Math.random() < 0.5 ? 'H' : 'T';
            
        case 'dice':
            return Math.floor(Math.random() * 6) + 1;
            
        case 'two-dice':
            const die1 = Math.floor(Math.random() * 6) + 1;
            const die2 = Math.floor(Math.random() * 6) + 1;
            return [die1, die2];
            
        case 'cards':
            return Math.floor(Math.random() * 52) + 1;
            
        case 'balls':
            const red = parseInt(document.getElementById('red-balls').value);
            const blue = parseInt(document.getElementById('blue-balls').value);
            const yellow = parseInt(document.getElementById('yellow-balls').value);
            const total = red + blue + yellow;
            const rand = Math.floor(Math.random() * total);
            
            if (rand < red) return 'red';
            if (rand < red + blue) return 'blue';
            return 'yellow';
    }
}

function checkEvent(result) {
    switch(simulationConfig.type) {
        case 'coin':
            return result === 'H';
            
        case 'dice':
            const diceEvent = document.getElementById('dice-event').value;
            switch(diceEvent) {
                case '6': return result === 6;
                case 'even': return result % 2 === 0;
                case 'greater-4': return result > 4;
            }
            break;
            
        case 'two-dice':
            const [die1, die2] = result;
            const sum = die1 + die2;
            const twoDiceEvent = document.getElementById('two-dice-event').value;
            switch(twoDiceEvent) {
                case 'sum-7': return sum === 7;
                case 'sum-11': return sum === 11;
                case 'double': return die1 === die2;
                case 'sum-even': return sum % 2 === 0;
            }
            break;
            
        case 'cards':
            const cardEvent = document.getElementById('card-event').value;
            const suit = Math.floor((result - 1) / 13); // 0-3
            const rank = (result - 1) % 13; // 0-12
            
            switch(cardEvent) {
                case 'ace': return rank === 0;
                case 'heart': return suit === 0;
                case 'face': return rank >= 10;
                case 'red': return suit === 0 || suit === 1;
            }
            break;
            
        case 'balls':
            const ballEvent = document.getElementById('ball-event').value;
            return result === ballEvent;
    }
    return false;
}

function startSimulation() {
    if (simulationConfig.isRunning) {
        pauseSimulation();
        return;
    }
    
    simulationConfig.maxTrials = parseInt(document.getElementById('num-trials').value);
    simulationConfig.isRunning = true;
    
    document.getElementById('sim-start-btn').innerHTML = '⏸️ Tạm dừng';
    document.getElementById('sim-pause-btn').disabled = false;
    
    const speed = parseInt(document.getElementById('simulation-speed').value);
    const displayMode = document.getElementById('display-mode').value;
    
    if (displayMode === 'final') {
        // Run all trials at once
        runAllTrials();
    } else {
        // Run trials with animation
        simulationConfig.intervalId = setInterval(() => {
            if (simulationConfig.trials >= simulationConfig.maxTrials) {
                pauseSimulation();
                return;
            }
            
            const batchSize = displayMode === 'batch' ? 10 : 1;
            for (let i = 0; i < batchSize && simulationConfig.trials < simulationConfig.maxTrials; i++) {
                runSingleTrial();
            }
            
            updateDisplay();
        }, speed);
    }
}

function runSingleTrial() {
    const result = performSingleTrial();
    const success = checkEvent(result);
    
    simulationConfig.trials++;
    
    if (!simulationConfig.results.successes) {
        simulationConfig.results.successes = 0;
    }
    
    if (success) {
        simulationConfig.results.successes++;
    }
    
    // Update chart data every 10 trials
    if (simulationConfig.trials % 10 === 0) {
        const probability = simulationConfig.results.successes / simulationConfig.trials;
        simulationConfig.chartData.push({
            trial: simulationConfig.trials,
            probability: probability
        });
    }
}

function runAllTrials() {
    for (let i = 0; i < simulationConfig.maxTrials; i++) {
        runSingleTrial();
    }
    updateDisplay();
    pauseSimulation();
}

function updateDisplay() {
    const experimentalDiv = document.getElementById('experimental-values');
    const probability = simulationConfig.results.successes / simulationConfig.trials;
    
    experimentalDiv.innerHTML = `
        <div><strong>Số lần thành công: ${simulationConfig.results.successes}/${simulationConfig.trials}</strong></div>
        <div><strong>Xác suất thực nghiệm: ${probability.toFixed(4)}</strong></div>
        <div style="margin-top: 10px; font-size: 0.9em; color: #666;">
            Tiến độ: ${((simulationConfig.trials / simulationConfig.maxTrials) * 100).toFixed(1)}%
        </div>
    `;
    
    updateChart();
}

function updateChart() {
    const canvas = document.getElementById('probability-chart');
    const ctx = canvas.getContext('2d');
    
    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    if (simulationConfig.chartData.length === 0) return;
    
    const width = canvas.width;
    const height = canvas.height;
    const padding = 40;
    
    // Draw axes
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(padding, height - padding);
    ctx.lineTo(width - padding, height - padding);
    ctx.moveTo(padding, padding);
    ctx.lineTo(padding, height - padding);
    ctx.stroke();
    
    // Draw theoretical probability line
    const theoreticalP = getTheoreticalProbability();
    const theoreticalY = height - padding - (theoreticalP * (height - 2 * padding));
    
    ctx.strokeStyle = '#dc3545';
    ctx.lineWidth = 2;
    ctx.setLineDash([5, 5]);
    ctx.beginPath();
    ctx.moveTo(padding, theoreticalY);
    ctx.lineTo(width - padding, theoreticalY);
    ctx.stroke();
    ctx.setLineDash([]);
    
    // Draw experimental data
    if (simulationConfig.chartData.length > 1) {
        ctx.strokeStyle = '#007bff';
        ctx.lineWidth = 2;
        ctx.beginPath();
        
        const maxTrials = simulationConfig.maxTrials;
        
        simulationConfig.chartData.forEach((point, index) => {
            const x = padding + (point.trial / maxTrials) * (width - 2 * padding);
            const y = height - padding - (point.probability * (height - 2 * padding));
            
            if (index === 0) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        });
        
        ctx.stroke();
    }
    
    // Add labels
    ctx.fillStyle = '#333';
    ctx.font = '12px Arial';
    ctx.fillText('Trials', width / 2 - 20, height - 10);
    
    ctx.save();
    ctx.translate(15, height / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.fillText('Probability', -30, 0);
    ctx.restore();
}

function getTheoreticalProbability() {
    switch(simulationConfig.type) {
        case 'coin': return 0.5;
        case 'dice':
            const diceEvent = document.getElementById('dice-event').value;
            switch(diceEvent) {
                case '6': return 1/6;
                case 'even': return 0.5;
                case 'greater-4': return 1/3;
            }
            break;
        case 'two-dice':
            const twoDiceEvent = document.getElementById('two-dice-event').value;
            switch(twoDiceEvent) {
                case 'sum-7': return 6/36;
                case 'sum-11': return 2/36;
                case 'double': return 6/36;
                case 'sum-even': return 0.5;
            }
            break;
        case 'cards':
            const cardEvent = document.getElementById('card-event').value;
            switch(cardEvent) {
                case 'ace': return 4/52;
                case 'heart': return 13/52;
                case 'face': return 12/52;
                case 'red': return 0.5;
            }
            break;
        case 'balls':
            const red = parseInt(document.getElementById('red-balls').value);
            const blue = parseInt(document.getElementById('blue-balls').value);
            const yellow = parseInt(document.getElementById('yellow-balls').value);
            const total = red + blue + yellow;
            const ballEvent = document.getElementById('ball-event').value;
            
            switch(ballEvent) {
                case 'red': return red / total;
                case 'blue': return blue / total;
                case 'yellow': return yellow / total;
            }
            break;
    }
    return 0.5;
}

function pauseSimulation() {
    simulationConfig.isRunning = false;
    if (simulationConfig.intervalId) {
        clearInterval(simulationConfig.intervalId);
    }
    
    document.getElementById('sim-start-btn').innerHTML = '▶️ Tiếp tục';
    document.getElementById('sim-pause-btn').disabled = true;
}

function resetSimulation() {
    pauseSimulation();
    simulationConfig.trials = 0;
    simulationConfig.results = {};
    simulationConfig.chartData = [];
    
    document.getElementById('sim-start-btn').innerHTML = '▶️ Bắt đầu Mô phỏng';
    document.getElementById('experimental-values').innerHTML = 'Chưa có dữ liệu';
    
    const canvas = document.getElementById('probability-chart');
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    setupExperiment();
});
</script>

## Quy tắc Xác suất

### Quy tắc Cộng

**Cho hai biến cố A và B**:

P(A ∪ B) = P(A) + P(B) - P(A ∩ B)

**Trường hợp đặc biệt** (A và B xung khắc):
P(A ∪ B) = P(A) + P(B)

### Quy tắc Nhân

**Xác suất có điều kiện**: P(A|B) = P(A ∩ B) / P(B)

**Quy tắc nhân tổng quát**: P(A ∩ B) = P(A|B) × P(B)

**Trường hợp độc lập**: P(A ∩ B) = P(A) × P(B)

## Ví dụ Tính toán

### Ví dụ 1: Tung hai đồng xu
Tìm xác suất có ít nhất một mặt ngửa.

**Giải**:
- Ω = {HH, HT, TH, TT}, |Ω| = 4
- A = "ít nhất một H" = {HH, HT, TH}
- P(A) = 3/4 = 0.75

**Cách khác**: P(A) = 1 - P(A^c) = 1 - P(TT) = 1 - 1/4 = 3/4

### Ví dụ 2: Rút bài
Từ bộ 52 lá, rút 2 lá. Tìm xác suất cả hai đều là Ace.

**Giải**:
- Cách 1: P = C(4,2)/C(52,2) = 6/1326 = 1/221
- Cách 2: P = (4/52) × (3/51) = 12/2652 = 1/221

### Ví dụ 3: Bài toán sinh nhật
Trong 23 người, xác suất có ít nhất 2 người sinh cùng ngày là bao nhiêu?

**Giải**:
P(ít nhất 2 người cùng sinh nhật) = 1 - P(tất cả khác sinh nhật)

P(tất cả khác) = (365/365) × (364/365) × ... × (343/365) ≈ 0.493

P(ít nhất 2 cùng) ≈ 1 - 0.493 = 0.507 > 50%

## Ứng dụng trong Khoa học Máy tính

### 1. Thuật toán Randomized

```python
import random

def quicksort_randomized(arr):
    """QuickSort với pivot ngẫu nhiên"""
    if len(arr) <= 1:
        return arr
    
    # Chọn pivot ngẫu nhiên - giảm xác suất worst case
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort_randomized(left) + middle + quicksort_randomized(right)

def monte_carlo_pi(n):
    """Ước lượng π bằng phương pháp Monte Carlo"""
    inside_circle = 0
    
    for _ in range(n):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x*x + y*y <= 1:
            inside_circle += 1
    
    # P(điểm trong hình tròn) = π/4
    return 4 * inside_circle / n
```

### 2. Hash Functions và Bloom Filters

```python
class BloomFilter:
    def __init__(self, size, hash_functions):
        self.size = size
        self.bit_array = [0] * size
        self.hash_functions = hash_functions
    
    def add(self, item):
        for hash_func in self.hash_functions:
            index = hash_func(item) % self.size
            self.bit_array[index] = 1
    
    def contains(self, item):
        for hash_func in self.hash_functions:
            index = hash_func(item) % self.size
            if self.bit_array[index] == 0:
                return False  # Chắc chắn không có
        return True  # Có thể có (false positive possible)
    
    def false_positive_rate(self, n_items):
        """Tính xác suất false positive"""
        k = len(self.hash_functions)
        m = self.size
        n = n_items
        
        # P(false positive) ≈ (1 - e^(-kn/m))^k
        return (1 - math.exp(-k * n / m)) ** k
```

### 3. Load Testing và Performance Analysis

```python
def simulate_server_load(arrival_rate, service_rate, simulation_time):
    """Mô phỏng tải server bằng quy trình Poisson"""
    import numpy as np
    
    # Thời gian giữa các request (exponential distribution)
    inter_arrival_times = np.random.exponential(1/arrival_rate, 
                                               int(simulation_time * arrival_rate * 2))
    
    # Thời gian xử lý (exponential distribution)  
    service_times = np.random.exponential(1/service_rate, len(inter_arrival_times))
    
    # Tính toán thống kê
    arrival_times = np.cumsum(inter_arrival_times)
    queue_lengths = []
    response_times = []
    
    # Simulation logic...
    return {
        'average_queue_length': np.mean(queue_lengths),
        'average_response_time': np.mean(response_times),
        'server_utilization': arrival_rate / service_rate
    }
```

## Bài tập thực hành

### Bài tập 1: Cơ bản
1. Tung 3 đồng xu. Tính xác suất có đúng 2 mặt ngửa.
2. Từ bộ bài 52 lá, rút 1 lá. Tính P(Ace hoặc bài Cơ).
3. Hộp có 5 bi đỏ và 3 bi xanh. Rút 2 bi không hoàn lại. Tính P(cả hai đều đỏ).

### Bài tập 2: Trung bình
1. Trong lớp 30 học sinh, xác suất có ít nhất 2 người sinh cùng tháng là bao nhiêu?
2. Mật khẩu gồm 4 chữ số. Tính xác suất có ít nhất 2 chữ số giống nhau.
3. Tung xúc xắc đến khi ra mặt 6. Tính xác suất cần đúng 3 lần tung.

### Bài tập 3: Ứng dụng
1. Hash table có 1000 slot. Sau khi thêm 50 key, ước tính xác suất collision.
2. Thuật toán randomized có xác suất thành công 0.7. Chạy 5 lần độc lập, tính P(ít nhất 1 lần thành công).
3. Server xử lý request với tỷ lệ lỗi 1%. Trong 100 request, tính P(có từ 2 lỗi trở lên).

<details>
<summary>Đáp án Bài tập 1</summary>

1. **P(đúng 2 H) = C(3,2) × (1/2)³ = 3/8 = 0.375**
2. **P(Ace ∪ Cơ) = P(Ace) + P(Cơ) - P(Ace Cơ) = 4/52 + 13/52 - 1/52 = 16/52 = 4/13**
3. **P(cả hai đỏ) = (5/8) × (4/7) = 20/56 = 5/14**

</details>

## Tóm tắt

**Xác suất Cơ bản** cung cấp nền tảng cho:

**Khái niệm chính**:
- Không gian mẫu Ω và biến cố A ⊆ Ω
- P(A) = |A|/|Ω| (trường hợp đồng khả năng)
- Tiên đề Kolmogorov: P(A) ≥ 0, P(Ω) = 1, tính cộng

**Quy tắc tính toán**:
- Quy tắc cộng: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
- Quy tắc nhân: P(A ∩ B) = P(A|B) × P(B)
- Độc lập: P(A ∩ B) = P(A) × P(B)

**Ứng dụng CS**:
- Thuật toán randomized và Monte Carlo
- Hash functions và Bloom filters
- Performance analysis và load testing
- Machine learning và AI

Trong bài tiếp theo, chúng ta sẽ học về **Biến ngẫu nhiên và Phân phối xác suất** - công cụ mạnh mẽ để mô hình hóa các hiện tượng ngẫu nhiên phức tạp.
