"""Tests for Task 5: empty lists, duplicates and uneven lengths."""
import unittest
from merge_office_lists import merge_sorted


class TestMerge(unittest.TestCase):
    def test_both_empty(self):
        self.assertEqual(merge_sorted([], []), [])

    def test_one_empty(self):
        self.assertEqual(merge_sorted([], [1, 2]), [1, 2])
        self.assertEqual(merge_sorted([3], []), [3])

    def test_duplicates_are_kept(self):
        self.assertEqual(merge_sorted([1, 3, 3], [3, 4]), [1, 3, 3, 3, 4])

    def test_uneven_lengths(self):
        self.assertEqual(merge_sorted([5], [1, 2, 3, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_stable_on_ties(self):
        a, b = [("A", 1)], [("B", 1)]
        self.assertEqual(merge_sorted(a, b, key=lambda x: x[1]), [("A", 1), ("B", 1)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
