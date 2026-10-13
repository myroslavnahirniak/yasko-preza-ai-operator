#!/usr/bin/env python3
"""Одна команда на правку слайда: патч overrides.json → збірка → (опційно) бамп версії CSS/JS → (опційно) скрин.
  python3 source/_edit.py 184 --reason "Мирослав: прибрати кроки" --b129 '{"steps":null}' --shot
  python3 source/_edit.py 185 --reason "текст вище" --t "Каждая <em>…</em>" --b @source/_tmp_body.html
  python3 source/_edit.py 193 --reason "…" --set lv=6 --bump --shot
Слайд = видимий номер, oid або фрагмент заголовка (як у _slide.py).
  --t / --b        заголовок / body (значення з @ = прочитати з файлу)
  --set k=v        інші ключі в set (lv, k, note); v як JSON, якщо парситься
  --b129 JSON      злити у foundation.block129 (null = видалити ключ). Напр. '{"layout":"s16-live","steps":["a","b"]}'
  --fnd JSON       злити у foundation (mediaBrief, animationBrief…)
  --bump           бампнути ?v= для css/js block-154-163 в index.html і google180.html (після правки CSS/JS)
  --no-build       тільки патч
  --shot [STEPS]   скрин після збірки (STEPS напр. "n,n,p"), файл shots/edit/s<N>-<k>.png
"""
import json,os,sys,argparse,subprocess,datetime,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _slide import load_S,find
def val(v):
    if v is None: return None
    if v.startswith('@'): return open(v[1:],encoding='utf-8').read().strip()
    return v
def jval(v):
    try: return json.loads(v)
    except Exception: return v
ap=argparse.ArgumentParser(); ap.add_argument('slide'); ap.add_argument('--reason',required=True)
ap.add_argument('--part',type=int,help='Edit one existing presentation part (1-based), preserving siblings'); ap.add_argument('--t'); ap.add_argument('--b'); ap.add_argument('--set',action='append',default=[])
ap.add_argument('--b129'); ap.add_argument('--fnd'); ap.add_argument('--bump',action='store_true')
ap.add_argument('--parts',help='Source-authorized presentationParts JSON file; preserve exact slide order')
ap.add_argument('--omit',choices=['true','false'],help='Hide/restore this source slide, preserving its data')
ap.add_argument('--no-build',action='store_true'); ap.add_argument('--shot',nargs='?',const='',default=None)
a=ap.parse_args()
S=load_S(); i,s=find(S,a.slide)
if s is None: sys.exit('слайд не знайдено: '+a.slide)
oid=s['googleObjectId']; num=i+1
p=os.path.join(ROOT,'source/overrides.json'); o=json.load(open(p,encoding='utf-8')); va=o['__visibleGoogleAudit']['slides']
e=va.setdefault(oid,{})
stamp=datetime.date.today().strftime('%d.%m')
e['reason']=(stamp+' '+a.reason+' | '+e.get('reason','')).strip(' |')[:600]
if a.parts:
    parts=json.load(open(a.parts,encoding='utf-8'))
    if parts.get('sourceGoogleObjectId')!=oid or not parts.get('authorization') or len(parts.get('slides',[]))<2:
        sys.exit('parts require matching sourceGoogleObjectId, authorization and at least two slides')
    e['presentationParts']=parts
if a.omit is not None: e['omit']=a.omit=='true'
if a.part is not None:
    parts=e.get('presentationParts',{}).get('slides',[])
    if not 1 <= a.part <= len(parts): sys.exit('presentation part not found')
    e=parts[a.part-1]
rm=e.setdefault('remove',[]) if a.part is None else []
for k in ['bg','photos','src','kind','poster','opening','viz','theme','fx','lost','bgside','ptall','img','k']:
    if k not in rm: rm.append(k)
st=e.setdefault('set',{}) if a.part is None else e
if a.t is not None: st['t']=val(a.t)
if a.b is not None: st['b']=val(a.b)
for kv in a.set:
    k,v=kv.split('=',1); st[k]=jval(val(v))
f=e.setdefault('foundation',{})
f.setdefault('type','content'); f.setdefault('omitMedia',True); f.setdefault('media',[]); f.setdefault('mediaNeeded',False); f.setdefault('sourceOnly',False); f.setdefault('local',0)
if a.fnd:
    for k,v in json.loads(a.fnd).items():
        if v is None: f.pop(k,None)
        else: f[k]=v
if a.b129:
    b=f.setdefault('block129',{'kind':'s16','v2':True})
    for k,v in json.loads(a.b129).items():
        if v is None: b.pop(k,None)
        else: b[k]=v
    if b.get('layout','').startswith('s16-'): f.pop('layout',None); f.pop('variant',None)
json.dump(o,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('patched #%d %s'%(num,oid))
if a.bump:
    tag='s16-'+datetime.date.today().strftime('%Y%m%d')+datetime.datetime.now().strftime('%H%M')
    for fn in ('index.html','google180.html'):
        fp=os.path.join(ROOT,fn); t=open(fp,encoding='utf-8').read()
        t=re.sub(r'(block-154-163\.(?:css|js)\?v=)[^"]+',r'\g<1>'+tag,t); open(fp,'w',encoding='utf-8').write(t)
    print('bumped block-154-163 → '+tag)
if a.no_build: sys.exit()
env=dict(os.environ,FOUNDATION_SOURCE='google-2026-09-16/foundation-source-v2.json')
subprocess.run([sys.executable,'source/_foundation_prepare.py'],cwd=ROOT,env=env,check=True,stdout=subprocess.DEVNULL)
r=subprocess.run([sys.executable,'source/_build_slides.py'],cwd=ROOT,capture_output=True,text=True); print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-300:])
if a.shot is not None:
    env2=dict(os.environ,URL='http://127.0.0.1:8765/google180.html?square&clean&s=%d'%num,OUT='shots/edit',NAME='s%d'%num,FIRST='7000',DELAY='2500',STEPS=a.shot)
    r=subprocess.run(['node','shots/_cdp_steps.mjs'],cwd=ROOT,env=env2,capture_output=True,text=True)
    print(r.stdout.strip()[-600:] or r.stderr[-400:]); print('shots: shots/edit/s%d-*.png'%num)
