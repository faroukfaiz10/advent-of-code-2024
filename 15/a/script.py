import re
from collections import Counter, defaultdict
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
from functools import cache
import math

ans = 0
grid = []
directions = []

with open("../input.txt") as file:
    is_grid = True
    for line in file.read().splitlines():
        if not line:
            is_grid = False
            continue
        if is_grid:
            grid.append(list(line))
        else:
            directions += list(line)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "@":
            x, y = i, j


def move(a, b, dir):
    global x, y

    if grid[a][b] == ".":
        return True
    elif grid[a][b] == "#":
        return False
    elif dir == ">":
        new_a, new_b = (a, b + 1)
    elif dir == "v":
        new_a, new_b = (a + 1, b)
    elif dir == "<":
        new_a, new_b = (a, b - 1)
    else:
        new_a, new_b = (a - 1, b)

    can_move = move(new_a, new_b, dir)
    if can_move:
        grid[new_a][new_b] = grid[a][b]
        if grid[a][b] == "@":
            grid[a][b] = "."
            x, y = new_a, new_b

    return can_move


for dir in directions:
    move(x, y, dir)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "O":
            ans += 100 * i + j


print(ans)
