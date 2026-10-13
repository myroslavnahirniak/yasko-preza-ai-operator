#!/usr/bin/env python3
"""13.10 Мирослав (номери +1): прибрати «Шестнадцать роликов», «Даже половина», «Эти деньги за месяц», «Вход можно разбить», «Что мы уже поставили»,
«Что вы умеете делать», «Первый блок в цифрах», «Помните 5 задач», «Карта», «Забрали карту»; гіфка на «херня за $70»; «Золотой дождь» у мокапі айфона."""
import json, shutil, time
from pathlib import Path
R = Path(__file__).resolve().parent.parent
OV = R / 'source/overrides.json'
o = json.load(open(OV)); do = o['__deckOrder']
shutil.copy(OV, R / f'source/_bak/overrides-1013-before-batch3-{int(time.time())}.json')
S = 'g3f9b3adf0b8_0_2226'
for n in (79, 80, 88, 89, 94, 95, 96, 97, 101, 102):
    k = f'{S}#{n}'
    if k not in do['drop']: do['drop'].append(k)
s = do['slides']['new-x12p70b']
if 's2n-gif' not in s['b']:
    s['b'] += ('<div class="s2n-gif"><video src="assets/gif/spanky-throwing-money.mp4" poster="assets/gif/spanky-throwing-money-poster.jpg" '
               'autoplay muted loop playsinline></video></div>')
g = do['slides']['new-x12gold']
if 's12-iph' not in g['b']:
    g['b'] = g['b'].replace('<div class="s12-phone"><video', '<div class="s12-phone"><div class="s12-iph"><video').replace('</video></div>', '</video></div></div>')
OV.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
