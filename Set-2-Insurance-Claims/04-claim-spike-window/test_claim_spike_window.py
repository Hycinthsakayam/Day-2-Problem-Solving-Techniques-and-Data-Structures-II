"""Tests for Task 4: empty input, no spike, exactly 100 and ties."""
import unittest
from claim_spike_window import longest_run_above


class TestClaimSpike(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(longest_run_above([]), (0, -1))

    def test_no_day_above_limit(self):
        self.assertEqual(longest_run_above([10, 100, 99]), (0, -1))

    def test_exactly_100_is_not_above(self):
        self.assertEqual(longest_run_above([101, 100, 101, 102]), (2, 2))

    def test_whole_list(self):
        self.assertEqual(longest_run_above([150, 200, 101]), (3, 0))

    def test_first_of_equal_runs_is_kept(self):
        self.assertEqual(longest_run_above([120, 130, 5, 140, 150]), (2, 0))

    def test_duplicate_values(self):
        self.assertEqual(longest_run_above([101, 101, 101, 50, 101]), (3, 0))


if __name__ == "__main__":
    unittest.main(verbosity=2)
