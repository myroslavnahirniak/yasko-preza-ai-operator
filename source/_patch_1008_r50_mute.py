#!/usr/bin/env python3
"""08.10 Мирослав: rest 50 (2921 частина 41, «AI-SEO · Клиенты») — прибрати звук ролика (block129.sound → false)."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-r50-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
x = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2921']['presentationParts']['slides'][40]
assert 'ai-seo-reel' in x['b'] and x['foundation']['block129'].get('sound') is True
x['foundation']['block129']['sound'] = False
x['b'] = x['b'].replace('playsinline preload="metadata"', 'muted playsinline preload="metadata"')
x['reason'] = (x.get('reason') or '') + ' · 08.10 Мирослав: без звуку'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
