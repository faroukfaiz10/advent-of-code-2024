import re
from collections import Counter, defaultdict, deque
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
from functools import cache
import math


with open("../input.txt") as file:
    lines = file.read().splitlines()

connections = defaultdict(set)
computers = set()

for line in lines:
    c1, c2 = line.split("-")
    connections[c1].add(c2)
    connections[c2].add(c1)
    computers.update({c1, c2})


triplets = set()
for computer in computers:
    if computer[0] != "t":
        continue
    neighbors = connections[computer]

    for neighbor in neighbors:
        for second_deg_neighbor in connections[neighbor]:
            if second_deg_neighbor in neighbors:
                triplet = tuple(sorted([computer, neighbor, second_deg_neighbor]))
                triplets.add(triplet)

print(len(triplets))
