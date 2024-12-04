import re
from collections import Counter

with open("../input.txt") as file:
    lines = file.read().splitlines()

checks = ["MAS", "SAM"]

ans = 0
for i in range(len(lines) - 2):
    for j in range(len(lines[0]) - 2):
        diag1 = lines[i][j] + lines[i + 1][j + 1] + lines[i + 2][j + 2]
        diag2 = lines[i][j + 2] + lines[i + 1][j + 1] + lines[i + 2][j]
        ans += diag1 in checks and diag2 in checks

print(ans)
