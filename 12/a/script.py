import re
from collections import Counter, defaultdict
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
from functools import cache
import math

ans = 0

with open("../input.txt") as file:
    grid = [list(line) for line in file.read().splitlines()]


def is_valid(i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])


visited = set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) in visited:
            continue
        region = 0
        perimeter = 0
        visited.add((i, j))
        q = [(i, j)]
        while q:
            x, y = q.pop()
            neighbors = [
                (a, b)
                for a, b in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
                if is_valid(a, b) and grid[a][b] == grid[x][y]
            ]
            region += 1
            perimeter += 4 - len(neighbors)
            new = [(a, b) for a, b in neighbors if (a, b) not in visited]
            for a, b in new:
                visited.add((a, b))
            q += new
        ans += region * perimeter

print(ans)
