#!/usr/bin/env python3
"""08.10 Мирослав:
rest 25 (2921 частина 3) — плитка 04 «реклама в соц сетях (AI-таргет)»: замість генерації ads-agent — реальний дашборд кабінету gen-2430/r-ads.webp;
rest 28 (copy-g266) — підзаголовок під «AI-дизайн»: що саме робить;
rest 30 (copy-g273) — замість постерів два ролики з автозапуском (додаткові відео стартують лише з autoplay loop у розмітці)."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1008-before-r25-r28-r30-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8')); V = o['__visibleGoogleAudit']['slides']
def rep(node, key, old, new, why):
    s = node[key] if key in node else node['set'][key]
    assert s.count(old) == 1, (why, old[:60]); s = s.replace(old, new)
    if key in node: node[key] = s
    else: node['set'][key] = s
    node['reason'] = (node.get('reason') or '') + ' · 08.10 Мирослав: ' + why
p25 = V['g3f9b3adf0b8_0_2921']['presentationParts']['slides'][2]
rep(p25, 'b', '<img src="assets/holst-media/ads-agent.webp" alt="Агент-рекламщик: креативы и запуск рекламы">',
    '<img src="assets/gen-2430/r-ads.webp" alt="Кабинет рекламы: расходы, покупки, показы, клики по креативам">',
    'плитка 04 — реальний дашборд реклами замість генерації')
rep(V['copy-g266'], 'b', '<h2 class="co-service-title">AI-дизайн</h2></div>',
    '<h2 class="co-service-title">AI-дизайн</h2><p class="co-service-sub">Презентации, коммерческие предложения, баннеры, афиши и т. д.</p></div>',
    'підзаголовок «Презентации, коммерческие предложения, баннеры, афиши и т. д.»')
rep(V['copy-g273'], 'b',
    '<img class="v" src="assets/google-source/2026-09-16/g203-image151.png" alt="AI-ролик для товара"><img class="v" src="assets/video/instagram/g205-poster-5s.jpg" alt="AI-ролик для одежды">',
    '<video class="v" src="assets/video/instagram/g203-DdMC9KlNLw1.mp4" poster="assets/google-source/2026-09-16/g203-image151.png" autoplay muted loop playsinline aria-label="AI-ролик для товара"></video>'
    '<video class="v" src="assets/video/instagram/g205-DcI63cOTcbd.mp4" poster="assets/video/instagram/g205-poster-5s.jpg" autoplay muted loop playsinline aria-label="AI-ролик для одежды"></video>',
    'ролики з автозапуском замість постерів')
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
