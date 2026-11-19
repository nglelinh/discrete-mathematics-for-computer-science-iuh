/** Đếm: tổ hợp, chỉnh hợp, Pascal, sao–vạch, chuồng bồ câu. Dùng BigInt để không tràn số. */

export function binom(n, k) {
  if (k < 0 || k > n) return 0n;
  k = Math.min(k, n - k);
  let r = 1n;
  for (let i = 1; i <= k; i++) r = (r * BigInt(n - k + i)) / BigInt(i);
  return r;
}
export function perm(n, k) {
  if (k < 0 || k > n) return 0n;
  let r = 1n;
  for (let i = 0; i < k; i++) r *= BigInt(n - i);
  return r;
}
export const fact = (n) => perm(n, n);

export function pascalRow(n) {
  const row = [1n];
  for (let k = 1; k <= n; k++) row.push((row[k - 1] * BigInt(n - k + 1)) / BigInt(k));
  return row;
}

/** Liệt kê tổ hợp chập k của {1..n} (tối đa limit). */
export function combinations(n, k, limit = 200) {
  const out = [];
  const cur = [];
  (function go(start) {
    if (out.length >= limit) return;
    if (cur.length === k) { out.push(cur.slice()); return; }
    for (let i = start; i <= n; i++) { cur.push(i); go(i + 1); cur.pop(); if (out.length >= limit) return; }
  })(1);
  return out;
}
export function permutations(n, k, limit = 200) {
  const out = [];
  const cur = [];
  const used = new Array(n + 1).fill(false);
  (function go() {
    if (out.length >= limit) return;
    if (cur.length === k) { out.push(cur.slice()); return; }
    for (let i = 1; i <= n; i++) {
      if (used[i]) continue;
      used[i] = true; cur.push(i); go(); cur.pop(); used[i] = false;
      if (out.length >= limit) return;
    }
  })();
  return out;
}

/** Nghiệm của x1+…+xk = n, mỗi xi ≥ lower. */
export function compositions(n, k, lower = 0, limit = 500) {
  const out = [];
  const rest = n - lower * k;
  if (rest < 0) return out;
  const cur = [];
  (function go(i, left) {
    if (out.length >= limit) return;
    if (i === k - 1) { out.push([...cur, left + lower]); return; }
    for (let x = 0; x <= left; x++) { cur.push(x + lower); go(i + 1, left - x); cur.pop(); if (out.length >= limit) return; }
  })(0, rest);
  return out;
}
export const countCompositions = (n, k, lower = 0) => {
  const rest = n - lower * k;
  return rest < 0 ? 0n : binom(rest + k - 1, k - 1);
};
export function starsBars(sol) {
  return sol.map((x) => '★'.repeat(x)).join(' | ');
}

export function pigeonBound(n, k) {
  return Math.ceil(n / k);
}
export const maxLoad = (counts) => Math.max(0, ...counts);
