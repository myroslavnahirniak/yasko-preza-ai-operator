#!/usr/bin/env python3
"""Импорт мастер-деки Влада (PREZA-EFIRA-v4.html — один HTML с var S/ACTS/DIR) → source/master.json, acts.json, dir.js.
   usage: python3 source/_import_master.py <path-to-PREZA-EFIRA-v4.html>"""
import re, json, sys, os, shutil, datetime
here=os.path.dirname(os.path.abspath(__file__))
src=sys.argv[1] if len(sys.argv)>1 else os.path.join(here,'akademia/akademia-university/07-webinar/PREZA-EFIRA-v4.html')
js=open(src,encoding='utf-8').read()
S=json.loads('['+re.search(r'var S = \[(.*?)\n\];', js, re.S).group(1)+']')
ACTS=re.findall(r'"([^"]+)"', re.search(r'var ACTS = \[(.*?)\];', js, re.S).group(1))
DIR=re.search(r'var DIR = (\{.*?\n\});', js, re.S).group(1)
stamp=datetime.datetime.now().strftime('%Y%m%d-%H%M')
for name in ('master.json','acts.json','dir.js'):
    p=os.path.join(here,name)
    if os.path.exists(p): shutil.copy(p, os.path.join(here,'_bak', f'{name}.{stamp}')) if os.path.isdir(os.path.join(here,'_bak')) else None
json.dump(S, open(os.path.join(here,'master.json'),'w',encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(ACTS, open(os.path.join(here,'acts.json'),'w',encoding='utf-8'), ensure_ascii=False)
open(os.path.join(here,'dir.js'),'w',encoding='utf-8').write(DIR)
ver=re.search(r'преза эфира (v\d[^\n]*)', js); 
print(f"imported {len(S)} slides ({sum(1 for s in S if s.get('mvp'))} mvp), {len(ACTS)} acts, DIR {len(DIR)} chars from {os.path.basename(src)} [{ver.group(1).strip() if ver else '?'}], mtime {datetime.datetime.fromtimestamp(os.path.getmtime(src)):%Y-%m-%d %H:%M}")
