"""Visual redesign, stable U001–U055 selection. Invoked by the sales source builder."""
import re, html

def esc(x): return html.escape(str(x),quote=True)
def txt(x): return re.sub(r'&lt;(/?)(em|b|br)/?&gt;',r'<\1\2>',esc(x or ''))
def p(x,cls=''): return '<p class="'+cls+'">'+txt(x)+'</p>' if x else ''
def image(src,cls=''): return '<img class="'+cls+'" src="'+esc(src)+'" alt="">'
def end(s): return p(s.get('final'),'sv-end')+('<p class="sv-disc">Результаты индивидуальны и не являются типичными</p>' if s.get('disc') else '')
def svg(body,vb='0 0 800 300'): return '<svg class="sv-drawing" viewBox="'+vb+'" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'+body+'</svg>'
def media(m):
 if not m:return ''
 if m.get('video'): return '<div class="sv-media sl2-media"><video src="'+m['video']+'"'+(' poster="'+m['poster']+'"' if m.get('poster') else '')+' muted playsinline loop preload="metadata"></video></div>'
 if m.get('fan'): return '<div class="sv-fan">'+''.join(image(x) for x in m['fan'])+'</div>'
 if m.get('img'):return '<div class="sv-media">'+image(m['img'])+'</div>'
 return ''
def art(src,kind='scene'): return '<div class="sv-'+kind+'">'+image(src)+'</div>' if src else ''
def item_list(items):
 return ''.join('<div class="sv-list-row"><i></i>'+txt(it.get('h','') if isinstance(it,dict) else it)+'</div>' for it in items)
def price(s):return '<div class="sv-value"><div><small>Ценность элемента</small><b>'+txt(s['value'])+'</b></div><div><small>Общая ценность</small><b>'+txt(s['acc'])+'</b></div><div class="sv-progress">'+''.join('<i class="'+('on' if x<int(s['num']) else '')+'"></i>' for x in range(17))+'</div></div>'
def element(s):
 u=s['u']; h=p(s.get('d'),'sv-description')+p(s.get('extra'),'sv-extra')
 if s.get('list'):
  h+='<div class="sv-agent-list">'+''.join('<div><span>'+txt(x['n'])+'</span><b>'+txt(x['h'])+'</b><strong>'+txt(x['price'])+'</strong></div>' for x in s['list'])+'</div>'
 elif s.get('places'):
  h+='<div class="sv-places">'+''.join('<div class="'+x['tone']+'"><b>'+txt(x['h'])+'</b><span>'+txt(x['d'])+'</span></div>' for x in s['places'])+'</div>'
 elif s.get('media'): h+='<div class="sv-proof">'+media(s['media'])+'</div>'
 elif s.get('lines'):h+='<div class="sv-element-lines">'+''.join(p(x) for x in s['lines'])+'</div>'
 if s.get('bg') and not s.get('list') and not s.get('places'):h+=art(s['bg'],'object')
 if u=='U036': h+='<div class="sv-discount">−75<span>%</span></div>'
 if u=='U039': h+=svg('<path d="M200 145C200 30 600 30 600 145M600 155C600 270 200 270 200 155" stroke="currentColor" stroke-width="3"/><path d="m578 127 22 25 22-25M178 173l22-25 22 25" stroke="currentColor" stroke-width="3"/>','0 0 800 300')
 return h+price(s)
