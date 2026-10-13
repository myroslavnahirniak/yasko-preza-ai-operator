# 21.09 · продаюча частина: генерує presentationParts для джерельного слайда 303 (g3f9b3adf0b8_0_2226)
# з даних source/google-sales-2026-09-21/data/sec-*.json (сім'ї шаблонів — див. BUILD-PLAN.md), старі 304–342 → omit.
# Запуск: python3 source/_patch_sales_2109.py [--test data/_test.json]   → далі стандартна збірка (_foundation_prepare + _build_slides).
import json,re,sys,os,glob,html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,'source/google-sales-2026-09-21')
SRC_OID='g3f9b3adf0b8_0_2226'
OLD_OIDS=['g3f9b3adf0b8_0_2233','g3f9b3adf0b8_0_2240','g3f9b3adf0b8_0_2247','g3f9b3adf0b8_0_2254','g3f9b3adf0b8_0_2261','g3f9b3adf0b8_0_2270','g3f9b3adf0b8_0_2278','g3f9b3adf0b8_0_2287','g3f9b3adf0b8_0_2293','g3f9b3adf0b8_0_2300','g3f9b3adf0b8_0_2306','g3f9b3adf0b8_0_2313','g3f9b3adf0b8_0_2320','g3f9b3adf0b8_0_2327','g3f9b3adf0b8_0_2334','g3f9b3adf0b8_0_2342','g3f9b3adf0b8_0_2349','g3f9b3adf0b8_0_2356','g3f9b3adf0b8_0_2363','g3f9b3adf0b8_0_2371','g3f9b3adf0b8_0_2378','g3f9b3adf0b8_0_2386','g3f9b3adf0b8_0_2399','g3f9b3adf0b8_0_2406','g3f9b3adf0b8_0_2414','g3f9b3adf0b8_0_2420','g3f9b3adf0b8_0_2427','g3f9b3adf0b8_0_2434','g3f9b3adf0b8_0_2442','g3f9b3adf0b8_0_2449','g3f9b3adf0b8_0_2456','g3f9b3adf0b8_0_2463','g3f9b3adf0b8_0_2470','g3f9b3adf0b8_0_2477','g3f9b3adf0b8_0_2484','g3f9b3adf0b8_0_2490','g3f9b3adf0b8_0_2497','g3f9b3adf0b8_0_2505','g3f9b3adf0b8_0_2513']
CTA='#ОПЛАТА'
# ---------- text helpers ----------
def T(s):
    """escape text but keep <em>, <br>, <b>"""
    if s is None: return ''
    s=html.escape(str(s),quote=False)
    for tag in ('em','b','br'):
        s=s.replace('&lt;'+tag+'&gt;','<'+tag+'>').replace('&lt;/'+tag+'&gt;','</'+tag+'>')
    return s
def num(s):
    """'$12.500' -> 12500 ; '$1.000–$3.000' -> None"""
    if s is None: return None
    m=re.fullmatch(r'\s*\$?\s*([\d.\s]+)\s*',str(s))
    if not m: return None
    try: return int(m.group(1).replace('.','').replace(' ',''))
    except: return None
