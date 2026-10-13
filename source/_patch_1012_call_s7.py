#!/usr/bin/env python3
"""12.10 дзвінок з Владом — блок «7 услуг» після «Это не ещё одна информация» (Google «продающая» G85–G180).
Порядок продаючої частини від «Антон Тысячник» (2226#58) до кінця = Google; 19 екранів, яких у Google немає,
поки лишаються біля сусідів (Мирослав: «поки залиш», питаємо Влада) — позначені KEEP.
Готові частини: картки послуг — копії з першої частини /rest, артефакти/Женя/Аня — приховані частини 2921.
Нові екрани (new-x12*) — Віоріка, Інна, фото Влада, «от $70/мес», «Золотой дождь».
Після: FOUNDATION_SOURCE=google-2026-09-16/foundation-source-v2.json python3 source/_foundation_prepare.py && python3 source/_build_slides.py
"""
import copy, json, shutil, time
from pathlib import Path

R = Path(__file__).resolve().parent.parent
OV = R / 'source/overrides.json'
o = json.load(open(OV))
shutil.copy(OV, R / f'source/_bak/overrides-1012-before-call-s7-{int(time.time())}.json')
do = o['__deckOrder']; V = o['__visibleGoogleAudit']['slides']; E = do['entries']
S = 'g3f9b3adf0b8_0_2226'; A = 'g3f9b3adf0b8_0_2921'
s = lambda n: f'{S}#{n}'
a = lambda n: f'{A}#{n}'
REASON = '12.10 дзвінок з Владом: блок «7 услуг» (Google «продающая»)'
eid = lambda e: e if isinstance(e, str) else (e.get('key') or e.get('id') or e.get('new'))

# ---- копії карток послуг (джерело + патч наявної копії з першої частини /rest)
def card(new_id, like):
    src = next(e for e in E if isinstance(e, dict) and e.get('id') == like)
    V[new_id] = copy.deepcopy(V[like])
    V[new_id]['reason'] = REASON + f' · копія {like}'
    return {'copy': src['copy'], 'id': new_id}

def cp(new_id, key):
    return {'copy': key, 'id': new_id}

# ---- нові екрани
IMG = 'assets/gen-rest-1012/s7/'
def new(nid, g, t, b, note=''):
    do['slides'][nid] = {
        'mvp': 1, 't': t, 'k': '', 'b': b,
        'note': f'{REASON}: Google G{g}. {note}'.strip(),
        'foundation': {'local': 0, 'type': 'content', 'sourceOnly': False, 'omitMedia': True, 'media': [],
                       'block129': {'kind': 's16', 'v2': True, 'layout': 's16-g1001'}},
        'googleNumber': 7000 + g, 'googleNow': g, 'originalLocal': None}
    return {'new': nid}

# G86 · таблиця 7 послуг = копія rest 16 (new-g251) разом з її патчем
do['slides']['new-x12tbl'] = copy.deepcopy(do['slides']['new-g251'])
do['slides']['new-x12tbl']['note'] = (do['slides']['new-x12tbl'].get('note') or '') + f'\n{REASON}: G86, копія rest 16'
if 'new-g251' in V:
    V['new-x12tbl'] = copy.deepcopy(V['new-g251'])

N = [
    new('new-x12v1', 128, 'Вложила $717 и&nbsp;сделала продажу на&nbsp;<em>$111.000</em>', '<i class="s2n s2n-say" hidden></i>'),
    new('new-x12v2', 129, '', f'<div class="s12-person"><img src="{IMG}vio-photo.webp" alt="Виорика Игнат"><div class="s12-pp"><p class="s12-nm">Виорика Игнат, <em>43</em></p><p class="s12-ds">мама в декрете, работает в найме в агентстве недвижимости</p></div></div>'),
    new('new-x12v3', 130, '', f'<div class="s2n s2n-pic s12-stack"><img src="{IMG}vio-review-1.webp" alt="Отзыв Виорики: раньше я думала, что таргет — это сложно"><img src="{IMG}vio-review-2.webp" alt="Результат за три недели: 75 заявок по $9.56 и первая продажа виллы за 115.000$"></div>'),
    new('new-x12v4', 131, '', f'<div class="s2n s2n-pic s12-ads"><img src="{IMG}vio-ad-1.webp" alt="Креатив: Entry — 1 &amp; 2 bedrooms от $115.000"><img src="{IMG}vio-ad-2.webp" alt="Креатив: Designed for living. Built for returns"></div>',
        'Креативи Віоріки — поки картинки з Google; відео Мирослав надішле (Влад: «видоси я тобі прислав»).'),
    new('new-x12v5', 132, '', f'<div class="s2n s2n-pic s12-one"><img src="{IMG}vio-fwd.webp" alt="Переслано от Viorika Ignat: креативы агента"></div>'),
    new('new-x12inna', 133, 'Инна · туризм · <em>в 56 лет</em>', f'<div class="s2n s2n-pic s12-inna"><img src="{IMG}inna-photo.webp" alt="Инна"><img src="{IMG}inna-case.webp" alt="Кейс Инны: $0,68 диалог с туристом"></div><a class="s12-site" href="https://synora-case.vercel.app/" target="_blank" rel="noopener">Видеоотзывы ↗</a>',
        'Влад: «получает по 70 центов потенциального клиента. И тут её видеоотзывы с сайта» (synora-case.vercel.app).'),
    new('new-x12f1', 147, '', f'<div class="s2n s2n-pic s12-fam"><img src="{IMG}fam-1.webp" alt=""><img src="{IMG}fam-2.webp" alt=""></div>',
        'Влад: «хочу ребёнка, виллу построить… поэтому у меня нет этого года».'),
    new('new-x12f2', 148, '', f'<div class="s2n s2n-pic s12-fam"><img src="{IMG}fam-3.webp" alt=""><img src="{IMG}fam-4.webp" alt=""><img src="{IMG}fam-5.webp" alt=""></div>'),
    new('new-x12p70', 160, '', '<div class="s12-p70"><div class="s12-logos"><span><img src="assets/gen-rest-1012/logos/privatbank.png" alt="ПриватБанк"></span><span><img src="assets/gen-rest-1012/logos/monobank.svg" alt="monobank"></span></div><p class="s12-big">от <em>$70/мес</em></p><p class="s12-sub">стоимость участия + подписка на нейронки</p><p class="s12-fin">Цена решения</p></div>',
        'Влад: «приват-логотип и моно-логотип… от 70 долларов в месяц… Цена вашего решения сегодня».'),
    new('new-x12p70b', 161, 'Есть какая-то херня, на которую вы тратите <em>$70/мес</em>?', '<p class="s2n s2n-lead">сижки, вейпы, подписки, суши, телочки, пивасик, игры</p>'),
    new('new-x12gold', 165, '', '<div class="s12-phone"><video src="assets/video/slots/zolotoy-dozhd.mp4" autoplay muted loop playsinline preload="auto"></video></div>',
        'Скріни каналу «Золотой дождь» без дат: беремо запис assets/video/slots/zolotoy-dozhd.mp4 (дати вже прибрані).'),
]
NV = {x['new']: x for x in N}

