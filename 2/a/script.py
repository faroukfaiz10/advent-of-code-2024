from collections import Counter

ans = 0
with open("input.txt") as file:
    for line in file.read().splitlines():
        levels = [int(i) for i in line.split()]
        asc = levels[1] > levels[0]
        safe = True
        for i in range(len(levels) - 1):
            diff = levels[i + 1] - levels[i]
            if (
                abs(diff) > 3
                or abs(diff) < 1
                or (asc and diff < 0)
                or (not asc and diff > 0)
            ):
                safe = False
                break
        ans += 1 if safe else 0
print(ans)
