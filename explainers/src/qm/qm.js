// Quine–McCluskey từng bước: dán cột, nguyên nhân nguyên tố, bảng phủ (cốt yếu, trội hàng/cột), Petrick.
// Logic thuần (không import Svelte); đã đối chiếu với tìm kiếm vét cạn trong tests/qm.test.js.

export const DEFAULT_NAMES = ['a', 'b', 'c', 'd', 'e', 'f'];

export const bitsOf = (m, n) => m.toString(2).padStart(n, '0');
export const literals = (bits) => [...bits].filter((c) => c !== '-').length;
export const popcount = (bits) => [...bits].filter((c) => c === '1').length;

/** Các minterm mà tích `bits` (có dấu -) phủ. */
export function coverOf(bits) {
  let list = [''];
  for (const c of bits) list = c === '-' ? list.flatMap((s) => [s + '0', s + '1']) : list.map((s) => s + c);
  return list.map((s) => parseInt(s, 2)).sort((a, b) => a - b);
}

export function termText(bits, names) {
  const parts = [];
  for (let i = 0; i < bits.length; i++) {
    if (bits[i] === '1') parts.push(names[i]);
    else if (bits[i] === '0') parts.push('¬' + names[i]);
  }
  return parts.length ? parts.join('') : '1';
}
export function sopText(terms, names) {
  if (!terms.length) return '0';
  return terms.map((t) => termText(t, names)).join(' + ');
}

/** "1, 5-7, 12" → [1,5,6,7,12] (loại trùng, kiểm tra miền). */
export function parseNums(text, n) {
  const max = 1 << n;
  const out = new Set();
  const errors = [];
  for (const tok of String(text).split(/[\s,;]+/).filter(Boolean)) {
    const m = tok.match(/^(\d+)(?:-(\d+))?$/);
    if (!m) { errors.push(`«${tok}» không phải số nguyên`); continue; }
    const a = Number(m[1]), b = m[2] === undefined ? a : Number(m[2]);
    for (let v = Math.min(a, b); v <= Math.max(a, b); v++) {
      if (v >= max) { errors.push(`${v} vượt quá 2^${n} − 1 = ${max - 1}`); break; }
      out.add(v);
    }
  }
  return { nums: [...out].sort((x, y) => x - y), errors };
}

const fmtList = (a) => (a.length ? a.join(', ') : '∅');
const minsText = (mins) => '(' + mins.join(',') + ')';

/** Chọn phủ nhỏ nhất (số hạng, rồi số literal) bằng nhánh–cận; dự phòng khi Petrick quá lớn. */
function bestCoverBB(cols, rowsOf, lit) {
  let best = null;
  const rec = (remaining, chosen, cost) => {
    if (best && (cost[0] > best.cost[0] || (cost[0] === best.cost[0] && cost[1] >= best.cost[1]))) return;
    if (!remaining.length) { best = { rows: [...chosen], cost: [...cost] }; return; }
    let pick = remaining[0];
    for (const c of remaining) if (rowsOf(c).length < rowsOf(pick).length) pick = c;
    for (const r of rowsOf(pick)) {
      const left = remaining.filter((c) => !rowsOf(c).includes(r));
      rec(left, [...chosen, r], [cost[0] + 1, cost[1] + lit(r)]);
    }
  };
  rec(cols, [], [0, 0]);
  return best;
}

const PETRICK_CAP = 4000;

