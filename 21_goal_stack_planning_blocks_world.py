"""Practical 21: Simplified Goal Stack Planning for Blocks World.
A small goal-stack-style planner achieves a specified arrangement by
pushing subgoals and applying legal primitive block moves.
"""
from copy import deepcopy

# A state is a list of stacks; each stack is bottom-to-top.
# Four table positions provide a temporary buffer.
start = [["A", "B"], ["C"], [], []]
goal = [["A"], ["B"], ["C"], []]

# Goal stack: satisfy these subgoals in order, using a temporary buffer.
goal_stack = [
    ("ON_TABLE", "B"),
    ("ON_TABLE", "C"),
    ("ON_TABLE", "B"),
]

def locate(state, block):
    for i, stack in enumerate(state):
        if block in stack:
            return i
    return None

def move_clear_block(state, block, destination):
    source = locate(state, block)
    if source is None or not state[source] or state[source][-1] != block:
        return False
    if source == destination:
        return False
    state[source].pop()
    state[destination].append(block)
    return True

state = deepcopy(start)
actions = []
# First clear B from A by moving it to a free table position.
if move_clear_block(state, "B", 2):
    actions.append("Move(B, Table position 3)")
# C is now clear; move it to another free table position.
if move_clear_block(state, "C", 3):
    actions.append("Move(C, Table position 4)")
# Put B at its required final table position.
if move_clear_block(state, "B", 1):
    actions.append("Move(B, Table position 2)")

if move_clear_block(state, "C", 2):
    actions.append("Move(C, Table position 3)")

print("Initial state:", start)
for action in actions:
    print(action)
print("Final state:", state)
print("Goal state:", goal)
print("Goal achieved:", state == goal)
