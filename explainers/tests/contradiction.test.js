import test from 'node:test';
import assert from 'node:assert/strict';
import { fractionTest, nearMisses, euclidStep, isPrimeNum, SQRT2_STEPS } from '../src/logic/contradiction.js';

test('không có a, b nào để a² = 2b² (b ≤ 3000), kể cả phân số tối giản', () => {
  for (let b = 1; b <= 3000; b++) { const a = Math.round(b * Math.SQRT2); for (const x of [a - 1, a, a + 1]) assert.notEqual(x * x, 2 * b * b); }
  for (const m of nearMisses(500)) assert.notEqual(m.diff, 0);
  const t = fractionTest(14, 10);
  assert.equal(t.ra, 7); assert.equal(t.rb, 5); assert.equal(t.equal, false);
  assert.equal(fractionTest(0, 3).equal, false);
  assert.ok(fractionTest(1, 0).error);
  assert.equal(SQRT2_STEPS.filter((s) => s.kind === 'contradiction').length, 1);
});
test('Euclid: N = tích + 1 chia mỗi p dư 1 và có ước nguyên tố nằm ngoài danh sách', () => {
  const sets = [[2], [2, 3], [2, 3, 5], [2, 3, 5, 7], [2, 3, 5, 7, 11, 13], [3, 5, 7], [2, 5, 11]];
  for (const s of sets) {
    const e = euclidStep(s);
    assert.ok(e.remainders.every((r) => r.r === 1));
    assert.ok(e.isNew && e.qIsPrime && e.N % e.q === 0);
  }
  assert.equal(euclidStep([2, 3, 5, 7, 11, 13]).N, 30031);
  assert.equal(euclidStep([2, 3, 5, 7, 11, 13]).q, 59);
  assert.ok(isPrimeNum(59) && !isPrimeNum(1));
});

import { PROOFS, counterexample, linesSound, countModels } from '../src/logic/predproof.js';
test('chứng minh vị từ: hợp lệ ⇔ không có phản ví dụ; dòng sai quy tắc chỉ ở chứng minh không hợp lệ', () => {
  for (const p of PROOFS) {
    assert.equal(counterexample(p) === null, p.valid, p.id);
    const badLines = p.lines.filter((l) => l.ok === false).length;
    assert.equal(badLines === 0, p.valid, p.id);
    if (p.valid) assert.ok(linesSound(p), p.id);
    assert.ok(countModels(p) > 0);
  }
  const ce = counterexample(PROOFS.find((p) => p.id === 'ei-twice'));
  assert.ok(ce.P.some(Boolean) && ce.Q.some(Boolean));
});
