# 21.09 · 212 «AI-продавец, который живёт в телефоне»: детальна SMIL-анімована SVG-сцена (три месенджери → телефон → чат → оплата), скрин лендингу Валюші у 3D-картці, теза 24/7 і ціна. Рядок «агент отвечает голосом» прибрано (Мирослав).
import json
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
oid='g3f9b3adf0b8_0_2888'
D='9s'
def win(t0,t1,fade=0.02):
    # opacity window inside the 9s loop (keyTimes fractions)
    a=max(0,t0-fade); b=min(1,t1+fade)
    return f'<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{a:.3f};{t0:.3f};{t1:.3f};{b:.3f};1" dur="{D}" repeatCount="indefinite"/>'
def fly(path,t0,t1):
    return f'<animateMotion path="{path}" dur="{D}" repeatCount="indefinite" calcMode="linear" keyPoints="0;0;1;1" keyTimes="0;{t0:.3f};{t1:.3f};1" rotate="0"/>'
def msg(x,y,w,text,me=False,t0=0,t1=1):
    w=int(len(text)*5.9+20)
    if me: x=358-w
    fill='#fdd506' if me else '#221b16'; col='#0b0907' if me else '#f5f3ee'
    tx=x+10
    return (f'<g opacity="0">{win(t0,t1)}<rect x="{x}" y="{y}" width="{w}" height="26" rx="9" fill="{fill}" stroke="{"none" if me else "#3a3129"}"/>'
            f'<text x="{tx}" y="{y+17}" font-family="Manrope,sans-serif" font-size="10.5" font-weight="{600 if me else 500}" fill="{col}">{text}</text></g>')
def typing(x,y,t0,t1):
    dots=''.join(f'<circle cx="{x+12+i*9}" cy="{y+13}" r="2.6" fill="#8a8278"><animate attributeName="opacity" values=".3;1;.3" keyTimes="0;.5;1" dur=".9s" begin="{i*0.18}s" repeatCount="indefinite"/></circle>' for i in range(3))
    return f'<g opacity="0">{win(t0,t1,0.01)}<rect x="{x}" y="{y}" width="44" height="26" rx="9" fill="#221b16" stroke="#3a3129"/>{dots}</g>'
def node(cx,cy,glyph,label,sub):
    return (f'<g><rect x="{cx-27}" y="{cy-27}" width="54" height="54" rx="14" fill="#15110d" stroke="#3a3129"/>{glyph}'
            f'<text x="{cx}" y="{cy+46}" text-anchor="middle" font-family="Unbounded,sans-serif" font-size="12.5" font-weight="500" fill="#f5f3ee">{label}</text>'
            f'<text x="{cx}" y="{cy+61}" text-anchor="middle" font-family="Manrope,sans-serif" font-size="10" fill="#c4bdb1">{sub}</text></g>')
def bubble(path,t0,t1):
    return (f'<g opacity="0">{win(t0,t1,0.01)}<g>{fly(path,t0,t1)}<rect x="-16" y="-10" width="32" height="20" rx="8" fill="#fdd506"/>'
            '<circle cx="-7" cy="0" r="2" fill="#0b0907"/><circle cx="0" cy="0" r="2" fill="#0b0907"/><circle cx="7" cy="0" r="2" fill="#0b0907"/></g></g>')
