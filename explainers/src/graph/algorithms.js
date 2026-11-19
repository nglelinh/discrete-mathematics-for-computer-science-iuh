/** Graph algorithm step generators for the Graph Explainer. */

export const ALGOS = {
  bfs: 'BFS',
  dfs: 'DFS',
  dijkstra: 'Dijkstra',
  kruskal: 'Kruskal (MST)',
  prim: 'Prim (MST)'
};

export const PSEUDO = {
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

export const PRESETS = {
  mau: {
    label: 'Đồ thị mẫu (6 đỉnh)',
    graph: () => ({
      nodes: [
        { id: 'A', x: 90, y: 80 },
        { id: 'B', x: 300, y: 55 },
        { id: 'C', x: 530, y: 80 },
        { id: 'D', x: 90, y: 280 },
        { id: 'E', x: 300, y: 310 },
        { id: 'F', x: 530, y: 280 }
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
    })
  },
  duong: {
    label: 'Đường đi A–D',
    graph: () => ({
      nodes: [
        { id: 'A', x: 80, y: 180 },
        { id: 'B', x: 250, y: 90 },
        { id: 'C', x: 420, y: 180 },
        { id: 'D', x: 590, y: 90 }
      ],
      edges: [
        { id: 'e0', u: 'A', v: 'B', w: 1 },
        { id: 'e1', u: 'B', v: 'C', w: 1 },
        { id: 'e2', u: 'C', v: 'D', w: 1 }
      ]
    })
  },
  chu_trinh: {
    label: 'Chu trình + dây',
    graph: () => ({
      nodes: [
        { id: 'A', x: 330, y: 50 },
        { id: 'B', x: 560, y: 180 },
        { id: 'C', x: 330, y: 320 },
        { id: 'D', x: 100, y: 180 }
      ],
      edges: [
        { id: 'e0', u: 'A', v: 'B', w: 3 },
        { id: 'e1', u: 'B', v: 'C', w: 4 },
        { id: 'e2', u: 'C', v: 'D', w: 2 },
        { id: 'e3', u: 'D', v: 'A', w: 5 },
        { id: 'e4', u: 'A', v: 'C', w: 8 }
      ]
    })
  }
};

export function cloneGraph(g) {
  return {
    nodes: g.nodes.map((n) => ({ id: n.id, x: n.x, y: n.y })),
    edges: g.edges.map((e) => ({ id: e.id, u: e.u, v: e.v, w: Number(e.w) }))
  };
}

export function neighbors(g, u) {
  const out = [];
  for (const e of g.edges) {
    if (e.u === u) out.push({ v: e.v, w: e.w, eid: e.id });
    else if (e.v === u) out.push({ v: e.u, w: e.w, eid: e.id });
  }
  out.sort((a, b) => (a.v < b.v ? -1 : a.v > b.v ? 1 : 0));
  return out;
}

export function findEdge(g, id) {
  return g.edges.find((e) => e.id === id) || null;
}

export function hasEdge(g, u, v) {
  return g.edges.some((e) => (e.u === u && e.v === v) || (e.u === v && e.v === u));
}

export function nextNodeId(g) {
  const used = new Set(g.nodes.map((n) => n.id));
  const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  for (const ch of alphabet) if (!used.has(ch)) return ch;
  let i = 1;
  while (used.has(`N${i}`)) i += 1;
  return `N${i}`;
}

export function nextEdgeId(g) {
  const used = new Set(g.edges.map((e) => e.id));
  let i = 0;
  while (used.has(`e${i}`)) i += 1;
  return `e${i}`;
}

function emptyPaint(g) {
  const nodes = {};
  const edges = {};
  for (const n of g.nodes) nodes[n.id] = 'idle';
  for (const e of g.edges) edges[e.id] = 'idle';
  return { nodes, edges };
}

function fmtDist(d) {
  return d === Infinity ? '∞' : d;
}

function stepOf(g, line, msg, extra = {}) {
  const paint = emptyPaint(g);
  return {
    line,
    msg,
    nodes: paint.nodes,
    edges: paint.edges,
    queue: [],
    stack: [],
    pq: [],
    dist: {},
    parent: {},
    setS: [],
    components: {},
    edgeList: [],
    mstWeight: null,
    ...extra
  };
}

function markVisited(s, visited, current) {
  for (const id of Object.keys(visited)) {
    if (visited[id]) s.nodes[id] = 'visited';
  }
  if (current) s.nodes[current] = 'current';
}

function applyTree(s, tree) {
  for (const id of Object.keys(tree)) {
    if (tree[id]) s.edges[id] = 'tree';
  }
}

function snapshotDist(dist) {
  const out = {};
  for (const id of Object.keys(dist)) out[id] = dist[id];
  return out;
}

function pqOf(g, dist, inS) {
  return g.nodes
    .filter((n) => !inS[n.id])
    .map((n) => ({ id: n.id, key: dist[n.id] }))
    .sort((a, b) => {
      if (a.key !== b.key) return a.key - b.key;
      return a.id < b.id ? -1 : 1;
    });
}

export function buildBfsSteps(g, src) {
  const visited = {};
  const dist = {};
  const parent = {};
  const tree = {};
  const steps = [];
  for (const n of g.nodes) {
    visited[n.id] = false;
    dist[n.id] = Infinity;
    parent[n.id] = null;
  }
  if (!g.nodes.some((n) => n.id === src)) {
    return [stepOf(g, 0, 'Chọn một đỉnh nguồn rồi chạy lại.')];
  }

  function snap(line, msg, current, extra = {}) {
    const s = stepOf(g, line, msg, {
      queue: Q.slice(),
      dist: snapshotDist(dist),
      parent: { ...parent },
      ...extra
    });
    markVisited(s, visited, current);
    applyTree(s, tree);
    return s;
  }

  visited[src] = true;
  dist[src] = 0;
  const Q = [src];
  steps.push(snap(1, `Khởi tạo: thăm ${src}, d[${src}] = 0, Q = [${src}].`, src));
  steps.push(snap(2, `Hàng đợi Q ← [${src}].`, src));

  while (Q.length) {
    const u = Q.shift();
    steps.push(snap(4, `Lấy ${u} ra khỏi hàng đợi. Q = [${Q.join(', ')}].`, u));
    for (const nb of neighbors(g, u)) {
      const { v, eid } = nb;
      const sex = snap(5, `Xét cạnh ${u} — ${v}.`, u);
      sex.edges[eid] = 'active';
      sex.nodes[v] = visited[v] ? 'visited' : 'frontier';
      steps.push(sex);
      if (!visited[v]) {
        visited[v] = true;
        dist[v] = dist[u] + 1;
        parent[v] = u;
        tree[eid] = true;
        Q.push(v);
        const sok = snap(7, `Chưa thăm: đánh dấu ${v}, d[${v}] = ${dist[v]}, đưa vào Q.`, v);
        sok.edges[eid] = 'tree';
        sok.nodes[v] = 'frontier';
        steps.push(sok);
      } else {
        const sskip = snap(6, `${v} đã thăm — bỏ qua.`, u);
        sskip.edges[eid] = 'rejected';
        steps.push(sskip);
      }
    }
  }
  steps.push(snap(3, 'Q rỗng. BFS kết thúc. Các cạnh xanh là cây BFS; bảng bên phải là khoảng cách (số cạnh).', null));
  return steps;
}

export function buildDfsSteps(g, src) {
  const visited = {};
  const tree = {};
  const steps = [];
  const stack = [];
  for (const n of g.nodes) visited[n.id] = false;
  if (!g.nodes.some((n) => n.id === src)) {
    return [stepOf(g, 0, 'Chọn một đỉnh nguồn rồi chạy lại.')];
  }

  function snap(line, msg, current, extra = {}) {
    const s = stepOf(g, line, msg, { stack: stack.slice(), ...extra });
    markVisited(s, visited, current);
    applyTree(s, tree);
    return s;
  }

  function rec(u) {
    stack.push(u);
    visited[u] = true;
    steps.push(snap(1, `Thăm ${u}. Ngăn xếp = [${stack.join(', ')}].`, u));
    for (const nb of neighbors(g, u)) {
      const { v, eid } = nb;
      const sex = snap(2, `Từ ${u} xét cạnh tới ${v}.`, u);
      sex.edges[eid] = 'active';
      sex.nodes[v] = visited[v] ? 'visited' : 'frontier';
      steps.push(sex);
      if (!visited[v]) {
        tree[eid] = true;
        rec(v);
        steps.push(snap(5, `Quay lui về ${u} (đã xong nhánh ${v}).`, u));
      } else {
        const sskip = snap(3, `${v} đã thăm — không gọi DFS lại.`, u);
        sskip.edges[eid] = 'rejected';
        steps.push(sskip);
      }
    }
    stack.pop();
  }

  const s0 = stepOf(g, 0, `Bắt đầu DFS tại ${src}.`);
  s0.nodes[src] = 'frontier';
  steps.push(s0);
  rec(src);
  const send = snap(5, 'DFS kết thúc (đã quay lui khỏi nguồn). Các cạnh xanh là cây DFS.', null);
  steps.push(send);
  return steps;
}

export function buildDijkstraSteps(g, src) {
  const dist = {};
  const parent = {};
  const inS = {};
  const steps = [];
  for (const n of g.nodes) {
    dist[n.id] = Infinity;
    parent[n.id] = null;
    inS[n.id] = false;
  }
  if (!g.nodes.some((n) => n.id === src)) {
    return [stepOf(g, 0, 'Chọn một đỉnh nguồn rồi chạy lại.')];
  }
  dist[src] = 0;

  function setS() {
    return g.nodes.filter((n) => inS[n.id]).map((n) => n.id);
  }

  function treeEdges() {
    const ids = {};
    for (const e of g.edges) {
      if (parent[e.v] === e.u || parent[e.u] === e.v) ids[e.id] = true;
    }
    return ids;
  }

  function paint(line, msg, current, activeEid) {
    const s = stepOf(g, line, msg, {
      dist: snapshotDist(dist),
      parent: { ...parent },
      setS: setS(),
      pq: pqOf(g, dist, inS)
    });
    for (const id of Object.keys(inS)) {
      if (inS[id]) s.nodes[id] = 'visited';
    }
    if (current) s.nodes[current] = 'current';
    applyTree(s, treeEdges());
    if (activeEid) s.edges[activeEid] = 'active';
    return s;
  }

  steps.push(paint(1, `Khởi tạo: d[${src}] = 0, các đỉnh khác d = ∞, S = ∅.`, src));
  let leftover = g.nodes.length;
  while (leftover-- >= 0) {
    let u = null;
    let best = Infinity;
    for (const n of g.nodes) {
      if (!inS[n.id] && dist[n.id] < best) {
        best = dist[n.id];
        u = n.id;
      }
    }
    if (u === null) {
      steps.push(paint(3, 'Không còn đỉnh ngoài S. Dijkstra kết thúc.', null));
      break;
    }
    steps.push(paint(4, `Chọn u = ${u} (d nhỏ nhất ngoài S: ${fmtDist(best)}).`, u));
    if (dist[u] === Infinity) {
      steps.push(paint(5, `d[${u}] = ∞ — các đỉnh còn lại không tới được từ ${src}. Dừng.`, u));
      break;
    }
    inS[u] = true;
    steps.push(paint(6, `Đưa ${u} vào S. S = {${setS().join(', ')}}.`, u));
    for (const nb of neighbors(g, u)) {
      const { v, w, eid } = nb;
      const cand = dist[u] + w;
      steps.push(
        paint(
          7,
          `Relax cạnh ${u} — ${v} (w = ${w}): ứng viên ${cand} so với d[${v}] = ${fmtDist(dist[v])}.`,
          u,
          eid
        )
      );
      if (cand < dist[v]) {
        dist[v] = cand;
        parent[v] = u;
        const sok = paint(9, `Cập nhật d[${v}] ← ${cand}, parent[${v}] ← ${u}.`, v, eid);
        sok.nodes[v] = 'frontier';
        steps.push(sok);
      }
    }
  }
  steps.push(paint(3, `Xong. Các cạnh xanh là cây đường đi ngắn nhất từ ${src} (theo parent).`, null));
  return steps;
}

export function buildKruskalSteps(g) {
  const parent = {};
  const steps = [];
  for (const n of g.nodes) parent[n.id] = n.id;

  function find(x) {
    return parent[x] === x ? x : (parent[x] = find(parent[x]));
  }
  function findPure(x, p) {
    return p[x] === x ? x : findPure(p[x], p);
  }
  function unite(a, b) {
    a = find(a);
    b = find(b);
    if (a !== b) parent[a] = b;
  }

  const edges = g.edges.slice().sort((a, b) => (a.w !== b.w ? a.w - b.w : a.id < b.id ? -1 : 1));
  const tree = {};
  const rejected = {};
  let weight = 0;
  let chosen = 0;
  const need = Math.max(0, g.nodes.length - 1);

  function components() {
    const p = { ...parent };
    const out = {};
    for (const n of g.nodes) out[n.id] = findPure(n.id, p);
    return out;
  }

  function edgeList() {
    return edges.map((e) => ({
      id: e.id,
      u: e.u,
      v: e.v,
      w: e.w,
      status: tree[e.id] ? 'tree' : rejected[e.id] ? 'rejected' : 'idle'
    }));
  }

  function paint(line, msg, activeEid) {
    const s = stepOf(g, line, msg, {
      mstWeight: weight,
      components: components(),
      edgeList: edgeList(),
      setS: []
    });
    applyTree(s, tree);
    for (const id of Object.keys(rejected)) s.edges[id] = 'rejected';
    if (activeEid) s.edges[activeEid] = 'active';
    if (activeEid) {
      const e = findEdge(g, activeEid);
      if (e) {
        s.nodes[e.u] = 'current';
        s.nodes[e.v] = 'current';
      }
    }
    return s;
  }

  steps.push(
    paint(
      1,
      'Sắp xếp cạnh theo trọng số tăng dần: ' +
        edges.map((e) => `${e.u}${e.v}(${e.w})`).join(', ') +
        '.'
    )
  );
  steps.push(paint(2, 'Mỗi đỉnh là một thành phần riêng (Union–Find).'));

  for (const e of edges) {
    steps.push(paint(3, `Xét cạnh ${e.u} — ${e.v} (w = ${e.w}).`, e.id));
    if (find(e.u) !== find(e.v)) {
      unite(e.u, e.v);
      tree[e.id] = true;
      weight += e.w;
      chosen += 1;
      steps.push(paint(5, `Khác thành phần → thêm vào MST. Tổng hiện tại = ${weight}.`, e.id));
    } else {
      rejected[e.id] = true;
      steps.push(paint(6, 'Cùng thành phần → bỏ (tránh chu trình).', e.id));
    }
  }
  const msg =
    chosen === need
      ? `Kruskal kết thúc. MST có ${chosen} cạnh, tổng trọng số = ${weight}.`
      : `Hết cạnh. Đồ thị có thể không liên thông (rừng khung), tổng = ${weight}, ${chosen} cạnh.`;
  steps.push(paint(3, msg));
  return steps;
}

export function buildPrimSteps(g, src) {
  const inS = {};
  const steps = [];
  for (const n of g.nodes) inS[n.id] = false;
  if (!g.nodes.some((n) => n.id === src)) {
    return [stepOf(g, 0, 'Chọn một đỉnh nguồn rồi chạy lại.')];
  }
  inS[src] = true;
  const tree = {};
  let weight = 0;

  function setS() {
    return g.nodes.filter((n) => inS[n.id]).map((n) => n.id);
  }

  function candidates() {
    const list = [];
    for (const e of g.edges) {
      if (inS[e.u] === inS[e.v]) continue;
      const from = inS[e.u] ? e.u : e.v;
      const to = inS[e.u] ? e.v : e.u;
      list.push({ id: e.id, u: from, v: to, w: e.w });
    }
    list.sort((a, b) => (a.w !== b.w ? a.w - b.w : a.id < b.id ? -1 : 1));
    return list;
  }

  function paint(line, msg, current, activeEid) {
    const s = stepOf(g, line, msg, {
      setS: setS(),
      mstWeight: weight,
      pq: candidates().map((e) => ({ id: `${e.u}${e.v}`, key: e.w, edge: `${e.u}—${e.v}` }))
    });
    for (const id of Object.keys(inS)) {
      if (inS[id]) s.nodes[id] = 'visited';
    }
    if (current) s.nodes[current] = 'current';
    applyTree(s, tree);
    if (activeEid) s.edges[activeEid] = 'active';
    return s;
  }

  steps.push(paint(1, `Bắt đầu Prim tại ${src}. S = {${src}}.`, src));
  let guard = g.nodes.length + 2;
  while (guard--) {
    if (setS().length === g.nodes.length) {
      steps.push(paint(2, `S đã chứa mọi đỉnh. Prim kết thúc. Tổng MST = ${weight}.`));
      break;
    }
    const cands = candidates();
    const best = cands[0] ? findEdge(g, cands[0].id) : null;
    if (!best) {
      steps.push(paint(4, `Không còn cạnh ra khỏi S — phần còn lại không tới được. Tổng = ${weight}.`));
      break;
    }
    const from = inS[best.u] ? best.u : best.v;
    const to = inS[best.u] ? best.v : best.u;
    steps.push(paint(3, `Cạnh nhẹ nhất ra khỏi S: ${from} — ${to} (w = ${best.w}).`, from, best.id));
    inS[to] = true;
    tree[best.id] = true;
    weight += best.w;
    steps.push(paint(5, `Thêm ${to} vào S, thêm cạnh vào MST. Tổng = ${weight}. S = {${setS().join(', ')}}.`, to, best.id));
  }
  return steps;
}

export function buildSteps(g, algo, src) {
  if (algo === 'bfs') return buildBfsSteps(g, src);
  if (algo === 'dfs') return buildDfsSteps(g, src);
  if (algo === 'dijkstra') return buildDijkstraSteps(g, src);
  if (algo === 'kruskal') return buildKruskalSteps(g);
  if (algo === 'prim') return buildPrimSteps(g, src);
  return [stepOf(g, 0, 'Thuật toán không hỗ trợ.')];
}

export function fmtVal(d) {
  return d === Infinity || d === undefined || d === null ? '∞' : String(d);
}
