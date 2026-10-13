#!/usr/bin/env python3
"""08.10 аудит другої частини проти Google (source/audit-1008/REPORT.md): прибрати текст, якого в Google нема
(Влад обрізав кадр / закрив латкою, або ми додали при переробці 06.10)."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-audit-text-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
V = o['__visibleGoogleAudit']['slides']; D = o['__deckOrder']['slides']
def cut(node, frags, why):
    b = node['b'] if 'b' in node else node['set']['b']
    for f in frags:
        assert b.count(f) == 1, (why, f[:60])
        b = b.replace(f, '')
    if 'b' in node: node['b'] = b
    else: node['set']['b'] = b
    node['reason'] = (node.get('reason') or '') + ' · 08.10 аудит Google: ' + why
# rest 3 · G233 — у Google лише картка замовлення зі штампом «ЭТОТ»
cut(V['g409d4d20be6_0_310'], ['<div class="s16-stations" aria-hidden="true"><span>Рецепт</span><span>Замес</span><span>Сборка</span><span>Украшение</span></div>',
    '<div class="s16-bottom"><p>Фабрика начинается не с печи. С решения: <em>какой именно торт.</em></p><p class="s16-lead">Агент — так же. Не «сделай сайт», а «сайт-визитка локальному бизнесу»</p></div>'],
    'прибрано етапи-чіпси і два рядки внизу (нема на G233)')
# rest 9 · G244 — Влад обрізав кадр до 84.5% висоти
cut(V['g409d4d20be6_0_322'], ['<div class="s16-bottom"><p>Пять слоёв × четыре этапа — и это только один торт</p><p class="s16-lead">Внутри каждого агента — часы работы и обучения на каждый этап</p></div>'],
    'прибрано два рядки внизу (Влад обрізав кадр G244)')
# rest 11 · G246 — Влад обрізав кадр до 89.5% висоти
cut(V['g3f9b3adf0b8_0_2950'], ['<p class="s16-lead">Вам его собирать не надо. Он уже собран</p>'],
    'прибрано «Вам его собирать не надо…» (Влад обрізав кадр G246)')
# rest 16 · G251 — таблиця без заголовка; заголовок ми додали 06.10 з сайту Холсту
cut(V['new-g251'], ['<div class="r20-head"><b class="r20-ttl">7 услуг, которые агенты <em>делают целиком</em></b><span class="r20-sub">Спрос и конкуренция — баллы из десяти</span></div>'],
    'прибрано заголовок «7 услуг…/Спрос и конкуренция…» (нема на G251)')
# rest 42/43 · G294/G295 — Влад закрив ціну білою латкою
cut(D['new-g294'], ['<div class="g2-price"><small>Стоимость услуги</small><b>$500–2 000</b><span>за сборку плюс ведение</span></div>'],
    'прибрано «Стоимость услуги $500–2 000» (Влад закрив латкою на G294)')
cut(D['new-g295'], ['<div class="g2-price"><small>Стоимость услуги</small><b>$1000</b><span>за сборку и ведение</span></div>'],
    'прибрано «Стоимость услуги $1000» (Влад закрив латкою на G295)')
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
