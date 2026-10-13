# name.png (апскейл або оригінальний кроп) -> name.webp, довга сторона <= 1800px, q88
from PIL import Image
import glob,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
for f in sorted(glob.glob('*.png')):
    n=f[:-4]; im=Image.open(f).convert('RGB'); w,h=im.size; k=min(1,1800/max(w,h))
    if k<1: im=im.resize((round(w*k),round(h*k)),Image.LANCZOS)
    im.save(n+'.webp',quality=88,method=6); print(n,(w,h),'->',im.size,os.path.getsize(n+'.webp')//1024,'KB')
