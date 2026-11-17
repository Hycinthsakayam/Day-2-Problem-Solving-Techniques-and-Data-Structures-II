"""Task 1 - binary search tree of product categories: insert, search and the three traversals."""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        cur = self.root
        while True:
            if key == cur.key:
                return                      # no duplicates
            side = "left" if key < cur.key else "right"
            nxt = getattr(cur, side)
            if nxt is None:
                setattr(cur, side, Node(key))
                return
            cur = nxt

    def search(self, key):
        cur, steps = self.root, 0
        while cur:
            steps += 1
            if key == cur.key:
                return True, steps
            cur = cur.left if key < cur.key else cur.right
        return False, steps

    def inorder(self, n="root"):
        n = self.root if n == "root" else n
        return [] if n is None else self.inorder(n.left) + [n.key] + self.inorder(n.right)

    def preorder(self, n="root"):
        n = self.root if n == "root" else n
        return [] if n is None else [n.key] + self.preorder(n.left) + self.preorder(n.right)

    def postorder(self, n="root"):
        n = self.root if n == "root" else n
        return [] if n is None else self.postorder(n.left) + self.postorder(n.right) + [n.key]

    def height(self, n="root"):
        n = self.root if n == "root" else n
        return 0 if n is None else 1 + max(self.height(n.left), self.height(n.right))


categories = ["Mobiles", "Electronics", "Toys", "Books", "Grocery", "Shoes", "Watches", "Appliances",
              "Fashion", "Kitchen", "Sports", "Beauty", "Furniture", "Laptops", "Pet Supplies"]

tree = BST()
for c in categories:
    tree.insert(c)

print("Inserted 15 categories in this order:")
print(" ", ", ".join(categories))
print(f"\nTree height: {tree.height()}")
print("\nInorder  :", ", ".join(tree.inorder()))
print("\nPreorder :", ", ".join(tree.preorder()))
print("\nPostorder:", ", ".join(tree.postorder()))

print("\nSearch:")
for q in ["Kitchen", "Laptops", "Garden"]:
    found, steps = tree.search(q)
    print(f"  {q:<8} -> {'found' if found else 'not found'} after {steps} comparisons")
print("\nInorder gives the categories in alphabetical order, which is what the category menu needs.")
