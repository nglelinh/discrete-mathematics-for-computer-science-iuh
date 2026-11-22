/**
 * Graph Explainer (vanilla JS + SVG) — bản dự phòng / fallback, Giai đoạn 2.
 * Bản chính (Svelte + D3, hình ảnh phong phú hơn) nằm ở:
 *   public/js/explainers/graph-explainer.js
 *   (nguồn: explainers/src/graph/)
 * Các bài 12-04, 16-03, 17-01 nhúng bản Svelte. Giữ file này nếu cần chạy
 * không qua bước `npm run build`.
 *
 * Mount:
 *   <div data-demo="graph-explainer" data-algorithm="bfs"></div>
 * Thuật toán: bfs, dfs, dijkstra, kruskal, prim
 */
(function () {
  'use strict';

  var ALGOS = {
    bfs: 'BFS',
    dfs: 'DFS',
    dijkstra: 'Dijkstra',
    kruskal: 'Kruskal (MST)',
    prim: 'Prim (MST)'
  };

  var PSEUDO = {
    bfs: [
      'BFS(G, s):',
      '  visited[s] ← đúng; d[s] ← 0',
      '  Q ← [s]',
      '  while Q không rỗng:',
      '    u ← lấy đầu Q',
      '    for mỗi v kề u:',
      '      if v chưa thăm:',
      '        visited[v] ← đúng; d[v] ← d[u]+1',
      '        đưa v vào Q'
    ],
    dfs: [
      'DFS(G, s):',
      '  thăm s (đánh dấu visited[s])',
      '  for mỗi v kề s:',
      '    if v chưa thăm:',
      '      DFS(G, v)',
      '  (quay lui khỏi s)'
    ],
    dijkstra: [
      'Dijkstra(G, s):',
      '  d[s] ← 0; d[khác] ← ∞',
      '  S ← ∅',
      '  while còn đỉnh ngoài S:',
      '    u ← đỉnh ngoài S có d nhỏ nhất',
      '    if d[u] = ∞: dừng',
      '    đưa u vào S',
      '    for mỗi cạnh (u, v, w):',
      '      if d[u] + w < d[v]:',
      '        d[v] ← d[u] + w; parent[v] ← u'
    ],
    kruskal: [
      'Kruskal(G):',
      '  sắp xếp cạnh theo w tăng dần',
      '  mỗi đỉnh là một thành phần',
      '  for mỗi cạnh (u, v) theo thứ tự:',
      '    if u, v khác thành phần:',
      '      thêm cạnh vào MST; hợp thành phần',
      '    else: bỏ cạnh (sẽ tạo chu trình)'
    ],
    prim: [
      'Prim(G, s):',
      '  S ← {s}',
      '  while S ≠ V:',
      '    chọn cạnh (u, v) nhẹ nhất, u ∈ S, v ∉ S',
      '    if không có cạnh như vậy: dừng',
      '    thêm v vào S; thêm cạnh vào MST'
    ]
  };

  function defaultGraph() {
    return {
      nodes: [
        { id: 'A', x: 70, y: 70 },
        { id: 'B', x: 230, y: 50 },
        { id: 'C', x: 400, y: 70 },
        { id: 'D', x: 70, y: 210 },
        { id: 'E', x: 230, y: 230 },
        { id: 'F', x: 400, y: 210 }
      ],
      edges: [
        { id: 'e0', u: 'A', v: 'B', w: 2 },
        { id: 'e1', u: 'B', v: 'C', w: 3 },
        { id: 'e2', u: 'A', v: 'D', w: 4 },
        { id: 'e3', u: 'B', v: 'E', w: 1 },
        { id: 'e4', u: 'C', v: 'F', w: 5 },
        { id: 'e5', u: 'D', v: 'E', w: 2 },
        { id: 'e6', u: 'E', v: 'F', w: 1 },
        { id: 'e7', u: 'D', v: 'B', w: 6 }
      ]
    };
  }

  function graphPath() {
    return {
      nodes: [
        { id: 'A', x: 60, y: 140 },
        { id: 'B', x: 180, y: 80 },
        { id: 'C', x: 300, y: 140 },
        { id: 'D', x: 420, y: 80 }
      ],
      edges: [
        { id: 'e0', u: 'A', v: 'B', w: 1 },
        { id: 'e1', u: 'B', v: 'C', w: 1 },
        { id: 'e2', u: 'C', v: 'D', w: 1 }
      ]
    };
  }

  function graphCycle() {
    return {
      nodes: [
        { id: 'A', x: 230, y: 40 },
        { id: 'B', x: 400, y: 140 },
        { id: 'C', x: 230, y: 240 },
        { id: 'D', x: 60, y: 140 }
      ],
      edges: [
        { id: 'e0', u: 'A', v: 'B', w: 3 },
        { id: 'e1', u: 'B', v: 'C', w: 4 },
        { id: 'e2', u: 'C', v: 'D', w: 2 },
        { id: 'e3', u: 'D', v: 'A', w: 5 },
        { id: 'e4', u: 'A', v: 'C', w: 8 }
      ]
    };
  }

  function cloneGraph(g) {
    return {
      nodes: g.nodes.map(function (n) { return { id: n.id, x: n.x, y: n.y }; }),
      edges: g.edges.map(function (e) { return { id: e.id, u: e.u, v: e.v, w: e.w }; })
    };
  }

  function neighbors(g, u) {
    var out = [];
    g.edges.forEach(function (e) {
      if (e.u === u) out.push({ v: e.v, w: e.w, eid: e.id });
      else if (e.v === u) out.push({ v: e.u, w: e.w, eid: e.id });
    });
    out.sort(function (a, b) { return a.v < b.v ? -1 : a.v > b.v ? 1 : 0; });
    return out;
  }

  function findEdge(g, id) {
    for (var i = 0; i < g.edges.length; i++) if (g.edges[i].id === id) return g.edges[i];
    return null;
  }

  function hasEdge(g, u, v) {
    return g.edges.some(function (e) {
      return (e.u === u && e.v === v) || (e.u === v && e.v === u);
    });
  }

  function emptyPaint(g) {
    var nodes = {}, edges = {};
    g.nodes.forEach(function (n) { nodes[n.id] = 'idle'; });
    g.edges.forEach(function (e) { edges[e.id] = 'idle'; });
    return { nodes: nodes, edges: edges };
  }

  function stepOf(g, line, msg, extra) {
    var paint = emptyPaint(g);
    var s = {
      line: line,
      msg: msg,
      nodes: paint.nodes,
      edges: paint.edges,
      queue: [],
      dist: {},
      setS: [],
      mstWeight: null
    };
    if (extra) Object.keys(extra).forEach(function (k) { s[k] = extra[k]; });
    return s;
  }

  function markVisited(s, visited, current) {
    Object.keys(visited).forEach(function (id) {
      if (visited[id]) s.nodes[id] = 'visited';
    });
    if (current) s.nodes[current] = 'current';
  }

  function buildBfsSteps(g, src) {
    var visited = {};
    var dist = {};
    var steps = [];
    g.nodes.forEach(function (n) { visited[n.id] = false; dist[n.id] = Infinity; });
    if (!g.nodes.some(function (n) { return n.id === src; })) {
      return [stepOf(g, 0, 'Chọn một đỉnh nguồn rồi chạy lại.')];
    }
    visited[src] = true;
    dist[src] = 0;
    var Q = [src];
    var s0 = stepOf(g, 1, 'Khởi tạo: thăm ' + src + ', d[' + src + '] = 0, Q = [' + src + '].', {
      queue: Q.slice(), dist: Object.assign({}, dist)
    });
    markVisited(s0, visited, src);
    steps.push(s0);

    var s1 = stepOf(g, 2, 'Hàng đợi Q ← [' + src + '].', { queue: Q.slice(), dist: Object.assign({}, dist) });
    markVisited(s1, visited, src);
    steps.push(s1);

    while (Q.length) {
      var u = Q.shift();
      var su = stepOf(g, 4, 'Lấy ' + u + ' ra khỏi hàng đợi. Q = [' + Q.join(', ') + '].', {
        queue: Q.slice(), dist: Object.assign({}, dist)
      });
      markVisited(su, visited, u);
      steps.push(su);

      neighbors(g, u).forEach(function (nb) {
        var v = nb.v, eid = nb.eid;
        var sex = stepOf(g, 5, 'Xét cạnh ' + u + ' — ' + v + '.', {
          queue: Q.slice(), dist: Object.assign({}, dist)
        });
        markVisited(sex, visited, u);
        sex.edges[eid] = 'active';
        sex.nodes[v] = visited[v] ? 'visited' : 'frontier';
        steps.push(sex);

        if (!visited[v]) {
          visited[v] = true;
          dist[v] = dist[u] + 1;
          Q.push(v);
          var sok = stepOf(g, 7, 'Chưa thăm: đánh dấu ' + v + ', d[' + v + '] = ' + dist[v] + ', đưa vào Q.', {
            queue: Q.slice(), dist: Object.assign({}, dist)
          });
          markVisited(sok, visited, v);
          sok.edges[eid] = 'tree';
          // keep previous tree edges: those that led to visited nodes at dist
          steps.forEach(function (prev) {
            Object.keys(prev.edges).forEach(function (id) {
              if (prev.edges[id] === 'tree') sok.edges[id] = 'tree';
            });
          });
          sok.edges[eid] = 'tree';
          steps.push(sok);
        } else {
          var sskip = stepOf(g, 6, v + ' đã thăm — bỏ qua.', {
            queue: Q.slice(), dist: Object.assign({}, dist)
          });
          markVisited(sskip, visited, u);
          // restore tree edges
          steps.forEach(function (prev) {
            Object.keys(prev.edges).forEach(function (id) {
              if (prev.edges[id] === 'tree') sskip.edges[id] = 'tree';
            });
          });
          sskip.edges[eid] = 'rejected';
          steps.push(sskip);
        }
      });
    }
    var send = stepOf(g, 3, 'Q rỗng. BFS kết thúc. Thứ tự thăm và khoảng cách (số cạnh) hiện ở bảng trạng thái.', {
      queue: [], dist: Object.assign({}, dist)
    });
    markVisited(send, visited, null);
    steps.forEach(function (prev) {
      Object.keys(prev.edges).forEach(function (id) {
        if (prev.edges[id] === 'tree') send.edges[id] = 'tree';
      });
    });
    steps.push(send);
    return steps;
  }

  function buildDfsSteps(g, src) {
    var visited = {};
    var steps = [];
    g.nodes.forEach(function (n) { visited[n.id] = false; });
    if (!g.nodes.some(function (n) { return n.id === src; })) {
      return [stepOf(g, 0, 'Chọn một đỉnh nguồn rồi chạy lại.')];
    }
    var tree = {};

    function rec(u) {
      visited[u] = true;
      var sEnter = stepOf(g, 1, 'Thăm ' + u + '.', {});
      markVisited(sEnter, visited, u);
      Object.keys(tree).forEach(function (id) { sEnter.edges[id] = 'tree'; });
      steps.push(sEnter);

      neighbors(g, u).forEach(function (nb) {
        var v = nb.v, eid = nb.eid;
        var sex = stepOf(g, 2, 'Từ ' + u + ' xét cạnh tới ' + v + '.', {});
        markVisited(sex, visited, u);
        Object.keys(tree).forEach(function (id) { sex.edges[id] = 'tree'; });
        sex.edges[eid] = 'active';
        sex.nodes[v] = visited[v] ? 'visited' : 'frontier';
        steps.push(sex);

        if (!visited[v]) {
          tree[eid] = true;
          rec(v);
          var sb = stepOf(g, 5, 'Quay lui về ' + u + ' (đã xong nhánh ' + v + ').', {});
          markVisited(sb, visited, u);
          Object.keys(tree).forEach(function (id) { sb.edges[id] = 'tree'; });
          steps.push(sb);
        } else {
          var sskip = stepOf(g, 3, v + ' đã thăm — không gọi DFS lại.', {});
          markVisited(sskip, visited, u);
          Object.keys(tree).forEach(function (id) { sskip.edges[id] = 'tree'; });
          sskip.edges[eid] = 'rejected';
          steps.push(sskip);
        }
      });
    }

    var s0 = stepOf(g, 0, 'Bắt đầu DFS tại ' + src + '.', {});
    s0.nodes[src] = 'frontier';
    steps.push(s0);
    rec(src);
    var send = stepOf(g, 5, 'DFS kết thúc (đã quay lui khỏi nguồn).', {});
    markVisited(send, visited, null);
    Object.keys(tree).forEach(function (id) { send.edges[id] = 'tree'; });
    steps.push(send);
    return steps;
  }

  function buildDijkstraSteps(g, src) {
    var dist = {}, parent = {}, inS = {};
    var steps = [];
    g.nodes.forEach(function (n) {
      dist[n.id] = Infinity;
      parent[n.id] = null;
      inS[n.id] = false;
    });
    if (!g.nodes.some(function (n) { return n.id === src; })) {
      return [stepOf(g, 0, 'Chọn một đỉnh nguồn rồi chạy lại.')];
    }
    dist[src] = 0;
    function setS() {
      return g.nodes.filter(function (n) { return inS[n.id]; }).map(function (n) { return n.id; });
    }
    function treeEdges() {
      var ids = {};
      g.edges.forEach(function (e) {
        var pu = parent[e.v] === e.u, pv = parent[e.u] === e.v;
        if (pu || pv) ids[e.id] = true;
      });
      return ids;
    }
    function paintStep(line, msg, current, activeEid) {
      var s = stepOf(g, line, msg, { dist: Object.assign({}, dist), setS: setS() });
      Object.keys(inS).forEach(function (id) { if (inS[id]) s.nodes[id] = 'visited'; });
      if (current) s.nodes[current] = 'current';
      var te = treeEdges();
      Object.keys(te).forEach(function (id) { s.edges[id] = 'tree'; });
      if (activeEid) s.edges[activeEid] = 'active';
      return s;
    }

    steps.push(paintStep(1, 'Khởi tạo: d[' + src + '] = 0, các đỉnh khác d = ∞, S = ∅.', src));
    var leftover = g.nodes.length;
    while (leftover-- >= 0) {
      var u = null, best = Infinity;
      g.nodes.forEach(function (n) {
        if (!inS[n.id] && dist[n.id] < best) { best = dist[n.id]; u = n.id; }
      });
      if (u === null) {
        steps.push(paintStep(3, 'Không còn đỉnh ngoài S. Dijkstra kết thúc.', null));
        break;
      }
      steps.push(paintStep(4, 'Chọn u = ' + u + ' (d nhỏ nhất ngoài S' + (best === Infinity ? '' : ': ' + best) + ').', u));
      if (dist[u] === Infinity) {
        steps.push(paintStep(5, 'd[' + u + '] = ∞ — các đỉnh còn lại không tới được từ ' + src + '. Dừng.', u));
        break;
      }
      inS[u] = true;
      steps.push(paintStep(6, 'Đưa ' + u + ' vào S. S = {' + setS().join(', ') + '}.', u));
      neighbors(g, u).forEach(function (nb) {
        var v = nb.v, w = nb.w, eid = nb.eid;
        var cand = dist[u] + w;
        var sex = paintStep(7, 'Relax cạnh ' + u + ' — ' + v + ' (w = ' + w + '): ứng viên ' + cand + ' so với d[' + v + '] = ' + (dist[v] === Infinity ? '∞' : dist[v]) + '.', u, eid);
        steps.push(sex);
        if (cand < dist[v]) {
          dist[v] = cand;
          parent[v] = u;
          var sok = paintStep(9, 'Cập nhật d[' + v + '] ← ' + cand + ', parent[' + v + '] ← ' + u + '.', v, eid);
          sok.nodes[v] = 'frontier';
          steps.push(sok);
        }
      });
    }
    var send = paintStep(3, 'Xong. Các cạnh xanh là cây đường đi ngắn nhất từ ' + src + ' (theo parent).', null);
    steps.push(send);
    return steps;
  }

  function buildKruskalSteps(g) {
    var parent = {}, steps = [];
    g.nodes.forEach(function (n) { parent[n.id] = n.id; });
    function find(x) { return parent[x] === x ? x : (parent[x] = find(parent[x])); }
    function unite(a, b) { a = find(a); b = find(b); if (a !== b) parent[a] = b; }

    var edges = g.edges.slice().sort(function (a, b) {
      if (a.w !== b.w) return a.w - b.w;
      return a.id < b.id ? -1 : 1;
    });
    var tree = {}, rejected = {}, weight = 0, chosen = 0;
    var need = Math.max(0, g.nodes.length - 1);

    function paint(line, msg, activeEid) {
      var s = stepOf(g, line, msg, { mstWeight: weight });
      Object.keys(tree).forEach(function (id) { s.edges[id] = 'tree'; });
      Object.keys(rejected).forEach(function (id) { s.edges[id] = 'rejected'; });
      if (activeEid) s.edges[activeEid] = 'active';
      g.nodes.forEach(function (n) {
        s.nodes[n.id] = 'idle';
      });
      if (activeEid) {
        var e = findEdge(g, activeEid);
        if (e) { s.nodes[e.u] = 'current'; s.nodes[e.v] = 'current'; }
      }
      return s;
    }

    steps.push(paint(1, 'Sắp xếp cạnh theo trọng số tăng dần: ' + edges.map(function (e) {
      return e.u + e.v + '(' + e.w + ')';
    }).join(', ') + '.'));
    steps.push(paint(2, 'Mỗi đỉnh là một thành phần riêng (Union–Find).'));

    edges.forEach(function (e) {
      steps.push(paint(3, 'Xét cạnh ' + e.u + ' — ' + e.v + ' (w = ' + e.w + ').', e.id));
      if (find(e.u) !== find(e.v)) {
        unite(e.u, e.v);
        tree[e.id] = true;
        weight += e.w;
        chosen += 1;
        steps.push(paint(5, 'Khác thành phần → thêm vào MST. Tổng hiện tại = ' + weight + '.', e.id));
      } else {
        rejected[e.id] = true;
        steps.push(paint(6, 'Cùng thành phần → bỏ (tránh chu trình).', e.id));
      }
    });
    var msg = chosen === need
      ? 'Kruskal kết thúc. MST có ' + chosen + ' cạnh, tổng trọng số = ' + weight + '.'
      : 'Hết cạnh. Đồ thị có thể không liên thông (rừng khung), tổng = ' + weight + ', ' + chosen + ' cạnh.';
    steps.push(paint(3, msg));
    return steps;
  }

  function buildPrimSteps(g, src) {
    var inS = {}, steps = [];
    g.nodes.forEach(function (n) { inS[n.id] = false; });
    if (!g.nodes.some(function (n) { return n.id === src; })) {
      return [stepOf(g, 0, 'Chọn một đỉnh nguồn rồi chạy lại.')];
    }
    inS[src] = true;
    var tree = {}, weight = 0;

    function setS() {
      return g.nodes.filter(function (n) { return inS[n.id]; }).map(function (n) { return n.id; });
    }
    function paint(line, msg, current, activeEid) {
      var s = stepOf(g, line, msg, { setS: setS(), mstWeight: weight });
      Object.keys(inS).forEach(function (id) { if (inS[id]) s.nodes[id] = 'visited'; });
      if (current) s.nodes[current] = 'current';
      Object.keys(tree).forEach(function (id) { s.edges[id] = 'tree'; });
      if (activeEid) s.edges[activeEid] = 'active';
      return s;
    }

    steps.push(paint(1, 'Bắt đầu Prim tại ' + src + '. S = {' + src + '}.', src));
    var guard = g.nodes.length + 2;
    while (guard--) {
      if (setS().length === g.nodes.length) {
        steps.push(paint(2, 'S đã chứa mọi đỉnh. Prim kết thúc. Tổng MST = ' + weight + '.'));
        break;
      }
      var best = null;
      g.edges.forEach(function (e) {
        var uIn = inS[e.u], vIn = inS[e.v];
        if (uIn === vIn) return;
        if (!best || e.w < best.w || (e.w === best.w && e.id < best.id)) best = e;
      });
      if (!best) {
        steps.push(paint(4, 'Không còn cạnh ra khỏi S — phần còn lại không tới được. Tổng = ' + weight + '.'));
        break;
      }
      var from = inS[best.u] ? best.u : best.v;
      var to = inS[best.u] ? best.v : best.u;
      steps.push(paint(3, 'Cạnh nhẹ nhất ra khỏi S: ' + from + ' — ' + to + ' (w = ' + best.w + ').', from, best.id));
      inS[to] = true;
      tree[best.id] = true;
      weight += best.w;
      steps.push(paint(5, 'Thêm ' + to + ' vào S, thêm cạnh vào MST. Tổng = ' + weight + '. S = {' + setS().join(', ') + '}.', to, best.id));
    }
    return steps;
  }

  function buildSteps(g, algo, src) {
    if (algo === 'bfs') return buildBfsSteps(g, src);
    if (algo === 'dfs') return buildDfsSteps(g, src);
    if (algo === 'dijkstra') return buildDijkstraSteps(g, src);
    if (algo === 'kruskal') return buildKruskalSteps(g);
    if (algo === 'prim') return buildPrimSteps(g, src);
    return [stepOf(g, 0, 'Thuật toán không hỗ trợ.')];
  }

  function addStyle() {
    if (document.getElementById('gex-style')) return;
    var s = document.createElement('style');
    s.id = 'gex-style';
    s.textContent = [
      '.gex{border:1px solid #e2e8f0;border-radius:12px;padding:16px 18px;background:#fff;margin:14px 0;font-family:system-ui,-apple-system,sans-serif;color:#0f172a}',
      '.gex h4{margin:0 0 6px;font-size:1.08rem;color:#004586}',
      '.gex p.gex-help{margin:0 0 10px;color:#64748b;font-size:.92rem;line-height:1.45}',
      '.gex-toolbar,.gex-controls{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:0 0 10px}',
      '.gex-toolbar label,.gex-controls label{font-size:.9rem;display:flex;gap:6px;align-items:center}',
      '.gex select,.gex input[type=number]{padding:6px 8px;border:1px solid #cbd5e1;border-radius:8px;background:#fff}',
      '.gex button{padding:7px 12px;border:1px solid #007bff;background:#007bff;color:#fff;border-radius:8px;cursor:pointer;font-size:.9rem}',
      '.gex button.gex-sec{background:#fff;color:#0f437a;border-color:#94a3b8}',
      '.gex button.gex-on{background:#0f766e;border-color:#0f766e;color:#fff}',
      '.gex button:disabled{opacity:.5;cursor:not-allowed}',
      '.gex-body{display:grid;grid-template-columns:1.35fr .9fr;gap:12px;align-items:stretch}',
      '@media (max-width:800px){.gex-body{grid-template-columns:1fr}}',
      '.gex-board{position:relative;height:300px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;overflow:hidden}',
      '.gex-board svg{width:100%;height:100%;display:block}',
      '.gex-edge{stroke:#94a3b8;stroke-width:2.5;fill:none}',
      '.gex-edge.hit{stroke:transparent;stroke-width:14;cursor:pointer}',
      '.gex-edge.active{stroke:#d97706;stroke-width:3.5}',
      '.gex-edge.tree{stroke:#16a34a;stroke-width:3.5}',
      '.gex-edge.rejected{stroke:#dc2626;stroke-width:2.5;stroke-dasharray:5 4}',
      '.gex-w{font-size:12px;fill:#334155;font-weight:700}',
      '.gex-node{stroke:#007bff;stroke-width:2;fill:#e8f4fd;cursor:pointer}',
      '.gex-node.current{fill:#fde68a;stroke:#d97706}',
      '.gex-node.visited{fill:#bbf7d0;stroke:#16a34a}',
      '.gex-node.frontier{fill:#dbeafe;stroke:#2563eb}',
      '.gex-node.idle{fill:#e8f4fd;stroke:#007bff}',
      '.gex-label{font-size:13px;font-weight:700;fill:#0f172a;text-anchor:middle;dominant-baseline:middle;pointer-events:none}',
      '.gex-pseudo{background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;padding:10px 12px;overflow:auto;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px;line-height:1.45}',
      '.gex-pseudo .ln{padding:1px 6px;border-radius:4px;white-space:pre}',
      '.gex-pseudo .ln.on{background:#fde68a;font-weight:700}',
      '.gex-msg{margin:10px 0 0;padding:10px 12px;border-radius:8px;background:#f8fafc;border-left:4px solid #007bff;font-size:.95rem;line-height:1.45;min-height:2.6em}',
      '.gex-state{margin-top:8px;font-size:.9rem;color:#334155}',
      '.gex-state code{background:#e2e8f0;padding:1px 5px;border-radius:4px}'
    ].join('');
    document.head.appendChild(s);
  }

  function fmtDist(d) {
    if (d === undefined || d === null) return '—';
    if (d === Infinity) return '∞';
    return String(d);
  }

  function nextId(g) {
    var letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    for (var i = 0; i < letters.length; i++) {
      var ch = letters[i];
      if (!g.nodes.some(function (n) { return n.id === ch; })) return ch;
    }
    return 'N' + g.nodes.length;
  }

  function nextEdgeId(g) {
    var n = 0;
    while (g.edges.some(function (e) { return e.id === 'e' + n; })) n++;
    return 'e' + n;
  }

  function mount(host) {
    if (!host || host.dataset.gexMounted) return;
    host.dataset.gexMounted = '1';
    addStyle();

    var initialAlgo = (host.getAttribute('data-algorithm') || 'bfs').toLowerCase();
    if (!ALGOS[initialAlgo]) initialAlgo = 'bfs';

    var graph = cloneGraph(defaultGraph());
    var algo = initialAlgo;
    var src = graph.nodes[0].id;
    var steps = [];
    var idx = 0;
    var mode = 'select';
    var edgeStart = null;
    var timer = null;
    var dragging = null;
    var wNew = 1;

    host.innerHTML =
      '<div class="gex">' +
        '<h4>Minh hoạ thuật toán đồ thị</h4>' +
        '<p class="gex-help">Chọn thuật toán, bấm <strong>Bước sau</strong> hoặc <strong>Chạy</strong> để xem từng dòng giả mã. Có thể kéo đỉnh, thêm/xóa đỉnh và cạnh (đồ thị vô hướng). Các cạnh xanh lục thuộc cây duyệt / MST; đỏ nét đứt là cạnh bị bỏ.</p>' +
        '<div class="gex-toolbar">' +
          '<label>Thuật toán <select data-gex="algo"></select></label>' +
          '<label data-gex="src-wrap">Đỉnh nguồn <select data-gex="src"></select></label>' +
          '<label>Đồ thị mẫu <select data-gex="preset">' +
            '<option value="default">Lưới có trọng số</option>' +
            '<option value="path">Đường đi</option>' +
            '<option value="cycle">Chu trình + dây</option>' +
          '</select></label>' +
          '<label>Trọng số cạnh mới <input data-gex="w" type="number" min="0" step="1" value="1" style="width:4.2em"></label>' +
        '</div>' +
        '<div class="gex-toolbar">' +
          '<button type="button" class="gex-sec" data-mode="select">Chọn / kéo</button>' +
          '<button type="button" class="gex-sec" data-mode="add-node">Thêm đỉnh</button>' +
          '<button type="button" class="gex-sec" data-mode="add-edge">Thêm cạnh</button>' +
          '<button type="button" class="gex-sec" data-mode="delete">Xóa</button>' +
        '</div>' +
        '<div class="gex-controls">' +
          '<button type="button" data-act="prev">Bước trước</button>' +
          '<button type="button" data-act="play">Chạy</button>' +
          '<button type="button" class="gex-sec" data-act="pause">Tạm dừng</button>' +
          '<button type="button" data-act="next">Bước sau</button>' +
          '<button type="button" class="gex-sec" data-act="reset">Đặt lại</button>' +
          '<label>Tốc độ <input data-gex="speed" type="range" min="200" max="1600" step="100" value="800"></label>' +
        '</div>' +
        '<div class="gex-body">' +
          '<div class="gex-board"><svg viewBox="0 0 480 300" data-gex="svg"></svg></div>' +
          '<div class="gex-pseudo" data-gex="pseudo"></div>' +
        '</div>' +
        '<div class="gex-msg" data-gex="msg"></div>' +
        '<div class="gex-state" data-gex="state"></div>' +
      '</div>';

    var $ = function (sel) { return host.querySelector(sel); };
    var algoSel = $('[data-gex="algo"]');
    var srcSel = $('[data-gex="src"]');
    var srcWrap = $('[data-gex="src-wrap"]');
    var svg = $('[data-gex="svg"]');
    var pseudo = $('[data-gex="pseudo"]');
    var msgEl = $('[data-gex="msg"]');
    var stateEl = $('[data-gex="state"]');

    Object.keys(ALGOS).forEach(function (k) {
      var o = document.createElement('option');
      o.value = k; o.textContent = ALGOS[k];
      if (k === algo) o.selected = true;
      algoSel.appendChild(o);
    });

    function stopPlay() {
      if (timer) { clearInterval(timer); timer = null; }
    }

    function rebuild() {
      stopPlay();
      if (!graph.nodes.some(function (n) { return n.id === src; })) {
        src = graph.nodes[0] ? graph.nodes[0].id : null;
      }
      steps = src || algo === 'kruskal' ? buildSteps(graph, algo, src) : [stepOf(graph, 0, 'Đồ thị trống — hãy thêm đỉnh.')];
      idx = 0;
      fillSrc();
      srcWrap.style.display = algo === 'kruskal' ? 'none' : '';
      paint();
    }

    function fillSrc() {
      var cur = src;
      srcSel.innerHTML = '';
      graph.nodes.forEach(function (n) {
        var o = document.createElement('option');
        o.value = n.id; o.textContent = n.id;
        if (n.id === cur) o.selected = true;
        srcSel.appendChild(o);
      });
      src = srcSel.value || cur;
    }

    function current() { return steps[idx] || stepOf(graph, 0, ''); }

    function paintModes() {
      host.querySelectorAll('[data-mode]').forEach(function (b) {
        b.classList.toggle('gex-on', b.getAttribute('data-mode') === mode);
      });
    }

    function nodeById(id) {
      for (var i = 0; i < graph.nodes.length; i++) if (graph.nodes[i].id === id) return graph.nodes[i];
      return null;
    }

    function paint() {
      var st = current();
      var lines = PSEUDO[algo] || [];
      pseudo.innerHTML = lines.map(function (ln, i) {
        return '<div class="ln' + (i === st.line ? ' on' : '') + '">' + escapeHtml(ln) + '</div>';
      }).join('');
      msgEl.textContent = st.msg || '';

      var bits = [];
      if (st.queue && (algo === 'bfs' || algo === 'dfs')) {
        bits.push((algo === 'bfs' ? 'Hàng đợi Q' : 'Ngăn xếp / nhánh hiện tại') + ': <code>[' + (st.queue || []).join(', ') + ']</code>');
      }
      if (st.dist && Object.keys(st.dist).length) {
        bits.push('d: ' + graph.nodes.map(function (n) {
          return '<code>' + n.id + '=' + fmtDist(st.dist[n.id]) + '</code>';
        }).join(' '));
      }
      if (st.setS && st.setS.length) bits.push('S = <code>{' + st.setS.join(', ') + '}</code>');
      if (st.mstWeight !== null && st.mstWeight !== undefined) bits.push('Tổng MST = <code>' + st.mstWeight + '</code>');
      bits.push('Bước ' + (idx + 1) + ' / ' + steps.length);
      stateEl.innerHTML = bits.join(' · ');

      var parts = [];
      graph.edges.forEach(function (e) {
        var a = nodeById(e.u), b = nodeById(e.v);
        if (!a || !b) return;
        var cls = 'gex-edge ' + (st.edges[e.id] || 'idle');
        var mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2;
        parts.push('<line class="gex-edge hit" data-eid="' + e.id + '" x1="' + a.x + '" y1="' + a.y + '" x2="' + b.x + '" y2="' + b.y + '"></line>');
        parts.push('<line class="' + cls + '" data-eid="' + e.id + '" x1="' + a.x + '" y1="' + a.y + '" x2="' + b.x + '" y2="' + b.y + '"></line>');
        parts.push('<text class="gex-w" x="' + mx + '" y="' + (my - 8) + '">' + e.w + '</text>');
      });
      graph.nodes.forEach(function (n) {
        var cls = 'gex-node ' + (st.nodes[n.id] || 'idle');
        parts.push('<circle class="' + cls + '" data-nid="' + n.id + '" cx="' + n.x + '" cy="' + n.y + '" r="16"></circle>');
        parts.push('<text class="gex-label" x="' + n.x + '" y="' + n.y + '">' + n.id + '</text>');
      });
      svg.innerHTML = parts.join('');
      paintModes();
    }

    function escapeHtml(s) {
      return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }

    function svgPoint(ev) {
      var rect = svg.getBoundingClientRect();
      var vb = svg.viewBox.baseVal;
      return {
        x: (ev.clientX - rect.left) / rect.width * vb.width,
        y: (ev.clientY - rect.top) / rect.height * vb.height
      };
    }

    svg.addEventListener('mousedown', function (ev) {
      var t = ev.target;
      var nid = t.getAttribute && t.getAttribute('data-nid');
      var eid = t.getAttribute && t.getAttribute('data-eid');
      var pt = svgPoint(ev);

      if (mode === 'add-node' && !nid) {
        if (graph.nodes.length >= 14) return;
        graph.nodes.push({ id: nextId(graph), x: Math.round(pt.x), y: Math.round(pt.y) });
        rebuild();
        return;
      }
      if (mode === 'delete') {
        if (nid) {
          graph.nodes = graph.nodes.filter(function (n) { return n.id !== nid; });
          graph.edges = graph.edges.filter(function (e) { return e.u !== nid && e.v !== nid; });
          rebuild();
        } else if (eid) {
          graph.edges = graph.edges.filter(function (e) { return e.id !== eid; });
          rebuild();
        }
        return;
      }
      if (mode === 'add-edge' && nid) {
        if (!edgeStart) {
          edgeStart = nid;
          return;
        }
        if (edgeStart !== nid && !hasEdge(graph, edgeStart, nid)) {
          var w = Number($('[data-gex="w"]').value);
          if (!isFinite(w) || w < 0) w = 1;
          graph.edges.push({ id: nextEdgeId(graph), u: edgeStart, v: nid, w: w });
        }
        edgeStart = null;
        rebuild();
        return;
      }
      if (mode === 'select' && nid) {
        dragging = { id: nid, dx: 0 };
        ev.preventDefault();
      }
    });

    window.addEventListener('mousemove', function (ev) {
      if (!dragging) return;
      var pt = svgPoint(ev);
      var n = nodeById(dragging.id);
      if (!n) return;
      n.x = Math.max(20, Math.min(460, Math.round(pt.x)));
      n.y = Math.max(20, Math.min(280, Math.round(pt.y)));
      paint();
    });
    window.addEventListener('mouseup', function () {
      if (dragging) { dragging = null; }
    });

    algoSel.addEventListener('change', function () { algo = algoSel.value; rebuild(); });
    srcSel.addEventListener('change', function () { src = srcSel.value; rebuild(); });
    $('[data-gex="preset"]').addEventListener('change', function () {
      var v = this.value;
      graph = cloneGraph(v === 'path' ? graphPath() : v === 'cycle' ? graphCycle() : defaultGraph());
      src = graph.nodes[0].id;
      rebuild();
    });
    $('[data-gex="w"]').addEventListener('change', function () {
      wNew = Number(this.value) || 1;
    });

    host.querySelectorAll('[data-mode]').forEach(function (b) {
      b.addEventListener('click', function () {
        mode = b.getAttribute('data-mode');
        edgeStart = null;
        paintModes();
      });
    });

    $('[data-act="next"]').addEventListener('click', function () {
      if (idx < steps.length - 1) { idx += 1; paint(); }
    });
    $('[data-act="prev"]').addEventListener('click', function () {
      if (idx > 0) { idx -= 1; paint(); }
    });
    $('[data-act="reset"]').addEventListener('click', function () { rebuild(); });
    $('[data-act="pause"]').addEventListener('click', stopPlay);
    $('[data-act="play"]').addEventListener('click', function () {
      stopPlay();
      timer = setInterval(function () {
        if (idx >= steps.length - 1) { stopPlay(); return; }
        idx += 1;
        paint();
      }, Number($('[data-gex="speed"]').value) || 800);
    });

    rebuild();
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-demo="graph-explainer"]').forEach(mount);
  });

  // Expose builders for a quick sanity check in the console / Node.
  window.GraphExplainer = {
    buildSteps: buildSteps,
    defaultGraph: defaultGraph
  };
})();
