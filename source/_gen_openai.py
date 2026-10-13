#!/usr/bin/env python3
"""Кадры слайдов через OpenAI gpt-image-2 (images/edits с референсами лица и стиля).
   python3 source/_gen_openai.py s02-mimo [s05-mir ...] | all   → assets/photo/gen/kie/<id>.png
   Брифы: source/kie-jobs.json. Ключ: OPENAI_API_KEY из yasko/.env или 4qlife/.env."""
import json, os, sys, base64, subprocess, time
here=os.path.dirname(os.path.abspath(__file__)); root=os.path.dirname(here)
def key():
    for p in (os.path.join(os.path.dirname(root),'.env'), os.environ.get('KEY_FILE',''), '/Users/miro/imperial/work/4qlife/.env'):
        if not p: continue
        if os.path.exists(p):
            for l in open(p):
                if l.startswith('OPENAI_API_KEY='): return l.strip().split('=',1)[1].strip('"')
    sys.exit('no OPENAI_API_KEY')
FULL='--full' in sys.argv
OVER='--overlay' in sys.argv
J=json.load(open(os.path.join(here,'kie-jobs-full.json' if (FULL or OVER) else 'kie-jobs.json'),encoding='utf-8'))
FACE_IMG=os.path.join(root,'assets/photo/vlad-portrait-studio.png'); STYLE_IMG=os.path.join(root,'assets/photo/vlad-portrait-gold.png')
STYLE=("Frame for a dark webinar presentation. Near-black background (#0B0907), warm yellow light (#FDD506) as the only accent colour, photo-real, shot on Leica Q3 35mm, natural film grain. "
       "No text, no letters, no logos, no captions anywhere. The bottom quarter of the frame stays dark and empty (a headline will be overlaid there). "
       "The second reference image sets the visual style: warm light on black, golden glowing wireframe figures. ")
FACE="The man is the person in the first reference photo — keep his exact likeness (face, beard, platinum-blond short hair), black clothes. "
TYPO=("This is a finished presentation SLIDE, square 1:1, for a Russian-language webinar. Typography is part of the image and must be rendered exactly, letter by letter, in Russian Cyrillic: "
      "the headline in a large, bold, tight geometric sans-serif (like Unbounded), white, occupying the lower third of the slide with generous margins; "
      "a small kicker line above the headline in yellow (#FDD506) monospace uppercase with letter spacing; an optional subline below the headline in a lighter grey sans-serif. "
      "The scene occupies the upper two thirds and fades into black behind the text. Premium keynote look (Apple / OpenAI), no other text, no logos, no watermark. ")
def run(job):
    if OVER:
        texts="Kicker line, small, yellow (#FDD506), monospace, uppercase, letter-spaced, placed above the headline: «"+job.get('kick','')+"». " if job.get('kick') else ""
        texts+="Headline, large, bold, tight geometric sans-serif (Unbounded-like), white, left-aligned, occupying the lower third with wide margins, exact text letter by letter: «"+job['title']+"». "
        if job.get('sub'): texts+="Subline below it, smaller, light grey sans-serif: «"+job.get('sub')+"». "
        if job.get('sub2'): texts+="Tiny yellow monospace footer line: «"+job['sub2']+"». "
        prompt=("Keep this image exactly as it is (same scene, same person, same lighting, same crop) and only ADD typography on top of the dark lower part, like a premium keynote slide. "
                "Render the Russian text EXACTLY as given, every letter and punctuation mark correct, no extra words. Where the text would sit over a bright area, darken that area slightly. "+texts)
        out=os.path.join(root,'assets/photo/gen/kie-text')
    elif FULL:
        texts="Kicker (yellow, small, uppercase): «"+job.get('kick','')+"». " if job.get('kick') else ""
        texts+="Headline (white, large, exact text): «"+job['title']+"». "
        if job.get('sub'): texts+="Subline (grey, small): «"+job['sub']+"». "
        if job.get('sub2'): texts+="Footer line (yellow, tiny mono): «"+job['sub2']+"». "
        prompt=TYPO+(FACE if job.get('face') else '')+texts+"Scene behind the text: "+job['brief']+" Colours: near-black #0B0907 background, warm yellow #FDD506 accent, nothing else."
        out=os.path.join(root,'assets/photo/gen/kie-full')
    else:
        prompt=job.get('frame_style',STYLE)+(FACE if job.get('face') else '')+"Scene: "+job['brief']
        out=os.path.join(root,'assets/photo/gen/kie')
    os.makedirs(out,exist_ok=True); fn=os.path.join(out,job['id']+'.png')
    size={'1:1':'1024x1024','16:9':'1536x1024','9:16':'1024x1536'}.get(job.get('aspect','1:1'),'1024x1024')
    cmd=['curl','-s','-m','300','https://api.openai.com/v1/images/edits','-H','Authorization: Bearer '+key(),'-F','model=gpt-image-2','-F','prompt='+prompt,'-F','size='+size,'-F','quality=high','-F','n=1','-F','output_format=png']
    if job.get('no_reference') and not OVER:
        cmd=['curl','-s','-m','300','https://api.openai.com/v1/images/generations','-H','Authorization: Bearer '+key(),'-H','Content-Type: application/json','--data-binary',json.dumps({'model':'gpt-image-2','prompt':prompt,'size':size,'quality':'high','n':1,'output_format':'png'})]
    elif OVER: cmd+=['-F','image[]=@'+os.path.join(root,'assets/photo/gen/kie',job['id']+'.png')]
    else:
        if job.get('face'): cmd+=['-F','image[]=@'+FACE_IMG]
        cmd+=['-F','image[]=@'+STYLE_IMG]
    t=time.time(); r=subprocess.run(cmd,capture_output=True,text=True); 
    try: d=json.loads(r.stdout)
    except Exception: print(job['id'],'BAD RESPONSE',r.stdout[:300]); return None
    if 'data' not in d: print(job['id'],'ERROR',json.dumps(d.get('error',d))[:400]); return None
    open(fn,'wb').write(base64.b64decode(d['data'][0]['b64_json']))
    print(job['id'],'ok',fn,f'{time.time()-t:.0f}s','usage:',d.get('usage',{}).get('total_tokens')); return fn
if __name__=='__main__':
    ids=[a for a in sys.argv[1:] if not a.startswith('--')] or ['s02-mimo']
    jobs=J['jobs'] if ids==['all'] else [j for j in J['jobs'] if j['id'] in ids]
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=3) as ex: list(ex.map(run,jobs))
