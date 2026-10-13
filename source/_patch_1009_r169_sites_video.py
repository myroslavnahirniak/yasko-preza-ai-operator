#!/usr/bin/env python3
"""09.10 Мирослав: rest 169 «База шаблонов сайтов» (2226 #18) — ліворуч відео-запис каталогу «Готовые сайты»
(~/Desktop/переліксайтів.mov, обрізано 1 с на початку і кінець до появи панелі скріншота → assets/video/sites-catalog-1009.mp4)
замість гортання кавʼярні; ліва колонка ширша (CSS .p7-tpl-vv у кінці rest-1006.css)."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1009-before-r169-video-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
part = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2226']['presentationParts']['slides'][17]
b = part['b']
OLD = ('<div class="p7-tpl p7-tpl-v"><div class="p7-win p7-w3"><div class="p7-bar"><i></i><i></i><i></i></div><div class="p7-shot p7-scroll">'
       '<img src="assets/vlad-1409/uslugi/sajty-coffee-full.jpg" alt="Шаблон: кофейня"></div></div>')
NEW = ('<div class="p7-tpl p7-tpl-v p7-tpl-vv"><div class="p7-win p7-w3"><div class="p7-bar"><i></i><i></i><i></i></div><div class="p7-shot p7-vshot">'
       '<video src="assets/video/sites-catalog-1009.mp4" poster="assets/video/sites-catalog-1009-poster.jpg" autoplay muted loop playsinline '
       'aria-label="Каталог «Готовые сайты»: шаблоны под разные ниши"></video></div></div>')
assert b.count(OLD) == 1
part['b'] = b.replace(OLD, NEW)
part['note'] = (part.get('note') or '') + '\n09.10 Мирослав: ліворуч відео каталогу «Готовые сайты» (перелік сайтів).'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
