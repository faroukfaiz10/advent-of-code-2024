import re
from collections import Counter, defaultdict, deque
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
from functools import cache
import math

with open("../input.txt") as file:
    grid = [list(line) for line in file.read().splitlines()]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            sx, sy = i, j
        elif grid[i][j] == "E":
            ex, ey = i, j

best = {}
q = deque([(sx, sy, 0, 0)])
parents = defaultdict(set)

while q:
    x, y, dir, cost = q.popleft()
    candidates_cost = [1] * 4
    candidates_cost[(dir + 1) % 4] += 1000
    candidates_cost[(dir + 3) % 4] += 1000
    candidates = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]

    neighbors = [
        (candidates[i][0], candidates[i][1], i, cost + candidates_cost[i])
        for i in range(4)
        if grid[candidates[i][0]][candidates[i][1]] != "#" and i != (dir + 2) % 4
    ]

    for nx, ny, ndir, ncost in neighbors:
        parents[(nx, ny)].add((x, y))
        if (nx, ny, ndir) not in best or best[(nx, ny, ndir)] > ncost:
            q.append((nx, ny, ndir, ncost))
            best[(nx, ny, ndir)] = ncost


def get_dir_change_cost(dir1, dir2):
    diff = abs(dir1 - dir2)
    return min(diff, 4 - diff) * 1000


def get_dir(px, py, cx, cy):
    dirs = [0, 1, 2, 3]
    idx = cx - px if cx - px else cy - py - 1
    return dirs[idx]


def cost_from_parent_to_child(px, py, cx, cy, dir):
    parent_child_dir = get_dir(px, py, cx, cy)
    return min(
        [
            best.get((px, py, d), math.inf)
            + get_dir_change_cost(parent_child_dir, d)
            + get_dir_change_cost(parent_child_dir, dir)
            for d in range(4)
        ]
    )


best_score = min([best.get((ex, ey, d), math.inf) for d in range(4)])
q = deque([(ex, ey, d) for d in range(4) if best.get((ex, ey, d)) == best_score])
ans = set()
while q:
    cx, cy, dir = q.popleft()
    parent_costs = [
        cost_from_parent_to_child(px, py, cx, cy, dir) for px, py in parents[(cx, cy)]
    ]
    min_cost = min(parent_costs)
    best_parents = [
        (px, py)
        for px, py in parents[(cx, cy)]
        if cost_from_parent_to_child(px, py, cx, cy, dir) == min_cost
    ]

    for px, py in best_parents:
        if (px, py) not in ans:
            parent_child_dir = get_dir(px, py, cx, cy)
            q.append((px, py, parent_child_dir))
    ans.update(best_parents)

print(len(ans) + 2)
