#!/usr/bin/env python3
"""09.10 Мирослав:
— rest 153 (new-c428): варіант В з design-r153-options.html, але замість Влада — згенерована картинка
  (GPT Image 2.5: платформа, від партнерів до неї золоті нитки, промінь угору) assets/gen-rest-1009/r153/platform-partners.webp;
— rest 159/160 (new-c434/435): замість скрінів — живий блок «На выходе пакета 01» з сайту потоку 4
  (assets/sites/aim-p4/, збирає source/_build_aim_p4_pult.py): 159 — вкладка AI-маркетинг, 160 — AI-сайты."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1009-before-r153-r159-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
S = o['__deckOrder']['slides']
S['new-c428']['b'] = (
    '<div class="s2n s2n-r153"><div class="r153-photo"><img src="assets/gen-rest-1009/r153/platform-partners.webp" '
    'alt="Платформа, к которой от партнёров тянутся золотые нити"></div>'
    '<div class="r153-h">И за это вы мне будете платить<br><em>до 5% от этой выручки</em> в месяц<br>на мою платформу</div>'
    '<div class="r153-goal"><p>Моя глобальная цель — зарабатывать</p><b>$15 000</b><span>в месяц,</span><p>помогая своим партнёрам</p></div>'
    '<p class="r153-end">Теперь вы понимаете, для чего я провожу этот мастер-класс</p></div>')
S['new-c428']['note'] = S['new-c428'].get('note', '') + '\n09.10 Мирослав: варіант В (картка цілі + згенерована платформа з партнерами).'
for k, i, nm in (('new-c434', 1, 'AI-маркетинг'), ('new-c435', 0, 'AI-сайты')):
    S[k]['b'] = ('<div class="s2n s2n-block"><iframe data-src="assets/sites/aim-p4/index.html?i=%d" '
                 'title="На выходе пакета 01 — агенты AI-сайты и AI-маркетинг (вкладка %s)" loading="lazy"></iframe></div>') % (i, nm)
    S[k]['note'] = S[k].get('note', '') + '\n09.10 Мирослав: живий блок з сайту потоку 4 замість скріна (вкладка %s).' % nm
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
