import test from 'node:test';
import assert from 'node:assert/strict';
import { RULE_PRESETS, evalTree, enumerate, postOrder, overlapDemo } from '../src/counting/rule.js';

test('quy tắc cộng/nhân khớp liệt kê trực tiếp', () => {
  const want = { outfit: 24, meal: 9, plate: 5 * 100 + 1000, pw: 4 * 8 * 8 };
  for (const p of RULE_PRESETS) {
    assert.equal(evalTree(p.tree), want[p.id], p.id);
    assert.equal(enumerate(p.tree).length, want[p.id], p.id);
  }
});
test('duyệt hậu tự: gốc đứng cuối, mỗi nút có đủ con trước nó', () => {
  for (const p of RULE_PRESETS) {
    const po = postOrder(p.tree);
    assert.equal(po.at(-1).node, p.tree);
    assert.equal(po.at(-1).value, evalTree(p.tree));
    po.forEach((x, i) => { if (x.node.kids) x.node.kids.forEach((k) => assert.ok(po.findIndex((y) => y.node === k) < i)); });
  }
});
test('bao hàm–loại trừ khớp đếm vét cạn', () => {
  for (let n = 1; n <= 80; n += 7) for (let a = 2; a <= 7; a++) for (let b = a + 1; b <= 9; b++) {
    const o = overlapDemo(n, a, b);
    assert.equal(o.union, o.brute);
    assert.ok(o.naive >= o.union);
  }
});
