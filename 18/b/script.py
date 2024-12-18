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

l = 0
r = len(lines) - 1

while l < r:
    m = (l + r) // 2
    grid = [["."] * SIZE for _ in range(SIZE)]
    for i in range(m):
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
    if not found or l == m:
        r = m
    else:
        l = m

print(lines[l])
