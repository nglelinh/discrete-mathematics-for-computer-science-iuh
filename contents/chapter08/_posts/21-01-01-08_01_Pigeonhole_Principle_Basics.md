---
layout: post
title: "Nguyên lý Dirichlet cơ bản"
categories: chapter08
date: 2021-01-01
order: 1
required: true
lang: en
---

# Nguyên lý Dirichlet cơ bản

Nếu có 11 file mà chỉ 10 thư mục để chứa, ít nhất một thư mục phải nhận từ 2 file trở lên. Phát biểu nghe gần như hiển nhiên, nhưng đằng sau nó là một nguyên lý đếm cực mạnh, đủ sức giải nhiều bài toán mà thoạt nhìn chẳng liên quan gì đến "chim bồ câu và chuồng".


Nguyên lý Dirichlet thường được dùng khi ta không cần biết chính xác đối tượng nào trùng nhau, chỉ cần chứng minh chắc chắn rằng sự trùng lặp phải xảy ra.
**Nguyên lý Dirichlet** cho phép ta kết luận sự tồn tại mà không cần chỉ ra đối tượng cụ thể. Nó xuất hiện trong phân tích xung đột băm, phân phối dữ liệu, lập lịch, nén thông tin, và nhiều chứng minh tổ hợp rất gọn nhưng sắc.

Điểm hay của nguyên lý này là nó biến trực giác về "không thể phân bố đều mãi" thành một công cụ hình thức. Chỉ cần mô hình hóa đúng đâu là đồ vật, đâu là ngăn chứa, ta có thể rút ra kết luận bất ngờ từ một quan sát rất cơ bản.

Trong bài này, chúng ta sẽ học phát biểu chuẩn của nguyên lý Dirichlet và luyện cách nhận ra nó trong những bài toán tưởng như không liên quan.

## Phát biểu Nguyên lý

### Nguyên lý Dirichlet đơn giản

**Phát biểu**: Nếu n + 1 con bồ câu bay vào n cái chuồng, thì ít nhất một chuồng chứa nhiều hơn một con bồ câu.

**Phát biểu toán học**: Nếu n + 1 đối tượng được phân vào n nhóm, thì ít nhất một nhóm chứa ít nhất 2 đối tượng.

### Nguyên lý Dirichlet tổng quát

**Phát biểu**: Nếu N đối tượng được phân vào n nhóm, thì ít nhất một nhóm chứa ít nhất ⌈N/n⌉ đối tượng.

Trong đó ⌈x⌉ là hàm ceiling (làm tròn lên).

## Ví dụ cơ bản

### Ví dụ 1: Sinh nhật
Trong một lớp có 13 học sinh, chứng minh rằng ít nhất có 2 học sinh sinh trong cùng một tháng.

**Giải**:
- 13 học sinh (bồ câu)
- 12 tháng (chuồng)
- Theo nguyên lý Dirichlet: 13 > 12, nên ít nhất một tháng có ≥ 2 học sinh sinh trong đó.

### Ví dụ 2: Tóc trên đầu
Chứng minh rằng ở Hà Nội có ít nhất 2 người có cùng số sợi tóc trên đầu.

**Giải**:
- Dân số Hà Nội: ~8 triệu người
- Số sợi tóc tối đa: ~200,000 sợi
- 8,000,000 > 200,000, nên ít nhất 2 người có cùng số sợi tóc.

### Ví dụ 3: Điểm số
Trong 11 bài kiểm tra, mỗi bài được chấm từ 0-10 điểm. Chứng minh rằng có ít nhất 2 bài có cùng điểm số.

**Giải**:
- 11 bài kiểm tra
- 11 điểm số có thể (0,1,2,...,10)
- Theo nguyên lý Dirichlet: 11 = 11, nhưng nếu có 12 bài thì chắc chắn có 2 bài cùng điểm.

## Công cụ tương tác: Mô phỏng Nguyên lý Dirichlet

Nếu dùng công cụ này, hãy dự đoán kết quả trước rồi mới thao tác. Việc so sánh dự đoán với kết quả thật sẽ giúp khái niệm bám chắc hơn.

