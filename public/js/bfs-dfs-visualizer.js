/**
 * BFS / DFS step-by-step visualizer for textbook lessons.
 * Mount: <div data-demo="bfs-dfs-visualizer"></div>
 */
(function () {
  function addStyle() {
    if (document.getElementById("bdv-style")) return;
    var s = document.createElement("style");
    s.id = "bdv-style";
    s.textContent = [
      ".bdv-wrap{border:1px solid #e2e8f0;border-radius:12px;padding:16px 18px;background:#fff;margin:14px 0;font-family:system-ui,-apple-system,sans-serif;color:#0f172a}",
      ".bdv-wrap h4{margin:0 0 6px;font-size:1.05rem;color:#004586}",
      ".bdv-wrap p.bdv-help{margin:0 0 10px;color:#64748b;font-size:.92rem;line-height:1.45}",
      ".bdv-toolbar{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:8px 0 12px}",
      ".bdv-toolbar button{border:1px solid #cbd5e1;background:#f8fafc;border-radius:8px;padding:7px 12px;cursor:pointer;font-weight:600;font-size:.9rem}",
      ".bdv-toolbar button:hover{background:#e8f1fb;border-color:#004586;color:#004586}",
      ".bdv-toolbar button:disabled{opacity:.45;cursor:not-allowed}",
      ".bdv-toolbar button.bdv-primary{background:#004586;color:#fff;border-color:#004586}",
      ".bdv-toolbar label{font-size:.9rem;color:#475569;display:flex;align-items:center;gap:6px}",
      ".bdv-board{position:relative;height:280px;border:1px solid #e2e8f0;border-radius:12px;background:#fafbfc;margin:8px 0 12px;overflow:hidden}",
      ".bdv-line{position:absolute;height:3px;background:#94a3b8;transform-origin:left center;z-index:1}",
      ".bdv-line.active{background:#004586;height:4px}",
      ".bdv-node{position:absolute;width:46px;height:46px;border-radius:999px;border:2.5px solid #64748b;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:700;transform:translate(-50%,-50%);z-index:2;transition:background .2s,border-color .2s,box-shadow .2s;box-shadow:0 1px 2px rgba(15,23,42,.06)}",
      ".bdv-node .bdv-id{font-size:14px;line-height:1;color:#0f172a}",
      ".bdv-node .bdv-d{font-size:10px;color:#64748b;margin-top:2px;font-weight:600}",
      ".bdv-node.frontier{background:#fff7ed;border-color:#ea580c;box-shadow:0 0 0 3px rgba(234,88,12,.15)}",
      ".bdv-node.current{background:#dbeafe;border-color:#004586;box-shadow:0 0 0 3px rgba(0,69,134,.2)}",
      ".bdv-node.done{background:#dcfce7;border-color:#16a34a}",
      ".bdv-panels{display:grid;grid-template-columns:1fr 1fr;gap:10px}",
      "@media (max-width:640px){.bdv-panels{grid-template-columns:1fr}}",
      ".bdv-panel{border:1px solid #e2e8f0;border-radius:10px;padding:10px 12px;background:#f8fafc;min-height:72px}",
      ".bdv-panel h5{margin:0 0 6px;font-size:.82rem;text-transform:uppercase;letter-spacing:.04em;color:#64748b}",
      ".bdv-panel .bdv-val{font-size:.95rem;line-height:1.5;color:#0f172a;word-break:break-word}",
      ".bdv-log{margin-top:10px;padding:10px 12px;border-radius:10px;background:#e8f1fb;border-left:4px solid #004586;font-size:.92rem;line-height:1.5;min-height:2.6em}",
      ".bdv-legend{display:flex;gap:12px;flex-wrap:wrap;margin-top:10px;font-size:.82rem;color:#64748b}",
      ".bdv-dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:4px;vertical-align:middle;border:1px solid #94a3b8}",
      ".bdv-dot.frontier{background:#fff7ed;border-color:#ea580c}",
      ".bdv-dot.current{background:#dbeafe;border-color:#004586}",
      ".bdv-dot.done{background:#dcfce7;border-color:#16a34a}"
    ].join("");
    document.head.appendChild(s);
  }

  function mount(host) {
    if (!host || host.dataset.bdvMounted) return;
    host.dataset.bdvMounted = "1";
    addStyle();

    // Fixed undirected graph used in the lesson figures
    var pts = {
      1: [50, 14],
      2: [22, 40],
      3: [78, 40],
      4: [16, 78],
      5: [50, 78],
      6: [84, 78]
    };
    var adj = {
      1: [2, 3],
      2: [1, 4, 5],
      3: [1, 5, 6],
      4: [2],
      5: [2, 3],
      6: [3]
    };
    var edgePairs = [
      [1, 2],
      [1, 3],
      [2, 4],
      [2, 5],
      [3, 5],
      [3, 6]
    ];

    host.innerHTML =
      '<div class="bdv-wrap">' +
      "<h4>Duyệt đồ thị từng bước — BFS / DFS</h4>" +
      '<p class="bdv-help">Chọn thuật toán, bấm <strong>Bước tiếp</strong> để xem hàng đợi (BFS) hoặc ngăn xếp (DFS). ' +
      "Lần đầu BFS thăm đỉnh là đường ngắn nhất theo số cạnh.</p>" +
      '<div class="bdv-toolbar">' +
      '<label><input type="radio" name="bdv-mode-' +
      host.id +
      '" value="bfs" checked> BFS (hàng đợi)</label>' +
      '<label><input type="radio" name="bdv-mode-' +
      host.id +
      '" value="dfs"> DFS (ngăn xếp)</label>' +
      '<button type="button" class="bdv-primary" data-act="step">Bước tiếp</button>' +
      '<button type="button" data-act="auto">Chạy hết</button>' +
      '<button type="button" data-act="reset">Reset</button>' +
      "</div>" +
      '<div class="bdv-board"></div>' +
      '<div class="bdv-panels">' +
      '<div class="bdv-panel"><h5 data-struct>Hàng đợi (queue)</h5><div class="bdv-val" data-struct-val>—</div></div>' +
      '<div class="bdv-panel"><h5>Thứ tự thăm</h5><div class="bdv-val" data-order-val>—</div></div>' +
      "</div>" +
      '<div class="bdv-log" data-log>Chọn BFS hoặc DFS, rồi bấm «Bước tiếp».</div>' +
      '<div class="bdv-legend">' +
      '<span><i class="bdv-dot frontier"></i>Trong cấu trúc</span>' +
      '<span><i class="bdv-dot current"></i>Đang xử lý</span>' +
      '<span><i class="bdv-dot done"></i>Đã xong</span>' +
      "</div>" +
      "</div>";

    // unique radio name
    if (!host.id) host.id = "bdv-" + Math.random().toString(36).slice(2, 8);
    host.querySelectorAll('input[type="radio"]').forEach(function (r) {
      r.name = "bdv-mode-" + host.id;
    });

    var board = host.querySelector(".bdv-board");
    var structTitle = host.querySelector("[data-struct]");
    var structVal = host.querySelector("[data-struct-val]");
    var orderVal = host.querySelector("[data-order-val]");
    var logEl = host.querySelector("[data-log]");
    var btnStep = host.querySelector('[data-act="step"]');
    var btnAuto = host.querySelector('[data-act="auto"]');
    var timer = null;

    var mode = "bfs";
    var state = null;

    function modeLabel() {
      return mode === "bfs" ? "hàng đợi" : "ngăn xếp";
    }

    function drawGraph(activeEdge) {
      board.innerHTML = "";
      edgePairs.forEach(function (e) {
        var a = e[0],
          b = e[1];
        var p = pts[a],
          q = pts[b];
        var dx = q[0] - p[0],
          dy = q[1] - p[1];
        var len = Math.sqrt(dx * dx + dy * dy);
        var d = document.createElement("div");
        d.className = "bdv-line";
        if (
          activeEdge &&
          ((activeEdge[0] === a && activeEdge[1] === b) ||
            (activeEdge[0] === b && activeEdge[1] === a))
        ) {
          d.classList.add("active");
        }
        d.style.left = p[0] + "%";
        d.style.top = p[1] + "%";
        d.style.width = len + "%";
        d.style.transform = "rotate(" + Math.atan2(dy, dx) + "rad)";
        board.appendChild(d);
      });

      Object.keys(pts).forEach(function (k) {
        var n = document.createElement("div");
        n.className = "bdv-node";
        n.dataset.v = k;
        n.style.left = pts[k][0] + "%";
        n.style.top = pts[k][1] + "%";
        var distText =
          state && state.dist[k] !== undefined ? "d=" + state.dist[k] : "";
        n.innerHTML =
          '<span class="bdv-id">' +
          k +
          '</span><span class="bdv-d">' +
          distText +
          "</span>";
        if (state) {
          if (state.current === +k) n.classList.add("current");
          else if (state.done[k]) n.classList.add("done");
          else if (state.inStruct[k]) n.classList.add("frontier");
        }
        board.appendChild(n);
      });
    }

    function fmtStruct(arr) {
      if (!arr.length) return "∅ (rỗng)";
      if (mode === "bfs") return arr.join(" → ") + "  (đầu ← … → cuối)";
      return arr.join(" → ") + "  (đáy … → đỉnh)";
    }

    function paint(msg, activeEdge) {
      structTitle.textContent =
        mode === "bfs" ? "Hàng đợi (queue)" : "Ngăn xếp (stack)";
      structVal.textContent = state ? fmtStruct(state.struct.slice()) : "—";
      orderVal.textContent =
        state && state.order.length ? state.order.join(" → ") : "—";
      logEl.textContent = msg || "";
      drawGraph(activeEdge || null);
      var finished = state && state.finished;
      btnStep.disabled = !!finished;
      btnAuto.disabled = !!finished;
    }

    function reset(keepMode) {
      if (timer) {
        clearInterval(timer);
        timer = null;
      }
      if (!keepMode) {
        var checked = host.querySelector('input[value="bfs"]');
        if (checked) checked.checked = true;
        mode = "bfs";
      }
      state = {
        struct: [1],
        seen: { 1: true },
        inStruct: { 1: true },
        done: {},
        dist: { 1: 0 },
        order: [],
        current: null,
        finished: false,
        parent: { 1: null }
      };
      paint(
        "Bắt đầu từ đỉnh 1. " +
          (mode === "bfs"
            ? "BFS: lấy đầu hàng đợi; láng giềng chưa thăm vào cuối hàng đợi."
            : "DFS: lấy đỉnh ngăn xếp; láng giềng chưa thăm đẩy lên đỉnh ngăn xếp.") +
          " Bấm «Bước tiếp»."
      );
    }

    function stepOnce() {
      if (!state || state.finished) return false;

      if (!state.struct.length) {
        state.current = null;
        state.finished = true;
        paint(
          "Hoàn tất. Thứ tự thăm: " +
            state.order.join(" → ") +
            ". " +
            (mode === "bfs"
              ? "Với BFS, d=k là số cạnh tối thiểu từ 1."
              : "DFS không đảm bảo đường ngắn nhất.")
        );
        return false;
      }

      var v =
        mode === "bfs" ? state.struct.shift() : state.struct.pop();
      state.inStruct[v] = false;
      state.current = v;
      state.order.push(v);
      state.done[v] = true;

      var discovered = [];
      // stable neighbor order for pedagogy
      var neigh = adj[v].slice();
      if (mode === "dfs") neigh = neigh.slice().reverse();

      neigh.forEach(function (u) {
        if (!state.seen[u]) {
          state.seen[u] = true;
          state.inStruct[u] = true;
          state.struct.push(u);
          state.dist[u] = state.dist[v] + 1;
          state.parent[u] = v;
          discovered.push(u);
        }
      });

      var msg =
        "Xử lý đỉnh " +
        v +
        " (d=" +
        state.dist[v] +
        "). ";
      if (discovered.length) {
        msg +=
          "Khám phá " +
          discovered.join(", ") +
          " → đưa vào " +
          modeLabel() +
          ".";
      } else {
        msg += "Không có láng giềng mới.";
      }
      if (!state.struct.length) {
        msg += " " + modeLabel() + " rỗng — sắp kết thúc.";
      }

      paint(msg, discovered.length ? [v, discovered[0]] : null);
      return true;
    }

    function setMode(m) {
      mode = m;
      reset(true);
    }

    host.querySelectorAll('input[type="radio"]').forEach(function (r) {
      r.addEventListener("change", function () {
        if (r.checked) setMode(r.value);
      });
    });

    btnStep.addEventListener("click", function () {
      if (timer) {
        clearInterval(timer);
        timer = null;
      }
      stepOnce();
    });

    btnAuto.addEventListener("click", function () {
      if (timer) {
        clearInterval(timer);
        timer = null;
      }
      timer = setInterval(function () {
        if (!stepOnce()) {
          clearInterval(timer);
          timer = null;
        }
      }, 700);
    });

    host.querySelector('[data-act="reset"]').addEventListener("click", function () {
      reset(true);
    });

    reset(false);
  }

  document.addEventListener("DOMContentLoaded", function () {
    document
      .querySelectorAll('[data-demo="bfs-dfs-visualizer"]')
      .forEach(mount);
  });
})();
