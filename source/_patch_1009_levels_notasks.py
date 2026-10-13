#!/usr/bin/env python3
"""09.10 Мирослав: програмні слайди rest 157/158/162/163/164 (2226 #7/#8/#11/#12/#13):
— у підписі лишити тільки «Уровень N» (без «Блок N · недели …»); рівні 162–164 за нотатками Влада:
  блок 3 = Silver = Уровень 2, блоки 4–5 = Gold = «третий уровень» → Уровень 3;
— прибрати кількість задач: «7/9 задач» біля модулів, цифри на іконках (pj-count), рядок «Выдаём в этом блоке N задач»."""
import json, re, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1009-before-levels-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
parts = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2226']['presentationParts']['slides']
LVL = {6: 1, 7: 1, 10: 2, 11: 3, 12: 3}
for i, lv in LVL.items():
    b = parts[i]['b']
    eb = re.findall(r'<div class="eyebrow">.*?</div>', b)
    assert len(eb) == 1 and 'недели' in eb[0], (i, eb)
    b = b.replace(eb[0], '<div class="eyebrow"><b class="lvl">Уровень %d</b></div>' % lv)
    b = re.sub(r'<span class="pj-task-count"><b>\d+</b><small>задач[аи]?</small></span>', '', b)
    b = re.sub(r'<span class="pj-count">\d+</span>', '', b)
    b = re.sub(r'<div class="mb-pack"><span class="mb-pack-l">[^<]*</span><b>\d+ задач[аи]?</b></div>', '', b)
    assert 'pj-task-count' not in b and 'pj-count' not in b and 'mb-pack' not in b, i
    parts[i]['b'] = b
    parts[i]['note'] = (parts[i].get('note') or '') + '\n09.10 Мирослав: підпис лише «Уровень %d», кількість задач прибрано.' % lv
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
