#!/usr/bin/env python3
"""09.10 Влад/Мирослав:
rest 110 «Осталось одно» (1774#32) — «визуал хуйня»: замість кільця два варіанти, живий текст як у Google G384:
   A (у деці): Влад на даху з біноклем над нічним містом (nano_banana_pro за референсами Влада) — місток до Секрету 3 «где брать людей»;
   B (new-c384b, у drop, вмикається заміною): той самий текст + gif «Арнольд з біноклем» (Tenor).
rest 88 (new-c356) — 4 шаблони білими картками як у бібліотеці WorkNotHunt, кожна відкриває сайт у новій вкладці.
Охотник з луком і фото Влада в системі — js/secret3-final-a.js (case 13), js/secret3-final-c.js (case 32)."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1009-before-vlad-visuals-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
V = o['__visibleGoogleAudit']['slides']; DO = o['__deckOrder']; D = DO['slides']; E = DO['entries']
PARTS = V['g3f9b3adf0b8_0_1774']['presentationParts']['slides']

TXT = ('<div class="s2n-txt"><p>Продавать вы умеете — точнее, уметь и не надо.</p>'
       '<p>Остался вопрос, который я слышу чаще всех: <b>а когда это делать и где брать людей?</b></p></div>')
p = PARTS[31]
p['t'] = 'Осталось <em>одно</em>'
p['b'] = ('<div class="s2n s2n-one">' + TXT + '<img class="ph" src="assets/gen-1009/vlad/roof-binoculars.webp" '
          'alt="Влад на крыше с биноклем над ночным городом"></div>')
p['foundation']['block129'] = {'kind': 's16', 'v2': True, 'layout': 's16-g1001'}
p['reason'] = (p.get('reason') or '') + ' · 09.10 Влад: «визуал хуйня, можно со мной» → живий текст + Влад з біноклем над містом (варіант A; B з gif — new-c384b)'

D['new-c384b'] = {'mvp': 1, 't': 'Осталось <em>одно</em>', 'k': '',
                  'b': ('<div class="s2n s2n-one s2n-one-gif">' + TXT + '<div class="gif"><video src="assets/gif/arnold-binoculars.mp4" '
                        'poster="assets/gif/arnold-binoculars-poster.jpg" autoplay muted loop playsinline aria-label="Арнольд высматривает в бинокль"></video></div></div>'),
                  'note': '09.10 варіант B для «Осталось одно» (Google G384): gif Арнольд з біноклем. Інші gif: assets/gif/looking-around.mp4, cricket-anybody-home.mp4.',
                  'foundation': {'local': 0, 'type': 'content', 'sourceOnly': False, 'omitMedia': True, 'media': [],
                                 'block129': {'kind': 's16', 'v2': True, 'layout': 's16-g1001'}},
                  'googleNumber': 5384, 'googleNow': 384, 'originalLocal': None}
k = 'g3f9b3adf0b8_0_1774#32'
i = [n for n, e in enumerate(E) if e == k]; assert len(i) == 1
if {'new': 'new-c384b'} not in E:
    E.insert(i[0] + 1, {'new': 'new-c384b'})
if 'new-c384b' not in DO['drop']:
    DO['drop'].append('new-c384b')

SITES = [('https://examples.worknothunt.xyz/sites/bakery-facilities/', 'tpl-bakery', 'Bakery Facilities', ['пекарня', 'лендинг']),
         ('https://oyla-landing.vercel.app/', 'tpl-oyla', 'OYLA', ['украшения', 'премиум']),
         ('https://examples.worknothunt.xyz/sites/blind-by-glamour/', 'tpl-blind', 'Blind by Glamour', ['оптика', 'лендинг']),
         ('https://examples.worknothunt.xyz/sites/veyra/', 'tpl-veyra', 'VEYRA', ['автосервис', '3D'])]
cards = ''.join('<a class="tc" href="%s" target="_blank" rel="noopener"><span class="im"><img src="assets/gen-1009/%s.webp" alt="Сайт %s"></span>'
                '<b>%s</b><span class="tg">%s</span><span class="go">Открыть сайт ↗</span></a>'
                % (u, f, n, n, ''.join('<i>%s</i>' % t for t in tags)) for u, f, n, tags in SITES)
D['new-c356']['b'] = '<div class="s2n s2n-tpl">%s</div>' % cards
D['new-c356']['note'] += ' · 09.10 Мирослав: білі картки як у бібліотеці шаблонів, кожна відкриває живий сайт (пекарня, украшения, оптика, автосервис — список Влада)'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
