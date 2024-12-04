import re
from collections import Counter

with open("../input.txt") as file:
    lines = file.read().splitlines()

nlines = len(lines)
ncols = len(lines[0])


def count(indices):
    s = ""
    for i, j in indices:
        if i < 0 or i >= nlines or j < 0 or j >= ncols:
            return 0
        s += lines[i][j]
    return 1 if s == "XMAS" else 0


ans = 0
for i in range(nlines):
    for j in range(ncols):
        ans += count([[i, j], [i + 1, j], [i + 2, j], [i + 3, j]])
        ans += count([[i, j], [i - 1, j], [i - 2, j], [i - 3, j]])
        ans += count([[i, j], [i, j + 1], [i, j + 2], [i, j + 3]])
        ans += count([[i, j], [i, j - 1], [i, j - 2], [i, j - 3]])
        ans += count([[i, j], [i + 1, j + 1], [i + 2, j + 2], [i + 3, j + 3]])
        ans += count([[i, j], [i + 1, j - 1], [i + 2, j - 2], [i + 3, j - 3]])
        ans += count([[i, j], [i - 1, j + 1], [i - 2, j + 2], [i - 3, j + 3]])
        ans += count([[i, j], [i - 1, j - 1], [i - 2, j - 2], [i - 3, j - 3]])

print(ans)