<div id="pigeonhole-simulator" class="interactive-tool">
    <h4>🐦 Mô phỏng Nguyên lý Dirichlet</h4>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin-bottom: 20px;">
        <div>
            <label><strong>Số đối tượng (N):</strong></label>
            <input type="number" id="num-objects" min="1" max="50" value="13" style="width: 100%; padding: 8px; margin-top: 5px;">
        </div>
        <div>
            <label><strong>Số nhóm (n):</strong></label>
            <input type="number" id="num-groups" min="1" max="20" value="12" style="width: 100%; padding: 8px; margin-top: 5px;">
        </div>
        <div>
            <label><strong>Tốc độ mô phỏng:</strong></label>
            <select id="simulation-speed" style="width: 100%; padding: 8px; margin-top: 5px;">
                <option value="100">Nhanh</option>
                <option value="300" selected>Vừa</option>
                <option value="600">Chậm</option>
            </select>
        </div>
    </div>
    
    <div style="margin-bottom: 20px;">
        <label><strong>Chọn ví dụ:</strong></label>
        <select id="example-selector" onchange="loadExample()" style="width: 100%; padding: 8px; margin-top: 5px;">
            <option value="">-- Chọn ví dụ --</option>
            <option value="birthday">Sinh nhật (13 người, 12 tháng)</option>
            <option value="socks">Tất (7 đôi, 3 màu)</option>
            <option value="cards">Bài (14 lá, 4 chất)</option>
            <option value="grades">Điểm số (12 bài, 11 điểm)</option>
        </select>
    </div>
    
    <div style="display: flex; gap: 10px; margin-bottom: 20px;">
        <button onclick="startSimulation()" id="start-btn" style="flex: 1; padding: 10px; background: #28a745; color: white; border: none; border-radius: 6px;">
            ▶️ Bắt đầu mô phỏng
        </button>
        <button onclick="resetSimulation()" style="flex: 1; padding: 10px; background: #6c757d; color: white; border: none; border-radius: 6px;">
            🔄 Đặt lại
        </button>
        <button onclick="stepSimulation()" style="flex: 1; padding: 10px; background: #007bff; color: white; border: none; border-radius: 6px;">
            ⏭️ Từng bước
        </button>
    </div>
    
    <div id="simulation-area" style="background: white; padding: 20px; border-radius: 8px; border: 1px solid #dee2e6; min-height: 300px;">
        <div id="prediction" style="background: #e3f2fd; padding: 15px; border-radius: 6px; margin-bottom: 20px;">
            <h5 style="margin: 0 0 10px 0; color: #1976d2;">📊 Dự đoán theo Nguyên lý Dirichlet</h5>
            <div id="prediction-text">Nhập số liệu để xem dự đoán</div>
        </div>
        
        <div id="visualization" style="margin-bottom: 20px;">
            <h5>🎯 Trực quan hóa:</h5>
            <div id="groups-display"></div>
        </div>
        
        <div id="simulation-log" style="background: #f8f9fa; padding: 15px; border-radius: 6px; max-height: 150px; overflow-y: auto;">
            <h6>📝 Nhật ký mô phỏng:</h6>
            <div id="log-content">Sẵn sàng bắt đầu...</div>
        </div>
    </div>
    <div data-demo="pigeonhole-visualizer"></div>
</div>

<script src="{{ '/public/js/pigeonhole-visualizer.js' | relative_url }}"></script>

<script>
let simulationState = {
    objects: [],
    groups: [],
    currentStep: 0,
    isRunning: false,
    intervalId: null
};

function loadExample() {
    const example = document.getElementById('example-selector').value;
    const objectsInput = document.getElementById('num-objects');
    const groupsInput = document.getElementById('num-groups');
    
    switch(example) {
        case 'birthday':
            objectsInput.value = 13;
            groupsInput.value = 12;
            break;
        case 'socks':
            objectsInput.value = 7;
            groupsInput.value = 3;
            break;
        case 'cards':
            objectsInput.value = 14;
            groupsInput.value = 4;
            break;
        case 'grades':
            objectsInput.value = 12;
            groupsInput.value = 11;
            break;
    }
    
    updatePrediction();
}

