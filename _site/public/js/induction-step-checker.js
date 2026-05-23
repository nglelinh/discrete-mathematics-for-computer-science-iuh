(function () {
  function render() {
    var host = document.querySelector('[data-demo="induction-checker"]');
    if (!host) return;

    host.insertAdjacentHTML(
      'beforeend',
      '<div class="iic-wrap">' +
        '<p>Chọn đúng các thành phần của chứng minh quy nạp cho định lý <strong>1+2+...+n = n(n+1)/2</strong>:</p>' +
        '<div class="iic-step">' +
          '<label>1. Mệnh đề P(n) là:</label>' +
          '<select id="iic-s1">' +
            '<option value="">---</option>' +
            '<option value="A">1+2+...+n = n(n+1)/2</option>' +
            '<option value="B">n(n+1)/2 = tổng</option>' +
            '<option value="C">n ≥ 1</option>' +
          '</select>' +
        '</div>' +
        '<div class="iic-step">' +
          '<label>2. Bước cơ sở P(1) kiểm tra:</label>' +
          '<select id="iic-s2">' +
            '<option value="">---</option>' +
            '<option value="A">1 = 1·2/2 = 1 → đúng</option>' +
            '<option value="B">1+2 = 3 = 3·4/2 = 6 → sai</option>' +
            '<option value="C">0 = 0·1/2 = 0 → đúng</option>' +
          '</select>' +
        '</div>' +
        '<div class="iic-step">' +
          '<label>3. Giả thiết quy nạp (đúng):</label>' +
          '<select id="iic-s3">' +
            '<option value="">---</option>' +
            '<option value="A">P(k+1) đúng</option>' +
            '<option value="B">P(k) đúng: 1+...+k = k(k+1)/2</option>' +
            '<option value="C">P(n) đúng với mọi n</option>' +
          '</select>' +
        '</div>' +
        '<div class="iic-step">' +
          '<label>4. Cần chứng minh:</label>' +
          '<select id="iic-s4">' +
            '<option value="">---</option>' +
            '<option value="A">P(k+1): 1+...+(k+1) = (k+1)(k+2)/2</option>' +
            '<option value="B">P(k): 1+...+k = k(k+1)/2</option>' +
            '<option value="C">P(n) với n tùy ý</option>' +
          '</select>' +
        '</div>' +
        '<button id="iic-check" class="iic-btn">Kiểm tra chứng minh</button>' +
        '<button id="iic-reset" class="iic-btn iic-reset">Làm lại</button>' +
        '<div id="iic-fb" class="iic-fb"></div>' +
      '</div>'
    );

    if (!document.getElementById('iic-style')) {
      var s = document.createElement('style');
      s.id = 'iic-style';
      s.textContent =
        '.iic-wrap{border:1px solid #e5e7eb;border-radius:10px;padding:16px;background:#fff;margin:12px 0}' +
        '.iic-step{margin:8px 0}' +
        '.iic-step label{display:block;margin-bottom:4px}' +
        '.iic-step select{width:100%;padding:6px;border:1px solid #cbd5e1;border-radius:6px}' +
        '.iic-btn{padding:7px 10px;border:1px solid #2563eb;background:#2563eb;color:#fff;border-radius:6px;cursor:pointer;margin:4px 4px 0 0}' +
        '.iic-reset{background:#fff;color:#334155;border-color:#cbd5e1}' +
        '.iic-fb{margin-top:10px;padding:8px;border-radius:8px;font-size:14px}' +
        '.iic-fb.ok{background:#dcfce7;color:#166534}' +
        '.iic-fb.err{background:#fee2e2;color:#991b1b}';
      document.head.appendChild(s);
    }

    var correct = { s1: 'A', s2: 'A', s3: 'B', s4: 'A' };
    var fb = document.getElementById('iic-fb');

    document.getElementById('iic-check').addEventListener('click', function () {
      var keys = ['iic-s1', 'iic-s2', 'iic-s3', 'iic-s4'];
      var allOk = true;
      var msgs = [];
      keys.forEach(function (k) {
        var val = document.getElementById(k).value;
        var step = k.replace('iic-s', '');
        if (!val) {
          allOk = false;
          msgs.push('Bước ' + step + ': chưa chọn.');
        } else if (val !== correct['s' + step]) {
          allOk = false;
          msgs.push('Bước ' + step + ': chưa đúng.');
        }
      });
      fb.className = 'iic-fb ' + (allOk ? 'ok' : 'err');
      if (allOk) {
        fb.innerHTML = '✅ Hoàn chỉnh! P(n) đúng với mọi n ≥ 1 theo nguyên lý quy nạp.';
      } else {
        fb.innerHTML = '❌ ' + (msgs.length ? msgs.join(' ') : 'Kiểm tra lại.');
      }
    });

    document.getElementById('iic-reset').addEventListener('click', function () {
      ['iic-s1', 'iic-s2', 'iic-s3', 'iic-s4'].forEach(function (id) { document.getElementById(id).value = ''; });
      fb.className = 'iic-fb';
      fb.textContent = '';
    });
  }

  document.addEventListener('DOMContentLoaded', render);
})();
