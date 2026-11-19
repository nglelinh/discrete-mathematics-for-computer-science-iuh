// Văn phạm phi ngữ cảnh: đọc văn bản, CYK, cây phân tích, dẫn xuất trái nhất. Hàm thuần.

/** "S -> A B | a" mỗi dòng một ký hiệu; ký hiệu cách nhau bởi khoảng trắng. Ký hiệu vế trái là biến, còn lại là ký hiệu kết thúc. */
export function parseGrammar(text) {
  const rules = [];
  const lhs = [];
  for (const line of String(text).split('\n')) {
    const t = line.trim();
    if (!t) continue;
    const m = /^(\S+)\s*(?:->|→)\s*(.+)$/.exec(t);
    if (!m) return { error: `Dòng “${t}” không có dạng  A -> …` };
    if (!lhs.includes(m[1])) lhs.push(m[1]);
    for (const alt of m[2].split('|')) {
      const rhs = alt.trim().split(/\s+/).filter((x) => x && x !== 'ε');
      if (!rhs.length) return { error: 'Chưa hỗ trợ sản xuất rỗng (ε).' };
      rules.push({ lhs: m[1], rhs });
    }
  }
  if (!rules.length) return { error: 'Chưa có luật nào.' };
  return { start: lhs[0], vars: lhs, rules, isVar: (x) => lhs.includes(x) };
}

export function checkCNF(g) {
  for (const r of g.rules) {
    const ok = (r.rhs.length === 1 && !g.isVar(r.rhs[0])) || (r.rhs.length === 2 && r.rhs.every((x) => g.isVar(x)));
    if (!ok) return `Luật ${r.lhs} → ${r.rhs.join(' ')} không ở dạng chuẩn Chomsky (A → BC hoặc A → a).`;
  }
  return null;
}

/** CYK từng bước: một bước cho mỗi (ô, điểm chia). table[`${i},${len}`] = mảng biến. */
export function cykSteps(g, tokens) {
  const n = tokens.length;
  const cell = {};
  const key = (i, len) => `${i},${len}`;
  const snap = () => Object.fromEntries(Object.entries(cell).map(([k, v]) => [k, [...v]]));
  const steps = [];
  steps.push({ cells: snap(), cur: null, split: null, msg: `Chuỗi có ${n} ký hiệu. Ô (i, ℓ) chứa các biến sinh ra đoạn con bắt đầu ở vị trí i, dài ℓ. Hàng ℓ=1 điền từ luật A → a.` });
  for (let i = 0; i < n; i++) {
    cell[key(i, 1)] = [...new Set(g.rules.filter((r) => r.rhs.length === 1 && r.rhs[0] === tokens[i]).map((r) => r.lhs))];
    steps.push({ cells: snap(), cur: [i, 1], split: null, msg: `Ô (${i + 1}, 1) cho “${tokens[i]}”: các biến có luật → ${tokens[i]} là {${cell[key(i, 1)].join(', ')}}.` });
  }
  for (let len = 2; len <= n; len++) {
    for (let i = 0; i + len <= n; i++) {
      cell[key(i, len)] = [];
      for (let k = 1; k < len; k++) {
        const L = cell[key(i, k)] || [], R = cell[key(i + k, len - k)] || [];
        const found = [];
        for (const r of g.rules) if (r.rhs.length === 2 && L.includes(r.rhs[0]) && R.includes(r.rhs[1])) found.push(r.lhs);
        for (const f of found) if (!cell[key(i, len)].includes(f)) cell[key(i, len)].push(f);
        steps.push({
          cells: snap(), cur: [i, len], split: { left: [i, k], right: [i + k, len - k], k },
          msg: `Ô (${i + 1}, ${len}), chia tại k=${k}: trái {${L.join(', ')}} × phải {${R.join(', ')}} ⇒ ` + (found.length ? 'thêm ' + [...new Set(found)].join(', ') : 'không có luật A → BC phù hợp') + '.'
        });
      }
    }
  }
  const top = n ? cell[key(0, n)] : [];
  const ok = top.includes(g.start);
  steps.push({ cells: snap(), cur: n ? [0, n] : null, split: null, done: true, accepted: ok, msg: ok ? `Ô đỉnh chứa ${g.start} ⇒ chuỗi THUỘC ngôn ngữ.` : `Ô đỉnh {${top.join(', ')}} không chứa ${g.start} ⇒ chuỗi KHÔNG thuộc ngôn ngữ.` });
  return { steps, accepted: ok };
}

/** Sinh mọi chuỗi kết thúc độ dài ≤ L của văn phạm CNF (dùng để đối chiếu CYK). */
export function enumerateLanguage(g, L) {
  const out = new Set();
  const seen = new Set();
  const q = [[g.start]];
  while (q.length) {
    const f = q.pop();
    const k = f.join(' ');
    if (seen.has(k)) continue;
    seen.add(k);
    const i = f.findIndex((x) => g.isVar(x));
    if (i < 0) { out.add(k); continue; }
    for (const r of g.rules) {
      if (r.lhs !== f[i]) continue;
      const nf = [...f.slice(0, i), ...r.rhs, ...f.slice(i + 1)];
      if (nf.length <= L) q.push(nf);
    }
  }
  return out;
}

