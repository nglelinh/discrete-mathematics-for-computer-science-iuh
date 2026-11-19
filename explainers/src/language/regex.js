// Regex → ε-NFA (Thompson) và DFA/NFA → regex (loại trạng thái).
import { PRESETS, accepts, EPS } from '../automata/automata.js';

export function parseRegex(src) {
  const s = String(src).replace(/\s+/g, '');
  let i = 0;
  const fail = (m) => { throw new Error(m); };
  function alt() {
    let a = cat();
    while (s[i] === '|') { i++; a = { t: 'alt', a, b: cat() }; }
    return a;
  }
  function cat() {
    let parts = [];
    while (i < s.length && s[i] !== '|' && s[i] !== ')') parts.push(rep());
    if (!parts.length) return { t: 'eps' };
    return parts.reduce((a, b) => ({ t: 'cat', a, b }));
  }
  function rep() {
    let a = atom();
    while (s[i] === '*' || s[i] === '+' || s[i] === '?') {
      const op = s[i++];
      a = op === '*' ? { t: 'star', a } : op === '+' ? { t: 'cat', a, b: { t: 'star', a: structuredClone(a) }, plus: true } : { t: 'alt', a, b: { t: 'eps' }, opt: true };
    }
    return a;
  }
  function atom() {
    const c = s[i];
    if (c === '(') { i++; const a = alt(); if (s[i] !== ')') fail('Thiếu dấu “)”.'); i++; return a; }
    if (c === 'ε') { i++; return { t: 'eps' }; }
    if (c && /[A-Za-z0-9]/.test(c)) { i++; return { t: 'chr', c }; }
    return fail(c ? `Ký tự “${c}” không hợp lệ (dùng chữ/số, | * + ? và ngoặc).` : 'Biểu thức chưa đầy đủ.');
  }
  if (!s) fail('Nhập một biểu thức chính quy.');
  const ast = alt();
  if (i < s.length) fail(`Thừa “${s[i]}” ở vị trí ${i + 1}.`);
  return ast;
}

export const showRegex = (n) => {
  switch (n.t) {
    case 'chr': return n.c;
    case 'eps': return 'ε';
    case 'cat': return (n.a.t === 'alt' ? '(' + showRegex(n.a) + ')' : showRegex(n.a)) + (n.b.t === 'alt' ? '(' + showRegex(n.b) + ')' : showRegex(n.b));
    case 'alt': return showRegex(n.a) + '|' + showRegex(n.b);
    default: return (n.a.t === 'chr' ? showRegex(n.a) : '(' + showRegex(n.a) + ')') + '*';
  }
};

/** Dựng Thompson, ghi mỗi trạng thái/cạnh mới thuộc bước nào. Trả về machine + steps. */
export function thompson(ast) {
  let nid = 0;
  const states = [], edges = [], steps = [];
  const mk = (born) => { const id = 'q' + nid++; states.push({ id, x: 0, y: 0, born }); return id; };
  const ed = (from, to, sym, born) => edges.push({ from, to, syms: [sym], born });
  function build(n) {
    const born = steps.length;
    let f;
    let desc;
    if (n.t === 'chr' || n.t === 'eps') {
      const a = mk(born), b = mk(born);
      ed(a, b, n.t === 'chr' ? n.c : EPS, born);
      f = { s: a, e: b };
      desc = n.t === 'chr' ? `Ký tự “${n.c}”: hai trạng thái nối bằng cạnh ${n.c}.` : 'ε: hai trạng thái nối bằng cạnh ε.';
    } else if (n.t === 'cat') {
      const x = build(n.a), y = build(n.b);
      const st = steps.length;
      ed(x.e, y.s, EPS, st);
      f = { s: x.s, e: y.e };
      desc = `Nối tiếp “${showRegex(n)}”: đuôi của vế trái nối ε vào đầu vế phải.`;
    } else if (n.t === 'alt') {
      const x = build(n.a), y = build(n.b);
      const st = steps.length;
      const s = mk(st), e = mk(st);
      ed(s, x.s, EPS, st); ed(s, y.s, EPS, st); ed(x.e, e, EPS, st); ed(y.e, e, EPS, st);
      f = { s, e };
      desc = `Hợp “${showRegex(n)}”: trạng thái đầu mới rẽ ε vào hai nhánh, hai nhánh cùng nối ε về trạng thái cuối mới.`;
    } else {
      const x = build(n.a);
      const st = steps.length;
      const s = mk(st), e = mk(st);
      ed(s, x.s, EPS, st); ed(x.e, e, EPS, st); ed(s, e, EPS, st); ed(x.e, x.s, EPS, st);
      f = { s, e };
      desc = `Bao đóng sao “${showRegex(n)}”: thêm cạnh ε bỏ qua (s→e) và lặp lại (cuối→đầu).`;
    }
    steps.push({ node: showRegex(n), desc });
    return f;
  }
  const f = build(ast);
  // đánh số lại: bước của cạnh nối thêm bằng chỉ số bước vừa tạo (steps.length-1 thuộc node gốc của khối)
  for (const x of [...states, ...edges]) x.born = Math.min(x.born, steps.length - 1);
  // bố cục theo lớp BFS (bỏ qua cạnh quay lui)
  const layer = { [f.s]: 0 };
  const q = [f.s];
  while (q.length) {
    const u = q.shift();
    for (const e of edges) if (e.from === u && layer[e.to] === undefined) { layer[e.to] = layer[u] + 1; q.push(e.to); }
  }
  const byLayer = {};
  states.forEach((s) => { const L = layer[s.id] ?? 0; (byLayer[L] ||= []).push(s); });
  const L = Math.max(...Object.keys(byLayer).map(Number));
  states.forEach((s) => {
    const col = byLayer[layer[s.id] ?? 0];
    s.x = 50 + (layer[s.id] ?? 0) * 78;
    s.y = 100 + (col.indexOf(s) - (col.length - 1) / 2) * 62;
  });
  const minY = Math.min(...states.map((s) => s.y));
  states.forEach((s) => { s.y += 40 - minY + 30; });
  return { machine: { states, start: f.s, accept: [f.e], edges }, steps, width: 50 + L * 78 + 70, height: Math.max(...states.map((s) => s.y)) + 50 };
}

