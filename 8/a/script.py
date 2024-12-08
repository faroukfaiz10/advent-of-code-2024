import re
from collections import Counter, defaultdict
from itertools import zip_longest

antennas = defaultdict(list)

with open("../input.txt") as file:
    lines = file.read().splitlines()
    height = len(lines)
    width = len(lines[0])
    for i in range(height):
        for j in range(width):
            if lines[i][j] != ".":
                antennas[lines[i][j]].append((i, j))

locations = set()


def add_location(locations, x, y, height, width):
    if x < 0 or x >= height or y < 0 or y >= width:
        return
    locations.add((x, y))


for freq in antennas:
    num_antennas = len(antennas[freq])
    for i in range(num_antennas):
        for j in range(i + 1, num_antennas):
            x1, y1 = antennas[freq][i]
            x2, y2 = antennas[freq][j]
            diff_x = x2 - x1
            diff_y = y2 - y1
            antinode = (x1 - diff_x, y1 - diff_y)
            antinode = (x1 - diff_x, y1 - diff_y)
            add_location(locations, x1 - diff_x, y1 - diff_y, height, width)
            add_location(locations, x2 + diff_x, y2 + diff_y, height, width)

print(len(locations))
