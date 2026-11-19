/** Dãy truy hồi tuyến tính bậc hai: a_n = c1 a_{n-1} + c2 a_{n-2} + k, và cây chia để trị. */

export function terms(c1, c2, k, a0, a1, N) {
  const a = [a0, a1];
  for (let n = 2; n <= N; n++) a.push(c1 * a[n - 1] + c2 * a[n - 2] + k);
  return a.slice(0, N + 1);
}

const fmt = (x) => {
  if (!Number.isFinite(x)) return String(x);
  const r = Math.round(x * 10000) / 10000;
  return Object.is(r, -0) ? '0' : String(r);
};
export { fmt };

/** Nghiệm tổng quát: nghiệm thuần nhất + nghiệm riêng, hệ số từ a0, a1. */
export function solveClosed(c1, c2, k, a0, a1) {
  const disc = c1 * c1 + 4 * c2;
  const charEq = `r² ${c1 >= 0 ? '−' : '+'} ${fmt(Math.abs(c1))}r ${c2 >= 0 ? '−' : '+'} ${fmt(Math.abs(c2))} = 0`;
  // nghiệm riêng cho hằng k
  let part = { type: 'const', p: 0 };
  if (k !== 0) {
    const s = 1 - c1 - c2;
    if (Math.abs(s) > 1e-12) part = { type: 'const', p: k / s };
    else if (Math.abs(c1 + 2 * c2) > 1e-12) part = { type: 'lin', p: k / (c1 + 2 * c2) };
    else part = { type: 'quad', p: k / 2 };
  }
  const partVal = (n) => (part.type === 'const' ? part.p : part.type === 'lin' ? part.p * n : part.p * n * n);

  if (c2 === 0) {
    // truy hồi cấp 1: aₙ = c1·aₙ₋₁ + k  →  aₙ = (a0 − p(0))·c1ⁿ + p(n)
    const C1o = a0 - partVal(0);
    const pf1 = (x) => (x < 0 ? `(${fmt(x)})` : fmt(x));
    const partTxt = k === 0 ? '' : part.type === 'const' ? ` + ${fmt(part.p)}` : part.type === 'lin' ? ` + ${fmt(part.p)}·n` : ` + ${fmt(part.p)}·n²`;
    return {
      disc, charEq: `r − ${fmt(c1)} = 0 (cấp 1)`, kind: 'order1', roots: [c1], C1: C1o, C2: 0, part,
      value: (n) => C1o * c1 ** n + partVal(n),
      formula: `aₙ = ${fmt(C1o)}·${pf1(c1)}ⁿ${partTxt}`
    };
  }
  let kind, roots, basis;
  if (disc > 1e-12) {
    const s = Math.sqrt(disc);
    const r1 = (c1 + s) / 2, r2 = (c1 - s) / 2;
    kind = 'distinct'; roots = [r1, r2];
    basis = [(n) => r1 ** n, (n) => r2 ** n];
  } else if (Math.abs(disc) <= 1e-12) {
    const r = c1 / 2;
    kind = 'double'; roots = [r];
    basis = [(n) => r ** n, (n) => n * r ** n];
  } else {
    const rho = Math.sqrt(-c2), theta = Math.atan2(Math.sqrt(-disc) / 2, c1 / 2);
    kind = 'complex'; roots = [{ rho, theta }];
    basis = [(n) => rho ** n * Math.cos(n * theta), (n) => rho ** n * Math.sin(n * theta)];
  }
  // giải C1, C2: basis_i(0) C1 + ... = a0 - part(0); tại n = 1 tương tự
  const t0 = a0 - partVal(0), t1 = a1 - partVal(1);
  const m = [[basis[0](0), basis[1](0)], [basis[0](1), basis[1](1)]];
  const det = m[0][0] * m[1][1] - m[0][1] * m[1][0];
  let C1 = 0, C2 = 0;
  if (Math.abs(det) > 1e-12) {
    C1 = (t0 * m[1][1] - m[0][1] * t1) / det;
    C2 = (m[0][0] * t1 - t0 * m[1][0]) / det;
  } else {
    // c2 = 0: nghiệm r2 = 0 suy biến; chỉ dùng C1 r1^n (n ≥ 1) và hiệu chỉnh n = 0
    C1 = Math.abs(c1) > 1e-12 ? t1 / c1 : 0;
    C2 = t0 - C1;
  }
  const value = (n) => C1 * basis[0](n) + C2 * basis[1](n) + partVal(n);

  const pf = (x) => (x < 0 ? `(${fmt(x)})` : fmt(x));
  let hom;
  if (kind === 'distinct') hom = `${fmt(C1)}·${pf(roots[0])}ⁿ + ${fmt(C2)}·${pf(roots[1])}ⁿ`;
  else if (kind === 'double') hom = `(${fmt(C1)} + ${fmt(C2)}·n)·${pf(roots[0])}ⁿ`;
  else hom = `${fmt(roots[0].rho)}ⁿ·(${fmt(C1)}·cos(${fmt(roots[0].theta)}·n) + ${fmt(C2)}·sin(${fmt(roots[0].theta)}·n))`;
  const partText = k === 0 ? '' : part.type === 'const' ? ` + ${fmt(part.p)}` : part.type === 'lin' ? ` + ${fmt(part.p)}·n` : ` + ${fmt(part.p)}·n²`;
  return { disc, charEq, kind, roots, C1, C2, part, value, formula: `aₙ = ${hom}${partText}` };
}

/** Cây chia để trị T(n) = a·T(n/b) + n^d với n = b^m, T(1) = 1. */
export function divideConquer(a, b, d, m) {
  const levels = [];
  let total = 0;
  for (let i = 0; i < m; i++) {
    const nodes = a ** i;
    const size = b ** (m - i);
    const each = size ** d;
    levels.push({ i, nodes, size, each, sum: nodes * each });
    total += nodes * each;
  }
  const leaves = a ** m;
  levels.push({ i: m, nodes: leaves, size: 1, each: 1, sum: leaves, leaf: true });
  total += leaves;
  const crit = b ** d;
  const cls = a < crit ? 'root' : a === crit ? 'balanced' : 'leaves';
  const theta = cls === 'root' ? `Θ(n^${d})` : cls === 'balanced' ? `Θ(n^${d} log n)` : `Θ(n^${fmt(Math.log(a) / Math.log(b))})`;
  return { levels, total, cls, theta, crit };
}
export function directT(a, b, d, n) {
  return n <= 1 ? 1 : a * directT(a, b, d, n / b) + n ** d;
}

/** Cây gọi đệ quy fib(n): trả về nút, số lần gọi, và số lời gọi lặp. */
export function fibTree(n) {
  let id = 0;
  const seen = new Map();
  let calls = 0;
  function go(x) {
    calls++;
    const node = { id: id++, n: x, kids: [], dup: false };
    seen.set(x, (seen.get(x) || 0) + 1);
    node.dup = seen.get(x) > 1;
    if (x >= 2) node.kids = [go(x - 1), go(x - 2)];
    return node;
  }
  const root = go(n);
  return { root, calls, distinct: n + 1, dupCalls: calls - (n + 1) };
}
