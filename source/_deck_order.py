#!/usr/bin/env python3
"""Порядок деки за Google-ревізією. Викликається з _foundation_prepare.py перед записом __google180.

overrides['__deckOrder'] = {source, entries:[...], hide:[key,...], slides:{id: slide}}
  key = "<googleObjectId>#<presentationPart або 0>" — стабільний ключ нашого екрана.
  entry:
    "key"                                  — екран як є
    {"key": k, "route": [a, b]}            — екран маршруту (reality-route), лише пункти a..b
    {"copy": k, "id": "copy-g004"}         — копія екрана з власним id (правиться окремо)
    {"new": "new-g013"}                    — новий слайд із __deckOrder.slides[id]
Невказані й неприховані екрани стають одразу після свого попереднього сусіда з вихідного порядку,
тож нові частини, додані пізніше через patch-скрипти, не губляться.
Правки копій і нових слайдів — через _edit.py N (patch лягає в __visibleGoogleAudit.slides[id]).
"""
import copy


def key(s):
    return f"{s.get('googleObjectId')}#{s.get('presentationPart') or 0}"


def _patch(s, p):
    if not p:
        return s
    for k in p.get('remove', []):
        s.pop(k, None)
    for k, v in p.get('set', {}).items():
        s[k] = copy.deepcopy(v)
    if 'foundation' in p:
        f = s.setdefault('foundation', {})
        for k, v in p['foundation'].items():
            if v is None:
                f.pop(k, None)
            elif k == 'block129' and isinstance(v, dict) and isinstance(f.get(k), dict):
                # як _edit.py --b129: зливаємо ключі, None прибирає ключ
                for bk, bv in v.items():
                    if bv is None:
                        f[k].pop(bk, None)
                    else:
                        f[k][bk] = copy.deepcopy(bv)
            else:
                f[k] = copy.deepcopy(v)
    return s


def apply(G, spec, patches):
    by = {key(s): s for s in G}
    hide = set(spec.get('hide', []))
    drop = set(spec.get('drop', []))   # 05.10: прибрати екран із порядку, але лишити джерелом для копій (ключ, id копії або id нового)
    out, placed = [], set()
    for e in spec['entries']:
        if isinstance(e, str):
            e = {'key': e}
        eid = e.get('key') or e.get('id') or e.get('new')
        if eid in drop:
            if 'key' in e:
                placed.add(e['key'])
            continue
        if 'key' in e:
            s = by.get(e['key'])
            if s is None:
                print('!! deckOrder: нема екрана', e['key'])
                continue
            if e.get('route'):
                s = copy.deepcopy(s)
                s['routeRoadmap']['range'] = e['route']
            elif e['key'] in placed:
                print('!! deckOrder: екран двічі без копії', e['key'])
                continue
            placed.add(e['key'])
        elif 'copy' in e:
            src = by.get(e['copy'])
            if src is None:
                print('!! deckOrder: нема джерела копії', e['copy'])
                continue
            s = copy.deepcopy(src)
            s.pop('displayNumber', None)
            s.update(googleObjectId=e['id'], copyOf=e['copy'])
            if out:
                s['a'] = out[-1].get('a', s.get('a'))   # копія з іншого акту бере акт сусідів (HUD «АКТ N»)
            s['note'] = (s.get('note') or '') + '\nКопія екрана ' + e['copy']
            _patch(s, patches.get(e['id']))
        else:
            s = copy.deepcopy(spec['slides'][e['new']])
            s['googleObjectId'] = e['new']
            p = patches.get(e['new'])
            if p and p.get('omit'):
                continue
            _patch(s, p)
        if out:
            s.setdefault('a', out[-1].get('a', 0))
            s.setdefault('lv', out[-1].get('lv', 6))
        out.append(s)
    # Unlisted screens follow their original predecessor (its last placed copy for split route screens).
    prev = None
    for s in G:
        k = key(s)
        if k in placed or k in hide:
            prev = k if k in placed else prev
            continue
        pos = max((i for i, x in enumerate(out) if key(x) == prev), default=-1) if prev else -1
        out.insert(pos + 1, s)
        print('deckOrder: невказаний екран', k, 'після', prev or 'початку')
        prev = k
    for i, s in enumerate(out, 1):
        if 'displayNumber' in s:
            s['displayNumber'] = i
    return out
