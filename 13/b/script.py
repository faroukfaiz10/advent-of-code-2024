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
    xp = 10000000000000 + int(xp.split("=")[1])
    yp = 10000000000000 + int(yp.split("=")[1])

    b = (xp * ya - yp * xa) // (xb * ya - xa * yb)
    a = (xp - xb * b) // xa

    if xa * a + xb * b == xp and ya * a + yb * b == yp:
        ans += 3 * a + b

print(ans)
