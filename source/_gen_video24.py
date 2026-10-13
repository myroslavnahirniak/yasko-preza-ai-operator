#!/usr/bin/env python3
"""30.09 Мирослав: фонове відео слайда 24 («реалити-шоу AI-агентов») — Seedance 2.5, «Живий макет» (tilt-shift мініатюра), ОДИН безперервний кадр 15 с; з 6 с камера статична, станції вмикаються по черзі (під моушн-виноски на слайді).
   Старт = assets/gen-2430/sb24/real/k1.png, фініш = real/k5.png (композиція під розкладку слайда), k2–k4 — референси проміжних фаз.
   python3 source/_gen_video24.py --cost          # вартість
   python3 source/_gen_video24.py draft           # чернетка 720p (дешево)
   python3 source/_gen_video24.py final [draft_job_id]   # 1080p
   Результат: assets/gen-2430/sb24/video24-<mode>.mp4"""
import json, os, re, subprocess, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(root, 'assets/gen-2430/sb24/diorama')
PROMPT = (
    "One single continuous camera shot, no cuts, photoreal like a real film shot on a handmade miniature model set with macro tilt-shift lenses; natural realistic colours, warm evening practical lights. "
    "0-2s: a young woman dentist in a white coat places a small white architectural model of her dental clinic on the dark wooden table; the man with platinum hair and beard in a white t-shirt and charcoal overshirt leans in to look. "
    "2-4s: without a cut the camera dives down into the model: now we are at miniature scale on a quiet night street, the clinic is dark and empty, tiny hooded agent figures with small head lamps walk in carrying ladders and light boxes. "
    "4-6s: the camera rises and pulls back to a frontal wide view of the whole diorama on the table (exactly the composition of the dark reference frame) and from this moment the camera is completely LOCKED-OFF and STATIC until the end. "
    "6-7.5s: the clinic shop window lights up as a bright website-like display. "
    "7.5-9s: the street light-box poster with a smiling patient lights up. "
    "9-10.5s: the rooftop billboard lights up. "
    "10.5-12s: at the reception inside the tiny phone glows and rings with small light rings. "
    "12-15s: a tiny concierge appears at the door and greets people, tiny patients walk along the street and enter, a queue forms, the small cash register at the reception glows warmly with a few gold coins; the frame ends exactly on the end image. "
    "Each element lights up clearly one after another, never all at once. Smooth motion, no text, no letters, no logos.")

def cmd(mode, draft_id=None):
    c = ['higgsfield', 'generate', 'create', 'seedance_2_5', '--mode', 'omni_reference', '--prompt', PROMPT,
         '--aspect_ratio', '1:1', '--duration', '15', '--generate_audio=false',
         '--start-image', os.path.join(D, 'k1.png'), '--end-image', os.path.join(D, 'k5.png')]
    for k in ('k2', 'k5dark', 'k3', 'k4'):
        c += ['--image-references', os.path.join(D, k + '.png')]
    c += ['--resolution', '720p', '--draft=true'] if mode == 'draft' else ['--resolution', '1080p']
    if draft_id: c += ['--draft_job_id', draft_id]
    return c

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == '--cost':
        for m in ('draft', 'final'):
            c = cmd(m); c[2] = 'cost'
            c = [x for x in c if x not in ('--wait',)]
            print(m, subprocess.run(c, capture_output=True, text=True).stdout.strip()[-80:])
        sys.exit()
    mode = a[0]; draft_id = a[1] if len(a) > 1 else None
    p = subprocess.run(cmd(mode, draft_id) + ['--wait', '--wait-timeout', '40m', '--json'], capture_output=True, text=True)
    open(os.path.join(D, f'video24-{mode}.json'), 'w').write(p.stdout + p.stderr)
    m = re.search(r'https://[^"\s]+\.mp4', p.stdout)
    if not m:
        print('FAIL', (p.stdout + p.stderr)[-400:]); sys.exit(1)
    fn = os.path.join(D, f'video24-{mode}.mp4')
    subprocess.run(['curl', '-4', '-sS', '-L', '-m', '600', '--retry', '3', '-o', fn, m.group(0)])
    jid = re.search(r'"id":\s*"([^"]+)"', p.stdout)
    print('ok', fn, 'job', jid.group(1) if jid else '?')
