#!/usr/bin/env python3
"""Regression checks for local r115 verification helpers and fixed boundaries."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("verify_r115", HERE / "verify_r115.py")
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class VerificationTests(unittest.TestCase):
    def test_sha256_known_value(self):
        self.assertEqual(v.sha(b"abc"), "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")

    def test_require_rejects_false(self):
        with self.assertRaises(AssertionError):
            v.require(False, "deliberate failure")

    def test_require_accepts_true(self):
        self.assertIsNone(v.require(True, "irrelevant"))

    def test_complete_scoped_inventory(self):
        self.assertEqual(v.validate_inventories(), (159, 291565))

    def test_search_metadata_is_separately_counted(self):
        n, results, zeros = v.validate_queries()
        self.assertEqual((n, results), (108, 431))
        self.assertEqual(zeros, ["Q42", "Q78", "Q96", "Q97"])

    def test_catalog_records_blocks_not_independent_source_count(self):
        self.assertEqual(v.validate_catalog(), 28)

    def test_selected_local_anchors(self):
        self.assertEqual(v.validate_anchors(), 26)

    def test_transcription_replacements(self):
        self.assertEqual(v.validate_corrections(), 3)

    def test_master_prefix_and_append_only(self):
        self.assertEqual(v.validate_master_pointer(), (52157, 359))

    def test_deliverable_links_and_boundaries(self):
        docs, links = v.validate_documents()
        self.assertEqual(docs, 6)
        self.assertGreater(links, 10)

    def test_missing_relative_link_fails(self):
        with tempfile.TemporaryDirectory(dir=HERE) as tmp:
            doc = Path(tmp) / "doc.md"
            doc.write_text("[missing](nonexistent.md)\n", encoding="utf-8")
            with self.assertRaises(AssertionError):
                v.validate_relative_links(doc)

    def test_directory_and_remote_links_are_handled(self):
        with tempfile.TemporaryDirectory(dir=HERE) as tmp:
            root = Path(tmp)
            (root / "dir").mkdir()
            doc = root / "doc.md"
            doc.write_text("[local directory](dir/) [external](https://example.org/)\n", encoding="utf-8")
            self.assertEqual(v.validate_relative_links(doc), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
