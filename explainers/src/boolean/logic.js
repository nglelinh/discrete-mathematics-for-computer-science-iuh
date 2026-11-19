/** Boolean expression parser, truth tables, Quine–McCluskey, and K-map geometry. */

export const VAR_NAMES = ['p', 'q', 'r', 's'];

export const PRESET_EXPR = {
  2: [
    { label: 'p ∧ q', expr: 'p ∧ q' },
    { label: 'p ∨ q', expr: 'p ∨ q' },
    { label: 'p ⊕ q', expr: 'p ⊕ q' },
    { label: 'p → q', expr: 'p → q' },
    { label: '¬p ∨ q', expr: '¬p ∨ q' }
  ],
  3: [
    { label: '(p ∧ q) → r', expr: '(p ∧ q) → r' },
    { label: 'p ∧ q ∧ r', expr: 'p ∧ q ∧ r' },
    { label: 'p ∨ (q ∧ r)', expr: 'p ∨ (q ∧ r)' },
    { label: 'p ⊕ q ⊕ r', expr: 'p ⊕ q ⊕ r' },
    { label: '(p ∨ q) ∧ ¬r', expr: '(p ∨ q) ∧ ¬r' }
  ],
  4: [
    { label: '(p ∧ q) ∨ (¬r ∧ s)', expr: '(p ∧ q) ∨ (¬r ∧ s)' },
    { label: 'p ∧ q ∧ r ∧ s', expr: 'p ∧ q ∧ r ∧ s' },
    { label: '(p ⊕ q) ∧ (r ∨ s)', expr: '(p ⊕ q) ∧ (r ∨ s)' },
    { label: 'p → (q ∧ r ∧ s)', expr: 'p → (q ∧ r ∧ s)' }
  ]
};

const TOKEN = /→|->|=>|↔|<->|<=>|⊕|\^|XOR|xor|∧|\/\\|&&|&|∨|\\\/|\|\||\||¬|~|!|TRUE|FALSE|true|false|[A-Za-z]\w*|[01]|\(|\)/g;

export function tokenize(src) {
  const input = String(src).trim();
  if (!input) throw new Error('Nhập một biểu thức logic.');
  const tokens = [];
  let last = 0;
  for (const m of input.matchAll(TOKEN)) {
    const gap = input.slice(last, m.index).trim();
    if (gap) throw new Error(`Không hiểu «${gap}» trong biểu thức.`);
    tokens.push(m[0]);
    last = m.index + m[0].length;
  }
  const tail = input.slice(last).trim();
  if (tail) throw new Error(`Không hiểu «${tail}» trong biểu thức.`);
  return tokens;
}

function normOp(t) {
  if (!t) return null;
  const u = t.toLowerCase();
  if (t === '→' || t === '->' || t === '=>') return 'IMP';
  if (t === '↔' || t === '<->' || t === '<=>') return 'IFF';
  if (t === '⊕' || t === '^' || u === 'xor') return 'XOR';
  if (t === '∧' || t === '/\\' || t === '&&' || t === '&') return 'AND';
  if (t === '∨' || t === '\\/' || t === '||' || t === '|') return 'OR';
  if (t === '¬' || t === '~' || t === '!') return 'NOT';
  return null;
}

function isIdent(t) {
  return /^[A-Za-z]\w*$/.test(t) && !['true', 'false', 'TRUE', 'FALSE', 'xor', 'XOR'].includes(t);
}

