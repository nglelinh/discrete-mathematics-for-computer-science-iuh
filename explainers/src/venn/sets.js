/** Biểu thức tập hợp trên A, B, C: phân tích, tính theo vùng Venn, phần tử, bao hàm–loại trừ. */

const NAMES = ['A', 'B', 'C'];

export function tokenize(src) {
  const s = String(src).trim();
  if (!s) throw new Error('Nhập một biểu thức tập hợp, ví dụ (A ∪ B)′ hoặc A ∩ B′.');
  const out = [];
  for (const ch of s) {
    if (/\s/.test(ch)) continue;
    if ('ABCU∅(){}'.includes(ch) || 'abc'.includes(ch)) out.push(ch.toUpperCase());
    else if ('∪|+'.includes(ch)) out.push('∪');
    else if ('∩&*'.includes(ch)) out.push('∩');
    else if ('\\−-'.includes(ch)) out.push('\\');
    else if ('Δ⊕^'.includes(ch)) out.push('Δ');
    else if ("'′ᶜ".includes(ch)) out.push("'");
    else if ('¬~!'.includes(ch)) out.push('¬');
    else throw new Error(`Không hiểu ký hiệu «${ch}». Dùng A, B, C, U, ∅, ∪, ∩, \\, Δ, ′ (bù), ¬.`);
  }
  return out;
}

export function parseSet(src) {
  const t = tokenize(src);
  let i = 0;
  const peek = () => t[i];
  function expr() {
    let l = term();
    while (['∪', 'Δ', '\\'].includes(peek())) {
      const op = t[i++];
      const r = term();
      l = { t: op === '∪' ? 'or' : op === 'Δ' ? 'xor' : 'diff', l, r };
    }
    return l;
  }
  function term() {
    let l = factor();
    while (peek() === '∩') {
      i++;
      l = { t: 'and', l, r: factor() };
    }
    return l;
  }
  function factor() {
    if (peek() === '¬') {
      i++;
      return { t: 'not', a: factor() };
    }
    let a = atom();
    while (peek() === "'") {
      i++;
      a = { t: 'not', a };
    }
    return a;
  }
  function atom() {
    const x = t[i++];
    if (x === undefined) throw new Error('Biểu thức chưa hoàn chỉnh.');
    if (x === '(') {
      const e = expr();
      if (t[i++] !== ')') throw new Error('Thiếu dấu đóng ngoặc ).');
      return e;
    }
    if (x === 'A' || x === 'B' || x === 'C') return { t: 'var', i: NAMES.indexOf(x) };
    if (x === 'U') return { t: 'U' };
    if (x === '∅') return { t: 'E' };
    throw new Error(`Không mong đợi «${x}».`);
  }
  const ast = expr();
  if (i < t.length) throw new Error(`Thừa «${t[i]}» ở cuối biểu thức.`);
  return ast;
}

/** mask: bit i = thuộc tập thứ i (A=bit0, B=bit1, C=bit2). */
export function evalSet(ast, mask) {
  switch (ast.t) {
    case 'var': return ((mask >> ast.i) & 1) === 1;
    case 'U': return true;
    case 'E': return false;
    case 'not': return !evalSet(ast.a, mask);
    case 'and': return evalSet(ast.l, mask) && evalSet(ast.r, mask);
    case 'or': return evalSet(ast.l, mask) || evalSet(ast.r, mask);
    case 'diff': return evalSet(ast.l, mask) && !evalSet(ast.r, mask);
    case 'xor': return evalSet(ast.l, mask) !== evalSet(ast.r, mask);
    default: return false;
  }
}

export function regionTable(ast, k) {
  const out = [];
  for (let m = 0; m < 1 << k; m++) out.push(evalSet(ast, m));
  return out;
}

/** Chuỗi mô tả một vùng: mask → "A ∩ B′ ∩ C". */
export function regionLabel(mask, k) {
  const parts = [];
  for (let i = 0; i < k; i++) parts.push(((mask >> i) & 1 ? '' : '') + NAMES[i] + ((mask >> i) & 1 ? '' : '′'));
  return parts.join(' ∩ ');
}

