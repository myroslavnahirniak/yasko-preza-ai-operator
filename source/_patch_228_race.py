# 21.09 · 228 «Нейросети стали советовать её сайт» → 2 підслайди (Мирослав): частина 1 — стовпчики 285 vs 22 + «$0 вложено»; частина 2 — «Нейросети начали её советовать раньше, чем обычный поиск…» + «На второй месяц — первые три консультации по $150» з SVG-гонкою по місяцях (s16-race).
import json,copy
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
oid='g409d4d20be6_0_407'; s=va[oid]
b1=s['set']['b']
cut=b1.index('<p class="s16-lead">'); b1=b1[:cut]+'</div>'
f1=copy.deepcopy(s['foundation'])
Y='#fdd506';G='#4a423a';C='#f5f3ee';MU='#c4bdb1';DM='#6f685e';D='7s'
def once(attr,vals,t0,t1):
    return f'<animate attributeName="{attr}" values="{vals}" keyTimes="0;{t0:.3f};{t1:.3f};1" dur="{D}" fill="freeze" calcMode="spline" keySplines="0 0 1 1;.2 .8 .2 1;0 0 1 1"/>'
def pop(t0):
    return f'<animate attributeName="opacity" values="0;0;1;1" keyTimes="0;{t0:.3f};{min(1,t0+.05):.3f};1" dur="{D}" fill="freeze"/>'
W,H=600,300;x0,x1=70,560;base=230
mx=lambda m:x0+(x1-x0)*(m-0)/3
svg=f'<svg class="s16-smil s16-race-svg" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">'
svg+=f'<line x1="{x0}" y1="{base}" x2="{x1}" y2="{base}" stroke="#3a3129" stroke-width="1.5"/>'
for m,l in ((0,'старт'),(1,'месяц 1'),(2,'месяц 2'),(3,'месяц 3')):
    svg+=f'<line x1="{mx(m):.0f}" y1="{base-4}" x2="{mx(m):.0f}" y2="{base+4}" stroke="#3a3129"/><text x="{mx(m):.0f}" y="{base+22}" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="10" letter-spacing="1.5" fill="{DM}">{l.upper()}</text>'
# neural nets: rises early
pn=f'M{x0} {base-6} C{mx(0.5):.0f} {base-6} {mx(0.8):.0f} {base-70} {mx(1):.0f} {base-95} S{mx(2):.0f} {base-150} {mx(3):.0f} {base-190}'
ps=f'M{x0} {base-4} L{mx(2.4):.0f} {base-6} C{mx(2.7):.0f} {base-8} {mx(2.85):.0f} {base-14} {mx(3):.0f} {base-22}'
svg+=f'<path d="{pn}" fill="none" stroke="{Y}" stroke-width="4" stroke-linecap="round" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100" filter="drop-shadow(0 0 6px rgba(253,213,6,.6))">{once("stroke-dashoffset","100;100;0;0",.12,.62)}</path>'
svg+=f'<path d="{ps}" fill="none" stroke="#7a726a" stroke-width="3" stroke-linecap="round" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100">{once("stroke-dashoffset","100;100;0;0",.12,.75)}</path>'
# labels at line ends
svg+=f'<g opacity="0">{pop(.62)}<text x="{x1-2}" y="{base-200}" text-anchor="end" font-family="Unbounded,sans-serif" font-size="13" font-weight="500" fill="{Y}">нейросети</text></g>'
svg+=f'<g opacity="0">{pop(.75)}<text x="{x1-2}" y="{base-32}" text-anchor="end" font-family="Unbounded,sans-serif" font-size="12" font-weight="500" fill="{MU}">обычный поиск</text></g>'
# month 1 marker: first recommendation
svg+=f'<g opacity="0">{pop(.3)}<circle cx="{mx(1):.0f}" cy="{base-95}" r="7" fill="{Y}"/><circle cx="{mx(1):.0f}" cy="{base-95}" r="7" fill="none" stroke="{Y}"><animate attributeName="r" values="7;22" dur="1.6s" begin="2.1s" repeatCount="indefinite"/><animate attributeName="opacity" values=".7;0" dur="1.6s" begin="2.1s" repeatCount="indefinite"/></circle>'
svg+=f'<rect x="{mx(1)-70:.0f}" y="{base-150}" width="140" height="34" rx="6" fill="#0b0907" stroke="{Y}"/><text x="{mx(1):.0f}" y="{base-136}" text-anchor="middle" font-family="Manrope,sans-serif" font-size="10.5" font-weight="700" fill="{Y}">ChatGPT советует её</text><text x="{mx(1):.0f}" y="{base-123}" text-anchor="middle" font-family="Manrope,sans-serif" font-size="9.5" fill="{MU}">поиск её ещё не видит</text></g>'
# month 2 marker: 3 consultations
svg+=f'<g opacity="0">{pop(.48)}<circle cx="{mx(2):.0f}" cy="{base-150}" r="7" fill="{Y}"/>'
for k in range(3):
    svg+=f'<g opacity="0">{pop(.52+k*.05)}<circle cx="{mx(2)-78+k*30:.0f}" cy="{base-196}" r="12" fill="{Y}"/><text x="{mx(2)-78+k*30:.0f}" y="{base-192}" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="11" font-weight="700" fill="#0b0907">$</text></g>'
svg+=f'<text x="{mx(2)-48:.0f}" y="{base-172}" text-anchor="middle" font-family="Manrope,sans-serif" font-size="10.5" font-weight="700" fill="{C}">3 консультации × $150</text></g>'
svg+='</svg>'
part2={'t':'Нейросети начали её советовать <em>раньше, чем обычный поиск</em> вообще её заметил',
 'b':'<div class="s16-race">'+svg+'</div><p class="s16-claim">На второй месяц — <b>первые три консультации по $150</b></p>',
 'lv':6,'note':'Кейс Ани, часть 3б: гонка «нейросети vs обычный поиск» по месяцам; завершить строкой про $150.\nGoogle Slides #1238 · '+oid,
 'foundation':copy.deepcopy(f1)}
part2['foundation']['block129']={'kind':'s16','v2':True,'layout':'s16-race','eyebrow':'Что вышло','sound':False}
part2['foundation']['mediaBrief']='SVG-гонка нейросети vs поиск.'; part2['foundation']['animationBrief']='Лінії малюються, маркери місяць 1 і місяць 2 спливають, три монети $150.'
part1={'t':s['set']['t'],'b':b1,'lv':6,'note':'Кейс Ани, часть 3а: 285 против 22 — вся мысль слайда. $0 в рекламу — отдельной строкой.\nGoogle Slides #1238 · '+oid,'foundation':f1}
s['presentationParts']={'sourceGoogleObjectId':oid,'authorization':'Прямий запит Мирослава 21.09.2026 у сесії: «оце перенеси на окремий слайд … і добав візуалізацію» (два речення про нейросети/поиск і $150).','allowPartTitles':True,'mediaStatus':'ready','slides':[part1,part2]}
s['reason']=(s.get('reason') or '')+' | 21.09 Мирослав: розбито на 2 підслайди — графік + окремий слайд-гонка з реченнями про нейросети/поиск і $150.'
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1); print('patched',oid,'2 parts')
