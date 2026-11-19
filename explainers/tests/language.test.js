import test from 'node:test';
import assert from 'node:assert/strict';
import { parseGrammar, checkCNF, cykSteps, enumerateLanguage, parseTrees, treeYield, internalCount, leftmostDerivation, layoutTree, CYK_PRESETS, TREE_PRESETS } from '../src/language/grammar.js';
import { TM_PRESETS, runTM } from '../src/language/tm.js';
import { PDA_PRESETS, runPDA } from '../src/language/pda.js';

function allStrings(alpha, L) {
  let out = [[]], cur = [[]];
  for (let l = 1; l <= L; l++) { cur = cur.flatMap((s) => alpha.map((a) => [...s, a])); out = out.concat(cur); }
  return out;
}

test('CYK khớp liệt kê ngôn ngữ trên mọi chuỗi độ dài ≤ 6', () => {
  for (const p of CYK_PRESETS.slice(0, 2)) {
    const g = parseGrammar(p.text);
    assert.equal(checkCNF(g), null);
    const terms = [...new Set(g.rules.filter((r) => r.rhs.length === 1).map((r) => r.rhs[0]))];
    const lang = enumerateLanguage(g, 6);
    for (const s of allStrings(terms, 6)) {
      if (!s.length) continue;
      assert.equal(cykSteps(g, s).accepted, lang.has(s.join(' ')), p.id + ' ' + s.join(''));
    }
  }
});
test('CYK: ví dụ baaba thuộc, abab của aⁿbⁿ không thuộc; CNF sai bị báo', () => {
  const g = parseGrammar(CYK_PRESETS[0].text);
  assert.ok(cykSteps(g, 'b a a b a'.split(' ')).accepted);
  const h = parseGrammar(CYK_PRESETS[2].text);
  assert.ok(!cykSteps(h, 'a b a b'.split(' ')).accepted);
  assert.ok(checkCNF(parseGrammar('S -> a b')));
  assert.ok(parseGrammar('S a').error);
});

test('cây phân tích: số cây, yield, dẫn xuất trái nhất', () => {
  const expect = { 'expr-amb': 2, 'expr-unamb': 1, else: 2, paren: 2 };
  for (const p of TREE_PRESETS) {
    const g = parseGrammar(p.text);
    const toks = p.input.split(' ');
    const { trees } = parseTrees(g, toks);
    assert.equal(trees.length, expect[p.id], p.id);
    for (const t of trees) {
      assert.deepEqual(treeYield(t), toks);
      const d = leftmostDerivation(t);
      assert.deepEqual(d[d.length - 1].form, toks);
      assert.equal(d.length - 1, internalCount(t));
      for (const st of d.slice(1)) {
        const [A, ...rhs] = st.rule.split(' → ').flatMap((x) => x.split(' '));
        assert.ok(g.rules.some((r) => r.lhs === A && r.rhs.join(' ') === rhs.join(' ')));
      }
      const L = layoutTree(t);
      assert.equal(L.width, toks.length);
    }
  }
});
test('cây phân tích: hai cây của id+id*id khác nhau; chuỗi sai không có cây', () => {
  const g = parseGrammar(TREE_PRESETS[0].text);
  const { trees } = parseTrees(g, 'id + id * id'.split(' '));
  assert.notEqual(JSON.stringify(trees[0], (k, v) => (k === 'id' ? undefined : v)), JSON.stringify(trees[1], (k, v) => (k === 'id' ? undefined : v)));
  assert.equal(parseTrees(g, 'id + + id'.split(' ')).trees.length, 0);
});

test('máy Turing: tăng 1, 0ⁿ1ⁿ, cộng đơn phân', () => {
  const [inc, anbn, un] = TM_PRESETS;
  for (let x = 0; x < 200; x++) {
    const w = x.toString(2);
    const r = runTM(inc, w);
    assert.equal(r.status, 'accept');
    assert.equal(r.output, (x + 1).toString(2));
  }
  for (const s of allStrings(['0', '1'], 8)) {
    const w = s.join('');
    if (!w) continue;
    const r = runTM(anbn, w);
    assert.equal(r.status === 'accept', anbn.oracle(w) === 'accept', w);
  }
  for (let a = 0; a < 6; a++) for (let b = 0; b < 6; b++) {
    const w = '1'.repeat(a) + '+' + '1'.repeat(b);
    const r = runTM(un, w);
    if (a + b > 0 && b > 0) { assert.equal(r.status, 'accept'); assert.equal(r.output, '1'.repeat(a + b)); }
  }
});

test('PDA: khớp vị từ trên mọi chuỗi độ dài ≤ 8', () => {
  for (const p of PDA_PRESETS) {
    const alpha = p.id === 'anbn' ? ['a', 'b'] : p.id === 'ww' ? ['0', '1'] : ['(', ')'];
    for (const s of allStrings(alpha, 8)) {
      const w = s.join('');
      assert.equal(runPDA(p, w).accepted, p.oracle(w), p.id + ' ' + w);
    }
  }
});
