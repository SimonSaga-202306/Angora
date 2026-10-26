#!/usr/bin/env python3
"""OCR the WeChat Talk long screenshots -> per-image .txt.
Skips images whose .txt already exists (resumable).
Run:  python3 workstation/99-raw/ocr_wechat.py
"""
import os, time, glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, "WeChat Talk")
OUT = os.path.join(ROOT, "workstation", "99-raw", "wechat-ocr")
os.makedirs(OUT, exist_ok=True)

from PIL import Image
from rapidocr_onnxruntime import RapidOCR

Image.MAX_IMAGE_PIXELS = None
ocr = RapidOCR()

CH, OV = 1200, 150  # slice height, overlap

files = sorted(glob.glob(os.path.join(SRC, "*.png")), key=os.path.getsize)
print(f"total images: {len(files)}", flush=True)

for idx, src in enumerate(files, 1):
    base = os.path.basename(src).replace("Weixin Image_", "").replace(".png", "")
    dst = os.path.join(OUT, base + ".txt")
    if os.path.exists(dst) and os.path.getsize(dst) > 200:
        print(f"[{idx}/{len(files)}] SKIP {base}", flush=True)
        continue
    t0 = time.time()
    try:
        im = Image.open(src).convert("RGB")
    except Exception as e:
        print(f"[{idx}/{len(files)}] ERR {base}: {e}", flush=True)
        continue
    W, H = im.size
    raw, y, sl = [], 0, 0
    while y < H:
        part = im.crop((0, y, W, min(y + CH, H)))
        p = "/tmp/wc_sl.png"
        part.save(p)
        try:
            res, _ = ocr(p)
        except Exception:
            res = None
        if res:
            for r in res:
                txt, score = r[1], r[2]
                if txt and score and score > 0.5 and txt.strip():
                    raw.append(txt.strip())
        y += CH - OV
        sl += 1
    uniq, prev = [], None
    for l in raw:
        if l != prev:
            uniq.append(l)
        prev = l
    with open(dst, "w", encoding="utf-8") as f:
        f.write(f"# SOURCE: {os.path.basename(src)}\n")
        f.write(f"# SIZE: {W}x{H}  SLICES: {sl}\n")
        f.write("#" * 60 + "\n")
        f.write("\n".join(uniq))
    print(f"[{idx}/{len(files)}] OK {base} {W}x{H} slices={sl} lines={len(uniq)} "
          f"{time.time()-t0:.1f}s", flush=True)

print("ALL DONE", flush=True)
