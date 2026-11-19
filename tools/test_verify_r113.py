#!/usr/bin/env python3
"""Fixture-only positive and negative checks for r113 evidence helpers."""
from __future__ import annotations

import unittest

import verify_r113 as v


class VerifyR113Tests(unittest.TestCase):
    def test_selected_body_is_bounded(self) -> None:
        text = "header\nSTART\nbody\nEND\nfooter"
        self.assertEqual(v.selected_body(text, "START", "END"), "START\nbody\n")

    def test_selected_body_rejects_missing_marker(self) -> None:
        with self.assertRaises(v.AuditError):
            v.selected_body("start and body", "start", "missing")

    def test_wayback_normalization_only_replaces_capture_path(self) -> None:
        a = "https://example.test/web/20210102030405/item?year=2021"
        b = "https://example.test/web/20250203040506/item?year=2021"
        self.assertEqual(v.normalize_wayback_timestamps(a), v.normalize_wayback_timestamps(b))
        self.assertNotEqual(v.normalize_wayback_timestamps(a), v.normalize_wayback_timestamps(b.replace("year=2021", "year=2022")))

    def test_redacted_view_masks_exactly_two_occurrences(self) -> None:
        text = "before DEMO middle DEMO after"
        view = v.make_redacted_view(text, "DEMO")
        self.assertEqual(view.count("[HISTORICAL_PUBLIC_DEFAULT_OMITTED]"), 2)
        self.assertNotIn("DEMO", view)

    def test_redacted_view_rejects_unexpected_count(self) -> None:
        with self.assertRaises(v.AuditError):
            v.make_redacted_view("only DEMO", "DEMO")
        with self.assertRaises(v.AuditError):
            v.make_redacted_view("anything", "")

    def test_source_classification_does_not_confuse_replay_with_index(self) -> None:
        self.assertTrue(v.is_non_source_id("A01"))
        self.assertTrue(v.is_non_source_id("X01"))
        self.assertTrue(v.is_non_source_id("R01"))
        self.assertFalse(v.is_non_source_id("AR01"))
        self.assertFalse(v.is_non_source_id("P01"))

    def test_join_detects_corrupt_chunk(self) -> None:
        v.verify_join([b"ne", b"ighbors"], b"neighbors")
        with self.assertRaises(v.AuditError):
            v.verify_join([b"ne", b"igbors"], b"neighbors")


if __name__ == "__main__":
    unittest.main()
