// DPLL: lan truyền đơn vị + quyết định + quay lui. Hàm thuần.

/** Đọc CNF: các mệnh đề cách nhau bởi ',' ';' '∧' hoặc xuống dòng; literal cách nhau bởi khoảng trắng, '∨' hay '|'; phủ định: ¬ ! ~ - */
export function parseCNF(text) {
  const names = [];
  const idx = (nm) => { let i = names.indexOf(nm); if (i < 0) { names.push(nm); i = names.length - 1; } return i + 1; };
  const clauses = [];
  const parts = String(text).split(/[,;∧\n]|&&|\)\s*\(/);
  for (const raw of parts) {
    const toks = raw.replace(/[()]/g, ' ').split(/[\s∨|]+/).filter(Boolean);
    if (!toks.length) continue;
    const lits = [];
    for (const t of toks) {
      const m = /^([¬!~-]*)([A-Za-z_][A-Za-z0-9_]*|\d+)$/.exec(t);
      if (!m) return { error: `Không đọc được literal “${t}”.` };
      const neg = m[1].length % 2 === 1;
      const v = idx(m[2]);
      lits.push(neg ? -v : v);
    }
    clauses.push([...new Set(lits)]);
  }
  if (!clauses.length) return { error: 'Chưa có mệnh đề nào.' };
  if (names.length > 8) return { error: 'Tối đa 8 biến.' };
  if (clauses.length > 16) return { error: 'Tối đa 16 mệnh đề.' };
  return { names, clauses };
}

export const litText = (l, names) => (l < 0 ? '¬' : '') + names[Math.abs(l) - 1];
export const clauseText = (c, names) => '(' + c.map((l) => litText(l, names)).join(' ∨ ') + ')';

function status(c, a) {
  let open = 0, last = 0;
  for (const l of c) {
    const v = a[Math.abs(l)];
    if (v === undefined) { open++; last = l; } else if (v === (l > 0)) return { s: 'sat' };
  }
  if (open === 0) return { s: 'conflict' };
  if (open === 1) return { s: 'unit', lit: last };
  return { s: 'open' };
}

export function dpllSteps(clauses, names, cap = 4000) {
  const steps = [];
  const nv = names.length;
  const snap = (a, trail, extra) => steps.push({
    assign: { ...a }, trail: trail.map((t) => ({ ...t })),
    cstat: clauses.map((c) => status(c, a).s), done: false, result: null, ...extra
  });
  let model = null;
  function go(a, trail, level) {
    for (;;) {
      if (steps.length > cap) return false;
      const sts = clauses.map((c) => status(c, a));
      const ci = sts.findIndex((s) => s.s === 'conflict');
      if (ci >= 0) { snap(a, trail, { level, hot: ci, msg: `XUNG ĐỘT: mệnh đề ${clauseText(clauses[ci], names)} bị sai hết literal ⇒ quay lui.` }); return false; }
      const ui = sts.findIndex((s) => s.s === 'unit');
      if (ui >= 0) {
        const l = sts[ui].lit; const v = Math.abs(l);
        a = { ...a, [v]: l > 0 }; trail = [...trail, { v, val: l > 0, why: 'unit' }];
        snap(a, trail, { level, hot: ui, msg: `Lan truyền đơn vị: mệnh đề ${clauseText(clauses[ui], names)} chỉ còn literal ${litText(l, names)} ⇒ bắt buộc ${names[v - 1]} = ${l > 0 ? 'T' : 'F'}.` });
        continue;
      }
      if (sts.every((s) => s.s === 'sat')) {
        model = { ...a };
        for (let v = 1; v <= nv; v++) if (model[v] === undefined) model[v] = false;
        snap(a, trail, { level, msg: 'Mọi mệnh đề đều thỏa ⇒ CNF thỏa được (SAT).', done: true, result: 'sat' });
        return true;
      }
      let v = 1; while (a[v] !== undefined) v++;
      for (const val of [true, false]) {
        const a2 = { ...a, [v]: val }; const t2 = [...trail, { v, val, why: val ? 'decision' : 'flip' }];
        snap(a2, t2, { level: level + 1, msg: val ? `Quyết định (mức ${level + 1}): thử ${names[v - 1]} = T.` : `Quay lui: nhánh ${names[v - 1]} = T thất bại, thử ${names[v - 1]} = F.` });
        if (go(a2, t2, level + 1)) return true;
      }
      snap(a, trail, { level, msg: `Cả hai giá trị của ${names[v - 1]} đều dẫn tới xung đột ⇒ quay lui lên mức trên.` });
      return false;
    }
  }
  snap({}, [], { level: 0, msg: `Có ${nv} biến, ${clauses.length} mệnh đề. Chưa gán biến nào.` });
  const ok = go({}, [], 0);
  if (!ok) snap({}, [], { level: 0, msg: 'Mọi nhánh đều thất bại ⇒ CNF vô nghiệm (UNSAT).', done: true, result: 'unsat' });
  return { steps, sat: ok, model };
}

export function evalCNF(clauses, a) {
  return clauses.every((c) => c.some((l) => a[Math.abs(l)] === (l > 0)));
}

export function bruteSat(clauses, nv) {
  for (let m = 0; m < 1 << nv; m++) {
    const a = {};
    for (let v = 1; v <= nv; v++) a[v] = !!((m >> (v - 1)) & 1);
    if (evalCNF(clauses, a)) return true;
  }
  return false;
}

export const DPLL_PRESETS = [
  { id: 'sat', name: 'Thỏa được (có quay lui)', text: '(p ∨ q) ∧ (¬p ∨ r) ∧ (¬q ∨ ¬r) ∧ (p ∨ ¬r) ∧ (¬p ∨ ¬q)' },
  { id: 'unit', name: 'Lan truyền đơn vị liên tiếp', text: '(p) ∧ (¬p ∨ q) ∧ (¬q ∨ r) ∧ (¬r ∨ s ∨ t) ∧ (¬s ∨ ¬t)' },
  { id: 'unsat', name: 'Vô nghiệm (4 mệnh đề / 2 biến)', text: '(p ∨ q) ∧ (p ∨ ¬q) ∧ (¬p ∨ q) ∧ (¬p ∨ ¬q)' },
  { id: 'php', name: 'Chuồng bồ câu: 3 thỏ, 2 chuồng', text: 'a1 b1, a2 b2, a3 b3, ¬a1 ¬a2, ¬a1 ¬a3, ¬a2 ¬a3, ¬b1 ¬b2, ¬b1 ¬b3, ¬b2 ¬b3' }
];