function updatePrediction() {
    const N = parseInt(document.getElementById('num-objects').value) || 0;
    const n = parseInt(document.getElementById('num-groups').value) || 1;
    const predictionDiv = document.getElementById('prediction-text');
    
    if (N === 0) {
        predictionDiv.innerHTML = 'Nhập số liệu để xem dự đoán';
        return;
    }
    
    const minInGroup = Math.ceil(N / n);
    const guarantee = N > n ? 'Chắc chắn' : 'Có thể';
    const color = N > n ? '#28a745' : '#ffc107';
    
    predictionDiv.innerHTML = `
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
            <div>
                <strong>Số đối tượng:</strong> ${N}<br>
                <strong>Số nhóm:</strong> ${n}<br>
                <strong>Tỷ lệ:</strong> ${(N/n).toFixed(2)}
            </div>
            <div style="color: ${color}; font-weight: bold;">
                <strong>${guarantee}</strong> có ít nhất 1 nhóm<br>
                chứa ≥ ${minInGroup} đối tượng<br>
                ${N > n ? '(Nguyên lý Dirichlet áp dụng)' : '(Không đảm bảo)'}
            </div>
        </div>
    `;
}

function initializeSimulation() {
    const N = parseInt(document.getElementById('num-objects').value);
    const n = parseInt(document.getElementById('num-groups').value);
    
    // Reset state
    simulationState.objects = Array.from({length: N}, (_, i) => ({
        id: i + 1,
        group: null,
        color: `hsl(${(i * 137.5) % 360}, 70%, 50%)`
    }));
    
    simulationState.groups = Array.from({length: n}, (_, i) => ({
        id: i + 1,
        objects: [],
        color: `hsl(${(i * 360 / n)}, 30%, 90%)`
    }));
    
    simulationState.currentStep = 0;
    simulationState.isRunning = false;
    
    updateVisualization();
    updateLog('Khởi tạo: ' + N + ' đối tượng, ' + n + ' nhóm');
}

function updateVisualization() {
    const groupsDiv = document.getElementById('groups-display');
    const n = simulationState.groups.length;
    
    let html = '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); gap: 10px;">';
    
    simulationState.groups.forEach(group => {
        html += `
            <div style="background: ${group.color}; border: 2px solid #dee2e6; border-radius: 8px; padding: 10px; text-align: center; min-height: 80px;">
                <div style="font-weight: bold; margin-bottom: 8px;">Nhóm ${group.id}</div>
                <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 4px;">
        `;
        
        group.objects.forEach(obj => {
            html += `<div style="width: 20px; height: 20px; background: ${obj.color}; border-radius: 50%; border: 1px solid #333; display: flex; align-items: center; justify-content: center; font-size: 10px; color: white; font-weight: bold;">${obj.id}</div>`;
        });
        
        html += `
                </div>
                <div style="margin-top: 8px; font-size: 0.9em; color: #666;">
                    ${group.objects.length} đối tượng
                </div>
            </div>
        `;
    });
    
    html += '</div>';
    groupsDiv.innerHTML = html;
}

function updateLog(message) {
    const logDiv = document.getElementById('log-content');
    const timestamp = new Date().toLocaleTimeString();
    logDiv.innerHTML += `<div>[${timestamp}] ${message}</div>`;
    logDiv.scrollTop = logDiv.scrollHeight;
}

function stepSimulation() {
    if (simulationState.currentStep >= simulationState.objects.length) {
        updateLog('Mô phỏng hoàn tất!');
        checkPigeonholePrinciple();
        return;
    }
    
    const obj = simulationState.objects[simulationState.currentStep];
    const randomGroup = Math.floor(Math.random() * simulationState.groups.length);
    
    // Assign object to group
    obj.group = randomGroup;
    simulationState.groups[randomGroup].objects.push(obj);
    
    updateVisualization();
    updateLog(`Đối tượng ${obj.id} → Nhóm ${randomGroup + 1} (${simulationState.groups[randomGroup].objects.length} đối tượng)`);
    
    simulationState.currentStep++;
    
    // Check if pigeonhole principle is triggered
    const maxInGroup = Math.max(...simulationState.groups.map(g => g.objects.length));
    const N = simulationState.objects.length;
    const n = simulationState.groups.length;
    const expectedMin = Math.ceil(N / n);
    
    if (maxInGroup >= expectedMin && N > n) {
        updateLog(`🎯 Nguyên lý Dirichlet được xác nhận! Nhóm có ${maxInGroup} đối tượng (≥ ${expectedMin})`);
    }
}

