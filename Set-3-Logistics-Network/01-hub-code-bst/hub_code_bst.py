"""Task 1 - hub codes in a BST: insert and search, tree height for different insertion orders, effect of sorted input."""


class Node:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None


class HubBST:
    def __init__(self, keys=()):
        self.root = None
        for k in keys:
            self.insert(k)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        cur = self.root
        while True:
            if key == cur.key:
                return
            nxt = cur.left if key < cur.key else cur.right
            if nxt is None:
                if key < cur.key:
                    cur.left = Node(key)
                else:
                    cur.right = Node(key)
                return
            cur = nxt

    def search(self, key):
        cur, depth = self.root, 0
        while cur:
            depth += 1
            if cur.key == key:
                return depth
            cur = cur.left if key < cur.key else cur.right
        return None

    def height(self):
        def h(n):
            return 0 if n is None else 1 + max(h(n.left), h(n.right))
        return h(self.root)

    def show(self):
        lines = []
        def walk(n, indent):
            if n:
                walk(n.right, indent + "      ")
                lines.append(indent + n.key)
                walk(n.left, indent + "      ")
        walk(self.root, "  ")
        return "\n".join(lines)


hubs = ["MAA", "BLR", "HYD", "BOM", "DEL", "CCU", "AMD", "PNQ", "COK", "JAI", "LKO", "NAG"]

mixed = ["JAI", "CCU", "MAA", "BOM", "DEL", "LKO", "PNQ", "AMD", "BLR", "COK", "HYD", "NAG"]
tree = HubBST(mixed)
print("Insertion order:", mixed)
print(f"Height: {tree.height()}  (best possible for 12 keys is 4)")
print(tree.show())
for code in ["HYD", "NAG", "GOI"]:
    d = tree.search(code)
    print(f"search {code}: " + (f"found at depth {d}" if d else "not found"))

tree.insert("GOI")
print(f"\nAfter inserting GOI, search GOI: depth {tree.search('GOI')}")

sorted_tree = HubBST(sorted(hubs))
print(f"\nInsertion in sorted order: {sorted(hubs)}")
print(f"Height: {sorted_tree.height()}  - every node only has a right child, the tree is a linked list")
print(f"search NAG now needs {sorted_tree.search('NAG')} comparisons instead of {tree.search('NAG')}")
print("\nSorted input makes search O(n) instead of O(log n). Shuffle the input or use a self-balancing")
print("tree (AVL / red-black) to keep the height close to log2(n).")
