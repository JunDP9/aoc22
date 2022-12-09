from functools import reduce

from utils import parse_input

FILE_PATH = 'input.txt'

parsed_input = parse_input(FILE_PATH)


def solution_part_one(commands):

    for command in commands:
        [direction, steps] = command.split(" ")






# def solution_part_two(parsed_input):


print(solution_part_one(parsed_input))
# print(solution_part_two(parsed_input))
