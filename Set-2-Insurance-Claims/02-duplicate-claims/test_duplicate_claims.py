"""Tests for Task 2: empty input, exact and near duplicates, different incident dates."""
import unittest
from duplicate_claims import find_duplicates, normalise


class TestDuplicateClaims(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(find_duplicates([]), [])

    def test_exact_duplicate(self):
        c = [("C1", "POL-1", "2026-01-01"), ("C2", "POL-1", "2026-01-01")]
        self.assertEqual(find_duplicates(c), [("C1", "C2")])

    def test_case_and_spacing_ignored(self):
        self.assertEqual(normalise(" pol - hlt 20 "), "POLHLT20")
        c = [("C1", "POL-HLT-20", "2026-01-01"), ("C2", "pol hlt 20", "2026-01-01")]
        self.assertEqual(find_duplicates(c), [("C1", "C2")])

    def test_different_date_is_not_duplicate(self):
        c = [("C1", "POL-1", "2026-01-01"), ("C2", "POL-1", "2026-01-02")]
        self.assertEqual(find_duplicates(c), [])

    def test_three_copies(self):
        c = [("C1", "P", "d"), ("C2", "p", "d"), ("C3", " P ", "d")]
        self.assertEqual(find_duplicates(c), [("C1", "C2"), ("C1", "C3")])


if __name__ == "__main__":
    unittest.main(verbosity=2)
