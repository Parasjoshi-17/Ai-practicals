"""Practical 14: DFS for Missionaries and Cannibals.
State: (missionaries_left, cannibals_left, boat_side); side 0=left, 1=right.
"""
TOTAL_M, TOTAL_C = 3, 3
BOAT = [(1,0),(2,0),(0,1),(0,2),(1,1)]

def safe(m, c):
    mr, cr = TOTAL_M-m, TOTAL_C-c
    return (0 <= m <= TOTAL_M and 0 <= c <= TOTAL_C
            and (m == 0 or m >= c)
            and (mr == 0 or mr >= cr))

def successors(state):
    m, c, side = state
    for dm, dc in BOAT:
        if side == 0:
            nxt = (m-dm, c-dc, 1)
        else:
            nxt = (m+dm, c+dc, 0)
        if safe(nxt[0], nxt[1]):
            yield nxt

def dfs():
    start, goal = (3,3,0), (0,0,1)
    stack = [start]
    parent = {start: None}
    while stack:
        state = stack.pop()
        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]
        for nxt in successors(state):
            if nxt not in parent:
                parent[nxt] = state
                stack.append(nxt)
    return None

print("State (M left, C left, boat side):")
print(dfs())
