#!/usr/bin/env python3
"""Read-only checks for the r109 Angora research and preservation ledger.

The checks prove saved-byte and linkage properties, not historical access order,
source accuracy, transcription fidelity, certification, or business performance.
The local stash may not exist in a fresh clone; its absence is reported explicitly.
"""
from __future__ import annotations

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
E = I / "61-source-evidence-r109-2026-10-26"
S = I / "60-entry-safety-r109-2026-10-26"
W = I / "01-text-verbatim/workstation"
BASE = "b4d05524eaabd58dc21ba49664c50a93c50a5810"
STASH = "e74e476b678b48c3ce060a8c01fd04dd926a99cc"
BRANCH = "arena/5da004bd-angora"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        require(reader.fieldnames is not None, f"missing CSV header: {path}")
        rows = list(reader)
        require(all(None not in row for row in rows), f"malformed CSV row: {path}")
        return rows


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def blob_digest(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def checked_bytes(data: bytes, size: int, sha: str, label: str) -> None:
    require(len(data) == size, f"wrong byte count: {label}")
    require(digest(data) == sha, f"wrong SHA-256: {label}")


def checked_append(before: bytes, addition: bytes, after: bytes, old_sha: str, new_sha: str) -> None:
    require(digest(before) == old_sha, "append: prior digest differs")
    require(after == before + addition, "append: original prefix or suffix differs")
    require(digest(after) == new_sha, "append: resulting digest differs")


def checked_line(line: str, needle: str, expected_line: str, sha: str) -> None:
    require(needle in line, "anchor substring missing")
    require(line == expected_line, "complete saved anchor line differs")
    require(digest(line.encode("utf-8")) == sha, "anchor line digest differs")


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", *args], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=check
    )


def tree_entries(revision: str) -> dict[str, str]:
    entries: dict[str, str] = {}
    for entry in git("ls-tree", "-r", "-z", "--full-tree", revision).stdout.split(b"\0"):
        if not entry:
            continue
        metadata, raw_name = entry.split(b"\t", 1)
        _mode, kind, oid = metadata.split()
        require(kind == b"blob", "unexpected non-blob tree entry")
        name = raw_name.decode("utf-8")
        require(name not in entries, "duplicate path in tree")
        entries[name] = oid.decode("ascii")
    return entries


def verify_branch() -> None:
    branch = git("branch", "--show-current").stdout.decode().strip()
    require(branch == BRANCH, f"unexpected branch: {branch}")
    require(git("merge-base", "--is-ancestor", BASE, "HEAD", check=False).returncode == 0,
            "r108 baseline is not a current-branch ancestor")
    baseline = json.loads((S / "baseline.json").read_text(encoding="utf-8"))
    require(baseline["session_date_supplied_utc"] == "2026-10-26", "session date differs")
    require(baseline["environment_start_observed_utc"] == "2026-11-19T09:52:36Z",
            "recorded environment observation differs")
    print("PASS branch and separately recorded session/environment dates")


