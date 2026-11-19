#!/usr/bin/env python3
"""Verify r103 bounded local records, not PDF originals or product compatibility.

Only local hashes, append-only prefixes and selected non-secret strings are
checked. Old verification tools are never executed, archives are not opened,
and mutation tests are performed in memory only.
"""
from __future__ import annotations

import copy
import csv
import hashlib
import re
import subprocess
import sys
from collections import Counter
from decimal import Decimal
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
I = ROOT / "ingest/angora-1__arena-01a0ce39__5acb613"
W = I / "01-text-verbatim/workstation"
P = I / "36-entry-safety-r103-2026-10-26"
S = I / "37-source-evidence-r103-2026-10-26"
F = I / "38-followup-angora-r103-2026-10-26"
REGISTRY = "02-extracted/mac_address&serial_number.xlsx.extracted.md"


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise AssertionError(msg)


def rows(p: Path) -> list[dict[str, str]]:
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def digest(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def file_under(root: Path, rel: str) -> Path:
    r = Path(rel)
    require(not r.is_absolute() and ".." not in r.parts, "unsafe relative path")
    p = root / r
    require(p.is_file() and not p.is_symlink() and p.resolve().is_relative_to(root.resolve()), f"missing/unsafe: {rel}")
    return p


def verify_group(scope: list[dict[str, str]], inv: list[dict[str, str]], count: int, size: int,
                 root: Path = I, pathkey: str = "path_from_ingest_root", prefix: bool = False) -> None:
    require(len(scope) == len(inv) == count and sum(int(x["size_bytes"]) for x in inv) == size, "scope count/size")
    require(len({r[pathkey] for r in inv}) == count, "duplicate source path")
    for n, (a, b) in enumerate(zip(scope, inv), 1):
        rel = b[pathkey]
        require(a["seq"] == b["seq"] == str(n), f"sequence: {rel}")
        require(a[pathkey] == rel and a["size_bytes"] == b["size_bytes"], f"scope mismatch: {rel}")
        if "representation" in a:
            require(a["representation"] == b["representation"], f"source kind: {rel}")
        data = file_under(root, rel).read_bytes()
        if prefix:
            data = data[:int(b["size_bytes"])]
        require(len(data) == int(b["size_bytes"]) and digest(data) == b["sha256"], f"bytes/prefix: {rel}")


def verify_candidate(candidate: list[dict[str, str]]) -> None:
    require(len(candidate) == len({r["path_from_ingest_root"] for r in candidate}) == 66, "candidate metadata count")
    require(sum(int(r["size_bytes"]) for r in candidate) == 969202, "candidate metadata sizes")
    for n, r in enumerate(candidate, 1):
        require(r["seq"] == str(n), "candidate sequence")
        # Metadata only: do not open, parse or analyze unselected candidate files.
        require(file_under(I, r["path_from_ingest_root"]).stat().st_size == int(r["size_bytes"]), "candidate size")


def verify_web(scope: list[dict[str, str]], inv: list[dict[str, str]]) -> None:
    require(len(scope) == len(inv) == 3 and sum(int(r["artifact_size_bytes"]) for r in inv) == 18498, "web artifact count/size")
    require([r["returned_chunks_saved"] for r in inv] == ["1/1", "1/1", "2/2"], "web chunk count")
    for n, (a, b) in enumerate(zip(scope, inv), 1):
        require(a["seq"] == b["seq"] == str(n) and a["url"] == b["url"], "web URL/sequence")
        rel = b["artifact_path_from_ingest_root"]
        require((I / rel) == (S / a["planned_path_from_r103_source_dir"]), "web planned path")
        data = file_under(I, rel).read_bytes()
        require(len(data) == int(b["artifact_size_bytes"]) and digest(data) == b["artifact_sha256"], "web artifact bytes")
    last = file_under(I, inv[-1]["artifact_path_from_ingest_root"]).read_text(encoding="utf-8")
    require("Dimensions (H x W x D): 10.8 x 13.7 x 5\n<!-- End chunk 0; start chunk 1." in last, "web gap boundary")
    require("-->\night: 70 grams" in last and "Apparent missing characters" in last, "web gap disclosed")


def verify_anchors(anchors: list[dict[str, str]], hashes: dict[str, str]) -> None:
    require(len(anchors) == len({r["id"] for r in anchors}) == 21, "anchor count")
    cache: dict[str, list[str]] = {}
    for r in anchors:
        rel = r["source_path_from_ingest_root"]
        require(rel in hashes and r["source_sha256_at_read"] == hashes[rel], f"anchor source: {r['id']}")
        if rel not in cache:
            cache[rel] = file_under(I, rel).read_text(encoding="utf-8").splitlines()
        n = int(r["line_1_based"])
        require(1 <= n <= len(cache[rel]) and r["exact_needle"] and r["exact_needle"] in cache[rel][n - 1], f"anchor token: {r['id']}")


def verify_assets(assets: list[dict[str, str]], sources: dict[str, dict[str, str]]) -> None:
    idx = {r["seq"]: r for r in rows(I / "00-manifest/FILE-INDEX.csv")}
    require(len(assets) == len({r["historical_index_seq"] for r in assets}) == 8, "asset count")
    for a in assets:
        old = idx[a["historical_index_seq"]]
        require(a["historical_original_path"] == old["path"] and a["historical_original_bytes"] == old["bytes"], "asset historical path/size")
        require(a["historical_original_sha256"] == old["sha256"] and a["historical_extraction_method"] == old["method"], "asset history hash/method")
        rel = a["current_representation_path_from_ingest_root"]
        require(rel == old["artifact_path"] and rel in sources and a["original_reobtained_this_round"] == "no", "asset source linkage")
        data = file_under(I, rel).read_bytes()
        require(len(data) == int(a["current_representation_bytes"]) and digest(data) == a["current_representation_sha256"] == sources[rel]["sha256"], "asset derivative bytes")
    pair = {a["historical_index_seq"]: a for a in assets}
    require(pair["49"]["historical_original_sha256"] == pair["151"]["historical_original_sha256"], "historic manual hash pair")
    require(pair["244"]["historical_original_sha256"] != pair["246"]["historical_original_sha256"], "drawing originals are distinct indexed files")


def body(path: str, method: str, side: str) -> bytes:
    data = file_under(I, path).read_bytes()
    if method == "1g":
        return data[data.index(b"\n\nA\n"):]
    if method == "100g":
        return data[data.index(b"## Angora Networks\n"):]
    if method == "manual":
        return data.split(b"-->\n\n", 1)[1]
    if method == "drawing":
        marker = b"## PAGE 1\n" if side == "a" else b"## PAGE 1/1\n"
        value = data.split(marker, 1)[1]
        if side == "b":
            value = value.split(b"\nPages without text layer:", 1)[0]
        return value.decode("utf-8").strip().encode("utf-8")
    raise AssertionError("unknown body method")


def verify_bodies(pairs: list[dict[str, str]], sources: dict[str, dict[str, str]]) -> None:
    sizes = {"1G10G-normalized-reuse": 6250, "100G-normalized-reuse": 8267, "industrial-manual-body": 6076, "sixth-drawing-text": 225}
    require(len(pairs) == 4 and {p["pair_id"] for p in pairs} == set(sizes), "body pair IDs")
    for p in pairs:
        a, b, method = p["left_path_from_ingest_root"], p["right_path_from_ingest_root"], p["comparison_method"]
        require(a in sources and b in sources and a != b, "body source paths")
        x, y = body(a, method, "a"), body(b, method, "b")
        require(x == y and len(x) == sizes[p["pair_id"]] == int(p["left_body_bytes"]) == int(p["right_body_bytes"]), "body bytes")
        require(digest(x) == p["left_body_sha256"] == p["right_body_sha256"] and p["bodies_identical"] == "yes", "body hashes")


def verify_registry(records: list[dict[str, str]], sources: dict[str, dict[str, str]]) -> None:
    require(REGISTRY in sources and len(records) == 16, "registry source/count")
    data = file_under(I, REGISTRY).read_bytes()
    lines = data.decode("utf-8").splitlines()
    selected = [(n, line) for n, line in enumerate(lines, 1) if "TT-2208-PG" in line]
    require(len(selected) == len(records) == 16, "registry target rows")
    counts: Counter[str] = Counter()
    macs, serials = set(), set()
    for record, (n, line) in zip(records, selected):
        cols = line.split("\t")
        require(len(cols) == 4 and re.fullmatch(r"(?i)(?:[0-9a-f]{2}:){5}[0-9a-f]{2}", cols[0]) is not None, "registry row schema")
        require(record["source_path_from_ingest_root"] == REGISTRY and record["source_sha256"] == sources[REGISTRY]["sha256"] == digest(data), "registry source hash")
        require(record["line_1_based"] == str(n) and record["document_order_id"] == cols[2] and record["model_substring"] == "TT-2208-PG", "registry line/order/model")
        require(record["row_text_sha256"] == digest(line.encode("utf-8")) and record["mac_field"] == record["serial_field"] == "present", "registry row hash")
        require(bool(cols[1]), "missing serial field")
        if cols[2] == "STSC20250711007":
            require("angora" not in line.casefold(), "second group row directly identifies Angora")
        counts[cols[2]] += 1
        macs.add(cols[0].upper()); serials.add(cols[1])
    require(counts == {"STSC20250619007": 6, "STSC20250711007": 10} and len(macs) == len(serials) == 16, "registry group/distinctness")


def verify_cases(cases: list[dict[str, str]], anchors: list[dict[str, str]]) -> None:
    require(len(cases) == len({x["case_id"] for x in cases}) == 6, "case count")
    ids = {x["id"] for x in anchors}
    for case in cases:
        require(set(case["anchor_ids"].split(";")) <= ids and case["observation"] and case["interpretation_limit"], "case anchor/limits")
    one_m_in_ft = Decimal(1) / Decimal("0.3048")
    require(abs(one_m_in_ft - Decimal("3.28084")) < Decimal("0.00001") and abs(one_m_in_ft - Decimal(6)) > 2, "length arithmetic")


def verify_entry(scope: list[dict[str, str]], comp: list[dict[str, str]]) -> None:
    require(len(scope) == len(comp) == 868 and sum(int(r["size_bytes"]) for r in scope) == 46015150, "entry count/size")
    require(Counter(r["comparison_to_remote"] for r in comp) == {"same": 837, "different": 31}, "entry status")
    require(len({r["path_from_repo_root"] for r in comp}) == 868, "entry duplicate")
    groups: Counter[str] = Counter()
    for n, (a, b) in enumerate(zip(scope, comp), 1):
        require(a["seq"] == b["seq"] == str(n) and a["path_from_repo_root"] == b["path_from_repo_root"] and a["size_bytes"] == b["bytes"], "entry scope")
        require(not b["new_protected_variant_path"], "unexpected new backup")
        if b["comparison_to_remote"] == "same":
            require(b["incoming_sha256"] == b["remote_sha256"] and not b["existing_protected_variant_path"], "same entry")
        else:
            rel = b["existing_protected_variant_path"]
            data = file_under(ROOT, rel).read_bytes()
            require(len(data) == int(b["bytes"]) and digest(data) == b["incoming_sha256"] and b["incoming_sha256"] != b["remote_sha256"], "protected copy")
            groups["r97" if "/14-protected-" in rel else "r99" if "/21-protected-" in rel else "r101" if "/28-protected-" in rel else "other"] += 1
    require(groups == {"r97": 27, "r99": 1, "r101": 3}, "protected groups")


def verify_overlap(local: list[dict[str, str]], overlaps: list[dict[str, str]]) -> None:
    olddir = I / "33-source-evidence-r102-2026-10-26"
    old = set()
    for name in ("read-inventory.csv", "supplement-ocr-read-inventory.csv", "supplement-certificate-read-inventory.csv", "supplement-ieee-read-inventory.csv"):
        old.update(r["path_from_ingest_root"] for r in rows(olddir / name))
    current = {r["path_from_ingest_root"] for r in local}
    require(len(old) == 29 and len(current) == len(overlaps) == 16 and len(old & current) == 7, "overlap counts")
    for a, b in zip(local, overlaps):
        rel = a["path_from_ingest_root"]
        require(b["path_from_ingest_root"] == rel and b["sha256"] == a["sha256"] and b["r102_source_path"] == ("yes" if rel in old else "no"), "overlap row")


def verify_git(local: list[dict[str, str]]) -> None:
    paths = [(I / r["path_from_ingest_root"]).relative_to(ROOT).as_posix() for r in local]
    index = {}
    for item in subprocess.check_output(["git", "ls-files", "-s", "-z", "--", *paths], cwd=ROOT).split(b"\0"):
        if item:
            m, p = item.split(b"\t", 1); index[p.decode("utf-8")] = m.split()[1].decode("ascii")
    require(len(paths) == 16 and set(index) == set(paths), "Git source index")
    for p in paths:
        oid = subprocess.check_output(["git", "hash-object", "--no-filters", "--", p], cwd=ROOT).decode().strip()
        require(oid == index[p], f"Git source blob: {p}")
    raw = subprocess.check_output(["git", "check-attr", "-z", "text", "--", *paths], cwd=ROOT).split(b"\0")
    triples = list(zip(*[iter(raw[:-1])] * 3))
    require(len(triples) == 16 and all(v == b"unset" for _, _, v in triples), "source -text")


def verify_links(context: list[dict[str, str]], guides: list[dict[str, str]]) -> int:
    docs = [P / "README.md", S / "README.md", F / "README.md", F / "angora-networks.md", I / "39-audit-r103-2026-10-26.md",
            W / "08-customer-pipeline/172-angora-optics-port-evidence-r103-2026-10-26.md", W / "09-orders/120-angora-orders-master-2026-10-21.mapping-r103.md"]
    texts = [(p, p.read_text(encoding="utf-8")) for p in docs]
    for r in context + guides:
        p = file_under(I, r["path_from_ingest_root"])
        tail = p.read_bytes()[int(r["size_bytes"]):].decode("utf-8")
        if tail:
            texts.append((p, tail))
    count = 0
    for origin, text in texts:
        for raw in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
            target = urlsplit(raw)
            if target.scheme or target.netloc or not target.path:
                continue
            p = (origin.parent / unquote(target.path)).resolve()
            require(p.is_relative_to(ROOT.resolve()) and p.exists(), f"missing link in {origin}: {raw}")
            count += 1
    require({p.name for p in F.glob("*.md")} == {"README.md", "angora-networks.md"}, "follow-up scope")
    for p in docs:
        text = p.read_text(encoding="utf-8")
        require(not re.search(r"(?i)(?:username|password)\s*[:=]|192\.168\.\d+\.\d+", text), f"credential-like field in {p}")
    return count


def reject(fn, *args) -> None:
    try:
        fn(*args)
    except (AssertionError, KeyError, IndexError, ValueError):
        return
    raise AssertionError(f"negative test accepted: {fn.__name__}")


def main() -> int:
    first_scope, first = rows(S / "source-scope-before-read.csv"), rows(S / "source-read-inventory.csv")
    second_scope, second = rows(S / "supplement-scope-before-read.csv"), rows(S / "supplement-read-inventory.csv")
    verify_group(first_scope, first, 14, 335008)
    verify_group(second_scope, second, 2, 84593)
    local = first + second
    require(len({r["path_from_ingest_root"] for r in local}) == 16, "local source uniqueness")
    sources = {r["path_from_ingest_root"]: r for r in local}
    verify_candidate(rows(S / "candidate-paths-metadata.csv"))
    print("PASS Local: 16/16 derivative paths, 419,601 bytes and SHA-256; 66 candidate records metadata only")

    guide_scope, guides = rows(S / "guide-scope-before-read.csv"), rows(S / "guide-read-inventory.csv")
    verify_group(guide_scope, guides, 2, 19722, prefix=True)
    c1s, c1 = rows(S / "context-scope-before-read.csv"), rows(S / "context-prefix-read-inventory.csv")
    c2s, c2 = rows(S / "supplement-context-scope-before-read.csv"), rows(S / "supplement-context-prefix-read-inventory.csv")
    verify_group(c1s, c1, 7, 129230, prefix=True)
    verify_group(c2s, c2, 2, 67156, prefix=True)
    before_checks, checks = rows(S / "protection-check-inputs-before-read.csv"), rows(S / "protection-check-read-inventory.csv")
    verify_group(before_checks, checks, 31, 1489548, root=ROOT, pathkey="path_from_repo_root")
    print("PASS Context: 2/2 guide prefixes; 9/9 background prefixes; 31/31 protection-check hashes")

    webscope, web = rows(S / "web-scope-before-fetch.csv"), rows(S / "web-visible-inventory.csv")
    verify_web(webscope, web)
    hashes = {r["path_from_ingest_root"]: r["sha256"] for r in local + guides}
    hashes.update({r["artifact_path_from_ingest_root"]: r["artifact_sha256"] for r in web})
    anchors, assets = rows(S / "evidence-traceability.csv"), rows(S / "local-asset-crossrefs.csv")
    registry, pairs, cases = rows(S / "tt-model-registry-row-index.csv"), rows(S / "extracted-body-identity.csv"), rows(S / "optics-conflict-cases.csv")
    verify_anchors(anchors, hashes); verify_assets(assets, sources); verify_registry(registry, sources); verify_bodies(pairs, sources); verify_cases(cases, anchors)
    print("PASS Evidence: 3 URL artifacts, 4 returned chunks with one disclosed gap; 21 anchors, 8 assets, 16 registry rows, 4 body pairs, 6 cases")

    es, entry = rows(P / "entry-scope-before-comparison.csv"), rows(P / "entry-comparison.csv")
    verify_entry(es, entry); verify_overlap(local, rows(S / "overlap-r102-by-path.csv")); verify_git(local)
    print("PASS Preservation: 868 entry paths, 31/31 protected variants, 7 r102 overlaps; 16/16 Git blobs and -text")
    print(f"PASS Links: {verify_links(c1 + c2, guides)} local links; one internal customer record; no login fields copied to deliverable documents")

    changed = copy.deepcopy(first); changed[0]["sha256"] = "0" * 64; reject(verify_group, first_scope, changed, 14, 335008)
    changed = copy.deepcopy(first_scope); changed[0]["path_from_ingest_root"] += ".bad"; reject(verify_group, changed, first, 14, 335008)
    changed = copy.deepcopy(c1); changed[0]["sha256"] = "0" * 64; reject(verify_group, c1s, changed, 7, 129230, I, "path_from_ingest_root", True)
    changed = copy.deepcopy(web); changed[0]["artifact_sha256"] = "0" * 64; reject(verify_web, webscope, changed)
    changed = copy.deepcopy(anchors); changed[0]["exact_needle"] = "__NOT_PRESENT__"; reject(verify_anchors, changed, hashes)
    changed = copy.deepcopy(assets); changed[0]["historical_original_sha256"] = "0" * 64; reject(verify_assets, changed, sources)
    changed = copy.deepcopy(registry); changed[0]["row_text_sha256"] = "0" * 64; reject(verify_registry, changed, sources)
    changed = copy.deepcopy(pairs); changed[0]["left_body_sha256"] = "0" * 64; reject(verify_bodies, changed, sources)
    changed = copy.deepcopy(entry); next(r for r in changed if r["comparison_to_remote"] == "different")["incoming_sha256"] = "0" * 64; reject(verify_entry, es, changed)
    changed = copy.deepcopy(rows(S / "overlap-r102-by-path.csv")); changed[0]["r102_source_path"] = "invalid"; reject(verify_overlap, local, changed)
    changed = copy.deepcopy(cases); changed[0]["anchor_ids"] = "missing-anchor"; reject(verify_cases, changed, anchors)
    print("PASS Negative: 11 in-memory corruptions of scopes, hashes, context, web, anchors, assets, registry, bodies, preservation, overlap and case references rejected")
    print("Boundary: normalized visible text and local indexes only; no original PDF authenticity, device compatibility, customer identity, delivery or acceptance claim.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AssertionError, OSError, subprocess.CalledProcessError, KeyError, ValueError, IndexError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
