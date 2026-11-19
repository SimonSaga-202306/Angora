#!/usr/bin/env python3
"""Verify r112 local evidence, raw sample blobs, and protected history.

Checks are local consistency checks, not proof of web transcription fidelity,
current vendor support, device behavior, certification, or deployment. A local
stash is checked only when its object exists; it is not a portable backup.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

from verify_r111 import AuditError, checked_path, git_tree, require, sha256, strict_csv, verify_anchor, verify_file, verify_join, verify_prefix

ROOT = Path(__file__).resolve().parents[1]
INGEST = Path("ingest/angora-1__arena-01a0ce39__5acb613")
R = ROOT / INGEST / "73-source-evidence-r112-2026-10-26"
ENTRY = ROOT / INGEST / "72-entry-safety-r112-2026-10-26"
WORK = ROOT / INGEST / "01-text-verbatim/workstation"
MANIFEST = R / "output-manifest-before-stage.csv"


def rows(name: str) -> list[dict[str, str]]:
    return strict_csv(R / name)


def verify_git_blob(data: bytes, expected_size: int, expected_oid: str) -> None:
    require(len(data) == expected_size, "Git blob size mismatch")
    oid = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
    require(oid == expected_oid, "Git blob object ID mismatch")


def directory_signature(items: list[dict]) -> set[tuple[str, str, int, str]]:
    values = set()
    for item in items:
        path, oid, size, kind = item["path"], item["sha"], item["size"], item["type"]
        require(kind == "file" and path.startswith("freeRadiusConfigs/"), "unexpected directory entry")
        require(".." not in Path(path).parts and len(oid) == 40 and isinstance(size, int), "invalid directory entry")
        values.add((path, oid, size, kind))
    require(len(values) == len(items), "duplicate directory entry")
    return values


def verify_directory_equivalence(first: list[dict], second: list[dict]) -> None:
    require(directory_signature(first) == directory_signature(second), "directory snapshots differ")


def require_complete_consistent_chunks(records: list[dict]) -> None:
    require(bool(records), "no chunk metadata")
    totals = {int(r["total_chunks"]) for r in records}
    titles = {r["title"] for r in records}
    require(len(totals) == len(titles) == 1, "chunk metadata identity or total drift")
    total = next(iter(totals))
    require([int(r["chunk_index"]) for r in records] == list(range(total)), "chunk sequence incomplete")
    require(all(r["has_more"] for r in records[:-1]) and not records[-1]["has_more"], "chunk termination inconsistent")


def parse_cdx(text: str) -> list[list[str]]:
    lines = text.splitlines()
    require(len(lines) >= 3 and lines[0] == "```json" and lines[-1] == "```", "CDX wrapper mismatch")
    try:
        data = json.loads("\n".join(lines[1:-1]))
    except json.JSONDecodeError as exc:
        raise AuditError("invalid CDX JSON") from exc
    require(isinstance(data, list), "CDX payload is not an array")
    if data:
        require(data[0] == ["timestamp", "original", "statuscode", "digest", "length"], "CDX header mismatch")
        require(all(len(row) == 5 and row[2] == "200" for row in data[1:]), "unexpected CDX record")
        return data[1:]
    return []


def check_inventories() -> dict[str, object]:
    specs = [
        ("prior-round-read-inventory.csv", ["prior-round-scope-before-read.csv"], 9, 60019),
        ("comparison-source-read-inventory.csv", ["comparison-source-scope-before-read.csv"], 6, 53706),
        ("prior-provenance-read-inventory.csv", ["prior-provenance-scope-before-read.csv"], 3, 16355),
        ("prior-gh-read-inventory.csv", ["prior-gh-scope-before-read.csv"], 2, 667),
        ("archive-index-read-inventory.csv", ["archive-index-read-scope-before-file-read.csv"], 4, 470),
        ("archive-index-extension-read-inventory.csv", ["archive-index-extension-read-scope-before-file-read.csv"], 2, 418),
        ("github-api-read-inventory.csv", ["github-api-read-scope-before-file-reread.csv", "github-ref-read-scope-before-file-reread.csv", "github-commit-read-scope-before-file-reread.csv"], 5, 22444),
        ("github-org-read-inventory.csv", ["github-org-read-scope-before-file-reread.csv"], 1, 5332),
        ("github-files-read-inventory.csv", ["github-files-read-scope-before-reread.csv"], 7, 91709),
        ("new-source-read-inventory.csv", ["new-source-read-scope-before-consolidated-read.csv"], 6, 38984),
        ("diagnostic-read-inventory.csv", ["diagnostic-read-scope-before-consolidated-read.csv"], 9, 39771),
        ("successful-chunk-read-inventory.csv", ["successful-chunk-read-scope-after-assembly.csv"], 4, 25840),
    ]
    all_rows = []
    groups = {}
    for inv_name, scope_names, expected_count, expected_bytes in specs:
        entries = rows(inv_name)
        scope = [x for name in scope_names for x in rows(name)]
        expected_paths = {x["repository_relative_path"] for x in scope}
        actual_paths = {x["repository_relative_path"] for x in entries}
        require(len(entries) == len(actual_paths) == expected_count, f"duplicate/count mismatch: {inv_name}")
        require(expected_paths == actual_paths, f"read scope differs: {inv_name}")
        total = 0
        for entry in entries:
            total += len(verify_file(checked_path(ROOT, entry["repository_relative_path"]),
                                     int(entry["bytes_read"]), entry["sha256"]))
        require(total == expected_bytes, f"byte total mismatch: {inv_name}")
        groups[inv_name] = {"paths": len(entries), "bytes": total}
        all_rows.extend(entries)
    paths = [r["repository_relative_path"] for r in all_rows]
    require(len(paths) == len(set(paths)) == 58, "58-path inventory has duplicates")
    require(sum(int(x["bytes_read"]) for x in all_rows) == 355715, "read total mismatch")
    return {"paths": len(paths), "bytes": 355715, "groups": groups, "path_set": set(paths)}


def check_catalog_anchors() -> dict[str, int]:
    catalog = rows("source-catalog.csv")
    by_id = {r["source_id"]: r for r in catalog}
    require(len(catalog) == len(by_id) == 41, "catalog ID count mismatch")
    for r in catalog:
        verify_file(checked_path(ROOT, r["repository_relative_path"]), int(r["bytes_read"]), r["sha256"])
    anchors = rows("evidence-traceability.csv")
    ids = {a["anchor_id"] for a in anchors}
    require(len(anchors) == len(ids) == 43, "anchor count mismatch")
    excluded = {"X01", "X02", "X03", "X04", "X05", "P01"}
    for a in anchors:
        sid = a["source_id"]
        require(sid in by_id and sid not in excluded, f"anchor uses excluded source: {sid}")
        source = by_id[sid]
        require(a["repository_relative_path"] == source["repository_relative_path"] and
                a["local_sha256"] == source["sha256"], "anchor source identity/hash mismatch")
        text = checked_path(ROOT, a["repository_relative_path"]).read_text(encoding="utf-8")
        verify_anchor(text, int(a["line_start"]), int(a["line_end"]), a["exact_fragment"])
    for name, count in [("claim-boundaries.csv", 18), ("issues-and-corrections.csv", 11)]:
        records = rows(name)
        require(len(records) == count, f"unexpected count: {name}")
        for record in records:
            for aid in filter(None, record["anchors"].split(";")):
                require(aid in ids, f"unknown anchor {aid} in {name}")
    require("excluded" in by_id["P01"]["limitations"], "P01 must be excluded from conclusions")
    return {"catalog_entries": len(catalog), "local_anchors": len(anchors), "boundaries": 18, "corrections": 11}


def check_search_and_cdx() -> dict[str, object]:
    for path in R.rglob("*.csv"):
        strict_csv(path)
    plans = rows("discovery-plan-before-search.csv") + rows("bug-followup-search-plan-before-search.csv")
    expected = [f"Q{i:02d}" for i in range(1, 23)]
    require([r["query_id"] for r in plans] == expected, "Q01–Q22 plans differ")
    result_count, empty = 0, []
    for qid in expected:
        found = strict_csv(R / "search-discovery" / f"{qid}.csv")
        require(found and all(r["query_id"] == qid for r in found), f"bad query record: {qid}")
        positions = [int(r["result_position"]) for r in found]
        if positions == [0]:
            empty.append(qid)
        else:
            require(positions == list(range(1, len(positions) + 1)), f"bad positions: {qid}")
            result_count += len(positions)
    require(result_count == 67 and empty == ["Q06", "Q18", "Q21"], "search counts differ")
    indexes = rows("archive-index-plan-before-fetch.csv") + rows("archive-index-extension-plan-before-fetch.csv")
    results = {}
    for entry in indexes:
        require("to=20261026" in entry["index_url"], "archive cutoff not recorded")
        result = parse_cdx((R / entry["planned_path"]).read_text(encoding="utf-8"))
        require(all(row[1] == entry["original_url"] for row in result), "CDX original URL differs")
        results[entry["index_id"]] = result
    require(set(results) == {f"A{i:02d}" for i in range(1, 7)}, "CDX identifiers differ")
    require(sum(len(x) for x in results.values()) == 4, "CDX record count differs")
    for entry in rows("archive-replay-plan-before-fetch.csv") + rows("archive-replay-extension-plan-before-fetch.csv"):
        require(any(x[0] == entry["capture"] for x in results[entry["index_id"]]), "replay missing from CDX")
    return {"query_count": len(expected), "nonempty_result_rows": result_count, "zero_queries": empty,
            "cdx_requests": len(results), "filtered_cdx_records": 4}


def check_github() -> dict[str, object]:
    directory = json.loads((R / "github-api/G02-freeradius-directory.json").read_text(encoding="utf-8"))
    pinned = json.loads((R / "github-api/G04-pinned-directory.json").read_text(encoding="utf-8"))
    ref = json.loads((R / "github-api/G03-linked-ref.json").read_text(encoding="utf-8"))
    commit = json.loads((R / "github-api/G05-pinned-commit.json").read_text(encoding="utf-8"))
    org = json.loads((R / "github-api/G06-organization-repositories.json").read_text(encoding="utf-8"))
    verify_directory_equivalence(directory, pinned)
    require(len(directory) == 7, "example directory count differs")
    commit_id = "7876ce42bafac38ada3c5ccca7df861ed33b63e9"
    require(ref["object"]["sha"] == commit["sha"] == commit_id, "pinned commit mismatch")
    require(isinstance(org, list) and len(org) == 1 and org[0]["full_name"] == "anwHub/3rdPartyConfigs", "org result differs")
    scope = rows("github-files-scope-before-fetch.csv")
    inv = rows("github-files-read-inventory.csv")
    by_path = {x["path"]: x for x in pinned}
    require(len(scope) == len(inv) == len(by_path) == 7, "Git blob scope count differs")
    require({x["github_original_path"] for x in scope} == set(by_path), "Git blob scope paths differ")
    by_id = {x["source_id"]: x for x in inv}
    for item in scope:
        a = by_path[item["github_original_path"]]
        entry = by_id[item["source_id"]]
        require(a["sha"] == item["git_blob_sha1_from_directory"] == entry["git_blob_sha1"], "Git blob ID metadata differs")
        require(a["size"] == int(item["expected_bytes"]) == int(entry["bytes_read"]), "Git blob size metadata differs")
        data = checked_path(ROOT, entry["repository_relative_path"]).read_bytes()
        verify_git_blob(data, a["size"], a["sha"])
    return {"example_files": 7, "example_bytes": 91709, "git_blob_matches": 7,
            "pinned_commit": commit_id, "current_vs_pinned_directory": "7/7 path, size, and blob match",
            "limitation": "public sample text and current ref do not prove archive-time branch state or execution"}


def check_chunks_and_failures() -> dict[str, object]:
    for sid, plan_name, assembly_name in [("X06", "X06-chunk-plan-after-first-result.csv", "X06-assembly-result.json"),
                                          ("AR01", "AR01-chunk-plan-after-first-result.csv", "AR01-assembly-result.json")]:
        plan = rows(plan_name)
        require([int(x["chunk_index"]) for x in plan] == [0, 1], f"{sid} chunk plan differs")
        parts = [(R / x["planned_chunk_path"]).read_bytes() for x in plan]
        merged = (R / plan[0]["planned_combined_path"]).read_bytes()
        verify_join(parts, merged)
        info = json.loads((R / assembly_name).read_text(encoding="utf-8"))
        require(info["tool_chunks_returned"] == 2 and not info["final_has_more"] and info["sha256"] == sha256(merged),
                f"{sid} assembly metadata differs")
        if sid == "X06":
            require(parts[0].endswith("oluşturabilmeni".encode()) and parts[1].startswith(b"zi ve"), "X06 boundary")
        else:
            require(parts[0].endswith(b"802-1x-port-based-authentication-") and parts[1].startswith(b"using-freeradius#)"), "AR01 boundary")
    drift = rows("video-drift-metadata.csv")
    first = [r for r in drift if r["source_id"] == "X01"]
    second = [r for r in drift if r["source_id"] == "X02"]
    require([int(r["total_chunks"]) for r in first] == [171, 5] and
            [int(r["total_chunks"]) for r in second] == [3, 3, 4], "video drift metadata differs")
    require(not (R / "external-visible/www.youtube.com/watch/z0loF632E2s/index.visible.md").exists(), "X01 must remain unassembled")
    require(not (R / "external-visible/www.youtube.com/watch/C43VQBJtdrk/index.visible.md").exists(), "X02 must remain unassembled")
    for sid in ["X03", "X04", "X05"]:
        text = (R / f"fetch-failures/{sid}.visible.md").read_text(encoding="utf-8")
        require("Error 522" in text, f"{sid} not recognized as error")
    return {"successful_multichunk_assemblies": 2, "video_sources_quarantined": 2, "live_522_errors": 3}


def check_safety() -> dict[str, object]:
    plan = rows("safety-metadata-scope-before-recheck.csv")
    inv = rows("safety-metadata-read-inventory.csv")
    require(len(plan) == len(inv) == 3 and {x["repository_relative_path"] for x in plan} ==
            {x["repository_relative_path"] for x in inv}, "safety metadata scope mismatch")
    for item in inv:
        verify_file(checked_path(ROOT, item["repository_relative_path"]), int(item["bytes_read"]), item["sha256"])
    require(sum(int(x["bytes_read"]) for x in inv) == 621041, "safety metadata byte total")
    incoming = strict_csv(ENTRY / "incoming-read-inventory.csv")
    stash_rows = strict_csv(ENTRY / "stash-untracked-tree-verification.csv")
    require(len(incoming) == len(stash_rows) == 868, "incoming safety row count")
    counts = Counter(x["comparison"] for x in incoming)
    require(counts == {"same_as_remote": 836, "different_but_equal_to_prior_protection": 32}, "incoming comparison differs")
    require(sum(int(x["bytes_read"]) for x in incoming) == 46015150, "incoming byte total")
    by_path = {x["repository_relative_path"]: x for x in stash_rows}
    require(len(by_path) == 868 and set(by_path) == {x["repository_relative_path"] for x in incoming}, "stash path set")
    base = json.loads((ENTRY / "baseline.json").read_text(encoding="utf-8"))["remote_tip_observed_before_fetch"]
    tree = git_tree(base)
    for row in incoming:
        s = by_path[row["repository_relative_path"]]
        require(s["pre_stash_blob_sha1"] == s["stash_blob_sha1"] == row["git_blob_sha1"] and
                s["pre_stash_mode"] == s["stash_mode"] == row["git_mode"] and s["exact_blob_and_mode_equal"] == "True",
                "stash metadata mismatch")
        path = row["repository_relative_path"] if row["comparison"] == "same_as_remote" else row["protected_variant_path"]
        require(tree.get(path) == (row["git_mode"], "blob", row["git_blob_sha1"]), "base tree blob/mode mismatch")
    protected_scope = rows("protected-variants-scope-before-recheck.csv")
    protected = rows("protected-variants-read-inventory.csv")
    require(len(protected_scope) == len(protected) == 32 and
            {x["protected_repository_relative_path"] for x in protected_scope} ==
            {x["protected_repository_relative_path"] for x in protected}, "protected path scope")
    for item in protected:
        data = verify_file(checked_path(ROOT, item["protected_repository_relative_path"]), int(item["bytes_read"]), item["sha256"])
        verify_git_blob(data, int(item["bytes_read"]), item["git_blob_sha1"])
    require(sum(int(x["bytes_read"]) for x in protected) == 17473261, "protected byte total")
    stash = json.loads((ENTRY / "stash-verification-before-fast-forward.json").read_text(encoding="utf-8"))["stash_commit"]
    present = subprocess.run(["git", "cat-file", "-e", stash + "^3"], cwd=ROOT,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
    if present:
        stree = git_tree(stash + "^3")
        require(len(stree) == 868, "live stash tree count")
        for path, item in by_path.items():
            require(stree.get(path) == (item["stash_mode"], "blob", item["stash_blob_sha1"]), "live stash tree mismatch")
        stash_result = "verified 868 local entries; not portable"
    else:
        stash_result = "local stash absent; saved metadata only"
    return {"metadata_paths": 3, "metadata_bytes": 621041, "protected_paths": 32,
            "protected_bytes": 17473261, "incoming_paths": 868, "incoming_bytes": 46015150,
            "stash": stash_result, "base_commit": base}


def check_dossier() -> dict[str, int]:
    plan, log = rows("append-plan-before-write.csv")[0], rows("append-log.csv")[0]
    target = plan["repository_relative_path"]
    require(target == log["repository_relative_path"], "append target mismatch")
    base = json.loads((ENTRY / "baseline.json").read_text(encoding="utf-8"))["remote_tip_observed_before_fetch"]
    old = subprocess.check_output(["git", "show", f"{base}:{target}"], cwd=ROOT)
    current = checked_path(ROOT, target).read_bytes()
    payload = (R / "append-payload-r112.md").read_bytes()
    require(len(old) == int(plan["expected_original_bytes"]) == int(log["before_bytes"]), "old dossier length")
    verify_prefix(old, current, payload, plan["expected_original_sha256"], int(plan["prior_prefix_bytes"]), plan["prior_prefix_sha256"])
    require(sha256(old[:int(plan["older_prefix_bytes"])]) == plan["older_prefix_sha256"], "older prefix mismatch")
    require(len(payload) == int(log["payload_bytes"]) and sha256(payload) == log["payload_sha256"], "payload mismatch")
    require(len(current) == int(log["after_bytes"]) and sha256(current) == log["after_sha256"], "append output mismatch")
    return {"old_bytes": len(old), "appended_bytes": len(payload), "new_bytes": len(current)}


def check_links() -> int:
    docs = [R / "README.md", R / "scope-and-sequence-deviations.md", R / "metadata-scope-correction.md",
            R / "fetch-failures/X01.visible.md", R / "fetch-failures/X02.visible.md",
            WORK / "08-customer-pipeline/181-angora-nac-support-bug-evidence-r112-2026-10-26.md",
            WORK / "09-orders/120-angora-orders-dossier-2026-10-21.r112-appendix.md",
            WORK / "09-orders/120-angora-orders-master-2026-10-21.mapping-r112.md",
            ROOT / INGEST / "74-followup-angora-r112-2026-10-26/angora-networks.md",
            ROOT / INGEST / "75-audit-r112-2026-10-26.md"]
    pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    n = 0
    for doc in docs:
        for m in pattern.finditer(doc.read_text(encoding="utf-8")):
            target = m.group(1).split("#", 1)[0]
            if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            path = (doc.parent / target).resolve()
            require(path.is_relative_to(ROOT) and path.exists(), f"broken local link in {doc}: {target}")
            n += 1
    return n


def check_manifest() -> dict[str, object]:
    if not MANIFEST.exists():
        return {"status": "not yet created"}
    entries = strict_csv(MANIFEST)
    require(len(entries) == len({x["repository_relative_path"] for x in entries}), "duplicate manifest path")
    self_path = str(MANIFEST.relative_to(ROOT))
    self_rows = [x for x in entries if x["repository_relative_path"] == self_path]
    require(len(self_rows) == 1 and self_rows[0]["sha256"] == "SELF", "manifest self marker")
    total = 0
    for entry in entries:
        if entry["repository_relative_path"] == self_path:
            continue
        total += len(verify_file(checked_path(ROOT, entry["repository_relative_path"]),
                                 int(entry["bytes"]), entry["sha256"]))
    return {"status": "verified local paths and hashes; self hash intentionally omitted", "paths": len(entries), "other_bytes": total}


def run() -> dict[str, object]:
    read = check_inventories()
    sources = check_catalog_anchors()
    discovery = check_search_and_cdx()
    github = check_github()
    chunks = check_chunks_and_failures()
    safety = check_safety()
    dossier = check_dossier()
    paths = set(read.pop("path_set"))
    paths.update(x["repository_relative_path"] for x in rows("safety-metadata-read-inventory.csv"))
    paths.update(x["protected_repository_relative_path"] for x in rows("protected-variants-read-inventory.csv"))
    require(len(paths) == 93, "combined safety/source path overlap")
    timing = json.loads((R / "timing-check.json").read_text(encoding="utf-8"))
    require(timing["elapsed_seconds"] >= 600 and
            abs((timing["monotonic_check_seconds"] - timing["monotonic_start_seconds"]) - timing["elapsed_seconds"]) < 0.002,
            "elapsed monotonic time mismatch")
    return {"status": "PASS", "read_scope": read, "sources": sources, "discovery": discovery,
            "github": github, "chunks": chunks, "safety": safety, "dossier_append": dossier,
            "distinct_paths_including_hash_only_safety": 93, "bytes_including_hash_only_safety": 18450017,
            "relative_links_checked": check_links(), "elapsed_monotonic_seconds": timing["elapsed_seconds"],
            "output_manifest": check_manifest(),
            "limitations": ["local hashes cannot prove tool transcript or webpage original-byte fidelity",
                            "Git blobs are public samples, not independent execution or production evidence",
                            "archive capture, Git commit, session date, and uncalibrated wall clock are different fields",
                            "no device, current support status, certification, customer delivery, or audio verified",
                            "saved read inventories cannot prove earlier access order; local stash is not portable"]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-summary", action="store_true", help="write summary before output manifest exists")
    args = parser.parse_args()
    try:
        if args.write_summary:
            require(not MANIFEST.exists(), "write summary before creating manifest to avoid stale hashes")
        result = run()
        if args.write_summary:
            (R / "verification-summary.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (AuditError, OSError, ValueError, KeyError, IndexError, json.JSONDecodeError, subprocess.CalledProcessError) as exc:
        print(f"FAIL: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
