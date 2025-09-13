---
layout: post
title: "Giới thiệu Lý thuyết Đồ thị"
categories: chapter12
date: 2021-01-01
order: 1
required: true
lang: vi
---

# Giới thiệu Lý thuyết Đồ thị

Lý thuyết đồ thị là một trong những lĩnh vực quan trọng nhất của toán học rời rạc, với ứng dụng rộng rãi trong khoa học máy tính, mạng xã hội, logistics, sinh học và nhiều lĩnh vực khác. Đồ thị cung cấp mô hình trực quan và mạnh mẽ để biểu diễn các mối quan hệ phức tạp.

## Định nghĩa và Khái niệm Cơ bản

### Đồ thị

**Định nghĩa**: Đồ thị G là một cặp có thứ tự G = (V, E), trong đó:
- V là tập hợp các **đỉnh** (vertices/nodes)
- E là tập hợp các **cạnh** (edges) nối các đỉnh

**Ký hiệu**:
- |V| = n: số đỉnh
- |E| = m: số cạnh
- Cạnh nối đỉnh u và v: e = {u, v} hoặc (u, v)

### Các loại Đồ thị

#### 1. Đồ thị Vô hướng (Undirected Graph)
- Cạnh không có hướng: {u, v} = {v, u}
- Biểu diễn mối quan hệ đối xứng

#### 2. Đồ thị Có hướng (Directed Graph/Digraph)
- Cạnh có hướng: (u, v) ≠ (v, u)
- Biểu diễn mối quan hệ không đối xứng

#### 3. Đồ thị Có trọng số (Weighted Graph)
- Mỗi cạnh có trọng số w(e)
- Biểu diễn khoảng cách, chi phí, thời gian

#### 4. Đồ thị Đơn giản vs Đa đồ thị
- **Đơn giản**: Không có cạnh lặp và khuyên (self-loop)
- **Đa đồ thị**: Cho phép nhiều cạnh giữa 2 đỉnh

## Cách Biểu diễn Đồ thị

### 1. Ma trận Kề (Adjacency Matrix)

Cho đồ thị G = (V, E) với V = {v₁, v₂, ..., vₙ}

Ma trận kề A là ma trận n×n với:
A[i][j] = 1 nếu có cạnh từ vᵢ đến vⱼ, ngược lại = 0

**Ví dụ**: Đồ thị vô hướng với V = {1, 2, 3}, E = {{1,2}, {2,3}}
```
    1  2  3
1 [ 0  1  0 ]
2 [ 1  0  1 ]
3 [ 0  1  0 ]
```

### 2. Danh sách Kề (Adjacency List)

Mỗi đỉnh v có danh sách các đỉnh kề với nó.

**Ví dụ**:
- 1: [2]
- 2: [1, 3]  
- 3: [2]

### 3. Danh sách Cạnh (Edge List)

Liệt kê tất cả các cạnh: E = [{1,2}, {2,3}]

## Công cụ tương tác: Trình tạo và Phân tích Đồ thị

<div id="graph-builder" class="interactive-tool">
    <h4>🕸️ Trình tạo và Phân tích Đồ thị</h4>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
        <div>
            <label><strong>Loại đồ thị:</strong></label>
            <select id="graph-type" onchange="updateGraphType()" style="width: 100%; padding: 8px; margin-top: 5px;">
                <option value="undirected">Vô hướng</option>
                <option value="directed">Có hướng</option>
                <option value="weighted">Có trọng số</option>
            </select>
        </div>
        <div>
            <label><strong>Chế độ:</strong></label>
            <select id="graph-mode" style="width: 100%; padding: 8px; margin-top: 5px;">
                <option value="build">Xây dựng đồ thị</option>
                <option value="example">Ví dụ mẫu</option>
                <option value="random">Tạo ngẫu nhiên</option>
            </select>
        </div>
    </div>
    
    <div id="graph-input-section">
        <div style="margin-bottom: 15px;">
            <label><strong>Danh sách đỉnh (cách nhau bởi dấu phẩy):</strong></label>
            <input type="text" id="vertices-input" placeholder="A,B,C,D" value="A,B,C,D" style="width: 100%; padding: 8px; margin-top: 5px;">
        </div>
        
        <div style="margin-bottom: 15px;">
            <label><strong>Danh sách cạnh:</strong></label>
            <textarea id="edges-input" placeholder="A-B&#10;B-C&#10;C-D&#10;D-A" style="width: 100%; padding: 8px; margin-top: 5px; height: 100px;">A-B
