#!/usr/bin/env python3
"""08.10 Мирослав: rest 23 (g3f9b3adf0b8_0_1528, «АГЕНТ») — прибрати знизу поле вводу (s16-chat/s16-input), обкладинку вирівняти (CSS)."""
import json, re, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-r23-noinput-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
x = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_1528']
b, n = re.subn(r'<div class="s16-chat" aria-hidden="true"><div class="s16-input">.*?</svg></div></div></div>', '', x['set']['b'])
assert n == 1 and 's16-input' not in b, n
x['set']['b'] = b
x['reason'] += ' · 08.10 Мирослав: прибрано поле вводу знизу, обкладинка по центру'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