def chapter(s):
 n=s['visual']['chapter'];h='<div class="sv-route">'+''.join('<div class="'+('active' if i==n else 'past' if i<n else '')+'"><b>0'+str(i)+'</b><span>'+x+'</span></div>' for i,x in enumerate(['Фундамент','Витрина','Контент','Клиенты','Продажи'],1))+'</div>'
 if s['visual'].get('art'):h+=art(s['visual']['art'],'chapter-art')
 else:
  shapes={1:'<path d="M70 220h240v-45H70zM95 160h190v-45H95zM120 100h140V55H120z" fill="#fdd506"/><path d="M340 250h380M450 220V85m100 135V50m100 170V120" stroke="#665a39" stroke-width="5"/>',2:'<path d="M60 210 190 80h420l130 130Z" fill="#fdd506"/><path d="M105 235h590v50H105z" fill="#594f31"/><rect x="220" y="20" width="360" height="200" rx="10" fill="#eee8db"/><path d="M250 60h300M250 95h150M250 125h200M250 160h120" stroke="#1a1711" stroke-width="12"/>',4:'<circle cx="570" cy="140" r="110" stroke="#51482c" stroke-width="3"/><circle cx="570" cy="140" r="72" stroke="#74642b" stroke-width="3"/><circle cx="570" cy="140" r="29" fill="#fdd506"/><path d="M80 140h420m-90-45 90 45-90 45" stroke="#fdd506" stroke-width="9"/><circle cx="100" cy="65" r="18" fill="#f0e9db"/><circle cx="180" cy="240" r="18" fill="#f0e9db"/>',5:'<rect x="85" y="45" width="220" height="190" rx="24" fill="#f0e9db"/><path d="m275 245-30 40-15-50" fill="#f0e9db"/><path d="M125 95h140m-140 40h110m-110 40h80" stroke="#5b5549" stroke-width="9"/><path d="M345 145h120m-30-25 30 25-30 25" stroke="#fdd506" stroke-width="6"/><circle cx="580" cy="145" r="100" fill="#fdd506"/><path d="m528 147 35 35 74-78" stroke="#18150e" stroke-width="12"/>'}
  h+='<div class="sv-chapter-drawing">'+svg(shapes.get(n,''))+'</div>'
 h+='<div class="sv-modules">'+''.join('<div><small>'+txt(x['m'])+'</small><section><h3>'+txt(x['h'])+'</h3>'+p(x.get('d'))+'</section>'+(('<strong>'+txt(x['n'])+'<small>задач</small></strong>') if x.get('n') else '')+'</div>' for x in s['modules'])+'</div>'
 r=s.get('result',{});g=s.get('give',{})
 h+='<div class="sv-result">'+(('<b>'+txt(g.get('v',''))+'<small>'+txt(g.get('h',''))+'</small></b>') if isinstance(g,dict) and g else '')+'<div><small>'+txt(r.get('h',''))+'</small>'+p(r.get('d'))+'</div></div>'
 return h

