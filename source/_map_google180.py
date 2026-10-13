#!/usr/bin/env python3
"""Read-only Google snapshot audit and local media materialization; never edits the app."""
import concurrent.futures, difflib, hashlib, html, json, re, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'source'
G = json.loads((SRC / 'final-google-outline-2026-09-11.json').read_text())
P = json.loads((SRC / 'final-google-geometry-2026-09-11.json').read_text())
M = json.loads((SRC / 'master.json').read_text())
O = json.loads((SRC / 'overrides.json').read_text())
OLD = json.loads((SRC / 'final-google-outline-2026-09-10.json').read_text())
old_by_id = {s['objectId']:s for s in OLD['slides']}
pages_by_id = {s['objectId']:s for s in P['slides']}

def norm(s):
    return re.sub(r'[^a-zа-я0-9]+', ' ', html.unescape(re.sub('<[^>]+>', ' ', s or '')).lower().replace('ё','е')).strip()

def plain(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', s or ''))).strip()

service_rx = re.compile(r'^(?:edit\s*[·:]|НОВЫЙ\s*[·:]|ДОРАБОТАТЬ\s*[·:]|НУЖНО ОТ ВЛАДА\s*[·:]|(?:🖼\s*)?ВИЗУАЛ\s*:|Вот тут нужно анимировать|тут примеры креативо|фото офис снаряд|распределить слайды|картинка Агенты)',re.I)
metadata_rx = re.compile(r'^(?:АКТ\s*\d|\d+\s*/\s*\d+\s*$)',re.I)
kickers = {'РЕАЛИТИ-ШОУ AI-АГЕНТОВ','УЗНАЁТЕ СЕБЯ?','СКЕПТИК / АГНОСТИК?','И Я ТАК ЖЕ','ФОРМАТ','ЗА АКТИВНОСТЬ','ПРИЗ №1','ПРАВИЛА ИГРЫ','ТЕМ, КТО ДО КОНЦА','ПРЯМО В ЭФИРЕ','РЕАЛИТИ','ОКНО ВОЗМОЖНОСТИ','ЧТО УЖЕ ПРОИЗОШЛО','УБЕЖДЕНИЕ 2','ЭКРАН','ЭКРАН И ЗВУК'}
manual = {
    1:(91,'exact_reordered_duplicate'),22:(21,'raster_verified_prior_audit'),
    45:(44,'duplicate_source_slide'),46:(44,'duplicate_source_slide'),
    71:(69,'semantic_reworded'),73:(134,'exact_reordered'),
    76:(74,'semantic_reworded'),77:(75,'semantic_reworded'),
    85:(84,'semantic_reworded'),86:(85,'semantic_reworded'),87:(86,'semantic_reworded'),
    89:(88,'semantic_expanded'),92:(91,'exact_repeated_source_slide'),
    94:(93,'semantic_expanded'),97:(95,'semantic_reworded'),98:(97,'semantic_reworded'),
    101:(101,'semantic_reworded'),102:(102,'semantic_reworded'),
    103:(103,'semantic_reworded'),105:(107,'semantic_reworded'),106:(108,'semantic_reworded'),
    107:(109,'semantic_reworded'),108:(110,'exact'),110:(111,'exact'),
    113:(111,'repeated_source_slide'),116:(111,'repeated_source_slide'),
    119:(115,'semantic_reworded'),121:(120,'semantic_expanded'),124:(104,'semantic_reworded'),
    126:(105,'semantic_subset'),131:(122,'exact'),
    133:(129,'alternate_source_version'),134:(129,'alternate_source_version'),135:(129,'alternate_source_version'),
    142:(131,'semantic_reworded'),145:(134,'semantic_reworded'),
    162:(150,'semantic_reworded'),163:(154,'semantic_expanded'),164:(156,'semantic_reworded'),
}

titles = [(i+1, m['t'], norm(m['t']), norm(O.get(m['t'],{}).get('t',m['t']))) for i,m in enumerate(M)]

def match(g):
    n = g['slideNumber']
    if n in manual:
        i, reason = manual[n]
        return i, reason, 1.0 if reason.startswith('exact') or reason == 'raster_verified_prior_audit' else .8, []
    text = norm(g.get('text'))
    lines = [norm(l) for l in (g.get('text') or '').splitlines() if norm(l) and not service_rx.match(l.strip()) and not metadata_rx.match(l.strip())]
    exact = []
    for i,raw,t,ot in titles:
        for candidate in set([t,ot]):
            if candidate and ((len(candidate)>13 and candidate in text) or candidate in lines):
                exact.append((len(candidate), i))
    if exact:
        exact.sort(reverse=True)
        i = exact[0][1]
        return i,'exact',1.0, [j for _,j in exact[1:] if j != i]
    scored = []
    for i,raw,t,ot in titles:
        if len(t)<12: continue
        ratio = max((difflib.SequenceMatcher(None,t,l,autojunk=False).ratio() for l in lines),default=0)
        if ratio > .65: scored.append((round(ratio,3),i))
    scored.sort(reverse=True)
    if scored and scored[0][0] >= .86:
        score,i=scored[0]
        return i,'fuzzy_title',score,[j for s,j in scored[1:3]]
    return None,'no_verified_local_match',0,[j for s,j in scored[:3]]

def dimensions(bytes_):
    # Metadata inspection only: no pixel transforms or image editing.
    from PIL import Image
    from io import BytesIO
    im=Image.open(BytesIO(bytes_)); return list(im.size), im.format.lower()

media_dir = ROOT / 'assets/google-source'; media_dir.mkdir(parents=True,exist_ok=True)
jobs=[]
for g in G['slides'][:180]:
    for e in pages_by_id[g['objectId']].get('pageElements',[]):
        if e.get('image',{}).get('contentUrl'):
            jobs.append((g['slideNumber'], e))

def fetch(job):
    n,e=job; u=e['image']['contentUrl']; stem=f'g{n:03d}-{e["objectId"]}'
    existing=list(media_dir.glob(stem+'.*'))
    try:
        if not existing and '--no-download' in sys.argv:
            return (e['objectId'],{'src':None,'pending':True,'stem':stem,'elementObjectId':e['objectId'],'size':e.get('size'),'transform':e.get('transform')})
        if existing: path=existing[0]; raw=path.read_bytes()
        else:
            with urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as r: raw=r.read()
            dims,fmt=dimensions(raw); ext={'jpeg':'jpg'}.get(fmt,fmt)
            path=media_dir/(stem+'.'+ext);path.write_bytes(raw)
        dims,fmt=dimensions(raw)
        return (e['objectId'], {'src':str(path.relative_to(ROOT)), 'elementObjectId':e['objectId'], 'naturalSize':dims,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'size':e.get('size'), 'transform':e.get('transform'),'crop':e.get('image',{}).get('imageProperties',{}).get('cropProperties'), 'title':e.get('title'), 'description':e.get('description')})
    except Exception as exc: return (e['objectId'],{'error':str(exc),'elementObjectId':e['objectId']})

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    downloads=dict(pool.map(fetch,jobs))

entries=[]
for g in G['slides'][:180]:
    n=g['slideNumber']; p=pages_by_id[g['objectId']]
    raw=g.get('text') or ''
    audience=[]; notes=[]; metadata=[]
    for line in raw.splitlines():
        line=line.strip()
        if not line: continue
        if metadata_rx.match(line): metadata.append(line)
        elif service_rx.match(line): notes.append(line)
        elif line in ['I','О','1']: metadata.append(line)
        else: audience.append(line)
    eyebrow=None
    if audience and (audience[0].upper() in kickers or audience[0].startswith('ПОСТАВЬТЕ «+»')):
        eyebrow=audience.pop(0)
    urls=[l for l in audience if re.match('https?://',l)]
    content=[l for l in audience if l not in urls]
    title=content[0] if content else ''
    body=content[1:]
    idx,reason,confidence,candidates=match(g)
    media=[downloads[e['objectId']] for e in p.get('pageElements',[]) if e['objectId'] in downloads]
    e={
      'googleNumber':n,'googleObjectId':g['objectId'],
      'originalOutlineTitle':g.get('title'),'originalText':raw,
      'title':title,'body':body,'text':'\n'.join(content),'eyebrow':eyebrow,
      'sourceLinks':urls,'sourceMetadata':metadata,'serviceNotes':notes,
      'existingLocal':idx,'existingLocalTitle':plain(M[idx-1]['t']) if idx else None,
      'existingLocalMasterTitle':M[idx-1]['t'] if idx else None,
      'matchReason':reason,'confidence':confidence,'alternativeLocalCandidates':candidates,
      'media':media,'isRasterOnly':bool(media) and not content and not urls,
      'isServiceOnly':bool(notes) and not content and not media and not urls,
      'hasUnextractedRasterContent':bool(media),
      'matchesSept10Snapshot':g['objectId'] in old_by_id and raw==(old_by_id[g['objectId']].get('text') or ''),
      'pageElements':p.get('pageElements',[]),
    }
    entries.append(e)

result={'presentationId':G['presentationId'],'presentationTitle':G['title'],'revisionId':G['revisionId'],'snapshotDate':'2026-09-11','snapshotCount':len(G['slides']),'pageSize':P.get('pageSize'),'scope':'physical Google slides 1–180 inclusive; raw presentation.slides order verified','slideCount':180,'endpoint':{'googleNumber':180,'googleObjectId':entries[-1]['googleObjectId'],'title':entries[-1]['title'],'existingLocal':entries[-1]['existingLocal']},'slides':entries}
(SRC/'google180-foundation-source.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
mapping={k:v for k,v in result.items() if k!='slides'}
mapping['slides']=[{k:e[k] for k in ['googleNumber','googleObjectId','title','existingLocal','existingLocalTitle','existingLocalMasterTitle','matchReason','confidence','alternativeLocalCandidates','serviceNotes','sourceLinks','isRasterOnly','isServiceOnly','matchesSept10Snapshot']} for e in entries]
(SRC/'google180-map.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'slides':len(entries),'downloads':len(downloads),'errors':[v for v in downloads.values() if 'error'in v],'exact':sum(e['confidence']==1 for e in entries),'semantic':sum(0<e['confidence']<1 for e in entries),'unmatched':sum(e['existingLocal']is None for e in entries),'rasterOnly':sum(e['isRasterOnly'] for e in entries),'endpoint':result['endpoint']},ensure_ascii=False,indent=2))
