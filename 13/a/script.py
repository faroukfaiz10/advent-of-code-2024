import re
from collections import Counter, defaultdict
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
from functools import cache
import math

ans = 0

with open("../input.txt") as file:
    lines = file.read().splitlines()

for i in range((len(lines) + 1) // 4):
    xa, ya = lines[4 * i].split(":")[1].split(", ")
    xa = int(xa.split("+")[1])
    ya = int(ya.split("+")[1])
    xb, yb = lines[4 * i + 1].split(":")[1].split(", ")
    xb = int(xb.split("+")[1])
    yb = int(yb.split("+")[1])
    xp, yp = lines[4 * i + 2].split(":")[1].split(", ")
    xp = int(xp.split("=")[1])
    yp = int(yp.split("=")[1])

    min_score = math.inf
    for a in range(101):
        for b in range(101):
            x = xa * a + xb * b
            y = ya * a + yb * b
            if x == xp and y == yp:
                min_score = min(min_score, 3 * a + b)
    if min_score < math.inf:
        ans += min_score

print(ans)
