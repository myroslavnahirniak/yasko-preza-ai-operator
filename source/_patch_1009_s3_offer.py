#!/usr/bin/env python3
"""09.10 · Google Влада після 08.10 (експорт source/google-2026-10-09/), від Секрету 3 до «Полной системы» (продаюча система):
Секрет 3: «ЕГО СЛОВА» Влад розбив на два екрани — G403 «Взял две ниши из списка связок» + картка «Украина» (нова),
          G404 «и включил охотника» + повідомлення Василия (наш 1943#18 без надзаголовка й перших рядків — js/secret3-final-b.js case 16).
Офер:     G427/G428 — нові: «$3000 чистого дохода в месяц» і «5% … $15 000 … для чего я провожу этот мастер-класс» (текст — з текстового поля Влада);
          G429 (2226#4) — латка поверх «AI Маркетолог 3.0» → постер без старої назви (source/_img_patch_1009.py);
          G432/G433 (2226#7/#8) — «Уровень 1» перед «Блок 1/2»;
          G434/G435 — нові: скріни блоку «Агенты AI-сайты и AI-маркетинг» з сайту; G436 — картка «AI-сайты» (копія каталогу, без легенди внизу);
          G437/G438 (2226#9 «Маркетинг — 7 задач», #10 «Сайты — 9 задач») приховано."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1009-before-s3-offer-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
V = o['__visibleGoogleAudit']['slides']; DO = o['__deckOrder']; E = DO['entries']; D = DO['slides']
S3, SV = 'g3f9b3adf0b8_0_1943', 'g3f9b3adf0b8_0_2226'
P3 = V[S3]['presentationParts']['slides']; PS = V[SV]['presentationParts']['slides']
A = 'assets/google-1009/'
NOTE = '09.10 Google Влада (G%d)'


def new(id, g, t, b):
    assert id not in D, id
    D[id] = {'mvp': 1, 't': t, 'k': '', 'b': b, 'note': '09.10: нова сторінка Google G%d.' % g,
             'foundation': {'local': 0, 'type': 'content', 'sourceOnly': False, 'omitMedia': True, 'media': [],
                            'block129': {'kind': 's16', 'v2': True, 'layout': 's16-g1001'}},
             'googleNumber': 5000 + g, 'googleNow': g, 'originalLocal': None}
    return {'new': id}


def at(key):
    hits = [i for i, e in enumerate(E) if e == key]
    assert len(hits) == 1, (key, hits)
    return hits[0]


# --- Секрет 3: G403 перед 1943#18, сам #18 = G404 ---
E.insert(at(S3 + '#18'), new('new-c403', 403, 'Взял две ниши из <em>списка связок</em>',
         '<div class="s2n s2n-pic"><img src="%sukraina-niches-card.webp" alt="Карточка «Украина» из списка связок: ниши — окна и двери, ремонт, мебель на заказ, стоматологии"></div>' % A))
x = P3[17]
x['t'] = 'и включил <em>охотника</em>'
x['b'] = x['b'].replace('<p>ЕГО СЛОВА</p><p>Взял две ниши из списка связок и включил охотника</p>', '<p>и включил охотника</p>')
x['note'] = (x.get('note') or '') + ' · ' + NOTE % 404 + ': без «ЕГО СЛОВА» і «Взял две ниши из списка связок» (окремий екран перед ним)'

# --- офер: G427, G428 після 2226#3 ---
i = at(SV + '#3') + 1
E[i:i] = [new('new-c427', 427, 'Мне интересно вывести каждого своего партнёра минимум на <em>$3000 чистого дохода в месяц</em>',
              '<p class="s2n s2n-lead">Развивать платформу, создавать новых агентов, тестировать, разрабатывать новые связки, исследовать новые тренды</p>'),
          new('new-c428', 428, '',
              '<div class="s2n s2n-goal"><div class="box">И за это вы мне будете платить <em>до 5% от этой выручки</em> в месяц на мою платформу</div>'
              '<p>Моя глобальная цель — зарабатывать <em>$15 000 в месяц</em>, помогая своим партнёрам</p>'
              '<p>Теперь вы понимаете, для чего я провожу этот мастер-класс</p></div>')]

# --- G429: постер без «AI Маркетолог 3.0» ---
y = PS[3]
y['foundation']['block129']['art'][0]['src'] = 'assets/gen-1009/r149-ustroeno-noname.webp'
y['reason'] = (y.get('reason') or '') + ' · ' + NOTE % 429 + ': латка поверх шапки скріна «AI Маркетолог 3.0» — стару назву прибрано'

# --- G432/G433: «Уровень 1» ---
for n, blk in ((7, 'Блок 1 · недели 1–2'), (8, 'Блок 2 · недели 3–4')):
    y = PS[n - 1]
    old = '<div class="eyebrow">%s</div>' % blk
    assert y['b'].count(old) == 1, (n, old)
    y['b'] = y['b'].replace(old, '<div class="eyebrow"><b class="lvl">Уровень 1</b>%s</div>' % blk)
    y['reason'] = (y.get('reason') or '') + ' · ' + NOTE % (424 + n) + ': «Уровень 1» перед блоком'

# --- G434–G436 після 2226#8; 2226#9/#10 приховати ---
i = at(SV + '#8') + 1
E[i:i] = [new('new-c434', 434, '', '<div class="s2n s2n-pic"><img src="%ssite-pack01-marketing.webp" alt="На выходе пакета 01: агенты AI-сайты и AI-маркетинг — вкладка AI-маркетинг"></div>' % A),
          new('new-c435', 435, '', ('<div class="s2n s2n-stack"><img src="%ssite-pack01-sites.webp" alt="На выходе пакета 01: агенты AI-сайты и AI-маркетинг — вкладка AI-сайты">'
                                    '<img src="%ssite-pack01-sites-service.webp" alt="AI-сайты, которые приводят клиентов: $250–1500 за пакет"></div>' % (A, A))),
          {'copy': SV + '#15', 'id': 'copy-c436'}]
c = json.loads(json.dumps({k: v for k, v in V['copy-g254'].items() if k in ('remove', 'set', 'foundation')}))
c['set']['b'] += '<i class="c436-crop" hidden></i>'
c['reason'] = '09.10 Google Влада (G436): картка «AI-сайты» каталогу після «Продукт и витрина», обріз знизу (без легенди)'
V['copy-c436'] = c
for n in (9, 10):   # ключі є в entries → лише drop (hide діє тільки на невказані екрани)
    k = SV + '#%d' % n
    if k not in DO['drop']:
        DO['drop'].append(k)

P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
