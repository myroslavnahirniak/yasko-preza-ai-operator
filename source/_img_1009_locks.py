#!/usr/bin/env python3
"""09.10 · rest 84/85 — «замочек» за ТЗ Влада (G352): список ніш і локацій закритий.
rest 84: нова таблиця ніш (~/Desktop/cities.png) — видно шапку і 2 перші ніші, решта розмита.
rest 85: «Города и районы» (фото 2 від Мирослава) — чітко лише шапка, заголовок графіка, рядок «Киев» і фільтри, решта розмита.
Розмиття як у .s2n-reveal: blur + brightness .5 + saturate .6. → assets/gen-s2-1009/r084-niches-lock.webp, r085-cities-kyiv.webp"""
import sys
from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/gen-s2-1009'; OUT.mkdir(exist_ok=True)
BG = (11, 9, 7)

def locked(im, keep, radius, feather=6, bright=0.5, sat=0.6):
    """keep — список прямокутників (x0,y0,x1,y1) у пікселях, що лишаються чіткими."""
    bl = im.filter(ImageFilter.GaussianBlur(radius))
    bl = ImageEnhance.Color(bl).enhance(sat); bl = ImageEnhance.Brightness(bl).enhance(bright)
    m = Image.new('L', im.size, 0); d = ImageDraw.Draw(m)
    for r in keep: d.rectangle(r, fill=255)
    m = m.filter(ImageFilter.GaussianBlur(feather))
    return Image.composite(im, bl, m)

def flat(p):
    im = Image.open(p)
    if im.mode == 'RGBA':
        bg = Image.new('RGB', im.size, BG); bg.paste(im, mask=im.split()[3]); return bg
    return im.convert('RGB')

# rest 84 · ніші (09.10, 2-га правка Мирослава): розмиття легке — видно, що там текст, але не читається;
# чіткі шапка, 3-тя і 7-ма ніші; 1-ша, 2-га та решта — під розмиттям. Межі рядків: 313/453/592/731/870/1009/1149/1288/1427/1566
a = flat(Path.home() / 'Desktop/cities.png').crop((340, 0, 2600, 1712))
W, H = a.size
a = locked(a, [(0, 0, W, 313), (0, 592, W, 731), (0, 1149, W, 1288)], radius=9, feather=3, bright=0.62, sat=0.7)
a.save(OUT / 'r084-niches-lock-v2.webp', quality=88, method=6); print('r084', a.size)

# rest 85 · міста: чітко шапка, заголовок графіка, «Киев», фільтри
src = sys.argv[1] if len(sys.argv) > 1 else None
if src:
    b = flat(src).crop((236, 0, 1764, 1196))
    keep = [(0, 0, 1528, 238),          # Скоринг мест · Города и районы · опис
            (20, 282, 1508, 372),       # Сколько карточек без своего сайта + підзаголовок
            (24, 622, 1504, 663),       # рядок «Киев»
            (8, 938, 744, 996)]         # Все · Англоязычные рынки · Свои за рубежом · Домашние и Азия
    b = locked(b, keep, radius=6, feather=3, bright=0.62, sat=0.7)  # 09.10: легше розмиття — видно, що там щось є
    b.save(OUT / 'r085-cities-kyiv-v2.webp', quality=88, method=6); print('r085', b.size)

# rest 86 · картки міст (09.10, Мирослав): легке розмиття; чітко лише фільтри і шапка першої картки (назва, бал, ринок, райони).
# Текст першої картки (абзац, Ниши/Чек/Язык, Риск) і дві інші картки — під розмиттям. Вебкамера Влада в правому верхньому куті — затерта.
src_exec = (Path(__file__).parent / '_img_patch_1008.py').read_text(encoding='utf-8')
_ns = {'__file__': str(Path(__file__).parent / '_img_patch_1008.py')}; exec(compile(src_exec[:src_exec.index('# G331')], '_img_patch_1008.py', 'exec'), _ns)
c = Image.open(ROOT / 'assets/google-1008call/cities-cards.webp').convert('RGB')
c = _ns['erase'](c, (1612 / 1800, 0, 1, 236 / 989), mode='box')
c = locked(c, [(0, 0, 890, 84), (72, 96, 612, 382)], radius=6, feather=3, bright=0.62, sat=0.7)
c.save(OUT / 'r086-cities-cards-v2.webp', quality=88, method=6); print('r086', c.size)
