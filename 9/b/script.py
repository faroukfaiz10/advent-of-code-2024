import re
from collections import Counter, defaultdict
from itertools import zip_longest
from bisect import bisect_left, insort
from operator import itemgetter
import math

ans = 0

with open("../input.txt") as file:
    line = file.read()

blocks = []
files = []
free = defaultdict(list)
for i in range(len(line)):
    repetition = int(line[i])
    if i % 2:
        free[min(repetition, 9)].append((len(blocks), repetition))
        blocks += repetition * ["."]
    else:
        files.append((len(blocks), repetition))
        blocks += repetition * [str(i // 2)]


def get_free_size(file_length):
    size = None
    min_idx = math.inf
    for j in range(file_length, 10):
        if len(free[j]) and free[j][0][0] < min_idx:
            min_idx = free[j][0][0]
            size = j
    return size


for i in range(len(files) - 1, -1, -1):
    file_start_idx, file_length = files[i]
    if not file_length:
        continue

    size = get_free_size(file_length)
    if not size:
        continue

    free_idx, free_size = free[size][0]
    if free_idx >= file_start_idx:
        continue

    for k in range(file_length):
        blocks[free_idx + k] = blocks[file_start_idx + k]
        blocks[file_start_idx + k] = "."
    files[i] = (free_idx, file_length)
    free[size].pop(0)
    diff = free_size - file_length
    if diff:
        insort(
            free[min(9, diff)],
            (free_idx + file_length, diff),
        )

for i in range(len(files)):
    start_idx, length = files[i]
    ans += i * (start_idx * length + (length * (length - 1)) // 2)

print(ans)