def verify_safety() -> None:
    incoming = read_csv(S / "incoming-read-inventory.csv")
    scope = read_csv(S / "incoming-scope-before-read.csv")
    saved = read_csv(S / "protected-variants-before-stash.csv")
    prior = read_csv(S / "variant-vs-r108-protected.csv")
    stash_record = read_csv(S / "stash-untracked-tree-verification.csv")
    require(len(incoming) == len(scope) == len(stash_record) == 868, "not 868 scoped paths")
    by_path = {r["repository_relative_path"]: r for r in incoming}
    require(len(by_path) == 868, "duplicate initial path")
    require({r["repository_relative_path"] for r in scope} == set(by_path), "entry scope differs")
    require(sum(int(r["bytes"]) for r in incoming) == 46_015_150, "initial bytes differ")
    require(Counter(r["comparison"] for r in incoming) ==
            {"same_as_remote": 836, "different_from_remote": 32}, "initial comparison differs")
    tree = tree_entries(BASE)
    for name, row in by_path.items():
        require(tree.get(name) == row["remote_blob_sha1"], "baseline remote tree does not match ledger")
        if row["comparison"] == "same_as_remote":
            require(row["worktree_blob_sha1"] == row["remote_blob_sha1"], "same blob mismatch")
        else:
            require(row["worktree_blob_sha1"] != row["remote_blob_sha1"], "different blob mismatch")

    require(len(saved) == len(prior) == 32, "protected-variant count differs")
    require({r["original_path"] for r in saved} ==
            {n for n, r in by_path.items() if r["comparison"] == "different_from_remote"},
            "protected variants do not cover all differences")
    total = 0
    for row in saved:
        data = (ROOT / row["protected_path"]).read_bytes()
        checked_bytes(data, int(row["bytes"]), row["sha256"], "protected variant")
        original = by_path[row["original_path"]]
        require(row["sha256"] == original["sha256"], "protected SHA differs from incoming")
        require(blob_digest(data) == original["worktree_blob_sha1"], "protected Git blob differs")
        total += len(data)
    require(total == 17_473_261, "protected byte total differs")
    require(Counter(r["exactly_matches_prior_protected_copy"] for r in prior) ==
            {"True": 31, "False": 1}, "prior protected-copy comparison differs")
    for row in prior:
        current = (ROOT / row["current_protected_path"]).read_bytes()
        require(digest(current) == row["current_sha256"], "current variant digest differs")
        if row["exactly_matches_prior_protected_copy"] == "True":
            previous = (ROOT / row["prior_protected_path"]).read_bytes()
            require(previous == current and digest(previous) == row["prior_sha256"],
                    "prior protected copy differs")
    records = {r["repository_relative_path"]: r for r in stash_record}
    require(set(records) == set(by_path), "recorded stash paths differ")
    for name, row in records.items():
        require(row["exact_blob_equal"] == "True", "recorded stash mismatch")
        require(row["stash_blob_sha1"] == row["worktree_blob_sha1_before_stash"] ==
                by_path[name]["worktree_blob_sha1"], "recorded stash blob differs")
    if git("cat-file", "-e", f"{STASH}^{{commit}}", check=False).returncode == 0:
        stashed = tree_entries(f"{STASH}^3")
        require(set(stashed) == set(by_path), "available stash tree paths differ")
        for name, row in by_path.items():
            require(stashed[name] == row["worktree_blob_sha1"], "available stash blob differs")
        stash_note = "local stash tree reverified"
    else:
        stash_note = "local stash unavailable; persisted verification record only"
    print(f"PASS 868 entry paths, 32 protected variants, 31 prior copies; {stash_note}")


def verify_appends() -> dict[str, dict[str, str]]:
    plans = read_csv(E / "append-plan-before-write.csv")
    logs = read_csv(E / "append-log.csv")
    require(len(plans) == len(logs) == 2, "append count differs")
    indexed = {r["repository_relative_path"]: r for r in logs}
    require(len(indexed) == 2, "duplicate append target")
    historical = {r["repository_relative_path"]: r for r in
                  read_csv(S / "historical-append-final-read-inventory.csv")}
    require(len(historical) == 9, "historical append-chain size differs")
    for plan in plans:
        name = plan["repository_relative_path"]
        require(name in indexed and name in historical, "append target outside prior chain")
        log = indexed[name]
        before = git("show", f"{BASE}:{name}").stdout
        suffix = (ROOT / plan["addition_path"]).read_bytes()
        after = (ROOT / name).read_bytes()
        checked_bytes(before, int(plan["prior_bytes"]), plan["prior_sha256"], "prior append prefix")
        checked_bytes(suffix, int(plan["addition_bytes"]), plan["addition_sha256"], "planned suffix")
        checked_append(before, suffix, after, plan["prior_sha256"], plan["planned_new_sha256"])
        require(len(after) == int(plan["planned_new_bytes"]), "new append byte count differs")
        require(log["prior_prefix_byte_identical"] == "True" and
                log["prior_sha256"] == plan["prior_sha256"] and
                log["new_sha256"] == plan["planned_new_sha256"], "append log differs")
        require(historical[name]["sha256"] == plan["prior_sha256"], "prior chain SHA differs")
    for name, row in historical.items():
        data = (ROOT / name).read_bytes()
        if name in indexed:
            data = data[:int(row["bytes"])]
        checked_bytes(data, int(row["bytes"]), row["sha256"], "historical append chain")
    print("PASS 2 append-only files and all 9 previous chain prefixes")
    return indexed


