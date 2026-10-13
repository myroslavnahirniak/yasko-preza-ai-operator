#!/usr/bin/env python3
"""09.10 Мирослав: rest 16 (new-g251) — «поміняй на цю»: таблиця як на rest 168 (останній крок каталогу 2226 #15):
«Каталог · 7 услуг, которые агенты делают целиком», рядки зверху вниз (чек, складність, попит, конкуренція).
Підказку «Нажмите на услугу…» прибрано — тут нема кроків, до яких повертатись; рядки не кнопки."""
import json, re, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1009-before-r16-cotable-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
src = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2226']['presentationParts']['slides'][14]['b']
a = src.rfind('<section class="s16-step catalog-orbit-stage"><div class="co-slidehead"><span class="co-small">Каталог</span>')
sec = src[a:src.index('</section>', a) + len('</section>')]
assert '<div class="co-table">' in sec
sec = re.sub(r'<div class="co-tablehint">.*?</div>', '', sec)
sec = re.sub(r'<button class="co-tr co-tablebutton" data-catalog-go="\d+">(.*?)</button>', r'<div class="co-tr">\1</div>', sec)
assert 'data-catalog-go' not in sec
x = o['__visibleGoogleAudit']['slides']['new-g251']
x['set']['b'] = sec
x.setdefault('foundation', {})['block129'] = {'kind': 's16', 'v2': True, 'layout': 's16-catalog-orbit', 'steps': ['Вся таблица'], 'focus': '.s16-step'}
x['reason'] = '09.10 Мирослав: таблиця як на rest 168 (Каталог · 7 услуг…), замість g2-tbl | ' + x.get('reason', '')
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok', len(sec))
