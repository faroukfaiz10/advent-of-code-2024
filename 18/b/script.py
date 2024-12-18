import re
from collections import Counter, defaultdict, deque
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
from functools import cache
import math


SIZE = 71
grid = [["."] * SIZE for _ in range(SIZE)]

with open("../input.txt") as file:
    lines = file.read().splitlines()


for i in range(len(lines)):
    x, y = lines[i].split(",")
    grid[int(y)][int(x)] = "#"
    q = [(0, 0)]
    visited = set()
    found = False
    while q:
        x, y = q.pop()
        if (x, y) == (SIZE - 1, SIZE - 1):
            found = True
            break
        candidates = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
        for a, b in candidates:
            if not (0 <= a < SIZE and 0 <= b < SIZE) or grid[b][a] == "#":
                continue
            if (a, b) in visited:
                continue
            q.append((a, b))
            visited.add((a, b))
    if not found:
        print(lines[i])
        break
