import test from 'node:test';
import assert from 'node:assert/strict';
import { binomBig, rowValues, totalSteps, stepIndex, cellOfStep, buildTimeline, stepInfo, explainStep, rowSum, symmetryPairs, hockey, isOdd, oddCount } from '../src/pascal/pascal.js';

test('dòng thời gian: mỗi ô bằng tổng hai ô cha, thứ tự từ đỉnh xuống', () => {
  const N = 20;
  const { rows, steps } = buildTimeline(N);
  assert.equal(steps.length, totalSteps(N));
  steps.forEach((s, i) => {
    assert.equal(stepIndex(s.r, s.k), i);
    assert.deepEqual(cellOfStep(i), { r: s.r, k: s.k });
    assert.equal(s.v, binomBig(s.r, s.k));
    if (s.r === 0) assert.equal(s.parents.length, 0);
    else if (s.k === 0 || s.k === s.r) { assert.equal(s.parents.length, 1); assert.equal(s.v, 1n); }
    else {
      assert.equal(s.parents.length, 2);
      assert.equal(s.parents[0].v + s.parents[1].v, s.v);
      assert.deepEqual(s.parents.map((p) => [p.r, p.k]), [[s.r - 1, s.k - 1], [s.r - 1, s.k]]);
      // cha phải nằm ở bước trước đó (đã tính xong)
      for (const p of s.parents) assert.ok(stepIndex(p.r, p.k) < i);
    }
  });
  assert.deepEqual(rows[5].map(Number), [1, 5, 10, 10, 5, 1]);
});

test('binomBig khớp công thức giai thừa và hàng đối xứng', () => {
  const fact = (n) => (n <= 1n ? 1n : n * fact(n - 1n));
  for (let n = 0; n <= 25; n++) for (let k = 0; k <= n; k++) {
    assert.equal(binomBig(n, k), fact(BigInt(n)) / (fact(BigInt(k)) * fact(BigInt(n - k))));
    assert.equal(binomBig(n, k), binomBig(n, n - k));
  }
  assert.equal(binomBig(5, 7), 0n);
  assert.equal(binomBig(60, 30), 118264581564861424n);
});

test('stepInfo: thời điểm nguyên / thập phân / biên', () => {
  const total = totalSteps(4);
  assert.deepEqual(stepInfo(0, total), { done: 0, cs: -1, cp: 1 });
  assert.deepEqual(stepInfo(3, total), { done: 3, cs: 2, cp: 1 });
  const m = stepInfo(3.25, total);
  assert.equal(m.done, 3); assert.equal(m.cs, 3); assert.ok(Math.abs(m.cp - 0.25) < 1e-9);
  assert.deepEqual(stepInfo(999, total), { done: total, cs: total - 1, cp: 1 });
});

test('diễn giải từng bước nêu đúng phép cộng', () => {
  const { steps } = buildTimeline(5);
  assert.match(explainStep(steps[0]), /Đỉnh/);
  const s = steps[stepIndex(4, 2)];
  assert.match(explainStep(s), /3 \+ 3 = 6/);
  assert.match(explainStep(steps[stepIndex(3, 0)]), /MỘT ô cha/);
  assert.match(explainStep(null), /Play/);
});

test('tổng hàng = 2^n, tổng xen kẽ = 0, đối xứng', () => {
  for (let n = 0; n <= 30; n++) {
    const r = rowSum(n);
    assert.equal(r.sum, r.pow);
    assert.equal(r.alt, n === 0 ? 1n : 0n);
    for (const p of symmetryPairs(n)) { assert.equal(binomBig(n, p.mirror), p.v); }
  }
  assert.equal(symmetryPairs(5).length, 3);
  assert.equal(symmetryPairs(4).at(-1).self, true);
});

test('cây gậy khúc côn cầu: Σ C(i,k) = C(n+1,k+1) với mọi n,k ≤ 25', () => {
  for (let n = 0; n <= 25; n++) for (let k = 0; k <= n; k++) {
    const h = hockey(n, k);
    assert.equal(h.sum, h.target.v);
    assert.equal(h.cells.length, n - k + 1);
    assert.ok(h.cells.every((c) => c.k === k));
  }
  assert.equal(hockey(5, 2).sum, 20n);
  assert.equal(hockey(2, 5), null);
});

test('tô màu mod 2 khớp tính chẵn lẻ thật và số ô lẻ là 2^(số bit 1 của n)', () => {
  for (let n = 0; n <= 40; n++) {
    let odd = 0;
    for (let k = 0; k <= n; k++) {
      assert.equal(isOdd(n, k), binomBig(n, k) % 2n === 1n, `${n},${k}`);
      if (isOdd(n, k)) odd++;
    }
    assert.equal(odd, oddCount(n));
    assert.equal(odd, 2 ** n.toString(2).replace(/0/g, '').length);
  }
  assert.equal(rowValues(3).map(Number).join(), '1,3,3,1');
});
