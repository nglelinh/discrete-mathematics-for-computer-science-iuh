// Bù hai, cộng có nhớ, thứ tự byte (endianness), Y2038.

export const mask = (n) => (1n << BigInt(n)) - 1n;
export const bitsOf = (u, n) => Array.from({ length: n }, (_, i) => Number((BigInt(u) >> BigInt(n - 1 - i)) & 1n));
export const fromBits = (bits) => bits.reduce((a, b) => (a << 1n) | BigInt(b), 0n);
export const toSigned = (u, n) => { u = BigInt(u) & mask(n); return u >> BigInt(n - 1) ? u - (1n << BigInt(n)) : u; };
export const range = (n) => ({ min: -(1n << BigInt(n - 1)), max: (1n << BigInt(n - 1)) - 1n });
export const fromSigned = (x, n) => BigInt(x) & mask(n);

/** Lấy số đối: 0) gốc, 1) đảo bit, 2) +1. */
export function negateStages(u, n) {
  u = BigInt(u) & mask(n);
  const inv = ~u & mask(n);
  const neg = (inv + 1n) & mask(n);
  return [u, inv, neg];
}

/** Cộng từng bit từ LSB: trả về mảng bước { i, a, b, cin, sum, cout } và kết quả. */
export function addSteps(a, b, n) {
  const A = bitsOf(a, n), B = bitsOf(b, n);
  let c = 0; const out = Array(n).fill(null); const steps = [];
  for (let i = n - 1; i >= 0; i--) {
    const t = A[i] + B[i] + c;
    const st = { pos: n - 1 - i, i, a: A[i], b: B[i], cin: c, sum: t & 1, cout: t >> 1 };
    out[i] = st.sum; c = st.cout; steps.push(st);
  }
  const carryIntoMsb = steps.length > 1 ? steps[steps.length - 2].cout : 0;
  const carryOut = steps[steps.length - 1].cout;
  const result = fromBits(out);
  return { steps, result, overflow: carryIntoMsb !== carryOut, carryOut };
}

export function bytesOf(value, order, width = 4) {
  const v = BigInt(value) & mask(width * 8);
  const be = Array.from({ length: width }, (_, i) => Number((v >> BigInt(8 * (width - 1 - i))) & 255n));
  return order === 'little' ? [...be].reverse() : be;
}
export function valueOfBytes(bytes, order) {
  const be = order === 'little' ? [...bytes].reverse() : bytes;
  return be.reduce((a, b) => (a << 8n) | BigInt(b), 0n);
}

export function y2038(offset) {
  const secs = (1n << 31n) - 1n + BigInt(offset);
  const wrapped = toSigned(secs, 32);
  const d = new Date(Number(wrapped) * 1000);
  const real = new Date(Number(secs) * 1000);
  return { secs, wrapped, wrappedDate: d.toISOString().replace('T', ' ').slice(0, 19) + ' UTC', realDate: real.toISOString().replace('T', ' ').slice(0, 19) + ' UTC' };
}
