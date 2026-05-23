(function () {
  function render() {
    var host = document.querySelector('[data-demo="direct-proof-builder"]');
    if (!host) return;

    host.insertAdjacentHTML(
      'beforeend',
      '<div class="dpb-wrap">' +
        '<p>Sắp xếp các bước thành chứng minh trực tiếp đúng cho định lý <strong>"Nếu n là số lẻ thì n² là số lẻ"</strong>:</p>' +
        '<ol id="dpb-steps" class="dpb-steps">' +
          '<li class="dpb-target" data-step="1">Thả bước 1 vào đây</li>' +
          '<li class="dpb-target" data-step="2">Thả bước 2 vào đây</li>' +
          '<li class="dpb-target" data-step="3">Thả bước 3 vào đây</li>' +
          '<li class="dpb-target" data-step="4">Thả bước 4 vào đây</li>' +
        '</ol>' +
        '<div class="dpb-pool" id="dpb-pool">' +
          '<div class="dpb-chip" draggable="true" data-id="B">Giả sử n là số lẻ</div>' +
          '<div class="dpb-chip" draggable="true" data-id="D">Theo định nghĩa, tồn tại k∈ℤ: n = 2k+1</div>' +
          '<div class="dpb-chip" draggable="true" data-id="A">n² = (2k+1)² = 4k² + 4k + 1 = 2(2k²+2k)+1</div>' +
          '<div class="dpb-chip" draggable="true" data-id="C">Vậy n² là số lẻ</div>' +
        '</div>' +
        '<button class="dpb-btn dpb-check-btn" id="dpb-check">Kiểm tra chứng minh</button>' +
        '<button class="dpb-btn dpb-reset-btn" id="dpb-reset">Làm lại</button>' +
        '<div class="dpb-feedback" id="dpb-feedback"></div>' +
      '</div>'
    );

    if (!document.getElementById('dpb-style')) {
      var s = document.createElement('style');
      s.id = 'dpb-style';
      s.textContent =
        '.dpb-wrap{border:1px solid #e5e7eb;border-radius:10px;padding:16px;background:#fff;margin:12px 0}' +
        '.dpb-steps{list-style:decimal;padding-left:24px}' +
        '.dpb-target{min-height:38px;border:2px dashed #cbd5e1;border-radius:8px;margin:6px 0;padding:6px 10px;color:#94a3b8;background:#f8fafc}' +
        '.dpb-target.filled{border-style:solid;background:#ecfeff;color:#155e75;font-weight:600}' +
        '.dpb-pool{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}' +
        '.dpb-chip{border:1px solid #64748b;border-radius:8px;padding:6px 10px;cursor:grab;background:#f1f5f9;color:#334155;font-size:13px}' +
        '.dpb-btn{padding:8px 14px;border-radius:8px;border:1px solid #cbd5e1;background:#fff;cursor:pointer;margin:4px 4px 0 0}' +
        '.dpb-check-btn{background:#2563eb;color:#fff;border-color:#2563eb}' +
        '.dpb-feedback{margin-top:10px;padding:8px;border-radius:8px;font-size:14px}' +
        '.dpb-feedback.ok{background:#dcfce7;color:#166534}' +
        '.dpb-feedback.error{background:#fee2e2;color:#991b1b}';
      document.head.appendChild(s);
    }

    var targets = host.querySelectorAll('.dpb-target');
    var chips = host.querySelectorAll('.dpb-chip');
    var feedback = document.getElementById('dpb-feedback');

    chips.forEach(function (chip) {
      chip.addEventListener('dragstart', function (e) {
        e.dataTransfer.setData('text/plain', chip.dataset.id);
      });
    });

    targets.forEach(function (target) {
      target.addEventListener('dragover', function (e) { e.preventDefault(); });
      target.addEventListener('drop', function (e) {
        e.preventDefault();
        var id = e.dataTransfer.getData('text/plain');
        target.dataset.chip = id;
        var chipText = host.querySelector('.dpb-chip[data-id="' + id + '"]');
        target.textContent = chipText ? chipText.textContent : id;
        target.classList.add('filled');
      });
    });

    document.getElementById('dpb-reset').addEventListener('click', function () {
      targets.forEach(function (t) {
        t.textContent = 'Thả bước ' + t.dataset.step + ' vào đây';
        t.classList.remove('filled');
        delete t.dataset.chip;
      });
      feedback.className = 'dpb-feedback';
      feedback.textContent = '';
    });

    document.getElementById('dpb-check').addEventListener('click', function () {
      var order = [];
      targets.forEach(function (t) { order.push(t.dataset.chip || '?'); });
      var correct = ['B', 'D', 'A', 'C'];
      var ok = order.every(function (v, i) { return v === correct[i]; });
      feedback.className = 'dpb-feedback ' + (ok ? 'ok' : 'error');
      if (ok) {
        feedback.innerHTML = '✅ Chứng minh hợp lệ: Giả thiết → định nghĩa → biến đổi → kết luận.';
      } else {
        feedback.innerHTML = '❌ Chưa đúng. Cấu trúc đúng: <br/>1. Giả sử n lẻ<br/>2. n = 2k+1 (định nghĩa)<br/>3. n² = 2(2k²+2k)+1 (biến đổi)<br/>4. Vậy n² lẻ.';
      }
    });
  }

  document.addEventListener('DOMContentLoaded', render);
})();