export function parse(src) {
  const tokens = tokenize(src);
  let i = 0;
  function peek() { return tokens[i] || null; }
  function eat() { return tokens[i++] || null; }

  function parseIff() {
    let left = parseImp();
    while (normOp(peek()) === 'IFF') {
      eat();
      left = { type: 'IFF', left, right: parseImp() };
    }
    return left;
  }
  function parseImp() {
    let left = parseOr();
    if (normOp(peek()) === 'IMP') {
      eat();
      left = { type: 'IMP', left, right: parseImp() };
    }
    return left;
  }
  function parseOr() {
    let left = parseXor();
    while (normOp(peek()) === 'OR') {
      eat();
      left = { type: 'OR', left, right: parseXor() };
    }
    return left;
  }
  function parseXor() {
    let left = parseAnd();
    while (normOp(peek()) === 'XOR') {
      eat();
      left = { type: 'XOR', left, right: parseAnd() };
    }
    return left;
  }
  function parseAnd() {
    let left = parseNot();
    while (normOp(peek()) === 'AND') {
      eat();
      left = { type: 'AND', left, right: parseNot() };
    }
    return left;
  }
  function parseNot() {
    if (normOp(peek()) === 'NOT') {
      eat();
      return { type: 'NOT', arg: parseNot() };
    }
    return parseAtom();
  }
  function parseAtom() {
    const t = peek();
    if (!t) throw new Error('Biểu thức chưa hoàn chỉnh.');
    if (t === '(') {
      eat();
      const inner = parseIff();
      if (eat() !== ')') throw new Error('Thiếu dấu đóng ngoặc ).');
      return inner;
    }
    if (t === '1' || t.toLowerCase() === 'true') {
      eat();
      return { type: 'CONST', value: 1 };
    }
    if (t === '0' || t.toLowerCase() === 'false') {
      eat();
      return { type: 'CONST', value: 0 };
    }
    if (isIdent(t)) {
      eat();
      return { type: 'VAR', name: t.toLowerCase() };
    }
    throw new Error(`Không mong đợi «${t}».`);
  }

  const ast = parseIff();
  if (i < tokens.length) throw new Error(`Thừa «${tokens[i]}» ở cuối biểu thức.`);
  return ast;
}

export function collectVars(ast, into = new Set()) {
  if (!ast) return into;
  if (ast.type === 'VAR') into.add(ast.name);
  if (ast.left) collectVars(ast.left, into);
  if (ast.right) collectVars(ast.right, into);
  if (ast.arg) collectVars(ast.arg, into);
  return into;
}

export function evalAst(ast, env) {
  switch (ast.type) {
    case 'CONST':
      return ast.value ? 1 : 0;
    case 'VAR':
      return env[ast.name] ? 1 : 0;
    case 'NOT':
      return evalAst(ast.arg, env) ? 0 : 1;
    case 'AND':
      return evalAst(ast.left, env) & evalAst(ast.right, env);
    case 'OR':
      return evalAst(ast.left, env) | evalAst(ast.right, env);
    case 'XOR':
      return evalAst(ast.left, env) ^ evalAst(ast.right, env);
    case 'IMP':
      return evalAst(ast.left, env) ? evalAst(ast.right, env) : 1;
    case 'IFF':
      return evalAst(ast.left, env) === evalAst(ast.right, env) ? 1 : 0;
    default:
      return 0;
  }
}

export function varsForCount(n, ast) {
  const used = ast ? [...collectVars(ast)] : [];
  const base = VAR_NAMES.slice(0, n);
  const extra = used.filter((v) => !base.includes(v));
  if (extra.length) {
    // Prefer declared names from the expression, in appearance order, padded.
    const names = [...used];
    for (const v of VAR_NAMES) if (!names.includes(v)) names.push(v);
    return names.slice(0, n);
  }
  return base;
}

export function truthTable(n, ast) {
  const vars = varsForCount(n, ast);
  const rows = [];
  const bits = 1 << n;
  for (let m = 0; m < bits; m++) {
    const env = {};
    const assign = [];
    for (let i = 0; i < n; i++) {
      const bit = (m >> (n - 1 - i)) & 1;
      env[vars[i]] = bit;
      assign.push(bit);
    }
    const value = ast ? evalAst(ast, env) : 0;
    rows.push({ minterm: m, assign, value, env });
  }
  return { vars, rows };
}

export function valuesFromAst(n, ast) {
  return truthTable(n, ast).rows.map((r) => r.value);
}

export function mintermsOf(values) {
  const out = [];
  for (let i = 0; i < values.length; i++) if (values[i]) out.push(i);
  return out;
}

export function bitstr(num, width) {
  return num.toString(2).padStart(width, '0');
}

function combineBits(a, b) {
  let diff = 0;
  let out = '';
  for (let i = 0; i < a.length; i++) {
    if (a[i] === b[i]) out += a[i];
    else {
      diff += 1;
      out += '-';
    }
  }
  return diff === 1 ? out : null;
}

function coveredBy(bits) {
  const set = new Set();
  const walk = (i, acc) => {
    if (i === bits.length) {
      set.add(parseInt(acc, 2));
      return;
    }
    if (bits[i] === '-') {
      walk(i + 1, acc + '0');
      walk(i + 1, acc + '1');
    } else walk(i + 1, acc + bits[i]);
  };
  walk(0, '');
  return set;
}

