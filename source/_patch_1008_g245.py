#!/usr/bin/env python3
"""08.10 Мирослав: rest 10 (copy-g245, «Агент AI-Сайты… конвейер») — у Google G245 Влад закрив латками
рядок «Первый готовый агент — ваш после блока 2» і «Вы ставите задачу словами…». Прибираємо обидва лише в копії
(оригінал #66 = G482 лишається з ними)."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-g245-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
x = o['__visibleGoogleAudit']['slides']['copy-g245']
b = x['set']['b']
for frag in ('<div class="eyebrow">Первый готовый агент — ваш после блока 2</div>',
             '<p class="note center">Вы ставите задачу словами. Кто за кем работает — решает агент</p>'):
    assert b.count(frag) == 1, frag
    b = b.replace(frag, '')
x['set']['b'] = b
x['reason'] += ' · 08.10 Мирослав: прибрано eyebrow і нижній рядок — у Google G245 Влад їх закрив'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
