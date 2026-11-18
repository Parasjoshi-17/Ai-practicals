"""Practical 12: DFS maze solving. S=start, G=goal, #=wall."""
maze = [
    list("S..#."),
    list(".#..."),
    list("...#."),
    list("#...."),
    list("...#G"),
]
start, goal = (0, 0), (4, 4)
rows, cols = len(maze), len(maze[0])

def dfs(start, goal):
    stack = [start]
    parent = {start: None}
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    while stack:
        r, c = stack.pop()
        if (r,c) == goal:
            path = []
            current = goal
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        for dr, dc in moves:
            nr, nc = r+dr, c+dc
            nxt = (nr,nc)
            if (0 <= nr < rows and 0 <= nc < cols
                    and maze[nr][nc] != "#" and nxt not in parent):
                parent[nxt] = (r,c)
                stack.append(nxt)
    return None

path = dfs(start, goal)
print("DFS path:", path)
if path:
    for r,c in path:
        if maze[r][c] not in "SG":
            maze[r][c] = "*"
for row in maze:
    print("".join(row))
