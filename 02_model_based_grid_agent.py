"""Practical 2: Model-based agent navigating a grid using internal state."""
from collections import deque
grid = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
]
start, goal = (0, 0), (3, 3)
# The agent stores a model of the world and its current position.
internal_state = {
    "position": start,
    "obstacles": {(r, c) for r, row in enumerate(grid)
                  for c, value in enumerate(row) if value == 1},
    "goal": goal,
}

def find_route(state, rows, cols):
    queue = deque([state["position"]])
    parent = {state["position"]: None}
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        current = queue.popleft()
        if current == state["goal"]:
            route = []
            while current is not None:
                route.append(current)
                current = parent[current]
            return route[::-1]
        r, c = current
        for dr, dc in moves:
            nxt = (r + dr, c + dc)
            nr, nc = nxt
            if (0 <= nr < rows and 0 <= nc < cols
                    and nxt not in state["obstacles"]
                    and nxt not in parent):
                parent[nxt] = current
                queue.append(nxt)
    return None

route = find_route(internal_state, len(grid), len(grid[0]))
if route:
    for position in route:
        internal_state["position"] = position
        print("Agent position:", internal_state["position"])
    print("Goal reached.")
else:
    print("No route exists.")
