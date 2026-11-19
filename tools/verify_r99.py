#!/usr/bin/env python3
"""Read-only r99 checks: selected local bytes/links/claims, not source authenticity.

No network, customer contact, archive extraction, or changes. The claimed full
reading is an execution record: this script cannot verify human reading or the
accuracy of the manual image transcription.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from hashlib import sha1, sha256
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
I = ROOT / "ingest/angora-1__arena-01a0ce39__5acb613"
W = I / "01-text-verbatim/workstation"
S = I / "22-source-evidence-r99-2026-10-26"
F = I / "23-followup-angora-r99-2026-10-26"
R = W / "08-customer-pipeline/168-angora-aftersales-project-evidence-r99-2026-10-26.md"
M = W / "09-orders/120-angora-orders-master-2026-10-21.mapping-r99.md"
A = I / "24-audit-r99-2026-10-26.md"


def require(value: bool, detail: str) -> None:
    if not value:
        raise ValueError(detail)


def csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf8", newline="") as f:
        return list(csv.DictReader(f))


def check(path: Path, size: str, digest: str) -> bytes:
    data = path.read_bytes()
    require(len(data) == int(size), f"size differs: {path}")
    require(sha256(data).hexdigest() == digest, f"SHA-256 differs: {path}")
    return data


def inventory() -> str:
    rows = csv_rows(S / "scope-inventory.csv")
    require(len(rows) == 30 and [int(x["seq"]) for x in rows] == list(range(1, 31)), "scope count/sequence")
    paths = {r["path_from_ingest_root"] for r in rows}
    require(len(paths) == 30, "duplicate representation path")
    require(sum(int(r["bytes"]) for r in rows) == 1017278, "byte total")
    require(Counter(r["representation"] for r in rows) == {
        "existing-text-layer-or-structure-extraction": 28,
        "extracted-PDF-embedded-image": 1,
        "PDF-image-extraction-note": 1,
    }, "representation kinds")
    for r in rows:
        data = check(I / r["path_from_ingest_root"], r["bytes"], r["sha256"])
        if r["representation"] == "extracted-PDF-embedded-image":
            require(data.startswith(b"\xff\xd8\xff"), "image is not JPEG")
            require(r["sha256"] == "40777dcc77156057d15d67906281b0a88cee56ee2f1109587a2830b1441c1a2f", "certificate image hash")
        else:
            data.decode("utf8")
    a = {x["representation_path"] for x in csv_rows(I / "15-source-evidence-r97-2026-10-26/local-first-second-inventory.csv")}
    b = {x["artifact_path"] for x in csv_rows(I / "18-source-evidence-r98-2026-10-26/local-order-dc-inventory.csv")}
    require((len(paths & a), len(paths & b), len(paths & a & b), len(paths - (a | b))) == (10, 18, 1, 3), "overlap counts")
    partial = csv_rows(S / "context-partial-inventory.csv")
    require(len(partial) == 21 and len({r["path_from_ingest_root"] for r in partial}) == 21, "partial inventory")
    for r in partial:
        check(I / r["path_from_ingest_root"], r["bytes"], r["sha256"])
        require("不计入30项完整阅读" in r["inspection_limit"], "partial mistakenly claimed full")
    return "30/30 selected derivative bytes; 21 partial-source hashes; r97/r98 overlaps 10/18/1"


def source_tokens() -> str:
    ext = I / "02-extracted"
    third = ext / "3rd order 176台2光16电 L2 PoE"
    jan = (third / "采购_Smartbyte/采购合同_STSC20250117007.xls.extracted.md").read_text(encoding="utf8")
    march = (third / "郑州仨戛通讯器材有限公司 P20250303-01（未税265220RMB）.doc.extracted.md").read_text(encoding="utf8")
    for token in ("深圳凌特华盛科技有限公司", "3年质保", "不含电源", "LT-IS6318GP-2GX16GT"):
        require(token in jan, f"January source missing: {token}")
    for token in ("惠州凌特华盛科技有限公司", "工业级产品质保期【五】年", "包含电源", "178"):
        require(token in march, f"March source missing: {token}")
    chat = json.loads((W / "01-knowledge-base/wechat-conversation-aligned.json").read_text(encoding="utf8"))
    events = [
        ("2024-08-06", "Levent", "All is OKAY"),
        ("2025-02-11", "Simon", "we did rewrite the SN and MAC"),
        ("2025-11-03", "Levent", "some frames are lost"),
        ("2025-11-10", "Levent", "NMS monitoring software to collect logs"),
        ("2026-01-20", "Levent", "IEC61850 certificate"),
        ("2026-01-21", "Simon", "Sorry, it is not available"),
        ("2026-02-02", "Levent", "customer decided to go another way"),
        ("2026-07-31", "Levent", "visible in the software but not active"),
        ("2026-07-31", "Simon", "just confirmed, its already removed"),
    ]
    for date, speaker, phrase in events:
        require(any(x["date"] == date and x["speaker"] == speaker and phrase in x["text"] for x in chat),
                f"chat token missing: {date} {speaker} {phrase}")
    email = (ext / "Gmail - TT switch administration guide.pdf.extracted.md").read_text(encoding="utf8")
    require("SNMP v3" in email and "Please try and let me know" in email, "email support sequence")
    manual = next(S.glob("transcriptions/**/page-01-img-01.jpg.transcription.md")).read_text(encoding="utf8")
    for token in ("22nd, Nov, 2024-22nd, Nov, 2025", "22nd, Nov, 2024-22nd, Nov, 2027", "10 pieces only, 3 boxes only"):
        require(token in manual, f"manual transcription missing: {token}")
    require(5 + 2 + 1 + 2 == 10, "certificate box count")
    return "selected derivative text/JSON event tokens and certificate box arithmetic (not factual authentication)"


def protected_variant() -> str:
    p = I / "21-protected-variants-r99-2026-10-26/original-paths/ingest/angora-1__arena-01a0ce39__5acb613/01-text-verbatim/workstation/01-knowledge-base/pdfs/info-rar-inventory.md"
    b = check(p, "1792", "311455043a55862366607d638934bded2b15db92dd2dc1b35bbda49f027f5471")
    require(sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest() == "c35c3d0507677e1704d8b091a22094ad7ba04727", "protected blob")
    return "r99 pre-fast-forward variant matches size, SHA-256 and Git blob"


def links() -> str:
    transcriptions = list(S.glob("transcriptions/**/*.md"))
    require(len(transcriptions) == 1, "expected one image transcription")
    docs = [R, M, S / "README.md", *transcriptions, F / "README.md", F / "angora-networks.md", A,
            I / "21-protected-variants-r99-2026-10-26/README.md"]
    require({p.name for p in F.glob("*.md")} == {"README.md", "angora-networks.md"}, "follow-up scope")
    pattern = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
    bad = []
    count = 0
    for doc in docs:
        for ref in pattern.findall(doc.read_text(encoding="utf8")):
            parsed = urlsplit(ref)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            count += 1
            if not (doc.parent / unquote(parsed.path)).exists():
                bad.append(f"{doc.relative_to(ROOT)} -> {ref}")
    require(not bad, "missing links:\n" + "\n".join(bad))
    return f"{count} local links exist across r99 deliverables"


def main() -> int:
    try:
        for name, fn in (("Inventory", inventory), ("Source", source_tokens),
                         ("Protected variant", protected_variant), ("Links", links)):
            print(f"PASS {name}: {fn()}")
        print("Scope: local derived bytes and selected strings only; no proof of original files, transcript accuracy, signing, delivery, repair or current status.")
        return 0
    except (OSError, ValueError, KeyError, StopIteration, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
