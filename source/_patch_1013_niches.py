#!/usr/bin/env python3
"""13.10 · «Разные ниши и разные страны» (2226#98): Влад 12.10 — «на них какие-то картинки… визуализация ниши» (Google G163 «картинки наши визуал»).
Мирослав: скріни наших сайтів + назва бренду. Скріни — assets/vlad-1409/brands/*.webp."""
import json, shutil, time
from pathlib import Path
R = Path(__file__).resolve().parent.parent
OV = R / 'source/overrides.json'
o = json.load(open(OV))
shutil.copy(OV, R / f'source/_bak/overrides-1013-before-niches-{int(time.time())}.json')
p = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2226']['presentationParts']['slides'][97]
B = 'assets/vlad-1409/brands/'
shots = {'ТІС': 'tis', 'Zarmilkas': 'zarmilkas', 'MAESTA': 'maesta', 'Діамант-М': 'diamant', 'L.K. Bauservice': 'lk-bauservice',
         'MALACLEAR': 'malaclear', 'BioSwiss': 'bioswiss', 'BATUMI BOX': 'batumibox', 'Свої цифри': 'svoi-cifry'}
b = p['b']
if 'nb-img' not in b:
    b = b.replace('<div class="nb">', '<div class="nb nb-img">')
    for name, f in shots.items():
        tag = f'<b>{name}</b>'
        assert tag in b, name
        # картинка перед підписом картки
        i = b.index(tag); j = b.rindex('<span>', 0, i)
        b = b[:j] + f'<i class="nb-shot" style="background-image:url({B}{f}.webp)"></i>' + b[j:]
    p['b'] = b
    p['note'] = ((p.get('note') or '') + '\n13.10: картки ніш зі скрінами наших сайтів (Влад 12.10, Google G163).').strip()
OV.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