export function primeImplicants(minterms, n) {
  if (!minterms.length) return [];
  let groups = new Map();
  for (const m of minterms) {
    const bits = bitstr(m, n);
    const ones = bits.split('').filter((c) => c === '1').length;
    if (!groups.has(ones)) groups.set(ones, []);
    groups.get(ones).push({ bits, used: false });
  }
  const primes = [];
  const seenPrime = new Set();
  // eslint-disable-next-line no-constant-condition
  while (true) {
    const next = new Map();
    const seen = new Set();
    const keys = [...groups.keys()].sort((a, b) => a - b);
    let combined = false;
    for (const k of keys) {
      const a = groups.get(k) || [];
      const b = groups.get(k + 1) || [];
      for (const x of a) {
        for (const y of b) {
          const c = combineBits(x.bits, y.bits);
          if (!c) continue;
          x.used = y.used = true;
          combined = true;
          if (seen.has(c)) continue;
          seen.add(c);
          const ones = c.split('').filter((ch) => ch === '1').length;
          if (!next.has(ones)) next.set(ones, []);
          next.get(ones).push({ bits: c, used: false });
        }
      }
    }
    for (const list of groups.values()) {
      for (const t of list) {
        if (!t.used && !seenPrime.has(t.bits)) {
          seenPrime.add(t.bits);
          primes.push({ bits: t.bits, covered: coveredBy(t.bits) });
        }
      }
    }
    if (!combined) break;
    groups = next;
  }
  return primes;
}

export function essentialCover(primes, minterms) {
  const leftover = new Set(minterms);
  const chosen = [];
  const remaining = () => primes.filter((p) => !chosen.includes(p));
  let guard = 64;
  while (leftover.size && guard--) {
    let picked = null;
    for (const m of leftover) {
      const who = remaining().filter((p) => p.covered.has(m));
      if (who.length === 1) {
        picked = who[0];
        break;
      }
    }
    if (!picked) {
      let bestN = -1;
      for (const p of remaining()) {
        const n = [...p.covered].filter((m) => leftover.has(m)).length;
        if (n > bestN) {
          bestN = n;
          picked = p;
        }
      }
    }
    if (!picked || [...picked.covered].every((m) => !leftover.has(m))) break;
    chosen.push(picked);
    for (const m of picked.covered) leftover.delete(m);
  }
  return chosen;
}

export function termLabel(bits, vars) {
  const parts = [];
  for (let i = 0; i < bits.length; i++) {
    if (bits[i] === '0') parts.push('¬' + vars[i]);
    else if (bits[i] === '1') parts.push(vars[i]);
  }
  return parts.length ? parts.join(' ∧ ') : '1';
}

export function sopLabel(groups, vars) {
  if (!groups.length) return '0';
  const terms = groups.map((g) => termLabel(g.bits, vars));
  if (terms.length === 1) return terms[0];
  return terms.map((t) => (t.includes('∧') ? `(${t})` : t)).join(' ∨ ');
}

export function grayCode(n) {
  const out = [];
  const N = 1 << n;
  for (let i = 0; i < N; i++) out.push(i ^ (i >> 1));
  return out;
}

/** K-map axes: 2: rows p, cols q; 3: rows p, cols qr; 4: rows pq, cols rs. */
export function kmapLayout(n) {
  if (n === 2) return { rowBits: 1, colBits: 1, rowVars: [0], colVars: [1] };
  if (n === 3) return { rowBits: 1, colBits: 2, rowVars: [0], colVars: [1, 2] };
  return { rowBits: 2, colBits: 2, rowVars: [0, 1], colVars: [2, 3] };
}

export function kmapCells(n, values) {
  const layout = kmapLayout(n);
  const rows = grayCode(layout.rowBits);
  const cols = grayCode(layout.colBits);
  const cells = [];
  for (let r = 0; r < rows.length; r++) {
    for (let c = 0; c < cols.length; c++) {
      const rowVal = rows[r];
      const colVal = cols[c];
      const minterm = (rowVal << layout.colBits) | colVal;
      cells.push({
        r,
        c,
        minterm,
        value: values[minterm] ? 1 : 0,
        rowGray: bitstr(rowVal, layout.rowBits),
        colGray: bitstr(colVal, layout.colBits)
      });
    }
  }
  return { layout, rows, cols, cells, nRows: rows.length, nCols: cols.length };
}

/**
 * Represent an implicant as one or more axis-aligned rectangles on the
 * Gray-coded K-map, including wrap-around (up to 4 pieces).
 */