IG=('<rect x="45" y="115" width="30" height="30" rx="9" fill="none" stroke="#f5f3ee" stroke-width="2.2"/><circle cx="60" cy="130" r="7" fill="none" stroke="#f5f3ee" stroke-width="2.2"/><circle cx="69" cy="121" r="1.8" fill="#f5f3ee"/>')
TG=('<path d="M44 280 L77 266 L70 296 L60 288 L53 294 L54 285 Z" fill="none" stroke="#f5f3ee" stroke-width="2.2" stroke-linejoin="round"/><path d="M54 285 L72 270" stroke="#f5f3ee" stroke-width="2.2"/>')
WA=('<circle cx="60" cy="430" r="14" fill="none" stroke="#f5f3ee" stroke-width="2.2"/><path d="M48 441 L45 447 L52 445" fill="none" stroke="#f5f3ee" stroke-width="2.2" stroke-linejoin="round"/><path d="M54 425 c0 7 5 12 12 12 l2-3 -4-3 -2 2 c-2-1-4-3-5-5 l2-2 -2-4 z" fill="#f5f3ee"/>')
P1='M90,130 C150,130 170,250 218,262'; P2='M90,280 C140,280 170,275 218,275'; P3='M90,430 C150,430 170,300 218,288'
svg=('<svg class="s16-scene-svg" viewBox="0 0 560 560" xmlns="http://www.w3.org/2000/svg" aria-label="Клиенты пишут в Instagram, Telegram и WhatsApp — AI-продавец отвечает в телефоне и доводит до оплаты">'
 '<defs><radialGradient id="sg" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fdd506" stop-opacity=".16"/><stop offset="1" stop-color="#fdd506" stop-opacity="0"/></radialGradient>'
 '<clipPath id="scr"><rect x="223" y="78" width="144" height="404" rx="16"/></clipPath></defs>'
 '<circle cx="295" cy="280" r="250" fill="url(#sg)"/>'
 '<g transform-origin="295 280"><animateTransform attributeName="transform" type="rotate" from="0 295 280" to="360 295 280" dur="60s" repeatCount="indefinite"/>'
 '<circle cx="295" cy="280" r="238" fill="none" stroke="#3a3129" stroke-width="1" stroke-dasharray="3 9"/></g>'
 f'<path d="{P1}" fill="none" stroke="#2a2420" stroke-width="1.4" stroke-dasharray="4 5"/><path d="{P2}" fill="none" stroke="#2a2420" stroke-width="1.4" stroke-dasharray="4 5"/><path d="{P3}" fill="none" stroke="#2a2420" stroke-width="1.4" stroke-dasharray="4 5"/>'
 +node(60,130,IG,'Instagram','директ и комментарии')+node(60,280,TG,'Telegram','чат и голосом')+node(60,430,WA,'WhatsApp','куда пишут чаще всего')+
 bubble(P1,0.02,0.15)+bubble(P2,0.30,0.43)+bubble(P3,0.58,0.71)+
 # phone
 '<rect x="215" y="70" width="160" height="420" rx="24" fill="#1a1310" stroke="#4f4541" stroke-width="1.5"/>'
 '<rect x="223" y="78" width="144" height="404" rx="16" fill="#0f0c09"/>'
 '<rect x="268" y="84" width="54" height="9" rx="4.5" fill="#1a1310"/>'
 '<g clip-path="url(#scr)">'
 '<rect x="223" y="78" width="144" height="34" fill="#15110d"/><line x1="223" y1="112" x2="367" y2="112" stroke="#2a2420"/>'
 '<circle cx="238" cy="95" r="7" fill="#fdd506"/><text x="250" y="99" font-family="Manrope,sans-serif" font-size="10.5" font-weight="700" fill="#f5f3ee">AI-продавец</text>'
 '<circle cx="330" cy="95" r="3" fill="#39d353"><animate attributeName="opacity" values="1;.25;1" dur="1.6s" repeatCount="indefinite"/></circle><text x="337" y="98.5" font-family="Manrope,sans-serif" font-size="8.5" fill="#c4bdb1">онлайн</text>'
 +msg(232,124,118,'Есть окошко завтра?',False,0.15,0.985)
 +typing(232,158,0.17,0.25)
 +msg(240,158,118,'Да, 12:00 или 17:30',True,0.26,0.985)
 +msg(232,196,120,'А если не приду?',False,0.43,0.985)
 +typing(232,230,0.45,0.53)
 +msg(240,230,118,'Перенесём бесплатно',True,0.54,0.985)
 +msg(232,268,100,'Беру на 12:00',False,0.71,0.985)
 +typing(232,302,0.73,0.79)
 +msg(240,302,118,'Ссылка на оплату →',True,0.80,0.985)
 # paid badge
 +f'<g opacity="0">{win(0.90,0.985,0.015)}<rect x="248" y="342" width="94" height="24" rx="12" fill="#0f0c09" stroke="#39d353"/><circle cx="262" cy="354" r="6" fill="#39d353"/><path d="M259 354 l2.5 2.5 4.5-5" fill="none" stroke="#0b0907" stroke-width="1.6"/><text x="273" y="358" font-family="Manrope,sans-serif" font-size="10" font-weight="700" fill="#39d353">Оплачено</text></g>'
 '</g>'
 '<rect x="270" y="470" width="50" height="4" rx="2" fill="#3a3129"/>'
 # coin flies to output
 f'<g opacity="0">{win(0.85,0.93,0.01)}<g><animateMotion path="M372,300 C420,300 430,285 468,285" dur="{D}" repeatCount="indefinite" calcMode="linear" keyPoints="0;0;1;1" keyTimes="0;0.85;0.93;1"/><circle r="11" fill="#fdd506"/><text y="4" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="12" font-weight="700" fill="#0b0907">$</text></g></g>'
 # output: coin icon that fills yellow at the moment of payment
 f'<circle cx="500" cy="285" r="34" fill="#15110d" stroke="#4f4541" stroke-width="1.5"><animate attributeName="fill" values="#15110d;#15110d;#fdd506;#fdd506;#15110d" keyTimes="0;0.905;0.93;0.99;1" dur="{D}" repeatCount="indefinite"/><animate attributeName="stroke" values="#4f4541;#4f4541;#fdd506;#fdd506;#4f4541" keyTimes="0;0.905;0.93;0.99;1" dur="{D}" repeatCount="indefinite"/></circle>'
 f'<circle cx="500" cy="285" r="34" fill="none" stroke="#fdd506" stroke-width="2" opacity="0"><animate attributeName="r" values="34;34;56;56" keyTimes="0;0.91;0.99;1" dur="{D}" repeatCount="indefinite"/><animate attributeName="opacity" values="0;0;.7;0;0" keyTimes="0;0.91;0.925;0.99;1" dur="{D}" repeatCount="indefinite"/></circle>'
 f'<text x="500" y="296" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="30" font-weight="700" fill="#8a8278">$<animate attributeName="fill" values="#8a8278;#8a8278;#0b0907;#0b0907;#8a8278" keyTimes="0;0.905;0.93;0.99;1" dur="{D}" repeatCount="indefinite"/></text>'
 '<text x="500" y="338" text-anchor="middle" font-family="Unbounded,sans-serif" font-size="12.5" font-weight="500" fill="#f5f3ee">оплата</text>'
 '<text x="500" y="353" text-anchor="middle" font-family="Manrope,sans-serif" font-size="10" fill="#c4bdb1">без вас и без выходных</text>'
 '</svg>')
