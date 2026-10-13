#!/usr/bin/env python3
"""09.10 Мирослав: rest 109 «И под каждую — своя модель поиска» — фон = чиста картинка b2 (ключ і машина, Desktop/b2.png),
заголовок, чіпи ніш і висновок — живим текстом шрифтами деки (раніше все було вшито в постер)."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1009-before-r109-live-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
p = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_1774']['presentationParts']['slides'][27]
assert 'модель' in p['t'], p['t']
NICHES = ['окна и двери', 'барбершоп', 'прокат авто', 'оптика', 'кондитерская', 'автомойка', 'студия маникюра', 'кофейня']
chips = ''.join('<span class="ch%s" style="--i:%d">%s</span>' % (' on' if n == 'прокат авто' else '', i, n) for i, n in enumerate(NICHES))
p['t'] = 'И под каждую — своя <em>модель поиска</em>'
p['b'] = ('<div class="s2n-model"><div class="chips">%s</div>'
          '<p class="fin">Не «попробуйте разное», а <em>последовательность</em>, которую уже прогнали и знают, чего от неё ждать</p></div>' % chips)
p['foundation']['block129'] = {'kind': 's16', 'v2': True, 'layout': 's16-g1001',
                               'art': [{'src': 'assets/gen-1009/r109-bg-keys-car.webp', 'alt': 'Ключ от авто и машина в золотом свете'}]}
p['reason'] = (p.get('reason') or '') + ' · 09.10 Мирослав: фон b2 + живий текст і чіпи (замість постера з вшитим текстом)'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
