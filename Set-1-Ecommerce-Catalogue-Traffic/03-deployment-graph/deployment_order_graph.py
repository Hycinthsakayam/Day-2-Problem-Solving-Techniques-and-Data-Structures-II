"""Task 3 - microservice dependencies as a graph: a valid deployment order (DFS and BFS) and circular dependency detection."""
from collections import deque

# service -> services it depends on (they must be deployed first)
depends_on = {
    "cart":         ["pricing", "inventory", "auth"],
    "pricing":      ["inventory", "catalogue"],
    "inventory":    ["catalogue"],
    "checkout":     ["cart", "payment", "auth"],
    "payment":      ["auth"],
    "catalogue":    [],
    "auth":         [],
    "notification": ["checkout"],
    "search":       ["catalogue"],
}


def deploy_order_dfs(graph):
    """returns (order, cycle). cycle is a list of services if a loop is found."""
    WHITE, GREY, BLACK = 0, 1, 2
    colour = {s: WHITE for s in graph}
    order, path = [], []

    def visit(s):
        colour[s] = GREY
        path.append(s)
        for dep in graph[s]:
            if colour[dep] == GREY:                      # back edge -> cycle
                return path[path.index(dep):] + [dep]
            if colour[dep] == WHITE:
                cycle = visit(dep)
                if cycle:
                    return cycle
        colour[s] = BLACK
        path.pop()
        order.append(s)                                   # all dependencies are already in order
        return None

    for s in sorted(graph):
        if colour[s] == WHITE:
            cycle = visit(s)
            if cycle:
                return None, cycle
    return order, None


def deploy_order_bfs(graph):
    """Kahn's algorithm: repeatedly deploy services whose dependencies are all deployed."""
    pending = {s: len(deps) for s, deps in graph.items()}
    users = {s: [] for s in graph}
    for s, deps in graph.items():
        for d in deps:
            users[d].append(s)
    ready = deque(sorted(s for s, n in pending.items() if n == 0))
    order = []
    while ready:
        s = ready.popleft()
        order.append(s)
        for u in sorted(users[s]):
            pending[u] -= 1
            if pending[u] == 0:
                ready.append(u)
    return order if len(order) == len(graph) else None


print("Dependencies:")
for s, deps in depends_on.items():
    print(f"  {s:<13} needs {deps if deps else '-'}")

order, cycle = deploy_order_dfs(depends_on)
print("\nDeployment order (DFS):", " -> ".join(order))
print("Deployment order (BFS):", " -> ".join(deploy_order_bfs(depends_on)))

broken = {k: list(v) for k, v in depends_on.items()}
broken["catalogue"] = ["pricing"]                   # someone adds catalogue -> pricing
print("\nAdded dependency: catalogue needs pricing")
order, cycle = deploy_order_dfs(broken)
print("DFS result: circular dependency found:", " -> ".join(cycle))
print("BFS result:", deploy_order_bfs(broken), "(some services never become ready)")
print("\nBoth run in O(V + E). DFS finds the exact loop; BFS shows that no complete order exists.")
