import test from 'node:test';
import assert from 'node:assert/strict';
import { binom, perm, fact, pascalRow, combinations, permutations, compositions, countCompositions, pigeonBound } from '../src/counting/counting.js';
import { terms, solveClosed, divideConquer, directT, fibTree } from '../src/recurrence/recurrence.js';

test('tổ hợp, chỉnh hợp, Pascal', () => {
  assert.equal(binom(10, 3), 120n);
  assert.equal(binom(52, 5), 2598960n);
  assert.equal(perm(10, 3), 720n);
  assert.equal(fact(10), 3628800n);
  for (let n = 0; n <= 14; n++) {
    const row = pascalRow(n);
    assert.equal(row.reduce((a, b) => a + b, 0n), 2n ** BigInt(n));
    for (let k = 0; k <= n; k++) {
      assert.equal(row[k], binom(n, k));
      if (n > 0 && k > 0 && k < n) assert.equal(row[k], binom(n - 1, k - 1) + binom(n - 1, k));
      assert.equal(binom(n, k) * fact(k), perm(n, k));
    }
  }
});

test('liệt kê khớp công thức', () => {
  for (let n = 1; n <= 7; n++) for (let k = 0; k <= n; k++) {
    assert.equal(BigInt(combinations(n, k, 1e6).length), binom(n, k));
    assert.equal(BigInt(permutations(n, k, 1e6).length), perm(n, k));
  }
});

test('sao–vạch: số nghiệm = C(n+k-1, k-1), mỗi nghiệm có tổng đúng', () => {
  for (let n = 0; n <= 9; n++) for (let k = 1; k <= 5; k++) for (const lower of [0, 1]) {
    const sols = compositions(n, k, lower, 1e6);
    assert.equal(BigInt(sols.length), countCompositions(n, k, lower));
    for (const s of sols) { assert.equal(s.reduce((a, b) => a + b, 0), n); assert.ok(s.every((x) => x >= lower)); }
    assert.equal(new Set(sols.map((s) => s.join(','))).size, sols.length);
  }
  assert.equal(countCompositions(10, 4, 1), binom(9, 3));
});

test('chuồng bồ câu', () => {
  assert.equal(pigeonBound(13, 12), 2);
  assert.equal(pigeonBound(25, 8), 4);
});

test('Fibonacci, Hà Nội, nghiệm kép, nghiệm phức', () => {
  assert.deepEqual(terms(1, 1, 0, 0, 1, 10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]);
  const fib = solveClosed(1, 1, 0, 0, 1);
  assert.equal(fib.kind, 'distinct');
  assert.ok(Math.abs(fib.value(10) - 55) < 1e-9);
  const hanoi = solveClosed(2, 0, 1, 0, 1);
  for (let n = 0; n <= 10; n++) assert.ok(Math.abs(hanoi.value(n) - (2 ** n - 1)) < 1e-9, 'hanoi ' + n);
  assert.equal(solveClosed(4, -4, 0, 1, 2).kind, 'double');
  assert.equal(solveClosed(1, -1, 0, 1, 1).kind, 'complex');
});

test('công thức đóng khớp truy hồi với mọi hệ số nhỏ (kể cả nghiệm riêng n, n²)', () => {
  let cases = 0;
  for (let c1 = -3; c1 <= 3; c1++) for (let c2 = -3; c2 <= 3; c2++) for (const k of [0, 1, 2, -3]) for (const [a0, a1] of [[0, 1], [1, 3], [2, -1], [5, 0]]) {
    // order-1 (c2 = 0): a1 phải khớp truy hồi a1 = c1 a0 + k
    const A1 = c2 === 0 ? c1 * a0 + k : a1;
    const seq = terms(c1, c2, k, a0, A1, 12);
    const sol = solveClosed(c1, c2, k, a0, A1);
    for (let n = 0; n <= 12; n++) {
      const tol = 1e-6 * Math.max(1, Math.abs(seq[n]));
      assert.ok(Math.abs(sol.value(n) - seq[n]) < tol, `c1=${c1} c2=${c2} k=${k} a0=${a0} a1=${A1} n=${n}: ${sol.value(n)} vs ${seq[n]}`);
    }
    cases++;
  }
  assert.equal(cases, 7 * 7 * 4 * 4);
});

test('chia để trị: tổng khớp đệ quy và phân loại Master', () => {
  for (const [a, b, d] of [[2, 2, 1], [1, 2, 0], [3, 2, 1], [4, 2, 1], [2, 2, 2], [1, 2, 1]]) {
    for (let m = 1; m <= 6; m++) {
      const r = divideConquer(a, b, d, m);
      assert.equal(r.total, directT(a, b, d, b ** m), `a=${a} b=${b} d=${d} m=${m}`);
    }
  }
  assert.equal(divideConquer(2, 2, 1, 4).cls, 'balanced');
  assert.equal(divideConquer(4, 2, 1, 4).cls, 'leaves');
  assert.equal(divideConquer(1, 2, 1, 4).cls, 'root');
  assert.equal(divideConquer(2, 2, 1, 3).theta, 'Θ(n^1 log n)');
});

test('cây fib: số lời gọi = 2F(n+1) − 1', () => {
  const F = [0, 1]; for (let i = 2; i < 20; i++) F.push(F[i - 1] + F[i - 2]);
  for (let n = 0; n <= 10; n++) assert.equal(fibTree(n).calls, 2 * F[n + 1] - 1);
  assert.equal(fibTree(5).dupCalls, fibTree(5).calls - 6);
});
