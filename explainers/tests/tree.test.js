import test from 'node:test';
import assert from 'node:assert/strict';
import { parseFreqs, freqsFromText, huffman, encode, decode, layoutForest, buildBST, insert, search, remove, preorder, inorder, postorder, levelorder, isBST, height, size, parseKeys } from '../src/tree/tree.js';

const isPrefixFree = (codes) => { const c = Object.values(codes); return c.every((a, i) => c.every((b, j) => i === j || !b.startsWith(a))); };

test('Huffman: ví dụ CLRS cho độ dài mã tối ưu', () => {
  const h = huffman(parseFreqs('a:45 b:13 c:12 d:16 e:9 f:5'));
  assert.equal(h.total, 100);
  assert.equal(h.bits, 224); // 45*1 + (13+12+16)*3 + (9+5)*4
  assert.equal(h.codes.a.length, 1);
  assert.equal(h.steps.length, 5);
  assert.equal(h.root.freq, 100);
  assert.ok(isPrefixFree(h.codes));
  assert.equal(h.fixedBits, 300);
});

test('Huffman: tiền tố tự do, mã/giải mã khứ hồi, tối ưu so với hoán vị độ dài', () => {
  let seed = 7; const rnd = () => (seed = (seed * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff;
  for (let t = 0; t < 100; t++) {
    const n = 2 + Math.floor(rnd() * 7);
    const fr = Array.from({ length: n }, (_, i) => ({ sym: String.fromCharCode(97 + i), freq: 1 + Math.floor(rnd() * 30) }));
    const h = huffman(fr);
    assert.ok(isPrefixFree(h.codes));
    // Kraft = 1 với cây đầy
    const kraft = Object.values(h.codes).reduce((s, c) => s + 2 ** -c.length, 0);
    assert.ok(Math.abs(kraft - 1) < 1e-9);
    const msg = fr.map((f) => f.sym).join('') + 'a';
    assert.equal(decode(h.root, encode(h.codes, msg)), msg);
    // không tệ hơn mã độ dài cố định
    assert.ok(h.bits <= h.fixedBits);
    // tổng chi phí = tổng trọng số các nút trong
    const internal = h.steps.reduce((s, st) => s + st.parent.freq, 0);
    assert.equal(internal, h.bits);
  }
});

test('Huffman: một ký tự và đầu vào rỗng', () => {
  const h = huffman([{ sym: 'x', freq: 4 }]);
  assert.equal(h.codes.x, '0');
  assert.equal(huffman([]).root, null);
  assert.deepEqual(freqsFromText('aab').sort((p, q) => p.sym.localeCompare(q.sym)), [{ sym: 'a', freq: 2 }, { sym: 'b', freq: 1 }]);
});

test('bố cục rừng không chồng nút', () => {
  const h = huffman(parseFreqs('a:5 b:9 c:12 d:13 e:16 f:45'));
  const L = layoutForest([h.root]);
  const keys = L.nodes.map((n) => `${n.x}/${n.depth}`);
  assert.equal(new Set(keys).size, keys.length);
  assert.equal(L.nodes.length, 11);
});

test('BST: chèn/tìm/duyệt', () => {
  const root = buildBST(parseKeys('8 3 10 1 6 14 4 7 13'));
  assert.deepEqual(inorder(root).map((n) => n.key), [1, 3, 4, 6, 7, 8, 10, 13, 14]);
  assert.deepEqual(preorder(root).map((n) => n.key), [8, 3, 1, 6, 4, 7, 10, 14, 13]);
  assert.deepEqual(postorder(root).map((n) => n.key), [1, 4, 7, 6, 3, 13, 14, 10, 8]);
  assert.deepEqual(levelorder(root).map((n) => n.key), [8, 3, 10, 1, 6, 14, 4, 7, 13]);
  assert.equal(height(root), 4);
  assert.equal(size(root), 9);
  assert.equal(search(root, 7).found, true);
  assert.equal(search(root, 5).found, false);
  assert.equal(insert(root, 7).added, false);
});

test('BST: xóa giữ tính chất (ngẫu nhiên)', () => {
  let seed = 3; const rnd = () => (seed = (seed * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff;
  for (let t = 0; t < 200; t++) {
    const keys = [...new Set(Array.from({ length: 12 }, () => Math.floor(rnd() * 40)))];
    let root = buildBST(keys);
    const del = keys[Math.floor(rnd() * keys.length)];
    const r = remove(root, del);
    assert.ok(isBST(r.root));
    assert.deepEqual(inorder(r.root).map((n) => n.key), keys.filter((k) => k !== del).sort((a, b) => a - b));
    assert.ok(['leaf', 'one', 'two'].includes(r.kind));
  }
  assert.equal(remove(buildBST([5]), 9).kind, null);
});

test('bố cục: mọi liên kết nối hai nút có tọa độ hữu hạn, con nằm dưới cha', () => {
  const L = layoutForest([huffman(parseFreqs('a:5 b:9 c:12 d:13 e:16 f:45')).root]);
  assert.equal(L.links.length, 10);
  for (const l of L.links) {
    for (const v of [l.from.x, l.from.y, l.to.x, l.to.y]) assert.ok(Number.isFinite(v));
    assert.ok(l.to.y > l.from.y);
  }
});
