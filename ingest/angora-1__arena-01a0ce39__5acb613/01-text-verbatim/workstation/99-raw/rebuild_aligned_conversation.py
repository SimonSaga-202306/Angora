#!/usr/bin/env python3
"""Rebuild the WeChat conversation with PER-LINE speaker attribution derived
from bubble alignment (see attribute_by_alignment.py).

For each screenshot we walk the OCR lines top-to-bottom, remember the current
timestamp, and group consecutive lines belonging to the same speaker into a
turn.  Consecutive turns that share a timestamp keep that timestamp, so a
single WeChat minute can now contain several correctly attributed turns.

Outputs:
  workstation/01-knowledge-base/wechat-conversation-aligned.md
  workstation/01-knowledge-base/wechat-conversation-aligned.json
Run: python3 workstation/99-raw/rebuild_aligned_conversation.py
"""
import os, re, json, glob
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
ALIGN = os.path.join(ROOT, "workstation", "99-raw", "wechat-ocr-aligned")
OUT_DIR = os.path.join(ROOT, "workstation", "01-knowledge-base")

TS_FULL = re.compile(r"^\s*(20\d{2})-(\d{1,2})-(\d{1,2})\s+(\d{1,2}):(\d{2})\s*$")
# NOTE: OCR frequently drops the space(s) -> "2/26Thursday 12:29" / "2/6Friday14:24".
# Whitespace around the weekday and before the time must therefore be optional,
# otherwise those whole blocks are silently discarded.
# NOTE: OCR mangles the weekday badly -- "Friday" -> "Hriday", "Thursday" -> "Thursday",
# sometimes with the space missing entirely ("2/26Thursday 12:29", "2/6Friday14:24").
# A literal weekday whitelist therefore drops the whole block.  Accept any alphabetic
# run (including none) and rely on the date/time numbers, which OCR reads reliably.
TS_SLASH = re.compile(r"^\s*(\d{1,2})/(\d{1,2})\s*[A-Za-z]*\s*(\d{1,2}):(\d{2})\s*$", re.I)
TS_DASH = re.compile(r"^\s*(\d{1,2})-(\d{1,2})\s*[A-Za-z]*\s*(\d{1,2}):(\d{2})\s*$", re.I)
SYS = re.compile(r"(You have added .* as your Weixin contact|joined the group|"
                 r"撤回了一条消息|recalled a message|以下为新消息|Below are new messages)", re.I)
NOISE = re.compile(r"^(微信电脑版|PDF| DOCX?| XLSX?| RAR| ZIP|微信电脑版)$", re.I)


def ts_norm(s):
    s = s.strip()
    m = TS_FULL.match(s)
    if m:
        return "%04d-%02d-%02d %02d:%s" % (int(m.group(1)), int(m.group(2)),
                                           int(m.group(3)), int(m.group(4)), m.group(5))
    m = TS_SLASH.match(s)
    if m:
        return "2026-%02d-%02d %02d:%s" % (int(m.group(1)), int(m.group(2)),
                                           int(m.group(3)), m.group(4))
    m = TS_DASH.match(s)
    if m:
        return "2026-%02d-%02d %02d:%s" % (int(m.group(1)), int(m.group(2)),
                                           int(m.group(3)), m.group(4))
    return None


MARGIN = 220   # px: a bubble hugging a screen edge by <= this much owns that side
ADDR_LEVENT = re.compile(r"(?:hi|hello|hey|thanks|thank you|thx|dear)\s*[,.:]?\s*levent", re.I)
ADDR_SIMON  = re.compile(r"(?:hi|hello|hey|thanks|thank you|thx|dear)\s*[,.:]?\s*simon", re.I)
ADDR_QUOTED = re.compile(r"(?:levent|simon)\s*kil", re.I)   # "Levent KILIC: ..." = forward-quote header


