import json,glob,os,subprocess
for jf in glob.glob('*.job.json'):
    name=jf[:-9]
    try: d=json.load(open(jf))
    except Exception: continue
    j=d[0] if isinstance(d,list) else d
    mn,full=j.get('min_result_url'),j.get('result_url')
    if mn and not os.path.exists(name+'.webp'):
        subprocess.run(['curl','-sL',mn,'-o',name+'.webp'])
    if full and not os.path.exists(name+'.master.png'):
        subprocess.run(['curl','-sL',full,'-o',name+'.master.png'])
    if os.path.exists(name+'.png'): os.remove(name+'.png')
    print(name, os.path.getsize(name+'.webp') if os.path.exists(name+'.webp') else '-', os.path.getsize(name+'.master.png') if os.path.exists(name+'.master.png') else '-')
