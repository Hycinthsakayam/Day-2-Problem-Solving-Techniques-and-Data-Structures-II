"""Task 1 - BST of claim IDs with insert and search, the three traversals, and which one gives sorted claims."""


class Node:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None


class ClaimBST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key):
        """returns False if the claim ID is already in the tree"""
        if self.root is None:
            self.root = Node(key)
            self.size = 1
            return True
        cur = self.root
        while True:
            if key == cur.key:
                return False
            if key < cur.key:
                if cur.left is None:
                    cur.left = Node(key); break
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = Node(key); break
                cur = cur.right
        self.size += 1
        return True

    def search(self, key):
        cur = self.root
        while cur and cur.key != key:
            cur = cur.left if key < cur.key else cur.right
        return cur is not None

    def inorder(self):
        out = []
        def walk(n):
            if n:
                walk(n.left); out.append(n.key); walk(n.right)
        walk(self.root)
        return out

    def preorder(self):
        out = []
        def walk(n):
            if n:
                out.append(n.key); walk(n.left); walk(n.right)
        walk(self.root)
        return out

    def postorder(self):
        out = []
        def walk(n):
            if n:
                walk(n.left); walk(n.right); out.append(n.key)
        walk(self.root)
        return out


if __name__ == "__main__":
    claims = ["CLM5040", "CLM2210", "CLM7788", "CLM1105", "CLM3302", "CLM6015", "CLM9001", "CLM2210", "CLM4470"]
    tree = ClaimBST()
    for c in claims:
        added = tree.insert(c)
        print(f"insert {c}: {'added' if added else 'duplicate - ignored'}")
    print(f"\nClaims stored: {tree.size}")
    print("Inorder  :", tree.inorder())
    print("Preorder :", tree.preorder())
    print("Postorder:", tree.postorder())
    for q in ["CLM3302", "CLM8000"]:
        print(f"search {q}: {'found' if tree.search(q) else 'not found'}")
    print("\nInorder (left, node, right) visits keys from smallest to largest, so it lists claims in sorted order.")
    print("Preorder is useful to copy the tree; postorder to delete it bottom-up.")