ICONS={
 'site':'<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M3 9h18M8 18v3M16 18v3"/>',
 'design':'<path d="M4 20h16M6 16l10-10 2 2L8 18H6z"/>',
 'video':'<path d="M15 10l4.5-2.5v9L15 14M4 7h11v10H4z"/>',
 'content':'<path d="M4 4h16v12H4zM8 8h8M8 12h5"/><path d="M4 20h16"/>',
 'ads':'<path d="M4 10v4h3l6 4V6L7 10zM16 9a4 4 0 0 1 0 6M18.5 6.5a8 8 0 0 1 0 11"/>',
 'seo':'<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4M8 11h6M11 8v6"/>',
 'seller':'<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
 'chat':'<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
 'hunt':'<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4M11 8v6M8 11h6"/>',
 'shield':'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="m9 12 2 2 4-4"/>',
 'coffee':'<path d="M5 8h11v6a5 5 0 0 1-10 0zM16 9h2a2 2 0 0 1 0 4h-2M7 4v2M10 4v2M13 4v2"/>',
 'doc':'<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
 'canvas':'<rect x="3" y="4" width="18" height="13" rx="1.5"/><path d="M8 21h8M12 17v4M7 12l3-3 3 3 2-2 2 2"/>',
 'key':'<circle cx="8" cy="12" r="4"/><path d="M12 12h9M18 12v3M15 12v2"/>',
 'check':'<path d="m5 12 4 4L19 6"/>',
 'x':'<path d="M6 6l12 12M18 6L6 18"/>',
 'clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'calendar':'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 'phone':'<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
 'map':'<path d="M3 6l6-2 6 2 6-2v14l-6 2-6-2-6 2zM9 4v14M15 6v14"/>',
 'star':'<path d="M12 3l2.5 5 5.5.8-4 3.9.9 5.5-4.9-2.6L7.1 18.2l.9-5.5-4-3.9L9.5 8z"/>',
 'gift':'<rect x="3" y="8" width="18" height="4"/><path d="M5 12v9h14v-9M12 8v13M12 8c-2 0-4-1-4-3s3-2 4 3c1-5 4-5 4-3s-2 3-4 3"/>',
 'people':'<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-4 3-6 6-6s6 2 6 6M15 15c3 0 6 1.5 6 5"/>',
 'book':'<path d="M4 19V5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2zm0 0a2 2 0 0 0 2 2h13"/>',
 'update':'<path d="M20 12a8 8 0 1 1-2.3-5.7M20 4v5h-5"/>',
 'board':'<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M8 21h8M7 9h4M7 13h6M14 9h3"/>',
 'script':'<path d="M6 3h12v18H6zM9 8h6M9 12h6M9 16h4"/>',
 'link':'<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
 'session':'<circle cx="12" cy="12" r="9"/><path d="M8 12h8M12 8v8"/>',
 'bank':'<path d="M3 10l9-6 9 6M5 10v8M9 10v8M15 10v8M19 10v8M3 20h18"/>',
 'arrow':'<path d="M5 12h14M13 6l6 6-6 6"/>',
 'task':'<rect x="4" y="4" width="16" height="16" rx="2"/><path d="m8 12 3 3 5-6"/>',
 'module':'<rect x="3" y="3" width="8" height="8"/><rect x="13" y="3" width="8" height="8"/><rect x="3" y="13" width="8" height="8"/><rect x="13" y="13" width="8" height="8"/>',
 'user':'<circle cx="12" cy="9" r="4"/><path d="M4 21c1-5 5-7 8-7s7 2 8 7"/>',
 'money':'<circle cx="12" cy="12" r="9"/><path d="M12 7v10M9.5 9.5h4a1.5 1.5 0 0 1 0 3h-3a1.5 1.5 0 0 0 0 3h4"/>',
 'lock':'<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
 'cursor':'<path d="M5 3l14 8-6 2-2 6z"/>',
 'sparkle':'<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2 2M16 16l2 2M6 18l2-2M16 8l2-2"/>',
}
def ico(k,size=''):
    p=ICONS.get(k or '','') or ICONS['sparkle']
    return '<svg class="sl2-ico'+(' '+size if size else '')+'" viewBox="0 0 24 24" aria-hidden="true">'+p+'</svg>'
def svg(k,cls=''):
    return '<svg'+(' class="'+cls+'"' if cls else '')+' viewBox="0 0 24 24" aria-hidden="true">'+ICONS.get(k,'')+'</svg>'
ARROW='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
_d=[0]
def A(cls='',step=.12,start=None):
    """class + animation delay for staggered appear"""
    if start is not None:_d[0]=start
    d=_d[0];_d[0]=round(d+step,2)
    return ' class="sl2-a'+(' '+cls if cls else '')+'" style="--d:'+('%.2f'%d)+'s"'
def media(m,extra_cls=''):
    if not m: return ''
    if 'ph' in m: return '<div class="sl2-media sl2-ph '+extra_cls+'"><div>'+T(m['ph'])+'</div></div>'
    if 'video' in m:
        p=m.get('poster'); return '<div class="sl2-media '+extra_cls+(' fit' if m.get('fit') else '')+'"><video src="'+m['video']+'"'+(' poster="./'+p+'"' if p else '')+' muted playsinline loop preload="metadata"></video></div>'
    if 'fan' in m: return '<div class="sl2-media fan '+extra_cls+'">'+''.join('<img src="'+s+'" alt="">' for s in m['fan'][:3])+'</div>'
    if 'img' in m: return '<div class="sl2-media '+extra_cls+(' top' if m.get('top',True) else '')+(' fit' if m.get('fit') else '')+'"><img src="'+m['img']+'" alt="'+T(m.get('alt',''))+'"></div>'
    if 'icon' in m: return '<div class="sl2-media icon '+extra_cls+'">'+ico(m['icon'])+'</div>'
    return ''
def lines(ls,cls='sl2-lines',anim=True):
    if not ls: return ''
    return '<div class="'+cls+'">'+''.join('<p'+(A() if anim else '')+'>'+T(l)+'</p>' for l in ls)+'</div>'
def final(s,plain=False,left=False):
    return ('<p'+A('sl2-final'+(' plain' if plain else '')+(' left' if left else '')+(' long' if len(str(s))>70 else ''))+'>'+T(s)+'</p>') if s else ''
def disc(s):
    return '<p class="sl2-disc">Результаты индивидуальны и не являются типичными</p>' if s.get('disc') else ''
def bgmark(s):
    return ('<i class="sl2-bg-'+(s.get('bgmode') or 'bottom')+'" hidden></i>') if s.get('bg') else ''
def btn(text,terms=None):
    h='<div'+A('sl2-ctawrap')+'><a class="sl2-btn" href="'+CTA+'" target="_blank" rel="noopener">'+T(text)+ARROW+'</a>'
    if terms: h+='<p class="sl2-terms">'+T(terms)+'</p>'
    return h+'</div>'
# ---------- families ----------
def f_statement(s):
    faq=s.get('faq') or (s.get('t','').startswith('«') and not s.get('k'))
    h=bgmark(s)
    if s.get('icon'): h+='<div'+A('sl2-topico')+'>'+ico(s['icon'])+'</div>'
    if faq: h+='<div class="sl2-faq"></div><div'+A('sl2-rule')+'></div>'
    h+=lines(s.get('lines'))
    if s.get('final'): h+='<p'+A('sl2-fin')+'>'+T(s['final'])+'</p>'
    return h+disc(s)
