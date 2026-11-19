import test from 'node:test';
import assert from 'node:assert/strict';
import { gcd, lcm, extendedEuclid, euclidSteps, modInverse, solveLinearCongruence, modPow, modPowSteps, sieve, factorize, isPrime, phi, rsaKeys, rsaEncrypt, rsaDecrypt, modTable, crt, mod } from '../src/numtheory/numtheory.js';

test('Bézout: s·a + t·b = gcd, kể cả số âm/0', () => {
  for (let a = -30; a <= 30; a++) for (let b = -30; b <= 30; b++) {
    if (a === 0 && b === 0) continue;
    const r = extendedEuclid(a, b);
    assert.equal(r.g, gcd(a, b));
    assert.equal(r.x * a + r.y * b, r.g);
  }
  assert.equal(euclidSteps(252, 105).g, 21);
  assert.equal(euclidSteps(252, 105).steps.length, 3);
  assert.equal(lcm(4, 6), 12);
});

test('nghịch đảo modulo và đồng dư tuyến tính', () => {
  for (let n = 2; n < 40; n++) for (let a = 0; a < n; a++) {
    const inv = modInverse(a, n);
    if (gcd(a, n) === 1) assert.equal(mod(a * inv, n), 1 % n);
    else assert.equal(inv, null);
  }
  for (let n = 2; n < 25; n++) for (let a = 1; a < n; a++) for (let c = 0; c < n; c++) {
    const brute = []; for (let x = 0; x < n; x++) if (mod(a * x, n) === c) brute.push(x);
    assert.deepEqual(solveLinearCongruence(a, c, n).solutions.sort((p, q) => p - q), brute);
  }
});

test('lũy thừa nhanh khớp phép nhân lặp và các bước', () => {
  for (let m = 2; m < 30; m++) for (let b = 0; b < 12; b++) for (let e = 0; e < 20; e++) {
    let v = 1 % m; for (let i = 0; i < e; i++) v = (v * b) % m;
    assert.equal(Number(modPow(b, e, m)), v);
    if (e > 0) assert.equal(modPowSteps(b, e, m).result, v);
  }
  assert.equal(modPow(2n, 1000n, 1000000007n), 688423210n);
  assert.equal(modPowSteps(3, 13, 7).bits, '1101');
});

test('sàng Eratosthenes, phân tích, phi, Fermat', () => {
  const s = sieve(100);
  assert.equal(s.primes.length, 25);
  assert.deepEqual(s.steps.map((x) => x.p), [2, 3, 5, 7]);
  for (let n = 2; n <= 200; n++) assert.equal(isPrime(n), sieve(200).primes.includes(n));
  assert.deepEqual(factorize(360), [[2, 3], [3, 2], [5, 1]]);
  assert.equal(phi(36), 12);
  for (const p of [5, 7, 11, 13]) for (let a = 1; a < p; a++) assert.equal(modPow(a, p - 1, p), 1n);
});

test('RSA đồ chơi mã hóa/giải mã khứ hồi', () => {
  const k = rsaKeys(61, 53, 17);
  assert.equal(k.n, 3233); assert.equal(k.d, 2753);
  for (let m = 0; m < k.n; m += 37) assert.equal(rsaDecrypt(rsaEncrypt(m, k), k), m);
  assert.ok(rsaKeys(10, 7).error);
  const k2 = rsaKeys(11, 13, 4); // e không hợp lệ → tự chọn
  assert.equal(gcd(k2.e, k2.phi), 1);
  for (let m = 0; m < k2.n; m++) assert.equal(rsaDecrypt(rsaEncrypt(m, k2), k2), m);
});

test('bảng đồng dư và CRT', () => {
  assert.deepEqual(modTable(3, '+')[2], [2, 0, 1]);
  assert.deepEqual(modTable(4, '*')[2], [0, 2, 0, 2]);
  const r = crt(2, 3, 3, 5);
  assert.equal(r.x % 3, 2); assert.equal(r.x % 5, 3); assert.equal(r.mod, 15);
  assert.equal(crt(1, 4, 1, 6), null);
});
