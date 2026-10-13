#!/usr/bin/env python3
"""09.10 · rest 97 «И дал ему ИИ-агента, которого обучил продавать»: та сама картинка з телефоном, переписка — про прокат авто (кейс VIP CAR).
gpt-image-2 images/edits з поточним постером як вхідним кадром. → assets/gen-s2-1009/r097-agent-chat-cars-<n>.png"""
import json, os, sys, base64, subprocess, time
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
argv = sys.argv[1:]; sys.argv = [sys.argv[0]]
src = open(os.path.join(here, '_gen_openai.py'), encoding='utf-8').read(); exec(src[:src.index('FULL=')])
N = int(argv[0]) if argv else 1
SRC = os.path.join(root, 'assets/gen-s2-1008/s2-370-agent-chat.webp')
from PIL import Image
tmp = os.path.join(root, 'assets/gen-s2-1009/_r097-src.png'); Image.open(SRC).convert('RGB').save(tmp)
PROMPT = ("Keep this image exactly as it is: the same phone, angle, perspective, lighting and glow, the same headline in the top-left corner, "
          "the same chat layout, bubble shapes, sizes and positions, the same small labels above the bubbles "
          "(«ПЕРВОЕ СООБЩЕНИЕ», «ОТВЕЧАЮТ», «ВТОРОЕ», «ТРЕТЬЕ — РАДИ НЕГО ВСЁ»), the same timestamps and ticks, the same fonts and colours. "
          "Change ONLY the message texts inside the four chat bubbles, rendered exactly letter by letter in Russian Cyrillic, with the same line style:\n"
          "Bubble 1 (top, grey): «Добрый день! Можно арендовать машину на выходные?»\n"
          "Bubble 2 (reply, grey, with the round avatar): «Да, конечно. На какие даты?»\n"
          "Bubble 3 (grey): «Я пробовал забронировать через сайт — не получилось. Вы так много клиентов теряете?»\n"
          "Bubble 4 (yellow outlined, bottom): «Я сделал вам новый сайт, где можно забронировать авто за минуту. Обычно беру за такие $1.000 — вам сделал бесплатно. Хотите посмотреть?»\n"
          "No other text changes, no extra words, no typos.")
def run(i):
    t = time.time()
    cmd = ['curl', '-s', '-m', '400', 'https://api.openai.com/v1/images/edits', '-H', 'Authorization: Bearer ' + key(),
           '-F', 'model=gpt-image-2', '-F', 'prompt=' + PROMPT, '-F', 'size=1024x1024', '-F', 'quality=high', '-F', 'n=1', '-F', 'image[]=@' + tmp]
    r = subprocess.run(cmd, capture_output=True, text=True)
    try: d = json.loads(r.stdout)
    except Exception: print(i, 'BAD RESPONSE', r.stdout[:300]); return
    if 'data' not in d: print(i, 'ERROR', json.dumps(d.get('error', d))[:400]); return
    fn = os.path.join(root, f'assets/gen-s2-1009/r097-agent-chat-cars-{i}.png'); open(fn, 'wb').write(base64.b64decode(d['data'][0]['b64_json']))
    print(i, 'ok', fn, f'{time.time() - t:.0f}s')
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=N) as ex: list(ex.map(run, range(1, N + 1)))
