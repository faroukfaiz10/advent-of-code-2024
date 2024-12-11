import re
from collections import Counter, defaultdict
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
import math

ans = 0

with open("../input.txt") as file:
    grid = [list(line) for line in file.read().splitlines()]


def get_valid_neighbors(i, j):
    s = set()
    for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            s.add((x, y))
    return s


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != "0":
            continue
        q = [(i, j)]
        visited = {(i, j)}
        while q:
            x, y = q.pop()
            visited.add((x, y))
            if grid[x][y] == "9":
                ans += 1
                continue
            q += [
                (i, j)
                for i, j in get_valid_neighbors(x, y) - visited
                if grid[i][j] == str(int(grid[x][y]) + 1)
            ]

print(ans)
