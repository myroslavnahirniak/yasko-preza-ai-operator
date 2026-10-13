#!/usr/bin/env python3
"""09.10 Мирослав: живий блок «На выходе пакета 01» з сайту потоку 4 (сайт-ai-маркетолог-поток4.zip) для rest 159/160.
Витягує з розпакованого сайту лише #pult-01 + його CSS/шрифти/картинки → assets/sites/aim-p4/index.html.
?i=0 — вкладка AI-сайты, ?i=1 — AI-маркетинг (автоперемикання вимкнено). Вміст масштабується під ширину iframe (zoom від 1440px).
usage: python3 source/_build_aim_p4_pult.py <розпакований>/aimarketolog-site"""
import re, sys, shutil
from pathlib import Path
SRC = Path(sys.argv[1])
OUT = Path(__file__).resolve().parent.parent / 'assets' / 'sites' / 'aim-p4'
t = (SRC / 'index.html').read_text(encoding='utf-8')
head = t[:t.find('</head>')]

def piece(start_pat, end_pat):
    a = t.find(start_pat); a = t.rfind('<div', 0, a)
    b = t.find(end_pat); b = t.rfind('<div', 0, b)
    return t[a:b]
pult = piece('id="pult-01"', 'id="pult-02"')
# 09.10: пакети 02 і 03 (rest 164/166) — окремі сторінки pult-02.html / pult-03.html
_a3 = t.rfind('<div', 0, t.find('id="pult-03"'))
PULTS = {'02': piece('id="pult-02"', 'id="pult-03"'), '03': t[_a3:t.find('</section>', _a3)]}
fonts_css = ''.join(re.findall(r'<style>(@font-face.*?)</style>', head, re.S))
links = re.findall(r'<link rel="stylesheet" href="/(_astro/[^"]+\.css)">', head)
# скрипти: live (iframe-сайт у блоці) і pult (вкладки)
scripts = [s for s in re.findall(r'<script type="module">(.*?)</script>', t, re.S) if '[data-live]' in s or '[data-pult]' in s]
scripts = [s.split('if(matchMedia("(max-width: 720px)")')[0] for s in scripts]
pult = re.sub(r'<script type="module">.*?</script>', '', pult, flags=re.S)
PULTS = {k: re.sub(r'<script type="module">.*?</script>', '', v, flags=re.S) for k, v in PULTS.items()}

def rel(s):
    s = s.replace('"/viz/', '"https://aimarketolog.site/viz/')
    return re.sub(r'(["(])/(assets|demos|fonts|_astro)/', r'\1\2/', s)
pult = rel(pult); fonts_css = rel(fonts_css)
PULTS = {k: rel(v) for k, v in PULTS.items()}
# 09.10 Мирослав (rest 161): у вкладці AI-сайты замість стоматології — сайт прокату авто VIP CAR (як у кейсі Секрету 2)
VIP = '../../gen-rest-1009/vip-car-poster.webp'
for a, b in (('https://svettutest.github.io/shablony-demo/stomatologia/', 'https://svettutest.github.io/shablony-demo/vip-car/'),
             ('--bg:url(assets/agents/site.webp)', '--bg:url(%s)' % VIP),
             ('<img class="live__poster" src="assets/agents/site.webp"', '<img class="live__poster" src="%s"' % VIP),
             ('aria-pressed="true" data-astro-cid-vwwuzmmn>Стоматология</button>', 'aria-pressed="true" data-astro-cid-vwwuzmmn>Прокат авто</button>')):
    assert pult.count(a) == 1, a
    pult = pult.replace(a, b)