B-C
C-D
D-A</textarea>
            <small style="color: #666;">
                Định dạng: A-B (vô hướng), A->B (có hướng), A-B:5 (có trọng số)
            </small>
        </div>
    </div>
    
    <div style="display: flex; gap: 10px; margin-bottom: 20px;">
        <button onclick="buildGraph()" style="flex: 1; padding: 10px; background: #007bff; color: white; border: none; border-radius: 6px; font-weight: bold;">
            🔨 Xây dựng Đồ thị
        </button>
        <button onclick="analyzeGraph()" style="flex: 1; padding: 10px; background: #28a745; color: white; border: none; border-radius: 6px; font-weight: bold;">
            📊 Phân tích
        </button>
        <button onclick="clearGraph()" style="flex: 1; padding: 10px; background: #6c757d; color: white; border: none; border-radius: 6px; font-weight: bold;">
            🗑️ Xóa
        </button>
    </div>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
        <div id="graph-visualization" style="background: white; padding: 15px; border-radius: 8px; border: 1px solid #dee2e6; min-height: 300px;">
            <h5>🎨 Trực quan hóa</h5>
            <svg id="graph-svg" width="100%" height="250" style="border: 1px solid #eee; border-radius: 4px;">
                <text x="50%" y="50%" text-anchor="middle" fill="#666">Nhập đồ thị để xem trực quan hóa</text>
            </svg>
        </div>
        
        <div id="graph-analysis" style="background: white; padding: 15px; border-radius: 8px; border: 1px solid #dee2e6; min-height: 300px;">
            <h5>📈 Phân tích</h5>
            <div id="analysis-results">
                <p style="color: #666; text-align: center;">Xây dựng đồ thị để xem phân tích</p>
            </div>
        </div>
    </div>
    
    <div id="representations-section" style="margin-top: 20px; background: #f8f9fa; padding: 15px; border-radius: 8px; display: none;">
        <h5>🔢 Các cách Biểu diễn</h5>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
            <div id="adjacency-matrix">
                <h6>Ma trận Kề</h6>
                <div id="matrix-display"></div>
            </div>
            <div id="adjacency-list">
                <h6>Danh sách Kề</h6>
                <div id="list-display"></div>
            </div>
        </div>
    </div>
</div>

<script>
let currentGraph = {
    vertices: [],
    edges: [],
    type: 'undirected',
    adjacencyMatrix: [],
    adjacencyList: {}
};

function updateGraphType() {
    const type = document.getElementById('graph-type').value;
    currentGraph.type = type;
    
    // Update input placeholder based on type
    const edgesInput = document.getElementById('edges-input');
    switch(type) {
        case 'undirected':
            edgesInput.placeholder = 'A-B\nB-C\nC-D\nD-A';
            break;
        case 'directed':
            edgesInput.placeholder = 'A->B\nB->C\nC->D\nD->A';
            break;
        case 'weighted':
            edgesInput.placeholder = 'A-B:5\nB-C:3\nC-D:2\nD-A:4';
            break;
    }
}

function buildGraph() {
    try {
        // Parse vertices
        const verticesText = document.getElementById('vertices-input').value.trim();
        const vertices = verticesText.split(',').map(v => v.trim()).filter(v => v);
        
        if (vertices.length === 0) {
            throw new Error('Vui lòng nhập ít nhất một đỉnh');
        }
        
        // Parse edges
        const edgesText = document.getElementById('edges-input').value.trim();
        const edgeLines = edgesText.split('\n').map(line => line.trim()).filter(line => line);
        
        const edges = [];
        const type = currentGraph.type;
        
        for (const line of edgeLines) {
            let edge;
            
            if (type === 'directed') {
                const match = line.match(/^(\w+)->(\w+)(?::(\d+(?:\.\d+)?))?$/);
                if (!match) throw new Error(`Định dạng cạnh không hợp lệ: ${line}`);
                
                const [, from, to, weight] = match;
                edge = {
                    from: from,
                    to: to,
                    weight: weight ? parseFloat(weight) : 1,
                    directed: true
                };
            } else {
                const match = line.match(/^(\w+)-(\w+)(?::(\d+(?:\.\d+)?))?$/);
                if (!match) throw new Error(`Định dạng cạnh không hợp lệ: ${line}`);
                
                const [, from, to, weight] = match;
                edge = {
                    from: from,
                    to: to,
                    weight: weight ? parseFloat(weight) : 1,
                    directed: false
                };
            }
            
            // Validate vertices exist
            if (!vertices.includes(edge.from) || !vertices.includes(edge.to)) {
                throw new Error(`Cạnh ${line} chứa đỉnh không tồn tại`);
            }
            
            edges.push(edge);
        }
        
        // Update current graph
        currentGraph.vertices = vertices;
        currentGraph.edges = edges;
        
        // Build adjacency representations
        buildAdjacencyMatrix();
        buildAdjacencyList();
        
        // Visualize
        visualizeGraph();
        
        // Show representations
        displayRepresentations();
        
        console.log('Graph built successfully:', currentGraph);
        
    } catch (error) {
        alert(`Lỗi: ${error.message}`);
    }
}

