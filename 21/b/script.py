from functools import cache

NUM_ROBOT_DIR_KEYPADS = 26
DIR_POS = {"<": (0, 0), "v": (0, 1), ">": (0, 2), "^": (1, 1), "A": (1, 2)}

with open("../input.txt") as file:
    codes = file.read().splitlines()


def get_key_pos(key, is_num_keypad):
    if not is_num_keypad:
        return DIR_POS[key]

    if key == "A":
        return (0, 2)

    num = int(key) - 1
    x = (num // 3) + 1
    y = num % 3 if num >= 0 else 1
    return (x, y)


@cache
def get_mov_seq(key1, key2, is_num_keypad):
    x1, y1 = get_key_pos(key1, is_num_keypad)
    x2, y2 = get_key_pos(key2, is_num_keypad)

    vertical = abs(x2 - x1) * ("^" if x2 > x1 else "v")
    horizontal = abs(y2 - y1) * (">" if y2 > y1 else "<")

    vertical_first = vertical + horizontal + "A"
    horizontal_first = horizontal + vertical + "A"

    # Check if either path goes through the empty gap.
    is_vertical_invalid = (is_num_keypad and y1 == 0 and x2 == 0) or (
        not is_num_keypad and y1 == 0 and x2 == 1
    )
    is_horizontal_invalid = (is_num_keypad and x1 == 0 and y2 == 0) or (
        not is_num_keypad and x1 == 1 and y2 == 0
    )

    if is_vertical_invalid:
        return horizontal_first
    if is_horizontal_invalid:
        return vertical_first

    return horizontal_first if horizontal.startswith("<") else vertical_first


@cache
def get_key_len_after_depth(prev_key, key, depth):
    if depth == 0:
        return 1

    next_seq = get_mov_seq(prev_key, key, depth == NUM_ROBOT_DIR_KEYPADS)
    return get_seq_len_after_depth(next_seq, depth - 1)


def get_seq_len_after_depth(seq, depth):
    prev_key = "A"
    l = 0
    for key in seq:
        l += get_key_len_after_depth(prev_key, key, depth)
        prev_key = key
    return l


ans = 0
for code in codes:
    ans += get_seq_len_after_depth(code, NUM_ROBOT_DIR_KEYPADS) * int(code[:-1])

print(ans)
