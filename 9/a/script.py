import re
from collections import Counter, defaultdict
from itertools import zip_longest

ans = 0

with open("../input.txt") as file:
    line = file.read()

blocks = []
for i in range(len(line)):
    blocks += int(line[i]) * (["."] if i % 2 else [str(i // 2)])

l = 0
r = len(blocks) - 1
while l < r:
    if blocks[l] != ".":
        l += 1
    elif blocks[r] == ".":
        r -= 1
    else:
        blocks[l] = blocks[r]
        blocks[r] = "."

for i in range(len(blocks)):
    if blocks[i] == ".":
        break
    ans += i * int(blocks[i])

print(ans)
