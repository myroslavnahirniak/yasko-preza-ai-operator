"""Source-v6 structure + existing service slides. Produces reviewable files; no overrides mutation."""
import sys,json,re,copy,html
from pathlib import Path
sys.path.insert(0,'/tmp/yasko-sales-libs');sys.path.insert(0,str(Path('source').resolve()))
from bs4 import BeautifulSoup as BS
import tinycss2
from _slide import load_S
ROOT=Path.cwd();D=ROOT/'source/sales-v6-20260921';ANCHOR='g3f9b3adf0b8_0_2226'
S=load_S();O=json.loads((ROOT/'source/overrides.json').read_text());old=O['__visibleGoogleAudit']['slides'][ANCHOR]['presentationParts']['slides'];src=json.loads((D/'source-slides.json').read_text())
if any('salesV6Source' in slide for slide in S):
 raise SystemExit('Sales v6 already migrated. Do not reselect by old display numbers; use final-map.json and stable object IDs.')
(D/'pre-migration-slides.json').write_text(json.dumps(S,ensure_ascii=False))
(D/'pre-migration-sales.json').write_text(json.dumps(old,ensure_ascii=False,indent=2))
# User: move the finished service demonstrations into their positions in the v6 selling structure.
# Number selection is captured with original object IDs in the manifest, then applied by object ID.
move={14:list(range(179,184)),53:list(range(227,236)),56:list(range(172,176)),61:list(range(169,172)),66:list(range(184,192)),73:list(range(192,197)),74:list(range(197,203)),78:list(range(219,227)),79:[216,218],80:[217],81:[236],85:[213,214],86:[215],90:list(range(203,208)),91:list(range(208,213))}
replace={53,56,66,73,74,79,80,85,86,90,91}
# These audience texts already match the new source. Preserve approved layouts and existing media.
reuse={4:3,5:4,30:37,34:42,35:45,37:47,44:55,47:60,49:63,50:64,51:62,54:68,55:69,57:71,60:73,64:75,72:79,77:85,82:86,83:43,97:87,100:88,101:89,102:90,103:91,104:92,105:93,106:94,107:95,108:96,110:98,111:99,112:100,113:101,114:102,115:103,117:104,118:106}
reuse.update({n:n+7 for n in range(13,30)})
reuse.update({31:38,32:39,33:40,42:53,98:83})
# Corresponding old designs can supply real photos and examples, not their outdated copy.
media_match={13:20,14:21,15:22,16:23,17:24,18:25,19:26,20:27,21:28,22:29,23:30,24:31,25:32,26:33,27:34,28:35,29:36,53:67,56:70,59:72,63:66,94:81,98:83,99:82}
emoji=re.compile('[\U0001F000-\U0001FAFF\u2600-\u27BF\ufe0f\u200d]')
def plain(h):
 b=BS(h,'html.parser');[x.decompose() for x in b.select('svg')];return b.get_text(' ',strip=True)
def palette(s):
 for a,b in [('49,233,129','253,213,6'),('49, 233, 129','253, 213, 6'),('#31E981','#FDD506'),('#31e981','#fdd506'),('#1C8F52','#8f780b'),('#1e9e58','#8f780b'),('#FFB02E','#fdd506'),('61,139,255','253,213,6')]:s=s.replace(a,b)
 return s