def render(s,body,bl):
 v=s.get('visual');
 if not v or v.get('version')!='sales3':return body,bl
 mode=v['mode'];u=s['u'];h=''
 marker='<i class="sv-marker sv-'+mode+' sv-'+u+(' sv-light' if v.get('light') else '')+'" hidden></i>'
 if mode=='desk':
  stage='<span class="sv-substage">02 / 02</span><i class="sv-desk-expanded" hidden></i>' if v.get('stage')==2 else ''
  return marker+stage+body+'<small class="sv-mock-label">Концепция рабочего процесса</small>',bl
 if mode=='desk-intro':
  offer_lines=s.get('lines',[])
  points=offer_lines[0].split(' · ') if offer_lines else []
  h=marker+'<span class="sv-substage">01 / 02</span><div class="sv-offer-copy"><ul class="sv-offer-points">'+''.join('<li>'+txt(x)+'</li>' for x in points)+'</ul><div class="sv-offer-audience">'+''.join(p(x) for x in offer_lines[1:])+'</div></div>'
  h+='<div class="sv-offer-video"><video data-src="'+esc(v['video'])+'" data-poster="'+esc(v['poster'])+'" muted loop playsinline preload="none"></video></div>'+p(s.get('final'),'sv-offer-final')
  return h,{'kind':'s16','v2':True,'layout':'s16-sales3','eyebrow':s.get('k','')}
 bl={'kind':'s16','v2':True,'layout':'s16-sales3','eyebrow':s.get('k','')}
 if mode=='element':h=element(s)
 elif mode=='chapter':h=chapter(s)
 elif mode=='iceberg':
  h=art(s['bg'])
  for cls,key in [('ice-top','top'),('ice-bottom','bottom')]:
   d=s[key];h+='<div class="sv-'+cls+'"><small>'+txt(d['k'])+'</small>'+''.join(p(x) for x in d['items'])+'</div>'
 elif mode=='compare':
  h+='<div class="sv-compare">'
  for i,c in enumerate(s['cols']):
   h+='<div class="'+('win' if i else 'dim')+'"><div class="sv-compare-art">'+svg(('<path d="M90 160 180 75l100 65 100-60 95 85 120-90 100 85" stroke="#a49c8c" stroke-width="7"/>' if i==0 else '<path d="M90 160H680m-45-45 45 45-45 45" stroke="#fdd506" stroke-width="7"/>'))+'</div><h3>'+txt(c['h'])+'</h3>'+item_list(c.get('items',[]))+'</div>'
  h+='</div>'+end(s)
  if u=='U008':
   drawings=re.findall(r'<svg.*?</svg>',h)
   closed=svg('<rect x="205" y="85" width="380" height="150" rx="34" fill="#bcb3a1"/><rect x="205" y="55" width="380" height="150" rx="34" fill="#ddd5c6" stroke="#8d8474" stroke-width="3"/><circle cx="395" cy="130" r="43" stroke="#8d8474" stroke-width="7"/><path d="M395 70v63" stroke="#8d8474" stroke-width="8"/>')
   opened=svg('<path d="M155 240h490l-45-65H200z" fill="#7e7563"/><path d="M180 167h440l-40-60H220z" fill="#d5c9b0"/><path d="M255 45h290v55H255z" fill="#fdd506"/><path d="M260 208v-53m135 53v-53m140 53v-53" stroke="#fdd506" stroke-width="4"/><circle cx="260" cy="224" r="13" fill="#fdd506"/><circle cx="395" cy="224" r="13" fill="#fdd506"/><circle cx="535" cy="224" r="13" fill="#fdd506"/>')
   h=h.replace(drawings[0],closed,1).replace(drawings[1],opened,1)
  if u=='U054':
   h=h.replace('class="dim"','class="win"',1).replace('class="win"','class="fit-first"',1)
   drawings=re.findall(r'<svg.*?</svg>',h)
   good=svg('<path d="M210 240V30h260v210M180 240h340M470 30l125 40v230l-125-60" stroke="#8a7731" stroke-width="7"/><circle cx="500" cy="145" r="8" fill="#8a7731"/>')
   bad=svg('<path d="M230 245V35h340v210M200 245h400" stroke="#8a8273" stroke-width="7"/><path d="m335 105 100 90m0-90-100 90" stroke="#8a8273" stroke-width="9"/>')
   h=h.replace(drawings[0],good,1).replace(drawings[1],bad,1)
 elif mode=='statement':
  h=art(s.get('bg') or v.get('art'))+'<div class="sv-statement-copy">'+''.join(p(x) for x in s.get('lines',[]))+p(s.get('final'),'sv-statement-final')+'</div>'
 elif mode=='steps':
  h='<div class="sv-steps">'+''.join('<div><b>'+txt(x['n'])+'</b><h3>'+txt(x['h'])+'</h3>'+p(x.get('d'))+'</div>' for x in s['items'])+'</div><div class="sv-screen">'+media(s.get('media'))+'</div>'+end(s)
 elif mode=='screen':
  h='<div class="sv-intro">'+''.join(p(x) for x in s.get('lines',[]))+'</div><div class="sv-screen"><div class="sv-browser-bar"><i></i><i></i><i></i><span>'+txt(s.get('link',''))+'</span></div>'+image(s['img'])+'</div>'
 elif mode=='services':
  h='<div class="sv-services" style="--count:'+str(len(s['cards']))+'">'
  for c in s['cards']:
   h+='<article>'+media(c.get('media'))+('<div class="sv-demo-caption"><small>Пример</small>'+''.join('<span>'+txt(x.get('t',''))+'</span>' for x in c.get('demo',[]))+'</div>' if c.get('demo') else '')+'<div class="sv-service-copy"><h3>'+txt(c['h'])+'</h3>'+p(c.get('d'))+''.join(p(x) for x in c.get('lines',[]))+'<strong>'+txt(c.get('price',''))+'</strong>'+p(c.get('pm'),'sv-pm')+p(c.get('tag'),'sv-tag')+'</div></article>'
  h+='</div>'
  if s.get('bubble'):h+='<div class="sv-bubble">'+p(s['bubble']['q'])+p(s['bubble']['a'])+'</div>'
  h+=end(s)
 elif mode=='cards':
  cards=s.get('cards',[]);h=''
  if s.get('band'):h+=p(s['band']['t'],'sv-band')
  if s.get('flow'):h+='<div class="sv-flow"><b>'+txt(s['flow']['from'])+'</b><span>→</span><b>'+txt(s['flow']['to'])+'</b></div>'
  h+='<div class="sv-cards" style="--count:'+str(len(cards))+'">'
  for i,c in enumerate(cards):h+='<article>'+media(c.get('media'))+'<small>'+str(i+1).zfill(2)+'</small><h3>'+txt(c['h'])+'</h3>'+p(c.get('d'))+p(c.get('v'),'sv-card-value')+p(c.get('vd'))+'</article>'
  h+='</div>'+end(s)
  if u=='U030':h+=art(v.get('art'),'kit-art')
  if u=='U012':h+='<div class="sv-conveyor-lines">'+svg('<path d="M400 0v530M385 64h30M385 200h30M385 336h30M385 472h30" stroke="#6c5d24" stroke-width="2"/><g fill="#fdd506">'+''.join('<circle cx="400" cy="'+str(y)+'" r="5"/>' for y in [64,200,336,472])+'</g>','0 0 800 540')+'</div>'
 elif mode=='stats':
  st=s['stats'];h='<div class="sv-stats">'+''.join('<div><b>'+txt(x['v'])+'</b><span>'+txt(x['h'])+'</span></div>' for x in st[:-1])+'</div><div class="sv-income"><small>'+txt(st[-1]['h'])+'</small><b>'+txt(st[-1]['v'])+'</b></div>'+end(s)
 elif mode=='package':
  rows=s['rows'];h='<div class="sv-ledger">'
  for part in [rows[:8],rows[8:]]:
   h+='<div>'
   for r in part:
    h+='<div class="sv-ledger-row'+(' off' if r.get('off') else '')+'"><small>'+txt(r.get('n'))+'</small><span>'+txt(r['h'])+'</span><b>'+txt(r.get('price'))+'</b>'
    if r.get('sub'):h+='<div class="sv-ledger-sub">'+''.join('<div class="'+('off' if x.get('off') else '')+'"><span>'+txt(x['h'])+'</span><b>'+txt(x.get('price'))+'</b></div>' for x in r['sub'])+'</div>'
    h+='</div>'
   h+='</div>'
  h+='</div><div class="sv-total"><span>'+txt(s['total']['h'])+'</span><b>'+txt(s['total']['v'])+'</b></div>'+end(s)
 elif mode=='packages':
  h='<div class="sv-packages">'
  for i,c in enumerate(s['packs']):
   h+='<article class="p'+str(i)+'"><div class="sv-pack-top"><small>'+txt(c.get('tag',''))+'</small><h3>'+txt(c['name'])+'</h3></div>'
   if c.get('value'):h+='<div class="sv-pack-value">'+txt(c['value'])+'</div>'
   if c.get('count'):
    count=str(c['count']).split(' ',1)
    h+='<div class="sv-pack-count">'+txt(count[0])+('<span> '+txt(count[1])+'</span>' if len(count)>1 else '')+'<small>'+txt(c.get('countd'))+'</small></div>'
   for x in c.get('metrics',[]):h+='<div class="sv-pack-metric"><span>'+txt(x['h'])+'</span><b>'+txt(x['v'])+'</b></div>'
   for x in c.get('chips',[]):h+=p(x,'sv-pack-chip')
   h+=p(c.get('sub'))+'</article>'
  h+='</div>'+end(s)
 else: raise ValueError(mode)
 return marker+h,bl
