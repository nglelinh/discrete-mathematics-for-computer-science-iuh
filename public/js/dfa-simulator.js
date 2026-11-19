/**
 * DFA simulator — even number of 1s on {0,1}.
 * Mount: <div data-demo="dfa-simulator"></div>
 */
(function () {
  function addStyle() {
    if (document.getElementById("dfa-sim-style")) return;
    var s = document.createElement("style");
    s.id = "dfa-sim-style";
    s.textContent =
      ".dfa-wrap{border:1px solid #e2e8f0;border-radius:12px;padding:16px;background:#fff;margin:14px 0;font-family:system-ui,sans-serif}" +
      ".dfa-wrap h4{margin:0 0 8px;color:#004586}" +
      ".dfa-wrap p{margin:0 0 10px;color:#64748b;font-size:.92rem;line-height:1.45}" +
      ".dfa-row{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:8px 0}" +
      ".dfa-row input{padding:8px 10px;border:1px solid #cbd5e1;border-radius:8px;min-width:220px;font-family:ui-monospace,monospace}" +
      ".dfa-row button{border:1px solid #cbd5e1;background:#f8fafc;border-radius:8px;padding:8px 12px;cursor:pointer;font-weight:600}" +
      ".dfa-row button:hover{background:#e8f1fb;border-color:#004586;color:#004586}" +
      ".dfa-board{display:flex;gap:40px;justify-content:center;align-items:center;min-height:120px;margin:12px 0;padding:16px;background:#fafbfc;border:1px solid #e2e8f0;border-radius:12px}" +
      ".dfa-state{width:64px;height:64px;border-radius:50%;border:3px solid #004586;display:flex;align-items:center;justify-content:center;font-weight:700;color:#004586;background:#fff;position:relative;transition:.2s}" +
      ".dfa-state.accept{box-shadow:inset 0 0 0 4px #fff,inset 0 0 0 7px #004586}" +
      ".dfa-state.cur{background:#dbeafe;transform:scale(1.08)}" +
      ".dfa-out{padding:10px 12px;border-radius:8px;background:#e8f1fb;border-left:4px solid #004586;line-height:1.6;font-size:.95rem}" +
      ".dfa-out.ok{background:#dcfce7;border-left-color:#16a34a}" +
      ".dfa-out.bad{background:#fee2e2;border-left-color:#dc2626}" +
      ".dfa-steps{margin-top:8px;font-family:ui-monospace,monospace;font-size:.88rem;color:#334155}";
    document.head.appendChild(s);
  }

  function mount(host) {
    if (!host || host.dataset.dfaMounted) return;
    host.dataset.dfaMounted = "1";
    addStyle();
    // DFA: even number of 1s
    var delta = {
      q0: { "0": "q0", "1": "q1" },
      q1: { "0": "q1", "1": "q0" }
    };
    var labels = { q0: "q₀ (chẵn)", q1: "q₁ (lẻ)" };
    host.innerHTML =
      '<div class="dfa-wrap"><h4>Mô phỏng DFA — chẵn số bit 1</h4>' +
      "<p>Σ = {0,1}. Trạng thái chấp nhận: q₀. Nhập chuỗi và bấm «Chạy» hoặc «Từng bước».</p>" +
      '<div class="dfa-row"><input data-w type="text" value="1100" placeholder="chuỗi 0/1">' +
      '<button type="button" data-run>Chạy</button>' +
      '<button type="button" data-step>Từng bước</button>' +
      '<button type="button" data-reset>Reset</button></div>' +
      '<div class="dfa-board">' +
      '<div class="dfa-state accept" data-s="q0">q₀</div>' +
      '<div class="dfa-state" data-s="q1">q₁</div>' +
      "</div>" +
      '<div class="dfa-out" data-out>Sẵn sàng.</div>' +
      '<div class="dfa-steps" data-steps></div></div>';

    var cur = "q0";
    var i = 0;
    var w = "";
    var path = ["q0"];

    function paint(msg, cls) {
      host.querySelectorAll(".dfa-state").forEach(function (el) {
        el.classList.toggle("cur", el.dataset.s === cur);
      });
      var out = host.querySelector("[data-out]");
      out.className = "dfa-out" + (cls ? " " + cls : "");
      out.textContent = msg;
      host.querySelector("[data-steps]").textContent =
        "Đường: " + path.map(function (q) { return q === "q0" ? "q₀" : "q₁"; }).join(" → ");
    }

    function reset() {
      cur = "q0";
      i = 0;
      path = ["q0"];
      w = (host.querySelector("[data-w]").value || "").replace(/[^01]/g, "");
      host.querySelector("[data-w]").value = w;
      paint("Chuỗi: «" + (w || "ε") + "». Bắt đầu tại q₀.", "");
    }

    function stepOnce() {
      if (i >= w.length) {
        var ok = cur === "q0";
        paint(
          ok
            ? "Hết chuỗi tại " + labels[cur] + " ∈ F → CHẤP NHẬN."
            : "Hết chuỗi tại " + labels[cur] + " ∉ F → TỪ CHỐI.",
          ok ? "ok" : "bad"
        );
        return false;
      }
      var a = w[i];
      var next = delta[cur][a];
      cur = next;
      path.push(cur);
      i++;
      paint(
        "Đọc '" + a + "' → " + labels[cur] + (i >= w.length ? " (hết chuỗi)" : ""),
        i >= w.length ? (cur === "q0" ? "ok" : "bad") : ""
      );
      if (i >= w.length) {
        var ok2 = cur === "q0";
        paint(
          "Hết chuỗi tại " + labels[cur] + (ok2 ? " ∈ F → CHẤP NHẬN." : " ∉ F → TỪ CHỐI."),
          ok2 ? "ok" : "bad"
        );
        return false;
      }
      return true;
    }

    host.querySelector("[data-run]").onclick = function () {
      reset();
      while (stepOnce()) {}
    };
    host.querySelector("[data-step]").onclick = function () {
      if (i === 0 && path.length === 1) {
        w = (host.querySelector("[data-w]").value || "").replace(/[^01]/g, "");
        host.querySelector("[data-w]").value = w;
      }
      stepOnce();
    };
    host.querySelector("[data-reset]").onclick = reset;
    host.querySelector("[data-w]").addEventListener("change", reset);
    reset();
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('[data-demo="dfa-simulator"]').forEach(mount);
  });
})();
