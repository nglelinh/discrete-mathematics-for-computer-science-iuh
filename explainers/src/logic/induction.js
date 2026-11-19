// Quy nạp toán học: hiệu ứng domino. Mọi kiểm tra dùng BigInt nên chính xác.

const sumTo = (n) => (n * (n + 1n)) / 2n;
const isPrime = (x) => { if (x < 2n) return false; for (let d = 2n; d * d <= x; d++) if (x % d === 0n) return false; return true; };

export const INDUCTION_PRESETS = [
  {
    id: 'sum', name: '1 + 2 + … + n = n(n+1)/2', n0: 1, count: 12, valid: true,
    holds: (n) => { let s = 0n; for (let i = 1n; i <= n; i++) s += i; return s === sumTo(n); },
    show: (n) => `1+…+${n} = ${sumTo(n)} và ${n}·${n + 1n}/2 = ${sumTo(n)}`,
    base: 'P(1): 1 = 1·2/2 = 1 ✓',
    step: 'Giả sử P(k): 1+…+k = k(k+1)/2. Cộng (k+1) vào hai vế: k(k+1)/2 + (k+1) = (k+1)(k+2)/2, đúng là P(k+1) ✓'
  },
  {
    id: 'pow2', name: '2ⁿ > n', n0: 1, count: 12, valid: true,
    holds: (n) => 2n ** n > n,
    show: (n) => `2^${n} = ${2n ** n} > ${n}`,
    base: 'P(1): 2¹ = 2 > 1 ✓',
    step: 'Giả sử 2ᵏ > k. Khi đó 2ᵏ⁺¹ = 2·2ᵏ > 2k ≥ k + 1 (vì k ≥ 1), tức P(k+1) ✓'
  },
  {
    id: 'div3', name: 'n³ − n chia hết cho 3', n0: 1, count: 12, valid: true,
    holds: (n) => (n ** 3n - n) % 3n === 0n,
    show: (n) => `${n}³ − ${n} = ${n ** 3n - n} = 3·${(n ** 3n - n) / 3n}`,
    base: 'P(1): 1³ − 1 = 0 = 3·0 ✓',
    step: '(k+1)³ − (k+1) = (k³ − k) + 3(k² + k). Số hạng đầu chia hết cho 3 (giả thiết quy nạp), số hạng sau là bội của 3 ⇒ P(k+1) ✓'
  },
  {
    id: 'nobase', name: 'Thiếu bước cơ sở: n = n + 1', n0: 1, count: 8, valid: false,
    holds: (n) => n === n + 1n,
    show: (n) => `${n} = ${n + 1n}?`,
    base: 'P(1): 1 = 2? ✗ SAI — cơ sở không đúng',
    step: 'Giả sử k = k + 1. Cộng 1 hai vế: k + 1 = k + 2 ✓. Bước quy nạp “đúng” nhưng vô nghĩa vì không có domino nào được đẩy.'
  },
  {
    id: 'prime', name: 'Kiểm tra nhiều trường hợp ≠ chứng minh: n² + n + 41 nguyên tố', n0: 0, count: 42, valid: false,
    holds: (n) => isPrime(n * n + n + 41n),
    show: (n) => `${n}² + ${n} + 41 = ${n * n + n + 41n}${isPrime(n * n + n + 41n) ? ' nguyên tố' : ' = hợp số'}`,
    base: 'P(0): 41 là số nguyên tố ✓ (cơ sở đúng)',
    step: 'Không có lập luận nào chứng minh được P(k) ⇒ P(k+1). Ta chỉ thử từng n: đúng với n = 0…39 nhưng không có “bước quy nạp” nên sớm muộn sẽ gãy.'
  }
];

/** Trả về các bước { phase, fallen, bad, msg }; fallen = số domino đã đổ, bad = domino sai (n). */
export function inductionSteps(preset, count = preset.count) {
  const n0 = BigInt(preset.n0);
  const steps = [];
  steps.push({ phase: 'intro', fallen: 0, bad: null, msg: `Mệnh đề P(n): ${preset.name}. Mỗi domino là một giá trị n. Quy nạp cần hai điều: (1) cơ sở: domino đầu bị đẩy; (2) bước quy nạp: domino k đổ thì domino k+1 đổ.` });
  const baseOK = preset.holds(n0);
  steps.push({ phase: 'base', fallen: baseOK ? 1 : 0, bad: baseOK ? null : preset.n0, msg: 'Bước cơ sở. ' + preset.base });
  steps.push({ phase: 'step', fallen: baseOK ? 1 : 0, bad: baseOK ? null : preset.n0, msg: 'Bước quy nạp. ' + preset.step });
  if (!baseOK) {
    steps.push({ phase: 'end', fallen: 0, bad: preset.n0, msg: 'Không có cơ sở thì chuỗi domino không bao giờ bắt đầu: bước quy nạp một mình không chứng minh được gì.' });
    return steps;
  }
  for (let i = 1; i < count; i++) {
    const n = n0 + BigInt(i);
    if (preset.holds(n)) steps.push({ phase: 'fall', fallen: i + 1, bad: null, msg: `Domino ${n - 1n} đổ ⇒ domino ${n} đổ. Kiểm tra: ${preset.show(n)} ✓` });
    else {
      steps.push({ phase: 'end', fallen: i, bad: Number(n), msg: `Domino ${n} KHÔNG đổ: ${preset.show(n)} ✗. Phản ví dụ! Thử đúng với mọi n nhỏ vẫn chưa phải là chứng minh.` });
      return steps;
    }
  }
  steps.push({ phase: 'end', fallen: count, bad: null, msg: preset.valid ? `Đã kiểm ${count} domino đầu, nhưng quan trọng hơn: cơ sở + bước quy nạp đảm bảo MỌI n ≥ ${preset.n0} đều đúng.` : 'Hết số domino hiển thị.' });
  return steps;
}
