#!/usr/bin/env python3
"""12.10 дзвінок з Владом — швидкий блок (transcripts/2026-10-12-preza-vlad/ROZBIR.md, A–D).
Порядок цін/оплати, прибрати 204, тексти й фото на існуючих екранах продаючої частини (oid 2226, частини #N = --part).
Після: FOUNDATION_SOURCE=google-2026-09-16/foundation-source-v2.json python3 source/_foundation_prepare.py && python3 source/_build_slides.py
"""
import json, shutil, time, re
from pathlib import Path

R = Path(__file__).resolve().parent.parent
OV = R / 'source/overrides.json'
P = 'g3f9b3adf0b8_0_2226'
o = json.load(open(OV))
shutil.copy(OV, R / f'source/_bak/overrides-1012-before-call-quick-{int(time.time())}.json')

do = o['__deckOrder']
E = do['entries']
k = lambda n: f'{P}#{n}'


def move(keys, before=None, after=None):
    for x in keys:
        E.remove(x)
    i = E.index(before) if before else E.index(after) + 1
    E[i:i] = keys


# B1 · спершу стек цінності, реальна ціна, ціна для ефіру — потім Bronze/Silver/Gold
move([k(45), k(46), k(47)], before=k(42))
# B2 · «Забирайте подарки» одразу після «Что фиксирует ваша десятка»
move([k(100)], after=k(50))
# B3 · «Сегодня вы выбираете не набор» — Влад: «не потрібен, видалити»
if k(52) not in do['drop']:
    do['drop'].append(k(52))
# B4 · «+30 минут» одразу після «Если эти два часа… нажмите сейчас»
move([k(56)], after=k(53))

parts = o['__visibleGoogleAudit']['slides'][P]['presentationParts']['slides']
part = lambda n: parts[n - 1]
REASON = '12.10 дзвінок з Владом (ROZBIR 2026-10-12)'


def note(s, why):
    s['note'] = ((s.get('note') or '') + f'\n{REASON}: {why}').strip()


def sub(n, old, new, why):
    s = part(n)
    assert old in s['b'], (n, old)
    s['b'] = s['b'].replace(old, new)
    note(s, why)


# A5 · rest 191: Мирослав — лишити один рядок, «клиентов находит агент» жовтим
sub(38, 'Ремесло делает агент, клиентов находит агент</p>', 'Ремесло делает агент, <em>клиентов находит агент</em></p>',
    '«клиентов находит агент» жовтим')

# B5 · rest 207: латка Влада в Google G79 — дрібний текст під гарантією прибрати
s = part(55)
s['b'] = re.sub(r'<div class="r189-tcq">.*?</div><div class="r189-disc">.*?</div>', '', s['b'])
note(s, 'без «Справедливо?» і дрібного рядка про бронь (латка G79)')

# B4 · rest 208: «+30 минут» — акцент, великим
sub(56, '<p class="sl2-a r210-h" style="--d:0.15s">Условия действуют до конца эфира <em>+&nbsp;30&nbsp;минут</em></p>',
    '<p class="sl2-a r210-h" style="--d:0.15s">Условия действуют до конца эфира</p>'
    '<div class="sl2-a r208-30" style="--d:0.3s"><b>+30</b><span>минут</span></div>',
    '«+30 минут» великим — акцент')

# D1 · rest 217 (G85)
sub(62, 'У вас уже полсотни сохранённых роликов про нейронки. Пятьдесят первый ничего не изменит',
    'У вас уже полсотни сохранённых роликов про нейронки.', 'без «Пятьдесят первый…»')
sub(62, 'Нужны агенты в руках и человек, который проверит ваш первый заказ',
    'Нужны агенты в руках, и вы умеете направлять их на свои задачи', 'текст з Google G85')

# D2 · rest 225 (G95): Влад зсунув кадр — без заголовка, без «Четыре сайта…» і кнопки
s = part(70)
s['t'] = ''
s['b'] = s['b'].replace('Четыре сайта — это четыре сотни сообщений агента<br>', '').replace('<div class="r222-q">Сколько бы это стоило?</div>', '')
note(s, 'як G95: без заголовка, рядка «Четыре сайта…» і кнопки')

# D4 · rest 231 (G149): «$10 грошима» — купюра на ноутбуці замість кулі
sub(76, 'Вторая история стоит <strong>десять долларов</strong>', 'Вторая история стоит <strong>$10</strong>', '$10 цифрою')
sub(76, 'assets/gen-164-213/s-sales-laptop-open.webp', 'assets/gen-rest-1012/r231-ten.webp', 'купюра $10 на ноутбуці')

# D5 · rest 232 (G150): Наталья, 47 → Аня, 39 + фото обох
sub(77, '<div class="p12-pane-h"><span>Наталья,</span> <b>47</b></div><div class="p12-it"><b>$300</b> на пятый день</div><div class="p12-it"><b>4 клиента</b> на обслуживании</div>',
    '<div class="p12-pane-h"><span>Аня,</span> <b>39</b></div><div class="p12-it"><b>$500</b> через 2 недели</div><div class="p12-it"><b>4 клиента</b> на обслуживании</div><div class="p12-it"><b>$2.000/мес</b> +</div>',
    'Аня, 39 замість Натальи (G150)')
sub(77, '<div class="sl2-a p12-pane" style="--d:0.2s">',
    '<div class="sl2-a p12-pane" style="--d:0.2s"><img class="p12-ph" src="assets/gen-rest-1012/sasha-14.webp" alt="Саша">', 'фото Саші')
sub(77, '<div class="sl2-a p12-pane" style="--d:0.4s">',
    '<div class="sl2-a p12-pane" style="--d:0.4s"><img class="p12-ph" src="assets/gen-rest-1012/anya-39.webp" alt="Аня">', 'фото Ані')

# D6 · rest 240 (G157)
sub(85, 'Готовы инвестировать $50/мес на нейронки', 'Готовы инвестировать $70/мес на нейронки', '$70 (G157)')

# D3 · rest 249 (G123): фото Свєти зверху
sub(91, '<b class="sl-big cnt"', '<div class="r249-ph"><img src="assets/gen-rest-1012/sveta-selfie.webp" alt=""><img src="assets/gen-rest-1012/sveta-roses.webp" alt=""></div><b class="sl-big cnt"',
    'два фото Свєти (G123)')

OV.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
