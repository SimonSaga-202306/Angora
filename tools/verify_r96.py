#!/usr/bin/env python3
"""Offline, read-only checks for the r96 Angora research deliverables.

Run from any directory: python3 tools/verify_r96.py
This checks the local inventory and selected arithmetic/links only. It cannot
verify remote pages, document authenticity, payments, shipment or OCR accuracy.
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
INGEST = ROOT / "ingest/angora-1__arena-01a0ce39__5acb613"
WORK = INGEST / "01-text-verbatim/workstation"
EVIDENCE = INGEST / "11-source-evidence-r96-2026-10-26"
FOLLOWUP = INGEST / "12-followup-angora-r96-2026-10-26"
REPORT = WORK / "08-customer-pipeline/165-angora-order-mac-document-reconciliation-2026-10-26.md"
MAPPING = WORK / "09-orders/120-angora-orders-master-2026-10-21.mapping-r96.md"


def check(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def evidence_inventory() -> str:
    manifest = (EVIDENCE / "README.md").read_text(encoding="utf-8")
    row = re.compile(r"\]\(([^)]+)\).*?\|\s*(\d+)\s*\|\s*`([0-9a-f]{64})`\s*\|")
    records = []
    urls = []
    for line in manifest.splitlines():
        match = row.search(line)
        if not match:
            continue
        path = unquote(match.group(1))
        records.append((path, int(match.group(2)), match.group(3)))
        urls.extend(re.findall(r"<(https?://[^>]+)>", line))
    check(len(records) == 24, f"expected 24 manifest rows; found {len(records)}")
    check(len({x[0] for x in records}) == 24, "duplicate local artifact path")
    check(len(urls) == len(set(urls)) == 19, "expected 19 distinct source URLs")
    on_disk = {
        p.relative_to(EVIDENCE).as_posix()
        for p in EVIDENCE.rglob("*")
        if p.is_file() and p.name != "README.md"
    }
    check(on_disk == {x[0] for x in records}, "manifest and on-disk file sets differ")
    for rel, size, digest in records:
        data = (EVIDENCE / rel).read_bytes()
        check(len(data) == size, f"size mismatch: {rel}")
        check(sha256(data).hexdigest() == digest, f"SHA-256 mismatch: {rel}")
    check(len(list(EVIDENCE.rglob("*.extracted.md"))) == 15, "not 15 visible-text files")
    check(len(list(EVIDENCE.rglob("*.search-snippet.md"))) == 1, "not one search excerpt")
    check(len(list((EVIDENCE / "visual-register").glob("*.png"))) == 5, "not five derived images")
    check(len([p for p in (EVIDENCE / "registry-copy").iterdir() if p.is_file()]) == 3, "not three mirror files")
    return "24/24 files, SHA-256 and sizes match; 19 distinct URL entries"


def registry_and_addresses() -> str:
    for filename, registry, prefix in (
        ("mam.csv", "MA-M", "980637A"),
        ("oui36.csv", "MA-S", "70B3D5822"),
    ):
        with (EVIDENCE / "registry-copy" / filename).open(encoding="utf-8-sig", newline="") as handle:
            matches = [row for row in csv.DictReader(handle) if row["Assignment"] == prefix]
        check(len(matches) == 1, f"{prefix}: expected one row")
        check(matches[0]["Registry"] == registry, f"wrong registry: {prefix}")
        check(matches[0]["Organization Name"] == "Angora Networks", f"wrong registrant: {prefix}")
    metadata = (EVIDENCE / "registry-copy/.lastupdate").read_bytes()
    check(metadata == b"1721654721\n", "unexpected mirror metadata")
    check(sha1(b"blob " + str(len(metadata)).encode() + b"\0" + metadata).hexdigest() ==
          "b5c9e9bd05991779d44720efc3a228600929efa7", "Git blob SHA-1 mismatch")
    p = INGEST / "02-extracted/mac_address&serial_number.xlsx.extracted.md"
    pattern = re.compile(r"^(98:06:37:A5:[0-9A-F]{2}:[0-9A-F]{2})(?:\t(.*))?$")
    rows = [m.groups() for line in p.read_text(encoding="utf-8").splitlines() if (m := pattern.match(line))]
    check(len(rows) == 1536, f"expected 1536 A5 rows, got {len(rows)}")
    values = [int(mac.replace(":", ""), 16) for mac, _ in rows]
    check(values == list(range(values[0], values[0] + 1536)), "A5 addresses are not contiguous")
    check(rows[0][0].endswith("A5:00:00") and rows[-1][0].endswith("A5:05:FF"), "wrong A5 endpoints")
    filled = [extra.split("\t") for _, extra in rows if extra]
    check(len(filled) == 35, f"expected 35 populated rows, got {len(filled)}")
    orders = Counter(parts[1] for parts in filled if len(parts) >= 2 and parts[0] and parts[1])
    check(orders == {"STSC20250507007": 6, "STSC20250526007": 13,
                     "STSC20250619007": 6, "STSC20250711007": 10},
          f"unexpected SN/order distribution: {orders}")
    check(int("980637A4FFFF", 16) - int("980637A10000", 16) + 1 == 262144,
          "A1–A4 inclusive range arithmetic failed")
    check(int("980637AFFFFF", 16) - int("980637A00000", 16) + 1 == 1048576,
          "MA-M inclusive range arithmetic failed")
    check(int("70B3D5822FFF", 16) - int("70B3D5822000", 16) + 1 == 4096,
          "MA-S inclusive range arithmetic failed")
    return "2 mirror prefixes match; A5 1536 rows, 35 populated; ranges recomputed"


def monetary_arithmetic() -> str:
    D = Decimal
    text = (INGEST / "02-extracted/成本统计.xlsx.extracted.md").read_text(encoding="utf-8")
    source_cells = (
        "总收款\t1265\tUSD\t9150.38", "总收款\t1545\tUSD\t10940.39",
        "\t200\tUSD\t5781.12", "\t600\tUSD", "总收款\t10000\tUSD\t72871.34",
        "\t37174\tUSD\t269548.88", "总收款\t1665\tUSD\t11933.07",
        "总收款\t3755\tUSD\t26827.99", "总收款\t990\tUSD\t7050.57",
        "国内运费STSC20250526007\t1\t30", "ANW-2116-PG\t178\t=1270+220",
        "LT-S8310GP-2GX8GT\t2\t500", "LT-S8528XGP-4XS24GT\t1\t1900",
        "LT-S8552XGP-4XS48GT\t1\t3100", "运费\t1\t991.42",
        "LT-S8328GP-4GX16GT-S\t8\t750", "LT-IS6310G-2GX8GT\t2\t622",
        "PVC\t100\t6.3", "软件定制费\t1\t1000", "运费\t1\t2093.61",
        "鹰峤电源\t2\t239", "运费\t1\t22425.96",
        "STC-424XGGPM\t3\t920", "STC-448XGGPM\t3\t1810", "运费\t1\t1515.99",
        "STC-424XGGPM\t10\t920", "运费\t1\t2947.19",
        "STI-288DGGPM\t6\t712", "运费\t1\t646.45",
    )
    for value in source_cells:
        check(value in text, f"source cost-table cell missing: {value}")

    extracted = INGEST / "02-extracted"
    fourth = "4th order sample  2层10G 24口 48口/"
    fifth = "5th order sample  2层10G 24口 48口/"
    sixth = "6th order 6台工业2光8/"
    invoice_tokens = {
        fourth + "Unshipped/采购合同_STSC20250228007.xls.extracted.md":
            ("\t4\t920\t3680", "\t3\t1810\t5430", "TOTAL\t\t\t\t7\t\t9110"),
        fourth + "Unshipped/STSC20250228007_R3.xls.extracted.md":
            ("TOTAL\t\t\t\t7\t\t2130", "ONE THOUSAND EIGHT HUNDRED AND FORTY FIVE"),
        fourth + "STSC20250507007.xls.extracted.md":
            ("TOTAL\t\t\t\t6\t\t1665",),
        fourth + "STSC20250507007_R1.xls.extracted.md":
            ("TOTAL\t\t\t\t6\t\t1920", "ONE THOUSAND SIX HUNDRED AND SIXTY FIVE"),
        fifth + "STSC20250526007.xls.extracted.md":
            ("\t10\t177\t1770", "Balance Payment\tOrder Reference: STSC20250507007",
             "Customized PVC Mask", "TOTAL\t\t\t\t13\t\t4675"),
        fifth + "STSC20250526007_R1.xls.extracted.md":
            ("\t10\t205\t2050", "TOTAL\t\t\t\t13\t\t3755"),
        sixth + "STSC20250619007_R1.xls.extracted.md":
            ("\t6\t125\t750", "Freight Cost\t130usd", "TOTAL\t\t\t\t6\t\t900"),
        sixth + "Shipment Info/CI.xls.extracted.md":
            ("\t6\t125\t750", "Freight Cost\t130usd", "TOTAL\t\t\t\t6\t\t900"),
    }
    for path, tokens in invoice_tokens.items():
        content = (extracted / path).read_text(encoding="utf-8")
        for token in tokens:
            check(token in content, f"invoice text missing {token!r}: {path}")

    project = (extracted / "Gmail - Angora Networks - 250 pieces potential order.pdf.extracted.md").read_text(encoding="utf-8")
    for token in ("received the order from the customer for 375 pcs", "plan to place an order of 385 pcs",
                  "plan to transfer USD$10K", "105*385*0.25=10106.25usd", "25%+25%+balance",
                  "NOT a guaranteed period", "issues with the customer about this order"):
        check(token in project, f"potential-project email text missing: {token}")
    check(D(385) * D(105) == D("40425"), "potential-project quotation arithmetic failed")
    usd = sum(map(D, ("1265", "1545", "200", "600", "10000", "37174", "1665", "3755", "990")))
    cny = sum(map(D, ("9150.38", "10940.39", "5781.12", "72871.34", "269548.88", "11933.07", "26827.99", "7050.57")))
    cost = (D(2)*500 + 1900 + 3100 + D("991.42") +
            D(8)*750 + D(2)*622 + D(100)*D("6.3") + 1000 + D("2093.61") +
            D(178)*(1270+220) + D(2)*239 + D("22425.96") +
            D(3)*920 + D(3)*1810 + D("1515.99") +
            D(10)*920 + D(3)*1810 + D("2947.19") +
            D(6)*712 + 30 + D("646.45"))
    check((usd, cny, cost, cny-cost) == (D("57194"), D("414103.74"), D("338314.62"), D("75789.12")),
          "six-order ledger arithmetic failed")
    check(usd * D("7.15") == D("408937.10"), "hypothetical exchange-rate arithmetic failed")
    check(D(4)*920 + D(3)*1810 == D("9110"), "4th-pre procurement arithmetic failed")
    check(D(1920)-D(1665) == D(255) and D(10)*(205-177) == D(255)+D(25),
          "4th/5th difference arithmetic failed")
    check(D(6)*125 + 125 + 25 == D(900), "6th invoice arithmetic failed")
    return "USD/CNY, 4th/5th and 6th arithmetic pass (not proof of settlement)"


def customers_and_links() -> str:
    customers = ROOT / "TR Customers"
    tier_files = {tier: set((customers / tier).glob("*.md")) for tier in "ABC"}
    counts = {tier: len(files) for tier, files in tier_files.items()}
    check(counts == {"A": 33, "B": 77, "C": 36}, f"unexpected tier counts: {counts}")
    index = (customers / "README.md").read_text(encoding="utf-8")
    refs = re.findall(r"\]\(((?:A|B|C)/[^)]+\.md)\)", index)
    actual = {p.relative_to(customers).as_posix() for files in tier_files.values() for p in files}
    check(len(refs) == 146 and set(refs) == actual, "customer index differs from dossier files")
    check({p.name for p in FOLLOWUP.glob("*.md")} == {"README.md", "angora-networks.md"},
          "r96 follow-up is not one separate customer file plus index")

    docs = [REPORT, MAPPING, FOLLOWUP / "README.md", FOLLOWUP / "angora-networks.md",
            EVIDENCE / "README.md", INGEST / "13-audit-r96-2026-10-26.md"]
    link_pattern = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
    local_links = 0
    failures = []
    for doc in docs:
        for target in link_pattern.findall(doc.read_text(encoding="utf-8")):
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            local_links += 1
            path = (doc.parent / unquote(parsed.path)).resolve()
            if not path.exists():
                failures.append(f"{doc.relative_to(ROOT)} -> {target}")
    check(not failures, "broken local links:\n" + "\n".join(failures))
    return f"146/146 customer files indexed, one r96 follow-up dossier, {local_links} local links exist"


def main() -> int:
    results = []
    for title, func in (("Evidence", evidence_inventory), ("Registry/MAC", registry_and_addresses),
                        ("Arithmetic", monetary_arithmetic), ("Customers/links", customers_and_links)):
        try:
            detail = func()
        except (OSError, ValueError, KeyError, csv.Error) as exc:
            print(f"FAIL {title}: {exc}", file=sys.stderr)
            results.append(False)
        else:
            print(f"PASS {title}: {detail}")
            results.append(True)
    print("Scope: local files only; no remote text equality, original PDF, payment or delivery verification.")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
