/* v6 source disclosures: local presentation interaction, no reference-site scripts. */
(function(){
 function init(root){
  root.querySelectorAll('.sales-v6').forEach(box=>{
   if(box.dataset.ready)return;box.dataset.ready='1';
   const host=box.closest('.b129');if(!host?.querySelector('.b13-head h1')?.textContent.trim())box.classList.add('v6-no-title');
   box.querySelectorAll('.mb-r[data-x]').forEach(row=>{
    row.setAttribute('role','button');row.tabIndex=0;row.setAttribute('aria-expanded','false');
    function toggle(e){e.stopPropagation();e.preventDefault();let open=!row.classList.contains('open');box.querySelectorAll('.mb-r.open').forEach(x=>{x.classList.remove('open');x.setAttribute('aria-expanded','false')});row.classList.toggle('open',open);row.setAttribute('aria-expanded',String(open));}
    row.addEventListener('click',toggle);row.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' ')toggle(e)});
   });
  });
 }
 new MutationObserver(()=>init(document)).observe(document.documentElement,{childList:true,subtree:true});init(document);
})();
