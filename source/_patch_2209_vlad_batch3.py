# 22.09 · правки Влада, пачка 3: фото разбомбленного офиса (55); «12 модулей»; убрать «Задачи — со 2-го блока…»; вернуть «Блок 2 · Продукт и витрина»; «Инструкция + задание» после «Как это устроено»; живой сайт skills-navigator в «46 готовых задач».
import json,copy,re
p='source/overrides.json'; o=json.load(open(p,encoding='utf-8')); va=o['__visibleGoogleAudit']['slides']
st=lambda t:re.sub('<[^>]+>','',t or '')
def why(s,msg): s['reason']=(s.get('reason') or '')+' | 22.09 Влад: '+msg
# 55 · офис
L=o['__lifeStory']['slides']['g3fadf66108e_0_405']
L['photos']=[{'src':'assets/photo/vlad/office-bombed.jpg','width':960,'height':1280,'role':'photo','fit':'cover'}]
L.pop('placeholders',None); L.pop('placeholderHint',None); L['variant']='portrait'; L['sourceMediaNotes']='Фото Влада: разбитые окна офиса (ofice.jpg, 22.09).'
sales=va['g3f9b3adf0b8_0_2226']; P=sales['presentationParts']['slides']
def find(title): return [i for i,x in enumerate(P) if st(x.get('t')).strip().startswith(title)][0]
# 12 модулей
i=find('Полная'); assert '13 модулей' in P[i]['t']; P[i]['t']=P[i]['t'].replace('13 модулей','12 модулей')
# Фундамент: убрать лишний текст
i=find('Фундамент'); b=P[i]['b']; old='<p class="note center">Задачи — со 2-го блока. Здесь навык и инструменты</p>'; assert old in b; P[i]['b']=b.replace(old,'')
# Блок 2 · Продукт и витрина — после Фундамента
pre=json.load(open('source/sales-v6-20260921/pre-migration-sales.json',encoding='utf-8'))[8]
assert 'Продукт и витрина' in pre['t']
blk2={k:copy.deepcopy(pre[k]) for k in ('t','k','b','lv','foundation') if k in pre}
blk2['note']='Блок 2 · Продукт и витрина (возвращён 22.09 по правке Влада «блок 2 пропустил»; из дореміграційних даних U010).\n'+(pre.get('note') or '')
blk2['a']=P[i].get('a',3); blk2['mvp']=P[i].get('mvp',1)
P.insert(i+1,blk2)
# Инструкция + задание — после «Как это устроено»
i=find('Как это'); base=P[i]
ws={'t':'Инструкция + задание <em>для тренировки</em>','lv':base.get('lv',6),'a':base.get('a',3),'mvp':base.get('mvp',1),
 'foundation':copy.deepcopy(base.get('foundation',{})),
 'b':'<i class="sv-marker sv-steps sv-U005b" hidden></i><p class="sv-description">К каждому уроку — воркшоп с пошаговой инструкцией и заданием на своём проекте</p><div class="sv-screen"><div class="sv-media"><img src="assets/vlad-1409/sales/sh-workshop4.jpg" alt="Воркшоп №4: Сайт за вечер"></div></div><p class="sv-end">ai-marketolog-workshop-4.vercel.app</p>',
 'note':'Инструкция + задание для тренировки (добавлен 22.09 по правке Влада «после этого слайда поставь этот»). Скрин ai-marketolog-workshop-4.vercel.app.'}
P.insert(i+1,ws)
# 46 задач — живой сайт
i=find('46 готовых'); b=P[i]['b']
old=re.search(r'<div class="sv-proof"><div class="sv-media"><img[^>]*></div></div>',b).group(0)
P[i]['b']=b.replace(old,'<div class="sv-proof"><div class="sv-media sv-media-live"><iframe data-src="https://skills-navigator-five.vercel.app/" title="Навигатор задач — живой сайт" loading="lazy"></iframe></div></div>')
why(sales,'«12 модулей»; убран «Задачи — со 2-го блока…»; возвращён Блок 2 · Продукт и витрина; добавлен «Инструкция + задание для тренировки»; в «46 готовых задач» живой сайт skills-navigator-five.vercel.app.')
json.dump(o,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1); print('batch3 ok, parts:',len(P))
