// CRT từng bước, Miller–Rabin, trao đổi khóa Diffie–Hellman. Dùng BigInt.

export const mod = (a, m) => ((a % m) + m) % m;
export function modPow(b, e, m) {
  let r = 1n; b = mod(BigInt(b), BigInt(m)); e = BigInt(e); m = BigInt(m);
  while (e > 0n) { if (e & 1n) r = (r * b) % m; b = (b * b) % m; e >>= 1n; }
  return r % m;
}
export function egcd(a, b) { if (b === 0n) return [a, 1n, 0n]; const [g, x, y] = egcd(b, a % b); return [g, y, x - (a / b) * y]; }
export function modInv(a, m) { const [g, x] = egcd(mod(a, m), m); return g === 1n ? mod(x, m) : null; }
const gcd = (a, b) => (b === 0n ? a : gcd(b, a % b));

/** Giải x ≡ aᵢ (mod mᵢ), các mᵢ đôi một nguyên tố cùng nhau. */
export function crtSolve(rems, mods) {
  const a = rems.map(BigInt), m = mods.map(BigInt);
  if (m.some((x) => x < 2n)) return { error: 'Mỗi modulo phải ≥ 2.' };
  for (let i = 0; i < m.length; i++) for (let j = i + 1; j < m.length; j++) if (gcd(m[i], m[j]) !== 1n) return { error: `m${i + 1} = ${m[i]} và m${j + 1} = ${m[j]} không nguyên tố cùng nhau (gcd = ${gcd(m[i], m[j])}); CRT dạng này không áp dụng.` };
  const M = m.reduce((x, y) => x * y, 1n);
  let sum = 0n;
  const steps = m.map((mi, i) => {
    const Mi = M / mi, yi = modInv(Mi, mi), term = mod(a[i], mi) * Mi * yi;
    sum += term;
    return { i, ai: mod(a[i], mi), mi, Mi, yi, term };
  });
  const x = mod(sum, M);
  return { M, steps, sum, x, check: m.map((mi, i) => ({ mi, ai: mod(a[i], mi), ok: x % mi === mod(a[i], mi) })) };
}

/** Miller–Rabin cho cơ sở a: n − 1 = 2^s·d; dãy a^d, a^{2d}, …, a^{2^s·d}. */
export function millerRabinSteps(n, a) {
  n = BigInt(n); a = BigInt(a);
  if (n < 3n || n % 2n === 0n) return { error: 'n phải là số lẻ ≥ 3.' };
  if (a < 2n || a > n - 2n) return { error: 'Cơ sở a phải thuộc [2, n−2].' };
  let d = n - 1n, s = 0;
  while (d % 2n === 0n) { d /= 2n; s++; }
  const seq = [modPow(a, d, n)];
  for (let r = 1; r <= s; r++) seq.push((seq[r - 1] * seq[r - 1]) % n);
  let pass = seq[0] === 1n, at = pass ? 0 : -1;
  for (let r = 0; r < s && !pass; r++) if (seq[r] === n - 1n) { pass = true; at = r; }
  return { n, a, s, d, seq, pass, at };
}
export function isProbablePrime(n, bases = [2, 3, 5, 7, 11, 13, 17]) {
  n = BigInt(n);
  if (n < 2n) return false;
  for (const p of [2n, 3n, 5n, 7n, 11n, 13n, 17n, 19n, 23n, 29n]) { if (n === p) return true; if (n % p === 0n) return false; }
  return bases.every((b) => millerRabinSteps(n, BigInt(b)).pass);
}

/** Diffie–Hellman với p, g và khóa riêng a, b. */
export function dhSteps(p, g, a, b) {
  p = BigInt(p); g = BigInt(g); a = BigInt(a); b = BigInt(b);
  const A = modPow(g, a, p), B = modPow(g, b, p);
  const sA = modPow(B, a, p), sB = modPow(A, b, p);
  let tries = 0n, found = null;
  for (let x = 1n; x < p; x++) { tries++; if (modPow(g, x, p) === A) { found = x; break; } }
  return { p, g, a, b, A, B, sA, sB, equal: sA === sB, eve: { tries, found, secret: found === null ? null : modPow(B, found, p) } };
}
