#!/usr/bin/env python3
"""Positive and negative tests for r112 helper checks using temporary data."""
from __future__ import annotations

import hashlib
import unittest

import verify_r112 as v


class VerifyR112Tests(unittest.TestCase):
    def test_git_blob_rejects_same_length_tampering(self) -> None:
        data = b"public sample\n"
        oid = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
        v.verify_git_blob(data, len(data), oid)
        with self.assertRaises(v.AuditError):
            v.verify_git_blob(b"Public sample\n", len(data), oid)

    def test_git_blob_rejects_wrong_size(self) -> None:
        data = b"abc"
        oid = hashlib.sha1(b"blob 3\0abc").hexdigest()
        with self.assertRaises(v.AuditError):
            v.verify_git_blob(data, 4, oid)

    def test_directory_compare_rejects_changed_blob(self) -> None:
        a = [{"path": "freeRadiusConfigs/eap", "sha": "a" * 40, "size": 9, "type": "file"}]
        v.verify_directory_equivalence(a, list(a))
        changed = [{**a[0], "sha": "b" * 40}]
        with self.assertRaises(v.AuditError):
            v.verify_directory_equivalence(a, changed)

    def test_directory_rejects_duplicate_and_traversal(self) -> None:
        a = {"path": "freeRadiusConfigs/eap", "sha": "a" * 40, "size": 9, "type": "file"}
        with self.assertRaises(v.AuditError):
            v.directory_signature([a, a])
        with self.assertRaises(v.AuditError):
            v.directory_signature([{**a, "path": "freeRadiusConfigs/../outside"}])

    def test_chunk_run_rejects_identity_and_count_drift(self) -> None:
        good = [{"chunk_index": 0, "total_chunks": 2, "title": "target", "has_more": True},
                {"chunk_index": 1, "total_chunks": 2, "title": "target", "has_more": False}]
        v.require_complete_consistent_chunks(good)
        with self.assertRaises(v.AuditError):
            v.require_complete_consistent_chunks([good[0], {**good[1], "total_chunks": 4}])
        with self.assertRaises(v.AuditError):
            v.require_complete_consistent_chunks([good[0], {**good[1], "title": "other"}])

    def test_chunk_run_rejects_incomplete_or_unterminated(self) -> None:
        first = {"chunk_index": 0, "total_chunks": 2, "title": "target", "has_more": True}
        with self.assertRaises(v.AuditError):
            v.require_complete_consistent_chunks([first])
        with self.assertRaises(v.AuditError):
            v.require_complete_consistent_chunks([first, {**first, "chunk_index": 1}])

    def test_cdx_requires_valid_header_and_status(self) -> None:
        good = '```json\n[["timestamp","original","statuscode","digest","length"],["20210101000000","https://example.org/","200","hash","1"]]\n```'
        self.assertEqual(len(v.parse_cdx(good)), 1)
        self.assertEqual(v.parse_cdx('```json\n[]\n```'), [])
        with self.assertRaises(v.AuditError):
            v.parse_cdx(good.replace('"200"', '"404"'))
        with self.assertRaises(v.AuditError):
            v.parse_cdx('not JSON')


if __name__ == "__main__":
    unittest.main()
