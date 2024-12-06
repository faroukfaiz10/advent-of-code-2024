import re
from collections import Counter, defaultdict

with open("../input.txt") as file:
    grid = [list(line) for line in file.read().splitlines()]

for i in range(len(grid)):
    if "^" in grid[i]:
        x0 = i
        y0 = grid[i].index("^")
        break


def get_next(dir, x, y):
    if dir == 0:
        return [x - 1, y]
    if dir == 1:
        return [x, y + 1]
    if dir == 2:
        return [x + 1, y]
    return [x, y - 1]


ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != ".":
            continue
        loop = False
        x, y, dir = x0, y0, 0
        visited = {(x, y, dir)}
        while True:
            new_x, new_y = get_next(dir, x, y)
            if not (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])):
                break
            if (new_x, new_y, dir) in visited:
                loop = True
                break
            if grid[new_x][new_y] != "#" and not (new_x == i and new_y == j):
                x, y = new_x, new_y
                visited.add((x, y, dir))
            else:
                dir = (dir + 1) % 4
        ans += loop

print(ans)
