# Set 2 – Insurance Claims Processing

## Complexity per solution

| Task | Solution | Time | Space | Tests include |
|---|---|---|---|---|
| 1 | BST insert / search | O(h) – O(log n) balanced, O(n) skewed | O(n) | empty tree, duplicate ID, sorted inorder |
| 1 | Traversals | O(n) | O(h) recursion | pre / post order on a small tree |
| 2 | Dict keyed by (normalised policy, incident date) | O(n) for n claims | O(n) | empty list, exact and case/space duplicates, 3 copies |
| 3 | BFS shortest path | O(V + E) | O(V) | empty graph, no path, start = goal |
| 3 | DFS loop detection | O(V + E) | O(V) | no loop, self-loop |
| 4 | Variable sliding window | O(n) | O(1) | empty, no day above 100, exactly 100, repeated values |
| 5 | Two-pointer merge | O(n + m) | O(n + m) output | both / one empty, duplicates, stable ties |
