import string

from utils import parse_input

sanitized_list = parse_input('input.txt')


def get_points(unique):
    if unique[0].isupper():
        score = string.ascii_lowercase.index((unique[0]).lower()) + 1
        return score + 26
    else:
        score = string.ascii_lowercase.index(unique[0]) + 1
        return score


def solution_part_one(input):
    total = 0
    for line in input:
        line_length = len(line)
        half_line_length = int(line_length / 2)
        first_part, second_part = set(line[0:half_line_length]), set(line[half_line_length:line_length])
        difference = first_part.difference(second_part)
        unique = first_part.difference(difference)
        total += get_points(list(unique))
    return total


def solution_part_two(input):
    total = 0
    for index in range(0, len(input), 3):
        first, second, third = set(input[index]), set(input[index + 1]), set(input[index + 2])
        common = list(first & second & third)
        total += get_points(common)
    return total


print(solution_part_one(sanitized_list))
print(solution_part_two(sanitized_list))
