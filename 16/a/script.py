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

"""
Pop from right bug: We don't re-queue a node if the new path has a higher cost, but the cost of reaching the node is not the only criteria to consider. 
A path reaching a node with a higher cost could be better than one reaching it with a lower cost if the former reaches the node in a "better" direction.

Popping from the left probably works because the directions are correct by design: The start node is at the bottom left and the only way forward is 
north-east which is likely to be the right direction to reach a node. But the current implementation could probably still give sub-optimal result for 
a carefully crafter counter-example.

To avoid potential issues, keep track of the lowest cost by direction in `best` (see solution B).
"""

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
        if (nx, ny) not in best or best[(nx, ny)] > ncost:
            q.append((nx, ny, ndir, ncost))
            best[(nx, ny)] = ncost

print(best[(ex, ey)])
