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
    for i, line in enumerate(file.read().splitlines()):
        if not line:
            is_grid = False
            continue
        if is_grid:
            new_line = ["."] * len(line) * 2
            for j in range(len(line)):
                new_line[2 * j] = "[" if line[j] == "O" else line[j]
                if line[j] == "@":
                    x, y = i, 2 * j
                    continue
                new_line[2 * j + 1] = "]" if line[j] == "O" else line[j]
            grid.append(new_line)
        else:
            directions += list(line)


def next_pos(a, b, dir):
    if dir == ">":
        return (a, b + 1)
    elif dir == "<":
        return (a, b - 1)
    elif dir == "v":
        return (a + 1, b)
    else:
        return (a - 1, b)


def can_move(a, b, dir):
    if grid[a][b] == ".":
        return True
    elif grid[a][b] == "#":
        return False

    to_check = [next_pos(a, b, dir)]
    if dir == "^" or dir == "v":
        if grid[a][b] == "[":
            to_check.append(next_pos(a, b + 1, dir))
        elif grid[a][b] == "]":
            to_check.append(next_pos(a, b - 1, dir))

    res = True
    for new_a, new_b in to_check:
        res = res and can_move(new_a, new_b, dir)
    return res


def move(a, b, dir, moved):
    global x, y

    if (a, b) in moved:
        return
    moved.add((a, b))

    new_a, new_b = next_pos(a, b, dir)
    if grid[new_a][new_b] != ".":
        move(new_a, new_b, dir, moved)

    if dir == "^" or dir == "v":
        if grid[a][b] == "[":
            move(a, b + 1, dir, moved)
        elif grid[a][b] == "]":
            move(a, b - 1, dir, moved)

    if grid[a][b] == "@":
        x, y = new_a, new_b

    grid[new_a][new_b] = grid[a][b]
    grid[a][b] = "."


for dir in directions:
    if not can_move(x, y, dir):
        continue
    moved = set()
    move(x, y, dir, moved)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "[":
            ans += 100 * i + j

print(ans)
