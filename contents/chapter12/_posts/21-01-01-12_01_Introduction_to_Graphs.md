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

Từ Google Maps tìm đường ngắn nhất, Facebook gợi ý bạn bè, đến hệ thống mạng trong doanh nghiệp hay pipeline phụ thuộc giữa các tác vụ, rất nhiều bài toán hiện đại đều xoay quanh một ý tưởng chung: có những đối tượng và có những kết nối giữa chúng. Khi số kết nối lớn lên, ta cần một mô hình đủ gọn để nhìn toàn cục mà không lạc trong chi tiết.

**Lý thuyết đồ thị** chính là mô hình đó. Nó biến thành phố, mạng xã hội, mạng máy tính hay dependency graph thành đỉnh và cạnh để ta có thể đặt câu hỏi chính xác: có đường đi không, thành phần nào quan trọng, chỗ nào tắc nghẽn, cấu trúc nào tối ưu hơn? Đây là một trong những chương gắn với khoa học máy tính rõ nhất của toàn bộ môn học.

## Định nghĩa và Khái niệm Cơ bản

### Đồ thị

**Định nghĩa**: Đồ thị $$G$$ là một cặp có thứ tự $$G = (V, E)$$, trong đó:

- $$V$$ là tập hợp các **đỉnh** (vertices/nodes)
- $$E$$ là tập hợp các **cạnh** (edges) nối các đỉnh

**Ký hiệu**:

- $$\|V\| = n$$: số đỉnh
- $$\|E\| = m$$: số cạnh
- Cạnh nối đỉnh $$u$$ và $$v$$: $$e = \{u, v\}$$ hoặc $$(u, v)$$

### Các loại Đồ thị

#### 1. Đồ thị Vô hướng (Undirected Graph)

- Cạnh không có hướng: $$\{u, v\} = \{v, u\}$$
- Biểu diễn mối quan hệ đối xứng

#### 2. Đồ thị Có hướng (Directed Graph/Digraph)

- Cạnh có hướng: $$(u, v) \neq (v, u)$$
- Biểu diễn mối quan hệ không đối xứng (ví dụ: follow trên Twitter)

#### 3. Đồ thị Có trọng số (Weighted Graph)

- Mỗi cạnh có trọng số $$w(e)$$
- Biểu diễn khoảng cách, chi phí, thời gian

#### 4. Đồ thị Đơn giản vs Đa đồ thị

- **Đơn giản**: Không có cạnh lặp và khuyên (self-loop)
- **Đa đồ thị**: Cho phép nhiều cạnh giữa 2 đỉnh

<figure class="image" style="align: center;">
<p align="center">
  <img src="/discrete-mathematics-for-computer-science-iuh/img/chapter_img/chapter12/graph_types.svg" alt="Các loại đồ thị" width="80%" height="80%">
  <figcaption style="text-align: center;">Hình 12.2: Các loại đồ thị — vô hướng, có hướng, có trọng số, và đa đồ thị.</figcaption>
</p>
</figure>

## Cách Biểu diễn Đồ thị

### 1. Ma trận Kề (Adjacency Matrix)

Cho đồ thị $$G = (V, E)$$ với $$V = \{v_1, v_2, \dots, v_n\}$$.

Ma trận kề $$A$$ là ma trận $$n \times n$$ với:
$$A[i][j] = 1$$ nếu có cạnh từ $$v_i$$ đến $$v_j$$, ngược lại $$= 0$$

**Ví dụ**: Đồ thị vô hướng với $$V = \{1, 2, 3\}$$, $$E = [\{1,2\}, \{2,3\}]$$

```
     1  2  3
 1 [ 0  1  0 ]
 2 [ 1  0  1 ]
 3 [ 0  1  0 ]
```

### 2. Danh sách Kề (Adjacency List)

Mỗi đỉnh $$v$$ có danh sách các đỉnh kề với nó.

**Ví dụ**:
- 1: [2]
- 2: [1, 3]
- 3: [2]

### 3. Danh sách Cạnh (Edge List)

Liệt kê tất cả các cạnh: $$E = [\{1,2\}, \{2,3\}]$$

<div class="content-box warning-box" markdown="1">
**Chú ý về ký hiệu tập hợp**: Khi viết tập cạnh trong Jekyll, tránh dùng hai lớp ngoặc nhọn lồng nhau. Dùng ký hiệu danh sách `[{1,2}, {2,3}]` thay cho tập hợp.
</div>

<div class="content-box insight-box" markdown="1">
**So sánh hai cách biểu diễn**:

