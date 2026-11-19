import test from 'node:test';
import assert from 'node:assert/strict';
import { modPow, modInv, crtSolve, millerRabinSteps, isProbablePrime, dhSteps } from '../src/numtheory/crypto.js';

const isPrime = (n) => { if (n < 2) return false; for (let d = 2; d * d <= n; d++) if (n % d === 0) return false; return true; };

test('CRT: nghiệm thỏa mọi đồng dư và nằm trong [0, M)', () => {
  const r = crtSolve([2, 3, 2], [3, 5, 7]);
  assert.equal(r.x, 23n); assert.equal(r.M, 105n);
  const mods = [[3, 5], [4, 9, 5], [7, 11, 13], [8, 15, 7]];
  for (const ms of mods) for (let t = 0; t < 40; t++) {
    const as = ms.map((m, i) => (t * (i + 3) + 5 * i) % m);
    const s = crtSolve(as, ms);
    assert.ok(s.check.every((c) => c.ok));
    assert.ok(s.x >= 0n && s.x < s.M);
    s.steps.forEach((st) => assert.equal((st.Mi * st.yi) % st.mi, 1n));
  }
  assert.ok(crtSolve([1, 2], [4, 6]).error);
});

test('Miller–Rabin: khớp chia thử cho n < 20000; giả nguyên tố mạnh', () => {
  for (let n = 2; n < 20000; n++) assert.equal(isProbablePrime(n, [2, 3, 5, 7]), isPrime(n), 'n=' + n);
  assert.equal(millerRabinSteps(2047, 2).pass, true);   // 2047 = 23·89 là giả nguyên tố mạnh cơ sở 2
  assert.equal(millerRabinSteps(2047, 3).pass, false);
  assert.equal(millerRabinSteps(561, 2).pass, false);   // số Carmichael bị lộ
  assert.equal(millerRabinSteps(221, 174).pass, true);  // 221 = 13·17, cơ sở nói dối
  const s = millerRabinSteps(561, 2);
  assert.equal(2n ** BigInt(s.s) * s.d, 560n);
  assert.equal(isProbablePrime(1000000007n), true);
  assert.equal(isProbablePrime(1000000007n * 998244353n), false);
});

test('Diffie–Hellman: hai bên ra cùng bí mật; Eve dò log rời rạc', () => {
  for (const [p, g] of [[23, 5], [29, 2], [101, 2], [1019, 2]]) for (let a = 2; a < 10; a++) for (let b = 3; b < 9; b++) {
    const d = dhSteps(p, g, a, b);
    assert.equal(d.sA, d.sB);
    assert.equal(modPow(g, d.eve.found, p), d.A);
    assert.equal(d.eve.secret, d.sA);
  }
  assert.equal(modPow(5, 6, 23), 8n);
  assert.equal(modInv(3n, 7n), 5n);
});
