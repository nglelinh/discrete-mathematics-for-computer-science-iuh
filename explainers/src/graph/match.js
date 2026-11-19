// Ghép cặp cực đại trên đồ thị hai phía (đường tăng, thuật toán Kuhn) và tô màu tham lam.

export const MATCH_PRESETS = [
  {
    id: 'jobs', name: 'Nhân viên – công việc',
    left: [{ id: 'An', y: 40 }, { id: 'Bình', y: 105 }, { id: 'Chi', y: 170 }, { id: 'Dũng', y: 235 }],
    right: [{ id: 'Web', y: 40 }, { id: 'DB', y: 105 }, { id: 'Test', y: 170 }, { id: 'UI', y: 235 }],
    edges: [['An', 'Web'], ['An', 'DB'], ['Bình', 'Web'], ['Chi', 'DB'], ['Chi', 'Test'], ['Dũng', 'Test'], ['Dũng', 'UI']]
  },
  {
    id: 'hall', name: 'Không có ghép đầy đủ (Hall bị vi phạm)',
    left: [{ id: 'X1', y: 50 }, { id: 'X2', y: 130 }, { id: 'X3', y: 210 }],
    right: [{ id: 'Y1', y: 50 }, { id: 'Y2', y: 130 }, { id: 'Y3', y: 210 }],
    edges: [['X1', 'Y1'], ['X2', 'Y1'], ['X3', 'Y1'], ['X3', 'Y2']]
  },
  {
    id: 'chain', name: 'Cần đường tăng dài',
    left: [{ id: 'L1', y: 40 }, { id: 'L2', y: 105 }, { id: 'L3', y: 170 }, { id: 'L4', y: 235 }],
    right: [{ id: 'R1', y: 40 }, { id: 'R2', y: 105 }, { id: 'R3', y: 170 }, { id: 'R4', y: 235 }],
    edges: [['L1', 'R1'], ['L1', 'R2'], ['L2', 'R2'], ['L2', 'R3'], ['L3', 'R3'], ['L3', 'R4'], ['L4', 'R4']]
  }
];

/** Thuật toán đường tăng: mỗi bước có matching hiện tại, cạnh đang xét, tập đỉnh phải đã thăm. */
export function kuhnSteps(g) {
  const adj = Object.fromEntries(g.left.map((l) => [l.id, g.edges.filter((e) => e[0] === l.id).map((e) => e[1])]));
  const matchL = {}, matchR = {};
  const steps = [];
  const snap = (extra) => steps.push({ matchL: { ...matchL }, matchR: { ...matchR }, edge: null, visited: [], root: null, size: Object.keys(matchL).length, done: false, ...extra });
  snap({ msg: 'Bắt đầu với ghép rỗng. Với mỗi đỉnh trái, tìm một đường tăng: đường đi xen kẽ cạnh chưa ghép / đã ghép, kết thúc ở đỉnh phải còn tự do.' });
  let visited;
  function tryFrom(u, root) {
    for (const r of adj[u]) {
      if (visited.has(r)) continue;
      visited.add(r);
      snap({ edge: [u, r], root, visited: [...visited], msg: `Xét cạnh ${u}–${r}.` });
      if (!matchR[r]) {
        matchR[r] = u; matchL[u] = r;
        snap({ edge: [u, r], root, visited: [...visited], msg: `${r} đang tự do ⇒ ghép ${u}–${r}.` });
        return true;
      }
      const w = matchR[r];
      snap({ edge: [u, r], root, visited: [...visited], msg: `${r} đã ghép với ${w}. Thử tìm cho ${w} một đỉnh phải khác (đi dọc đường xen kẽ).` });
      if (tryFrom(w, root)) {
        matchR[r] = u; matchL[u] = r;
        snap({ edge: [u, r], root, visited: [...visited], msg: `${w} đã chuyển chỗ ⇒ ${u} nhận ${r}. Đường tăng làm ghép lớn thêm 1.` });
        return true;
      }
    }
    return false;
  }
  for (const l of g.left) {
    visited = new Set();
    snap({ root: l.id, msg: `Tìm đường tăng xuất phát từ ${l.id}.` });
    const ok = tryFrom(l.id, l.id);
    if (!ok) snap({ root: l.id, visited: [...visited], msg: `Không có đường tăng từ ${l.id}: ${l.id} chưa được ghép.` });
  }
  const size = Object.keys(matchL).length;
  snap({ done: true, msg: `Ghép cực đại có ${size} cặp${size === g.left.length ? ' (ghép đầy đủ phía trái).' : `; ${g.left.length - size} đỉnh trái không được ghép.`}` });
  return steps;
}