s=va.get(oid) or {}
s['reason']='21.09 Мирослав: детальна SVG-анімація (SMIL, цикл 9 с): повідомлення з Instagram/Telegram/WhatsApp летять у телефон, AI-продавець відповідає в чаті, доводить до оплати; скрин лендингу Валюші у 3D-картці; рядок «агент отвечает голосом» прибрано.'
s['mediaStatus']='ready'
rm=s.setdefault('remove',[])
for k in ['bg','photos','src','kind','poster','opening','viz','theme','fx','lost','bgside','ptall','img']:
    if k not in rm: rm.append(k)
st=s.setdefault('set',{})
st['t']='AI-продавец, который <em>живёт в телефоне</em>'
st['b']=('<div class="s16-scene">'+svg+'</div>'
 '<div class="s16-site"><div class="s16-tilt"><div class="s16-win"><div class="bar"><i></i><i></i><i></i><span>valyusha-landing.vercel.app</span></div><img src="assets/vlad-1409/uslugi/prodavec.jpg" alt="Лендинг Валюши — AI-помощник в Telegram"></div></div></div>'
 '<p class="s16-claim"><b>24/7</b> отвечает клиентам, снимает сомнения и доводит до оплаты</p>'
 '<span class="s16-price"><i>$500–$2.000 · за сборку плюс ведение · сложность средняя</i></span>')
st['lv']=6
f=s.setdefault('foundation',{})
f.update({'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False,
          'mediaBrief':'SVG-сцена продавця в телефоні + скрин лендингу Валюші.','animationBrief':'SMIL-цикл 9 с: повідомлення → чат → оплата; поява картки сайту; hover — нахил.'})
f.pop('variant',None); f.pop('layout',None)
f['block129']={'kind':'s16','v2':True,'layout':'s16-seller','eyebrow':'Услуга 5 из 7'}
va[oid]=s
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1); print('patched',oid,len(svg))
