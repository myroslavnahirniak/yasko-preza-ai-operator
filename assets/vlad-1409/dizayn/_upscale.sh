#!/bin/zsh
# Bytedance Image Upscale (2 кр./шт, 2k). usage: ./_upscale.sh name [name...] — оригінал зберігається в _src/, name.png замінюється апскейлом
cd "$(dirname "$0")"; mkdir -p _src
for name in "$@"; do
  cp "$name.png" "_src/$name.png"
  out=$(higgsfield generate create bytedance_image_upscale --image-references "_src/$name.png" --resolution 2k --wait --wait-timeout 10m --json 2>&1)
  echo "$out" > "_src/$name.job.json"
  url=$(echo "$out" | python3 -c "
import json,sys,re
raw=sys.stdin.read()
try:
  d=json.loads(raw); j=d[0] if isinstance(d,list) else d; print(j.get('result_url') or j.get('min_result_url') or '')
except Exception:
  m=re.findall(r'https?://\S+\.(?:png|jpg|jpeg|webp)\S*',raw); print(m[0] if m else '')")
  if [ -n "$url" ]; then curl -sL "$url" -o "_src/$name.up"; python3 -c "
from PIL import Image; im=Image.open('_src/$name.up').convert('RGB'); im.save('$name.png'); print('$name', im.size)"; else echo "NO URL $name"; echo "$out" | head -c 400; fi
done
echo UPSCALE_DONE
