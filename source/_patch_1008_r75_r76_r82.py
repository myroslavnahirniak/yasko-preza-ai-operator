#!/usr/bin/env python3
"""08.10 Мирослав: Секрет 2 (1774):
rest 75 (#8) — фон a4 + надзаголовок/заголовок живим текстом («Сколько их всего» / «Это одна связка. У нас их больше двадцати»);
rest 76 (#9) — фон a5 + заголовок «Биржа против салона груминга» і низ «Услуга одна и та же. Меняется только «где находим»» (тексти зі старого постера r079);
rest 82 (#20) — розділено на 2 екрани: a6 («Алгоритм, который я ему дал») + новий екран new-x082b з a7 («Пять шагов…») одразу після."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-r75-r76-r82-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
parts = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_1774']['presentationParts']['slides']
def native(i, t, k, img, alt, body, chk):
    p = parts[i]; f = p['foundation']
    assert chk in p['t'], (i, p['t'])
    f.pop('importedHTML', None); f.pop('importedLocal', None)
    f['block129'] = {'kind': 's16', 'v2': True, 'layout': 's16-g1001', 'eyebrow': k or None, 'art': [{'src': 'assets/gen-rest-1006/' + img, 'alt': alt}]}
    p['t'], p['k'], p['b'] = t, k, body
    p['note'] = '08.10 Мирослав: картинка %s на фон, текст живим. Було: %s' % (img, p.get('note', '')[:160])
native(7, 'Это одна связка. У нас их больше <em>двадцати</em>', 'Сколько их всего', 'r075-svazki-a4.webp',
       'Стена из 21 ящика под семь услуг, открыт один — «связка» AI-сайтов. Семь услуг — и под каждую свои связки', '<i class="r07x-svazka" hidden></i>', 'двадцати')
native(8, 'Биржа против салона <em>груминга</em>', '', 'r076-birzha-a5.webp',
       'Биржа: тысячи исполнителей на один заказ, выигрывает тот, кто дешевле. Салон: конкурентов ноль, вы — единственный, кто написал',
       '<i class="r07x-svazka r076-birzha" hidden></i><p class="r076-fin">Услуга одна и та же.<br><em>Меняется только «где находим»</em></p>', 'Биржа')
p = parts[19]
assert 'Алгоритм' in p['t'], p['t']
p['foundation']['block129']['art'] = [{'src': 'assets/gen-rest-1006/r082-algoritm-a6.webp', 'alt': 'Алгоритм, который я ему дал: найди 10 салонов, напиши каждому «можно записаться?», когда ответят «хотел через сайт — не вышло», «я вам его уже сделал», сказал «да» — агент собирает сайт по шаблону'}]
p['note'] = '08.10 Мирослав: розділено на 2 екрани — тут a6 (алгоритм, 5 кроків), далі new-x082b (a7). ' + p.get('note', '')[:200]
D = o['__deckOrder']; E = D['entries']
i = E.index('g3f9b3adf0b8_0_1774#20'); assert {'new': 'new-x082b'} not in E
E.insert(i + 1, {'new': 'new-x082b'})
D['slides']['new-x082b'] = {'mvp': 1, 't': 'Пять шагов. <em>Ни одного, где надо уметь продавать</em>', 'k': '', 'b': '',
    'note': '08.10 Мирослав: друга половина слайда «Алгоритм, который я ему дал» (Секрет 2): картинка a7 — «Саше хватило первой десятки. Обычно нужно больше — посчитаем в следующем секрете. 10 салонов → 5 шагов. Пять шагов. Ни одного, где надо уметь продавать».',
    'foundation': {'local': 0, 'type': 'content', 'sourceOnly': False, 'omitMedia': True, 'media': [],
        'block129': {'kind': 's16', 'v2': True, 'layout': 's16-poster', 'art': [{'src': 'assets/gen-rest-1006/r082b-pyat-shagov-a7.webp',
            'alt': 'Саше хватило первой десятки. Обычно нужно больше — посчитаем в следующем секрете. 10 салонов → 5 шагов. Пять шагов. Ни одного, где надо уметь продавать'}]}},
    'googleNumber': 4082, 'googleNow': None, 'originalLocal': None}
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
