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
    for i in range(len(stones)):
        l = len(stones[i])
        if stones[i] == "0":
            stones[i] = "1"
        elif l % 2 == 0:
            right = stones[i][l // 2 :].lstrip("0") or "0"
            stones.append(right)
            stones[i] = stones[i][: l // 2]
        else:
            stones[i] = str(int(stones[i]) * 2024)
print(len(stones))
