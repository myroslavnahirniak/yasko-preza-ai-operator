#!/usr/bin/env python3
"""13.10 Мирослав: прибрати rest 219 (стара картка AI-сайты), 223 «Вот что собирает», 227 «Юра», 230 повтор «Охотника», 231 «Три агента», 255 «Ваше лицо работает без вас»;
артефакти «Что делает агент» — одразу живе демо без кроку-списку; rest 239 відео Жені — кнопка звуку; rest 250 Света — скрін з кружечками (Google G115)."""
import json, shutil, time
from pathlib import Path
R = Path(__file__).resolve().parent.parent
OV = R / 'source/overrides.json'
o = json.load(open(OV)); do = o['__deckOrder']; V = o['__visibleGoogleAudit']['slides']
shutil.copy(OV, R / f'source/_bak/overrides-1013-before-cleanup-{int(time.time())}.json')
S = 'g3f9b3adf0b8_0_2226'; A = 'g3f9b3adf0b8_0_2921'
for k in (f'{S}#67', f'{S}#59', f'{S}#64', 'new-x226hunt', f'{S}#73', f'{S}#92'):
    if k not in do['drop']: do['drop'].append(k)
P = {S: V[S]['presentationParts']['slides'], A: V[A]['presentationParts']['slides']}
for oid, n in ((S, 68), (A, 7), (A, 18), (A, 26), (A, 31)):
    p = P[oid][n - 1]; b = p['b']
    i = b.find('<div class="s16-step"', 10)
    if b.startswith('<div class="s16-step"') and i > 0 and 's16-demo' in b[i:]:
        p['b'] = b[i:]
    p['foundation']['block129']['steps'] = ['Живое демо агента']
    p['note'] = ((p.get('note') or '') + '\n13.10 Мирослав: одразу артефакт, без кроку-списку.').strip()
z = P[A][18]
if 'snd-btn' not in z['b']:
    z['b'] = z['b'].replace('</video></div>', '</video><button type="button" class="snd-btn" aria-label="Выключить звук"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9z"/><path class="w" d="M16.5 8.5a5 5 0 0 1 0 7M19 6a8.5 8.5 0 0 1 0 12"/><path class="x" d="M16 9l5 6M21 9l-5 6"/></svg></button></div>', 1)
sv = V['g409d4d20be6_0_198']['set']
if 'r250-circ' not in sv['b']:
    sv['b'] = sv['b'].replace('</figure>', '</figure><div class="r250-circ" style="background-image:url(assets/gen-rest-1012/s7/sveta-circles.webp)"></div>', 1)
OV.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
