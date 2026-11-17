"""Task 3 - 10 hubs as an adjacency list: fewest-hop route with BFS and every hub reachable from the central depot with DFS."""
from collections import deque

routes = {                      # direct routes (one-way, as operated)
    "NAG": ["DEL", "BOM", "HYD", "CCU"],      # central depot (Nagpur)
    "DEL": ["JAI", "LKO", "NAG"],
    "BOM": ["AMD", "PNQ", "NAG"],
    "HYD": ["BLR", "MAA", "NAG"],
    "CCU": ["LKO", "NAG"],
    "BLR": ["MAA", "COK"],
    "MAA": ["BLR"],
    "JAI": ["AMD"],
    "AMD": ["BOM"],
    "PNQ": ["BLR"],
    "LKO": [],
    "COK": [],
    "GOI": ["PNQ"],              # Goa only sends parcels out, nothing reaches it
}


def fewest_hops(graph, start, goal):
    prev = {start: None}
    q = deque([start])
    while q:
        hub = q.popleft()
        if hub == goal:
            path = []
            while hub:
                path.append(hub)
                hub = prev[hub]
            return path[::-1]
        for nxt in graph.get(hub, []):
            if nxt not in prev:
                prev[nxt] = hub
                q.append(nxt)
    return None


def reachable(graph, start):
    seen, order, stack = set(), [], [start]
    while stack:
        hub = stack.pop()
        if hub in seen:
            continue
        seen.add(hub)
        order.append(hub)
        for nxt in reversed(graph.get(hub, [])):
            if nxt not in seen:
                stack.append(nxt)
    return order


print("Adjacency list:")
for hub, nxt in routes.items():
    print(f"  {hub} -> {', '.join(nxt) if nxt else '(none)'}")

for a, b in [("JAI", "COK"), ("CCU", "MAA"), ("MAA", "DEL"), ("LKO", "MAA")]:
    p = fewest_hops(routes, a, b)
    print(f"\nFewest hops {a} -> {b}: " + (f"{' -> '.join(p)}  ({len(p) - 1} hops)" if p else "no route"))

r = reachable(routes, "NAG")
print(f"\nReachable from central depot NAG (DFS order): {', '.join(r)}")
print(f"Not reachable: {sorted(set(routes) - set(r))}")
print("\nBFS gives the fewest hops because it explores all 1-hop hubs, then 2-hop hubs, and so on. DFS lists")
print("every hub connected to the depot. Both are O(V + E) on an adjacency list.")
