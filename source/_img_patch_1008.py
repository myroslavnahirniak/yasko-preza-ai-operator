#!/usr/bin/env python3
"""08.10 дзвінок з Владом, Секрет 2: прибрати вшитий у постери текст так, як Влад підрізав кадри в Google (G331–G384).
Заливка — інтерполяція з меж прямокутника (Coons-патч) + легкий шум, щоб на темному градієнті не було плями.
mode 'text' — зафарбовуються лише світлі пікселі (текст) з розширенням, решта кадру (плече, телефон) лишається.
Вихід — assets/gen-s2-1008/*.webp (оригінали не чіпаємо)."""
import numpy as np
from pathlib import Path
from PIL import Image, ImageFilter, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/gen-s2-1008'
OUT.mkdir(exist_ok=True)
FONT = Path.home() / 'Library/Fonts'


def _fill(a, K):
    """Push-pull: заповнює невідоме (K=0) згладженим фоном із відомих пікселів (K=1), будь-якого розміру діри."""
    H, W = K.shape
    n = 1
    while n < max(H, W):
        n *= 2
    c = np.zeros((n, n, 3)); w = np.zeros((n, n))
    c[:H, :W] = a * K[..., None]; w[:H, :W] = K
    pyr = [(c, w)]
    while pyr[-1][1].shape[0] > 1:
        c, w = pyr[-1]; m = c.shape[0] // 2
        pyr.append((c.reshape(m, 2, m, 2, 3).sum((1, 3)), w.reshape(m, 2, m, 2).sum((1, 3))))
    c, w = pyr[-1]
    v = c / np.maximum(w, 1e-6)[..., None]
    for c, w in reversed(pyr[:-1]):
        up = np.repeat(np.repeat(v, 2, 0), 2, 1)
        # трохи згладити блоки від repeat
        up = (up + np.roll(up, 1, 0) + np.roll(up, -1, 0) + np.roll(up, 1, 1) + np.roll(up, -1, 1)) / 5
        al = np.minimum(w, 1.0)[..., None]
        v = al * (c / np.maximum(w, 1e-6)[..., None]) + (1 - al) * up
    return v[:H, :W]


def erase(im, box, mode='box', thr=60, grow=6, known_thr=70):
    """box у частках кадру. mode 'text' — міняємо лише світлі пікселі (текст) з розширенням, 'box' — увесь прямокутник.
    Фон — push-pull із темних пікселів довкола (світлі, тобто текст і об'єкти, у зразок не беруться)."""
    a = np.asarray(im.convert('RGB')).astype(float)
    H, W = a.shape[:2]
    x0, y0, x1, y1 = int(box[0] * W), int(box[1] * H), int(box[2] * W), int(box[3] * H)
    lum = a @ [0.299, 0.587, 0.114]
    R = np.zeros((H, W), bool); R[y0:y1, x0:x1] = True
    if mode == 'box':
        M = R.astype(float)
    else:
        t = ((lum > thr) & R).astype(np.uint8) * 255
        M = np.asarray(Image.fromarray(t).filter(ImageFilter.MaxFilter(grow * 2 + 1))).astype(float) / 255
        M *= R
    lumb = np.asarray(Image.fromarray(lum.astype(np.uint8)).filter(ImageFilter.MaxFilter(9))).astype(float)
    K = ((M < 0.5) & (lumb < known_thr)).astype(float)
    est = _fill(a, K)
    est += np.random.default_rng(7).normal(0, 1.0, est.shape)
    Ms = np.asarray(Image.fromarray((M * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2))).astype(float) / 255
    out = a * (1 - Ms[..., None]) + est * Ms[..., None]
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))


def shift_up(im, frac):
    """Зсув кадру вгору на frac висоти; низ добудовується тим самим фоном (push-pull)."""
    a = np.asarray(im.convert('RGB')).astype(float); H = a.shape[0]; d = int(frac * H)
    b = np.zeros_like(a); b[:H - d] = a[d:]
    K = np.ones(a.shape[:2]); K[H - d:] = 0
    est = _fill(b, K); b[H - d:] = est[H - d:]
    return Image.fromarray(np.clip(b, 0, 255).astype(np.uint8))


