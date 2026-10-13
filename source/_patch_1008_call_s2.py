#!/usr/bin/env python3
"""08.10 дзвінок з Владом, розділ B (transcripts/2026-10-08-preza-vlad/ROZBIR.md): Секрет 2 = Google 326–384,
як Влад переписав його під час дзвінка (свіжий експорт: source/google-2026-10-08-call/).
Порядок і текст — з Google (описки виправлено, акцент — <em> замість капсу); картинки Влада — assets/google-1008call/;
підрізані постери (латки/обрізи Влада) — assets/gen-s2-1008/ (source/_img_patch_1008.py); бабуся-швачка і приціл — Higgsfield.
Нові екрани — layout s16-g1001 з маркером .s2n-* (CSS у кінці css/rest-1006.css)."""
import json, re, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-call-s2-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
V = o['__visibleGoogleAudit']['slides']; DO = o['__deckOrder']; E = DO['entries']; D = DO['slides']
S2 = 'g3f9b3adf0b8_0_1774'
PARTS = V[S2]['presentationParts']['slides']
A, G8 = 'assets/google-1008call/', 'assets/gen-s2-1008/'
strip = lambda h: re.sub(r'<[^>]+>', '', h or '')


def new(id, g, t, b, layout='s16-g1001', art=None):
    assert id not in D, id
    b129 = {'kind': 's16', 'v2': True, 'layout': layout}
    if art:
        b129['art'] = art
    D[id] = {'mvp': 1, 't': t, 'k': '', 'b': b,
             'note': '08.10 дзвінок з Владом: нова сторінка Google G%d (Секрет 2).' % g,
             'foundation': {'local': 0, 'type': 'content', 'sourceOnly': False, 'omitMedia': True, 'media': [], 'block129': b129},
             'googleNumber': 5000 + g, 'googleNow': g, 'originalLocal': None}
    return {'new': id}


def poster(src, alt):
    return [{'src': src, 'alt': alt}]


def part(n, g, **kw):
    """Правка частини 1774 #n (як у Google Gg)."""
    p = PARTS[n - 1]; f = p['foundation']
    if 'poster' in kw:
        f.pop('importedHTML', None); f.pop('importedLocal', None)
        f['block129'] = {'kind': 's16', 'v2': True, 'layout': 's16-poster', 'art': poster(kw['poster'], strip(kw.get('t', p['t'])))}
    if 't' in kw:
        p['t'] = kw['t']
    if 'b' in kw:
        p['b'] = kw['b']
    p['reason'] = (p.get('reason') or '') + ' · 08.10 дзвінок з Владом: як у Google G%d' % g
    return S2 + '#%d' % n


# --- правки наших екранів (латки й обрізи Влада) ---
k331 = part(10, 331, poster=G8 + 's2-331-dontlove.webp')                   # без «Даже когда было агентство… Я нанял отдел продаж»
k332 = part(11, 332, poster=G8 + 's2-332-photographer.webp')               # лише колонка «Фотограф», без «Сначала отдал…»
k358 = part(15, 358, poster=G8 + 's2-358-safe.webp')                       # без «Первый вопрос закрыт. Второй тяжелее»
k359 = part(9, 359, t='')                                                  # без заголовка «Биржа против салона груминга»
k360 = part(6, 360, poster=G8 + 's2-360-svazka3.webp')                     # три картки без заголовка і нижнього рядка
PARTS[5]['k'] = ''; PARTS[5]['foundation']['block129'].pop('eyebrow', None)
k370 = part(21, 370, poster=G8 + 's2-370-agent-chat.webp', t='И дал ему ИИ-агента, которого обучил <em>продавать</em>')
k384 = part(32, 384, poster=G8 + 's2-384-one-left.webp', t='Осталось <em>одно</em>')  # без «Петля закрыта.» і «Видите себя внутри?…»

y = V['new-g336']                                                          # G338: «-80% от рыночной стоимости» замість «¼»
y['set']['t'] = 'А потом спросил: «Если вам надо, можете заплатить за него <em>-80% от рыночной стоимости</em>»'
y['foundation']['block129']['art'] = poster(G8 + 's2-338-minus80.webp', 'А потом спросил: «Если вам надо, можете заплатить за него -80% от рыночной стоимости»')
y['reason'] += ' · 08.10 дзвінок з Владом: «-80% от рыночной стоимости» замість «¼» (Google G338), і в заголовку, і на бирці'

g329 = D['new-g329']                                                       # G329: плашка-цитата зверху + фото Саші за ноутом
g329['t'] = ''
g329['b'] = ('<div class="s2n s2n-qp"><div class="s2n-quote"><p>Саша говорил слово в слово.</p><p class="acc">Через сутки у него была первая продажа</p></div>'
             '<img src="%ssasha-laptop.webp" alt="Саша за ноутбуком"></div>' % A)