def f_cta(s):
    return bgmark(s)+lines(s.get('lines'))+btn(s.get('btn') or 'Забронировать место — $10',s.get('terms'))+disc(s)
def f_two(s):
    mode=s.get('mode','vs');cols=s.get('cols',[])
    h=bgmark(s)+'<div class="sl2-cols'+('' if s.get('final') else ' nofinal')+'">'
    for i,c in enumerate(cols):
        tone=c.get('tone') or ('win' if (mode=='vs' and i==1) else ('dim' if mode=='vs' else 'pair'))
        h+='<div'+A('sl2-col '+tone,.25)+'><h4>'+T(c.get('h',''))+'</h4>'
        if c.get('big'): h+='<div class="sl2-big">'+T(c['big'])+(('<small>'+T(c['bigd'])+'</small>') if c.get('bigd') else '')+'</div>'
        for it in c.get('items',[]):
            if isinstance(it,dict):
                if it.get('v') and not it.get('h'): h+='<div class="sl2-big">'+T(it['v'])+'</div>'
                elif it.get('v'): h+='<div class="sl2-big">'+T(it['v'])+'<small>'+T(it['h'])+'</small></div>'
                else: h+='<div class="sl2-li">'+(ico(it['icon'],'xs') if it.get('icon') else svg('check' if tone=='win' else 'arrow'))+'<span>'+T(it.get('h',''))+'</span></div>'
            else: h+='<div class="sl2-li">'+svg('check' if tone=='win' else ('x' if c.get('cross') else 'arrow'))+'<span>'+T(it)+'</span></div>'
        if c.get('sum'): h+='<div class="sl2-sum">'+T(c['sum'])+'</div>'
        h+='</div>'
    return h+'</div>'+final(s.get('final'),plain=s.get('finalPlain',False))+disc(s)
def f_steps(s):
    row=s.get('dir')=='row';tone=s.get('tone','')
    h=bgmark(s)
    if row:
        h+='<div class="sl2-stepsh'+(' '+tone if tone else '')+'">'+''.join('<div'+A('sl2-stp',.2)+'><span class="n">'+T(it.get('n',''))+'</span><h5>'+T(it.get('h',''))+(('&nbsp;'+svg('check','sl2-chk')) if it.get('icon')=='check' else '')+'</h5>'+(('<p>'+T(it['d'])+'</p>') if it.get('d') else '')+'</div>' for it in s.get('items',[]))+'</div>'
        if s.get('price'): h+='<div'+A('sl2-price')+'><small>'+T(s['price'].get('k',''))+'</small><b>'+T(s['price'].get('v',''))+'</b></div>'
        if s.get('media'): h+='<div'+A('sl2-stepmedia')+'>'+media(s['media'])+'</div>'
    else:
        h+='<div class="sl2-stepsv'+('' if s.get('final') else ' nofinal')+(' '+tone if tone else '')+'">'+''.join('<div'+A('sl2-stp',.2)+'><span class="n">'+T(it.get('n',''))+'</span><div><h5>'+T(it.get('h',''))+'</h5>'+(('<p>'+T(it['d'])+'</p>') if it.get('d') else '')+'</div></div>' for it in s.get('items',[]))+'</div>'
    return h+final(s.get('final'),plain=s.get('finalPlain',False))+disc(s)
def f_block(s):
    h=bgmark(s)+'<div class="sl2-mods">'
    for m in s.get('modules',[]):
        h+='<div'+A('sl2-mod',.2)+'><span class="m">'+T(m.get('m',''))+'</span><div><h5>'+T(m.get('h',''))+'</h5>'+(('<p>'+T(m['d'])+'</p>') if m.get('d') else '')+'</div><div class="n">'+(T(m['n'])+'<small>задач</small>' if m.get('n') else '')+'</div></div>'
    h+='</div><div'+A('sl2-band')+'>'
    g=s.get('give') or {}; r=s.get('result') or {}
    h+='<div><small>'+T(g.get('h','ВЫДАЁМ В ЭТОМ БЛОКЕ'))+'</small><b>'+T(g.get('v',''))+'</b></div>' if g else '<div></div>'
    h+='<div><small>'+T(r.get('h','РЕЗУЛЬТАТ БЛОКА'))+'</small><p>'+T(r.get('d',''))+'</p></div></div>'
    return h+disc(s)
