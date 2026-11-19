import test from 'node:test';
import assert from 'node:assert/strict';
import { parseRegex, thompson, machineAt, eliminationSteps, toJsRegExp, REGEX_PRESETS, ELIM_PRESETS, showRegex } from '../src/language/regex.js';
import { accepts, stringsUpTo } from '../src/automata/automata.js';
import { MEALY_PRESETS, runTransducer } from '../src/language/mealy.js';
import { PUMP_LANGS, evaluate } from '../src/language/pumping.js';
import { runCfgPda } from '../src/language/cfgpda.js';
import { parseGrammar, parseTrees, TREE_PRESETS } from '../src/language/grammar.js';

const strs = (alpha, L) => stringsUpTo(alpha.split(''), L);

test('Thompson: NFA khớp RegExp của JS trên mọi chuỗi ≤ 6', () => {
  for (const p of [...REGEX_PRESETS, { text: '(ab|b)*a?' }, { text: 'a|ε' }]) {
    const ast = parseRegex(p.text);
    const T = thompson(ast);
    const alpha = [...new Set(p.text.match(/[a-z0-9]/g))].join('') || 'a';
    const js = new RegExp('^(?:' + p.text.replace(/ε/g, '(?:)') + ')$');
    for (const w of strs(alpha, 6)) assert.equal(accepts(T.machine, w), js.test(w), p.text + ' / ' + w);
    // số trạng thái của Thompson ≤ 2·(số ký hiệu)
    assert.ok(T.machine.states.length <= 4 * p.text.replace(/[()]/g, '').length);
    // các bước tăng dần: máy ở bước cuối đủ trạng thái
    assert.equal(machineAt(T, T.steps.length - 1).states.length, T.machine.states.length);
  }
  assert.throws(() => parseRegex('(a'));
  assert.throws(() => parseRegex('a$'));
  assert.equal(showRegex(parseRegex('a(b|c)*')), 'a(b|c)*');
});

test('loại trạng thái: regex sinh ra tương đương otomat (mọi chuỗi ≤ 7, hai thứ tự)', () => {
  for (const pr of ELIM_PRESETS) {
    const M = pr.make();
    const alpha = pr.alpha;
    const ids = M.states.map((s) => s.id);
    for (const order of [ids, [...ids].reverse()]) {
      const { regex, steps } = eliminationSteps(M, order);
      assert.ok(regex !== null);
      const re = toJsRegExp(regex);
      for (const w of strs(alpha, 7)) assert.equal(re.test(w), accepts(M, w), `${pr.id} ${order} ${regex} / ${w}`);
      assert.equal(steps.length, ids.length + 2);
    }
  }
});

test('Mealy/Moore: khớp hàm tham chiếu', () => {
  for (const p of MEALY_PRESETS) {
    const r = runTransducer(p, p.input);
    assert.deepEqual(r.outputs, p.ref(p.input.includes(' ') ? p.input : p.input), p.id);
  }
  const add = MEALY_PRESETS.find((p) => p.id === 'add');
  for (let a = 0; a < 32; a++) for (let b = 0; b < 32; b += 3) {
    const bitsA = a.toString(2).padStart(6, '0').split('').reverse(), bitsB = b.toString(2).padStart(6, '0').split('').reverse();
    const inp = bitsA.map((x, i) => x + bitsB[i]).join(' ') + ' 00';
    const out = runTransducer(add, inp).outputs.reverse().join('');
    assert.equal(parseInt(out, 2), a + b);
  }
  assert.ok(runTransducer(MEALY_PRESETS[0], '012').error);
});

test('bổ đề bơm: ngôn ngữ không chính quy / không phi ngữ cảnh không có cách chia nào bơm được', () => {
  const find = (k, id) => PUMP_LANGS[k].find((l) => l.id === id);
  for (const id of ['anbn', 'pal']) for (let p = 1; p <= 7; p++) {
    const L = find('regular', id);
    assert.ok(evaluate(L, 'regular', L.word(p), p).every((r) => !r.survives), id + p);
  }
  for (let p = 1; p <= 4; p++) {
    const L = find('cfl', 'anbncn');
    assert.ok(evaluate(L, 'cfl', L.word(p), p).every((r) => !r.survives), 'anbncn' + p);
  }
  for (let p = 1; p <= 3; p++) { const L = find('cfl', 'ww'); assert.ok(evaluate(L, 'cfl', L.word(p), p).every((r) => !r.survives), 'ww' + p); }
  const ab = find('regular', 'abstar');
  for (let p = 2; p <= 5; p++) assert.ok(evaluate(ab, 'regular', ab.word(p), p).some((r) => r.survives));
  const cf = find('cfl', 'anbn');
  for (let p = 2; p <= 4; p++) assert.ok(evaluate(cf, 'cfl', cf.word(p), p).some((r) => r.survives), 'anbn cfl ' + p);
});

test('CFG → PDA: chấp nhận đúng khi và chỉ khi có cây phân tích', () => {
  for (const pr of TREE_PRESETS) {
    const g = parseGrammar(pr.text);
    const terms = [...new Set(g.rules.flatMap((r) => r.rhs).filter((x) => !g.isVar(x)))];
    const L = pr.id === 'else' ? 0 : pr.id === 'expr-amb' || pr.id === 'expr-unamb' ? 4 : 5;
    const gen = (len) => (len === 0 ? [[]] : gen(len - 1).flatMap((w) => terms.map((t) => [...w, t])));
    for (let len = 1; len <= L; len++) for (const w of gen(len)) {
      assert.equal(runCfgPda(g, w).accepted, parseTrees(g, w).trees.length > 0, pr.id + ' ' + w.join(' '));
    }
    const full = pr.input.split(' ');
    assert.ok(runCfgPda(g, full).accepted, pr.id + ' preset');
  }
});
