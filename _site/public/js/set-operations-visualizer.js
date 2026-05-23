(function () {
  function render() {
    var host = document.getElementById('set-operations-visualizer');
    if (!host) return;

    // Clear existing inline content and rebuild from scratch
    host.innerHTML =
      '<div class="sov-wrap">' +
      '<h4>Trực quan hóa phép toán tập hợp</h4>' +
      '<div class="sov-grid">' +
        '<label>A: <input id="sov-a" type="text" value="1,2,3,4" /></label>' +
        '<label>B: <input id="sov-b" type="text" value="3,4,5,6" /></label>' +
        '<label>Phép toán: <select id="sov-op">' +
          '<option value="union">A ∪ B (Hợp)</option>' +
          '<option value="intersection">A ∩ B (Giao)</option>' +
          '<option value="difference">A \\ B (Hiệu)</option>' +
          '<option value="symmetric">A △ B (Hiệu đối xứng)</option>' +
        '</select></label>' +
      '</div>' +
      '<button id="sov-run" class="sov-btn">Thực hiện</button>' +
      '<div id="sov-venn" class="sov-venn"></div>' +
      '<div id="sov-result" class="sov-result"></div>' +
      '</div>';

    if (!document.getElementById('sov-style')) {
      var s = document.createElement('style');
      s.id = 'sov-style';
      s.textContent =
        '.sov-wrap{border:1px solid #e5e7eb;border-radius:10px;padding:16px;background:#fff;margin:12px 0}' +
        '.sov-grid{display:flex;flex-wrap:wrap;gap:12px;align-items:end;margin-bottom:10px}' +
        '.sov-grid label{display:flex;flex-direction:column;font-size:13px;color:#334155}' +
        '.sov-grid input,.sov-grid select{padding:6px 8px;border:1px solid #cbd5e1;border-radius:6px}' +
        '.sov-btn{padding:8px 14px;border-radius:8px;border:1px solid #2563eb;background:#2563eb;color:#fff;cursor:pointer}' +
        '.sov-venn{position:relative;width:300px;height:200px;margin:16px auto;border:1px solid #e5e7eb;border-radius:12px;overflow:hidden}' +
        '.sov-circle{position:absolute;border-radius:50%;border:2px solid #3b82f6;background:rgba(59,130,246,0.12);display:flex;align-items:center;justify-content:center;font-size:12px;pointer-events:none}' +
        '.sov-result{padding:10px;background:#f8fafc;border-radius:8px;font-size:14px}';
      document.head.appendChild(s);
    }

    function parseSet(val) {
      return [...new Set(
        val.split(',').map(function (x) { return x.trim(); }).filter(function (x) { return x !== ''; })
      )];
    }

    function vennCircle(x, y, r, label, els) {
      return '<div class="sov-circle" style="left:' + (x - r) + 'px;top:' + (y - r) + 'px;width:' + (2 * r) + 'px;height:' + (2 * r) + 'px">' +
        (els ? els.join('&nbsp;') : label) +
        '</div>';
    }

    document.getElementById('sov-run').addEventListener('click', function () {
      var A = parseSet(document.getElementById('sov-a').value);
      var B = parseSet(document.getElementById('sov-b').value);
      var op = document.getElementById('sov-op').value;

      var result;
      var sym;
      if (op === 'union') { result = A.concat(B.filter(function (x) { return A.indexOf(x) === -1; })); sym = '∪'; }
      else if (op === 'intersection') { result = A.filter(function (x) { return B.indexOf(x) !== -1; }); sym = '∩'; }
      else if (op === 'difference') { result = A.filter(function (x) { return B.indexOf(x) === -1; }); sym = '\\'; }
      else { var diff1 = A.filter(function (x) { return B.indexOf(x) === -1; }); var diff2 = B.filter(function (x) { return A.indexOf(x) === -1; }); result = diff1.concat(diff2); sym = '△'; }

      var onlyA = A.filter(function (x) { return B.indexOf(x) === -1; });
      var onlyB = B.filter(function (x) { return A.indexOf(x) === -1; });
      var both = A.filter(function (x) { return B.indexOf(x) !== -1; });

      var vennDiv = document.getElementById('sov-venn');
      vennDiv.innerHTML =
        vennCircle(110, 90, 70, 'A', onlyA) +
        vennCircle(180, 90, 70, 'B', onlyB) +
        vennCircle(145, 90, 70, 'A∩B', both);

      var resultDiv = document.getElementById('sov-result');
      resultDiv.innerHTML =
        '<strong>A ' + sym + ' B</strong> = {' + result.join(', ') + '}<br/>' +
        '<small>|A| = ' + A.length + ', |B| = ' + B.length + ', |A' + sym + 'B| = ' + result.length + '</small>';
    });

    document.getElementById('sov-run').click();
  }

  document.addEventListener('DOMContentLoaded', render);
})();
