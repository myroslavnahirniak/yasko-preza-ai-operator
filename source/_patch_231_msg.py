# 21.09 · 231 «Люди с нейросетей покупают лучше остальных» → 2 підслайди (Мирослав): частина 1 — три метрики (графік по центру); частина 2 — цитата клієнта як повідомлення в чаті (аватар-іконка, по центру) і висновок «Он сам увидел заказы — и продлил работу».
import json,copy
p='source/overrides.json'; o=json.load(open(p)); va=o['__visibleGoogleAudit']['slides']
oid='g409d4d20be6_0_417'; s=va[oid]
b1=s['set']['b']; cut=b1.index('<div class="s16-bottom">'); b1=b1[:cut]
f1=copy.deepcopy(s['foundation'])
AV='<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="23" fill="#15110d" stroke="#3a3129"/><circle cx="24" cy="19" r="7.5" fill="none" stroke="#f5f3ee" stroke-width="2"/><path d="M10 40c1.5-8 7-12 14-12s12.5 4 14 12" fill="none" stroke="#f5f3ee" stroke-width="2" stroke-linecap="round"/></svg>'
part2={'t':'Он сам увидел заказы — <em>и продлил работу</em>',
 'b':('<div class="s16-msg"><div class="who">'+AV+'<div><b>Клиент</b><span>интернет-магазин It’s Beauty</span></div></div>'
      '<div class="bubble">«Я стал реально чаще видеть органические заказы — и конкретно по той категории, которую ты сейчас качаешь»</div>'
      '<p class="src">слова самого клиента</p></div>'),
 'lv':6,'note':'Кейс Ани, часть 4б: цитата клиента как сообщение в чате; вывод — «Он сам увидел заказы — и продлил работу».\nGoogle Slides #1240 · '+oid,
 'foundation':copy.deepcopy(f1)}
part2['foundation']['block129']={'kind':'s16','v2':True,'layout':'s16-msg','eyebrow':'И это деньги','sound':False}
part2['foundation']['mediaBrief']='Цитата клієнта як повідомлення.'; part2['foundation']['animationBrief']='Повідомлення спливає, потім висновок.'
part1={'t':s['set']['t'],'b':b1,'lv':6,'note':'Кейс Ани, часть 4а: три метрики против обычного трафика.\nGoogle Slides #1240 · '+oid,'foundation':f1}
s['presentationParts']={'sourceGoogleObjectId':oid,'authorization':'Прямий запит Мирослава 21.09.2026 у сесії: «оце теж перенеси на окремий слайд … оформи по центру … ніби це їй написав хтось, аватарку постав іконку».','allowPartTitles':True,'mediaStatus':'ready','slides':[part1,part2]}
s['reason']=(s.get('reason') or '')+' | 21.09 Мирослав: цитату винесено на окремий слайд-повідомлення (s16-msg); метрики вирівняно по центру.'
json.dump(o,open(p,'w'),ensure_ascii=False,indent=1); print('patched',oid,'2 parts')