function buildAdjacencyMatrix() {
    const n = currentGraph.vertices.length;
    const matrix = Array(n).fill().map(() => Array(n).fill(0));
    
    currentGraph.edges.forEach(edge => {
        const fromIdx = currentGraph.vertices.indexOf(edge.from);
        const toIdx = currentGraph.vertices.indexOf(edge.to);
        
        if (currentGraph.type === 'weighted') {
            matrix[fromIdx][toIdx] = edge.weight;
            if (!edge.directed) {
                matrix[toIdx][fromIdx] = edge.weight;
            }
        } else {
            matrix[fromIdx][toIdx] = 1;
            if (!edge.directed) {
                matrix[toIdx][fromIdx] = 1;
            }
        }
    });
    
    currentGraph.adjacencyMatrix = matrix;
}

function buildAdjacencyList() {
    const list = {};
    
    // Initialize empty lists
    currentGraph.vertices.forEach(v => {
        list[v] = [];
    });
    
    // Add edges
    currentGraph.edges.forEach(edge => {
        if (currentGraph.type === 'weighted') {
            list[edge.from].push(`${edge.to}(${edge.weight})`);
            if (!edge.directed) {
                list[edge.to].push(`${edge.from}(${edge.weight})`);
            }
        } else {
            list[edge.from].push(edge.to);
            if (!edge.directed) {
                list[edge.to].push(edge.from);
            }
        }
    });
    
    currentGraph.adjacencyList = list;
}