def verify_local(appended: dict[str, dict[str, str]]) -> None:
    groups = [
        ("local-scope-before-read.csv", "local-read-inventory.csv", 40),
        ("supplemental-local-scope-before-read.csv", "supplemental-local-read-inventory.csv", 5),
        ("training-local-scope-before-read.csv", "training-local-read-inventory.csv", 2),
        ("comparison-local-scope-before-read.csv", "comparison-local-read-inventory.csv", 1),
        ("comparison-social-scope-before-read.csv", "comparison-social-read-inventory.csv", 1),
    ]
    all_rows: list[dict[str, str]] = []
    for scope_name, inventory_name, count in groups:
        scope, inventory = read_csv(E / scope_name), read_csv(E / inventory_name)
        require(len(scope) == len(inventory) == count, f"local scope count differs: {scope_name}")
        require([r["repository_relative_path"] for r in scope] ==
                [r["repository_relative_path"] for r in inventory], "scope/inventory order differs")
        for before, row in zip(scope, inventory):
            name = row["repository_relative_path"]
            require(before["bytes_before_read"] == row["bytes_before_read"] == row["bytes_read"],
                    "recorded local byte counts differ")
            require(row["full_bytes_read"] == "True", "incomplete local byte read")
            data = (ROOT / name).read_bytes()
            if name in appended:
                data = data[:int(row["bytes_read"])]
            checked_bytes(data, int(row["bytes_read"]), row["sha256"], "local inventory")
        all_rows.extend(inventory)
    names = {r["repository_relative_path"] for r in all_rows}
    require(len(names) == len(all_rows) == 49, "local paths are not 49 unique paths")
    require(sum(int(r["bytes_read"]) for r in all_rows) == 828_240, "local byte sum differs")
    prev_dir = I / "57-source-evidence-r108-2026-10-26"
    prev = read_csv(prev_dir / "local-read-inventory.csv") + read_csv(prev_dir / "social-selection-read-inventory.csv")
    prev_names = {r["repository_relative_path"] for r in prev}
    require(len(prev_names) == 24 and len(prev_names & names) == 10, "r108/r109 overlap differs")
    cmp_rows = read_csv(E / "local-scope-r108-r109-comparison.csv")
    require(len(cmp_rows) == len(prev_names | names) == 63, "comparison table size differs")
    require({r["repository_relative_path"] for r in cmp_rows} == prev_names | names,
            "comparison table paths differ")
    for row in cmp_rows:
        name = row["repository_relative_path"]
        require(row["r108"] == str(name in prev_names) and row["r109"] == str(name in names),
                "comparison membership differs")
    print("PASS 49/49 scoped byte reads (828,240 bytes) and 10-path overlap with r108")


def verify_sources(appended: dict[str, dict[str, str]]) -> None:
    sources = read_csv(E / "source-catalog.csv")
    require(len(sources) == 9 and len({r["source_id"] for r in sources}) == 9,
            "source catalog count differs")
    catalog = {r["source_id"]: r for r in sources}
    require(sum(int(r["bytes"]) for r in sources) == 101_321, "source byte total differs")
    for row in sources:
        name = row["repository_relative_path"]
        data = (ROOT / name).read_bytes()
        if name in appended:
            data = data[:int(row["bytes"])]
        checked_bytes(data, int(row["bytes"]), row["sha256"], "catalog source")
    anchors = read_csv(E / "evidence-traceability.csv")
    ids = {r["anchor_id"] for r in anchors}
    require(len(anchors) == len(ids) == 44, "anchor count differs")
    for row in anchors:
        source = catalog[row["source_id"]]
        require(row["repository_relative_path"] == source["repository_relative_path"],
                "anchor source path differs")
        lines = (ROOT / row["repository_relative_path"]).read_text(encoding="utf-8").splitlines()
        number = int(row["line_1_based"])
        require(1 <= number <= len(lines), "anchor line number out of range")
        line = lines[number - 1]
        require(len(line.encode("utf-8")) == int(row["source_line_utf8_bytes"]),
                "anchor line bytes differ")
        checked_line(line, row["exact_substring"], row["full_saved_source_line"], row["source_line_sha256"])
    for filename, expected in (("lifecycle-claim-boundaries.csv", 14), ("issues-and-corrections.csv", 8)):
        rows = read_csv(E / filename)
        require(len(rows) == expected, f"matrix count differs: {filename}")
        for row in rows:
            require(set(row["anchor_ids"].split(";")) <= ids, "matrix refers to unknown anchor")
    require(len(read_csv(E / "training-visible-paragraph-check.csv")) == 4,
            "bilingual comparison count differs")
    tr = (ROOT / catalog["S07"]["repository_relative_path"]).read_text(encoding="utf-8").splitlines()
    en = (ROOT / catalog["S08"]["repository_relative_path"]).read_text(encoding="utf-8").splitlines()
    phrase = "Angora Networks works hard to support its customers with the highest quality products and services."
    require(en[10].count(phrase) == 2, "English repeated sentence count differs")
    require("Eğitim, önleyici desteğin çok önemli bir parçasıdır" in tr[10],
            "Turkish preventive-support sentence missing")
    require(not any("preventive" in line.casefold() for line in en), "unexpected English preventive literal")
    print("PASS 9 separate saved artifacts, 44 exact full-line anchors and bilingual text comparison")


