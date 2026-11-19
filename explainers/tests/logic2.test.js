import test from 'node:test';
import assert from 'node:assert/strict';
import { cantorPair, unpair, diagonalFlip, differsFromAll, randomRows, HILBERT, hotelAfter } from '../src/logic/infinity.js';
import { fullAdder, rippleSteps } from '../src/logic/adder.js';
import { rng, birthdayProb, minPeople, simulateBirthday, expectedOccupied, hashInserts, simulateQueue } from '../src/logic/sim.js';
import { INFERENCE_PRESETS, checkArgument } from '../src/logic/inference.js';

test('ghép cặp Cantor là song ánh trên ℕ×ℕ', () => {
  const seen = new Set();
  for (let i = 0; i < 40; i++) for (let j = 0; j < 40; j++) { const n = cantorPair(i, j); assert.ok(!seen.has(n)); seen.add(n); assert.deepEqual(unpair(n), [i, j]); }
  for (let n = 0; n < 500; n++) { const [i, j] = unpair(n); assert.equal(cantorPair(i, j), n); }
  assert.deepEqual([0, 1, 2, 3, 4, 5].map(unpair), [[0, 0], [1, 0], [0, 1], [2, 0], [1, 1], [0, 2]]);
});
test('đường chéo Cantor khác mọi dòng', () => {
  for (let s = 1; s < 60; s++) { const rows = randomRows(2 + (s % 8), s); assert.ok(differsFromAll(rows, diagonalFlip(rows))); }
});
test('khách sạn Hilbert: mỗi phòng 1..50 đúng một khách, không xung đột', () => {
  for (const sc of HILBERT) {
    const rooms = hotelAfter(sc, 50);
    assert.ok(rooms.every((x) => x && x !== 'XUNG ĐỘT'), sc.id + ' ' + rooms.join());
    assert.equal(new Set(rooms).size, 50);
  }
});

test('bộ cộng ripple-carry: cộng và trừ khớp số học mod 16, cờ tràn đúng', () => {
  for (let a = 0; a < 16; a++) for (let b = 0; b < 16; b++) {
    const s = rippleSteps(a, b, 4, false);
    assert.equal(s.result, (a + b) & 15); assert.equal(s.cout, (a + b) >> 4);
    const sa = a > 7 ? a - 16 : a, sb = b > 7 ? b - 16 : b;
    assert.equal(s.overflow, sa + sb < -8 || sa + sb > 7);
    const d = rippleSteps(a, b, 4, true);
    assert.equal(d.result, (a - b + 16) & 15);
    assert.equal(d.overflow, sa - sb < -8 || sa - sb > 7);
  }
  for (const [a, b, c] of [[0, 0, 0], [1, 1, 0], [1, 1, 1], [1, 0, 1]]) assert.equal(fullAdder(a, b, c).sum + 2 * fullAdder(a, b, c).cout, a + b + c);
});

test('ngày sinh: 23 người ≈ 50,7%, minPeople(0.5)=23, mô phỏng sát công thức', () => {
  assert.ok(Math.abs(birthdayProb(23) - 0.5073) < 0.001);
  assert.equal(minPeople(0.5), 23);
  assert.equal(minPeople(0.99), 57);
  assert.equal(birthdayProb(366), 1);
  assert.ok(Math.abs(simulateBirthday(23, 365, 20000, rng(5)) - birthdayProb(23)) < 0.02);
});
test('băm: số bucket bị chiếm trung bình khớp công thức', () => {
  let sum = 0; const T = 3000;
  for (let t = 0; t < T; t++) { const r = hashInserts(20, 50, rng(t + 1)); sum += r.steps[r.steps.length - 1].occupied; }
  assert.ok(Math.abs(sum / T - expectedOccupied(20, 50)) < 0.1);
});
test('hàng đợi: định luật Little và tải', () => {
  const big = simulateQueue({ lambda: 20, service: 0.1, c: 200, T: 400, seed: 3 });
  assert.ok(big.maxWait === 0);
  assert.ok(Math.abs(big.avgInSystem - 20 * 0.1) < 0.25, 'L=λW ' + big.avgInSystem);
  assert.ok(Math.abs(big.avgInSystem - big.throughput * big.avgSojourn) < 1e-9);
  const small = simulateQueue({ lambda: 20, service: 0.1, c: 2, T: 200, seed: 3 });
  assert.ok(small.avgWait > big.avgWait + 1);
  assert.ok(small.utilization <= 1.0001);
  assert.deepEqual(simulateQueue({ lambda: 5, service: 0.2, c: 2, seed: 9 }).n, simulateQueue({ lambda: 5, service: 0.2, c: 2, seed: 9 }).n);
});

test('suy diễn: quy tắc hợp lệ, ngụy biện không hợp lệ, lỗi cú pháp', () => {
  const expect = { mp: true, mt: true, hs: true, ds: true, res: true, aff: false, den: false };
  for (const p of INFERENCE_PRESETS) assert.equal(checkArgument(p.premises, p.conclusion).valid, expect[p.id], p.id);
  const aff = checkArgument('p → q\nq', 'p');
  assert.deepEqual(aff.rows.filter((r) => r.bad).map((r) => r.env), [{ p: 0, q: 1 }]);
  assert.ok(checkArgument('p →', 'q').error);
});