/** Tìm các cây phân tích (tối đa cap) của chuỗi token. Không hỗ trợ ε. */
export function parseTrees(g, tokens, cap = 30) {
  const n = tokens.length;
  const memo = new Map();
  const busy = new Set();
  let nid = 0;
  const mk = (sym, children, token) => ({ sym, children, token });
  function parse(A, i, j) {
    const k = `${A}|${i}|${j}`;
    if (memo.has(k)) return memo.get(k);
    if (busy.has(k)) return [];
    busy.add(k);
    const res = [];
    for (const r of g.rules) {
      if (r.lhs !== A) continue;
      for (const kids of seq(r.rhs, 0, i, j)) {
        if (res.length >= cap) break;
        res.push(mk(A, kids));
      }
    }
    busy.delete(k);
    memo.set(k, res);
    return res;
  }
  function* seq(rhs, p, i, j) {
    if (p === rhs.length) { if (i === j) yield []; return; }
    const X = rhs[p];
    if (!g.isVar(X)) {
      if (i < j && tokens[i] === X) for (const rest of seq(rhs, p + 1, i + 1, j)) yield [mk(X, null, X), ...rest];
      return;
    }
    for (let m = i + 1; m <= j; m++) {
      for (const t of parse(X, i, m)) for (const rest of seq(rhs, p + 1, m, j)) yield [t, ...rest];
    }
  }
  const trees = n ? parse(g.start, 0, n) : [];
  const label = (t) => { t.id = nid++; t.children?.forEach(label); };
  trees.forEach((t) => { nid = 0; label(t); });
  return { trees, capped: trees.length >= cap };
}

export const treeYield = (t) => (t.children ? t.children.flatMap(treeYield) : [t.token]);
export function internalCount(t) { return t.children ? 1 + t.children.reduce((a, c) => a + internalCount(c), 0) : 0; }

/** Dẫn xuất trái nhất: mỗi bước thay biến ngoài cùng bên trái. */
export function leftmostDerivation(tree) {
  let form = [tree];
  const steps = [{ form: form.map((x) => x.sym), expand: null, rule: null, ids: [] }];
  const expanded = [];
  for (;;) {
    const i = form.findIndex((x) => x.children);
    if (i < 0) break;
    const node = form[i];
    form = [...form.slice(0, i), ...node.children, ...form.slice(i + 1)];
    expanded.push(node.id);
    steps.push({ form: form.map((x) => x.sym), expand: node.id, rule: `${node.sym} → ${node.children.map((c) => c.sym).join(' ')}`, ids: [...expanded] });
  }
  return steps;
}

/** Bố trí cây: lá theo thứ tự x = 0,1,2…; nút trong ở giữa các con; y = độ sâu. */
export function layoutTree(t) {
  let leaf = 0, maxD = 0;
  const nodes = [], links = [];
  function go(n, d) {
    maxD = Math.max(maxD, d);
    let x;
    if (!n.children) x = leaf++;
    else { const xs = n.children.map((c) => go(c, d + 1)); x = (xs[0] + xs[xs.length - 1]) / 2; n.children.forEach((c, i) => links.push([n.id, c.id])); }
    nodes.push({ id: n.id, sym: n.sym, x, y: d, leaf: !n.children });
    return x;
  }
  go(t, 0);
  return { nodes, links, width: Math.max(leaf, 1), depth: maxD };
}

export const CYK_PRESETS = [
  { id: 'classic', name: 'Ví dụ kinh điển (baaba)', input: 'b a a b a', text: 'S -> A B | B C\nA -> B A | a\nB -> C C | b\nC -> A B | a' },
  { id: 'anbn', name: 'aⁿbⁿ (n ≥ 1) dạng CNF', input: 'a a b b', text: 'S -> A T | A B\nT -> S B\nA -> a\nB -> b' },
  { id: 'reject', name: 'Chuỗi bị từ chối', input: 'a b a b', text: 'S -> A T | A B\nT -> S B\nA -> a\nB -> b' }
];

export const TREE_PRESETS = [
  { id: 'expr-amb', name: 'Biểu thức nhập nhằng', input: 'id + id * id', text: 'E -> E + E | E * E | ( E ) | id' },
  { id: 'expr-unamb', name: 'Biểu thức không nhập nhằng', input: 'id + id * id', text: 'E -> E + T | T\nT -> T * F | F\nF -> ( E ) | id' },
  { id: 'else', name: 'Dangling else', input: 'if b then if b then a else a', text: 'S -> if b then S | if b then S else S | a' },
  { id: 'paren', name: 'Dấu ngoặc cân bằng', input: '( ) ( ) ( )', text: 'S -> ( S ) | S S | ( )' }
];
