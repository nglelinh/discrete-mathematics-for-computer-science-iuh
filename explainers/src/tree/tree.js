// Logic thuần cho cây: Huffman, duyệt cây nhị phân, cây tìm kiếm nhị phân (BST).

/* ---------------- Huffman ---------------- */
export function parseFreqs(text) {
  const out = [];
  const seen = new Set();
  for (const tok of String(text).split(/[\s,;]+/).filter(Boolean)) {
    const m = tok.match(/^(.+?)[:=](\d+(?:\.\d+)?)$/);
    if (!m) continue;
    if (seen.has(m[1])) continue;
    seen.add(m[1]);
    out.push({ sym: m[1], freq: Number(m[2]) });
  }
  return out;
}

export function freqsFromText(text) {
  const m = new Map();
  for (const c of text) m.set(c, (m.get(c) || 0) + 1);
  return [...m].map(([sym, freq]) => ({ sym, freq }));
}

let uid = 0;
const leaf = (sym, freq, order) => ({ id: 'n' + uid++, sym, freq, order, left: null, right: null });

const byFreq = (a, b) => a.freq - b.freq || a.order - b.order;

/** Huffman: mỗi bước lấy hai cây có trọng số nhỏ nhất (hòa → theo thứ tự tạo), gộp lại. */
export function huffman(freqs) {
  uid = 0;
  let forest = freqs.filter((f) => f.freq > 0).map((f, i) => leaf(f.sym, f.freq, i));
  const steps = [];
  let order = forest.length;
  const snapshot = () => forest.slice().sort(byFreq);
  const initial = snapshot();
  while (forest.length > 1) {
    forest.sort(byFreq);
    const [a, b] = forest;
    const parent = { id: 'n' + uid++, sym: null, freq: a.freq + b.freq, order: order++, left: a, right: b };
    forest = [...forest.slice(2), parent];
    steps.push({ a, b, parent, forest: snapshot() });
  }
  const root = forest[0] || null;
  const codes = {};
  const walk = (n, code) => {
    if (!n) return;
    if (!n.left && !n.right) { codes[n.sym] = code || '0'; return; }
    walk(n.left, code + '0');
    walk(n.right, code + '1');
  };
  walk(root, '');
  const total = freqs.reduce((s, f) => s + f.freq, 0);
  const bits = freqs.reduce((s, f) => s + f.freq * (codes[f.sym] ? codes[f.sym].length : 0), 0);
  const fixedLen = freqs.length > 1 ? Math.ceil(Math.log2(freqs.length)) : 1;
  return { initial, steps, root, codes, total, bits, avg: total ? bits / total : 0, fixedLen, fixedBits: fixedLen * total };
}

export function encode(codes, msg) {
  let out = '';
  for (const c of msg) { if (!(c in codes)) return null; out += codes[c]; }
  return out;
}

export function decode(root, bits) {
  if (!root) return '';
  if (!root.left && !root.right) return root.sym.repeat(bits.length);
  let out = '', n = root;
  for (const b of bits) {
    n = b === '0' ? n.left : n.right;
    if (!n) return null;
    if (!n.left && !n.right) { out += n.sym; n = root; }
  }
  return n === root ? out : null;
}

/** Bố cục cho rừng cây: trả về nodes (x,y) và links, rộng w. */
export function layoutForest(trees, { dx = 46, dy = 62, gap = 28 } = {}) {
  const nodes = [], links = [];
  let cursor = 0, maxDepth = 0;
  for (const t of trees) {
    const startX = cursor;
    const place = (n, depth) => {
      maxDepth = Math.max(maxDepth, depth);
      if (!n.left && !n.right) { const x = cursor; cursor += dx; nodes.push({ n, x, depth, y: depth * dy }); return x; }
      const xs = [];
      if (n.left) xs.push(place(n.left, depth + 1));
      if (n.right) xs.push(place(n.right, depth + 1));
      const x = (xs[0] + xs[xs.length - 1]) / 2;
      nodes.push({ n, x, depth, y: depth * dy });
      return x;
    };
    place(t, 0);
    cursor += gap;
    void startX;
  }
  const pos = new Map(nodes.map((o) => [o.n.id, o]));
  for (const o of nodes) {
    if (o.n.left) links.push({ from: o, to: pos.get(o.n.left.id), bit: '0' });
    if (o.n.right) links.push({ from: o, to: pos.get(o.n.right.id), bit: '1' });
  }
  return { nodes, links, width: Math.max(cursor - gap, dx), height: maxDepth * dy };
}

