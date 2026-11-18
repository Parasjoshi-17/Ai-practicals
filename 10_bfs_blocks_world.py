"""Practical 10: BFS planning in Blocks World.
State is a tuple of stacks; each stack is bottom-to-top.
A legal action moves the top block of one stack onto another stack or the table.
"""
from collections import deque

START = (("A", "B"), ("C",), ())
GOAL  = (("A",), ("B",), ("C",))

def successors(state):
    for i, stack in enumerate(state):
        if not stack:
            continue
        block = stack[-1]
        for j in range(len(state)):
            if i == j:
                continue
            new = [list(s) for s in state]
            new[i].pop()
            new[j].append(block)
            yield tuple(tuple(s) for s in new)
        # Move the top block to an empty table position (stack slot).
        for j in range(len(state)):
            if not state[j] and i != j:
                new = [list(s) for s in state]
                new[i].pop()
                new[j].append(block)
                yield tuple(tuple(s) for s in new)

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
        for nxt in successors(state):
            if nxt not in parent:
                parent[nxt] = state
                q.append(nxt)
    return None

path = bfs(START, GOAL)
if path:
    for step, state in enumerate(path):
        print(f"Step {step}:", state)
else:
    print("Goal not reachable.")
