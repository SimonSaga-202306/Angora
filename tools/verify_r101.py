#!/usr/bin/env python3
"""Verify r101's bounded local evidence, not original authenticity or deployment.

All mutation tests operate on in-memory CSV rows. This tool does not open any
archive, contact an external service, change devices or read the passed RFPs.
"""
from __future__ import annotations

import copy
import csv
import hashlib
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
I = ROOT / "ingest/angora-1__arena-01a0ce39__5acb613"
W = I / "01-text-verbatim/workstation"
S = I / "29-source-evidence-r101-2026-10-26"
P = I / "28-protected-variants-r101-2026-10-26"
F = I / "30-followup-angora-r101-2026-10-26"
GROUPS = (
    ("scope-before-read.csv", "read-inventory.csv", 19, 1872079),
    ("supplement-ocr-scope-before-read.csv", "supplement-ocr-read-inventory.csv", 3, 70196),
    ("supplement-manual-scope-before-read.csv", "supplement-manual-read-inventory.csv", 7, 10318789),
    ("supplement-monitoring-scope-before-read.csv", "supplement-monitoring-read-inventory.csv", 3, 67217),
    ("supplement-ac5-scope-before-read.csv", "supplement-ac5-read-inventory.csv", 3, 21172),
    ("supplement-user-manual-scope-before-read.csv", "supplement-user-manual-read-inventory.csv", 3, 3837329),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def source_path(rel: str) -> Path:
    path = I / rel
    require(not Path(rel).is_absolute() and ".." not in Path(rel).parts, f"unsafe path {rel!r}")
    require(path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(I.resolve()), f"missing/unsafe {rel!r}")
    return path


def verify_group(scope: list[dict[str, str]], inv: list[dict[str, str]], count: int, size: int) -> None:
    require(len(scope) == len(inv) == count, "scope/inventory count")
    require([int(r["seq"]) for r in scope] == list(range(1, count + 1)), "scope sequence")
    require([int(r["seq"]) for r in inv] == list(range(1, count + 1)), "inventory sequence")
    require(sum(int(r["size_bytes"]) for r in inv) == size, "group byte total")
    require(len({r["path_from_ingest_root"] for r in inv}) == count, "duplicate in group")
    for a, b in zip(scope, inv):
        rel = b["path_from_ingest_root"]
        require(a["path_from_ingest_root"] == rel and a["size_bytes"] == b["size_bytes"], f"scope differs: {rel}")
        data = source_path(rel).read_bytes()
        require(len(data) == int(b["size_bytes"]) and digest(data) == b["sha256"], f"source bytes differ: {rel}")


def verify_context(scope: list[dict[str, str]], inv: list[dict[str, str]]) -> None:
    require(len(scope) == len(inv) == 10, "context count")
    require(sum(int(r["size_bytes"]) for r in inv) == 159790, "context byte count")
    for n, (a, b) in enumerate(zip(scope, inv), 1):
        rel = b["path_from_ingest_root"]
        require(a["seq"] == b["seq"] == str(n), f"context sequence: {rel}")
        require(a["path_from_ingest_root"] == rel and a["size_bytes"] == b["size_bytes"], f"context scope: {rel}")
        data = source_path(rel).read_bytes()
        prefix = data[: int(b["size_bytes"])]
        require(len(prefix) == int(b["size_bytes"]) and digest(prefix) == b["sha256"], f"context prefix differs: {rel}")
        if rel.endswith("/05-verified-quotes-by-speaker.md"):
            require(len(data) == len(prefix), "r99 hash-locked 05 was modified")


def verify_anchors(anchors: list[dict[str, str]], sources: dict[str, dict[str, str]]) -> None:
    require(len(anchors) == 34 and len({r["id"] for r in anchors}) == 34, "anchor count/IDs")
    cache: dict[str, list[str]] = {}
    for r in anchors:
        rel = r["source_path_from_ingest_root"]
        require(rel in sources and r["source_sha256"] == sources[rel]["sha256"], f"anchor outside source: {r['id']}")
        if rel not in cache:
            cache[rel] = source_path(rel).read_text(encoding="utf-8", errors="replace").splitlines()
        line = int(r["line_1_based"])
        require(1 <= line <= len(cache[rel]), f"anchor line range: {r['id']}")
        require(r["exact_needle"] and r["exact_needle"] in cache[rel][line - 1], f"anchor token: {r['id']}")


def verify_manuals(manuals: list[dict[str, str]], sources: dict[str, dict[str, str]]) -> None:
    index = {r["seq"]: r for r in rows(I / "00-manifest/FILE-INDEX.csv")}
    require(len(manuals) == 10 and len({r["historic_index_seq"] for r in manuals}) == 10, "manual record count")
    by_seq = {r["historic_index_seq"]: r for r in manuals}
    for m in manuals:
        old = index[m["historic_index_seq"]]
        require(m["historic_original_path"] == old["path"], "manual original path")
        require(m["historic_original_bytes"] == old["bytes"] and m["historic_original_sha256"] == old["sha256"], "historic manual metadata")
        require(m["historic_extraction_method"] == old["method"], "manual historic method")
        rel = m["current_extraction_path_from_ingest_root"]
        require(rel == old["artifact_path"] and rel in sources, "manual source linkage")
        data = source_path(rel).read_bytes()
        require(len(data) == int(m["current_extraction_bytes"]) and digest(data) == m["current_extraction_sha256"], "manual extracted bytes")
        require(m["original_reobtained_this_round"] == "no", "unsupported original claim")
        if m["pdf_text_body_sha256_if_applicable"]:
            require(b"-->\n\n" in data, "PDF extraction header")
            require(b"PDF: pages=2" in data and b"Pages without text layer: 0/2" in data, "manual PDF text-layer page metadata")
            body = data.split(b"-->\n\n", 1)[1]
            require(digest(body) == m["pdf_text_body_sha256_if_applicable"], "PDF extracted-body hash")
    a, b = by_seq["49"], by_seq["151"]
    require(a["historic_original_bytes"] == b["historic_original_bytes"] == "599437", "manual original size pair")
    require(a["historic_original_sha256"] == b["historic_original_sha256"] == "b62601e199425ba687725a729d520165f00b63dd1cd03b6b3764694c16880e04", "manual historic hash pair")
    expected_body = "3a6c67372b9d463fa9ee379ad6aee055169b0bf5bfeed505e9835c46855b99ba"
    require(a["pdf_text_body_sha256_if_applicable"] == b["pdf_text_body_sha256_if_applicable"] == expected_body, "manual extracted-body pair")


def verify_protected(before: list[dict[str, str]], comp: list[dict[str, str]]) -> None:
    require(len(before) == len(comp) == 868, "entry inventory count")
    require(sum(int(r["size_bytes"]) for r in before) == 46015150, "entry inventory bytes")
    require(Counter(r["comparison_to_remote"] for r in comp) == {"same": 837, "different": 31}, "entry comparison counts")
    require(len({r["path_from_repo_root"] for r in comp}) == 868, "entry paths duplicate")
    saved = new = 0
    for a, b in zip(before, comp):
        require(a["path_from_repo_root"] == b["path_from_repo_root"] and a["size_bytes"] == b["bytes"], "entry scope mismatch")
        rel = Path(b["path_from_repo_root"])
        require(not rel.is_absolute() and ".." not in rel.parts, "unsafe entry path")
        if b["comparison_to_remote"] == "same":
            require(b["incoming_sha256"] == b["remote_sha256"], "same comparison hashes differ")
            require(not b["existing_protected_variant_path"], "same unexpectedly protected")
            continue
        require(b["incoming_sha256"] != b["remote_sha256"], "difference hash equal")
        if b["existing_protected_variant_path"]:
            backup = ROOT / b["existing_protected_variant_path"]
            saved += 1
        else:
            backup = P / "original-paths" / rel
            new += 1
        require(backup.is_file() and not backup.is_symlink() and backup.resolve().is_relative_to(ROOT.resolve()), f"missing preserved variant: {rel}")
        data = backup.read_bytes()
        require(len(data) == int(b["bytes"]) and digest(data) == b["incoming_sha256"], f"preserved variant bytes: {rel}")
    require((saved, new) == (28, 3), "preserved variant groups")


def verify_git_and_attributes(items: list[dict[str, str]]) -> None:
    paths = [(I / r["path_from_ingest_root"]).relative_to(ROOT).as_posix() for r in items]
    output = subprocess.check_output(["git", "ls-files", "-s", "-z", "--", *paths], cwd=ROOT)
    tracked: dict[str, str] = {}
    for item in output.split(b"\0"):
        if item:
            h, p = item.split(b"\t", 1)
            tracked[p.decode("utf-8")] = h.split()[1].decode("ascii")
    require(len(tracked) == len(paths) == 38, "source Git-index count")
    for p in paths:
        oid = subprocess.check_output(["git", "hash-object", "--no-filters", "--", p], cwd=ROOT).decode().strip()
        require(tracked[p] == oid, f"source Git blob differs: {p}")
    raw = subprocess.check_output(["git", "check-attr", "-z", "text", "--", *paths], cwd=ROOT).split(b"\0")
    triples = list(zip(*[iter(raw[:-1])] * 3))
    require(len(triples) == len(paths) and all(value == b"unset" for _, _, value in triples), "source -text attributes")


def verify_overlaps(items: list[dict[str, str]]) -> None:
    current = {r["path_from_ingest_root"] for r in items}
    groups = (
        ("15-source-evidence-r97-2026-10-26/local-first-second-inventory.csv", "representation_path", 4),
        ("18-source-evidence-r98-2026-10-26/local-order-dc-inventory.csv", "artifact_path", 9),
        ("22-source-evidence-r99-2026-10-26/scope-inventory.csv", "path_from_ingest_root", 6),
        ("22-source-evidence-r99-2026-10-26/context-partial-inventory.csv", "path_from_ingest_root", 8),
    )
    for file, key, expected in groups:
        previous = {r[key] for r in rows(I / file)}
        require(len(current & previous) == expected, f"overlap {file}")
    old = set()
    for group in ("selected", "rootfs-text", "supplement-wechat", "supplement-ocr"):
        old.update(r["path_from_ingest_root"] for r in rows(I / f"25-source-evidence-r100-2026-10-26/{group}-read-inventory.csv"))
    require(len(old) == 4903 and len(current & old) == 8, "r100 overlap")


def verify_links(context: list[dict[str, str]]) -> int:
    docs = [
        S / "README.md", P / "README.md", F / "README.md", F / "angora-networks.md",
        I / "31-audit-r101-2026-10-26.md",
        W / "08-customer-pipeline/170-angora-training-manual-nms-r101-2026-10-26.md",
        W / "09-orders/120-angora-orders-master-2026-10-21.mapping-r101.md",
        W / "01-knowledge-base/05-verified-quotes-by-speaker.mapping-r101.md",
    ]
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
            require(path.is_relative_to(ROOT.resolve()) and path.exists(), f"broken local link in {origin}: {raw}")
            count += 1
    require({p.name for p in F.glob("*.md")} == {"README.md", "angora-networks.md"}, "follow-up customer scope")
    return count


def reject(fn, *args) -> None:
    try:
        fn(*args)
    except (AssertionError, KeyError, IndexError, ValueError):
        return
    raise AssertionError(f"negative test was accepted: {fn.__name__}")


def main() -> int:
    all_items = []
    for scope_file, read_file, count, size in GROUPS:
        a, b = rows(S / scope_file), rows(S / read_file)
        verify_group(a, b, count, size)
        all_items.extend(b)
    require(len(all_items) == len({r["path_from_ingest_root"] for r in all_items}) == 38, "global source count")
    require(sum(int(r["size_bytes"]) for r in all_items) == 16186782, "global source bytes")
    sources = {r["path_from_ingest_root"]: r for r in all_items}
    print("PASS Inventory: 38/38 existing derivative paths, 16,186,782 bytes and SHA-256; scope matches each recorded group")

    context_scope, context = rows(S / "context-before-read.csv"), rows(S / "context-prefix-read-inventory.csv")
    verify_context(context_scope, context)
    print("PASS Context: 10/10 prior-file prefixes, 159,790 bytes; hashed 05 source remains unchanged")

    anchors, manuals = rows(S / "evidence-traceability.csv"), rows(S / "manual-history-crossrefs.csv")
    verify_anchors(anchors, sources)
    verify_manuals(manuals, sources)
    require(150 / 24 == 6.25, "illustrative CCTV arithmetic")
    print("PASS Traceability: 34 exact line anchors; 10 historical paths and four 2-page PDF extracts; illustrative 150/24 arithmetic")

    entry_before, entry_comp = rows(P / "entry-scope-before-comparison.csv"), rows(P / "entry-comparison.csv")
    verify_protected(entry_before, entry_comp)
    print("PASS Protected: 868 entry paths: 837 same, 31 differing; all 28 existing and 3 new variant copies match")

    verify_git_and_attributes(all_items)
    verify_overlaps(all_items)
    print("PASS Git/overlap: 38/38 selected local Git blobs match and -text; r97/r98/r99-full/r99-partial/r100 overlaps 4/9/6/8/8")

    n = verify_links(context)
    print(f"PASS Links: {n} local links in r101 deliverables and appended corrections; one internal customer follow-up")

    first_scope = rows(S / GROUPS[0][0])
    first_inv = rows(S / GROUPS[0][1])
    mutated = copy.deepcopy(first_inv)
    mutated[0]["sha256"] = "0" * 64
    reject(verify_group, first_scope, mutated, 19, 1872079)
    mutated = copy.deepcopy(first_scope)
    mutated[0]["path_from_ingest_root"] += ".wrong"
    reject(verify_group, mutated, first_inv, 19, 1872079)
    mutated = copy.deepcopy(anchors)
    mutated[0]["exact_needle"] = "__NOT_IN_SOURCE__"
    reject(verify_anchors, mutated, sources)
    mutated = copy.deepcopy(context)
    mutated[0]["sha256"] = "0" * 64
    reject(verify_context, context_scope, mutated)
    mutated = copy.deepcopy(manuals)
    mutated[0]["historic_original_sha256"] = "0" * 64
    reject(verify_manuals, mutated, sources)
    mutated = copy.deepcopy(entry_comp)
    next(r for r in mutated if r["comparison_to_remote"] == "different")["incoming_sha256"] = "0" * 64
    reject(verify_protected, entry_before, mutated)
    print("PASS Negative: six in-memory changes to source hash, scope, anchor, context, historic index and preserved variant rejected")
    print("Boundary: local derivative bytes/selected strings only; not original authenticity, screenshot speaker certainty, transfer, deployment, repair, training or acceptance.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, OSError, subprocess.CalledProcessError, KeyError, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
