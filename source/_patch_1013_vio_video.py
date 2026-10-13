#!/usr/bin/env python3
"""13.10 Мирослав: відео креативів Віоріки (Влад на дзвінку 12.10: «вот такие видео… видосы я тебе прислал») — новий екран після креативів-картинок (new-x12v4)."""
import json, shutil, time, copy
from pathlib import Path
R = Path(__file__).resolve().parent.parent
OV = R / 'source/overrides.json'
o = json.load(open(OV)); do = o['__deckOrder']; E = do['entries']
shutil.copy(OV, R / f'source/_bak/overrides-1013-before-vio-video-{int(time.time())}.json')
s = copy.deepcopy(do['slides']['new-x12v4'])
V = 'assets/gen-rest-1012/s7/vio-video-'
s['b'] = (f'<div class="s2n s2n-pic s12-ads s12-vids"><video src="{V}1.mp4" poster="{V}1.jpg" autoplay muted loop playsinline preload="auto"></video>'
          f'<video src="{V}2.mp4" poster="{V}2.jpg" autoplay muted loop playsinline preload="auto"></video></div>')
s['note'] = '13.10: відео креативів Віоріки (~Downloads/viorika1/2.MOV від Мирослава), після креативів-картинок G131.'
do['slides']['new-x12v4v'] = s
i = next(k for k, e in enumerate(E) if isinstance(e, dict) and e.get('new') == 'new-x12v4')
if not any(isinstance(e, dict) and e.get('new') == 'new-x12v4v' for e in E):
    E.insert(i + 1, {'new': 'new-x12v4v'})
OV.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
