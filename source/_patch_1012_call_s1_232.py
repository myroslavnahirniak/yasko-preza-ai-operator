#!/usr/bin/env python3
"""12.10 Мирослав: слайд 1 головної — оффер «$250 в день на AI-агентах» (Влад на дзвінку 47:55); rest 232 — «Между ними 25 лет» (Саша 14 / Аня 39)."""
import json, shutil, time
from pathlib import Path
R = Path(__file__).resolve().parent.parent
OV = R / 'source/overrides.json'
o = json.load(open(OV))
shutil.copy(OV, R / f'source/_bak/overrides-1012-before-s1-232-{int(time.time())}.json')
s = o['Как заработать первые $1.000 на AI в 2026']
s['opening']['lines'] = ['Как зарабатывать', '<em>$250 в день</em>', 'на AI-агентах']
old = 'И продавать услуги <strong><em>за $250–3 000,</em></strong> которые'
new = 'Продавая услуги <strong><em>за $250–3 000,</em></strong> которые'
assert old in s['opening']['body'] and old in s['b']
s['opening']['body'] = s['opening']['body'].replace(old, new)
s['b'] = s['b'].replace(old, new)
s['t'] = 'Как зарабатывать $250 в день на AI-агентах'
s['note'] = s['note'].replace('Полный текст: И продавать услуги', 'Полный текст: Продавая услуги') + '\n12.10 Влад: оффер с продуктом — «Как зарабатывать $250 в день на AI-агентах, продавая услуги, которые целиком делают AI-агенты».'
p = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2226']['presentationParts']['slides'][76]
assert p['t'].startswith('Между ними 33 года')
p['t'] = p['t'].replace('33 года', '25 лет')
OV.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