def main():
    files = sorted(glob.glob(os.path.join(ALIGN, "*.jsonl")))
    try:
        cfg = json.load(open(os.path.join(ALIGN, "_alignment.json"), encoding="utf-8"))
    except Exception:
        cfg = {"left_is_levent": True}
    turns = []
    for fp in files:
        src = os.path.basename(fp)[:-6].replace("Weixin Image_", "")
        lines = [json.loads(l) for l in open(fp, encoding="utf-8") if l.strip()]
        lines.sort(key=lambda r: (r["y"], r["x0"]))
        # derive the two bubble margins from the data itself: left bubbles hug
        # min(x0), right bubbles hug max(x1).  Short centred lines fall in between
        # and stay on the geometric (centre-based) verdict.
        xs0 = sorted(r["x0"] for r in lines)
        xs1 = sorted(r["x1"] for r in lines)
        LEFT_HUG  = xs0[int(len(xs0) * 0.03)]
        RIGHT_HUG = xs1[int(len(xs1) * 0.97)]
        cur_ts, cur_spk, buf, buf_y = None, None, [], None
        for r in lines:
            txt = r["text"].strip()
            ts = ts_norm(txt)
            if ts:
                if buf and cur_spk:
                    turns.append(_mk(cur_ts, cur_spk, buf, src))
                cur_ts, buf, cur_spk = ts, [], None
                continue
            if not txt or NOISE.match(txt):
                continue
            spk = r.get("speaker")
            if ADDR_QUOTED.search(txt):
                spk = cur_spk if cur_spk else spk   # forwarded-quote header, not a real turn
            # --- hybrid: margin-hugging beats centre-of-mass for short lines --
            levent_side = cfg.get("left_is_levent", True)
            hugs_left  = r["x0"] <= LEFT_HUG + MARGIN
            hugs_right = r["x1"] >= RIGHT_HUG - MARGIN
            if hugs_left and not hugs_right:
                spk = "Levent" if levent_side else "Simon"
            elif hugs_right and not hugs_left:
                spk = "Simon" if levent_side else "Levent"
            # explicit address marker wins over geometry
            if ADDR_LEVENT.search(txt) and not ADDR_SIMON.search(txt):
                spk = "Simon"
            elif ADDR_SIMON.search(txt) and not ADDR_LEVENT.search(txt):
                spk = "Levent"
            if SYS.search(txt):
                spk = "System"
            if spk is None:
                # timestamp-only or unassigned line: keep the running turn
                spk = cur_spk if cur_spk else "?"
            if spk != cur_spk and buf:
                turns.append(_mk(cur_ts, cur_spk, buf, src))
                buf = []
            cur_spk = spk
            buf.append(txt)
        if buf and cur_spk:
            turns.append(_mk(cur_ts, cur_spk, buf, src))

    # drop chat-header artefacts (window controls / contact name banner)
    HEADER = re.compile(r"^[X×]|^Levent KILI[ÇC]$", re.I)
    turns = [t for t in turns if not HEADER.match(t["text"].strip()) or len(t["text"].strip()) > 12]
    turns = [t for t in turns if t["datetime"]]

    turns.sort(key=lambda t: t["datetime"])
    # dedupe identical (ts, speaker, text)
    seen, out = set(), []
    for t in turns:
        k = (t["datetime"], t["speaker"], t["text"][:160])
        if k in seen:
            continue
        seen.add(k)
        out.append(t)

    md = ["# 微信对话全录 · 逐行说话人归因版（气泡对齐法）", "",
          "> 来源：`WeChat Talk/` 26 张长截图；OCR 保留行级坐标后按**气泡左右对齐**判定说话人",
          "> **判定依据**：左栏（行中心 xc ≈ 200–800）= **Levent**；右栏（xc ≈ 900–1400）= **Simon（我方）**。",
          "> 26 张截图判定结果**完全一致**（左=Levent / 右=Simon），并以称呼证据（Hi Simon / Hi Levent）交叉投票确认。",
          "",
          f"> 共 **{len(out)}** 个对话轮次，范围 {out[0]['datetime']} → {out[-1]['datetime']}",
          f"> 说话人分布：{dict(Counter(t['speaker'] for t in out))}",
          "",
          "> ✅ 相较旧版 `wechat-conversation.md`（整块单一说话人），本版可正确处理",
          "> **一个时间戳内含多轮**的情况，避免把我方的话误归到对方名下。", "", "---", ""]
    last_date = None
    for t in out:
        if t["date"] != last_date:
            md += [f"\n## 📅 {t['date']}\n"]
            last_date = t["date"]
        md += [f"**[{t['time']}] {t['speaker']}：** {t['text']}", ""]
    open(os.path.join(OUT_DIR, "wechat-conversation-aligned.md"), "w", encoding="utf-8").write("\n".join(md))
    json.dump(out, open(os.path.join(OUT_DIR, "wechat-conversation-aligned.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print("turns:", len(out))
    print("by speaker:", dict(Counter(t["speaker"] for t in out)))
    print("by year:", dict(Counter(t["date"][:4] for t in out)))
    print("range:", out[0]["datetime"], "->", out[-1]["datetime"])


def _mk(ts, spk, buf, src):
    text = "\n".join(l for l in buf if l).strip()
    return {"datetime": ts or "", "date": (ts or "")[:10], "time": (ts or "")[11:],
            "speaker": spk, "text": text, "source_screenshot": src}


if __name__ == "__main__":
    main()
