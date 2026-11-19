// Máy Turing một băng, tất định.

export const TM_PRESETS = [
  {
    id: 'inc', name: 'Cộng 1 cho số nhị phân', input: '1011',
    desc: 'Đi sang phải tới ô trống, rồi quay lại: gặp 1 thì ghi 0 và nhớ sang trái, gặp 0 hoặc ô trống thì ghi 1 và dừng.',
    start: 'q0', accept: 'qA',
    rules: [
      ['q0', '0', 'q0', '0', 'R'], ['q0', '1', 'q0', '1', 'R'], ['q0', '_', 'q1', '_', 'L'],
      ['q1', '1', 'q1', '0', 'L'], ['q1', '0', 'qA', '1', 'S'], ['q1', '_', 'qA', '1', 'S']
    ],
    oracle: (w) => (/^[01]+$/.test(w) ? (BigInt('0b' + w) + 1n).toString(2) : null)
  },
  {
    id: 'anbn', name: 'Nhận dạng 0ⁿ1ⁿ', input: '000111',
    desc: 'Mỗi vòng: đánh dấu một số 0 đầu bằng X, đi sang phải đánh dấu một số 1 bằng Y, quay về. Hết 0 mà vẫn còn 1 (hoặc ngược lại) thì từ chối.',
    start: 'q0', accept: 'qA',
    rules: [
      ['q0', '0', 'q1', 'X', 'R'], ['q0', 'Y', 'q3', 'Y', 'R'], ['q0', '_', 'qA', '_', 'S'],
      ['q1', '0', 'q1', '0', 'R'], ['q1', 'Y', 'q1', 'Y', 'R'], ['q1', '1', 'q2', 'Y', 'L'],
      ['q2', '0', 'q2', '0', 'L'], ['q2', 'Y', 'q2', 'Y', 'L'], ['q2', 'X', 'q0', 'X', 'R'],
      ['q3', 'Y', 'q3', 'Y', 'R'], ['q3', '_', 'qA', '_', 'S']
    ],
    oracle: (w) => { const m = /^(0*)(1*)$/.exec(w); return m && m[1].length === m[2].length ? 'accept' : 'reject'; }
  },
  {
    id: 'unary', name: 'Cộng số đơn phân 111+11', input: '111+11',
    desc: 'Thay dấu + bằng 1 rồi xóa một số 1 ở cuối: 111+11 → 11111.',
    start: 'q0', accept: 'qA',
    rules: [
      ['q0', '1', 'q0', '1', 'R'], ['q0', '+', 'q1', '1', 'R'],
      ['q1', '1', 'q1', '1', 'R'], ['q1', '_', 'q2', '_', 'L'], ['q2', '1', 'qA', '_', 'S']
    ],
    oracle: (w) => { const m = /^(1*)\+(1*)$/.exec(w); return m ? '1'.repeat(m[1].length + m[2].length) : null; }
  }
];

/** Chạy tối đa cap bước. Trả về { configs:[{state,tape,head,rule}], status:'accept'|'reject'|'cap', output }. */
export function runTM(tm, input, cap = 600) {
  const rules = new Map(tm.rules.map((r) => [r[0] + '\u0000' + r[1], r]));
  let tape = (input || '').split('');
  let head = 0;
  if (!tape.length) tape = ['_'];
  let state = tm.start;
  const snap = (rule) => ({ state, tape: [...tape], head, rule });
  const configs = [snap(null)];
  let status = 'cap';
  for (let s = 0; s < cap; s++) {
    if (state === tm.accept) { status = 'accept'; break; }
    const sym = tape[head] ?? '_';
    const r = rules.get(state + '\u0000' + sym);
    if (!r) { status = 'reject'; break; }
    tape[head] = r[3]; state = r[2];
    if (r[4] === 'R') head++; else if (r[4] === 'L') head--;
    if (head < 0) { tape.unshift('_'); head = 0; }
    if (head >= tape.length) tape.push('_');
    configs.push(snap(r));
    if (state === tm.accept) { status = 'accept'; break; }
  }
  const output = tape.join('').replace(/^_+|_+$/g, '');
  return { configs, status, output };
}
