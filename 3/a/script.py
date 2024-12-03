import re
from collections import Counter


with open("../input.txt") as file:
    pairs = re.findall(r"mul\((\d+),(\d+)\)", file.read())
ans = 0
for a, b in pairs:
    ans += int(a) * int(b)
print(ans)