export function runQM(n, onesIn, dcsIn, namesIn) {
  const names = namesIn && namesIn.length >= n ? namesIn.slice(0, n) : DEFAULT_NAMES.slice(0, n);
  const dcSet = new Set(dcsIn);
  const ones = [...new Set(onesIn)].filter((m) => !dcSet.has(m)).sort((a, b) => a - b);
  const dcs = [...dcSet].sort((a, b) => a - b);
  const steps = [];
  const out = { n, names, ones, dcs, columns: [], items: [], steps, primes: [], chart: null, picks: [], result: null };

  if (!ones.length) {
    steps.push({ phase: 1, kind: 'empty', title: 'Hàm hằng 0', text: 'Không có minterm bắt buộc (F = 1) nào, nên F = 0 — không cần lập bảng.' });
    out.result = { terms: [], text: '0', cost: [0, 0], alternatives: 1, verified: true };
    return out;
  }

  // ---------------- Phần 1: dán cột ----------------
  const mk = (col, bits, mins, step) => ({ id: `c${col}:${bits}`, col, bits, mins, ones: popcount(bits), used: false, usedStep: null, step, dcOnly: mins.every((m) => dcSet.has(m)) });
  let cur = [...ones, ...dcs].sort((a, b) => a - b).map((m) => mk(0, bitsOf(m, n), [m], 0));
  out.columns.push(cur);
  out.items.push(...cur);
  steps.push({
    phase: 1, kind: 'init', col: 0, title: 'Cột 1 — xếp theo số bit 1',
    text: `Đưa ${ones.length} minterm bắt buộc${dcs.length ? ` và ${dcs.length} don't-care (${fmtList(dcs)}) — don't-care chỉ giúp dán, chưa tính vào bảng phủ` : ''} vào cột 1, chia nhóm theo số bit 1 (nhóm 0, 1, 2, …).`
  });
  let col = 0;
  for (;;) {
    const groups = new Map();
    for (const it of cur) (groups.get(it.ones) || groups.set(it.ones, []).get(it.ones)).push(it);
    const keys = [...groups.keys()].sort((a, b) => a - b);
    const next = new Map();
    let produced = 0;
    for (const k of keys) {
      if (!groups.has(k + 1)) continue;
      const combos = [];
      const stepIdx = steps.length;
      for (const a of groups.get(k)) for (const b of groups.get(k + 1)) {
        let diff = -1, cnt = 0;
        for (let i = 0; i < n; i++) if (a.bits[i] !== b.bits[i]) { cnt++; diff = i; }
        if (cnt !== 1 || a.bits[diff] === '-' || b.bits[diff] === '-') continue;
        const bits = a.bits.slice(0, diff) + '-' + a.bits.slice(diff + 1);
        const mins = [...new Set([...a.mins, ...b.mins])].sort((x, y) => x - y);
        let res = next.get(bits);
        const isNew = !res;
        if (!res) { res = mk(col + 1, bits, mins, stepIdx); next.set(bits, res); out.items.push(res); produced++; }
        else res.step = Math.min(res.step, stepIdx);
        for (const it of [a, b]) { it.used = true; if (it.usedStep === null) it.usedStep = stepIdx; }
        combos.push({ a: a.id, b: b.id, res: res.id, isNew, bits });
      }
      steps.push({
        phase: 1, kind: 'pair', col, k, combos, title: `Cột ${col + 1}: so nhóm ${k} với nhóm ${k + 1}`,
        text: combos.length
          ? `So từng cặp giữa nhóm ${k} bit 1 và nhóm ${k + 1} bit 1; cặp khác đúng một bit thì dán, bit khác thay bằng «-». Dán được ${combos.length} cặp: ${combos.map((c) => `${out.items.find((x) => x.id === c.a).mins.length === 1 ? out.items.find((x) => x.id === c.a).mins[0] : minsText(out.items.find((x) => x.id === c.a).mins)} + ${out.items.find((x) => x.id === c.b).mins.length === 1 ? out.items.find((x) => x.id === c.b).mins[0] : minsText(out.items.find((x) => x.id === c.b).mins)} → ${c.bits}`).join('; ')}. Hai mục tham gia được đánh dấu ✓ (không phải nguyên nhân nguyên tố).`
          : `Không có cặp nào khác đúng một bit giữa nhóm ${k} và nhóm ${k + 1} (hoặc dấu «-» không thẳng hàng), nên không dán được.`
      });
    }
    const nextItems = [...next.values()];
    if (!nextItems.length) {
      steps.push({ phase: 1, kind: 'colEnd', col, final: true, title: `Cột ${col + 1} — không dán được nữa`, text: `Cột ${col + 1} không sinh thêm mục nào, nên dừng. Mọi mục chưa có ✓ ở mọi cột là các nguyên nhân nguyên tố.` });
      break;
    }
    col += 1;
    cur = nextItems.sort((x, y) => x.ones - y.ones || (x.bits < y.bits ? -1 : 1));
    out.columns.push(cur);
    steps.push({ phase: 1, kind: 'colEnd', col: col - 1, final: false, title: `Hết cột ${col}`, text: `Cột ${col + 1} gồm ${cur.length} mục: ${cur.map((i) => i.bits).join(', ')}. Lặp lại việc dán cho cột này (chỉ dán được khi dấu «-» nằm cùng vị trí).` });
  }

  // nguyên nhân nguyên tố = mọi mục không có ✓
  out.primes = out.items.filter((i) => !i.used).sort((a, b) => literals(a.bits) - literals(b.bits) || (a.bits < b.bits ? -1 : 1));
  steps.push({
    phase: 1, kind: 'primes', title: 'Các nguyên nhân nguyên tố',
    text: `Có ${out.primes.length} nguyên nhân nguyên tố (mục không có ✓): ${out.primes.map((p) => `${p.bits} = ${termText(p.bits, names)} ${minsText(p.mins)}`).join('; ')}.`
  });

  // ---------------- Phần 2: bảng phủ ----------------
  const rows = out.primes.filter((p) => p.mins.some((m) => !dcSet.has(m)));
  const dropped = out.primes.filter((p) => !rows.includes(p));
  const rowCols = (r) => r.mins.filter((m) => !dcSet.has(m));
  const lit = (rid) => literals(rows.find((r) => r.id === rid).bits);
  const snap = (activeRows, activeCols, picked, extra = {}) => ({ activeRows: [...activeRows], activeCols: [...activeCols], picked: [...picked], ...extra });
  let aRows = rows.map((r) => r.id);
  let aCols = [...ones];
  const picked = [];
  out.chart = { rows, cols: ones, dropped };
  steps.push({
    phase: 2, kind: 'chart', title: 'Lập bảng phủ',
    text: `Hàng = ${rows.length} nguyên nhân nguyên tố, cột = ${ones.length} minterm bắt buộc (don't-care không có cột${dropped.length ? `; ${dropped.map((d) => d.bits).join(', ')} chỉ phủ don't-care nên bị loại` : ''}). Dấu ● nghĩa là hàng phủ cột.`,
    ...snap(aRows, aCols, picked)
  });
  const rowsOf = (c) => aRows.filter((rid) => rowCols(rows.find((r) => r.id === rid)).includes(c));
  const colsOf = (rid) => rowCols(rows.find((r) => r.id === rid)).filter((c) => aCols.includes(c));
  const rowLabel = (rid) => { const r = rows.find((x) => x.id === rid); return `${r.bits} (${termText(r.bits, names)})`; };

  for (let guard = 0; guard < 500 && aCols.length; guard++) {
    // 1. nguyên tố cốt yếu
    const single = aCols.find((c) => rowsOf(c).length === 1);
    if (single !== undefined) {
      const rid = rowsOf(single)[0];
      const covered = colsOf(rid);
      picked.push(rid);
      aRows = aRows.filter((x) => x !== rid);
      aCols = aCols.filter((c) => !covered.includes(c));
      steps.push({ phase: 2, kind: 'essential', rid, col: single, covered, title: 'Nguyên tố cốt yếu',
        text: `Cột ${single} chỉ có đúng một dấu ● (hàng ${rowLabel(rid)}), nên hàng này BẮT BUỘC chọn — nguyên nhân nguyên tố cốt yếu. Chọn nó rồi xóa các cột nó phủ: ${fmtList(covered)}.`,
        ...snap(aRows, aCols, picked, { hiRow: rid, hiCols: covered }) });
      continue;
    }
    // loại hàng rỗng
    const empty = aRows.find((rid) => !colsOf(rid).length);
    if (empty) {
      aRows = aRows.filter((x) => x !== empty);
      steps.push({ phase: 2, kind: 'dropRow', rid: empty, title: 'Xóa hàng rỗng', text: `Hàng ${rowLabel(empty)} không còn phủ cột nào còn lại nên xóa.`, ...snap(aRows, aCols, picked, { hiRow: empty }) });
      continue;
    }
    // 2. trội hàng
    let rd = null;
    outer: for (const r of aRows) for (const r2 of aRows) {
      if (r === r2) continue;
      const A = colsOf(r), B = colsOf(r2);
      if (!A.every((c) => B.includes(c))) continue;
      const la = lit(r), lb = lit(r2);
      if (lb > la) continue;
      if (A.length === B.length && lb === la && aRows.indexOf(r2) > aRows.indexOf(r)) continue;
      rd = { r, r2 }; break outer;
    }
    if (rd) {
      aRows = aRows.filter((x) => x !== rd.r);
      steps.push({ phase: 2, kind: 'rowDom', rid: rd.r, by: rd.r2, title: 'Trội hàng',
        text: colsOf(rd.r).length === colsOf(rd.r2).length && lit(rd.r) === lit(rd.r2)
          ? `Hàng ${rowLabel(rd.r)} và hàng ${rowLabel(rd.r2)} phủ đúng cùng các cột còn lại với cùng số literal — hai hàng ngang nhau, giữ ${rowLabel(rd.r2)} và bỏ hàng kia (phương án thay thế cho cùng chi phí).`
          : `Hàng ${rowLabel(rd.r2)} phủ mọi cột mà hàng ${rowLabel(rd.r)} phủ (và không nhiều literal hơn) — hàng ${rowLabel(rd.r)} bị trội nên xóa.`,
        ...snap(aRows, aCols, picked, { hiRow: rd.r2, hiCols: colsOf(rd.r2), removedRow: rd.r }) });
      continue;
    }
    // 3. trội cột
    let cd = null;
    outer2: for (const c of aCols) for (const c2 of aCols) {
      if (c === c2) continue;
      const A = rowsOf(c), B = rowsOf(c2);
      if (!B.every((r) => A.includes(r))) continue;
      if (A.length === B.length && aCols.indexOf(c) < aCols.indexOf(c2)) continue; // cột giống nhau: giữ cột đầu
      cd = { c, c2 }; break outer2;
    }
    if (cd) {
      aCols = aCols.filter((x) => x !== cd.c);
      steps.push({ phase: 2, kind: 'colDom', col: cd.c, by: cd.c2, title: 'Trội cột',
        text: `Mọi hàng phủ cột ${cd.c2} cũng phủ cột ${cd.c}; phủ được cột ${cd.c2} thì cột ${cd.c} tự được phủ, nên xóa cột ${cd.c}${rowsOf(cd.c).length === rowsOf(cd.c2).length ? ' (hai cột giống nhau)' : ''}.`,
        ...snap(aRows, aCols, picked, { hiCols: [cd.c2], removedCol: cd.c }) });
      continue;
    }
    break;
  }

  // 4. Petrick cho phần còn lại (lõi vòng)
  let petrickChoice = [];
  let alternatives = 1;
  if (aCols.length) {
    const clauses = aCols.map((c) => ({ col: c, rows: rowsOf(c) }));
    const idx = new Map(aRows.map((rid, i) => [rid, i]));
    const letter = (rid) => 'P' + (idx.get(rid) + 1);
    steps.push({ phase: 2, kind: 'petrickSetup', title: "Phương pháp Petrick",
      text: `Còn lõi vòng chưa quyết định được: ${aCols.length} cột × ${aRows.length} hàng. Với mỗi cột, ít nhất MỘT hàng phủ nó phải được chọn: ${clauses.map((c) => `m${c.col}: (${c.rows.map(letter).join(' + ')})`).join(' · ')}. Nhân các tổng này (luật hấp thụ X + XY = X) rồi chọn tích nhỏ nhất.`,
      letters: aRows.map((rid) => ({ rid, p: letter(rid) })),
      ...snap(aRows, aCols, picked) });
    const maskOf = (rid) => 1n << BigInt(idx.get(rid));
    const pop = (m) => { let c = 0; while (m) { c += Number(m & 1n); m >>= 1n; } return c; };
    const absorb = (list) => {
      const u = [...new Set(list.map(String))].map(BigInt).sort((a, b) => pop(a) - pop(b) || (a < b ? -1 : 1));
      const kept = [];
      for (const m of u) if (!kept.some((k) => (k & m) === k)) kept.push(m);
      return kept;
    };
    const show = (m) => aRows.filter((rid) => m & maskOf(rid)).map(letter).join('');
    let prod = [0n];
    let fallback = false;
    for (let i = 0; i < clauses.length; i++) {
      const expanded = [];
      for (const t of prod) for (const rid of clauses[i].rows) expanded.push(t | maskOf(rid));
      prod = absorb(expanded);
      steps.push({ phase: 2, kind: 'petrickMul', i, title: `Nhân thừa số ${i + 1}/${clauses.length}`,
        text: `Nhân thêm (${clauses[i].rows.map(letter).join(' + ')}) và hấp thụ: còn ${prod.length} tích${prod.length <= 10 ? ': ' + prod.map(show).join(' + ') : ' (hiển thị 10 đầu): ' + prod.slice(0, 10).map(show).join(' + ') + ' + …'}.`,
        ...snap(aRows, aCols, picked, { hiCols: [clauses[i].col] }) });
      if (prod.length > PETRICK_CAP) { fallback = true; break; }
    }
    let best;
    if (!fallback) {
      const costOf = (m) => [pop(m), aRows.reduce((s, rid) => s + (m & maskOf(rid) ? lit(rid) : 0), 0)];
      const scored = prod.map((m) => ({ m, cost: costOf(m) })).sort((a, b) => a.cost[0] - b.cost[0] || a.cost[1] - b.cost[1]);
      const top = scored[0];
      alternatives = scored.filter((s) => s.cost[0] === top.cost[0] && s.cost[1] === top.cost[1]).length;
      best = aRows.filter((rid) => top.m & maskOf(rid));
      steps.push({ phase: 2, kind: 'petrickPick', title: 'Chọn tích nhỏ nhất',
        text: `Mỗi tích trong kết quả là một cách phủ đủ. Chọn tích ít hạng nhất, hòa thì ít literal nhất: ${show(top.m)} (${top.cost[0]} hạng, ${top.cost[1]} literal)${alternatives > 1 ? `; còn ${alternatives - 1} phương án tối ưu khác cùng chi phí` : ''}.`,
        candidates: scored.slice(0, 8).map((s) => ({ label: show(s.m), cost: s.cost })),
        ...snap(aRows, aCols, picked, { petrickRows: best }) });
    } else {
      const bb = bestCoverBB(aCols, rowsOf, lit);
      best = bb.rows;
      steps.push({ phase: 2, kind: 'petrickPick', title: 'Chọn phủ nhỏ nhất (nhánh–cận)',
        text: `Tích Petrick quá lớn (> ${PETRICK_CAP} tích) nên dùng tìm kiếm nhánh–cận cho cùng mục tiêu: chọn ${best.map(letter).join(', ')} (${bb.cost[0]} hạng, ${bb.cost[1]} literal).`,
        candidates: [], ...snap(aRows, aCols, picked, { petrickRows: best }) });
    }
    petrickChoice = best;
  }

  const finalRows = [...picked, ...petrickChoice];
  out.picks = finalRows.map((rid) => rows.find((r) => r.id === rid));
  const terms = out.picks.map((r) => r.bits).sort();
  const cost = [terms.length, terms.reduce((s, t) => s + literals(t), 0)];
  const covered = new Set(terms.flatMap(coverOf));
  const verified = ones.every((m) => covered.has(m)) && [...covered].every((m) => dcSet.has(m) || ones.includes(m));
  out.result = { terms, text: sopText(terms, names), cost, alternatives, verified };
  steps.push({ phase: 2, kind: 'result', title: 'Kết quả — SOP tối tiểu',
    text: `F = ${out.result.text}  (${cost[0]} hạng, ${cost[1]} literal). Kiểm tra: phủ đủ ${ones.length} minterm bắt buộc và không phủ ô nào ngoài minterm/don't-care — ${verified ? 'đúng' : 'SAI'}.`,
    ...snap([], [], picked, { petrickRows: petrickChoice, final: finalRows }) });
  return out;
}

