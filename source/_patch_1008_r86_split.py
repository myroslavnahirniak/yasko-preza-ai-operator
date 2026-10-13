#!/usr/bin/env python3
"""08.10 Мирослав: Секрет 2, «Саша» (1774 #23, постер s250) — розділено на 2 екрани: a8 («Саша · Первая продажа — меньше чем через сутки»)
+ новий екран new-x086b з a9 («Мой сын заработал свои первые деньги раньше, чем я в его возрасте узнал, что так вообще можно»)."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-r86-split-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
parts = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_1774']['presentationParts']['slides']
p = parts[22]; assert p['t'].startswith('Саша'), p['t']
p['foundation']['block129']['art'] = [{'src': 'assets/gen-rest-1006/r086-sasha-a8.webp', 'alt': 'Кто это сделал — Саша. Первая продажа — меньше чем через сутки. Сколько заняло: меньше 24 часов. Сколько принесло: $250'}]
p['note'] = '08.10 Мирослав: розділено на 2 екрани — тут a8 (Саша, цифри), далі new-x086b (a9, «Мой сын…»). ' + p.get('note', '')[:200]
D = o['__deckOrder']; E = D['entries']
i = E.index('g3f9b3adf0b8_0_1774#23'); assert {'new': 'new-x086b'} not in E
E.insert(i + 1, {'new': 'new-x086b'})
D['slides']['new-x086b'] = {'mvp': 1, 't': 'Мой сын заработал <em>свои первые деньги</em> раньше, чем я в его возрасте узнал, <em>что так вообще можно</em>', 'k': '', 'b': '',
    'note': '08.10 Мирослав: друга половина слайда «Саша» (Секрет 2): картинка a9.',
    'foundation': {'local': 0, 'type': 'content', 'sourceOnly': False, 'omitMedia': True, 'media': [],
        'block129': {'kind': 's16', 'v2': True, 'layout': 's16-poster', 'art': [{'src': 'assets/gen-rest-1006/r086b-syn-a9.webp',
            'alt': 'Мой сын заработал свои первые деньги раньше, чем я в его возрасте узнал, что так вообще можно'}]}},
    'googleNumber': 4086, 'googleNow': None, 'originalLocal': None}
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