| Tiêu chí | Ma trận Kề | Danh sách Kề |
|----------|------------|--------------|
| Bộ nhớ | $$O(n^2)$$ | $$O(n + m)$$ |
| Kiểm tra cạnh $$(u,v)$$ | $$O(1)$$ | $$O(deg(u))$$ |
| Duyệt tất cả đỉnh kề | $$O(n)$$ | $$O(deg(u))$$ |
| Thích hợp cho | Đồ thị dày đặc | Đồ thị thưa |

Trong thực tế lập trình, **danh sách kề** được dùng phổ biến hơn vì hầu hết đồ thị trong ứng dụng thực tế đều thưa (sparse).
</div>

## Công cụ tương tác: Trình tạo và Phân tích Đồ thị

<div id="graph-builder" class="interactive-tool">
    <h4>Trình tạo và Phân tích Đồ thị</h4>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
        <div>
            <label><strong>Loại đồ thị:</strong></label>
            <select id="graph-type" onchange="updateGraphType()" style="width: 100%; padding: 8px; margin-top: 5px;">
                <option value="undirected">Vô hướng</option>
                <option value="directed">Có hướng</option>
                <option value="weighted">Có trọng số</option>
            </select>
        </div>
    </div>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
        <div>
            <label><strong>Danh sách đỉnh:</strong></label>
            <input type="text" id="vertices-input" value="A, B, C, D" placeholder="A, B, C, D" style="width: 100%; padding: 8px; margin-top: 5px;">
        </div>
        <div>
            <label><strong>Danh sách cạnh:</strong></label>
            <textarea id="edges-input" rows="4" placeholder="A-B&#10;B-C&#10;C-D&#10;D-A" style="width: 100%; padding: 8px; margin-top: 5px;">A-B
B-C
C-D
D-A</textarea>
        </div>
    </div>
    
    <button onclick="buildGraph()" style="background: #6f42c1; color: white; border: none; padding: 10px 20px; border-radius: 5px;">Xây dựng Đồ thị</button>
    <button onclick="analyzeGraph()" style="background: #28a745; color: white; border: none; padding: 10px 20px; border-radius: 5px; margin-left: 10px;">Phân tích</button>
    
    <div id="analysis-results" style="margin-top: 15px; padding: 15px; background: #f8f9fa; border-radius: 5px;">
        <p style="color: #666; text-align: center;">Xây dựng đồ thị để xem phân tích</p>
    </div>
    
    <div id="representations-section" style="margin-top: 20px; background: #f8f9fa; padding: 15px; border-radius: 8px; display: none;">
        <h5>Các cách Biểu diễn</h5>
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
        const verticesText = document.getElementById('vertices-input').value.trim();
        const vertices = verticesText.split(',').map(v => v.trim()).filter(v => v);
        if (vertices.length === 0) {
            throw new Error('Vui lòng nhập ít nhất một đỉnh');
        }
        const edgesText = document.getElementById('edges-input').value.trim();
        const edgeLines = edgesText.split('\n').map(line => line.trim()).filter(line => line);
        const edges = [];
        const type = currentGraph.type;
        for (const line of edgeLines) {
            let edge;
            if (type === 'directed') {
                const match = line.match(/^(\w+)->(\w+)(?::(\d+(?:\.\d+)?))?$/);
                if (!match) throw new Error('Định dạng cạnh không hợp lệ: ' + line);
                const [, u, v, w] = match;
                edge = { u, v, w: w ? parseFloat(w) : 1 };
            } else {
                const match = line.match(/^(\w+)-(\w+)(?::(\d+(?:\.\d+)?))?$/);
                if (!match) throw new Error('Định dạng cạnh không hợp lệ: ' + line);
                const [, u, v, w] = match;
                edge = { u, v, w: w ? parseFloat(w) : 1 };
            }
            edges.push(edge);
        }
        currentGraph.vertices = vertices;
        currentGraph.edges = edges;
        document.getElementById('analysis-results').innerHTML =
            '<p><strong>Đồ thị đã xây dựng:</strong> ' + vertices.length + ' đỉnh, ' + edges.length + ' cạnh</p>';
        document.getElementById('representations-section').style.display = 'block';
        displayRepresentations();
    } catch (e) {
        document.getElementById('analysis-results').innerHTML =
            '<p style="color: red;">Lỗi: ' + e.message + '</p>';
    }
}

