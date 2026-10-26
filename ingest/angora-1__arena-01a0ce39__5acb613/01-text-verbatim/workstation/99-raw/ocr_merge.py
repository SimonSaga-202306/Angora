#!/usr/bin/env python3
"""Merge OCR'd WeChat screenshots -> chronological .md + .json.

Timestamp rules (per user):
  * "YYYY-M-D HH:MM" -> that year (2024 / 2025)
  * "M-D HH:MM"      -> 2026 (WeChat hides the year for the current year)
Run: python3 workstation/99-raw/ocr_merge.py
"""
import os, re, json, glob, unicodedata
from datetime import date
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OCR_DIR = os.path.join(ROOT, "workstation", "99-raw", "wechat-ocr")
OUT_DIR = os.path.join(ROOT, "workstation", "01-knowledge-base")
os.makedirs(OUT_DIR, exist_ok=True)

TS_FULL  = re.compile(r"^(20\d{2})-(\d{1,2})-(\d{1,2})\s+(\d{1,2}):(\d{2})$")
TS_SHORT = re.compile(r"^(\d{1,2})-(\d{1,2})\s+(\d{1,2}):(\d{2})$")
# WeChat English UI renders current-year stamps as "M/D Weekday HH:MM" (e.g. "4/16 Thursday 11:34")
TS_SLASH = re.compile(r"^(\d{1,2})/(\d{1,2})(?:\s+(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)[a-z]*)?\s+(\d{1,2}):(\d{2})$",
                      re.I)
TS_DATE  = re.compile(r"^(20\d{2})-(\d{1,2})-(\d{1,2})$")
TS_SDATE = re.compile(r"^(\d{1,2})/(\d{1,2})(?:\s+(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)[a-z]*)?$", re.I)
WD = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday",
      4: "Friday", 5: "Saturday", 6: "Sunday"}
SYS = re.compile(r"(You have added .* as your Weixin contact|joined the group|"
                 r"撤回了一条消息|recalled a message|以下为新消息|Below are new messages)", re.I)
LEVENT_MARK = re.compile(r"(^|\W)(Hi Simon|Hi, Simon|Thanks Simon|Thank you Simon|Simon,)", re.I)
SIMON_MARK  = re.compile(r"(^|\W)(Hi,? Levent|Hi Levent|Levent,|Thanks,? Levent)", re.I)


