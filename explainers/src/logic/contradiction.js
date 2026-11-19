// Phản chứng: √2 vô tỷ (bước chứng minh + thử phân số) và vô hạn số nguyên tố.
export const gcd = (a, b) => (b ? gcd(b, a % b) : Math.abs(a));

export const SQRT2_STEPS = [
  { text: 'Giả sử phản chứng: √2 là số hữu tỷ.', kind: 'assume' },
  { text: 'Khi đó √2 = a/b với a, b nguyên, b ≠ 0 và gcd(a, b) = 1 (phân số tối giản).', kind: 'setup' },
  { text: 'Bình phương hai vế: 2 = a²/b², tức a² = 2b².', kind: 'derive' },
  { text: 'a² = 2b² là số chẵn ⇒ a chẵn (bình phương số lẻ là số lẻ). Viết a = 2k.', kind: 'derive' },
  { text: 'Thế vào: (2k)² = 2b² ⇒ 4k² = 2b² ⇒ b² = 2k², nên b² chẵn ⇒ b chẵn.', kind: 'derive' },
  { text: 'Vậy a và b cùng chẵn ⇒ cả hai chia hết cho 2, trái với gcd(a, b) = 1.', kind: 'contradiction' },
  { text: 'Mâu thuẫn ⇒ giả sử sai. Vậy √2 là số vô tỷ. ∎', kind: 'conclude' }
];

/** Thử một phân số a/b: có thể thỏa a² = 2b² không? */
export function fractionTest(a, b) {
  if (!Number.isInteger(a) || !Number.isInteger(b) || b === 0) return { error: 'Cần hai số nguyên, b ≠ 0.' };
  const g = gcd(a, b), ra = a / g, rb = b / g;
  const sq = ra * ra, dbl = 2 * rb * rb;
  return { g, ra, rb, sq, dbl, equal: sq === dbl, diff: sq - dbl, aEven: ra % 2 === 0, bEven: rb % 2 === 0 };
}
/** Với mỗi b, a gần b√2 nhất và độ lệch a² − 2b² (luôn ≠ 0). */
export function nearMisses(maxB) {
  const out = [];
  for (let b = 1; b <= maxB; b++) {
    const a = Math.round(b * Math.SQRT2);
    out.push({ a, b, diff: a * a - 2 * b * b });
  }
  return out;
}

export function smallestFactor(n) {
  for (let d = 2; d * d <= n; d++) if (n % d === 0) return d;
  return n;
}
/** Euclid: giả sử p₁…p_k là mọi số nguyên tố. */
export function euclidStep(primes) {
  const N = primes.reduce((a, b) => a * b, 1) + 1;
  const q = smallestFactor(N);
  return { N, q, remainders: primes.map((p) => ({ p, r: N % p })), isNew: !primes.includes(q), qIsPrime: smallestFactor(q) === q };
}
export const isPrimeNum = (n) => Number.isInteger(n) && n >= 2 && smallestFactor(n) === n;
