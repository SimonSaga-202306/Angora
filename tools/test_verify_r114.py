#!/usr/bin/env python3
"""Positive/negative fixture tests for r114 verifier helpers, no network."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import verify_r114 as v


class VerifyR114Tests(unittest.TestCase):
    def test_anchor_must_be_on_expected_line(self) -> None:
        text = "first\nsource phrase\nlast\n"
        self.assertTrue(v.anchor_present(text, 2, "source phrase"))
        self.assertFalse(v.anchor_present(text, 1, "source phrase"))
        self.assertFalse(v.anchor_present(text, 0, "source phrase"))

    def test_correction_changes_exactly_one_piece(self) -> None:
        self.assertTrue(v.is_expected_correction(b"a old b", b"a new b", b"old", b"new"))
        self.assertFalse(v.is_expected_correction(b"a old b", b"a new c", b"old", b"new"))
        self.assertFalse(v.is_expected_correction(b"old old", b"new old", b"old", b"new"))
        self.assertFalse(v.is_expected_correction(b"x", b"x", b"", b"y"))

    def test_valid_cdx_and_wrong_status(self) -> None:
        header = ["urlkey", "timestamp", "original", "mimetype", "statuscode", "digest", "length"]
        row = ["key", "20221204195052", "https://example.test", "text/html", "200", "D", "1"]
        wrapped = lambda values: "```json\n" + json.dumps(values) + "\n```"
        self.assertEqual(v.parse_cdx(wrapped([header, row])), [row])
        with self.assertRaises(v.AuditError):
            v.parse_cdx(wrapped([header, row[:4] + ["404"] + row[5:]]))

    def test_cdx_rejects_future_and_bad_wrapper(self) -> None:
        header = ["urlkey", "timestamp", "original", "mimetype", "statuscode", "digest", "length"]
        row = ["key", "20261027000000", "https://example.test", "text/html", "200", "D", "1"]
        with self.assertRaises(v.AuditError):
            v.parse_cdx("```json\n" + json.dumps([header, row]) + "\n```")
        with self.assertRaises(v.AuditError):
            v.parse_cdx("[]")

    def test_rejects_escaping_or_absolute_paths(self) -> None:
        with self.assertRaises(v.AuditError):
            v.checked_path("../outside")
        with self.assertRaises(v.AuditError):
            v.checked_path("/tmp/outside")
        self.assertEqual(v.checked_path("tools").name, "tools")

    def test_strict_csv_rejects_extra_columns(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "file.csv"
            path.write_text("a,b\n1,2\n", encoding="utf-8")
            self.assertEqual(v.strict_csv(path), [{"a": "1", "b": "2"}])
            path.write_text("a,b\n1,2,3\n", encoding="utf-8")
            with self.assertRaises(v.AuditError):
                v.strict_csv(path)

    def test_checked_file_detects_changed_byte(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source.txt"
            path.write_bytes(b"abc")
            self.assertEqual(v.checked_file(path, 3, v.sha256(b"abc")), b"abc")
            path.write_bytes(b"abd")
            with self.assertRaises(v.AuditError):
                v.checked_file(path, 3, v.sha256(b"abc"))


if __name__ == "__main__":
    unittest.main()
