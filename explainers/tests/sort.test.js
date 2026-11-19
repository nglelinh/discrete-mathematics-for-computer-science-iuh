import test from 'node:test';
import assert from 'node:assert/strict';
import { sortSteps, searchSteps } from '../src/recurrence/sort.js';

const rnd = (seed) => () => { seed = (seed * 1664525 + 1013904223) >>> 0; return seed / 2 ** 32; };
const arrays = () => { const r = rnd(7); return Array.from({ length: 60 }, (_, t) => Array.from({ length: 1 + (t % 10) }, () => Math.floor(r() * 20))); };

test('mọi thuật toán cho hoán vị đã sắp xếp; mỗi bước là hoán vị của mảng đầu', () => {
  for (const arr of arrays()) for (const k of ['bubble', 'insertion', 'selection']) {
    const r = sortSteps(k, arr);
    assert.deepEqual(r.result, [...arr].sort((x, y) => x - y), k);
    for (const s of r.steps) assert.deepEqual([...s.arr].sort((x, y) => x - y), [...arr].sort((x, y) => x - y));
  }
});
test('số so sánh: bubble và selection = n(n−1)/2; insertion ≤ n(n−1)/2; hoán đổi = số nghịch thế (bubble/insertion)', () => {
  for (const arr of arrays()) {
    const n = arr.length, tot = (n * (n - 1)) / 2;
    assert.equal(sortSteps('bubble', arr).comps, tot);
    assert.equal(sortSteps('selection', arr).comps, tot);
    assert.ok(sortSteps('insertion', arr).comps <= tot);
    let inv = 0; for (let i = 0; i < n; i++) for (let j = i + 1; j < n; j++) if (arr[i] > arr[j]) inv++;
    assert.equal(sortSteps('bubble', arr).swaps, inv);
    assert.equal(sortSteps('insertion', arr).swaps, inv);
    assert.ok(sortSteps('selection', arr).swaps <= n - 1);
  }
});
test('tìm kiếm khớp indexOf; nhị phân ≤ ⌊log₂n⌋+1 so sánh', () => {
  for (const raw of arrays()) {
    const arr = [...new Set(raw)].sort((a, b) => a - b);
    for (let t = -1; t <= 21; t++) {
      const l = searchSteps('linear', arr, t), b = searchSteps('binary', arr, t);
      assert.equal(l.index, arr.indexOf(t));
      assert.equal(b.index, arr.indexOf(t));
      assert.ok(b.comps <= Math.floor(Math.log2(arr.length)) + 1);
    }
  }
});
