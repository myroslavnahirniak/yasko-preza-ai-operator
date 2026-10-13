# 21.09 · слайд «Услуги» (Google 204, g409d4d20be6_0_489): замість статичного скрина — живий сайт roma-kp-site.vercel.app
# (локальна копія assets/sites/roma-kp/) у вікні браузера. Кожен крок прокручує сайт до наступного розділу (10 розділів),
# сайт можна крутити колесом рукою — крапки кроків слідують за розділом. Запуск: python3 source/_patch_193_roma_live.py → стандартна збірка.
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(ROOT,'source/overrides.json'); o=json.load(open(p,encoding='utf-8')); va=o['__visibleGoogleAudit']['slides']
oid='g409d4d20be6_0_489'
s=va.get(oid) or {}
s['reason']='21.09 Мирослав: покрокова анімація — живий сайт (локальна копія roma-kp-site.vercel.app) у вікні браузера; крок = розділ сайту, колесом можна крутити рукою.'
s['mediaStatus']='ready'
rm=s.setdefault('remove',[])
for k in ['bg','photos','src','kind','poster','opening','viz','theme','fx','lost','bgside','ptall','img','k']:
    if k not in rm: rm.append(k)
st=s.setdefault('set',{})
st['t']='<em>Услуги</em>'
st['b']=('<div class="s16-live" aria-label="roma-kp-site.vercel.app">'
         '<div class="s16-bar"><i></i><i></i><i></i><span class="s16-url">roma-kp-site.vercel.app</span></div>'
         '<div class="s16-view" data-w="1100"><iframe src="assets/sites/roma-kp/index.html" title="Сайт Романа Ильина — собран агентом"></iframe></div>'
         '</div>')
st['lv']=6
f=s.setdefault('foundation',{})
f.update({'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False,
          'mediaBrief':'Живий сайт у вікні браузера (локальна копія: 242 кадри планети + GSAP/Lenis).',
          'animationBrief':'Вікно з’являється; кожен крок плавно прокручує сайт до наступного розділу — кадри планети й тексти анімуються самим сайтом. Колесом можна крутити рукою.'})
f.pop('variant',None); f.pop('layout',None)
f['block129']={'kind':'s16','v2':True,'layout':'s16-live','focus':'.s16-none',
  'steps':['Тело — не цель','01 · Большое «зачем»','02 · Почему прошлый раз не сработал','03 · Как это устроено','04 · Тренировки',
           '05 · Управляемый цикл','06 · Питание','07 · План питания','08 · Результат','Форматы и цена']}
va[oid]=s
json.dump(o,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('patched',oid)
