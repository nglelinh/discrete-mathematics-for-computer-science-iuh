// Chứng minh vị từ từng dòng, kiểm tra ngữ nghĩa trên mọi mô hình hữu hạn (≤ 3 phần tử).
// Mô hình m = { n, P: bool[], Q: bool[], c, d } — c, d là hai hằng; P, Q là hai vị từ.
const f = {
  allPQ: (m) => m.P.every((p, i) => !p || m.Q[i]),
  exP: (m) => m.P.some(Boolean), exQ: (m) => m.Q.some(Boolean), exPQ: (m) => m.P.some((p, i) => p && m.Q[i]), allP: (m) => m.P.every(Boolean),
  Pc: (m) => m.P[m.c], Qc: (m) => m.Q[m.c], Qd: (m) => m.Q[m.d], PcQc: (m) => !m.P[m.c] || m.Q[m.c], PcAndQc: (m) => m.P[m.c] && m.Q[m.c], PcAndQd: (m) => m.P[m.c] && m.Q[m.d]
};
export const PROOFS = [
  { id: 'socrates', name: 'Socrates: UI rồi MP', valid: true, note: 'P(x) = “x là người”, Q(x) = “x phải chết”, c = Socrates.',
    lines: [
      { t: '∀x (P(x) → Q(x))', rule: 'Tiền đề', f: f.allPQ, premise: true },
      { t: 'P(c)', rule: 'Tiền đề', f: f.Pc, premise: true },
      { t: 'P(c) → Q(c)', rule: 'UI từ dòng 1 (thay x bằng hằng c)', f: f.PcQc, ok: true },
      { t: 'Q(c)', rule: 'Modus ponens: dòng 2, 3', f: f.Qc, ok: true }],
    conclusion: f.Qc },
  { id: 'exists', name: 'Có người đạt P thì có người đạt Q: EI, UI, MP, EG', valid: true, note: 'Từ “mọi P đều Q” và “có P” suy ra “có Q”.',
    lines: [
      { t: '∀x (P(x) → Q(x))', rule: 'Tiền đề', f: f.allPQ, premise: true },
      { t: '∃x P(x)', rule: 'Tiền đề', f: f.exP, premise: true },
      { t: 'P(c)', rule: 'EI từ dòng 2: c là tên MỚI, chưa dùng ở dòng nào', f: f.Pc, ei: true, ok: true },
      { t: 'P(c) → Q(c)', rule: 'UI từ dòng 1 (thay x bằng c)', f: f.PcQc, ok: true },
      { t: 'Q(c)', rule: 'Modus ponens: dòng 3, 4', f: f.Qc, ok: true },
      { t: '∃x Q(x)', rule: 'EG từ dòng 5', f: f.exQ, ok: true }],
    conclusion: f.exQ },
  { id: 'ei-twice', name: 'LỖI: dùng lại tên c cho hai lần EI', valid: false, note: '“Có P” và “có Q” không có nghĩa là một phần tử vừa P vừa Q.',
    lines: [
      { t: '∃x P(x)', rule: 'Tiền đề', f: f.exP, premise: true },
      { t: '∃x Q(x)', rule: 'Tiền đề', f: f.exQ, premise: true },
      { t: 'P(c)', rule: 'EI từ dòng 1: c là tên mới', f: f.Pc, ei: true, ok: true },
      { t: 'Q(c)', rule: 'EI từ dòng 2', f: f.Qc, ei: true, ok: false, why: 'c đã được dùng ở dòng 3, phải chọn tên mới d. Hai phần tử chứng kiến chưa chắc là một.' },
      { t: 'P(c) ∧ Q(c)', rule: 'Hội: dòng 3, 4', f: f.PcAndQc, ok: true },
      { t: '∃x (P(x) ∧ Q(x))', rule: 'EG từ dòng 5', f: f.exPQ, ok: true }],
    conclusion: f.exPQ },
  { id: 'ug-bad', name: 'LỖI: tổng quát hóa từ một hằng cụ thể (UG sai)', valid: false, note: 'UG chỉ dùng được khi c là phần tử TÙY Ý, không phải một phần tử đã chọn.',
    lines: [
      { t: 'P(c)', rule: 'Tiền đề (c là một phần tử cụ thể)', f: f.Pc, premise: true },
      { t: '∀x P(x)', rule: 'UG từ dòng 1', f: f.allP, ok: false, why: 'c xuất hiện trong tiền đề nên không còn tùy ý; một phần tử có P chưa nói gì về mọi phần tử.' }],
    conclusion: f.allP }
];

export function* models(maxN = 3) {
  for (let n = 1; n <= maxN; n++) for (let pm = 0; pm < 1 << n; pm++) for (let qm = 0; qm < 1 << n; qm++) for (let c = 0; c < n; c++) for (let d = 0; d < n; d++)
    yield { n, P: Array.from({ length: n }, (_, i) => !!(pm >> i & 1)), Q: Array.from({ length: n }, (_, i) => !!(qm >> i & 1)), c, d };
}
/** Mô hình thỏa mọi tiền đề mà kết luận sai; null nếu không có. */
export function counterexample(proof) {
  const prem = proof.lines.filter((l) => l.premise);
  for (const m of models()) if (prem.every((l) => l.f(m)) && !proof.conclusion(m)) return m;
  return null;
}
export function countModels(proof) {
  const prem = proof.lines.filter((l) => l.premise); let n = 0;
  for (const m of models()) if (prem.every((l) => l.f(m))) n++;
  return n;
}
/** Với mọi mô hình: tiền đề và các dòng EI (giả định về c) đúng ⇒ mọi dòng đúng. */
export function linesSound(proof) {
  const assume = proof.lines.filter((l) => l.premise || l.ei);
  for (const m of models()) if (assume.every((l) => l.f(m))) for (const l of proof.lines) if (!l.f(m)) return false;
  return true;
}