export const machineAt = (T, k) => {
  const states = T.machine.states.filter((s) => s.born <= k);
  const ids = new Set(states.map((s) => s.id));
  return { states, start: T.machine.start, accept: T.machine.accept, edges: T.machine.edges.filter((e) => e.born <= k && ids.has(e.from) && ids.has(e.to)) };
};

// ---------------- loại trạng thái ----------------
const isAtom = (x) => /^[A-Za-z0-9ε]$/.test(x) || (x.startsWith('(') && matchParen(x) === x.length - 1);
function matchParen(x) { let d = 0; for (let i = 0; i < x.length; i++) { if (x[i] === '(') d++; else if (x[i] === ')') { d--; if (d === 0) return i; } } return -1; }
const hasTopAlt = (x) => { let d = 0; for (const c of x) { if (c === '(') d++; else if (c === ')') d--; else if (c === '|' && d === 0) return true; } return false; };
const wrap = (x) => (hasTopAlt(x) ? '(' + x + ')' : x);
const atom = (x) => (isAtom(x) ? x : '(' + x + ')');
const U = (a, b) => {
  if (a === null) return b; if (b === null) return a; if (a === b) return a;
  if (a === 'ε') return b === 'ε' ? 'ε' : atom(b) + '?';
  if (b === 'ε') return atom(a) + '?';
  return a + '|' + b;
};
const C = (a, b) => (a === null || b === null ? null : a === 'ε' ? b : b === 'ε' ? a : wrap(a) + wrap(b));
const S = (a) => (a === null || a === 'ε' ? 'ε' : atom(a) + '*');

export function eliminationSteps(M, order) {
  const ids = ['S', ...M.states.map((s) => s.id), 'F'];
  const lab = {};
  const get = (a, b) => lab[a + '>' + b] ?? null;
  const set = (a, b, v) => { if (v === null) delete lab[a + '>' + b]; else lab[a + '>' + b] = v; };
  set('S', M.start, 'ε');
  for (const a of M.accept) set(a, 'F', U(get(a, 'F'), 'ε'));
  for (const e of M.edges) for (const s of e.syms) if (s !== EPS) set(e.from, e.to, U(get(e.from, e.to), s));
    else set(e.from, e.to, U(get(e.from, e.to), 'ε'));
  let alive = [...ids];
  const snapshot = () => ({ alive: [...alive], labels: { ...lab } });
  const steps = [{ ...snapshot(), removed: null, msg: 'Thêm trạng thái đầu mới S (nối ε vào trạng thái đầu cũ) và trạng thái cuối mới F (nối ε từ các trạng thái nhận). Mỗi cạnh mang một biểu thức chính quy. Lần lượt loại các trạng thái ban đầu.' }];
  for (const q of order) {
    const others = alive.filter((x) => x !== q);
    const loop = S(get(q, q));
    const notes = [];
    for (const i of others) for (const j of others) {
      const inn = get(i, q), out = get(q, j);
      if (inn === null || out === null) continue;
      const via = C(C(inn, loop), out);
      const before = get(i, j);
      set(i, j, U(before, via));
      notes.push(`${i}→${j}: ${before ?? '∅'} ∪ ${inn}${loop === 'ε' ? '' : ' ' + loop}${' ' + out} = ${get(i, j)}`);
    }
    for (const x of others) { set(x, q, null); set(q, x, null); }
    set(q, q, null);
    alive = others;
    steps.push({ ...snapshot(), removed: q, msg: `Loại ${q}. ` + (notes.length ? 'Thay mọi đường đi qua nó: ' + notes.join('; ') + '.' : 'Không có đường đi nào qua nó.') });
  }
  const regex = get('S', 'F');
  steps.push({ ...snapshot(), removed: null, done: true, regex, msg: regex === null ? 'Không còn đường từ S tới F: ngôn ngữ rỗng (∅).' : `Chỉ còn S → F, nhãn là biểu thức chính quy: ${regex}` });
  return { steps, regex };
}

export function toJsRegExp(r) { return new RegExp('^(?:' + (r === null ? '[^\\s\\S]' : r.replace(/ε/g, '(?:)')) + ')$'); }

export const REGEX_PRESETS = [
  { id: 'abb', name: '(a|b)*abb', text: '(a|b)*abb' },
  { id: 'ab', name: 'a*b*', text: 'a*b*' },
  { id: 'opt', name: 'a(b|c)+d?', text: 'a(b|c)+d?' },
  { id: 'ones', name: '(0|1)*1(0|1)', text: '(0|1)*1(0|1)' }
];
export const ELIM_PRESETS = PRESETS.filter((p) => ['dfa01', 'even1', 'nfa101'].includes(p.id));
export { accepts };
