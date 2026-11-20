#!/usr/bin/env python3
"""Local consistency checks for r115. Not a verification of source truth/fidelity."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[3]
I = ROOT / "ingest/angora-1__arena-01a0ce39__5acb613"
D = I / "85-source-evidence-r115-2026-10-26"
W = I / "01-text-verbatim/workstation"


def require(value, message):
    if not value:
        raise AssertionError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def csvrows(path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def validate_relative_links(document):
    text = document.read_text(encoding="utf-8")
    count = 0
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if target.startswith(("https://", "http://", "mailto:", "#")):
            continue
        target = unquote(target.split("#", 1)[0])
        if not target:
            continue
        path = (document.parent / target).resolve()
        require(path.exists(), f"broken local link: {document}: {target}")
        count += 1
    return count


def validate_inventories():
    specs = [
        ("prior-round-read-inventory.csv", 13, 95096),
        ("source-read-inventory.csv", 127, 169015),
        ("extension-read-inventory.csv", 19, 27454),
    ]
    seen = set()
    total = 0
    for name, expected_count, expected_bytes in specs:
        rows = csvrows(D / name)
        require(len(rows) == expected_count, f"{name}: count")
        subtotal = 0
        for row in rows:
            rel = row["path"]
            require(rel not in seen, f"duplicate inventory path {rel}")
            seen.add(rel)
            data = (ROOT / rel).read_bytes()
            data.decode("utf-8")
            require(len(data) == int(row["bytes_read"]), f"size: {rel}")
            require(sha(data) == row["sha256"], f"hash: {rel}")
            subtotal += len(data)
        require(subtotal == expected_bytes, f"{name}: total bytes")
        total += subtotal
    require(len(seen) == 159 and total == 291565, "combined inventory")
    return len(seen), total


def validate_queries():
    counts = []
    zeros = []
    for number in range(1, 109):
        qid = f"Q{number:02}"
        obj = json.loads((D / f"search-discovery/{qid}.json").read_text(encoding="utf-8"))
        require(obj["id"] == qid and obj["status"] == "success", qid)
        n = obj["reported_result_count"]
        require(isinstance(n, int) and n >= 0, f"count {qid}")
        counts.append(n)
        if not n:
            zeros.append(qid)
    require(sum(counts) == 431, "search counts")
    require(zeros == ["Q42", "Q78", "Q96", "Q97"], "zero query list")
    plans = [D / "search-plan-before-search.csv"]
    plans.extend(D / f"search-plan-extension{'-' + str(n) if n >= 2 else ''}-before-search.csv" for n in range(1, 9))
    rows = [r for plan in plans for r in csvrows(plan)]
    require([r["id"] for r in rows] == [f"Q{i:02}" for i in range(1, 109)], "plan order")
    for row in rows:
        saved = json.loads((D / f"search-discovery/{row['id']}.json").read_text(encoding="utf-8"))
        require(saved["query"] == row["query"], f"query mismatch {row['id']}")
    return len(counts), sum(counts), zeros


def validate_anchors():
    rows = csvrows(D / "evidence-traceability.csv")
    extension = csvrows(D / "evidence-traceability-extension.csv")
    require(len(rows) == 18 and len(extension) == 8, "anchor counts")
    for row in rows:
        path = D / row["path_relative_to_r115"]
        data = path.read_bytes()
        require(sha(data) == row["file_sha256"], f"anchor hash: {path}")
        require(data.decode("utf-8").count(row["exact_utf8_anchor"]) == int(row["occurrences"]), f"anchor: {path}")
    for row in extension:
        path = ROOT / row["path"]
        data = path.read_bytes()
        require(sha(data) == row["file_sha256"], f"extension hash: {path}")
        require(data.decode("utf-8").count(row["exact_utf8_anchor"]) == int(row["occurrences"]), f"extension anchor: {path}")
    return len(rows) + len(extension)


def validate_corrections():
    checks = [
        ("P02", "external-visible/e-safe.org/2025-e-safe-siber-guvenlik-odulleri-juri-seviyesi/chunk-0.visible.md", "İlgili kişinin hak ve özgürlüklerine", "İlgili kişinin temel hak ve özgürlüklerine"),
        ("P03", "external-visible/www.enerjimagazin.com/haber-epdk-ve-elder-in-enerjim-sensin-programinda-finalistler-aciklandi-12770.html/chunk-0.visible.md", "| |     |     |     |\n| --- | --- | --- |\n\n|     |     |     |\n| --- | --- | --- |\n| Adınız", "| |     |     |     |\n| --- | --- | --- |\n\n| |     |     |     |\n| --- | --- | --- |\n| Adınız"),
        ("P10", "external-chunks/e-safe.org/siber-vatanin-mimarlari-bestepede-43032/chunk-0.visible.md", "](https://e-safe.org/turkiyede-kvk-farkindaligi-icin-onemli-bir-etkinlik-0-24-screenshot-scaled.jpg)", "](https://e-safe.org/turkiyede-kvk-farkindaligi-icin-onemli-bir-etkinlik-47524)"),
    ]
    for name, corrected_path, old, new in checks:
        draft = (D / f"transcription-drafts/{name}/chunk-0.pre-correction.visible.md").read_text(encoding="utf-8")
        corrected = (D / corrected_path).read_text(encoding="utf-8")
        require(draft.count(old) == 1 and draft.replace(old, new, 1) == corrected, f"correction {name}")
    return len(checks)


def validate_catalog():
    rows = csvrows(D / "source-catalog.csv") + csvrows(D / "source-catalog-extension.csv")
    require(len(rows) == 28, "catalog blocks")
    for row in rows:
        require((D / row["local_path_relative_to_r115"]).is_file(), f"catalog {row}")
    p01 = next(r for r in csvrows(D / "fetch-outcomes.csv") if r["source_id"] == "P01")
    require(p01["blocks_fetched"] == "1" and p01["blocks_available"] == "16", "P01 partial status")
    return len(rows)


def validate_documents():
    docs = [
        W / "08-customer-pipeline/184-angora-institutional-partnership-evidence-r115-2026-10-26.md",
        W / "09-orders/120-angora-orders-dossier-2026-10-21.r115-appendix.md",
        W / "09-orders/120-angora-orders-master-2026-10-21.mapping-r115.md",
        I / "86-followup-angora-r115-2026-10-26/angora-networks.md",
        I / "87-audit-r115-2026-10-26.md",
        D / "README.md",
    ]
    n = sum(validate_relative_links(doc) for doc in docs)
    report = docs[0].read_text(encoding="utf-8")
    for phrase in ["主体未确认", "ULAK", "候选", "前三", "四个", "159/159", "291,565", "没有完整持久化", "P01", "不宣称穷尽"]:
        require(phrase in report, f"report missing boundary: {phrase}")
    for doc in docs[1:3]:
        s = doc.read_text(encoding="utf-8")
        require("r107" in s and "r114" in s, f"missing prior round cross-reference: {doc}")
    return len(docs), n


def validate_master_pointer():
    plan = json.loads((D / "dossier-append-plan-before-write.json").read_text(encoding="utf-8"))
    data = (ROOT / plan["target"]).read_bytes()
    n = plan["expected_head_and_local_prefix_bytes"]
    require(len(data) == n + plan["addition_bytes"], "master length")
    require(sha(data[:n]) == plan["expected_head_and_local_prefix_sha256"], "master prefix")
    addition = (ROOT / plan["addition_path"]).read_bytes()
    require(data[n:] == addition and sha(addition) == plan["addition_sha256"], "master suffix")
    return n, len(addition)


def main():
    branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=ROOT, text=True).strip()
    require(branch == "arena/5da004bd-angora", "branch")
    elapsed = json.loads((D / "timing-checkpoint.json").read_text(encoding="utf-8"))
    require(elapsed["same_boot_id_as_first_recorded_checkpoint"] and elapsed["elapsed_from_first_checkpoint_seconds"] > 600, "time")
    results = {
        "status": "PASS",
        "branch": branch,
        "inventories": validate_inventories(),
        "query_metadata": validate_queries(),
        "catalog_blocks": validate_catalog(),
        "selected_local_anchors": validate_anchors(),
        "single_replacement_corrections": validate_corrections(),
        "documents_and_local_links": validate_documents(),
        "master_prefix_and_append_bytes": validate_master_pointer(),
        "same_boot_checked_elapsed_seconds": elapsed["elapsed_from_first_checkpoint_seconds"],
        "limitations": "Local consistency only; not source fidelity, completeness of search responses, historical publication, legal identity, real-world performance, contract, delivery or award truth.",
    }
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
