#!/usr/bin/env python3
"""Read-only offline checks for r97 source inventory, backup and selected claims.

Run from any directory with `python3 tools/verify_r97.py`. This checks local
bytes, selected source strings, arithmetic and links. It does not fetch or
validate remote pages, original source files, signatures, settlement, shipment,
product functionality, identities or historic snapshot dates.
"""
from __future__ import annotations

import csv
from collections import Counter
from decimal import Decimal
from hashlib import sha1, sha256
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
I = ROOT / "ingest/angora-1__arena-01a0ce39__5acb613"
W = I / "01-text-verbatim/workstation"
S = I / "15-source-evidence-r97-2026-10-26"
B = I / "14-protected-variants-r97-2026-10-26"
R = W / "08-customer-pipeline/166-angora-first-second-order-software-r97-2026-10-26.md"
M = W / "09-orders/120-angora-orders-master-2026-10-21.mapping-r97.md"
F = I / "16-followup-angora-r97-2026-10-26"


def require(value: bool, message: str) -> None:
    if not value:
        raise ValueError(message)


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
    require(len(rows) == 5 and len({x[0] for x in rows}) == 5, "expected five distinct URL rows")
    require(len({x[1] for x in rows}) == 5, "duplicate r97 evidence artifact")
    artifacts = set()
    for url, rel, size, digest in rows:
        path = S / unquote(rel)
        data = check_bytes(path, int(size), digest)
        require(url.encode() in data, f"source header missing URL: {url}")
        artifacts.add(path.resolve())
    actual = {p.resolve() for p in S.rglob("*.extracted.md")}
    require(artifacts == actual, "evidence artifacts differ from manifest")
    require({p.name for p in F.glob("*.md")} == {"README.md", "angora-networks.md"},
            "expected one separate Angora dossier and its index")
    return "5/5 local visible-text artifacts; URL headers, SHA-256 and sizes match"


def local_inventory() -> str:
    with (S / "local-first-second-inventory.csv").open(encoding="utf8", newline="") as f:
        entries = list(csv.DictReader(f))
    require(len(entries) == 108, "expected 108 local source inventory rows")
    require(len({r["original_path"] for r in entries}) == 108, "duplicate source path")
    require(len({r["representation_path"] for r in entries}) == 108, "duplicate artifact path")
    kinds = Counter(r["representation_kind"] for r in entries)
    require(kinds == {"02-extracted": 32, "03-binary-meta": 76}, f"wrong kinds: {kinds}")
    order_counts = Counter(r["original_path"].split("/", 1)[0] for r in entries)
    require(sorted(order_counts.values()) == [48, 60], f"wrong order counts: {order_counts}")
    with (I / "00-manifest/FILE-INDEX.csv").open(encoding="utf8", newline="") as f:
        historic = {r["path"]: r for r in csv.DictReader(f)}
    total = 0
    for r in entries:
        old = historic.get(r["original_path"])
        require(old is not None, f"source absent from historical index: {r['original_path']}")
        require((r["original_bytes_from_historic_manifest"], r["original_sha256_from_historic_manifest"],
                 r["representation_kind"], r["representation_path"]) ==
                (old["bytes"], old["sha256"], old["kind"], old["artifact_path"]),
                f"historical index mismatch: {r['original_path']}")
        data = check_bytes(I / r["representation_path"], int(r["representation_bytes_actual"]),
                           r["representation_sha256_actual"])
        total += len(data)
    require(total == 802476, f"unexpected artifact bytes: {total}")
    return "108/108 derived files; 32 text/layer, 76 metadata; historic index matches"