/** Hợp các vùng được chọn → biểu thức (dạng "tổng các vùng"). */
export function unionOfRegions(sel, k) {
  const ms = sel.map((v, m) => (v ? m : -1)).filter((m) => m >= 0);
  if (!ms.length) return '∅';
  if (ms.length === 1 << k) return 'U';
  return ms.map((m) => (k > 1 ? '(' + regionLabel(m, k) + ')' : regionLabel(m, k))).join(' ∪ ');
}

export function parseElements(text) {
  const s = String(text).trim();
  if (!s) return [];
  const out = [];
  for (const part of s.split(/[,;\s]+/).filter(Boolean)) {
    const r = part.match(/^(-?\d+)\.\.(-?\d+)$/);
    if (r) {
      const a = Number(r[1]);
      const b = Number(r[2]);
      if (b - a > 60) throw new Error('Khoảng quá lớn (tối đa 60 phần tử).');
      for (let x = a; x <= b; x++) out.push(String(x));
    } else out.push(part);
  }
  return [...new Set(out)];
}

/** Tính tập kết quả: trả về { universe, sets:[...], mask(e), result }. */
export function evaluateOnElements(ast, k, universe, sets) {
  const mask = (e) => sets.reduce((m, s, i) => m | (s.includes(e) ? 1 << i : 0), 0);
  const result = universe.filter((e) => evalSet(ast, mask(e)));
  return { mask, result };
}

export function sameSetFamily(a, b, k) {
  const ta = regionTable(a, k);
  const tb = regionTable(b, k);
  const diff = [];
  for (let m = 0; m < ta.length; m++) if (ta[m] !== tb[m]) diff.push(m);
  return { equal: diff.length === 0, diff };
}

const inter = (...xs) => xs.reduce((a, b) => a.filter((e) => b.includes(e)));
const uni = (...xs) => [...new Set(xs.flat())];

/** Nguyên lý bao hàm–loại trừ: trả về các số hạng và tổng. */
export function inclusionExclusion(sets) {
  const k = sets.length;
  const terms = [];
  for (let m = 1; m < 1 << k; m++) {
    const idx = [];
    for (let i = 0; i < k; i++) if ((m >> i) & 1) idx.push(i);
    const size = inter(...idx.map((i) => sets[i])).length;
    terms.push({
      label: idx.length === 1 ? `|${NAMES[idx[0]]}|` : '|' + idx.map((i) => NAMES[i]).join(' ∩ ') + '|',
      sign: idx.length % 2 ? 1 : -1,
      size
    });
  }
  const total = terms.reduce((s, t) => s + t.sign * t.size, 0);
  return { terms, total, actual: uni(...sets).length };
}

export const IDENTITIES = [
  { label: 'De Morgan: (A ∪ B)′ = A′ ∩ B′', k: 2, a: "(A ∪ B)'", b: "A' ∩ B'" },
  { label: 'De Morgan: (A ∩ B)′ = A′ ∪ B′', k: 2, a: "(A ∩ B)'", b: "A' ∪ B'" },
  { label: 'Hiệu: A \\ B = A ∩ B′', k: 2, a: 'A \\ B', b: "A ∩ B'" },
  { label: 'Phân phối: A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)', k: 3, a: 'A ∩ (B ∪ C)', b: '(A ∩ B) ∪ (A ∩ C)' },
  { label: 'Hấp thụ: A ∪ (A ∩ B) = A', k: 2, a: 'A ∪ (A ∩ B)', b: 'A' },
  { label: 'Hiệu đối xứng: A Δ B = (A ∪ B) \\ (A ∩ B)', k: 2, a: 'A Δ B', b: '(A ∪ B) \\ (A ∩ B)' },
  { label: 'Sai thường gặp: (A ∪ B)′ ≠ A′ ∪ B′', k: 2, a: "(A ∪ B)'", b: "A' ∪ B'" }
];