def f_get(s):
    cards=s.get('cards',[]);one=len(cards)==1
    h=bgmark(s)+'<div class="sl2-gets'+(' one' if one else '')+('' if s.get('final') else ' nofinal')+'" style="--cols:'+str(max(1,len(cards)))+'">'
    for c in cards:
        m=media(c.get('media'))
        if c.get('demo'):
            def dsp(d):
                if not isinstance(d,dict): return '<span>'+T(d)+'</span>'
                k=d.get('kind','');cls=' class="win"' if k=='btn' or d.get('win') else (' class="hl"' if k in ('headline','title') else '')
                pre=(svg('star','sl2-st') if d.get('icon')=='star' else '')+('↑ ' if d.get('arrow')=='up' else '↓ ' if d.get('arrow')=='down' else '')
                return '<span'+cls+'>'+pre+T(d.get('t',''))+'</span>'
            demo='<div class="sl2-demo">'+''.join(dsp(d) for d in c['demo'])+'</div>'
            m=(m[:-6]+demo+'</div>') if m else '<div class="sl2-media">'+demo+'</div>'
        h+='<div'+A('sl2-get',.22)+'>'+m+'<div class="sl2-txt"><div class="sl2-hd">'+ico(c.get('icon'),'sm')+'<h5>'+T(c.get('h',''))+'</h5></div>'+(('<p>'+T(c['d'])+'</p>') if c.get('d') else '')+(('<div class="sl2-cl">'+''.join('<div>'+T(l)+'</div>' for l in c['lines'])+'</div>') if c.get('lines') else '')
        if c.get('price'): h+='<div class="sl2-price">'+T(c['price'])+(('<small>'+T(c['pm'])+'</small>') if c.get('pm') else '')+'</div>'
        if c.get('tag'): h+='<span class="sl2-tag">'+T(c['tag'])+'</span>'
        h+='</div></div>'
    if one and s.get('bubble'):
        b=s['bubble'];b=[b['q'],b['a']] if isinstance(b,dict) else (b if isinstance(b,list) else [b])
        h+='<div class="sl2-bubble">'+''.join('<span'+A(('me' if i%2 else ''),.5)+'>'+T(x)+'</span>' for i,x in enumerate(b))+'</div>'
    return h+'</div>'+final(s.get('final'),plain=s.get('finalPlain',False))+disc(s)
def f_element(s):
    n=int(re.sub(r'\D','',s.get('num','1')) or 1)
    h=bgmark(s)+'<div class="sl2-prog"><i style="--w:'+('%.1f'%(n/17*100))+'%"></i></div>'
    if s.get('d'): h+='<p'+A('sl2-eld')+'>'+T(s['d'])+'</p>'
    if s.get('extra'): h+='<p'+A('sl2-extra')+'>'+T(s['extra'])+'</p>'
    v=s.get('value','');acc=s.get('acc') or v;prev=s.get('accPrev','$0')
    h+='<div'+A('sl2-val')+'><small>ЦЕННОСТЬ</small><b>'+T(v)+'</b><small>НАКОПЛЕНО</small><b class="acc" data-count="'+str(num(acc) or '')+'" data-from="'+str(num(prev) or 0)+'">'+T(acc)+'</b></div>'
    if s.get('list'):
        h+='<div class="sl2-elist">'+''.join('<div'+A('',.1)+'><span class="n">'+T(it.get('n') or ('%02d'%(i+1)))+'</span>'+ico(it.get('icon'),'xs')+'<span>'+T(it.get('h',''))+'</span><span class="p">'+T(it.get('price',''))+'</span></div>' for i,it in enumerate(s['list']))+'</div>'
    elif s.get('places'):
        side=' side' if s.get('media') else ''
        h+='<div class="sl2-places'+side+'">'+''.join('<div'+A(it.get('tone',''),.1)+'><b>'+T(it.get('h',''))+'</b><span>'+T(it.get('d',''))+'</span></div>' for it in s['places'])+'</div>'
        if s.get('media'): h+='<div'+A('sl2-elm side')+'>'+media(s['media'])+'</div>'
    elif s.get('media'):
        h+='<div'+A('sl2-elm')+'>'+media(s['media'])+'</div>'
    elif s.get('lines'):
        h+=lines(s['lines'],'sl2-lines el')
    else:
        h+='<div class="sl2-wm">'+('%02d'%n)+'</div>'
    return h+disc(s)
def f_package(s):
    h='<div class="sl2-pk">';lastg=None
    for r in s.get('rows',[]):
        if r.get('group') and r['group']!=lastg: h+='<div class="sl2-pkg">'+T(r['group'])+'</div>';lastg=r['group']
        h+='<div class="sl2-pkr'+(' off' if r.get('off') else '')+'"><span class="n">'+T(r.get('n',''))+'</span><span>'+T(r.get('h',''))+'</span><span class="p">'+T(r.get('price',''))+'</span>'
        if r.get('sub'): h+='<div class="sl2-pks">'+''.join('<span>'+T(x.get('h',''))+'<b>'+T(x.get('price',''))+'</b></span>' for x in r['sub'])+'</div>'
        h+='</div>'
    t=s.get('total') or {}
    h+='</div><div'+A('sl2-pkt')+'><span>'+T(t.get('h','Ценность'))+'</span><b>'+T(t.get('v',''))+'</b></div>'
    return h+disc(s)
