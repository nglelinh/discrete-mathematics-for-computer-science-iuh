// Bổ đề bơm: duyệt mọi cách chia và kiểm tra có “bơm” được không.

const rep = (s, k) => s.repeat(k);
const isAnBn = (w) => /^(a*)(b*)$/.test(w) && /^(a*)/.exec(w)[1].length === w.length - /^(a*)/.exec(w)[1].length;
const isAnBnCn = (w) => { const m = /^(a*)(b*)(c*)$/.exec(w); return !!m && m[1].length === m[2].length && m[2].length === m[3].length; };
const isPal = (w) => w === [...w].reverse().join('');

export const PUMP_LANGS = {
  regular: [
    { id: 'anbn', name: 'L = { aⁿbⁿ : n ≥ 0 } (không chính quy)', inL: (w) => isAnBn(w), word: (p) => rep('a', p) + rep('b', p), regular: false },
    { id: 'pal', name: 'L = { palindrome trên {0,1} } (không chính quy)', inL: isPal, word: (p) => rep('0', p) + '1' + rep('0', p), alpha: '01', regular: false },
    { id: 'abstar', name: 'L = (ab)* (chính quy)', inL: (w) => /^(ab)*$/.test(w), word: (p) => rep('ab', p), regular: true }
  ],
  cfl: [
    { id: 'anbncn', name: 'L = { aⁿbⁿcⁿ } (không phi ngữ cảnh)', inL: isAnBnCn, word: (p) => rep('a', p) + rep('b', p) + rep('c', p), regular: false },
    { id: 'anbn', name: 'L = { aⁿbⁿ } (phi ngữ cảnh)', inL: (w) => isAnBn(w), word: (p) => rep('a', p) + rep('b', p), regular: true },
    { id: 'ww', name: 'L = { ww : w ∈ {a,b}* } (không phi ngữ cảnh)', inL: (w) => w.length % 2 === 0 && w.slice(0, w.length / 2) === w.slice(w.length / 2), word: (p) => rep('a', p) + rep('b', p) + rep('a', p) + rep('b', p), regular: false }
  ]
};

export const IS = [0, 1, 2, 3];

/** Mọi cách chia xyz với |xy| ≤ p, |y| ≥ 1. */
export function regularSplits(w, p) {
  const out = [];
  for (let a = 0; a <= Math.min(p, w.length); a++) for (let b = a + 1; b <= Math.min(p, w.length); b++) out.push({ parts: [w.slice(0, a), w.slice(a, b), w.slice(b)], idx: [a, b] });
  return out;
}
/** Mọi cách chia uvxyz với |vxy| ≤ p, |vy| ≥ 1. */
export function cflSplits(w, p) {
  const out = [];
  const n = w.length;
  for (let i = 0; i <= n; i++) for (let j = i; j <= n; j++) for (let k = j; k <= n; k++) for (let l = k; l <= n && l - i <= p; l++) {
    if ((j - i) + (l - k) < 1) continue;
    out.push({ parts: [w.slice(0, i), w.slice(i, j), w.slice(j, k), w.slice(k, l), w.slice(l)], idx: [i, j, k, l] });
  }
  return out;
}

/** Bơm: các phần ở vị trí pumped (1 và 3 cho CFL, 1 cho regular) lặp i lần. */
export function pump(parts, kind, i) {
  if (kind === 'regular') return parts[0] + rep(parts[1], i) + parts[2];
  return parts[0] + rep(parts[1], i) + parts[2] + rep(parts[3], i) + parts[4];
}

export function evaluate(lang, kind, w, p) {
  const splits = kind === 'regular' ? regularSplits(w, p) : cflSplits(w, p);
  return splits.map((s) => {
    const res = IS.map((i) => lang.inL(pump(s.parts, kind, i)));
    return { ...s, res, survives: res.every(Boolean) };
  });
}
