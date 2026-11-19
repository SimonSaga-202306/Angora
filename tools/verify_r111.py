#!/usr/bin/env python3
"""Verify r111 local inventories and evidence boundaries, not source authenticity.

The optional local stash check is skipped when the stash object is unavailable:
it is not a portable backup.  No PASS content is printed or interpreted.
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

ROOT = Path(__file__).resolve().parents[1]
INGEST = Path("ingest/angora-1__arena-01a0ce39__5acb613")
R = ROOT / INGEST / "69-source-evidence-r111-2026-10-26"
ENTRY = ROOT / INGEST / "68-entry-safety-r111-2026-10-26"
WORK = ROOT / INGEST / "01-text-verbatim/workstation"
MANIFEST = R / "output-manifest-before-stage.csv"


class AuditError(Exception):
    """A local consistency check failed."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AuditError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def checked_path(root: Path, relative: str) -> Path:
    p = (root / relative).resolve()
    require(p.is_relative_to(root.resolve()), f"path escapes repository: {relative}")
    return p


def verify_file(path: Path, expected_size: int, expected_sha: str) -> bytes:
    try:
        data = path.read_bytes()
    except OSError as exc:
        raise AuditError(f"cannot read {path}: {exc}") from exc
    require(len(data) == expected_size, f"size mismatch: {path}")
    require(sha256(data) == expected_sha, f"SHA-256 mismatch: {path}")
    return data


def strict_csv(path: Path) -> list[dict[str, str]]:
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.reader(handle, strict=True)
            header = next(reader)
            require(len(header) == len(set(header)), f"duplicate CSV headings: {path}")
            rows = []
            for row in reader:
                require(len(row) == len(header), f"malformed CSV at {path}:{reader.line_num}")
                rows.append(dict(zip(header, row)))
            return rows
    except (OSError, UnicodeError, csv.Error, StopIteration) as exc:
        raise AuditError(f"cannot parse CSV {path}: {exc}") from exc


def verify_anchor(text: str, first: int, last: int, fragment: str) -> None:
    lines = text.splitlines()
    require(1 <= first <= last <= len(lines), "anchor line range is invalid")
    require(bool(fragment), "empty anchor fragment")
    require(fragment in "\n".join(lines[first - 1:last]), "anchor fragment not in claimed lines")


def verify_join(parts: list[bytes], combined: bytes) -> None:
    require(bool(parts), "no chunks")
    require(b"".join(parts) == combined, "chunks do not reconstruct local combined page")


def verify_prefix(old: bytes, current: bytes, payload: bytes, old_digest: str,
                  older_length: int, older_digest: str) -> None:
    require(sha256(old) == old_digest, "old prefix digest mismatch")
    require(0 <= older_length <= len(old), "invalid earlier prefix length")
    require(sha256(old[:older_length]) == older_digest, "earlier prefix digest mismatch")
    require(current == old + payload, "current dossier is not exact append of planned payload")


def inventory_rows(name: str) -> list[dict[str, str]]:
    return strict_csv(R / name)


