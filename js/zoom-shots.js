/* 09.10 Мирослав · rest 139 (після «Окна Киев»): колаж скрінів переписки — клік по скріну відкриває його на весь екран.
   Дека гортає слайд кліком по документу, тож тут перехоплюємо клік і клавіші на window (capture), поки попап відкритий.
   ←/→ — сусідній скрін, Esc або клік — закрити. */
(function(){
  var box=null, list=[], cur=0;
  function show(k){ cur=(k+list.length)%list.length; box.querySelector('img').src=list[cur]; box.querySelector('.zs-n').textContent=(cur+1)+' / '+list.length; }
  function open(shots,k){
    list=shots; box=document.createElement('div'); box.className='zs-pop';
    box.innerHTML='<img alt=""><span class="zs-n"></span><span class="zs-x" aria-hidden="true">×</span>';
    document.body.appendChild(box); show(k); requestAnimationFrame(function(){ box.classList.add('on'); });
  }
  function close(){ if(!box) return; var b=box; box=null; b.classList.remove('on'); setTimeout(function(){ b.remove(); },200); }
  window.addEventListener('click',function(e){
    if(box){ e.stopPropagation(); e.preventDefault(); close(); return; }
    var t=e.target.closest&&e.target.closest('[data-zoom]'); if(!t) return;
    var wrap=t.closest('.s2n-shots'); if(!wrap||!wrap.closest('.slide.on')) return;
    e.stopPropagation(); e.preventDefault();
    var items=[].slice.call(wrap.querySelectorAll('[data-zoom]'));
    open(items.map(function(x){ return x.getAttribute('data-zoom'); }), items.indexOf(t));
  },true);
  window.addEventListener('keydown',function(e){
    if(!box) return;
    e.stopPropagation(); e.preventDefault();
    if(e.key==='ArrowRight'||e.key===' ') show(cur+1);
    else if(e.key==='ArrowLeft') show(cur-1);
    else close();
  },true);
}());
