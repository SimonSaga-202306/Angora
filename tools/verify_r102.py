#!/usr/bin/env python3
"""Verify r102's bounded local evidence and preservation; no archive extraction.

This checks local derivative bytes and selected identity-document strings. It
cannot authenticate originals, prove OCR speakers, deliveries, live devices,
legal compliance or customer acceptance. Mutation tests are in memory only.
"""
from __future__ import annotations

import copy
import csv
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
I = ROOT / "ingest/angora-1__arena-01a0ce39__5acb613"
W = I / "01-text-verbatim/workstation"
S = I / "33-source-evidence-r102-2026-10-26"
P = I / "32-entry-safety-r102-2026-10-26"
F = I / "34-followup-angora-r102-2026-10-26"
GROUPS = (
    ("scope-before-read.csv", "read-inventory.csv", 15, 1413626),
    ("supplement-ocr-scope-before-read.csv", "supplement-ocr-read-inventory.csv", 12, 236997),
    ("supplement-certificate-scope-before-read.csv", "supplement-certificate-read-inventory.csv", 1, 2545),
    ("supplement-ieee-scope-before-read.csv", "supplement-ieee-read-inventory.csv", 1, 608108),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def digest(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def source_path(rel: str) -> Path:
    path = I / rel
    require(not Path(rel).is_absolute() and ".." not in Path(rel).parts, f"unsafe relative path: {rel!r}")
    require(path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(I.resolve()), f"missing or unsafe: {rel!r}")
    return path


def verify_group(scope: list[dict[str, str]], inv: list[dict[str, str]], count: int, size: int) -> None:
    require(len(scope) == len(inv) == count, "group count")
    require(sum(int(r["size_bytes"]) for r in inv) == size, "group bytes")
    require(len({r["path_from_ingest_root"] for r in inv}) == count, "duplicate source paths")
    for n, (a, b) in enumerate(zip(scope, inv), 1):
        rel = b["path_from_ingest_root"]
        require(a["seq"] == b["seq"] == str(n), f"sequence: {rel}")
        require(a["path_from_ingest_root"] == rel and a["size_bytes"] == b["size_bytes"], f"scope mismatch: {rel}")
        data = source_path(rel).read_bytes()
        require(len(data) == int(b["size_bytes"]) and digest(data) == b["sha256"], f"source bytes: {rel}")


def verify_context(scope: list[dict[str, str]], inv: list[dict[str, str]]) -> None:
    require(len(scope) == len(inv) == 9 and sum(int(r["size_bytes"]) for r in inv) == 178368, "context count/bytes")
    for n, (a, b) in enumerate(zip(scope, inv), 1):
        rel = b["path_from_ingest_root"]
        require(a["seq"] == b["seq"] == str(n), f"context sequence: {rel}")
        require(a["path_from_ingest_root"] == rel and a["size_bytes"] == b["size_bytes"], f"context scope: {rel}")
        original = source_path(rel).read_bytes()[:int(b["size_bytes"])]
        require(len(original) == int(b["size_bytes"]) and digest(original) == b["sha256"], f"context prefix: {rel}")


def verify_anchors(anchors: list[dict[str, str]], sources: dict[str, dict[str, str]]) -> None:
    require(len(anchors) == len({r["id"] for r in anchors}) == 29, "anchor IDs/count")
    cache: dict[str, list[str]] = {}
    for r in anchors:
        rel = r["source_path_from_ingest_root"]
        require(rel in sources and r["source_sha256"] == sources[rel]["sha256"], f"anchor source: {r['id']}")
        if rel not in cache:
            cache[rel] = source_path(rel).read_text(encoding="utf-8", errors="replace").splitlines()
        n = int(r["line_1_based"])
        require(1 <= n <= len(cache[rel]) and bool(r["exact_needle"]) and r["exact_needle"] in cache[rel][n - 1], f"anchor line/token: {r['id']}")


def verify_ocr_dates(events: list[dict[str, str]], sources: dict[str, dict[str, str]]) -> None:
    expected = {
        "Weixin Image_2026-09-23_223749_931.jsonl": {93, 99},
        "Weixin Image_2026-09-23_224033_579.jsonl": {202, 240},
        "Weixin Image_2026-09-23_224111_987.jsonl": {206, 207, 208, 209, 210, 290, 291},
        "Weixin Image_2026-09-23_224347_969.jsonl": {73, 74, 75, 95},
    }
    require(len(events) == 15, "OCR event count")
    actual: dict[str, set[int]] = {}
    cache: dict[str, list[dict]] = {}
    timestamp = re.compile(r"^20\d\d-\d{1,2}-\d{1,2} \d{1,2}:\d{2}$")
    for event in events:
        rel = event["source_path_from_ingest_root"]
        require(rel in sources and event["source_sha256"] == sources[rel]["sha256"], "OCR source linkage")
        if rel not in cache:
            cache[rel] = [json.loads(line) for line in source_path(rel).read_text(encoding="utf-8").splitlines()]
        data = cache[rel]
        n = int(event["event_line_1_based"])
        require(1 <= n <= len(data), "OCR line bounds")
        obj = data[n - 1]
        require(event["event_text"] == obj["text"] and event["event_speaker_in_aligned_ocr"] == (obj.get("speaker") or "unattributed"), "OCR event content")
        prior = [(i, row["text"]) for i, row in enumerate(data, 1) if i < n and timestamp.fullmatch(str(row.get("text", "")))]
        later = [(i, row["text"]) for i, row in enumerate(data, 1) if i > n and timestamp.fullmatch(str(row.get("text", "")))]
        require(bool(prior) and bool(later), "OCR timestamp boundaries")
        pi, pt = prior[-1]
        ni, nt = later[0]
        require((str(pi), pt, str(ni), nt) == (event["preceding_timestamp_line_1_based"], event["preceding_timestamp_text"], event["next_timestamp_line_1_based"], event["next_timestamp_text"]), "OCR nearest timestamp boundary")
        require(pt.split()[0] == nt.split()[0], "OCR event spans two different dates")
        actual.setdefault(Path(rel).name, set()).add(n)
    require(actual == expected and sum(map(len, actual.values())) == len(events), "OCR event selection")


def verify_assets(assets: list[dict[str, str]], sources: dict[str, dict[str, str]]) -> None:
    idx = {r["seq"]: r for r in rows(I / "00-manifest/FILE-INDEX.csv")}
    require(len(assets) == len({r["historical_index_seq"] for r in assets}) == 13, "asset records")
    meta_count = 0
    for a in assets:
        old = idx[a["historical_index_seq"]]
        require(a["historical_original_path"] == old["path"], "historic path")
        require(a["historical_original_bytes"] == old["bytes"] and a["historical_original_sha256"] == old["sha256"], "historic size/hash")
        require(a["historical_extraction_method"] == old["method"], "historic method")
        rel = a["current_representation_path_from_ingest_root"]
        require(rel == old["artifact_path"] and rel in sources, "asset representation path")
        rep = source_path(rel).read_bytes()
        require(len(rep) == int(a["current_representation_bytes"]) and digest(rep) == a["current_representation_sha256"] == sources[rel]["sha256"], "asset representation bytes")
        require(a["original_reobtained_this_round"] == "no", "unsupported original claim")
        if "metadata" in a["representation"]:
            meta = json.loads(rep)
            require(meta["path"] == old["path"] and str(meta["bytes"]) == old["bytes"] and meta["sha256"] == old["sha256"], "metadata/index disagreement")
            meta_count += 1
    require(meta_count == 6, "metadata count")


def verify_mac_tables(records: list[dict[str, str]], sources: dict[str, dict[str, str]]) -> None:
    rel = "02-extracted/2nd order sample 2层10G 16口 2光8管理/Angora-Replies_2024.10.23.docx.extracted.md"
    require(len(records) == 14 and rel in sources, "MAC table row count/source")
    text = source_path(rel).read_text(encoding="utf-8")
    expected = []
    mac_pattern = r"\b(?:[0-9A-F]{2}:){5}[0-9A-F]{2}\b"
    for table in (1, 2):
        block = re.search(rf"\[TABLE {table}\].*?\n\n", text, re.S)
        require(bool(block), f"table {table} missing")
        values = re.findall(mac_pattern, block.group())
        require(len(values) == 7, f"table {table} count")
        previous = None
        for n, mac in enumerate(values, 1):
            v = int(mac.replace(":", ""), 16)
            require(v >> 20 == int("980637A", 16), "outside recorded MA-M")
            expected.append((str(table), str(n), mac, "" if previous is None else str(v - previous)))
            previous = v
    require(expected[:7] == [("1", str(i), expected[i - 1][2], expected[i - 1][3]) for i in range(1, 8)], "table 1 order")
    require([x[2] for x in expected[:7]] == [x[2] for x in expected[7:]], "source table duplicates")
    require(len({x[2] for x in expected}) == 7, "MAC unique count")
    require([int(x[3]) for x in expected[1:7]] == [64, 64, 48, 80, 64, 64], "MAC gaps")
    for r, (table, n, mac, gap) in zip(records, expected):
        require(r["source_path_from_ingest_root"] == rel and r["source_sha256"] == sources[rel]["sha256"], "MAC source linkage")
        require((r["source_table"], r["source_row"], r["mac_address"], r["delta_from_previous_row_decimal"]) == (table, n, mac, gap), "MAC row differs")
        require(r["registered_ma_m_prefix"] == "98:06:37:A /28", "MAC prefix label")


def verify_ranges() -> None:
    registry = rows(I / "11-source-evidence-r96-2026-10-26/registry-copy/mam.csv")
    matches = [r for r in registry if r.get("Assignment", "").upper() == "980637A"]
    require(len(matches) == 1 and matches[0]["Registry"] == "MA-M" and matches[0]["Organization Name"] == "Angora Networks", "fixed mirror registration")
    lo, hi = int("980637A10000", 16), int("980637A4FFFF", 16)
    require(lo >> 20 == hi >> 20 == int("980637A", 16) and hi - lo + 1 == 262144 and 2**20 == 1048576, "address arithmetic")
    doc = source_path("02-extracted/3rd order 176台2光16电 L2 PoE/Info to be provided-Angora.docx.extracted.md").read_text(encoding="utf-8")
    require("25012116XXX03" in doc and "from 001 to 176" in doc, "proposed serial pattern")
    require("98:06:37:A1:00:00. to 98:06:37:A4:FF:FF" in doc, "source address range")
    cert = source_path("02-extracted/3rd order 176台2光16电 L2 PoE/Shipment Info/Certificate of Warranty.psd.extracted.md").read_text(encoding="utf-8")
    serial = lambda n: f"25012116{n:03d}03"
    require(f"{serial(1)}~{serial(176)}" in cert and f"{serial(177)}~{serial(178)}" in cert, "certificate serial ranges")


def verify_entry(before: list[dict[str, str]], comp: list[dict[str, str]]) -> None:
    require(len(before) == len(comp) == 868 and sum(int(r["size_bytes"]) for r in before) == 46015150, "entry scope")
    require(len({r["path_from_repo_root"] for r in comp}) == 868, "duplicate entry path")
    require(Counter(r["comparison_to_remote"] for r in comp) == {"same": 837, "different": 31}, "entry comparison counts")
    groups: Counter[str] = Counter()
    for a, b in zip(before, comp):
        require(a["path_from_repo_root"] == b["path_from_repo_root"] and a["size_bytes"] == b["bytes"], "entry scope mismatch")
        if b["comparison_to_remote"] == "same":
            require(b["incoming_sha256"] == b["remote_sha256"] and not b["existing_protected_variant_path"], "same-entry metadata")
            continue
        rel = Path(b["existing_protected_variant_path"])
        require(not rel.is_absolute() and ".." not in rel.parts, "unsafe protected path")
        path = ROOT / rel
        require(path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(ROOT.resolve()), "missing protected copy")
        data = path.read_bytes()
        require(len(data) == int(b["bytes"]) and digest(data) == b["incoming_sha256"] and b["incoming_sha256"] != b["remote_sha256"], "protected byte mismatch")
        groups["r97" if "/14-protected-" in str(rel) else "r99" if "/21-protected-" in str(rel) else "r101" if "/28-protected-" in str(rel) else "other"] += 1
    require(groups == {"r97": 27, "r99": 1, "r101": 3}, "protected group counts")


def previous_sets() -> dict[str, set[str]]:
    def grab(file: str, key: str) -> set[str]:
        return {r[key] for r in rows(I / file)}
    result = {
        "r97": grab("15-source-evidence-r97-2026-10-26/local-first-second-inventory.csv", "representation_path"),
        "r98": grab("18-source-evidence-r98-2026-10-26/local-order-dc-inventory.csv", "artifact_path"),
        "r99_full": grab("22-source-evidence-r99-2026-10-26/scope-inventory.csv", "path_from_ingest_root"),
        "r99_partial": grab("22-source-evidence-r99-2026-10-26/context-partial-inventory.csv", "path_from_ingest_root"),
    }
    for label, root, stems in (
        ("r100", "25-source-evidence-r100-2026-10-26", ("selected", "rootfs-text", "supplement-wechat", "supplement-ocr")),
        ("r101", "29-source-evidence-r101-2026-10-26", ("", "supplement-ocr", "supplement-manual", "supplement-monitoring", "supplement-ac5", "supplement-user-manual")),
    ):
        result[label] = set()
        for stem in stems:
            result[label] |= grab(f"{root}/{stem + '-' if stem else ''}read-inventory.csv", "path_from_ingest_root")
    return result


def verify_overlap(items: list[dict[str, str]], overlaps: list[dict[str, str]]) -> None:
    require(len(overlaps) == len(items) == 29, "overlap row count")
    groups = previous_sets()
    current = {r["path_from_ingest_root"] for r in items}
    counts = {k: len(current & v) for k, v in groups.items()}
    require(counts == {"r97": 8, "r98": 7, "r99_full": 5, "r99_partial": 5, "r100": 4, "r101": 7}, "overlap counts")
    for a, b in zip(items, overlaps):
        rel = a["path_from_ingest_root"]
        require(b["path_from_ingest_root"] == rel and b["sha256"] == a["sha256"], "overlap row source")
        for k, group in groups.items():
            require(b[k] == ("yes" if rel in group else "no"), f"overlap flag {k}: {rel}")


def verify_git(items: list[dict[str, str]]) -> None:
    paths = [(I / r["path_from_ingest_root"]).relative_to(ROOT).as_posix() for r in items]
    tracked = {}
    for item in subprocess.check_output(["git", "ls-files", "-s", "-z", "--", *paths], cwd=ROOT).split(b"\0"):
        if item:
            meta, path = item.split(b"\t", 1)
            tracked[path.decode("utf-8")] = meta.split()[1].decode("ascii")
    require(set(tracked) == set(paths) and len(paths) == 29, "Git index source paths")
    for path in paths:
        oid = subprocess.check_output(["git", "hash-object", "--no-filters", "--", path], cwd=ROOT).decode().strip()
        require(oid == tracked[path], f"Git blob differs: {path}")
    raw = subprocess.check_output(["git", "check-attr", "-z", "text", "--", *paths], cwd=ROOT).split(b"\0")
    triples = list(zip(*[iter(raw[:-1])] * 3))
    require(len(triples) == 29 and all(v == b"unset" for _, _, v in triples), "source -text attributes")


def verify_links(context: list[dict[str, str]]) -> int:
    docs = [S / "README.md", P / "README.md", F / "README.md", F / "angora-networks.md",
            I / "35-audit-r102-2026-10-26.md",
            W / "08-customer-pipeline/171-angora-branding-label-identity-r102-2026-10-26.md",
            W / "09-orders/120-angora-orders-master-2026-10-21.mapping-r102.md"]
    texts = [(p, p.read_text(encoding="utf-8")) for p in docs]
    for r in context:
        p = source_path(r["path_from_ingest_root"])
        tail = p.read_bytes()[int(r["size_bytes"]):].decode("utf-8")
        if tail:
            texts.append((p, tail))
    count = 0
    for origin, text in texts:
        for raw in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
            target = urlsplit(raw)
            if target.scheme or target.netloc or not target.path:
                continue
            path = (origin.parent / unquote(target.path)).resolve()
            require(path.is_relative_to(ROOT.resolve()) and path.exists(), f"missing link in {origin}: {raw}")
            count += 1
    require({p.name for p in F.glob("*.md")} == {"README.md", "angora-networks.md"}, "follow-up scope")
    return count


def reject(fn, *args) -> None:
    try:
        fn(*args)
    except (AssertionError, KeyError, IndexError, ValueError):
        return
    raise AssertionError(f"negative test accepted: {fn.__name__}")


def main() -> int:
    items = []
    for scope, inv, count, size in GROUPS:
        a, b = rows(S / scope), rows(S / inv)
        verify_group(a, b, count, size)
        items.extend(b)
    require(len(items) == len({r["path_from_ingest_root"] for r in items}) == 29, "source total")
    require(sum(int(r["size_bytes"]) for r in items) == 2261276, "source total bytes")
    sources = {r["path_from_ingest_root"]: r for r in items}
    print("PASS Inventory: 29/29 bounded derivative paths, 2,261,276 bytes and SHA-256")

    cs, context = rows(S / "context-before-read.csv"), rows(S / "context-prefix-read-inventory.csv")
    verify_context(cs, context)
    print("PASS Context: 9/9 previous-report prefixes preserved, 178,368 bytes")

    anchors, assets, mac = rows(S / "evidence-traceability.csv"), rows(S / "asset-records-crossrefs.csv"), rows(S / "mac-address-table-rows.csv")
    events = rows(S / "ocr-event-date-boundaries.csv")
    verify_anchors(anchors, sources)
    verify_ocr_dates(events, sources)
    verify_assets(assets, sources)
    verify_mac_tables(mac, sources)
    verify_ranges()
    print("PASS Evidence: 29 selected line anchors; 15 OCR date boundaries; 13 historic asset paths; two 7-row MAC tables, serial and fixed-registry arithmetic")

    entry_scope, entry = rows(P / "entry-scope-before-comparison.csv"), rows(P / "entry-comparison.csv")
    verify_entry(entry_scope, entry)
    print("PASS Safety: 868 incoming paths, 837 same and 31 different; all 31 already protected byte-for-byte")

    verify_git(items)
    verify_overlap(items, rows(S / "overlap-by-path.csv"))
    print("PASS Git/overlaps: 29/29 local Git blobs match, all -text; overlaps 8/7/5/5/4/7")
    print(f"PASS Links: {verify_links(context)} local links in r102 deliverables/corrections; one internal customer file")

    a, b = rows(S / GROUPS[0][0]), rows(S / GROUPS[0][1])
    changed = copy.deepcopy(b); changed[0]["sha256"] = "0" * 64
    reject(verify_group, a, changed, 15, 1413626)
    changed = copy.deepcopy(a); changed[0]["path_from_ingest_root"] += ".bad"
    reject(verify_group, changed, b, 15, 1413626)
    changed = copy.deepcopy(context); changed[0]["sha256"] = "0" * 64
    reject(verify_context, cs, changed)
    changed = copy.deepcopy(anchors); changed[0]["exact_needle"] = "__NOT_IN_SOURCE__"
    reject(verify_anchors, changed, sources)
    changed = copy.deepcopy(events); changed[0]["preceding_timestamp_text"] = "2024-10-24 10:41"
    reject(verify_ocr_dates, changed, sources)
    changed = copy.deepcopy(assets); changed[0]["historical_original_sha256"] = "0" * 64
    reject(verify_assets, changed, sources)
    changed = copy.deepcopy(mac); changed[1]["delta_from_previous_row_decimal"] = "999"
    reject(verify_mac_tables, changed, sources)
    changed = copy.deepcopy(entry); next(x for x in changed if x["comparison_to_remote"] == "different")["incoming_sha256"] = "0" * 64
    reject(verify_entry, entry_scope, changed)
    changed = copy.deepcopy(rows(S / "overlap-by-path.csv")); changed[0]["r101"] = "invalid"
    reject(verify_overlap, items, changed)
    print("PASS Negative: nine in-memory mutations of hashes, scope, context, anchors, OCR dates, assets, MAC rows, safety and overlaps rejected")
    print("Boundary: evidence is local and derivative; no claim about original authenticity, physical marking, deployment, legal compliance or acceptance.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, OSError, subprocess.CalledProcessError, KeyError, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