def check_inventories() -> tuple[list[dict[str, str]], dict[str, int]]:
    groups = [
        ("prior-round-read-inventory.csv", "prior-round-scope-before-read.csv", 6, 62357),
        ("prior-round-extension-read-inventory.csv", "prior-round-extension-scope-before-read.csv", 4, 4191),
        ("comparison-extension-read-inventory.csv", "comparison-extension-scope-before-read.csv", 4, 59332),
        ("external-read-inventory.csv", "external-read-scope-before-consolidated-read.csv", 6, 69921),
        ("external-extension-read-inventory.csv", "external-extension-read-scope-before-read.csv", 1, 5019),
        ("X02-chunk-read-inventory.csv", "X02-chunk-plan-after-first-two-results.csv", 5, 36335),
    ]
    combined = []
    totals = {}
    for inventory, scope, expected_count, expected_bytes in groups:
        rows = inventory_rows(inventory)
        plan = inventory_rows(scope)
        if inventory == "X02-chunk-read-inventory.csv":
            planned = {str((INGEST / R.name / r["planned_chunk_path"]).as_posix()) for r in plan}
        else:
            planned = {r["repository_relative_path"] for r in plan}
        actual = {r["repository_relative_path"] for r in rows}
        require(len(rows) == expected_count and len(actual) == expected_count,
                f"wrong count or duplicate path: {inventory}")
        require(planned == actual, f"scope/read path mismatch: {inventory}")
        total = 0
        for row in rows:
            path = checked_path(ROOT, row["repository_relative_path"])
            total += len(verify_file(path, int(row["bytes_read"]), row["sha256"]))
        require(total == expected_bytes, f"wrong byte total: {inventory}")
        combined.extend(rows)
        totals[inventory] = total
    require(len(combined) == 26 and len({r["repository_relative_path"] for r in combined}) == 26,
            "source and comparison paths are not unique")
    require(sum(totals.values()) == 237155, "source/read byte total differs")
    return combined, totals


def check_catalog_and_anchors() -> tuple[int, int]:
    catalog = inventory_rows("source-catalog.csv")
    by_id = {row["source_id"]: row for row in catalog}
    expected = {"X01", "X02", "X03", "X04", "X05", "X06", "X07", "X08", "P01", "P02", "P03", "P04"}
    require(len(catalog) == len(by_id) == 12 and set(by_id) == expected, "catalog IDs differ")
    require(not by_id["X03"]["repository_relative_path"], "unopened X03 has a claimed file")
    for sid, row in by_id.items():
        if sid == "X03":
            continue
        verify_file(checked_path(ROOT, row["repository_relative_path"]), int(row["bytes_read"]), row["sha256"])
    require("failure" in by_id["X01"]["tier"], "X01 not marked as failure")
    anchor_rows = inventory_rows("evidence-traceability.csv")
    ids = {r["anchor_id"] for r in anchor_rows}
    require(len(anchor_rows) == len(ids) == 35, "anchor count or uniqueness differs")
    for a in anchor_rows:
        require(a["source_id"] in by_id and a["source_id"] not in {"X01", "X03"}, "invalid anchor source")
        source = by_id[a["source_id"]]
        require(a["repository_relative_path"] == source["repository_relative_path"], "anchor source path mismatch")
        require(a["local_sha256"] == source["sha256"], "anchor digest mismatch")
        text = checked_path(ROOT, a["repository_relative_path"]).read_text(encoding="utf-8")
        verify_anchor(text, int(a["line_start"]), int(a["line_end"]), a["exact_fragment"])
    for name, field, count in [("claim-boundaries.csv", "anchors", 14),
                                ("issues-and-corrections.csv", "anchors", 10)]:
        rows = inventory_rows(name)
        require(len(rows) == count, f"wrong count: {name}")
        for row in rows:
            for anchor in filter(None, row[field].split(";")):
                require(anchor in ids, f"unknown anchor {anchor} in {name}")
    plan = inventory_rows("X02-chunk-plan-after-first-two-results.csv")
    require([int(x["chunk_index"]) for x in plan] == list(range(5)), "X02 chunk indices differ")
    parts = [(R / x["planned_chunk_path"]).read_bytes() for x in plan]
    merged = checked_path(ROOT, by_id["X02"]["repository_relative_path"]).read_bytes()
    verify_join(parts, merged)
    # These checks concern only the saved local transcription, not the source response.
    require(parts[0].endswith(b"bi") and parts[1].startswith("lişim".encode()), "X02 boundary 0/1")
    require(parts[1].endswith(b"Y\xc3\xb6netm") and parts[2].startswith(b"eni"), "X02 boundary 1/2")
    require(parts[2].endswith(b"/i") and parts[3].startswith(b"mages/"), "X02 boundary 2/3")
    require(parts[3].endswith(b"Rekl") and parts[4].startswith(b"am Ad"), "X02 boundary 3/4")
    assembly = json.loads((R / "X02-assembly-result.json").read_text(encoding="utf-8"))
    require(assembly["tool_chunks_returned"] == 5 and not assembly["final_has_more"], "X02 metadata differs")
    require(assembly["sha256"] == sha256(merged), "X02 assembly digest differs")
    return len(catalog), len(anchor_rows)


