import re
from collections import Counter, defaultdict, deque
from itertools import zip_longest, combinations
from operator import itemgetter
from bisect import bisect_left, insort
from functools import cache
import math

ans = 0

with open("../input.txt") as file:
    lines = file.read().splitlines()

connections = defaultdict(set)
computers = set()

for line in lines:
    c1, c2 = line.split("-")
    connections[c1].add(c2)
    connections[c2].add(c1)
    computers.update({c1, c2})

for size in range(14, 2, -1):
    for c in computers:
        candidates = connections[c]
        for combination in combinations(candidates, size - 1):
            if all(
                all(
                    candidate in connections[neighbor]
                    for candidate in combination
                    if candidate != neighbor
                )
                for neighbor in combination
            ):
                print(",".join(sorted(combination + (c,))))
                exit()
