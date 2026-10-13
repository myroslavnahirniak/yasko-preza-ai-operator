#!/usr/bin/env python3
"""08.10 Мирослав: rest 37 (2921 частина 27, «Умеет делать вирусные карусели и гайды») — прибрати g215-image155, лишити одне фото по центру."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-r37-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
x = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2921']['presentationParts']['slides'][26]
old = '<figure class="ag-pair ag-pair-tall ag-pair-fit r041-pair"><div><img src="assets/google-source/2026-09-16/g215-image152.png" alt=""></div><div><img src="assets/google-source/2026-09-16/g215-image155.png" alt=""></div></figure>'
assert x['b'] == old, x['b'][:120]
x['b'] = '<figure class="ag-pair ag-pair-tall ag-pair-fit r041-pair r037-one"><div><img src="assets/google-source/2026-09-16/g215-image152.png" alt="Вирусная карусель, сделанная агентом"></div></figure>'
x['reason'] = (x.get('reason') or '') + ' · 08.10 Мирослав: прибрано g215-image155, одне фото по центру'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
