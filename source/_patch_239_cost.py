# 21.09 · 239 «Ваши расходы на всё это»: замість трьох простих іконок — SMIL-сцена (s16-smil): офіс, команда, зарплати промальовуються штрихом, оживають (вікна засвічуються, монети ростуть), потім кожен перекреслюється жовтим і гасне, під ним «$0». Картка підписки без змін.
import json
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
oid='g3f9b3adf0b8_0_2932'; s=va[oid]
Y='#fdd506';C='#d9d2c4';MU='#8c816a';DM='#5a5148';D='7s'
def draw(t0,t1): # stroke draw once (keyTimes fractions of 7s)
    return f'<animate attributeName="stroke-dashoffset" values="1;1;0;0" keyTimes="0;{t0:.3f};{t1:.3f};1" dur="{D}" fill="freeze" calcMode="spline" keySplines="0 0 1 1;.2 .8 .2 1;0 0 1 1"/>'
def pop(t0,w=.05): return f'<animate attributeName="opacity" values="0;0;1;1" keyTimes="0;{t0:.3f};{min(1,t0+w):.3f};1" dur="{D}" fill="freeze"/>'
def fade(t0,to=.32,w=.08): return f'<animate attributeName="opacity" values="1;1;{to};{to}" keyTimes="0;{t0:.3f};{min(1,t0+w):.3f};1" dur="{D}" fill="freeze"/>'
def P(d,t0,t1,col=C,w=1.6): return f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1">{draw(t0,t1)}</path>'
def cross(cx,cy,t0):
    d=f'M{cx-34} {cy-30} C{cx-14} {cy-16} {cx+8} {cy+6} {cx+36} {cy+30}'
    return f'<path d="{d}" fill="none" stroke="{Y}" stroke-width="4" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" filter="drop-shadow(0 0 4px rgba(253,213,6,.6))">{draw(t0,t0+.07)}</path>'
def badge(cx,y,t0):
    return f'<g opacity="0">{pop(t0)}<rect x="{cx-22}" y="{y-11}" width="44" height="22" rx="11" fill="{Y}"/><text x="{cx}" y="{y+5}" text-anchor="middle" font-family="Unbounded,sans-serif" font-size="12" font-weight="500" fill="#0b0907">$0</text></g>'
def label(cx,y,txt,t0):
    return f'<g opacity="0">{pop(t0)}<text x="{cx}" y="{y}" text-anchor="middle" font-family="Manrope,sans-serif" font-size="14" fill="#aaa18f">{txt}</text><line x1="{cx-len(txt)*3.9}" y1="{y-5}" x2="{cx+len(txt)*3.9}" y2="{y-5}" stroke="{Y}" stroke-width="2" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1">{draw(t0+.02,t0+.08)}</line></g>'
W,H=600,172
# ── 1. офіс (cx=100) ──
o1=100;g1=f'<g opacity="1">{fade(.40)}'
g1+=P(f'M{o1-40} 96 V34 H{o1+40} V96',.05,.22)+P(f'M{o1-48} 96 H{o1+48}',.10,.18)+P(f'M{o1-44} 34 H{o1+44} L{o1+38} 26 H{o1-38} Z',.12,.22)
g1+=P(f'M{o1-8} 96 V74 H{o1+8} V96',.18,.26)
for r,yy in enumerate((44,60)):
    for c,xx in enumerate((o1-30,o1-12,o1+6,o1+24)):
        g1+=f'<rect x="{xx}" y="{yy}" width="10" height="10" fill="{Y}" opacity="0"><animate attributeName="opacity" values="0;0;.9;.9;.25;.25" keyTimes="0;{.24+(r*4+c)*.012:.3f};{.27+(r*4+c)*.012:.3f};.40;.48;1" dur="{D}" fill="freeze"/></rect>'
        g1+=P(f'M{xx} {yy} h10 v10 h-10 Z',.14+(r*4+c)*.01,.22+(r*4+c)*.01,MU,1.2)
