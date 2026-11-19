#!/usr/bin/env python3
"""Offline read-only checks for r98.

Checks the frozen local inventory and selected source strings/math/links, not
original binary files, remote response equality, independent signatures,
settlement, delivery, Incoterms applicability, product tests or authenticity.
Run: python3 tools/verify_r98.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from decimal import Decimal
from hashlib import sha256
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
I = ROOT / "ingest/angora-1__arena-01a0ce39__5acb613"
W = I / "01-text-verbatim/workstation"
S = I / "18-source-evidence-r98-2026-10-26"
F = I / "19-followup-angora-r98-2026-10-26"
R = W / "08-customer-pipeline/167-angora-orders-warranty-datacenter-r98-2026-10-26.md"
M = W / "09-orders/120-angora-orders-master-2026-10-21.mapping-r98.md"
A = I / "20-audit-r98-2026-10-26.md"
PREFIXES = ("3rd order ", "4th order ", "5th order ", "6th order ", "INFO_2025.12.17/")
EXTRA = {
    "Agenda for WeChat meeting at 2024.10.31.docx",
    "Agenda for WeChat meeting at 2025.docx",
    "Key Points in WeChat meeting at 2024.10.31.docx",
    "Reply on SAGA Enterprise L3 Recommendation Report.docx",
    "SAGA Enterprise L3 Recommendation Report.pdf",
    "mac_address&serial_number.xlsx",
    "成本统计.xlsx",
    "运费一览表.xlsx",
    "workstation/01-knowledge-base/wechat-conversation-aligned.md",
    "2nd order sample 2层10G 16口 2光8管理/ANW-2116-PG User Manual.pdf",
}


def require(value: bool, message: str) -> None:
    if not value:
        raise ValueError(message)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf8", newline="") as f:
        return list(csv.DictReader(f))


def check_bytes(path: Path, expected_size: int, expected_sha: str) -> bytes:
    data = path.read_bytes()
    require(len(data) == expected_size, f"size mismatch: {path}")
    require(sha256(data).hexdigest() == expected_sha, f"SHA-256 mismatch: {path}")
    return data


def evidence_pages() -> str:
    pattern = re.compile(
        r"^\| (https?://[^ ]+) \| \[[^\]]+\]\(([^)]+)\) \| (\d+) \| `([0-9a-f]{64})` \|"
    )
    rows = [m.groups() for line in (S / "README.md").read_text(encoding="utf8").splitlines()
            if (m := pattern.match(line))]
    require(len(rows) == 4 and len({x[0] for x in rows}) == 4, "expected four distinct URLs")
    require(len({x[1] for x in rows}) == 4, "duplicate evidence artifact")
    expected = set()
    for _url, rel, size, digest in rows:
        path = S / unquote(rel)
        check_bytes(path, int(size), digest)
        expected.add(path.resolve())
    require(expected == {p.resolve() for p in S.rglob("*.extracted.md")},
            "evidence manifest differs from actual page artifacts")
    require({p.name for p in F.glob("*.md")} == {"README.md", "angora-networks.md"},
            "expected one independent customer follow-up plus index")
    return "4/4 local visible-text artifacts, sizes and SHA-256 match (not remote equality)"


def local_inventory() -> str:
    entries = read_csv(S / "local-order-dc-inventory.csv")
    history_rows = read_csv(I / "00-manifest/FILE-INDEX.csv")
    historic = {r["path"]: r for r in history_rows}
    require(len(historic) == len(history_rows), "historical path duplicate")
    selected = {r["path"] for r in history_rows
                if r["path"].startswith(PREFIXES) or r["path"] in EXTRA}
    require(len(entries) == 187 and len(selected) == 187, "expected 187 selected source paths")
    require({r["source_path"] for r in entries} == selected, "scope mismatch")
    require(len({r["source_path"] for r in entries}) == 187, "duplicate source path")
    require(len({r["artifact_path"] for r in entries}) == 187, "duplicate artifact path")
    require(Counter(r["kind"] for r in entries) ==
            {"02-extracted": 87, "03-binary-meta": 98, "01-text-verbatim": 2}, "kind mismatch")
    require([sum(r["source_path"].startswith(x) for r in entries) for x in PREFIXES] ==
            [47, 51, 36, 27, 16], "scope counts mismatch")
    total = source_bytes = 0
    for r in entries:
        old = historic[r["source_path"]]
        require((r["seq"], r["source_bytes_in_original_index"], r["source_sha256_in_original_index"],
                 r["kind"], r["extraction_method"], r["artifact_path"]) ==
                (old["seq"], old["bytes"], old["sha256"], old["kind"], old["method"], old["artifact_path"]),
                f"historical index mismatch: {r['source_path']}")
        data = check_bytes(I / r["artifact_path"], int(r["artifact_bytes_read"]), r["artifact_sha256_read"])
        if r["kind"] == "01-text-verbatim":
            require(len(data) == int(old["bytes"]) and sha256(data).hexdigest() == old["sha256"],
                    f"byte-verbatim artifact differs from historical source index: {r['source_path']}")
        total += len(data)
        source_bytes += int(old["bytes"])
    require(total == 22218235 and source_bytes == 388771437, "unexpected byte totals")
    previous = read_csv(I / "15-source-evidence-r97-2026-10-26/local-first-second-inventory.csv")
    previous_paths = {r["original_path"] for r in previous}
    require(len(previous_paths) == 108 and len(selected & previous_paths) == 1 and
            len(selected | previous_paths) == 294, "r97/r98 overlap mismatch")
    return "187/187 local artifacts: 87 extracts, 98 metadata, 2 verbatim; 1 overlap with r97"


def cross_references_and_rar() -> str:
    historic = {r["path"]: r for r in read_csv(I / "00-manifest/FILE-INDEX.csv")}
    rows = read_csv(S / "photo-and-manual-crossreferences.csv")
    require(len(rows) == 26 and len({r["source_path"] for r in rows}) == 26, "crossref paths mismatch")
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in rows:
        old = historic[r["source_path"]]
        require((r["source_bytes_in_original_index"], r["source_sha256_in_original_index"]) ==
                (old["bytes"], old["sha256"]), f"crossref index mismatch: {r['source_path']}")
        groups[r["group"]].append(r)
    photo = {name: v for name, v in groups.items() if name.startswith("photo-")}
    require(len(photo) == 7 and sum(map(len, photo.values())) == 21, "expected seven photo groups")
    for name, g in photo.items():
        require(len(g) == 3 and len({(x["source_bytes_in_original_index"],
                                     x["source_sha256_in_original_index"]) for x in g}) == 1,
                f"photo group mismatch: {name}")
        require(any(x["source_path"].startswith("4th order ") for x in g) and
                any(x["source_path"].startswith("5th order ") for x in g), f"wrong scope: {name}")
    manuals = groups.get("manual-01", [])
    require(len(manuals) == 5 and len({x["source_sha256_in_original_index"] for x in manuals}) == 1,
            "manual crossref mismatch")
    rar = json.loads((I / "04-archive-members/INFO_2025.12.17/INFO.rar.inventory.json").read_text(encoding="utf8"))
    members = rar["members"]
    require(len(members) == 15, "RAR member count mismatch")
    require(Counter(m["status"] for m in members) ==
            {"covered-by-loose-file": 14, "differs-from-loose-file": 1}, "RAR status mismatch")
    for m in members:
        loose = historic[m["loose"]]
        require(m["sha256"] == loose["sha256"], f"historical loose hash mismatch: {m['member']}")
        require((m["bytes"] == int(loose["bytes"])) == (m["status"] == "covered-by-loose-file"),
                f"RAR index size/status mismatch: {m['member']}")
    diff = next(m for m in members if m["status"] == "differs-from-loose-file")
    require(diff["member"] == "Saga Software Function List_EN.pptx" and diff["bytes"] == 154139 and
            historic[diff["loose"]]["bytes"] == "154107", "RAR version size difference mismatch")
    generator = (ROOT / "tools/extract_archives.py").read_text(encoding="utf8")
    require('status = "covered-by-loose-file" if loose_size == size' in generator and
            '"sha256": loose_sha' in generator, "RAR generator behavior changed; re-audit semantics")
    return "7 photo groups/21 paths, 5 manual paths; RAR directory/loose-size semantics (no extraction)"


def source_and_math() -> str:
    ext = I / "02-extracted"
    third = ext / "3rd order 176台2光16电 L2 PoE"
    pi = (third / "STSC20250117007.xls.extracted.md").read_text(encoding="utf8")
    ci = (third / "Shipment Info/Commercial Invoice_R1.xls.extracted.md").read_text(encoding="utf8")
    pl = (third / "Shipment Info/PL_STSC20250117007.xls.extracted.md").read_text(encoding="utf8")
    warranty = (third / "Shipment Info/Certificate of Warranty.psd.extracted.md").read_text(encoding="utf8")
    for token in ("47174", "ONE THOUSAND FIVE HUNDRED AND FORTY FIVE DOLLARS", "Warranty: 3 years"):
        require(token in pi, f"third PI token missing: {token}")
    for token in ("42720", "4454", "CPT to Ankara Turkey", "FORTY SEVEN THOUSAND ONE HUNDRED"):
        require(token in ci, f"third CI token missing: {token}")
    for token in ("471.9", "TWENTY THREE(23)CARTONS", "ONE HUNDRED AND SEVENTY EIGHT"):
        require(token in pl, f"third PL token missing: {token}")
    for token in ("17th, March, 2025-17th, March, 2028", "1ZB600960435009531", "178 pieces only"):
        require(token in warranty, f"warranty PSD layer token missing: {token}")
    dc = ext / "INFO_2025.12.17"
    rfp = (dc / "ANW-DC-RFP-EN.pdf.extracted.md").read_text(encoding="utf8")
    high = (dc / "STH25G Series Switches Datasheet_EN.pptx.extracted.md").read_text(encoding="utf8")
    low = (dc / "STH1G Series Switches Datasheet_EN.pptx.extracted.md").read_text(encoding="utf8")
    peak = (dc / "Performance of PeakNetX Platform_EN.pptx.extracted.md").read_text(encoding="utf8")
    license_table = (dc / "Saga Software Function List_EN.pptx.extracted.md").read_text(encoding="utf8")
    for token in ("3.6 Tbps", "128 GB SSD", "16 GB RAM", "294,000 entries", "300,000 hours", "Annex-5"):
        require(token in rfp, f"RFP token missing: {token}")
    for token in ("carried on PeakNetX Platform", "DRAM: 2GB", "eMMc: 8GB", "STH-8C48DX"):
        require(token in high, f"STH25G token missing: {token}")
    for token in ("carried on VastLakes Platform", "STH-2QX4XF48GE-HSI"):
        require(token in low, f"STH1G token missing: {token}")
    require("Default profile:122880" in peak and "System packet buffer capacity\t36MByte" in peak,
            "PeakNetX profile/buffer token missing")
    require("Requires ST licence" in license_table and "not available on BigFlow Platform" in license_table,
            "STOS footnote missing")
    chat = (W / "01-knowledge-base/wechat-conversation-aligned.md").read_text(encoding="utf8")
    for token in ("## 📅 2025-03-03", "## 📅 2025-03-04", "## 📅 2025-03-05",
                  "## 📅 2025-03-07", "## 📅 2025-03-17", "Not Turk Telekom, another big client",
                  "## 📅 2025-12-17", "Stacking requires ST license"):
        require(token in chat, f"chat token missing: {token}")
    require(176 * 205 + 176 * 38 + 25 + 700 - 319 + 4000 == 47174, "PI arithmetic")
    require(178 * 240 + 4454 == 47174 and 178 * 1490 == 265220, "CI/supplier arithmetic")
    require(Decimal("466.4") + Decimal("5.5") == Decimal("471.9"), "PL weight arithmetic")
    return "selected source strings, third-order PI/CI/supplier math, PL weight and RFP facts pass"


def links() -> str:
    docs = [R, M, S / "README.md", F / "README.md", F / "angora-networks.md", A]
    pattern = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
    count = 0
    bad = []
    for doc in docs:
        for link in pattern.findall(doc.read_text(encoding="utf8")):
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            count += 1
            if not (doc.parent / unquote(parsed.path)).exists():
                bad.append(f"{doc.relative_to(ROOT)} -> {link}")
    require(not bad, "missing local links:\n" + "\n".join(bad))
    return f"{count} local links exist in r98 report, mapping, source, follow-up and audit"


def main() -> int:
    try:
        for label, fn in (("Evidence", evidence_pages), ("Inventory", local_inventory),
                          ("Crossrefs/RAR", cross_references_and_rar), ("Source/math", source_and_math),
                          ("Links", links)):
            print(f"PASS {label}: {fn()}")
        print("Scope: local bytes/index/selected text and math only; not originals, remote text equality, authenticity, settlement, shipment or functional tests.")
        return 0
    except (OSError, ValueError, KeyError, StopIteration) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
