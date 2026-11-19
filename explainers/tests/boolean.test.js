import test from 'node:test';
import assert from 'node:assert/strict';
import { parse, mintermsOf } from '../src/boolean/logic.js';
import {
  resolveVars, valuesFor, minimize, coverValue, posLabel, sopText, canonicalForms, compareValues, DC
} from '../src/boolean/logic2.js';
import { netlistFromAst, netlistFromCover, evalNet, layoutNet } from '../src/boolean/circuit.js';

const names3 = ['p', 'q', 'r'];

test('bảng chân trị: XOR, kéo theo, ↔', () => {
  assert.deepEqual(valuesFor(2, parse('p ⊕ q'), ['p', 'q']), [0, 1, 1, 0]);
  assert.deepEqual(valuesFor(2, parse('p → q'), ['p', 'q']), [1, 1, 0, 1]);
  assert.deepEqual(valuesFor(2, parse('p ↔ q'), ['p', 'q']), [1, 0, 0, 1]);
});

test('resolveVars: lỗi khi dùng quá nhiều biến, giữ thứ tự p,q,r', () => {
  assert.throws(() => resolveVars(2, [parse('p ∧ q ∧ r')]));
  assert.deepEqual(resolveVars(3, [parse('p ∨ r')]), ['p', 'q', 'r']);
  assert.deepEqual(resolveVars(2, [parse('y ∧ x')]), ['x', 'y']);
});

test('SOP và POS đúng với mọi hàm 3 biến (không don\'t care)', () => {
  for (let f = 0; f < 256; f++) {
    const v = Array.from({ length: 8 }, (_, i) => (f >> i) & 1);
    const s = minimize(v, 3, 'sop');
    const p = minimize(v, 3, 'pos');
    for (let m = 0; m < 8; m++) {
      assert.equal(coverValue(s, m), v[m], `SOP f=${f} m=${m}`);
      assert.equal(coverValue(p, m), v[m], `POS f=${f} m=${m}`);
    }
  }
});

test('SOP/POS đúng với hàm ngẫu nhiên 4 biến có don\'t care', () => {
  let seed = 12345;
  const rnd = () => (seed = (seed * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff;
  for (let t = 0; t < 300; t++) {
    const v = Array.from({ length: 16 }, () => { const r = rnd(); return r < 0.4 ? 0 : r < 0.8 ? 1 : DC; });
    const s = minimize(v, 4, 'sop');
    const p = minimize(v, 4, 'pos');
    for (let m = 0; m < 16; m++) {
      if (v[m] === DC) continue;
      assert.equal(coverValue(s, m), v[m], `SOP t=${t} m=${m}`);
      assert.equal(coverValue(p, m), v[m], `POS t=${t} m=${m}`);
    }
  }
});

test('don\'t care thu gọn hơn: m=0,1,5 và d=2,7 (bài 13-04) → ¬x¬z ∨ ¬y z', () => {
  const v = [1, 1, DC, 0, 0, 1, 0, DC];
  const s = minimize(v, 3, 'sop');
  assert.equal(s.cover.length, 2);
  const label = sopText(s.cover, ['x', 'y', 'z']);
  assert.ok(label.includes('¬x ∧ ¬z') || label.includes('¬x ∧ ¬y'), label);
  const noDc = minimize([1, 1, 0, 0, 0, 1, 0, 0], 3, 'sop');
  assert.ok(noDc.cover.length >= s.cover.length);
});

test('hằng: F=0 và F=1', () => {
  const zero = minimize(Array(4).fill(0), 2, 'sop');
  assert.equal(sopText(zero.cover, ['p', 'q']), '0');
  const one = minimize(Array(4).fill(1), 2, 'sop');
  assert.equal(sopText(one.cover, ['p', 'q']), '1');
  assert.equal(posLabel(minimize(Array(4).fill(1), 2, 'pos').cover, ['p', 'q']), '1');
  assert.equal(posLabel(minimize(Array(4).fill(0), 2, 'pos').cover, ['p', 'q']), '0');
});

test('POS của p→q là (¬p ∨ q); chuẩn tắc', () => {
  const v = valuesFor(2, parse('p → q'), ['p', 'q']);
  assert.equal(posLabel(minimize(v, 2, 'pos').cover, ['p', 'q']), '¬p ∨ q');
  const c = canonicalForms(v, ['p', 'q']);
  assert.equal(c.sigma, 'Σm(0, 1, 3)');
  assert.equal(c.pi, 'ΠM(2)');
  assert.equal(c.cnf, '(¬p ∨ q)');
});

test('so sánh: De Morgan tương đương; p→q ≢ q→p', () => {
  const n = ['p', 'q'];
  const a = valuesFor(2, parse('¬(p ∧ q)'), n);
  const b = valuesFor(2, parse('¬p ∨ ¬q'), n);
  assert.equal(compareValues(a, b).equivalent, true);
  const c = compareValues(valuesFor(2, parse('p → q'), n), valuesFor(2, parse('q → p'), n));
  assert.equal(c.equivalent, false);
  assert.deepEqual(c.diff, [1, 2]);
  assert.equal(c.aImpB, false);
});

test('mạch từ AST cho cùng giá trị với biểu thức, mọi tổ hợp', () => {
  for (const src of ['(p ∧ q) → r', 'p ⊕ q ⊕ r', '¬(p ∨ q) ↔ (¬p ∧ ¬q)', '(p ∨ q) ∧ ¬r']) {
    const ast = parse(src);
    const net = netlistFromAst(ast, names3);
    const vals = valuesFor(3, ast, names3);
    for (let m = 0; m < 8; m++) {
      const env = { p: (m >> 2) & 1, q: (m >> 1) & 1, r: m & 1 };
      assert.equal(evalNet(net, env)[net.out], vals[m], `${src} m=${m}`);
    }
    const lay = layoutNet(net);
    assert.ok(lay.width > 0 && lay.height > 0 && lay.pos.every((p) => Number.isFinite(p.x + p.y)));
  }
});

test('mạch SOP/POS từ phủ cho cùng giá trị', () => {
  for (const f of [0, 1, 0x96, 0xe8, 0x7f, 0xff, 0x18]) {
    const v = Array.from({ length: 8 }, (_, i) => (f >> i) & 1);
    for (const kind of ['sop', 'pos']) {
      const min = minimize(v, 3, kind);
      const net = netlistFromCover(min.cover, names3, kind);
      for (let m = 0; m < 8; m++) {
        const env = { p: (m >> 2) & 1, q: (m >> 1) & 1, r: m & 1 };
        assert.equal(evalNet(net, env)[net.out], v[m], `${kind} f=${f} m=${m}`);
      }
      layoutNet(net);
    }
  }
});