# Fully scoped source layout styles; source JavaScript is never executed or copied.
raw=(D/'source-style.css').read_text();rules=tinycss2.parse_stylesheet(raw,skip_comments=True,skip_whitespace=True)
anims={tinycss2.serialize(r.prelude).strip() for r in rules if r.type=='at-rule' and r.lower_at_keyword=='keyframes'}
def scope_rules(rs):
 out=[]
 for r in rs:
  if r.type=='qualified-rule':
   sels=tinycss2.serialize(r.prelude);body=tinycss2.serialize(r.content)
   scoped=[]
   for sel in sels.split(','):
    sel=sel.strip()
    if not sel or re.search(r'(^|\s)(html|body|:root|#stage|#hud|#director|#progress|#nav)(\b|:|$)',sel) or sel in ['.slide','.slide.on']:continue
    sel=re.sub(r'^\.slide(?:\.on)?\s+','',sel)
    scoped.append('.sales-v6 '+sel)
   if scoped:out.append(','.join(scoped)+'{'+body+'}')
  elif r.type=='at-rule' and r.lower_at_keyword=='keyframes':out.append(tinycss2.serialize([r]))
  elif r.type=='at-rule' and r.lower_at_keyword in ['media','supports'] and r.content:
   out.append('@'+r.lower_at_keyword+' '+tinycss2.serialize(r.prelude)+'{'+scope_rules(tinycss2.parse_rule_list(r.content,skip_comments=True,skip_whitespace=True))+'}')
 return '\n'.join(out)
css=palette(scope_rules(rules))
for name in sorted(anims,key=len,reverse=True):css=re.sub(r'(?<![\w-])'+re.escape(name)+r'(?![\w-])','sv6-'+name,css)
# Extract large embedded image data into static assets so the style remains small/cacheable.
def data_asset(m):
 import base64,hashlib
 typ,blob=m.group(1),m.group(2); ext={'jpeg':'jpg','png':'png','webp':'webp'}.get(typ,typ)
 dst=ROOT/'assets/sales-v6'/('ref-'+hashlib.sha256(blob.encode()).hexdigest()[:12]+'.'+ext);dst.parent.mkdir(exist_ok=True)
 dst.write_bytes(base64.b64decode(blob));return 'url("../'+str(dst.relative_to(ROOT))+'")'
css=re.sub(r'url\([\"\x27]?data:image/(jpeg|png|webp);base64,([^\"\x27)]+)[\"\x27]?\)',data_asset,css)
(ROOT/'css/sales-v6-source.css').write_text('/* Source composition rules, isolated to .sales-v6; brand overrides in sales-v6.css. */\n'+css)

def native(n,s):
 z=BS(s['b'],'html.parser')
 # Never ship executable content or editorial event handlers from the reference.
 for el in z.select('script,iframe'):el.decompose()
 for el in z.find_all(True):
  for attr in list(el.attrs):
   if attr.startswith('on'):del el[attr]
  if el.name=='a' and (el.get('href','').startswith('#') or not el.get('href')):
   el['href']='#ОПЛАТА';el['data-sales-cta']='true'
 for tx in list(z.find_all(string=True)):
  cleaned=emoji.sub('',str(tx))
  if cleaned!=str(tx):tx.replace_with(cleaned)
 for im in z.find_all('img'):
  path=im.get('src','')
  if path and not path.startswith(('http','data:')) and not (ROOT/path).exists():
   im['src']='https://preza-ai-operator-v6.vercel.app/'+path
 # One place for typography: title remains editable HTML, not baked into artwork.
 t=s.get('t','');heading=z.select_one('h1,h2')
 if heading:t=str(heading.decode_contents());heading.decompose()
 if not t:t=s['dirk'] if n not in [45,46,52,116] else ''
 body=palette(str(z))
 body=re.sub(r'font-size:clamp\([^)]*\);?', '', body)
 if n==67:body=body.replace('class="big-num"','class="big-num v6-case-number"')
 if n in [8,9]:body='<div class="v6-task-list">'+body+'</div>'
 if n in [7,10,11,12]:body='<div class="v6-program">'+body+'</div>'
 if '<em>' not in t and t:
  accents={6:'как она устроена',7:'готовый результат',8:'7 задач',9:'9 задач',10:'месяц контента за день',11:'находит агент',12:'без вас',36:'стоит вход',38:'не заработаете всё сами',39:'делаете сами',40:'контент работал за вас',41:'продавать должен агент',43:'Реальная цена',48:'путь оплаты',58:'А что после?',61:'внутри — конвейер',62:'где брать клиентов',63:'в подарок',65:'три услуги',67:'Светлана',68:'половину входа',69:'Закрыть вкладку',70:'Начать сегодня',71:'Система одна',75:'один вечер',76:'окупит вход',78:'приводят агенты',81:'каждый месяц',84:'закрывает агент',87:'пока вы спите',88:'и так уйдут',89:'на части',92:'без вас',93:'под ключ',94:'поставили бизнесам',95:'умеете делать',96:'в цифрах',99:'сколько на ней заработали',109:'никто не ответит'}
  accent=accents.get(n)
  if accent:t=t.replace(accent,'<em>'+accent+'</em>')
 return {'a':6,'lv':6,'mvp':1,'t':t,'k':'','b':f'<div class="sales-v6 v6-source-{n}">'+body+'</div>','note':s.get('note',''),'salesV6Source':n,'salesV6Label':s['dirk'],'foundation':{'type':'content','sourceOnly':False,'omitMedia':True,'media':[],'local':0,'block129':{'kind':'s16','v2':True,'layout':'s16-salesv6','eyebrow':''}}}
