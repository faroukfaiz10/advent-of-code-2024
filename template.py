import re
from collections import Counter, defaultdict
from itertools import zip_longest

ans = 0

with open("../input.txt") as file:
    for line in file.read().splitlines():
        l, r = line.split()

print(ans)