/** Giá trị hàm (0/1/2=dc) từ danh sách minterm/dc. */
export function valuesFrom(n, ones, dcs) {
  const v = new Array(1 << n).fill(0);
  for (const m of dcs) v[m] = 2;
  for (const m of ones) v[m] = 1;
  return v;
}

export const PRESETS = [
  { id: 'f1', label: 'F₁ (mục 5b): w x y z — 5, 6, 7, 9, 11, 15', n: 4, names: ['w', 'x', 'y', 'z'], ones: '5,6,7,9,11,15', dc: '' },
  { id: 'dc3', label: 'Có don\'t-care (mục 4): a b c — 1, 2, 5; d: 0, 7', n: 3, names: ['a', 'b', 'c'], ones: '1,2,5', dc: '0,7' },
  { id: 'four', label: 'Ví dụ bốn biến (mục 5): 0,2,3,5,7,8,10,11,13,15', n: 4, names: ['a', 'b', 'c', 'd'], ones: '0,2,3,5,7,8,10,11,13,15', dc: '', note: 'Khớp với bài (mục 5): ¬b¬d và bd là nguyên tố cốt yếu (bd là hàng duy nhất phủ m5, m13); cd (hoặc ¬bc, cùng chi phí) phủ nốt m3, m11. SOP tối tiểu: bd + cd + ¬b¬d.' },
  { id: 'cyclic', label: 'Lõi vòng → Petrick: 0,1,2,5,6,7 (3 biến)', n: 3, names: ['a', 'b', 'c'], ones: '0,1,2,5,6,7', dc: '' },
  { id: 'five', label: 'Năm biến: 0,1,2,5,7,8,9,10,14,15,16,18,20,21,23,26', n: 5, names: ['a', 'b', 'c', 'd', 'e'], ones: '0,1,2,5,7,8,9,10,14,15,16,18,20,21,23,26', dc: '' },
  { id: 'six', label: 'Sáu biến: 0-7, 16-19, 40, 42, 56-63; d: 20, 21', n: 6, names: ['a', 'b', 'c', 'd', 'e', 'f'], ones: '0-7,16-19,40,42,56-63', dc: '20,21' }
];
