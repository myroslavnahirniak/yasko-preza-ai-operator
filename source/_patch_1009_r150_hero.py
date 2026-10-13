#!/usr/bin/env python3
"""09.10 Мирослав: rest 150 «AI-Оператор · ПРЕДЛОЖЕНИЕ» (2226 #1) — замість тексту й відео hero-operator-15s
scroll-scrub hero «точь-в-точь як на aimarketolog.site», але з відео ai-operator.mp4 і офером:
«$250 в день на AI-агентах. Без опыта, без аудитории и без технической работы. / Ты получаешь штат AI-агентов:
найти клиентов, оказать услугу, продать. / За 10 недель получишь навык управлять агентами и собирать своих под любую задачу.»
Сторінка: assets/sites/aiop-hero/ (порт act1 з ai-marketolog-launch-3/apps/aim3d, 786 AVIF-кадрів), на весь слайд (CSS .s2n-hero у кінці rest-1006.css)."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1009-before-r150-hero-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
part = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2226']['presentationParts']['slides'][0]
assert 'sv-desk-intro sv-U003"' in part['b'] and 'hero-operator-15s' in part['b'], 'не той екран'
part['b'] = ('<div class="s2n s2n-hero"><iframe data-src="assets/sites/aiop-hero/index.html" '
             'title="AI-Оператор: $250 в день на AI-агентах — скрол-анимация как на aimarketolog.site"></iframe></div>')
fb = part.setdefault('foundation', {})
fb['layout'] = 's16-g1001'
fb.setdefault('block129', {}).update({'kind': 's16', 'v2': True, 'layout': 's16-g1001', 'eyebrow': ''})
part['note'] = (part.get('note') or '') + '\n09.10 Мирослав: офер AI-Оператора на скрол-анимації з ai-operator.mp4 (як hero aimarketolog.site) замість тексту й відео.'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
