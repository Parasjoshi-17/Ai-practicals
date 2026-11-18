start = (("A", "B"), ("C",), ())
goal = (("A",), ("B",), ("C",))
visited = set()

def dfs(state, path):

    if state == goal:
        return path

    visited.add(state)

    for i in range(3):
        if state[i]:
            block = state[i][-1]

            for j in range(3):
                if i != j:
                    new = [list(s) for s in state]
                    new[i].pop()
                    new[j].append(block)

                    new = tuple(tuple(s) for s in new)

                    if new not in visited:
                        result = dfs(new, path + [new])
                        if result:
                            return result

    return None

path = dfs(start, [start])

for step, state in enumerate(path or []):
    print("Step", step, ":", state)
