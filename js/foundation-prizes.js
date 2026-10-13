/* Prize sequence: live source copy, finite motion, no extra navigation steps. */
(function () {
  'use strict';
  function esc(value) { return String(value == null ? '' : value).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  function lazy(html) { return String(html || '').replace(/\ssrc=(['"])(assets\/)/g, ' data-src=$1$2'); }
  var cardPaths = [
    '<rect x="15" y="9" width="50" height="62" rx="7"/><path d="M24 20h32v10H24zM26 42h4m13 0h4m-21 12h4m13 0h4m9-12v17"/>',
    '<path d="M13 24h54v38H13zM13 34h54M25 47h16m-16 7h9"/><circle cx="54" cy="52" r="5"/>',
    '<path d="M18 63V45q0-10 12-10h19q13 0 13-11V14M54 22l8-8 8 8"/><circle cx="18" cy="65" r="5"/>',
    '<rect x="9" y="15" width="62" height="49" rx="7"/><path d="m26 29-10 10 10 10m28-20 10 10-10 10M44 27l-8 24"/>',
    '<rect x="10" y="19" width="60" height="43" rx="6"/><path d="m12 22 28 23 28-23M12 59l17-16m39 16L51 43"/>',
    '<path d="M32 48l16-16m-24 7-5 5a11 11 0 0 0 16 16l9-9m-8-22 9-9a11 11 0 0 1 16 16l-5 5"/>'
  ];
  function cardIcon(i) { return '<svg viewBox="0 0 80 80" fill="none" aria-hidden="true">' + cardPaths[i % cardPaths.length] + '</svg>'; }
  function signal() {
    return '<div class="fp-signal" aria-hidden="true"><div class="fp-wave">' + [14,24,38,52,32,65,42,28,49,33,18].map(function (h,i) { return '<i style="--wh:'+h+'%;--wi:'+i+'"></i>'; }).join('') + '</div><div class="fp-signal-line"><i></i></div><div class="fp-secret-message"><i></i><i></i><i></i><i></i><i></i></div></div>';
  }
  function site() {
    return '<div class="fp-site-preview" aria-hidden="true"><div class="fp-browser-bar"><i></i><i></i><i></i><u></u></div><div class="fp-site-canvas"><div class="fp-site-nav"><i></i><span></span><span></span></div><div class="fp-site-hero"><div class="fp-site-lines"><b></b><b></b><span></span><span></span><u></u></div><div class="fp-site-object"><i></i><i></i><i></i></div></div><div class="fp-site-tiles"><i></i><i></i><i></i></div></div><div class="fp-site-ready"><svg viewBox="0 0 24 24"><path d="m5 12 5 5 10-11"/></svg></div></div>';
  }
  function render(s,idx) {
    var cfg=s.foundation || {}, local=Number(cfg.local || idx+1);
    if(local<27 || local>32) return null;
    var sec=document.createElement('section');
    sec.className='slide foundation fp fp-'+local;
    sec.dataset.idx=idx; sec.dataset.lv=s.lv || 5; sec.dataset.foundationLocal=local; sec._s=s;
    var title=String(s.t || ''), match=title.match(/^(Приз №[123]\s*—)\s*(.*)$/);
    var headline=match ? '<span class="fp-title-kicker">'+esc(match[1])+'</span><span class="fp-title-main">'+esc(match[2])+'</span>' : esc(title);
    if(local===32) headline=esc(title).replace(/разницу/, '<span class="fp-title-accent">разницу</span>');
    sec.innerHTML='<div class="fp-ambient" aria-hidden="true"></div><header class="fp-header"><h1 class="fp-title split-done">'+headline+'</h1></header><div class="fp-body">'+lazy(s.b)+'</div>';
    var body=sec.querySelector('.fp-body');
    if(local===27) {
      [].forEach.call(body.querySelectorAll('.hm'),function(card,i) {
        card.style.setProperty('--card-i',i);
        var old=card.querySelector('i');
        if(old) old.outerHTML='<i class="fp-card-icon">'+cardIcon(i)+'</i>';
      });
    }
    if(local===28) {
      var box=document.createElement('div'); box.className='fp-document-window embedwrap';
      box.innerHTML='<div class="fp-browser-bar" aria-hidden="true"><i></i><i></i><i></i><u></u></div><iframe data-src="'+esc(s.src || 'https://holst-ai-operator.vercel.app/')+'" title="'+esc(s.t)+'" loading="lazy" allow="clipboard-write"></iframe>';
      box.addEventListener('click',function(event){event.stopPropagation();});
      sec.appendChild(box);
    }
    if(local===29) sec.insertAdjacentHTML('beforeend',signal());
    if(local===30) {
      var chat=body.querySelector('.chatbox');
      if(chat) {
        chat.classList.remove('type','seq'); chat.classList.add('fp-chat');
        [].forEach.call(chat.querySelectorAll('.cmsg'),function(message,i){ message.style.setProperty('--message-i',i); });
      }
      sec.insertAdjacentHTML('beforeend',site());
    }
    if(local===31) {
      var amount=body.querySelector('b.acc');
      var percent=amount&&amount.textContent.match(/на\s+(\d+)%\s+дешевле/);
      if(percent) {
        amount.innerHTML='<span class="fp-percent-prefix">на </span><span class="fp-percent-number">'+percent[1]+'%</span><span class="fp-percent-suffix"> дешевле</span>';
        var punctuation=amount.nextSibling;
        if(punctuation && punctuation.nodeType===3 && /^\s*[.!]\s*$/.test(punctuation.nodeValue)) {
          amount.querySelector('.fp-percent-suffix').appendChild(punctuation);
        }
      }
    }
    if(local===32) {
      var table=body.querySelector('.pricecmp');
      if(table) {
        table.setAttribute('role','table'); table.setAttribute('aria-label',s.t);
        [].forEach.call(table.querySelectorAll('.pr'),function(row,i){
          row.setAttribute('role','row'); row.style.setProperty('--row-i',i);
          [].forEach.call(row.children,function(cell){cell.setAttribute('role',i===0?'columnheader':'cell');});
        });
        var emoji=table.querySelector('.hgs');
        if(emoji) emoji.innerHTML='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m14 2-9 12h7l-2 8 9-13h-7z"/></svg>';
      }
    }
    return sec;
  }
  window.FoundationPrizes={render:render};
})();
