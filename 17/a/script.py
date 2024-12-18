import re
from collections import Counter, defaultdict, deque
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
from functools import cache
import math

ans = []

with open("../input.txt") as file:
    lines = file.read().splitlines()

A, B, C = [int(lines[i].split(": ")[1]) for i in range(3)]
program = [int(i) for i in lines[4].split(": ")[1].split(",")]

ip = 0


def combo(operand):
    if operand < 4:
        return operand
    return [A, B, C][operand - 4]


while ip < len(program):
    opcode = program[ip]
    operand = program[ip + 1]
    if opcode == 0:
        A //= 2 ** combo(operand)
    elif opcode == 1:
        B ^= operand
    elif opcode == 2:
        B = combo(operand) % 8
    elif opcode == 3:
        if A:
            ip = operand
            continue
    elif opcode == 4:
        B ^= C
    elif opcode == 5:
        ans.append(str(combo(operand) % 8))
    elif opcode == 6:
        B = A // 2 ** combo(operand)
    elif opcode == 7:
        C = A // 2 ** combo(operand)
    ip += 2

print(",".join(ans))
