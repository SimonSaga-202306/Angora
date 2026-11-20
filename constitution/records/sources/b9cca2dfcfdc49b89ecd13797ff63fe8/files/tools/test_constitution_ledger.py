#!/usr/bin/env python3
"""Offline integration tests with disposable HTTP and Git fixtures."""
import hashlib
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlsplit

SCRIPT = Path(__file__).resolve().parent / "constitution_ledger.py"
BRANCH = "arena/5da004bd-angora"
BINARY = b"\x00\xffraw\r\n\xe4\xb8\xad\x00"


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.0"
    followed = 0

    def log_message(self, *args):
        pass

    def do_GET(self):
        route = urlsplit(self.path).path
        if route == "/file.bin":
            status, body, headers = 200, BINARY, []
        elif route == "/missing":
            status, body, headers = 404, b"not found\x00\xff", []
        elif route == "/redirect":
            status, body, headers = 302, b"redirect", [("Location", "/target")]
        elif route == "/secret-redirect":
            status, body, headers = 302, b"redirect", [("Location", "/target?access_token=never-save")]
        elif route == "/cookie":
            status, body, headers = 200, b"ok", [("Set-Cookie", "session=never-save")]
        elif route == "/large":
            status, body, headers = 200, b"1234567890ABCDEF", []
        elif route == "/short":
            self.send_response(200)
            self.send_header("Content-Length", "100")
            self.end_headers()
            self.wfile.write(b"short")
            self.close_connection = True
            return
        elif route == "/target":
            type(self).followed += 1
            status, body, headers = 200, b"must not follow", []
        else:
            status, body, headers = 500, b"bad fixture path", []
        self.send_response(status)
        self.send_header("Content-Length", str(len(body)))
        for name, value in headers:
            self.send_header(name, value)
        self.end_headers()
        try:
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            pass


class LedgerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.thread.join(timeout=5)
        cls.server.server_close()

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.dir = Path(self.tmp.name)
        self.root = self.dir / "ledger"
        self.input = self.dir / "input.bin"
        self.input.write_bytes(BINARY)

    def cli(self, *args, code=0):
        proc = subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.root), *map(str, args)],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                              env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
        self.assertEqual(proc.returncode, code, f"stdout={proc.stdout}\nstderr={proc.stderr}")
        return (json.loads(proc.stdout) if proc.stdout.strip() else None), proc

    def msg(self, data=None, extra=()):
        if data is not None:
            self.input.write_bytes(data)
        return self.cli("message", "--file", self.input, "--role", "user", "--method", "supplied_file", *extra)[0]

    def fetch(self, path, code=0, extra=()):
        return self.cli("fetch", "--url", self.base + path, "--authorization-note", "local fixture authorized", *extra, code=code)[0]

    def meta(self, record):
        return json.loads((Path(record["record_dir"]) / "metadata.json").read_text())

    def mutate_meta(self, record, meta):
        (Path(record["record_dir"]) / "metadata.json").write_text(json.dumps(meta), encoding="utf-8")

    def test_message_preserves_binary_and_unknown_event_time(self):
        record = self.msg()
        meta = self.meta(record)
        self.assertEqual((Path(record["record_dir"]) / "message.bin").read_bytes(), BINARY)
        self.assertIsNone(meta["event_at_beijing"])
        self.assertIsNone(meta["event_time_source"])
        self.assertTrue(meta["recorded_at_beijing_unverified"].endswith("+08:00"))
        self.assertIn("upstream completeness", meta["fidelity"])
        self.assertEqual(meta["files"]["message.bin"]["sha256"], hashlib.sha256(BINARY).hexdigest())

    def test_identical_messages_are_separate(self):
        first, second = self.msg(), self.msg()
        self.assertNotEqual(first["id"], second["id"])
        self.assertEqual((Path(first["record_dir"]) / "message.bin").read_bytes(), (Path(second["record_dir"]) / "message.bin").read_bytes())
        self.assertEqual(self.cli("verify")[0]["records_checked"], 2)

    def test_message_version_keeps_original(self):
        first = self.msg(b"first")
        second = self.msg(b"second", ("--supersedes", first["id"]))
        self.assertEqual((Path(first["record_dir"]) / "message.bin").read_bytes(), b"first")
        self.assertEqual((Path(second["record_dir"]) / "message.bin").read_bytes(), b"second")
        self.assertEqual(self.meta(second)["supersedes_record_id"], first["id"])
        self.cli("verify")

    def test_unknown_previous_version_rejected(self):
        self.cli("message", "--file", self.input, "--role", "user", "--method", "supplied_file", "--supersedes", "f" * 32, code=2)
        self.assertFalse((self.root / "records").exists())

    def test_known_time_converted_and_original_preserved(self):
        meta = self.meta(self.msg(extra=("--event-at", "2025-12-31T16:00:00Z", "--event-time-source", "platform")))
        self.assertEqual(meta["event_at_beijing"], "2026-01-01T00:00:00.000000+08:00")
        self.assertEqual(meta["event_time_input_original"], "2025-12-31T16:00:00Z")
        self.cli("verify")

    def test_naive_or_unattributed_time_rejected(self):
        self.cli("message", "--file", self.input, "--role", "user", "--method", "supplied_file", "--event-at", "2025-12-31T16:00:00", "--event-time-source", "user", code=2)
        self.cli("message", "--file", self.input, "--role", "user", "--method", "supplied_file", "--event-at", "2025-12-31T16:00:00Z", code=2)
        self.assertFalse((self.root / "records").exists())

    def test_invalid_time_provenance_detected(self):
        record = self.msg()
        meta = self.meta(record)
        meta["event_time_source"] = "user"
        self.mutate_meta(record, meta)
        report = self.cli("verify", code=2)[0]
        self.assertTrue(any("provenance" in error for error in report["errors"]))

    def test_source_original_path_and_binary(self):
        record = self.cli("source", "--file", self.input, "--original-path", "files/子目录/original.bin", "--method", "supplied_file")[0]
        self.assertEqual((Path(record["record_dir"]) / "files/files/子目录/original.bin").read_bytes(), BINARY)
        self.assertEqual(self.meta(record)["original_relative_path"], "files/子目录/original.bin")
        self.cli("verify")

    def test_unsafe_original_paths_rejected(self):
        for value in ("../outside", "/absolute", "a/../b", "a\\b", "a//b"):
            self.cli("source", "--file", self.input, "--original-path", value, "--method", "supplied_file", code=2)
        self.assertFalse((self.root / "records").exists())

    def test_missing_source_records_failure_not_fake_payload(self):
        record = self.cli("source", "--file", self.dir / "missing", "--original-path", "missing.bin", "--method", "supplied_file", code=2)[0]
        self.assertEqual(record["outcome"], "partial_or_failed")
        self.assertTrue((Path(record["record_dir"]) / "failure.txt").is_file())
        self.assertFalse((Path(record["record_dir"]) / "files/missing.bin").exists())
        self.assertEqual(self.cli("verify")[0]["records_with_logged_failures"], 1)

    def test_event_is_not_merged_with_message(self):
        message = self.msg()
        event = self.cli("event", "--file", self.input, "--event-kind", "correction", "--method", "supplied_file")[0]
        self.assertNotEqual(message["id"], event["id"])
        self.assertEqual(self.meta(event)["event_kind"], "correction")
        self.cli("verify")

    def test_fetch_binary_entity(self):
        record = self.fetch("/file.bin")
        self.assertEqual((Path(record["record_dir"]) / "files/127.0.0.1/file.bin").read_bytes(), BINARY)
        self.assertTrue(self.meta(record)["body_complete"])
        self.cli("verify")

    def test_http_error_body_and_failure_kept(self):
        record = self.fetch("/missing", code=2)
        self.assertEqual(self.meta(record)["http_status"], 404)
        self.assertTrue(self.meta(record)["body_complete"])
        self.assertEqual((Path(record["record_dir"]) / "files/127.0.0.1/missing").read_bytes(), b"not found\x00\xff")
        self.assertIn("HTTP status 404", (Path(record["record_dir"]) / "failure.txt").read_text())
        self.cli("verify")

    def test_redirect_not_followed(self):
        before = Handler.followed
        record = self.fetch("/redirect", code=2)
        self.assertEqual(Handler.followed, before)
        self.assertEqual(self.meta(record)["http_status"], 302)
        self.assertEqual((Path(record["record_dir"]) / "files/127.0.0.1/redirect").read_bytes(), b"redirect")
        self.cli("verify")

    def test_sensitive_headers_redacted(self):
        cookie = self.fetch("/cookie")
        redirect = self.fetch("/secret-redirect", code=2)
        for record in (cookie, redirect):
            text = (Path(record["record_dir"]) / "response-headers.json").read_text()
            self.assertNotIn("never-save", text)
            self.assertIn("[REDACTED]", text)

    def test_sensitive_url_refused_without_saving_secret(self):
        secret = "literal-secret-not-to-save"
        record = self.fetch("/file.bin?access_token=" + secret, code=2)
        self.assertIsNone(self.meta(record)["requested_url"])
        self.assertFalse(self.meta(record)["body_present"])
        for path in Path(record["record_dir"]).rglob("*"):
            if path.is_file():
                self.assertNotIn(secret.encode(), path.read_bytes())
        self.cli("verify")

    def test_fetch_requires_authorization_note(self):
        self.cli("fetch", "--url", self.base + "/file.bin", "--authorization-note", " ", code=2)
        self.assertFalse((self.root / "records").exists())

    def test_fetch_size_limit_retains_received_prefix(self):
        record = self.fetch("/large", code=2, extra=("--max-bytes", "4"))
        self.assertTrue(self.meta(record)["truncated_by_limit"])
        self.assertFalse(self.meta(record)["body_complete"])
        self.assertEqual((Path(record["record_dir"]) / "files/127.0.0.1/large").read_bytes(), b"12345")
        self.cli("verify")

    def test_invalid_fetch_limit_rejected(self):
        for value in ("0", str(64 * 1024 * 1024 + 1)):
            self.cli("fetch", "--url", self.base + "/file.bin", "--authorization-note", "fixture", "--max-bytes", value, code=2)
        self.assertFalse((self.root / "records").exists())

    def test_incomplete_response_not_claimed_complete(self):
        record = self.fetch("/short", code=2)
        self.assertFalse(self.meta(record)["body_complete"])
        self.assertEqual((Path(record["record_dir"]) / "files/127.0.0.1/short").read_bytes(), b"short")
        self.assertTrue((Path(record["record_dir"]) / "failure.txt").is_file())
        self.cli("verify")

    def test_transport_failure_has_no_fabricated_body(self):
        sock = socket.socket()
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
        sock.close()
        record = self.cli("fetch", "--url", f"http://127.0.0.1:{port}/offline", "--authorization-note", "local fixture", "--timeout", "2", code=2)[0]
        self.assertFalse(self.meta(record)["body_present"])
        self.assertIsNone(self.meta(record)["http_status"])
        self.assertFalse((Path(record["record_dir"]) / "files").exists())
        self.cli("verify")

    def test_successful_message_cannot_omit_payload(self):
        record = self.msg()
        d = Path(record["record_dir"])
        (d / "message.bin").unlink()
        meta = self.meta(record)
        del meta["files"]["message.bin"]
        self.mutate_meta(record, meta)
        report = self.cli("verify", code=2)[0]
        self.assertTrue(any("required payload" in error for error in report["errors"]))

    def test_successful_source_cannot_omit_payload(self):
        record = self.cli("source", "--file", self.input, "--original-path", "a/original.bin", "--method", "supplied_file")[0]
        d = Path(record["record_dir"])
        (d / "files/a/original.bin").unlink()
        meta = self.meta(record)
        del meta["files"]["files/a/original.bin"]
        self.mutate_meta(record, meta)
        report = self.cli("verify", code=2)[0]
        self.assertTrue(any("required payload" in error for error in report["errors"]))

    def test_successful_crawl_cannot_omit_body(self):
        record = self.fetch("/file.bin")
        d = Path(record["record_dir"])
        (d / "files/127.0.0.1/file.bin").unlink()
        meta = self.meta(record)
        del meta["files"]["files/127.0.0.1/file.bin"]
        meta["body_present"] = False
        meta["body_complete"] = False
        self.mutate_meta(record, meta)
        report = self.cli("verify", code=2)[0]
        self.assertTrue(any("successful crawl" in error for error in report["errors"]))

    def test_failure_record_cannot_be_omitted(self):
        record = self.cli("source", "--file", self.dir / "missing", "--original-path", "missing", "--method", "supplied_file", code=2)[0]
        d = Path(record["record_dir"])
        (d / "failure.txt").unlink()
        meta = self.meta(record)
        del meta["files"]["failure.txt"]
        self.mutate_meta(record, meta)
        report = self.cli("verify", code=2)[0]
        self.assertTrue(any("failure record" in error for error in report["errors"]))

    def test_snapshot_lists_then_reads_and_allows_later_additions(self):
        self.msg()
        snap = self.cli("snapshot")[0]
        scope = json.loads((self.root / "snapshots" / snap["id"] / "scope.json").read_text())
        self.assertEqual((snap["listed"], snap["read"], len(scope["files"])), (2, 2, 2))
        self.msg(b"later")
        report = self.cli("verify", "--snapshot", snap["id"])[0]
        self.assertEqual(report["records_checked"], 2)
        self.assertEqual(len(report["snapshot"]["new_files_since_snapshot"]), 2)

    def test_snapshot_detects_coordinated_payload_and_metadata_change(self):
        record = self.msg()
        snap = self.cli("snapshot")[0]
        d = Path(record["record_dir"])
        (d / "message.bin").write_bytes(b"tampered")
        meta = self.meta(record)
        meta["files"]["message.bin"] = {"bytes": 8, "sha256": hashlib.sha256(b"tampered").hexdigest()}
        self.mutate_meta(record, meta)
        self.cli("verify")  # self-declared hash alone cannot catch a coordinated modification
        report = self.cli("verify", "--snapshot", snap["id"], code=2)[0]
        self.assertGreaterEqual(sum("snapshot file changed" in error for error in report["errors"]), 2)

    def test_snapshot_detects_missing_file(self):
        record = self.msg()
        snap = self.cli("snapshot")[0]
        (Path(record["record_dir"]) / "message.bin").unlink()
        report = self.cli("verify", "--snapshot", snap["id"], code=2)[0]
        self.assertTrue(any("missing" in error for error in report["errors"]))

    def test_unexpected_file_and_incomplete_record_detected(self):
        record = self.msg()
        extra = Path(record["record_dir"]) / "extra.txt"
        extra.write_text("unexpected")
        self.assertTrue(any("undeclared" in e for e in self.cli("verify", code=2)[0]["errors"]))
        extra.unlink()
        broken = self.root / "records/events" / ("a" * 32)
        broken.mkdir(parents=True)
        (broken / "event.bin").write_bytes(b"partial")
        self.assertTrue(any("invalid record" in e for e in self.cli("verify", code=2)[0]["errors"]))

    def test_symlinked_record_bucket_is_rejected(self):
        (self.root / "records").mkdir(parents=True)
        (self.root / "records/messages").symlink_to(self.dir, target_is_directory=True)
        self.cli("message", "--file", self.input, "--role", "user", "--method", "supplied_file", code=2)
        self.assertTrue(any("unexpected records entry" in e for e in self.cli("verify", code=2)[0]["errors"]))

    def test_symlinked_records_root_rejected_by_verify(self):
        self.root.mkdir()
        outside = self.dir / "outside"
        outside.mkdir()
        (self.root / "records").symlink_to(outside, target_is_directory=True)
        report = self.cli("verify", code=2)[0]
        self.assertTrue(any("records root" in error for error in report["errors"]))

    def test_symlinked_records_root_rejected_by_snapshot(self):
        self.root.mkdir()
        outside = self.dir / "outside"
        outside.mkdir()
        (self.root / "records").symlink_to(outside, target_is_directory=True)
        self.cli("snapshot", code=2)
        self.assertFalse((self.root / "snapshots").exists())

    def test_symlinked_snapshot_root_rejected(self):
        self.msg()
        snap = self.cli("snapshot")[0]
        snapshots = self.root / "snapshots"
        outside = self.dir / "outside-snapshots"
        snapshots.rename(outside)
        snapshots.symlink_to(outside, target_is_directory=True)
        report = self.cli("verify", "--snapshot", snap["id"], code=2)[0]
        self.assertTrue(any("symlink" in error for error in report["errors"]))

    def test_recovery_plan_readonly_and_simulated_protection(self):
        repo = self.dir / "fixture-repo"
        repo.mkdir()

        def g(*args, data=None):
            proc = subprocess.run(["git", "-C", str(repo), *args], input=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.assertEqual(proc.returncode, 0, proc.stderr.decode(errors="replace"))
            return proc.stdout

        g("init", "--quiet", "--initial-branch=" + BRANCH)
        (repo / "tracked.txt").write_bytes(b"base")
        g("add", "tracked.txt")
        g("-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "--quiet", "-m", "base")
        head = g("rev-parse", "HEAD").strip()
        old_blob = g("rev-parse", "HEAD:tracked.txt").strip()
        original = b"local untracked\x00"
        new_blob = g("hash-object", "-w", "--stdin", data=original).strip()
        tree = g("mktree", data=b"100644 blob " + old_blob + b"\ttracked.txt\n100644 blob " + new_blob + b"\tcollision.txt\n").strip()
        remote = g("-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit-tree", tree.decode(), "-p", head.decode(), "-m", "remote child").strip()
        ref = "refs/remotes/origin/" + BRANCH
        g("update-ref", ref, remote.decode())
        (repo / "collision.txt").write_bytes(original)
        before = g("status", "--porcelain=v1", "-z", "--untracked-files=all")
        plan = self.cli("recovery-plan", "--repo", repo)[0]
        self.assertFalse(plan["mutations_performed"])
        self.assertFalse(plan["clean_fast_forward_candidate_only"])
        self.assertTrue(plan["head_is_ancestor_of_tracking"])
        self.assertEqual(before, g("status", "--porcelain=v1", "-z", "--untracked-files=all"))
        self.assertEqual((repo / "collision.txt").read_bytes(), original)
        g("stash", "push", "--include-untracked", "--message", "fixture-protect-do-not-drop", "--", "collision.txt")
        self.assertEqual(g("show", "stash@{0}^3:collision.txt"), original)
        stash = g("rev-parse", "stash@{0}").strip()
        g("merge", "--ff-only", ref)
        self.assertEqual((repo / "collision.txt").read_bytes(), original)
        self.assertEqual(g("rev-parse", "stash@{0}").strip(), stash)
        self.assertEqual(g("status", "--porcelain=v1", "-z", "--untracked-files=all"), b"")


if __name__ == "__main__":
    unittest.main(verbosity=2)
