#!/usr/bin/env python3
"""09.10 Мирослав (нумерація до вставки Свети; поточні rest 260/262/271 — 2226 #105/#107/#116):
— «Дорого»: постер без вшитого тексту (GPT Image 2.5 edit → r257-dorogo-clean.webp), текст і цінники — HTML;
— «Я в этом ноль»: згенерований фон (рука з телефоном, запис голосового), екран телефона — HTML у вигляді Telegram:
  голосове → агент відповідає сайтом прокату авто VIP CAR; палець поверх екрана — вирізка r259-phone-top.png;
— «Сколько стоит год «я подумаю»»: постер без тексту (r268-god-clean.webp), текст — HTML."""
import json, shutil, time
from pathlib import Path
P = Path(__file__).resolve().parent / 'overrides.json'
shutil.copy(P, P.parent / '_bak' / ('overrides-1009-before-r257-259-268-%d.json' % time.time()))
o = json.loads(P.read_text(encoding='utf-8'))
p = o['__visibleGoogleAudit']['slides']['g3f9b3adf0b8_0_2226']['presentationParts']['slides']
def note(x, s): x['note'] = (x.get('note') or '') + '\n09.10 Мирослав: ' + s

x = p[104]; assert 'Дорого' in x['t']
x['b'] = ('<div class="pz pz-dorogo"><i class="pz-tag t1">$250</i><i class="pz-tag t2">$250</i><i class="pz-card">$490</i>'
          '<div class="pz-bot"><p>Один сайт — $250. Вход от $490.</p><b>Это две сделки</b></div></div>')
x['foundation']['block129']['art'] = [{'src': 'assets/gen-rest-1009/r257-dorogo-clean.webp', 'alt': 'Два сайта по $250 и вход $490'}]
note(x, 'текст і цінники — HTML поверх чистого постера.')

x = p[106]; assert 'Я в этом' in x['t']
x['b'] = ('<div class="tg-scene"><div class="gp-col tg-col"><h2 class="gp-title">«Я в этом <em>ноль</em>»</h2><i class="r24q-rule"></i>'
          '<p class="gp-lead">Задачу ставите словами. Программировать не придётся</p></div>'
          '<div class="tg-scr"><div class="tg-head"><i class="tg-back">‹</i><span class="tg-ava">AI</span><div><b>AI-агент</b><small>бот</small></div></div>'
          '<div class="tg-feed">'
          '<div class="tg-msg out tg-voice"><i class="tg-play"></i><span class="tg-wave">' + ''.join('<i style="--h:%d"></i>' % h for h in (3,6,9,5,8,10,7,4,9,6,3,7,10,8,5,9,4,6,8,3,5,7,4)) + '</span>'
          '<span class="tg-dur">0:14</span><span class="tg-time">19:02 <i class="tg-ok">✓✓</i></span></div>'
          '<div class="tg-msg in tg-txt">Готово! Собрал сайт проката авто — проверьте и опубликуйте 🚗<span class="tg-time">19:06</span></div>'
          '<div class="tg-msg in tg-link"><span class="tg-l1">vip-car.vercel.app</span><b>VIP CAR — прокат премиум-авто в Киеве</b>'
          '<span class="tg-l2">Машина, которую вы выбрали, приезжает к вам сама</span><img src="assets/gen-rest-1009/vip-car-poster.webp" alt="Сайт проката авто VIP CAR"><span class="tg-time">19:06</span></div>'
          '</div><div class="tg-input"><span>Сообщение</span><i class="tg-mic"></i></div></div>'
          '<img class="tg-top" src="assets/gen-rest-1009/r259-phone-top.png" alt=""></div>')
x['foundation']['block129']['art'] = [{'src': 'assets/gen-rest-1009/r259-phone-bg.webp', 'alt': 'Рука держит телефон и записывает голосовое'}]
note(x, 'фон — рука з телефоном (голосове), екран — HTML як Telegram, агент відповідає сайтом VIP CAR.')

x = p[115]; assert 'год «я подумаю»' in x['t']
x['b'] = ('<div class="pz pz-god"><div class="pz-big">$3.000</div>'
          '<div class="pz-bot"><p>Один сайт в месяц по $250 — это $3.000 за год</p><b>Ровно столько стоит год в статусе «я подумаю»</b></div></div>')
x['foundation']['block129']['art'] = [{'src': 'assets/gen-rest-1009/r268-god-clean.webp', 'alt': 'Человек в кресле смотрит на ряд несделанных сайтов'}]
note(x, 'текст — HTML поверх чистого постера.')
P.write_text(json.dumps(o, ensure_ascii=False, indent=2), encoding='utf-8')
print('ok')
