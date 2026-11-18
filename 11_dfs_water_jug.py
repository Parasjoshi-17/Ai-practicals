small, big = 1,6
start = (0, 0)
visited = set()

def dfs(state, path):
    if state[1] == 1:
        return path

    visited.add(state)
    a, b = state

    moves = [
        (small, b), (a, big),  # Fill
        (0, b), (a, 0),        # Empty
        (a-min(a, big-b), b+min(a, big-b)), # Small to Big
        (a+min(b, small-a), b-min(b, small-a)) # Big to Small
    ]

    for s in moves:
        if s not in visited:
            result = dfs(s, path + [s])
            if result:
                return result

    return None

path = dfs(start, [start])
print("Solution:", path)
