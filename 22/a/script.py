import re
from collections import Counter, defaultdict, deque
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
from functools import cache
import math

ans = 0
MODULO = 16777216

with open("../input.txt") as file:
    seeds = file.read().splitlines()


for seed in seeds:
    secret = int(seed)
    for _ in range(2000):
        secret = ((secret * 64) ^ secret) % MODULO
        secret = ((secret // 32) ^ secret) % MODULO
        secret = ((secret * 2048) ^ secret) % MODULO
    ans += secret
print(ans)
