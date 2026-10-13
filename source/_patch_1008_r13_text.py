#!/usr/bin/env python3
"""08.10 Мирослав: rest 13 (new-g248) — інший шрифт заголовка: на переробці 06.10 текст був намальований на постері GPT.
Постер обрізано до смуги без тексту (assets/gen-rest-1006/r013-band.webp), заголовок і підпис — живим текстом, як на сусідніх."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-r13-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
x = o['__visibleGoogleAudit']['slides']['new-g248']
x['foundation']['block129'].update(layout='s16-g1001', art=[{'src': 'assets/gen-rest-1006/r013-band.webp',
    'alt': 'Документ с печатью, дуга из иконок услуг и флакон вакцины'}])
x['set']['b'] = '<div class="r13-sub"><span>Начиная от юридического документа,</span><span>заканчивая разработкой вакцины.</span></div>'
x['reason'] += ' · 08.10 Мирослав: заголовок і підпис живим текстом (на постері був шрифт GPT), постер → смуга r013-band'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
