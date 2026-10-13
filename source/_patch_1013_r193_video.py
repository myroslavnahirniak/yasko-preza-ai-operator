#!/usr/bin/env python3
"""13.10 Мирослав: rest 193 «Ремесло делает агент» — замість рюкзака картинка Влада з Google G61 («три кнопки» + команда), оживлена Seedance 2.5 (варіант A «ланцюжок»); один прохід без петлі, текст над відео."""
import json, shutil, time
from pathlib import Path
R = Path(__file__).resolve().parent.parent
OV = R / 'source/overrides.json'
o = json.load(open(OV))
shutil.copy(OV, R / f'source/_bak/overrides-1013-before-r193-video-{int(time.time())}.json')
p = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2226']['presentationParts']['slides'][37]
V = 'assets/gen-rest-1013/r193/r193-chain'
p['b'] = ('<div class="r193"><p class="r193-t">Ремесло делает агент, <em>клиентов находит агент</em></p>'
          f'<div class="r193-vid"><video src="{V}.mp4" poster="{V}-poster.jpg" autoplay muted playsinline preload="auto"></video></div></div>')
p.setdefault('foundation', {}).setdefault('block129', {})['art'] = None
p['note'] = ((p.get('note') or '') + '\n13.10: відео «ланцюжок» (Seedance 2.5 з картинки Google G61), один прохід.').strip()
OV.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
