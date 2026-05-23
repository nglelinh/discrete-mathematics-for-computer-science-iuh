(function () {
  function render() {
    const host = document.querySelector('[data-demo="nested-quantifier-grid"]');
    if (!host) return;

    host.insertAdjacentHTML(
      'beforeend',
      `
      <div class="nqg-wrap">
        <p><strong>Bật/tắt</strong> ô để mô tả quan hệ Takes(student, course).</p>
        <table class="nqg-table" id="nqg-table"></table>
        <div class="nqg-result" id="nqg-result"></div>
        <button id="nqg-reset">Reset</button>
      </div>
    `
    );

    if (!document.getElementById('nqg-style')) {
      const s = document.createElement('style');
      s.id = 'nqg-style';
      s.textContent = `
        .nqg-wrap{border:1px solid #e5e7eb;border-radius:10px;padding:12px;background:#fff}
        .nqg-table{border-collapse:collapse;margin:8px 0}
        .nqg-table th,.nqg-table td{border:1px solid #cbd5e1;padding:8px 10px;text-align:center}
        .nqg-cell{cursor:pointer;background:#fee2e2}
        .nqg-cell.on{background:#dcfce7}
        .nqg-result{margin:8px 0;padding:8px;background:#f8fafc;border-radius:8px}
      `;
      document.head.appendChild(s);
    }

    const students = ['An', 'Bình', 'Chi'];
    const courses = ['DM', 'Algo', 'DB'];
    const state = Array.from({ length: students.length }, () => Array(courses.length).fill(false));

    const table = document.getElementById('nqg-table');
    const result = document.getElementById('nqg-result');

    function build() {
      table.innerHTML = `
        <thead>
          <tr><th>SV \\ Môn</th>${courses.map((c) => `<th>${c}</th>`).join('')}</tr>
        </thead>
        <tbody>
          ${students
            .map(
              (s, i) =>
                `<tr><th>${s}</th>${courses
                  .map(
                    (c, j) =>
                      `<td class="nqg-cell ${state[i][j] ? 'on' : ''}" data-i="${i}" data-j="${j}">${state[i][j] ? '✓' : '·'}</td>`
                  )
                  .join('')}</tr>`
            )
            .join('')}
        </tbody>
      `;

      table.querySelectorAll('.nqg-cell').forEach((cell) => {
        cell.addEventListener('click', () => {
          const i = Number(cell.dataset.i);
          const j = Number(cell.dataset.j);
          state[i][j] = !state[i][j];
          build();
          evalQuantifiers();
        });
      });
    }

    function evalQuantifiers() {
      const forallExists = state.every((row) => row.some(Boolean)); // ∀x∃y
      const existsForall = courses.some((_, j) => state.every((row) => row[j])); // ∃y∀x
      result.innerHTML = `
        <div>$$\\forall x\\exists y\,Takes(x,y)$$: <strong>${forallExists ? 'Đúng' : 'Sai'}</strong></div>
        <div>$$\\exists y\\forall x\,Takes(x,y)$$: <strong>${existsForall ? 'Đúng' : 'Sai'}</strong></div>
        <small>Gợi ý: đổi một cột thành toàn ✓ để làm $$\\exists y\\forall x$$ đúng.</small>
      `;
      if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([result]).catch(() => {});
    }

    document.getElementById('nqg-reset').addEventListener('click', () => {
      for (let i = 0; i < state.length; i++) for (let j = 0; j < state[i].length; j++) state[i][j] = false;
      build();
      evalQuantifiers();
    });

    build();
    evalQuantifiers();
  }

  document.addEventListener('DOMContentLoaded', render);
})();
