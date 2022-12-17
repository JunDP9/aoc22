from functools import cmp_to_key
from utils import parse_input

FILE_PATH = 'input.txt'

parsed_input = parse_input(FILE_PATH)


def special_compare(pair_left, pair_right):
    if isinstance(pair_left, int) and isinstance(pair_right, int):
        return pair_left - pair_right
    if isinstance(pair_left, list) and isinstance(pair_right, int):
        temp_right_list = [pair_right]
        return special_compare(pair_left, temp_right_list)
    if isinstance(pair_left, int) and isinstance(pair_right, list):
        temp_left_list = [pair_left]
        return special_compare(temp_left_list, pair_right)
    for ll, rr in zip(pair_left, pair_right):
        compare = special_compare(ll, rr)
        if compare == 0:
            continue
        return compare
    return len(pair_left) - len(pair_right)


def solution_part_one(input_list):
    pairs = get_pairs(input_list)
    correct_indices = []
    for pair_left, pair_right in pairs:
        if special_compare(pair_left, pair_right) < 0:
            correct_indices.append(pairs.index((pair_left, pair_right)) + 1)
    return sum(correct_indices)


def get_pairs(input_list):
    pairs = []
    for idx in range(0, len(input_list), 3):
        if input_list[idx]:
            pairs.append((eval(input_list[idx]), eval(input_list[idx + 1])))
    return pairs


def solution_part_two(input_list):
    packet, packet_two = [[2]], [[6]]
    pairs = [eval(line) for line in input_list if line]
    pairs.append(packet)
    pairs.append(packet_two)
    pairs = sorted(pairs, key=cmp_to_key(special_compare))
    print(pairs)
    return (pairs.index(packet)+1) * (pairs.index(packet_two)+1)


print(solution_part_one(parsed_input))
print(solution_part_two(parsed_input))
