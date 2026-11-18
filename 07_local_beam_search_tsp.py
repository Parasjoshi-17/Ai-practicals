"""Practical 7: Local Beam Search for TSP (small illustrative distance matrix)."""
import random

DIST = [
    [0, 10, 15, 20, 12],
    [10, 0, 35, 25, 17],
    [15, 35, 0, 30, 28],
    [20, 25, 30, 0, 14],
    [12, 17, 28, 14, 0],
]
N = len(DIST)
BEAM_WIDTH = 4
MAX_STEPS = 500
random.seed(7)

def tour_cost(tour):
    return sum(DIST[tour[i]][tour[(i+1) % N]] for i in range(N))

def neighbors(tour):
    result = []
    for i in range(1, N):
        for j in range(i+1, N):
            candidate = list(tour)
            candidate[i], candidate[j] = candidate[j], candidate[i]
            result.append(tuple(candidate))
    return result

beam = {tuple([0] + random.sample(range(1, N), N-1)) for _ in range(BEAM_WIDTH)}
best = min(beam, key=tour_cost)
for _ in range(MAX_STEPS):
    candidates = set()
    for tour in beam:
        candidates.update(neighbors(tour))
    if not candidates:
        break
    beam = set(sorted(candidates, key=tour_cost)[:BEAM_WIDTH])
    current_best = min(beam, key=tour_cost)
    if tour_cost(current_best) < tour_cost(best):
        best = current_best

print("Best tour:", list(best) + [best[0]])
print("Tour cost:", tour_cost(best))
