(function () {
  function render() {
    var host1 = document.querySelector('[data-demo="proposition-checker"]');
    var host2 = document.querySelector('[data-demo="logic-evaluator"]');

    // Proposition checker (Chapter 1, lesson 1)
    if (host1) {
      host1.insertAdjacentHTML(
        'beforeend',
        '<div class="pch-wrap">' +
          '<label>Nhập câu để kiểm tra:</label>' +
          '<input id="pch-input" type="text" placeholder="Ví dụ: 2 + 2 = 4" />' +
          '<button id="pch-check">Kiểm tra</button>' +
          '<div id="pch-fb" class="pch-fb"></div>' +
        '</div>'
      );

      if (!document.getElementById('pch-style')) {
        var s = document.createElement('style');
        s.id = 'pch-style';
        s.textContent =
          '.pch-wrap{border:1px solid #e5e7eb;border-radius:10px;padding:12px;background:#fff;margin:12px 0}' +
          '.pch-wrap input{padding:6px 8px;border:1px solid #cbd5e1;border-radius:6px;width:70%}' +
          '.pch-wrap button{margin-left:6px;padding:6px 10px;border:1px solid #2563eb;background:#2563eb;color:#fff;border-radius:6px;cursor:pointer}' +
          '.pch-fb{margin-top:8px;padding:8px;border-radius:8px;font-size:14px}';
        document.head.appendChild(s);
      }

      var checkBtn = document.getElementById('pch-check');
      var inputEl = document.getElementById('pch-input');
      var fbEl = document.getElementById('pch-fb');

      var examples = {
        '2+2=4': { ok: true, msg: 'Đây là mệnh đề đúng (giá trị chân lý: Đúng).' },
        '2+2=5': { ok: true, msg: 'Đây là mệnh đề sai (giá trị chân lý: Sai).' },
        'Hà Nội là thủ đô của Việt Nam': { ok: true, msg: 'Đây là mệnh đề đúng (giá trị chân lý: Đúng).' },
        'x+1=5': { ok: false, msg: 'Không phải mệnh đề: giá trị phụ thuộc vào x.' },
        'Hôm nay trời đẹp quá!': { ok: false, msg: 'Không phải mệnh đề: đây là ý kiến chủ quan.' },
        'Mấy giờ rồi?': { ok: false, msg: 'Không phải mệnh đề: đây là câu hỏi.' },
        'Hãy đóng cửa!': { ok: false, msg: 'Không phải mệnh đề: đây là câu mệnh lệnh.' }
      };

      checkBtn.addEventListener('click', function () {
        var input = inputEl.value.trim();
        if (!input) { fbEl.textContent = 'Vui lòng nhập một câu.'; fbEl.style.color = '#64748b'; return; }

        var key = Object.keys(examples).find(function (k) { return input.indexOf(k) !== -1; });
        if (key) {
          var r = examples[key];
          fbEl.textContent = r.msg;
          fbEl.style.color = r.ok ? '#166534' : '#991b1b';
        } else {
          fbEl.innerHTML = 'Chưa có trong bộ mẫu. Gợi ý: nếu câu có thể khẳng định đúng/sai khách quan → mệnh đề. Nếu là câu hỏi/mệnh lệnh/cảm thán/chứa biến → không phải mệnh đề.';
          fbEl.style.color = '#475569';
        }
      });
    }

    // Logic evaluator (Chapter 1, lesson 2)
    if (host2) {
      host2.insertAdjacentHTML(
        'beforeend',
        '<div class="lev-wrap">' +
          '<div class="lev-row">' +
            'p: <select id="lev-p"><option value="T">T</option><option value="F">F</option></select> ' +
            'q: <select id="lev-q"><option value="T">T</option><option value="F">F</option></select> ' +
            'r: <select id="lev-r"><option value="T">T</option><option value="F">F</option></select>' +
          '</div>' +
          '<div class="lev-row">' +
            '<label>Biểu thức: <input id="lev-expr" value="(p -> q) and (q -> r)" size="40"/></label>' +
          '</div>' +
          '<button id="lev-run">Tính giá trị</button>' +
          '<div id="lev-output" class="lev-output"></div>' +
        '</div>'
      );

      if (!document.getElementById('lev-style')) {
        var s2 = document.createElement('style');
        s2.id = 'lev-style';
        s2.textContent =
          '.lev-wrap{border:1px solid #e5e7eb;border-radius:10px;padding:12px;background:#fff;margin:12px 0}' +
          '.lev-row{display:flex;gap:8px;align-items:center;margin-bottom:8px}' +
          '.lev-row input{padding:6px;border:1px solid #cbd5e1;border-radius:6px}' +
          '.lev-wrap select{padding:6px;border:1px solid #cbd5e1;border-radius:6px}' +
          '.lev-wrap button{padding:6px 10px;border:1px solid #2563eb;background:#2563eb;color:#fff;border-radius:6px;cursor:pointer}' +
          '.lev-output{margin-top:8px;padding:8px;border-radius:8px;font-size:14px}';
        document.head.appendChild(s2);
      }

      // Simple tokenizer + parser for and/or/not/->/<-> and T/F
      function tokenize(expr) {
        var src = expr.replace(/\s+/g, '')
          .replace(/<->/g, '↔').replace(/->/g, '→')
          .replace(/and/gi, '∧').replace(/or/gi, '∨').replace(/not/gi, '!');
        var tokens = [];
        for (var i = 0; i < src.length; i++) {
          var ch = src[i];
          if ('()!∧∨→↔'.indexOf(ch) !== -1) tokens.push(ch);
          else if (/[pqr]/i.test(ch)) tokens.push(ch.toLowerCase());
          else if (/[TF10]/.test(ch)) tokens.push(ch === 'T' || ch === '1' ? '1' : '0');
          else throw new Error('Ký tự không hợp lệ: ' + ch);
        }
        return tokens;
      }

      var prec = { '!': 5, '∧': 4, '∨': 3, '→': 2, '↔': 1 };
      var rightAssoc = { '!': true, '→': true, '↔': true };

      function toRpn(tokens) {
        var out = [], ops = [], i, t, o;
        for (i = 0; i < tokens.length; i++) {
          t = tokens[i];
          if (/[pqr01]/.test(t)) out.push(t);
          else if (t === '(') ops.push(t);
          else if (t === ')') {
            while (ops.length && ops[ops.length - 1] !== '(') out.push(ops.pop());
            if (!ops.length) throw new Error('Ngoặc không khớp.');
            ops.pop();
          } else {
            while (ops.length && ops[ops.length - 1] !== '(' &&
              ((rightAssoc[t] && prec[t] < prec[ops[ops.length - 1]]) ||
               (!rightAssoc[t] && prec[t] <= prec[ops[ops.length - 1]]))) {
              out.push(ops.pop());
            }
            ops.push(t);
          }
        }
        while (ops.length) {
          o = ops.pop();
          if (o === '(' || o === ')') throw new Error('Ngoặc không khớp.');
          out.push(o);
        }
        return out;
      }

      function evalRpn(rpn, env) {
        var st = [], i, t;
        for (i = 0; i < rpn.length; i++) {
          t = rpn[i];
          if (/[pqr01]/.test(t)) st.push(env[t] === '1' || env[t] === 'T' || env[t] === true);
          else if (t === '!') st.push(!st.pop());
          else {
            var b = st.pop(), a = st.pop();
            if (t === '∧') st.push(a && b);
            else if (t === '∨') st.push(a || b);
            else if (t === '→') st.push(!a || b);
            else if (t === '↔') st.push(a === b);
          }
        }
        if (st.length !== 1) throw new Error('Biểu thức lỗi.');
        return st[0];
      }

      document.getElementById('lev-run').addEventListener('click', function () {
        var out = document.getElementById('lev-output');
        try {
          var pVal = document.getElementById('lev-p').value;
          var qVal = document.getElementById('lev-q').value;
          var rVal = document.getElementById('lev-r').value;
          var expr = document.getElementById('lev-expr').value;
          var tokens = tokenize(expr);
          var rpn = toRpn(tokens);
          var env = { p: pVal, q: qVal, r: rVal, '0': '0', '1': '1' };
          var result = evalRpn(rpn, env);
          out.textContent = 'Kết quả: ' + (result ? 'Đúng (T)' : 'Sai (F)');
          out.style.color = result ? '#166534' : '#991b1b';
        } catch (e) {
          out.textContent = 'Lỗi: ' + e.message;
          out.style.color = '#b91c1c';
        }
      });
    }
  }

  document.addEventListener('DOMContentLoaded', render);
})();
