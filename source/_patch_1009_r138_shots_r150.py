#!/usr/bin/env python3
"""09.10 Мирослав:
— після rest 138 («Окна Киев», Секрет 3 #27) новий екран new-x138s: колаж трьох скрінів переписки з «Конверсія Вікон»
  (Desktop vid1–3.jpg → assets/gen-rest-1009/s138/chat-N.webp), клік — скрін на весь екран (js/zoom-shots.js);
— rest 150 «AI-Оператор» (2226 #2, sv-U003b): без заголовка й підзаголовка, відео на весь слайд (CSS у кінці rest-1006.css)."""
import json, shutil, time, copy
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1009-before-r138-shots-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
D = o['__deckOrder']
NEW = 'new-x138s'
ZOOM = '<i class="zs-ic" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21M10.5 7.5v6M7.5 10.5h6"/></svg></i>'
ALT = ['Переписка с «Конверсія Вікон»: сделал бесплатный сайт, скинул ссылку',
       'Переписка с «Конверсія Вікон»: довести сайт до ума — $250',
       'Переписка с «Конверсія Вікон»: договорились за 10 000 грн']
body = '<div class="s2n s2n-shots">' + ''.join(
    '<button type="button" class="zs-c zs-c%d" data-zoom="assets/gen-rest-1009/s138/chat-%d.webp"><img src="assets/gen-rest-1009/s138/chat-%d.webp" alt="%s">%s</button>' % (k, k, k, ALT[k - 1], ZOOM)
    for k in (1, 2, 3)) + '</div>'
s = copy.deepcopy(D['slides']['new-c434'])
s.update({'t': '', 'k': '', 'b': body, 'note': '09.10 Мирослав: скріни переписки з «Конверсія Вікон» після слайда «Окна Киев»; клік — збільшити.',
          'googleNumber': 9138, 'googleNow': None})
D['slides'][NEW] = s
E = D['entries']
if not any(isinstance(e, dict) and e.get('new') == NEW for e in E):
    i = E.index('g3f9b3adf0b8_0_1943#27')
    E.insert(i + 1, {'new': NEW})
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