seg = [
    s(62),                                   # G85 Это не ещё одна информация
    {'new': 'new-x12tbl'},                   # G86 таблиця 7 послуг
    card('copy-x12c01', 'copy-g254'),        # G87 AI-сайты
    s(68),                                   # G88 артефакт «Что делает агент по сайтам»
    s(67), s(69),                            # KEEP 222, 224
    s(66),                                   # G89 конвейер
    s(58),                                   # G90 Антон
    s(59),                                   # KEEP 214
    s(60), s(61), s(63),                     # G91–G93
    s(64),                                   # KEEP 219 Юра
    s(65), s(70),                            # G94, G95
    s(71), {'new': 'new-x226hunt'}, s(73),            # (#71 у drop) KEEP 226, 228
    card('copy-x12c02', 'copy-g266'),        # G96 AI-дизайн
    cp('copy-x12d2', a(6)), a(7),            # G97 что выходит, G98 артефакт
    s(74),                                   # G100 Один макет окупает
    card('copy-x12c03', 'copy-g273'),        # G101 AI-видео
    cp('copy-x12v3', a(14)), a(18),          # G102 Услуга 3 из 7, G103 артефакт
    a(19), a(20), a(21), a(22), a(23), a(24),  # G104–G109 Женя
    card('copy-x12c04', 'copy-g287'),        # G110 Контент-завод
    cp('copy-x12k4', a(25)), a(26),          # G111, G112 артефакт
    cp('copy-x12k5', a(27)), cp('copy-x12k6', a(28)),  # G113, G114
    'g409d4d20be6_0_198#0', 'g409d4d20be6_0_203#0', 'g409d4d20be6_0_208#0', s(90), s(91),  # G115–G123 Света
    s(92),                                   # KEEP 250
    card('copy-x12c05', 'copy-g293'), a(31),  # G124 AI-продавец, G125 артефакт
    card('copy-x12c06', 'copy-c06'), a(35),  # G126 AI-таргет, G127 артефакт
    NV['new-x12v1'], NV['new-x12v2'], NV['new-x12v3'], NV['new-x12v4'], NV['new-x12v5'], NV['new-x12inna'],  # G128–G133
    card('copy-x12c07', 'copy-c07'),         # G134 AI-SEO
    a(44), a(45), a(46), a(48), a(49), a(51), a(52), a(53),  # G135–G142 Аня
    cp('copy-x12n3', s(84)),                 # G143 Три набора на одном экране
    cp('copy-x12whole', s(45)),              # G144 Что входит целиком
    s(72), s(75),                            # G145, G146
    NV['new-x12f1'], NV['new-x12f2'],        # G147, G148
    s(76), s(77), s(78),                     # G149–G151
    s(79), s(80),                            # KEEP 234, 235
    s(81), s(82), s(83), s(84), s(85), s(86), s(87),  # G153–G159
    s(88), s(89),                            # KEEP 243, 244
    NV['new-x12p70'], NV['new-x12p70b'],     # G160, G161
    s(93),                                   # G162 Под ключ
    s(94), s(95), s(96), s(97),              # KEEP 252–255
    s(98), s(99),                            # G163, G164
    NV['new-x12gold'],                       # G165
    s(101), s(102),                          # KEEP 258, 259
    *[s(n) for n in range(103, 116)],        # G166–G178
    s(116),                                  # KEEP 273
    s(117), s(118),                          # G179, G180
]

i0 = E.index(s(58))
old = E[i0:]
oldk = [eid(x) for x in old]
newk = [eid(x) for x in seg]
missing = [k for k in oldk if k not in newk]
dups = {k for k in newk if newk.count(k) > 1}
assert not missing, missing
assert not dups, dups
for k in newk:
    if k.startswith(A) and k in do['hide']:
        pass  # прихована частина 2921 стає видимою, бо тепер є в entries
E[i0:] = seg
json.dump  # noqa
OV.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok: сегмент', len(old), '→', len(seg))
