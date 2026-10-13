#!/usr/bin/env python3
"""09.10 Мирослав: rest 80 (new-c348) — картки «Одна ниша» / «Топ-локации» живим HTML замість скрінів (без чорного фону скрінів)."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1009-before-r80-cards-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
s = o['__deckOrder']['slides']['new-c348']
OLD = ('<div class="cards"><img src="assets/google-1008call/card-nisha.webp" alt="Одна ниша — не распыляемся, берём одну и знаем её">'
       '<img src="assets/google-1008call/card-lokacii.webp" alt="Топ-локации — города, где покупают чаще"></div>')
TARGET = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.4"/></svg>'
PIN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.4"/></svg>'
NEW = ('<div class="cards"><div class="aim-c">%s<b>Одна ниша</b><span>не распыляемся —<br>берём одну и знаем её</span></div>'
       '<div class="aim-c">%s<b>Топ-локации</b><span>города, где покупают чаще</span></div></div>') % (TARGET, PIN)
assert s['b'].count(OLD) == 1
s['b'] = s['b'].replace(OLD, NEW)
s['note'] = s.get('note', '') + '\n09.10 Мирослав: картки «Одна ниша» / «Топ-локации» — HTML, не скріни.'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
