#!/usr/bin/env python3
"""08.10 Мирослав:
rest 55 (g3f9b3adf0b8_0_1679, «Вот что собралось…») — без фото Влада; фон — ледь видний знак питання (r055-question-bg.webp), заголовок по центру;
rest 63 live / 64 локально (new-g332, «А потом я осознал…») — замість постера GPT: заголовок по центру, під ним gif Confused Travolta (assets/gif/travolta-confused.mp4)."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-r55-r63-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8')); V = o['__visibleGoogleAudit']['slides']
x = V['g3f9b3adf0b8_0_1679']
x['foundation']['block129']['art'] = [{'src': 'assets/gen-rest-1006/r055-question-bg.webp', 'alt': 'Ледь видний золотий знак питання на темному тлі'}]
x['reason'] += ' · 08.10 Мирослав: без фото, фон — ледь видний знак питання, заголовок по центру'
y = V['new-g332']
y['foundation']['block129'].update(layout='s16-g1001', art=None)
y['set']['b'] = ('<div class="r63-gif"><video src="assets/gif/travolta-confused.mp4" poster="assets/gif/travolta-confused-poster.jpg" '
                 'autoplay muted loop playsinline aria-label="Растерянный Траволта оглядывается"></video></div>')
y['set']['note'] = '08.10 Мирослав: заголовок по центру, під ним gif Confused Travolta (Tenor, «What? Huh?»), замість постера GPT.'
y['reason'] += ' · 08.10 Мирослав: gif Траволти замість постера'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