def f_packages3(s):
    mode=s.get('mode','value')
    h=bgmark(s)+'<div class="sl2-p3'+('' if s.get('final') else ' nofinal')+'">'
    for p in s.get('packs',[]):
        nm=p.get('name','');h+='<div'+A('sl2-pc'+(' gold' if nm.lower()=='gold' else ''),.25)+'><div class="nm">'+T(nm)+'</div>'
        if p.get('tag'): h+='<div class="tag">'+T(p['tag'])+'</div>'
        if mode=='value': h+='<div class="val">'+T(p.get('value',''))+'</div>'
        elif mode=='price': h+='<div class="val old">'+T(p.get('value',''))+'</div><div class="val now">'+T(p.get('price',''))+'</div>'
        elif mode=='today': h+='<div class="val old">'+T(p.get('value',''))+'</div><div class="val old2">'+T(p.get('price',''))+'</div><div class="val now">'+T(p.get('today',''))+'</div>'
        if p.get('sub'): h+='<div class="sub">'+T(p['sub'])+'</div>'
        if p.get('metrics'): h+='<div class="met">'+''.join('<div><span>'+T(m.get('h',''))+'</span><b>'+T(m.get('v',''))+'</b></div>' for m in p['metrics'])+'</div>'
        if p.get('chips'): h+='<div class="chips">'+''.join('<span>'+T(c)+'</span>' for c in p['chips'])+'</div>'
        if p.get('count'): h+='<div class="cnt">'+T(p['count'])+(('<small>'+T(p['countd'])+'</small>') if p.get('countd') else '')+'</div>'
        h+='</div>'
    return h+'</div>'+final(s.get('final'),plain=True)+disc(s)
def f_package_one(s):
    h=bgmark(s)+lines([s['d']] if s.get('d') else [])
    if s.get('blocks'): h+='<div'+A('sl2-grp')+'><small>Блоки программы</small><div>'+''.join('<span class="sl2-chip">'+T(b)+'</span>' for b in s['blocks'])+'</div></div>'
    if s.get('agents'): h+='<div'+A('sl2-grp')+'><small>Агенты</small><div>'+''.join('<span class="sl2-chip win">'+T(b)+'</span>' for b in s['agents'])+'</div></div>'
    return h+disc(s)
def f_table(s):
    h='<div class="sl2-tbl"><div class="sl2-tr th"><span></span>'+''.join('<span>'+T(c)+'</span>' for c in s.get('cols',[]))+'</div>'
    def cell(v):
        if v is True: return '<span>'+svg('check')+'</span>'
        if v is False or v is None or v=='': return '<span><i></i></span>'
        vs=str(v); return '<span class="'+('tx' if len(vs)>4 and not re.fullmatch(r'[\d$., ·+–-]+',vs) else '')+'">'+T(vs)+'</span>'
    for r in s.get('rows',[]): h+='<div'+A('sl2-tr',.07)+'><span>'+T(r.get('h',''))+'</span>'+''.join(cell(v) for v in r.get('v',[]))+'</div>'
    for r in s.get('foot',[]): h+='<div'+A('sl2-tr foot'+(' win' if r.get('tone')=='win' else ''),.15)+'><span>'+T(r.get('h',''))+'</span>'+''.join(cell(v) for v in r.get('v',[]))+'</div>'
    return h+'</div>'+disc(s)
def f_money(s):
    mode=s.get('mode','')
    h=bgmark(s)
    if s.get('icon'): h+='<div'+A('sl2-topico')+'>'+ico(s['icon'])+'</div>'
    if s.get('pre'): h+='<p'+A('sl2-pre')+'>'+T(s['pre'])+'</p>'
    if mode=='slider':
        h+='<div'+A('sl2-slider')+'><i></i></div><div'+A('sl2-slider-l')+'><span>'+T(s.get('from','$0'))+'</span><b>'+T(s.get('num',''))+'</b></div>'
        if s.get('k2'): h+='<p'+A('sl2-lines')+' style="margin-top:2cqh;letter-spacing:.14em;text-transform:uppercase;font-size:2cqw">'+T(s['k2'])+'</p>'
    elif mode=='rows':
        h+='<div class="sl2-rows">'+''.join('<div'+A(r.get('tone',''),.2)+'><span class="n">'+T(r.get('n',''))+'</span><span class="h">'+T(r.get('h',''))+'</span><span class="v">'+T(r.get('v',''))+'</span></div>' for r in s.get('rows',[]))+'</div>'
        if s.get('btn'): h+=btn(s['btn'],s.get('terms'))
    elif mode in ('stats','funnel','age'):
        if s.get('num'): h+='<div'+A('sl2-num'+(' mid' if len(s['num'])>6 else ''))+'>'+T(s['num'])+'</div>'
        h+='<div class="sl2-stats'+(' funnel' if mode=='funnel' else '')+'">'+''.join('<div'+A('',.2)+'><b'+(' class="sm"' if len(str(st.get('v','')))>7 else '')+'>'+T(st.get('v',''))+'</b>'+(('<small>'+T(st['h'])+'</small>') if st.get('h') else '')+'</div>' for st in s.get('stats',[]))+'</div>'
        if s.get('rows'): h+='<div class="sl2-rows">'+''.join('<div'+A(r.get('tone',''),.2)+'><span class="n">'+T(r.get('n',''))+'</span><span class="h">'+T(r.get('h',''))+'</span><span class="v">'+T(r.get('v',''))+'</span></div>' for r in s['rows'])+'</div>'
    else:
        if s.get('num'): h+='<div'+A('sl2-num'+(' mid' if len(s['num'])>6 else '')+(' sm' if len(s['num'])>12 else ''))+'>'+T(s['num'])+'</div>'
    h+=lines(s.get('lines'))
    if s.get('final'): h+='<p'+A('sl2-fin')+'>'+T(s['final'])+'</p>'
    return h+disc(s)