function visualizeGraph() {
    const svg = document.getElementById('graph-svg');
    const width = svg.clientWidth || 400;
    const height = 250;
    
    // Clear previous content
    svg.innerHTML = '';
    
    if (currentGraph.vertices.length === 0) {
        svg.innerHTML = '<text x="50%" y="50%" text-anchor="middle" fill="#666">Không có đồ thị để hiển thị</text>';
        return;
    }
    
    // Position vertices in a circle
    const centerX = width / 2;
    const centerY = height / 2;
    const radius = Math.min(width, height) / 3;
    
    const positions = {};
    currentGraph.vertices.forEach((vertex, i) => {
        const angle = (2 * Math.PI * i) / currentGraph.vertices.length;
        positions[vertex] = {
            x: centerX + radius * Math.cos(angle),
            y: centerY + radius * Math.sin(angle)
        };
    });
    
    // Draw edges
    currentGraph.edges.forEach(edge => {
        const fromPos = positions[edge.from];
        const toPos = positions[edge.to];
        
        // Draw line
        const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
        line.setAttribute('x1', fromPos.x);
        line.setAttribute('y1', fromPos.y);
        line.setAttribute('x2', toPos.x);
        line.setAttribute('y2', toPos.y);
        line.setAttribute('stroke', '#007bff');
        line.setAttribute('stroke-width', '2');
        svg.appendChild(line);
        
        // Draw arrow for directed graphs
        if (edge.directed || currentGraph.type === 'directed') {
            const arrowSize = 8;
            const angle = Math.atan2(toPos.y - fromPos.y, toPos.x - fromPos.x);
            
            // Calculate arrow position (slightly before the target vertex)
            const arrowX = toPos.x - 20 * Math.cos(angle);
            const arrowY = toPos.y - 20 * Math.sin(angle);
            
            const arrow = document.createElementNS('http://www.w3.org/2000/svg', 'polygon');
            const x1 = arrowX - arrowSize * Math.cos(angle - Math.PI/6);
            const y1 = arrowY - arrowSize * Math.sin(angle - Math.PI/6);
            const x2 = arrowX - arrowSize * Math.cos(angle + Math.PI/6);
            const y2 = arrowY - arrowSize * Math.sin(angle + Math.PI/6);
            
            arrow.setAttribute('points', `${arrowX},${arrowY} ${x1},${y1} ${x2},${y2}`);
            arrow.setAttribute('fill', '#007bff');
            svg.appendChild(arrow);
        }
        
        // Draw weight label
        if (currentGraph.type === 'weighted' && edge.weight !== 1) {
            const midX = (fromPos.x + toPos.x) / 2;
            const midY = (fromPos.y + toPos.y) / 2;
            
            const weightLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            weightLabel.setAttribute('x', midX);
            weightLabel.setAttribute('y', midY - 5);
            weightLabel.setAttribute('text-anchor', 'middle');
            weightLabel.setAttribute('fill', '#dc3545');
            weightLabel.setAttribute('font-size', '12');
            weightLabel.setAttribute('font-weight', 'bold');
            weightLabel.textContent = edge.weight;
            svg.appendChild(weightLabel);
        }
    });
    
    // Draw vertices
    currentGraph.vertices.forEach(vertex => {
        const pos = positions[vertex];
        
        // Draw circle
        const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        circle.setAttribute('cx', pos.x);
        circle.setAttribute('cy', pos.y);
        circle.setAttribute('r', '15');
        circle.setAttribute('fill', '#fff');
        circle.setAttribute('stroke', '#333');
        circle.setAttribute('stroke-width', '2');
        svg.appendChild(circle);
        
        // Draw label
        const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');
        label.setAttribute('x', pos.x);
        label.setAttribute('y', pos.y + 4);
        label.setAttribute('text-anchor', 'middle');
        label.setAttribute('fill', '#333');
        label.setAttribute('font-weight', 'bold');
        label.textContent = vertex;
        svg.appendChild(label);
    });
}

function analyzeGraph() {
    if (currentGraph.vertices.length === 0) {
        alert('Vui lòng xây dựng đồ thị trước khi phân tích');
        return;
    }
    
    const analysis = {
        numVertices: currentGraph.vertices.length,
        numEdges: currentGraph.edges.length,
        density: 0,
        degrees: {},
        isConnected: false,
        hasCycles: false
    };
    
    // Calculate density
    const maxEdges = currentGraph.type === 'directed' ? 
        analysis.numVertices * (analysis.numVertices - 1) :
        analysis.numVertices * (analysis.numVertices - 1) / 2;
    
    analysis.density = maxEdges > 0 ? (analysis.numEdges / maxEdges) : 0;
    
    // Calculate degrees
    currentGraph.vertices.forEach(v => {
        analysis.degrees[v] = 0;
    });
    
    currentGraph.edges.forEach(edge => {
        analysis.degrees[edge.from]++;
        if (!edge.directed && currentGraph.type !== 'directed') {
            analysis.degrees[edge.to]++;
        }
    });
    
    // Simple connectivity check (for undirected graphs)
    if (currentGraph.type === 'undirected') {
        analysis.isConnected = checkConnectivity();
    }
    
    displayAnalysis(analysis);
}

function checkConnectivity() {
    if (currentGraph.vertices.length <= 1) return true;
    
    const visited = new Set();
    const stack = [currentGraph.vertices[0]];
    
    while (stack.length > 0) {
        const vertex = stack.pop();
        if (visited.has(vertex)) continue;
        
        visited.add(vertex);
        
        // Add neighbors to stack
        currentGraph.edges.forEach(edge => {
            if (edge.from === vertex && !visited.has(edge.to)) {
                stack.push(edge.to);
            }
            if (!edge.directed && edge.to === vertex && !visited.has(edge.from)) {
                stack.push(edge.from);
            }
        });
    }
    
    return visited.size === currentGraph.vertices.length;
}

