#!/usr/bin/env python3
"""08.10 Мирослав: rest 19 (copy-g254, «AI-сайты») — замість фото телефона живий сайт ZARMILKAS в iframe, який можна гортати
(рамка .s16-phone як на rest 197; fitPhone + автопрокрутка з js/block-154-163.js, ручний скрол перехоплює)."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-r19-iframe-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
x = o['__visibleGoogleAudit']['slides']['copy-g254']
old = '<img class="phone" src="assets/google-1008/g254-zarmilkas-phone.webp" alt="Сайт ZARMILKAS на телефоне">'
assert x['set']['b'].count(old) == 1
x['set']['b'] = x['set']['b'].replace(old, '<div class="s16-phone" aria-label="zarmilkas-troyanda-video.vercel.app">'
    '<iframe src="assets/sites/zarmilkas/index.html" title="Сайт Zarmilkas — собран агентом" loading="lazy"></iframe></div>')
x['reason'] += ' · 08.10 Мирослав: живий сайт ZARMILKAS в iframe замість фото'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
