(function () {
  function render() {
    var host = document.querySelector('[data-demo="summation-loop-visualizer"]');
    if (!host) return;

    host.insertAdjacentHTML(
      'beforeend',
      '<div class="slv-wrap">' +
        '<div class="slv-grid">' +
          '<label>Kiểu vòng lặp: <select id="slv-type">' +
            '<option value="single">for i = 1 to n: work</option>' +
            '<option value="nested">for i = 1 to n: for j = 1 to i: work</option>' +
            '<option value="nestedn">for i = 1 to n: for j = 1 to n: work</option>' +
          '</select></label>' +
          '<label>n = <input id="slv-n" type="number" value="4" min="1" max="8"/></label>' +
        '</div>' +
        '<button id="slv-run">Hiển thị</button>' +
        '<div id="slv-formula" class="slv-formula"></div>' +
        '<div id="slv-grid" class="slv-grid-display"></div>' +
        '<div id="slv-sum" class="slv-sum"></div>' +
      '</div>'
    );

    if (!document.getElementById('slv-style')) {
      var s = document.createElement('style');
      s.id = 'slv-style';
      s.textContent =
        '.slv-wrap{border:1px solid #e5e7eb;border-radius:10px;padding:12px;background:#fff;margin:12px 0}' +
        '.slv-grid{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:10px}' +
        '.slv-grid label{display:flex;align-items:center;gap:6px}' +
        '.slv-grid input,.slv-grid select{padding:6px;border:1px solid #cbd5e1;border-radius:6px}' +
        '.slv-wrap button{padding:7px 10px;border:1px solid #2563eb;background:#2563eb;color:#fff;border-radius:6px;cursor:pointer;margin-bottom:10px}' +
        '.slv-formula{padding:8px;background:#f0f9ff;border-radius:8px;margin-bottom:8px;font-size:14px}' +
        '.slv-grid-display{overflow:auto;margin-bottom:8px}' +
        '.slv-grid-display table{border-collapse:collapse}' +
        '.slv-grid-display td{border:1px solid #e5e7eb;padding:4px 8px;text-align:center}' +
        '.slv-grid-display td.hit{background:#dcfce7}' +
        '.slv-sum{padding:8px;background:#f8fafc;border-radius:8px}';
      document.head.appendChild(s);
    }

    function draw() {
      var type = document.getElementById('slv-type').value;
      var n = Number(document.getElementById('slv-n').value) || 4;
      if (n < 1) n = 1;
      if (n > 8) n = 8;
      document.getElementById('slv-n').value = n;

      var formula = '', rows = '', total = 0;

      if (type === 'single') {
        formula = '∑<sub>i=1</sub><sup>n</sup> 1 = n = ' + n;
        rows = '<table><tr>' + Array.from({ length: n }, function (_, i) { return '<td class="hit">' + (i + 1) + '</td>'; }).join('') + '</tr></table>';
        total = n;
      } else if (type === 'nested') {
        formula = '∑<sub>i=1</sub><sup>n</sup> i = n(n+1)/2 = ' + (n * (n + 1) / 2);
        var trs = [];
        var c = 0;
        for (var i = 1; i <= n; i++) {
          var tds = [];
          for (var j = 1; j <= n; j++) {
            tds.push(j <= i ? '<td class="hit">·</td>' : '<td> </td>');
            if (j <= i) c++;
          }
          trs.push('<tr>' + tds.join('') + '</tr>');
        }
        rows = '<table>' + trs.join('') + '</table>';
        total = c;
      } else {
        formula = '∑<sub>i=1</sub><sup>n</sup> n = n² = ' + (n * n);
        var trs2 = [];
        for (var i2 = 1; i2 <= n; i2++) {
          var tds2 = [];
          for (var j2 = 1; j2 <= n; j2++) {
            tds2.push('<td class="hit">·</td>');
          }
          trs2.push('<tr>' + tds2.join('') + '</tr>');
        }
        rows = '<table>' + trs2.join('') + '</table>';
        total = n * n;
      }

      document.getElementById('slv-formula').innerHTML = '<strong>Ký hiệu Sigma:</strong> ' + formula;
      document.getElementById('slv-grid').innerHTML = rows;
      document.getElementById('slv-sum').innerHTML = '<strong>Tổng số ô (O):</strong> ' + total;
    }

    document.getElementById('slv-run').addEventListener('click', draw);
    draw();
  }

  document.addEventListener('DOMContentLoaded', render);
})();