function startSimulation() {
    if (simulationState.isRunning) {
        stopSimulation();
        return;
    }
    
    if (simulationState.currentStep === 0) {
        initializeSimulation();
    }
    
    const speed = parseInt(document.getElementById('simulation-speed').value);
    simulationState.isRunning = true;
    document.getElementById('start-btn').innerHTML = '⏸️ Tạm dừng';
    
    simulationState.intervalId = setInterval(() => {
        stepSimulation();
        if (simulationState.currentStep >= simulationState.objects.length) {
            stopSimulation();
        }
    }, speed);
}

function stopSimulation() {
    simulationState.isRunning = false;
    if (simulationState.intervalId) {
        clearInterval(simulationState.intervalId);
    }
    document.getElementById('start-btn').innerHTML = '▶️ Tiếp tục';
}

function resetSimulation() {
    stopSimulation();
    simulationState.currentStep = 0;
    document.getElementById('start-btn').innerHTML = '▶️ Bắt đầu mô phỏng';
    document.getElementById('log-content').innerHTML = 'Sẵn sàng bắt đầu...';
    initializeSimulation();
}

function checkPigeonholePrinciple() {
    const N = simulationState.objects.length;
    const n = simulationState.groups.length;
    const groupSizes = simulationState.groups.map(g => g.objects.length);
    const maxSize = Math.max(...groupSizes);
    const expectedMin = Math.ceil(N / n);
    
    let result = '<div style="background: ';
    if (maxSize >= expectedMin && N > n) {
        result += '#d4edda; color: #155724;';
        result += '"><h6>✅ Nguyên lý Dirichlet được xác nhận!</h6>';
    } else {
        result += '#fff3cd; color: #856404;';
        result += '"><h6>⚠️ Trường hợp đặc biệt</h6>';
    }
    
    result += `
        <div>Nhóm lớn nhất: ${maxSize} đối tượng</div>
        <div>Dự đoán tối thiểu: ${expectedMin} đối tượng</div>
        <div>Phân bố: [${groupSizes.join(', ')}]</div>
    </div>`;
    
    updateLog(result);
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    // Add event listeners
    document.getElementById('num-objects').addEventListener('input', updatePrediction);
    document.getElementById('num-groups').addEventListener('input', updatePrediction);
    
    // Initial setup
    updatePrediction();
    initializeSimulation();
});
</script>

## Chứng minh Nguyên lý Dirichlet

### Chứng minh phản chứng

**Giả sử** mỗi chuồng chứa nhiều nhất 1 con bồ câu.

Khi đó, tổng số bồ câu ≤ n × 1 = n.

Nhưng ta có n + 1 con bồ câu, mâu thuẫn với giả thiết.

Vậy ít nhất một chuồng chứa ≥ 2 con bồ câu. ∎

### Chứng minh tổng quát

**Giả sử** mỗi nhóm chứa < ⌈N/n⌉ đối tượng.

Khi đó, mỗi nhóm chứa ≤ ⌈N/n⌉ - 1 đối tượng.

Tổng số đối tượng ≤ n × (⌈N/n⌉ - 1) < n × (N/n + 1 - 1) = N.

Mâu thuẫn! Vậy ít nhất một nhóm chứa ≥ ⌈N/n⌉ đối tượng. ∎

## Ứng dụng trong Khoa học Máy tính

### 1. Hash Tables và Collision
```python
def hash_collision_guarantee(num_keys, table_size):
    """Đảm bảo collision trong hash table"""
    if num_keys > table_size:
        return True, f"Chắc chắn có collision (≥{math.ceil(num_keys/table_size)} keys/bucket)"
    return False, "Không đảm bảo collision"

# Ví dụ: 1000 keys, 100 buckets
# Chắc chắn có bucket chứa ≥ 10 keys
```

### 2. Load Balancing
```python
def load_balancing_analysis(tasks, servers):
    """Phân tích cân bằng tải"""
    min_load_per_server = math.ceil(tasks / servers)
    return {
        'guaranteed_max_load': min_load_per_server,
        'is_perfectly_balanced': tasks % servers == 0,
        'overloaded_servers': max(0, tasks - servers * (min_load_per_server - 1))
    }
```

