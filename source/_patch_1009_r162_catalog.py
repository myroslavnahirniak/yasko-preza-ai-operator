#!/usr/bin/env python3
"""09.10 Мирослав: новий екран після rest 161 (new-c435) = rest 162 — живий «пульт 7 AI-агентів + Охотник» з сайту AI-Оператора
(assets/sites/aiop-catalog, збирає source/_build_aiop_catalog.py), квадратна розкладка, перемикання кліком по пульту."""
import json, shutil, time, copy
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1009-before-r162-catalog-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
D = o['__deckOrder']; NEW = 'new-x162cat'
s = copy.deepcopy(D['slides']['new-c435'])
s.update({'t': '', 'k': '', 'googleNumber': 9162, 'googleNow': None,
          'b': '<div class="s2n s2n-block sq2"><iframe data-src="assets/sites/aiop-catalog/index.html?i=0" title="Пульт AI-агентов: 7 услуг + AI-Охотник в подарок" loading="lazy"></iframe></div>',
          'note': '09.10 Мирослав: живий блок «пульт агентів» з сайту AI-Оператора (ai-operator-agents.vercel.app), квадрат; агенти перемикаються кліком.'})
D['slides'][NEW] = s
E = D['entries']
if not any(isinstance(e, dict) and e.get('new') == NEW for e in E):
    E.insert(E.index({'new': 'new-c435'}) + 1, {'new': NEW})
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