def f_case(s):
    v=s.get('video','');p=s.get('poster','')
    h='<div class="s16-card"><video src="'+v+'"'+(' poster="./'+p+'"' if p else '')+' playsinline loop preload="metadata"></video></div>'
    if s.get('quote'): h+='<p class="s16-quote">'+T(s['quote'])+'</p>'
    r=s.get('result') or {}
    h+='<div class="s16-result"><b'+(' class="sm"' if len(str(r.get('v','')))>6 else '')+'>'+T(r.get('v',''))+'</b><span>'+T(r.get('d',''))+'</span></div>'
    rows=[]
    if s.get('was'): rows.append(('Было',s['was']))
    for x in s.get('path',[]): rows.append((x.get('h',''),x.get('d','')))
    if rows: h+='<div class="s16-path">'+''.join('<div><b>'+T(a)+'</b>'+T(b)+'</div>' for a,b in rows)+'</div>'
    return h+disc(s)
def f_cards(s):
    cards=s.get('cards',[]);cols=s.get('cols') or (3 if len(cards)>4 else len(cards))
    h=bgmark(s)
    both=bool(s.get('band') and s.get('flow'))
    if s.get('band'): h+='<div'+A('sl2-band2')+'>'+ico(s['band'].get('icon'),'xs')+'<span>'+T(s['band'].get('t',''))+'</span></div>'
    if s.get('flow'): h+='<div'+A('sl2-flow'+(' second' if both else ''))+'><b>'+T(s['flow'].get('from',''))+'</b>'+ARROW+'<span>'+T(s['flow'].get('to',''))+'</span></div>'
    if s.get('mode')=='chips' and not s.get('chips'):
        for c in cards: c['iconic']=True
    if s.get('chips'):
        h+='<div class="sl2-cg chips'+('' if s.get('final') else ' nofinal')+'">'+''.join('<span'+A('sl2-chip',.15)+'>'+T(c)+'</span>' for c in s['chips'])+'</div>'
    else:
        dense=' dense' if len(cards)>=7 else (' six' if (len(cards)>=5 and any(c.get('v') for c in cards)) else '')
        allic=all((not (c.get('media') or {})) or ('icon' in (c.get('media') or {})) for c in cards)
        if allic and not dense: s['mode']='chips'
        h+='<div class="sl2-cg'+('' if s.get('final') else ' nofinal')+(' withboth' if both else (' withflow' if (s.get('flow') or s.get('band')) else ''))+(' noh' if s.get('noh') else '')+(' center' if s.get('mode')=='chips' else '')+dense+'" style="--cols:'+str(cols)+'">'
        for c in cards:
            m=c.get('media') or {}
            iconic=c.get('iconic') or (not m) or ('icon' in m)
            strip=bool(dense) and iconic
            h+='<div'+A('sl2-cc'+(' iconic' if (iconic and not strip) else ''),.12)+'>'
            if m and not iconic: h+=media(m)
            elif strip: h+='<div class="sl2-media icon">'+ico(m.get('icon') or c.get('icon') or 'sparkle')+'</div>'
            elif m.get('icon'): h+=ico(m['icon'])
            elif c.get('icon'): h+=ico(c['icon'])
            h+='<div class="sl2-txt">'+(('<span class="tag">'+((svg(c['icon'],'sl2-ti')) if (c.get('icon') and m) else '')+T(c['tag'])+'</span>') if c.get('tag') else '')+'<h5>'+T(c.get('h',''))+'</h5>'+(('<p>'+T(c['d'])+'</p>') if c.get('d') else '')+(('<span class="v">'+T(c['v'])+'</span>') if c.get('v') else '')+(('<span class="vd">'+T(c['vd'])+'</span>') if c.get('vd') else '')+'</div>'
            if c.get('chip'): h+='<span class="chip">'+T(c['chip'])+'</span>'
            h+='</div>'
        h+='</div>'
    return h+final(s.get('final'),plain=s.get('finalPlain',False))+disc(s)
def f_screen(s):
    h=lines(s.get('lines'))
    if s.get('link'): h+='<p'+A('sl2-link')+'>'+T(s['link'])+'</p>'
    if s.get('iframe'): h+='<div'+A('sl2-shot')+'><iframe src="'+s['iframe']+'" title="Демо" loading="lazy"></iframe></div>'
    else: h+='<div'+A('sl2-shot'+(' still' if s.get('noscroll') else ''))+'><img src="'+s.get('img','')+'" alt=""></div>'
    return h+disc(s)