# 12.10 Мирослав: у пакеті 01 AI-маркетинг першим, AI-сайты другим (номери 01/02 за новим порядком)
def _swap01(s):
    A = 'data-astro-cid-vwwuzmmn'
    def split_children(block_start, child_tag):
        i = s.index(block_start); j = s.index('>', i) + 1
        parts = []; pos = j
        for _ in range(2):
            a = s.index(child_tag, pos); depth = 0; k = a
            while True:
                o = s.find('<div', k + 1) if child_tag.startswith('<div') else -1
                c = s.find('</div>' if child_tag.startswith('<div') else '</button>', k + 1)
                if child_tag.startswith('<button'):
                    parts.append((a, c + len('</button>'))); pos = c + 9; break
                if o != -1 and o < c: depth += 1; k = o
                else:
                    if depth == 0: parts.append((a, c + 6)); pos = c + 6; break
                    depth -= 1; k = c
        return parts
    for start, tag in (('<div class="pult__line"', '<button'), ('<div class="pult__screen"', '<div class="pult__slide'), ('<div class="pult__captions"', '<div class="pult__cap')):
        (a1, b1), (a2, b2) = split_children(start, tag)
        x, y = s[a1:b1], s[a2:b2]
        def fix(z, newi, on):
            e = z.index('>') + 1; head, rest = z[:e], z[e:]   # лише перший тег (зовнішній)
            head = head.replace('data-i="%d"' % (1 - newi), 'data-i="%d"' % newi)
            head = head.replace(' is-on', '')
            if on: head = head.replace('class="', 'class="', 1).replace('pult__key"', 'pult__key is-on"').replace('class="pult__slide', 'class="pult__slide is-on', 1).replace('class="pult__cap"', 'class="pult__cap is-on"', 1)
            head = head.replace('aria-pressed="true"', 'aria-pressed="%s"' % ('true' if on else 'false')).replace('aria-pressed="false"', 'aria-pressed="%s"' % ('true' if on else 'false'))
            return head + rest
        nx, ny = fix(y, 0, True), fix(x, 1, False)
        if tag == '<button':
            nx = nx.replace('>02</span>', '>01</span>', 1); ny = ny.replace('>01</span>', '>02</span>', 1)
        s = s[:a1] + nx + s[b1:a2] + ny + s[b2:]
    return s
pult = _swap01(pult)
pult = pult.replace('>Агенты AI-сайты и AI-маркетинг</h3>', '>Агенты AI-маркетинг и AI-сайты</h3>', 1)
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir(parents=True)
need = set(re.findall(r'(?:src|poster|href|data-live)="((?:assets|demos)/[^"?#]+)"|url\(((?:assets|demos)/[^)]+)\)', pult + ''.join(PULTS.values())))
need = {a or b for a, b in need}
for r in sorted(need):
    p = SRC / r
    if p.is_dir():
        if not (OUT / r).exists(): shutil.copytree(p, OUT / r)
    elif p.exists():
        (OUT / r).parent.mkdir(parents=True, exist_ok=True); shutil.copy(p, OUT / r)
    else:
        print('нема', r)
(OUT / '_astro').mkdir()
for css in links:
    c = (SRC / css).read_text(encoding='utf-8')
    c = re.sub(r'url\(/(_astro|fonts|assets|frames)/', r'url(../\1/', c)
    (OUT / css).write_text(c, encoding='utf-8')
for f in (SRC / '_astro').glob('*.woff2'): shutil.copy(f, OUT / '_astro' / f.name)
shutil.copytree(SRC / 'fonts', OUT / 'fonts')
# у деці iframe ширший за блок (250% + scale .4), щоб медіа-запити сайту бачили десктоп ≥1440px; zoom вписує 1440 у ширину

def page(pult, pid, title):
    return f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · AI-Маркетолог</title>