def text(im, xy, lines, size, font='Unbounded-Bold.ttf', anchor='la', spacing=1.12):
    """lines: [[(текст, колір), …], …] — рядки з кольоровими шматками."""
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(str(FONT / font), size)
    x, y = xy
    for line in lines:
        w = sum(d.textlength(t, font=f) for t, _ in line)
        cx = x - w / 2 if anchor == 'ma' else x
        for t, col in line:
            d.text((cx, y), t, font=f, fill=col)
            cx += d.textlength(t, font=f)
        y += int(size * spacing)
    return im


W, Y = (245, 241, 233), (253, 213, 6)
A = ROOT / 'assets'


def save(im, name, q=86):
    im.save(OUT / name, quality=q)
    print('→', name, im.size)


# G331 · «Я никогда не любил продавать» без «Даже когда было агентство… Я нанял отдел продаж»
im = Image.open(A / 'secret2-full/s237-dontlove.webp').convert('RGB')
im = erase(im, (0.03, 0.575, 0.50, 0.885), mode='text', thr=60, grow=7)
save(im, 's2-331-dontlove.webp')

# G332 / G333 · «Поэтому у меня всегда была одна стратегия»: фотограф окремо, маркетолог окремо, без «Сначала отдал…»
base = Image.open(A / 'secret2-full/s238-strategy.webp').convert('RGB')
base = erase(base, (0.03, 0.79, 0.97, 0.965), mode='box')
save(erase(base, (0.50, 0.255, 0.985, 0.80), mode='box'), 's2-332-photographer.webp')
save(erase(base, (0.02, 0.255, 0.50, 0.80), mode='box'), 's2-333-marketer.webp')

# G338 · «-80% от рыночной стоимости» замість «¼» — і в заголовку, і на бирці
im = Image.open(A / 'gen-rest-1006/r071-poster-v1.webp').convert('RGB')
im = erase(im, (0.01, 0.05, 0.99, 0.225), mode='text', thr=55, grow=9)
im = text(im, (900, 58), [[('А потом спросил:', W)]], 66, anchor='ma')
im = text(im, (900, 158), [[('«Если вам надо, можете заплатить за него', W)]], 44, font='Unbounded-SemiBold.ttf', anchor='ma')
im = text(im, (900, 236), [[('-80% от рыночной стоимости»', Y)]], 56, anchor='ma')
im = erase(im, (0.452, 0.630, 0.508, 0.697), mode='text', thr=60, grow=4)
im = text(im, (855, 1158), [[('-80%', Y)]], 36, anchor='ma')
save(im, 's2-338-minus80.webp')

# G343 / G345 / G360 · «Связка»: одна картка, дві, три — без нижнього рядка «Одна услуга, один тип клиента…»
base = Image.open(A / 'gen-rest-1006/r072-svazka-a2.webp').convert('RGB')
base = erase(base, (0.02, 0.785, 0.98, 0.955), mode='box')
save(base, 's2-360-svazka3.webp')
save(erase(base, (0.66, 0.235, 0.985, 0.79), mode='box'), 's2-345-svazka2.webp')
save(erase(base, (0.345, 0.235, 0.985, 0.79), mode='box'), 's2-343-svazka1.webp')

# G358 · «Сломать невозможно» без «Первый вопрос закрыт. Второй тяжелее»
im = Image.open(A / 'gen-secret2-full/s242.webp').convert('RGB')
save(erase(im, (0.03, 0.755, 0.80, 0.93), mode='box'), 's2-358-safe.webp')

# G370 · замість «Вот что именно пишем» — «И дал ему ИИ-агента, которого обучил продавать»
im = Image.open(A / 'gen-secret2-full/s248.webp').convert('RGB')
im = erase(im, (0.02, 0.012, 0.86, 0.132), mode='text', thr=60, grow=9)
im = erase(im, (0.02, 0.125, 0.52, 0.215), mode='text', thr=60, grow=9)
im = text(im, (105, 92), [[('И дал ему ИИ-агента,', W)], [('которого обучил', W)], [('продавать', Y)]], 74)
save(im, 's2-370-agent-chat.webp')

# G384 · без «Петля закрыта.» і без «Видите себя внутри? Напишите «вижу»»
im = Image.open(A / 'gen-secret2-full/s259.webp').convert('RGB')
im = erase(im, (0.03, 0.07, 0.80, 0.1395), mode='box')
im = erase(im, (0.03, 0.755, 0.70, 0.93), mode='box')
im = shift_up(im, 0.055)
save(im, 's2-384-one-left.webp')