def check_search_and_csv() -> dict[str, object]:
    for path in R.rglob("*.csv"):
        strict_csv(path)
    plans = ["discovery-plan-before-search.csv", "discovery-extension-plan-before-search.csv",
             "discovery-video-event-plan-before-search.csv", "discovery-registration-plan-before-search.csv",
             "discovery-organizer-registry-plan-before-search.csv"]
    rows = [row for name in plans for row in inventory_rows(name)]
    ids = [r["query_id"] for r in rows]
    expected = [f"Q{i:02d}" for i in range(1, 29)]
    require(ids == expected, "query plans do not have Q01–Q28 exactly once")
    require(rows[9]["query"].startswith("site:ictmedia.com.tr"), "Q10 executed plan not narrowed")
    correction = (R / "scope-and-record-corrections.md").read_text(encoding="utf-8")
    require('"Angora Networks" ağ teknolojileri üretim yatırım kapasite -filetype:pdf' in correction,
            "Q10 original query disclosure missing")
    total, empty = 0, []
    for qid in expected:
        results = strict_csv(R / "search-discovery" / f"{qid}.csv")
        require(results and all(r["query_id"] == qid for r in results), f"result attribution wrong: {qid}")
        positions = [int(r["result_position"]) for r in results]
        if positions == [0]:
            empty.append(qid)
        else:
            require(positions == list(range(1, len(positions) + 1)), f"result positions wrong: {qid}")
            total += len(positions)
    require(total == 98, f"query result metadata count is {total}, expected 98")
    require(empty == ["Q12", "Q16", "Q20", "Q21", "Q25"], "zero-result metadata differs")
    return {"queries": len(expected), "nonempty_result_rows": total, "zero_result_query_ids": empty}


def git_tree(ref: str) -> dict[str, tuple[str, str, str]]:
    try:
        data = subprocess.check_output(["git", "ls-tree", "-rz", "--full-tree", ref], cwd=ROOT)
    except subprocess.CalledProcessError as exc:
        raise AuditError(f"cannot read git tree {ref}") from exc
    result = {}
    for entry in data.split(b"\0"):
        if not entry:
            continue
        meta, path = entry.split(b"\t", 1)
        mode, kind, oid = meta.decode("ascii").split()
        result[path.decode("utf-8")] = (mode, kind, oid)
    return result


