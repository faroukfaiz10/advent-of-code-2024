import re
from collections import Counter, defaultdict, deque
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
from functools import cache
import math

ans = 0

with open("../input.txt") as file:
    grid = [list(line) for line in file.read().splitlines()]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            (sx, sy) = (i, j)
        elif grid[i][j] == "E":
            (ex, ey) = (i, j)


def get_best_costs(ix, iy):
    q = deque([(ix, iy, 0)])
    best = {}
    while q:
        x, y, cost = q.popleft()
        candidates = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for a, b in candidates:
            if not (0 <= a < len(grid) and 0 <= b < len(grid[0])) or grid[a][b] == "#":
                continue
            if best.get((a, b), math.inf) > cost + 1:
                best[(a, b)] = cost + 1
                q.append((a, b, cost + 1))

    best[(ix, iy)] = 0
    return best


sbest = get_best_costs(sx, sy)
ebest = get_best_costs(ex, ey)
og_cost = sbest[(ex, ey)]

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        if grid[i][j] != "#":
            continue
        neighbors = [
            (a, b)
            for (a, b) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            if grid[a][b] != "#"
        ]
        for a1, b1 in neighbors:
            for a2, b2 in neighbors:
                saved = og_cost - (sbest[(a1, b1)] + ebest[(a2, b2)] + 2)
                if saved >= 100:
                    ans += 1

print(ans)