/* ---------------- Cây nhị phân / BST ---------------- */
let bid = 0;
export const bnode = (key) => ({ id: 'b' + bid++, key, left: null, right: null });

export function insert(root, key) {
  const path = [];
  if (!root) return { root: bnode(key), path: [], added: true };
  let n = root;
  for (;;) {
    path.push(n.id);
    if (key === n.key) return { root, path, added: false };
    const side = key < n.key ? 'left' : 'right';
    if (!n[side]) { n[side] = bnode(key); return { root, path, added: true, side }; }
    n = n[side];
  }
}

export function search(root, key) {
  const path = [];
  let n = root;
  while (n) {
    path.push(n.id);
    if (key === n.key) return { found: true, path };
    n = key < n.key ? n.left : n.right;
  }
  return { found: false, path };
}

export function minNode(n) { while (n && n.left) n = n.left; return n; }

/** Xóa: trả về gốc mới và mô tả trường hợp (lá / một con / hai con → kế thừa). */
export function remove(root, key) {
  let kind = null;
  const rec = (n, k) => {
    if (!n) return null;
    if (k < n.key) { n.left = rec(n.left, k); return n; }
    if (k > n.key) { n.right = rec(n.right, k); return n; }
    if (!n.left && !n.right) { kind = 'leaf'; return null; }
    if (!n.left) { kind = 'one'; return n.right; }
    if (!n.right) { kind = 'one'; return n.left; }
    kind = 'two';
    const s = minNode(n.right);
    n.key = s.key;
    n.right = rec(n.right, s.key);
    return n;
  };
  const r = rec(root, key);
  return { root: r, kind };
}

export function buildBST(keys) {
  let root = null;
  for (const k of keys) root = insert(root, k).root;
  return root;
}

export function parseKeys(text) {
  return String(text).split(/[\s,;]+/).filter(Boolean).map(Number).filter((x) => Number.isFinite(x));
}

export const preorder = (n, out = []) => (n ? (out.push(n), preorder(n.left, out), preorder(n.right, out), out) : out);
export const inorder = (n, out = []) => (n ? (inorder(n.left, out), out.push(n), inorder(n.right, out), out) : out);
export const postorder = (n, out = []) => (n ? (postorder(n.left, out), postorder(n.right, out), out.push(n), out) : out);
export function levelorder(root) {
  const out = [], q = root ? [root] : [];
  while (q.length) { const n = q.shift(); out.push(n); if (n.left) q.push(n.left); if (n.right) q.push(n.right); }
  return out;
}
export const ORDERS = {
  pre: { label: 'Tiền thứ tự (NLR)', fn: preorder },
  in: { label: 'Trung thứ tự (LNR)', fn: inorder },
  post: { label: 'Hậu thứ tự (LRN)', fn: postorder },
  level: { label: 'Theo mức (BFS)', fn: levelorder }
};
export const height = (n) => (n ? 1 + Math.max(height(n.left), height(n.right)) : 0);
export const size = (n) => (n ? 1 + size(n.left) + size(n.right) : 0);
export const isBST = (n, lo = -Infinity, hi = Infinity) => !n || (n.key > lo && n.key < hi && isBST(n.left, lo, n.key) && isBST(n.right, n.key, hi));

export const HUFFMAN_PRESETS = [
  { label: 'CLRS: a45 b13 c12 d16 e9 f5', text: 'a:45 b:13 c:12 d:16 e:9 f:5', msg: 'abcdef' },
  { label: 'Từ "ABRACADABRA"', text: 'A:5 B:2 R:2 C:1 D:1', msg: 'ABRACADABRA' },
  { label: 'Hai ký tự', text: 'x:3 y:7', msg: 'xyy' }
];
