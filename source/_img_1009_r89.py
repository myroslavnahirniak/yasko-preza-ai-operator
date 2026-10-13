#!/usr/bin/env python3
"""09.10 · rest 89 (G357 «Пустой шаблон и готовый сайт»): праве вікно — новий сайт VIP CAR (кейс прокату авто) замість fainopet (грумінг).
Скрин сайту — headless Chrome 1080×890 (пропорція вмісту вікна), вставка рівно у вікно, адреса в рядку браузера замінена."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
ROOT = Path(__file__).resolve().parents[1]
base = Image.open(ROOT / 'assets/secret2-full/s241-empty.webp').convert('RGB')
X0, Y0, X1, Y1 = 656, 398, 1196, 843                      # вміст правого вікна
site = Image.open(ROOT / 'assets/gen-s2-1009/_vipcar-after-1080.png').convert('RGB').resize((X1 - X0, Y1 - Y0), Image.LANCZOS)
m = Image.new('L', site.size, 255); d = ImageDraw.Draw(m)
r = 12; w, h = site.size                                  # заокруглені нижні кути, як у рамки вікна
d.rectangle((0, h - r, r, h), fill=0); d.rectangle((w - r, h - r, w, h), fill=0)
d.pieslice((0, h - 2 * r, 2 * r, h), 90, 180, fill=255); d.pieslice((w - 2 * r, h - 2 * r, w, h), 0, 90, fill=255)
base.paste(site, (X0, Y0), m)
d = ImageDraw.Draw(base)
d.rectangle((748, 360, 1190, 390), fill=(21, 21, 19))     # стара адреса fainopet.vercel.app
try: f = ImageFont.truetype(str(ROOT / 'assets/fonts/Manrope-500-latin.woff2'), 21)
except Exception: f = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', 20)
d.text((755, 362), 'svettutest.github.io/…/vip-car', font=f, fill=(205, 203, 198))
out = ROOT / 'assets/gen-s2-1009/r089-empty-vipcar.webp'; base.save(out, quality=90, method=6); print(out, base.size)
