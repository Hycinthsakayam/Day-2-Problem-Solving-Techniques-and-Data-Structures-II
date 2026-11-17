"""Tests for Task 1: empty tree, duplicates and sorted inorder."""
import unittest
from claim_bst import ClaimBST


class TestClaimBST(unittest.TestCase):
    def test_empty_tree(self):
        t = ClaimBST()
        self.assertEqual(t.inorder(), [])
        self.assertEqual(t.preorder(), [])
        self.assertFalse(t.search("CLM0001"))

    def test_duplicate_is_ignored(self):
        t = ClaimBST()
        self.assertTrue(t.insert("CLM2000"))
        self.assertFalse(t.insert("CLM2000"))
        self.assertEqual(t.size, 1)

    def test_inorder_is_sorted(self):
        t = ClaimBST()
        ids = ["CLM5", "CLM2", "CLM8", "CLM1", "CLM9", "CLM3"]
        for i in ids:
            t.insert(i)
        self.assertEqual(t.inorder(), sorted(ids))

    def test_traversal_orders(self):
        t = ClaimBST()
        for i in ["B", "A", "C"]:
            t.insert(i)
        self.assertEqual(t.preorder(), ["B", "A", "C"])
        self.assertEqual(t.postorder(), ["A", "C", "B"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
