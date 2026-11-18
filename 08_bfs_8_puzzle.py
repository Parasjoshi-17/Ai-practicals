"""Practical 8: BFS planning for the 8-puzzle. 0 is the blank."""
from collections import deque

START = (1, 2, 3, 4, 0, 6, 7, 5, 8)
GOAL  = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def neighbors(state):
    z = state.index(0)
    r, c = divmod(z, 3)
    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr*3+nc
            s = list(state)
            s[z], s[j] = s[j], s[z]
            yield tuple(s)

def bfs(start, goal):
    q = deque([start])
    parent = {start: None}
    while q:
        state = q.popleft()
        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]
        for nxt in neighbors(state):
            if nxt not in parent:
                parent[nxt] = state
                q.append(nxt)
    return None

path = bfs(START, GOAL)
if path:
    print("Number of moves:", len(path)-1)
    for state in path:
        print(state[:3], state[3:6], state[6:])
        print()
else:
    print("No solution found.")
