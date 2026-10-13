#!/usr/bin/env python3
"""09.10 · rest 82 «Есть разница, где охотиться?»: фони карток Киев / Харьков (gpt-image-2, images/generations, 1024×1536).
→ assets/gen-rest-1006/r082-<city>.png (+ .webp). Ключ — як у _gen_openai.py."""
import json, os, sys, base64, subprocess, time
from concurrent.futures import ThreadPoolExecutor
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
sys.argv = [sys.argv[0]]
src = open(os.path.join(here, '_gen_openai.py'), encoding='utf-8').read()
exec(src[:src.index('FULL=')])  # key()
STYLE = ("Vertical photo, 2:3. Photo-real night cityscape, shot on Leica Q3 35mm, natural film grain, cinematic low-key exposure. "
         "Near-black sky and shadows (#0B0907), warm amber-yellow city lights (#FDD506) as the only accent colour, no blue or green tint. "
         "The middle band of the frame is calm and darker so a large white city name can be overlaid in the centre. "
         "No text, no letters, no readable signs, no logos, no watermark. ")
JOBS = {
    'kyiv': "Kyiv, Ukraine at night: view across the Dnipro river with long reflections of lights in the water, the steel Motherland Monument "
            "and the golden domes of the Kyiv Pechersk Lavra on the green hilly right bank, lit bridges, warm windows.",
    'kharkiv': "Kharkiv, Ukraine at night: Freedom Square with the monumental constructivist Derzhprom building lit by warm floodlights, "
               "wide empty square with glowing street lamps, wet pavement reflecting the lights.",
}
OUT = os.path.join(root, 'assets/gen-rest-1006')
def run(k):
    body = json.dumps({'model': 'gpt-image-2', 'prompt': STYLE + 'Scene: ' + JOBS[k], 'size': '1024x1536', 'quality': 'high', 'n': 1})
    t = time.time()
    r = subprocess.run(['curl', '-s', '-m', '300', 'https://api.openai.com/v1/images/generations', '-H', 'Authorization: Bearer ' + key(),
                        '-H', 'Content-Type: application/json', '--data-binary', body], capture_output=True, text=True)
    try: d = json.loads(r.stdout)
    except Exception: print(k, 'BAD RESPONSE', r.stdout[:300]); return
    if 'data' not in d: print(k, 'ERROR', json.dumps(d.get('error', d))[:400]); return
    fn = os.path.join(OUT, f'r082-{k}.png'); open(fn, 'wb').write(base64.b64decode(d['data'][0]['b64_json']))
    from PIL import Image
    Image.open(fn).convert('RGB').save(fn[:-4] + '.webp', 'WEBP', quality=86, method=6)
    print(k, 'ok', fn, f'{time.time() - t:.0f}s')
with ThreadPoolExecutor(max_workers=2) as ex: list(ex.map(run, JOBS))
