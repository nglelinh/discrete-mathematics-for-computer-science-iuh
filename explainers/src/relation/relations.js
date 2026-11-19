/** Quan hệ hai ngôi trên tập n phần tử, biểu diễn bằng ma trận 0/1. */

export const makeMatrix = (n, f = () => false) => Array.from({ length: n }, (_, i) => Array.from({ length: n }, (_, j) => !!f(i, j)));
export const cloneM = (M) => M.map((r) => r.slice());

/** Mỗi tính chất trả về { ok, witness: { cells: [[i,j]...], msg } | null }. */
export function properties(M, labels) {
  const n = M.length;
  const L = (i) => labels[i];
  const pair = (i, j) => `(${L(i)}, ${L(j)})`;
  const res = {};

  let w = null;
  for (let i = 0; i < n && !w; i++) if (!M[i][i]) w = { cells: [[i, i]], msg: `Thiếu ${pair(i, i)}: ${L(i)} không quan hệ với chính nó.` };
  res.reflexive = { ok: !w, witness: w };

  w = null;
  for (let i = 0; i < n && !w; i++) if (M[i][i]) w = { cells: [[i, i]], msg: `Có ${pair(i, i)}: ${L(i)} quan hệ với chính nó.` };
  res.irreflexive = { ok: !w, witness: w };

  w = null;
  for (let i = 0; i < n && !w; i++) for (let j = 0; j < n && !w; j++) if (M[i][j] && !M[j][i]) w = { cells: [[i, j], [j, i]], msg: `Có ${pair(i, j)} nhưng thiếu ${pair(j, i)}.` };
  res.symmetric = { ok: !w, witness: w };

  w = null;
  for (let i = 0; i < n && !w; i++) for (let j = i + 1; j < n && !w; j++) if (M[i][j] && M[j][i]) w = { cells: [[i, j], [j, i]], msg: `Có cả ${pair(i, j)} và ${pair(j, i)} nhưng ${L(i)} ≠ ${L(j)}.` };
  res.antisymmetric = { ok: !w, witness: w };

  w = null;
  for (let i = 0; i < n && !w; i++) for (let j = 0; j < n && !w; j++) if (M[i][j] && M[j][i]) w = { cells: i === j ? [[i, i]] : [[i, j], [j, i]], msg: i === j ? `Có ${pair(i, i)} — bất đối xứng không cho phép khuyên.` : `Có cả ${pair(i, j)} và ${pair(j, i)}.` };
  res.asymmetric = { ok: !w, witness: w };

  w = null;
  for (let i = 0; i < n && !w; i++) for (let j = 0; j < n && !w; j++) if (M[i][j]) for (let k = 0; k < n && !w; k++) if (M[j][k] && !M[i][k]) w = { cells: [[i, j], [j, k], [i, k]], msg: `Có ${pair(i, j)} và ${pair(j, k)} nhưng thiếu ${pair(i, k)}.` };
  res.transitive = { ok: !w, witness: w };

  res.equivalence = { ok: res.reflexive.ok && res.symmetric.ok && res.transitive.ok };
  res.partialOrder = { ok: res.reflexive.ok && res.antisymmetric.ok && res.transitive.ok };
  return res;
}

export function reflexiveClosure(M) {
  const R = cloneM(M);
  const added = [];
  for (let i = 0; i < M.length; i++) if (!R[i][i]) { R[i][i] = true; added.push([i, i]); }
  return { R, added };
}
export function symmetricClosure(M) {
  const R = cloneM(M);
  const added = [];
  for (let i = 0; i < M.length; i++) for (let j = 0; j < M.length; j++) if (M[i][j] && !R[j][i]) { R[j][i] = true; added.push([j, i]); }
  return { R, added };
}

/** Warshall: trả về các ảnh chụp W_0 … W_n; ảnh k thêm các ô qua đỉnh trung gian k-1. */
export function warshallSteps(M) {
  const n = M.length;
  let cur = cloneM(M);
  const steps = [{ k: 0, M: cloneM(cur), added: [], via: null }];
  for (let k = 0; k < n; k++) {
    const next = cloneM(cur);
    const added = [];
    for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) if (cur[i][k] && cur[k][j] && !cur[i][j]) { next[i][j] = true; added.push([i, j]); }
    steps.push({ k: k + 1, M: cloneM(next), added, via: k });
    cur = next;
  }
  return steps;
}
export function transitiveClosure(M) {
  const s = warshallSteps(M);
  return s[s.length - 1].M;
}

export function equivalenceClasses(M) {
  const n = M.length;
  const seen = new Array(n).fill(false);
  const out = [];
  for (let i = 0; i < n; i++) {
    if (seen[i]) continue;
    const cls = [];
    for (let j = 0; j < n; j++) if (M[i][j]) { cls.push(j); seen[j] = true; }
    out.push(cls);
  }
  return out;
}

/** Sơ đồ Hasse của thứ tự riêng phần: cạnh phủ và tầng. */
export function hasse(M) {
  const n = M.length;
  const lt = (a, b) => a !== b && M[a][b];
  const cover = [];
  for (let a = 0; a < n; a++) for (let b = 0; b < n; b++) {
    if (!lt(a, b)) continue;
    let between = false;
    for (let c = 0; c < n; c++) if (lt(a, c) && lt(c, b)) between = true;
    if (!between) cover.push([a, b]);
  }
  const level = new Array(n).fill(0);
  for (let it = 0; it < n; it++) for (const [a, b] of cover) level[b] = Math.max(level[b], level[a] + 1);
  const maximal = [...Array(n).keys()].filter((a) => ![...Array(n).keys()].some((b) => lt(a, b)));
  const minimal = [...Array(n).keys()].filter((a) => ![...Array(n).keys()].some((b) => lt(b, a)));
  return { cover, level, maximal, minimal };
}

export const PRESETS = [
  { id: 'mod2', label: 'Đồng dư mod 2 trên {1..6} (tương đương)', labels: ['1', '2', '3', '4', '5', '6'], f: (i, j) => (i - j) % 2 === 0 },
  { id: 'leq', label: '≤ trên {1..5} (thứ tự toàn phần)', labels: ['1', '2', '3', '4', '5'], f: (i, j) => i <= j },
  { id: 'div', label: 'Ước số "a | b" trên {1,2,3,4,6,12} (thứ tự riêng phần)', labels: ['1', '2', '3', '4', '6', '12'], f: (i, j) => [1, 2, 3, 4, 6, 12][j] % [1, 2, 3, 4, 6, 12][i] === 0 },
  { id: 'lt', label: '< trên {1..4} (bất phản xạ, bắc cầu)', labels: ['1', '2', '3', '4'], f: (i, j) => i < j },
  { id: 'sym', label: 'Bạn bè (đối xứng, không bắc cầu)', labels: ['An', 'Bình', 'Chi', 'Dũng'], f: (i, j) => [[0, 1], [1, 2], [2, 3]].some(([a, b]) => (a === i && b === j) || (a === j && b === i)) },
  { id: 'next', label: 'Kế tiếp i → i+1 (chưa bắc cầu — thử Warshall)', labels: ['1', '2', '3', '4', '5'], f: (i, j) => j === i + 1 },
  { id: 'empty', label: 'Rỗng (tự vẽ)', labels: ['a', 'b', 'c', 'd'], f: () => false }
];
