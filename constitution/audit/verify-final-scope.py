#!/usr/bin/env python3
"""One-shot, bounded final readback; scope CSV is written before this program runs."""
import csv
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "constitution/audit"
SCOPE = D / "final-full-scope-before-read.csv"
INVENTORY = D / "final-full-read-inventory.csv"
RESULT = D / "final-crosscheck-result.json"
C = ROOT / "constitution"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(value, message):
    if not value:
        raise AssertionError(message)


def check(name, fn, results):
    try:
        detail = fn()
        results[name] = {"ok": True, "detail": detail}
    except Exception as exc:
        results[name] = {"ok": False, "detail": f"{type(exc).__name__}: {exc}"}


def source_payload(metadata):
    names = [name for name in metadata["files"] if name.startswith("files/")]
    require(len(names) == 1, f"expected one source payload in {metadata['id']}")
    return C / "records/sources" / metadata["id"] / names[0]


def main():
    rows = list(csv.DictReader(SCOPE.open(encoding="utf-8", newline="")))
    contents, read_errors = {}, []
    with INVENTORY.open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["path", "listed_bytes", "bytes_read", "sha256", "outcome"], lineterminator="\n")
        writer.writeheader()
        for row in rows:
            name = row["path"]
            try:
                p = ROOT / name
                require(not p.is_symlink() and p.is_file(), "not a regular file")
                data = p.read_bytes()
                require(len(data) == int(row["listed_bytes"]), "size changed since listing")
                contents[name] = data
                writer.writerow({"path": name, "listed_bytes": row["listed_bytes"], "bytes_read": len(data),
                                 "sha256": hashlib.sha256(data).hexdigest(), "outcome": "read"})
            except (OSError, ValueError, AssertionError) as exc:
                read_errors.append(f"{name}: {exc}")
                writer.writerow({"path": name, "listed_bytes": row["listed_bytes"], "bytes_read": "", "sha256": "", "outcome": f"failed: {exc}"})
            stream.flush()
    results = {}
    message_meta = [read_json(path) for path in sorted((C / "records/messages").glob("*/metadata.json"))]
    source_meta = [read_json(path) for path in sorted((C / "records/sources").glob("*/metadata.json"))]
    source_by_id = {item["id"]: item for item in source_meta}

    def full_read():
        require(not read_errors, "; ".join(read_errors))
        require(len(contents) == len(rows), "scope count mismatch")
        return {"listed": len(rows), "read": len(contents), "bytes": sum(len(x) for x in contents.values())}

    def messages():
        inbox = sorted(p for p in (C / "inbox").rglob("*") if p.is_file())
        for p in inbox:
            rel = p.relative_to(ROOT).as_posix()
            matches = [m for m in message_meta if m.get("input_path") == rel]
            require(len(matches) == 1, f"{rel}: expected one record, got {len(matches)}")
            m = matches[0]
            expected_role = "user" if "user-messages" in p.parts else "assistant"
            require(m.get("role") == expected_role, f"role mismatch: {rel}")
            require((C / "records/messages" / m["id"] / "message.bin").read_bytes() == p.read_bytes(), f"bytes mismatch: {rel}")
            require(m.get("event_at_beijing") is None and m.get("event_time_source") is None, f"invented event time: {rel}")
            require("unverified" in m.get("clock_provenance", ""), f"missing clock caveat: {rel}")
        require(len(inbox) == len(message_meta), "extra message record or missing inbox item")
        return {"inbox_files": len(inbox), "matching_message_records": len(message_meta), "upstream_fidelity": "not independently established"}

    def rules():
        files = sorted((C / "rules").glob("*.md"))
        require(len(files) == 6, "not six independent rule files")
        identifiers = set()
        for p in files:
            rel = p.relative_to(ROOT).as_posix()
            candidates = [m for m in source_meta if m.get("original_relative_path") == rel]
            require(len(candidates) == 1, f"rule source count: {rel}")
            require(source_payload(candidates[0]).read_bytes() == p.read_bytes(), f"rule bytes differ: {rel}")
            identifiers.add(candidates[0]["id"])
        require(len(identifiers) == 6, "rules were not stored as separate sources")
        return {"separate_rules": len(files), "independent_source_records": len(identifiers)}

    def versions():
        counts = {}
        for original in ("constitution/policies/publication-consent.md", "constitution/README.md",
                         "tools/constitution_ledger.py", "tools/test_constitution_ledger.py"):
            candidates = [m for m in source_meta if m.get("original_relative_path") == original]
            minimum = 3 if original == "constitution/README.md" else 2
            require(len(candidates) == minimum, f"{original}: expected {minimum} versions, found {len(candidates)}")
            roots = [m for m in candidates if not m.get("supersedes_record_id")]
            require(len(roots) == 1, f"{original}: version root mismatch")
            visited = [roots[0]]
            while True:
                children = [m for m in candidates if m.get("supersedes_record_id") == visited[-1]["id"]]
                require(len(children) <= 1, f"{original}: ambiguous chain")
                if not children:
                    break
                require(children[0] not in visited, "version cycle")
                visited.append(children[0])
            require(len(visited) == len(candidates), f"{original}: disconnected versions")
            require(source_payload(visited[-1]).read_bytes() == (ROOT / original).read_bytes(), f"{original}: latest bytes differ")
            counts[original] = len(visited)
        for ref, name, copy in [
            ("adec2a0", "constitution/README.md", "constitution/history/README-checkpoint-adec2a0.md"),
            ("adec2a0", "constitution/policies/publication-consent.md", "ingest/angora-1__arena-01a0ce39__5acb613/96-entry-safety-privacy-reset/protected-new-inputs/constitution/policies/publication-consent.md"),
            ("cb1246f", "tools/constitution_ledger.py", "constitution/history/constitution_ledger.py.cb1246f.txt"),
            ("cb1246f", "tools/test_constitution_ledger.py", "constitution/history/test_constitution_ledger.py.cb1246f.txt")]:
            obj = subprocess.check_output(["git", "show", ref + ":" + name], cwd=ROOT)
            require(obj == (ROOT / copy).read_bytes(), f"old copy differs from Git: {name}")
        return {"version_counts": counts, "old_git_blob_copies_compared": 4}

    def publication():
        decision = read_json(C / "inbox/user-messages/privacy-answer-0002.json")
        require(decision["answers"][0]["selectedOptionId"] == "publish_all", "unexpected user choice")
        repo = json.loads((C / "evidence/github/recheck.stdout.bin").read_bytes())
        require(repo["nameWithOwner"] == "SimonSaga-202306/Angora" and repo["isPrivate"] is False, "repo visibility mismatch")
        return {"user_choice": "publish_all", "repo_is_private": False, "credential_exception_retained": True}

    def time_evidence():
        crawls = [read_json(p) for p in (C / "records/crawls").glob("*/metadata.json")]
        relevant = [x for x in crawls if x.get("requested_url") == "https://time.is/Beijing"]
        require(len(relevant) == 1, "direct time.is attempt count mismatch")
        crawl = relevant[0]
        require(crawl["outcome"] == "recorded_with_failure" and crawl["body_present"] is False and crawl["http_status"] is None, "failure misrepresented")
        require((C / "records/crawls" / crawl["id"] / "failure.txt").is_file(), "missing direct failure")
        first = read_json(C / "evidence/time-is/fetch-page-post-reset/transcription-check-result.json")
        second = read_json(C / "evidence/time-is/fetch-page-post-reset/transcription-check-result-02.json")
        require(first["checks"]["city_count_50"] is False and second["observed_city_count"] == 49, "city count history mismatch")
        require(all(second["checks"].values()), "second transcription check failed")
        return {"raw_html_obtained": False, "fetch_failure_preserved": True, "observed_cities": 49, "count_discrepancy_reason": "unknown"}

    def tests_and_snapshot():
        test = read_json(C / "audit/rebuilt-test-02.result.json")
        log = (C / "audit/rebuilt-test-02.stderr.bin").read_bytes()
        require(test["exit_code"] == 0 and b"Ran 34 tests" in log and b"\nOK\n" in log, "34-test run not confirmed")
        prior_failure = read_json(C / "audit/symlink-gap-before-fix.result.json")
        require(prior_failure["exit_code"] != 0, "repair-before result missing")
        v = read_json(C / "audit/snapshot-02-verify.stdout.bin")
        require(v["outcome"] == "ok" and v["records_with_logged_failures"] == 1 and not v["snapshot"]["new_files_since_snapshot"], "snapshot verification mismatch")
        return {"offline_tests": 34, "test_exit_code": 0, "snapshot_records": v["records_checked"], "logged_fetch_failures": 1}

    def recovery():
        p = ROOT / "ingest/angora-1__arena-01a0ce39__5acb613/96-entry-safety-privacy-reset"
        r = read_json(p / "full-read-and-comparison-summary.json")
        s = read_json(p / "stash-third-parent-verification.json")
        require((r["original_paths"], r["same_path_byte_identical"], r["other_path_byte_identical"]) == (868, 836, 32), "remote entry comparison mismatch")
        require(s["matching_path_and_blob"] == 868 and s["new_inputs_and_safety_directory_excluded"], "stash verification mismatch")
        require(subprocess.run(["git", "cat-file", "-e", s["stash_commit"] + "^{commit}"], cwd=ROOT).returncode == 0, "stash object absent in this environment")
        return {"original_paths": 868, "remote_same_path": 836, "remote_other_path": 32, "stash_checked_now": True, "stash_not_durable": True}

    def links():
        targets = [ROOT / "AGENTS.md", C / "README.md", C / "OPERATING-GUIDE.md"]
        targets += sorted((C / "rules").glob("*.md")) + sorted((C / "policies").glob("*.md")) + sorted((C / "issues").glob("*.md"))
        bad, checked = [], 0
        for p in targets:
            for raw in re.findall(r"\]\(([^)]+)\)", p.read_text(encoding="utf-8")):
                target = raw.split(" ", 1)[0]
                parsed = urlsplit(target)
                if parsed.scheme or target.startswith("#"):
                    continue
                local = unquote(parsed.path)
                if not local:
                    continue
                checked += 1
                if not (p.parent / local).exists():
                    bad.append(f"{p.relative_to(ROOT)} -> {target}")
        require(not bad, "broken local links: " + "; ".join(bad))
        return {"markdown_files": len(targets), "local_links_checked": checked}

    def secrets():
        patterns = (rb"ghp_[A-Za-z0-9]{36}", rb"github_pat_[A-Za-z0-9_]{50,}",
                    rb"AIza[A-Za-z0-9_-]{35}", rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")
        flagged = []
        for path, data in contents.items():
            if any(re.search(pattern, data) for pattern in patterns):
                flagged.append(path)
        require(not flagged, "potential secret pattern in: " + ", ".join(flagged))
        return {"files_scanned": len(contents), "patterns": len(patterns), "limitation": "limited patterns cannot prove absence of credentials"}

    for name, fn in (("full_read", full_read), ("message_mapping", messages), ("six_rules", rules),
                     ("version_chains_and_old_git_copies", versions), ("public_consent", publication),
                     ("time_source_limitations", time_evidence), ("tests_and_snapshot", tests_and_snapshot),
                     ("entry_recovery", recovery), ("local_links", links), ("limited_secret_patterns", secrets)):
        check(name, fn, results)
    report = {"outcome": "ok" if all(v["ok"] for v in results.values()) else "failed",
              "checks": results,
              "scope_note": "only prelisted paths; excludes this report, inventory, scope CSV and later files",
              "limits": "no proof of missing historical chat, platform transport bytes, webpage truth, or absolute completeness"}
    with RESULT.open("x", encoding="utf-8") as stream:
        json.dump(report, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["outcome"] == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
