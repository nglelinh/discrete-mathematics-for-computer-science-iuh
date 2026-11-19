// Logic thuần cho lý thuyết số (dùng BigInt khi cần để tránh tràn).

export const mod = (a, n) => ((a % n) + n) % n;

export function gcd(a, b) { a = Math.abs(a); b = Math.abs(b); while (b) [a, b] = [b, a % b]; return a; }
export const lcm = (a, b) => (a && b ? Math.abs(a * b) / gcd(a, b) : 0);

/** Euclid mở rộng: các dòng a = q·b + r kèm hệ số s,t sao cho s·a + t·b = gcd. */
export function extendedEuclid(a, b) {
  let [r0, r1] = [a, b], [s0, s1] = [1, 0], [t0, t1] = [0, 1];
  const rows = [{ q: null, r: r0, s: s0, t: t0 }, { q: null, r: r1, s: s1, t: t1 }];
  while (r1 !== 0) {
    const q = Math.trunc(r0 / r1);
    [r0, r1] = [r1, r0 - q * r1];
    [s0, s1] = [s1, s0 - q * s1];
    [t0, t1] = [t1, t0 - q * t1];
    rows.push({ q, r: r1, s: s1, t: t1 });
  }
  let g = r0, x = s0, y = t0;
  if (g < 0) { g = -g; x = -x; y = -y; }
  return { g, x, y, rows };
}

/** Các bước thuần Euclid (không hệ số): a = q b + r. */
export function euclidSteps(a, b) {
  const steps = [];
  a = Math.abs(a); b = Math.abs(b);
  while (b) { const q = Math.floor(a / b), r = a % b; steps.push({ a, b, q, r }); [a, b] = [b, r]; }
  return { steps, g: a };
}

export function modInverse(a, n) {
  const { g, x } = extendedEuclid(mod(a, n), n);
  return g === 1 ? mod(x, n) : null;
}

/** Nghiệm của a x ≡ c (mod n). */
export function solveLinearCongruence(a, c, n) {
  const g = gcd(a, n);
  if (c % g !== 0) return { solutions: [], g };
  const a1 = a / g, c1 = c / g, n1 = n / g;
  const inv = modInverse(a1, n1);
  const x0 = mod(inv * c1, n1);
  const sols = [];
  for (let k = 0; k < g; k++) sols.push(x0 + k * n1);
  return { solutions: sols, g, x0, n1 };
}

/** Lũy thừa nhanh theo bình phương liên tiếp (BigInt). */
export function modPow(base, exp, m) {
  base = BigInt(base); exp = BigInt(exp); m = BigInt(m);
  let result = 1n % m; base = ((base % m) + m) % m;
  while (exp > 0n) { if (exp & 1n) result = (result * base) % m; base = (base * base) % m; exp >>= 1n; }
  return result;
}

export function modPowSteps(base, exp, m) {
  const bits = exp.toString(2);
  let result = 1 % m;
  const rows = [];
  let b = ((base % m) + m) % m;
  // duyệt từ bit thấp đến cao
  const lowToHigh = [...bits].reverse();
  for (let i = 0; i < lowToHigh.length; i++) {
    const bit = lowToHigh[i];
    const before = result;
    if (bit === '1') result = (result * b) % m;
    rows.push({ i, bit, sq: b, before, result, mult: bit === '1' });
    b = (b * b) % m;
  }
  return { bits, rows, result };
}

export function sieve(n, upto = n) {
  const comp = new Array(n + 1).fill(false);
  const steps = []; // mỗi bước: p và các bội bị gạch
  for (let p = 2; p * p <= n; p++) {
    if (comp[p]) continue;
    const crossed = [];
    for (let m = p * p; m <= n; m += p) if (!comp[m]) { comp[m] = true; crossed.push(m); }
    steps.push({ p, crossed });
  }
  const primes = [];
  for (let i = 2; i <= upto; i++) if (!comp[i]) primes.push(i);
  return { comp, steps, primes };
}

export function factorize(n) {
  const out = [];
  for (let p = 2; p * p <= n; p++) { let e = 0; while (n % p === 0) { n /= p; e++; } if (e) out.push([p, e]); }
  if (n > 1) out.push([n, 1]);
  return out;
}
export const isPrime = (n) => n >= 2 && factorize(n).length === 1 && factorize(n)[0][1] === 1;
export const phi = (n) => factorize(n).reduce((r, [p]) => (r / p) * (p - 1), n);

/** RSA đồ chơi với số nhỏ. */
export function rsaKeys(p, q, eWanted) {
  if (!isPrime(p) || !isPrime(q) || p === q) return { error: 'p và q phải là hai số nguyên tố khác nhau.' };
  const n = p * q, ph = (p - 1) * (q - 1);
  let e = eWanted;
  if (!e || gcd(e, ph) !== 1 || e <= 1 || e >= ph) {
    e = 3; while (e < ph && gcd(e, ph) !== 1) e += 2;
    if (e >= ph) return { error: 'Không tìm được e hợp lệ — chọn p, q lớn hơn.' };
  }
  const d = modInverse(e, ph);
  return { p, q, n, phi: ph, e, d };
}
export const rsaEncrypt = (m, k) => Number(modPow(m, k.e, k.n));
export const rsaDecrypt = (c, k) => Number(modPow(c, k.d, k.n));

/** Bảng cộng/nhân đồng dư. */
export function modTable(n, op) {
  return Array.from({ length: n }, (_, i) => Array.from({ length: n }, (_, j) => mod(op === '+' ? i + j : i * j, n)));
}

/** Định lý số dư Trung Hoa cho hai modulus nguyên tố cùng nhau. */
export function crt(a1, n1, a2, n2) {
  if (gcd(n1, n2) !== 1) return null;
  const inv = modInverse(n1, n2);
  const k = mod((a2 - a1) * inv, n2);
  return { x: a1 + n1 * k, mod: n1 * n2 };
}
