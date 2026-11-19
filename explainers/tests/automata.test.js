import test from 'node:test';
import assert from 'node:assert/strict';
import { PRESETS, simulate, accepts, subsetConstruction, minimizeDFA, stringsUpTo, isDFA, isComplete, epsClosure, alphabetOf, EPS } from '../src/automata/automata.js';

const preset = (id) => PRESETS.find((p) => p.id === id).make();

test('DFA kết thúc bằng 01 và chẵn số 1', () => {
  const M = preset('dfa01');
  assert.ok(isDFA(M) && isComplete(M));
  for (const w of stringsUpTo(['0', '1'], 8)) assert.equal(accepts(M, w), w.endsWith('01'), w);
  const E = preset('even1');
  for (const w of stringsUpTo(['0', '1'], 8)) assert.equal(accepts(E, w), (w.match(/1/g) || []).length % 2 === 0, w);
});

test('NFA chứa 101, ký tự thứ 3 từ cuối là 1', () => {
  const M = preset('nfa101');
  assert.ok(!isDFA(M));
  for (const w of stringsUpTo(['0', '1'], 9)) assert.equal(accepts(M, w), w.includes('101'), w);
  const T = preset('nfa3');
  for (const w of stringsUpTo(['0', '1'], 9)) assert.equal(accepts(T, w), w.length >= 3 && w[w.length - 3] === '1', w);
});

test('ε-NFA: a*b* và đóng ε', () => {
  const M = preset('enfa');
  assert.deepEqual(epsClosure(M, ['p']), ['p', 'r']);
  for (const w of stringsUpTo(['a', 'b'], 8)) assert.equal(accepts(M, w), /^a*b*$/.test(w), w);
});

test('subset construction: tương đương NFA trên mọi chuỗi ≤ 9; kích thước đúng', () => {
  for (const id of ['nfa101', 'nfa3', 'enfa', 'dfa01']) {
    const M = preset(id);
    const { dfa, rows } = subsetConstruction(M);
    assert.ok(isDFA(dfa) && isComplete(dfa), id + ' DFA đầy đủ');
    const A = alphabetOf(M);
    for (const w of stringsUpTo(A, 9)) assert.equal(accepts(dfa, w), accepts(M, w), `${id} ${w}`);
    if (id === 'nfa3') assert.equal(rows.length, 8);
  }
});

test('subset construction trên NFA ngẫu nhiên (có ε)', () => {
  let seed = 7;
  const rnd = () => (seed = (seed * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff;
  for (let t = 0; t < 150; t++) {
    const n = 2 + Math.floor(rnd() * 4);
    const ids = Array.from({ length: n }, (_, i) => 'q' + i);
    const edges = [];
    for (const a of ids) for (const b of ids) {
      const syms = ['a', 'b', EPS].filter((_, i) => rnd() < (i === 2 ? 0.12 : 0.25));
      if (syms.length) edges.push({ from: a, to: b, syms });
    }
    const M = { states: ids.map((id) => ({ id, x: 0, y: 0 })), start: 'q0', accept: ids.filter(() => rnd() < 0.4), edges };
    const { dfa } = subsetConstruction(M);
    for (const w of stringsUpTo(['a', 'b'], 6)) assert.equal(accepts(dfa, w), accepts(M, w), `t=${t} w=${w}`);
  }
});

test('tối thiểu hóa DFA: ngôn ngữ giữ nguyên, "kết thúc 01" có 3 trạng thái', () => {
  const D = subsetConstruction(preset('nfa101')).dfa;
  const { machine, groups } = minimizeDFA(D);
  assert.ok(groups.length <= D.states.length);
  for (const w of stringsUpTo(['0', '1'], 9)) assert.equal(accepts(machine, w), accepts(D, w), w);
  assert.equal(minimizeDFA(preset('dfa01')).groups.length, 3);
  // một DFA thừa trạng thái: hai bản sao của "chẵn 1"
  const dup = {
    states: ['a', 'b', 'c', 'd'].map((id) => ({ id, x: 0, y: 0 })), start: 'a', accept: ['a', 'c'],
    edges: [{ from: 'a', to: 'a', syms: ['0'] }, { from: 'a', to: 'b', syms: ['1'] }, { from: 'b', to: 'b', syms: ['0'] }, { from: 'b', to: 'c', syms: ['1'] },
      { from: 'c', to: 'c', syms: ['0'] }, { from: 'c', to: 'd', syms: ['1'] }, { from: 'd', to: 'd', syms: ['0'] }, { from: 'd', to: 'a', syms: ['1'] }]
  };
  assert.equal(minimizeDFA(dup).groups.length, 2);
});

test('mô phỏng trả về vết đúng độ dài', () => {
  const r = simulate(preset('nfa3'), '0100');
  assert.equal(r.trace.length, 5);
  assert.equal(r.accept, true); // ký tự thứ 3 từ cuối là 1
  assert.equal(simulate(preset('nfa3'), '0010').accept, false);
  assert.equal(simulate(preset('nfa3'), '100').accept, true);
});
