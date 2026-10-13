#!/usr/bin/env python3
"""_restmap.py [N...] — поточний rest N → ключ у __deckOrder.entries (індекс, ключ/копія/new) і заголовок.
Без аргументів — повний список від REST_FROM. Перевіряє, що кількість збігається з js/slides-google180.js."""
import json, re, subprocess, sys
from pathlib import Path
R = Path(__file__).resolve().parent.parent
o = json.load(open(R / 'source/overrides.json'))
do = o['__deckOrder']; drop = set(do.get('drop', []))
eff = []
for i, e in enumerate(do['entries']):
    d = {'key': e} if isinstance(e, str) else e
    eid = d.get('key') or d.get('id') or d.get('new')
    if eid in drop: continue
    eff.append((i, eid, d))
js = subprocess.run(['node', '-e', "global.window=global;require('./js/slides-google180.js');const st=x=>(x||'').replace(/<[^>]+>/g,' ').replace(/\\s+/g,' ').trim();console.log(JSON.stringify(window.S.map(s=>[s.googleObjectId+(s.presentationPart!=null&&!String(s.googleObjectId).startsWith('copy-')&&!String(s.googleObjectId).startsWith('new-')?'#'+s.presentationPart:''),st(s.t).slice(0,60),s.copyOf||''])))"], cwd=R, capture_output=True, text=True).stdout
S = json.loads(js)
a = next(i for i, s in enumerate(S) if s[0] == 'g3f9b3adf0b8_0_2786')
if len(eff) != len(S): print(f'!! eff {len(eff)} != S {len(S)} — невказані екрани, мапа неточна', file=sys.stderr)
want = [int(x) for x in sys.argv[1:]] or range(1, len(S) - a + 1)
pos = {}
for i, eid, d in eff:
    pos.setdefault(eid if '#' in eid or not eid.startswith('g') else eid + '#0', (i, d))
for r in want:
    i = a + r - 1
    k = S[i][0] if ('#' in S[i][0] or S[i][0].startswith(('copy-', 'new-'))) else S[i][0] + '#0'
    ei, d = pos.get(k, (None, None))
    print(f"r{r:3} deck{i+1:3} e[{ei}] {k:34} | {S[i][1]}")
