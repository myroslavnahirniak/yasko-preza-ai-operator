# 21.09 · 205 «Имеет базу 100+ каруселей»: артефакт Claude «Сто каруселей» (локальна копія assets/artifacts-2109/carousels/index.html) у вікні браузера, s16-frame; клік по панелі — на весь слайд.
import json
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
oid='g409d4d20be6_0_182'
s=va.get(oid) or {}
s['reason']='21.09 Мирослав: артефакт «Сто каруселей» iframe-ом усередині прези (s16-frame), масштаб з 1100px, автоскрол; клік по панелі вікна — на весь слайд.'
s['mediaStatus']='ready'
rm=s.setdefault('remove',[])
for k in ['bg','photos','src','kind','poster','opening','viz','theme','fx','lost','bgside','ptall','img']:
    if k not in rm: rm.append(k)
st=s.setdefault('set',{})
st['t']='Имеет базу <em>100+ каруселей</em>'
st['b']=('<div class="s16-frame" aria-label="Сто каруселей"><div class="s16-fbar"><i></i><i></i><i></i><span class="s16-url">Сто каруселей · 100 кадров из 334 находок</span><span class="s16-hint">▶ на весь слайд</span></div>'
         '<div class="s16-view" data-w="1100"><iframe src="assets/artifacts-2109/carousels/index.html" title="Сто каруселей — библиотека референсов" loading="lazy"></iframe></div></div>')
st['lv']=6
f=s.setdefault('foundation',{})
f.update({'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False,
          'mediaBrief':'Артефакт «Сто каруселей» у вікні браузера.','animationBrief':'Поява вікна; iframe сам гортає; клік — на весь слайд.'})
f.pop('variant',None); f.pop('layout',None)
f['block129']={'kind':'s16','v2':True,'layout':'s16-frame','eyebrow':'Агент · контент'}
va[oid]=s
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1); print('patched',oid)
