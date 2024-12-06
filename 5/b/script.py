import re
from collections import Counter, defaultdict

ans = 0
orderings = defaultdict(list)
updates = []
medians = []

with open("../input.txt") as file:
    for line in file.read().splitlines():
        if "|" in line:
            l, r = line.split("|")
            orderings[l].append(r)
        elif "," in line:
            pages = line.split(",")
            indices = {}
            for i, page in enumerate(pages):
                indices[page] = i
            updates.append(indices)
            medians.append(int(pages[len(pages) // 2]))


def is_ordered(update):
    for l in orderings:
        for r in orderings[l]:
            try:
                li = update[l]
                ri = update[r]
                if li > ri:
                    return False
            except KeyError:
                pass
    return True


for i in range(len(updates)):
    if is_ordered(updates[i]):
        continue
    pages = set(updates[i].keys())
    ordered = []
    while pages:
        late = set()
        for page in pages:
            for later_page in orderings[page]:
                late.add(later_page)
        next = (pages - late).pop()
        pages.remove(next)
        ordered.append(int(next))

    ans += ordered[len(ordered) // 2]

print(ans)
