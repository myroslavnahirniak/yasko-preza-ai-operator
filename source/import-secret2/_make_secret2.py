#!/usr/bin/env python3
"""Окремий HTML Секрету 2 з v5-прези (preza-ai-operator-v5.vercel.app).
Бере двигун v5 (CSS+JS) як є, підміняє масив S на зріз акту «Секрет 2».
Запуск: python3 source/import-secret2/_make_secret2.py  → secret2.html
"""
import json, re, pathlib, datetime
ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC  = ROOT/'source/import-secret2/remote-index.html'
OUT  = ROOT/'secret2-source.html'
FIRST, LAST = 228, 259          # номери v5 (?s=N, 1-based): титул Секрету 2 … «Петля закрыта»

html = SRC.read_text(encoding='utf-8')
a = html.index('var S = [')
b = html.index('\n];', a) + 3
S = json.loads(html[a+len('var S = '):b].strip().rstrip(';'))
sl = S[FIRST-1:LAST]
assert sl[0]['k'].startswith('Секрет №2') and all(x['a']==4 for x in sl), 'зріз не збігається з актом Секрет 2'
for n, x in zip(range(FIRST, LAST+1), sl):
    x['v5'] = n                  # оригінальний номер у v5, показується в HUD

new_S = 'var S = ' + json.dumps(sl, ensure_ascii=False, indent=1) + ';'
out = html[:a] + new_S + html[b:]
out = out.replace('<title>AI-Оператор — преза эфира</title>',
                  f'<title>AI-Оператор · Секрет 2 (v5 {FIRST}–{LAST})</title>')
# HUD: свій номер + номер у v5
out = out.replace('hud.textContent=(i+1)+" / "+slides.length;',
                  'hud.textContent=(i+1)+" / "+slides.length+(s.v5?"  ·  v5 s="+s.v5:"");')
assert out.count('v5 s=')==1
out = out.replace('<body>', f'<body>\n<!-- Секрет 2 · зріз v5 {FIRST}–{LAST} · зібрано {datetime.date.today()} · source/import-secret2/_make_secret2.py -->', 1)
OUT.write_text(out, encoding='utf-8')
print(f'{OUT.name}: {len(sl)} слайдів, {len(out)//1024} KB')
for n,x in zip(range(FIRST,LAST+1),sl): print(f'  {n:>3}  {x.get("kind") or "-":6} {x.get("t","")[:70]}')
