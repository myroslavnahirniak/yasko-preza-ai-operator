#!/usr/bin/env python3
"""10.10 Мирослав: модуль M10 «Агент-охотник» прибрано → у програмі 11 модулів (M0 + M1…M11 → M11 AI-продавец став M10, M12 «Поиск клиентов и связки» → M11);
«12/13 модулей» скрізь → 11 (Элемент 1, Gold: ledger, eyebrow, «Три набора», «Что входит целиком», «Реальная цена», «Цена для эфира», порівняння);
Элемент 16 — опис словами Мирослава; дубль блоку «На выходе пакета 01» (new-c434, вкладка AI-маркетинг) прибрано."""
import json, re, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1010-before-modules11-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
D = o['__deckOrder']
p = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2226']['presentationParts']['slides']
def note(x, s): x['note'] = (x.get('note') or '') + '\n10.10 Мирослав: ' + s

# 1) прибрати M10 «Агент-охотник» (рядок mb-r + розкриття mb-x)
x = p[11]; b = x['b']
m = re.search(r'<div class="mb-r"[^>]*><span class="mb-c">M10</span>.*?</div><div class="mb-x">.*?</div></div>(?=<div class="mb-r"|</div><div class="outcome"|</div><div class="mb-pack")', b, re.S)
if not m:  # без розкриття
    m = re.search(r'<div class="mb-r"[^>]*><span class="mb-c">M10</span>.*?</div>(?=<div class="mb-r"|</div><div class="outcome")', b, re.S)
assert m and 'Агент-охотник' in m.group(0), 'M10 не знайдено'
x['b'] = b.replace(m.group(0), '', 1)
assert 'Агент-охотник' not in x['b']
note(x, 'модуль M10 «Агент-охотник» прибрано.')
# 2) перенумерація M11→M10, M12→M11
x = p[12]; b = x['b']
assert '<span class="mb-c">M11</span>' in b and '<span class="mb-c">M12</span>' in b
x['b'] = b.replace('<span class="mb-c">M11</span>', '<span class="mb-c">M10</span>').replace('<span class="mb-c">M12</span>', '<span class="mb-c">M11</span>')
note(x, 'перенумерація: AI-продавец M10, «Поиск клиентов и связки» M11 (усього 11 модулів).')

# 3) кількість модулів = 11 скрізь
n = 0
for i, y in enumerate(p):
    for key in ('t', 'b', 'k'):
        v = y.get(key)
        if not isinstance(v, str): continue
        w = re.sub(r'\b1[23](\s*модул)', r'11\1', v)
        w = re.sub(r'(1[23])( МОДУЛЕЙ)', r'11\2', w)
        w = re.sub(r'(<span>модулей</span><b>)13(</b>)', r'\g<1>11\2', w)
        if w != v: y[key] = w; n += 1; print('upd', i, key)
    eb = (y.get('foundation') or {}).get('block129', {}).get('eyebrow')
    if isinstance(eb, str) and re.search(r'1[23] МОДУЛЕЙ', eb):
        y['foundation']['block129']['eyebrow'] = re.sub(r'1[23] МОДУЛЕЙ', '11 МОДУЛЕЙ', eb); n += 1; print('upd eyebrow', i)
print('module-count fields changed:', n)

# 4) Элемент 16 — опис словами Мирослава
for y in p:
    if 'день в день связкам' in y.get('b', ''):
        y['b'] = re.sub(r'<p class="sv-description">.*?</p>', '<p class="sv-description">Доступ к актуальным день в день связкам и способам заработка в виде: услуга, что продавать, плюс ниша, плюс локация, плюс способ</p>', y['b'], count=1)
        note(y, 'опис дослівно за Мирославом («…плюс ниша, плюс локация, плюс способ»).')

# 5) дубль пакета 01
if 'new-c434' not in D['drop']: D['drop'].append('new-c434')
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