function displayAnalysis(analysis) {
    const resultsDiv = document.getElementById('analysis-results');
    
    const degreeList = Object.entries(analysis.degrees)
        .map(([v, d]) => `${v}: ${d}`)
        .join(', ');
    
    resultsDiv.innerHTML = `
        <div style="background: #f8f9fa; padding: 15px; border-radius: 6px;">
            <h6>📊 Thống kê cơ bản:</h6>
            <div style="margin-bottom: 10px;">
                <strong>Số đỉnh:</strong> ${analysis.numVertices}<br>
                <strong>Số cạnh:</strong> ${analysis.numEdges}<br>
                <strong>Mật độ:</strong> ${(analysis.density * 100).toFixed(1)}%
            </div>
            
            <h6>🔗 Bậc của các đỉnh:</h6>
            <div style="background: white; padding: 10px; border-radius: 4px; font-family: monospace; font-size: 0.9em;">
                ${degreeList}
            </div>
            
            ${currentGraph.type === 'undirected' ? `
                <div style="margin-top: 10px;">
                    <strong>Liên thông:</strong> 
                    <span style="color: ${analysis.isConnected ? '#28a745' : '#dc3545'};">
                        ${analysis.isConnected ? '✅ Có' : '❌ Không'}
                    </span>
                </div>
            ` : ''}
            
            <div style="margin-top: 15px; font-size: 0.9em; color: #666;">
                <strong>Loại đồ thị:</strong> ${getGraphTypeDescription()}
            </div>
        </div>
    `;
}

function getGraphTypeDescription() {
    const type = currentGraph.type;
    switch(type) {
        case 'undirected': return 'Đồ thị vô hướng';
        case 'directed': return 'Đồ thị có hướng';
        case 'weighted': return 'Đồ thị có trọng số';
        default: return 'Không xác định';
    }
}

function displayRepresentations() {
    const representationsSection = document.getElementById('representations-section');
    const matrixDisplay = document.getElementById('matrix-display');
    const listDisplay = document.getElementById('list-display');
    
    // Display adjacency matrix
    let matrixHTML = '<table style="border-collapse: collapse; font-family: monospace; font-size: 0.9em;">';
    
    // Header row
    matrixHTML += '<tr><td style="border: 1px solid #dee2e6; padding: 4px; background: #f8f9fa;"></td>';
    currentGraph.vertices.forEach(v => {
        matrixHTML += `<td style="border: 1px solid #dee2e6; padding: 4px; background: #f8f9fa; text-align: center; font-weight: bold;">${v}</td>`;
    });
    matrixHTML += '</tr>';
    
    // Data rows
    currentGraph.vertices.forEach((v, i) => {
        matrixHTML += `<tr><td style="border: 1px solid #dee2e6; padding: 4px; background: #f8f9fa; font-weight: bold;">${v}</td>`;
        currentGraph.adjacencyMatrix[i].forEach(val => {
            const cellColor = val > 0 ? '#d4edda' : '#fff';
            matrixHTML += `<td style="border: 1px solid #dee2e6; padding: 4px; text-align: center; background: ${cellColor};">${val}</td>`;
        });
        matrixHTML += '</tr>';
    });
    matrixHTML += '</table>';
    
    matrixDisplay.innerHTML = matrixHTML;
    
    // Display adjacency list
    let listHTML = '<div style="font-family: monospace; font-size: 0.9em;">';
    Object.entries(currentGraph.adjacencyList).forEach(([vertex, neighbors]) => {
        listHTML += `<div style="margin-bottom: 8px; padding: 8px; background: white; border-radius: 4px; border: 1px solid #dee2e6;">`;
        listHTML += `<strong>${vertex}:</strong> [${neighbors.join(', ')}]`;
        listHTML += '</div>';
    });
    listHTML += '</div>';
    
    listDisplay.innerHTML = listHTML;
    
    representationsSection.style.display = 'block';
}

function clearGraph() {
    currentGraph = {
        vertices: [],
        edges: [],
        type: 'undirected',
        adjacencyMatrix: [],
        adjacencyList: {}
    };
    
    document.getElementById('vertices-input').value = '';
    document.getElementById('edges-input').value = '';
    document.getElementById('graph-svg').innerHTML = '<text x="50%" y="50%" text-anchor="middle" fill="#666">Nhập đồ thị để xem trực quan hóa</text>';
    document.getElementById('analysis-results').innerHTML = '<p style="color: #666; text-align: center;">Xây dựng đồ thị để xem phân tích</p>';
    document.getElementById('representations-section').style.display = 'none';
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    updateGraphType();
});
</script>

