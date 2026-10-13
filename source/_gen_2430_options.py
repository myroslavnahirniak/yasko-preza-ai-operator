#!/usr/bin/env python3
"""30.09 Мирослав: варіанти оформлення слайдів 24 (реаліті-шоу), 27 (Приз №1 · холст), 31 (Приз №3 · барига).
   Фото-сцени — у стилі слайдів 23/26 (клоші), скетчі — у стилі assets/sketches/reality-route-*.
   python3 source/_gen_2430_options.py [ключі]   → assets/gen-2430/<key>.png + .webp"""
import json, os, re, subprocess, sys, concurrent.futures as cf
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(root, 'assets/gen-2430'); os.makedirs(OUT, exist_ok=True)
A = lambda p: os.path.join(root, 'assets', p)
PHOTO_REFS = [A('photo/s26-three-prizes-v1.png'), A('photo/slidebg3.png')]
SKETCH_REFS = [A('sketches/reality-route-ads-v1.png'), A('sketches/reality-route-website-v1.png')]
PHOTO = ("Square 1:1 photoreal cinematic render in exactly the visual style of the reference images: near-black background, warm gold light, "
         "electric-yellow (#FDD506) accents, soft haze, premium keynote look. The upper 45% of the frame is dark calm empty space for a headline. "
         "Absolutely no readable text, no letters, no numbers, no logos, no watermark. ")
SKETCH = ("Square 1:1 detailed pencil and charcoal cross-hatched sketch on pure black paper in exactly the style of the reference sketches, "
          "cream-grey graphite lines with electric-yellow (#FDD506) marker highlights, one object centred with lots of black space around, slight 3/4 view. "
          "Absolutely no readable text, no letters, no numbers, no logos, no watermark. ")
J = {
 's24-studio':   ('p', "A dark reality-show TV studio at night seen from the audience. Five identical matte-black glass booths stand evenly spaced in one straight row across the lower half of the frame, "
                       "each lit from inside with warm gold light and containing one glowing workstation monitor with abstract UI. A professional TV camera on a tripod and a small red on-air lamp in the foreground left, spotlights from above. No people."),
 's27-cloche':   ('p', "Continuation of the reference image with three cloches: now one matte-black and gold cloche is lifted and floating above a black marble pedestal, "
                       "revealing a sleek tablet lying on the pedestal whose screen glows with an abstract document layout (yellow heading bars, grey text lines, small cards). Warm golden light spills from under the cloche."),
 's31-cloche':   ('p', "Continuation of the reference image with three cloches: now one matte-black and gold cloche is lifted and floating above a black marble pedestal, "
                       "revealing a neat fan of glowing premium membership cards with gold edges and abstract gradient faces (no logos, no text). Warm golden light spills from under the cloche, a few golden coins on the marble."),
 's24-ad':       ('s', "A single social-media ad post card (square post frame with rounded corners) showing a product photo of a cosmetic bottle, a round yellow sale badge shape and a yellow button shape, a small hand cursor about to click the button."),
 's27-calc':     ('s', "A vintage desk calculator with a paper tape curling out of it; on the tape a hand-drawn rising line chart highlighted in yellow; the calculator display glows yellow."),
 's27-prices':   ('s', "A paper price tag on a string with a yellow edge, hanging over a small fanned stack of service cards (a website card, a video card, a chat card)."),
 's27-path':     ('s', "A winding road seen from above with six small milestone flags along it, leading to a small shop door with a warm light; the road centre line is yellow."),
 's27-prompts':  ('s', "An open laptop with a code window on screen, a big glowing yellow copy icon (two overlapping rounded squares) floating above the keyboard, a finger about to tap it."),
 's27-message':  ('s', "A paper envelope with a folded letter half pulled out and a small yellow speech bubble floating above it."),
 's27-links':    ('s', "A chain of three large interlocking chain links, the middle link glowing yellow, small bookmark cards hanging from the links."),
}
def run(k):
    kind, p = J[k]
    base, refs, res, q = (PHOTO, PHOTO_REFS, '2k', 'xhigh') if kind == 'p' else (SKETCH, SKETCH_REFS, '1k', 'high')
    cmd = ['higgsfield', 'generate', 'create', 'gpt_image_2_5', '--prompt', base + p, '--aspect_ratio', '1:1', '--resolution', res,
           '--quality', q, '--wait', '--wait-timeout', '20m', '--json']
    for r in refs: cmd += ['--image-references', r]
    pr = subprocess.run(cmd, capture_output=True, text=True)
    m = re.search(r'https://[^"\s]+\.(?:png|jpg|jpeg|webp)', pr.stdout)
    if not m: return k, 'FAIL ' + (pr.stdout + pr.stderr)[-300:]
    fn = os.path.join(OUT, k + '.png')
    subprocess.run(['curl', '-4', '-sS', '-L', '-m', '180', '--retry', '3', '-o', fn, m.group(0)])
    subprocess.run(['cwebp', '-quiet', '-q', '84', fn, '-o', fn[:-4] + '.webp'])
    with open(os.path.join(OUT, '_prompts.log'), 'a', encoding='utf-8') as f: f.write(json.dumps({'key': k, 'prompt': base + p}, ensure_ascii=False) + '\n')
    return k, 'ok'
if __name__ == '__main__':
    keys = sys.argv[1:] or list(J)
    with cf.ThreadPoolExecutor(4) as ex:
        for k, r in ex.map(run, keys): print(k, r, flush=True)
