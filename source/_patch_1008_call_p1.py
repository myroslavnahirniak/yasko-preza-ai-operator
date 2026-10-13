#!/usr/bin/env python3
"""08.10 дзвінок Влад × Мирослав (transcripts/2026-10-08-preza-vlad/ROZBIR.md, розділ A) — перша частина /rest:
rest 41 (copy-g293) «УСЛУГА 07 / 07» → «05 / 07» і картка тепер перед rest 40 («живёт в телефоне»), як у решти послуг;
rest 56 (…3012) «Это получится сделать, если вы не маркетолог…» червоним, без жовтої плашки (Google G324);
rest 23 (…1528) замість статичної обкладинки — відео «Агент-сайтов-инструкция» (обкладинка = його перший кадр);
rest 10 (copy-g245) замість 8 неонових роботів — зелена «студія агента» з того ж відео (луп туди-назад);
rest 16 (new-g251) знову таблиця (як v5 #170), конкуренція AI-продавця 3, як на картці;
нові картки каталогу 06/07 AI-таргет і 07/07 AI-SEO (копії 2226#16) перед їхніми екранами; на картці AI-SEO — відео AI-SEO;
rest 44 (2921#33) менше тексту: без рядка «Запускает → Тестирует → Оптимизирует» і без ціни (вона на картці);
rest 45 (2921#36) без плашки «$400–$1.800 · …» (вона на картці);
rest 47–49 (ChatGPT / Gemini / карта) прибрано — це все є у відео AI-SEO;
«УСЛУГА 0N / 07» на екранах послуг — той самий формат і місце, що на картках (маркер .svc-eb, CSS у rest-1006.css).
"""
import json, re, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-call-p1-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
V = o['__visibleGoogleAudit']['slides']; DO = o['__deckOrder']; E = DO['entries']
NOTE = ' · 08.10 дзвінок з Владом'
PARTS = V['g3f9b3adf0b8_0_2921']['presentationParts']['slides']


def idx(pred):
    hits = [i for i, e in enumerate(E) if pred(e)]
    assert len(hits) == 1, hits
    return hits[0]


def rep(s, old, new):
    assert s.count(old) == 1, old[:80]
    return s.replace(old, new)


# --- rest 41: номер картки AI-продавця + порядок (картка перед «живёт в телефоне») ---
y = V['copy-g293']
y['set']['b'] = rep(y['set']['b'], 'УСЛУГА 07 / 07', 'УСЛУГА 05 / 07')
y['reason'] += NOTE + ': номер 05 / 07, картка перед «AI-продавец, который живёт в телефоне»'
c = E.pop(idx(lambda e: isinstance(e, dict) and e.get('id') == 'copy-g293'))
E.insert(idx(lambda e: e == 'g3f9b3adf0b8_0_2921#30'), c)

# --- rest 56: червоний рядок без плашки ---
x = V['g3f9b3adf0b8_0_3012']
x['set']['b'] = rep(x['set']['b'], '<div class="s16-bottom">', '<div class="s16-bottom r56-red">')
x['reason'] += NOTE + ': «Это получится сделать…» червоним без жовтої плашки, як у Google G324'

# --- rest 23: відео агента замість статичної обкладинки ---
x = V['g3f9b3adf0b8_0_1528']
x['set']['b'] = rep(x['set']['b'],
    '<img class="r23-cover" src="assets/google-1008/g261-agent-cover.webp" alt="AI-агент, который делает сайт — собирает сайт клиники сам и показывает каждый шаг работы">',
    '<video class="r23-cover" src="assets/video/agent-sites/agent-sites-instrukciya.mp4" poster="assets/video/agent-sites/agent-sites-instrukciya-poster.jpg" '
    'autoplay muted loop playsinline aria-label="AI-агент, который делает сайт — собирает сайт клиники сам и показывает каждый шаг работы"></video>')
x['reason'] += NOTE + ': замість обкладинки — відео «Агент-сайтов-инструкция» (Влад надіслав у Telegram)'

# --- rest 10: студія агента (зелений пайплайн) замість 8 неонових роботів ---
x = V['copy-g245']
x['set']['b'] = rep(x['set']['b'], '<div class="r10-out">',
    '<div class="r10-studio"><video src="assets/video/agent-sites/r010-studio-loop.mp4" poster="assets/video/agent-sites/r010-studio-loop-poster.jpg" '
    'autoplay muted loop playsinline aria-label="Офис агента: специалисты по очереди делают свою часть сайта"></video></div><div class="r10-out">')
x['foundation']['block129']['art'] = None
x['reason'] = x.get('reason', '') + NOTE + ': замість «нейрослопу» (8 неонових роботів) — анімація студії агента з відео «Агент-сайтов-инструкция»'

# --- rest 16: таблиця замість сітки карток ---
src = o['__deckOrder']['slides']['new-g251']['b']
rows = src.split('<div class="row">')
r5 = [i for i, r in enumerate(rows) if '<em>05</em>AI-продавец' in r]
assert len(r5) == 1
r = rows[r5[0]]
cmp_old = re.search(r'<span class="sg cmp">(.*?)</span><b>6</b>', r).group(0)
r = r.replace(cmp_old, '<span class="sg cmp">' + '<i class="on"></i>' * 3 + '<i></i>' * 7 + '</span><b>3</b>')
rows[r5[0]] = r
V['new-g251']['set']['b'] = '<div class="row">'.join(rows)
V['new-g251']['reason'] += NOTE + ': знову таблиця, як у v5 #170 (картки «ніяк не порівняти»); попит і конкуренція — різними кольорами'

