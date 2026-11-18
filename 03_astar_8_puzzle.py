"""Practical 3: A* search for the 8-puzzle. 0 represents the blank."""
import heapq

START = (1, 2, 3, 4, 0, 6, 7, 5, 8)
GOAL  = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def manhattan(state):
    distance = 0
    for index, tile in enumerate(state):
        if tile == 0:
            continue
        goal_index = GOAL.index(tile)
        r1, c1 = divmod(index, 3)
        r2, c2 = divmod(goal_index, 3)
        distance += abs(r1-r2) + abs(c1-c2)
    return distance

def neighbors(state):
    zero = state.index(0)
    r, c = divmod(zero, 3)
    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr*3+nc
            new_state = list(state)
            new_state[zero], new_state[j] = new_state[j], new_state[zero]
            yield tuple(new_state)

def astar(start, goal):
    frontier = [(manhattan(start), 0, start)]
    parent = {start: None}
    cost = {start: 0}
    while frontier:
        _, g, current = heapq.heappop(frontier)
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        if g != cost[current]:
            continue
        for nxt in neighbors(current):
            new_g = g + 1
            if new_g < cost.get(nxt, float("inf")):
                cost[nxt] = new_g
                parent[nxt] = current
                heapq.heappush(frontier, (new_g + manhattan(nxt), new_g, nxt))
    return None

def show(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])

path = astar(START, GOAL)
if path:
    print("Moves:", len(path)-1)
    for step, state in enumerate(path):
        print(f"\nStep {step}")
        show(state)
else:
    print("No solution found.")
