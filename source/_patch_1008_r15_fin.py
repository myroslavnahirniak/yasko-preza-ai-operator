#!/usr/bin/env python3
"""08.10 Мирослав: rest 15 (new-g250) — «Никому не нужен сайт — нужны клиенты с сайта.» у жовтий контейнер під заголовком,
текст чорний, «нужны клиенты с сайта.» жирним."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-r15-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
x = o['__visibleGoogleAudit']['slides']['new-g250']
old = '<p class="g2-fin">Никому не нужен сайт — нужны <em>клиенты с сайта</em>.</p>'
assert x['set']['b'].count(old) == 1
x['set']['b'] = x['set']['b'].replace(old, '<p class="g2-fin r15-box">Никому не нужен сайт — <b>нужны клиенты с сайта.</b></p>')
x['reason'] += ' · 08.10 Мирослав: фінальний рядок — жовтий контейнер під заголовком, «нужны клиенты с сайта.» жирним'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
