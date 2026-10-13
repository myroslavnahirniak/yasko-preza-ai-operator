#!/usr/bin/env python3
"""13.10 Мирослав: rest 149 «Два пути» (Секрет 3, case 37) — три підслайди: a) тільки «САМ»; b) обидві колонки; c) усе затемнене, по центру плашка «Готов показать, как мы это делаем».
Рендерер Секрету 3 кроків не має → оригінал + 2 копії; варіант = foundation.secret3Final.variant → клас .sf-v-a/b/c (js/secret3-final.js)."""
import json, shutil, time
from pathlib import Path
R = Path(__file__).resolve().parent.parent
OV = R / 'source/overrides.json'
o = json.load(open(OV)); do = o['__deckOrder']; E = do['entries']; V = o['__visibleGoogleAudit']['slides']
shutil.copy(OV, R / f'source/_bak/overrides-1013-before-two-paths-{int(time.time())}.json')
K = 'g3f9b3adf0b8_0_1943#37'
part = V['g3f9b3adf0b8_0_1943']['presentationParts']['slides'][36]
part['foundation']['secret3Final'] = {'n': 37, 'variant': 'a'}
i = E.index(K)
for j, v in enumerate(('b', 'c'), 1):
    cid = f'copy-x13pv2{v}'
    V[cid] = {'reason': f'13.10 Мирослав: «Два пути» підслайд {v}', 'foundation': {'secret3Final': {'n': 37, 'variant': v}}}
    if not any(isinstance(e, dict) and e.get('id') == cid for e in E):
        E.insert(i + j, {'copy': K, 'id': cid})
OV.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