def f_desk(s):
    h=lines(s.get('lines'))
    h+='<div'+A('sl2-desk')+'>'
    if s.get('deskTitle'): h+='<div class="sl2-dt">'+T(s['deskTitle'])+'</div>'
    tm=s.get('team',[]);tk=s.get('teamK') or s.get('teamHead') or {}
    h+='<div class="sl2-team"><small class="k">'+T(tk.get('h') or tk.get('k') or 'ВАША КОМАНДА')+((' · <b>'+T(tk.get('v') or tk.get('badge'))+'</b>') if (tk.get('v') or tk.get('badge')) else '')+'</small>'
    for x in tm:
        if x.get('group'): h+='<small class="k g">'+T(x['group'])+'</small>'
        h+='<div'+(' class="on"' if x.get('active') else '')+'>'+ico(x.get('icon'),'xs')+'<div><b>'+T(x.get('h',''))+'</b><span>'+T(x.get('d',''))+'</span></div></div>'
    h+='</div>'
    ag=s.get('agent') or {};task=s.get('task') or {}
    h+='<div class="sl2-agent"><div class="h">'+ico(ag.get('icon','site'),'xs')+'<span>'+T(ag.get('h','AI-Сайты'))+'</span></div><div class="d">'+T(ag.get('d',''))+'</div>'
    if task: h+='<div class="sl2-task"><b>'+T(task.get('k','ЗАДАЧА'))+'</b>'+T(task.get('q',''))+'</div>'
    st=s.get('stages',[])
    h+='<div class="sl2-stg">'
    for x in st:
        state=x.get('state') or ('done' if x.get('t') else 'todo')
        h+='<div class="'+state+'"><span>'+(svg('check') if state=='done' else '<i class="dot"></i>')+T(x.get('h',''))+'</span><span>'+T(x.get('t',''))+'</span></div>'
    h+='</div></div>'
    c=s.get('control') or {};fd=s.get('feed') or {}
    h+='<div class="sl2-ctrl"><small class="k">'+T(c.get('k','ВО ГЛАВЕ'))+'</small><div class="you">'+T(c.get('h','вы'))+'</div>'
    if c.get('sub'): h+='<p class="sub">'+T(c['sub'])+(('<b>'+T(c['status'])+'</b>') if c.get('status') else '')+'</p>'
    h+=''.join('<p>'+T(l)+'</p>' for l in c.get('lines',[]))+(('<a class="sl2-btn" href="'+CTA+'">'+T(c['btn'])+'</a>') if c.get('btn') else '')
    if fd: h+='<div class="sl2-feed"><small class="k">'+T(fd.get('k','ЛЕНТА СОБЫТИЙ'))+'</small>'+''.join('<div'+(' class="now"' if i==0 else '')+'><span>'+T(x.get('t',''))+'</span><span>'+T(x.get('d',''))+'</span></div>' for i,x in enumerate(fd.get('items',[])))+'</div>'
    h+='</div></div>'
    return h+final(s.get('final'),plain=True)+disc(s)
def f_hunter(s):
    h='<div class="sl2-hl">'+''.join('<div'+A('',.15)+'>'+svg('check')+'<span>'+T(l)+'</span></div>' for l in s.get('lines',[]))+'</div>'
    val=s.get('value') or {};vk=val.get('k','ЦЕННОСТЬ') if isinstance(val,dict) else 'ЦЕННОСТЬ';vv=val.get('v','') if isinstance(val,dict) else val
    h+='<div'+A('sl2-hv')+'><small>'+T(vk)+'</small><b>'+T(vv)+'</b><span>'+T(s.get('free',''))+'</span></div>'
    h+='<div'+A('sl2-hr')+'>'+media(s.get('media') or {'img':'assets/gen-164-213/s179-hunter-map.webp','alt':'Карта с найденными клиентами'})+'<small class="k">'+T(s.get('k2',''))+'</small><div class="sl2-hstg">'+''.join('<span>'+T(x)+'</span>' for x in s.get('stages',[]))+'</div>'
    fn=s.get('funnel',[]);big=[x for x in fn if x.get('h')];sub=[x for x in fn if not x.get('h')]
    h+='<div class="sl2-hfun">'+''.join('<div><b'+(' class="win"' if i==len(big)-1 else '')+'>'+T(x.get('v',''))+'</b><small>'+T(x.get('h',''))+'</small></div>' for i,x in enumerate(big))+'</div>'
    if sub: h+='<div class="sl2-hsub">'+''.join('<span>'+T(x.get('v',''))+'</span>' for x in sub)+'</div>'
    if s.get('final'): h+='<div class="sl2-hfin">'+T(s['final'])+'</div>'
    return h+'</div>'+disc(s)
def f_week(s):
    h=bgmark(s)+'<div class="sl2-week">'+''.join('<div'+A('sl2-day'+(' on' if d.get('v') else ''),.1)+'><small>'+T(d.get('d',''))+'</small>'+(('<b>'+T(d['v'])+'</b>') if d.get('v') else '')+'</div>' for d in s.get('days',[]))+'</div>'
    if s.get('final'): h+='<p'+A('sl2-fin')+'>'+T(s['final'])+'</p>'
    return h+disc(s)
def f_iceberg(s):
    t=s.get('top') or {};b=s.get('bottom') or {}
    h='<div'+A('sl2-ice top')+'><small>'+T(t.get('k',''))+'</small>'+''.join('<p'+A()+'>'+T(x)+'</p>' for x in t.get('items',[]))+'</div><div class="sl2-wl"></div>'
    h+='<div'+A('sl2-ice bottom')+'><small>'+T(b.get('k',''))+'</small>'+''.join('<p'+A()+'>'+T(x)+'</p>' for x in b.get('items',[]))+'</div>'
    return h+disc(s)
