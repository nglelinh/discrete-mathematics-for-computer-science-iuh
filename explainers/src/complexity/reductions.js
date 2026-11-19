// Quy dẫn đa thức: SAT → 3-SAT, IS ↔ CLIQUE ↔ VC, xấp xỉ Vertex Cover gấp đôi.
import { clauseText } from '../logic/dpll.js';

/** Biến mỗi mệnh đề (độ dài k) thành các mệnh đề đúng 3 literal, dùng biến mới yᵢ. */
const sub = (n) => String(n).replace(/\d/g, (d) => '₀₁₂₃₄₅₆₇₈₉'[d]);
export function to3SAT(clauses, names) {
  const all = [...names];
  let fresh = 0;
  const newVar = () => { fresh++; all.push('y' + fresh); return all.length; };
  const out = [];
  const steps = [];
  for (const c of clauses) {
    let prod = [];
    const k = c.length;
    let rule;
    if (k === 1) {
      const a = newVar(), b = newVar();
      prod = [[c[0], a, b], [c[0], a, -b], [c[0], -a, b], [c[0], -a, -b]];
      rule = 'k = 1: thêm 2 biến mới a, b và 4 mệnh đề phủ mọi tổ hợp của (a, b); chúng đều chứa l₁ nên chỉ đúng khi l₁ đúng.';
    } else if (k === 2) {
      const a = newVar();
      prod = [[c[0], c[1], a], [c[0], c[1], -a]];
      rule = 'k = 2: thêm 1 biến mới a và hai mệnh đề (l₁ ∨ l₂ ∨ a), (l₁ ∨ l₂ ∨ ¬a).';
    } else if (k === 3) {
      prod = [[...c]];
      rule = 'k = 3: giữ nguyên.';
    } else {
      const ys = Array.from({ length: k - 3 }, () => newVar());
      prod.push([c[0], c[1], ys[0]]);
      for (let i = 1; i < k - 3; i++) prod.push([-ys[i - 1], c[i + 1], ys[i]]);
      prod.push([-ys[k - 4], c[k - 2], c[k - 1]]);
      rule = `k = ${k}: dùng ${k - 3} biến mới tạo chuỗi: (l₁ ∨ l₂ ∨ y₁), (¬y₁ ∨ l₃ ∨ y₂), … , (¬y${sub(k - 3)} ∨ l${sub(k - 1)} ∨ l${sub(k)}).`;
    }
    out.push(...prod);
    steps.push({ orig: c, produced: prod, rule, names: [...all] });
  }
  return { clauses: out, names: all, steps, fresh };
}

export const GRAPH_PRESETS = [
  {
    id: 'house', name: 'Ngôi nhà (6 đỉnh)',
    nodes: [{ id: 'A', x: 270, y: 30 }, { id: 'B', x: 130, y: 100 }, { id: 'C', x: 410, y: 100 }, { id: 'D', x: 130, y: 220 }, { id: 'E', x: 410, y: 220 }, { id: 'F', x: 270, y: 150 }],
    edges: [['A', 'B'], ['A', 'C'], ['B', 'C'], ['B', 'D'], ['C', 'E'], ['D', 'E'], ['F', 'B'], ['F', 'C']]
  },
  {
    id: 'cycle', name: 'Chu trình C₆',
    nodes: [0, 1, 2, 3, 4, 5].map((i) => ({ id: String.fromCharCode(65 + i), x: 270 + 110 * Math.sin((i * Math.PI) / 3), y: 125 - 100 * Math.cos((i * Math.PI) / 3) })),
    edges: [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['E', 'F'], ['F', 'A']]
  },
  {
    id: 'star', name: 'Sao + cạnh phụ',
    nodes: [{ id: 'A', x: 270, y: 125 }, { id: 'B', x: 270, y: 25 }, { id: 'C', x: 400, y: 80 }, { id: 'D', x: 400, y: 175 }, { id: 'E', x: 270, y: 235 }, { id: 'F', x: 140, y: 175 }, { id: 'G', x: 140, y: 80 }],
    edges: [['A', 'B'], ['A', 'C'], ['A', 'D'], ['A', 'E'], ['A', 'F'], ['A', 'G'], ['B', 'C']]
  },
  {
    id: 'matching', name: '3 cạnh rời nhau (tỉ lệ xấu nhất = 2)',
    nodes: [{ id: 'A', x: 90, y: 60 }, { id: 'B', x: 90, y: 200 }, { id: 'C', x: 270, y: 60 }, { id: 'D', x: 270, y: 200 }, { id: 'E', x: 450, y: 60 }, { id: 'F', x: 450, y: 200 }],
    edges: [['A', 'B'], ['C', 'D'], ['E', 'F']]
  }
];

const has = (g, a, b) => g.edges.some((e) => (e[0] === a && e[1] === b) || (e[0] === b && e[1] === a));
export const isIndependent = (g, S) => S.every((a, i) => S.every((b, j) => i >= j || !has(g, a, b)));
export const isVertexCover = (g, S) => g.edges.every(([a, b]) => S.includes(a) || S.includes(b));
export function complement(g) {
  const edges = [];
  g.nodes.forEach((a, i) => g.nodes.forEach((b, j) => { if (i < j && !has(g, a.id, b.id)) edges.push([a.id, b.id]); }));
  return { nodes: g.nodes, edges };
}
export const isClique = (g, S) => S.every((a, i) => S.every((b, j) => i >= j || has(g, a, b)));
export function subsets(ids) {
  const out = [];
  for (let m = 0; m < 1 << ids.length; m++) out.push(ids.filter((_, i) => (m >> i) & 1));
  return out;
}
export function maxIndependent(g) {
  const ids = g.nodes.map((n) => n.id);
  return subsets(ids).filter((S) => isIndependent(g, S)).sort((a, b) => b.length - a.length)[0];
}
export function minVertexCover(g) {
  const ids = g.nodes.map((n) => n.id);
  return subsets(ids).filter((S) => isVertexCover(g, S)).sort((a, b) => a.length - b.length)[0];
}

/** 2-xấp xỉ: lấy một cạnh chưa phủ, thêm cả hai đầu mút, xóa mọi cạnh kề. */
export function approxVCSteps(g) {
  let left = g.edges.map((e) => [...e]);
  const cover = [];
  const chosen = [];
  const steps = [{ cover: [], chosen: [], left: left.map((e) => [...e]), edge: null, msg: `Còn ${left.length} cạnh chưa được phủ. Lặp: chọn một cạnh chưa phủ, đưa CẢ HAI đầu mút vào phủ.` }];
  while (left.length) {
    const [u, v] = left[0];
    cover.push(u, v); chosen.push([u, v]);
    left = left.filter((e) => !e.includes(u) && !e.includes(v));
    steps.push({ cover: [...cover], chosen: chosen.map((e) => [...e]), left: left.map((e) => [...e]), edge: [u, v], msg: `Chọn cạnh ${u}–${v}: thêm ${u}, ${v}; xóa mọi cạnh chứa chúng. Còn ${left.length} cạnh.` });
  }
  const opt = minVertexCover(g).length;
  steps.push({ cover: [...cover], chosen: chosen.map((e) => [...e]), left: [], edge: null, done: true, opt, msg: `Hết cạnh. |C| = ${cover.length}, tối ưu |OPT| = ${opt}, tỉ lệ ${(cover.length / Math.max(1, opt)).toFixed(2)} ≤ 2 (vì các cạnh đã chọn rời nhau, OPT phải chứa ít nhất một đầu mút của mỗi cạnh).` });
  return steps;
}
export { clauseText };
