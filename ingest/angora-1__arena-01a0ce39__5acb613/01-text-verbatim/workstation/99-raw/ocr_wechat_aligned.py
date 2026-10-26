#!/usr/bin/env python3
"""WeChat long-screenshot OCR that PRESERVES line geometry.

Why: in a 1:1 WeChat chat the two parties are visually distinguished by
left/right alignment (plus avatars).  Plain text OCR throws that away, so a
single timestamp block containing several turns can only be given ONE speaker
-> lines get mis-attributed (e.g. our own words assigned to the counterparty).

This script re-runs OCR and stores, for every line, the horizontal centre of
its bounding box, so a later pass can cluster lines into left/right columns and
derive a per-line speaker.

Output: workstation/99-raw/wechat-ocr-aligned/<image>.jsonl
        one JSON object per line: {"y","x0","x1","xc","text","conf","slice"}
Resume-safe: existing files are skipped.
"""
import os, re, json, sys, glob
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(ROOT, "WeChat Talk")
OUT = os.path.join(ROOT, "workstation", "99-raw", "wechat-ocr-aligned")
os.makedirs(OUT, exist_ok=True)

SLICE_H = 1200
OVERLAP = 150
CONF = 0.5


def slices(h):
    y, out = 0, []
    while y < h:
        out.append((y, min(y + SLICE_H, h)))
        if y + SLICE_H >= h:
            break
        y += SLICE_H - OVERLAP
    return out


def main():
    try:
        from rapidocr_onnxruntime import RapidOCR
    except ImportError:
        print("RapidOCR missing", file=sys.stderr)
        return 9
    ocr = RapidOCR()
    imgs = sorted(glob.glob(os.path.join(SRC, "*.png")))
    print(f"total images: {len(imgs)}", flush=True)
    for i, p in enumerate(imgs, 1):
        name = os.path.basename(p)[:-4]
        dst = os.path.join(OUT, name + ".jsonl")
        if os.path.exists(dst):
            print(f"[{i}/{len(imgs)}] SKIP {name}", flush=True)
            continue
        im = Image.open(p)
        W, H = im.size
        recs = []
        for y0, y1 in slices(H):
            box = (0, y0, W, y1)
            res, _ = ocr(p, box=box) if _supports_box(ocr) else ocr(im.crop(box))
            for item in (res or []):
                b, txt, conf = item[0], item[1], item[2]
                if conf is None or conf < CONF:
                    continue
                xs = [pt[0] for pt in b]
                ys = [pt[1] for pt in b]
                recs.append({
                    "y": round(sum(ys) / len(ys) + y0, 1),
                    "x0": round(min(xs), 1),
                    "x1": round(max(xs), 1),
                    "xc": round(sum(xs) / len(xs), 1),
                    "text": txt.strip(),
                    "conf": round(float(conf), 3),
                    "slice": y0,
                })
        # dedupe: same text + nearly same y (overlap artefacts)
        recs.sort(key=lambda r: (r["y"], r["x0"]))
        kept, last = [], {}
        for r in recs:
            k = r["text"]
            if k in last and abs(r["y"] - last[k]) < 12:
                continue
            last[k] = r["y"]
            kept.append(r)
        with open(dst, "w", encoding="utf-8") as f:
            for r in kept:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"[{i}/{len(imgs)}] OK {name} {W}x{H} lines={len(kept)}", flush=True)
    print("ALL DONE", flush=True)
    return 0


def _supports_box(ocr):
    """RapidOCR's __call__ does not take a box kwarg; we crop manually."""
    return False


if __name__ == "__main__":
    sys.exit(main())
