#!/usr/bin/env python3
"""08.10 Мирослав: картки послуг каталогу (УСЛУГА 0N / 07, layout s16-catalog-orbit) — SVG-ілюстрації замінити реальними
матеріалами послуги; низ спростити (CSS: без смуги вкладок). Копії rest 19/28/30/35/41 + каталоги rest 145/146 (2226#15/#16)."""
import json, re, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-catalog-media-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8')); V = o['__visibleGoogleAudit']['slides']
M = {  # послуга → [(src, клас, alt)]
    '01': [('assets/google-1008/g254-zarmilkas-phone.webp', 'phone', 'Сайт ZARMILKAS на телефоне')],
    '02': [('assets/vlad-1409/dizayn/kp-hero.webp', 'h', 'Коммерческое предложение «Александр, вот как мы вырастим ваш бренд»'),
           ('assets/vlad-1409/dizayn/kp-1.webp', 'h', 'Страница КП «Точка А»')],
    '03': [('assets/google-source/2026-09-16/g203-image151.png', 'v', 'AI-ролик для товара'),
           ('assets/video/instagram/g205-poster-5s.jpg', 'v', 'AI-ролик для одежды')],
    '04': [('assets/s202-avatar/poster-1.jpg', 'v', 'Ролик с AI-аватаром'),
           ('assets/s202-avatar/poster-2.jpg', 'v', 'Ролик с AI-аватаром')],
    '05': [('assets/vlad-1409/dizayn/reels-1.webp', 'v', 'Рекламный креатив «Тебе не нужен дизайнер»'),
           ('assets/vlad-1409/dizayn/reels-2.webp', 'v', 'Рекламный креатив «Смотри, что сделал AI»')],
    '06': [('assets/google-1001/src/g304-image298.jpg', 'h', 'Нейросеть советует салон на карте')],
    '07': [('assets/video/avatar-consultant-poster.jpg', 'v', 'Видеоконсультант онлайн'),
           ('assets/video/seller-voice-poster.jpg', 'v', 'AI-продавец в переписке')],
}
def media(n):
    items = M[n]; stack = ' co-stack' if all(c == 'h' for _, c, _ in items) and len(items) > 1 else ''
    return '<div class="co-product-scene co-media co-m%s%s">%s</div>' % (n, stack, ''.join(
        '<img class="%s" src="%s" alt="%s">' % (c, s, a) for s, c, a in items))
def fix(html):
    out, pos, n_done = [], 0, 0
    for m in re.finditer(r'<div class="co-product-scene">', html):
        i = m.start(); j = html.index('</svg>', i) + len('</svg>')
        v = re.match(r'<img class="co-vlad"[^>]*>', html[j:]); j += v.end() if v else 0
        assert html.startswith('</div>', j), html[j:j + 80]
        j += len('</div>')
        num = re.findall(r'УСЛУГА (\d\d) / 07', html[:i])[-1]
        out.append(html[pos:i] + media(num)); pos = j; n_done += 1
    return ''.join(out) + html[pos:], n_done
total = 0
for cid in ('copy-g254', 'copy-g266', 'copy-g273', 'copy-g287', 'copy-g293'):
    x = V[cid]; x['set']['b'], n = fix(x['set']['b']); total += n
    x['reason'] += ' · 08.10 Мирослав: SVG → реальні матеріали послуги'
parts = V['g3f9b3adf0b8_0_2226']['presentationParts']['slides']
for i in (14, 15):
    parts[i]['b'], n = fix(parts[i]['b']); total += n
print('замінено сцен:', total)
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
