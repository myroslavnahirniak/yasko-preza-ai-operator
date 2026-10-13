#!/usr/bin/env python3
"""10.10 Мирослав: тарифи (2226 #42–#44) — варіант A «Сходи» з design-r194-options.html: три набори поруч, поточний підсвічений,
+ живіший фон: картинка набору на весь слайд (приглушена), золоте світло за активною колонкою."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1010-before-tiersA-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
p = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2226']['presentationParts']['slides']
MODS = ['Фундамент', 'Маркетинг и сайты', 'Контент-завод', 'Привлечение клиентов', 'Продажи и связки']
T = [dict(n='Bronze', p='$490', m=2, a=['AI-сайты'], img='assets/gen-tarif/bronze.webp',
          lead='Разобраться руками, собрать первый сайт и найти первого клиента среди знакомых'),
     dict(n='Silver', p='$749', m=3, a=['AI-сайты', 'AI-дизайн', 'AI-видео', 'Контент-завод'], img='assets/gen-sales3/content-factory.png',
          lead='Четыре услуги в прайсе и контент-завод с вашим двойником — услуга с оплатой каждый месяц'),
     dict(n='Gold', p='$1.500', m=5, a=['AI-сайты', 'AI-дизайн', 'AI-видео', 'Контент-завод', 'AI-таргет', 'AI-SEO', 'AI-продавец', 'страт-сессии'],
          img='assets/gen-s120-team/workforce.png',
          lead='Реклама приводит клиентов, агент закрывает сделку, а ваш проект мы разбираем на страт-сессиях')]
def body(s):
    x = T[s]
    cols = ''.join(
        '<div class="tA-col%s%s" style="--i:%d"><span class="nm">%s</span><span class="pr">%s</span>'
        '<span class="lb">блоки</span><div class="ls">%s</div><span class="lb">агенты</span><div class="ls ag">%s</div></div>' % (
            ' on' if k == s else '', ' past' if k < s else '', k, y['n'], y['p'],
            ''.join('<span>%s</span>' % m for m in MODS[:y['m']]), ''.join('<span>%s</span>' % a for a in y['a']))
        for k, y in enumerate(T))
    return ('<div class="sales-v6 tA tA-%d"><img class="tA-bg" src="%s" alt="" aria-hidden="true"><i class="tA-shade"></i><i class="tA-glow"></i>'
            '<div class="tA-pill">Набор «%s» · %s</div><p class="tA-lead">%s</p><div class="tA-row">%s</div>'
            '<div class="tA-disc">результаты индивидуальны</div></div>') % (s, x['img'], x['n'], x['p'], x['lead'], cols)
for s, i in enumerate((41, 42, 43)):
    assert 'tier-scene' in p[i]['b'] and T[s]['n'] in p[i]['t'], (i, p[i]['t'])
    p[i]['b'] = body(s)
    p[i]['note'] = (p[i].get('note') or '') + '\n10.10 Мирослав: варіант A «Сходи» (три набори поруч, поточний підсвічений) + картинка набору фоном.'
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
