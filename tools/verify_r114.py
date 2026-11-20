#!/usr/bin/env python3
"""Verify r114's local records without reopening the quarantined old page.

This checks inventories, anchors, local corrections, links, and an append-only
prefix. It cannot establish source-to-tool transcription fidelity, original
HTML bytes, corporate identity, current device behaviour, certification,
meeting attendance, or delivery. It does not open any network connection.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
INGEST = Path("ingest/angora-1__arena-01a0ce39__5acb613")
R = ROOT / INGEST / "81-source-evidence-r114-2026-10-26"
WORK = ROOT / INGEST / "01-text-verbatim/workstation"
QUARANTINE = "49-source-evidence-r106-2026-10-26/external-visible/www.angoranetworks.com/angora-networks-_en/index.en.extracted.md"
BASE = "0f924fe12dd75744f3ef91c6971161eef47491b9"


class AuditError(Exception):
    pass


def require(value: object, message: str) -> None:
    if not value:
        raise AuditError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def checked_path(value: str | Path) -> Path:
    path = Path(value)
    require(not path.is_absolute() and ".." not in path.parts, f"unsafe path: {value}")
    resolved = (ROOT / path).resolve()
    require(resolved.is_relative_to(ROOT.resolve()), f"outside root: {value}")
    return resolved


def strict_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, strict=True)
        require(reader.fieldnames is not None and len(set(reader.fieldnames)) == len(reader.fieldnames), f"CSV header: {path}")
        result = list(reader)
        require(all(None not in row and all(value is not None for value in row.values()) for row in result), f"CSV row shape: {path}")
        return result


def checked_file(path: Path, expected_bytes: int, expected_sha: str) -> bytes:
    data = path.read_bytes()
    data.decode("utf-8")
    require(len(data) == expected_bytes, f"size mismatch: {path}")
    require(sha256(data) == expected_sha, f"SHA-256 mismatch: {path}")
    return data


def anchor_present(text: str, line_number: int, needle: str) -> bool:
    lines = text.splitlines()
    return bool(needle) and 1 <= line_number <= len(lines) and needle in lines[line_number - 1]


def is_expected_correction(old: bytes, new: bytes, before: bytes, after: bytes) -> bool:
    return bool(before) and before != after and old.count(before) == 1 and old.replace(before, after, 1) == new


def parse_cdx(text: str) -> list[list[str]]:
    lines = text.splitlines()
    require(len(lines) >= 3 and lines[0] == "```json" and lines[-1] == "```", "CDX wrapper differs")
    try:
        rows = json.loads("\n".join(lines[1:-1]))
    except json.JSONDecodeError as exc:
        raise AuditError("invalid CDX JSON") from exc
    require(isinstance(rows, list) and rows, "missing CDX header")
    require(rows[0] == ["urlkey", "timestamp", "original", "mimetype", "statuscode", "digest", "length"], "CDX header differs")
    for row in rows[1:]:
        require(len(row) == 7 and row[3] == "text/html" and row[4] == "200", "unexpected CDX row")
        require(re.fullmatch(r"\d{14}", row[1]) is not None and row[1][:8] <= "20261026", "CDX timestamp outside cutoff")
    return rows[1:]


def check_read_scopes() -> dict[str, object]:
    old_names = ["prior-round-read-inventory.csv", "prior-timeline-read-inventory.csv", "external-read-inventory.csv", "extension-read-inventory.csv", "cutoff-archive-read-inventory.csv", "search-discovery-read-inventory.csv"]
    previous = [entry for name in old_names for entry in strict_csv(R / name)]
    previous_paths = [entry["path"] for entry in previous]
    require(len(previous) == len(set(previous_paths)) == 97, "previous path count differs")
    prior_bytes = 0
    checked = 0
    skipped = 0
    for entry in previous:
        path = checked_path(entry["path"])
        size = int(entry.get("actual_bytes") or entry.get("bytes") or "0")
        prior_bytes += size
        if QUARANTINE in entry["path"]:
            require(path.stat().st_size == size, "quarantined file size differs")
            skipped += 1
            continue
        checked_file(path, size, entry["sha256"])
        checked += 1
    require(prior_bytes == 323433 and checked == 96 and skipped == 1, "previous read summary differs")
    scope = strict_csv(R / "continuation-expanded-read-scope-before-reread.csv")
    inv = strict_csv(R / "continuation-expanded-read-inventory.csv")
    require(len(scope) == len(inv) == 30, "continuation scope count differs")
    require([r["path"] for r in scope] == [r["path"] for r in inv], "continuation scope paths differ")
    require(len(set(r["path"] for r in inv)) == 30 and not set(previous_paths).intersection(r["path"] for r in inv), "scope paths overlap")
    total = 0
    for item, record in zip(scope, inv):
        require(item["id"] == record["id"] and item["expected_bytes"] == record["bytes"], "scope row differs")
        total += len(checked_file(checked_path(record["path"]), int(record["bytes"]), record["sha256"]))
    require(total == 90584, "new scope byte total differs")
    summary = json.loads((R / "combined-read-summary.json").read_text(encoding="utf-8"))
    require(summary["combined_distinct_paths_previously_or_now_read"] == 127 and summary["combined_bytes"] == 414017, "combined summary differs")
    return {"previously_read_paths": 97, "previous_rechecked": checked, "quarantined_not_reopened": skipped, "new_paths": 30, "combined_paths": 127, "combined_bytes": prior_bytes + total}


def check_catalogs_and_anchors() -> dict[str, int]:
    catalogs = ["source-catalog.csv", "source-catalog-extension.csv", "source-catalog-cutoff-archive.csv", "source-catalog-2022-event.csv"]
    catalog_count = 0
    for name in catalogs:
        for item in strict_csv(R / name):
            path = item.get("local_path") or item.get("path")
            require(path is not None and QUARANTINE not in path, "catalog includes quarantined content")
            checked_file(checked_path(path), int(item["bytes"]), item["sha256"])
            catalog_count += 1
    anchor_count = 0
    ids: set[str] = set()
    for name in ["evidence-traceability.csv", "cutoff-evidence-traceability.csv", "event-2022-evidence-traceability.csv"]:
        for entry in strict_csv(R / name):
            aid = entry["anchor_id"]
            require(aid not in ids, f"duplicate anchor: {aid}")
            ids.add(aid)
            path = entry.get("local_path") or entry.get("path")
            require(path is not None and QUARANTINE not in path, "anchor points at quarantine")
            data = checked_path(path).read_bytes()
            expected = entry.get("local_sha256") or entry.get("source_sha256")
            require(sha256(data) == expected, f"anchor hash differs: {aid}")
            require(anchor_present(data.decode("utf-8"), int(entry["line_1_based"]), entry["exact_substring"]), f"anchor text differs: {aid}")
            anchor_count += 1
    require(len(strict_csv(R / "claim-boundaries.csv")) == 13 and len(strict_csv(R / "issues-and-corrections.csv")) == 14, "boundary/issue counts differ")
    return {"catalog_path_rows": catalog_count, "anchors": anchor_count, "boundaries": 13, "corrections": 14}


def check_search_and_cdx() -> dict[str, object]:
    for path in R.rglob("*.csv"):
        strict_csv(path)
    count = 0
    empty: list[str] = []
    for n in range(1, 70):
        qid = f"Q{n:02d}"
        rows = strict_csv(R / "search-discovery" / f"{qid}.csv")
        require(rows, f"missing query result: {qid}")
        positions = [int(row["rank"]) for row in rows]
        if positions == [0]:
            empty.append(qid)
        else:
            require(positions == list(range(1, len(positions) + 1)), f"query ranks differ: {qid}")
            count += len(rows)
    require(count == 254 and len(empty) == 3, "search result counts differ")
    index08 = parse_cdx((R / "archive-index/www.kamubib-bimy.org/2022/program/index.cdx.visible.txt").read_text(encoding="utf-8"))
    index09 = parse_cdx((R / "archive-index/www.kamubib-bimy.org/2022/oturumlar/oturum-4-evren-otesi-ve-siber-guvenlik/index.cdx.visible.txt").read_text(encoding="utf-8"))
    require({"20220705134406", "20221204195052"}.issubset({r[1] for r in index08}), "2022 programme replay not in index")
    require("20221204180601" in {r[1] for r in index09}, "session replay not in index")
    require(not any(p.suffix.lower() in {".pdf", ".zip", ".rar"} for p in R.rglob("*")), "unexpected binary download in r114 evidence")
    return {"queries": 69, "nonzero_search_rows": count, "zero_queries": empty, "new_cdx_records": len(index08) + len(index09)}


def check_ar08_and_comparison() -> dict[str, object]:
    chunk0 = (R / "archive-chunks/AR08/chunk-0.visible.md").read_bytes()
    chunk1 = (R / "archive-chunks/AR08/chunk-1.visible.md").read_bytes()
    draft = (R / "archive-transcription-drafts/AR08/chunk-1.pre-correction.visible.md").read_bytes()
    before = "M. Fatih ULUÇAM, _T.C. Sağlık Bakanlığı Sistem Yönetimi ve Bilgi Güvenliği Daire Başkanı_".encode()
    after = "M. Fatih ULUÇAM, _T.C. Sağlık Bakanlığı Sistem Yönetimi ve Bilgi Güvenliği Dairesi Başkanı_".encode()
    require(is_expected_correction(draft, chunk1, before, after), "AR08 known correction differs")
    require(chunk0.endswith("Genel Müdür Yardı".encode()) and chunk1.startswith("mcısı_".encode()), "AR08 chunk boundary differs")
    correction = json.loads((R / "AR08-correction-result.json").read_text(encoding="utf-8"))
    require(sha256(draft) == correction["old_sha256"] and sha256(chunk1) == correction["current_sha256"], "AR08 correction hashes differ")
    require(not (R / "archive-replay/www.kamubib-bimy.org/2022/program/20221204195052/index.visible.md").exists(), "removed AR08 concatenation reappeared")
    july = (R / "archive-replay/www.kamubib-bimy.org/2022/program/20220705134406/index.visible.md").read_text(encoding="utf-8")
    first, second = chunk0.decode("utf-8"), chunk1.decode("utf-8")
    comparison = strict_csv(R / "event-2022-selected-comparison.csv")
    require(len(comparison) == 4, "comparison scope differs")
    for item in comparison:
        text = item["selected_substring"]
        require(str(text in july) == item["july_in_local_saved_text"], "July comparison differs")
        require(str(text in first) == item["december_chunk0"] and str(text in second) == item["december_chunk1"], "December comparison differs")
    return {"chunks_kept_separate": 2, "known_transcription_edits": 1, "selected_substrings": len(comparison)}


def check_dossier() -> dict[str, object]:
    result = json.loads((R / "dossier-append-result.json").read_text(encoding="utf-8"))
    path = checked_path(result["path"])
    whole = path.read_bytes()
    n = result["prefix_bytes"]
    require(len(whole) == result["total_bytes"] and sha256(whole) == result["total_sha256"], "dossier total differs")
    require(sha256(whole[:n]) == result["prefix_sha256"] and sha256(whole[n:]) == result["append_sha256"], "dossier prefix/append differs")
    base = subprocess.check_output(["git", "show", f"{BASE}:{result['path']}"], cwd=ROOT)
    require(base == whole[:n] and len(whole[n:]) == result["append_bytes"], "HEAD historical prefix differs")
    return {"prefix_bytes": n, "append_bytes": len(whole[n:]), "total_bytes": len(whole)}


def check_links() -> int:
    docs = [R / "README.md", ROOT / INGEST / "83-audit-r114-2026-10-26.md", WORK / "08-customer-pipeline/183-angora-early-business-institutions-evidence-r114-2026-10-26.md", WORK / "09-orders/120-angora-orders-dossier-2026-10-21.r114-appendix.md", WORK / "09-orders/120-angora-orders-master-2026-10-21.mapping-r114.md", ROOT / INGEST / "82-followup-angora-r114-2026-10-26/angora-networks.md"]
    total = 0
    for doc in docs:
        text = doc.read_text(encoding="utf-8")
        for raw in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", text):
            ref = raw.split("#", 1)[0]
            if not ref or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", ref):
                continue
            target = (doc.parent / unquote(ref)).resolve()
            require(target.is_relative_to(ROOT.resolve()) and target.exists(), f"broken local link in {doc}: {raw}")
            total += 1
    return total


def main() -> None:
    timing = json.loads((R / "continuation-timing-check.json").read_text(encoding="utf-8"))
    require(timing["same_runtime"] and timing["elapsed_seconds"] >= 600, "continuation elapsed under 10 minutes")
    result = {"status": "PASS", "read_scopes": check_read_scopes(), "sources_and_anchors": check_catalogs_and_anchors(), "discovery_and_cdx": check_search_and_cdx(), "ar08": check_ar08_and_comparison(), "dossier": check_dossier(), "local_links_checked": check_links(), "elapsed_seconds": timing["elapsed_seconds"], "limitations": "Local consistency only; not remote response, original HTML, certificate, attendance, delivery or device test."}
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (AuditError, OSError, ValueError, KeyError, subprocess.CalledProcessError) as exc:
        raise SystemExit(f"FAIL: {exc}") from exc
