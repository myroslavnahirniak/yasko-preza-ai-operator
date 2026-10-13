#!/bin/zsh
# GPT Image 2.5, 3:2, face reference. Usage: ./_gen.sh <name> "<prompt>"
cd "$(dirname "$0")"
name="$1"; prompt="$2"; ref="../photo/vlad-avatar.jpg"
out=$(higgsfield generate create gpt_image_2_5 --prompt "$prompt" --image-references "$ref" --aspect_ratio 3:2 --resolution 2k --quality xhigh --wait --wait-timeout 15m --json 2>&1)
echo "$out" > "${name}.job.json"
url=$(python3 - "$out" <<'PY'
import json,sys,re
raw=sys.argv[1]
try: d=json.loads(raw)
except Exception:
  m=re.findall(r'https?://\S+\.(?:png|jpg|jpeg|webp)\S*',raw); print(m[0] if m else ''); sys.exit()
def walk(o):
  if isinstance(o,dict):
    for v in o.values():
      r=walk(v)
      if r: return r
  elif isinstance(o,list):
    for v in o:
      r=walk(v)
      if r: return r
  elif isinstance(o,str) and o.startswith('http') and re.search(r'\.(png|jpg|jpeg|webp)',o): return o
print(walk(d) or '')
PY
)
[ -n "$url" ] || { echo "NO URL for $name"; exit 1; }
curl -sL "$url" -o "${name}.png" && python3 -c "from PIL import Image; im=Image.open('${name}.png').convert('RGB'); im.save('${name}.webp',quality=86)"
printf '%s\n%s\n' "$name" "$prompt" >> _prompts.log
echo "$name -> ${name}.webp"
