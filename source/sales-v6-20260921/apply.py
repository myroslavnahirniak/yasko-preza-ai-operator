"""Apply reviewed migration through the sanctioned editor; check concurrent edits first."""
from pathlib import Path
import sys,json,subprocess,copy,re
sys.path.insert(0,str(Path('source').resolve()))
from _slide import load_S
R=Path.cwd();D=R/'source/sales-v6-20260921';anchor='g3f9b3adf0b8_0_2226';sec='g3f9b3adf0b8_0_1943'
m=json.loads((D/'migration-map.json').read_text());o=json.loads((R/'source/overrides.json').read_text());va=o['__visibleGoogleAudit']['slides'];current=load_S();before=json.loads((D/'pre-migration-slides.json').read_text())
assert va[anchor]['presentationParts']['slides']==json.loads((D/'pre-migration-sales.json').read_text()),'Sales changed since preparation — refresh plan first'
for move in m['moved']:
 n=move['fromDisplay'];assert current[n-1]==before[n-1],f'Concurrent change at {n} — refresh plan first'
(D/'affected-overrides-before.json').write_text(json.dumps({oid:va[oid] for oid in {anchor,sec,*[x['objectId'] for x in m['moved']]}},ensure_ascii=False,indent=1))
def edit(oid,*args):
 r=subprocess.run([sys.executable,'source/_edit.py',oid,'--reason','Мирослав: структура продажу v6, перенесення готових послуг з контентної частини','--no-build',*args],capture_output=True,text=True)
 if r.returncode:raise RuntimeError(r.stdout+r.stderr)
edit(anchor,'--parts',str(D/'parts.json'))
for oid in dict.fromkeys(x['objectId'] for x in m['moved']):edit(oid,'--omit','true')
# The two source introduction topics are already at the end of Secret 3, keep only one copy.
secparts=va[sec]['presentationParts']['slides'];part=next(i for i,p in enumerate(secparts,1) if p.get('secret3SourceNumber')==35)
replace={'Больше 96 задач, которые делают агенты':'46 готовых задач под ваши услуги','21 связка на поиск клиентов':'Связки на поиск клиентов под каждую услугу'}
b=secparts[part-1]['b']
for a,z in replace.items():b=b.replace(a,z)
(D/'iceberg-body.html').write_text(b);edit(sec,'--part',str(part),'--b','@'+str(D/'iceberg-body.html'))
for f in ['js/secret3-final-c.js','source/secret3-final-20260921/segment-c.js']:
 p=R/f;s=p.read_text()
 for a,z in replace.items():s=s.replace(a,z)
 p.write_text(s)
# Renderers must be cached by their new version; _foundation_prepare derives google180 from index.
for f in ['index.html','google180.html']:
 p=R/f;s=p.read_text();s=re.sub(r'(secret3-final-c.js\?v=)[^\"]+',r'\g<1>sales-v6-20260921',s)
 if 'css/sales-v6.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="css/sales-v6-source.css?v=sales-v6-20260921"><link rel="stylesheet" href="css/sales-v6.css?v=sales-v6-20260921"></head>')
 if 'js/sales-v6.js' not in s:s=s.replace('</body>','<script src="js/sales-v6.js?v=sales-v6-20260921"></script></body>')
 p.write_text(s)
env=__import__('os').environ.copy();env['FOUNDATION_SOURCE']='google-2026-09-16/foundation-source-v2.json'
for cmd in [['source/_foundation_prepare.py'],['source/_build_slides.py']]:
 r=subprocess.run([sys.executable,*cmd],env=env,capture_output=True,text=True,check=True);print(r.stdout[-400:])
print('Applied',len(m['moved']),'moved pages across',len(set(x['objectId'] for x in m['moved'])),'objects')
