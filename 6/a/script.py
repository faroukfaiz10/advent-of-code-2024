import re
from collections import Counter, defaultdict

with open("../input.txt") as file:
    grid = [list(line) for line in file.read().splitlines()]

for i in range(len(grid)):
    if "^" in grid[i]:
        x = i
        y = grid[i].index("^")
        break


def get_next(dir, x, y):
    if dir == 0:
        return [x - 1, y]
    if dir == 1:
        return [x, y + 1]
    if dir == 2:
        return [x + 1, y]
    return [x, y - 1]


dir = 0  # 0: ^, 1: >, etc.
visited = {(x, y)}
while True:
    new_x, new_y = get_next(dir, x, y)
    if not (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])):
        break
    if grid[new_x][new_y] != "#":
        x, y = new_x, new_y
        visited.add((x, y))
    else:
        dir = (dir + 1) % 4

print(len(visited))