export function implicantRects(bits, n) {
  const { layout, rows, cols, nRows, nCols } = kmapCells(n, []);
  const covered = coveredBy(bits);
  const coords = [];
  for (let r = 0; r < nRows; r++) {
    for (let c = 0; c < nCols; c++) {
      const minterm = (rows[r] << layout.colBits) | cols[c];
      if (covered.has(minterm)) coords.push({ r, c });
    }
  }
  if (!coords.length) return [];
  const rowSet = [...new Set(coords.map((x) => x.r))].sort((a, b) => a - b);
  const colSet = [...new Set(coords.map((x) => x.c))].sort((a, b) => a - b);
  const rowParts = wrapSegments(rowSet, nRows);
  const colParts = wrapSegments(colSet, nCols);
  const rects = [];
  for (const rp of rowParts) {
    for (const cp of colParts) {
      rects.push({ r0: rp.start, c0: cp.start, h: rp.len, w: cp.len });
    }
  }
  return rects;
}

function wrapSegments(sortedUnique, size) {
  if (sortedUnique.length === size) return [{ start: 0, len: size }];
  if (!sortedUnique.length) return [];
  // If the set is a wrap-around block (includes 0 and size-1, with a gap),
  // split into two contiguous segments.
  const isContig = (arr) => arr.every((v, i) => i === 0 || v === arr[i - 1] + 1);
  if (isContig(sortedUnique)) {
    return [{ start: sortedUnique[0], len: sortedUnique.length }];
  }
  if (sortedUnique[0] === 0 && sortedUnique[sortedUnique.length - 1] === size - 1) {
    let leftLen = 1;
    while (leftLen < sortedUnique.length && sortedUnique[leftLen] === leftLen) leftLen += 1;
    let rightStart = size - 1;
    let k = sortedUnique.length - 1;
    while (k >= 0 && sortedUnique[k] === rightStart) {
      rightStart -= 1;
      k -= 1;
    }
    rightStart += 1;
    const rightLen = size - rightStart;
    if (leftLen + rightLen === sortedUnique.length) {
      return [
        { start: rightStart, len: rightLen },
        { start: 0, len: leftLen }
      ];
    }
  }
  // Fallback: each run of consecutive indices.
  const parts = [];
  let start = sortedUnique[0];
  let prev = start;
  for (let i = 1; i <= sortedUnique.length; i++) {
    const v = sortedUnique[i];
    if (v !== prev + 1) {
      parts.push({ start, len: prev - start + 1 });
      start = v;
    }
    prev = v;
  }
  return parts;
}

export function prettyAst(ast) {
  if (!ast) return '';
  const wrap = (inner, ok) => (ok ? inner : `(${inner})`);
  switch (ast.type) {
    case 'CONST':
      return ast.value ? '1' : '0';
    case 'VAR':
      return ast.name;
    case 'NOT': {
      const tight = ast.arg.type === 'VAR' || ast.arg.type === 'CONST' || ast.arg.type === 'NOT';
      return '¬' + wrap(prettyAst(ast.arg), tight);
    }
    case 'AND':
      return `${wrap(prettyAst(ast.left), ast.left.type !== 'OR' && ast.left.type !== 'IMP' && ast.left.type !== 'IFF' && ast.left.type !== 'XOR')} ∧ ${wrap(prettyAst(ast.right), ast.right.type !== 'OR' && ast.right.type !== 'IMP' && ast.right.type !== 'IFF' && ast.right.type !== 'XOR')}`;
    case 'OR':
      return `${wrap(prettyAst(ast.left), ast.left.type !== 'IMP' && ast.left.type !== 'IFF')} ∨ ${wrap(prettyAst(ast.right), ast.right.type !== 'IMP' && ast.right.type !== 'IFF')}`;
    case 'XOR':
      return `${prettyAst(ast.left)} ⊕ ${prettyAst(ast.right)}`;
    case 'IMP':
      return `${wrap(prettyAst(ast.left), ast.left.type !== 'IMP' && ast.left.type !== 'IFF')} → ${prettyAst(ast.right)}`;
    case 'IFF':
      return `${prettyAst(ast.left)} ↔ ${prettyAst(ast.right)}`;
    default:
      return '';
  }
}

export const GROUP_COLORS = [
  '#0f766e',
  '#7c3aed',
  '#c2410c',
  '#0369a1',
  '#be185d',
  '#4d7c0f',
  '#b45309',
  '#1d4ed8'
];
