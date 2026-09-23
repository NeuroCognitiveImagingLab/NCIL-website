#!/usr/bin/env python3
"""Square-crop head-and-shoulders portraits around the detected face.

Framing contract: the face bounding box occupies FACE_FRAC of the square's
height, and the eye line sits EYE_FRAC down from the top. Those two numbers are
the whole design -- everything else is clamping to stay inside the source image.
"""
import json, os, sys
from PIL import Image, ImageOps

FACE_FRAC = float(os.environ.get('FACE_FRAC', 0.52))
EYE_FRAC  = float(os.environ.get('EYE_FRAC',  0.42))
SIDE      = int(os.environ.get('SIDE', 800))

W = os.environ['W']
recs = json.load(open(f"{W}/faces.json"))
outdir = sys.argv[1] if len(sys.argv) > 1 else f"{W}/out"
os.makedirs(outdir, exist_ok=True)

report = []
for r in recs:
    if 'error' in r or len(r['faces']) != 1:
        continue
    src = r['file']
    f = r['faces'][0]
    im = Image.open(os.path.join(f"{W}/originals", src))
    im = ImageOps.exif_transpose(im)          # honour phone rotation
    if im.mode != 'RGB':
        im = im.convert('RGB')
    iw, ih = im.size
    # Vision ran on the un-transposed bitmap; NSImage already applies EXIF, so
    # sizes must agree. If they don't, skip rather than crop blind.
    if (round(r['w']), round(r['h'])) != (iw, ih):
        report.append((src, 'SIZE MISMATCH', f"vision {int(r['w'])}x{int(r['h'])} vs pil {iw}x{ih}"))
        continue

    side = f['h'] / FACE_FRAC
    side = min(side, iw, ih)                  # can't crop bigger than the source
    left = f['eyeX'] - side / 2
    top  = f['eyeY'] - side * EYE_FRAC
    left = max(0, min(left, iw - side))       # slide back inside the frame
    top  = max(0, min(top,  ih - side))

    crop = im.crop((round(left), round(top), round(left + side), round(top + side)))
    # Never upscale: a 42px face blown up to 800px is worse than a small sharp one.
    out_side = min(SIDE, round(side))
    crop = crop.resize((out_side, out_side), Image.LANCZOS)
    # keep the exact filename, extension included -- member front matter points at it
    out = os.path.join(outdir, src)
    crop.save(out, 'JPEG', quality=88, optimize=True, progressive=True)

    if out_side < 350:
        status = 'LOW-RES'
    elif out_side < SIDE:
        status = 'soft'
    else:
        status = 'ok'
    report.append((src, status, f"{out_side}px square from a {iw}x{ih} source"))

for name, status, detail in sorted(report):
    if status in ('LOW-RES', 'SIZE MISMATCH'):
        print(f"  {status:14s} {name:40s} {detail}")
print(f"\nwrote {len([r for r in report if r[1] != 'SIZE MISMATCH'])} crops to {outdir}")
