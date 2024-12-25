import re
from collections import Counter, defaultdict, deque
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
from functools import cache
import math

ans = 0
is_reading_gates = False
num_bits = 0

wires = {}
connections = {}
with open("../input.txt") as file:
    for line in file.read().splitlines():
        if line == "":
            is_reading_gates = True
            continue
        if not is_reading_gates:
            wire, value = line.split(": ")
            wires[wire] = int(value)
            continue

        inputs, output = line.split(" -> ")
        if output[0] == "z" and output[1:].isdigit():
            num_bits += 1

        for i in range(3):
            gate = [" AND ", " OR ", " XOR "][i]
            if gate in inputs:
                wire1, wire2 = inputs.split(gate)
                connections[output] = (wire1, wire2, i)


@cache
def get_bit(wire):
    try:
        return wires[wire]
    except:
        wire1, wire2, gate = connections[wire]
        bit1 = get_bit(wire1)
        bit2 = get_bit(wire2)
        if gate == 0:
            return bit1 & bit2
        elif gate == 1:
            return bit1 | bit2
        else:
            return bit1 ^ bit2


print(
    int("".join([str(get_bit(f"z{num_bits - i - 1:02}")) for i in range(num_bits)]), 2)
)
