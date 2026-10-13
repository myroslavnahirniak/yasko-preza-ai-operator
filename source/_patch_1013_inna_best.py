#!/usr/bin/env python3
"""13.10 Мирослав: Влад 12.10 15:36 у Telegram — «лучше всего сработавший креатив» Інни (2 медіа + войс). Новий екран після кейсу Інни (new-x12inna)."""
import json, shutil, time, copy
from pathlib import Path
R = Path(__file__).resolve().parent.parent
OV = R / 'source/overrides.json'
o = json.load(open(OV)); do = o['__deckOrder']; E = do['entries']
shutil.copy(OV, R / f'source/_bak/overrides-1013-before-inna-best-{int(time.time())}.json')
s = copy.deepcopy(do['slides']['new-x12inna'])
A = 'assets/gen-rest-1012/s7/'
s['t'] = 'Лучше всего сработавший <em>креатив</em>'
s['b'] = (f'<div class="s2n s2n-pic s12-best"><img src="{A}inna-ads.webp" alt="Рекламный кабинет: креатив «Переїзди без героїзму»">'
          f'<video src="{A}inna-best.mp4" poster="{A}inna-best.jpg" autoplay muted loop playsinline preload="auto"></video></div>')
s['note'] = '13.10: Влад у Telegram 12.10 — креативи Інни (туризм, 56 лет), «лучше всего сработавший креатив»; файли inna1.jpg / inna2.mp4 від Мирослава.'
do['slides']['new-x12innab'] = s
i = next(k for k, e in enumerate(E) if isinstance(e, dict) and e.get('new') == 'new-x12inna')
if not any(isinstance(e, dict) and e.get('new') == 'new-x12innab' for e in E):
    E.insert(i + 1, {'new': 'new-x12innab'})
OV.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
