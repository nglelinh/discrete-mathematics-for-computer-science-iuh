/** Phần mở rộng: don't-care, POS/CNF, so sánh hai biểu thức, danh sách dạng chuẩn. */
import {
  VAR_NAMES,
  collectVars,
  evalAst,
  primeImplicants,
  essentialCover,
  bitstr,
  GROUP_COLORS,
  implicantRects,
  termLabel
} from './logic.js';

export const DC = 2; // giá trị "không quan tâm" (don't care)

export function resolveVars(n, asts) {
  const used = new Set();
  for (const a of asts) if (a) collectVars(a, used);
  if (used.size > n) {
    throw new Error(
      `Biểu thức dùng ${used.size} biến (${[...used].sort().join(', ')}) nhưng đang chọn ${n} biến — tăng số biến hoặc rút gọn biểu thức.`
    );
  }
  const names = new Set(used);
  for (const v of VAR_NAMES) {
    if (names.size >= n) break;
    names.add(v);
  }
  const canon = (v) => VAR_NAMES.indexOf(v);
  return [...names].sort((a, b) => {
    const ca = canon(a);
    const cb = canon(b);
    if (ca >= 0 && cb >= 0) return ca - cb;
    if (ca >= 0) return -1;
    if (cb >= 0) return 1;
    return a < b ? -1 : 1;
  });
}

export function valuesFor(n, ast, names) {
  const out = [];
  for (let m = 0; m < 1 << n; m++) {
    const env = {};
    for (let i = 0; i < n; i++) env[names[i]] = (m >> (n - 1 - i)) & 1;
    out.push(ast ? evalAst(ast, env) : 0);
  }
  return out;
}

export function assignOf(m, n) {
  const a = [];
  for (let i = 0; i < n; i++) a.push((m >> (n - 1 - i)) & 1);
  return a;
}

export function envOf(m, names) {
  const env = {};
  const n = names.length;
  for (let i = 0; i < n; i++) env[names[i]] = (m >> (n - 1 - i)) & 1;
  return env;
}

/** Tối tiểu hóa: kind='sop' phủ các ô 1; kind='pos' phủ các ô 0. Ô DC dùng tự do. */
export function minimize(values, n, kind = 'sop') {
  const target = kind === 'sop' ? 1 : 0;
  const must = [];
  const dc = [];
  values.forEach((v, i) => {
    if (v === target) must.push(i);
    else if (v === DC) dc.push(i);
  });
  const primes = primeImplicants([...must, ...dc], n);
  const cover = must.length ? essentialCover(primes, must) : [];
  return { kind, must, dc, primes, cover };
}

export function clauseLabel(bits, names) {
  const parts = [];
  for (let i = 0; i < bits.length; i++) {
    if (bits[i] === '0') parts.push(names[i]);
    else if (bits[i] === '1') parts.push('¬' + names[i]);
  }
  return parts.length ? parts.join(' ∨ ') : '0';
}

export function posLabel(groups, names) {
  if (!groups.length) return '1';
  const cl = groups.map((g) => clauseLabel(g.bits, names));
  if (cl.length === 1) return cl[0];
  return cl.map((c) => (c.includes('∨') ? `(${c})` : c)).join(' ∧ ');
}

export function sopText(groups, names) {
  if (!groups.length) return '0';
  const t = groups.map((g) => termLabel(g.bits, names));
  if (t.length === 1) return t[0];
  return t.map((x) => (x.includes('∧') ? `(${x})` : x)).join(' ∨ ');
}

/** Giá trị hàm tối tiểu tại ô m (dùng để kiểm thử). */
export function coverValue(min, m) {
  const hit = min.cover.some((g) => g.covered.has(m));
  return min.kind === 'sop' ? (hit ? 1 : 0) : hit ? 0 : 1;
}

export function groupsFor(min, names, n) {
  return min.cover.map((g, i) => ({
    bits: g.bits,
    covered: g.covered,
    color: GROUP_COLORS[i % GROUP_COLORS.length],
    label: min.kind === 'sop' ? termLabel(g.bits, names) : clauseLabel(g.bits, names),
    rects: implicantRects(g.bits, n)
  }));
}

export function canonicalForms(values, names) {
  const n = names.length;
  const ones = [];
  const zeros = [];
  const dcs = [];
  values.forEach((v, i) => (v === DC ? dcs : v ? ones : zeros).push(i));
  const lit = (i, neg) => (neg ? '¬' : '') + names[i];
  const minterm = (m) =>
    bitstr(m, n)
      .split('')
      .map((b, i) => lit(i, b === '0'))
      .join('');
  const maxterm = (m) =>
    '(' +
    bitstr(m, n)
      .split('')
      .map((b, i) => lit(i, b === '1'))
      .join(' ∨ ') +
    ')';
  const list = (a) => a.join(', ');
  return {
    ones,
    zeros,
    dcs,
    sigma: `Σm(${list(ones)})` + (dcs.length ? ` + d(${list(dcs)})` : ''),
    pi: `ΠM(${list(zeros)})` + (dcs.length ? ` · d(${list(dcs)})` : ''),
    dnf: ones.length ? ones.map(minterm).join(' ∨ ') : '0',
    cnf: zeros.length ? zeros.map(maxterm).join(' ∧ ') : '1'
  };
}

export function compareValues(a, b) {
  const diff = [];
  for (let i = 0; i < a.length; i++) if ((a[i] ? 1 : 0) !== (b[i] ? 1 : 0)) diff.push(i);
  const aImpB = a.every((v, i) => !v || b[i]);
  const bImpA = b.every((v, i) => !v || a[i]);
  return { equivalent: diff.length === 0, diff, aImpB, bImpA };
}
