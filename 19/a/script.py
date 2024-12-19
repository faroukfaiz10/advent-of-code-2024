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
def check(design):
    if len(design) == 0:
        return True
    for i in range(len(design), 0, -1):
        if design[:i] in patterns:
            # print(design, design[:i], design[i:])
            good = check(design[i:])
            if good:
                return True
    return False


for design in lines[2:]:
    ans += check(design)
print(ans)
