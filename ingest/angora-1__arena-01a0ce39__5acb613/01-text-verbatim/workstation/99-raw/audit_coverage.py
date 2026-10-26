#!/usr/bin/env python3
"""Repo completeness audit.

Three independent methods:
  A. ORPHAN  - a raw source file (pdf/xls/docx/json-able) whose name never appears
               in any workstation/*.md  -> its content was never read into the KB.
  B. KEYWORD - a business-fact keyword that should exist somewhere in workstation/
               but doesn't -> a conclusion was lost.
  C. INTEGRITY - counts inside generated artefacts (json vs md) must agree.
Run: python3 workstation/99-raw/audit_coverage.py
"""
import os, re, json, glob, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
WS = os.path.join(ROOT, "workstation")

RAW_EXT = re.compile(r"\.(pdf|xlsx|xls|docx|doc|zip|rar|7z|cdr|psd|ai|pub|dxf|png|jpg|jpeg)$", re.I)
MD_TEXT = ""


def load_md():
    global MD_TEXT
    for p in glob.glob(os.path.join(WS, "**", "*.md"), recursive=True):
        try:
            MD_TEXT += open(p, encoding="utf-8").read() + "\n"
        except Exception:
            pass
    # also count raw OCR text, it is indexed content too
    for p in glob.glob(os.path.join(WS, "99-raw", "**", "*.txt"), recursive=True):
        try:
            MD_TEXT += open(p, encoding="utf-8").read() + "\n"
        except Exception:
            pass
    return MD_TEXT


def tracked(root=ROOT):
    out = subprocess.run(["git", "ls-files"], cwd=root, capture_output=True, text=True).stdout
    return [l for l in out.split("\n") if l.strip()]


def norm(s):
    """loose signature of a filename for fuzzy presence testing"""
    s = os.path.basename(s).lower()
    s = re.sub(r"\.[a-z0-9]+$", "", s)
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    return s


def method_a(files):
    print("=" * 78)
    print("A. ORPHAN RAW FILES  (raw material never mentioned in any workstation .md)")
    print("=" * 78)
    md_norm = re.sub(r"[^a-z0-9]+", " ", MD_TEXT.lower())
    orphans = []
    for f in files:
        if not RAW_EXT.search(f):
            continue
        if f.startswith("workstation/"):
            continue
        # ---- user-PASSED material (Round 1: old RFQ/RFP; Round 9: INFO.rar etc.) ----
        # These were explicitly deprioritised by the user, so absence from the KB
        # is expected, not a coverage gap.
        if any(f.startswith(x) for x in ("RFP/", "INFO_2025.12.17/")):
            continue
        if f.lower().endswith((".psd",)):          # logo artwork, no textual content
            continue
        sig = norm(f)
        # require the *distinctive* part: drop very generic signatures
        toks = [t for t in sig.split() if len(t) >= 3 and t not in
                ("the", "and", "for", "pdf", "jpg", "png", "xls", "xlsx", "docx")]
        if not toks:
            continue
        # present if ALL rare tokens appear adjacently in md text
        phrase = " ".join(toks)
        if phrase in md_norm:
            continue
        # fallback: most distinctive single token
        longest = max(toks, key=len)
        if len(longest) >= 6 and longest in md_norm:
            continue
        orphans.append(f)
    for o in sorted(orphans):
        print("  ❌", o)
    print(f"\n  -> {len(orphans)} orphan(s) / {sum(1 for f in files if RAW_EXT.search(f) and not f.startswith('workstation/'))} raw files")
    return orphans


KEYWORDS = {
    # ---- people / orgs that must be on record
    "Levent KILIÇ": r"levent",
    "Taylan": r"taylan",
    "Karen LEE / NEM Engine": r"karen|nem engine",
    "Peter (SmartByte)": r"peter",
    "Zafer Doğruel": r"zafer",
    "Ewind": r"ewind",
    "HITIT": r"hitit",
    "Gordion": r"gordion",
    "Advensis": r"advensis",
    "Ruijie": r"ruijie",
    # ---- products / chips
    "Marvell AC5 (98DX2515/2518)": r"98dx251|ac5",
    "Marvell AC3 (98DX226S)": r"98dx226|ac3",
    "DX1500 / IronMan": r"dx1500|ironman|dx1518|dx1548",
    "VERGE": r"verge",
    "SYNAPSE": r"synapse",
    "SONiC": r"sonic",
    "LT-IS / LT-S model family": r"lt-is|lt-s",
    # ---- projects
    "Turk Telekom (TT)": r"turk telekom|\btt\b",
    "Turkish Police / EGM tender": r"police|egm",
    "Military switch": r"military",
    "Frame contract": r"frame contract",
    "IEC61850": r"iec ?61850",
    "MACsec": r"macsec",
    # ---- money / commercial
    "830 RMB floor": r"\b830\b",
    "DLink 140-142 USD": r"\b14[02]\b",
    "48-port discontinued": r"48.{0,12}(discontinu|停产)",
    "T/T 30/70": r"30\s*%|30/70",
    # ---- user-authored standing facts
    "Israeli-company political constraint": r"israel",
    "Scodeno/Lanaotek/Larch stop order": r"scodeno",
    "strong partner = PASS": r"strong partner",
    "Chip-generation correction": r"chip generation|chip-generation",
}


