#!/usr/bin/env python3
"""06.10 QA: copy-g016 (екран 12 частини 1, затверджена) — копія g3f9b3adf0b8_0_2921#29, яку rest-redo пакет 2
переробив для rest 43 (r043-pair зі стрілкою). Частину 1 не чіпаємо: копії — власне set.b з тілом до переробки
(бекап source/_bak/overrides-1006-before-rest-redo.json). rest 43 лишається новим."""
import json, shutil, time
from pathlib import Path
R = Path(__file__).resolve().parents[1]
P = R / 'source/overrides.json'
shutil.copy(P, R / f'source/_bak/overrides.json.qa1006-copy016-{time.strftime("%H%M%S")}')
o = json.loads(P.read_text(encoding='utf-8'))
bak = json.loads((R / 'source/_bak/overrides-1006-before-rest-redo.json').read_text(encoding='utf-8'))
old = bak['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2921']['presentationParts']['slides'][28]['b']
assert 'Автомонтаж' in bak['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2921']['presentationParts']['slides'][28]['t']
A = o['__visibleGoogleAudit']['slides']
A.setdefault('copy-g016', {})
A['copy-g016'].setdefault('set', {})['b'] = old
A['copy-g016']['reason'] = '06.10 QA: тіло екрана частини 1 зафіксовано як до rest-redo (джерело #29 переробили на rest 43)'
P.write_text(json.dumps(o, ensure_ascii=False, indent=1), encoding='utf-8')
print('copy-g016 set.b =', old[:80])
