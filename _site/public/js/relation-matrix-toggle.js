(function () {
  var A = [1, 2, 3];
  function pairKey(a, b) { return a + ',' + b; }
  function pairText(a, b) { return '(' + a + ',' + b + ')'; }
  function addStyle() {
    if (document.getElementById('rmt-style')) return;
    var s = document.createElement('style');
    s.id = 'rmt-style';
    s.textContent = '.rmt-wrap{border:1px solid #e5e7eb;border-radius:12px;padding:16px;background:#fff;margin:14px 0}.rmt-grid{display:grid;grid-template-columns:44px repeat(3,54px);gap:6px;align-items:center;margin:12px 0}.rmt-head,.rmt-row{font-weight:600;color:#495057;text-align:center}.rmt-cell{height:46px;border:1px solid #cbd5e1;border-radius:8px;background:#f8fafc;display:flex;align-items:center;justify-content:center}.rmt-cell:has(input:checked){background:#dbeafe;border-color:#007bff}.rmt-cell input{width:18px;height:18px;accent-color:#007bff}.rmt-out{padding:10px;border-radius:8px;background:#f8f9fa;border-left:4px solid #007bff}.rmt-ok{color:#166534;font-weight:600}.rmt-bad{color:#991b1b;font-weight:600}';
    document.head.appendChild(s);
  }
  function mount(host) {
    if (!host || host.dataset.rmtMounted) return;
    host.dataset.rmtMounted = '1';
    addStyle();
    var html = '<div class="rmt-wrap"><h4>Ma trận quan hệ trên A = {1,2,3}</h4><p>Chọn ô để thêm cặp (hàng, cột) vào quan hệ R.</p><div class="rmt-grid"><div></div>';
    A.forEach(function (j) { html += '<div class="rmt-head">' + j + '</div>'; });
    A.forEach(function (i) {
      html += '<div class="rmt-row">' + i + '</div>';
      A.forEach(function (j) { html += '<label class="rmt-cell" title="' + pairText(i, j) + '"><input type="checkbox" data-pair="' + pairKey(i, j) + '"></label>'; });
    });
    html += '</div><div class="rmt-out" aria-live="polite"></div></div>';
    host.insertAdjacentHTML('beforeend', html);
    var out = host.querySelector('.rmt-out');
    function render() {
      var pairs = Array.prototype.slice.call(host.querySelectorAll('input[data-pair]:checked')).map(function (el) {
        var p = el.dataset.pair.split(','); return pairText(p[0], p[1]);
      });
      var keys = {};
      Array.prototype.slice.call(host.querySelectorAll('input[data-pair]:checked')).forEach(function (el) { keys[el.dataset.pair] = true; });
      var missing = A.filter(function (x) { return !keys[pairKey(x, x)]; });
      out.innerHTML = '<strong>R = {' + (pairs.length ? pairs.join(', ') : '∅') + '}</strong><br>' + (missing.length ? '<span class="rmt-bad">Không phản xạ</span>: thiếu ' + missing.map(function (x) { return pairText(x, x); }).join(', ') : '<span class="rmt-ok">Phản xạ</span>: mọi (a,a) đều có trong R.');
    }
    host.addEventListener('change', render);
    render();
  }
  function safeMount(host) { try { mount(host); } catch (err) { if (host) host.innerHTML = '<div class="rmt-out">Không thể tải demo ma trận quan hệ. Hãy tải lại trang.</div>'; } }
  document.addEventListener('DOMContentLoaded', function () {
    safeMount(document.querySelector('#relation-explorer .interactive-tool') || document.querySelector('#relation-explorer'));
    Array.prototype.forEach.call(document.querySelectorAll('[data-demo="relation-matrix-toggle"]'), safeMount);
  });
})();
