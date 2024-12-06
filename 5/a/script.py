import re
from collections import Counter

ans = 0
orderings = []
updates = []
medians = []

with open("../input.txt") as file:
    for line in file.read().splitlines():
        if "|" in line:
            orderings.append(line.split("|"))
        elif "," in line:
            pages = line.split(",")
            indices = {}
            for i, page in enumerate(pages):
                indices[page] = i
            updates.append(indices)
            medians.append(int(pages[len(pages) // 2]))

for i in range(len(updates)):
    ordered = True
    for l, r in orderings:
        try:
            li = updates[i][l]
            ri = updates[i][r]
            if li > ri:
                ordered = False
                break
        except KeyError:
            pass
    ans += medians[i] if ordered else 0

print(ans)
