import re
from collections import Counter, defaultdict, deque
from itertools import zip_longest
from operator import itemgetter
from bisect import bisect_left, insort
from functools import cache
import math
import random


ans = 0
is_reading_gates = False
z_num_bits = 0

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
            z_num_bits += 1

        for i in range(3):
            gate = [" AND ", " OR ", " XOR "][i]
            if gate in inputs:
                wire1, wire2 = inputs.split(gate)
                connections[output] = (wire1, wire2, i)


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


x_num_bits = sum([1 for wire in wires if wire[0] == "x"])
y_num_bits = sum([1 for wire in wires if wire[0] == "y"])

first_wrong_bit = z_num_bits
last_change_idx = 0

while True:
    x = random.randint(0, 1 << (x_num_bits - 1))
    y = random.randint(0, 1 << (y_num_bits - 1))

    x_bin = format(x, f"0{x_num_bits}b")
    for i in range(x_num_bits):
        wires[f"x{x_num_bits - i - 1:02}"] = int(x_bin[i])

    y_bin = format(y, f"0{y_num_bits}b")
    for i in range(y_num_bits):
        wires[f"y{y_num_bits - i - 1:02}"] = int(y_bin[i])

    correct_z_bin = format(x + y, f"0{z_num_bits}b")[-z_num_bits:]
    computed_z_bin = "".join(
        [str(get_bit(f"z{z_num_bits - i - 1:02}")) for i in range(z_num_bits)]
    )

    for i in range(z_num_bits):
        idx = z_num_bits - i - 1
        if correct_z_bin[idx] == computed_z_bin[idx]:
            continue
        if i < first_wrong_bit:
            first_wrong_bit = i
            last_change_idx = 0

        break

    last_change_idx += 1
    if last_change_idx > 1000:
        break

print(first_wrong_bit)
