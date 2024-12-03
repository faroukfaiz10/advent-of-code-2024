import re
from collections import Counter


with open("../input.txt") as file:
    matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", file.read())
ans = 0
enabled = True
for a, b, c, d in matches:
    if c:
        enabled = True
    elif d:
        enabled = False
    elif enabled:
        ans += int(a) * int(b)
print(ans)
