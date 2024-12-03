from collections import Counter


def check(levels, recurse):
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        if (
            abs(diff) > 3
            or abs(diff) < 1
            or (asc and diff < 0)
            or (not asc and diff > 0)
        ):
            if not recurse:
                return False

            l1 = levels.copy()
            l2 = levels.copy()
            del l1[i]
            del l2[i + 1]
            return check(l1, False) or check(l2, False)
    return True


ans = 0
with open("input.txt") as file:
    for line in file.read().splitlines():
        levels = [int(i) for i in line.split()]
        asc = Counter([levels[i + 1] > levels[i] for i in range(3)]).most_common(1)[0][
            0
        ]
        ans += 1 if check(levels, True) else 0


print(ans)
