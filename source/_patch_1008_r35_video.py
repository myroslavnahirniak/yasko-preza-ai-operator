#!/usr/bin/env python3
"""08.10 Мирослав: rest 35 (copy-g287, «Контент-завод с AI-аватаром») — замість постерів два ролики з автозапуском."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-r35-video-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
x = o['__visibleGoogleAudit']['slides']['copy-g287']
old = '<img class="v" src="assets/s202-avatar/poster-1.jpg" alt="Ролик с AI-аватаром"><img class="v" src="assets/s202-avatar/poster-2.jpg" alt="Ролик с AI-аватаром">'
assert x['set']['b'].count(old) == 1
x['set']['b'] = x['set']['b'].replace(old,
    '<video class="v" src="assets/s202-avatar/clip-1.mp4" poster="assets/s202-avatar/poster-1.jpg" autoplay muted loop playsinline aria-label="Ролик с AI-аватаром"></video>'
    '<video class="v" src="assets/s202-avatar/clip-2.mp4" poster="assets/s202-avatar/poster-2.jpg" autoplay muted loop playsinline aria-label="Ролик с AI-аватаром"></video>')
x['reason'] += ' · 08.10 Мирослав: ролики з автозапуском замість постерів'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
