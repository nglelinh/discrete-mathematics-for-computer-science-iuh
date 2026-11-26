"""Lồng tiếng cho các reel toán rời rạc (giọng Trường, ElevenLabs eleven_v3; dự phòng Gemini Algenib).

  python vo/dm_vo.py probe <reel>        chạy dò thời gian phụ đề (vo/probe.py) -> media/vo_cache/<reel>/probe.json
  python vo/dm_vo.py texts <reel>        in từng đoạn lời dẫn, số ký tự
  python vo/dm_vo.py plan  <reel>        xếp lịch đoạn thu (el_NN.mp3 hoặc gm_NN.wav) và báo tràn
  python vo/dm_vo.py mux   <reel>        ghép vào public/videos/reels/<video>.mp4 (bản không tiếng lưu ở media/vo_cache/<reel>/silent.mp4)
  python vo/dm_vo.py gemini <reel>       thu bằng Gemini TTS (cần GEMINI_API_KEY) -> gm_NN.wav

Lời dẫn nằm ở vo/narration_dm.py: REELS[tên] = (file.py, Scene, video.mp4, [(giây bắt đầu, lời dẫn)]).
Lời dẫn viết sẵn theo cách đọc (chữ cái đơn đọc thành tên chữ, số viết thành chữ). Mỗi đoạn bắt đầu đúng mốc phụ đề;
nếu đoạn trước còn đang đọc thì đoạn sau lùi lại (GAP 0,25 s). Nếu đoạn cuối vượt hết video thì kéo dài khung hình cuối.
Cache (mp3/wav/m4a/silent.mp4) ở manim/reels/media/vo_cache (gitignore); chỉ commit mp4 cuối và kịch bản."""
import json, os, shutil, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
REELS_DIR = os.path.abspath(os.path.join(HERE, ".."))
ROOT = os.path.abspath(os.path.join(REELS_DIR, "..", ".."))
CACHE = os.path.join(REELS_DIR, "media", "vo_cache")
PUB = os.path.join(ROOT, "public", "videos", "reels")
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.expanduser("~/teaching/skills/course-manim-voice/scripts"))
import vo_gemini as vg
from narration_dm import REELS
GAP, TAIL_PAD = 0.25, 0.5


def has_audio(p):
    return bool(subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", p], text=True).strip())


def d_of(reel):
    d = os.path.join(CACHE, reel); os.makedirs(d, exist_ok=True); return d


def probe(reel):
    f, sc, vid, segs = REELS[reel]
    out = os.path.join(d_of(reel), "probe.json")
    subprocess.run([sys.executable, os.path.join(HERE, "probe.py"), f, sc, out], cwd=REELS_DIR, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    j = json.load(open(out)); print(reel, "duration", j["duration"], "caption starts", [c[0] for c in j["captions"]])


def silent_path(reel):
    d = d_of(reel); s = os.path.join(d, "silent.mp4"); pub = os.path.join(PUB, REELS[reel][2])
    if not os.path.exists(s):
        assert not has_audio(pub), "video công khai đã có tiếng và chưa có bản không tiếng"
        shutil.copy(pub, s)
    return s


def plan(reel, kind=None, log=print):
    f, sc, vid, segs = REELS[reel]
    d = d_of(reel); out, prev_end = [], 0.0
    for i, (t, text) in enumerate(segs):
        src = None
        for k, ext in ((kind, None),) if kind else (("el", "mp3"), ("gm", "wav")):
            pass
        cand = [("el", "mp3"), ("gm", "wav")] if not kind else [kind]
        for pre, ext in cand:
            p = os.path.join(d, f"{pre}_{i:02d}.{ext}")
            if os.path.exists(p): src = (pre, p)
        if not src: raise SystemExit(f"thiếu đoạn {i} cho {reel}")
        wav = os.path.join(d, f"w_{i:02d}.wav")
        if src[0] == "gm": wav = src[1]
        elif not os.path.exists(wav):  # chỉ chỉnh âm lượng, không cắt khoảng lặng
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", src[1], "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "24000", "-ac", "1", wav], check=True)
        dur = vg.probe_duration(wav)
        start = max(t, prev_end + GAP) if i else t
        end = start + dur
        log(f"  seg {i} cap@{t:6.2f} start={start:6.2f} dur={dur:5.2f} end={end:6.2f} lag={start - t:4.2f}")
        out.append((wav, start, dur)); prev_end = end
    return out, prev_end


def mux(reel):
    f, sc, vid, segs = REELS[reel]
    pub = os.path.join(PUB, vid); silent = silent_path(reel); d = d_of(reel)
    out, vend = plan(reel)
    vd = vg.probe_duration(silent)
    video = silent
    need = vend + TAIL_PAD - vd
    if need > 0:  # kéo dài khung hình cuối cho đủ lời dẫn
        video = os.path.join(d, "silent_ext.mp4")
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", silent, "-vf", f"tpad=stop_mode=clone:stop_duration={need:.2f}", "-c:v", "libx264", "-crf", "20", "-preset", "slow", "-pix_fmt", "yuv420p", "-an", video], check=True)
        vd = vg.probe_duration(video); print(f"  kéo dài video thêm {need:.2f}s")
    m4a = os.path.join(d, "vo.m4a")
    vg.build_vo_track([(w, s) for w, s, _ in out], vd, m4a)
    vg.mux(video, m4a, pub)
    print(f"MUXED {pub} {vg.probe_duration(pub):.2f}s audio={has_audio(pub)} (video gốc {vg.probe_duration(silent):.2f}s)")


def main():
    mode, reel = sys.argv[1], sys.argv[2]
    if mode == "probe": probe(reel)
    elif mode == "texts":
        tot = 0
        for i, (t, x) in enumerate(REELS[reel][3]): print(i, t, len(x), x); tot += len(x)
        print("TOTAL", tot)
    elif mode == "plan": plan(reel)
    elif mode == "mux": mux(reel)
    elif mode == "gemini":
        d = d_of(reel)
        for i, (t, x) in enumerate(REELS[reel][3]):
            wav = os.path.join(d, f"gm_{i:02d}.wav")
            dur, model = vg.synth_segment(x, wav, models=("gemini-3.8-flash-tts",))
            print(f"  gm {i} {dur:.2f}s [{model}]", flush=True)


if __name__ == "__main__":
    main()