FAM={'s16-statement':f_statement,'s16-cta':f_cta,'s16-two':f_two,'s16-steps':f_steps,'s16-block':f_block,'s16-get':f_get,'s16-element':f_element,'s16-package':f_package,'s16-packages3':f_packages3,'s16-package-one':f_package_one,'s16-table':f_table,'s16-money':f_money,'s16-number':f_money,'s16-case':f_case,'s16-cards':f_cards,'s16-screen':f_screen,'s16-desk':f_desk,'s16-hunter':f_hunter,'s16-week':f_week,'s16-iceberg':f_iceberg}
def build(s):
    _d[0]=0.2
    fam=s.get('family','s16-statement')
    if fam=='s16-number': fam='s16-money'
    fn=FAM.get(fam) or f_statement
    b=fn(s)
    bl={'kind':'s16','v2':True,'layout':fam}
    if s.get('k'): bl['eyebrow']=s['k']
    if s.get('bg'):
        src=s['bg'] if '/' in s['bg'] else 'assets/gen-164-213/'+s['bg']+('' if s['bg'].endswith(('.webp','.jpg','.png')) else '.webp')
        bl['art']=[{'src':src,'alt':''}]
    if fam=='s16-case': bl['sound']=True
    plain=re.sub(r'<[^>]+>','',s.get('t',''));est=(len(plain)+29)//30
    if est>=2 and fam in ('s16-two','s16-steps','s16-block','s16-get','s16-packages3','s16-cards','s16-screen','s16-table','s16-hunter','s16-package','s16-desk'): b='<i class="sl2-t'+str(min(est,3))+'" hidden></i>'+b
    from _sales_visual_306_350 import render as render_sales3
    b, bl = render_sales3(s, b, bl)
    fam = bl['layout']
    note=(s.get('note') or '').strip()
    note+=('\n' if note else '')+'Google sales #'+s.get('u','')
    return {'t':s.get('t',''),'k':s.get('k',''),'b':b,'lv':s.get('lv',6),'note':note,'foundation':{'block129':bl,'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False,'layout':fam,'mediaBrief':s.get('mediaBrief','Продаюча частина, сім’я '+fam),'animationBrief':'Поява елементів по черзі; фінальна композиція статична.'}}
def main():
    args=sys.argv[1:]
    files=[os.path.join(D,'data',args[args.index('--test')+1])] if '--test' in args else sorted(glob.glob(os.path.join(D,'data','sec-*.json')))
    items=[]
    for f in files:
        for s in json.load(open(f,encoding='utf-8')):
            if s.get('skip'): continue
            items.append(s)
    parts=[]
    for item in items:
        if item.get('visual',{}).get('split')=='intro-desk':
            import copy
            intro=copy.deepcopy(item)
            intro['visual']['mode']='desk-intro'
            intro['note']+='\nПодслайд 1/2: предложение и видео с первого слайда.'
            parts.append(build(intro))
            desk=copy.deepcopy(item)
            desk['lines']=[]
            desk['final']=''
            desk['visual']['stage']=2
            desk['note']+='\nПодслайд 2/2: рабочий стол; текст предложения вынесен на предыдущий подслайд.'
            parts.append(build(desk))
        else:
            parts.append(build(item))
    if len(parts)<2: raise SystemExit('need at least 2 slides')
    p=os.path.join(ROOT,'source/overrides.json');o=json.load(open(p,encoding='utf-8'));va=o['__visibleGoogleAudit']['slides']
    s=va.get(SRC_OID) or {}
    s['reason']='21.09 Мирослав: продаюча частина зібрана з Google-деки «Copy of PREZA-prodayushchaya-1309-final» (PPTX від Мирослава 21.09) у стилі перших 150 слайдів; дані source/google-sales-2026-09-21/data, сім’ї css/block-sales-2109.css.'
    s['mediaStatus']='ready'
    rm=s.setdefault('remove',[])
    for k in ['bg','photos','src','kind','poster','opening','viz','theme','fx','lost','bgside','ptall','img','k']:
        if k not in rm: rm.append(k)
    s.setdefault('set',{})
    s['presentationParts']={'sourceGoogleObjectId':SRC_OID,'authorization':'Прямий запит Мирослава 21.09.2026 у сесії: «потрібно зробити на основі цього продаючу частину… щоб я не правив кожний слайд» + PPTX-експорт Google-деки, наданий ним; старі 304–342 замінюються цим блоком.','allowPartTitles':True,'mediaStatus':'ready','slides':parts}
    f=s.setdefault('foundation',{});f.update({'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False});f.pop('variant',None);f.pop('layout',None)
    f['block129']=parts[0]['foundation']['block129']
    s['set']['t']=parts[0]['t'];s['set']['b']=parts[0]['b']
    va[SRC_OID]=s
    for oid in OLD_OIDS:
        x=va.get(oid) or {};x['omit']=True;x['reason']=(x.get('reason','')+' | 21.09: замінено новою продаючою частиною (parts на 303)').strip(' |');va[oid]=x
    json.dump(o,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print('sales parts:',len(parts),'from',[os.path.basename(x) for x in files],'| omitted old:',len(OLD_OIDS))
if __name__=='__main__': main()
