"""Tests for Task 3: empty graph, unknown stages, shortest path and loops."""
import unittest
from approval_stages_graph import find_loop, shortest_path, stages


class TestApprovalGraph(unittest.TestCase):
    def test_empty_graph(self):
        self.assertIsNone(shortest_path({}, "A", "B"))
        self.assertIsNone(find_loop({}))

    def test_shortest_path_skips_surveyor(self):
        p = shortest_path(stages, "Registration", "Settlement")
        self.assertEqual(p, ["Registration", "Document Check", "Assessment", "Settlement"])

    def test_same_start_and_goal(self):
        self.assertEqual(shortest_path(stages, "Assessment", "Assessment"), ["Assessment"])

    def test_no_backward_path(self):
        self.assertIsNone(shortest_path(stages, "Closed", "Registration"))

    def test_no_loop_in_normal_flow(self):
        self.assertIsNone(find_loop(stages))

    def test_self_loop(self):
        self.assertEqual(find_loop({"A": ["A"]}), ["A", "A"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
