#!/usr/bin/env python3
"""09.10 · rest 109 «И под каждую — своя модель поиска»: у підсвіченому жовтому чипі «груминг» → «прокат авто» (кейс VIP CAR). gpt-image-2 images/edits."""
import json, os, sys, base64, subprocess, time
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
sys.argv = [sys.argv[0]]
src = open(os.path.join(here, '_gen_openai.py'), encoding='utf-8').read(); exec(src[:src.index('FULL=')])
from PIL import Image
OUT = os.path.join(root, 'assets/gen-s2-1009'); tmp = os.path.join(OUT, '_r109-src.png')
Image.open(os.path.join(root, 'assets/gen-secret2-full/s255.webp')).convert('RGB').save(tmp)
P = ("Keep this image exactly as it is — same layout, same headline, same chips, same fonts, colours, lighting and objects. "
     "Change ONLY the text inside the highlighted yellow chip: replace «груминг» with exactly «прокат авто» (Russian, lowercase), "
     "keeping the yellow chip style; the chip may become a little wider to fit the text. All other chips and texts stay letter by letter the same. No other changes.")
def run(i):
    t = time.time()
    r = subprocess.run(['curl', '-s', '-m', '400', 'https://api.openai.com/v1/images/edits', '-H', 'Authorization: Bearer ' + key(), '-F', 'model=gpt-image-2',
                        '-F', 'prompt=' + P, '-F', 'size=1024x1024', '-F', 'quality=high', '-F', 'n=1', '-F', 'image[]=@' + tmp], capture_output=True, text=True)
    try: d = json.loads(r.stdout)
    except Exception: print(i, 'BAD', r.stdout[:300]); return
    if 'data' not in d: print(i, 'ERROR', json.dumps(d.get('error', d))[:400]); return
    open(os.path.join(OUT, f'r109-chips-cars-{i}.png'), 'wb').write(base64.b64decode(d['data'][0]['b64_json'])); print(i, 'ok', f'{time.time() - t:.0f}s')
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=2) as ex: list(ex.map(run, (1, 2)))
