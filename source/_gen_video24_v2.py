#!/usr/bin/env python3
"""30.09 Мирослав: відео слайда 24 «одним кадром» (без розкадровки з різними планами — через неї Seedance «стрибав»).
   Метод як у відео відкриття (source/hero-loop-2026-09-10-v2/video/request.json): одна композиція, карта референсів, таймлайн, інваріанти.
   A — один стартовий кадр (sb24/live/k1), Seedance сам «пірнає» в макет;  B — нерухома камера на вуличці (k6dark → k6lit).
   python3 source/_gen_video24_v2.py A|B [final]  → assets/gen-2430/sb24/diorama/video24-<A|B>-<draft|final>.mp4"""
import os, re, subprocess, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(root, 'assets/gen-2430/sb24/diorama')
P = {
 'A': ("Create one continuous 15-second cinematic shot from the start image @Image1, square 1:1, one single take with no cuts. Photoreal, natural realistic colours, warm evening practical light. "
       "Start exactly on @Image1: a young woman dentist in a white coat has just placed a small white architectural model of her dental clinic on the dark wooden table; "
       "the man with platinum-white hair and a beard, in a white t-shirt and an open charcoal overshirt, leans on the table and looks at the model with calm interest, then gives a small confident nod as if he already knows how to solve it. "
       "0-4 seconds: the camera slowly and smoothly glides forward and down towards the model, as if shrinking to its scale, the office softly blurs away. "
       "4-15 seconds: at miniature scale, one continuous gentle glide along the tiny night street in front of the clinic, real tilt-shift macro look: tiny hooded agent figures with small head lamps switch things on one after another — "
       "first the clinic's big shop window lights up like a website display, then a street light-box poster with a smiling patient, then a billboard on the roof, then a desk phone at the reception glows and rings, "
       "finally the door opens, a tiny concierge greets people, tiny patients walk in and queue, a small cash register glows warmly. "
       "Smooth, continuous, calm pace; consistent people and model; no text, no letters, no numbers, no logos."),
 'B': ("Create one continuous 15-second video, square 1:1, with a COMPLETELY LOCKED CAMERA. This is a subtle living background for a webinar slide, not a slideshow: no cuts, no zooms, no camera movement at all. "
       "REFERENCE MAP: @Image1 (start image) is the exact opening state and the master composition: a photoreal handmade miniature (tilt-shift macro) of a small dental clinic on a night street, everything switched off, "
       "tiny hooded agent figures with head lamps standing ready at five spots. The end image is the SAME composition with all five installations switched on and patients arriving — the state to reach by the end. "
       "Scene invariants: keep the building, window frames, the billboard frame on the roof, the light-box, trees, lamp posts, wet road, blurred city bokeh, lighting and framing exactly stable; natural realistic colours. "
       "ACTION TIMELINE: 0-2 s: quiet life only — head lamps flicker slightly, a tiny car passes on the wet road, reflections shimmer. "
       "2-4 s: the agent at the far-left shop window touches it and the window lights up as a website display. "
       "4-6 s: the agent at the street light-box switches on the poster with the smiling patient. "
       "6-8.5 s: the agent on the roof switches on the billboard with the smiling woman. "
       "8.5-10.5 s: inside, at the reception, a tiny desk phone lights up and rings with small light rings. "
       "10.5-15 s: the entrance door opens, a tiny concierge in a dark suit greets people, tiny patients walk along the pavement from the right and enter, a short queue forms, the reception glows warmly. "
       "Everything that lights up stays lit. Only one installation changes at a time. End exactly on the lit end image. No text, no letters, no numbers, no logos."),
}
def cmd(v, final):
    c = ['higgsfield', 'generate', 'create', 'seedance_2_5', '--mode', 'omni_reference', '--prompt', P[v],
         '--aspect_ratio', '1:1', '--duration', '15', '--generate_audio=false']
    if v == 'A':
        c += ['--start-image', os.path.join(root, 'assets/gen-2430/sb24/live/k1.png'), '--image-references', os.path.join(root, 'assets/photo/vlad-avatar.jpg')]
    else:
        c += ['--start-image', os.path.join(D, 'k6dark.png'), '--end-image', os.path.join(D, 'k6lit.png')]
    c += ['--resolution', '1080p'] if final else ['--resolution', '720p', '--draft=true']
    return c
if __name__ == '__main__':
    v = sys.argv[1]; final = len(sys.argv) > 2 and sys.argv[2] == 'final'
    tag = f"video24-{v}-{'final' if final else 'draft'}"
    p = subprocess.run(cmd(v, final) + ['--wait', '--wait-timeout', '40m', '--json'], capture_output=True, text=True)
    open(os.path.join(D, tag + '.json'), 'w').write(p.stdout + p.stderr)
    m = re.search(r'https://[^"\s]+\.mp4', p.stdout)
    if not m: print(v, 'FAIL', (p.stdout + p.stderr)[-400:]); sys.exit(1)
    fn = os.path.join(D, tag + '.mp4')
    subprocess.run(['curl', '-4', '-sS', '-L', '-m', '600', '--retry', '3', '-o', fn, m.group(0)])
    print(v, 'ok', fn)
