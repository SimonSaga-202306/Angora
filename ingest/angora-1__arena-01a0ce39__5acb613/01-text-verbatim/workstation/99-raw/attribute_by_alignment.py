#!/usr/bin/env python3
"""Per-line speaker attribution for the WeChat screenshots using BUBBLE ALIGNMENT.

Why this exists
---------------
Plain OCR throws away geometry.  A WeChat timestamp block can then contain
several turns, and a single speaker has to be assigned to the whole block ->
our own words get attributed to the counterparty (real example: the
"Security project... Dahua is just too strong" line).

In a 1:1 WeChat conversation the two parties are separated horizontally:
one party's bubbles hug the LEFT edge, the other's hug the RIGHT edge.
RapidOCR gives us bounding boxes, so we can recover that.

Method
------
1. Read every line with its horizontal centre `xc` and the image width.
2. Split lines into a left cluster and a right cluster (Otsu-like threshold on
   xc, with a dead-zone in the middle left unassigned).
3. Decide which cluster is Simon by using EXPLICIT address markers:
       "Hi Simon"  / "Thanks Simon"  -> spoken BY Levent
       "Hi Levent" / "Hi, Levent"    -> spoken BY Simon
   Whichever cluster contains more "Hi Levent"-type markers is Simon.
4. Emit a per-line speaker for every OCR line, and rebuild the conversation
   with per-line attribution.

Run: python3 workstation/99-raw/attribute_by_alignment.py
"""
import os, re, json, glob, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
ALIGN = os.path.join(ROOT, "workstation", "99-raw", "wechat-ocr-aligned")
MERGED = os.path.join(ROOT, "workstation", "01-knowledge-base", "wechat-conversation.json")
OUT_MD = os.path.join(ROOT, "workstation", "01-knowledge-base", "wechat-conversation-aligned.md")
OUT_JSON = os.path.join(ROOT, "workstation", "01-knowledge-base", "wechat-conversation-aligned.json")

# markers:  phrase -> who is SPEAKING
SAID_BY_SIMON = re.compile(r"(?:hi|hello|hey|thanks|thank you|thx|dear)\s*,?\s*levent", re.I)
SAID_BY_LEVENT = re.compile(r"(?:hi|hello|hey|thanks|thank you|thx|dear)\s*,?\s*simon", re.I)

TS_FULL = re.compile(r"^\s*(20\d{2})-(\d{1,2})-(\d{1,2})\s+(\d{1,2}):(\d{2})\s*$")
TS_SLASH = re.compile(r"^\s*(\d{1,2})/(\d{1,2})(?:\s+(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)[a-z]*)?\s+(\d{1,2}):(\d{2})\s*$", re.I)
TS_DASH = re.compile(r"^\s*(\d{1,2})-(\d{1,2})\s+(\d{1,2}):(\d{2})\s*$")


def is_ts(s):
    return bool(TS_FULL.match(s) or TS_SLASH.match(s) or TS_DASH.match(s))


def ts_norm(s):
    s = s.strip()
    m = TS_FULL.match(s)
    if m:
        return "%04d-%02d-%02d %02d:%s" % (int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), m.group(5))
    m = TS_SLASH.match(s)
    if m:
        return "2026-%02d-%02d %02d:%s" % (int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4))
    m = TS_DASH.match(s)
    if m:
        return "2026-%02d-%02d %02d:%s" % (int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4))
    return None


def otsu_split(values):
    """1-D two-class threshold; returns threshold or None"""
    if len(values) < 8:
        return None
    lo, hi = min(values), max(values)
    if hi - lo < 40:
        return None
    best, best_t = -1, None
    for i in range(1, 40):
        t = lo + (hi - lo) * i / 40.0
        a = [v for v in values if v <= t]
        b = [v for v in values if v > t]
        if len(a) < 5 or len(b) < 5:
            continue
        ma, mb = statistics.mean(a), statistics.mean(b)
        va, vb = statistics.pvariance(a) or 1e-9, statistics.pvariance(b) or 1e-9
        score = (ma - mb) ** 2 / (va + vb)
        if score > best:
            best, best_t = score, t
    return best_t


def main():
    files = sorted(glob.glob(os.path.join(ALIGN, "*.jsonl")))
    if not files:
        print("no aligned OCR found")
        return 9
    print(f"aligned files: {len(files)}")
    per_image = {}
    for fp in files:
        name = os.path.basename(fp)[:-6]
        lines = [json.loads(l) for l in open(fp, encoding="utf-8") if l.strip()]
        if not lines:
            continue
        # content lines only (skip timestamps / system when clustering)
        body = [l for l in lines if not is_ts(l["text"])]
        xs = [l["xc"] for l in body]
        t = otsu_split(xs)
        if t is None:
            print(f"  ⚠️ {name}: no clean left/right split (xc spread {max(xs)-min(xs):.0f}px) - skipped")
            continue
        left = [l for l in body if l["xc"] <= t]
        right = [l for l in body if l["xc"] > t]
        s_left = sum(1 for l in left if SAID_BY_SIMON.search(l["text"]))
        l_left = sum(1 for l in left if SAID_BY_LEVENT.search(l["text"]))
        s_right = sum(1 for l in right if SAID_BY_SIMON.search(l["text"]))
        l_right = sum(1 for l in right if SAID_BY_LEVENT.search(l["text"]))
        # score each side for "is Simon"
        simon_left = s_left - l_left
        simon_right = s_right - l_right
        left_is_simon = simon_left >= simon_right
        per_image[name] = {
            "threshold": round(t, 1),
            "left_is_simon": left_is_simon,
            "n_left": len(left), "n_right": len(right),
            "evidence": {"simon_markers_left": s_left, "levent_markers_left": l_left,
                         "simon_markers_right": s_right, "levent_markers_right": l_right},
        }
        print(f"  ✅ {name}: thr={t:.0f} L={len(left)} R={len(right)} "
              f"left={'Simon' if left_is_simon else 'Levent'} "
              f"(evidence L:+{simon_left} R:+{simon_right})")
    json.dump(per_image, open(os.path.join(ALIGN, "_alignment.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    # ---- rebuild the conversation with per-line speakers -------------------
    merged = json.load(open(MERGED, encoding="utf-8"))
    stats = {"lines": 0, "attributed": 0, "ambiguous": 0}
    for fp in files:
        name = os.path.basename(fp)[:-6]
        cfg = per_image.get(name)
        lines = [json.loads(l) for l in open(fp, encoding="utf-8") if l.strip()]
        for l in lines:
            stats["lines"] += 1
            if cfg is None or is_ts(l["text"]):
                l["speaker"] = None
                continue
            side_simon = (l["xc"] <= cfg["threshold"]) == cfg["left_is_simon"]
            if cfg["evidence"]["simon_markers_left"] == 0 and cfg["evidence"]["levent_markers_left"] == 0 \
               and cfg["evidence"]["simon_markers_right"] == 0 and cfg["evidence"]["levent_markers_right"] == 0:
                l["speaker"] = None
                stats["ambiguous"] += 1
                continue
            l["speaker"] = "Simon" if side_simon else "Levent"
            stats["attributed"] += 1
        with open(fp, "w", encoding="utf-8") as f:
            for l in lines:
                f.write(json.dumps(l, ensure_ascii=False) + "\n")
    print(f"\nlines={stats['lines']} attributed={stats['attributed']} ambiguous={stats['ambiguous']}")
    print("wrote", os.path.relpath(os.path.join(ALIGN, "_alignment.json"), ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
