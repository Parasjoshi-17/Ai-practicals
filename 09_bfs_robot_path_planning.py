"""Practical 9: BFS robot path planning on a grid. 0=free, 1=obstacle."""
from collections import deque

grid = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
]
start, goal = (0, 0), (3, 3)
directions = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    parent = {start: None}
    while queue:
        r, c = queue.popleft()
        current = (r, c)
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            nxt = (nr, nc)
            if (0 <= nr < rows and 0 <= nc < cols
                    and grid[nr][nc] == 0 and nxt not in parent):
                parent[nxt] = (r, c)
                queue.append(nxt)
    return None

path = bfs(grid, start, goal)
print("Path:", path)
if path:
    print("Moves:", len(path)-1)
