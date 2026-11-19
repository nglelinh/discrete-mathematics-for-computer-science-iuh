// Kiểm tra quy tắc suy diễn bằng bảng chân trị: hợp lệ ⇔ không có dòng nào mọi tiền đề đúng mà kết luận sai.
import { parse, collectVars, evalAst } from '../boolean/logic.js';

export const INFERENCE_PRESETS = [
  { id: 'mp', name: 'Modus ponens', premises: 'p → q\np', conclusion: 'q' },
  { id: 'mt', name: 'Modus tollens', premises: 'p → q\n¬q', conclusion: '¬p' },
  { id: 'hs', name: 'Tam đoạn luận giả định', premises: 'p → q\nq → r', conclusion: 'p → r' },
  { id: 'ds', name: 'Tam đoạn luận tuyển', premises: 'p ∨ q\n¬p', conclusion: 'q' },
  { id: 'res', name: 'Phép giải (resolution)', premises: 'p ∨ q\n¬p ∨ r', conclusion: 'q ∨ r' },
  { id: 'aff', name: 'NGỤY BIỆN: khẳng định hệ quả', premises: 'p → q\nq', conclusion: 'p' },
  { id: 'den', name: 'NGỤY BIỆN: phủ định giả thiết', premises: 'p → q\n¬p', conclusion: '¬q' }
];

export function checkArgument(premisesText, conclusionText) {
  let prem, conc;
  try {
    prem = premisesText.split('\n').map((s) => s.trim()).filter(Boolean).map(parse);
    conc = parse(conclusionText);
  } catch (e) { return { error: e.message }; }
  if (!prem.length) return { error: 'Cần ít nhất một tiền đề.' };
  const vars = [...new Set([...prem.flatMap((p) => [...collectVars(p)]), ...collectVars(conc)])].sort();
  if (vars.length > 5) return { error: 'Tối đa 5 biến.' };
  const rows = [];
  for (let m = 0; m < 1 << vars.length; m++) {
    const env = Object.fromEntries(vars.map((v, i) => [v, (m >> (vars.length - 1 - i)) & 1]));
    const pv = prem.map((p) => evalAst(p, env));
    const cv = evalAst(conc, env);
    const critical = pv.every(Boolean);
    rows.push({ env, pv, cv, critical, bad: critical && !cv });
  }
  return { vars, rows, valid: !rows.some((r) => r.bad), count: prem.length };
}
