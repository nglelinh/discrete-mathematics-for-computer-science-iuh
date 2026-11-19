/** Hàm f: X → Y với X = {0..nx-1}, Y = {0..ny-1}; f[x] = y hoặc null (chưa gán). */

export function analyze(f, nx, ny) {
  const unassigned = [];
  f.slice(0, nx).forEach((y, x) => { if (y === null || y === undefined) unassigned.push(x); });
  const wellDefined = unassigned.length === 0;
  const preimage = Array.from({ length: ny }, () => []);
  f.slice(0, nx).forEach((y, x) => { if (y !== null && y !== undefined) preimage[y].push(x); });
  const collisions = preimage.map((xs, y) => ({ y, xs })).filter((c) => c.xs.length > 1);
  const missed = preimage.map((xs, y) => ({ y, xs })).filter((c) => c.xs.length === 0).map((c) => c.y);
  const injective = wellDefined && collisions.length === 0;
  const surjective = wellDefined && missed.length === 0;
  const image = preimage.map((xs, y) => (xs.length ? y : -1)).filter((y) => y >= 0);
  return { wellDefined, unassigned, preimage, collisions, missed, injective, surjective, bijective: injective && surjective, image };
}

export function inverse(f, nx, ny) {
  const a = analyze(f, nx, ny);
  if (!a.bijective) return null;
  const g = new Array(ny).fill(null);
  f.slice(0, nx).forEach((y, x) => (g[y] = x));
  return g;
}

export function compose(g, f, nx) {
  return Array.from({ length: nx }, (_, x) => (f[x] === null || f[x] === undefined || g[f[x]] === null || g[f[x]] === undefined ? null : g[f[x]]));
}

export const PRESETS = [
  { id: 'inj', label: 'Đơn ánh nhưng không toàn ánh (3 → 5)', nx: 3, ny: 5, f: [1, 3, 4] },
  { id: 'surj', label: 'Toàn ánh nhưng không đơn ánh (5 → 3)', nx: 5, ny: 3, f: [0, 1, 2, 2, 0] },
  { id: 'bij', label: 'Song ánh (4 → 4)', nx: 4, ny: 4, f: [2, 0, 3, 1] },
  { id: 'sq', label: 'f(x) = x² mod 5 trên {0..4}', nx: 5, ny: 5, f: [0, 1, 4, 4, 1] },
  { id: 'inc', label: 'f(x) = x + 1 mod 5 (song ánh)', nx: 5, ny: 5, f: [1, 2, 3, 4, 0] },
  { id: 'bad', label: 'Không phải hàm: một x chưa có ảnh', nx: 4, ny: 4, f: [0, null, 2, 3] }
];
