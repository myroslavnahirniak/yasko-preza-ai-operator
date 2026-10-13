#!/usr/bin/env python3
"""09.10 Мирослав, правки /rest 162–179 (oid g3f9b3adf0b8_0_2226):
— 162/163/164 (#11/#12/#13): друга частина заголовка з нового рядка;
— 166 (#15) AI-таргет: таргет-креативи в мокапах телефонів (Холст gen/ads-phones-s16.png);
— 166 (#15) останній крок: замість карток Холсту у 2 колонки — початкова таблиця зверху вниз (з бекапу до 08.10, AI-продавец конкуренція 3);
— 167 (#16) прибрати з порядку (лишається джерелом для копій);
— 173 (#22) і 179 (#28): рендер на всю зону з м'якими краями, як 174/175 (маркери r8-m173 / r8-m179, CSS у кінці rest-1006.css)."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1009-before-rest162-179-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
parts = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2226']['presentationParts']['slides']

def note(i, s):
    parts[i]['note'] = (parts[i].get('note') or '') + '\n09.10 Мирослав: ' + s

# 162–164: перенос
T = {10: ('Контент-завод: <em>месяц контента за день</em>', 'Контент-завод:<br><em>месяц контента за день</em>'),
     11: ('Привлечение: клиентов <em>находит агент</em>', 'Привлечение:<br>клиентов <em>находит агент</em>'),
     12: ('Продажи и масштаб: сделка закрывается <em>без вас</em>', 'Продажи и масштаб:<br>сделка закрывается <em>без вас</em>')}
for i, (old, new) in T.items():
    assert parts[i]['t'] == old, (i, parts[i]['t'])
    parts[i]['t'] = new

# 166: AI-таргет → телефони
b = parts[14]['b']
OLD_ADS = ('<div class="co-product-scene co-media co-m05"><img class="v" src="assets/vlad-1409/dizayn/reels-1.webp" alt="Рекламный креатив «Тебе не нужен дизайнер»">'
           '<img class="v" src="assets/vlad-1409/dizayn/reels-2.webp" alt="Рекламный креатив «Смотри, что сделал AI»"></div>')
NEW_ADS = ('<div class="co-product-scene co-media co-m05 co-m05p"><img class="phones" src="assets/gen-rest-1009/ads-phones.webp" '
           'alt="Таргет-креативы в ленте Instagram на трёх телефонах"></div>')
assert b.count(OLD_ADS) == 1
b = b.replace(OLD_ADS, NEW_ADS)

# 166: останній крок → початкова таблиця
bak = json.loads((P.parent / '_bak' / 'overrides-1008-before-catalog-holst-1791443173.json').read_text(encoding='utf-8'))
ob = bak['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2226']['presentationParts']['slides'][14]['b']
TABLE = ob[ob.index('<div class="co-table">'):ob.index('<div class="co-tablehint">')]
K6 = '<span class="co-name">AI-продавец</span><span class="co-fee"><b>$500–$2.000</b><small>за сборку и ведение</small></span><span>средняя</span><span class="co-score">7</span><span class="co-score co-gray">6</span>'
assert TABLE.count(K6) == 1
TABLE = TABLE.replace(K6, K6[:-len('6</span>')] + '3</span>')
h0 = b.index('<div class="co-holst r20-cat">'); h1 = b.index('<div class="co-tablehint">')
b = b[:h0] + TABLE + b[h1:]
parts[14]['b'] = b
note(14, 'AI-таргет — телефони з креативами; останній крок — таблиця зверху вниз замість карток у 2 колонки.')

# 167: прибрати
drop = o['__deckOrder']['drop']
if 'g3f9b3adf0b8_0_2226#16' not in drop:
    drop.append('g3f9b3adf0b8_0_2226#16')

# 173: договір — м'які краї як 174/175
b = parts[21]['b']
M0 = '<i class="sv-marker sv-polished sv-element sv-U038 p7-dark p7-el r8-dk" hidden></i>'
A0 = '<div class="sv-object sv-doc"><img src="assets/photo/replace/blurcontract.webp" alt="Пример договора на оказание услуг"></div>'
assert b.count(M0) == 1 and b.count(A0) == 1
b = b.replace(M0, '<i class="sv-marker sv-element sv-U038 p9-dark r8-m173" hidden></i>')
b = b.replace(A0, '<div class="r8-art"><img src="assets/gen-rest-1009/contract-dark.webp" alt="Пример договора на оказание услуг"></div>')
parts[21]['b'] = b
note(21, 'градієнт як на 174/175 — кадр на всю зону, краї розчиняються (без овальної віньєтки).')

# 179: скрипти — додати градієнт по краях
b = parts[27]['b']
M1 = '<i class="sv-marker sv-polished sv-element sv-U044 p7-dark p7-el r8-dk" hidden></i>'
A1 = '<div class="sv-object sv-render"><img src="assets/gen-2209/scripts-ui.jpg" alt="Чат с клиентом: ответы на «Дорого», «Я подумаю» и шаблон КП"></div>'
assert b.count(M1) == 1 and b.count(A1) == 1
b = b.replace(M1, '<i class="sv-marker sv-element sv-U044 p9-dark r8-m179" hidden></i>')
b = b.replace(A1, '<div class="r8-art r8-sq"><img src="assets/gen-2209/scripts-ui.jpg" alt="Чат с клиентом: ответы на «Дорого», «Я подумаю» и шаблон КП"></div>')
parts[27]['b'] = b
note(27, 'краї рендера розчиняються у фон, як 174/175.')

P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
