"""Materialize the Google-scope design as override data, then use the normal build."""
from pathlib import Path
import json,re,html,copy,collections
ROOT=Path(__file__).resolve().parent.parent
P=ROOT/'source'
def load(n):return json.loads((P/n).read_text())
def write(n,o):(P/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def norm(t):return re.sub(r'[^\w$]+',' ',html.unescape(re.sub('<[^>]+>',' ',t or '')).lower()).strip()
def text(t):return html.unescape(re.sub('<[^>]+>',' ',t or ''))
def bodyhtml(parts):return ''.join('<p>'+html.escape(p)+'</p>' for p in parts if p)
master=load('master.json');ov=load('overrides.json');bykey={norm(k):k for k in ov if not k.startswith('__')}
visible_audit=ov.get('__visibleGoogleAudit',{})
visible_patches=visible_audit.get('slides',{})
plans={s['local']:s for n in ['foundation-plan-27-105.json','foundation-plan-106-185.json'] for s in load(n)}
import os
source=load(os.environ.get('FOUNDATION_SOURCE','google180-foundation-source.json'))
transcripts={}
if (P/'foundation-ocr-transcripts.json').exists():
    tx=load('foundation-ocr-transcripts.json')
    if isinstance(tx,dict):tx=tx.get('slides',tx.get('transcripts',[]))
    transcripts={int(s.get('google',s.get('googleNumber',0))):s for s in tx}
corrections={}
if (P/'foundation-copy-corrections.json').exists():
    corrections={s['google']:s for s in load('foundation-copy-corrections.json')}
used={s['existingLocal'] for s in source['slides'] if s['existingLocal']}
for i in sorted(used):
 if i<27 or i not in plans:continue
 plan=copy.deepcopy(plans[i]);key=bykey.get(norm(master[i-1]['t']),master[i-1]['t']);config={k:v for k,v in plan.items() if k not in ['title','existingMedia','reason']}
 config['omitMedia']=plan.get('omitMedia',i in [68,74,98]);config['mediaNeeded']=not plan['existingMedia'] and plan['layout'] in ['media','split']
 ov.setdefault(key,{})['foundation']=config
local=[]
for s in master:
 local.append(s|ov.get(bykey.get(norm(s.get('t')),s.get('t')),{}))
# Keys created above also need to be merged on this run.
bykey={norm(k):k for k in ov if not k.startswith('__')}
local=[s|ov.get(bykey.get(norm(s.get('t')),''),{}) for s in master]
G=[];review=[]
for row in source['slides']:
 g=row['googleNumber'];i=row['existingLocal'];reason=row['matchReason'];same=reason.startswith('exact') or reason=='raster_verified_prior_audit';approved=i and i<=26
 plan=copy.deepcopy(plans.get(i,{}));media=[m['src'] for m in row['media'] if m.get('src')]
 if i and (same or approved):
  s=copy.deepcopy(local[i-1]);f=copy.deepcopy(s.get('foundation',{}));status='ready' if approved else 'none'
 else:
  s={'a':0 if g<40 else 1 if g<133 else 3,'lv':6,'mvp':1,'t':row['title'],'b':bodyhtml(row['body']),'note':'\n'.join(row['serviceNotes'])}
  if row['eyebrow']:s['k']=row['eyebrow']
  f={k:plan[k] for k in ['type','layout','mediaBrief','animationBrief'] if k in plan}
  f['sourceOnly']=bool(row['isRasterOnly']);f['media']=media
  if row['isRasterOnly']:f['type']='content';f['layout']='media'
  if not row['title'] and row['sourceLinks']:
   url=re.sub(r'\s+','',row['sourceLinks'][0]).rstrip('/')
   s['kind']='embed';s['src']=url;s['t']='';f.update(type='motion',layout='media',media=[],demoPreviews=media,mediaNeeded=False)
  elif row['isServiceOnly'] and not media:
   s['t']='';s['b']='';f.update(type='minimal',layout='statement',mediaNeeded=True)
  # Existing video is reusable when the source page is its updated caption.
  if i and local[i-1].get('kind') in ['video','meme']:
   old=local[i-1];src=old.get('img') or old.get('src')
   if src and re.search(r'\.(mp4|webm)$',src):f['media']=[src];s['poster']=old.get('poster');f['sourceOnly']=False
  status='ready' if media else 'none'
 if not approved:
  f['local']=i if i and same else 0
  f['google']=g;f['type']=f.get('type') or ('minimal' if len(text(s.get('b'))) <110 and not media else 'content')
  f['layout']=f.get('layout') or ('statement' if f['type']=='minimal' else 'media' if media else 'editorial')
  f['mediaBrief']=f.get('mediaBrief') or ('Зберегти реальний матеріал із Google Slides.' if media else 'Текстова композиція; додаткове фото необов’язкове.')
  f['animationBrief']=f.get('animationBrief') or 'Коротка поява заголовка й контенту; фінальна композиція залишається видимою.'
  if f.get('sourceOnly') and not media:f['mediaNeeded']=True
  if f.get('mediaNeeded'):status='needed'
  elif not media and not any(s.get(k) for k in ['bg','photos','img','src']) and not re.search('<(?:img|video)',s.get('b') or ''):status='none'
  else:status='ready'
  s['foundation']=f
  if g in [1,92]:f['layout']='chat';f['type']='motion'
  # Semantic source changes do not inherit an old photograph or old headline.
  if not same and not approved:s.pop('opening',None)
 else:s.pop('foundation',None)
 tr=row.get('editableTranscript') or transcripts.get(g)
 if tr and tr.get('verified') and not approved:
  s['t']=tr['title'];s['b']=bodyhtml(tr.get('body',[]));s['k']=tr.get('eyebrow') or '';s.pop('opening',None);s.pop('bg',None);s.pop('photos',None);s.pop('src',None);s.pop('kind',None)
  f.update(local=0,sourceOnly=False,media=[],omitMedia=True,mediaNeeded=False)
  length=sum(len(p) for p in tr.get('body',[]));f['type']='minimal' if length<220 else 'content';f['layout']='statement' if length<220 else 'cards' if len(tr.get('body',[]))>=3 else 'editorial';status='none'
  if tr.get('table'):
   table=tr['table'];s['b']='<table class="fd-table"><thead><tr>'+''.join('<th>'+html.escape(str(c))+'</th>' for c in table['columns'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+('—' if c is None else html.escape(str(c)))+'</td>' for c in r)+'</tr>' for r in table['rows'])+'</tbody></table>'
   f.update(layout='comparison',type='motion')
  if tr.get('imageCrop') and media:f.update(media=media[:1],mediaCrop=tr['imageCrop'],layout='media',omitMedia=False);status='ready'
  if g in [156,159,168]:
   parts=tr['body'];s['b']='<div class="big-num">'+html.escape(parts[0])+'</div>'+bodyhtml(parts[1:]);f.update(type='motion',layout='metric')
  if g in [140,148,150,151]:
   parts=tr['body'];cols=[]
   for p in parts[:2]:
    lines=p.split('\n');cols.append('<div class="col"><h5>'+html.escape(lines[0])+'</h5>'+''.join('<div>'+html.escape(v)+'</div>' for v in lines[1:])+'</div>')
   s['b']='<div class="duo">'+''.join(cols)+'</div>'+bodyhtml(parts[2:]);f.update(layout='comparison',type='motion')
  if g in [112,120]:
   parts=tr['body'];cols=[]
   for p in parts[:2]:
    lines=p.split('\n');cols.append('<div class="col"><h5>'+html.escape(lines[0])+'</h5>'+''.join('<div>'+html.escape(v)+'</div>' for v in lines[1:])+'</div>')
   s['b']='<div class="duo">'+''.join(cols)+'</div>'+bodyhtml(parts[2:]);f.update(layout='comparison',type='motion')
  if g in [115,116,121,123]:f.update(type='motion',layout='cards')
  if g==122:
   agent='<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="6" width="14" height="14" rx="3"/><path d="M12 2v4M8 11h1m6 0h1M8 16h8M2 10v6m20-6v6"/></svg>'
   person='<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="7" r="4"/><path d="M4 22v-4a8 8 0 0 1 16 0v4"/></svg>'
   s['b']=bodyhtml(tr['body'][:1])+'<div class="fd-flow">'+''.join('<span>'+html.escape(p.strip())+'</span>' for p in tr['body'][1].split('→'))+'</div><p class="mut fd-legend">'+agent+' — работает AI-агент · '+person+' — это вы</p>';f.update(type='motion',layout='timeline')
  if g==135:
   s['b']='<div class="fd-stats">'+''.join('<div><b>'+html.escape(p.split('\n')[0])+'</b><span>'+html.escape(p.split('\n')[-1])+'</span></div>' for p in tr['body'][:4])+'</div>'+bodyhtml(tr['body'][4:]);f.update(type='motion',layout='metric');s['note']+='\n60% у джерельних нотатках позначено як заглушку; потрібне підтвердження перед ефіром.'
  if g==96 and media:f.update(media=[media[-1]],mediaCrop={'x':.012,'y':.188,'w':.952,'h':.67},layout='media',type='content',omitMedia=False);status='ready'
  if g==119 and media:f.update(media=[media[-1]],mediaCrop={'x':.47,'y':.073,'w':.52,'h':.88},portrait=True,layout='media',type='content',omitMedia=False);status='ready'
  if g in [137,147,149,167,174]:f.update(type='motion',layout='cards')
  if g==139:
   s['b']='<div class="fd-speed">'+''.join('<div><span>'+html.escape(p.split(' — ')[0])+'</span><b>'+html.escape(p.split(' — ')[-1])+'</b></div>' for p in tr['body'][:5])+'</div>'+bodyhtml(tr['body'][5:]);f.update(type='motion',layout='timeline')
  if g in [157,158]:
   parts=tr['body'];s['b']='<div class="fd-bars"><div><span>'+html.escape(parts[0])+'</span><i style="width:100%"></i></div><div><span>'+html.escape(parts[1])+'</span><i style="width:12.5%"></i></div></div>'+bodyhtml(parts[2:]);f.update(layout='diagram',type='motion')
  if g==153 and len(media)>1:f.update(media=[media[-1]],layout='media',type='content',omitMedia=False);status='ready'
  if g==177 and media:
   crops=[(.037,.432,.218,.152),(.265,.432,.218,.152),(.492,.432,.218,.152),(.720,.432,.218,.152)]
   figures=[]
   for label,(cx,cy,cw,ch) in zip(tr['body'][:4],crops):
    figures.append('<figure><div><img src="'+media[0]+'" alt="" style="position:absolute;width:'+str(100/cw)+'%;height:'+str(100/ch)+'%;max-height:none;left:'+str(-cx/cw*100)+'%;top:'+str(-cy/ch*100)+'%;object-fit:fill"></div><figcaption>'+html.escape(label)+'</figcaption></figure>')
   s['b']='<div class="fd-site-grid">'+''.join(figures)+'</div>'+bodyhtml(tr['body'][4:5]);s['disc']=1;f.update(layout='editorial',type='content')
  f['mediaBrief']='Редагований текст відновлено з видимого оригіналу; додаткове фото необов’язкове.'
  if f.get('media'):f['mediaBrief']='Справжнє фото або скриншот із джерела, збережений окремо від редагованого тексту.'
  if g==177:f['mediaBrief']='Чотири реальні приклади сайтів із джерела; підписи редагуються окремо.'
  if tr.get('table'):f['mediaBrief']='Редагована таблиця восьми послуг; останній нерозбірливий показник конкуренції позначено тире.'
  if g==135:f['mediaBrief']='Чотири числові картки з джерела. Значення60% у нотатках автора позначене як заглушка й потребує підтвердження.'
  f['animationBrief']={'comparison':'Коротка поява колонок порівняння; фінальні значення залишаються видимими.','metric':'Поява числових акцентів і підписів, без нескінченного повтору.','timeline':'Послідовна поява схеми; весь ланцюжок залишається на одному слайді.','diagram':'Поява порівняння та заповнення смуг зліва направо.','cards':'Швидка почергова поява змістових карток.','statement':'Спокійна поява заголовка й тези.','media':'Коротка поява тексту та зображення.','editorial':'Коротка поява заголовка й текстових блоків.'}.get(f['layout'],'Коротка поява композиції.')
  s['foundation']=f
 if g in corrections:
  fix=corrections[g]
  for key in ['t','title','b']:
   if key in fix:s['t' if key=='title' else key]=fix[key]
  if g==93:i=96;s['foundation'].update(local=96,layout='timeline',type='motion',omitMedia=True,media=[]);s.pop('bg',None)
  briefs={32:'Велике «на90% дешевле» за актуальним текстом Google; ціна й умова залишаються разом.',63:'Справжній скриншот балансу; текст винесено в окрему зону.',78:'Одна велика теза на темному фоні, без доданих речень.',92:'Одна вступна репліка за актуальним джерелом, без доданого листування.',93:'Ланцюжок робіт за вечір із точними етапами з джерела; додаткове фото не потрібне.',108:'Одна велика теза за актуальним текстом Google.'}
  if g in briefs:f['mediaBrief']=briefs[g]
  if g==92:f.update(type='minimal',layout='statement',animationBrief='Коротка поява вступної репліки.');status='none'
 if s.get('kind')=='embed':f['mediaNeeded']=False;status='ready'
 if g==125:
  s.pop('bg',None);s.pop('photos',None);f.update(type='minimal',layout='statement',media=[],omitMedia=True,mediaNeeded=False,mediaBrief='Чиста типографічна теза на темному фоні; фото не потрібне.',animationBrief='Коротка поява заголовка і пояснення.');status='none'
 if s.get('kind')=='embed' and f.get('demoPreviews'):
  f['mediaBrief']='Справжні прев’ю з Google Slides і кнопка відкриття живої демонстрації: '+s['src']
  f['animationBrief']='Поява вікна з прев’ю; живий сайт відкривається окремо кнопкою.'
 if g in [131,143]:s['b']=bodyhtml(row['body'])
 if g==144:
  s['b']='<div class="route">'+''.join('<div class="rt"><i>'+str(n)+'</i><b>'+h+'</b><span>'+b+'</span></div>' for n,h,b in [(1,'Спрос вырос вдвое','бизнесу нужно то, чего год назад не существовало'),(2,'Рынок ещё пустой','в вашем городе эти услуги не делает почти никто'),(3,'Исполнитель бесплатный','работу делает AI-агент, а не вы')])+'</div><p class="acc">Дальше покажу каждое</p>'
 if g==152:
  s['b']='<div class="duo"><div class="col"><h5>Исчезнет к 2030-му</h5><div class="big">92 млн</div><div>рабочих мест по миру</div></div><div class="col good"><h5>Появится к 2030-му</h5><div class="big">170 млн</div><div>новых рабочих мест</div></div></div><p class="acc">Работы стало больше, просто она другая</p>'
 if g==136:status='needed';f['mediaBrief']='У Google тут лише службова фраза «распределить слайды». Потрібен зміст або рішення прибрати цю сторінку.'
 # Visible PDF evidence has final priority over hidden native text and old local matches.
 patch=visible_patches.get(row['googleObjectId'])
 # Explicitly omitted source pages (duplicate hero, Google 1) are not shown at all.
 if patch and patch.get('omit'):continue
 if patch:
  if patch.get('inheritLocal'):
   i=patch['inheritLocal'];s=copy.deepcopy(local[i-1]);s.pop('foundation',None);f={};approved=bool(s.get('opening'))
  for key in patch.get('remove',[]):s.pop(key,None)
  for key,value in patch.get('set',{}).items():s[key]=copy.deepcopy(value)
  if 'foundation' in patch:
   f=copy.deepcopy(s.get('foundation',f));f.update(copy.deepcopy(patch['foundation']));f['google']=g;s['foundation']=f;approved=False
  status=patch.get('mediaStatus',status)
  s['visibleAudit']={'evidence':f'source/audit-final-2026-09-11/rendered/slide-{g:03}.png','reason':patch.get('reason','')}
 s['googleNumber']=g;s['googleObjectId']=row['googleObjectId'];s['originalLocal']=i
 if row.get('googleNow'):s['googleNow']=row['googleNow'];f['googleNow']=row['googleNow']
 # The approved life-line chapter is keyed by physical source objectId, not
 # duplicate headlines or the shifted display-page number.
 life=ov.get('__lifeStory',{}).get('slides',{}).get(row['googleObjectId'])
 if life:
  s['lifeStory']=copy.deepcopy(life)
  f.update(type='motion',layout='life-line',mediaNeeded=False,mediaBrief='Усі змістові фото цього Google-слайда; окремі композиції для коротких тез, розповіді й документів.',animationBrief='Спільна лінія життя знизу, перехід за кліком, точки для навігації та збільшення фото.');status='ready'
 s['note']=(s.get('note') or '')+'\nGoogle Slides #'+str(g)+' · '+row['googleObjectId']
 if row['isRasterOnly'] and not approved:s['note']+='\nТекст відновлено з видимого растрового оригіналу.' if tr and tr.get('verified') else '\nОригінальний растровий матеріал: текст збережено в зображенні.'
 # Presentation parts require explicit, source-bound user authorization.
 # ObjectId patches take priority; legacy title-keyed route parts stay supported.
 presentation=(patch or {}).get('presentationParts') or ov.get(bykey.get(norm(row['title']),''),{}).get('presentationParts')
 variants=[s]
 if presentation:
  if presentation.get('sourceGoogleObjectId')!=row['googleObjectId'] or not presentation.get('authorization'):
   raise ValueError('Presentation parts require explicit authorization and the matching source objectId: '+row['title'])
  parts=presentation.get('slides',[])
  if len(parts)<2:raise ValueError('Presentation parts must contain at least two slides: '+row['title'])
  variants=[]
  for part in parts:
   slide=copy.deepcopy(s);slide.update(copy.deepcopy(presentation.get('set',{})));slide.update(copy.deepcopy(part))
   slide['t']=part.get('t',s['t']) if presentation.get('allowPartTitles') else s['t']
   slide['googleNumber']=g;slide['googleObjectId']=row['googleObjectId'];slide['originalLocal']=i
   slide['sourceGoogleNumber']=g;slide['sourceGoogleObjectId']=row['googleObjectId']
   variants.append(slide)
 for part,slide in enumerate(variants,1):
  display=len(G)+1;sf=slide.get('foundation',f)
  if presentation:slide.update(displayNumber=display,presentationPart=part,presentationPartCount=len(variants))
  G.append(slide)
  title=text(slide.get('t')) or ('Матеріал із Google Slides' if row['isRasterOnly'] else 'Демонстрація' if row['sourceLinks'] else 'Місце для контенту')
  typ=sf.get('type','content') if not approved else ('video' if i==1 else 'motion' if i in [3,15,17,18,20,21,24,26] else 'content' if i in range(5,14) else 'minimal')
  item={'google':g,'displayNumber':display,'local':i,'title':title,'type':typ,'layout':sf.get('layout','approved'),'mediaStatus':presentation.get('mediaStatus',status) if presentation else status,'mediaBrief':sf.get('mediaBrief') or 'Погоджене оформлення збережено.','animationBrief':sf.get('animationBrief') or 'Наявна погоджена поведінка.','url':f'google180.html?square&clean&s={display}&v=foundation','thumbnail':f'shots/foundation/g{g:03}-part{part}.jpg' if presentation else f'shots/foundation/g{g:03}.jpg','sourceOnly':bool(sf.get('sourceOnly')),'sourceObjectId':row['googleObjectId'],'matchReason':reason}
  if presentation:item.update(presentationPart=part,presentationPartCount=len(variants))
  review.append(item)
attention={27:'Залишився фінальний моушн: три роботи під кришками, які піднімаються по черзі. Зараз використано погоджений чорновий кадр.',135:'Авторська позначка:60% — заглушка. Підтвердити або замінити число.',136:'У джерелі лише «распределить слайды». Потрібен зміст або рішення прибрати сторінку.',173:'Останній показник конкуренції нерозбірливий у джерелі; зараз стоїть тире.'}
for item in review:
 if item['google'] in attention:item['reviewNote']=attention[item['google']]
# Порядок/приховування/нові слайди за Google-ревізією (source/_deck_order.py, дані в ov['__deckOrder']).
if ov.get('__deckOrder'):
 import _deck_order
 G=_deck_order.apply(G,ov['__deckOrder'],visible_patches)
ov['__google180']={'sourceRevision':visible_audit.get('sourceRevision',source['revisionId']),'scope':'Google physical slides 1–180','slides':G}
write('overrides.json',ov);write('foundation-review-data.json',review)
(ROOT/'js/foundation-review-data.js').write_text('window.FOUNDATION_REVIEW='+json.dumps(review,ensure_ascii=False)+';\n')
page=(ROOT/'index.html').read_text().replace('js/slides.js?','js/slides-google180.js?').replace('<title>AI-Оператор — преза эфира · v5</title>','<title>AI-Оператор · Google 1–180 · базове оформлення</title>')
(ROOT/'google180.html').write_text(page)
print('Prepared',len(G),'Google slides; types:',dict(collections.Counter(s['type'] for s in review)))
