# 21.09 · 202 «Контент-завод с AI-аватаром»: варіант 2 (Мирослав) — три ролики аватара з артефакту Claude (assets/s202-avatar/clip-1..3.mp4) віялом у 3D, усі елементи джерела збережено.
import json
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
oid='g3f9b3adf0b8_0_2884'; A='assets/s202-avatar/'
s=va.get(oid) or {}
s['reason']='21.09 Мирослав: варіант 2 — веєр із трьох телефонів (ролики аватара з артефакту «Контент-завод»), підписи платформ, три виходи агента, теза, ціна; hover — 3D-нахил.'
s['mediaStatus']='ready'
rm=s.setdefault('remove',[])
for k in ['bg','photos','src','kind','poster','opening','viz','theme','fx','lost','bgside','ptall','img']:
    if k not in rm: rm.append(k)
def ph(cls,n,title):
    return (f'<figure class="{cls}"><video src="{A}clip-{n}.mp4" poster="{A}poster-{n}.jpg" muted autoplay loop playsinline preload="metadata" title="{title}"></video></figure>')
st=s.setdefault('set',{})
st['t']='Контент-завод с <em>AI-аватаром</em>'
st['b']=('<div class="s16-avafan"><div class="s16-tilt">'+ph('a',1,'Reels · Instagram')+ph('b',2,'Shorts · YouTube')+ph('c',3,'TikTok')+'</div></div>'
 '<div class="s16-caps"><div><b>Reels · Instagram</b><span>вертикаль до 60 секунд</span></div><div><b>Shorts · YouTube</b><span>вертикаль до 60 секунд</span></div><div><b>TikTok</b><span>своя нарезка и хук</span></div></div>'
 '<div class="s16-out"><div><i>01</i><b>Контент-план под площадку</b></div><div><i>02</i><b>Посты, сценарии, Reels с аватаром</b></div><div><i>03</i><b>Выкладка по расписанию</b><span>аккаунт живёт без вас</span></div></div>'
 '<p class="s16-claim">готовый контент для соцсетей, который приносит подписчиков и клиентов</p>'
 '<span class="s16-price">$400–$1.400 · за пакет в месяц · сложность средняя</span>')
st['lv']=6
f=s.setdefault('foundation',{})
f.update({'type':'content','local':0,'sourceOnly':False,'omitMedia':True,'media':[],'mediaNeeded':False,
          'mediaBrief':'Три ролики аватара віялом у 3D.','animationBrief':'Поява віяла і карток; відео грають самі; hover — нахил.'})
f.pop('variant',None); f.pop('layout',None)
f['block129']={'kind':'s16','v2':True,'layout':'s16-avafan','eyebrow':'Услуга 4 из 7'}
va[oid]=s
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1); print('patched',oid)
