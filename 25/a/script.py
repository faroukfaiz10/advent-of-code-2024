import re
from collections import Counter, defaultdict, deque
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
from functools import cache
import math

ans = 0
columns = [-1] * 5
is_first_line = True
keys = []
locks = []


def parse_key_or_lock(lines):
    columns = [-1] * 5
    is_key = lines[0] == ("." * 5)
    for line in lines:
        for i in range(5):
            columns[i] += line[i] == "#"
    (keys if is_key else locks).append(columns)


with open("../input.txt") as file:
    lines = file.read().splitlines()
    for i in range((len(lines) + 1) // 8):
        parse_key_or_lock(lines[8 * i : 8 * (i + 1) - 1])

for key in keys:
    for lock in locks:
        ans += all(key[i] + lock[i] < 6 for i in range(5))


print(ans)
