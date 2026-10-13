#!/bin/zsh
# Batch: GPT Image 2.5, 1:1, 2k, xhigh. Usage: ./_gen.sh <name> "<prompt>"
set -e
cd "$(dirname "$0")"
name="$1"; prompt="$2"
out=$(higgsfield generate create gpt_image_2_5 --prompt "$prompt" --aspect_ratio 1:1 --resolution 2k --quality xhigh --wait --wait-timeout 15m --json 2>&1)
echo "$out" > "${name}.job.json"
url=$(echo "$out" | python3 -c "
import json,sys,re
raw=sys.stdin.read()
try:
  d=json.loads(raw)
except Exception:
  m=re.findall(r'https?://\S+\.(?:png|jpg|jpeg|webp)\S*',raw); print(m[0] if m else ''); sys.exit()
def walk(o):
  if isinstance(o,dict):
    for k,v in o.items():
      r=walk(v)
      if r: return r
  elif isinstance(o,list):
    for v in o:
      r=walk(v)
      if r: return r
  elif isinstance(o,str) and o.startswith('http') and re.search(r'\.(png|jpg|jpeg|webp)',o): return o
print(walk(d) or '')
")
[ -n "$url" ] || { echo "NO URL for $name"; exit 1; }
curl -sL "$url" -o "${name}.png"
printf '%s\n%s\n' "$name" "$prompt" >> _prompts.log
echo "$name -> ${name}.png ($url)"