def protected_variants() -> str:
    pattern = re.compile(
        r"^\| `([^`]+)` \| \[原路径副本\]\(([^)]+)\) \| (\d+) \| `([0-9a-f]{64})` \| `([0-9a-f]{40})` \| `([0-9a-f]{40})` \|$"
    )
    rows = [m.groups() for line in (B / "README.md").read_text(encoding="utf8").splitlines()
            if (m := pattern.match(line))]
    require(len(rows) == 27 and len({r[0] for r in rows}) == 27, "expected 27 distinct backup entries")
    actual = {p.resolve() for p in (B / "original-paths").rglob("*") if p.is_file()}
    expected = set()
    hashes = {}
    total = 0
    for original, rel, size, digest, blob, _old_head in rows:
        require(unquote(rel) == "original-paths/" + original, f"original path not preserved: {original}")
        p = B / unquote(rel)
        data = check_bytes(p, int(size), digest)
        require(sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest() == blob,
                f"Git blob mismatch: {original}")
        total += len(data)
        hashes[original] = (int(size), digest)
        expected.add(p.resolve())
    require(actual == expected, "backup manifest differs from actual files")
    require(total == 17427183, f"wrong backup byte total: {total}")
    audit = (I / "13-audit-r96-2026-10-26.md").read_text(encoding="utf8")
    old_pattern = re.compile(r"^\| `([^`]+)` \| (\d+) \| `([0-9a-f]{64})` \| `[0-9a-f]{64}` \|$")
    old = [m.groups() for line in audit.splitlines() if (m := old_pattern.match(line))]
    require(len(old) == 23, "r96 audit expected 23 historic differences")
    for path, size, digest in old:
        require(hashes.get(path) == (int(size), digest), f"r96 variant not matched: {path}")
    return "27/27 preserved byte-for-byte, including all 23 r96 audit variants"


def source_checks_and_arithmetic() -> str:
    ext = I / "02-extracted"
    first = ext / "1st order sample  3层10G 24口 48口"
    second = ext / "2nd order sample 2层10G 16口 2光8管理"
    layer = (ext / "Gmail - layer 3 managed switch.pdf.extracted.md").read_text(encoding="utf8")
    require("Sun, Apr 28, 2024" in layer and "Taylan has already responded to an earlier email" in layer,
            "earlier contact email not found")
    pi1 = (first / "STSC20240508007.pdf.extracted.md").read_text(encoding="utf8")
    for token in ("STC-28DGGPM", "Commercial Ethernet Switch", "STC-424XGGPM", "STC-448XGGPM", "$1,265.00"):
        require(token in pi1, f"first invoice missing: {token}")
    for file, token in (("STSC20241021007.xls.extracted.md", "\t7\t\t1545"),
                        ("STSC20241028007.xls.extracted.md", "\t1\t\t200"),
                        ("STSC20241105007.xls.extracted.md", "\t3\t\t600"),
                        ("CI.xls.extracted.md", "\t10\t\t2345")):
        require(token in (second / file).read_text(encoding="utf8"), f"second invoice token missing: {file}")
    supplier = next(second.glob("*P20241026-01*pdf.extracted.md")).read_text(encoding="utf8")
    require("人民币：6624" in supplier and "管理界面修改费用 1000" in supplier,
            "supplier contract total/fee absent")
    D = Decimal
    require(5*D(150)+2*D(110)+320+230+25 == 1545, "initial PI arithmetic")
    require(3*D(150)+125+25 == 600 and D(1545)+200+600 == 2345, "additional PI arithmetic")
    require(8*D(252)+2*D("164.5") == 2345, "commercial invoice arithmetic")
    require(5*750+2*622+630+1000 == 6624 and 5*750+2*622+630 == 5624,
            "supplier contract arithmetic")
    mac_re = r"\b(?:[0-9A-F]{2}:){5}[0-9A-F]{2}\b"
    a = set(re.findall(mac_re, (second / "采购合同_STSC20241021007.xls.extracted.md").read_text(encoding="utf8")))
    b = set(re.findall(mac_re, (second / "采购合同_STSC20241105007.xls.extracted.md").read_text(encoding="utf8")))
    require(len(a) == 7 and len(b) == 3 and len(a | b) == 10, "unexpected 7+3 requested addresses")
    require(all(int(mac.replace(":", ""), 16) >> 20 == int("980637A", 16) for mac in a | b),
            "requested address falls outside recorded /28")
    return "selected source tokens, invoice math and 7+3 requested MAC values pass"


def links() -> str:
    docs = [R, M, S / "README.md", B / "README.md", F / "README.md", F / "angora-networks.md",
            I / "17-audit-r97-2026-10-26.md"]
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
    return f"{count} local links exist in report, mapping, manifests and follow-up"


def main() -> int:
    try:
        for label, fn in (("Evidence", evidence_pages), ("Local inventory", local_inventory),
                          ("Backup", protected_variants), ("Source/math", source_checks_and_arithmetic),
                          ("Links", links)):
            print(f"PASS {label}: {fn()}")
        print("Scope: local bytes and selected source strings only; not original documents, remote text equality, payment, shipment or project outcome.")
        return 0
    except (OSError, ValueError, KeyError, StopIteration) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
