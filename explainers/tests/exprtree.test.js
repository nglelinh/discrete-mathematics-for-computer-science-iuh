import test from 'node:test';
import assert from 'node:assert/strict';
import { parse, collectVars, evalAst, show, layout, evaluateTree } from '../src/exprtree/parser.js';

const s = (x) => show(parse(x));

test('độ ưu tiên ¬ > ∧ > ∨ > → > ↔', () => {
  assert.equal(s('p ∨ q ∧ r'), 'p ∨ q ∧ r');
  assert.equal(parse('p ∨ q ∧ r').op, '∨');
  assert.equal(parse('p ∨ q ∧ r').children[1].op, '∧');
  assert.equal(parse('¬p ∧ q').op, '∧');
  assert.equal(parse('p ∧ q → r').op, '→');
  assert.equal(parse('p → q ↔ r').op, '↔');
  assert.equal(parse('p ↔ q → r').op, '↔');
  assert.equal(parse('p → q ∨ r').children[1].op, '∨');
});

test('→ kết hợp phải', () => {
  const a = parse('p → q → r');
  assert.equal(a.op, '→');
  assert.equal(a.children[0].type, 'var');
  assert.equal(a.children[1].op, '→');
  const b = parse('(p → q) → r');
  assert.equal(b.children[0].op, '→');
});

test('∧ ∨ kết hợp trái; ↔ kết hợp trái', () => {
  const a = parse('p ∧ q ∧ r');
  assert.equal(a.children[0].op, '∧');
  assert.equal(a.children[1].name, 'r');
});

test('ký hiệu ASCII tương đương', () => {
  const x = parse('!(p & q) | ~r -> p <-> q');
  const y = parse('¬(p ∧ q) ∨ ¬r → p ↔ q');
  assert.deepEqual(x, y);
});

test('ngoặc và ¬ chồng', () => {
  assert.equal(parse('¬¬p').children[0].op, '¬');
  assert.equal(parse('(p ∨ q) ∧ r').op, '∧');
  assert.equal(parse('((p))').type, 'var');
});

test('lỗi: ngoặc, thiếu toán hạng, ký tự lạ, rỗng', () => {
  for (const bad of ['', '   ', '(p ∧ q', 'p ∧ q)', 'p ∧', '∧ p', 'p q', 'p # q', '()', '¬', 'p → → q'])
    assert.throws(() => parse(bad), Error, bad);
});

test('giá trị: ((p ∨ q) → ¬r) ↔ p khớp bảng chân trị trong bài', () => {
  const ast = parse('((p ∨ q) → ¬r) ↔ p');
  assert.deepEqual(collectVars(ast), ['p', 'q', 'r']);
  const expect = [false, true, false, true, true, false, false, false]; // TTT..FFF
  let i = 0;
  for (const p of [true, false]) for (const q of [true, false]) for (const r of [true, false]) {
    // lưu ý: thứ tự trong bài là p,q,r với T trước
  }
  const rows = [];
  for (const p of [true, false]) for (const q of [true, false]) for (const r of [true, false]) rows.push(evalAst(ast, { p, q, r }));
  assert.deepEqual(rows, expect);
  i++;
});

test('evaluateTree khớp evalAst và gốc ở cuối thứ tự', () => {
  const ast = parse('(p → q) ∧ ¬(q ↔ r)');
  const { root } = layout(ast);
  for (let m = 0; m < 8; m++) {
    const env = { p: !!(m & 1), q: !!(m & 2), r: !!(m & 4) };
    const { val, order } = evaluateTree(root, env);
    assert.equal(val[root.id], evalAst(ast, env));
    assert.equal(order[order.length - 1], root.id);
  }
});