def check_safety() -> dict[str, object]:
    scopes = inventory_rows("safety-metadata-recheck-scope-before-full-read.csv")
    reads = inventory_rows("safety-metadata-recheck-read-inventory.csv")
    require(len(scopes) == len(reads) == 3, "safety metadata count differs")
    require({x["repository_relative_path"] for x in scopes} ==
            {x["repository_relative_path"] for x in reads}, "safety metadata scope mismatch")
    for x in reads:
        verify_file(checked_path(ROOT, x["repository_relative_path"]), int(x["bytes_read"]), x["sha256"])
    require(sum(int(x["bytes_read"]) for x in reads) == 609109, "safety metadata total differs")
    incoming = strict_csv(ENTRY / "incoming-read-inventory.csv")
    stash_rows = strict_csv(ENTRY / "stash-untracked-tree-verification.csv")
    require(len(incoming) == len(stash_rows) == 868, "incoming or stash inventory count differs")
    counts = Counter(r["comparison"] for r in incoming)
    require(counts == {"same_as_remote": 836, "different_but_equal_to_remote_prior_protection": 32},
            "incoming comparison counts differ")
    require(sum(int(r["bytes_read"]) for r in incoming) == 46015150, "incoming size differs")
    stash_by_path = {x["repository_relative_path"]: x for x in stash_rows}
    require(len(stash_by_path) == 868 and set(stash_by_path) ==
            {x["repository_relative_path"] for x in incoming}, "stash path set differs")
    for row in stash_rows:
        require(row["pre_stash_blob_sha1"] == row["stash_blob_sha1"] and
                row["pre_stash_mode"] == row["stash_mode"] and row["exact_blob_and_mode_equal"] == "True",
                "stored stash comparison differs")
    base = json.loads((ENTRY / "baseline.json").read_text(encoding="utf-8"))["remote_head_after_fetch"]
    tree = git_tree(base)
    for row in incoming:
        key = row["repository_relative_path"] if row["comparison"] == "same_as_remote" else row["protected_variant_path"]
        require(tree.get(key) == (row["git_mode"], "blob", row["git_blob_sha1"]), "base tree blob or mode differs")
    protected = inventory_rows("protected-variants-recheck-read-inventory.csv")
    protected_plan = inventory_rows("protected-variants-recheck-scope-before-read.csv")
    require(len(protected) == len(protected_plan) == 32, "protected copy count differs")
    require({x["protected_repository_relative_path"] for x in protected} ==
            {x["protected_repository_relative_path"] for x in protected_plan}, "protected scope mismatch")
    for row in protected:
        data = verify_file(checked_path(ROOT, row["protected_repository_relative_path"]),
                           int(row["bytes_read"]), row["sha256"])
        oid = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
        require(oid == row["git_blob_sha1"], "protected git blob digest differs")
    require(sum(int(x["bytes_read"]) for x in protected) == 17473261, "protected bytes differ")
    stash = json.loads((ENTRY / "stash-verification-before-fast-forward.json").read_text(encoding="utf-8"))["stash_commit"]
    present = subprocess.run(["git", "cat-file", "-e", stash + "^3"], cwd=ROOT,
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
    if present:
        stash_tree = git_tree(stash + "^3")
        require(len(stash_tree) == 868, "live stash tree count differs")
        for path, row in stash_by_path.items():
            require(stash_tree.get(path) == (row["stash_mode"], "blob", row["stash_blob_sha1"]),
                    "live stash blob or mode differs")
        stash_result = "verified 868 local tree entries; stash is not portable"
    else:
        stash_result = "local stash object absent; saved metadata only, no live tree verification"
    return {"metadata_paths": 3, "metadata_bytes": 609109, "protected_paths": 32,
            "protected_bytes": 17473261, "incoming_paths": 868, "incoming_bytes": 46015150,
            "stash": stash_result, "base_tree": base}


def check_dossier() -> dict[str, object]:
    plan = inventory_rows("append-plan-before-write.csv")[0]
    log = inventory_rows("append-log.csv")[0]
    target = plan["repository_relative_path"]
    require(target == log["repository_relative_path"], "dossier plan/log path mismatch")
    base = json.loads((ENTRY / "baseline.json").read_text(encoding="utf-8"))["remote_head_after_fetch"]
    old = subprocess.check_output(["git", "show", f"{base}:{target}"], cwd=ROOT)
    current = checked_path(ROOT, target).read_bytes()
    payload = (R / "append-payload-r111.md").read_bytes()
    require(len(old) == int(plan["expected_original_bytes"]) == int(log["before_bytes"]), "dossier old size differs")
    require(len(payload) == int(log["payload_bytes"]) and sha256(payload) == log["payload_sha256"], "payload differs")
    verify_prefix(old, current, payload, log["before_sha256"], int(plan["known_older_prefix_bytes"]),
                  plan["known_older_prefix_sha256"])
    require(len(current) == int(log["after_bytes"]) and sha256(current) == log["after_sha256"], "dossier after differs")
    return {"old_bytes": len(old), "appended_bytes": len(payload), "current_bytes": len(current)}


def check_links() -> int:
    docs = [R / "README.md", R / "scope-and-record-corrections.md",
            WORK / "08-customer-pipeline/180-angora-commercial-history-evidence-r111-2026-10-26.md",
            WORK / "09-orders/120-angora-orders-dossier-2026-10-21.r111-appendix.md",
            WORK / "09-orders/120-angora-orders-master-2026-10-21.mapping-r111.md",
            ROOT / INGEST / "70-followup-angora-r111-2026-10-26/angora-networks.md",
            ROOT / INGEST / "71-audit-r111-2026-10-26.md"]
    count = 0
    pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    for doc in docs:
        text = doc.read_text(encoding="utf-8")
        for match in pattern.finditer(text):
            target = match.group(1).split("#", 1)[0]
            if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            path = (doc.parent / target).resolve()
            require(path.is_relative_to(ROOT) and path.exists(), f"broken local link in {doc}: {target}")
            count += 1
    return count


def check_manifest() -> dict[str, object]:
    if not MANIFEST.exists():
        return {"status": "not yet created"}
    rows = strict_csv(MANIFEST)
    require(len(rows) == len({r["repository_relative_path"] for r in rows}), "duplicate manifest path")
    self_relative = str(MANIFEST.relative_to(ROOT))
    self_rows = [r for r in rows if r["repository_relative_path"] == self_relative]
    require(len(self_rows) == 1 and self_rows[0]["sha256"] == "SELF", "manifest self marker missing")
    total = 0
    for row in rows:
        if row["repository_relative_path"] == self_relative:
            continue
        data = verify_file(checked_path(ROOT, row["repository_relative_path"]), int(row["bytes"]), row["sha256"])
        total += len(data)
    return {"status": "verified local paths and hashes; self hash intentionally omitted", "paths": len(rows),
            "other_bytes": total}


def run() -> dict[str, object]:
    read_rows, totals = check_inventories()
    catalog_count, anchor_count = check_catalog_and_anchors()
    search = check_search_and_csv()
    safety = check_safety()
    dossier = check_dossier()
    safety_paths = inventory_rows("safety-metadata-recheck-read-inventory.csv")
    protected_paths = inventory_rows("protected-variants-recheck-read-inventory.csv")
    paths = {x["repository_relative_path"] for x in read_rows}
    paths.update(x["repository_relative_path"] for x in safety_paths)
    paths.update(x["protected_repository_relative_path"] for x in protected_paths)
    require(len(paths) == 61, "61-path combined accounting contains overlap")
    timing = json.loads((R / "timing-check.json").read_text(encoding="utf-8"))
    require(timing["elapsed_seconds"] >= 600, "elapsed monotonic interval is below ten minutes")
    require(abs((timing["monotonic_check_seconds"] - timing["monotonic_start_seconds"]) -
                timing["elapsed_seconds"]) < 0.002, "elapsed monotonic calculation differs")
    return {"status": "PASS", "source_and_comparison_paths": len(read_rows),
            "source_and_comparison_bytes": sum(totals.values()), "catalog_entries": catalog_count,
            "exact_local_anchors": anchor_count, "search": search, "safety": safety,
            "distinct_paths_including_hash_only_safety": len(paths),
            "bytes_including_hash_only_safety": 237155 + 609109 + 17473261,
            "dossier_append": dossier, "relative_links_checked": check_links(),
            "elapsed_monotonic_seconds": timing["elapsed_seconds"], "output_manifest": check_manifest(),
            "limitations": ["local hashes do not verify original web content or transcription fidelity",
                            "no audio, legal registration, device behavior, certification or delivery verified",
                            "monotonic elapsed time does not calibrate calendar dates or prove continuous work",
                            "local stash may not exist in a future clone; it is not a remote backup",
                            "stored inventories and hashes cannot prove the order of prior reads"]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-summary", action="store_true", help="write summary before building output manifest")
    args = parser.parse_args()
    try:
        if args.write_summary:
            require(not MANIFEST.exists(), "write summary before creating manifest, to avoid a stale manifest hash")
        result = run()
        if args.write_summary:
            (R / "verification-summary.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (AuditError, OSError, ValueError, KeyError, IndexError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
