// Logic thuần cho tam giác Pascal: dòng thời gian xây từ đỉnh xuống, đồng nhất thức, tô màu mod 2.

export function binomBig(n, k) {
  if (k < 0 || k > n) return 0n;
  k = Math.min(k, n - k);
  let r = 1n;
  for (let i = 1; i <= k; i++) r = (r * BigInt(n - k + i)) / BigInt(i);
  return r;
}
export const rowValues = (n) => Array.from({ length: n + 1 }, (_, k) => binomBig(n, k));

/** Số bước (ô) khi xây đến hàng N: 1 + 2 + … + (N+1). */
export const totalSteps = (N) => ((N + 1) * (N + 2)) / 2;
/** Chỉ số bước của ô (r,k). */
export const stepIndex = (r, k) => (r * (r + 1)) / 2 + k;
/** Bước thứ i → ô (r,k). */
export function cellOfStep(i) {
  let r = 0;
  while (((r + 1) * (r + 2)) / 2 <= i) r++;
  return { r, k: i - (r * (r + 1)) / 2 };
}

/** Dòng thời gian: mỗi bước tính một ô, kèm các ô cha ngay phía trên và công thức cộng. */
export function buildTimeline(N) {
  const rows = [];
  const steps = [];
  for (let r = 0; r <= N; r++) {
    const row = [];
    for (let k = 0; k <= r; k++) {
      const parents = [];
      if (r > 0) {
        if (k - 1 >= 0) parents.push({ r: r - 1, k: k - 1, v: rows[r - 1][k - 1] });
        if (k <= r - 1) parents.push({ r: r - 1, k, v: rows[r - 1][k] });
      }
      const v = r === 0 ? 1n : parents.reduce((s, p) => s + p.v, 0n);
      row.push(v);
      steps.push({ r, k, parents, v });
    }
    rows.push(row);
  }
  return { rows, steps };
}

/** Diễn giải thời điểm T (số thực): ô đang bay (cs) và tiến độ của nó (cp ∈ (0,1]). */
export function stepInfo(T, total) {
  if (T <= 0) return { done: 0, cs: -1, cp: 1 };
  if (T >= total) return { done: total, cs: total - 1, cp: 1 };
  const idx = Math.floor(T), prog = T - idx;
  if (prog === 0) return { done: idx, cs: idx - 1, cp: 1 };
  return { done: idx, cs: idx, cp: prog }; // ô idx đang chạy, chưa hoàn tất
}

export function explainStep(s) {
  if (!s) return 'Bấm Play hoặc Bước tiếp: tam giác được xây từ đỉnh xuống, mỗi ô bằng tổng hai ô ngay phía trên.';
  if (s.r === 0) return 'Đỉnh: C(0,0) = 1 — một tập rỗng chỉ có một tập con.';
  if (s.parents.length === 1) return `Hàng ${s.r}, ô ${s.k}: mép tam giác chỉ có MỘT ô cha (${s.parents[0].v}) nên ${s.v} = ${s.parents[0].v}. Vì C(${s.r},0) = C(${s.r},${s.r}) = 1.`;
  const [a, b] = s.parents;
  return `Hàng ${s.r}, ô ${s.k}: ${a.v} + ${b.v} = ${s.v}, tức C(${s.r},${s.k}) = C(${s.r - 1},${s.k - 1}) + C(${s.r - 1},${s.k}).`;
}

/* ---- đồng nhất thức ---- */
export function rowSum(n) {
  const row = rowValues(n);
  const sum = row.reduce((s, v) => s + v, 0n);
  const alt = row.reduce((s, v, k) => (k % 2 ? s - v : s + v), 0n);
  return { row, sum, pow: 1n << BigInt(n), alt };
}
export function symmetryPairs(n) {
  const out = [];
  for (let k = 0; k <= Math.floor(n / 2); k++) out.push({ k, mirror: n - k, v: binomBig(n, k), self: k === n - k });
  return out;
}
/** Cây gậy khúc côn cầu: Σ_{i=k}^{n} C(i,k) = C(n+1,k+1). */
export function hockey(n, k) {
  if (k < 0 || n < k) return null;
  const cells = [];
  for (let i = k; i <= n; i++) cells.push({ r: i, k, v: binomBig(i, k) });
  const sum = cells.reduce((s, c) => s + c.v, 0n);
  return { cells, sum, target: { r: n + 1, k: k + 1, v: binomBig(n + 1, k + 1) } };
}
/** C(n,k) lẻ ⇔ không có bit 1 nào của k trùng bit 1 của n−k (định lý Lucas/Kummer cho p = 2). */
export const isOdd = (n, k) => (k & (n - k)) === 0;
export function oddCount(n) { let c = 0; for (let k = 0; k <= n; k++) if (isOdd(n, k)) c++; return c; }

export const PRESETS = { build: 'build', rowsum: 'rowsum', sym: 'sym', hockey: 'hockey' };
export const RATES = [0.8, 1.6, 3.2, 6.5, 13]; // số ô mỗi giây