# --- картки 06/07 і 07/07 у форматі каталогу ---
STRIP = ['AI-сайты', 'AI-дизайн', 'AI-видео', 'Контент-завод', 'AI-таргет', 'AI-SEO', 'AI-продавец']


def bars(n):
    return ''.join('<i class="co-on"></i>' if i < n else '<i class=""></i>' for i in range(10))


def card(num, title, media, cls, price, unit, diff, dem, cmp, active):
    strip = ''.join('<button class="%s" data-catalog-go="%d">%s</button>' % ('co-active' if k == active else '', i, k) for i, k in enumerate(STRIP, 1))
    return ('<section class="s16-step catalog-orbit-stage"><div class="co-slidehead"><div class="co-servicenum">УСЛУГА %s / 07</div>'
            '<h2 class="co-service-title">%s</h2></div><div class="co-product-scene co-media %s">%s</div>'
            '<div class="co-portrait"><img src="assets/photo/vlad-portrait-studio.png" alt="Влад"><span><b>7 услуг</b>агенты делают целиком</span></div>'
            '<div class="co-facts"><div class="co-pricebox"><span class="co-label">Ваш чек</span><div class="co-price">%s</div><span class="co-unit">%s</span></div>'
            '<div class="co-difficulty"><span>Сложность</span><b>%s</b></div>'
            '<div class="co-metric"><div class="co-metrichead">Спрос<strong>%d</strong></div><div class="co-bars">%s</div></div>'
            '<div class="co-metric co-competition"><div class="co-metrichead">Конкуренция<strong>%d</strong></div><div class="co-bars">%s</div></div></div>'
            '<div class="co-service-strip">%s</div><div class="co-legend">Жёлтое — сильная сторона. Серое — то, о чём надо знать заранее</div></section>'
            ) % (num, title, cls, media, price, unit, diff, dem, bars(dem), cmp, bars(cmp), strip)


TEMPLATE = {k: v for k, v in V['copy-g293'].items() if k in ('remove', 'foundation')}
cards = {
    'copy-c06': ('g3f9b3adf0b8_0_2921#33', 'AI-таргет', card('06', 'AI-таргет (платная реклама)',
        '<img class="h" src="assets/gen-rest-1006/r048-ads-agent-final.webp" alt="Агент ведёт бюджет в объявления, которые приносят заявки, и ставит на паузу те, что сливают">',
        'co-m06', '$300–$800', 'в месяц', 'средняя', 7, 7, 'AI-таргет')),
    'copy-c07': ('g3f9b3adf0b8_0_2921#36', 'AI-SEO', card('07', 'AI-SEO (видимость в нейросетях)',
        '<video class="sq" src="assets/video/vlad-1409/ai-seo-reel-1080.mp4" poster="./assets/video/vlad-1409/ai-seo-reel-1080-poster.jpg" '
        'autoplay muted loop playsinline aria-label="AI-SEO: клиенты приходят из нейросетей"></video>',
        'co-m07s', '$400–$1.800', 'за пакет в месяц', 'средняя', 7, 1, 'AI-SEO')),
}
for cid, (before, step, html) in cards.items():
    assert cid not in V
    rec = json.loads(json.dumps(TEMPLATE))
    rec['foundation']['block129']['steps'] = [step]
    rec['set'] = {'b': html}
    rec['reason'] = '08.10 дзвінок з Владом: картка каталогу «%s» у тому ж форматі, що й інші послуги (чек / складність / попит / конкуренція)' % step
    V[cid] = rec
    E.insert(idx(lambda e: e == before), {'copy': 'g3f9b3adf0b8_0_2226#16', 'id': cid})

# --- rest 44: менше тексту ---
p = PARTS[32]
p['b'] = rep(p['b'], '<div class="s215-flow"><span>Запускает</span><i>→</i><span>Тестирует</span><i>→</i><span>Оптимизирует <b>24/7</b></span></div>', '')
p['b'] = rep(p['b'], '<div><strong>$300–$800</strong><span>в месяц · сложность средняя</span></div>', '')
p['reason'] = (p.get('reason') or '') + NOTE + ': менше тексту — без рядка «Запускает → Тестирует → Оптимизирует» і без ціни (вона на картці 06/07)'

# --- rest 45: без плашки з ціною (вона на картці 07/07) ---
p = PARTS[35]
p['b'] = rep(p['b'], '<span class="s16-price">$400–$1.800 · за пакет в месяц · сложность средняя</span>', '')
p['reason'] = (p.get('reason') or '') + NOTE + ': ціна й складність — на картці 07/07, плашку прибрано'

# --- rest 47–49 прибрати: ChatGPT / Gemini / карта є у відео AI-SEO ---
for k in ('g3f9b3adf0b8_0_2921#42', 'g3f9b3adf0b8_0_2921#43', 'new-g304'):
    if k not in DO['drop']:
        DO['drop'].append(k)

# --- «УСЛУГА 0N / 07» на екранах послуг: формат і місце як на картках ---
LABEL = {5: '02', 13: '03', 24: '04', 29: '05', 32: '06', 35: '07', 36: '07'}
for i, n in LABEL.items():
    p = PARTS[i]
    b129 = p['foundation']['block129']
    assert (b129.get('eyebrow') or '').startswith('Услуга'), (i, b129.get('eyebrow'))
    b129['eyebrow'] = 'Услуга %s / 07' % n
    if 'svc-eb' not in p['b']:
        p['b'] = '<i class="svc-eb" hidden></i>' + p['b']
# копія 2921#30 у головній частині (вже записана) — лишається як була
V['copy-g023'].setdefault('foundation', {}).setdefault('block129', {})['eyebrow'] = 'Услуга 5 из 7'

P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
