(function () {
  var A = [1, 2, 3];
  function style() { if (document.getElementById('wv-style')) return; var s = document.createElement('style'); s.id = 'wv-style'; s.textContent = '.wv-wrap{border:1px solid #e5e7eb;border-radius:12px;padding:16px;background:#fff;margin:14px 0}.wv-grid{display:grid;grid-template-columns:44px repeat(3,52px);gap:6px;align-items:center;margin:12px 0}.wv-head,.wv-row{text-align:center;font-weight:600;color:#495057}.wv-cell{height:44px;border:1px solid #cbd5e1;border-radius:8px;background:#f8fafc;display:flex;align-items:center;justify-content:center}.wv-cell:has(input:checked){background:#dbeafe;border-color:#007bff}.wv-new{box-shadow:0 0 0 3px rgba(40,167,69,.28);background:#dcfce7!important}.wv-actions{display:flex;gap:8px;flex-wrap:wrap}.wv-actions button{padding:9px 14px;border:1px solid #007bff;background:#007bff;color:#fff;border-radius:8px;cursor:pointer}.wv-out{margin-top:10px;padding:10px;border-radius:8px;background:#f8f9fa}'; document.head.appendChild(s); }
  function matrix(host) { return A.map(function (_, i) { return A.map(function (_, j) { return host.querySelector('[data-i="' + i + '"][data-j="' + j + '"]').checked; }); }); }
  function paint(host, m, changed) { A.forEach(function (_, i) { A.forEach(function (_, j) { var el = host.querySelector('[data-i="' + i + '"][data-j="' + j + '"]'); el.checked = m[i][j]; el.parentNode.classList.toggle('wv-new', !!changed[i + ',' + j]); }); }); }
  function step(m, k) { var changed = {}; var next = m.map(function (r) { return r.slice(); }); for (var i = 0; i < 3; i++) for (var j = 0; j < 3; j++) if (!next[i][j] && m[i][k] && m[k][j]) { next[i][j] = true; changed[i + ',' + j] = true; } return { matrix: next, changed: changed }; }
  function mount(host) {
    if (!host || host.dataset.wvMounted) return; host.dataset.wvMounted = '1'; style();
    var html = '<div class="wv-wrap"><h4>Warshall: bao đóng bắc cầu</h4><p>Chọn ma trận ban đầu, rồi cho từng đỉnh k làm trung gian.</p><div class="wv-grid"><div></div>';
    A.forEach(function (x) { html += '<div class="wv-head">' + x + '</div>'; });
    A.forEach(function (x, i) { html += '<div class="wv-row">' + x + '</div>'; A.forEach(function (y, j) { html += '<label class="wv-cell"><input type="checkbox" data-i="' + i + '" data-j="' + j + '" ' + ((i === 0 && j === 1) || (i === 1 && j === 2) ? 'checked' : '') + '></label>'; }); });
    html += '</div><div class="wv-actions"><button type="button" data-act="step">Bước Warshall</button><button type="button" data-act="run">Chạy hết</button><button type="button" data-act="reset">Đặt lại</button></div><div class="wv-out" aria-live="polite">Sẵn sàng: bước tiếp theo k = 1.</div></div>';
    host.innerHTML = html;
    var k = 0, out = host.querySelector('.wv-out');
    function doStep() { if (k >= 3) { out.textContent = 'Đã hoàn tất k = 1,2,3. Ma trận hiện là bao đóng bắc cầu.'; return false; } var r = step(matrix(host), k); paint(host, r.matrix, r.changed); var added = Object.keys(r.changed).map(function (c) { var p = c.split(','); return '(' + A[p[0]] + ',' + A[p[1]] + ')'; }); out.textContent = 'Bước k = ' + A[k] + ': ' + (added.length ? 'thêm ' + added.join(', ') : 'không thêm ô nào') + '. Bước tiếp theo k = ' + (k < 2 ? A[k + 1] : 'xong') + '.'; k++; return true; }
    host.addEventListener('change', function () { k = 0; paint(host, matrix(host), {}); out.textContent = 'Ma trận đổi. Bắt đầu lại từ k = 1.'; });
    host.querySelector('[data-act="step"]').addEventListener('click', doStep);
    host.querySelector('[data-act="run"]').addEventListener('click', function () { while (doStep()) {} });
    host.querySelector('[data-act="reset"]').addEventListener('click', function () { k = 0; Array.prototype.forEach.call(host.querySelectorAll('input'), function (el) { el.checked = (el.dataset.i === '0' && el.dataset.j === '1') || (el.dataset.i === '1' && el.dataset.j === '2'); el.parentNode.classList.remove('wv-new'); }); out.textContent = 'Đã đặt lại. Bước tiếp theo k = 1.'; });
  }
  function safeMount(host) { try { mount(host); } catch (err) { if (host) host.innerHTML = '<div class="wv-out">Không thể tải demo Warshall. Hãy tải lại trang.</div>'; } }
  document.addEventListener('DOMContentLoaded', function () { Array.prototype.forEach.call(document.querySelectorAll('[data-demo="relation-closure-warshall"]'), safeMount); });
})();
