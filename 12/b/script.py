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
        sides = set()
        visited.add((i, j))
        q = [(i, j)]
        while q:
            x, y = q.pop()
            candidates = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
            neighbors = [
                [a, b]
                for a, b in candidates
                if is_valid(a, b) and grid[a][b] == grid[x][y]
            ]
            sides.update(
                [(x, y, i) for i in range(4) if candidates[i] not in neighbors]
            )
            region += 1
            new = [(a, b) for a, b in neighbors if (a, b) not in visited]
            for a, b in new:
                visited.add((a, b))
            q += new

        num_sides = len(sides)
        while sides:
            x, y, d = sides.pop()
            if d == 0 or d == 1:
                num_sides -= (x, y + 1, d) in sides
                num_sides -= (x, y - 1, d) in sides
            else:
                num_sides -= (x + 1, y, d) in sides
                num_sides -= (x - 1, y, d) in sides

        ans += region * num_sides

print(ans)
