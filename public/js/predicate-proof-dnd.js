(function () {
  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function normalizeFormula(s) {
    return String(s || '')
      .replace(/\s+/g, '')
      .replace(/∀/g, 'forall')
      .replace(/∃/g, 'exists')
      .replace(/→/g, '->')
      .replace(/¬/g, '!')
      .toLowerCase();
  }

  function splitTopLevelAnd(expr) {
    // very lightweight splitter for patterns like A∧B
    let depth = 0;
    for (let i = 0; i < expr.length; i++) {
      const ch = expr[i];
      if (ch === '(') depth++;
      else if (ch === ')') depth = Math.max(0, depth - 1);
      else if ((ch === '∧' || ch === '&') && depth === 0) {
        return [expr.slice(0, i), expr.slice(i + 1)];
      }
    }
    return null;
  }

  class PredicateProofDnD {
    constructor(container) {
      this.container = container;
      this.rules = ['UI', 'UG', 'EI', 'EG', 'MP'];

      // Guided exercise
      this.lines = [
        { id: 1, text: '∀x (P(x) → Q(x))', kind: 'premise' },
        { id: 2, text: '∃x P(x)', kind: 'premise' },
        { id: 3, text: 'P(c)', kind: 'derived' },
        { id: 4, text: 'P(c) → Q(c)', kind: 'derived' },
        { id: 5, text: 'Q(c)', kind: 'derived' },
        { id: 6, text: '∃x Q(x)', kind: 'goal' }
      ];

      this.expected = {
        3: { rule: 'EI', refs: '2' },
        4: { rule: 'UI', refs: '1' },
        5: { rule: 'MP', refs: '3,4' },
        6: { rule: 'EG', refs: '5' }
      };

      this.state = {}; // lineId -> { rule, refs }
      this.render();
      this.bind();
    }

    render() {
      this.container.innerHTML = `
        <div class="ppd-wrap">
          <h4>Demo kéo-thả quy tắc suy luận vị từ</h4>
          <p class="ppd-help">
            Mục tiêu: từ 2 tiền đề, xây dựng chứng minh để suy ra <strong>∃x Q(x)</strong>.
            Kéo thẻ quy tắc vào cột “Rule”, nhập dòng tham chiếu (ví dụ: <code>3,4</code>), rồi bấm kiểm tra.
          </p>

          <div class="ppd-rules" aria-label="Rule tokens">
            ${this.rules
              .map(
                (r) =>
                  `<button class="ppd-rule-token" draggable="true" data-rule="${r}" title="Drag ${r}">${r}</button>`
              )
              .join('')}
          </div>

          <div class="ppd-board">
            <table class="ppd-table">
              <thead>
                <tr>
                  <th>Dòng</th>
                  <th>Mệnh đề</th>
                  <th>Rule (kéo-thả)</th>
                  <th>Refs</th>
                  <th>KQ</th>
                </tr>
              </thead>
              <tbody>
                ${this.lines
                  .map((line) => {
                    if (line.kind === 'premise') {
                      return `
                        <tr data-line="${line.id}">
                          <td>${line.id}</td>
                          <td><code>${escapeHtml(line.text)}</code></td>
                          <td><span class="ppd-badge premise">Premise</span></td>
                          <td>-</td>
                          <td><span class="ppd-status ok">Cho trước</span></td>
                        </tr>
                      `;
                    }

                    return `
                      <tr data-line="${line.id}">
                        <td>${line.id}${line.kind === 'goal' ? ' 🎯' : ''}</td>
                        <td><code>${escapeHtml(line.text)}</code></td>
                        <td>
                          <div class="ppd-dropzone" data-line="${line.id}" tabindex="0" role="button" aria-label="Drop rule for line ${line.id}">Thả rule vào đây</div>
                        </td>
                        <td>
                          <input class="ppd-refs" data-line="${line.id}" placeholder="vd: 3,4" />
                        </td>
                        <td><span class="ppd-status" data-status="${line.id}">Chưa kiểm tra</span></td>
                      </tr>
                    `;
                  })
                  .join('')}
              </tbody>
            </table>
          </div>

          <div class="ppd-actions">
            <button class="ppd-btn" data-action="check-line">Kiểm tra từng dòng</button>
            <button class="ppd-btn primary" data-action="check-all">Kiểm tra toàn bộ chứng minh</button>
            <button class="ppd-btn" data-action="reset">Làm lại</button>
          </div>

          <div class="ppd-feedback" aria-live="polite"></div>
        </div>
      `;

      if (!document.getElementById('ppd-style')) {
        const style = document.createElement('style');
        style.id = 'ppd-style';
        style.textContent = `
          .ppd-wrap { border: 1px solid #d8dee4; border-radius: 10px; padding: 16px; background: #fff; }
          .ppd-wrap h4 { margin: 0 0 8px; }
          .ppd-help { margin: 0 0 12px; color: #4a5568; }
          .ppd-rules { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 12px; }
          .ppd-rule-token { border: 1px solid #3b82f6; background: #eff6ff; color: #1d4ed8; border-radius: 8px; padding: 6px 10px; cursor: grab; font-weight: 700; }
          .ppd-table { width: 100%; border-collapse: collapse; font-size: 14px; }
          .ppd-table th, .ppd-table td { border: 1px solid #e5e7eb; padding: 8px; vertical-align: middle; }
          .ppd-dropzone { min-height: 34px; border: 2px dashed #cbd5e1; border-radius: 8px; padding: 6px 8px; background: #f8fafc; color: #64748b; }
          .ppd-dropzone.filled { border-style: solid; background: #ecfeff; color: #155e75; font-weight: 700; }
          .ppd-refs { width: 100%; border: 1px solid #cbd5e1; border-radius: 6px; padding: 6px; }
          .ppd-actions { display: flex; gap: 8px; margin-top: 12px; flex-wrap: wrap; }
          .ppd-btn { border: 1px solid #cbd5e1; background: #fff; border-radius: 8px; padding: 8px 12px; cursor: pointer; }
          .ppd-btn.primary { background: #2563eb; border-color: #2563eb; color: #fff; }
          .ppd-feedback { margin-top: 10px; font-size: 14px; }
          .ppd-status.ok { color: #166534; font-weight: 700; }
          .ppd-status.err { color: #b91c1c; font-weight: 700; }
          .ppd-badge.premise { background: #f1f5f9; color: #334155; border-radius: 999px; padding: 2px 8px; }
          @media (max-width: 900px) {
            .ppd-table { font-size: 13px; }
            .ppd-wrap { overflow-x: auto; }
          }
        `;
        document.head.appendChild(style);
      }
    }

    bind() {
      // Drag start tokens
      this.container.querySelectorAll('.ppd-rule-token').forEach((btn) => {
        btn.addEventListener('dragstart', (e) => {
          e.dataTransfer.setData('text/plain', btn.dataset.rule);
        });
      });

      // Drop zones
      this.container.querySelectorAll('.ppd-dropzone').forEach((zone) => {
        zone.addEventListener('dragover', (e) => e.preventDefault());
        zone.addEventListener('drop', (e) => {
          e.preventDefault();
          const rule = e.dataTransfer.getData('text/plain');
          const line = Number(zone.dataset.line);
          if (!this.state[line]) this.state[line] = { rule: '', refs: '' };
          this.state[line].rule = rule;
          zone.textContent = rule;
          zone.classList.add('filled');
        });
      });

      // Refs input sync
      this.container.querySelectorAll('.ppd-refs').forEach((inp) => {
        inp.addEventListener('input', () => {
          const line = Number(inp.dataset.line);
          if (!this.state[line]) this.state[line] = { rule: '', refs: '' };
          this.state[line].refs = inp.value.trim();
        });
      });

      // Buttons
      this.container.querySelector('[data-action="check-line"]').addEventListener('click', () => {
        this.checkAll(false);
      });
      this.container.querySelector('[data-action="check-all"]').addEventListener('click', () => {
        this.checkAll(true);
      });
      this.container.querySelector('[data-action="reset"]').addEventListener('click', () => this.reset());
    }

    getLineText(lineId) {
      const row = this.lines.find((l) => l.id === lineId);
      return row ? row.text : '';
    }

    // Lightweight semantic validation for this guided puzzle
    validateLine(lineId) {
      const cfg = this.state[lineId] || { rule: '', refs: '' };
      const rule = (cfg.rule || '').toUpperCase();
      const refs = (cfg.refs || '').replace(/\s+/g, '');

      if (!rule) return { ok: false, msg: 'Chưa thả rule.' };
      if (!refs) return { ok: false, msg: 'Chưa nhập refs.' };

      const expected = this.expected[lineId];
      if (!expected) return { ok: true, msg: 'Premise.' };

      // Structural checks by rule
      if (rule === 'MP') {
        const parts = refs.split(',').map((n) => Number(n)).filter(Boolean);
        if (parts.length !== 2) return { ok: false, msg: 'MP cần đúng 2 refs (vd: 3,4).' };
        const a = this.getLineText(parts[0]);
        const b = this.getLineText(parts[1]);
        const target = this.getLineText(lineId);
        const na = normalizeFormula(a);
        const nb = normalizeFormula(b);
        const nt = normalizeFormula(target);
        const arrowA = na.split('->');
        const arrowB = nb.split('->');
        const matchA = arrowA.length === 2 && normalizeFormula(arrowA[0]) === normalizeFormula(b) && normalizeFormula(arrowA[1]) === nt;
        const matchB = arrowB.length === 2 && normalizeFormula(arrowB[0]) === normalizeFormula(a) && normalizeFormula(arrowB[1]) === nt;
        if (!matchA && !matchB) return { ok: false, msg: 'MP sai: cần dạng φ và φ→ψ để suy ra ψ.' };
      }

      if (rule === 'UI') {
        const src = Number(refs);
        const srcText = this.getLineText(src);
        if (!srcText.includes('∀')) return { ok: false, msg: 'UI cần nguồn có ∀.' };
      }

      if (rule === 'EI') {
        const src = Number(refs);
        const srcText = this.getLineText(src);
        if (!srcText.includes('∃')) return { ok: false, msg: 'EI cần nguồn có ∃.' };
      }

      if (rule === 'EG') {
        const src = Number(refs);
        if (!src) return { ok: false, msg: 'EG cần 1 ref hợp lệ.' };
      }

      // Guided exactness check
      const isExactRule = rule === expected.rule;
      const isExactRefs = refs === expected.refs;
      if (!isExactRule || !isExactRefs) {
        return {
          ok: false,
          msg: `Gần đúng nhưng chưa khớp bài hướng dẫn. Dòng ${lineId} cần ${expected.rule} từ refs ${expected.refs}.`
        };
      }

      return { ok: true, msg: 'Đúng.' };
    }

    setStatus(lineId, ok, msg) {
      const el = this.container.querySelector(`[data-status="${lineId}"]`);
      if (!el) return;
      el.textContent = msg;
      el.classList.remove('ok', 'err');
      el.classList.add(ok ? 'ok' : 'err');
    }

    checkAll(strict) {
      const checkLines = [3, 4, 5, 6];
      let okCount = 0;
      let firstErr = '';

      checkLines.forEach((lineId) => {
        const res = this.validateLine(lineId);
        this.setStatus(lineId, res.ok, res.msg);
        if (res.ok) okCount++;
        else if (!firstErr) firstErr = `Dòng ${lineId}: ${res.msg}`;
      });

      const fb = this.container.querySelector('.ppd-feedback');
      if (okCount === checkLines.length) {
        fb.innerHTML = '<span class="ppd-status ok">✅ Chứng minh hợp lệ. Bạn đã dùng đúng EI, UI, MP, EG.</span>';
      } else if (strict) {
        fb.innerHTML = `<span class="ppd-status err">❌ Chưa hợp lệ. ${escapeHtml(firstErr || 'Kiểm tra lại refs và rule.')}</span>`;
      } else {
        fb.innerHTML = `<span class="ppd-status">Đã kiểm tra từng dòng: ${okCount}/${checkLines.length} dòng đúng.</span>`;
      }
    }

    reset() {
      this.state = {};
      this.container.querySelectorAll('.ppd-dropzone').forEach((z) => {
        z.textContent = 'Thả rule vào đây';
        z.classList.remove('filled');
      });
      this.container.querySelectorAll('.ppd-refs').forEach((i) => (i.value = ''));
      this.container.querySelectorAll('[data-status]').forEach((s) => {
        s.textContent = 'Chưa kiểm tra';
        s.classList.remove('ok', 'err');
      });
      const fb = this.container.querySelector('.ppd-feedback');
      fb.textContent = '';
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    const mount = document.getElementById('predicate-proof-demo');
    if (!mount) return;
    new PredicateProofDnD(mount);
  });
})();
