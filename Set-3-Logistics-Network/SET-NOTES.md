# Set 3 – Logistics Network and Delivery Windows

## Decision and complexity table

| Problem | Data structure / pattern | Why | Time | Space |
|---|---|---|---|---|
| Hub code search | BST | Ordered keys; height 5 for a mixed order, 12 for sorted input | O(h) | O(n) |
| Tracking look-up and double scans | Hash map; key (tracking, hub) | O(1) look-up, repeat scans found in one pass | O(n) | O(n) |
| Fewest-hop route | Adjacency list + BFS | Explores level by level, so the first hit has the fewest hops | O(V + E) | O(V) |
| Hubs reachable from depot | DFS with a stack | Visits everything connected; GOI is not reachable | O(V + E) | O(V) |
| Best 4-hour window | Fixed sliding window | Running total updated per hour | O(n) | O(1) |
| Route palindrome | Two pointers | Compare from both ends, skip separators, ignore case | O(n) | O(1) |