<style>{fonts_css}</style>
{''.join('<link rel="stylesheet" href="%s">' % c for c in links)}
<style>
html,body{{margin:0;padding:0;background:transparent!important;overflow:hidden}}
#pp{{width:1440px;transform-origin:0 0}}
#pp #modules{{padding:0!important;background:transparent!important}}
#pp .container{{max-width:none!important;padding:0!important;margin:0!important}}
#pp .pult{{margin:0!important}}
#pp .mp-pack{{display:none!important}}
/* 12.10 Мирослав: «Кто уже так зарабатывает» / кейси учнів прибрано всюди */
#pp .pult__more,#pp .pult__case{{display:none!important}}
/* 09.10 квадрат (?sq=1): база 960px, екран над описом, опис у дві колонки — для квадратного слайда */
#pp.sq{{width:960px}}
#pp.sq .pult__body{{grid-template-columns:1fr!important}}
#pp.sq .pult__screen{{aspect-ratio:16/7.6}}
#pp.sq .pult__cap.is-on{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:14px 26px;align-items:start}}
#pp.sq .pult__cap .pult__top{{grid-column:1/-1}}
#pp.sq .pult__cap .pult__how,#pp.sq .pult__cap .pult__does{{grid-column:1}}
#pp.sq .pult__cap .pult__two{{grid-column:2;grid-row:2 / span 2}}
#pp.sq .pult__cap .pult__more{{grid-column:1/-1}}
/* 12.10 Мирослав: у слайдах пакетів без назви агента, «Как работает агент» і пунктів — лишаються ціна, «Бизнесу», «Заработок»; усе крупніше */
#pp.sq .pult__name,#pp.sq .pult__how,#pp.sq .pult__does{{display:none!important}}
#pp.sq .pult__top:not(:has(.pult__price)){{display:none!important}}
#pp.sq .pult__screen{{aspect-ratio:16/8.6}}
#pp.sq .pult__title{{font-size:34px!important}}
#pp.sq .pult__k{{font-size:13px!important}}
#pp.sq .pult__key{{min-height:62px!important;font-size:18px!important}}
#pp.sq .pult__num{{font-size:18px!important}}
#pp.sq .pult__cap.is-on{{display:grid!important;grid-template-columns:minmax(0,1fr) minmax(0,1fr)!important;gap:14px 16px!important;align-items:stretch!important}}
#pp.sq .pult__cap .pult__top{{grid-column:1/-1!important;margin:0!important;justify-content:flex-start!important}}
#pp.sq .pult__price{{font-size:17px!important;gap:10px!important}}
#pp.sq .pult__price span{{font-size:13px!important}}
#pp.sq .pult__price b{{font-size:34px!important}}
#pp.sq .pult__cap .pult__two{{display:contents!important}}
#pp.sq .pult__path{{padding:16px 20px!important;border-radius:16px!important}}
#pp.sq .pult__path .k{{font-size:13px!important;margin-bottom:8px!important}}
#pp.sq .pult__path p{{font-size:20px!important;line-height:1.4!important;color:#f4efe7!important}}
</style><link rel="stylesheet" href="modes.css?v=1"></head><body>
<div id="pp"><section class="pad-y" id="modules" data-astro-cid-vwwuzmmn><div class="container container--wide" data-astro-cid-vwwuzmmn>{pult}</div></section></div>
{''.join('<script type="module">%s</script>' % s for s in scripts)}
<script>
(function(){{
  var pp=document.getElementById('pp'), q=new URLSearchParams(location.search), base=1440;
  if(q.get('sq')){{pp.classList.add('sq');base=960;}}
  function fit(){{var k=innerWidth/base;pp.style.zoom=k;}}
  fit(); addEventListener('resize',fit);
  var i=+(new URLSearchParams(location.search).get('i')||0);
  // pult:open вимикає автоперемикання і ставить потрібну вкладку
  function pick(){{document.dispatchEvent(new CustomEvent('pult:open',{{detail:{{pult:'{pid}',i:i}}}}));scrollTo(0,0);}}
  // module-скрипти виконуються до DOMContentLoaded — тоді слухач pult:open уже є
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',pick); else pick();
  addEventListener('load',pick);
  // стрілки/пробіл з iframe — у деку
  addEventListener('keydown',function(e){{if(parent===window)return;if(/^(ArrowLeft|ArrowRight|ArrowUp|ArrowDown|PageUp|PageDown|Home|End| )$/.test(e.key)){{try{{parent.document.dispatchEvent(new KeyboardEvent('keydown',{{key:e.key,bubbles:true,cancelable:true}}));e.preventDefault()}}catch(x){{}}}}}});
}})();
</script>
<script src="modes.js?v=1"></script>
</body></html>'''
for _f in ('modes.css', 'modes.js'): shutil.copy(Path(__file__).resolve().parent / 'aim-p4-modes' / _f, OUT / _f)
(OUT / 'index.html').write_text(page(pult, '01', 'На выходе пакета 01'), encoding='utf-8')
for k, v in PULTS.items():
    (OUT / ('pult-%s.html' % k)).write_text(page(v, k, 'На выходе пакета ' + k), encoding='utf-8')
print('ok', OUT, 'refs:', len(need), 'scripts:', len(scripts))
