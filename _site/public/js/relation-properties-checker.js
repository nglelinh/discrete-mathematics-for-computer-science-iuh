(function () {
  var A = [1, 2, 3];
  function key(a, b) { return a + ',' + b; }
  function txt(a, b) { return '(' + a + ',' + b + ')'; }
  function style() {
    if (document.getElementById('rpc2-style')) return;
    var s = document.createElement('style');
    s.id = 'rpc2-style';
    s.textContent = '.rpc2-wrap{border:1px solid #e5e7eb;border-radius:12px;padding:16px;background:#fff;margin:14px 0}.rpc2-row{display:flex;gap:8px;flex-wrap:wrap}.rpc2-row input{flex:1;min-width:260px;padding:10px;border:1px solid #cbd5e1;border-radius:8px}.rpc2-row button{padding:10px 16px;border:1px solid #007bff;background:#007bff;color:#fff;border-radius:8px;cursor:pointer}.rpc2-out{margin-top:12px;display:grid;gap:8px}.rpc2-card{padding:10px;border-radius:8px;background:#f8f9fa;border-left:4px solid #6c757d}.rpc2-pass{border-left-color:#28a745}.rpc2-fail{border-left-color:#dc3545}.rpc2-pass strong{color:#166534}.rpc2-fail strong{color:#991b1b}.rpc2-err{padding:10px;border-radius:8px;background:#fee2e2;color:#991b1b}';
    document.head.appendChild(s);
  }
  function parse(value) {
    var pairs = [], seen = {}, re = /\(\s*([123])\s*,\s*([123])\s*\)/g, m;
    while ((m = re.exec(value)) !== null) {
      var k = key(m[1], m[2]);
      if (!seen[k]) { seen[k] = true; pairs.push([Number(m[1]), Number(m[2])]); }
    }
    return pairs;
  }
  function hasInvalidTokens(value) {
    return value.replace(/\(\s*[123]\s*,\s*[123]\s*\)/g, '').replace(/[\s,]/g, '') !== '';
  }
  function check(pairs) {
    var set = {};
    pairs.forEach(function (p) { set[key(p[0], p[1])] = true; });
    var missRef = A.filter(function (x) { return !set[key(x, x)]; });
    var symBad = pairs.find(function (p) { return p[0] !== p[1] && !set[key(p[1], p[0])]; });
    var antiBad = pairs.find(function (p) { return p[0] !== p[1] && set[key(p[1], p[0])]; });
    var transBad = null;
    pairs.forEach(function (p) { pairs.forEach(function (q) { if (!transBad && p[1] === q[0] && !set[key(p[0], q[1])]) transBad = [p[0], p[1], q[1]]; }); });
    return [
      ['Phản xạ', !missRef.length, missRef.length ? 'Thiếu ' + missRef.map(function (x) { return txt(x, x); }).join(', ') : 'Mọi phần tử có cặp với chính nó.'],
      ['Đối xứng', !symBad, symBad ? 'Có ' + txt(symBad[0], symBad[1]) + ' nhưng thiếu ' + txt(symBad[1], symBad[0]) + '.' : 'Mỗi cặp đều có cặp đảo.'],
      ['Phản đối xứng', !antiBad, antiBad ? 'Có cả ' + txt(antiBad[0], antiBad[1]) + ' và ' + txt(antiBad[1], antiBad[0]) + ' với hai phần tử khác nhau.' : 'Không có hai chiều giữa hai phần tử khác nhau.'],
      ['Bắc cầu', !transBad, transBad ? 'Có ' + txt(transBad[0], transBad[1]) + ' và ' + txt(transBad[1], transBad[2]) + ' nhưng thiếu ' + txt(transBad[0], transBad[2]) + '.' : 'Mọi đường đi hai bước đều đã có cặp tắt.']
    ];
  }
  function mount(host) {
    if (!host || host.dataset.rpc2Mounted) return;
    host.dataset.rpc2Mounted = '1'; style();
    host.innerHTML = '<div class="rpc2-wrap"><h4>Kiểm tra tính chất quan hệ</h4><p>Tập nền A = {1,2,3}. Nhập các cặp theo dạng (1,1),(1,2).</p><div class="rpc2-row"><input type="text" value="(1,1),(1,2),(2,1),(2,2),(3,3)" aria-label="Các cặp của quan hệ"><button type="button">Kiểm tra</button></div><div class="rpc2-out" aria-live="polite"></div></div>';
    var input = host.querySelector('input'), out = host.querySelector('.rpc2-out');
    host.querySelector('button').addEventListener('click', function () {
      var pairs = parse(input.value.trim());
      if (!input.value.trim() || !pairs.length) { out.innerHTML = '<div class="rpc2-err">Không có cặp hợp lệ. Hãy nhập dạng (1,2),(2,1) với phần tử thuộc {1,2,3}.</div>'; return; }
      if (hasInvalidTokens(input.value.trim())) { out.innerHTML = '<div class="rpc2-err">Có phần nhập không hợp lệ. Chỉ dùng các cặp dạng (1,2) với phần tử thuộc {1,2,3}, ngăn cách bằng dấu phẩy.</div>'; return; }
      out.innerHTML = check(pairs).map(function (r) { return '<div class="rpc2-card ' + (r[1] ? 'rpc2-pass' : 'rpc2-fail') + '"><strong>' + (r[1] ? '✓ ' : '✗ ') + r[0] + '</strong><br>' + r[2] + '</div>'; }).join('');
    });
    host.querySelector('button').click();
  }
  function safeMount(host) { try { mount(host); } catch (err) { if (host) host.innerHTML = '<div class="rpc2-err">Không thể tải demo kiểm tra quan hệ. Hãy tải lại trang.</div>'; } }
  document.addEventListener('DOMContentLoaded', function () { Array.prototype.forEach.call(document.querySelectorAll('[data-demo="relation-classifier"]'), safeMount); });
})();
