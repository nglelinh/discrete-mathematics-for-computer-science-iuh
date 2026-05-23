(function () {
  function render() {
    var host = document.querySelector('[data-tool="relation-practice-checker"]');
    if (!host) return;

    host.insertAdjacentHTML(
      'beforeend',
      '<div class="rpc-wrap">' +
        '<p>Nhập các cặp (a,b) của quan hệ trên tập nền <strong>A = {1,2,3}</strong>, phân cách bằng dấu phẩy:</p>' +
        '<input id="rpc-input" type="text" placeholder="Ví dụ: (1,1),(1,2),(2,1),(2,2),(3,3)" size="60"/>' +
        '<button id="rpc-check">Kiểm tra tính chất</button>' +
        '<div id="rpc-output" class="rpc-output"></div>' +
      '</div>'
    );

    if (!document.getElementById('rpc-style')) {
      var s = document.createElement('style');
      s.id = 'rpc-style';
      s.textContent =
        '.rpc-wrap{border:1px solid #e5e7eb;border-radius:10px;padding:12px;background:#fff;margin:12px 0}' +
        '.rpc-wrap input{padding:6px 8px;border:1px solid #cbd5e1;border-radius:6px;width:70%}' +
        '.rpc-wrap button{margin-left:6px;padding:6px 10px;border:1px solid #2563eb;background:#2563eb;color:#fff;border-radius:6px;cursor:pointer}' +
        '.rpc-output{margin-top:10px;padding:10px;border-radius:8px;font-size:14px}' +
        '.rpc-prop{padding:4px 0}' +
        '.rpc-pass{color:#166534}' +
        '.rpc-fail{color:#991b1b}';
      document.head.appendChild(s);
    }

    function parsePairs(val) {
      var pairs = [];
      var re = /\((\d+),(\d+)\)/g;
      var m;
      while ((m = re.exec(val)) !== null) {
        pairs.push([Number(m[1]), Number(m[2])]);
      }
      return pairs;
    }

    function pairStr(a, b) { return '(' + a + ',' + b + ')'; }

    document.getElementById('rpc-check').addEventListener('click', function () {
      var val = document.getElementById('rpc-input').value;
      var pairs = parsePairs(val);
      var out = document.getElementById('rpc-output');

      if (pairs.length === 0) {
        out.innerHTML = '<span class="rpc-fail">Không tìm thấy cặp hợp lệ. Nhập dạng (1,2),(2,1).</span>';
        return;
      }

      var base = [1, 2, 3];
      var set = {};
      pairs.forEach(function (p) { set[pairStr(p[0], p[1])] = true; });

      // reflexive
      var refl = base.every(function (x) { return set[pairStr(x, x)]; });
      var reflFail = refl ? '' : base.filter(function (x) { return !set[pairStr(x, x)]; }).join(', ');

      // symmetric
      var sym = pairs.every(function (p) { return p[0] === p[1] || set[pairStr(p[1], p[0])]; });
      var symFail = '';
      if (!sym) {
        pairs.forEach(function (p) {
          if (p[0] !== p[1] && !set[pairStr(p[1], p[0])]) symFail = pairStr(p[0], p[1]) + ' thiếu chiều ngược';
        });
      }

      // antisymmetric
      var antisym = pairs.every(function (p) {
        return p[0] === p[1] || !set[pairStr(p[1], p[0])];
      });
      var antiFail = '';
      if (!antisym) {
        pairs.forEach(function (p) {
          if (p[0] !== p[1] && set[pairStr(p[1], p[0])]) antiFail = pairStr(p[0], p[1]) + ' và ' + pairStr(p[1], p[0]) + ' cùng có';
        });
      }

      // transitive
      var trans = true;
      var transFail = '';
      var keys = Object.keys(set);
      var i, j, k;
      outer:
      for (i = 0; i < base.length; i++) {
        for (j = 0; j < base.length; j++) {
          for (k = 0; k < base.length; k++) {
            if (set[pairStr(base[i], base[j])] && set[pairStr(base[j], base[k])] && !set[pairStr(base[i], base[k])]) {
              trans = false;
              transFail = pairStr(base[i], base[j]) + ' và ' + pairStr(base[j], base[k]) + ' có nhưng thiếu ' + pairStr(base[i], base[k]);
              break outer;
            }
          }
        }
      }

      var html = '';
      html += '<div class="rpc-prop"><strong>Phản xạ:</strong> ';
      html += refl ? '<span class="rpc-pass">Đúng</span>' : '<span class="rpc-fail">Sai (thiếu: ' + reflFail + ')</span>';
      html += '</div>';

      html += '<div class="rpc-prop"><strong>Đối xứng:</strong> ';
      html += sym ? '<span class="rpc-pass">Đúng</span>' : '<span class="rpc-fail">Sai (' + symFail + ')</span>';
      html += '</div>';

      html += '<div class="rpc-prop"><strong>Phản đối xứng:</strong> ';
      html += antisym ? '<span class="rpc-pass">Đúng</span>' : '<span class="rpc-fail">Sai (' + antiFail + ')</span>';
      html += '</div>';

      html += '<div class="rpc-prop"><strong>Bắc cầu:</strong> ';
      html += trans ? '<span class="rpc-pass">Đúng</span>' : '<span class="rpc-fail">Sai (' + transFail + ')</span>';
      html += '</div>';

      out.innerHTML = html;
    });
  }

  document.addEventListener('DOMContentLoaded', render);
})();
