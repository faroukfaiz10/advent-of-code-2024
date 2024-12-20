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

ROWS = len(grid)
COLUMNS = len(grid[0])

for i in range(ROWS):
    for j in range(COLUMNS):
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
            if not (0 <= a < ROWS and 0 <= b < COLUMNS) or grid[a][b] == "#":
                continue
            if best.get((a, b), math.inf) > cost + 1:
                best[(a, b)] = cost + 1
                q.append((a, b, cost + 1))

    best[(ix, iy)] = 0
    return best


sbest = get_best_costs(sx, sy)
ebest = get_best_costs(ex, ey)
og_cost = sbest[(ex, ey)]

for i in range(1, ROWS - 1):
    for j in range(1, COLUMNS - 1):
        if grid[i][j] == "#":
            continue
        i_cost = sbest[(i, j)]
        for dx in range(max(-i, -20), min(ROWS - i, 21)):
            dy_start, dy_end = max(-j, -20 + abs(dx)), min(COLUMNS - j, 21 - abs(dx))
            for dy in range(dy_start, dy_end):
                if grid[i + dx][j + dy] == "#":
                    continue
                saved = og_cost - (i_cost + ebest[(i + dx, j + dy)] + abs(dx) + abs(dy))
                if saved >= 100:
                    ans += 1

print(ans)
