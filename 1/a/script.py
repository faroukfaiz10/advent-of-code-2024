left = []
right = []
with open("input.txt") as file:
    for line in file.read().splitlines():
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))
left.sort()
right.sort()

ans = 0
for i in range(len(left)):
    ans += abs(left[i] - right[i])
print(ans)
