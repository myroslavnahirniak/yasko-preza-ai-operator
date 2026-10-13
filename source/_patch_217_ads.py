# 21.09 · 217 «AI-таргет (платная реклама)»: варіант А з design-s217-options.html — SVG-«пульт кампаній» (SMIL, рестарт при вході), лічильник $400.000+, вікно GitHub, три виходи агента, теза, ціна. SVG генерується з тієї ж функції svgA() → assets/s217-ads.svg.html.
import json
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
oid='g3f9b3adf0b8_0_2892'
svg=open('assets/s217-ads.svg.html',encoding='utf-8').read().replace('<svg ','<svg class="s16-ads-svg" ',1)
s=va.get(oid) or {}
s['reason']='21.09 Мирослав: варіант А (спрощений) — SVG-пульт кампаній: FB/IG → агент → 9 оголошень, 5 вимикає, 3 масштабує з перетоком бюджету; $400.000+ лічильником; GitHub у вікні; три виходи агента; теза й ціна.'
s['mediaStatus']='ready'
rm=s.setdefault('remove',[])
for k in ['bg','photos','src','kind','poster','opening','viz','theme','fx','lost','bgside','ptall','img']:
    if k not in rm: rm.append(k)
ITEMS=[('01','Facebook и Instagram','настраивает и запускает кампании'),('02','Объявления','создаёт и тестирует десятками'),('03','24/7','ведёт и переключает без выходных')]
st=s.setdefault('set',{})
st['t']='AI-таргет <em>(платная реклама)</em>'
st['b']=('<div class="s16-board">'+svg+'</div>'
 '<div class="s16-side"><div class="s16-big"><span data-count="400000" data-from="0">$400.000</span>+<small>рекламного бюджета уже прошло через этого агента</small></div>'
 '<div class="s16-git"><div class="win"><div class="bar"><i></i><i></i><i></i><span>github.com · ai-ads-agent</span></div><img src="assets/vlad-1409/uslugi/target-github.jpg" alt="Движок агента-рекламщика на GitHub"></div><p class="cap">движок агента-рекламщика, открытый код</p></div></div>'
 '<div class="s16-out">'+''.join(f'<div><i>{n}</i><b>{a}</b><span>{b}</span></div>' for n,a,b in ITEMS)+'</div>'
 '<p class="s16-claim">Заменяет работу полноценного таргетолога</p>'
 '<span class="s16-price">$300–$800 · в месяц · сложность средняя</span>')
st['lv']=6
f=s.setdefault('foundation',{})
f.update({'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False,
          'mediaBrief':'SVG-пульт кампаній + GitHub.','animationBrief':'SMIL один прохід ~6 с при вході: оголошення → тест → вимкнув/масштабує; лічильник бюджету.'})
f.pop('variant',None); f.pop('layout',None)
f['block129']={'kind':'s16','v2':True,'layout':'s16-ads','eyebrow':'Услуга 6 из 7'}
va[oid]=s
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1); print('patched',oid,len(svg))
