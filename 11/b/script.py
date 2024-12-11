import re
from collections import Counter, defaultdict
from itertools import zip_longest
from operator import itemgetter
from functools import cache
from bisect import bisect_left, insort
import math
import sys

ans = 0

with open("../input.txt") as file:
    stones = file.read().split()


@cache
def rec(stone, blinks):
    l = len(stone)
    if blinks == 1:
        return 2 if l % 2 == 0 else 1
    if stone == "0":
        return rec("1", blinks - 1)
    elif l % 2 == 0:
        right = stone[l // 2 :].lstrip("0") or "0"
        left = stone[: l // 2]
        return rec(left, blinks - 1) + rec(right, blinks - 1)
    else:
        return rec(str(int(stone) * 2024), blinks - 1)


for stone in stones:
    ans += rec(stone, 75)

print(ans)