g1+=P(f'M{o1+58} 96 V80 M{o1+58} 82 c-8-2-10-10-6-14 c4-4 10-2 12 4 c4-2 8 2 6 8 c-2 4-8 4-12 2',.2,.3,MU,1.3)
g1+='</g>'+cross(o1,66,.44)+badge(o1,112,.52)+label(o1,160,'офис',.30)
# ── 2. команда (cx=300) ──
o2=300;g2=f'<g opacity="1">{fade(.46)}'
g2+=P(f'M{o2-52} 78 H{o2+52} M{o2-46} 78 V96 M{o2+46} 78 V96',.08,.2)
for k,xx in enumerate((o2-30,o2,o2+30)):
    d=.12+k*.05
    g2+=P(f'M{xx} 44 a8 8 0 1 0 0.1 0',d,d+.08)+P(f'M{xx-14} 78 c0-12 6-18 14-18 s14 6 14 18',d+.04,d+.12)
    g2+=P(f'M{xx-11} 70 h22 l-2 8 h-18 Z',d+.08,d+.15,MU,1.3)
    g2+=f'<g opacity="0">{pop(.30+k*.04)}<path d="M{xx+10} 30 h16 a4 4 0 0 1 4 4 v8 a4 4 0 0 1 -4 4 h-8 l-5 5 v-5 h-3 a4 4 0 0 1 -4 -4 v-8 a4 4 0 0 1 4 -4 z" fill="{Y}"/><circle cx="{xx+15}" cy="38" r="1.4" fill="#0b0907"/><circle cx="{xx+20}" cy="38" r="1.4" fill="#0b0907"/><circle cx="{xx+25}" cy="38" r="1.4" fill="#0b0907"/></g>'
g2+='</g>'+cross(o2,62,.50)+badge(o2,112,.58)+label(o2,160,'команда',.34)
# ── 3. зарплати (cx=500) ──
o3=500;g3=f'<g opacity="1">{fade(.52)}'
# один конверт: заливка панеллю, контур, клапан; усередині купюра з $
g3+=f'<rect x="{o3-40}" y="52" width="80" height="50" rx="5" fill="#15110d" stroke="{C}" stroke-width="1.6" opacity="0">{pop(.10,.06)}</rect>'
g3+=P(f'M{o3-40} 57 l40 26 l40-26',.16,.26,C,1.6)+P(f'M{o3-40} 100 l30-22 M{o3+40} 100 l-30-22',.22,.30,MU,1.2)
g3+=f'<g opacity="0">{pop(.30)}<rect x="{o3-24}" y="34" width="48" height="26" rx="3" fill="#0b0907" stroke="{Y}" stroke-width="1.6"/><circle cx="{o3}" cy="47" r="8" fill="{Y}"/><text x="{o3}" y="51" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="11" font-weight="700" fill="#0b0907">$</text><rect x="{o3-19}" y="40" width="3" height="14" rx="1.5" fill="{Y}" opacity=".6"/><rect x="{o3+16}" y="40" width="3" height="14" rx="1.5" fill="{Y}" opacity=".6"/></g>'
g3+='</g>'+cross(o3,62,.56)+badge(o3,112,.64)+label(o3,160,'зарплаты',.38)
svg=f'<svg class="s16-smil s238-scene-svg" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">'+g1+g2+g3+'</svg>'
b=s['set']['b']; a=b.index('<div class="s238-scene">') if '<div class="s238-scene">' in b else b.index('<div class="s238-expenses">'); e=b.index('<div class="s238-subscription">')
s['set']['b']=b[:a]+'<div class="s238-scene">'+svg+'</div>'+b[e:]
s['reason']=(s.get('reason') or '')+' | 21.09 Мирослав: прості іконки замінено SMIL-сценою (промальовка → оживання → жовте перекреслення → $0).'
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1); print('patched',len(svg))