def verify_fetch_records() -> None:
    direct_plan = read_csv(E / "external-fetch-plan-before-fetch.csv")
    alias_plan = read_csv(E / "external-alias-plan-before-fetch.csv")
    direct = read_csv(E / "external-fetch-attempts-01.csv")
    aliases = read_csv(E / "external-fetch-attempts-02.csv")
    require(len(direct_plan) == len(direct) == 5 and len(alias_plan) == len(aliases) == 3,
            "target fetch counts differ")
    require({r["source_id"] for r in direct_plan} == {r["source_id"] for r in direct}, "direct plan differs")
    require({r["source_id"] for r in alias_plan} == {r["source_id"] for r in aliases}, "alias plan differs")
    for row in direct + aliases:
        require(row["status"] == "error" and row["chunk_index"] == "0" and
                row["tool_message"] == "Failed to fetch page", "unexpected target fetch status")
        require(".pdf" not in row["attempted_url"].lower(), "PDF was in targeted fetch plan")
    require(len(read_csv(E / "discovery-plan-before-search.csv")) == 5 and
            len(read_csv(E / "discovery-events-plan-before-search.csv")) == 3,
            "discovery query count differs")
    require(len(read_csv(E / "discovery-metadata.csv")) == 24 and
            len(read_csv(E / "discovery-events-metadata.csv")) == 12, "discovery result count differs")
    for name in ("GH01A", "GH02A", "GH03A", "GR01", "GR02"):
        result = json.loads((E / f"github-api-{name}.json").read_text(encoding="utf-8"))
        require(result["total_count"] == 0 and result["items"] == [], "GitHub search result differs")
    account = json.loads((E / "github-api-GR03.json").read_text(encoding="utf-8"))
    require(account["status"] == "error" and "404" in account["message"], "GitHub account result differs")
    print("PASS 8 recorded target fetch failures, 8 discovery queries, and GitHub metadata results")


def verify_links() -> None:
    docs = [
        W / "08-customer-pipeline/178-angora-product-lifecycle-evidence-r109-2026-10-26.md",
        W / "09-orders/120-angora-orders-dossier-2026-10-21.r109-appendix.md",
        W / "09-orders/120-angora-orders-master-2026-10-21.mapping-r109.md",
        I / "62-followup-angora-r109-2026-10-26/angora-networks.md",
        I / "63-audit-r109-2026-10-26.md", E / "README.md",
        E / "append-planned-social.md", E / "append-planned-dossier.md",
    ]
    count = 0
    for doc in docs:
        require(doc.is_file(), f"missing report: {doc}")
        # Planned append texts are snippets relative to their respective destination files.
        parent = doc.parent
        if doc.name == "append-planned-social.md":
            parent = W / "02-social-intel"
        elif doc.name == "append-planned-dossier.md":
            parent = W / "09-orders"
        for target in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("#"):
                continue
            resolved = (parent / unquote(parsed.path)).resolve()
            require(resolved.is_relative_to(ROOT), f"link leaves workspace: {doc} -> {target}")
            require(resolved.exists(), f"missing link: {doc} -> {target}")
            count += 1
    print(f"PASS {count} local report links")


def negative_tests() -> None:
    original = b"old source\n"
    suffix = b"new appendix\n"
    old_sha, new_sha = digest(original), digest(original + suffix)
    line = "Angora saved line"
    line_sha = digest(line.encode("utf-8"))
    tests = [
        lambda: checked_bytes(b"bad", len(original), old_sha, "negative"),
        lambda: checked_bytes(original, len(original) + 1, old_sha, "negative"),
        lambda: checked_bytes(original, len(original), "0" * 64, "negative"),
        lambda: checked_append(original, suffix, b"changed\n" + suffix, old_sha, new_sha),
        lambda: checked_append(original, suffix, original + b"changed\n", old_sha, new_sha),
        lambda: checked_append(original, suffix, original + suffix, "0" * 64, new_sha),
        lambda: checked_append(original, suffix, original + suffix, old_sha, "0" * 64),
        lambda: checked_line(line, "missing", line, line_sha),
        lambda: checked_line(line, "Angora", line + "x", line_sha),
        lambda: checked_line(line, "Angora", line, "0" * 64),
        lambda: require(blob_digest(b"a") == blob_digest(b"b"), "Git blob differs"),
        lambda: require(len({"same", "same"}) == 2, "duplicate paths"),
    ]
    for number, test in enumerate(tests, 1):
        try:
            test()
        except AssertionError:
            continue
        raise AssertionError(f"negative test unexpectedly passed: {number}")
    print(f"PASS {len(tests)} in-memory corruption/duplicate negative tests")


def main() -> int:
    try:
        verify_branch()
        verify_safety()
        appended = verify_appends()
        verify_local(appended)
        verify_sources(appended)
        verify_fetch_records()
        verify_links()
        negative_tests()
    except (AssertionError, OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        print(f"FAIL {error}", file=sys.stderr)
        return 1
    print("r109 verification PASS (byte and linkage checks only)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
