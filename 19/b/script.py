import re
from collections import Counter, defaultdict, deque
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
from functools import cache
import math

ans = 0

with open("../input.txt") as file:
    lines = file.read().splitlines()

patterns = set(lines[0].split(", "))


@cache
def count(design):
    c = 0
    if len(design) == 0:
        return 1
    for i in range(len(design), 0, -1):
        if design[:i] in patterns:
            c += count(design[i:])
    return c


for design in lines[2:]:
    ans += count(design)
print(ans)
