#!/usr/bin/env python3
"""Verify r113 local inventories, historical comparisons and append-only update.

This checks saved files and recorded metadata, not source-page fidelity, real
hardware behavior, credentials, current firmware, certificates or delivery.
It never prints the historical public default value preserved in one source.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path

from verify_r111 import AuditError, checked_path, require, sha256, strict_csv, verify_anchor, verify_file, verify_join, verify_prefix
from verify_r112 import parse_cdx

ROOT = Path(__file__).resolve().parents[1]
INGEST = Path("ingest/angora-1__arena-01a0ce39__5acb613")
R = ROOT / INGEST / "77-source-evidence-r113-2026-10-26"
ENTRY = ROOT / INGEST / "76-entry-safety-r113-2026-10-26"
WORK = ROOT / INGEST / "01-text-verbatim/workstation"
MANIFEST = R / "output-manifest-before-stage.csv"


def rows(name: str) -> list[dict[str, str]]:
    return strict_csv(R / name)


def selected_body(text: str, start_marker: str, end_marker: str) -> str:
    try:
        start = text.index(start_marker)
        end = text.index(end_marker, start)
    except ValueError as exc:
        raise AuditError("comparison body marker missing") from exc
    require(end > start, "invalid comparison body range")
    return text[start:end]


def normalize_wayback_timestamps(text: str) -> str:
    return re.sub(r"(?<=/web/)\d{14}(?=/)", "<CAPTURE>", text)


def make_redacted_view(text: str, token: str) -> str:
    require(bool(token) and text.count(token) == 2, "expected exactly two public default occurrences")
    return text.replace(token, "[HISTORICAL_PUBLIC_DEFAULT_OMITTED]")


def is_non_source_id(source_id: str) -> bool:
    return source_id in {"X01", "R01"} or bool(re.fullmatch(r"A\d{2}", source_id))


def check_inventories() -> dict[str, object]:
    groups = [
        ("prior-round-read-inventory.csv", "prior-round-scope-before-read.csv", 10, 76661),
        ("comparison-source-read-inventory.csv", "comparison-source-scope-before-read.csv", 5, 35169),
        ("prior-event-comparison-read-inventory.csv", "prior-event-comparison-scope-before-read.csv", 2, 24055),
        ("archive-index-read-inventory.csv", "archive-index-read-scope-before-file-read.csv", 9, 4118),
        ("archive-replay-read-inventory.csv", "archive-replay-read-scope-before-consolidated-read.csv", 9, 67829),
        ("archive-chunk-read-inventory.csv", "archive-chunk-read-scope-after-assembly.csv", 10, 50035),
        ("AR06-redacted-review-read-inventory.csv", "AR06-redacted-review-scope-before-read.csv", 1, 8761),
        ("external-read-inventory.csv", "external-read-scope-before-file-reread.csv", 1, 8046),
    ]
    entries = []
    summary = {}
    for inv, plan, count, expected_bytes in groups:
        a, b = rows(inv), rows(plan)
        ap = {x["repository_relative_path"] for x in a}
        bp = {x["repository_relative_path"] for x in b}
        require(len(a) == len(ap) == count and ap == bp, f"scope/count mismatch: {inv}")
        total = 0
        for x in a:
            total += len(verify_file(checked_path(ROOT, x["repository_relative_path"]), int(x["bytes_read"]), x["sha256"]))
        require(total == expected_bytes, f"byte mismatch: {inv}")
        summary[inv] = {"paths": len(a), "bytes": total}
        entries.extend(a)
    paths = [x["repository_relative_path"] for x in entries]
    require(len(paths) == len(set(paths)) == 47, "read scope has duplicated paths")
    require(sum(int(x["bytes_read"]) for x in entries) == 274674, "total read bytes differ")
    return {"paths": len(paths), "bytes": 274674, "groups": summary}


def check_catalog_and_anchors() -> dict[str, int]:
    catalog = rows("source-catalog.csv")
    by_id = {r["source_id"]: r for r in catalog}
    require(len(catalog) == len(by_id) == 27, "catalog count differs")
    for r in catalog:
        verify_file(checked_path(ROOT, r["repository_relative_path"]), int(r["bytes_read"]), r["sha256"])
    require("unrelated" in by_id["X01"]["source_level"] and "not independent" in by_id["R01"]["source_level"],
            "unrelated and redacted sources must not be upgraded")
    anchors = rows("evidence-traceability.csv")
    ids = {a["anchor_id"] for a in anchors}
    require(len(anchors) == len(ids) == 36, "anchor count differs")
    for a in anchors:
        sid = a["source_id"]
        require(sid in by_id and not is_non_source_id(sid), "anchor uses non-source metadata")
        source = by_id[sid]
        require(a["repository_relative_path"] == source["repository_relative_path"] and a["local_sha256"] == source["sha256"],
                "anchor source identity/hash differs")
        text = checked_path(ROOT, a["repository_relative_path"]).read_text(encoding="utf-8")
        verify_anchor(text, int(a["line_start"]), int(a["line_end"]), a["exact_fragment"])
    for name, count in [("claim-boundaries.csv", 17), ("issues-and-corrections.csv", 10)]:
        data = rows(name)
        require(len(data) == count, f"count differs: {name}")
        for entry in data:
            for aid in filter(None, entry["anchors"].split(";")):
                require(aid in ids, f"unknown anchor {aid}")
    return {"catalog_entries": len(catalog), "local_anchors": len(anchors), "boundaries": 17, "corrections": 10}


def check_search_and_cdx() -> dict[str, object]:
    for path in R.rglob("*.csv"):
        strict_csv(path)
    plans = rows("discovery-plan-before-search.csv") + rows("business-discovery-extension-plan-before-search.csv")
    expected = [f"Q{i:02d}" for i in range(1, 20)]
    require([r["query_id"] for r in plans] == expected, "search plans differ")
    result_count = 0
    empty = []
    for qid in expected:
        results = strict_csv(R / "search-discovery" / f"{qid}.csv")
        require(results and all(x["query_id"] == qid for x in results), f"query id mismatch: {qid}")
        positions = [int(x["result_position"]) for x in results]
        if positions == [0]:
            empty.append(qid)
        else:
            require(positions == list(range(1, len(positions) + 1)), f"query positions mismatch: {qid}")
            result_count += len(positions)
    require(result_count == 34 and empty == ["Q03", "Q13", "Q14", "Q16", "Q18", "Q19"], "query counts differ")
    indexes = rows("archive-index-plan-before-fetch.csv")
    require(len(indexes) == 9, "CDX plan count differs")
    result = {}
    for x in indexes:
        require("to=20261026" in x["index_url"], "CDX cutoff missing")
        found = parse_cdx((R / x["planned_path"]).read_text(encoding="utf-8"))
        require(all(z[1] == x["original_url"] for z in found), "CDX original URL differs")
        result[x["index_id"]] = found
    require(sum(map(len, result.values())) == 26 and not result["A02"] and not result["A08"], "CDX results differ")
    plans = rows("archive-replay-plan-before-fetch.csv")
    replay = rows("archive-replay-results.csv")
    require(len(plans) == len(replay) == 9, "archive replay count differs")
    for x in plans:
        require(any(c[0] == x["capture"] for c in result[x["index_id"]]), "replay absent from CDX")
    by = {x["replay_id"]: x for x in replay}
    for p in plans:
        x = by[p["replay_id"]]
        require(x["capture"] == p["capture"] and x["original_url"] == p["original_url"] and
                x["replay_url"] == p["replay_url"] and x["repository_relative_path"] == str(INGEST / R.name / p["planned_success_path"]),
                "replay metadata differs from prelisted plan")
    require(sum(int(x["tool_chunks"]) for x in replay) == 14 and sum(int(x["bytes"]) for x in replay) == 67829,
            "archive chunks or byte count differs")
    require(not list(R.rglob("*.pdf")) and not list(R.rglob("*.zip")), "unexpected PDF or ZIP in r113 evidence")
    return {"queries": 19, "nonempty_result_rows": result_count, "zero_queries": empty,
            "cdx_requests": 9, "filtered_cdx_records": 26, "replays": 9, "tool_chunks": 14}


def check_chunks() -> dict[str, object]:
    endings = {
        "AR03": (b"switch#sh lldp ne", b"ighbors`"),
        "AR04": (b"switch#sh lldp ne", b"ighbors`"),
        "AR06": (b"ht_kb=yazilim-guncelleme", b"-tftp-verge-anahtarlar"),
        "AR07": ("Yazılım Güncell".encode(), b"eme (TFTP)"),
        "AR08": ("Komut Satı".encode(), "rı kullanımı".encode()),
    }
    for sid, (left, right) in endings.items():
        plan = rows(f"{sid}-chunk-plan-after-first-result.csv")
        require([int(x["chunk_index"]) for x in plan] == [0, 1], f"{sid} chunk plan differs")
        parts = [(R / x["planned_chunk_path"]).read_bytes() for x in plan]
        require(parts[0].endswith(left) and parts[1].startswith(right), f"{sid} chunk boundary differs")
        merged = (R / plan[0]["planned_combined_path"]).read_bytes()
        verify_join(parts, merged)
        info = json.loads((R / f"{sid}-assembly-result.json").read_text(encoding="utf-8"))
        require(info["tool_chunks_returned"] == 2 and not info["final_has_more"] and info["sha256"] == sha256(merged),
                f"{sid} assembly metadata differs")
    return {"two_chunk_assemblies": len(endings), "auxiliary_chunks": 10}


def check_comparison(plan_file: str, result_file: str, normalize: bool) -> bool:
    plan = rows(plan_file)[0]
    result = json.loads((R / result_file).read_text(encoding="utf-8"))
    bodies = []
    for i, key in enumerate(["source_a", "source_b"]):
        path = R / plan[key]
        raw = path.read_bytes()
        body = selected_body(raw.decode("utf-8"), plan["start_marker"], plan["end_marker"])
        part = result["parts"][i]
        require(len(raw) == part["file_bytes"] and sha256(raw) == part["file_sha256"], "comparison source digest differs")
        if normalize:
            require(len(body.encode()) == part["body_utf8_bytes"] and sha256(body.encode()) == part["body_sha256"], "LLDP body digest differs")
            normalized = normalize_wayback_timestamps(body).encode("utf-8")
            require(len(normalized) == part["normalized_body_bytes"] and sha256(normalized) == part["normalized_body_sha256"], "normalized body digest differs")
            bodies.append(normalized)
        else:
            data = body.encode("utf-8")
            require(len(data) == part["selected_body_bytes"] and sha256(data) == part["selected_body_sha256"], "voice body digest differs")
            bodies.append(data)
    same = bodies[0] == bodies[1]
    field = "normalized_saved_text_equal" if normalize else "selected_saved_body_byte_identical"
    require(same == result[field] and same, "comparison result differs")
    return same


def check_redacted_and_unrelated() -> dict[str, object]:
    meta = json.loads((R / "AR06-redacted-review-metadata.json").read_text(encoding="utf-8"))
    source = checked_path(ROOT, meta["source_path"]).read_bytes()
    view = checked_path(ROOT, meta["review_path"]).read_bytes()
    require(len(source) == meta["source_bytes"] and sha256(source) == meta["source_sha256"], "AR06 source differs")
    require(len(view) == meta["review_bytes"] and sha256(view) == meta["review_sha256"] and meta["replacement_count"] == 2,
            "AR06 review metadata differs")
    # Value is public historical text; it is not printed, used for access, or included in summaries.
    public_word = bytes([97, 100, 109, 105, 110]).decode("ascii")
    expected = make_redacted_view(source.decode("utf-8"), public_word).encode("utf-8")
    require(view == expected, "AR06 redacted view differs outside two replacements")
    x = rows("external-read-inventory.csv")[0]
    text = checked_path(ROOT, x["repository_relative_path"]).read_text(encoding="utf-8")
    require(not re.search(r"(?i)\bangora\b", text) and x["angora_token_present"] == "False", "X01 unrelated classification differs")
    return {"redacted_positions": 2, "magazine_false_positive": True}


def check_dossier() -> dict[str, int]:
    plan, log = rows("append-plan-before-write.csv")[0], rows("append-log.csv")[0]
    target = plan["repository_relative_path"]
    require(target == log["repository_relative_path"], "append target mismatch")
    base = json.loads((ENTRY / "baseline.json").read_text(encoding="utf-8"))["local_head"]
    old = subprocess.check_output(["git", "show", f"{base}:{target}"], cwd=ROOT)
    current = checked_path(ROOT, target).read_bytes()
    payload = (R / "append-payload-r113.md").read_bytes()
    require(len(old) == int(plan["expected_original_bytes"]) == int(log["before_bytes"]), "old dossier size mismatch")
    verify_prefix(old, current, payload, plan["expected_original_sha256"], int(plan["prior_prefix_bytes"]), plan["prior_prefix_sha256"])
    require(sha256(old[:int(plan["older_prefix_bytes"])]) == plan["older_prefix_sha256"], "older prefix mismatch")
    require(len(payload) == int(log["payload_bytes"]) and sha256(payload) == log["payload_sha256"], "append payload mismatch")
    require(len(current) == int(log["after_bytes"]) and sha256(current) == log["after_sha256"], "append output mismatch")
    return {"old_bytes": len(old), "appended_bytes": len(payload), "new_bytes": len(current)}


def check_links() -> int:
    docs = [R / "README.md", R / "scope-and-sequence-deviations.md", R / "AR06-redacted-review-plan-before-write.md",
            WORK / "08-customer-pipeline/182-angora-management-voice-evidence-r113-2026-10-26.md",
            WORK / "09-orders/120-angora-orders-dossier-2026-10-21.r113-appendix.md",
            WORK / "09-orders/120-angora-orders-master-2026-10-21.mapping-r113.md",
            ROOT / INGEST / "78-followup-angora-r113-2026-10-26/angora-networks.md",
            ROOT / INGEST / "79-audit-r113-2026-10-26.md"]
    pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    count = 0
    for doc in docs:
        for match in pattern.finditer(doc.read_text(encoding="utf-8")):
            target = match.group(1).split("#", 1)[0]
            if not target or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            p = (doc.parent / target).resolve()
            require(p.is_relative_to(ROOT) and p.exists(), f"broken local link in {doc}: {target}")
            count += 1
    return count


def check_manifest() -> dict[str, object]:
    if not MANIFEST.exists():
        return {"status": "not yet created"}
    entries = strict_csv(MANIFEST)
    require(len(entries) == len({x["repository_relative_path"] for x in entries}), "duplicate manifest entry")
    self_path = str(MANIFEST.relative_to(ROOT))
    own = [x for x in entries if x["repository_relative_path"] == self_path]
    require(len(own) == 1 and own[0]["sha256"] == "SELF", "manifest self marker missing")
    total = 0
    for x in entries:
        if x["repository_relative_path"] == self_path:
            continue
        total += len(verify_file(checked_path(ROOT, x["repository_relative_path"]), int(x["bytes"]), x["sha256"]))
    return {"status": "verified local paths and hashes; self hash intentionally omitted", "paths": len(entries), "other_bytes": total}


def run() -> dict[str, object]:
    baseline = json.loads((ENTRY / "baseline.json").read_text(encoding="utf-8"))
    require(baseline["initial_status_entries"] == 0 and baseline["local_head"] == baseline["remote_tip_observed"], "entry baseline differs")
    require(subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip() == baseline["branch"], "current branch differs")
    read = check_inventories()
    sources = check_catalog_and_anchors()
    discovery = check_search_and_cdx()
    chunks = check_chunks()
    lldp = check_comparison("lldp-body-comparison-plan-before-compare.csv", "lldp-body-comparison-result.json", True)
    voice = check_comparison("voice-body-comparison-plan-before-compare.csv", "voice-body-comparison-result.json", False)
    safety = check_redacted_and_unrelated()
    dossier = check_dossier()
    timing = json.loads((R / "timing-check.json").read_text(encoding="utf-8"))
    require(timing["elapsed_seconds"] >= 600 and
            abs(timing["monotonic_check_seconds"] - timing["monotonic_start_seconds"] - timing["elapsed_seconds"]) < 0.002,
            "elapsed monotonic timing differs")
    return {"status": "PASS", "read_scope": read, "sources": sources, "discovery": discovery,
            "chunks": chunks, "local_body_comparisons": {"lldp_normalized_equal": lldp, "voice_selected_bytes_equal": voice},
            "safe_review": safety, "dossier_append": dossier, "relative_links_checked": check_links(),
            "elapsed_monotonic_seconds": timing["elapsed_seconds"], "output_manifest": check_manifest(),
            "limitations": ["manual local transcription hashes cannot prove tool response or original HTML fidelity",
                            "selected body comparisons cannot prove firmware state or intermediate history",
                            "no current device, certification, deployment, original images or MIB ZIP verified",
                            "local inventories cannot prove first-read ordering; deviations are documented",
                            "uncalibrated wall clock differs from supplied session date"]}


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
