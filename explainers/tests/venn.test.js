import test from 'node:test';
import assert from 'node:assert/strict';
import { parseSet, regionTable, sameSetFamily, parseElements, evaluateOnElements, inclusionExclusion, unionOfRegions, IDENTITIES } from '../src/venn/sets.js';

test('phân tích và vùng: A ∩ B′ trên 2 tập', () => {
  assert.deepEqual(regionTable(parseSet("A ∩ B'"), 2), [false, true, false, false]);
  assert.deepEqual(regionTable(parseSet('A Δ B'), 2), [false, true, true, false]);
  assert.deepEqual(regionTable(parseSet('A \\ B'), 2), [false, true, false, false]);
});

test('ưu tiên: ∩ chặt hơn ∪, bù hậu tố', () => {
  assert.deepEqual(regionTable(parseSet('A ∪ B ∩ C'), 3), regionTable(parseSet('A ∪ (B ∩ C)'), 3));
  assert.deepEqual(regionTable(parseSet("(A ∪ B)'"), 2), [true, false, false, false]);
});

test('các đẳng thức trong IDENTITIES đúng/sai như nhãn', () => {
  for (const id of IDENTITIES) {
    const r = sameSetFamily(parseSet(id.a), parseSet(id.b), id.k);
    assert.equal(r.equal, !id.label.includes('≠'), id.label);
  }
});

test('lỗi cú pháp có thông báo tiếng Việt', () => {
  assert.throws(() => parseSet('A ∪'), /chưa hoàn chỉnh/);
  assert.throws(() => parseSet('(A ∪ B'), /ngoặc/);
  assert.throws(() => parseSet('A ? B'), /Không hiểu/);
});

test('phần tử và kết quả trên dữ liệu', () => {
  const U = parseElements('1..8');
  assert.equal(U.length, 8);
  const A = ['1', '2', '3', '4'];
  const B = ['3', '4', '5', '6'];
  const { result } = evaluateOnElements(parseSet('A ∩ B'), 2, U, [A, B]);
  assert.deepEqual(result, ['3', '4']);
  assert.deepEqual(evaluateOnElements(parseSet("(A ∪ B)'"), 2, U, [A, B]).result, ['7', '8']);
});

test('bao hàm–loại trừ khớp |A ∪ B ∪ C| thực tế', () => {
  const A = ['1', '2', '3', '4', '5'];
  const B = ['4', '5', '6', '7'];
  const C = ['5', '7', '8', '9'];
  const ie = inclusionExclusion([A, B, C]);
  assert.equal(ie.total, ie.actual);
  assert.equal(ie.actual, 9);
  const ie2 = inclusionExclusion([A, B]);
  assert.equal(ie2.total, 7);
});

test('unionOfRegions sinh biểu thức tương đương', () => {
  const sel = regionTable(parseSet('A Δ B'), 2);
  const back = parseSet(unionOfRegions(sel, 2));
  assert.deepEqual(regionTable(back, 2), sel);
  assert.equal(unionOfRegions([false, false, false, false], 2), '∅');
});
