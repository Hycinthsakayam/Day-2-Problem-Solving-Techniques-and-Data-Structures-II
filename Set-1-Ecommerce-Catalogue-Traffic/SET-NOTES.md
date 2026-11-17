# Set 1 – E-Commerce Catalogue and Traffic Analysis

## Decision table

| Problem | Data structure / pattern | Reason | Complexity |
|---|---|---|---|
| Category browsing | Binary search tree | Inorder traversal gives the alphabetical menu; search follows one path | O(h) search, h = 5 here |
| SKU look-up | Hash table (chaining) / dict | Direct jump to a bucket by hash; collisions kept in a short chain | O(1) average |
| Deployment order | Directed graph, DFS topological sort (and Kahn's BFS) | A service must come after everything it depends on; a back edge reveals a loop | O(V + E) |
| Peak traffic window | Fixed-size sliding window | Reuse the previous 180-minute sum instead of re-adding | O(n) vs O(n·k) brute force |
| Gift-card pairs | Two pointers on a sorted list | Move the left pointer up if the sum is too small, the right one down if too big | O(n) time, O(1) space |
