#!/usr/bin/env python3
"""08.10 Мирослав: rest 71–73 live (72–74 локально) — Секрет 2, частини 1774 #5/#6/#7: картинки Мирослава a1/a2/a3 на весь кадр
замість iframe secret2 (n=232/233) і постера GPT r077; надзаголовок + заголовок живим текстом угорі ліворуч, як у його макетах s1/s2."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-r71-73-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
parts = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_1774']['presentationParts']['slides']
SPEC = {4: ('Продавать не нужно. Нужна <em>связка</em>', 'Как это устроено', 'r071-svazka-a1.webp', 'Что продаём, кому продаём, как подходим — спрос есть, конкуренции нет: это и есть связка'),
        5: ('Связка, которую <em>я собрал</em>', 'Вот моя первая', 'r072-svazka-a2.webp', 'Что: AI-сайты от $250. Кому: локальному бизнесу. Как: показываем готовое — одна услуга, один тип клиента, один способ подойти'),
        6: ('Как — это четыре <em>решения</em>', 'Как именно', 'r073-svazka-a3.webp', 'Одна ниша, один шаблон, топ-локации, бесплатный сайт — четыре решения принимаются один раз, дальше повторяется')}
for i, (t, k, img, alt) in SPEC.items():
    p = parts[i]; f = p['foundation']
    assert p['t'].replace('<em>', '').replace('</em>', '').startswith(t.replace('<em>', '').replace('</em>', '')[:12]), p['t']
    f.pop('importedHTML', None); f.pop('importedLocal', None)
    f['block129'] = {'kind': 's16', 'v2': True, 'layout': 's16-g1001', 'eyebrow': k,
                     'art': [{'src': 'assets/gen-rest-1006/' + img, 'alt': alt}]}
    p['t'], p['k'] = t, k
    p['b'] = '<i class="r07x-svazka" hidden></i>'
    p['note'] = '08.10 Мирослав: картинка %s на весь кадр, заголовок живим текстом (макет s1/s2). Було: %s' % (img, p.get('note', '')[:160])
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
