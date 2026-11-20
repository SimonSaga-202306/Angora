#!/usr/bin/env python3
"""Per-item, append-only evidence ledger; not an automatic platform chat hook."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from datetime import datetime
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parent.parent
DEFAULT_ROOT = REPO / "constitution"
ZONE = ZoneInfo("Asia/Shanghai")
SCHEMA = "constitution-ledger/v1"
BUCKETS = {"messages", "sources", "events", "crawls"}
MAX_FETCH = 64 * 1024 * 1024
DEFAULT_FETCH = 16 * 1024 * 1024
SECRET_PARTS = ("token", "secret", "signature", "password", "credential", "authorization")
SECRET_KEYS = {"api_key", "apikey", "key", "sig", "auth", "session", "code"}
SECRET_HEADERS = {"set-cookie", "set-cookie2", "cookie", "authorization", "proxy-authorization", "x-api-key", "authentication-info"}


def now_beijing() -> str:
    return datetime.now(ZONE).isoformat(timespec="microseconds")


def to_beijing(value: str) -> str:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (ValueError, AttributeError) as exc:
        raise ValueError("event time must be ISO 8601 with explicit timezone") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("event time needs an explicit timezone offset")
    return parsed.astimezone(ZONE).isoformat(timespec="microseconds")


def times(event_at=None, event_source=None) -> dict:
    if bool(event_at) != bool(event_source):
        raise ValueError("--event-at and --event-time-source must be supplied together")
    return {"event_at_beijing": to_beijing(event_at) if event_at else None,
            "event_time_source": event_source, "event_time_input_original": event_at,
            "recorded_at_beijing_unverified": now_beijing(),
            "clock_provenance": "system wall clock, Asia/Shanghai; synchronization and event time unverified"}


def relative_path(value: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        raise ValueError("path must be a nonempty POSIX relative path")
    path = PurePosixPath(value)
    if path.is_absolute() or any(p in (".", "..") for p in value.split("/")) or str(path) != value:
        raise ValueError("path must be normalized, relative, and contain no traversal")
    return str(path)


def inspect_url(url: str):
    try:
        parts = urllib.parse.urlsplit(url)
        if parts.scheme not in ("http", "https") or not parts.hostname:
            return None, "only absolute http(s) URLs with a hostname are accepted; URL withheld"
        if parts.username is not None or parts.password is not None:
            return None, "URL userinfo is not accepted; URL withheld"
        for key, _ in urllib.parse.parse_qsl(parts.query, keep_blank_values=True):
            lower = key.lower()
            if lower in SECRET_KEYS or any(term in lower for term in SECRET_PARTS):
                return None, "potential credential-bearing query is not accepted; URL withheld"
        if any(term in parts.fragment.lower() for term in SECRET_PARTS):
            return None, "potential credential-bearing fragment is not accepted; URL withheld"
        _ = parts.port
        return parts, None
    except ValueError:
        return None, "invalid URL; URL withheld"


def response_path(parts) -> str:
    host = urllib.parse.quote(parts.hostname or "unknown", safe=".-")
    segments = []
    for segment in parts.path.split("/"):
        if not segment:
            continue
        if segment in (".", ".."):
            segment = "%2E" * len(segment)
        segments.append(urllib.parse.quote(segment, safe="%._~-"))
    if not segments or parts.path.endswith("/"):
        segments.append("index.response")
    return relative_path("files/" + "/".join([host, *segments]))


def encode(obj) -> bytes:
    return (json.dumps(obj, ensure_ascii=True, indent=2) + "\n").encode("utf-8")


def write_new(path: Path, data: bytes):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(data)


def digest(path: Path) -> dict:
    h = hashlib.sha256()
    n = 0
    with path.open("rb") as stream:
        while chunk := stream.read(1024 * 1024):
            h.update(chunk)
            n += len(chunk)
    return {"bytes": n, "sha256": h.hexdigest()}


def allocate(root: Path, bucket: str):
    if bucket not in BUCKETS and bucket != "snapshots":
        raise ValueError("invalid record bucket")
    parent = root / ("snapshots" if bucket == "snapshots" else "records")
    if parent.is_symlink():
        raise ValueError("ledger directory must not be a symlink")
    parent.mkdir(parents=True, exist_ok=True)
    if bucket != "snapshots":
        parent = parent / bucket
        if parent.is_symlink():
            raise ValueError("record bucket must not be a symlink")
        parent.mkdir(exist_ok=True)
    for _ in range(10):
        ident = uuid.uuid4().hex
        record = parent / ident
        try:
            record.mkdir()
            return ident, record
        except FileExistsError:
            pass
    raise RuntimeError("could not allocate a unique record directory")


def add_data(files, record: Path, name: str, data: bytes):
    name = relative_path(name)
    write_new(record / name, data)
    files[name] = digest(record / name)


def finish(record: Path, meta: dict, files: dict):
    meta["files"] = files
    write_new(record / "metadata.json", encode(meta))


def check_previous(root: Path, bucket: str, ident: str | None):
    if ident is None:
        return
    if len(ident) != 32 or any(c not in "0123456789abcdef" for c in ident):
        raise ValueError("--supersedes must be a 32-character record ID")
    if not (root / "records" / bucket / ident / "metadata.json").is_file():
        raise ValueError("--supersedes must reference an existing record of the same type")


def capture_copy(root: Path, args, bucket: str):
    tf = times(args.event_at, args.event_time_source)
    check_previous(root, bucket, args.supersedes)
    if bucket == "sources":
        original = relative_path(args.original_path)
        if args.source_uri:
            _, problem = inspect_url(args.source_uri)
            if problem:
                raise ValueError(problem)
        payload = "files/" + original
    else:
        original = None
        payload = "message.bin" if bucket == "messages" else "event.bin"
    ident, record = allocate(root, bucket)
    meta = {"schema": SCHEMA, "id": ident, "type": bucket[:-1], **tf,
            "capture_method": args.method,
            "fidelity": "exact copy of supplied input only; upstream completeness and protocol bytes are not assumed",
            "input_path": args.file, "supersedes_record_id": args.supersedes, "note": args.note}
    if bucket == "messages":
        meta["role"] = args.role
    elif bucket == "sources":
        meta.update({"original_relative_path": original, "source_uri": args.source_uri})
    else:
        meta["event_kind"] = args.event_kind
    failures = []
    files = {}
    target = record / payload
    before = None
    try:
        if args.file == "-":
            source = sys.stdin.buffer
        else:
            before = Path(args.file).stat()
            source = Path(args.file).open("rb")
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as output:
                while chunk := source.read(1024 * 1024):
                    output.write(chunk)
        finally:
            if args.file != "-":
                source.close()
        if before is not None:
            after = Path(args.file).stat()
            if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
                failures.append("source changed while copying; completeness unverified")
    except (OSError, ValueError) as exc:
        failures.append(f"copy failed: {type(exc).__name__}: {exc}")
    if target.is_file():
        files[payload] = digest(target)
    if failures:
        add_data(files, record, "failure.txt", ("\n".join(failures) + "\n").encode())
    meta["outcome"] = "partial_or_failed" if failures else "copied"
    finish(record, meta, files)
    return {"id": ident, "record_dir": str(record), "outcome": meta["outcome"]}, 2 if failures else 0


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def capture_fetch(root: Path, args):
    if not args.authorization_note.strip():
        raise ValueError("a non-secret authorization note is required")
    if not 0 < args.max_bytes <= MAX_FETCH:
        raise ValueError(f"--max-bytes must be between 1 and {MAX_FETCH}")
    if not 0 < args.timeout <= 120:
        raise ValueError("--timeout must be greater than zero and at most 120 seconds")
    parts, problem = inspect_url(args.url)
    ident, record = allocate(root, "crawls")
    start = time.monotonic()
    meta = {"schema": SCHEMA, "id": ident, "type": "crawl", **times(),
            "authorization_note": args.authorization_note, "requested_url": args.url if not problem else None,
            "requested_url_withheld_reason": problem, "request_method": "GET", "redirects_followed": False,
            "request_authentication": "none supplied by this tool",
            "headers_representation": "client-parsed pairs, not raw wire headers; sensitive headers redacted",
            "body_representation": "HTTP entity bytes exposed by client after HTTP framing, not a raw network packet",
            "max_bytes": args.max_bytes}
    failures, files, headers = [], {}, []
    response = None
    status = None
    body_present = body_complete = truncated = False
    if problem:
        failures.append(problem)
    else:
        req = urllib.request.Request(args.url, method="GET", headers={"User-Agent": "Angora-constitution-archive/1", "Accept-Encoding": "identity"})
        try:
            response = urllib.request.build_opener(NoRedirect()).open(req, timeout=args.timeout)
        except urllib.error.HTTPError as exc:
            response = exc  # error/redirect responses are still readable
        except Exception as exc:
            failures.append(f"transport failed: {type(exc).__name__}: {exc}")
        if response is not None:
            body_path = None
            try:
                status = int(response.status)
                for name, value in response.headers.raw_items():
                    redact = name.lower() in SECRET_HEADERS
                    if name.lower() == "location":
                        _, location_problem = inspect_url(urllib.parse.urljoin(args.url, value))
                        redact = redact or bool(location_problem)
                    headers.append([name, "[REDACTED]" if redact else value])
                relative = response_path(parts)
                body_path = record / relative
                body_path.parent.mkdir(parents=True, exist_ok=True)
                received = 0
                with body_path.open("xb") as output:
                    body_present = True
                    while True:
                        try:
                            chunk = response.read(min(65536, max(1, args.max_bytes + 1 - received)))
                        except Exception as exc:
                            partial = getattr(exc, "partial", b"")
                            if isinstance(partial, bytes) and partial:
                                output.write(partial)
                                received += len(partial)
                            failures.append(f"body read failed: {type(exc).__name__}: {exc}")
                            break
                        if not chunk:
                            body_complete = True
                            break
                        output.write(chunk)
                        received += len(chunk)
                        if received > args.max_bytes:
                            truncated = True
                            failures.append("body exceeds size limit; saved received prefix including one probe byte")
                            break
                files[relative] = digest(body_path)
                expected = response.headers.get("Content-Length")
                if body_complete and expected and expected.isdigit() and status not in (204, 304) and received != int(expected):
                    body_complete = False
                    failures.append(f"Content-Length mismatch: expected {expected}, received {received}")
                if not 200 <= status < 300:
                    failures.append(f"HTTP status {status}; redirect, if any, was not followed")
            except Exception as exc:
                failures.append(f"response capture failed: {type(exc).__name__}: {exc}")
                if body_path is not None and body_path.is_file():
                    files[relative] = digest(body_path)
            finally:
                try:
                    response.close()
                except Exception as exc:
                    failures.append(f"response close failed: {type(exc).__name__}: {exc}")
    add_data(files, record, "response-headers.json", encode({"response_present": response is not None,
             "representation": meta["headers_representation"], "headers": headers}))
    if failures:
        add_data(files, record, "failure.txt", ("\n".join(failures) + "\n").encode())
    meta.update({"http_status": status, "body_present": body_present, "body_complete": body_complete,
                 "truncated_by_limit": truncated, "outcome": "recorded_with_failure" if failures else "complete",
                 "finished_at_beijing_unverified": now_beijing(),
                 "elapsed_monotonic_seconds_same_process": round(time.monotonic() - start, 6)})
    finish(record, meta, files)
    return {"id": ident, "record_dir": str(record), "outcome": meta["outcome"], "http_status": status}, 2 if failures else 0


def list_files(root: Path):
    base = root / "records"
    if not base.exists():
        return []
    entries = []
    for directory, dirs, names in os.walk(base, followlinks=False):
        dirs.sort()
        names.sort()
        keep = []
        for name in dirs:
            path = Path(directory) / name
            if path.is_symlink():
                entries.append({"path": path.relative_to(root).as_posix(), "listed_bytes": None, "kind": "symlink"})
            else:
                keep.append(name)
        dirs[:] = keep
        for name in names:
            path = Path(directory) / name
            entries.append({"path": path.relative_to(root).as_posix(),
                            "listed_bytes": None if path.is_symlink() else path.stat().st_size,
                            "kind": "symlink" if path.is_symlink() else "file"})
    return sorted(entries, key=lambda x: x["path"])


def snapshot(root: Path):
    ident, directory = allocate(root, "snapshots")
    scope = {"schema": SCHEMA, "id": ident, "listed_at_beijing_unverified": now_beijing(),
             "clock_provenance": "system wall clock, synchronization unverified", "files": list_files(root)}
    scope_bytes = encode(scope)
    write_new(directory / "scope.json", scope_bytes)  # list first, then read
    entries, errors = [], []
    for item in scope["files"]:
        path = root / item["path"]
        if item["kind"] != "file":
            errors.append(f"not a regular file: {item['path']}")
            continue
        try:
            before = path.stat()
            result = digest(path)
            after = path.stat()
            if result["bytes"] != item["listed_bytes"] or (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
                errors.append(f"file changed since listing or during read: {item['path']}")
            entries.append({"path": item["path"], **result})
        except OSError as exc:
            errors.append(f"read failed: {item['path']}: {type(exc).__name__}: {exc}")
    manifest = {"schema": SCHEMA, "id": ident, "scope_sha256": hashlib.sha256(scope_bytes).hexdigest(),
                "finished_at_beijing_unverified": now_beijing(), "files": entries, "errors": errors,
                "outcome": "complete" if not errors else "partial"}
    write_new(directory / "manifest.json", encode(manifest))
    return {"id": ident, "directory": str(directory), "listed": len(scope["files"]), "read": len(entries),
            "bytes_read": sum(x["bytes"] for x in entries), "errors": errors}, 2 if errors else 0


def validate_inventory(meta, bucket, declared):
    event_at = meta.get("event_at_beijing")
    if event_at is None:
        if meta.get("event_time_source") is not None or meta.get("event_time_input_original") is not None:
            raise ValueError("unknown event time has inconsistent provenance")
    elif (not isinstance(meta.get("event_time_input_original"), str) or not meta.get("event_time_source")
          or to_beijing(meta["event_time_input_original"]) != event_at):
        raise ValueError("event time and provenance do not agree")
    outcome = meta.get("outcome")
    if bucket in ("messages", "sources", "events"):
        if outcome not in ("copied", "partial_or_failed"):
            raise ValueError("invalid copy outcome")
        if bucket == "messages":
            required = "message.bin"
            if meta.get("role") not in ("user", "assistant"):
                raise ValueError("invalid message role")
        elif bucket == "sources":
            required = "files/" + relative_path(meta.get("original_relative_path", ""))
        else:
            required = "event.bin"
        if outcome == "copied" and required not in declared:
            raise ValueError("successful copy missing required payload inventory")
        if outcome == "partial_or_failed" and "failure.txt" not in declared:
            raise ValueError("failed copy missing failure record")
        if outcome == "copied" and "failure.txt" in declared:
            raise ValueError("successful copy declares failure")
    else:
        if outcome not in ("complete", "recorded_with_failure") or "response-headers.json" not in declared:
            raise ValueError("invalid crawl outcome or missing header representation")
        bodies = [name for name in declared if name.startswith("files/")]
        if len(bodies) > 1 or bool(bodies) != meta.get("body_present"):
            raise ValueError("crawl body inventory disagrees with body_present")
        if meta.get("body_complete") and not meta.get("body_present"):
            raise ValueError("complete body is not present")
        if outcome == "recorded_with_failure" and "failure.txt" not in declared:
            raise ValueError("failed crawl missing failure record")
        if outcome == "complete":
            status = meta.get("http_status")
            if not meta.get("body_complete") or not isinstance(status, int) or not 200 <= status < 300 or "failure.txt" in declared:
                raise ValueError("successful crawl lacks complete 2xx body or declares failure")


def verify(root: Path, snapshot_id: str | None):
    errors, count, files_checked, logged_failures = [], 0, 0, 0
    base = root / "records"
    if base.exists():
        for bucket in sorted(base.iterdir()):
            if bucket.is_symlink() or not bucket.is_dir() or bucket.name not in BUCKETS:
                errors.append(f"unexpected records entry: {bucket.relative_to(root)}")
                continue
            for record in sorted(bucket.iterdir()):
                if record.is_symlink() or not record.is_dir():
                    errors.append(f"unexpected bucket entry: {record.relative_to(root)}")
                    continue
                count += 1
                try:
                    mp = record / "metadata.json"
                    if mp.is_symlink():
                        raise ValueError("metadata is a symlink")
                    meta = json.loads(mp.read_text(encoding="utf-8"))
                    if meta.get("schema") != SCHEMA or meta.get("id") != record.name or meta.get("type") != bucket.name[:-1]:
                        raise ValueError("schema, id or type mismatch")
                    if not str(meta.get("recorded_at_beijing_unverified", "")).endswith("+08:00"):
                        raise ValueError("recorded time is not Beijing offset")
                    declared = meta.get("files")
                    if not isinstance(declared, dict):
                        raise ValueError("file inventory missing")
                    validate_inventory(meta, bucket.name, declared)
                    expected = {"metadata.json"}
                    for name, claimed in declared.items():
                        relative_path(name)
                        expected.add(name)
                        path = record / name
                        if path.is_symlink() or not path.is_file():
                            errors.append(f"missing or nonregular payload: {path.relative_to(root)}")
                        else:
                            if digest(path) != claimed:
                                errors.append(f"payload hash/size mismatch: {path.relative_to(root)}")
                            files_checked += 1
                    actual = set()
                    for directory, dirs, names in os.walk(record, followlinks=False):
                        for name in list(dirs):
                            p = Path(directory) / name
                            if p.is_symlink():
                                actual.add(p.relative_to(record).as_posix())
                                dirs.remove(name)
                        for name in names:
                            actual.add((Path(directory) / name).relative_to(record).as_posix())
                    if actual != expected:
                        errors.append(f"undeclared or missing files in {record.relative_to(root)}: {sorted(actual ^ expected)}")
                    if meta.get("supersedes_record_id"):
                        check_previous(root, bucket.name, meta["supersedes_record_id"])
                    if "failure.txt" in declared:
                        logged_failures += 1
                except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
                    errors.append(f"invalid record {record.relative_to(root)}: {type(exc).__name__}: {exc}")
    snap_report = None
    if snapshot_id:
        try:
            if len(snapshot_id) != 32 or any(c not in "0123456789abcdef" for c in snapshot_id):
                raise ValueError("invalid snapshot ID")
            directory = root / "snapshots" / snapshot_id
            scope_bytes = (directory / "scope.json").read_bytes()
            scope = json.loads(scope_bytes)
            manifest = json.loads((directory / "manifest.json").read_bytes())
            if scope.get("id") != snapshot_id or manifest.get("id") != snapshot_id:
                raise ValueError("snapshot id mismatch")
            if manifest.get("scope_sha256") != hashlib.sha256(scope_bytes).hexdigest():
                raise ValueError("snapshot scope hash mismatch")
            if manifest.get("errors") or manifest.get("outcome") != "complete":
                raise ValueError("snapshot is not complete")
            planned = {x["path"] for x in scope["files"]}
            baseline = {x["path"]: x for x in manifest["files"]}
            if planned != set(baseline) or len(baseline) != len(manifest["files"]):
                raise ValueError("snapshot scope and manifest disagree")
            current = {x["path"] for x in list_files(root)}
            for name, item in baseline.items():
                relative_path(name)
                path = root / name
                if path.is_symlink() or not path.is_file():
                    errors.append(f"snapshot file missing or nonregular: {name}")
                elif digest(path) != {"bytes": item["bytes"], "sha256": item["sha256"]}:
                    errors.append(f"snapshot file changed: {name}")
            snap_report = {"id": snapshot_id, "baseline_files": len(baseline), "new_files_since_snapshot": sorted(current - planned)}
        except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
            errors.append(f"invalid snapshot: {type(exc).__name__}: {exc}")
    report = {"outcome": "ok" if not errors else "failed", "records_checked": count,
              "payload_files_checked": files_checked, "records_with_logged_failures": logged_failures,
              "snapshot": snap_report, "errors": errors,
              "limitation": "hashes check local bytes, not truth or completeness; pin snapshots in Git or another trusted system"}
    return report, 2 if errors else 0


def git(repo: Path, *args, check=True):
    return subprocess.run(["git", "-C", str(repo), *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=check)


def recovery_plan(repo: Path):
    branch = git(repo, "symbolic-ref", "--short", "HEAD").stdout.decode("utf-8", "surrogateescape").strip()
    head = git(repo, "rev-parse", "HEAD").stdout.decode().strip()
    tracking = f"refs/remotes/origin/{branch}"
    found = git(repo, "rev-parse", "--verify", "--quiet", tracking, check=False)
    remote = found.stdout.decode().strip() if found.returncode == 0 else None
    raw = git(repo, "status", "--porcelain=v1", "-z", "--untracked-files=all").stdout.split(b"\0")
    changes, i = [], 0
    while i < len(raw):
        item = raw[i]
        i += 1
        if not item:
            continue
        code = item[:2].decode("ascii")
        change = {"status": code, "path": os.fsdecode(item[3:])}
        if "R" in code or "C" in code:
            if i >= len(raw) or not raw[i]:
                raise ValueError("incomplete rename/copy status")
            change["original_path"] = os.fsdecode(raw[i])
            i += 1
        changes.append(change)
    ancestor = None
    if remote:
        result = git(repo, "merge-base", "--is-ancestor", "HEAD", remote, check=False)
        if result.returncode not in (0, 1):
            raise RuntimeError("git merge-base failed")
        ancestor = result.returncode == 0
    return {"observed_at_beijing_unverified": now_beijing(), "current_branch": branch, "head": head,
            "tracking_ref": tracking, "tracking_commit": remote, "head_is_ancestor_of_tracking": ancestor,
            "dirty_entries": changes, "dirty_entry_count": len(changes),
            "clean_fast_forward_candidate_only": not changes and ancestor is True,
            "ignored_files_inspected": False, "mutations_performed": False,
            "next_steps": "Fetch current branch explicitly, re-run, inspect ignored/dirty files, protect and verify collisions; only then consider ff-only. Never pop/drop unverified protection.",
            "limitations": "Tracking ref may be stale; clean candidate does not guarantee ignored-file safety. This command does not fetch, stash, merge, or recover files."}


def add_copy_args(p):
    p.add_argument("--file", required=True, help="input path, or - for stdin; copied without transcoding")
    p.add_argument("--method", required=True, choices=("manual_transcription", "platform_visible_copy", "platform_export", "supplied_file", "tool_visible_transcription"))
    p.add_argument("--event-at", help="known event time with explicit offset; omit if unknown")
    p.add_argument("--event-time-source", choices=("user", "platform", "tool", "document"))
    p.add_argument("--supersedes", help="existing record ID of the same type")
    p.add_argument("--note", default="", help="provenance and limits; never credentials")


def parser_for_cli():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    sub = p.add_subparsers(dest="command", required=True)
    m = sub.add_parser("message", help="one message per record")
    add_copy_args(m)
    m.add_argument("--role", required=True, choices=("user", "assistant"))
    s = sub.add_parser("source", help="one source file per record")
    add_copy_args(s)
    s.add_argument("--original-path", required=True)
    s.add_argument("--source-uri")
    e = sub.add_parser("event", help="one change, check or issue per record")
    add_copy_args(e)
    e.add_argument("--event-kind", required=True)
    f = sub.add_parser("fetch", help="one expressly authorized request; no redirects or credentials")
    f.add_argument("--url", required=True)
    f.add_argument("--authorization-note", required=True)
    f.add_argument("--timeout", type=float, default=20)
    f.add_argument("--max-bytes", type=int, default=DEFAULT_FETCH)
    sub.add_parser("snapshot", help="list scope before reading and hash ledger records")
    v = sub.add_parser("verify", help="verify records and optionally a prior snapshot")
    v.add_argument("--snapshot")
    r = sub.add_parser("recovery-plan", help="read-only Git recovery assessment")
    r.add_argument("--repo", type=Path, default=REPO)
    return p


def main(argv=None):
    args = parser_for_cli().parse_args(argv)
    try:
        if args.command in ("message", "source", "event"):
            output, code = capture_copy(args.root, args, {"message": "messages", "source": "sources", "event": "events"}[args.command])
        elif args.command == "fetch":
            output, code = capture_fetch(args.root, args)
        elif args.command == "snapshot":
            output, code = snapshot(args.root)
        elif args.command == "verify":
            output, code = verify(args.root, args.snapshot)
        else:
            output, code = recovery_plan(args.repo), 0
        print(json.dumps(output, ensure_ascii=True, indent=2))
        return code
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"error: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