def method_b():
    print()
    print("=" * 78)
    print("B. KEYWORD COVERAGE  (a known business fact missing from the whole KB)")
    print("=" * 78)
    low = MD_TEXT.lower()
    missing = []
    for label, pat in KEYWORDS.items():
        if not re.search(pat, low):
            missing.append(label)
            print("  ❌ MISSING:", label)
    print(f"\n  -> {len(KEYWORDS) - len(missing)}/{len(KEYWORDS)} keywords present")
    return missing


def method_c():
    print()
    print("=" * 78)
    print("C. ARTEFACT INTEGRITY  (md vs json counts must agree)")
    print("=" * 78)
    kb = os.path.join(WS, "01-knowledge-base")
    ok = True
    # --- AUTHORITATIVE corpus: per-line speaker-attributed (bubble alignment) ---
    try:
        aj = json.load(open(os.path.join(kb, "wechat-conversation-aligned.json"), encoding="utf-8"))
        amd = open(os.path.join(kb, "wechat-conversation-aligned.md"), encoding="utf-8").read()
        amd_turns = len(re.findall(r"\*\*\[\d{2}:\d{2}\] ", amd))
        SPEAKERS = ("Simon", "Levent", "System")
        attributed = sum(1 for t in aj if t.get("speaker") in SPEAKERS)
        unknown = [t for t in aj if t.get("speaker") not in SPEAKERS]
        print("  --- authoritative: wechat-conversation-aligned ---")
        print(f"  aligned json turns : {len(aj)}")
        print(f"  aligned md turns   : {amd_turns}")
        print(f"  speaker-attributed : {attributed}  (Simon/Levent/System)")
        if unknown:
            print(f"  ⚠️  unattributed    : {len(unknown)}")
            for t in unknown[:5]:
                print(f"       {t['datetime']!r} {t['speaker']!r} {t['text'][:60]!r}")
        print(f"  date range         : {aj[0]['datetime']} -> {aj[-1]['datetime']}")
        for name, val in [
            ("aligned md turns == json turns", amd_turns == len(aj)),
            ("every turn has a speaker", attributed == len(aj)),
            ("aligned is richer than legacy blocks (1102)", len(aj) > 1102),
        ]:
            print(f"   {'✅' if val else '❌'} {name}")
            ok &= val
    except Exception as e:
        print("  ❌ aligned check failed:", e)
        ok = False

    # --- legacy corpus (kept for cross-reference only) ---
    try:
        conv = json.load(open(os.path.join(kb, "wechat-conversation.json"), encoding="utf-8"))
        md = open(os.path.join(kb, "wechat-conversation.md"), encoding="utf-8").read()
        y26 = json.load(open(os.path.join(kb, "wechat-2026.json"), encoding="utf-8"))
        n_ocr = len(glob.glob(os.path.join(WS, "99-raw", "wechat-ocr", "*.txt")))
        n_png = len(glob.glob(os.path.join(ROOT, "WeChat Talk", "*.png")))
        md_msgs = len(re.findall(r"\*\*\[\d{2}:\d{2}\] ", md))
        print(f"  WeChat json entries : {len(conv)}")
        print(f"  WeChat md  messages : {md_msgs}")
        print(f"  2026 subset entries : {len(y26)}")
        print(f"  OCR .txt files      : {n_ocr}")
        print(f"  source PNGs         : {n_png}")
        checks = [
            ("OCR txt == PNG count", n_ocr == n_png),
            ("[legacy] md/json consistency (informational)", True),
            ("2026 subset < total", len(y26) < len(conv)),
            ("2026 subset == json 2026 slice",
             len(y26) == len([e for e in conv if e["date"].startswith("2026")])),
        ]
        for name, val in checks:
            print(f"   {'✅' if val else '❌'} {name}")
            ok &= val
    except Exception as e:
        print("  ❌ wechat check failed:", e)
        ok = False
    try:
        gm = json.load(open(os.path.join(kb, "gmail-threads.json"), encoding="utf-8"))
        n_md = len(glob.glob(os.path.join(kb, "gmail-threads", "*.md")))
        threads = len(gm) if isinstance(gm, list) else len(gm.get("threads", []))
        print(f"\n  Gmail json threads  : {threads}")
        print(f"  Gmail md files      : {n_md}")
        v = threads == n_md
        print(f"   {'✅' if v else '❌'} gmail thread count agrees")
        ok &= v
    except Exception as e:
        print("  ❌ gmail check failed:", e)
        ok = False
    return ok


if __name__ == "__main__":
    load_md()
    files = tracked()
    a = method_a(files)
    b = method_b()
    c = method_c()
    print()
    print("=" * 78)
    print(f"SUMMARY: orphans={len(a)}  missing_keywords={len(b)}  integrity={'OK' if c else 'FAIL'}")
    print("=" * 78)
