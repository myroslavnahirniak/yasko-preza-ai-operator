#!/usr/bin/env python3
"""06.10 QA: копії copy-g249 (rest 18) і copy-g254 (rest 23) беруть джерело g3f9b3adf0b8_0_2226#15,
яке пакет 7 переробив на «ЭЛЕМЕНТ 2 ИЗ 17» (rest 149). Повертаємо копіям їхній layout/заголовок каталогу,
як було до переробки (бекап source/_bak/overrides-1006-before-rest-redo.json). Джерело #15 не чіпаємо."""
import json, shutil, time
from pathlib import Path
R = Path(__file__).resolve().parents[1]
P = R / 'source/overrides.json'
shutil.copy(P, R / f'source/_bak/overrides.json.qa1006-copies-{time.strftime("%H%M%S")}')
o = json.loads(P.read_text(encoding='utf-8'))
A = o['__visibleGoogleAudit']['slides']
for cid in ('copy-g249', 'copy-g254'):
    a = A[cid]
    a.setdefault('set', {})['t'] = '7 услуг, которые агенты <em>делают целиком</em>'
    b = a.setdefault('foundation', {}).setdefault('block129', {})
    b.update({'layout': 's16-catalog-orbit', 'focus': '.s16-step', 'eyebrow': None})
    a['reason'] = (a.get('reason') or '') + ' · 06.10 QA: layout/заголовок каталогу зафіксовано в копії (джерело #15 переробили на rest 149)'
    print(cid, json.dumps(b, ensure_ascii=False))
P.write_text(json.dumps(o, ensure_ascii=False, indent=1), encoding='utf-8')
