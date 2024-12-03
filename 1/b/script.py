from collections import Counter

left = []
right = []
with open("input.txt") as file:
    for line in file.read().splitlines():
        l, r = line.split()
        left.append(l)
        right.append(r)

counter = Counter(right)
ans = 0
for l in left:
    ans += int(l) * counter[l]

print(ans)