## Các Khái niệm Cơ bản

### Bậc của Đỉnh (Degree)

**Đồ thị vô hướng**:
- deg(v) = số cạnh kề với đỉnh v
- **Định lý bắt tay**: Σ deg(v) = 2|E|

**Đồ thị có hướng**:
- deg⁺(v) = bậc ra (out-degree)
- deg⁻(v) = bậc vào (in-degree)
- deg(v) = deg⁺(v) + deg⁻(v)

### Đường đi và Chu trình

**Đường đi (Path)**: Dãy đỉnh v₀, v₁, ..., vₖ sao cho mỗi cặp liên tiếp được nối bởi cạnh.

**Đường đi đơn giản**: Không có đỉnh lặp lại (trừ có thể đỉnh đầu và cuối).

**Chu trình (Cycle)**: Đường đi đóng (v₀ = vₖ) với ít nhất 3 đỉnh.

### Tính Liên thông

**Đồ thị liên thông**: Có đường đi giữa mọi cặp đỉnh.

**Thành phần liên thông**: Tập con liên thông cực đại.

## Các Loại Đồ thị Đặc biệt

### 1. Đồ thị Đầy đủ (Complete Graph)

**Ký hiệu**: Kₙ
**Định nghĩa**: Mọi cặp đỉnh đều được nối bởi cạnh
**Số cạnh**: |E| = n(n-1)/2

### 2. Đồ thị Hai phía (Bipartite Graph)

**Định nghĩa**: Tập đỉnh có thể chia thành 2 tập rời nhau sao cho mọi cạnh nối 2 tập khác nhau.

**Ký hiệu**: G = (X ∪ Y, E) với X ∩ Y = ∅

**Đồ thị hai phía đầy đủ**: Kₘ,ₙ - mọi đỉnh trong X nối với mọi đỉnh trong Y.

### 3. Đồ thị Chu trình (Cycle Graph)

**Ký hiệu**: Cₙ
**Định nghĩa**: n đỉnh tạo thành một chu trình duy nhất

### 4. Đồ thị Bánh xe (Wheel Graph)

**Ký hiệu**: Wₙ
**Định nghĩa**: Cₙ + 1 đỉnh trung tâm nối với tất cả đỉnh của chu trình

## Ứng dụng trong Khoa học Máy tính

### 1. Mạng máy tính và Internet

```python
class NetworkGraph:
    def __init__(self):
        self.routers = {}  # Adjacency list representation
        
    def add_router(self, router_id):
        """Thêm router vào mạng"""
        if router_id not in self.routers:
            self.routers[router_id] = []
    
    def add_connection(self, router1, router2, bandwidth):
        """Thêm kết nối giữa 2 router"""
        self.routers[router1].append((router2, bandwidth))
        self.routers[router2].append((router1, bandwidth))
    
    def find_shortest_path(self, start, end):
        """Tìm đường đi ngắn nhất (Dijkstra's algorithm)"""
        # Implementation here...
        pass
    
    def check_connectivity(self):
        """Kiểm tra tính liên thông của mạng"""
        if not self.routers:
            return True
        
        visited = set()
        start = next(iter(self.routers))
        self._dfs(start, visited)
        
        return len(visited) == len(self.routers)
    
    def _dfs(self, node, visited):
        """Depth-First Search"""
        visited.add(node)
        for neighbor, _ in self.routers[node]:
            if neighbor not in visited:
                self._dfs(neighbor, visited)
```

### 2. Mạng xã hội

```python
class SocialNetwork:
    def __init__(self):
        self.users = {}
        self.friendships = {}
    
    def add_friendship(self, user1, user2):
        """Thêm mối quan hệ bạn bè (đồ thị vô hướng)"""
        if user1 not in self.friendships:
            self.friendships[user1] = set()
        if user2 not in self.friendships:
            self.friendships[user2] = set()
            
        self.friendships[user1].add(user2)
        self.friendships[user2].add(user1)
    
    def mutual_friends(self, user1, user2):
        """Tìm bạn chung"""
        friends1 = self.friendships.get(user1, set())
        friends2 = self.friendships.get(user2, set())
        return friends1.intersection(friends2)
    
    def friend_recommendations(self, user, max_recommendations=5):
        """Gợi ý kết bạn dựa trên bạn chung"""
        user_friends = self.friendships.get(user, set())
        recommendations = {}
        
        for friend in user_friends:
            friend_friends = self.friendships.get(friend, set())
            for potential_friend in friend_friends:
                if potential_friend != user and potential_friend not in user_friends:
                    recommendations[potential_friend] = recommendations.get(potential_friend, 0) + 1
        
        # Sort by number of mutual friends
        sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
        return sorted_recommendations[:max_recommendations]
```

