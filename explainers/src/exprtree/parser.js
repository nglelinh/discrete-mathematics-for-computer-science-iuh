// Bộ phân tích biểu thức logic → cây cú pháp, kèm bố cục và tính giá trị từ lá lên gốc.
// Độ ưu tiên: ¬ > ∧ > ∨ > → > ↔ ;  → kết hợp phải;  ∧ ∨ ↔ kết hợp trái.

const SYMBOLS = [
  ['<->', '↔'], ['<=>', '↔'], ['↔', '↔'],
  ['->', '→'], ['=>', '→'], ['→', '→'],
  ['/\\', '∧'], ['&&', '∧'], ['&', '∧'], ['∧', '∧'],
  ['\\/', '∨'], ['||', '∨'], ['|', '∨'], ['∨', '∨'],
  ['¬', '¬'], ['!', '¬'], ['~', '¬'],
  ['(', '('], [')', ')']
];

export const PREC = { '↔': 1, '→': 2, '∨': 3, '∧': 4, '¬': 5 };

export function tokenize(src) {
  const s = String(src ?? '');
  const out = [];
  let i = 0;
  while (i < s.length) {
    const ch = s[i];
    if (/\s/.test(ch)) { i++; continue; }
    const sym = SYMBOLS.find(([k]) => s.startsWith(k, i));
    if (sym) { out.push({ t: sym[1], pos: i }); i += sym[0].length; continue; }
    if (/[A-Za-z]/.test(ch)) {
      let j = i + 1;
      while (j < s.length && /[A-Za-z0-9_]/.test(s[j])) j++;
      out.push({ t: 'var', v: s.slice(i, j), pos: i });
      i = j; continue;
    }
    if (ch === '0' || ch === '1') { out.push({ t: 'const', v: ch === '1', pos: i }); i++; continue; }
    throw new Error(`Ký tự «${ch}» (vị trí ${i + 1}) không phải phép toán hay biến hợp lệ.`);
  }
  return out;
}

export function parse(src) {
  const toks = tokenize(src);
  if (!toks.length) throw new Error('Hãy nhập một công thức, ví dụ (p ∨ q) → ¬r.');
  let k = 0;
  const peek = () => toks[k];
  const where = (tk) => (tk ? `ở vị trí ${tk.pos + 1}` : 'ở cuối công thức');

  function binary(level) {
    // level 1: ↔ , 2: → (phải), 3: ∨ , 4: ∧
    if (level === 5) return unary();
    const op = { 1: '↔', 2: '→', 3: '∨', 4: '∧' }[level];
    let left = binary(level + 1);
    if (op === '→') {
      if (peek() && peek().t === '→') {
        k++;
        const right = binary(2);
        return { type: 'op', op, children: [left, right] };
      }
      return left;
    }
    while (peek() && peek().t === op) {
      k++;
      const right = binary(level + 1);
      left = { type: 'op', op, children: [left, right] };
    }
    return left;
  }

  function unary() {
    const tk = peek();
    if (!tk) throw new Error('Công thức bị thiếu vế phải: cần một biến hoặc dấu ngoặc ở cuối.');
    if (tk.t === '¬') { k++; return { type: 'op', op: '¬', children: [unary()] }; }
    if (tk.t === 'var') { k++; return { type: 'var', name: tk.v }; }
    if (tk.t === 'const') { k++; return { type: 'const', value: tk.v }; }
    if (tk.t === '(') {
      k++;
      const inner = binary(1);
      if (!peek() || peek().t !== ')') throw new Error(`Thiếu dấu «)» để đóng ngoặc mở ở vị trí ${tk.pos + 1}.`);
      k++;
      return inner;
    }
    if (tk.t === ')') throw new Error(`Dấu «)» ${where(tk)} không có dấu «(» tương ứng, hoặc thiếu toán hạng trước nó.`);
    throw new Error(`Phép toán «${tk.t}» ${where(tk)} đang thiếu vế trái.`);
  }

  const ast = binary(1);
  if (k < toks.length) {
    const tk = toks[k];
    if (tk.t === ')') throw new Error(`Dấu «)» ${where(tk)} thừa, không có «(» tương ứng.`);
    throw new Error(`Sau một biểu thức hoàn chỉnh, «${tk.t === 'var' ? tk.v : tk.t}» ${where(tk)} xuất hiện không đúng chỗ (thiếu phép toán ở giữa?).`);
  }
  return ast;
}

export function collectVars(ast, set = new Set()) {
  if (ast.type === 'var') set.add(ast.name);
  else if (ast.type === 'op') ast.children.forEach((c) => collectVars(c, set));
  return [...set].sort();
}

export function evalOp(op, a, b) {
  switch (op) {
    case '¬': return !a;
    case '∧': return a && b;
    case '∨': return a || b;
    case '→': return !a || b;
    case '↔': return a === b;
  }
  throw new Error('Phép toán lạ: ' + op);
}

export function evalAst(ast, env) {
  if (ast.type === 'var') return !!env[ast.name];
  if (ast.type === 'const') return ast.value;
  return evalOp(ast.op, evalAst(ast.children[0], env), ast.children[1] ? evalAst(ast.children[1], env) : undefined);
}

/** Chuỗi có ngoặc tối thiểu (để kiểm tra / hiển thị). */
export function show(ast, parentPrec = 0, side = '') {
  if (ast.type === 'var') return ast.name;
  if (ast.type === 'const') return ast.value ? 'T' : 'F';
  if (ast.op === '¬') return '¬' + show(ast.children[0], PREC['¬']);
  const p = PREC[ast.op];
  const [l, r] = ast.children;
  const needL = ast.op === '→' ? PREC[l.op] !== undefined && l.type === 'op' && PREC[l.op] <= p : false;
  const ls = show(l, ast.op === '→' ? 99 : p - 1, 'l');
  const rs = show(r, ast.op === '→' ? p - 1 : p, 'r');
  void needL; void side;
  const s = `${ls} ${ast.op} ${rs}`;
  return p <= parentPrec ? `(${s})` : s;
}

/** Gán id, độ sâu, tọa độ (x theo thứ tự lá, y theo độ sâu). */
export function layout(ast) {
  let leaf = 0, id = 0, maxDepth = 0;
  function go(n, depth) {
    const node = { ...n, id: id++, depth };
    maxDepth = Math.max(maxDepth, depth);
    if (n.type === 'op') {
      node.kids = n.children.map((c) => go(c, depth + 1));
      node.x = node.kids.reduce((s, c) => s + c.x, 0) / node.kids.length;
    } else {
      node.kids = [];
      node.x = leaf++;
    }
    return node;
  }
  const root = go(ast, 0);
  return { root, leaves: Math.max(leaf, 1), depth: maxDepth };
}

export function flatten(root, out = []) {
  out.push(root);
  root.kids.forEach((c) => flatten(c, out));
  return out;
}

/** Giá trị của từng nút (theo id) và thứ tự tính (hậu tự), mỗi nút chỉ tính khi con đã xong. */
export function evaluateTree(root, env) {
  const val = {};
  const order = [];
  (function go(n) {
    n.kids.forEach(go);
    let v;
    if (n.type === 'var') v = !!env[n.name];
    else if (n.type === 'const') v = n.value;
    else v = evalOp(n.op, val[n.kids[0].id], n.kids[1] ? val[n.kids[1].id] : undefined);
    val[n.id] = v;
    order.push(n.id);
  })(root);
  return { val, order };
}
