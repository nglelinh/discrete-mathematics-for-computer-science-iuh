"""Chạy trên Mac: fetch_el.py <reel> status1.txt [status2.txt ...] — ánh xạ mỗi generation theo đầu lời dẫn rồi tải el_NN.mp3 vào media/vo_cache/<reel>/."""
import json, os, sys, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from narration_dm import REELS
reel = sys.argv[1]; texts = [t for _, t in REELS[reel][3]]
d = os.path.join(HERE, '..', 'media', 'vo_cache', reel); os.makedirs(d, exist_ok=True)
got = set()
for fn in sys.argv[2:]:
    s = open(fn).read(); s = s[s.index('{'):s.rindex('}') + 1]; j = json.loads(s)
    for g in j['generations']:
        if g['status'] != 'completed' or not g.get('content_url'): print('chưa xong', g['id'], g['status']); continue
        p = g.get('prompt') or ''
        idx = [i for i, t in enumerate(texts) if t[:40] == p[:40]]
        if len(idx) != 1: print('không ánh xạ được', g['id'], p[:40], idx); continue
        i = idx[0]; urllib.request.urlretrieve(g['content_url'], os.path.join(d, f'el_{i:02d}.mp3')); got.add(i)
print('đã tải', sorted(got), 'trên', len(texts), 'đoạn', 'ĐỦ' if len(got) == len(texts) else 'CÒN THIẾU')