### 3. Thuật toán Randomized
```python
def birthday_attack_probability(hash_bits):
    """Tính xác suất collision trong hash function"""
    hash_space = 2 ** hash_bits
    # Theo nguyên lý Dirichlet: cần √(hash_space) attempts
    return math.sqrt(hash_space)

# SHA-256 (256 bits): cần ~2^128 attempts để guarantee collision
```

## Bài tập thực hành

### Bài tập 1: Cơ bản
1. Trong 367 người, chứng minh rằng có ít nhất 2 người sinh cùng ngày.
2. Chọn 5 điểm bất kỳ trong hình vuông 2×2. Chứng minh rằng có 2 điểm cách nhau ≤ √2.
3. Trong 10 số nguyên bất kỳ, chứng minh rằng có 2 số có cùng chữ số cuối.

### Bài tập 2: Trung bình
1. Chứng minh rằng trong 6 người bất kỳ, có 3 người quen nhau hoặc 3 người không quen nhau.
2. Trong dãy 101 số nguyên, chứng minh rằng có một đoạn con liên tiếp có tổng chia hết cho 100.
3. Cho 51 số nguyên từ 1 đến 100. Chứng minh rằng có 2 số mà một số chia hết cho số kia.

### Bài tập 3: Nâng cao
1. Trong mặt phẳng có 5 điểm, không có 3 điểm thẳng hàng. Chứng minh rằng có 4 điểm tạo thành tứ giác lồi.
2. Cho 2n + 1 số thực. Chứng minh rằng có thể chọn n + 1 số sao cho trung bình cộng ≥ trung bình cộng của tất cả.
3. Trong bảng n×n, mỗi ô chứa số 1 hoặc -1. Chứng minh rằng có 2 hàng hoặc 2 cột có tích vô hướng ≥ 0.

<details>
<summary>Đáp án Bài tập 1</summary>

1. **367 người, 366 ngày** → Theo nguyên lý Dirichlet: 367 > 366
2. **Chia hình vuông thành 4 ô 1×1** → 5 điểm, 4 ô → có ô chứa ≥ 2 điểm → khoảng cách ≤ đường chéo = √2
3. **10 số, 10 chữ số cuối (0-9)** → Theo nguyên lý Dirichlet: 10 = 10, nhưng nếu có 11 số thì chắc chắn

</details>

## Các biến thể của Nguyên lý Dirichlet

### 1. Nguyên lý Dirichlet mạnh
Nếu N đối tượng được phân vào n nhóm và N > kn, thì ít nhất một nhóm chứa > k đối tượng.

### 2. Nguyên lý Dirichlet liên tục
Nếu N đối tượng được phân bố liên tục trên độ dài L, thì có đoạn độ dài L/n chứa ≥ N/n đối tượng.

### 3. Nguyên lý Dirichlet xác suất
Nếu phân bố ngẫu nhiên N đối tượng vào n nhóm, xác suất để mỗi nhóm chứa ≤ k đối tượng giảm exponentially khi N tăng.

## Tóm tắt

Trước khi rời bài, hãy kiểm tra xem bạn có thể tự nhắc lại ý chính, điều kiện áp dụng và một ví dụ tiêu biểu mà không cần nhìn tài liệu hay không.

**Nguyên lý Dirichlet** là công cụ chứng minh mạnh mẽ:

**Phát biểu cơ bản**: N đối tượng, n nhóm (N > n) → ít nhất 1 nhóm có ≥ 2 đối tượng

**Phát biểu tổng quát**: N đối tượng, n nhóm → ít nhất 1 nhóm có ≥ ⌈N/n⌉ đối tượng

**Ứng dụng**:
- Hash tables và collision detection
- Load balancing trong hệ thống phân tán  
- Thuật toán randomized và cryptography
- Chứng minh tồn tại trong tổ hợp

**Kỹ thuật chứng minh**: Thường dùng phản chứng hoặc đếm trực tiếp

Trong bài tiếp theo, chúng ta sẽ học về **Nguyên lý Dirichlet nâng cao** với các ứng dụng phức tạp hơn trong lý thuyết số và hình học.
