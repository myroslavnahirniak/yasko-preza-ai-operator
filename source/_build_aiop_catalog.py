#!/usr/bin/env python3
"""09.10 Мирослав: rest 162 — живий блок «пульт агентів» (7 AI-агентів + 1 в подарок) з сайту AI-Оператора
(holst-2809/sajt-src/ai-operator-sajt, живий ai-operator-agents.vercel.app) → assets/sites/aiop-catalog/index.html.
На сайті агенти перемикаються прокруткою (sticky); тут — кліком по пульту, без прокрутки. Квадратна розкладка:
пульт 4×2, текст агента угорі у дві колонки, демо нижче на всю ширину; база 1000px, zoom під ширину iframe. ?i=N — стартовий агент."""
import re, shutil
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT.parent / 'holst-2809' / 'sajt-src' / 'ai-operator-sajt'
OUT = ROOT / 'assets' / 'sites' / 'aiop-catalog'
t = (SRC / 'index.html').read_text(encoding='utf-8')
head = t[:t.find('</head>')]
css = ''.join(re.findall(r'<style[^>]*>(.*?)</style>', head, re.S))
fonts = ''.join(re.findall(r'<link[^>]+fonts\.googleapis[^>]+>', head))
i = t.find('<section class="naA" id="agents-v2"'); e = t.find('</section>', i) + len('</section>')
section = t[i:e]
# 09.10 Мирослав (rest 162): у агента AI-сайты замість стоматології — сайт прокату авто VIP CAR (як у кейсі Секрету 2 і на rest 161)
VIP = '../../gen-rest-1009/vip-car-poster.webp'
for a, b in (('https://svettutest.github.io/shablony-demo/stomatologia/', 'https://svettutest.github.io/shablony-demo/vip-car/'),
             ('<img class="naIfPo" src="media-v4/na/site-poster.webp"', '<img class="naIfPo" src="%s"' % VIP),
             ('comfort-dental · сайт, собранный агентом', 'vip-car · сайт, собранный агентом'),
             ('задача: сайт стоматологии с записью онлайн|собираю данные клиники с карт и отзывов|', 'задача: сайт проката авто с бронью онлайн|собираю данные автопарка и отзывы клиентов|')):
    assert section.count(a) == 1, a
    section = section.replace(a, b)
scripts = []
for m in re.finditer(r'<script>(.*?)</script>', t, re.S):
    s = m.group(1)
    if "getElementById('agents-v2')" in s or ".naD-live" in s:
        scripts.append(s)
# головний скрипт: замість прокрутки — клік по пульту
J = [k for k, s in enumerate(scripts) if 'function desk()' in s][0]
s = scripts[J]
R = [("function desk(){return innerWidth>900&&!RM}", "function desk(){return true}"),
     ("function activate(i){if(i===cur)return;cur=i;", "function activate(i){if(i===cur)return;cur=i;if(fill)fill.style.transform='scaleX('+((i+1)/N)+')';"),
     ("keys.forEach(function(b,k){b.addEventListener('click',function(){if(isDesk){var top=scr.getBoundingClientRect().top+scrollY,tot=scr.offsetHeight-innerHeight;scrollTo({top:top+tot*(k+.5)/N,behavior:RM?'auto':'smooth'})}else ags[k].scrollIntoView({behavior:'smooth',block:'start'})})});",
      "keys.forEach(function(b,k){b.addEventListener('click',function(){activate(k)})});")]
for a, b in R:
    assert s.count(a) == 1, a[:60]
    s = s.replace(a, b)
s = re.sub(r"function onScroll\(\)\{if\(!isDesk\)return;.*?activate\(Math\.min\(N-1,Math\.floor\(p\*N\*\.9999\)\)\)\}",
           "function onScroll(){if(cur<0)activate(START)}", s, flags=re.S)
assert 'activate(START)' in s
scripts[J] = "var START=+(new URLSearchParams(location.search).get('i')||0);" + s

if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir(parents=True)
refs = set(re.findall(r'(?:src|poster|data-src|data-prez)="((?:media-v4|video|img|demo|prez)/[^"#?]+)"', section))
for r in sorted(refs):
    top = r.split('/')[0]
    if top in ('demo', 'prez'):          # демо-папка цілком (index.html + свої ассети)
        d = SRC / '/'.join(r.split('/')[:2])
        if d.is_dir() and not (OUT / d.relative_to(SRC)).exists(): shutil.copytree(d, OUT / d.relative_to(SRC))
        continue
    p = SRC / r
    if p.exists():
        (OUT / r).parent.mkdir(parents=True, exist_ok=True); shutil.copy(p, OUT / r)
    else:
        print('нема', r)

SQ = """
html,body{margin:0;padding:0;background:transparent!important;overflow:hidden}
#sq{width:1000px;transform-origin:0 0}
#sq .naA{padding:26px 28px 28px;border-radius:28px;margin:0}
#sq .naA-head{display:none}
#sq .wrap{max-width:none!important;width:auto!important;padding:0!important;margin:0!important}
#sq .naA-scroll{height:auto!important;margin:0!important}
#sq .naA-sticky{position:static!important;height:auto!important;display:block!important}
#sq .naA-deck{padding:0!important}
#sq .naA-pult{grid-template-columns:repeat(4,minmax(0,1fr))!important}
#sq .naK .t{font-size:15px}
#sq .naA-stage{height:742px!important;margin-top:20px!important}
#sq .naAg{grid-template-columns:minmax(0,1fr)!important;grid-template-rows:auto minmax(0,1fr)!important;gap:18px!important}
#sq .naAg-t{display:grid!important;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);column-gap:30px;align-content:start}
#sq .naAg-t>.naAg-top{grid-column:1/-1;grid-row:1}
#sq .naAg-t>h3{grid-column:1/-1;grid-row:2;font-size:34px}
#sq .naAg-t>.naAg-do{grid-column:1;grid-row:3}
#sq .naAg-t>.naAg-bot{grid-column:2;grid-row:3;align-self:start;margin-top:16px}
#sq .naAg-t>.naAg-seg{display:none}
#sq .naD{height:100%!important}
#sq .naA-sum{display:none!important}
"""
html = f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>7 AI-агентов · пульт</title>{fonts}
<style>{css}</style><style>{SQ}</style></head><body>
<div id="sq">{section}</div>
{''.join('<script>%s</script>' % s for s in scripts)}
<script>(function(){{var b=document.getElementById('sq');function fit(){{b.style.zoom=innerWidth/1000}}fit();addEventListener('resize',fit);/* стрілки/пробіл з iframe — у деку */addEventListener('keydown',function(e){{if(parent===window)return;if(/^(ArrowLeft|ArrowRight|ArrowUp|ArrowDown|PageUp|PageDown|Home|End| )$/.test(e.key)){{try{{parent.document.dispatchEvent(new KeyboardEvent('keydown',{{key:e.key,bubbles:true,cancelable:true}}));e.preventDefault()}}catch(x){{}}}}}});}})();</script>
</body></html>'''
(OUT / 'index.html').write_text(html, encoding='utf-8')
print('ok', OUT, 'refs', len(refs), 'scripts', len(scripts))
