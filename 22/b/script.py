import re
from collections import Counter, defaultdict, deque
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
from functools import cache
import math

MODULO = 16777216
NUM_DAYS = 2000

ans = 0
with open("../input.txt") as file:
    seeds = file.read().splitlines()

seqs_bananas = {}

for seed in seeds:
    secret = int(seed)
    visited_seqs = set()
    diffs = [0] * NUM_DAYS
    last_price = secret % 10
    for i in range(NUM_DAYS):
        secret = ((secret * 64) ^ secret) % MODULO
        secret = ((secret // 32) ^ secret) % MODULO
        secret = ((secret * 2048) ^ secret) % MODULO

        price = secret % 10
        diffs[i] = price - last_price
        last_price = price

        if i < 2:
            continue

        key = (diffs[i - 3], diffs[i - 2], diffs[i - 1], diffs[i])
        if key in visited_seqs:
            continue

        bananas = seqs_bananas.get(key, 0) + price
        seqs_bananas[key] = bananas
        ans = max(ans, bananas)
        visited_seqs.add(key)

print(ans)
