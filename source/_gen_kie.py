#!/usr/bin/env python3
"""Генерация кадров слайдов через KIE.AI (GPT Image 2).
   python3 source/_gen_kie.py                 # dry-run: печатает payload'ы
   python3 source/_gen_kie.py --run s02-mimo  # запустить один job (или --run all)
   Ключ: KIE_API_KEY в ../.env (папка yasko). Результат: assets/photo/gen/kie/<id>.png + kie-log.json"""
import json, os, sys, time, urllib.request
here=os.path.dirname(os.path.abspath(__file__)); root=os.path.dirname(here)
env=os.path.join(os.path.dirname(root),'.env')
KEY=None
for line in open(env):
    if line.startswith('KIE_API_KEY='): KEY=line.strip().split('=',1)[1]
J=json.load(open(os.path.join(here,'kie-jobs.json'),encoding='utf-8'))
STYLE=("Presentation frame for a dark webinar deck. Black background (#0B0907), warm yellow light (#FDD506) as the only accent, "
       "cinematic photo-real, no text, no letters, no logos anywhere in the frame; bottom quarter of the frame stays dark and empty for a headline overlay. "
       "Second reference image sets the visual style (golden wireframe figures, warm light on black). ")
FACE="The man is the person from the first reference photo (same face, beard, platinum-blond short hair, black clothes) — keep his likeness exactly. "
def payload(job):
    refs=(J['face_refs'] if job.get('face') else [])+J['style_refs']
    prompt=STYLE+(FACE if job.get('face') else "")+"Scene: "+job['brief']
    return {"model":"gpt-image-2-image-to-image","input":{"prompt":prompt,"input_urls":refs,"aspect_ratio":job.get('aspect','1:1'),"resolution":"2K","background":"opaque"}}
def api(path,data=None):
    req=urllib.request.Request('https://api.kie.ai/api/v1/'+path, data=json.dumps(data).encode() if data else None,
        headers={'Authorization':'Bearer '+KEY,'Content-Type':'application/json'}, method='POST' if data else 'GET')
    with urllib.request.urlopen(req,timeout=60) as r: return json.load(r)
def run(job):
    p=payload(job); print("→",job['id'],"…",end=' ',flush=True)
    r=api('jobs/createTask',p)
    if r.get('code')!=200: print("FAIL",r); return None
    tid=r['data']['taskId']
    for _ in range(90):
        time.sleep(5); s=api('jobs/recordInfo?taskId='+tid); d=s.get('data') or {}
        st=d.get('state')
        if st=='success':
            urls=json.loads(d.get('resultJson') or '{}').get('resultUrls') or []
            out=os.path.join(root,'assets','photo','gen','kie'); os.makedirs(out,exist_ok=True)
            fn=os.path.join(out,job['id']+'.png'); urllib.request.urlretrieve(urls[0],fn)
            print("ok",fn,"credits:",d.get('creditsConsumed')); return fn
        if st=='fail': print("FAIL",d.get('failMsg') or d); return None
    print("timeout"); return None
if __name__=='__main__':
    if '--run' in sys.argv:
        if not KEY: sys.exit("нет KIE_API_KEY в yasko/.env")
        which=sys.argv[sys.argv.index('--run')+1]
        jobs=J['jobs'] if which=='all' else [j for j in J['jobs'] if j['id']==which]
        log=[]
        for j in jobs: log.append({'id':j['id'],'file':run(j),'payload':payload(j)})
        json.dump(log,open(os.path.join(here,'kie-log.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    else:
        for j in J['jobs']: print(json.dumps(payload(j),ensure_ascii=False)[:600],"\n")
