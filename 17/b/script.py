import re
from collections import Counter, defaultdict, deque
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
from functools import cache
import math
import json


with open("../input.txt") as file:
    lines = file.read().splitlines()

program = [int(i) for i in lines[4].split(": ")[1].split(",")]

candidates = defaultdict(list)
for a in range(2**10):
    B = (a % 8) ^ 3
    C = a // 2**B
    B ^= 5 ^ C

    candidates[B % 8].append(format(a, "010b"))


# Idea: https://www.reddit.com/r/adventofcode/comments/1hgiihp/comment/m2jlslp
def build(output_idx, bin_value):
    if output_idx == -1:
        print(int(bin_value, 2))
        exit(0)

    for candidate in candidates[program[output_idx]]:
        if output_idx == len(program) - 1:
            build(output_idx - 1, candidate)
        elif candidate.startswith(bin_value[-7:]):
            build(output_idx - 1, bin_value + candidate[-3:])


build(len(program) - 1, None)
