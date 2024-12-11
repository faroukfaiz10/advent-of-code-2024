import re
from collections import Counter, defaultdict
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
import math

ans = 0

with open("../input.txt") as file:
    stones = file.read().split()

for k in range(25):
    offset = 0
    for i in range(len(stones)):
        idx = i + offset
        l = len(stones[idx])
        if stones[idx] == "0":
            stones[idx] = "1"
        elif l % 2 == 0:
            right = stones[idx][l // 2 :].lstrip("0")
            right = right if len(right) else "0"
            stones.insert(idx + 1, right)
            stones[idx] = stones[idx][: l // 2]
            offset += 1
        else:
            stones[idx] = str(int(stones[idx]) * 2024)
print(len(stones))
