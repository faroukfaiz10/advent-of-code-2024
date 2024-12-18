import re
from collections import Counter, defaultdict, deque
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
from functools import cache
import math


SIZE = 71
BYTES = 1024
grid = [["."] * SIZE for _ in range(SIZE)]

with open("../input.txt") as file:
    lines = file.read().splitlines()
    for i in range(BYTES):
        x, y = lines[i].split(",")
        grid[int(y)][int(x)] = "#"

q = deque([(0, 0, 0)])
best = {}
while q:
    x, y, cost = q.popleft()
    candidates = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    for a, b in candidates:
        if not (0 <= a < SIZE and 0 <= b < SIZE) or grid[b][a] == "#":
            continue
        if cost + 1 < best.get((a, b), math.inf):
            q.append((a, b, cost + 1))
            best[(a, b)] = cost + 1

print(best[(SIZE - 1, SIZE - 1)])