g329['foundation']['block129'].pop('art', None)
g329['note'] += ' · 08.10 дзвінок: плашка зверху + фото Саші за ноутбуком (Google G329), стоїть після «базару».'

# --- нові екрани ---
SAY = '<i class="s2n s2n-say" hidden></i>'
LOCK = ('<svg viewBox="0 0 48 48" aria-hidden="true"><rect x="9" y="21" width="30" height="22" rx="4" fill="none" stroke="#fdd506" stroke-width="2.6"/>'
        '<path d="M15 21v-6a9 9 0 0 1 18 0v6" fill="none" stroke="#fdd506" stroke-width="2.6"/><circle cx="24" cy="31" r="2.6" fill="#fdd506"/><path d="M24 33v4" stroke="#fdd506" stroke-width="2.6" stroke-linecap="round"/></svg>')
pic = lambda *imgs, cls='': '<div class="s2n s2n-pic%s">%s</div>' % (cls, ''.join('<img src="%s" alt="%s">' % (s, a) for s, a in imgs))

n330 = new('new-c330', 330, 'А через месяц <em>$950</em>', pic((A + 'sasha-sofa.webp', 'Саша'), (A + 'sasha-chat-950.webp', 'Переписка: «Сколько ты на сайтах заработал за этот месяц с хвостом?» — «900–1100$ примерно»'), cls=' s2n-two'))
n333 = new('new-c333', 333, 'Поэтому у меня всегда была одна <em>стратегия</em>', '', 's16-poster', poster(G8 + 's2-333-marketer.webp', 'Маркетолог: опыта не было — тренировался на бесплатных, делал работу целиком, а потом спрашивал: «сколько готовы заплатить?»'))
n339 = new('new-c339', 339, 'Согласились <em>бы?</em>', SAY)
n341 = new('new-c341', 341, 'И предложил ему <em>нестандартную связку</em>', SAY)
n343 = new('new-c343', 343, 'Что: AI-сайты от $250', '', 's16-poster', poster(G8 + 's2-343-svazka1.webp', 'Что: AI-сайты от $250'))
n344 = new('new-c344', 344, '', '<div class="s2n s2n-card"><img src="%scard-ai-sites.webp" alt="AI-сайты, которые приводят клиентов: $250–$1.200 за пакет, сложность лёгкая, спрос 9, конкуренция 8"><p>Начали с самой <em>простой услуги</em></p></div>' % A)
n345 = new('new-c345', 345, 'Что: AI-сайты от $250 · Кому: локальному бизнесу', '', 's16-poster', poster(G8 + 's2-345-svazka2.webp', 'Что: AI-сайты от $250. Кому: локальному бизнесу — он есть на Google-картах, а сайта нет или он старый'))
n346 = new('new-c346', 346, '', ('<div class="s2n s2n-vs2"><div class="l"><b>Фриланс-биржи</b><span>с жадными заказчиками</span></div>'
                                 '<div class="r"><b>Локальные бизнесы</b><span>с бабками и херовым сайтом</span></div>'
                                 '<img src="%sbirzha-sketch.webp" alt="Слева толпа исполнителей у одного заказчика, справа заказчик без единого исполнителя"></div>' % A))
n347 = new('new-c347', 347, 'И я дал ему наводку, где водятся клиенты, которые купят с <em>наибольшей вероятностью</em>', SAY)
n348 = new('new-c348', 348, '', ('<div class="s2n s2n-aim"><img class="hero" src="%ss2-348-pricel.webp" alt="Прицел наведён на один салон груминга на карте города">'
                                 '<div class="cards"><img src="%scard-nisha.webp" alt="Одна ниша — не распыляемся, берём одну и знаем её"><img src="%scard-lokacii.webp" alt="Топ-локации — города, где покупают чаще"></div></div>' % (G8, A, A)))
n349 = new('new-c349', 349, 'Есть разница, <em>кому</em> продавать услугу?', ('<div class="s2n s2n-vs"><figure><img src="%ss2-349-babushka.webp" alt="Бабушка-швея, которая делает пошив на заказ"></figure>'
                                                                              '<figure><img src="%ss2-349-dog.webp" alt="Груминг: собака на столе у грумера"></figure></div>' % (G8, G8)))
n350 = new('new-c350', 350, 'Есть разница, <em>где</em> охотиться?', '<div class="s2n s2n-cities"><span>Киев</span><span>Харьков</span></div>')
n351 = new('new-c351', 351, '?????', pic((A + 'salon-reply.webp', 'Ответ салона: «У нас такая ситуация, что нам не нужно много клиентов — у нас некому работать»')))
n352 = new('new-c352', 352, 'С моим комьюнити мы исследуем ниши и города, которые купят с <em>наибольшей вероятностью</em>, где минимальная конкуренция',
           '<div class="s2n s2n-lock"><img src="%sniches-table.webp" alt=""><span class="lk">%s</span></div>' % (A, LOCK))
