// Bộ cộng lan truyền mang (ripple-carry) n bit, có chế độ trừ (bù hai).

export const fullAdder = (a, b, c) => {
  const x1 = a ^ b;
  return { x1, sum: x1 ^ c, a1: a & b, a2: c & x1, cout: (a & b) | (c & x1) };
};

/** a, b: số nguyên 0…2ⁿ−1. sub=true: tính a − b = a + ~b + 1. Trả về mỗi tầng + kết quả. */
export function rippleSteps(a, b, n = 4, sub = false) {
  const mask = (1 << n) - 1;
  a &= mask; b &= mask;
  let c = sub ? 1 : 0;
  const stages = [];
  for (let i = 0; i < n; i++) {
    const ai = (a >> i) & 1, bi = (((b >> i) & 1) ^ (sub ? 1 : 0));
    const fa = fullAdder(ai, bi, c);
    stages.push({ i, a: ai, b: bi, bRaw: (b >> i) & 1, cin: c, ...fa });
    c = fa.cout;
  }
  const result = stages.reduce((r, s) => r | (s.sum << s.i), 0);
  const cinMsb = n > 1 ? stages[n - 2].cout : (sub ? 1 : 0);
  const signed = (result >> (n - 1)) & 1 ? result - (1 << n) : result;
  return { stages, result, cout: c, overflow: (cinMsb ^ c) === 1, signed, delay: 2 * n + 1 };
}
