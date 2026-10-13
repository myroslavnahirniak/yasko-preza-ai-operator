#!/usr/bin/env python3
"""08.10 аудит Google: rest 145 (g3f9b3adf0b8_0_2226#15) = G415–G423 — каталог «7 услуг, которые агенты делают целиком»
(відео-вступ → таблиця). Переробка 06.10 (пакет 7) зробила з нього «ЭЛЕМЕНТ 2 ИЗ 17» — в Google такого нема.
Повертаємо частину з бекапу перед переробкою."""
import json, shutil, time
from pathlib import Path
SRC = Path(__file__).resolve().parent
P = SRC / 'overrides.json'
shutil.copy(P, SRC / '_bak' / ('overrides-1008-before-restore-2226-15-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
b = json.loads((SRC / '_bak/overrides-1006-before-rest-redo.json').read_text(encoding='utf-8'))
part = lambda x: x['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2226']['presentationParts']['slides']
assert 'Готовые агенты' in part(o)[14]['t'] and 'делают целиком' in part(b)[14]['t']
part(o)[14] = b['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2226']['presentationParts']['slides'][14]
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