function displayRepresentations() {
    const vertices = currentGraph.vertices;
    const n = vertices.length;
    const adjMatrix = Array.from({length: n}, () => Array(n).fill(0));
    const adjList = {};
    vertices.forEach(v => { adjList[v] = []; });
    for (const edge of currentGraph.edges) {
        const i = vertices.indexOf(edge.u);
        const j = vertices.indexOf(edge.v);
        if (i !== -1 && j !== -1) {
            adjMatrix[i][j] = 1;
            adjList[edge.u].push(edge.v);
            if (currentGraph.type === 'undirected') {
                adjMatrix[j][i] = 1;
                adjList[edge.v].push(edge.u);
            }
        }
    }
    let matrixHtml = '<table style="border-collapse: collapse; margin: 10px 0;">';
    matrixHtml += '<tr><td></td>';
    vertices.forEach(v => { matrixHtml += '<td style="padding: 5px 10px; font-weight: bold;">' + v + '</td>'; });
    matrixHtml += '</tr>';
    for (let i = 0; i < n; i++) {
        matrixHtml += '<tr><td style="padding: 5px 10px; font-weight: bold;">' + vertices[i] + '</td>';
        for (let j = 0; j < n; j++) {
            matrixHtml += '<td style="padding: 5px 10px; text-align: center;">' + adjMatrix[i][j] + '</td>';
        }
        matrixHtml += '</tr>';
    }
    matrixHtml += '</table>';
    document.getElementById('matrix-display').innerHTML = matrixHtml;
    let listHtml = '<ul style="list-style: none; padding: 0;">';
    for (const v of vertices) {
        listHtml += '<li><strong>' + v + '</strong>: [' + adjList[v].join(', ') + ']</li>';
    }
    listHtml += '</ul>';
    document.getElementById('list-display').innerHTML = listHtml;
}

function analyzeGraph() {
    if (currentGraph.vertices.length === 0) {
        document.getElementById('analysis-results').innerHTML =
            '<p style="color: red;">Hãy xây dựng đồ thị trước!</p>';
        return;
    }
    const V = currentGraph.vertices.length;
    const E = currentGraph.edges.length;
    const degrees = {};
    currentGraph.vertices.forEach(v => { degrees[v] = 0; });
    for (const edge of currentGraph.edges) {
        degrees[edge.u]++;
        if (currentGraph.type === 'undirected') degrees[edge.v]++;
    }
    let degStr = Object.entries(degrees).map(([v, d]) => v + ': ' + d).join(', ');
    document.getElementById('analysis-results').innerHTML =
        '<p><strong>Phân tích đồ thị:</strong></p>' +
        '<ul><li>Số đỉnh: ' + V + '</li>' +
        '<li>Số cạnh: ' + E + '</li>' +
        '<li>Bậc các đỉnh: ' + degStr + '</li></ul>';
}
</script>

## Bài tập thực hành

### Bài tập 1: Xác định loại đồ thị

Cho đồ thị $$G = (V, E)$$ với $$V = \{1, 2, 3, 4\}$$ và $$E = \{\{1,2\}, \{2,3\}, \{3,4\}, \{4,1\}, \{1,3\}\}$$. Vẽ đồ thị và xác định:

a) Đây là đồ thị loại gì?
b) Viết ma trận kề
c) Viết danh sách kề

<details>
<summary>Đáp án</summary>

a) Đồ thị vô hướng, đơn giản (không có cạnh lặp hay khuyên).

b) Ma trận kề:
```
     1  2  3  4
 1 [ 0  1  1  1 ]
 2 [ 1  0  1  0 ]
 3 [ 1  1  0  1 ]
 4 [ 1  0  1  0 ]
```

c) Danh sách kề:
- 1: [2, 3, 4]
- 2: [1, 3]
- 3: [1, 2, 4]
- 4: [1, 3]
</details>

### Bài tập 2: Bậc của đỉnh

Tính bậc của mỗi đỉnh trong đồ thị ở Bài tập 1. Đỉnh nào có bậc lớn nhất?

<details>
<summary>Đáp án</summary>

deg(1) = 3 (kề với 2, 3, 4)
deg(2) = 2 (kề với 1, 3)
deg(3) = 3 (kề với 1, 2, 4)
deg(4) = 2 (kề với 1, 3)

Đỉnh 1 và 3 có bậc lớn nhất (= 3).
</details>

## Tóm tắt

- **Đồ thị**: $$G = (V, E)$$ — tập đỉnh và tập cạnh
- **Phân loại**: vô hướng, có hướng, có trọng số, đơn/đa đồ thị
- **Biểu diễn**: ma trận kề ($$O(n^2)$$), danh sách kề ($$O(n+m)$$), danh sách cạnh
- **Bậc của đỉnh**: số cạnh liên thuộc (vô hướng) hoặc bậc vào/ra (có hướng)

Trong bài tiếp theo, chúng ta sẽ tìm hiểu về đường đi, chu trình và tính liên thông — những khái niệm nền tảng để phân tích cấu trúc đồ thị.