export function bruteMaxMatching(g) {
  const adj = g.left.map((l) => g.edges.filter((e) => e[0] === l.id).map((e) => e[1]));
  let best = 0;
  (function go(i, used, cnt) {
    if (i === adj.length) { best = Math.max(best, cnt); return; }
    go(i + 1, used, cnt);
    for (const r of adj[i]) if (!used.has(r)) { used.add(r); go(i + 1, used, cnt + 1); used.delete(r); }
  })(0, new Set(), 0);
  return best;
}

// ---------------- Tô màu tham lam ----------------
export const COLOR_PRESETS = [
  {
    id: 'crown', name: 'Đồ thị “vương miện” (thứ tự quyết định số màu)',
    nodes: [{ id: 'u1', x: 110, y: 50 }, { id: 'u2', x: 110, y: 130 }, { id: 'u3', x: 110, y: 210 }, { id: 'v1', x: 430, y: 50 }, { id: 'v2', x: 430, y: 130 }, { id: 'v3', x: 430, y: 210 }],
    edges: [['u1', 'v2'], ['u1', 'v3'], ['u2', 'v1'], ['u2', 'v3'], ['u3', 'v1'], ['u3', 'v2']],
    badOrder: ['u1', 'v1', 'u2', 'v2', 'u3', 'v3']
  },
  {
    id: 'c5', name: 'Chu trình C₅ (χ = 3)',
    nodes: [0, 1, 2, 3, 4].map((i) => ({ id: 'c' + (i + 1), x: 270 + 95 * Math.sin((i * 2 * Math.PI) / 5), y: 130 - 95 * Math.cos((i * 2 * Math.PI) / 5) })),
    edges: [['c1', 'c2'], ['c2', 'c3'], ['c3', 'c4'], ['c4', 'c5'], ['c5', 'c1']], badOrder: ['c1', 'c3', 'c2', 'c5', 'c4']
  },
  {
    id: 'sched', name: 'Xếp lịch thi (môn trùng sinh viên không cùng ca)',
    nodes: [{ id: 'Toán', x: 90, y: 60 }, { id: 'Lý', x: 260, y: 40 }, { id: 'Hóa', x: 440, y: 70 }, { id: 'Tin', x: 120, y: 200 }, { id: 'Anh', x: 300, y: 210 }, { id: 'Sử', x: 460, y: 190 }],
    edges: [['Toán', 'Lý'], ['Toán', 'Tin'], ['Lý', 'Hóa'], ['Lý', 'Tin'], ['Lý', 'Anh'], ['Hóa', 'Anh'], ['Hóa', 'Sử'], ['Anh', 'Sử'], ['Tin', 'Anh']],
    badOrder: ['Toán', 'Hóa', 'Sử', 'Lý', 'Tin', 'Anh']
  }
];

export const degree = (g, id) => g.edges.filter((e) => e.includes(id)).length;
export function orderOf(g, kind) {
  const ids = g.nodes.map((n) => n.id);
  if (kind === 'degree') return [...ids].sort((a, b) => degree(g, b) - degree(g, a) || ids.indexOf(a) - ids.indexOf(b));
  if (kind === 'bad' && g.badOrder) return g.badOrder;
  return ids;
}

export function greedySteps(g, order) {
  const color = {};
  const nb = (v) => g.edges.filter((e) => e.includes(v)).map((e) => (e[0] === v ? e[1] : e[0]));
  const steps = [{ color: {}, cur: null, forbidden: [], msg: 'Duyệt đỉnh theo thứ tự đã chọn; mỗi đỉnh nhận màu nhỏ nhất chưa có ở các đỉnh kề.' }];
  for (const v of order) {
    const forb = [...new Set(nb(v).filter((u) => color[u] !== undefined).map((u) => color[u]))].sort((a, b) => a - b);
    let c = 0;
    while (forb.includes(c)) c++;
    color[v] = c;
    steps.push({ color: { ...color }, cur: v, forbidden: forb, msg: `${v}: các đỉnh kề đã dùng màu {${forb.map((x) => x + 1).join(', ') || '∅'}} ⇒ chọn màu ${c + 1}.` });
  }
  const used = new Set(Object.values(color)).size;
  steps.push({ color: { ...color }, cur: null, forbidden: [], done: true, used, msg: `Tô xong với ${used} màu.` });
  return steps;
}

export function chromaticNumber(g) {
  const ids = g.nodes.map((n) => n.id);
  for (let k = 1; k <= ids.length; k++) {
    const col = {};
    const ok = (function go(i) {
      if (i === ids.length) return true;
      for (let c = 0; c < k; c++) {
        if (g.edges.some(([a, b]) => (a === ids[i] && col[b] === c) || (b === ids[i] && col[a] === c))) continue;
        col[ids[i]] = c;
        if (go(i + 1)) return true;
        delete col[ids[i]];
      }
      return false;
    })(0);
    if (ok) return k;
  }
  return ids.length;
}

export const isProper = (g, color) => g.edges.every(([a, b]) => color[a] !== color[b]);
