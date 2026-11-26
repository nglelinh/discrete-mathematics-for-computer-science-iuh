"""Ghi mốc thời gian phụ đề (caption) của một reel Manim mà không cần render video.

  python vo/probe.py <file.py> <Scene> <out.json>

Phụ đề = Text nằm ở y = CAP_Y (6.3), x = 0. Ghi (giây, nội dung) mỗi khi phụ đề đổi, và tổng thời lượng cảnh.
Dùng để canh lời dẫn: chạy trong thư mục manim/reels (common.py ở đó)."""
import importlib, json, os, sys
sys.path.insert(0, os.getcwd())
from manim import config, Scene, Text
config.write_to_movie = False
config.disable_caching = True
config.quality = "low_quality"
config.frame_rate = 60
config.verbosity = "ERROR"
config.progress_bar = "none"

# Máy này không có LaTeX đầy đủ (thiếu standalone.cls/dvisvgm): thay bằng SVG giả để chạy dò thời gian
import tempfile
_dummy = os.path.join(tempfile.gettempdir(), "vo_probe_dummy.svg")
open(_dummy, "w").write('<svg xmlns="http://www.w3.org/2000/svg" width="40" height="20" viewBox="0 0 40 20"><path d="M0 0 L40 0 L40 20 L0 20 Z" fill="white"/></svg>')
import manim.mobject.text.tex_mobject as _tm
_tm.tex_to_svg_file = lambda *a, **k: _dummy

log, state = [], {"last": None}
_play, _wait = Scene.play, Scene.wait


def cur_cap(scene):
    best = None
    for m in scene.mobjects:
        if isinstance(m, Text) and abs(m.get_center()[1] - 6.3) < 0.05 and abs(m.get_center()[0]) < 0.05:
            best = m.text if best is None else best
    return best


def wrap(orig):
    def f(self, *a, **kw):
        t0 = self.renderer.time
        r = orig(self, *a, **kw)
        c = cur_cap(self)
        if c != state["last"]:
            log.append((round(t0, 2), c)); state["last"] = c
        return r
    return f


Scene.play, Scene.wait = wrap(_play), wrap(_wait)
file, scene_name, out = sys.argv[1:4]
mod = importlib.import_module(file[:-3])
sc = getattr(mod, scene_name)()
sc.render()
json.dump({"duration": round(sc.renderer.time, 2), "captions": log}, open(out, "w"), ensure_ascii=False, indent=1)
print("duration", round(sc.renderer.time, 2), "captions", len(log))
