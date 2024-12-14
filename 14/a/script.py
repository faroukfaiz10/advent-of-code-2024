import re
from collections import Counter, defaultdict
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
from functools import cache
import math

WIDTH = 101
HEIGHT = 103

with open("../input.txt") as file:
    lines = file.read().splitlines()

ps = []
vs = []
for line in lines:
    p, v = line.split()
    ps.append([int(i) for i in p.split("=")[1].split(",")])
    vs.append([int(i) for i in v.split("=")[1].split(",")])

for _ in range(100):
    for i in range(len(ps)):
        x, y = ps[i]
        x = (x + vs[i][0]) % WIDTH
        y = (y + vs[i][1]) % HEIGHT
        ps[i] = [x, y]

quadrants = [0] * 4
for x, y in ps:
    if x == WIDTH // 2 or y == HEIGHT // 2:
        continue
    quadrants[2 * (x < WIDTH // 2) + (y < HEIGHT // 2)] += 1

print(math.prod(quadrants))
