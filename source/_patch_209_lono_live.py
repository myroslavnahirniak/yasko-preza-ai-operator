# 21.09 · слайд 209 «Имея в арсенале 3 агента, она:» (g409d4d20be6_0_208): варіант А — три пункти зверху + живий сайт LONO (локальна копія assets/sites/lono, символьні лінки /_next, /assets/concepts, /assets/img), крок = розділ сайту.
import json
p='source/overrides.json'; o=json.load(open(p,encoding='utf-8')); va=o['__visibleGoogleAudit']['slides']
oid='g409d4d20be6_0_208'; s=va.get(oid) or {}
s['reason']='21.09 Мирослав: варіант А — заголовок і три пункти зверху, нижче вікно браузера з живим сайтом lono-next.vercel.app (локальна копія, покрокова прокрутка як на 193).'
s['mediaStatus']='ready'
rm=s.setdefault('remove',[])
for k in ['bg','photos','src','kind','poster','opening','viz','theme','fx','lost','bgside','ptall','img','k']:
    if k not in rm: rm.append(k)
ROWS=['начинала с AI-дизайна','продала сайт за $1000','создала контент-завод для соц сетей']
st=s.setdefault('set',{}); st['t']='Имея в арсенале <em>3 агента</em>, она:'
st['b']=('<div class="s16-rows">'+''.join(f'<div><i>0{i+1}</i><b>{r}</b></div>' for i,r in enumerate(ROWS))+'</div>'
 '<div class="s16-live" aria-label="lono-next.vercel.app"><div class="s16-bar"><i></i><i></i><i></i><span class="s16-url">lono-next.vercel.app</span></div>'
 '<div class="s16-view" data-w="1100"><iframe src="assets/sites/lono/index.html" title="LONO — сайт, проданный за $1000"></iframe></div></div>')
st['lv']=6
f=s.setdefault('foundation',{})
f.update({'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False,'mediaBrief':'Живий сайт LONO у вікні браузера, три пункти зверху.','animationBrief':'Крок — розділ сайту (8), колесом можна крутити рукою.'})
f.pop('variant',None); f.pop('layout',None)
f['block129']={'kind':'s16','v2':True,'layout':'s16-live','focus':'.s16-none','steps':['Главная','What it is','Owners','Method','Sprint','Partners','About','Contact']}
va[oid]=s
json.dump(o,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1); print('patched',oid)
