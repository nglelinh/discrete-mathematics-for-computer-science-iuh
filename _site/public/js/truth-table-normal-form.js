(function () {
  function esc(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
  }

  function tokenize(input) {
    const src = input
      .replace(/\s+/g, '')
      .replace(/<->/g, '↔')
      .replace(/->/g, '→')
      .replace(/\bnot\b/gi, '!')
      .replace(/\band\b/gi, '∧')
      .replace(/\bor\b/gi, '∨');

    const tokens = [];
    for (let i = 0; i < src.length; i++) {
      const ch = src[i];
      if ('()!∧∨→↔'.includes(ch)) {
        tokens.push(ch);
      } else if (/[pqr]/i.test(ch)) {
        tokens.push(ch.toLowerCase());
      } else {
        throw new Error('Ký tự không hợp lệ: ' + ch);
      }
    }
    return tokens;
  }

  const prec = { '!': 5, '∧': 4, '∨': 3, '→': 2, '↔': 1 };
  const rightAssoc = new Set(['!', '→', '↔']);

  function toRpn(tokens) {
    const out = [];
    const ops = [];
    for (const t of tokens) {
      if (/[pqr]/.test(t)) {
        out.push(t);
      } else if (t === '(') {
        ops.push(t);
      } else if (t === ')') {
        while (ops.length && ops[ops.length - 1] !== '(') out.push(ops.pop());
        if (!ops.length) throw new Error('Ngoặc không khớp.');
        ops.pop();
      } else {
        while (
          ops.length &&
          ops[ops.length - 1] !== '(' &&
          ((rightAssoc.has(t) && prec[t] < prec[ops[ops.length - 1]]) ||
            (!rightAssoc.has(t) && prec[t] <= prec[ops[ops.length - 1]]))
        ) {
          out.push(ops.pop());
        }
        ops.push(t);
      }
    }
    while (ops.length) {
      const o = ops.pop();
      if (o === '(' || o === ')') throw new Error('Ngoặc không khớp.');
      out.push(o);
    }
    return out;
  }

  function evalRpn(rpn, env) {
    const st = [];
    for (const t of rpn) {
      if (/[pqr]/.test(t)) st.push(Boolean(env[t]));
      else if (t === '!') {
        if (!st.length) throw new Error('Biểu thức lỗi.');
        st.push(!st.pop());
      } else {
        if (st.length < 2) throw new Error('Biểu thức lỗi.');
        const b = st.pop();
        const a = st.pop();
        if (t === '∧') st.push(a && b);
        else if (t === '∨') st.push(a || b);
        else if (t === '→') st.push(!a || b);
        else if (t === '↔') st.push(a === b);
      }
    }
    if (st.length !== 1) throw new Error('Biểu thức lỗi.');
    return st[0];
  }

  function rowToMinterm(row) {
    const lits = [];
    for (const v of ['p', 'q', 'r']) lits.push(row[v] ? v : `¬${v}`);
    return `(${lits.join(' ∧ ')})`;
  }
  function rowToMaxterm(row) {
    const lits = [];
    for (const v of ['p', 'q', 'r']) lits.push(row[v] ? `¬${v}` : v);
    return `(${lits.join(' ∨ ')})`;
  }

  function render() {
    const host = document.querySelector('[data-tool="truth-table-normal-form"]');
    if (!host) return;

    host.insertAdjacentHTML(
      'beforeend',
      `
      <div class="ttnf-wrap">
        <div class="ttnf-input">
          <label>Biểu thức (dùng p,q,r và !, and, or, ->, <->):</label>
          <input id="ttnf-expr" value="(p -> q) and (q -> r)" />
          <button id="ttnf-run">Sinh bảng</button>
        </div>
        <div id="ttnf-msg" class="ttnf-msg"></div>
        <div id="ttnf-out"></div>
      </div>
    `
    );

    if (!document.getElementById('ttnf-style')) {
      const style = document.createElement('style');
      style.id = 'ttnf-style';
      style.textContent = `
        .ttnf-wrap{border:1px solid #e5e7eb;border-radius:10px;padding:12px;background:#fff}
        .ttnf-input{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
        .ttnf-input input{min-width:280px;padding:6px 8px;border:1px solid #cbd5e1;border-radius:6px}
        .ttnf-input button{padding:6px 10px;border:1px solid #2563eb;background:#2563eb;color:#fff;border-radius:6px;cursor:pointer}
        .ttnf-msg{margin:8px 0;color:#475569}
        .ttnf-table{width:100%;border-collapse:collapse;margin-top:8px}
        .ttnf-table th,.ttnf-table td{border:1px solid #e5e7eb;padding:6px;text-align:center}
        .ttnf-form{margin-top:10px;padding:8px;background:#f8fafc;border-radius:8px}
        .ttnf-form code{white-space:normal}
      `;
      document.head.appendChild(style);
    }

    const btn = document.getElementById('ttnf-run');
    const input = document.getElementById('ttnf-expr');
    const msg = document.getElementById('ttnf-msg');
    const out = document.getElementById('ttnf-out');

    function run() {
      try {
        const expr = input.value.trim();
        const rpn = toRpn(tokenize(expr));
        const rows = [];
        for (let p = 1; p >= 0; p--) {
          for (let q = 1; q >= 0; q--) {
            for (let r = 1; r >= 0; r--) {
              const env = { p: !!p, q: !!q, r: !!r };
              rows.push({ ...env, f: evalRpn(rpn, env) });
            }
          }
        }

        const dnfTerms = rows.filter((x) => x.f).map(rowToMinterm);
        const cnfTerms = rows.filter((x) => !x.f).map(rowToMaxterm);

        const dnf = dnfTerms.length ? dnfTerms.join(' ∨ ') : 'False';
        const cnf = cnfTerms.length ? cnfTerms.join(' ∧ ') : 'True';

        msg.textContent = 'Đã sinh bảng chân trị + DNF/CNF đầy đủ.';
        out.innerHTML = `
          <table class="ttnf-table">
            <thead><tr><th>p</th><th>q</th><th>r</th><th>F</th></tr></thead>
            <tbody>
              ${rows
                .map(
                  (x) => `<tr><td>${x.p ? 'T' : 'F'}</td><td>${x.q ? 'T' : 'F'}</td><td>${x.r ? 'T' : 'F'}</td><td>${
                    x.f ? 'T' : 'F'
                  }</td></tr>`
                )
                .join('')}
            </tbody>
          </table>
          <div class="ttnf-form"><strong>DNF:</strong><br/><code>${esc(dnf)}</code></div>
          <div class="ttnf-form"><strong>CNF:</strong><br/><code>${esc(cnf)}</code></div>
        `;
      } catch (e) {
        msg.textContent = 'Lỗi: ' + e.message;
        out.innerHTML = '';
      }
    }

    btn.addEventListener('click', run);
    run();
  }

  document.addEventListener('DOMContentLoaded', render);
})();
