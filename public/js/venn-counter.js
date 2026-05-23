(function () {
  function num(v) {
    const n = Number(v);
    return Number.isFinite(n) ? n : 0;
  }

  function render() {
    const host = document.querySelector('[data-tool="venn-counter"]');
    if (!host) return;

    host.insertAdjacentHTML(
      'beforeend',
      `
      <div class="vc-wrap">
        <div class="vc-grid">
          <label>|A| <input id="vc-a" type="number" value="30" min="0"/></label>
          <label>|B| <input id="vc-b" type="number" value="25" min="0"/></label>
          <label>|C| <input id="vc-c" type="number" value="20" min="0"/></label>
          <label>|A∩B| <input id="vc-ab" type="number" value="8" min="0"/></label>
          <label>|A∩C| <input id="vc-ac" type="number" value="6" min="0"/></label>
          <label>|B∩C| <input id="vc-bc" type="number" value="5" min="0"/></label>
          <label>|A∩B∩C| <input id="vc-abc" type="number" value="2" min="0"/></label>
        </div>
        <button id="vc-calc">Tính |A∪B∪C|</button>
        <div id="vc-out" class="vc-out"></div>
      </div>
    `
    );

    if (!document.getElementById('vc-style')) {
      const s = document.createElement('style');
      s.id = 'vc-style';
      s.textContent = `
        .vc-wrap{border:1px solid #e5e7eb;border-radius:10px;padding:12px;background:#fff}
        .vc-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:8px;margin-bottom:10px}
        .vc-grid label{display:flex;flex-direction:column;font-size:13px;color:#334155}
        .vc-grid input{padding:6px;border:1px solid #cbd5e1;border-radius:6px}
        .vc-wrap button{padding:7px 10px;border:1px solid #2563eb;background:#2563eb;color:#fff;border-radius:6px;cursor:pointer}
        .vc-out{margin-top:10px;padding:10px;background:#f8fafc;border-radius:8px}
        .vc-out.err{background:#fee2e2;color:#991b1b}
        .vc-out.ok{background:#dcfce7;color:#166534}
      `;
      document.head.appendChild(s);
    }

    const out = document.getElementById('vc-out');
    document.getElementById('vc-calc').addEventListener('click', () => {
      const A = num(document.getElementById('vc-a').value);
      const B = num(document.getElementById('vc-b').value);
      const C = num(document.getElementById('vc-c').value);
      const AB = num(document.getElementById('vc-ab').value);
      const AC = num(document.getElementById('vc-ac').value);
      const BC = num(document.getElementById('vc-bc').value);
      const ABC = num(document.getElementById('vc-abc').value);

      const union = A + B + C - AB - AC - BC + ABC;
      const checks = [];
      if (ABC > AB || ABC > AC || ABC > BC) checks.push('|A∩B∩C| không thể lớn hơn các giao đôi.');
      if (AB > Math.min(A, B)) checks.push('|A∩B| > min(|A|,|B|).');
      if (AC > Math.min(A, C)) checks.push('|A∩C| > min(|A|,|C|).');
      if (BC > Math.min(B, C)) checks.push('|B∩C| > min(|B|,|C|).');
      if (union < 0) checks.push('Kết quả âm -> dữ liệu không nhất quán.');

      if (checks.length) {
        out.className = 'vc-out err';
        out.innerHTML = `<strong>Dữ liệu có vấn đề:</strong><ul>${checks.map((x) => `<li>${x}</li>`).join('')}</ul>`;
      } else {
        out.className = 'vc-out ok';
        out.innerHTML = `
          <div><strong>Áp dụng bao hàm - loại trừ:</strong></div>
          <div>|A∪B∪C| = |A| + |B| + |C| - |A∩B| - |A∩C| - |B∩C| + |A∩B∩C|</div>
          <div>= ${A} + ${B} + ${C} - ${AB} - ${AC} - ${BC} + ${ABC}</div>
          <div><strong>= ${union}</strong></div>
        `;
      }
    });

    document.getElementById('vc-calc').click();
  }

  document.addEventListener('DOMContentLoaded', render);
})();
