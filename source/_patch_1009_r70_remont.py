#!/usr/bin/env python3
"""09.10 Мирослав: rest 70/71 (new-g335 / new-g336) — відео remont-A-seedance-mini (Влад робить ремонт).
70 — перший кадр як фото, 71 — те саме відео програється (один раз, тримає останній кадр).
Текст — живий заголовок угорі на темному полі, відео окремою карткою нижче: читається і не закриває Влада."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1009-before-r70-remont-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
A = o['__visibleGoogleAudit']['slides']
POSTER = 'assets/video/remont/remont-a-poster.webp'
A['new-g335']['set']['b'] = ('<div class="s2n s2n-vcard"><img src="%s" alt="Влад в рабочем комбинезоне в квартире во время ремонта"></div>' % POSTER)
A['new-g336']['set']['b'] = ('<div class="s2n s2n-vcard s2n-vcont"><video src="assets/video/remont/remont-a.mp4" poster="%s" muted playsinline preload="auto" '
                             'aria-label="Влад делает ремонт и улыбается"></video></div>' % POSTER)
for k in ('new-g335', 'new-g336'):
    A[k]['foundation']['block129']['art'] = None
    A[k]['reason'] = '09.10 Мирослав: відео ремонту — 70 фото (перший кадр), 71 програється; текст угорі, Влад не закритий | ' + A[k].get('reason', '')
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
