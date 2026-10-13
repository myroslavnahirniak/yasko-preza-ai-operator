#!/usr/bin/env python3
"""Шпаргалка по слайду без читання хендофів. Використання:
  python3 source/_slide.py 184            — за видимим номером у google180.html
  python3 source/_slide.py g409d4d20be6_0_480   — за googleObjectId
  python3 source/_slide.py "Одной кнопкой"      — за фрагментом заголовка
Виводить: номер, oid, заголовок, layout, кроки, арт, body (скорочено), рядки CSS/JS цього layout, і команди для правки/збірки/скрина.
"""
import json,re,os,sys,glob
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load_S():
    src=open(os.path.join(ROOT,'js/slides-google180.js'),encoding='utf-8').read()
    m=re.search(r'window\.S=(\[.*?\]);\n',src,re.S)
    return json.loads(m.group(1))
def strip(h): return re.sub(r'<[^>]+>','',h or '').strip()
def find(S,key):
    key=str(key).strip()
    if key.isdigit():
        i=int(key)-1
        return (i,S[i]) if 0<=i<len(S) else (None,None)
    for i,s in enumerate(S):
        if s.get('googleObjectId')==key: return i,s
    k=key.lower()
    for i,s in enumerate(S):
        if k in strip(s.get('t','')).lower(): return i,s
    return None,None
def layout_of(s):
    f=s.get('foundation') or {}; b=f.get('block129') or {}
    return b.get('layout') or f.get('layout') or s.get('kind') or '-'
def css_hits(layout):
    pats=['b13-v2-'+layout,'fd-'+layout,'.'+layout]
    out=[]
    for fn in sorted(glob.glob(os.path.join(ROOT,'css/*.css'))+glob.glob(os.path.join(ROOT,'js/*.js'))):
        if fn.endswith('slides-google180.js') or fn.endswith('slides.js') or fn.endswith('foundation-review-data.js'): continue
        for n,line in enumerate(open(fn,encoding='utf-8'),1):
            if any(p in line for p in pats):
                out.append('%s:%d: %s'%(os.path.relpath(fn,ROOT),n,line.strip()[:130]))
    return out
def main():
    if len(sys.argv)<2: print(__doc__); return
    S=load_S(); i,s=find(S,sys.argv[1])
    if s is None: print('не знайдено'); return
    f=s.get('foundation') or {}; b=f.get('block129') or {}; oid=s.get('googleObjectId')
    print('slide  #%d  (google %s)  oid %s'%(i+1,f.get('googleNow','?'),oid))
    print('url    http://127.0.0.1:8765/google180.html?square&clean&s=%d'%(i+1))
    print('title  %s'%(s.get('t','')))
    print('layout %s   kind=%s v2=%s eyebrow=%s'%(layout_of(s),b.get('kind'),b.get('v2'),b.get('eyebrow')))
    if b.get('steps'): print('steps  %s  focus=%s'%(b['steps'],b.get('focus')))
    if b.get('art'): print('art    %s'%[a.get('src') for a in b['art']])
    for k in ('bg','src','img','poster'):
        if s.get(k): print('%-6s %s'%(k,s[k]))
    body=s.get('b','')
    print('body   (%d chars) %s%s'%(len(body),body[:400],'…' if len(body)>400 else ''))
    if s.get('note'): print('note   %s'%s['note'].strip()[:200])
    o=json.load(open(os.path.join(ROOT,'source/overrides.json'),encoding='utf-8'))
    ov=o['__visibleGoogleAudit']['slides'].get(oid)
    print('override: %s'%('є (reason: %s)'%(ov.get('reason','')[:160]) if ov else 'нема'))
    hits=css_hits(layout_of(s))
    print('\nCSS/JS цього layout (%d рядків):'%len(hits))
    for h in hits[:30]: print('  '+h)
    if len(hits)>30: print('  … ще %d (grep -n "b13-v2-%s" css/*.css)'%(len(hits)-30,layout_of(s)))
    print('''
Правка:   python3 source/_edit.py %d --reason "…" [--t "<em>…</em>"] [--b @file.html] [--b129 '{"steps":null}'] [--set lv=6] [--shot]
CSS:      правити css/block-154-163.css (s16-*) → бампнути ?v= у index.html і google180.html (_edit.py робить сам з --bump)
Збірка:   _edit.py збирає сам; вручну: FOUNDATION_SOURCE=google-2026-09-16/foundation-source-v2.json python3 source/_foundation_prepare.py && python3 source/_build_slides.py
Скрин:    URL="http://127.0.0.1:8765/google180.html?square&clean&s=%d" OUT=shots/edit NAME=s%d FIRST=7000 STEPS="n,n" node shots/_cdp_steps.mjs'''%(i+1,i+1,i+1))
if __name__=='__main__': main()
