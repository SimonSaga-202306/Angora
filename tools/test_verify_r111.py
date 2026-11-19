#!/usr/bin/env python3
"""Negative and positive tests for the reusable r111 local checks."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import verify_r111 as v


class VerifyR111Tests(unittest.TestCase):
    def test_file_hash_catches_same_length_tampering(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "saved.txt"
            path.write_bytes(b"good")
            self.assertEqual(v.verify_file(path, 4, v.sha256(b"good")), b"good")
            path.write_bytes(b"evil")
            with self.assertRaises(v.AuditError):
                v.verify_file(path, 4, v.sha256(b"good"))

    def test_file_size_is_not_just_a_hash_check(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "saved.txt"
            path.write_bytes(b"short")
            with self.assertRaises(v.AuditError):
                v.verify_file(path, 6, v.sha256(b"short"))

    def test_csv_parser_rejects_unquoted_commas_and_accepts_quotes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "records.csv"
            path.write_text('id,title\n1,"one, two"\n', encoding="utf-8")
            self.assertEqual(v.strict_csv(path)[0]["title"], "one, two")
            path.write_text("id,title\n1,one, two\n", encoding="utf-8")
            with self.assertRaises(v.AuditError):
                v.strict_csv(path)

    def test_line_anchor_rejects_wrong_line_and_missing_text(self) -> None:
        text = "first\nsecond\nthird\n"
        v.verify_anchor(text, 2, 3, "second\nthird")
        with self.assertRaises(v.AuditError):
            v.verify_anchor(text, 1, 1, "second")
        with self.assertRaises(v.AuditError):
            v.verify_anchor(text, 2, 3, "not present")

    def test_chunks_reject_reordering_and_corruption(self) -> None:
        parts = [b"foo", b"bar", b"baz"]
        v.verify_join(parts, b"foobarbaz")
        with self.assertRaises(v.AuditError):
            v.verify_join([parts[1], parts[0], parts[2]], b"foobarbaz")
        with self.assertRaises(v.AuditError):
            v.verify_join(parts, b"foobarbAx")

    def test_dossier_rejects_changed_prefix_and_suffix(self) -> None:
        old, payload = b"old-prefix", b"\nappend"
        v.verify_prefix(old, old + payload, payload, v.sha256(old), 3, v.sha256(b"old"))
        with self.assertRaises(v.AuditError):
            v.verify_prefix(old, b"bad-prefix" + payload, payload, v.sha256(old), 3, v.sha256(b"old"))
        with self.assertRaises(v.AuditError):
            v.verify_prefix(old, old + b"other", payload, v.sha256(old), 3, v.sha256(b"old"))
        with self.assertRaises(v.AuditError):
            v.verify_prefix(old, old + payload, payload, v.sha256(old), 3, v.sha256(b"bad"))

    def test_repository_boundary_rejects_escape(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "root"
            root.mkdir()
            self.assertEqual(v.checked_path(root, "child"), root / "child")
            with self.assertRaises(v.AuditError):
                v.checked_path(root, "../outside")


if __name__ == "__main__":
    unittest.main()
