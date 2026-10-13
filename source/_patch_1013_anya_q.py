#!/usr/bin/env python3
"""13.10 Мирослав: rest 263 (Аня, сайт) — кнопка на geo.annakotsur.com; новий підслайд після «Потом она взяла клиента — и повторила» (2921#48):
цитата клієнта It's Beauty по словах + висновок «Он сам увидел заказы — и продлил работу» (текст як у Google G139 / 2921#50)."""
import json, shutil, time, copy
from pathlib import Path
R = Path(__file__).resolve().parent.parent
OV = R / 'source/overrides.json'
o = json.load(open(OV)); do = o['__deckOrder']; E = do['entries']; V = o['__visibleGoogleAudit']['slides']
shutil.copy(OV, R / f'source/_bak/overrides-1013-before-anya-q-{int(time.time())}.json')
A = 'g3f9b3adf0b8_0_2921'
p45 = V[A]['presentationParts']['slides'][44]
if 'annakotsur.com/"' not in p45['b']:
    p45['b'] += '<a class="s12-site s13-site" href="https://geo.annakotsur.com/" target="_blank" rel="noopener">Открыть сайт ↗</a>'
q = '«Я стал реально чаще видеть органические заказы — и конкретно по той категории, которую ты сейчас качаешь»'
words = q.split(' ')
spans = ' '.join(f'<span style="--i:{i}">{w}</span>' for i, w in enumerate(words))
do['slides']['new-x13itsq'] = {
    'mvp': 1, 't': '', 'k': '',
    'b': ('<div class="s13q"><p class="s13q-k">слова самого клиента · интернет-магазин It’s Beauty</p>'
          f'<blockquote class="s13q-t" style="--n:{len(words)}">{spans}</blockquote>'
          '<p class="s13q-fin">Он сам увидел заказы — <em>и продлил работу</em></p></div>'),
    'note': '13.10 Мирослав: підслайд після «Потом она взяла клиента» — цитата клієнта It’s Beauty з анімацією (Google G139).',
    'foundation': {'local': 0, 'type': 'content', 'sourceOnly': False, 'omitMedia': True, 'media': [],
                   'block129': {'kind': 's16', 'v2': True, 'layout': 's16-g1001'}},
    'googleNumber': 7139, 'googleNow': 139, 'originalLocal': None}
i = E.index(f'{A}#48')
if not any(isinstance(e, dict) and e.get('new') == 'new-x13itsq' for e in E):
    E.insert(i + 1, {'new': 'new-x13itsq'})
OV.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok', len(words), 'слів')