def norm(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", s).strip())


def base_speaker(t):
    if SYS.search(t): return "System"
    if re.search(r"\bTaylan\b", t, re.I): return "Taylan"
    a, b = LEVENT_MARK.search(t), SIMON_MARK.search(t)
    if a and b: return "Levent" if a.start() < b.start() else "Simon"
    if a: return "Levent"
    if b: return "Simon"
    return None


def attribute(entries):
    last = None
    for e in entries:
        s = base_speaker(e["text"])
        if s in ("System", "Taylan"):
            e["speaker"], e["attribution"] = s, "explicit"
            continue
        if s:
            last = s
            e["speaker"], e["attribution"] = s, "explicit"
        elif last:
            e["speaker"], e["attribution"] = last + "?", "inferred"
        else:
            e["speaker"], e["attribution"] = "?", "unknown"


# ---------------------------------------------------------------------------
# Multi-turn splitting.  One WeChat timestamp block frequently contains SEVERAL
# turns by alternating speakers (e.g. a "Hi Levent" reply inside the same
# minute).  Assigning a single speaker to the whole block mis-attributes lines,
# which matters a lot when quoting somebody.  We therefore split each entry
# into sub-turns at every explicit address marker found on its own line.
# ---------------------------------------------------------------------------
TURN_MARK = re.compile(r"^\s*(?:Hi|Hi,|Hello|Thanks|Thank you|Thx|Hey|Yes|No|Ok)[^\n]{0,40}?"
                       r"\b(Simon|Levent)\b", re.I)
NAME_ONLY = re.compile(r"^\s*(Levent KILI[ÇC]|Levent|Simon)\s*:?\s*$", re.I)


def split_turns(text, block_speaker):
    """-> list of (speaker, lines[]) sub-turns"""
    lines = text.split("\n")
    turns, cur = [], None
    for ln in lines:
        m = TURN_MARK.match(ln)
        name = None
        if m:
            name = "Simon" if m.group(1).lower() == "simon" else "Levent"
        else:
            m2 = NAME_ONLY.match(ln)
            if m2:
                n = m2.group(1).lower()
                name = "Levent" if n.startswith("levent") else "Simon"
        if name:
            # start a new turn attributed to the ADDRESSEE's counterpart:
            # "Hi Levent" is said BY Simon, "Hi Simon" is said BY Levent.
            if re.search(r"\bLevent\b", ln, re.I):
                spk = "Simon"
            else:
                spk = "Levent"
            cur = [spk, []]
            turns.append(cur)
            cur[1].append(ln)
        else:
            if cur is None:
                cur = [block_speaker.rstrip("?"), []]
                turns.append(cur)
            cur[1].append(ln)
    out = [(s, "\n".join(l for l in ls if l).strip()) for s, ls in turns]
    return [(s, t) for s, t in out if t]


files = sorted(glob.glob(os.path.join(OCR_DIR, "*.txt")))
entries = []
for fp in files:
    src = os.path.basename(fp)[:-4]
    cur = None
    for line in open(fp, encoding="utf-8").read().split("\n"):
        if line.startswith("#"):
            continue
        s = norm(line)
        if not s:
            continue
        m = TS_FULL.match(s) or TS_SHORT.match(s) or TS_SLASH.match(s)
        if m:
            g = m.groups()
            if TS_FULL.match(s):
                y, mo, d, hh, mm = int(g[0]), int(g[1]), int(g[2]), int(g[3]), g[4]
            else:                      # both short forms mean the current year (2026)
                y, mo, d, hh, mm = 2026, int(g[0]), int(g[1]), int(g[2]), g[3]
            # weekday cross-check: only possible when the stamp carried a weekday name
            wm = re.search(r"(Mon|Tue|Wed|Thu|Fri|Sat|Sun)[a-z]*", s, re.I)
            if wm and (mo, d) != (0, 0):
                try:
                    exp = WD[date(y, mo, d).weekday()]
                    if exp[:3].lower() != wm.group(1)[:3].lower():
                        print(f"  !! weekday mismatch {s!r}: {y}-{mo}-{d} is a {exp}")
                except ValueError:
                    print(f"  !! bad date {s!r} -> {y}-{mo}-{d}")
            ts = f"{y}-{mo:02d}-{d:02d} {hh:02d}:{mm}"
            if cur: entries.append(cur)
            cur = {"datetime": ts, "date": ts.split()[0], "time": ts.split()[1],
                   "lines": [], "source": src}
            continue
        if TS_DATE.match(s) or TS_SDATE.match(s):
            continue
        if cur is not None:
            cur["lines"].append(s)
    if cur: entries.append(cur)

merged, seen = [], set()
for e in entries:
    txt = "\n".join(l for l in e["lines"] if l).strip()
    if not txt:
        continue
    key = (e["datetime"], txt[:160])
    if key in seen:
        continue
    seen.add(key)
    merged.append({"datetime": e["datetime"], "date": e["date"], "time": e["time"],
                   "speaker": "?", "text": txt, "source_screenshot": e["source"]})

    merged.sort(key=lambda x: x["datetime"])
attribute(merged)

# split multi-turn blocks; a block that yields >1 turn is flagged
multi = 0
for e in merged:
    turns = split_turns(e["text"], e["speaker"])
    e["turns"] = [{"speaker": s, "text": t} for s, t in turns]
    e["multi_turn"] = len(turns) > 1
    if e["multi_turn"]:
        multi += 1
print(f"multi-turn blocks split: {multi} / {len(merged)}")

md = ["# 微信对话全记录：Simon（Saga） ↔ Levent KILIÇ（Angora Networks）", "",
      "> 来源：`WeChat Talk/` 长截图，经 OCR 提取并按时间排序",
      "> **年份规则**：带年份的时间戳（如 `2024-5-2 16:36`）按标注年份；"
      "**只有月日的时间戳（如 `4/16 Thursday 11:34`）为 2026 年**（微信对当年隐藏年份，已用星期名交叉验证）",
      f"> 已处理截图 {len(files)} / 25　共 {len(merged)} 条消息", "",
      "> ⚠️ 说话人为基于称呼的**启发式推断**：`Simon`/`Levent` = 有明确称呼证据，"
      "带 `?` = 依上下文推断，请以截图原文为准。", "", "---", ""]
last_date = None
for e in merged:
    if e["date"] != last_date:
        md += [f"\n## 📅 {e['date']}\n"]
        last_date = e["date"]
    if e.get("multi_turn"):
        md += [f"**[{e['time']}]** _(本时间戳块含多轮，已拆分)_", ""]
        for t in e["turns"]:
            md += [f"- **{t['speaker']}：** {t['text']}", ""]
    else:
        md += [f"**[{e['time']}] {e['speaker']}：** {e['text']}", ""]

open(os.path.join(OUT_DIR, "wechat-conversation.md"), "w", encoding="utf-8").write("\n".join(md))
json.dump(merged, open(os.path.join(OUT_DIR, "wechat-conversation.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)

print("OCR files:", len(files))
print("entries:", len(merged))
print("by year:", dict(Counter(e["date"][:4] for e in merged)))
print("by speaker:", dict(Counter(e["speaker"] for e in merged)))
if merged:
    print("range:", merged[0]["datetime"], "->", merged[-1]["datetime"])
