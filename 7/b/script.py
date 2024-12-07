import re
from collections import Counter, defaultdict
from itertools import zip_longest

ans = 0

with open("../input.txt") as file:
    for line in file.read().splitlines():
        result, rest = line.split(": ")
        result = int(result)
        nums = list(map(int, rest.split()))
        for i in range(3 ** (len(nums) - 1)):
            total = nums[0]
            operators = [(i // (3**j)) % 3 for j in range(len(nums) - 1)]
            for j in range(len(nums) - 1):
                if operators[j] == 0:
                    total += nums[j + 1]
                elif operators[j] == 1:
                    total *= nums[j + 1]
                else:
                    total = int(str(total) + str(nums[j + 1]))
                if total > result:
                    break
            if total == result:
                ans += result
                break

print(ans)
