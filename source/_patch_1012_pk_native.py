#!/usr/bin/env python3
"""12.10 Мирослав: блоки «На выходе пакета 01/02/03» (rest 160/164/167) — не iframe сайту, а власна верстка під квадрат:
вкладки агентів великими пігулками, на екрані один агент: медіа на всю ширину, назва + ціна, 3 короткі пункти, «Заработок» одним рядком.
Дані — source/aim-p4-modes/packs.json (витягнуто з сайту потоку 4). Перемикання — js/pk-tabs.js."""
import json, shutil, time, html
from pathlib import Path
ROOT = Path(__file__).resolve().parent
P = ROOT / 'overrides.json'
shutil.copy(P, ROOT / '_bak' / ('overrides-1012-before-pk-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
packs = json.loads((ROOT / 'aim-p4-modes' / 'packs.json').read_text(encoding='utf-8'))
def media_path(s):
    if not s: return ''
    if s.startswith('../../'): return 'assets/' + s[6:]
    return 'assets/sites/aim-p4/' + s
def body(pid):
    pk = packs[pid]; ag = pk['agents']
    tabs = ''.join('<button type="button" class="pk-tab%s" data-i="%d"><i>%s</i>%s</button>' % (' on' if n == 0 else '', n, a['num'], a['nm']) for n, a in enumerate(ag))
    panes = []
    for n, a in enumerate(ag):
        if a.get('video'):
            m = '<video data-s3-final src="%s" poster="%s" muted loop playsinline preload="%s"></video>' % (media_path(a['video']), media_path(a.get('poster') or a.get('img')), 'auto' if n == 0 else 'none')
        else:
            m = '<img src="%s" alt="%s">' % (media_path(a['img']), html.escape(a['nm']))
        price = ('<span class="pk-pr"><b>%s</b> %s</span>' % (a['price'], a['unit'])) if a.get('price') else ''
        does = ''.join('<li>%s</li>' % d for d in a['does'][:3])
        earn = ('<p class="pk-earn"><span>Заработок</span>%s</p>' % a['earn']) if a.get('earn') else ''
        panes.append('<div class="pk-ag%s" data-i="%d"><div class="pk-media">%s</div><div class="pk-hd"><span class="pk-nm">%s</span>%s</div><ul class="pk-do">%s</ul>%s</div>' % (
            ' on' if n == 0 else '', n, m, a['nm'], price, does, earn))
    return ('<div class="pk"><div class="pk-top"><span class="pk-k">%s</span><span class="pk-t">%s</span></div><div class="pk-tabs n%d">%s</div>%s</div>'
            % (pk['k'], pk['title'], len(ag), tabs, ''.join(panes)))
S = o['__deckOrder']['slides']
for nid, pid in (('new-c435', '01'), ('new-x163p2', '02'), ('new-x164p3', '03')):
    S[nid]['b'] = body(pid)
    S[nid]['note'] = (S[nid].get('note') or '') + '\n12.10 Мирослав: власна верстка пакета %s (один агент на екран, великий шрифт), замість iframe сайту.' % pid
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
