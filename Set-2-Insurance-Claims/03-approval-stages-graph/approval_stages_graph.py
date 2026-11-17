"""Task 3 - claim approval stages as a directed graph: shortest path with BFS and loop detection with DFS."""
from collections import deque

stages = {
    "Registration":   ["Document Check"],
    "Document Check": ["Assessment"],
    "Assessment":     ["Surveyor", "Settlement"],      # small claims can skip the surveyor
    "Surveyor":       ["Senior Review", "Settlement"],
    "Senior Review":  ["Settlement"],
    "Settlement":     ["Closed"],
    "Closed":         [],
}


def shortest_path(graph, start, goal):
    if start not in graph or goal not in graph:
        return None
    prev = {start: None}
    q = deque([start])
    while q:
        node = q.popleft()
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = prev[node]
            return path[::-1]
        for nxt in graph[node]:
            if nxt not in prev:
                prev[nxt] = node
                q.append(nxt)
    return None


def find_loop(graph):
    state = {}                                    # 1 = on current path, 2 = finished
    path = []

    def dfs(n):
        state[n] = 1
        path.append(n)
        for m in graph.get(n, []):
            if state.get(m) == 1:
                return path[path.index(m):] + [m]
            if m not in state:
                found = dfs(m)
                if found:
                    return found
        state[n] = 2
        path.pop()
        return None

    for n in graph:
        if n not in state:
            found = dfs(n)
            if found:
                return found
    return None


if __name__ == "__main__":
    for a, b in [("Registration", "Settlement"), ("Surveyor", "Closed"), ("Settlement", "Registration")]:
        p = shortest_path(stages, a, b)
        print(f"Shortest path {a} -> {b}: " + (" -> ".join(p) + f"  ({len(p) - 1} steps)" if p else "no path"))
    print("\nLoop in the normal flow:", find_loop(stages))

    rework = {k: list(v) for k, v in stages.items()}
    rework["Senior Review"].append("Assessment")   # senior review sends the claim back for re-assessment
    print("Add rework edge Senior Review -> Assessment")
    print("Loop found:", " -> ".join(find_loop(rework)))
    print("\nBFS explores stage by stage, so the first time it reaches the goal is the fewest steps: O(V + E).")
    print("DFS finds a loop when it reaches a stage that is still on the current path (a back edge): O(V + E).")