### 3. Cấu trúc dữ liệu và Thuật toán

```python
class DependencyGraph:
    """Đồ thị phụ thuộc cho build systems"""
    
    def __init__(self):
        self.dependencies = {}  # target -> list of dependencies
        self.reverse_deps = {}  # dependency -> list of targets that depend on it
    
    def add_dependency(self, target, dependency):
        """Thêm phụ thuộc: target phụ thuộc vào dependency"""
        if target not in self.dependencies:
            self.dependencies[target] = []
        if dependency not in self.reverse_deps:
            self.reverse_deps[dependency] = []
            
        self.dependencies[target].append(dependency)
        self.reverse_deps[dependency].append(target)
    
    def topological_sort(self):
        """Sắp xếp topo để xác định thứ tự build"""
        in_degree = {}
        
        # Calculate in-degrees
        for target in self.dependencies:
            in_degree[target] = len(self.dependencies[target])
        
        # Find nodes with no dependencies
        queue = [target for target, degree in in_degree.items() if degree == 0]
        result = []
        
        while queue:
            current = queue.pop(0)
            result.append(current)
            
            # Update in-degrees of dependent targets
            for dependent in self.reverse_deps.get(current, []):
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)
        
        if len(result) != len(self.dependencies):
            raise ValueError("Circular dependency detected!")
        
        return result
    
    def has_cycle(self):
        """Kiểm tra chu trình (circular dependency)"""
        try:
            self.topological_sort()
            return False
        except ValueError:
            return True
```

## Bài tập thực hành

### Bài tập 1: Cơ bản
1. Vẽ đồ thị K₅ và tính số cạnh.
2. Chứng minh rằng trong đồ thị n đỉnh, số đỉnh có bậc lẻ là chẵn.
3. Tìm tất cả đồ thị đơn giản có 4 đỉnh và 3 cạnh.

### Bài tập 2: Biểu diễn
1. Cho đồ thị với ma trận kề, vẽ đồ thị và viết danh sách kề.
2. Chuyển đổi giữa các cách biểu diễn đồ thị.
3. So sánh độ phức tạp không gian của ma trận kề và danh sách kề.

### Bài tập 3: Ứng dụng
1. Mô hình hóa mạng máy tính trong phòng lab bằng đồ thị.
2. Thiết kế cấu trúc dữ liệu để biểu diễn mạng xã hội.
3. Sử dụng đồ thị để mô hình hóa hệ thống phụ thuộc package.

<details>
<summary>Đáp án Bài tập 1</summary>

1. **K₅**: 5 đỉnh, mỗi đỉnh nối với 4 đỉnh khác → |E| = 5×4/2 = 10 cạnh
2. **Định lý bắt tay**: Σ deg(v) = 2|E| (chẵn) → số đỉnh bậc lẻ phải chẵn
3. **4 đỉnh, 3 cạnh**: Đường đi P₄, Sao K₁,₃, và các biến thể

</details>

## Tóm tắt

**Lý thuyết Đồ thị** cung cấp:

**Khái niệm cơ bản**:
- Đồ thị G = (V, E): đỉnh và cạnh
- Các loại: vô hướng, có hướng, có trọng số
- Biểu diễn: ma trận kề, danh sách kề, danh sách cạnh

**Tính chất quan trọng**:
- Bậc đỉnh và định lý bắt tay
- Đường đi, chu trình, tính liên thông
- Các loại đồ thị đặc biệt (K_n, C_n, bipartite)

**Ứng dụng CS**:
- Mạng máy tính và routing algorithms
- Mạng xã hội và recommendation systems
- Dependency graphs và topological sorting
- Data structures và graph algorithms

Trong bài tiếp theo, chúng ta sẽ học về **Thuật toán Đồ thị** - các phương pháp duyệt, tìm đường đi ngắn nhất và các thuật toán quan trọng khác.