parts=[];manifest=[];moved=[]
for n,s in enumerate(src,1):
 if n<=2:continue # Same two exact source topics already conclude Secret 3.
 start=len(parts)
 if n not in replace:
  if n==3:
   for k in [0,1]:
    p=copy.deepcopy(old[k]);p['salesV6Source']=n;p['salesV6Label']=s['dirk'];parts.append(p)
  elif n in reuse:
   p=copy.deepcopy(old[reuse[n]-1]);p['salesV6Source']=n;p['salesV6Label']=s['dirk'];parts.append(p)
  else:parts.append(native(n,s))
 for display in move.get(n,[]):
  p=copy.deepcopy(S[display-1]);oid=p['googleObjectId']
  p['movedFrom']={'objectId':oid,'display':display,'part':p.get('presentationPart',1)};p['salesV6Source']=n;p['salesV6Label']=s['dirk'];p['a']=6
  for k in ['displayNumber','presentationPart','presentationPartCount','visibleAudit']:p.pop(k,None)
  parts.append(p);moved.append({'fromDisplay':display,'objectId':oid,'part':p['movedFrom']['part'],'salesSource':n,'title':plain(p['t'])})
 manifest.append({'source':n,'label':s['dirk'],'firstPart':start+1,'lastPart':len(parts),'mode':'moved content' if n in replace else ('preserved layout' if n in reuse or n==3 else 'source copy in brand style')})
assert len({x['fromDisplay'] for x in moved})==len(moved)
result={'sourceGoogleObjectId':ANCHOR,'authorization':'Мирослав 21.09: структура продажу з preza-ai-operator-v6.vercel.app; оформлені слайди про агентів перенести з контентної частини в кінець, у відповідні місця продажу. Межі наданих слайдів збережено.','allowPartTitles':True,'mediaStatus':'ready','slides':parts}
(D/'parts.json').write_text(json.dumps(result,ensure_ascii=False,indent=1));(D/'migration-map.json').write_text(json.dumps({'moved':moved,'structure':manifest},ensure_ascii=False,indent=2))
# Standalone preview uses the real engine and same assets; production data are untouched.
preview=copy.deepcopy(parts)
(ROOT/'js/slides-sales-v6-preview.js').write_text((ROOT/'js/slides-google180.js').read_text().split('window.S=')[0]+'window.S='+json.dumps(preview,ensure_ascii=False)+';\n')
page=(ROOT/'google180.html').read_text();page=re.sub(r'js/slides-google180.js\?[^\"]*','js/slides-sales-v6-preview.js?v=sales-v6',page)
page=page.replace('</head>','<link rel="stylesheet" href="css/sales-v6-source.css?v=1"><link rel="stylesheet" href="css/sales-v6.css?v=1"></head>');page=page.replace('</body>','<script src="js/sales-v6.js?v=1"></script></body>')
(ROOT/'sales-v6-preview.html').write_text(page)
print('PREVIEW:',len(parts),'parts;',len(moved),'moved pages;',len({x['objectId'] for x in moved}),'source objects')
