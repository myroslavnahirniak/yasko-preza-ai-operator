#!/usr/bin/env python3
"""08.10 Мирослав: rest 10 (copy-g245) — за його макетом: фон = 8 кольорових роботів-станцій (r010-conveyor-bg.webp),
заголовок, підзаголовок «8 задач…» і плашка «Задача словами → сайт…» живим текстом. Оригінал #66 (rest 196) не чіпаємо."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-r10-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
x = o['__visibleGoogleAudit']['slides']['copy-g245']
icon = ('<svg viewBox="0 0 48 40" aria-hidden="true"><path d="M8 4h32a5 5 0 0 1 5 5v17a5 5 0 0 1-5 5H20l-9 7v-7H8a5 5 0 0 1-5-5V9a5 5 0 0 1 5-5z" '
        'fill="none" stroke="#fdd506" stroke-width="2.6" stroke-linejoin="round"/><path d="M13 13h22M13 18.5h22M13 24h14" stroke="#fdd506" stroke-width="2.6" stroke-linecap="round"/></svg>')
x['set']['b'] = ('<div class="r10-v2"><p class="r10-sub">8 задач. Один результат — сайт, который приводит клиентов</p>'
                 '<div class="r10-out"><span class="r10-ic">%s</span><span class="r10-in">Задача словами</span><em>→</em>'
                 '<b>сайт, который приводит клиентов</b></div></div>' % icon)
x.setdefault('foundation', {})['block129'] = {'kind': 's16', 'v2': True, 'layout': 's16-g1001', 'focus': None, 'steps': None,
    'art': [{'src': 'assets/gen-rest-1006/r010-conveyor-bg.webp', 'alt': 'Восемь агентов-станций по порядку: аналитик, маркетолог, архитектор, дизайнер, иллюстратор, разработчик, конверсионщик, публикация'}]}
x['reason'] += ' · 08.10 Мирослав: макет Мирослава — фон 8 роботів-станцій, підзаголовок і плашка живим текстом'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