n353 = new('new-c353', 353, '', ('<div class="s2n s2n-reveal s2n-rows"><img src="%sniches-table.webp" alt="Ниши, где покупают чаще: кузовной ремонт, автосервис…">'
                                 '<div class="bl"><img src="%sniches-table.webp" alt=""></div><span class="lk">%s</span></div>' % (A, A, LOCK)))
n354 = new('new-c354', 354, '', ('<div class="s2n s2n-reveal s2n-cols"><img src="%scities-cards.webp" alt="Где покупают: карточки городов и районов">'
                                 '<div class="bl"><img src="%scities-cards.webp" alt=""></div><span class="lk">%s</span></div>' % (A, A, LOCK)))
n355 = new('new-c355', 355, 'Я дал ему готовый <em>шаблон сайта</em>', pic((A + 'templates-100.webp', 'Агент подбирает дизайн из базы 100+ готовых сайтов')))
n356 = new('new-c356', 356, '', '<div class="s2n s2n-grid4">%s</div>' % ''.join(
    '<img src="%stpl-%d.webp" alt="%s">' % (A, i, a) for i, a in enumerate(['Шаблон: пекарня', 'Шаблон: украшения', 'Шаблон: очки', 'Шаблон: автосервис'], 1)))
n366 = new('new-c366', 366, 'Связка через <em>бесплатный сайт</em>', ('<div class="s2n s2n-list"><div>Найти бизнес с херовым сайтом</div>'
                                                                   '<div>Сказать, что сделали для него сайт <b>бесплатно</b></div>'
                                                                   '<div>Тем, кому стало интересно, ИИ-агент делает «черновик сайта», но с данными конкретного бизнеса</div>'
                                                                   '<div>Докручиваем уже за деньги</div></div>'))
n368 = new('new-c368', 368, 'Из 20 бизнесов по статистике <em>2 захотят на него посмотреть</em>', SAY)
n369 = new('new-c369', 369, 'А 50% из них <em>купят его</em>', SAY)
n371 = new('new-c371', 371, 'Сайт <em>до</em>', pic((A + 'fainopet-before.webp', 'Старый сайт груминг-салона «ФАЙНО!pet»')))
n372 = new('new-c372', 372, 'Сайт <em>после</em>', ('<div class="s2n s2n-site"><div class="bar"><i></i><i></i><i></i><span>fainopet.vercel.app</span>'
                                                    '<a href="https://fainopet.vercel.app/" target="_blank" rel="noopener">открыть ↗</a></div>'
                                                    '<iframe data-src="https://fainopet.vercel.app/" title="ФАЙНО!pet — новый сайт груминг-салона" loading="lazy"></iframe></div>'))
n373 = new('new-c373', 373, '', pic((A + 'msg-70.webp', 'Сайт уже работает и открывается в интернете. Он готов примерно на 70%…')))
n374 = new('new-c374', 374, '', pic((A + 'msg-1000.webp', 'Обычно за такую работу я беру $1000. Но основа уже готова, поэтому для вас я доделаю его за $250…')))
n375 = new('new-c375', 375, '', pic((A + 'msg-templates.webp', 'Если не ответили 2 дня… Если спросят, почему так дёшево…')))
n379 = new('new-c379', 379, 'И взял себе <em>спортбайк</em>)', pic((A + 'sasha-bike.webp', 'Саша и его спортбайк')))

# --- порядок Секрету 2 = Google 326–384 ---
a = [i for i, e in enumerate(E) if isinstance(e, dict) and e.get('id') == 'copy-g327']
b = [i for i, e in enumerate(E) if e == 'g3f9b3adf0b8_0_1943#1']
assert len(a) == 1 and len(b) == 1 and a[0] < b[0], (a, b)
ORDER = ([E[a[0]], S2 + '#2', S2 + '#3', {'new': 'new-g329'}, n330, k331, k332, n333,
          {'new': 'new-g332'}, {'new': 'new-g333'}, {'new': 'new-g334'}, {'new': 'new-g335'}, {'new': 'new-g336'}, n339,
          S2 + '#16', n341, n343, n344, n345, n346, n347, n348, n349, n350, n351, n352, n353, n354, n355, n356,
          S2 + '#14', k358, k359, k360, S2 + '#17', n366, n368, n369, k370, n371, n372, n373, n374, n375,
          S2 + '#26', S2 + '#25', {'new': 'new-x086b'}, n379, S2 + '#27', S2 + '#8', S2 + '#28', k384])
old = E[a[0]:b[0]]
E[a[0]:b[0]] = ORDER
gone = [e for e in old if isinstance(e, str) and e not in ORDER]
for k in gone:
    if k not in DO['hide']:
        DO['hide'].append(k)
print('Секрет 2: було', len(old), 'екранів, стало', len(ORDER), '; приховано', len(gone), ':', ', '.join(k.split('#')[1] for k in gone),
      '; прибрано нові:', [e['new'] for e in old if isinstance(e, dict) and 'new' in e and e not in ORDER])
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
